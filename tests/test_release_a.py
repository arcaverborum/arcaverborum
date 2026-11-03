"""Schema-A release: identifiers, licence canonicalization, tier filtering."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import pytest
import yaml

from arcaverborum.release_a import (
    build_tier,
    canonical_license,
    load_tiers,
    parse_release_id,
    source_terms,
)

FORM_FIELDS = ["av_id", "Glottocode", "Variety_Name", "concept_id", "concept_label", "Concepticon_ID", "Value",
               "Form", "Segments", "Segments_Source", "Cognacy", "canonical_cognate_id", "Alignment",
               "Morpheme_Index", "Segment_Slice", "Doubt", "Cognate_Detection_Method", "Cognate_Source", "Loan",
               "Comment", "transcription_source", "cognate_source", "source_form_id", "source_language_id",
               "source_parameter_id", "bibtex_key", "quality_score", "tier"]


def test_release_ids():
    assert parse_release_id("A-2026-11-10") == dict(letter="A", date="2026-11-10", same_day=1)
    assert parse_release_id("B-2027-01-31.2")["same_day"] == 2
    for bad in ("a-2026-11-10", "A-2026-13-01", "A-2026-11-10.1", "A20261110", "AB-2026-11-10"):
        with pytest.raises(ValueError):
            parse_release_id(bad)


def test_unknown_licences_fail_closed():
    tiers = load_tiers()
    assert canonical_license("https://creativecommons.org/licenses/by/4.0/", tiers) == "CC-BY-4.0"
    assert canonical_license("https://creativecommons.org/licenses/by/4.0", tiers) == "CC-BY-4.0"
    assert canonical_license("", tiers) == ""
    with pytest.raises(ValueError, match="Unknown licence"):
        canonical_license("All rights reserved", tiers)


def _write(path: Path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _fixture(root: Path):
    agg = root / "output/aggregate"
    rows = [
        ("by-lang", "by_src", "by_src", "water"),
        ("nc-lang", "nc_src", "nc_src", "water"),
        ("mixed", "by_src", "nc_src", "fire"),
        ("undeclared", "none_src", "none_src", ""),
    ]
    forms = []
    for i, (av, ts, cs, concept) in enumerate(rows):
        forms.append({**dict.fromkeys(FORM_FIELDS, ""), "av_id": av, "concept_id": concept, "Value": f"v{i}",
                      "Form": f"f{i}", "Segments_Source": "source", "Cognacy": f"{cs}-1",
                      "transcription_source": ts, "cognate_source": cs, "source_form_id": f"s{i}",
                      "bibtex_key": "key1"})
    _write(agg / "forms.csv", FORM_FIELDS, forms)
    _write(agg / "varieties.csv", ["av_id", "Glottocode", "Name", "Family", "Macroarea", "transcription_source",
                                   "cognate_source", "pinned", "forms_score", "cognates_score", "tier"],
           [dict(av_id=av, Glottocode="", Name=av) for av, *_ in rows])
    _write(agg / "parameters.csv", ["concept_id", "concepticon_id", "label", "pos", "semantic_field", "definition"],
           [dict(concept_id="water", label="water"), dict(concept_id="fire", label="fire")])
    _write(agg / "metadata.csv", ["Dataset", "Title", "Citation", "URL", "License", "Repository_Version"],
           [dict(Dataset="by_src", License="https://creativecommons.org/licenses/by/4.0/"),
            dict(Dataset="nc_src", License="https://creativecommons.org/licenses/by-nc/4.0/"),
            dict(Dataset="none_src", License="")])
    (agg / "sources.bib").write_text("@book{key1, title={T}}\n")
    _write(root / "raw/glottolog/languages.csv", ["ID", "Latitude", "Longitude"], [])
    for av, *_ in rows:
        folder = root / "varieties" / av
        (folder / "custom").mkdir(parents=True)
        (folder / "config.yaml").write_text(yaml.safe_dump(dict(av_id=av)))
        (folder / "custom/forms.csv").write_text("x\n")


@pytest.mark.parametrize("tier,expected", [
    ("full", {"by-lang", "nc-lang", "mixed", "undeclared"}),
    ("redistributable", {"by-lang", "nc-lang", "mixed"}),
    ("by", {"by-lang"}),
])
def test_tiers_filter_rows_and_curation_files(tmp_path, tier, expected):
    _fixture(tmp_path)
    tiers = load_tiers()
    terms = source_terms(tmp_path / "output/aggregate/metadata.csv", tiers)
    out = tmp_path / "out"
    meta = build_tier(tmp_path, out, "A-2026-11-10", tier, tiers["tiers"][tier], terms,
                      git_commit="abc", snapshot_sha256="")
    with (out / "data/forms.csv").open() as handle:
        kept = list(csv.DictReader(handle))
    assert {r["av_id"] for r in kept} == expected
    assert {p.name for p in (out / "curation").iterdir()} == expected
    allowed_licences = set(tiers["tiers"][tier]["allow"]) | ({""} if tier == "full" else set())
    assert {r["License"] for r in kept} <= allowed_licences
    if tier == "by":
        # The mixed construction's cognacy comes from an NC source: excluded entirely.
        assert all(r["cognate_source"] == "by_src" for r in kept)
    assert meta["cldf"]["forms"] == len(kept)
    manifest = json.loads((out / "MANIFEST.json").read_text())
    assert manifest["records"] == len(kept) and manifest["tier"] == tier
    assert "CC BY 4.0" in (out / "LICENSES.md").read_text()

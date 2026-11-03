"""Accepted-inputs snapshot: key closure, deterministic packing, verified unpacking."""

from __future__ import annotations

import csv
import json

import pytest
import yaml

from arcaverborum.snapshot import _filter_csv, enrolled, input_keys, pack, unpack
from arcaverborum.variety import FALLBACK_SOURCE, Variety


def _variety(root, av_id, sources, dormant=False, preserved=None):
    folder = root / av_id
    (folder / "custom").mkdir(parents=True)
    cfg = dict(av_id=av_id, glottocode=av_id[:4] + "1234", sources=sources)
    if dormant:
        cfg["dormant"] = True
    (folder / "config.yaml").write_text(yaml.safe_dump(cfg))
    if preserved:
        with (folder / "custom/preserved_forms.csv").open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["Glottocode", "transcription_source"])
            writer.writeheader()
            writer.writerows(preserved)


def test_input_keys_cover_primary_union_fallback_and_supplements(tmp_path):
    _variety(tmp_path, "abcd", dict(transcription="src", source_glottocodes=[" EXTR1234 "],
                                     source_language_ids=["m1"]),
             preserved=[dict(Glottocode="Supp1234", transcription_source="other")])
    _variety(tmp_path, "efgh", dict(transcription="src2"), dormant=True)
    catalog = {"abcd": Variety("abcd", glottocode="abcd1234"), "efgh": Variety("efgh", glottocode="efgh1234")}
    assert enrolled(tmp_path) == ["abcd"]
    keys = input_keys(enrolled(tmp_path), tmp_path, catalog)
    assert keys == {("abcd1234", "src"), ("extr1234", "src"), ("abcd1234", FALLBACK_SOURCE),
                    ("supp1234", "other")}


def test_filter_csv_keeps_header_and_selected_rows(tmp_path):
    src = tmp_path / "in.csv"
    src.write_text("Glottocode,Dataset,ID\nabcd1234,src,1\nzzzz1234,src,2\n")
    n = _filter_csv(src, tmp_path / "out/f.csv", lambda row, ix: row[ix["ID"]] == "1")
    assert n == 1 and (tmp_path / "out/f.csv").read_text() == "Glottocode,Dataset,ID\nabcd1234,src,1\n"


def test_pack_is_deterministic_and_unpack_verifies(tmp_path):
    tree = tmp_path / "tree"
    (tree / "intake").mkdir(parents=True)
    (tree / "intake/a.csv").write_text("x\n")
    from arcaverborum.snapshot import _sha

    (tree / "SNAPSHOT.json").write_text(json.dumps(dict(files=[dict(path="intake/a.csv",
                                                                     sha256=_sha(tree / "intake/a.csv"))])))
    first = pack(tree, tmp_path / "one.tar.gz")
    second = pack(tree, tmp_path / "two.tar.gz")
    assert first == second
    with pytest.raises(FileExistsError):
        pack(tree, tmp_path / "one.tar.gz")
    target = tmp_path / "unpacked"
    target.mkdir()
    assert unpack(tmp_path / "one.tar.gz", target)["files"][0]["path"] == "intake/a.csv"
    (tree / "intake/a.csv").write_text("changed\n")
    pack(tree, tmp_path / "bad.tar.gz")
    with pytest.raises(ValueError, match="corrupted"):
        unpack(tmp_path / "bad.tar.gz", tmp_path / "unpacked2")


def test_guarded_cognacy_sources_are_snapshot_inputs(tmp_path):
    from arcaverborum.snapshot import guarded_cognacy_files

    data = tmp_path / "src/arcaverborum/data"
    data.mkdir(parents=True)
    (data / "cognacy_scope_policies.csv").write_text(
        "dataset,policy,forms_sha256,cognates_sha256,evidence,emission_guard\n"
        "kept,structured_only,a,b,e,true\nignored,structured_only,a,b,e,\n")
    assert guarded_cognacy_files(tmp_path) == ["raw/lexibank/kept/cldf/forms.csv",
                                               "raw/lexibank/kept/cldf/cognates.csv"]

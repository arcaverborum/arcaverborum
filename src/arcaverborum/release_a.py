"""Schema-A release builder: one release identifier, three licence tiers.

``build_release_a(root, "A-2026-11-10")`` reads the current aggregate (which
must be complete; see :func:`arcaverborum.aggregate.check_build_complete`)
and writes, for each tier in ``data/release_tiers.json``::

    output/release/<id>/arcaverborum-<id>-<tier>/
        data/forms.csv          accepted records + License, terms_status
        data/varieties.csv      accepted constructions (with coordinates)
        data/concepts.csv       Arca concept catalog entries in use
        data/sources.csv        per-source terms, citation, record counts
        data/sources.bib
        data/recordings.csv     recording metadata (when any)
        cldf/                   CLDF Wordlist export of the same rows
        curation/<av_id>/...    config, custom files and recipes of
                                constructions whose every source is in the tier
        wordnet/                Arca's typed WordNet links (sidecar)
        LICENSES.md, README.md, CITATION.cff, MANIFEST.json

A row belongs to a tier only if the terms of *both* its transcription source
and its cognate source are allowed there. Licences are canonicalized through
the tier table; an unknown licence string fails the build.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

from arcaverborum.release import _PROP, CLDF

csv.field_size_limit(sys.maxsize)

PACKAGE_DATA = Path(__file__).parent / "data"
RELEASE_ID = re.compile(r"^(?P<letter>[A-Z])-(?P<date>\d{4}-\d{2}-\d{2})(?:\.(?P<n>[2-9]|[1-9]\d+))?$")
MISSING = "missing_declaration"
ORG_URL = "https://github.com/arcaverborum/arcaverborum"
SITE_URL = "https://arcaverborum.org"


def parse_release_id(release_id: str) -> dict:
    m = RELEASE_ID.match(release_id)
    if not m:
        raise ValueError(f"Release identifier must look like A-2026-11-10 or A-2026-11-10.2: {release_id!r}")
    from datetime import date

    date.fromisoformat(m["date"])
    return dict(letter=m["letter"], date=m["date"], same_day=int(m["n"] or 1))


def load_tiers(path: Path = PACKAGE_DATA / "release_tiers.json") -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def canonical_license(raw: str, tiers: dict) -> str:
    raw = (raw or "").strip()
    if not raw:
        return ""
    for spdx, spellings in tiers["licenses"].items():
        if raw in spellings or raw.rstrip("/") in (s.rstrip("/") for s in spellings):
            return spdx
    raise ValueError(f"Unknown licence declaration {raw!r}; add it to release_tiers.json after review")


def source_terms(metadata_csv: Path, tiers: dict) -> dict[str, dict]:
    terms = {}
    with Path(metadata_csv).open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            spdx = canonical_license(row.get("License", ""), tiers)
            terms[row["Dataset"]] = dict(row, spdx=spdx, terms_status="declared" if spdx else MISSING)
    return terms


def allowed(source: str, terms: dict, tier: dict) -> bool:
    t = terms.get(source)
    if t is None:
        raise ValueError(f"Source {source!r} has no metadata entry")
    if not t["spdx"]:
        return bool(tier.get("allow_missing_declaration"))
    return t["spdx"] in tier["allow"]


def _sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def _read(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write(path: Path, fields: list[str], rows) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
            n += 1
    return n


# ---------------------------------------------------------------- CLDF export

_CLDF_FORMS = ["ID", "Language_ID", "Parameter_ID", "Value", "Form", "Segments", "Comment", "Source",
               "Loan", "License", "terms_status", "transcription_source", "cognate_source",
               "source_form_id", "source_parameter_id", "Segments_Source", "quality_score"]
_CLDF_COGNATES = ["ID", "Form_ID", "Cognateset_ID", "Cognate_Source", "Cognate_Detection_Method",
                  "Alignment", "Segment_Slice", "Morpheme_Index", "Doubt"]
_CLDF_LANGUAGES = ["ID", "Name", "Glottocode", "Family", "Macroarea", "Latitude", "Longitude", "tier"]
_CLDF_PARAMETERS = ["ID", "Name", "Concepticon_ID", "pos", "semantic_field", "Description"]
UNMAPPED = "unmapped"


def _cols(names):
    return [dict(name=n, **({"propertyUrl": _PROP[n]} if n in _PROP else {})) for n in names]


def _cldf_metadata(release_id: str, tier: str) -> dict:
    fk = lambda col, res: {"columnReference": [col], "reference": {"resource": res, "columnReference": ["ID"]}}  # noqa: E731
    return {
        "@context": ["http://www.w3.org/ns/csvw", {"@language": "en"}],
        "dc:conformsTo": CLDF + "Wordlist",
        "dc:title": f"Arca Verborum {release_id} ({tier})",
        "dcat:version": release_id,
        "dc:license": "Per-row; see the License and terms_status columns of forms.csv and ../LICENSES.md",
        "dc:source": "sources.bib",
        "tables": [
            {"url": "forms.csv", "dc:conformsTo": CLDF + "FormTable",
             "tableSchema": {"columns": _cols(_CLDF_FORMS), "primaryKey": ["ID"],
                             "foreignKeys": [fk("Language_ID", "languages.csv"),
                                             fk("Parameter_ID", "parameters.csv")]}},
            {"url": "languages.csv", "dc:conformsTo": CLDF + "LanguageTable",
             "tableSchema": {"columns": _cols(_CLDF_LANGUAGES), "primaryKey": ["ID"]}},
            {"url": "parameters.csv", "dc:conformsTo": CLDF + "ParameterTable",
             "tableSchema": {"columns": _cols(_CLDF_PARAMETERS), "primaryKey": ["ID"]}},
            {"url": "cognates.csv", "dc:conformsTo": CLDF + "CognateTable",
             "tableSchema": {"columns": _cols(_CLDF_COGNATES), "primaryKey": ["ID"],
                             "foreignKeys": [fk("Form_ID", "forms.csv")]}},
        ],
    }


def validate_cldf(cldf_dir: Path) -> dict:
    """Referential integrity of the CLDF export (no pycldf dependency)."""
    langs = {r["ID"] for r in _read(cldf_dir / "languages.csv")}
    params = {r["ID"] for r in _read(cldf_dir / "parameters.csv")}
    forms, problems = set(), []
    for r in _read(cldf_dir / "forms.csv"):
        if r["ID"] in forms:
            problems.append("duplicate form " + r["ID"])
        forms.add(r["ID"])
        if r["Language_ID"] not in langs:
            problems.append("form language " + r["ID"])
        if r["Parameter_ID"] not in params:
            problems.append("form parameter " + r["ID"])
        if not r["Form"]:
            problems.append("empty form " + r["ID"])
    cognates = 0
    for r in _read(cldf_dir / "cognates.csv"):
        cognates += 1
        if r["Form_ID"] not in forms:
            problems.append("cognate form " + r["ID"])
    if problems:
        raise ValueError(f"CLDF export invalid ({len(problems)}): " + "; ".join(problems[:10]))
    return dict(forms=len(forms), languages=len(langs), parameters=len(params), cognates=cognates)


# ---------------------------------------------------------------- builder

def _glottolog_coords(path: Path) -> dict[str, tuple[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    return {r["ID"]: (r.get("Latitude", ""), r.get("Longitude", "")) for r in _read(path)}


def _curation_files(root: Path, av_id: str) -> list[Path]:
    folder = root / "varieties" / av_id
    files = [folder / "config.yaml"]
    files += [p for p in sorted(folder.rglob("*")) if p.is_file() and "generated" not in p.relative_to(folder).parts
              and p != folder / "config.yaml"]
    return [p for p in files if p.exists()]


def build_tier(root: Path, out: Path, release_id: str, tier_name: str, tier: dict, terms: dict,
               *, git_commit: str, snapshot_sha256: str) -> dict:
    agg = root / "output" / "aggregate"
    out.mkdir(parents=True, exist_ok=False)
    data, cldf = out / "data", out / "cldf"
    data.mkdir()
    cldf.mkdir()

    forms_fields = None
    counts, per_source, segments = Counter(), Counter(), Counter()
    excluded_sources: set[str] = set()
    variety_sources: dict[str, set[str]] = defaultdict(set)
    concepts_used: set[str] = set()
    bib_keys: set[str] = set()
    n_forms = n_cognates = 0
    with (agg / "forms.csv").open(encoding="utf-8", newline="") as fin, \
            (data / "forms.csv").open("w", encoding="utf-8", newline="") as f_native, \
            (cldf / "forms.csv").open("w", encoding="utf-8", newline="") as f_cldf, \
            (cldf / "cognates.csv").open("w", encoding="utf-8", newline="") as f_cog:
        reader = csv.DictReader(fin)
        forms_fields = list(reader.fieldnames) + ["License", "terms_status"]
        w_native = csv.DictWriter(f_native, fieldnames=forms_fields, lineterminator="\n")
        w_cldf = csv.DictWriter(f_cldf, fieldnames=_CLDF_FORMS, lineterminator="\n", extrasaction="ignore")
        w_cog = csv.DictWriter(f_cog, fieldnames=_CLDF_COGNATES, lineterminator="\n")
        for w in (w_native, w_cldf, w_cog):
            w.writeheader()
        sequence: Counter = Counter()
        for row in reader:
            ts = row["transcription_source"]
            cs = row.get("cognate_source") or ts
            variety_sources[row["av_id"]].update({ts, cs})
            if not (allowed(ts, terms, tier) and allowed(cs, terms, tier)):
                excluded_sources.update(s for s in (ts, cs) if not allowed(s, terms, tier))
                continue
            t = terms[ts]
            row["License"] = t["spdx"]
            row["terms_status"] = t["terms_status"]
            w_native.writerow(row)
            n_forms += 1
            counts[row["av_id"]] += 1
            per_source[ts] += 1
            segments[row["Segments_Source"]] += 1
            for key in (row.get("bibtex_key") or "").split(";"):
                if key.strip():
                    bib_keys.add(key.split("[", 1)[0].strip())
            sequence[row["av_id"]] += 1
            form_id = f"{row['av_id']}-{sequence[row['av_id']]:06d}"
            concept = row.get("concept_id") or UNMAPPED
            concepts_used.add(concept)
            w_cldf.writerow(dict(row, ID=form_id, Language_ID=row["av_id"], Parameter_ID=concept,
                                 Source=row.get("bibtex_key", ""), Form=row.get("Form") or row.get("Value", "")))
            cognacy = (row.get("canonical_cognate_id") or row.get("Cognacy") or "").strip()
            for i, cset in enumerate(sorted({c.strip() for c in cognacy.split(";") if c.strip()})):
                n_cognates += 1
                w_cog.writerow(dict(ID=f"{form_id}-c{i + 1}", Form_ID=form_id, Cognateset_ID=cset,
                                    Cognate_Source=row.get("Cognate_Source", ""),
                                    Cognate_Detection_Method=row.get("Cognate_Detection_Method", ""),
                                    Alignment=row.get("Alignment", ""), Segment_Slice=row.get("Segment_Slice", ""),
                                    Morpheme_Index=row.get("Morpheme_Index", ""), Doubt=row.get("Doubt", "")))

    # Recordings follow the same source rule.
    recordings = []
    for path in sorted((root / "varieties").glob("*/generated/recordings.csv")):
        for r in _read(path):
            if allowed(r["source"], terms, tier):
                recordings.append(r)
                counts.setdefault(r["av_id"], 0)
    recording_by_av = Counter(r["av_id"] for r in recordings)
    accepted = sorted(av for av in counts if counts[av] or recording_by_av[av])
    if recordings:
        _write(data / "recordings.csv", list(recordings[0]), recordings)

    coords = _glottolog_coords(root / "raw" / "glottolog" / "languages.csv")
    varieties = [r for r in _read(agg / "varieties.csv") if r["av_id"] in set(accepted)]
    for r in varieties:
        r["Latitude"], r["Longitude"] = coords.get(r.get("Glottocode", ""), ("", ""))
        r["records"] = counts[r["av_id"]]
        r["recordings"] = recording_by_av[r["av_id"]]
    v_fields = list(_read(agg / "varieties.csv")[0]) + ["Latitude", "Longitude", "records", "recordings"]
    _write(data / "varieties.csv", v_fields, varieties)
    _write(cldf / "languages.csv", _CLDF_LANGUAGES,
           [dict(r, ID=r["av_id"]) for r in varieties])

    concepts = [r for r in _read(agg / "parameters.csv") if r["concept_id"] in concepts_used]
    _write(data / "concepts.csv", list(_read(agg / "parameters.csv")[0]), concepts)
    cldf_params = [dict(ID=r["concept_id"], Name=r["label"], Concepticon_ID=r.get("concepticon_id", ""),
                        pos=r.get("pos", ""), semantic_field=r.get("semantic_field", ""),
                        Description=r.get("definition", "")) for r in concepts]
    if UNMAPPED in concepts_used:
        cldf_params.append(dict(ID=UNMAPPED, Name="(source meaning not mapped to an Arca concept)",
                                Description="Records whose source meaning is not mapped; see source_parameter_id."))
    _write(cldf / "parameters.csv", _CLDF_PARAMETERS, cldf_params)

    sources = []
    for name in sorted(per_source):
        t = terms[name]
        sources.append(dict(source=name, records=per_source[name], license=t["spdx"], terms_status=t["terms_status"],
                            title=t.get("Title", ""), citation=t.get("Citation", ""), url=t.get("URL", ""),
                            version=t.get("Repository_Version", "")))
    _write(data / "sources.csv", ["source", "records", "license", "terms_status", "title", "citation", "url",
                                  "version"], sources)
    bib_text = (agg / "sources.bib").read_text(encoding="utf-8")
    from arcaverborum.aggregate import _bibtex_key, _split_bibtex

    entries = [e for e in _split_bibtex(bib_text) if _bibtex_key(e) in bib_keys]
    for target in (data / "sources.bib", cldf / "sources.bib"):
        target.write_text("\n\n".join(entries) + ("\n" if entries else ""), encoding="utf-8")
    (cldf / "cldf-metadata.json").write_text(json.dumps(_cldf_metadata(release_id, tier_name), indent=2,
                                                        ensure_ascii=False) + "\n", encoding="utf-8")
    cldf_stats = validate_cldf(cldf)

    # Curation files only where every source of the construction is in the tier.
    curated = []
    for av in accepted:
        if all(allowed(s, terms, tier) for s in variety_sources.get(av, set())):
            for path in _curation_files(root, av):
                target = out / "curation" / path.relative_to(root / "varieties")
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, target)
            curated.append(av)

    wordnet_dir = PACKAGE_DATA / "wordnet"
    for name in ("links.csv", "coverage.csv", "sources.json", "summary.json"):
        if (wordnet_dir / name).exists():
            (out / "wordnet").mkdir(exist_ok=True)
            shutil.copyfile(wordnet_dir / name, out / "wordnet" / name)

    meta = dict(release_id=release_id, tier=tier_name, tier_description=tier["description"],
                records=n_forms, constructions=len(accepted),
                lexical_constructions=sum(1 for av in accepted if counts[av]),
                recording_only_constructions=sum(1 for av in accepted if not counts[av]),
                recordings=len(recordings), concepts=len(concepts), cognate_judgements=n_cognates,
                sources=len(sources), curated_constructions=len(curated),
                excluded_sources=sorted(excluded_sources), segments_source=dict(segments),
                sources_by_license=dict(Counter(s["license"] or MISSING for s in sources)),
                records_by_license=_records_by_license(sources),
                cldf=cldf_stats, git_commit=git_commit, accepted_inputs_snapshot_sha256=snapshot_sha256)
    (out / "LICENSES.md").write_text(_licenses_md(meta, sources), encoding="utf-8")
    (out / "README.md").write_text(_readme(meta), encoding="utf-8")
    (out / "CITATION.cff").write_text(_citation(meta), encoding="utf-8")
    files = [dict(path=p.relative_to(out).as_posix(), bytes=p.stat().st_size, sha256=_sha(p))
             for p in sorted(out.rglob("*")) if p.is_file()]
    (out / "MANIFEST.json").write_text(json.dumps(dict(meta, files=files), indent=1, ensure_ascii=False) + "\n",
                                       encoding="utf-8")
    return meta


def _records_by_license(sources: list[dict]) -> dict[str, int]:
    totals: Counter = Counter()
    for s in sources:
        totals[s["license"] or MISSING] += s["records"]
    return dict(totals)


def _licenses_md(meta: dict, sources: list[dict]) -> str:
    lines = [
        f"# Licences — Arca Verborum {meta['release_id']} ({meta['tier']})", "",
        "There is no single licence for this collection. Terms are per source and per row.", "",
        "- **Source records** keep their source's terms: see the `License` and `terms_status` columns of",
        "  `data/forms.csv` and the table below. Keep the attribution, citations and per-entry URLs.",
        "- **Arca's own work** — identifiers, the variety and concept catalogs, concept/WordNet links,",
        "  scores and other code-generated products — is licensed **CC BY 4.0**.",
        "- **Adaptations of ShareAlike records** (normalizations, segmentations, corrections) are",
        "  distributed under the same terms as their source (CC BY-SA 4.0 or CC BY-NC-SA 4.0).",
        "- WordNet sidecars keep their Open English WordNet (CC BY 4.0), CILI and Princeton WordNet notices",
        "  (see `wordnet/sources.json`).",
        "- Code: MIT, in the repository " + ORG_URL + ".",
        "- `terms_status = missing_declaration` marks sources whose redistribution terms are not declared;",
        "  they are included in good faith pending clarification with the rights holders.", "",
        "| Source | Records | Licence | Terms status |", "| --- | ---: | --- | --- |",
    ]
    lines += [f"| {s['source']} | {s['records']:,} | {s['license'] or '—'} | {s['terms_status']} |" for s in sources]
    return "\n".join(lines) + "\n"


def _readme(meta: dict) -> str:
    return "\n".join([
        f"# Arca Verborum {meta['release_id']} — {meta['tier']}", "",
        meta["tier_description"], "",
        f"- {meta['records']:,} lexical records in {meta['lexical_constructions']:,} constructions"
        f" ({meta['recording_only_constructions']} recording-only; {meta['recordings']} recordings)",
        f"- {meta['concepts']:,} concepts; {meta['cognate_judgements']:,} cognate judgements; "
        f"{meta['sources']} sources", "",
        "Schema letter A: tables are read by header; added columns keep the letter, breaking changes",
        "bump it. `data/` holds the native tables, `cldf/` a CLDF Wordlist export of the same rows,",
        "`curation/` the reviewed configs and custom files of constructions fully inside this tier.",
        "Rebuild from the repository with the accepted-inputs snapshot of the same release.", "",
        f"Repository: {ORG_URL} (commit {meta['git_commit'] or 'unknown'}). Explorer: {SITE_URL}.",
        "The baseline was built by the maintainer with extensive AI assistance; every change is owned",
        "by its human author, and model reviews are not counted as expert review.", "",
        "See LICENSES.md before reuse.", "",
    ])


def _citation(meta: dict) -> str:
    return "\n".join([
        "cff-version: 1.2.0",
        'message: "Cite this release together with the original sources of the records you use."',
        f'title: "Arca Verborum {meta["release_id"]} ({meta["tier"]})"',
        "type: dataset",
        "authors:",
        "  - family-names: Tresoldi",
        "    given-names: Tiago",
        '    orcid: "https://orcid.org/0000-0002-2863-1467"',
        f"version: \"{meta['release_id']}\"",
        f"date-released: \"{parse_release_id(meta['release_id'])['date']}\"",
        f'url: "{SITE_URL}"',
        f'repository-code: "{ORG_URL}"',
        "",
    ])


def build_release_a(root: Path, release_id: str, *, tiers: list[str] | None = None, git_commit: str = "",
                    snapshot_sha256: str = "", out_root: Path | None = None) -> dict:
    parse_release_id(release_id)
    os.environ["ARCA_BUILD_DATE"] = parse_release_id(release_id)["date"]
    table = load_tiers()
    names = tiers or list(table["tiers"])
    terms = source_terms(Path(root) / "output" / "aggregate" / "metadata.csv", table)
    out_root = Path(out_root or Path(root) / "output" / "release" / release_id)
    results = {}
    for name in names:
        results[name] = build_tier(Path(root), out_root / f"arcaverborum-{release_id}-{name}", release_id, name,
                                   table["tiers"][name], terms, git_commit=git_commit,
                                   snapshot_sha256=snapshot_sha256)
    return results

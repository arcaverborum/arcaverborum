"""Source extensions: new intake sources contributed through a pull request.

The accepted-inputs snapshot only changes when a release is cut, so a pull
request cannot add rows to it. A new source is committed instead as a small,
git-tracked folder::

    extensions/<dataset>/
        README.md         provenance: where the data come from, who prepared it, how
        metadata.csv      one row: Dataset, Title, Citation, URL, License, ...
        languages.csv     ID, Name, Glottocode (+ optional intake language columns)
        parameters.csv    ID, Name (+ optional Concepticon_ID, Concepticon_Gloss)
        forms.csv         ID, Language_ID, Parameter_ID, Value and/or Form
                          (+ optional Segments, Comment, Source, Cognacy, ...)
        sources.bib       BibTeX; every key starts with ``<dataset>_``

:func:`materialize` writes them, in the intake schema, to ``intake/extensions/``
(ignored by git, like all intake), where the build reads them next to the
Lexibank and Wiktionary intake. Extensions stay in git: they are build inputs
in every workspace, the maintainer's included, and a clean checkout plus the
release snapshot still re-derives everything.

:func:`validate` fails closed: unknown columns, dangling references, duplicate
IDs, a dataset name already used by another intake source, an undeclared or
unreviewed licence, or a Glottocode missing from the frozen Glottolog table.
"""

from __future__ import annotations

import csv
import io
import re
import shutil
from pathlib import Path

EXT_DIR = "extensions"
OUT_DIR = "intake/extensions"
OTHER_INTAKE = ("lexibank", "wiktionary")

FORMS_COLUMNS = ["ID", "Dataset", "Local_ID", "Language_ID", "Parameter_ID", "Value", "Form", "Segments",
                 "Comment", "Source", "Loan", "Graphemes", "Profile", "Cognacy", "Doubt",
                 "Cognate_Detection_Method", "Cognate_Source", "Alignment", "Morpheme_Index", "Segment_Slice",
                 "Glottocode", "Glottolog_Name", "Concepticon_Gloss"]
LANGUAGE_COLUMNS = ["ID", "Dataset", "Name", "Glottocode", "Glottolog_Name", "ISO639P3code", "Macroarea",
                    "Latitude", "Longitude", "Family", "Location", "Remark"]
PARAMETER_COLUMNS = ["ID", "Dataset", "Name", "Concepticon_ID", "Concepticon_Gloss"]
METADATA_COLUMNS = ["Dataset", "Title", "Citation", "URL", "License", "CLDF_Module", "Repository_Version",
                    "Python_Version", "Form_Count", "Language_Count", "Parameter_Count", "Has_Cognates"]

TABLES = {  # file in extensions/<dataset>/ → (intake file, columns, required columns)
    "forms.csv": ("forms.csv", FORMS_COLUMNS, ["ID", "Language_ID", "Parameter_ID"]),
    "languages.csv": ("languages.csv", LANGUAGE_COLUMNS, ["ID", "Name", "Glottocode"]),
    "parameters.csv": ("parameters_raw.csv", PARAMETER_COLUMNS, ["ID", "Name"]),
    "metadata.csv": ("metadata.csv", METADATA_COLUMNS, ["Dataset", "Title", "Citation", "License"]),
}

NAME = re.compile(r"^[a-z][a-z0-9_]{2,63}$")
GLOTTOCODE = re.compile(r"^[a-z0-9]{4}[0-9]{4}$")
BIBKEY = re.compile(r"^@\w+\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)


def datasets(root: Path) -> list[str]:
    base = Path(root) / EXT_DIR
    return sorted(p.name for p in base.iterdir() if p.is_dir()) if base.is_dir() else []


def _read(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def _source_keys(value: str) -> list[str]:
    return [k.split("[", 1)[0].strip() for k in (value or "").split(";") if k.strip()]


def _reference_tables(root: Path) -> dict:
    """Glottolog codes/names, Concepticon IDs/glosses and datasets of other intake sources, when present."""
    root = Path(root)
    ref: dict = {"glottolog": {}, "concepticon": {}, "datasets": set()}
    glottolog = root / "raw/glottolog/languages.csv"
    if glottolog.exists():
        _, rows = _read(glottolog)
        ref["glottolog"] = {r["Glottocode"]: r.get("Name", "") for r in rows if r.get("Glottocode")}
    concepticon = root / "raw/concepticon/concepticon.tsv"
    if concepticon.exists():
        with concepticon.open(encoding="utf-8", newline="") as handle:
            ref["concepticon"] = {r["ID"]: r.get("GLOSS", "") for r in csv.DictReader(handle, delimiter="\t")}
    for source in OTHER_INTAKE:
        meta = root / "intake" / source / "metadata.csv"
        if meta.exists():
            ref["datasets"] |= {r["Dataset"] for r in _read(meta)[1]}
    return ref


def validate(root: Path) -> list[str]:
    """Problems with the committed extensions; empty when all are acceptable."""
    from arcaverborum.release_a import canonical_license, load_tiers

    root = Path(root)
    ref = _reference_tables(root)
    tiers = load_tiers()
    problems: list[str] = []
    for name in datasets(root):
        folder = root / EXT_DIR / name

        def bad(message: str, name=name) -> None:
            problems.append(f"extensions/{name}: {message}")

        if not NAME.match(name):
            bad("folder name must be a lower-case dataset identifier (a-z, 0-9, _; 3-64 characters)")
        if name in ref["datasets"]:
            bad("dataset name is already used by another intake source")
        missing = [f for f in [*TABLES, "sources.bib", "README.md"] if not (folder / f).is_file()]
        if missing:
            bad("missing " + ", ".join(missing))
            continue
        tables = {}
        for filename, (_, columns, required) in TABLES.items():
            header, rows = _read(folder / filename)
            unknown = [c for c in header if c not in columns]
            absent = [c for c in required if c not in header]
            if unknown:
                bad(f"{filename}: unknown columns {unknown}")
            if absent:
                bad(f"{filename}: missing columns {absent}")
            for row in rows:
                if row.get("Dataset", name) not in ("", name):
                    bad(f"{filename}: Dataset must be {name!r} or empty")
                    break
            if "ID" in header:
                ids = [r["ID"] for r in rows]
                if any(not i or i != i.strip() for i in ids):
                    bad(f"{filename}: empty or padded ID")
                if len(set(ids)) != len(ids):
                    bad(f"{filename}: duplicate IDs")
            tables[filename] = rows
        meta = tables["metadata.csv"]
        if len(meta) != 1:
            bad("metadata.csv must have exactly one row")
        else:
            try:
                if not canonical_license(meta[0].get("License", ""), tiers):
                    bad("metadata.csv: License is required; undeclared terms cannot be contributed")
            except ValueError as exc:
                bad(f"metadata.csv: {exc}")
            if not (meta[0].get("Title", "").strip() and meta[0].get("Citation", "").strip()):
                bad("metadata.csv: Title and Citation are required")
        languages = {r.get("ID"): r for r in tables["languages.csv"]}
        for row in tables["languages.csv"]:
            code = (row.get("Glottocode") or "").strip()
            if not GLOTTOCODE.match(code):
                bad(f"languages.csv: {row.get('ID')!r} has no valid Glottocode")
            elif ref["glottolog"] and code not in ref["glottolog"]:
                bad(f"languages.csv: Glottocode {code} is not in the frozen Glottolog table")
        parameters = {r.get("ID") for r in tables["parameters.csv"]}
        for row in tables["parameters.csv"]:
            cid = (row.get("Concepticon_ID") or "").strip()
            if cid and ref["concepticon"] and cid not in ref["concepticon"]:
                bad(f"parameters.csv: Concepticon_ID {cid} is not in the frozen Concepticon table")
        bib = (folder / "sources.bib").read_text(encoding="utf-8")
        keys = BIBKEY.findall(bib)
        if len(set(keys)) != len(keys):
            bad("sources.bib: duplicate keys")
        if any(not k.startswith(name + "_") for k in keys):
            bad(f"sources.bib: every key must start with {name + '_'!r}")
        dangling = set()
        for row in tables["forms.csv"]:
            if row.get("Language_ID") not in languages:
                dangling.add(f"Language_ID {row.get('Language_ID')!r}")
            if row.get("Parameter_ID") not in parameters:
                dangling.add(f"Parameter_ID {row.get('Parameter_ID')!r}")
            if not ((row.get("Value") or "").strip() or (row.get("Form") or "").strip()):
                dangling.add(f"form {row.get('ID')!r} has neither Value nor Form")
            for key in _source_keys(row.get("Source", "")):
                if key not in keys:
                    dangling.add(f"Source {key!r} not in sources.bib")
        for item in sorted(dangling)[:20]:
            bad(f"forms.csv: {item}")
        if not tables["forms.csv"]:
            bad("forms.csv has no rows")
    return problems


def _csv_text(columns: list[str], rows: list[dict]) -> str:
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=columns, lineterminator="\n", extrasaction="raise")
    writer.writeheader()
    writer.writerows({c: row.get(c, "") or "" for c in columns} for row in rows)
    return out.getvalue()


def _write_if_changed(path: Path, text: str) -> None:
    """Keep the file (and its mtime) when the content is unchanged, so the intake DB stays current."""
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def materialize(root: Path) -> Path | None:
    """Write the committed extensions to ``intake/extensions/``; remove it when there are none.

    Validates first and raises ``ValueError`` on any problem. Returns the
    intake directory, or ``None`` when no extension is committed.
    """
    root = Path(root)
    out = root / OUT_DIR
    names = datasets(root)
    if not names:
        if out.exists():
            shutil.rmtree(out)
        return None
    problems = validate(root)
    if problems:
        raise ValueError("Invalid source extensions:\n  " + "\n  ".join(problems))
    ref = _reference_tables(root)
    merged: dict[str, list[dict]] = {f: [] for f in TABLES}
    bib = []
    for name in names:
        folder = root / EXT_DIR / name
        tables = {f: _read(folder / f)[1] for f in TABLES}
        languages = {r["ID"]: r for r in tables["languages.csv"]}
        concept_gloss = {r["ID"]: (r.get("Concepticon_Gloss") or ref["concepticon"].get(
            (r.get("Concepticon_ID") or "").strip(), "")) for r in tables["parameters.csv"]}
        for r in tables["languages.csv"]:
            code = r["Glottocode"].strip()
            glottolog_name = r.get("Glottolog_Name") or ref["glottolog"].get(code, "")
            merged["languages.csv"].append(dict(r, Dataset=name, Glottocode=code, Glottolog_Name=glottolog_name))
        for r in tables["parameters.csv"]:
            merged["parameters.csv"].append(dict(r, Dataset=name, Concepticon_Gloss=concept_gloss[r["ID"]]))
        for r in tables["forms.csv"]:
            lang = languages[r["Language_ID"]]
            code = lang["Glottocode"].strip()
            merged["forms.csv"].append(dict(
                r, Dataset=name, Glottocode=code,
                Glottolog_Name=lang.get("Glottolog_Name") or ref["glottolog"].get(code, ""),
                Concepticon_Gloss=concept_gloss[r["Parameter_ID"]]))
        meta = dict(tables["metadata.csv"][0], Dataset=name, Form_Count=str(len(tables["forms.csv"])),
                    Language_Count=str(len(tables["languages.csv"])),
                    Parameter_Count=str(len(tables["parameters.csv"])),
                    Has_Cognates=str(any((r.get("Cognacy") or "").strip() for r in tables["forms.csv"])))
        merged["metadata.csv"].append(meta)
        bib.append((folder / "sources.bib").read_text(encoding="utf-8").strip())
    for filename, (target, columns, _) in TABLES.items():
        _write_if_changed(out / target, _csv_text(columns, merged[filename]))
    _write_if_changed(out / "sources.bib", "\n\n".join(b for b in bib if b) + "\n")
    return out

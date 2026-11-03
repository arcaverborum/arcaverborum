"""Accepted-inputs snapshot: everything `update`, `aggregate` and the site
builders read, and nothing else.

A snapshot is a directory (and a deterministic ``.tar.gz``) laid out like the
paths the build reads, so unpacking it at the root of a fresh checkout is a
complete build workspace::

    intake/lexibank/{forms,languages,parameters_raw,metadata}.csv, sources.bib
    intake/wiktionary/{forms,languages,parameters_raw,metadata,pronunciations}.csv
    raw/glottolog/languages.csv
    raw/concepticon/concepticon.tsv
    raw/lexibank/<dataset>/cldf/{forms,cognates}.csv   (guarded cognacy scope)
    SNAPSHOT.json

Form rows are selected by the exact ``(glottocode, dataset)`` keys that
:func:`input_keys` derives from the variety configs and custom files: the same
function `update_many` uses to decide what a build may read. Lexibank
``parameters_raw`` is reduced to the parameters of those rows. Language,
metadata and bibliography tables are kept whole (they are small and feed the
catalog). The Wiktionary pronunciation ledger is not a build input; it is
kept, reduced to accepted rows, as per-entry provenance.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
import shutil
import sys
import tarfile
from pathlib import Path

import yaml

SNAPSHOT_SCHEMA = 1
csv.field_size_limit(sys.maxsize)

WHOLE_FILES = [
    "intake/lexibank/languages.csv",
    "intake/lexibank/metadata.csv",
    "intake/lexibank/sources.bib",
    "intake/wiktionary/languages.csv",
    "intake/wiktionary/metadata.csv",
    "intake/wiktionary/sources.bib",
    "intake/wiktionary/parameters_raw.csv",
    "raw/glottolog/languages.csv",
    "raw/concepticon/concepticon.tsv",
]
FORMS_FILES = ["intake/lexibank/forms.csv", "intake/wiktionary/forms.csv"]


def guarded_cognacy_files(root: Path) -> list[str]:
    """Raw CLDF tables that the build re-reads, hash-pinned, to repair cognacy scope.

    See ``sources/cognacy_scope.py``: datasets whose policy has
    ``emission_guard = true`` are read from ``raw/lexibank/<dataset>/cldf/``.
    """
    path = Path(root) / "src/arcaverborum/data/cognacy_scope_policies.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        guarded = sorted(r["dataset"] for r in csv.DictReader(handle) if r.get("emission_guard") == "true")
    return [f"raw/lexibank/{d}/cldf/{t}" for d in guarded for t in ("forms.csv", "cognates.csv")]


def input_keys(av_ids, varieties_root: Path, catalog: dict) -> set[tuple[str, str]]:
    """``(glottocode_lc, dataset)`` slices a build of ``av_ids`` may read.

    The primary slice, any reviewed source-code union, the GLED fallback
    slice, and every supplement key declared in ``custom/``.
    """
    from arcaverborum.supplements import input_keys as supplemental_keys
    from arcaverborum.variety import FALLBACK_SOURCE, Variety, VarietyDir, load_config, source_code

    wanted: set[tuple[str, str]] = set()
    for av_id in av_ids:
        vd = VarietyDir(av_id=av_id, root=Path(varieties_root) / av_id)
        if not vd.exists():
            continue
        try:
            cfg = load_config(vd)
        except Exception:
            continue
        sources = cfg.get("sources") or {}
        gc = source_code(cfg, catalog.get(av_id, Variety(av_id)))
        for code in {gc.lower(), *sources.get("source_glottocodes", [])}:
            wanted.add((code.strip().lower(), sources.get("transcription", "")))
        wanted.add((gc.lower(), FALLBACK_SOURCE))
        wanted.update(supplemental_keys(vd.custom_dir))
    return wanted


def enrolled(varieties_root: Path) -> list[str]:
    """Non-dormant enrolled varieties."""
    from arcaverborum.aggregate import is_dormant

    result = []
    for child in sorted(Path(varieties_root).iterdir()):
        cfg = child / "config.yaml"
        if child.is_dir() and cfg.exists() and not is_dormant(yaml.safe_load(cfg.read_text(encoding="utf-8")) or {}):
            result.append(child.name)
    return result


def _sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def _filter_csv(src: Path, dst: Path, keep) -> int:
    dst.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with src.open(newline="", encoding="utf-8") as fin, dst.open("w", newline="", encoding="utf-8") as fout:
        reader = csv.reader(fin)
        header = next(reader)
        writer = csv.writer(fout, lineterminator="\n")
        writer.writerow(header)
        index = {name: i for i, name in enumerate(header)}
        width = len(header)
        for row in reader:
            if len(row) < width:  # pandas (the build's reader) pads short rows with empty values
                row = row + [""] * (width - len(row))
            if keep(row, index):
                writer.writerow(row)
                n += 1
    return n


def export(root: Path, output: Path, *, git_commit: str = "") -> dict:
    """Write the snapshot tree under ``output`` (must not exist)."""
    from arcaverborum.catalog import build_catalog, load_avid_registry
    from arcaverborum.glottolog import load_glottolog

    root = Path(root)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    languages = [root / "intake" / s / "languages.csv" for s in ("lexibank", "wiktionary")]
    catalog = build_catalog([p for p in languages if p.exists()],
                            glottolog=load_glottolog(root / "raw/glottolog/languages.csv"),
                            avid_registry=load_avid_registry())
    av_ids = enrolled(root / "varieties")
    wanted = input_keys(av_ids, root / "varieties", catalog)

    counts: dict[str, int] = {}
    lexibank_parameters: set[str] = set()
    wiktionary_forms: set[str] = set()
    for rel in FORMS_FILES:
        src = root / rel
        if not src.exists():
            raise FileNotFoundError(src)
        sink = lexibank_parameters if "lexibank" in rel else wiktionary_forms
        column = "Parameter_ID" if "lexibank" in rel else "ID"

        def keep(row, index, sink=sink, column=column):
            if (row[index["Glottocode"]].strip().lower(), row[index["Dataset"]]) in wanted:
                sink.add(row[index[column]])
                return True
            return False

        counts[rel] = _filter_csv(src, output / rel, keep)

    rel = "intake/lexibank/parameters_raw.csv"
    counts[rel] = _filter_csv(root / rel, output / rel, lambda row, index: row[index["ID"]] in lexibank_parameters)
    rel = "intake/wiktionary/pronunciations.csv"
    if (root / rel).exists():
        counts[rel] = _filter_csv(root / rel, output / rel,
                                  lambda row, index: row[index["source_form_id"]] in wiktionary_forms)
    for rel in WHOLE_FILES + guarded_cognacy_files(root):
        src = root / rel
        if not src.exists():
            raise FileNotFoundError(src)
        (output / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, output / rel)

    files = []
    for path in sorted(p for p in output.rglob("*") if p.is_file()):
        rel = path.relative_to(output).as_posix()
        files.append(dict(path=rel, bytes=path.stat().st_size, sha256=_sha(path),
                          **({"rows": counts[rel]} if rel in counts else {})))
    manifest = dict(
        schema=SNAPSHOT_SCHEMA,
        kind="Arca Verborum accepted-inputs snapshot",
        git_commit=git_commit,
        varieties=len(av_ids),
        input_keys=len(wanted),
        files=files,
        notes=[
            "Unpack at the root of a checkout of the same commit; `build.py update --all`, "
            "`aggregate` and the site builders then need no other input and no network.",
            "raw/glottolog/languages.csv and raw/concepticon/concepticon.tsv are the frozen tables "
            "the build used (fetched 2026-08-22 from the upstream default branches); see their sha256.",
            "Row licenses follow the per-source terms in intake metadata and the release datasheet; "
            "this snapshot follows the terms of the -full release tier.",
        ],
    )
    (output / "SNAPSHOT.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")
    return manifest


def pack(tree: Path, archive: Path) -> str:
    """Deterministic tar.gz of ``tree`` (sorted, zeroed metadata). Returns sha256."""
    tree = Path(tree)
    archive = Path(archive)
    if archive.exists():
        raise FileExistsError(archive)
    with archive.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=9, mtime=0, filename="") as gz:
            with tarfile.open(fileobj=gz, mode="w", format=tarfile.PAX_FORMAT) as tar:
                for path in sorted(p for p in tree.rglob("*") if p.is_file()):
                    info = tarfile.TarInfo(path.relative_to(tree).as_posix())
                    info.size = path.stat().st_size
                    info.mtime = 0
                    info.mode = 0o644
                    info.uid = info.gid = 0
                    info.uname = info.gname = ""
                    with path.open("rb") as handle:
                        tar.addfile(info, handle)
    return _sha(archive)


def unpack(archive: Path, root: Path) -> dict:
    """Unpack a snapshot into ``root``, verifying every file against SNAPSHOT.json."""
    root = Path(root)
    with tarfile.open(archive, "r:gz") as tar:
        tar.extractall(root, filter="data")
    manifest = json.loads((root / "SNAPSHOT.json").read_text())
    for entry in manifest["files"]:
        if _sha(root / entry["path"]) != entry["sha256"]:
            raise ValueError("Snapshot file corrupted: " + entry["path"])
    return manifest

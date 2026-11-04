"""Slice additions: rows of an already-pinned Lexibank dataset that a pull request needs.

A release's accepted-inputs snapshot holds only the ``(glottocode, dataset)``
groups that accepted constructions declared when the release was cut. A pull
request that starts reading another group of a dataset the snapshot already
pins (for example a supplement from IDS for a new language) commits that group
here, exactly as it stands in the full intake::

    slices/lexibank/
        datasets.csv          Dataset, Repository_Version   (must equal intake metadata)
        forms.csv             the intake forms rows, whole groups, intake column order
        parameters_raw.csv    the intake parameter rows those forms use

:func:`materialize` writes ``intake/slices/`` for the build:

* in a snapshot workspace, where a committed group is absent from
  ``intake/lexibank/forms.csv``, its rows (and any parameter rows the snapshot
  lacks) are written there and read after the Lexibank and Wiktionary intake;
* in a full workspace, where the group is present, nothing is written, after
  checking that the committed rows are the complete group, row for row.

A group that is only partly present, or differs from the intake, fails closed.
The next release's snapshot contains these groups, after which the committed
rows are redundant (and still checked).
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

csv.field_size_limit(1 << 30)  # intake rows can carry very long fields

SLICE_DIR = "slices/lexibank"
OUT_DIR = "intake/slices"
INTAKE = "intake/lexibank"


def _read(path: Path) -> tuple[list[str], list[list[str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader, [])
        width = len(header)
        rows = [r + [""] * (width - len(r)) if len(r) < width else r for r in reader]
    return header, rows


def present(root: Path) -> bool:
    return (Path(root) / SLICE_DIR / "forms.csv").is_file()


def _committed(root: Path):
    base = Path(root) / SLICE_DIR
    fh, forms = _read(base / "forms.csv")
    ph, params = _read(base / "parameters_raw.csv") if (base / "parameters_raw.csv").is_file() else (fh[:0], [])
    with (base / "datasets.csv").open(encoding="utf-8", newline="") as handle:
        pins = {r["Dataset"]: r["Repository_Version"] for r in csv.DictReader(handle)}
    return fh, forms, ph, params, pins


def _intake_groups(path: Path, wanted: set[tuple[str, str]]):
    """Rows of ``wanted`` groups in an intake forms file, in file order."""
    header, found = None, {}
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader)
        gi, di, width = header.index("Glottocode"), header.index("Dataset"), len(header)
        for row in reader:
            if len(row) < width:  # pandas (the build's reader) pads short rows with empty values
                row = row + [""] * (width - len(row))
            key = (row[gi].strip().lower(), row[di])
            if key in wanted:
                found.setdefault(key, []).append(row)
    return header, found


def validate(root: Path) -> list[str]:
    """Problems with the committed slices (empty list: valid). Needs the intake on disk."""
    root = Path(root)
    if not present(root):
        return []
    problems: list[str] = []
    fh, forms, ph, params, pins = _committed(root)
    ih = _read_header(root / INTAKE / "forms.csv")
    if fh != ih:
        problems.append("slices/lexibank/forms.csv: header differs from intake/lexibank/forms.csv")
        return problems
    if params and ph != _read_header(root / INTAKE / "parameters_raw.csv"):
        problems.append("slices/lexibank/parameters_raw.csv: header differs from intake/lexibank/parameters_raw.csv")
        return problems
    with (root / INTAKE / "metadata.csv").open(encoding="utf-8", newline="") as handle:
        versions = {r["Dataset"]: r["Repository_Version"] for r in csv.DictReader(handle)}
    col = {name: i for i, name in enumerate(fh)}
    used = {r[col["Dataset"]] for r in forms}
    for ds in sorted(used):
        if ds not in versions:
            problems.append(f"slices: dataset {ds!r} is not in the intake")
        elif pins.get(ds) != versions[ds]:
            problems.append(f"slices: dataset {ds!r} pinned to {pins.get(ds)!r}, intake has {versions[ds]!r}")
    ids = [r[col["ID"]] for r in forms]
    if len(set(ids)) != len(ids):
        problems.append("slices/lexibank/forms.csv: duplicate IDs")
    pcol = {name: i for i, name in enumerate(ph)}
    pids = [r[pcol["ID"]] for r in params] if params else []
    if len(set(pids)) != len(pids):
        problems.append("slices/lexibank/parameters_raw.csv: duplicate IDs")
    with (root / INTAKE / "languages.csv").open(encoding="utf-8", newline="") as handle:
        langs = {r["ID"]: (r.get("Glottocode") or "").strip().lower() for r in csv.DictReader(handle)}
    for r in forms:
        lid, gc = r[col["Language_ID"]], r[col["Glottocode"]].strip().lower()
        if lid not in langs:
            problems.append(f"slices: {r[col['ID']]}: unknown Language_ID {lid}")
        elif langs[lid] != gc:
            problems.append(f"slices: {r[col['ID']]}: Glottocode {gc} differs from languages.csv ({langs[lid]})")
    if problems:
        return problems

    groups: dict[tuple[str, str], list[list[str]]] = {}
    for r in forms:
        groups.setdefault((r[col["Glottocode"]].strip().lower(), r[col["Dataset"]]), []).append(r)
    _, found = _intake_groups(root / INTAKE / "forms.csv", set(groups))
    for key, rows in groups.items():
        have = found.get(key)
        if have is not None and have != rows:
            problems.append(f"slices: group {key[0]}/{key[1]} differs from the intake "
                            f"({len(rows)} committed rows, {len(have)} in intake)")
    _, iparams = _read(root / INTAKE / "parameters_raw.csv")
    known = {r[0]: r for r in iparams}
    committed = {r[pcol["ID"]]: r for r in params}
    for pid, row in committed.items():
        if pid in known and known[pid] != row:
            problems.append(f"slices: parameter {pid} differs from the intake")
    for r in forms:
        if r[col["Parameter_ID"]] not in known and r[col["Parameter_ID"]] not in committed:
            problems.append(f"slices: {r[col['ID']]}: Parameter_ID missing from intake and slice")
    return problems


def _read_header(path: Path) -> list[str]:
    with path.open(encoding="utf-8", newline="") as handle:
        return next(csv.reader(handle), [])


def _write(path: Path, header: list[str], rows: list[list[str]]) -> None:
    import io

    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    text = buffer.getvalue()
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def materialize(root: Path) -> Path | None:
    """Write ``intake/slices/`` (only the groups the intake lacks). Fails closed on any problem."""
    root = Path(root)
    out = root / OUT_DIR
    if not present(root):
        if out.exists():
            for name in ("forms.csv", "parameters_raw.csv", "languages.csv", "STAMP.json"):
                (out / name).unlink(missing_ok=True)
        return None
    stamp = hashlib.sha256()
    for rel in (f"{SLICE_DIR}/forms.csv", f"{SLICE_DIR}/parameters_raw.csv", f"{SLICE_DIR}/datasets.csv"):
        p = root / rel
        stamp.update(p.read_bytes() if p.exists() else b"")
    for rel in (f"{INTAKE}/forms.csv", f"{INTAKE}/parameters_raw.csv", f"{INTAKE}/metadata.csv"):
        st = (root / rel).stat()
        stamp.update(f"{rel}:{st.st_size}:{st.st_mtime_ns}".encode())
    key = stamp.hexdigest()
    stamp_file = out / "STAMP.json"
    if stamp_file.exists() and json.loads(stamp_file.read_text()).get("key") == key:
        return out
    problems = validate(root)
    if problems:
        raise ValueError("Invalid slices:\n  " + "\n  ".join(problems))
    fh, forms, ph, params, _ = _committed(root)
    col = {name: i for i, name in enumerate(fh)}
    groups = {(r[col["Glottocode"]].strip().lower(), r[col["Dataset"]]) for r in forms}
    _, found = _intake_groups(root / INTAKE / "forms.csv", groups)
    emit = [r for r in forms if (r[col["Glottocode"]].strip().lower(), r[col["Dataset"]]) not in found]
    iheader, iparams = _read(root / INTAKE / "parameters_raw.csv")
    known = {r[0] for r in iparams}
    needed = {r[col["Parameter_ID"]] for r in emit}
    pemit = [r for r in params if r[0] in needed and r[0] not in known]
    if emit:
        _write(out / "forms.csv", fh, emit)
        _write(out / "parameters_raw.csv", ph or iheader, pemit)
        _write(out / "languages.csv", _read_header(root / INTAKE / "languages.csv"), [])
    else:  # full workspace: every group is already in the intake; add no intake source
        for name in ("forms.csv", "parameters_raw.csv", "languages.csv"):
            (out / name).unlink(missing_ok=True)
        out.mkdir(parents=True, exist_ok=True)
    stamp_file.write_text(json.dumps({"key": key, "groups_emitted": len(groups) - len(found),
                                      "groups_present": len(found), "forms": len(emit)}) + "\n")
    return out


def export_groups(root: Path, groups: list[tuple[str, str]], dest: Path | None = None) -> dict:
    """Maintainer helper: copy whole intake groups (and their parameters) into ``slices/lexibank/``."""
    root = Path(root)
    dest = Path(dest or root / SLICE_DIR)
    wanted = {(g.lower(), d) for g, d in groups}
    header, found = _intake_groups(root / INTAKE / "forms.csv", wanted)
    missing = wanted - set(found)
    if missing:
        raise ValueError(f"groups not in the intake: {sorted(missing)}")
    old_rows = _read(dest / "forms.csv")[1] if (dest / "forms.csv").exists() else []
    col = {name: i for i, name in enumerate(header)}
    keep = [r for r in old_rows if (r[col["Glottocode"]].strip().lower(), r[col["Dataset"]]) not in wanted]
    rows = keep + [r for key in sorted(found) for r in found[key]]
    pheader, iparams = _read(root / INTAKE / "parameters_raw.csv")
    need = {r[col["Parameter_ID"]] for r in rows}
    params = [r for r in iparams if r[0] in need]
    with (root / INTAKE / "metadata.csv").open(encoding="utf-8", newline="") as handle:
        versions = {r["Dataset"]: r["Repository_Version"] for r in csv.DictReader(handle)}
    used = sorted({r[col["Dataset"]] for r in rows})
    _write(dest / "forms.csv", header, rows)
    _write(dest / "parameters_raw.csv", pheader, params)
    _write(dest / "datasets.csv", ["Dataset", "Repository_Version"], [[d, versions[d]] for d in used])
    return {"groups": len({(r[col['Glottocode']].strip().lower(), r[col['Dataset']]) for r in rows}),
            "forms": len(rows), "parameters": len(params)}

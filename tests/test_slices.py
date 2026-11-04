import csv
from pathlib import Path

import pytest

from arcaverborum import slices

FORMS = ["ID", "Dataset", "Language_ID", "Parameter_ID", "Value", "Form", "Segments", "Glottocode"]
PARAMS = ["ID", "Dataset", "Name", "Concepticon_ID", "Concepticon_Gloss"]


def write(path: Path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def read(path: Path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.reader(handle))


GROUP = [
    ["ids_cofan-1-1", "ids", "ids_cofan", "ids_1-1", "a", "a", "a", "cofa1242"],
    ["ids_cofan-1-2", "ids", "ids_cofan", "ids_1-2", "bi", "bi", "b i", "cofa1242"],
]
OTHER = [["ids_paez-1-1", "ids", "ids_paez", "ids_1-1", "u", "u", "u", "paez1247"]]
PARAM_ROWS = [["ids_1-1", "ids", "world", "1", "WORLD"], ["ids_1-2", "ids", "earth", "2", "EARTH"]]


def full_workspace(tmp_path: Path) -> Path:
    root = tmp_path / "full"
    intake = root / "intake/lexibank"
    write(intake / "forms.csv", FORMS, OTHER + GROUP)
    write(intake / "parameters_raw.csv", PARAMS, PARAM_ROWS)
    write(intake / "metadata.csv", ["Dataset", "Repository_Version"], [["ids", "v1.2"]])
    write(intake / "languages.csv", ["ID", "Glottocode"], [["ids_cofan", "cofa1242"], ["ids_paez", "paez1247"]])
    return root


def snapshot_workspace(tmp_path: Path, full: Path) -> Path:
    """Same intake minus the cofa1242/ids group and the parameter only it uses."""
    root = tmp_path / "snap"
    intake = root / "intake/lexibank"
    write(intake / "forms.csv", FORMS, OTHER)
    write(intake / "parameters_raw.csv", PARAMS, PARAM_ROWS[:1])
    write(intake / "metadata.csv", ["Dataset", "Repository_Version"], [["ids", "v1.2"]])
    write(intake / "languages.csv", ["ID", "Glottocode"], [["ids_cofan", "cofa1242"], ["ids_paez", "paez1247"]])
    for name in ("forms.csv", "parameters_raw.csv", "datasets.csv"):
        src = full / slices.SLICE_DIR / name
        dst = root / slices.SLICE_DIR / name
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(src.read_bytes())
    return root


def test_export_then_full_workspace_adds_nothing(tmp_path):
    full = full_workspace(tmp_path)
    stats = slices.export_groups(full, [("cofa1242", "ids")])
    assert stats == {"groups": 1, "forms": 2, "parameters": 2}
    assert read(full / slices.SLICE_DIR / "datasets.csv")[1] == ["ids", "v1.2"]
    assert slices.validate(full) == []
    out = slices.materialize(full)
    assert not (out / "forms.csv").exists()  # no extra intake source in a full workspace


def test_snapshot_workspace_gets_the_missing_group(tmp_path):
    full = full_workspace(tmp_path)
    slices.export_groups(full, [("cofa1242", "ids")])
    snap = snapshot_workspace(tmp_path, full)
    assert slices.validate(snap) == []
    out = slices.materialize(snap)
    assert read(out / "forms.csv")[1:] == GROUP
    assert read(out / "parameters_raw.csv")[1:] == [PARAM_ROWS[1]]  # only what the snapshot lacks
    assert read(out / "languages.csv") == [["ID", "Glottocode"]]


def test_changed_row_fails_closed(tmp_path):
    full = full_workspace(tmp_path)
    slices.export_groups(full, [("cofa1242", "ids")])
    path = full / slices.SLICE_DIR / "forms.csv"
    rows = read(path)
    rows[1][4] = "changed"
    write(path, rows[0], rows[1:])
    assert any("differs from the intake" in p for p in slices.validate(full))
    with pytest.raises(ValueError):
        slices.materialize(full)


def test_partial_group_fails_closed(tmp_path):
    full = full_workspace(tmp_path)
    slices.export_groups(full, [("cofa1242", "ids")])
    path = full / slices.SLICE_DIR / "forms.csv"
    rows = read(path)
    write(path, rows[0], rows[1:2])
    assert any("differs from the intake" in p for p in slices.validate(full))


def test_version_pin_must_match(tmp_path):
    full = full_workspace(tmp_path)
    slices.export_groups(full, [("cofa1242", "ids")])
    write(full / slices.SLICE_DIR / "datasets.csv", ["Dataset", "Repository_Version"], [["ids", "v1.1"]])
    assert any("pinned to" in p for p in slices.validate(full))


def test_unknown_parameter_fails(tmp_path):
    full = full_workspace(tmp_path)
    slices.export_groups(full, [("cofa1242", "ids")])
    snap = snapshot_workspace(tmp_path, full)
    write(snap / slices.SLICE_DIR / "parameters_raw.csv", PARAMS, [])
    assert any("Parameter_ID missing" in p for p in slices.validate(snap))


def test_no_slices_is_a_no_op(tmp_path):
    full = full_workspace(tmp_path)
    assert slices.validate(full) == []
    assert slices.materialize(full) is None

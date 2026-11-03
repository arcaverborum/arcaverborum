"""Source extensions: committed new sources are validated fail-closed and materialized as intake."""

from __future__ import annotations

import csv

import pytest

from arcaverborum.extensions import materialize, validate

NAME = "demosource"


def _write(path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def _workspace(tmp_path, **override):
    _write(tmp_path / "raw/glottolog/languages.csv", ["ID", "Name", "Glottocode"],
           [["xokl1240", "Xokleng", "xokl1240"]])
    (tmp_path / "raw/concepticon").mkdir(parents=True)
    (tmp_path / "raw/concepticon/concepticon.tsv").write_text("ID\tGLOSS\n1277\tHAND\n", encoding="utf-8")
    _write(tmp_path / "intake/lexibank/metadata.csv", ["Dataset", "License"], [["diacl", "CC-BY-4.0"]])
    ext = tmp_path / "extensions" / override.get("name", NAME)
    name = override.get("name", NAME)
    _write(ext / "metadata.csv", ["Dataset", "Title", "Citation", "URL", "License"],
           [[name, "Demo", "Doe 2026. Demo wordlist.", "https://example.org",
             override.get("license", "https://creativecommons.org/licenses/by/4.0/")]])
    _write(ext / "languages.csv", ["ID", "Name", "Glottocode"],
           [["xok", "Xokleng", override.get("glottocode", "xokl1240")]])
    _write(ext / "parameters.csv", ["ID", "Name", "Concepticon_ID"], [["hand", "hand", "1277"]])
    _write(ext / "forms.csv", ["ID", "Language_ID", "Parameter_ID", "Value", "Form", "Source"],
           [["xok-hand", override.get("language_id", "xok"), "hand", "ŋɛ̃", "ŋɛ̃",
             override.get("source", f"{name}_Doe2026")]])
    (ext / "sources.bib").write_text(
        "@book{" + override.get("bibkey", f"{name}_Doe2026") + ",\n  title = {Demo},\n  year = {2026}\n}\n",
        encoding="utf-8")
    (ext / "README.md").write_text("Demo wordlist, elicited by the contributor.\n", encoding="utf-8")
    return tmp_path


def test_valid_extension_materializes_in_intake_schema(tmp_path):
    root = _workspace(tmp_path)
    assert validate(root) == []
    out = materialize(root)
    assert out == root / "intake/extensions"
    forms = list(csv.DictReader((out / "forms.csv").open(encoding="utf-8")))
    assert forms == [dict(forms[0], ID="xok-hand", Dataset=NAME, Glottocode="xokl1240", Glottolog_Name="Xokleng",
                          Concepticon_Gloss="HAND", Value="ŋɛ̃")]
    params = list(csv.DictReader((out / "parameters_raw.csv").open(encoding="utf-8")))
    assert params[0]["Concepticon_Gloss"] == "HAND"
    meta = list(csv.DictReader((out / "metadata.csv").open(encoding="utf-8")))
    assert (meta[0]["Dataset"], meta[0]["Form_Count"], meta[0]["Has_Cognates"]) == (NAME, "1", "False")
    assert "@book{demosource_Doe2026" in (out / "sources.bib").read_text(encoding="utf-8")


def test_unchanged_extensions_keep_intake_files_untouched(tmp_path):
    root = _workspace(tmp_path)
    out = materialize(root)
    before = (out / "forms.csv").stat().st_mtime_ns
    materialize(root)
    assert (out / "forms.csv").stat().st_mtime_ns == before


def test_no_extensions_removes_materialized_intake(tmp_path):
    root = _workspace(tmp_path)
    materialize(root)
    import shutil

    shutil.rmtree(root / "extensions" / NAME)
    assert materialize(root) is None
    assert not (root / "intake/extensions").exists()


@pytest.mark.parametrize("override, message", [
    (dict(license=""), "License is required"),
    (dict(license="all rights reserved"), "Unknown licence declaration"),
    (dict(glottocode="zzzz9999"), "not in the frozen Glottolog table"),
    (dict(language_id="nope"), "Language_ID 'nope'"),
    (dict(bibkey="Doe2026", source="Doe2026"), "every key must start with"),
    (dict(source="demosource_Missing"), "not in sources.bib"),
    (dict(name="diacl"), "already used by another intake source"),
    (dict(name="Bad-Name"), "lower-case dataset identifier"),
])
def test_invalid_extensions_fail_closed(tmp_path, override, message):
    root = _workspace(tmp_path, **override)
    problems = validate(root)
    assert any(message in p for p in problems), problems
    with pytest.raises(ValueError, match="Invalid source extensions"):
        materialize(root)

"""CODEOWNERS generation from editors.csv."""

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("codeowners", ROOT / "scripts/codeowners.py")
codeowners = importlib.util.module_from_spec(spec)
spec.loader.exec_module(codeowners)


def test_rules_go_from_general_to_specific(tmp_path):
    (tmp_path / "tup-guarani").mkdir()
    (tmp_path / "tup-guarani/config.yaml").write_text("av_id: tup-guarani\n")
    rows = [dict(github_login="boss", name="M", scope="maintainer"),
            dict(github_login="fam", name="F", scope="family:tup;family:arw"),
            dict(github_login="lang", name="L", scope="variety:tup-guarani"),
            dict(github_login="sem", name="S", scope="layer:concepts")]
    lines = codeowners.generate(rows, tmp_path).splitlines()
    assert lines.index("* @boss") < lines.index("/varieties/tup-*/ @fam") < lines.index(
        "/varieties/tup-guarani/ @fam @lang")
    assert "/varieties/arw-*/ @fam" in lines
    assert "/src/arcaverborum/data/concepts.csv @boss @sem" in lines
    assert lines[-2:] == ["/editors.csv @boss", "/.github/ @boss"]


@pytest.mark.parametrize("scope", ["variety:tup-unknown", "family:tupi", "layer:phonology", "editor"])
def test_bad_scopes_fail(tmp_path, scope):
    rows = [dict(github_login="boss", name="M", scope="maintainer"), dict(github_login="x", name="X", scope=scope)]
    with pytest.raises(SystemExit):
        codeowners.generate(rows, tmp_path)


def test_committed_codeowners_is_current():
    assert codeowners.main(["--check"]) == 0

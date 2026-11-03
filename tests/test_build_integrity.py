"""Build integrity: failed builds fail the CLI, aggregates refuse stale or
missing outputs, dormant identities are explicit, upstream tables never
download implicitly, and published dates are pinnable."""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path

import pytest
import yaml

from arcaverborum import tracking
from arcaverborum.aggregate import check_build_complete, is_dormant

ROOT = Path(__file__).resolve().parents[1]


def _variety(root: Path, av_id: str, **extra) -> Path:
    folder = root / av_id
    folder.mkdir(parents=True)
    cfg = dict(av_id=av_id, name=av_id, glottocode="", sources=dict(transcription="src"),
               scoring=dict(forms_score=0.5, tier="bronze"), **extra)
    (folder / "config.yaml").write_text(yaml.safe_dump(cfg))
    return folder


def _built(folder: Path) -> None:
    cfg = yaml.safe_load((folder / "config.yaml").read_text())
    digest, comps = tracking.fingerprint(tracking.config_component(cfg),
                                         tracking.custom_component(folder / "custom"), "", tracking.recipe_hash())
    (folder / "generated").mkdir(exist_ok=True)
    (folder / "generated" / "forms.csv").write_text("ID\n")
    tracking.write_manifest(folder / "generated", digest, comps, 0)


def test_complete_build_has_no_problems(tmp_path):
    _built(_variety(tmp_path, "a"))
    _variety(tmp_path, "d", dormant=True)
    assert check_build_complete(tmp_path) == []


def test_unbuilt_stale_and_dormant_output_are_reported(tmp_path):
    _variety(tmp_path, "unbuilt")
    stale = _variety(tmp_path, "stale")
    _built(stale)
    cfg = yaml.safe_load((stale / "config.yaml").read_text())
    cfg["sources"]["transcription"] = "other"
    (stale / "config.yaml").write_text(yaml.safe_dump(cfg))
    dormant = _variety(tmp_path, "dormant", dormant=True)
    _built(dormant)
    problems = check_build_complete(tmp_path)
    assert problems == ["dormant: dormant but has generated output",
                        "stale: config changed since build",
                        "unbuilt: not built"]


def test_dormant_flag():
    assert is_dormant({"dormant": True}) and not is_dormant({})


def _build_cli():
    spec = importlib.util.spec_from_file_location("build_cli", ROOT / "build.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_update_exits_nonzero_when_a_variety_fails(monkeypatch, tmp_path):
    cli = _build_cli()
    import arcaverborum.variety as variety
    monkeypatch.setattr(variety, "update_many", lambda **_: {"built": 1, "failed": 1})
    monkeypatch.setattr(cli, "_combined_intake", lambda: {"forms": [], "languages": [], "parameters": []})
    args = argparse.Namespace(av_ids=["x"], all_varieties=False, family=None, macroarea=None,
                              force=False, csv=True, intake_db=str(tmp_path / "db"))
    assert cli.cmd_update(args) == 1
    monkeypatch.setattr(variety, "update_many", lambda **_: {"built": 1, "failed": 0})
    assert cli.cmd_update(args) == 0


def test_aggregate_refuses_incomplete_builds(monkeypatch, tmp_path):
    cli = _build_cli()
    _variety(tmp_path, "unbuilt")
    monkeypatch.setattr(cli, "VARIETIES_DIR", tmp_path)
    assert cli.cmd_aggregate(argparse.Namespace(allow_incomplete=False)) == 1


def test_upstream_tables_never_download_implicitly(monkeypatch, tmp_path):
    from arcaverborum import concepticon, glottolog

    def no_network(*_, **__):
        raise AssertionError("network access attempted")

    monkeypatch.setattr(glottolog.urllib.request, "urlopen", no_network)
    monkeypatch.setattr(glottolog, "RAW_CACHE", tmp_path / "missing.csv")
    monkeypatch.setattr(concepticon, "RAW_CACHE", tmp_path / "missing.tsv")
    with pytest.raises(FileNotFoundError):
        glottolog.load_glottolog()
    with pytest.raises(FileNotFoundError):
        concepticon.load_concepticon_by_id()


def test_build_date_is_pinnable(monkeypatch):
    from arcaverborum.buildinfo import build_date

    monkeypatch.setenv("ARCA_BUILD_DATE", "2026-11-10")
    assert build_date() == "2026-11-10"
    monkeypatch.delenv("ARCA_BUILD_DATE")
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "0")
    assert build_date() == "1970-01-01"

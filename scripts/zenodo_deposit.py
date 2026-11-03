#!/usr/bin/env python3
"""Prepare (and optionally upload) a schema-letter Arca Verborum release to Zenodo.

The first schema-A deposit mints a NEW concept DOI. Later releases become new
versions of it once its record id is stored in
``src/arcaverborum/data/zenodo.json`` (``concept_record_id``). The pre-2026-11
record ``10.5281/zenodo.17294927`` is linked as a related work, not continued.

Safe by design:

* Without a token, or with ``--dry-run``: writes the deposit metadata JSON next
  to the release and prints the files to upload. No network.
* With a token: creates a DRAFT and uploads the files. It publishes only with
  ``--publish`` (irreversible). ``--sandbox`` targets sandbox.zenodo.org.

Token: ``--token``, or ``ZENODO_TOKEN`` (``ZENODO_SANDBOX_TOKEN`` for --sandbox).

Usage::

    python scripts/zenodo_deposit.py A-2026-11-10 --dry-run
    ZENODO_SANDBOX_TOKEN=... python scripts/zenodo_deposit.py A-2026-11-10 --sandbox
    ZENODO_TOKEN=... python scripts/zenodo_deposit.py A-2026-11-10 --publish
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from arcaverborum.release_a import ORG_URL, SITE_URL, parse_release_id  # noqa: E402

STATE = PROJECT_ROOT / "src/arcaverborum/data/zenodo.json"
PREVIOUS_RECORD_DOI = "10.5281/zenodo.17294927"
LEXIBANK_DOI = "10.1038/s41597-022-01432-0"
MAINTAINER = {"name": "Tresoldi, Tiago", "orcid": "0000-0002-2863-1467",
              "affiliation": "Department of Linguistics and Philology, Uppsala University"}
# Zenodo needs one record-level licence id. All sources require attribution; NC/SA
# and undeclared terms are per row. "other-at" (Other, Attribution) is the least
# misleading single choice; the description and LICENSES.md are authoritative.
RECORD_LICENSE = "other-at"


def editors(path: Path = PROJECT_ROOT / "editors.csv") -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        rows = [r for r in csv.DictReader(handle) if r.get("name")]
    return [dict(name=r["name"], type="Editor", **({"orcid": r["orcid"]} if r.get("orcid") else {}))
            for r in rows if r.get("github_login") != "tresoldi"]


def release_files(release_dir: Path, release_id: str) -> list[Path]:
    files = sorted(release_dir.glob(f"arcaverborum-{release_id}-*.tar.gz"))
    files += [p for p in (release_dir / "SHA256SUMS",) if p.exists()]
    if not files:
        raise SystemExit(f"No release archives in {release_dir}")
    return files


def build_metadata(release_dir: Path, release_id: str) -> dict:
    parse_release_id(release_id)
    tiers = {}
    for tier in ("full", "redistributable", "by"):
        manifest = release_dir / f"arcaverborum-{release_id}-{tier}" / "MANIFEST.json"
        if manifest.exists():
            tiers[tier] = json.loads(manifest.read_text(encoding="utf-8"))
    if "full" not in tiers:
        raise SystemExit("The full tier manifest is required")
    full = tiers["full"]
    tier_items = "".join(
        f"<li><code>{t}</code>: {m['records']:,} records, {m['constructions']:,} constructions, "
        f"{m['sources']} sources. {m['tier_description']}</li>" for t, m in tiers.items())
    description = (
        "<p><strong>Arca Verborum</strong> is a per-variety lexical database for computational historical "
        "linguistics: for each language variety it keeps one reviewed construction from the best available "
        "lexical evidence, with full provenance, its own frozen variety and concept identifiers, "
        "Concepticon/Glottolog/WordNet mappings, and a CLDF export. It is built on top of Lexibank, GLED, "
        "Wiktionary and original sources, whose contribution is foundational.</p>"
        f"<p>Release <strong>{release_id}</strong> (schema letter {release_id[0]}) has three licence tiers:</p>"
        f"<ul>{tier_items}</ul>"
        "<p><strong>Licensing is per source and per row.</strong> Each record keeps its source's terms in the "
        "<code>License</code> and <code>terms_status</code> columns; see LICENSES.md in each archive. Arca's own "
        "identifiers, catalogs, links and scores are CC BY 4.0; adaptations of ShareAlike records keep their "
        "source's terms. Rows marked <code>missing_declaration</code> (full tier only) come from sources whose "
        "redistribution terms are undeclared; they are included in good faith pending clarification with the "
        "rights holders. The record-level licence below is a placeholder required by Zenodo.</p>"
        "<p>The accepted-inputs snapshot rebuilds the release from the repository at the recorded commit "
        f"({full.get('git_commit') or 'see MANIFEST.json'}). Explorer: {SITE_URL}. Repository: {ORG_URL}.</p>"
        "<p>The baseline was built by the maintainer with extensive AI assistance; every change is owned by its "
        "human author and model reviews are not counted as expert review.</p>"
    )
    related = [
        {"identifier": ORG_URL, "relation": "isSupplementedBy", "scheme": "url"},
        {"identifier": LEXIBANK_DOI, "relation": "references", "scheme": "doi"},
        {"identifier": PREVIOUS_RECORD_DOI, "relation": "continues", "scheme": "doi"},
    ]
    return {"metadata": {
        "title": f"Arca Verborum {release_id}",
        "upload_type": "dataset",
        "publication_date": parse_release_id(release_id)["date"],
        "description": description,
        "creators": [MAINTAINER],
        "contributors": editors(),
        "version": release_id,
        "license": RECORD_LICENSE,
        "access_right": "open",
        "keywords": ["computational historical linguistics", "comparative linguistics", "lexical database",
                     "wordlist", "cognates", "CLDF", "Concepticon", "WordNet", "colexification"],
        "related_identifiers": related,
        "notes": "Mixed per-row terms (CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, GPL-3.0, public domain, and "
                 "undeclared in the full tier). See LICENSES.md.",
    }}


def _api(base, path, token, method="GET", **kw):
    import requests

    params = kw.pop("params", {}) | {"access_token": token}
    r = requests.request(method, f"{base}/api{path}", params=params, timeout=120, **kw)
    if r.status_code >= 400:
        raise SystemExit(f"Zenodo API {method} {path} failed [{r.status_code}]: {r.text[:500]}")
    return r.json() if r.text else {}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("release_id")
    ap.add_argument("--release-dir", default=None, help="Default: output/release/<release_id>")
    ap.add_argument("--sandbox", action="store_true")
    ap.add_argument("--publish", action="store_true", help="Publish the draft (irreversible)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--token", default=None)
    args = ap.parse_args(argv)

    release_dir = Path(args.release_dir or PROJECT_ROOT / "output/release" / args.release_id)
    metadata = build_metadata(release_dir, args.release_id)
    files = release_files(release_dir, args.release_id)
    meta_path = release_dir / f"zenodo-deposit-{args.release_id}.json"
    meta_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote deposit metadata -> {meta_path}")
    for f in files:
        print(f"  upload: {f.name} ({f.stat().st_size / 1e6:.1f} MB)")

    token = args.token or os.environ.get("ZENODO_SANDBOX_TOKEN" if args.sandbox else "ZENODO_TOKEN")
    if args.dry_run or not token:
        print("Dry run: no network. Upload the files above with this metadata, or pass a token.")
        return 0

    base = "https://sandbox.zenodo.org" if args.sandbox else "https://zenodo.org"
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    concept = state.get("sandbox_concept_record_id" if args.sandbox else "concept_record_id")
    if concept:
        latest = _api(base, f"/records/{concept}", token)
        draft = _api(base, f"/deposit/depositions/{latest['id']}/actions/newversion", token, "POST")
        draft = _api(base, draft["links"]["latest_draft"].split("/api", 1)[1], token)
        for old in draft.get("files", []):
            _api(base, f"/deposit/depositions/{draft['id']}/files/{old['id']}", token, "DELETE")
    else:
        draft = _api(base, "/deposit/depositions", token, "POST", json={})
    bucket = draft["links"]["bucket"]
    import requests

    for f in files:
        with f.open("rb") as handle:
            r = requests.put(f"{bucket}/{f.name}", data=handle, params={"access_token": token}, timeout=3600)
            r.raise_for_status()
    _api(base, f"/deposit/depositions/{draft['id']}", token, "PUT", json=metadata)
    print(f"Draft ready: {draft['links']['html']}")
    if args.publish:
        published = _api(base, f"/deposit/depositions/{draft['id']}/actions/publish", token, "POST")
        print(f"Published: {published.get('doi')} (concept {published.get('conceptdoi')})")
        key = "sandbox_concept_record_id" if args.sandbox else "concept_record_id"
        state[key] = published.get("conceptrecid")
        STATE.write_text(json.dumps(state, indent=1) + "\n")
        print(f"Recorded {key} in {STATE.relative_to(PROJECT_ROOT)}; commit it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

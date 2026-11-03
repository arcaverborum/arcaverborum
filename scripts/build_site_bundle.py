#!/usr/bin/env python3
"""Seal the explorer (code + data from one commit) into a deployable bundle.

    python scripts/build_site_bundle.py release A-2026-11-10 OUT.tar.gz
    python scripts/build_site_bundle.py live <git-sha> OUT.tar.gz

The bundle is ``web/`` without development-only files, with the generated
``web/data/`` built from the same commit. ``release`` bundles record the
release identifier in ``RELEASE``; ``live`` bundles get a banner naming the
data revision and pointing to the latest release. The archive is
deterministic (sorted members, zeroed metadata).
"""

from __future__ import annotations

import argparse
import html
import json
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from arcaverborum.snapshot import pack  # noqa: E402

EXCLUDE = {"README.md", "tests", "notices", "CNAME", "core.html", "app.js", "arca-core.sqlite.gz", "BUILD_INFO"}
BUILD_DIRS = ("colexification", "colexification-graphs", "colexification-communities", "concept-rows")
BANNER_STYLE = ("background:#fff3cd;color:#3d2f00;border-bottom:1px solid #d4b106;padding:.5rem 1rem;"
                "font:14px/1.4 system-ui,sans-serif")


def banner(revision: str) -> str:
    rev = html.escape(revision[:12])
    return (f'<div class="live-banner" role="note" style="{BANNER_STYLE}"><strong>Live data</strong> from the '
            f'current <code>master</code> (revision <code>{rev}</code>), not a release. For citable data use '
            '<a href="https://arcaverborum.org">the latest release</a>.</div>')


def assemble(web: Path, target: Path, channel: str, ident: str, release_dir: Path | None = None) -> None:
    if not (web / "data" / "manifest.json").exists():
        raise SystemExit("web/data is not built; run scripts/build_research_web.py first")
    referenced = (web / "data" / "manifest.json").read_text(encoding="utf-8")
    for item in sorted(web.iterdir()):
        if item.name in EXCLUDE:
            continue
        dest = target / item.name
        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copyfile(item, dest)
    # Content-addressed build directories that the data manifest no longer references are stale.
    for family in BUILD_DIRS:
        for build in sorted((target / "data" / family).glob("*")) if (target / "data" / family).exists() else []:
            if build.is_dir() and build.name not in referenced:
                shutil.rmtree(build)
    index = target / "index.html"
    text = index.read_text(encoding="utf-8")
    text = text.replace(' · <a href="core.html">Previous Core explorer</a>', "")
    if channel == "live":
        if "<body>" not in text:
            raise SystemExit("index.html has no <body> tag to attach the live banner")
        text = text.replace("<body>", "<body>\n" + banner(ident), 1)
        (target / "REVISION").write_text(ident + "\n")
    else:
        text = text.replace("</footer>", ' · <a href="https://live.arcaverborum.org">Live master</a></footer>', 1)
        (target / "RELEASE").write_text(ident + "\n")
    index.write_text(text, encoding="utf-8")
    downloads = target / "downloads.html"
    if downloads.exists():
        page = downloads.read_text(encoding="utf-8")
        page = page.replace("<!--RELEASE-SECTION-->", release_section(channel, ident, release_dir))
        downloads.write_text(page, encoding="utf-8")


def release_section(channel: str, ident: str, release_dir: Path | None) -> str:
    releases = "https://github.com/arcaverborum/arcaverborum/releases"
    if channel == "live":
        return (f'<h2>Live data</h2><p>This site shows the current <code>master</code> (revision '
                f'<code>{html.escape(ident[:12])}</code>), which is not a release. Download the '
                f'<a href="{releases}/latest">latest release</a> for citable data.</p>')
    rows = []
    for tier in ("by", "redistributable", "full"):
        manifest = (release_dir / f"arcaverborum-{ident}-{tier}" / "MANIFEST.json") if release_dir else None
        if not manifest or not manifest.exists():
            raise SystemExit(f"Missing tier manifest for {tier}: pass --release-dir")
        m = json.loads(manifest.read_text(encoding="utf-8"))
        name = f"arcaverborum-{ident}-{tier}.tar.gz"
        rows.append(f'<tr><td><a href="{releases}/download/{ident}/{name}"><code>{tier}</code></a></td>'
                    f'<td>{m["records"]:,}</td><td>{m["lexical_constructions"]:,}</td><td>{m["sources"]}</td></tr>')
    snapshot = f"arcaverborum-{ident}-snapshot.tar.gz"
    return (f'<h2>Release {html.escape(ident)}</h2>'
            '<div class="scroll" role="region" aria-label="Release downloads" tabindex="0"><table>'
            '<thead><tr><th scope="col">Tier</th><th scope="col">Records</th><th scope="col">Constructions</th>'
            '<th scope="col">Sources</th></tr></thead><tbody>' + "".join(rows) + '</tbody></table></div>'
            f'<p><a href="{releases}/download/{ident}/{snapshot}">Accepted-inputs snapshot</a> · '
            f'<a href="{releases}/download/{ident}/SHA256SUMS">SHA256SUMS</a> · '
            f'<a href="{releases}/tag/{ident}">Release notes and all assets</a></p>')


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("channel", choices=["release", "live"])
    ap.add_argument("ident", help="Release identifier (release) or git revision (live)")
    ap.add_argument("output", type=Path)
    ap.add_argument("--web", type=Path, default=ROOT / "web")
    ap.add_argument("--release-dir", type=Path, help="Directory with the release's tier folders (release channel)")
    args = ap.parse_args(argv)
    if args.channel == "release":
        from arcaverborum.release_a import parse_release_id

        parse_release_id(args.ident)
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "site"
        target.mkdir()
        assemble(args.web, target, args.channel, args.ident, args.release_dir)
        digest = pack(target, args.output)
    print(f"{digest}  {args.output.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

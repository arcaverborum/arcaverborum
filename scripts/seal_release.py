#!/usr/bin/env python3
"""Pack a built release into its upload assets and write SHA256SUMS.

    python scripts/seal_release.py A-2026-11-10 [--extra SNAPSHOT.tar.gz SITE.tar.gz ...]

Packs each ``output/release/<id>/arcaverborum-<id>-<tier>/`` folder into a
deterministic ``.tar.gz`` next to it, copies the extra assets there, and
writes ``SHA256SUMS`` over every asset. Existing archives are never
overwritten.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from arcaverborum.release_a import parse_release_id  # noqa: E402
from arcaverborum.snapshot import _sha, pack  # noqa: E402


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("release_id")
    ap.add_argument("--extra", nargs="*", type=Path, default=[])
    ap.add_argument("--release-dir", type=Path)
    args = ap.parse_args(argv)
    parse_release_id(args.release_id)
    out = args.release_dir or ROOT / "output/release" / args.release_id
    tiers = sorted(p for p in out.glob(f"arcaverborum-{args.release_id}-*") if p.is_dir())
    if not tiers:
        raise SystemExit(f"No tier folders in {out}")
    assets = []
    for tier in tiers:
        archive = out / (tier.name + ".tar.gz")
        pack(tier, archive)
        assets.append(archive)
    for extra in args.extra:
        dest = out / extra.name
        if dest.resolve() != extra.resolve():
            if dest.exists():
                raise SystemExit(f"{dest} exists")
            shutil.copyfile(extra, dest)
        assets.append(dest)
    lines = [f"{_sha(a)}  {a.name}" for a in sorted(assets, key=lambda p: p.name)]
    (out / "SHA256SUMS").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())

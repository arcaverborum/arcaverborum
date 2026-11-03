#!/usr/bin/env python3
"""Tier-1 proof: re-derive the accepted outputs from git + the accepted-inputs snapshot.

Exports the committed tree (``git archive``) into an empty work directory,
unpacks the snapshot there, and runs ``update --all`` and ``aggregate`` (and,
with ``--web``, the lexical site builder) with network access disabled and a
pinned build date. Every derived file is then compared byte-for-byte with the
reference workspace. Exit status 0 means identical outputs.

    python scripts/verify_rederivation.py SNAPSHOT.tar.gz WORKDIR [--web] [--report out.json]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def derived(root: Path, web: bool) -> dict[str, str]:
    files = sorted(root.glob("varieties/*/generated/*.csv")) + sorted((root / "output/aggregate").glob("*"))
    if web:
        files += sorted(p for p in (root / "web/data").rglob("*") if p.is_file())
    return {p.relative_to(root).as_posix(): sha(p) for p in files if p.is_file()}


def run(cmd: list[str], cwd: Path, env: dict, log: Path) -> float:
    start = time.time()
    with log.open("a") as handle:
        handle.write(f"$ {' '.join(cmd)}\n")
        handle.flush()
        subprocess.run(cmd, cwd=cwd, env=env, stdout=handle, stderr=subprocess.STDOUT, check=True)
    return round(time.time() - start, 1)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("snapshot", type=Path)
    ap.add_argument("workdir", type=Path)
    ap.add_argument("--reference", type=Path, default=ROOT)
    ap.add_argument("--ref", default="HEAD", help="git revision to export (default HEAD)")
    ap.add_argument("--web", action="store_true",
                    help="Also rebuild and compare all site data (lexical, concept rows, colexification, communities)")
    ap.add_argument("--build-date", default="2026-11-02")
    ap.add_argument("--report", type=Path)
    args = ap.parse_args(argv)

    from arcaverborum.snapshot import unpack

    work = args.workdir.resolve()
    work.mkdir(parents=True, exist_ok=False)
    archive = subprocess.run(["git", "-C", str(args.reference), "archive", args.ref], capture_output=True, check=True)
    tar_path = work.parent / (work.name + ".git-archive.tar")
    tar_path.write_bytes(archive.stdout)
    with tarfile.open(tar_path) as tar:
        tar.extractall(work, filter="data")
    tar_path.unlink()
    manifest = unpack(args.snapshot, work)
    shutil.rmtree(work / "web" / "data", ignore_errors=True)  # generated; never an input

    env = dict(os.environ, PYTHONPATH=str(work / "src"), ARCA_BUILD_DATE=args.build_date,
               http_proxy="http://127.0.0.1:9", https_proxy="http://127.0.0.1:9",
               HTTP_PROXY="http://127.0.0.1:9", HTTPS_PROXY="http://127.0.0.1:9", no_proxy="")
    log = work.parent / (work.name + ".log")
    timings = {}
    timings["update"] = run([sys.executable, "build.py", "update", "--all"], work, env, log)
    timings["aggregate"] = run([sys.executable, "build.py", "aggregate"], work, env, log)
    if args.web:
        timings["web"] = run([sys.executable, "scripts/build_research_web.py", "--root", str(work),
                              "--with-communities"], work, env, log)

    ref = derived(args.reference.resolve(), args.web)
    new = derived(work, args.web)
    missing = sorted(set(ref) - set(new))
    extra = sorted(set(new) - set(ref))
    differ = sorted(k for k in set(ref) & set(new) if ref[k] != new[k])
    report = dict(snapshot=str(args.snapshot), snapshot_git_commit=manifest.get("git_commit"),
                  exported_ref=args.ref, compared_files=len(ref), identical=len(ref) - len(missing) - len(differ),
                  missing=missing[:50], extra=extra[:50], differ=differ[:50],
                  n_missing=len(missing), n_extra=len(extra), n_differ=len(differ), timings_seconds=timings,
                  ok=not (missing or extra or differ))
    text = json.dumps(report, indent=1)
    print(text)
    if args.report:
        args.report.write_text(text + "\n")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())

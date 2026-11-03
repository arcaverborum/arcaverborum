#!/usr/bin/env python3
"""Generate .github/CODEOWNERS from editors.csv (and check it in CI).

Scopes (semicolon-separated in the ``scope`` column):

  maintainer            owns everything not owned more specifically, plus
                        editors.csv and .github/
  family:<code>         every variety whose av_id starts with ``<code>-``
                        (the top-level Glottolog family code)
  variety:<av_id>       one construction; family editors of the same
                        family are requested too
  layer:concepts | layer:colexification | layer:pipeline

GitHub applies the *last* matching rule, so rules go from general to
specific. Usage: ``python scripts/codeowners.py [--check]``.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAYERS = {
    "pipeline": ["/src/", "/build.py", "/explore.py", "/scripts/", "/tests/", "/pyproject.toml",
                 "/requirements.lock"],
    "concepts": ["/src/arcaverborum/data/concepts.csv", "/src/arcaverborum/data/concept_*.csv",
                 "/src/arcaverborum/data/concepticon_*.csv", "/src/arcaverborum/data/semantic_field_codes.csv",
                 "/src/arcaverborum/data/wordnet/"],
    "colexification": ["/src/arcaverborum/data/colexification/", "/src/arcaverborum/colexification*.py",
                       "/scripts/*colexification*.py"],
}
AV_ID = re.compile(r"^[a-z0-9]{3}-[a-z0-9-]+$")
FAMILY = re.compile(r"^[a-z0-9]{3}$")


def load(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        if not row.get("github_login") or not row.get("name"):
            raise SystemExit(f"editors.csv: login and name are required: {row}")
    return rows


def generate(rows: list[dict], varieties: Path) -> str:
    maintainers, families, variety_owners, layers = [], defaultdict(list), defaultdict(list), defaultdict(list)
    for row in rows:
        login = "@" + row["github_login"].strip().lstrip("@")
        for scope in filter(None, (s.strip() for s in row["scope"].split(";"))):
            kind, _, value = scope.partition(":")
            if scope == "maintainer":
                maintainers.append(login)
            elif kind == "family" and FAMILY.match(value):
                families[value].append(login)
            elif kind == "variety" and AV_ID.match(value):
                if not (varieties / value / "config.yaml").exists():
                    raise SystemExit(f"editors.csv: unknown variety {value!r}")
                variety_owners[value].append(login)
            elif kind == "layer" and value in LAYERS:
                layers[value].append(login)
            else:
                raise SystemExit(f"editors.csv: bad scope {scope!r} for {login}")
    if not maintainers:
        raise SystemExit("editors.csv: at least one maintainer is required")
    lines = ["# Generated from editors.csv by scripts/codeowners.py; do not edit by hand.",
             "# GitHub applies the last matching rule.", "", "* " + " ".join(maintainers), ""]
    for layer in sorted(layers):
        owners = " ".join(sorted(set(layers[layer] + maintainers)))
        lines += [f"{pattern} {owners}" for pattern in LAYERS[layer]]
    for family in sorted(families):
        lines.append(f"/varieties/{family}-*/ " + " ".join(sorted(set(families[family]))))
    for av in sorted(variety_owners):
        owners = set(variety_owners[av]) | set(families.get(av[:3], []))
        lines.append(f"/varieties/{av}/ " + " ".join(sorted(owners)))
    if lines[-1] != "":
        lines.append("")
    lines += ["# Governance files stay with the maintainer.",
              "/editors.csv " + " ".join(maintainers), "/.github/ " + " ".join(maintainers), ""]
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="Fail if .github/CODEOWNERS is out of date")
    args = ap.parse_args(argv)
    text = generate(load(ROOT / "editors.csv"), ROOT / "varieties")
    target = ROOT / ".github" / "CODEOWNERS"
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != text:
            print("CODEOWNERS is out of date; run python scripts/codeowners.py", file=sys.stderr)
            return 1
        return 0
    target.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())

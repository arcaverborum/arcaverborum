"""Copy whole intake groups into slices/lexibank/ for a pull request (maintainer workspace).

    python scripts/add_slices.py cofa1242/idssegmented paez1247/idssegmented ...

Each argument is ``<glottocode>/<dataset>``. Run it on a workspace with the full
intake; see slices/README.md.
"""

import sys
from pathlib import Path

from arcaverborum.slices import export_groups, validate

ROOT = Path(__file__).resolve().parents[1]


def main(args: list[str]) -> int:
    groups = [tuple(a.split("/", 1)) for a in args]
    if not groups or any(len(g) != 2 for g in groups):
        print(__doc__)
        return 2
    print(export_groups(ROOT, groups))
    problems = validate(ROOT)
    for p in problems:
        print("ERROR", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

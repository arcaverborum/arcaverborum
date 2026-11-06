"""Guard Kunza's IDS forms as written-only (kuc-kunza, NEXT fidelity item).

IDS contribution 308 (Lehnert Santander) gives Kunza in the 19th-century
spellings of its historical sources and supplies no transcription column: the
plain ``ids`` rows have empty Segments. The ``idssegmented`` rows the
construction reads carry segments derived by Lexibank's tokenization of those
spellings (e.g. ``hoyri`` -> ``h o y/j r i``, ``quis-ti`` -> ``q u i s + t i``),
which the build labelled as source transcriptions. This writes guarded
``orthographic_only`` overrides for every idssegmented Kunza row, keeping the
spelling, source IDs, concepts and cognacy unchanged.

Usage: python scripts/kunza_written.py [--write]
"""

from __future__ import annotations

import argparse
import csv
import io
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from arcaverborum.supplements import evidence_hash  # noqa: E402

AV_ID = "kuc-kunza"
NOTE = (
    "Written-only: IDS 308 (Lehnert Santander) gives 19th-century source spellings with no "
    "transcription (plain ids rows have empty Segments); idssegmented segments are a Lexibank "
    "tokenization of the spelling, not a supplied reading. Guarded evidence; spelling retained."
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    uri = (ROOT / "intake/intake.sqlite").resolve().as_uri() + "?mode=ro"
    with sqlite3.connect(uri, uri=True) as db:
        db.row_factory = sqlite3.Row
        rows = [dict(r) for r in db.execute(
            "SELECT * FROM forms WHERE gc_lc='kunz1244' AND Dataset='idssegmented' ORDER BY seq")]
        plain = db.execute(
            "SELECT count(*), sum(Segments != '') FROM forms WHERE gc_lc='kunz1244' AND Dataset='ids'"
        ).fetchone()
    if not rows or plain[0] != len(rows) or plain[1]:
        raise SystemExit(f"unexpected intake: {len(rows)} idssegmented, ids {tuple(plain)}")
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=["source_form_id", "expected_evidence_sha256",
                                             "transcription_policy", "notes"], lineterminator="\n")
    writer.writeheader()
    writer.writerows({"source_form_id": r["ID"], "expected_evidence_sha256": evidence_hash(r),
                      "transcription_policy": "orthographic_only", "notes": NOTE} for r in rows)
    path = ROOT / "varieties" / AV_ID / "custom" / "transcriptions.csv"
    print(f"{len(rows)} rows")
    if args.write:
        path.parent.mkdir(exist_ok=True)
        path.write_text(out.getvalue(), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

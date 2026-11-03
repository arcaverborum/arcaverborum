"""Build-time facts that must be reproducible.

Published artefacts never read the wall clock directly. A release sets
``ARCA_BUILD_DATE`` (ISO date, normally the date in the release identifier);
``SOURCE_DATE_EPOCH`` is honoured as the reproducible-builds convention.
Only unpinned local work falls back to today's date.
"""

from __future__ import annotations

import os
from datetime import date, datetime, timezone


def build_date() -> str:
    """ISO date to stamp into published artefacts."""
    explicit = os.environ.get("ARCA_BUILD_DATE", "").strip()
    if explicit:
        return date.fromisoformat(explicit).isoformat()
    epoch = os.environ.get("SOURCE_DATE_EPOCH", "").strip()
    if epoch:
        return datetime.fromtimestamp(int(epoch), tz=timezone.utc).date().isoformat()
    return date.today().isoformat()

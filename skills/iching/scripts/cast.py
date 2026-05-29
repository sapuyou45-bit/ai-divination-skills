#!/usr/bin/env python3
"""Compatibility wrapper for the packaged I Ching CLI."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from ai_divination_skills.iching import main
except ImportError:
    from _standalone_iching import main


if __name__ == "__main__":
    raise SystemExit(main())

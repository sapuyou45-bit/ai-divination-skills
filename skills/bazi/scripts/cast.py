#!/usr/bin/env python3
"""Compatibility wrapper for the packaged Bazi (八字 / Four Pillars) CLI."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from ai_divination_skills.bazi import main
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _standalone_bazi import main


if __name__ == "__main__":
    raise SystemExit(main())

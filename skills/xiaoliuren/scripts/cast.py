#!/usr/bin/env python3
"""Compatibility wrapper for the packaged Xiao Liu Ren CLI."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from ai_divination_skills.xiaoliuren import main


if __name__ == "__main__":
    raise SystemExit(main())

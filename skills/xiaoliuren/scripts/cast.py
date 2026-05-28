#!/usr/bin/env python3
"""Cast Xiao Liu Ren as JSON for AI agent interpretation."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from typing import Any


POSITIONS = [
    {
        "index": 1,
        "name_pinyin": "Da An",
        "name_en": "Great Peace",
        "keywords": ["stable", "slow", "safe", "settled"],
    },
    {
        "index": 2,
        "name_pinyin": "Liu Lian",
        "name_en": "Lingering Delay",
        "keywords": ["delay", "entanglement", "waiting", "unclear"],
    },
    {
        "index": 3,
        "name_pinyin": "Su Xi",
        "name_en": "Swift Joy",
        "keywords": ["quick news", "opening", "pleasant movement", "timely help"],
    },
    {
        "index": 4,
        "name_pinyin": "Chi Kou",
        "name_en": "Red Mouth",
        "keywords": ["conflict", "argument", "friction", "caution with speech"],
    },
    {
        "index": 5,
        "name_pinyin": "Xiao Ji",
        "name_en": "Small Fortune",
        "keywords": ["modest gain", "small help", "manageable progress", "partial success"],
    },
    {
        "index": 6,
        "name_pinyin": "Kong Wang",
        "name_en": "Empty Void",
        "keywords": ["absence", "uncertainty", "pause", "low traction"],
    },
]


def chinese_hour_index(dt: datetime) -> int:
    hour = dt.hour
    if hour == 23 or hour == 0:
        return 1
    return ((hour + 1) // 2) + 1


def position_for(month: int, day: int, hour: int) -> dict[str, Any]:
    for label, value, lower, upper in [("month", month, 1, 12), ("day", day, 1, 30), ("hour", hour, 1, 12)]:
        if value < lower or value > upper:
            raise ValueError(f"{label} must be between {lower} and {upper}")
    index = ((month + day + hour - 2) % 6) + 1
    return POSITIONS[index - 1]


def cast_numbers(month: int, day: int, hour: int) -> dict[str, Any]:
    position = position_for(month, day, hour)
    return {
        "system": "xiaoliuren",
        "method": "numbers",
        "inputs": {"month": month, "day": day, "hour": hour},
        "formula": "((month + day + hour - 2) % 6) + 1",
        "position": position,
    }


def cast_time(raw_datetime: str | None) -> dict[str, Any]:
    dt = datetime.fromisoformat(raw_datetime) if raw_datetime else datetime.now()
    month = dt.month
    day = min(dt.day, 30)
    hour = chinese_hour_index(dt)
    result = cast_numbers(month, day, hour)
    result["method"] = "time"
    result["datetime"] = dt.isoformat(timespec="seconds")
    result["calendar_note"] = "Uses Gregorian month/day as a lightweight fallback. For traditional lunar casting, pass lunar numbers with --method numbers."
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Cast Xiao Liu Ren for AI agent interpretation.")
    parser.add_argument("--method", choices=["numbers", "time"], default="time")
    parser.add_argument("--month", type=int, help="Lunar month number, 1-12, for --method numbers.")
    parser.add_argument("--day", type=int, help="Lunar day number, 1-30, for --method numbers.")
    parser.add_argument("--hour", type=int, help="Chinese hour branch index, 1-12, for --method numbers.")
    parser.add_argument("--datetime", help="ISO datetime for time fallback, for example 2026-05-29T14:30:00.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.method == "numbers":
        missing = [name for name in ["month", "day", "hour"] if getattr(args, name) is None]
        if missing:
            raise SystemExit(f"Missing required arguments for --method numbers: {', '.join('--' + name for name in missing)}")
        result = cast_numbers(args.month, args.day, args.hour)
    else:
        result = cast_time(args.datetime)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

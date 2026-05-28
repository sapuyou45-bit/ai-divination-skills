#!/usr/bin/env python3
"""Cast an I Ching hexagram as JSON for AI agent interpretation."""

from __future__ import annotations

import argparse
import json
import random
from typing import Any


TRIGRAM_BITS = {
    "Heaven": "111",
    "Lake": "110",
    "Fire": "101",
    "Thunder": "100",
    "Wind": "011",
    "Water": "010",
    "Mountain": "001",
    "Earth": "000",
}

HEXAGRAMS = {
    ("Heaven", "Heaven"): (1, "Qian / The Creative"),
    ("Earth", "Earth"): (2, "Kun / The Receptive"),
    ("Water", "Thunder"): (3, "Zhun / Difficulty at the Beginning"),
    ("Mountain", "Water"): (4, "Meng / Youthful Folly"),
    ("Water", "Heaven"): (5, "Xu / Waiting"),
    ("Heaven", "Water"): (6, "Song / Conflict"),
    ("Earth", "Water"): (7, "Shi / The Army"),
    ("Water", "Earth"): (8, "Bi / Holding Together"),
    ("Wind", "Heaven"): (9, "Xiao Chu / Small Taming"),
    ("Heaven", "Lake"): (10, "Lu / Treading"),
    ("Earth", "Heaven"): (11, "Tai / Peace"),
    ("Heaven", "Earth"): (12, "Pi / Standstill"),
    ("Heaven", "Fire"): (13, "Tong Ren / Fellowship"),
    ("Fire", "Heaven"): (14, "Da You / Great Possession"),
    ("Earth", "Mountain"): (15, "Qian / Modesty"),
    ("Thunder", "Earth"): (16, "Yu / Enthusiasm"),
    ("Lake", "Thunder"): (17, "Sui / Following"),
    ("Mountain", "Wind"): (18, "Gu / Work on the Decayed"),
    ("Earth", "Lake"): (19, "Lin / Approach"),
    ("Wind", "Earth"): (20, "Guan / Contemplation"),
    ("Fire", "Thunder"): (21, "Shi He / Biting Through"),
    ("Mountain", "Fire"): (22, "Bi / Grace"),
    ("Mountain", "Earth"): (23, "Bo / Splitting Apart"),
    ("Earth", "Thunder"): (24, "Fu / Return"),
    ("Heaven", "Thunder"): (25, "Wu Wang / Innocence"),
    ("Mountain", "Heaven"): (26, "Da Chu / Great Taming"),
    ("Mountain", "Thunder"): (27, "Yi / Nourishment"),
    ("Lake", "Wind"): (28, "Da Guo / Great Preponderance"),
    ("Water", "Water"): (29, "Kan / The Abysmal"),
    ("Fire", "Fire"): (30, "Li / The Clinging"),
    ("Lake", "Mountain"): (31, "Xian / Influence"),
    ("Thunder", "Wind"): (32, "Heng / Duration"),
    ("Heaven", "Mountain"): (33, "Dun / Retreat"),
    ("Thunder", "Heaven"): (34, "Da Zhuang / Great Power"),
    ("Fire", "Earth"): (35, "Jin / Progress"),
    ("Earth", "Fire"): (36, "Ming Yi / Darkening of the Light"),
    ("Wind", "Fire"): (37, "Jia Ren / The Family"),
    ("Fire", "Lake"): (38, "Kui / Opposition"),
    ("Water", "Mountain"): (39, "Jian / Obstruction"),
    ("Thunder", "Water"): (40, "Jie / Deliverance"),
    ("Mountain", "Lake"): (41, "Sun / Decrease"),
    ("Wind", "Thunder"): (42, "Yi / Increase"),
    ("Lake", "Heaven"): (43, "Guai / Breakthrough"),
    ("Heaven", "Wind"): (44, "Gou / Coming to Meet"),
    ("Lake", "Earth"): (45, "Cui / Gathering Together"),
    ("Earth", "Wind"): (46, "Sheng / Pushing Upward"),
    ("Lake", "Water"): (47, "Kun / Oppression"),
    ("Water", "Wind"): (48, "Jing / The Well"),
    ("Lake", "Fire"): (49, "Ge / Revolution"),
    ("Fire", "Wind"): (50, "Ding / The Cauldron"),
    ("Thunder", "Thunder"): (51, "Zhen / The Arousing"),
    ("Mountain", "Mountain"): (52, "Gen / Keeping Still"),
    ("Wind", "Mountain"): (53, "Jian / Development"),
    ("Thunder", "Lake"): (54, "Gui Mei / Marrying Maiden"),
    ("Thunder", "Fire"): (55, "Feng / Abundance"),
    ("Fire", "Mountain"): (56, "Lu / The Wanderer"),
    ("Wind", "Wind"): (57, "Xun / The Gentle"),
    ("Lake", "Lake"): (58, "Dui / The Joyous"),
    ("Wind", "Water"): (59, "Huan / Dispersion"),
    ("Water", "Lake"): (60, "Jie / Limitation"),
    ("Wind", "Lake"): (61, "Zhong Fu / Inner Truth"),
    ("Thunder", "Mountain"): (62, "Xiao Guo / Small Preponderance"),
    ("Water", "Fire"): (63, "Ji Ji / After Completion"),
    ("Fire", "Water"): (64, "Wei Ji / Before Completion"),
}

TRIGRAM_BY_BITS = {bits: name for name, bits in TRIGRAM_BITS.items()}
HEXAGRAM_BY_BINARY = {
    TRIGRAM_BITS[lower] + TRIGRAM_BITS[upper]: {"number": number, "name": name, "upper": upper, "lower": lower}
    for (upper, lower), (number, name) in HEXAGRAMS.items()
}


def make_rng(seed: str | None) -> random.Random | random.SystemRandom:
    if seed is not None:
        return random.Random(seed)
    return random.SystemRandom()


def coin_line(rng: random.Random | random.SystemRandom) -> int:
    return sum(rng.choice([2, 3]) for _ in range(3))


def parse_manual_lines(raw: str) -> list[int]:
    values = [int(part.strip()) for part in raw.split(",") if part.strip()]
    if len(values) != 6:
        raise ValueError("--lines must contain exactly six comma-separated values")
    if any(value not in [6, 7, 8, 9] for value in values):
        raise ValueError("line values must be 6, 7, 8, or 9")
    return values


def line_record(index: int, value: int) -> dict[str, Any]:
    labels = {
        6: ("old yin", "yin", True),
        7: ("young yang", "yang", False),
        8: ("young yin", "yin", False),
        9: ("old yang", "yang", True),
    }
    line_type, polarity, changing = labels[value]
    return {
        "line": index,
        "value": value,
        "type": line_type,
        "polarity": polarity,
        "changing": changing,
    }


def hexagram_for_binary(binary: str) -> dict[str, Any]:
    data = HEXAGRAM_BY_BINARY[binary]
    return {
        "number": data["number"],
        "name": data["name"],
        "binary": binary,
        "upper_trigram": data["upper"],
        "lower_trigram": data["lower"],
    }


def cast(method: str, seed: str | None, manual_lines: str | None) -> dict[str, Any]:
    if method == "manual":
        if not manual_lines:
            raise ValueError("--lines is required for manual casts")
        values = parse_manual_lines(manual_lines)
        randomness = "manual"
    else:
        rng = make_rng(seed)
        values = [coin_line(rng) for _ in range(6)]
        randomness = "seeded" if seed is not None else "system"

    primary_bits = "".join("1" if value in [7, 9] else "0" for value in values)
    resulting_bits = "".join(
        "0" if value == 9 else "1" if value == 6 else "1" if value == 7 else "0"
        for value in values
    )
    lines = [line_record(index, value) for index, value in enumerate(values, start=1)]
    changing_lines = [line["line"] for line in lines if line["changing"]]

    return {
        "system": "iching",
        "method": method,
        "randomness": randomness,
        "line_order": "bottom-to-top",
        "lines": lines,
        "changing_lines": changing_lines,
        "primary_hexagram": hexagram_for_binary(primary_bits),
        "resulting_hexagram": hexagram_for_binary(resulting_bits),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Cast an I Ching hexagram for AI agent interpretation.")
    parser.add_argument("--method", choices=["random", "coins", "manual"], default="coins")
    parser.add_argument("--seed", help="Optional deterministic seed for tests and reproducible demos.")
    parser.add_argument("--lines", help="Manual bottom-to-top line values, for example: 6,7,8,9,7,8")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = cast(args.method, args.seed, args.lines)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

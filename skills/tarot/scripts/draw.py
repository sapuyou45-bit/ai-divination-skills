#!/usr/bin/env python3
"""Draw tarot cards as JSON for AI agent interpretation."""

from __future__ import annotations

import argparse
import json
import random
from typing import Any


MAJOR_ARCANA = [
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgement",
    "The World",
]

SUITS = ["Wands", "Cups", "Swords", "Pentacles"]
RANKS = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]

SPREADS = {
    "single": ["Focus"],
    "three-card": ["Situation", "Obstacle", "Guidance"],
    "decision": ["Option A", "Option B", "Hidden factor", "Advice"],
    "creative": ["Character", "Conflict", "Turn"],
    "project": ["Current system", "Technical debt", "Next step"],
}


def build_deck(deck_name: str) -> list[dict[str, str]]:
    major = [{"name": name, "arcana": "major", "suit": ""} for name in MAJOR_ARCANA]
    if deck_name == "major":
        return major

    minor = [
        {"name": f"{rank} of {suit}", "arcana": "minor", "suit": suit}
        for suit in SUITS
        for rank in RANKS
    ]
    return major + minor


def make_rng(seed: str | None) -> random.Random | random.SystemRandom:
    if seed is not None:
        return random.Random(seed)
    return random.SystemRandom()


def draw(deck_name: str, spread_name: str, reversals: bool, seed: str | None) -> dict[str, Any]:
    positions = SPREADS[spread_name]
    deck = build_deck(deck_name)
    if len(positions) > len(deck):
        raise ValueError("spread has more positions than available cards")

    rng = make_rng(seed)
    selected = rng.sample(deck, len(positions))
    cards = []
    for position, card in zip(positions, selected):
        reversed_card = bool(rng.choice([False, True])) if reversals else False
        cards.append(
            {
                "position": position,
                "name": card["name"],
                "arcana": card["arcana"],
                "suit": card["suit"],
                "reversed": reversed_card,
                "orientation": "reversed" if reversed_card else "upright",
            }
        )

    return {
        "system": "tarot",
        "deck": deck_name,
        "spread": spread_name,
        "randomness": "seeded" if seed is not None else "system",
        "reversals_enabled": reversals,
        "cards": cards,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Draw tarot cards for AI agent interpretation.")
    parser.add_argument("--deck", choices=["major", "full"], default="major")
    parser.add_argument("--spread", choices=sorted(SPREADS), default="single")
    parser.add_argument("--reversals", action="store_true")
    parser.add_argument("--seed", help="Optional deterministic seed for tests and reproducible demos.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = draw(args.deck, args.spread, args.reversals, args.seed)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

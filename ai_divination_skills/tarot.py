"""Tarot draw logic for package and CLI use."""

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
    major = [{"name": name, "arcana": "major", "suit": "", "index": str(index)} for index, name in enumerate(MAJOR_ARCANA)]
    if deck_name == "major":
        return major

    minor = [
        {"name": f"{rank} of {suit}", "arcana": "minor", "suit": suit, "index": str(22 + suit_index * len(RANKS) + rank_index)}
        for suit_index, suit in enumerate(SUITS)
        for rank_index, rank in enumerate(RANKS)
    ]
    return major + minor


def make_rng(seed: str | None) -> random.Random | random.SystemRandom:
    if seed is not None:
        return random.Random(seed)
    return random.SystemRandom()


def fisher_yates_shuffle(deck: list[dict[str, str]], rng: random.Random | random.SystemRandom) -> list[dict[str, str]]:
    shuffled = list(deck)
    for index in range(len(shuffled) - 1, 0, -1):
        swap_index = rng.randrange(index + 1)
        shuffled[index], shuffled[swap_index] = shuffled[swap_index], shuffled[index]
    return shuffled


def draw(deck_name: str, spread_name: str, reversals: bool, seed: str | None) -> dict[str, Any]:
    positions = SPREADS[spread_name]
    deck = build_deck(deck_name)
    if len(positions) > len(deck):
        raise ValueError("spread has more positions than available cards")

    rng = make_rng(seed)
    shuffled = fisher_yates_shuffle(deck, rng)
    selected = shuffled[: len(positions)]
    cards = []
    for position, card in zip(positions, selected):
        reversed_card = bool(rng.choice([False, True])) if reversals else False
        cards.append(
            {
                "position": position,
                "name": card["name"],
                "index": int(card["index"]),
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
        "deck_size": len(deck),
        "draw_count": len(selected),
        "drawn_indices": [int(card["index"]) for card in selected],
        "shuffle_algorithm": "fisher-yates",
        "rng_mode": "seeded-demo" if seed is not None else "system",
        "randomness": "seeded" if seed is not None else "system",
        "reversals_enabled": reversals,
        "cards": cards,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Draw tarot cards for AI agent interpretation.")
    parser.add_argument("--deck", choices=["major", "full"], default="major")
    parser.add_argument("--spread", choices=sorted(SPREADS), default="single")
    parser.add_argument("--reversals", action="store_true")
    parser.add_argument("--seed", help="Optional deterministic seed for tests and reproducible demos.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    result = draw(args.deck, args.spread, args.reversals, args.seed)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0

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

MAJOR_MEANINGS = {
    "The Fool": {
        "upright": [
            "beginning",
            "risk",
            "openness"
        ],
        "shadow": "naivety",
        "question": "What can start small?"
    },
    "The Magician": {
        "upright": [
            "agency",
            "tools",
            "focus"
        ],
        "shadow": "manipulation",
        "question": "What resources are already available?"
    },
    "The High Priestess": {
        "upright": [
            "intuition",
            "hidden knowledge"
        ],
        "shadow": "passivity",
        "question": "What is known but not yet said?"
    },
    "The Empress": {
        "upright": [
            "growth",
            "care",
            "creation"
        ],
        "shadow": "overindulgence",
        "question": "What needs nurturing?"
    },
    "The Emperor": {
        "upright": [
            "structure",
            "authority",
            "boundaries"
        ],
        "shadow": "rigidity",
        "question": "What needs clearer rules?"
    },
    "The Hierophant": {
        "upright": [
            "tradition",
            "teaching",
            "institutions"
        ],
        "shadow": "conformity",
        "question": "Which convention helps or limits this?"
    },
    "The Lovers": {
        "upright": [
            "alignment",
            "choice",
            "values"
        ],
        "shadow": "divided motives",
        "question": "What choice reveals the real value?"
    },
    "The Chariot": {
        "upright": [
            "direction",
            "discipline",
            "momentum"
        ],
        "shadow": "forcefulness",
        "question": "What needs coordinated effort?"
    },
    "Strength": {
        "upright": [
            "patience",
            "courage",
            "restraint"
        ],
        "shadow": "suppression",
        "question": "How can pressure be met gently?"
    },
    "The Hermit": {
        "upright": [
            "reflection",
            "study",
            "solitude"
        ],
        "shadow": "isolation",
        "question": "What needs quiet investigation?"
    },
    "Wheel of Fortune": {
        "upright": [
            "cycles",
            "timing",
            "change"
        ],
        "shadow": "helplessness",
        "question": "What is turning without permission?"
    },
    "Justice": {
        "upright": [
            "fairness",
            "evidence",
            "consequence"
        ],
        "shadow": "cold judgment",
        "question": "What would be balanced and accountable?"
    },
    "The Hanged Man": {
        "upright": [
            "pause",
            "reversal",
            "surrender"
        ],
        "shadow": "stagnation",
        "question": "What changes if the view is inverted?"
    },
    "Death": {
        "upright": [
            "ending",
            "transition",
            "release"
        ],
        "shadow": "clinging",
        "question": "What needs to end cleanly?"
    },
    "Temperance": {
        "upright": [
            "integration",
            "pacing",
            "repair"
        ],
        "shadow": "dilution",
        "question": "What needs proportion?"
    },
    "The Devil": {
        "upright": [
            "attachment",
            "compulsion",
            "constraint"
        ],
        "shadow": "denial",
        "question": "What bargain has become a chain?"
    },
    "The Tower": {
        "upright": [
            "disruption",
            "truth",
            "collapse"
        ],
        "shadow": "avoidance",
        "question": "What unstable structure is being protected?"
    },
    "The Star": {
        "upright": [
            "hope",
            "renewal",
            "guidance"
        ],
        "shadow": "distance",
        "question": "What restores faith without fantasy?"
    },
    "The Moon": {
        "upright": [
            "uncertainty",
            "dreams",
            "distortion"
        ],
        "shadow": "confusion",
        "question": "What is unclear and needs testing?"
    },
    "The Sun": {
        "upright": [
            "clarity",
            "vitality",
            "success"
        ],
        "shadow": "overexposure",
        "question": "What becomes simple in daylight?"
    },
    "Judgement": {
        "upright": [
            "reckoning",
            "calling",
            "review"
        ],
        "shadow": "self-condemnation",
        "question": "What is ready to be answered for?"
    },
    "The World": {
        "upright": [
            "completion",
            "integration",
            "arrival"
        ],
        "shadow": "closure anxiety",
        "question": "What cycle is complete?"
    }
}

SUIT_THEMES = {
    "Wands": [
        "energy",
        "initiative",
        "work",
        "ambition"
    ],
    "Cups": [
        "emotion",
        "relationship",
        "belonging",
        "desire"
    ],
    "Swords": [
        "thought",
        "conflict",
        "language",
        "decisions"
    ],
    "Pentacles": [
        "material reality",
        "money",
        "health routines",
        "craft"
    ]
}

RANK_THEMES = {
    "Ace": "seed",
    "Two": "choice or balance",
    "Three": "development",
    "Four": "stability or pause",
    "Five": "friction",
    "Six": "adjustment or return",
    "Seven": "challenge",
    "Eight": "effort or movement",
    "Nine": "culmination",
    "Ten": "completion or burden",
    "Page": "learner",
    "Knight": "active pursuit",
    "Queen": "mature receptivity",
    "King": "mature direction"
}


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


def card_meanings(card: dict[str, str], reversed_card: bool) -> dict[str, Any]:
    """Attach audited meaning data so the model interprets data, not memory."""
    if card["arcana"] == "major":
        data = MAJOR_MEANINGS[card["name"]]
        return {
            "keywords_upright": data["upright"],
            "shadow": data["shadow"],
            "question": data["question"],
            "reading_cue": data["shadow"] if reversed_card else ", ".join(data["upright"]),
        }
    rank = card["name"].split(" of ")[0]
    suit = card["suit"]
    return {
        "keywords_upright": [RANK_THEMES[rank]] + SUIT_THEMES[suit],
        "rank_theme": RANK_THEMES[rank],
        "suit_themes": SUIT_THEMES[suit],
        "reading_cue": f"{RANK_THEMES[rank]} (reversed: blocked or excess)" if reversed_card else RANK_THEMES[rank],
    }


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
                "meanings": card_meanings(card, reversed_card),
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

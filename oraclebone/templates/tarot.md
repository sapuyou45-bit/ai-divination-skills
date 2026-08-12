# Tarot Interpretation Template

Use this only after the tarot script has produced Input JSON.

## Input JSON To Cite

- `deck`
- `spread`
- `deck_size`
- `draw_count`
- `drawn_indices`
- `shuffle_algorithm`
- `rng_mode`
- each card's `position`, `name`, `arcana`, `suit`, and `orientation`

## Boundaries

- Do not invent extra cards, hidden cards, clarifiers, or deck imagery.
- Do not redraw because the cards feel too negative, too positive, or unclear.
- Do not treat seeded demo output as a real reading unless the user explicitly chose a reproducible demo.
- Do not use copyrighted deck art unless the user provides licensed assets.

## Suggested Response Shape

1. Restate the spread and the cards in their positions.
2. Explain each card through its position rather than as a generic meaning dump.
3. Connect repeated themes across positions.
4. Offer one or two practical next steps.
5. Mention method metadata, especially `shuffle_algorithm` and `rng_mode`, when auditability matters.

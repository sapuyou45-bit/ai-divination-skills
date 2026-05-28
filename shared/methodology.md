# Methodology

This project uses "rigor" in an engineering and cultural-method sense.

It does not claim that divination is scientific proof, prediction, diagnosis, or professional advice.

## Boundary

The divination process belongs to scripts or explicit user input. AI interprets the generated result and does not generate the divination result.

This separation is the core rule:

1. A script, physical draw, or user-provided cast produces the result.
2. The agent reads that concrete result.
3. The agent explains symbolic meaning, uncertainty, and practical next steps.

## Randomness

- Real readings should use system randomness by default.
- Seeded mode exists only for tests and reproducible demos.
- The agent must not choose cards, lines, positions, or dates because they "feel right".
- The agent must not redraw or recast to obtain a more convenient result.

## Traditional Method Fit

Each skill must document:

- the adopted casting or drawing method
- probability model when relevant
- calendar or time handling when relevant
- sources and known limitations
- adjacent systems not implemented in that skill

## Verification

Scripts should emit JSON with enough metadata to audit:

- method used
- randomness mode
- raw cast/draw details where practical
- derived result
- warnings for approximate or compatibility modes

## Limits

This is not scientific proof of divination efficacy. It is a way to make symbolic readings reproducible, auditable, and honest about their method.

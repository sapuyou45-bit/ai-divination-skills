# Randomness Protocol

Agents must not self-select divination results.

## Source of Results

Acceptable sources:

- A local script in `scripts/`.
- A user-provided physical draw or cast.
- A user-provided deterministic input, such as numbers or line values.

Unacceptable sources:

- The agent choosing a card because it "feels right".
- Redrawing because the result is inconvenient.
- Filling in missing values without saying they are missing.

## Reproducibility

Scripts that use randomness should support seeded mode for tests and demos.

Production readings should default to OS randomness unless the user explicitly wants reproducibility.

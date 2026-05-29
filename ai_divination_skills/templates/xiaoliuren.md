# Xiao Liu Ren Interpretation Template

Use this only after the Xiao Liu Ren script has produced Input JSON.

## Input JSON To Cite

- `method`
- `accuracy`
- `inputs`
- `formula`
- `position`
- `datetime`, when present
- `lunar_date`, when present
- `warning`, when present

## Boundaries

- Do not invent lunar dates, hour branches, or positions.
- Do not redraw or recast because the position feels too simple.
- Do not present `time` Gregorian fallback as a traditional lunar cast.
- Do not resolve leap lunar months for the user; ask for explicit `numbers` input instead.

## Suggested Response Shape

1. Restate the month, day, hour, and resulting position.
2. State whether the method is strict lunar input, lunar-time conversion, or Gregorian fallback.
3. Interpret the position's keywords in relation to the user's question.
4. Translate the reading into a small timing, communication, or action recommendation.
5. Repeat any warning if the method is approximate.

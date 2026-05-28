# I Ching Casting Methods

## coins

Default method. The script simulates three coins for each line.

Values:

- 6: old yin, changing
- 7: young yang
- 8: young yin
- 9: old yang, changing

The script generates six lines from bottom to top.

## random

Same line value space as `coins`, intended for simple randomized casts and seeded tests.

## manual

Use when the user provides line values from a physical or external cast.

Example:

```bash
python3 scripts/cast.py --method manual --lines 6,7,8,9,7,8
```

Never reorder user-provided lines unless the user clearly says they gave them top-to-bottom. If order is unclear, ask.

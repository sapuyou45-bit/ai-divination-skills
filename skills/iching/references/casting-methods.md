# I Ching Casting Methods

## coins

Default method. The script simulates three coins for each line.

Values:

- 6: old yin, changing
- 7: young yang
- 8: young yin
- 9: old yang, changing

The script generates six lines from bottom to top.

Probability:

- 6: 1/8
- 7: 3/8
- 8: 3/8
- 9: 1/8

Each output line includes the raw coin tosses and coin values.

## yarrow

Digital equivalent of the traditional yarrow-stalk probability model.

Probability:

- 6: 1/16
- 7: 5/16
- 8: 7/16
- 9: 3/16

This preserves the yarrow line distribution but does not simulate the physical stalk ritual.

## random

Compatibility alias for `coins`. Prefer explicit `coins` or `yarrow`.

## manual

Use when the user provides line values from a physical or external cast.

Example:

```bash
python3 scripts/cast.py --method manual --lines 6,7,8,9,7,8
```

Never reorder user-provided lines unless the user clearly says they gave them top-to-bottom. If order is unclear, ask.

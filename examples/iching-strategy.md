# I Ching Strategy Example

Prompt:

> Use I Ching to reflect on whether this is a good moment to push a strategic change.

Command:

```bash
python3 skills/iching/scripts/cast.py --method yarrow --seed strategy
```

Script result:

```json
{
  "system": "iching",
  "line_order": "bottom-to-top",
  "method": "yarrow",
  "line_probabilities": {"6": "1/16", "7": "5/16", "8": "7/16", "9": "3/16"},
  "changing_lines": [1, 2],
  "primary_hexagram": {
    "number": 34,
    "name": "Da Zhuang / Great Power",
    "binary": "111100",
    "upper_trigram": "Thunder",
    "lower_trigram": "Heaven"
  },
  "resulting_hexagram": {
    "number": 62,
    "name": "Xiao Guo / Small Preponderance",
    "binary": "001100"
  }
}
```

Reading shape:

1. Result: Hexagram 34, Great Power, changing lines 1 and 2, moving to Hexagram 62, Small Preponderance.
2. Symbolic Reading: The situation has force, but the changing early lines warn against pushing before the base is disciplined.
3. Situation Mapping: A strategic change may have energy behind it, but the path narrows toward careful, modest execution.
4. Hidden Variables: Power at the start can become overreach if small constraints are ignored.
5. Actionable Guidance: Start with a contained pilot, define limits, and treat details as the main risk surface.
6. Boundaries: This frames strategic posture; it does not decide the strategy or guarantee adoption.

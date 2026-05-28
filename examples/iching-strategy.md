# I Ching Strategy Example

Prompt:

> Use I Ching to reflect on whether this is a good moment to push a strategic change.

Command:

```bash
python3 skills/iching/scripts/cast.py --method random --seed strategy
```

Script result:

```json
{
  "system": "iching",
  "line_order": "bottom-to-top",
  "changing_lines": [],
  "primary_hexagram": {
    "number": 47,
    "name": "Kun / Oppression",
    "binary": "010110",
    "upper_trigram": "Lake",
    "lower_trigram": "Water"
  },
  "resulting_hexagram": {
    "number": 47,
    "name": "Kun / Oppression",
    "binary": "010110"
  }
}
```

Reading shape:

1. Result: Hexagram 47, Oppression, with no changing lines.
2. Symbolic Reading: The situation is constrained and may not respond to direct pressure.
3. Situation Mapping: A strategic change can still be right, but the current container may lack resources, consent, or timing.
4. Hidden Variables: Exhaustion and bottlenecks may matter more than the idea itself.
5. Actionable Guidance: Reduce load first. Identify one constraint that can be removed before asking people to move.
6. Boundaries: This does not decide the strategy. It frames the condition under which the strategy is being attempted.

# Tarot Decision Example

Prompt:

> Use tarot to compare whether I should keep the current project scope or cut it down for the first release.

Command:

```bash
python3 skills/tarot/scripts/draw.py --deck major --spread decision --seed demo --reversals
```

Script result:

```json
{
  "system": "tarot",
  "deck": "major",
  "spread": "decision",
  "cards": [
    {"position": "Option A", "name": "The World", "orientation": "upright"},
    {"position": "Option B", "name": "The Devil", "orientation": "upright"},
    {"position": "Hidden factor", "name": "Wheel of Fortune", "orientation": "upright"},
    {"position": "Advice", "name": "The Tower", "orientation": "reversed"}
  ]
}
```

Reading shape:

1. Result: The World, The Devil, Wheel of Fortune, The Tower reversed.
2. Symbolic Reading: The current scope looks complete, but may also carry attachment and inertia.
3. Situation Mapping: Option A may preserve the whole vision. Option B may reveal which parts are dependency traps.
4. Hidden Variables: Timing is changing. The decision may be less about preference and more about release conditions.
5. Actionable Guidance: Run a scope audit and mark what can ship, what must wait, and what only feels essential.
6. Boundaries: This is a release-planning reflection, not a guarantee of market response.

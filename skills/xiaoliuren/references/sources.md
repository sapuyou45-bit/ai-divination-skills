# Xiao Liu Ren Sources and Method Choices

## Adopted

- `numbers` is the strictest method: the user provides lunar month, lunar day, and Chinese hour index.
- `lunar-time` converts Gregorian datetime to Chinese lunar date with optional `lunar_python`.
- `time` is retained as a Gregorian fallback for rough demos only.
- Leap lunar months are rejected by default; the user should provide explicit `numbers` input to avoid false precision.
- The AI interprets the computed position and does not choose a position.

Primary references:

- lunar-python calendar library: https://github.com/6tail/lunar-python
- lunar-python conversion examples: https://deepwiki.com/6tail/lunar-python/6-examples-and-usage

## Not adopted

- Automatic leap-month interpretation is not implemented.
- Almanac day-selection rules are not implemented.
- Broader Liu Ren systems are not implemented in this lightweight skill.

## Notes

Traditional accuracy depends on correct lunar date and hour input. When that information is uncertain, prefer `--method numbers` with user-confirmed values.

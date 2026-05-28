# Xiao Liu Ren Inputs

Traditional Xiao Liu Ren commonly uses:

- Lunar month number: 1-12.
- Lunar day number: 1-30.
- Chinese hour branch index: 1-12.

The MVP script does not calculate the Chinese lunar calendar. For traditional accuracy, ask the user for lunar numbers or use an external lunar calendar before running `--method numbers`.

The `--method time` fallback uses Gregorian month/day. If the Gregorian day is 31, the script clamps it to 30 so the value stays inside the lunar day input range.

## Hour Index

| Index | Branch | Time |
|---:|---|---|
| 1 | Zi | 23:00-01:00 |
| 2 | Chou | 01:00-03:00 |
| 3 | Yin | 03:00-05:00 |
| 4 | Mao | 05:00-07:00 |
| 5 | Chen | 07:00-09:00 |
| 6 | Si | 09:00-11:00 |
| 7 | Wu | 11:00-13:00 |
| 8 | Wei | 13:00-15:00 |
| 9 | Shen | 15:00-17:00 |
| 10 | You | 17:00-19:00 |
| 11 | Xu | 19:00-21:00 |
| 12 | Hai | 21:00-23:00 |

## Formula

The script uses:

```text
((month + day + hour - 2) % 6) + 1
```

The result maps to the six positions in `positions.md`.

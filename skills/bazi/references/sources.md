# Sources and Engine Notes

## Engine

The bazi script wraps the [`lunar-python`](https://github.com/6tail/lunar-python) library, which implements the classical solar-term-aware lunar calendar in pure Python.

## Why an engine, not a hand calculation

Bazi requires solar terms (节气) for month-pillar boundaries and a sexagenary day count anchored on historical reference days. Hand-coding these is error-prone; pinning to a maintained library makes the chart reproducible and auditable.

## Adopted

- Classical Four Pillars structure: 年柱 / 月柱 / 日柱 / 时柱, each = 天干 + 地支.
- Heavenly Stem and Earthly Branch tables with element (五行) and yin/yang polarity.
- NaYin (纳音) per pillar from the classical 60 jiazi mapping.
- Day Master (日主) = day stem, surfaced explicitly as the chart's "self" axis.
- 生肖 (Chinese zodiac) from the year branch.

## Not adopted

- Da Yun (大运) — luck pillars are not computed; they need gender + birthplace and a fixed convention.
- Liu Nian (流年) — yearly transit pillars are not derived.
- Shen Sha (神煞) — auspicious/inauspicious stars are not enumerated; tradition varies and the JSON deliberately stays minimal.
- Hidden Stems (藏干) inside each branch are not expanded.
- Strength scoring (旺衰) is not computed.
- True solar time correction is not applied; the script uses the input datetime as-is.

If a user asks for any of the above, surface the limit explicitly — do not invent the values.

## Reading List

- 《滴天髓》(Di Tian Sui)
- 《子平真诠》(Zi Ping Zhen Quan)
- 《穷通宝鉴》(Qiong Tong Bao Jian)

These are classical references for interpretation, not for recomputing the chart.

# Bazi (Four Pillars / 八字) Interpretation Template

Use this only after the bazi script has produced Input JSON.

## Input JSON To Cite

- `inputs.datetime`
- `lunar_date`
- `shengxiao`
- `day_master`
- `pillars.year` / `pillars.month` / `pillars.day` / `pillars.hour`
  (each with `ganzhi`, `stem`, `branch`, `nayin`)
- `five_elements_tally`
- `notes`

## Boundaries

- Do not invent stems (天干), branches (地支), wuxing (五行), or NaYin (纳音). Use only what the JSON returned.
- Do not recompute the chart by hand or "correct" the engine.
- Do not redraw or recast because the chart looks unfavorable.
- Do not pretend to read shen sha (神煞), da yun (大运), or liu nian (流年) — they are not in the JSON.
- If the user did not provide an exact birth hour, surface the limitation and refuse to overstate precision.
- Do not give medical, legal, or financial guarantees.

## Suggested Response Shape

1. Restate the birth datetime, lunar date, and Chinese zodiac (生肖).
2. List the four pillars (year/month/day/hour) with their 干支 and elements, in order.
3. Identify the day master (日主) — stem character, element, polarity — and what it means as the "self" axis.
4. Read the `five_elements_tally`: which element dominates, which is missing or weak.
5. Tie the dominant/weak elements back to the user's question in 1–2 grounded paragraphs.
6. If the hour pillar was missing or low confidence, say so explicitly.

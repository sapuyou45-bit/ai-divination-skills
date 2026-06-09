# Pillars, Stems, Branches, and Elements

A bazi chart is four pillars: year, month, day, hour. Each pillar = one Heavenly Stem (天干) + one Earthly Branch (地支).

## Heavenly Stems (天干)

| Char | Pinyin | Element | Polarity |
|------|--------|---------|----------|
| 甲   | Jia    | wood    | yang     |
| 乙   | Yi     | wood    | yin      |
| 丙   | Bing   | fire    | yang     |
| 丁   | Ding   | fire    | yin      |
| 戊   | Wu     | earth   | yang     |
| 己   | Ji     | earth   | yin      |
| 庚   | Geng   | metal   | yang     |
| 辛   | Xin    | metal   | yin      |
| 壬   | Ren    | water   | yang     |
| 癸   | Gui    | water   | yin      |

## Earthly Branches (地支)

| Char | Pinyin | Element | Polarity | Zodiac  |
|------|--------|---------|----------|---------|
| 子   | Zi     | water   | yang     | Rat     |
| 丑   | Chou   | earth   | yin      | Ox      |
| 寅   | Yin    | wood    | yang     | Tiger   |
| 卯   | Mao    | wood    | yin      | Rabbit  |
| 辰   | Chen   | earth   | yang     | Dragon  |
| 巳   | Si     | fire    | yin      | Snake   |
| 午   | Wu     | fire    | yang     | Horse   |
| 未   | Wei    | earth   | yin      | Goat    |
| 申   | Shen   | metal   | yang     | Monkey  |
| 酉   | You    | metal   | yin      | Rooster |
| 戌   | Xu     | earth   | yang     | Dog     |
| 亥   | Hai    | water   | yin      | Pig     |

## Day Master (日主)

The Day Stem is the "self" axis of the chart. All other elements are read relative to it (supporting, draining, controlling, etc.). The script returns `day_master` separately for convenience.

## Five Elements Tally

The script counts wuxing across all 8 characters (4 stems + 4 branches). Use the tally to spot dominance, weakness, or absence; do **not** invent extra wuxing from shen sha or hidden stems — they are not in the output.

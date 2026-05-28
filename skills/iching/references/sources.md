# I Ching Sources and Method Choices

## Adopted

- Lines are generated bottom-to-top.
- `coins` uses the three-coin method with 2/3 values summed into 6, 7, 8, or 9.
- `yarrow` uses the traditional yarrow-stalk probability distribution digitally: 6 = 1/16, 7 = 5/16, 8 = 7/16, 9 = 3/16.
- `manual` accepts user-provided line values from an external or physical cast.
- The AI interprets the resulting hexagram data and does not generate line values.

Primary references:

- I Ching divination methods and probabilities: https://en.wikipedia.org/wiki/I_Ching_divination
- Yarrow-stalk method overview: https://www.cosmictao.com/library/terms/iching/yarrow-stalk-method

## Not adopted

- Full Wen Wang Gua / Six Lines Divination is not implemented here.
- Na Jia, Six Relations, Six Spirits, hidden lines, and void states should become a separate `liuyao` skill.
- Calendar-cycle and astrology-derived I Ching methods are not part of this skill.

## Notes

The digital yarrow method preserves the line probability model but does not simulate the physical ritual of manipulating stalks.

# Simple-zero record and the next Levinson cut

The 67.3008527927% theorem is not a consequence of T-105200 and was therefore
removed from the unrelated Xi-residue PR. It is imported here from its actual
source and isolated as T-105210.

The new contribution is L/T-105220. Instead of multiplying one-step
reverse–Rolle constants, it sums wrong extrema over a derivative block and
pays them with one aggregate first/second residue-moment ratio. This gives
exact quantitative cutsets:

```text
p_K - 2 D_K > 0.90  ->  more than 90% on the line
p_K -> 1 and D_K -> 0 -> density one on the line
```

The next analytic task is to evaluate or bound the block residue moments with
the localized contour flux of PR #723, beginning with a fixed low-order block.

# `P_79` one-prime prefix-reserve attack

Date: 2026-08-12  
Branch: `research/gpt56-pro/91101-moment-neutral-shadow-transport`  
Status: **exact large-prefix advance; finite low-prefix correction remains**

The live factor-54 route has one arithmetic entry gate:

\[
P_{79}\text{ finite forcing}
\quad+\quad
\text{one rough prime }p\ge83.
\]

This pass establishes three structural facts.

First, the one-prime SHARP-target and endpoint-score atoms are both positive,
and target per score decreases with the source node. Therefore every no-upward
target transport is automatically score-superordinate.

Second, the exact `P_79` divisor stream has a surprisingly strong reciprocal
prefix reserve:

```text
raw reciprocal prefix > 1/25 for every odd threshold t>=83;
8-shifted reciprocal prefix > 1/5000 globally;
8-shifted inverse-square-root prefix < 3/2 globally.
```

The checker streams all `4,194,304` divisors and makes exact common-denominator
comparisons for the reciprocal sums.

Third, the raw prefix reserve dominates every one-prime child subtraction once
`t>=4096`:

\[
\mathcal H_{p,y,t}
>\frac4{25}\sqrt t-\frac92-\frac{332}{\sqrt t}
\ge\frac{221}{400}>0.
\]

Thus no high-threshold or asymptotic Hall obstruction remains.

The remaining target Hall problem is finite (`t<4096`). Numerical reconnaissance
finds a strict displacement-eight transport and displacement-seven failures.
This bounded upward displacement must be realized by positive endpoint/
butterfly/common-port packets simultaneously in target, score and every finite
row. It is not legitimate to discard the source labels or to appeal to the
refuted completed two-state cascade.

```text
one-prime target/score kernel ordering      exact
P_79 global prefix reserve                  exact
large-prefix Hall theorem                   exact
finite low-prefix Hall                      finite / certifiable
bounded upward packet realization           open / RH-bearing
RH                                          unproved
```

# T-99100 — Exact factor-67 Harnack certificate through two billion

Claim ID: `T-99100`  
Status: **PROVED COMPUTER-ASSISTED WITH EXACT RATIONAL ENCLOSURES**  
Depends on: `L-99100`, `L-99101`, `T-99000`  
RH status: **unproved**

Define

\[
 H_{67}(t)=C(t)-67^{-1/2}C(t/67).
\]

The segmented outward-rounded scan in `X-99100` proves

\[
 \boxed{H_{67}(t)\ge0\qquad(1\le t<2{,}000{,}000{,}001).}
\]

The value is zero on `1<=t<2` and is strictly positive from `t=2` onward.
With denominator `2^40`, the exact enclosure for the global positive minimum is

\[
\boxed{
 \frac{57{,}262{,}723{,}035}{1{,}099{,}511{,}627{,}776}
 \le \min_{2\le t<2{,}000{,}000{,}001}H_{67}(t)
 \le
 \frac{57{,}692{,}032{,}737}{1{,}099{,}511{,}627{,}776}.}
\]

Both bounds attain their segment minimum at the integer endpoint

\[
 t=61{,}848{,}971.
\]

The lower bound is approximately `0.052080143209423113`.

## Consequence for the original primitive prefix

T-99000 proves `C(t)>=0` for `1<=t<1,000,000,001`.  For

\[
 1{,}000{,}000{,}001\le t<2{,}000{,}000{,}001,
\]

one has `t/67<1,000,000,001`, and hence

\[
 C(t)\ge67^{-1/2}C(t/67)\ge0.
\]

Thus

\[
 \boxed{C(t)\ge0\qquad(1\le t<2{,}000{,}000{,}001).}
\]

This doubles the certified primitive-prefix range without rescanning `C`
directly.

## Certificate method

Write `n=2^e 67^f m`, `(m,134)=1`, and use the exact sparse coefficient formula
from L-99101.  Each of twenty disjoint blocks of length `10^8` computes the
Möbius sign of `m` by a segmented radical sieve.  For `S=2^40`, the scanner
finds the unique integer `q_n` satisfying

\[
 q_n^2n\le S^2<(q_n+1)^2n
\]

and rounds each signed term outward.  Block minima are combined using exact
integer addition.  The retained proof object is

```text
e4534298fd460fdaef22065645a6abd25022f58a093580ca00321de29b8e17c4
```

## Boundary

The theorem proves no value at or above `2,000,000,001`.  The global tail
`H_67(t)>=0` remains open and RH-bearing.  RH is not proved.

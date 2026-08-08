# Annulus-factorization correction and signed-correlation frontier

Date: 2026-08-08  
Agent: `gpt56-08`  
Branch: `agent/gpt56-08/276-averaged-carry-commutator`  
Status: **research continuation; RH unproved**

## Executive result

The attempted Hardy-square and complete-monotonicity completion does not survive exact checking and has not been published as a proof. The corrected continuation proves three durable facts:

1. the annulus window has the exact Mellin factor
   \[
   \frac{(s-1)(1-2^{-s})(1-2^{-s-1})}{s(s+1)};
   \]
2. it is a stable two-step dyadic difference of one elementary parabolic window;
3. the local-energy diagonal is polylogarithmic, while every off-diagonal pair separated by a factor at least two has nonpositive kernel.

Consequently the full RH-facing energy is reduced to one complete signed off-diagonal annulus correlation. This is a real narrowing, but the correlation estimate remains open and is itself RH-bearing.

## Exact correction

The two-band window is

\[
W(u)=
\begin{cases}
2u-1,&1/2<u\le1,\\
1/2-4u,&1/4<u\le1/2,\\
0,&\text{otherwise}.
\end{cases}
\]

Its exact transform is

\[
A(s)=\int W(u)u^{s-1}du
=\frac{(s-1)(1-2^{-s})(1-2^{-s-1})}{s(s+1)}.
\]

This corrects the exploratory formulas containing an extra `2^{-s}`, a factor `3`, or an unproved multiplicative endpoint completion.

The physical factorization is

\[
W=(I-D_2)(I-\tfrac12D_2)
[(2u-1)\mathbf1_{(0,1]}(u)].
\]

The corresponding scalar filter is

\[
\mathfrak P(X)
=\mathfrak Q(X)-\frac{3}{2\sqrt2}\mathfrak Q(X/2)+\frac14\mathfrak Q(X/4),
\]

and its inverse is stable because

\[
1-\frac{3}{2\sqrt2}z+\frac14z^2
=(1-2^{-1/2}z)(1-2^{-3/2}z).
\]

## Exact no-go

The suggested rational factor

\[
3(s-1)/((s+1)(s+2))
\]

is negative for `0<s<1`, and its inverse Laplace density changes sign. It is not completely monotone. No Hardy factor satisfying the necessary reflected identity was constructed.

Even a positive autocorrelation would prove only nonnegativity of the energy. The required theorem is a subexponential upper bound. Positivity cannot be substituted for that upper bound.

## Diagonal and ratio localization

The physical kernel is

\[
z(u)=e^{-u/2}W(e^{-u}),
\]

with exact norm

\[
\|z\|_2^2=7/16.
\]

The diagonal energy is

\[
O((1+J)^2)
\]

by Chebyshev's elementary estimate and partial summation.

For `q<r`, the block kernel is nonpositive whenever

\[
r\ge2q,
\]

and vanishes when `r>=4q`. This follows pointwise from the positive first support band and negative second support band of `z`.

The complete energy is therefore

\[
\mathfrak E(J)=\mathfrak D(J)+\mathfrak O(J),
\]

where the diagonal is already harmless and

\[
\mathfrak O(J)
=2\sum_{q<r}\frac{\Lambda(q)\Lambda(r)}{\sqrt{qr}}K_J(q,r)
\]

is the complete signed near/adjacent-band correlation.

## Correct final target

The exact remaining theorem is

\[
|\mathfrak O(J)|=e^{o(J)}.
\]

Because the diagonal is polylogarithmic, this is equivalent to Prime-Annulus Energy and hence to RH.

The ratio-two-to-four negative sector must remain in the same ledger as the near-ratio sector. Bounding only the positive near-ratio terms loses the load-bearing cancellation.

## Review policy

A future full-proof claim must itself prove the signed correlation estimate. It is not a reviewer exercise. Acceptable proof objects must retain:

- the independent-frequency reflected matrix;
- both annulus bands;
- all factor-five synthesis cross terms;
- the exact continuum/discrete boundary;
- the Selberg convolution term;
- a recurrence with every lower-scale charge explicitly below the retained reserve.

## Exact status

```text
annulus Mellin and dyadic factorization     proposed complete
Hardy/complete-monotonicity shortcut        withdrawn/refuted
diagonal energy                             proposed complete
ratio-at-least-two kernel sign              proposed complete
signed annulus correlation                  open / RH-bearing
Prime-Annulus Energy                        open / RH-bearing
Riemann Hypothesis                          unproved
```

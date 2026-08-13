# L-91557 — The equality density supplies the native score front door, and the parabolic score is at most `4 sqrt(X)+4 log X`

Claim ID: `L-91557`  
Status: **PROVED EXACT SCORE CONSUMER ON THE FROZEN RESET IDENTITY — FINAL PHYSICAL ASSEMBLY STILL REQUIRES REVIEW**  
Created: 2026-08-13  
Depends on: PR #265 `L-26204`; `L-24502`; `L-91110`; `L-91114/L-91115`; `L-91329`; `L-91545`, `L-91547`, `L-91553/L-91554`, `L-91556`  
RH status: **unproved**

## 1. The correct native score front door

Let `L_*(t)` be the causal continuum endpoint equality weight of `L-26204`.
Its positive endpoint kernel `varrho` satisfies

\[
 (L_* *\varrho)(t)=t,
 \tag{L-91557.1}
\]

so it exactly saturates the normalized critical carry target.  Its critical
endpoint-score mass is

\[
 \boxed{
 2\int_0^\infty e^{-t/2}L_*(t)\,dt=4.
 }
 \tag{L-91557.2}
\]

At physical endpoint `X`, scale covariance multiplies this score by `sqrt(X)`.
Thus the complete continuum equality density has exact native score

\[
 \boxed{
 \mathcal J_{\rm eq}^{\rm cont}(X)=4\sqrt X.
 }
 \tag{L-91557.3}
\]

This, rather than a pointwise identification of `5 sqrt(Y)-3` with component
entropy, is the native score boundary.  `R-91552` remains valid: the latter
pointwise identification is false.

## 2. The row-budgeted reset preserves the equality score

`L-91556` gives the exact one-prime native budget

\[
 T_s+T_h=T_0,
 \qquad
 \widetilde S_s+\widetilde S_h=S_0,
 \qquad
 \kappa_s+\kappa_h=1,
 \tag{L-91557.4}
\]

with

\[
 \kappa_s=1-r^2,
 \qquad
 \kappa_h=r^2.
 \tag{L-91557.5}
\]

The excess binary score `r(1-r)(z-1)` is favorable current-generation slack and
is not charged to the recursive row.

Apply target Hall with the row-budgeted score.  `L-91545/L-91556` give:

```text
exact target use;
native score superordination;
exact parent-row partition;
positive target-null Hall row bonus.
```

Apply the fixed `67` split.  `L-91553/L-91556` prove that every nonterminal
physical component-row difference realizes at least the complete native score
difference.  `L-91554` proves that the total terminal score-realization deficit
of one fixed-Euler source tree is absolutely bounded by

\[
 C_{79}=5600
 \qquad\text{or}\qquad
 C_{61}=3600.
 \tag{L-91557.6}
\]

Therefore, on the exact one-use source identity consumed by
`L-91545/L-91547`, the positive continuum reset output has score

\[
 \boxed{
 \mathcal J_{\rm reset}^{\rm cont}(X)
 \ge4\sqrt X-C_P,
 }
 \tag{L-91557.7}
\]

where `P=P_79` or `P_61`.  This is an all-depth statement for one post-Hall
fixed-Euler source tree; the finite-support deficit is not multiplied by the
number of `67` levels.

The logical input here is the one-use source identity: the current packets,
children and target-null bonuses must be the positive decomposition of the
same equality-density target, not merely scalar objects with matching target
values.  The local target/score/row normalization of that identity is now exact
by `L-91556`.

## 3. Positive quantization cannot lower the score

Let the positive continuum packets be pushed to the common parent endpoint
coordinate and summed before discretization.  `L-91110` proves that the local
martingale B-spline quantization satisfies

\[
 \boxed{
 \sum_T\Lambda_TH_T
 \ge
 \int\lambda(s)\dot H(s)\,ds.
 }
 \tag{L-91557.8}
\]

Thus quantization cannot consume any of the lower bound (L-91557.7).  The only
finite score charges are the explicitly separated global safety factor,
finite/continuum mismatch, fixed top omission, terminal collar and common
endpoint port.  Denote their one-use total by `C_fin`.

On the cited finite assembly inputs, the resulting nonnegative row therefore
has

\[
 \boxed{
 \mathcal S_X(d_X)
 \ge4\sqrt X-C_P-C_{\rm fin}.
 }
 \tag{L-91557.9}
\]

The final ordinary/radix-four capacity reconstruction remains a separate review
obligation; Section 5 records it explicitly.

## 4. An explicit upper bound for the native parabolic score

For `2<=m<=X`, retain

\[
 b_X(m)=2\sqrt m
 \left[
  \log\frac Xm-2\left(1-\sqrt{m/X}\right)
 \right]
 \tag{L-91557.10}
\]

and

\[
 J_\Lambda(X)
 =\sum_{m=2}^Xb_X(m)\log\frac m{m-1}.
 \tag{L-91557.11}
\]

Put

\[
 f_X(x)=\frac{b_X(x)}x
 =2x^{-1/2}\log\frac Xx-4x^{-1/2}+4X^{-1/2}.
 \tag{L-91557.12}
\]

`L-24502` proves that `f_X` is nonnegative and decreasing.  Hence

\[
 \sum_{m=2}^X\frac{b_X(m)}m
 \le\int_1^Xf_X(x)\,dx.
 \tag{L-91557.13}
\]

Direct integration gives

\[
 \boxed{
 \int_1^Xf_X(x)\,dx
 =4\sqrt X-4\log X-\frac4{\sqrt X}.
 }
 \tag{L-91557.14}
\]

Also

\[
 \log\frac m{m-1}
 \le\frac1{m-1}
 =\frac1m+\frac1{m(m-1)}
 \tag{L-91557.15}
\]

and, because the bracket in (L-91557.10) is at most `log(X/m)`,

\[
 b_X(m)\le2\sqrt m\log X.
 \tag{L-91557.16}
\]

For `m>=2`, `m-1>=m/2`, and the decreasing-integral bound gives

\[
 \sum_{m=2}^\infty m^{-3/2}\le2.
 \tag{L-91557.17}
\]

Therefore

\[
\begin{aligned}
 \sum_{m=2}^X\frac{b_X(m)}{m(m-1)}
 &\le4\log X\sum_{m=2}^Xm^{-3/2}\\
 &\le8\log X.
\end{aligned}
 \tag{L-91557.18}
\]

Combining (L-91557.13)--(L-91557.18),

\[
 \boxed{
 J_\Lambda(X)
 \le4\sqrt X+4\log X-\frac4{\sqrt X}
 <4\sqrt X+4\log X.
 }
 \tag{L-91557.19}
\]

This is unconditional and elementary.

## 5. Native logarithmic-loss consequence

If the final finite row in Section 3 is radix-four detail feasible in the exact
sense of `L-90029`, then (L-91557.9) and (L-91557.19) give

\[
\begin{aligned}
 \mathfrak L_X(d_X)
 &=J_\Lambda(X)-\mathcal S_X(d_X)\\
 &\le4\log X+C_P+C_{\rm fin}.
\end{aligned}
 \tag{L-91557.20}
\]

Hence

\[
 \boxed{
 \mathfrak L_X(d_X)=O(\log X)=o(\log^2X).
 }
 \tag{L-91557.21}
\]

By `L-90029`, this would imply RH.

The native score boundary is therefore no longer an unidentified equality
between `S_parent` and `J_Lambda`.  It is the exact continuum equality score
`4 sqrt(X)` plus the elementary finite comparison (L-91557.19).

## 6. Remaining load-bearing interface

This lemma is a score consumer.  It does not by itself establish that the final
finite row is detail feasible.  A hostile reviewer must still reconstruct:

1. the exact one-use source identity from the equality density through the
   binary/Hall/fixed-67 packets;
2. the pushforward of every child to the common parent coordinate;
3. the single global quantization, safety factor, top omission and terminal
   collar;
4. one-use common-port accounting;
5. every physical integer radix-four column inequality;
6. the uniform finite base;
7. replay after rebasing onto the current moving PR #399 head.

Any failure there retracts (L-91557.9) while leaving the exact score mass four,
the row-budget theorem and the parabolic upper bound intact.

```text
equality-density normalized score                    EXACTLY 4
physical equality score                              EXACTLY 4 sqrt(X)
binary native target/score/row budget                 EXACT / L-91556
all-depth finite-Euler score deficit                  ABSOLUTELY BOUNDED
positive B-spline quantization                        SCORE-FAVORABLE
J_Lambda(X) < 4 sqrt(X)+4 log(X)                      EXACT
native O(log X) loss                                  CONDITIONAL ON FINAL CAPACITY
final radix-four physical assembly                    OPEN / REVIEW-BEARING
Riemann Hypothesis                                    UNPROVEN
```

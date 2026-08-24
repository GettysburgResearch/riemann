# L-102830 — Largest-two ownership is an exact subpower gauge for the Wick pair current

Claim ID: `L-102830`  
Status: **PROVED EXACT OWNER-REALLOCATION THEOREM**  
Created: 2026-08-24  
Depends on: `L-102746--L-102749`; `T-102820`  
RH status: **not assumed**

Fix a total order on the labelled prime coordinates which refines prime size.
The two copies of `67` remain distinct by a fixed tie-breaker. For a squarefree
labelled occurrence `S` with `k=|S|>=2`, write

\[
\operatorname{Top}_2(S)=\{p(S),q(S)\},
\qquad p(S)>q(S).
\]

`L-102746` assigns the coefficient of `S` equally to its
\(\binom{k}{2}\) unordered owner pairs. Define instead the largest-two gauge:
put the complete coefficient on `Top_2(S)` and zero on every other pair.

## 1. Physical realization is unchanged

The physical realization forgets the pair-owner coordinate only after all
shares belonging to one labelled occurrence are summed. Both owner rules sum to
the same coefficient of the same product. Hence

\[
\boxed{
\mathcal R_{\rm phys}(J_{\rm equal})
=
\mathcal R_{\rm phys}(J_{\rm top2}).
}
\tag{L-102830.1}
\]

This is coefficient-exact and commutes with every fixed source region, Euler or
half-divisor gauge, common-mother observation and completion parameter.

## 2. The labelled transfer costs only a squared logarithm

For one depth-`k` occurrence with physical vector `v`, the equal-pair labelled
energy is

\[
\sum_P\left\|\binom{k}{2}^{-1}v\right\|^2
=
\binom{k}{2}^{-1}\|v\|^2,
\]

while the largest-two labelled energy is `||v||^2`. The exact transfer factor
is therefore

\[
\boxed{\binom{k}{2}.}
\tag{L-102830.2}
\]

On the horizon `n<=16Y`,

\[
k\le {\log(16Y)\over\log2}+1,
\]

including the second labelled `67`. Consequently

\[
\boxed{
\|J_{\rm top2}\|_{\rm labelled}^2
\ll (\log(2Y))^2
\|J_{\rm equal}\|_{\rm labelled}^2.
}
\tag{L-102830.3}
\]

Thus the canonical equal-pair gauge and deterministic largest-two gauge are
subpower-equivalent before physical collapse.

## 3. Why this gauge is useful

In the largest-two gauge every hard occurrence has exactly two unsquared
arithmetic owners and every remaining prime label is smaller than the second
owner. This permits the square-completion and injectivity theorem of
`L-102831`.

No cross-owner estimate is claimed here. The theorem changes coordinates
without changing the literal physical current.
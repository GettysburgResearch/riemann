# L-102863 — Balanced cross-side phases give a modulus-free fixed-pair bound

Claim ID: `L-102863`  
Status: **PROVED UNCONDITIONAL FIXED-PAIR ESTIMATE**  
Created: 2026-08-24  
Depends on: `L-102836`, `L-102860--L-102862`  
RH status: **not assumed**

Work in the clean direct sector of `L-102862`:

\[
N=pq\,a^2,
\qquad
M=rs\,b^2,
\]

where `p>q`, `r>s`, the four owners are distinct, and no owner occurs in the
opposite square core. Put the cores in octaves

\[
A\le a<2A,
\qquad
B\le b<2B.
\]

Use the nonzero phase modulo `r` on the `N` field and the nonzero phase modulo
`p` on the `M` field. Let `F_k^(N)` and `F_h^(M)` denote the corresponding
phase fields, including the literal owner-pair coefficients

\[
(pq)^{-1/2},
\qquad
(rs)^{-1/2}.
\]

The two nonzero Ramanujan sums give

\[
\mathcal C_{P,Q}
=
\sum_{h=1}^{p-1}
\sum_{k=1}^{r-1}
\langle F_k^{(N)},F_h^{(M)}\rangle.
\tag{L-102863.1}

## 1. Fixed-side phase energies

Applying `L-102836` with the opposite owner as modulus gives

\[
\boxed{
\sum_{k=1}^{r-1}\|F_k^{(N)}\|_2^2
\ll_\phi
{1\over pq}\left(1+{r\over A}\right),
}
\tag{L-102863.2}

and

\[
\boxed{
\sum_{h=1}^{p-1}\|F_h^{(M)}\|_2^2
\ll_\phi
{1\over rs}\left(1+{p\over B}\right).
}
\tag{L-102863.3}

No cancellation in the core coefficients is used.

## 2. Exact owner/modulus cancellation

Cauchy in the two phase variables gives

\[
|\mathcal C_{P,Q}|
\le
\left(r\sum_k\|F_k^{(N)}\|_2^2\right)^{1/2}
\left(p\sum_h\|F_h^{(M)}\|_2^2\right)^{1/2}.
\]

Substituting (L-102863.2)--(L-102863.3),

\[
\boxed{
|\mathcal C_{P,Q}|
\ll_\phi
{1\over\sqrt{qs}}
\left(1+{r\over A}\right)^{1/2}
\left(1+{p\over B}\right)^{1/2}.
}
\tag{L-102863.4}

The phase-cardinality factors `r` and `p` have canceled the literal weights of
the selected owners. No positive power of either largest owner remains.

In the doubly long regime

\[
A\ge r,
\qquad
B\ge p,
\]

one obtains

\[
\boxed{
|\mathcal C_{P,Q}|
\ll_\phi {1\over\sqrt{qs}}.
}
\tag{L-102863.5}

## Scope

This is a complete estimate for one fixed clean owner quadruple and two core
octaves. The residual second-owner weights are removed by the four-phase
normalization in `L-102864`. Coherent summation over owner quadruples remains
arithmetic.
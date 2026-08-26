# L-102865 — An exact adaptive selector optimizes the owner phases in every core regime

Claim ID: `L-102865`  
Status: **PROVED EXACT FINITE OPTIMIZATION THEOREM**  
Created: 2026-08-24  
Depends on: `L-102836`, `L-102839`, `L-102862--L-102864`  
RH status: **not assumed**

Work in the clean four-owner sector

\[
N=pq\,a^2,
\qquad
M=rs\,b^2,
\]

with core octaves `A<=a<2A` and `B<=b<2B`.

Choose subsets

\[
S_N\subseteq\{r,s\},
\qquad
S_M\subseteq\{p,q\},
\]

not both empty. The moduli in `S_N` phase the `N` field and the moduli in
`S_M` phase the `M` field. Put

\[
L_N=\prod_{\ell\in S_N}\ell,
\qquad
L_M=\prod_{\ell\in S_M}\ell,
\]

with an empty product equal to one.

Every selected nonzero Ramanujan sum equals `-1`, so their product represents
the original cross coefficient up to the known sign
`(-1)^(|S_N|+|S_M|)`. No zero frequency is introduced.

## 1. Uniform subset bound

Chinese-remainder orthogonality gives

\[
\sum_{\mathbf h_N}\|F_{\mathbf h_N}^{(N)}\|_2^2
\ll_\phi
{1\over pq}\left(1+{L_N\over A}\right),
\]

and

\[
\sum_{\mathbf h_M}\|F_{\mathbf h_M}^{(M)}\|_2^2
\ll_\phi
{1\over rs}\left(1+{L_M\over B}\right).
\]

For `L_N=1` or `L_M=1`, these are the unphased one-octave same-pair bounds.
Cauchy over the selected phase packets yields

\[
\boxed{
|\mathcal C_{P,Q}|
\ll_\phi
\left[
{L_NL_M\over pqrs}
\left(1+{L_N\over A}\right)
\left(1+{L_M\over B}\right)
\right]^{1/2}.
}
\tag{L-102865.1}

## 2. Exact local optimization

There are only

\[
(2^2)(2^2)-1=15
\]

nonempty choices. Therefore the best source-faithful fixed-pair estimate is

\[
\boxed{
|\mathcal C_{P,Q}|
\ll_\phi
\min_{\substack{S_N\subseteq\{r,s\},\ S_M\subseteq\{p,q\}\\
S_N\cup S_M\ne\varnothing}}
\left[
{L_NL_M\over pqrs}
\left(1+{L_N\over A}\right)
\left(1+{L_M\over B}\right)
\right]^{1/2}.
}
\tag{L-102865.2}

This single formula contains:

```text
one-phase largest-discrepancy dispersion;
balanced one-phase-per-side dispersion;
two-modulus phases on one side;
three-phase hybrids;
full four-owner normalization.
```

For example, selecting only the smallest usable owner `ell` gives

\[
|\mathcal C_{P,Q}|
\ll_\phi
\left[{\ell\over pqrs}
\left(1+{\ell\over A_{\rm phased}}\right)\right]^{1/2},
\]

while selecting all four owners gives `L-102864`.

## Meaning

No phase choice is globally optimal. Long cores favor more phase directions;
short cores retain the weights of large owners. Equation (L-102865.2) makes
that tradeoff exact before coherent summation. The remaining theorem is the
arithmetic summation of these optimally normalized packets, not selection of a
phase architecture.
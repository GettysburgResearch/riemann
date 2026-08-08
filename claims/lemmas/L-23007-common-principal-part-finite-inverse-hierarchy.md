# L-23007 — Common principal part of the finite inverse-zeta hierarchy

Claim ID: `L-23007`  
Title: Every finite Heath--Brown inverse residual carries exactly the same nontrivial-zero principal part as `1/zeta`, while every cross-order difference is reciprocal-free  
Status: **PROPOSED — COMPLETE MEROMORPHIC ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: `L-15159`; `L-23006`; elementary Laurent expansion  
Scope: every finite truncation parameter `V` and order `K`; no bound for the common Möbius core

## 1. Dirichlet-series coordinates

For `Re(s)>1`, put

\[
 M_V(s)=\sum_{n\le V}{\mu(n)\over n^s}
\]

and

\[
 \boxed{R_V(s)=1-\zeta(s)M_V(s).}
\tag{L-23007.1}
\]

The finite inverse packet and its residual have Dirichlet series

\[
 \boxed{
 A_{K,V}(s)
 =M_V(s)\sum_{j=0}^{K-1}R_V(s)^j
 ={1-R_V(s)^K\over\zeta(s)},}
\tag{L-23007.2}
\]

\[
 \boxed{
 E_{K,V}(s)
 :={1\over\zeta(s)}-A_{K,V}(s)
 ={R_V(s)^K\over\zeta(s)}.}
\tag{L-23007.3}
\]

Equation (L-23007.3) is the Dirichlet-series form of

\[
 \mu-A_{K,V}=\mu*r_V^{*K}
\]

from `L-23006`.

## 2. Exact principal-part invariance

Let `rho` be a nontrivial zero of `zeta` of multiplicity `m`. Write

\[
 \zeta(s)=(s-\rho)^m g_\rho(s),
 \qquad g_\rho(\rho)\ne0.
\tag{L-23007.4}
\]

Because `M_V` is entire,

\[
 R_V(s)
 =1-(s-\rho)^m g_\rho(s)M_V(s)
 =1+O((s-\rho)^m).
\tag{L-23007.5}
\]

Hence for every finite `K>=1`,

\[
 R_V(s)^K=1+O((s-\rho)^m).
\tag{L-23007.6}
\]

Multiplication of the order-`m` Laurent expansion of `1/zeta` by
`1+O((s-rho)^m)` changes only its holomorphic part. Therefore

\[
 \boxed{
 \operatorname{PP}_{s=\rho}E_{K,V}(s)
 =\operatorname{PP}_{s=\rho}{1\over\zeta(s)},}
\tag{L-23007.7}
\]

where `PP` denotes the complete negative-power Laurent polynomial, including
multiplicity.

Thus every finite residual has not merely the same rightmost pole location but
the same complete principal part at every nontrivial zero.

## 3. Adjacent-order coboundary

Subtracting (L-23007.2) at consecutive orders gives

\[
 \boxed{
 A_{K+1,V}-A_{K,V}
 =M_V R_V^K.}
\tag{L-23007.8}
\]

Equivalently,

\[
 \boxed{
 E_{K,V}-E_{K+1,V}
 =M_V R_V^K.}
\tag{L-23007.9}
\]

The right side contains only the finite Dirichlet polynomial `M_V` and
nonnegative powers of `zeta`; it has no reciprocal-zeta pole at a nontrivial
zero. More generally, for `L>K`,

\[
 \boxed{
 E_{K,V}-E_{L,V}
 =M_VR_V^K\sum_{j=0}^{L-K-1}R_V^j.}
\tag{L-23007.10}
\]

After the pole at `s=1` is removed by the safe-window moments, these differences
are precisely the reciprocal-free complete-lattice rows to which `L-23005`
applies.

## 4. Finite cross-order quotient

Allow finitely many pairs `(K_j,V_j)` and coefficients `c_j`. Equations
(L-23007.3) and

\[
 E_{K_j,V_j}={1\over\zeta}-A_{K_j,V_j}
\]

give

\[
 \boxed{
 \sum_j c_jE_{K_j,V_j}
 =\left(\sum_jc_j\right){1\over\zeta}
  -\sum_jc_jA_{K_j,V_j}.}
\tag{L-23007.11}
\]

Consequently, at every nontrivial zero,

\[
 \boxed{
 \operatorname{PP}\left(\sum_jc_jE_{K_j,V_j}\right)
 =\left(\sum_jc_j\right)
  \operatorname{PP}\left({1\over\zeta}\right).}
\tag{L-23007.12}
\]

There is an exact dichotomy.

- If `sum c_j=0`, all nontrivial-zero poles cancel, and the combination is a
  reciprocal-free finite zeta-polynomial packet.
- If `sum c_j!=0`, the full Möbius principal part survives, scaled by
  `sum c_j`.

Thus the finite inverse hierarchy has a one-dimensional meromorphic quotient:
all cross-order differences are analytically harmless, while the common
quotient class is represented by `1/zeta` itself.

## 5. Safe-window consequence

Let `H` be a compact safe window whose transform is nonzero at every point in
`0<Re z<1/2`. Multiplying (L-23007.7) by `widehat H(s-1/2)` preserves every
hypothetical off-line principal part. Hence every finite residual safe signal
has exactly the same rightmost-zero exponent as the Möbius safe signal.

Increasing the finite identity order does not attenuate an off-line pole: at a
zero one has `R_V(rho)=1` exactly.

## 6. Proof boundary

Closed exactly:

- the residual principal-part invariance;
- the reciprocal-free adjacent-order difference;
- the one-dimensional finite cross-order quotient.

Not closed:

- a source-specific nonlinear estimate for the common quotient class;
- an infinite, nonuniform cross-order limit with all convergence and safe-window
  costs proved;
- the fixed-ratio Mertens bound or RH.

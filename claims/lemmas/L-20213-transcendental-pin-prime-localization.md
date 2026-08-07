# L-20213 — The transcendental exposure pin is confined to the oldest prime prefix

Claim ID: `L-20213`  
Title: At the critical mesh, the exact pole-exposure pin changes only prime powers below `n^(2/N)` and costs `e^-N`  
Status: **PROPOSED — COMPLETE ALGEBRAIC CONSEQUENCE OF `T-20206`**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20206`; the exact finite formula for `Psi`  
Scope: one fixed degree `N>=2`, every integer sample `n>=2`

## 1. Exact decomposition

Let `P_N` be the algebraic endpoint Fejer filter of `L-20211` and let

\[
 \widetilde P_N(x)=P_N(x)+e^{-N}(1-\cos x).
\]

The pinned screw statistic is exactly

\[
\boxed{
 \mathcal E_N(t)
 =\mathcal E_N^{(0)}(t)+e^{-N}\Psi(t),}
\]

where

\[
 \mathcal E_N^{(0)}(t)
 =\sum_{k=1}^{N}\lambda_{N,k}^{(0)}\Psi(kt).
\]

Likewise, for the prime ramps,

\[
\boxed{
 \widetilde L_N(s)
 =L_N(s)+e^{-N}(1-s)_+.}
\]

## 2. Complete prime coefficient

For a prime power `q`, put

\[
 s_q={\log q\over t}.
\]

The exact filtered prime coefficient is

\[
\boxed{
 -t{\Lambda(q)\over\sqrt q}
 \left[
  L_N(s_q)+e^{-N}(1-s_q)_+
 \right].}
\]

The pin contribution vanishes identically when

\[
 q>e^t.
\]

The degree-`N` algebraic filter, by contrast, has support through

\[
 q\le e^{Nt}.
\]

## 3. Critical mesh

At the pole-descent sampling points

\[
 t_n={2\log n\over N},
\]

the complete algebraic filter includes every prime power through

\[
 e^{Nt_n}=n^2,
\]

whereas the transcendental pin touches only

\[
\boxed{
 q\le e^{t_n}=n^{2/N}.}
\]

Thus the pin alters a prefix whose logarithmic length is only `1/N` of the full
support, and every altered coefficient is multiplied by `e^-N`.

The pin-side prime term is explicitly

\[
\boxed{
 -e^{-N}
 \sum_{q\le n^{2/N}}
 {\Lambda(q)\over\sqrt q}
 \left({2\log n\over N}-\log q\right).}
\]

No prime power outside this prefix is changed.

## 4. Other source terms

The polar, gamma, and Lerch changes are exactly `e^-N` times the corresponding
terms of `Psi(t_n)`. They have no hidden dependence on the degree-`N` algebraic
coefficients. A production certificate can therefore maintain two separately
bound ledgers:

1. the algebraic endpoint-filter statistic;
2. the scalar pinned `Psi` statistic multiplied by the symbolic factor `e^-N`.

The final directed interval is their Minkowski sum, while the analytic
noncancellation theorem retains `e^-N` symbolically rather than replacing it by
a decimal.

## 5. Quantitative interpretation

For a fixed large `N`, the pin has two very different effects:

- **analytic:** it gives an uncancellable transcendental residue at every
  hypothetical off-line pole;
- **arithmetic:** it adds only an exponentially small scalar correction supported
  on the oldest prime prefix.

This is the desired bridge between false-RH exposure and near-optimal prime
conditioning. The remaining burden is the cofinal sign of the algebraic bulk;
the pin does not reintroduce a terminal or full-support prime penalty.

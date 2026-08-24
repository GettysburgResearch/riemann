# L-102885 — The derivative outer detector is a stable image of the same-`K1` wavelet

Claim ID: `L-102885`  
Status: **PROVED EXACT MELLIN/DIFFERENTIAL IDENTIFICATION**  
Created: 2026-08-24  
Depends on: `L-102500`; `T-102790`; `L-102880`  
RH status: **not assumed**

Let `K_XD` be the corrected same-`K1` compact wavelet of `L-102500`, with multiplier

\[
m_{XD}(s)
={q(s)^2r(s)^2(s+3/2)\over s^2(s-1/2)},
\]

where

\[
q(s)=1-\sqrt2\,2^{-s},
\qquad r(s)=1-2^{-s}.
\]

Let `R_L` be the centered outer kernel and `K_L=DR_L` the derivative detector of `L-102880`.  `T-102790` gives

\[
\widehat{R_L}(s)
={1\over2}(s-1)(5s+3/2)m_\Phi(s).
\]

Therefore

\[
\widehat{K_L}(s)
={1\over2}s(s-1)(5s+3/2)m_\Phi(s)
\]

and

\[
\boxed{
(s+3/2)\widehat{K_L}(s)
=s(s-1)(5s+3/2)m_{XD}(s).
}
\tag{L-102885.1}

Equivalently, as compactly supported logarithmic distributions,

\[
\boxed{
(D+3/2)K_L
=D(D-1)(5D+3/2)K_{XD}.
}
\tag{L-102885.2}

## 1. Stable direction

The inverse of `D+3/2` on the zero-extended causal line is positive:

\[
[(D+3/2)^{-1}f](u)
=\int_{-\infty}^{u}e^{-3(u-v)/2}f(v)\,dv.
\]

Thus `K_L` is a fixed stable resolvent of a finite differential image of the same corrected `K1` wavelet used by the largest-prime/Vaughan programme.

## 2. Source consequence

All multiplicative source shifts, stopped-prime projections, owner phases and Euler/half-divisor/Wick gauges commute with (L-102885.2).  Hence the stopped balanced current in `L-102881` and the same-`K1` balanced current are not independent source problems; they are fixed differential coordinates on the same literal stopped source.

## Scope

Differentiation need not preserve one-sided logarithmic mass, and the source-free reverse estimate is false by the high-frequency firewalls already retained on PR #719.  The theorem merges the source and multiplier lineage; it does not prove `SLCD102890`.

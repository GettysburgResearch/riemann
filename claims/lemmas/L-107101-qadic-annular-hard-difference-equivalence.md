# L-107101 — Annular hard differences are power-equivalent to the prefix stack

**Claim ID:** `L-107101`  
**Status:** proved exact finite Hardy-frame theorem  
**Date:** 2026-08-31

Define

\[
c_j=u_j-u_{j+1}
=\left(w_{k,X}\sum_{X/q^{j+1}<n\le X/q^j,\ q\nmid n}
\mu(n)n^{-1/2-it_{k,X}}\right)_k.
\]

Hence each `c_j` is supported on one literal ratio-67 annulus. Since
`c=(I-S)u`,

\[
\|c\|_{\ell^2}\le2\|u\|_{\ell^2}.
\]

The sequence terminates and `u_j=sum_{m>=j}c_m`, so finite Hardy gives

\[
\|u\|_{\ell^2}\le(J+1)\|c\|_{\ell^2}.
\]

Therefore

\[
\boxed{(J+1)^{-2}\sum_j\|u_j\|^2
\le\sum_j\|c_j\|^2
\le4\sum_j\|u_j\|^2.}\tag{1}
\]

Combining with L-107100,

\[
\boxed{\frac{(1-q^{-1/2})^4}{4}\sum_j\|c_j\|^2
\le\sum_j\|g_j\|^2
\le(1+q^{-1/2})^4(J+1)^2\sum_j\|c_j\|^2.}\tag{2}
\]

All losses are constant or polylogarithmic. The parent-grid Poisson theorem is
uniform in `j`: a smaller prefix has no larger physical support, and the outer
padding and frequency cutoff dominate the requirements of L-107021. Summing
`O(log X)` errors still gives every-power decay after increasing the fixed
padding constant.

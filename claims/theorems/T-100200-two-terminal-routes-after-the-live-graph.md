# T-100200 — Two terminal closure routes after the live graph

Claim ID: `T-100200`  
Status: **UNCONDITIONAL STRUCTURAL ADVANCE; TWO EXPLICIT FINAL GATES OPEN**  
Created: 2026-08-20  
Base: PR #672 at `2a351548eb7960ff8ae99f193c10e278984c5657`  
External sibling: PR #590 at `d42817f4de15b97d37f760578d64d067a77be5c5`  
RH status: **unproved**

After PRs #673--#680, the complete Hardy/GCD squares, the minimal wavelet energy, and the critical variation criteria are known to be RH-equivalent. They are retained as consumers and diagnostics, not counted as independent closure routes.

The two routes with remaining structural leverage are:

## Route A — cell-Hankel quadratic envelope

The envelope is exactly

\[
\frac{\mathcal E_2(X)}X=z_X^{\mathsf T}M_{\lfloor X\rfloor}z_X.
\]

Its arithmetic state has signed rank-one Euler updates. The complete continuous mixed-activation problem reduces to cell endpoints plus one two-by-two Schur inequality `CEHC100200`.

\[
\boxed{\mathrm{CEHC100200}\Longrightarrow RH.}
\]

The determinant driver is the explicit reciprocal-zeta scalar of `L-100201`, so the unresolved arithmetic is visible and cannot be hidden in activation bookkeeping.

## Route B — largest-prime telescoping and terminal collar

The constant and half-order asymptotic modes of the small-prime cube telescope exactly under largest-prime ownership. Every deep residual history is bounded absolutely. The only remaining object is the subpower multiplicative collar `RAPC100210`, containing the exact inactive-subset correction.

\[
\boxed{\mathrm{RAPC100210}\Longrightarrow\mathrm{BLPTE67}\Longrightarrow RH.}
\]

## Exact boundary

```text
quadratic envelope 2x2 state                 PROVED EXACT
cell minimum / Schur complement reduction     PROVED EXACT
rank-one Euler update                         PROVED EXACT
CEHC100200                                    OPEN / CONCLUSION-BEARING

largest-prime constant telescoping            PROVED EXACT
physical activation-tail correction           PROVED EXACT
deep residual histories                       CLOSED ABSOLUTELY
RAPC100210                                    OPEN / CONCLUSION-BEARING

Riemann Hypothesis                            UNPROVEN
```
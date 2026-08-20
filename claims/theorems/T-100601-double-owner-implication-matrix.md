# T-100601 — Double-owner implication matrix after compositional audit

Status: **PROVED EXACT DECOMPOSITION; REGIONAL ESTIMATES MUST REMAIN ORIENTED; RH UNPROVEN**

The exact double-owner decomposition `L-100605` turns the native Euler source into blocks indexed by endpoint primes `(p_i,p_j)`:

\[
\mathcal D_{i,i}=-r_iU_i,
\qquad
\mathcal D_{i,j}=r_ir_jU_iU_j
\prod_{i<h<j}(I-r_hU_h),\quad i<j.
\]

After projection through the fixed ratio-eight minimal wavelet, every active block has

\[
X/8\le p_i p_j m\le X,
\]

with all prime factors of `m` strictly between the endpoint primes.  This finite-interval localization is exact.

## Region geometry

- `i=j`: an explicit singleton-owner term;
- `p_j/p_i<=8`: a short finite interval constrained by compact support;
- `p_j/p_i>8`: a long interior interval where finite squaring is an available internal coordinate.

However, the regions are **not independent positive packets**.  PR #695 proves that the double-owner matrix is a mixed coboundary and that adjacent rectangles telescope through shared oriented boundary interval states.  It also proves that finite squaring has to retain its first-transition packet: the completed core and transition terms carry equal power-sized critical modes.

Consequently the former regionwise assignment

```text
bound diagonal;
bound short region;
bound completed long region;
add positive divisor renewals;
```

is not conclusion-safe.  It destroys both rectangle-boundary cancellation and completed-minus-transition carrier cancellation.

## Divisor-renewal correction

A completion or future monomial `S_df` is a dilation.  PR #671 `L-99961` concerns the restriction `sum_m beta(dm)m^-z`.  No positive-renewal arrow is available until an independent physical source theorem creates a literal divisibility restriction.  The former Region IV and `DOEC100601` formulation are therefore withdrawn.

## Correct matrix frontier

The valid architecture is now

```text
native source
 -> exact double-owner blocks
 -> mixed-coboundary rectangle telescope
 -> inverse-free completed-minus-transition homotopy
 -> one oriented balanced boundary trace
 -> compact wavelet / negative-mass detector
 -> RH.
```

The first four arrows are exact on PRs #691 and #695.  The final balanced one-sided estimate remains open.

```text
double-owner decomposition              PROVED EXACT
double-owner rectangle telescope        PROVED EXACT ON PR #695
finite squaring as internal coordinate  PROVED EXACT
regionwise absolute closure             REFUTED
positive-renewal Region IV               WITHDRAWN
balanced boundary estimate              OPEN / RH-BEARING
Riemann Hypothesis                      UNPROVEN
```

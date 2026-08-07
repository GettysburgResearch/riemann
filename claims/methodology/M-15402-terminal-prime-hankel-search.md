# M-15402 — Phase-aware terminal-prime Hankel search

Claim ID: `M-15402`  
Title: Search the pole-subtracted endpoint Hankel block instead of scalar local potentials  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15404`, `T-15402`, `X-15403`  
Scope: proof-producing positive/negative reconnaissance after the scalar Barta no-go

## Strategic correction

The exact scalar obstruction proves that local positive supersolutions discard
the signed-edge frustration responsible for cancelling terms of order
`exp(a)`. The replacement search must keep the terminal prime reflections and
the polar channel in one correlated matrix.

## Finite packet

Choose real rational splines `phi_1,...,phi_m` supported in `(0,R)`. Form the
odd endpoint packets of `L-15404`. For every pair define the cross-convolution

\[
 C_{ij}(u)=\int\phi_i(u-r)\phi_j(r)\,dr
\]

and the pole vector

\[
 p_i=\int e^{-r/2}\phi_i(r)\,dr.
\]

At support `a`, the terminal arithmetic matrix is

\[
 H_a^{term}(i,j)=
 2\sum_{0\le2a-\log n\le2R}
 {\Lambda(n)\over\sqrt n}C_{ij}(2a-\log n)
 -2e^a p_ip_j.
\]

Add the exact second polar exponential, the fixed small-prime overlap, and every
cancellation-safe archimedean block before any sign is promoted.

## Discovery ladder

1. Start with low-degree compact splines and one fixed `R`.
2. Scan supports using ordinary arithmetic only to nominate negative matrix
   directions.
3. Rank by a complete sensitivity-weighted error estimate, not the midpoint
   eigenvalue.
4. Freeze a finalist to a rational vector.
5. Enumerate the complete terminal prime-power window with directed square roots,
   logarithms, spline evaluations, and accumulation.
6. Evaluate all fixed small primes and archimedean terms independently.
7. Require a strict upper endpoint below zero.
8. Reproduce the terminal manifest and final contraction with an independent
   backend before any candidate status.

## Positive programme

`T-15402` gives a second use. Uniform boundedness of every fixed profile row is
RH-equivalent. A positive attack should seek a structural proof that the
pole-subtracted terminal distribution is translation bounded. Merely proving
that its leading PNT term cancels is insufficient.

The exact obstruction shows what such a proof must control: the zero-spectrum
remainder, not the pole.

## Candidate scheduling

Useful profile families include:

- compact Laguerre-like splines with prescribed Laplace moments;
- polarized pairs whose Laplace transforms target one complex frequency;
- finite orthogonal bases on `[0,R]`;
- profiles satisfying `p_i=0`, which remove the pole/polar rank-one channel
  exactly and expose the zero-sensitive remainder directly.

The last family is especially useful numerically: the enormous leading terms
vanish algebraically rather than by interval subtraction.

## Fail-closed gates

A certificate must reject:

- omission of higher prime powers;
- a terminal window chosen from rounded exponentials;
- independent widening of the pole and polar terms when an exact algebraic
  cancellation is available;
- midpoint profile eigenvectors not frozen to rationals;
- incomplete same-end small-prime contributions;
- profiles touching endpoints without an explicit regularity convention;
- any inference from boundedness on finitely many supports to RH.

## Wider role

This is the direct computational manifestation of the scalar no-go:

```text
local scalar gauge -> impossible;
phase-aware finite Hankel packet -> exact pole cancellation and complete RH
sensitivity.
```

# Brownian high-frequency strike: the raw cofinal stability route is false

**Date:** 2026-08-11  
**Base:** PR #343 at `fed85f2969a5ab9f09890cd89bd6b57ff2115320`  
**Scientific status:** the Riemann Hypothesis remains unproved

## Executive result

The raw one-sided Brownian/Dirichlet-Hermite route was the strongest genuinely independent live proposal in the 2026-08-11 review wave. Its exact finite mathematics survives, but its conclusion-producing theorem does not:

> For every fixed `1/4<sigma<1/2` and every sufficiently large `N`, the raw Brownian numerator `H_N` has infinitely many zeros with real parts tending to `sigma` and imaginary parts tending to infinity.

Therefore no unbounded subsequence of the raw truncations is zero-free in `Re z>1/4`. The cofinal stability hypothesis of PR #343 is false.

The proof is unconditional and does not depend on the finite numerical roots. It combines:

1. the exact positive coefficients of `L-34003`;
2. a selected prime block near `sqrt(N)`;
3. Steinhaus orthogonality to make the unselected-prime residual bounded;
4. a polygon cancellation using the selected prime phases;
5. Kronecker approximation to realise that torus point as a vertical limit;
6. Hurwitz/Rouché to transfer the torus zero to infinitely many actual zeros of `H_N`.

## Why this matters

The route’s prior evidence was local in height: exact `N=2,3,4` stability, strong finite scans, and local-uniform convergence to xi. None of those can see a vertical-limit obstruction at height tending to infinity for each fixed `N`.

This is the same methodological lesson that mattered in Anthropic’s Zeta23 campaign: attack the exact conclusion-producing statistic, and treat a clean refutation as progress rather than forcing a preferred mechanism. Here the “strongest independent route” is not merely still open; its declared cofinal antecedent is false.

## The exact mechanism

Write

```text
H_N(z)=z F_N(z)+G_N(z),
F_N(z)=sum_(n<=N) C_(N,n)n^(-2z).
```

For fixed `sigma in (1/4,1/2)`, construct a completely multiplicative unimodular twist `chi` with

```text
sum_(n<=N) C_(N,n) chi(n)n^(-2sigma)=0.
```

The construction separates primes `2 sqrt(N)<=p<=3 sqrt(N)`. Their coefficients are uniformly bounded below, their multiples are exponentially suppressed, and their total independent phase mass grows like

```text
N^(1/2-sigma)/log N -> infinity.
```

The rest of the Dirichlet polynomial has one twist whose modulus is bounded by the square root of

```text
sum 16 n^(-4sigma)<infinity.
```

The selected phases then cancel it exactly. Rational independence of the prime logarithms gives vertical shifts converging to this twist, and

```text
H_N(z+it_j)/(z+it_j) -> F_(N,chi)(z)
```

locally uniformly. Hurwitz gives the claimed zeros.

## Fixed-height salvage

A second theorem identifies the exact first truncation correction:

```text
m_N(s)
 =2 xi(s)-(2s/(pi N))xi(s-2)+O_K(N^-2).
```

At a fixed simple xi zero `rho`, the nearby raw approximant zero obeys

```text
s_N
 =rho+[rho xi(rho-2)/(pi xi'(rho))]N^-1+O_rho(N^-2).
```

In the `z=s/2` coordinate the coefficient simplifies to

```text
(rho-3)zeta(rho-2)/[(rho-1)zeta'(rho)].
```

This explains the excellent local convergence and the observed `1/N` motion of individual finite-height roots. It also explains why local convergence is not enough: the refuting roots live in a different regime, with imaginary height escaping for fixed `N`.

## Finite diagnostics

The retained standard-library regression reports

```text
PASS_X_90601_BROWNIAN_BOHR_INSTABILITY
```

and checks 3,160 exact coefficient-ratio identities. It finds, among other controls,

```text
H_63(0.2508380937103963 + 55.82354339041126 i) ~= 0,
H_60(0.2526864586875894 + 270.25661198043434 i) ~= 0,
```

with relative residuals around `1e-15`. These are diagnostics only; the asymptotic theorem is analytic.

## Corrected route map

```text
raw finite gamma/Dirichlet/Hermite algebra       retained;
raw N=2,3,4 half-plane stability                 retained;
raw local-uniform convergence to xi              retained;
raw fixed-zero 1/N displacement                  new theorem;
raw all-N stability                              false;
raw all-large-N stability                        false;
raw cofinal stable subsequence                   false;
symmetrized Brownian/Robin canonical system      separate and still open;
Riemann Hypothesis                               unproved.
```

## Next attack after the refutation

Three legitimate Brownian continuations remain:

1. **Height-dependent truncation:** choose `N=N(T)` and prove stability only below height `T`, then diagonalise over xi zeros. The new theorem says global finite-`N` stability is impossible, not that every bounded-height theorem is impossible.
2. **Producer redesign:** modify the finite Dirichlet coefficients so that every vertical-limit polynomial is zero-free in the RH-facing half-plane.
3. **Symmetrized canonical system:** return to the aggregate Brownian/Robin construction, which is not refuted here.

The repository should stop advertising raw cofinal half-plane stability as an open finish line.

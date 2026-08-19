# M-99100 — Proof program for the phase-locked Hermite annular cancellation theorem

## Objective

Prove `PLHAC99100` from `T-99100`. The theorem is fixed-center and source-specific; uniform-center positivity, coefficientwise magnitude, and post-hoc Gram contractions are forbidden by `T-98710` and `R-99100`.

## Prescribed source

Use the Sibuya-decorated fractional source of `L-98710` and the exact fractional owner probabilities `P_(theta,n)` of `L-99103`. Do not expand into colliding generalized-prime histories after integer products have been formed.

## Prescribed scale

For a hypothetical zero `rho=1/2+delta+i gamma`, work only on

```text
log n = 2 delta T + O_delta(sqrt T),
M = floor(2(1/2-delta)^2 T).
```

The high-order notch has already removed the safe-line saddle. Any argument which pays the remaining annulus by absolute values loses the exact factor `exp(delta(1-2delta)T)` and cannot close.

## Source-level martingale decomposition

Apply the logarithmic-owner recursion before summing the integer source. The phase-twisted process

```text
(-1)^t (D_1...D_t)^(-i gamma) f_(theta,gamma)(N_t)
```

is an exact bounded martingale. Expand the notched annular observable into martingale differences and eliminate cross generations by conditional orthogonality.

The desired estimate is a multiplicative Carleson embedding in which the notch's Gaussian/Hermite weight is the predictable test function. A successful proof must retain:

- the complete source index;
- the fixed arithmetic phase `gamma`;
- the annular log-position;
- the exponent decorations at repeated primes;
- and the factor-four finite gauge.

## Bilinear/dispersion form

After one owner step, divisor switching produces a phase-locked bilinear form between generalized-prime powers `d` and descendants `m`, constrained by

```text
log(dm)=2delta T+O(sqrt T).
```

Use a Vaughan/Heath--Brown decomposition only after this source split. The correct large-sieve target is not a source-blind operator norm; it is a martingale-difference square function with the fixed phase `d^(-i gamma)` and actual Sibuya weights.

## Fail-closed success criterion

The final proof must exhibit a positive `eta(rho,theta)` in

```text
exp((delta^2-eta)T+o(T)).
```

A polylogarithmic saving, a mean-square statement averaged over moving centers, or the optimal magnitude rate `delta-delta^2` is insufficient.

## Current boundary

```text
optimal notch identity                 proved exact
notch saddle optimization              proved exact
magnitude-only route                   refuted
phase-locked annulus                    proved exact
fractional owner martingale            proved exact
PLHAC99100 arithmetic Carleson bound    open / RH-bearing
Riemann Hypothesis                      unproved
```

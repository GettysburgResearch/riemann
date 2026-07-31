# X-15604 — Exact Weil-cardinal defect algebra

This experiment replays the finite algebra of `L-15613` and `L-15614`.

It does **not** evaluate the completed zeta function, locate a Riemann zero, or
certify the analytic normalization of the Weil form.  Its inputs are typed
finite zero configurations.

## Exact model

For each distinct centered zero id `omega`, the cardinal vector is represented
only by its values on the zero set.  The polarized Weil Gram is reconstructed as

```text
Q(k_omega,k_nu) = multiplicity(nu) if nu=conjugate(omega), else 0.
```

Additional exact `E`-range radical coordinates contribute zero rows and columns.

A certified critical-line zero may be positively deflated.  The checker
subtracts its positive diagonal contribution and verifies that its cardinal
coordinate becomes an exact residual radical.  Off-line coordinates may not be
deflated.

## Retained controls

### Critical-line-only control

Two line-zero cardinals of multiplicities one and two, together with a
two-dimensional exact radical, have original inertia

```text
positive 2, negative 0, zero 2.
```

After positive zero deflation the complete residual Gram is zero.  With synthetic
block error `1/100`, cross-square `1/400`, and complement floor `1/2`, the exact
Schur floor is

```text
-3/200.
```

This illustrates the cofinal `0^-` mechanism.

### Off-line-pair control

Adding one conjugate off-line pair gives original inertia

```text
positive 3, negative 1, zero 2.
```

After deflating the two line zeros, the off-line pair retains inertia `(1,1)`.
The exact vector `(1,-1)` has

```text
quadratic             -2
coordinate norm^2      2
Rayleigh              -1.
```

The synthetic Schur floor is `-203/200`.  This is a zero-model regression, not
a zeta counterexample.

## Verification

The checker uses only:

- Python integers;
- `fractions.Fraction`;
- exact symmetric congruence elimination;
- exact quadratic and Schur arithmetic;
- JSON and SHA-256.

Ten adversarial tests pass.  They reject broken conjugation, multiplicity drift,
illegal off-line deflation, false inertia, a forged negative witness, a false
Schur floor, a nonpositive complement, and Boolean-as-integer contamination.

## Production contract

A future `DIRECTED_ZETA_ZERO_CONFIGURATION` certificate must independently
bind:

1. the centered `Xi` normalization;
2. every listed zero ball and multiplicity;
3. conjugation and critical-line status;
4. the cardinal-transform normalization;
5. directed tail/form bounds;
6. localized block and cross-map intervals;
7. the complement floor.

A synthetic or midpoint zero list cannot be promoted.

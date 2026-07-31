# Squared-residual lower-floor route to RH

Agent: `gpt56-pro-09-b`  
Date: 2026-07-30  
Issue: #143  
Stacked base: PR #150

## Verdict

I did not obtain a proof of the Riemann hypothesis.

The contribution is a strict weakening of the strongest positive route already
in the repository.  Instead of proving that one localized Weil ground
eigenfunction is simple-even and converges to the explicit CCM prolate target,
it is enough to prove that a sequence of **ambient lower spectral floors** has
negative part tending to zero.

## The new sufficient criterion

Let

```text
mu_lambda = inf spectrum(A_lambda)
```

for the localized Weil operator.  The source proves `mu_lambda` is
nonincreasing as the support grows.  Therefore, if for a cofinal sequence
`lambda_j -> infinity` one proves

```text
mu_(lambda_j) >= F_j,
liminf F_j >= 0,
```

then every fixed localized support has nonnegative Weil form and RH follows.
The `F_j` may be negative at every finite level.

This removes the need for:

- ground-state simplicity;
- parity of an individual ground vector;
- convergence of that vector to `k_lambda`;
- real-zero finite determinants and Hurwitz convergence.

## Block Temple--Schur floor

For a finite packet `S` containing all near-radical prolate modes, write

```text
A = [ B   R* ]
    [ R   C  ]
```

and prove on the complete complement

```text
C - gamma I >= h M,
h > 0.
```

Then

```text
inf spectrum(A)
  >= min(gamma, lambda_min(B-h^-1 R* M^-1 R)).
```

The cross interaction is charged quadratically.  For one trial vector the loss
is

```text
||residual||_(M^-1)^2 / h,
```

not the linear residual/gap ratio needed to control eigenvector distance.

The distinction is exact.  In the retained epsilon family,

```text
residual ~ h ~ epsilon,
distance ratio squared = 1,
energy penalty = epsilon -> 0.
```

Thus the old target-ground convergence condition can fail while the new RH
floor condition succeeds.

## Radical-tail identity

If a Hermitian-form radical vector is split as `r=k+t`, then exactly

```text
Q(k,g) = -Q(t,g),
Q(k,k) = Q(t,t).
```

The CCM target is intended to be the support truncation of a global arithmetic
`E(h_lambda)` vector lying in the Weil radical.  Subject to normalization and
domain review, its entire localized residual is therefore the external tail.

This connects the very small prolate concentration defect to the correct
operator quantity.  The remaining theorem is not ordinary L2 leakage; it is a
continuity estimate for the Weil form in a graph/form norm controlled by that
leakage.

## Literature audit

The July 2026 literature reinforces this diagnosis:

- CCM state that convergence of the explicit prolate candidate to the lowest
  localized Weil eigenfunction is the unresolved positive step.
- The Connes--van Suijlekom simple-even theorem gives real zeros after a suitable
  extremal eigenfunction is established, but does not supply an operator floor.
- Suzuki's localized operators have real-rooted finite characteristic functions;
  convergence remains the global step.
- The 29 July Suzuki finite-element paper observes positive,
  superexponentially small finite eigenvalues but explicitly does not prove RH.
  Conforming Ritz values are ambient upper bounds unless supplemented by a
  lower-bound residual estimator.
- The certified Toeplitz-minor wedge proves a large positivity tail while
  leaving the complementary RH-critical regime open.

## Exact finite verifier

`X-14304` checks the finite block certificate using only integers and
`fractions.Fraction`.  It verifies:

- positive complement metric;
- complete complement coercivity slack;
- exact `M^-1 R` solve;
- the Schur-corrected low block;
- a rational lower floor by exact `LDL*`;
- a separately gated operator-radius loss.

Nine adversarial tests pass.  The synthetic proof-object digest is

```text
bdc5d3a7d70ae9fe048411d2195f6c18de2323015a86c9e85ac8e9fd6de09463
```

## The two remaining analytic blockers

The frontier is now concentrated in two statements:

1. **radical-tail continuity:** prove a norm in which the discarded prolate tail
   controls the localized Weil cross residual;
2. **complete complement coercivity:** prove an ambient lower bound for every
   mode outside the retained prolate packet, including the infinite
   high-frequency tail.

Both are weaker and more local than proving convergence of a chosen ground
eigenvector.

## Recommended computation

At the next available CCM support levels, export a block containing every
observed tiny prolate mode and report separately:

```text
complement floor h,
cross residual norm R,
linear ratio R/h,
squared penalty R^2/h,
Schur-corrected block floor,
ambient assembly radius.
```

A stable linear ratio with a decaying squared penalty would be direct evidence
that the new theorem has removed the previous false bottleneck.

## Status

- `L-14308`, `L-14309`, `T-14302`, `M-14302`: `PROPOSED`.
- `X-14304`: exact finite arithmetic and synthetic controls.
- No production CCM lower-floor packet exists yet.
- No RH proof is claimed.

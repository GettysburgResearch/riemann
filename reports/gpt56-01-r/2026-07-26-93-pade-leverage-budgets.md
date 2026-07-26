# Report — Christoffel–Padé residual-mass budgets

Agent: `gpt56-01-r`  
Issue: #93  
Date: 2026-07-26

## Result

Concurrent PRs independently proved positive-anchor recurrences and the generic
fixed-response line-mass inequality. This contribution was narrowed and
renumbered before review:

```text
L-9316  Christoffel–Padé optimized-gap and residual-segment theorem
X-9314  exact residual-mass budget checker
```

L-9316 identifies the two distances from a one-node Padé scalar to its feasible
interval as exact positive extremal integrals. The minimizing endpoint
polynomials provide lower and upper leverage kernels for every positive piece
of the residual RH measure.

This yields the finite contradiction predicate

```text
upper(total directed Padé gap)
<
lower(proof-gated residual-submeasure contribution).
```

The right side accounts for only a certified subset of the positive RH measure,
so it cannot exceed the total gap under RH.

## Relationship to L-12103

L-12103 proves the general fixed-response budget for multi-anchor ladders.
L-9316 adds the optimized Padé gap identities, global monotonicity of those
optimized gaps, the support-aware upper endpoint, and safe far-endpoint residual
segments.

## Atomic and segment budgets

The atomic form uses pairwise-disjoint critical-line zero bins not already
removed from the residual table.

The strengthened form handles safe far-endpoint deflation. If an actual squared
distance lies in `[L,U]` and was subtracted at `B>=U`, the residual factor
contains common positive Lebesgue measure on `[U,B]`. X-9314 lower-bounds its
contribution by

```text
multiplicity * (B-U) * inf leverage on [U,B].
```

This prevents double counting and makes the checker directly compatible with
the count-shell/far-endpoint tables already produced in PR #103 and PR #105.

## Why this matters

The test composes directly with:

- PR #132's PA-3/PA-7 rational near-null directions and L-12103;
- PR #108's saturated sign-chain zero bins;
- PR #107's selected-factor removal;
- PR #110's complete-slab support edge;
- PR #127's support-aware Padé endpoint polynomials.

It can detect an impossible mass budget without first rebuilding a fully
deflated completed-ξ moment table. The leverage intervals rank zero-bin or
segment-endpoint refinement by witness-specific value rather than width or
distance alone.

## Exact checker

X-9314 uses only integer/Fraction interval arithmetic. It verifies endpoint
normalization, atomic anti-overlap, proof-gate status, support containment,
polynomial interval evaluation, positive denominators, atomic/segment measure
weights, and the strict final comparison.

Eight adversarial tests are included. Synthetic controls give one consistent
atomic budget, strict lower/upper atomic contradictions of `-1/10` and `-1/20`,
and a strict far-endpoint segment contradiction.

## Counterexample status

No Riemann-ξ residual-mass budget has yet been assembled, and no negative is
claimed. The theorem and checker expose a new finite use for the already
expensive PA-3/PA-7, zero-bin, safe-factor, and moment artifacts.

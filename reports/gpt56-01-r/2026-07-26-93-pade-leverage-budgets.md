# Report — Christoffel–Padé residual-mass budgets

Agent: `gpt56-01-r`  
Issue: #93  
Date: 2026-07-26

## Result

L-9314 identifies the two distances from a one-node Padé scalar to its feasible
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

## Atomic and segment budgets

The first form uses pairwise-disjoint critical-line zero bins not already
removed from the residual table.

The strengthened form handles safe far-endpoint deflation. If an actual squared
distance lies in `[L,U]` and was subtracted at `B>=U`, the residual factor
contains common positive Lebesgue measure on `[U,B]`. X-9312 lower-bounds its
contribution by

```text
multiplicity * (B-U) * inf leverage on [U,B].
```

This prevents double counting and makes the checker directly compatible with
the count-shell/far-endpoint tables already produced in PR #103 and PR #105.

## Why this matters

The test composes directly with:

- PR #108's saturated sign-chain zero bins;
- PR #107's selected-factor removal;
- PR #110's complete-slab support edge;
- PR #127's one-node Padé candidates.

It can detect an impossible mass budget without first rebuilding a fully
deflated completed-ξ moment table. The leverage intervals rank zero-bin or
segment-endpoint refinement by witness-specific value rather than width or
distance alone.

## Exact checker

X-9312 uses only integer/Fraction interval arithmetic. It verifies endpoint
normalization, atomic anti-overlap, proof-gate status, support containment,
polynomial interval evaluation, positive denominators, atomic/segment measure
weights, and the strict final comparison.

Eight adversarial tests pass. Synthetic controls give one consistent atomic
budget, strict lower/upper atomic contradictions of `-1/10` and `-1/20`, and a
strict far-endpoint segment contradiction.

## Counterexample status

No Riemann-ξ residual-mass budget has yet been assembled, and no negative is
claimed. The theorem and checker expose a new finite use for the already
expensive zero-bin, safe-factor, and moment artifacts.

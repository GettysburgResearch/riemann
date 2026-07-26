# Report — Christoffel–Padé line-mass budgets

Agent: `gpt56-01-r`  
Issue: #93  
Date: 2026-07-26

## Result

L-9314 identifies the two distances from a one-node Padé scalar to its feasible
interval as exact positive extremal integrals.  The minimizing endpoint
polynomials provide lower and upper leverage kernels for every residual
critical-line zero.

This yields a new finite RH contradiction predicate:

```text
upper(total directed Padé gap)
<
sum proof-gated disjoint-bin multiplicity * lower(bin leverage).
```

The right side accounts for only a certified subset of the positive RH measure,
so it cannot exceed the total gap under RH.

## Why this matters

The test composes directly with:

- PR #108's saturated sign-chain zero bins;
- PR #107's selected-factor removal;
- PR #110's complete-slab support edge;
- PR #127's one-node Padé candidates.

It can detect an impossible mass budget without first rebuilding a fully
deflated completed-ξ moment table.  The same leverage intervals rank zero-bin
refinement by witness-specific value rather than width or distance alone.

## Exact checker

X-9312 uses only integer/Fraction interval arithmetic.  It verifies endpoint
normalization, bin disjointness, proof-gate status, support containment,
polynomial interval evaluation, positive denominators, multiplicities, and the
strict final comparison.

Seven adversarial tests pass.  Synthetic controls give one consistent lower
budget and strict lower/upper contradictions of `-1/10` and `-1/20`.

## Counterexample status

No Riemann-ξ line-mass budget has yet been assembled, and no negative is
claimed.  The theorem and checker expose a new finite use for the already
expensive zero-bin and moment artifacts.

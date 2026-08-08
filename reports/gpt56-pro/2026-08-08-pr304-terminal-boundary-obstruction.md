# Adversarial reconstruction of PR #304: the first terminal boundary is linear

**Agent:** `gpt56-pro`  
**Date:** 2026-08-08  
**Frozen target:** PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
**Verdict:** the displayed complete proof is unproven; its boundary atomic-norm estimate is false.

## Main finding

The proposed proof terminates every finite cutoff source independently through
the adjacent-tree commutator map. Its quantitative hinge is

```text
sum_a ||sigma_a||_at = polylog(X).
```

The exact first aggregate boundary already satisfies

```text
||sigma_0||_at > X/4000.
```

The witness occupies the fixed annulus

```text
49X/100 <= q <= X/2.
```

On this annulus the finite central residual has only the row `2q-1`, while the
analytic central residual retains a fixed positive eta coefficient. The
boundary is therefore uniformly positive of size `X^-1/2`. Since these columns
lie above half of the next endpoint, each is its own unique divisor-source
coordinate. Summing the square-root weights gives a linear norm.

## What survives

The adjacent commutator is still an exact and useful source map. Its
`O(sqrt(m))` capacity bound is also valid. The error is applying that absolute
map to a macroscopic boundary which must remain coupled to the positive flow
that generated it.

## Correct continuation

The next proof attempt should work in PR #272's explicit Pascal-cycle
coordinates on the **difference of the analytic and finite positive flows**.
It should not form the standalone boundary source norm.

No RH conclusion is claimed in this report.

## Exact repair interface

`L-30502` reconstructs the boundary before divisor-source inversion as the
carry image of the difference between the finite stopped central flow and the
infinite analytic central flow. Both constituents are nonnegative. This proves
that the appropriate remaining quantity is the cycle-optimized negative
capacity of their difference, not the isolated source atomic norm. It does not
assert that this optimized debt is small.

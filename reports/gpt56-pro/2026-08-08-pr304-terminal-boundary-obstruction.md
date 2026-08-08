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

After reconstructing the stopped-layer activation exactly, the first aggregate
boundary is

```text
b_X(q)=log(X/(2q-1)) C p(q)-C_X w_X(q).
```

On

```text
2X/5 <= q <= 9X/20
```

one has

```text
b_X(q)<-1/(35 sqrt X).
```

These columns lie above half of the next endpoint, so each is its own unique
divisor-source coordinate. Hence

```text
||sigma_0||_at > X/1500.
```

The first/all-generation polylog source norm is therefore false.

## What survives

The adjacent commutator is still an exact source map, and its `O(sqrt(m))`
capacity upper bound remains valid. The error is applying that absolute map to
a macroscopic activated boundary.

## Exact flow origin and remaining target

`L-30502` proves that every individual stopped boundary is the carry image of a
difference of two nonnegative central flows. It also proves that aggregation
must retain the output activation `Y>=2q-1`; an unqualified sum of the flow
differences is not the aggregate boundary.

A repaired proof must emit the full activated finite/analytic flow manifest and
optimize it in PR #272's Pascal-cycle space before negative capacity is measured.
No smallness theorem for that optimized object is claimed here.

RH remains unproved.

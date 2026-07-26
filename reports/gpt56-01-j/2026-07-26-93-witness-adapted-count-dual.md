# Report — witness-adapted count duals

Agent: `gpt56-01-j`  
Issue: #93  
Date: 2026-07-26

## Result

The current overlapping-count work computes a maximal radial Stieltjes envelope, but a fixed direct-`xi` row can exploit correlations that no single pointwise radial profile preserves. L-9305 gives the exact dual:

```text
A^T lambda <= c  =>  R_beta >= m^T lambda under RH.
```

An integer primal with equal objective proves optimality for the declared rational cell costs.

## Strict separation

The synthetic model has:

```text
raw row                    positive
coarse safe deflation      positive
row-adapted optimum        negative
```

with exact objectives `2` and `17/6`. Seven tests pass.

## Strategic implication

The same expensive Turing count table can now be reused across many cheap two-point direct-`xi` rows. New count endpoints should be ranked by improvement to the active dual objective, not only by improvement to a universal radial profile.

## Counterexample status

No Riemann-`xi` negative was produced. No candidate ID is allocated.

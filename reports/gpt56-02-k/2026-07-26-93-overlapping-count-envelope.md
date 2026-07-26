# Agent report — optimal overlapping interval-count deflation

Agent ID: `gpt56-02-k`  
Issue: #93  
Branch: `agent/gpt56-02-k/93-overlapping-count-envelope`  
Date: 2026-07-26  
Status: theorem and exact synthetic checker complete; Riemann-xi production pending

## Objective

Strengthen the total-count direct-xi route after L-9303. Nested symmetric counts
discard exact information from overlapping and one-sided Turing windows.

## Breakthrough

For atom cell counts `x`, every exact interval count is one consecutive-ones
equation `A x=m`. The least count forced into a symmetric target window is the
exact LP

```text
min q_R^T x
subject to A x=m, x>=0.
```

The interval matrix is totally unimodular. One integer primal and one rational
unrestricted dual certify the optimum exactly.

Running this at all mirrored endpoint radii produces the pointwise minimum
cumulative squared-distance count across every RH-compatible zero configuration.
That step function is the maximal common Stieltjes submeasure forced by the
entire exact count table.

## Strict gain

An exact synthetic table with counts `21,21,22` on two overlapping and one full
interval forces twenty inner zeros. The raw Loewner row is positive; assigning
all twenty-two zeros to the outer radius remains positive; the optimal
overlap-derived profile is strictly negative.

## Verification

```text
9 exact adversarial tests pass
raw row                         positive
outer-only deflated row         positive
optimal profile row             negative
unresolved rows                 0
```

The checker rejects false counts, bad primal or dual data, wrong semantic gates,
missing breakpoints, decreasing profiles, and Boolean counts.

## Counterexample status

None. The strict negative is a synthetic separation only.

## Next offense

Use exact asymmetric total-count windows around new high-height nominees. The
primal-dual profile tells us which additional endpoint can most strengthen the
active direct-xi row, so Turing evaluations become adaptive rather than a fixed
concentric ladder.

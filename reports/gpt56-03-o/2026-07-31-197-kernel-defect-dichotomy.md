# Report — the final selected-zero kernel has a strict RH dichotomy

Agent: `gpt56-03-o`  
Issue: #197  
Stack: PR #192

## Main result

The corrected kernel form is

\[
 S_K=B_K-Z^*C^{-1}Z.
\]

The correction is negative semidefinite. Therefore it cannot rescue a negative
kernel direction.

If RH is false, an off-line conjugate zero pair of multiplicity `m` supplies an
exact Xi-cardinal difference `h_rho` that vanishes at every selected real zero
and has Weil value `-2m`. On any form/metric-complete kernel hierarchy, its
supported repaired copies give a fixed negative corrected Rayleigh gap.

If RH is true, the complete Weil form and all positive-complement Schur
complements are nonnegative.

Hence the requested cofinal `-o(1)` kernel floor is equivalent to RH once the
complete selected-zero-kernel capture hypothesis is stated explicitly.

## Breakthrough in proof architecture

The result removes a misleading intermediate frontier. There is no further
purely finite Schur or dimension argument that can close the sign. The only
noncircular positive target is complete radical synthesis in the form/metric
norm, including every zero-invisible direction introduced by ambient deficit
capture.

## Exact regression

`X-19701` verifies the signature on a rational model with a nonzero complement
cross map:

```text
raw negative value       -2
corrected value           -17/8
normalized corrected     -17/16
line-only control floor    31/16
```

Nine mutation tests pass locally.

## Status

No proof of RH is claimed. The contribution proves the exact dichotomy and
prevents the final RH-bearing sign theorem from being mislabeled as a routine
tail estimate.

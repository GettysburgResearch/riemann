# R-30501 — The terminal adjacent-commutator proof pays a linear first boundary

Claim ID: `R-30501`  
Title: PR #304's polylogarithmic boundary-source composition is false at the first generation  
Status: **EXACT REFUTATION OF THE FROZEN FULL-PROOF COMPOSITION**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen target: PR #304 head `78b75fc17e27334a9950018528c1c6e083d74820`

## Frozen claims contradicted

PR #304 uses

\[
\sum_a\|\sigma_a\|_{\rm at}
=
O((1+\log X)^B)
\]

as `L-30403.8/T-30401.4`, and then terminates every source separately through
the adjacent-tree map.

`L-30501` reconstructs the active stopped-power aggregation exactly and proves
that the complete first source already obeys

\[
\boxed{
\|\sigma_0\|_{\rm at}>X/1500
}
\qquad(X\ge250).
\]

Therefore the displayed first/all-generation polylogarithmic atomic-norm claim
is false.

## Why source recombination does not repair the claim

The source in `L-30501` is formed after the complete positive stopped-power sum
and all first-generation arithmetic destinations. On

\[
2X/5\le q\le9X/20,
\]

the next endpoint contains no proper multiple of `q`; triangular divisor
inversion forces

\[
\sigma_0(q)=b_X(q)<-1/(35\sqrt X).
\]

There is no further source-level common-destination cancellation in this band.
Keeping stopped layers separate is worse by the triangle inequality.

## Correct verdict

```text
adjacent-tree divisor-source identity          RETAINED
24 sqrt(m) source-to-flow upper bound           RETAINED
logarithmic cost for one already-paired fiber   RETAINED
first aggregate boundary atomic norm polylog    FALSE
all-generation boundary atomic norm polylog     FALSE
T-30401 as a complete RH proof                  UNPROVEN
Riemann Hypothesis                              UNPROVEN
```

This does not lower-bound the optimized signed-flow debt. It shows that PR #304's
specific strategy of terminating each boundary through the absolute source norm
overpays a macroscopic transition state.

## Required repair

`L-30502` shows that every individual stopped boundary originates as a
difference of two positive central flows, but the active-layer condition is
column dependent. A corrected proof must emit the complete activated flow
manifest and optimize it in the Pascal-cycle space before negative capacity is
taken.

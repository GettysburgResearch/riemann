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
\tag{R-30501.1}
\]

as `L-30403.8/T-30401.4`, and then terminates every source separately by

\[
\Phi(\sigma_a)
=
\sum_m\sigma_a(m)E_{m-1}.
\]

`L-30501` proves that the complete **first** aggregated source already obeys

\[
\boxed{
\|\sigma_0\|_{\rm at}>X/4000
}
\qquad(X\ge200).
\tag{R-30501.2}
\]

Therefore (R-30501.1) is false. The terminal-source composition cannot yield
polylogarithmic Cycle Debt by the displayed triangle estimate.

## Why common-destination recombination does not repair the claim

The source in `L-30501` is formed only after:

```text
the full positive stopped-power endpoint sum;
the complete analytic/finite difference;
all first-generation arithmetic destinations.
```

On the annulus

\[
49X/100\le q\le X/2
\]

the next endpoint contains no proper multiple of \(q\). Hence triangular
divisor inversion forces

\[
\sigma_0(q)=b_X(q)>0.
\]

There is no further source-level common-destination cancellation available in
that range.

Keeping the stopped layers separate is worse: by the triangle inequality, the
sum of their atomic norms is at least the norm of their aggregate.

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

This does not show that the optimized signed flow has linear debt. It shows
that PR #304's specific strategy of terminating each boundary source through
the absolute adjacent-commutator estimate overpays a macroscopic positive
boundary state.

## Required repair

The top-annulus source must remain coupled to the positive analytic/finite
flow before the negative-capacity functional is taken. A corrected proof must
construct that coupled flow explicitly; it cannot bound the boundary source
in isolation.

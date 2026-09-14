# Second checkpoint: square-defect descent and debt-free flux

The one-step coherence ratio has an exact quadratic dual. For any positive
scale `lambda_k`, every wrong extremum contributes at least one unit to

```text
sum_c (1 + lambda_k rho_(k,c))^2.
```

Summing these defects over a derivative block gives an additive reverse-Rolle
loss budget. Optimizing `lambda_k` recovers the familiar first/second residue
coherence, but no ratio is needed in the analytic formulation.

The canonical second-moment contour from PR #723 has poles at zeros of the
next derivative. At a fixed finite window these poles can be removed exactly:
interpolate the residue values on the current derivative-zero set and use

```text
(F_(k+1)/F_k) (1 + lambda_k U_k)^2.
```

Its residues are the desired square defects and it has no adjacent-derivative
poles. The new cost is the boundary growth of `U_k`, which is explicit and
source-matched. This exposes a direct bridge to de Branges/Pick interpolation.

The exact remaining cut is `IBFC105222`: a combined boundary-flux estimate
below 1.73991107% of the common zero count for the literature-instantiated
three-level 90% target, or `o(N)` for density one.

Neither estimate is proved here. RH remains unproved.

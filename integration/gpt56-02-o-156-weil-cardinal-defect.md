# Integration handoff — Weil-cardinal defect packets

Target stack: Issue #156, PRs #159, #161, #163.

## Import

- `L-15613`: exact cardinal defect Gram and off-line negative block;
- `L-15614`: positive critical-line zero deflation makes line-cardinal vectors
  exact residual radicals;
- `R-15602`: localized `L2` density does not imply small exterior form tail;
- `T-15603`: corrected cofinal trace-tail/Schur theorem;
- `X-15604`: exact finite algebra checker.

## Revised packet

Replace

```text
R_lambda + evaluation-visible V_lambda
```

by

```text
exact E-range radicals
+ cardinals for proof-grade critical-line zeros
+ unresolved defect.
```

Subtract the positive finite zero form before the packet calculation.  The first
two summands are then exact radicals of the residual Weil form.

## Production sequence

1. Choose a proof-grade finite line-zero set `Z_j`.
2. Produce directed cardinal transforms and Hardy/form tail bounds.
3. Form the residual positive deficit operator
   `D_tilde=D_(j,G)+Q_(Z_j)`.
4. Build the packet from exact E-radicals and line-cardinals.
5. Certify
   `Tr((I-P_L)D_tilde) <= G/2`.
6. Certify growing-packet compression `alpha_j` and cross residual `beta_j`.
7. Apply
   `F_j >= -alpha_j-2 beta_j^2/G_j`.
8. Preserve every unresolved off-line-style defect; it may not be positively
   deflated.

## Search implication

The finite line-visible block is no longer the main arithmetic sign problem.
The exact remaining object is the uncaptured positive-defect trace.  A generic
periodized E-range density argument cannot close it, because an off-line
cardinal difference has fixed negative Weil value while still admitting local
`L2` approximation with escaping exterior form norm.

## Nonclaim

No cofinal positive-defect trace bound is supplied.  RH remains unproved.

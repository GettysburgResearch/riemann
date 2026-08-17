## Standalone hostile reconstruction of the parity-resummed factor-67 route

```text
frozen base PR:  #566
base SHA:        2407b4ffe5024a2e3898922cf0b722d5cf69e496
mandatory input: #574 @ 74fba7f3e55fa9a53d1eb814e5067f5011ef5e86
mandatory input: #575 @ 265c481ebd02807ab7d9a95cb0cf905a22c1876f
head branch:     paper/arxiv-parity-completed-scalar-lorenz-v3-final
```

This paper uses manuscript writing as a hostile reconstruction rather than an exposition pass. It withdraws the unproved concrete use of `L-96651` and proves the strongest exact replacement.

## Main result

The literal completed-parity source reduces at each real endpoint to one exact finite scalar Lorenz program. If the uniform inequality `CPSL67` holds, then

```text
CPSL67
 -> 5c_X(2)+3c_X(3) >= 0 eventually
 -> exact reciprocal-zeta Mellin transform
 -> Landau
 -> RH.
```

The finite primal, explicit fractional-knapsack formula and one-parameter dual are proved exactly. The dual shows that `CPSL67` already contains the conclusion-producing scalar sign. It is the first unsupported and RH-bearing arrow.

## Mandatory corrections incorporated

- PR #574: `H^T K`, owner ordering, and Cauchy–Binet transport only determinant signs; TP2 does not imply target capacity.
- PR #575: scalar exactness does not lift to rows two and three; the route remains scalar.
- PR #561: the odd-history `(67)` witness at `X=61841` is binding and rules out leafwise canonical Hall.
- The compact-plus-MPFR terminal theorem is retained only in canonical local orientation.
- Target-active scalar-zero atoms and both activation sides are included.

## Validation

The independent verifier checks exact finite source algebra, history parity, causal coefficient cancellation, the scalar/two-row tradeoff, rational Lorenz primal/dual identities, the odd-history witness, and the Mellin numerator. It explicitly records:

```text
L96651_proved=false
CPSL67_proved=false
terminal_51M_campaign_rerun=false
rh_established=false
```

The deterministic ZIP, compiled PDF, full TeX source, checksum ledger, patch and publisher are mirrored in the connected Google Drive folder and attached in the session handoff.

## Exact status

```text
complete standalone reconstruction      YES
complete unconditional RH proof         NO
strongest exact theorem                 CPSL67 -> RH
first unsupported arrow                 uniform CPSL67
Riemann Hypothesis                       UNPROVEN
```

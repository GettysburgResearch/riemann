# One-shot exact-root SONTR / NRCT hardening

Date: 2026-08-15  
Repository: `gfreund123/riemann`  
Base: PR #486 at `0d8badeda73626598a74dc3ef009b67a74af3b81`  
Reviews answered: PR #482 and PR #484

## Status

This packet hardens the canonical one-shot factor-67 proposal in three ways:

1. Hall is integrated exactly as a measurable kernel, so activation collars and
   mesh refinement disappear from the controlling proof.
2. Every causal child remains an internal positive colour of one total parent
   row. The exported recursive child family is empty.
3. The complete native root slack is bounded directly in the `Y_4` metric by
   an explicit absolute constant below `61000`; the RH-bearing estimate
   `J_Lambda(X)-4sqrt(X)=O(log X)` is absent.

The packet is a complete RH proof proposal for independent frozen-head review.
RH is not treated as accepted before that review.

## Controlling files

```text
R-91754  benchmark-bridge firewall
L-91754  exact measurable whole-cell Hall integration
L-91755  one-shot port-free total-row identity
L-91756  explicit native slack <61000
T-91752  SONTR/NRCT and endpoint composition
O-91754  review DAG and falsifiers
X-91754  exact finite algebra and constants
```

## Main output

For every integer `X>=10^12`, the construction gives one nonnegative finite row
`d_X` satisfying

\[
 C_{d_X}\le w_X,
 \qquad
 \Xi_{d_X}\le\Omega_X,
\]

and

\[
\boxed{
0\le J_\Lambda(X)-\mathcal H(d_X)
 =\sum_qY_4(q)[\Omega_X(q)-\Xi_{d_X}(q)]<61000.
}
\]

All source-owned child colours are already contained in `d_X`; no child is
exported. Thus SONTR and NRCT hold with an empty recursive family. The resident
complete-prime-power endpoint theorem gives the proposed implication to RH.

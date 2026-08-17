# T96500 integration handoff

UTC cutoff: 2026-08-16T23:52:55Z

## Base

```text
PR #550 head: 20646a78c3e8843001cb49ea0c9741f6d0d446f7
PR #534 head: ef18bdda5a65334695008e4c1f5986833160d84f
main observed: 994bd4bedcc8b61cebabaf005cc69225fc3fe459
```

## Integration verdict

Do not integrate PR #550's parity-blind L-96302 composition as a proof of
full-row positivity. Preserve its exact Mellin consumer and canonical-orientation
Target-Lorenz certificates at their stated scopes.

Integrate this successor as a correction/no-go packet:

- L-96500: parity-covariant gluing;
- L-96501: exact activation and magnitude covariance;
- R-96500: explicit odd-history obstruction;
- L-96502: exact depth-L source expansion;
- R-96501: fixed-depth positive-reset no-go;
- L-96503: global common-source primal-dual theorem;
- T-96500: GPHT23 conditional RH reduction.

## Exact boundary

```text
parity-blind local gluing                 refuted as argument
fixed-depth local repair                  refuted
full-row/two-row positivity               open / not refuted
global GPHT23 producer                    open / RH-bearing
two-row Mellin-Landau consumer            exact
Riemann Hypothesis                        unproved
```

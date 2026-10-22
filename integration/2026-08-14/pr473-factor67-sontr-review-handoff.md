# Integration handoff — PR #473 factor-67 SONTR review

```text
reviewed PR:            #473
reviewed head:          71d6a859ea741fe035de709e8d10ed37301b778e
reviewed tree:          036365630b50cde18929715fa9d9211434821a09
review cutoff UTC:      2026-08-14T20:19:52Z
main at review:         9c7538559d7f56c2914b39aed5a1fb3fbf7ce131
```

## Verdict

```text
compact Hall/reserve layer                 VERIFIED WITH FROZEN INPUTS
global grouped-child mass normalization    UNPROVEN / GAP
T-91660 / T-91661                          UNPROVEN / GAP
Riemann Hypothesis                         UNPROVEN
```

## First open arrow

```text
fiberwise causal children
  -> positive endpoint direct integral
  -> grouped unit-target-mass child packets
  -> normalized coefficients summing below 1/8
```

PR #473 proves the per-packet coefficient inequality but not the mass-weighted
direct-integral theorem required by `T-91312`.

## Immediate action

Stack or reconstruct PR #476 `L-91694`, then rewrite the SONTR decomposition
using actual aggregate child target masses. Do not merely reuse one scalar
coefficient list after grouping.

## Retain

- exact Hall total-row transparency;
- `159/500 < L < 183/100`;
- `C67<19`;
- interior reserve `41 Omega/[32(K+178)]`;
- terminal reserve `581 X^(-3/2)`;
- narrow aggregate Schur-port summation.

## Fix

- `T-91660` false editorial display `b*=bar b*`;
- path/blob-complete dependency scopes;
- explicit mass-normalized grouped-child identity.

No integration or merge is recommended until the repaired stack is reviewed.

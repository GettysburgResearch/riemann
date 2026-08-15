# Claim-status audit — Target-Lorenz vector primal/dual packet

Audit date: 2026-08-14  
Origin PR: `#468`  
Origin parent: `a41f81466f85d52597c97b41505756a8860698d0`  
Renumber cutoff: `2026-08-14T19:56:18Z`  
RH status: **unproved**

## Collision disposition

Temporary files using `L/R/O/T/X-91685--91687` were published before live
PRs #469--#475 became visible. Those descendants independently use the same
claim numbers. The packet is normatively renumbered to `91720+` and the
temporary paths are deleted. No mathematical assertion is strengthened by the
renumbering.

## Exact claims proved in this packet

### `L-91720`

For an ordered even source with positive target capacities, a cone-decreasing
physical-vector-per-target profile and an increasing score-per-target profile,
the leftmost exact-target removal simultaneously maximizes the physical vector
and minimizes score. The cutoff formulas are exact LP dual certificates.

A failed physical coordinate separates every exact-target common-source
submeasure, not only the greedy removal.

PR #470 independently proves the corresponding leftmost-basis statement for
the live stopped-leaf box LP. The present claim is the abstract ordered-cone
form with explicit dual functionals.

### `R-91720`

The global reduction of the causal target cutoff to
`sqrt(y)(sqrt(p)+1)` is false because the child term switches off at `d=y`.
The displayed same-scalar pair gives an exact algebraic counterexample. The
correct target cell variables are `(sqrt(py),sqrt(y))` with fixed activation
indicators.

### `L-91722` full signed determinant lower bound

The unused even source is a right-tail target submeasure, so its row is bounded
by the cutoff ratio times its exact target. This gives a sufficient full
signed-packet determinant for every Lorenz margin.

### `L-91721` support-easy reduction

If the target cutoff `c` lies at or beyond `py/j`, all nonzero row coordinates
have already been consumed by the removal, so the Lorenz margin equals the
complete signed causal row.

## Conditional claim

### `T-91720`

The implication

```text
AVLT + ANRL -> NRCT -> endpoint deficit o(log^2 X) -> proposed RH conclusion
```

is conditional and applies only to the Target-Lorenz fallback route.

It does not classify the newer factor-67 SONTR proposal on PR #473 as proved.
That proposal requires independent reconstruction of its finite realization,
source ownership, reserve, common-port, and endpoint-consumer imports.

## Discovery only

`recon.py` scans 17,160 structured cases and finds no negative margin. Its
minimum is at `(p,y,j)=(67,1,66)`, in the already proved first quotient cell.
Binary64 reconnaissance is not a theorem about the remaining real cells.

## Explicitly not established by this packet

```text
all stopped-leaf Target-Lorenz row margins    NOT PROVED
factor-67 SONTR frozen stack                  NOT INDEPENDENTLY RECONSTRUCTED
Native-Root Capacity Theorem                  NOT ACCEPTED
CFFP                                           NOT ACCEPTED
Riemann Hypothesis                             NOT PROVED
```

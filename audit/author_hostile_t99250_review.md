# Author hostile audit — T-99250

Status: **internal adversarial review, not an independent acceptance review**  
Frozen intended base: PR #642 head `07aa0d4838458a1b2d3af9e5bc96616baa6b4767`

## Verdict by interface

### PR #642 SHARP kernel

The elementary convolution identity, cumulative moment formula, and analytic
positivity proof were independently re-derived. No counterexample was found.
The kernel theorem is treated as exact at its stated fixed-row scope.

### Child source map

The phrase “endpoint restriction” can be read too strongly. A bare support cut
of the parent kernel measure is not the child measure. The exact source map is

\[
R_{Z\mid Y}(t)
=\mathbf1_{t\le Z}T(Z/t)/T(Y/t).
\]

This repair is proved in `L-99250`. It also proves normalized-profile
monotonicity and gives a literal random-key common parent.

### Compact Hall

The complete finite base was re-evaluated with exact rational square-root
intervals. The worst SHARP prefix remains `t=13`, `x=67` and is strictly above
`7/20`. Replacing SHARP by the older equality target makes the same state less
than `-3/10`; the target choice is load-bearing.

### Global source tree

The positive kernel does not by itself prove the signed scalar `Psi`
nonnegative. Rather than silently importing an endpoint frame or claiming that
finite Hall data decide the unbounded state, `T-99250` removes the global tree
from its conclusion-facing path and states one scalar Harnack tail explicitly.

### Factor-67 scalar

The coefficient reindexing gives the exact local square `(1,-2,1)`. The direct
Mellin transform has no positive-real singularity and cannot lose an off-line
zero to the 67 factor. The Landau implication is valid if the global scalar
sign is supplied.

### Computation

The `2^50` producer was rerun from source through `10^8`; stdout is retained.
The fast verifier separately reconstructs the exact interval at the reported
minimizer. Raw support cutoff, wrong target, and false global status are
binding negative controls.

## Final audit boundary

```text
kernel algebra/positivity                   survives reconstruction
RN child/common-parent map                  repaired exactly
compact Hall base                           survives exact replay
local square and finite H67 sign            survives exact replay
direct Mellin-Landau consumer               survives reconstruction
global H67 tail                             unproved
accepted RH proof                           no
```

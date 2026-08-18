# Q4: one-sided subpower closure and exact moment compression

## Executive result

The published `SACF` gate asks for an absolute polylogarithmic estimate.  The
quadratic identity shows that both requirements are stronger than necessary.
The negative cross correlation is automatically bounded by the already-closed
diagonal, so only an upper estimate is needed.  Moreover, an `X^o(1)` upper
bound is enough for Mellin holomorphy throughout `Re s>0`.

The new gate is

```text
UOSACF: S_H(X) <= X^o(1)
```

for one polylogarithmic separation threshold.  It still implies RH and remains
open.

The pass also expands each exact Q4 band-pair kernel into fifteen universal
squarefree power-log moments and gives an exact lcm-based formula for every
moment.  This removes the analytic kernel from the remaining arithmetic
estimate and leaves a finite family of one-sided outer Möbius/divisor forms.

## Boundary

```text
one-sided/subpower reduction       PROVED
finite moment compression          PROVED
UOSACF                             OPEN / RH-BEARING
RH                                 UNPROVEN
```

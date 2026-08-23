# T-105200 interface with the reviewed T-105101/T-105102 parent additions

Frozen parent branch: `codex/105100-residue-second-moment`  
Parent head reviewed here: `0c1aedcafe7c6fe384695eee64435cc87b792aea`  
Continuation branch: `research/gpt56-pro/105200-xi-residue-geometry`  
RH status: **unproved**

PR #723 added two exact sharp-window identities after this continuation branch
was originally forked:

- `L-105101`: the rectangular second-residue flux;
- `L-105102`: the paired first/second residue-coherence flux.

The T-105200 packet is compatible with, and strictly complementary to, those
identities.

## Sharp-window coordinate

For one regular rectangle, `L-105101--L-105102` give the exact hard-cutoff
ledger

```text
real critical moments
 = oriented four-edge contour charges
 - nonreal critical corrections
 - adjacent-derivative debt.
```

Its advantages are exact height support and direct entire-function validity.
Its open costs are boundary-charge estimation, a uniform thin-strip choice,
nonreal corrections and the adjacent-derivative debt.

## Smooth Poisson coordinate

`L-105200` replaces the hard cutoff by

```text
Omega_(a,T)(x)=[T^2/((x-a)^2+T^2)]^3.
```

The count, first residue moment and second residue moment then use the same
positive real-axis weight and one universal boundary differential at the two
points `a +/- iT`.  For Xi, `L-105202` moves those points to the zero-free real
axis and evaluates the main carriers by Stirling asymptotics.

`L-105201` additionally constructs a finite Bézout correction which removes
the complete adjacent-derivative debt pointwise.  Its entire analogue is the
open interpolation gate `EBCI105200`.

## Combined use

The two coordinate systems should not be identified term by term:

```text
sharp rectangle: exact finite-height support and four-edge bookkeeping;
smooth Poisson:  common positive weight and zero-free-axis main terms.
```

A valid continuation may use the sharp identity to control leakage between
neighbouring windows and the smooth identity to evaluate the bulk moment
carrier.  Any such comparison must retain the same derivative level,
nonreal-critical correction and common-zero/multiplicity ledger.

No theorem in either packet currently bounds all correction terms.  The exact
combined frontier remains:

```text
entire Bézout interpolation with controlled growth;
nonreal-critical first and second residue corrections;
sharp-to-smooth leakage on one derivative/height schedule;
summable reverse-Rolle descent.
```

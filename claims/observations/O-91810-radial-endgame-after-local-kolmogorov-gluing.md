# O-91810 — Radial endgame after local Kolmogorov gluing

Claim ID: `O-91810`  
Status: **CURRENT BOUNDARY / EXACT REDUCTION**  
Created: 2026-08-13  
Depends on: `L-91800`--`L-91804`, `L-91810`, `L-91811`  
RH status: **unproved**

## Freeze

```text
parent PR:      #430
parent head:    cedf2f5b43c99d6e6f9a760236432b123dd91770
branch:         research/gpt56-sol/91810-radial-log-derivative-locality
```

## What changed

PR #430 left `RLSL` as construction of an interval-natural completed source/model morphism. Two parts of that burden are now removed.

`L-91810` proves the visible completed Xi transfer itself already has an exact additive logarithmic cocycle in horizontal depth. Zero crossings are exactly the point-depth singularities of that radial logarithmic derivative.

`L-91811` proves that once positive source/model kernel measures are available interval by interval, their minimal Kolmogorov systems glue canonically. Interval naturality of the Hilbert map is then automatic; it is not a second independent construction problem.

## New sharp gate

The remaining theorem can therefore be stated without existential colligations:

> **Radial Kernel-Measure Domination (RKMD).** On every finite carrier/delay/orientation/bridge packet and every half-open rational depth interval `I`, construct the completed arithmetic kernel measure and the critical/stable/hyperbolic model kernel measure so that
>
> \[
> C^{\rm model}(I)\preceq A^{\rm arith}(I),
> \]
>
> compatibly under refinement.

Because the arithmetic source is diffuse while the hyperbolic crossed-zero component is pure point, RKMD plus `L-91802/L-91803/L-91811` forces the hyperbolic component to vanish.

## Why this is narrower than the old gate

The old formulations asked for one or more of:

```text
an explicit global source-to-model isometry;
a canonical output allocation;
a global kernel defect plus a carrier-height decay rate;
a separately postulated interval-natural Fock morphism.
```

RKMD asks only for an intervalwise Loewner inequality between two explicitly defined positive kernel measures. The lurking/module map and the spectral-type conclusion then follow functorially.

## Exact boundary

```text
arithmetic prime/eta/bridge/gamma radial diffuseness    EXACT/parent
crossed-zero hyperbolic depth is pure point             EXACT/parent
diffuse source cannot dominate target atoms             EXACT/parent
completed scalar Xi transfer is interval additive       EXACT/L-91810
local kernel systems glue to module map                  EXACT/L-91811
separate RLSL morphism-construction burden               REMOVED
RKMD intervalwise kernel-measure domination              OPEN / RH-BEARING
Riemann Hypothesis                                       UNPROVED
```

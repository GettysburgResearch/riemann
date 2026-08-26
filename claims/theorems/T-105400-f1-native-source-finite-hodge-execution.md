# T-105400 — Finite F1 native-source Hodge realization and exact cofinal frontier

Claim ID: `T-105400`  
Status: **PROVED FINITE REALIZATION / COFINAL TRACE FRONTIER OPEN**  
Created: 2026-08-23  
Frozen programme: PR #727 at `71782530d175162040a8c182a4cb1602d2b23821`  
Frozen arithmetic input: PR #719 at `fb71bd7e191aab615beb94711ba35abec3691032`  
RH status: **unproved**

The first execution pass proves the following.

```text
native labelled Euler source
 -> twisted cubical corner boundary                    PROVED EXACT

completion tangent
 -> one divisor coefficient per labelled prime         PROVED EXACT

least/greatest/double owner
 -> shellings/strata of the same finite source         PROVED EXACT

source-twisted toric product
 -> exact Hodge-index form and uniform primitive gap    PROVED EXACT

three filtered SHARP rays
 -> one primitive mixed intersection                    PROVED EXACT

Lorentz current
 -> optimal bound by a carrier-free primitive energy    PROVED EXACT
```

The programme's initial polymatroid-only formulation is repaired: the finite
geometry is the toric prime box with the native source carried as a twisted
coefficient module. Activation is a moving tropical section of this fixed
source geometry.

## Exact conclusion-facing reduction

For the PR #719 current,

\[
|5A-G|^2
\le
\frac{769}{2}
\frac{49A^2-96AG+48G^2}{24}.
\]

The right side is exactly one third of the sum of the three pairwise
carrier-free ray-difference squares.

Thus the remaining arithmetic theorem is

```text
F1PE105403:
subpower block integral of the primitive three-ray Hodge energy.
```

It is an arithmetic trace/occupancy theorem, not another finite Hodge-sign
problem. It is source-compatible with the half-divisor near-collision,
same-kernel cross-core, and completion-defect programmes.

## Current programme disposition

```text
NPR105300 finite native source functor              PROVED as L-105400
AHG105301 finite degree-one Hodge gap                PROVED as L-105401
three-ray primitive realization                     PROVED as L-105402
finite mixed trace inequality                       PROVED as L-105402
cofinal arithmetic trace/occupancy                   OPEN as F1PE105403
fixed-detector composition                          PROVED CONDITIONALLY
Riemann Hypothesis                                  UNPROVED
```

No finite signature statement is promoted to RH. A later pass on this same PR
should attack `F1PE105403` by an adelic/gcd trace decomposition, preserving all
three ray differences until after carrier cancellation.

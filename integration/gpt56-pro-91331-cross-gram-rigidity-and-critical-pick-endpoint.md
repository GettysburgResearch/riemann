# Integration handoff — cross-Gram rigidity and the exact critical Pick endpoint

## Freeze

```text
parent PR:      #400
child PR:       #429
parent head:    7dc9fec9eb5fab4ee9340ddbc5a52e36a6ab617e
prior child:    90ef3725e4b405ba77a888d1dc623886d0e029db
session date:   2026-08-13
RH:             unproved
```

Read the current child head from GitHub after publication.

## I. The all-scale fixed-contraction architecture is rigid, not contractive

`R-91331` proves the general theorem:

```text
V_alpha and M_alpha isometries;
C one fixed contraction;
C V_alpha = M_alpha for every alpha
```

implies

```text
C is isometric on the closed span of all Ran(V_alpha);
V_alpha* V_beta = M_alpha* M_beta for every pair;
source and output normal curvatures are identical;
all L-91305 defect/reserve terms vanish on the actual curve.
```

Thus an exact fixed Hilbert contraction between isometric curves cannot be a
strict curvature data-processing mechanism. It can only be an isometric
realization of the complete output cross-Gram kernel.

For the completed Fisher source,

```text
V_a*V_b = rho(a,b) I,
0<rho(a,b)<1 for a!=b
```

by strict log-convexity of `xi(1/2+a)`. For the Suzuki phase,

```text
M_(Theta_a)* M_(Theta_b)
 = M_(conjugate(Theta_a) Theta_b),
```

which is unitary. Hence no fixed contraction can map the completed Fisher
isometries to the Suzuki multipliers at even two distinct scales. `R-91330`'s
speed obstruction remains correct but is subsumed by this stronger global
cross-Gram obstruction.

The abstract identities in `L-91305` remain algebraically correct; their
intended strict-reserve application is normatively superseded.

## II. The sole non-safe scalar channel is exactly `-Xi'/Xi`

`L-91329` localized each physical Cauchy carrier to:

```text
one common analytic safe multiplier D_a;
safe scalar jets at heights 2a and 4a;
one critical xi/xi'/xi'' confluent block at height a.
```

`L-91332` identifies the invariant of that critical block. With

```text
Xi(x)=xi(1/2+i x),
m(z)=-Xi'(z)/Xi(z),
Z_a(x)=xi(1/2+2a+i x),
```

the height-one coefficient pair satisfies

```text
A/B = -i a m(x),
```

and its confluent determinant is

```text
A B' - A' B
 = i a [Xi'(x)^2-Xi(x)Xi''(x)] / Z_a(x)^2.
```

Across independent carriers, the divided-difference polarization is the Pick
kernel

```text
P_m(z,w)
 = [m(z)-conjugate(m(w))]/[z-conjugate(w)].
```

The equivalence is exact:

```text
RH
<=> every zero of Xi is real
<=> m=-Xi'/Xi is Herglotz on C_+
<=> every finite Pick matrix of P_m is PSD.
```

The diagonal first Laguerre inequality alone is insufficient. The full
all-carrier Pick matrices are the critical object, matching the repository's
full-Gram warning.

## III. Correct endgame after all corrections

The present branch has closed or eliminated:

```text
delayed half-line density;
canonical bridge geometry;
raw-delay model-space invariance error;
physical-input model/amplitude/leakage bookkeeping;
normalized Fisher Bochner-domain error;
structured reciprocal-xi domain;
continuous delay analysis;
all unsafe scalar data except one critical confluent channel;
the proposed all-scale fixed-contraction shortcut.
```

What remains is a fixed-scale direct positive-form theorem:

```text
construct the full Pick kernel of -Xi'/Xi,
with the common safe D_a multiplier,
safe height-2/height-4 jets,
reflected orientation,
canonical bridge,
and exact Jordan plus gamma/pole normalization,
from the completed source form without assuming RH.
```

Equivalently, prove the finite source-minus-output matrices of
`L-91327`--`L-91329` positive for every carrier set. This is still RH-bearing
and cannot be obtained from the refuted all-scale Hilbert contraction.

## IV. Correct live status

```text
delayed weighted form core                            PROVED
canonical bridge geometry                             PROVED
full physical Hardy delay colligation                 PROVED
normalized Fisher-Hankel Bochner core                 REFUTED
bounded renormalized source feature                   PROVED
safe Suzuki tangent on all K_Theta                    PROVED
continuous delay -> finite pole jets                  PROVED
one critical xi/xi'/xi'' block isolated               PROVED
all-scale fixed isometric contraction reserve         IMPOSSIBLE
critical channel = Pick kernel of -Xi'/Xi             PROVED
source construction of that full Pick kernel          OPEN / RH-BEARING
mixed orientation and bridge arithmetic rows          OPEN
Riemann Hypothesis                                    UNPROVED
```

# C-91333 — Normative supersession map for the delay/Fisher/colligation line

Claim ID: `C-91333`  
Status: **NORMATIVE CORRECTION AND SUPERSESSION MAP**  
Created: 2026-08-13  
Applies to: `L-91305`, `L-91309`, `L-91316`, `L-91322`, `L-91323`  
Controlled by: `R-91324`, `L-91325`, `L-91328`, `R-91330`, `R-91331`  
RH status: **unproved**

## 1. Purpose

The branch was developed in theorem order. Later hostile audits proved that two
Fisher/colligation continuations attached to earlier exact delay lemmas cannot
be retained. This record fixes the normative reading order and prevents the
exact Hardy geometry from being conflated with superseded Fisher conclusions.

Whenever an earlier file conflicts with this record or with the controlling
correction/refutation named above, the later correction controls.

## 2. `L-91322`: exact geometry retained, Fisher appendix superseded

The following parts of `L-91322` remain exact and normative:

```text
Sections 1--4;
compressed backward-shift invariance of K_Theta;
raw delay = resident model state + negative-Hardy leakage;
all cross-delay Gram identities;
resident semigroup and leakage cocycle;
the reflected geometric construction in Section 6.
```

The following parts are superseded and must not be used:

```text
Section 5 as an application of the normalized Bochner operator of L-91316;
equations L-91322.17 and L-91322.18 as Hilbert-space Fisher identities;
the score-orthogonal Fisher reserve asserted after L-91322.18;
the Fisher-dependent conclusion in Section 7;
the corresponding Fisher rows in the Section 8 status table.
```

Reason: `R-91324` proves that the natural pre-projected normalized feature map
used by `L-91316` has domain `{0}`. The corrected source factorization is
`L-91325`, and `L-91328` proves that its structured reciprocal-amplitude
composite is defined on the whole Suzuki model space.

The delay dilation itself is independent of this correction and is unaffected.

## 3. `L-91323`: full physical colligation retained, old Fisher endpoint superseded

The following parts of `L-91323` remain exact and normative:

```text
Sections 1--5;
H2+ = model plus completed-amplitude coordinates;
three-channel model/amplitude/leakage delay isometry;
amplitude-to-model forcing commutator;
all physical cross-carrier and cross-delay Gram identities;
upper-triangular state semigroup and leakage cocycle;
explicit rational Cauchy coordinates and forced resident vector.
```

The following parts are superseded and must not be used:

```text
the invocation of L-91322.17 in Section 6;
the claim that the old normalized Fisher-Hankel reserve applies to the forced
resident packet;
the Fisher-dependent endpoint language in Section 7.
```

The correct continuation is:

```text
forced resident packet                  L-91323, retained;
bounded renormalized source feature     L-91325;
full structured domain                  L-91328;
finite pole-jet reduction               L-91327;
one safe multiplier / critical jet      L-91329;
critical Pick channel                   L-91332.
```

## 4. `L-91316`: pointwise identities retained, dense Bochner operator rejected

Retain:

```text
the finite-carrier covariance identity inherited from L-91312;
the separate model-space shape/Hankel identity L-91316.7.
```

Do not retain:

```text
the declared common dense-core Bochner map A_a;
the global normalized Fisher-Hankel contraction;
the positive score-orthogonal reserve built from that map;
any delayed direct-integral conclusion depending on that map.
```

`R-91324` is the controlling refutation. `L-91325` is the controlling
renormalized replacement.

## 5. `L-91305` and `L-91309`: strict all-scale fixed-contraction route rejected

The algebraic projection identities in `L-91305` remain correct. Their intended
use as a strict curvature data-processing reserve for a genuine family of
source and output isometries is superseded by `R-91331`:

```text
one fixed contraction mapping isometric curves exactly
is isometric on the entire curve span;
it preserves every cross-scale Gram operator;
source and output normal curvatures are equal;
all proposed defect/reserve terms vanish on the curve.
```

The fixed completed Riemann-density source space and normalized tilt curve in
`L-91309` remain exact. The open target of one fixed contraction sending that
curve to all Suzuki phase multipliers is refuted:

```text
R-91330: incompatible tangent speeds at large scale;
R-91331: incompatible cross-Grams at any two distinct scales.
```

Adding another positive channel while retaining an exact isometric source
curve does not evade the cross-Gram rigidity theorem.

## 6. Normative theorem graph

```text
delayed weighted half-line core                      L-91320, PROVED
canonical two-sided bridge geometry                  L-91321, PROVED
resident model/leakage delay dilation                L-91322 Sections 1--4, PROVED
full physical model/amplitude/leakage colligation    L-91323 Sections 1--5, PROVED
normalized Fisher-Hankel Bochner core                R-91324, REFUTED
bounded renormalized random feature                  L-91325, PROVED
safe Suzuki tangent on all K_Theta                   L-91328, PROVED
continuous delay reduced to finite pole jets         L-91327, PROVED
one safe multiplier and one critical xi jet          L-91329, PROVED
all-scale fixed isometric contraction reserve        R-91330/R-91331, IMPOSSIBLE
critical channel = Pick kernel of -Xi'/Xi            L-91332, PROVED
source construction of the full critical Pick form  OPEN / RH-BEARING
mixed orientation and bridge arithmetic rows         OPEN
Riemann Hypothesis                                   UNPROVED
```

## 7. Correct remaining theorem

The branch must now be read as a fixed-scale direct positive-form programme.
For every finite carrier set, form the exact source and output matrices on the
finite confluent pole-jet coordinates, adjoin the reflected orientation and the
canonical bridge, and prove

\[
 G_a^{\rm source}(W)-G_a^{\rm output}(W)\succeq0.
\]

The only non-safe scalar channel is the full Pick kernel of
`m=-Xi'/Xi`; its positivity is RH-equivalent. A future proof must construct
that kernel from the completed Jordan plus gamma/pole source without assuming
its positivity. Neither the refuted normalized Bochner contraction nor the
refuted all-scale fixed Hilbert colligation may be used.

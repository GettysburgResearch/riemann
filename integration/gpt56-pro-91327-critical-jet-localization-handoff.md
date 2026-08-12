# Integration handoff — finite pole jets, bounded safe tangent, and one critical confluent block

## Freeze

```text
parent PR:      #400
child PR:       #429
initial child:  80ba1f2958ab6e561dc5e91430ffd21c05d02f11
session date:   2026-08-13
RH:             unproved
```

Read the current child head from GitHub after publication.

## I. Continuous delay has become finite algebra

`L-91327` proves that the ordinary Hardy simple/double-pole space at a finite
node set is invariant under the backward delay semigroup. For each node `w`,

```text
kappa_w              -> exp(-i conjugate(w) tau) kappa_w;
kappa_w^[1]          -> exp(-i conjugate(w) tau)
                        (kappa_w^[1]-i tau kappa_w).
```

The Cauchy mother uses only the nodes

```text
x+i a, x+2 i a, x+4 i a,
```

and their first confluent jets. Thus one carrier occupies at most six
coordinates, and every finite carrier-delay packet is one finite triangular
coefficient block after model projection.

The tangent of each model kernel is reduced to ordinary Hardy kernels and the
logarithmic-phase Toeplitz columns. Every physical output Gram is therefore a
finite matrix; delay no longer contributes an infinite-dimensional analytic
obligation.

## II. The safe tangent is bounded on the whole model space

`L-91328` sharpens the earlier logarithmic estimate. On the safe line
`sigma=1/2+a>1`,

```text
ell_a(t)
 =2 i a Im[(xi'/xi)(sigma+i t)].
```

The real logarithmic gamma growth cancels. Absolute convergence of
`zeta'/zeta`, elementary rational bounds, and the digamma series give an
explicit uniform bound for `ell_a`.

Consequences:

```text
dot Theta_a is a bounded Hardy multiplier;
J_a is bounded on all K_(Theta_a);
D_a from L-91325 equals the full model space;
T_(varphi,a) C_a B_a is defined and bounded after parameterization
by every model-space input.
```

The ambient reciprocal-xi Toeplitz operator remains unbounded. What disappears
is the domain ambiguity on the structured Suzuki range.

## III. The global Toeplitz projection collapses to one safe multiplier

`L-91329` defines

```text
D_a(z)=a (xi'/xi)(1/2+a-i z),
```

which is analytic on the whole upper half-plane because its xi argument stays
in `Re(s)>1`.

For ordinary kernels,

```text
T_(ell_a) kappa_w
 = (conjugate(D_a(w))-D_a(z)) kappa_w(z).
```

After the exact cancellation with the derivative of the inner multiplier, the
model-space tangent column is

```text
A_a k_w^Theta
 = (A_a(w)-B_a(w) D_a(z)) kappa_w(z),
```

with

```text
B_a(w)=xi(sigma-i conjugate(w))/xi(sigma+i conjugate(w));
A_a(w)=a xi'(sigma-i conjugate(w))/xi(sigma+i conjugate(w)).
```

The first confluent column is the derivative of this formula and uses only
`kappa_w`, `kappa_w^[1]`, `D_a kappa_w`, and `D_a kappa_w^[1]`.

No reflected logarithmic derivative or reciprocal-zero singularity remains.

## IV. Only one critical xi jet survives

At the three physical heights `r=1,2,4`, put

```text
u_r=1/2+(r-1)a+i x;
v_r=1/2+(r+1)a+i x.
```

The scalar tangent coefficients are quotients of xi, xi', and xi'' at `u_r`
by xi values at `v_r`.

For `r=2,4`, all of `u_r,v_r` lie in `Re(s)>1`. The sole non-safe scalar block
is

```text
xi(1/2+i x), xi'(1/2+i x), xi''(1/2+i x)
```

from the simple/double pole at height `a`, divided by the very safe value
`xi(1/2+2a+i x)` and its safe derivatives.

Thus the same-orientation physical endgame is one finite confluent block with:

```text
one common safe analytic multiplier D_a;
one critical xi/xi'/xi'' row per carrier;
exact Cauchy coefficients;
exact triangular delay matrices.
```

The reflected orientation is its conjugate, and the canonical bridge appends
one explicit rational row and column.

## V. Correct remaining theorem

Let `G_a^out(W)` be the finite matrix formed from the localized tangent columns
and let `G_a^src(W)` be the complete Jordan plus gamma/pole first-chaos source
matrix on the same resident coordinates. The conclusion-producing statement is
exactly

```text
G_a^src(W)-G_a^out(W) >= 0
```

for every finite carrier set, after adjoining the reflected and bridge blocks.

This is still RH-bearing. The present packet removes:

```text
continuous-delay analysis;
physical-input ambiguity;
form-domain ambiguity;
normalized Fisher-Bochner ambiguity;
Riesz-projection ambiguity in the tangent columns;
all unsafe scalar data except one explicit critical confluent jet.
```

It does not sign the final source-minus-output matrix.

## VI. Correct live status

```text
delayed weighted form core                         PROVED
canonical bridge geometry                          PROVED
full physical model/amplitude/leakage colligation PROVED
normalized Fisher-Hankel Bochner core             REFUTED
bounded renormalized source feature               PROVED
safe Suzuki tangent on full model space           PROVED
continuous delay -> finite pole-jet blocks        PROVED
Toeplitz tangent -> one safe multiplier            PROVED
only critical xi/xi'/xi'' block isolated          PROVED
completed source-minus-output block positivity    OPEN / RH-BEARING
mixed orientation and bridge arithmetic rows      OPEN
Riemann Hypothesis                                UNPROVED
```

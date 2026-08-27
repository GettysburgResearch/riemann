## T105650–T105653 addendum — adaptive Jensen index and convex-order Turán flow

**The Riemann Hypothesis remains unproved.**

This checkpoint digests the common interface of:

```text
PR #729  actual current/Turan hierarchy, anti-inner collar, owner law;
PR #731  signed hard-band index, canonical correlations, oriented phase angle;
PR #724  residue/Loewner split;
PR #728  source-owned exterior-square/de Branges coordinates;
PR #726  one-sided Hardy phase reserve.
```

### Exact logarithmic index

For a finite reduced quotient `U=A/B`,

```text
J_y(U)
 = 1/(4 pi y) integral_R log |U(x+i y)|^2 dx
 = sum_(b in B) min(1,Im(b)/y)
   -sum_(a in A) min(1,Im(a)/y).
```

Hence

```text
lim_(y->0) J_y(U) = deg B-deg A = -wind U.
```

The derivatives of `y J_y` recover the complete signed depth-counting function
and vertical divisor. Multiplicity and horizontal collisions are automatic.

### Soft current charge is a random-scale index

With

```text
mu(ds)=2s/(1+s)^3 ds,
```

one has exactly

```text
2 delta/(H+2 delta)
 = integral min(1,delta/(Hs/2)) mu(ds).
```

Thus every exponential soft-depth charge is a universal positive average of
exact clipped indices. For a complete quotient, the signed soft-depth divisor
is the same average of `J_(Hs/2)(U)`.

Independently, every monotone current profile `r` has the Stieltjes resolution

```text
2 delta integral r(xi)e^(-2 delta xi) dxi
 = integral (1-e^(-2 delta L)) d(-r)(L),
```

with complementary endpoint charge

```text
integral e^(-2 delta L) d(-r)(L).
```

The actual Xi current is therefore an exact positive mixture of the adaptive
hard-band source/index splits already proved at first anti-inner contact.

### Full complex convex majorization

For a polynomial with roots `z_j`, critical points `c_k`, and centroid `zbar`,
there is an explicit doubly stochastic matrix `S` such that

```text
(c_1,...,c_(n-1),zbar)^T = S (z_1,...,z_n)^T.
```

Therefore every convex function on the complex plane decreases under
differentiation after the centroid atom is retained. This includes every
projected convex moment, radial moment, and convex disk-escape moment.

For a real polynomial and every height `H>=0`,

```text
sum_roots |Im rho-H|
 -sum_critical |Im c-H|
 -H >= 0.
```

Along a derivative ladder ending in a real-rooted packet,

```text
2 * parent upper penetration at H
 = sum_r adjacent Jessen-Turan excess_r(H),
```

with every summand nonnegative. The horizontally averaged balanced Turan flow
therefore already has the correct sign.

### Exact surviving defect

For a finite inner quotient,

```text
||H_U||_HS^2
 = lim_(y->0) J_y(U)
   + ||H_(U^-1)||_HS^2.
```

The first term is the complete signed integer flow. The second is a positive,
degree-zero, reverse-oriented phase-overlap defect. It is equivalently the
canonical-correlation deficit or the favorable Hardy energy lost by an
adverse-only estimate.

The exact fixture

```text
U=B_(i a)/B_(i b),  a!=b,
```

has zero signed index and zero sufficiently-fine logarithmic index, but

```text
||H_U||_HS^2=(a-b)^2/(a+b)^2>0.
```

Thus the remaining theorem is genuinely separate from RH's integer index:

```text
D0PHASE105650

Absorb the degree-zero reverse phase overlap in the actual Xi
parent/derivative and endpoint quotients by the positive current/Turan reserve,
retaining point evaluation, confluence and one endpoint ledger.
```

### Exact replay

```text
PASS_X_105650_ADAPTIVE_JENSEN_INDEX
checks=3836
bc40c413a854087e28fe82e7a73e0f5022d7b31d7f9acb8f7f7da80630cce486
RH_UNPROVEN
```

The replay checks finite rational mixture, coarea, hard-band conservation and
the degree-zero separator. It does not replay the analytic log integral,
complex majorization proof, cofinal Xi transfer, `D0PHASE105650`, the pointwise
microscope or RH.

### Updated frontier

```text
adaptive signed logarithmic index                     PROVED EXACT
soft depth = random-scale exact index                 PROVED EXACT
actual monotone current = adaptive hard-band mixture  PROVED EXACT
complex convex critical-point majorization            PROVED EXACT
balanced horizontal Jessen-Turan sign                 PROVED EXACT
signed-index / owner normalization                    CLOSED AT NORMAL FORM
degree-zero phase-overlap defect                      OPEN / RH-BEARING
pointwise physical localization                       OPEN / RH-BEARING
cofinal endpoint/common-zero ledger                   OPEN
fixed-width terminal derivative theorem               PROPOSED / REVIEW
Riemann Hypothesis                                     UNPROVEN
```

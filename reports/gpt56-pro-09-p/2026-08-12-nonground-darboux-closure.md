# Non-ground/Darboux closure after the three-obligation attack

Date: 2026-08-12  
Branch: `agent/gpt56-pro-09-i/198-square-screw-criterion`  
Scientific status: **the Riemann Hypothesis remains unproved**

## Final mathematical disposition

The three requested obligations cannot all be proved in their original form.
The exact finite counterexample `R-19848` shows that a perfectly isolated simple
even interior CCM eigenline can have transform polynomial `z^2+1`.  Thus the
generic non-ground conclusion is false.

The attack nevertheless closes the precise finite theory and two of the three
quantitative components.

## 1. Isolated-line geometry

`L-19867` proves the complete source-bound residual-pencil theorem.  For

```text
D=[[m,b*],[b,C]] >=0,
G=diag(1,C),
C>=I,
```

the complement singular moat is exactly `1`, the target residual is at most
`sqrt(m+m^2)`, and the generalized spectrum is

```text
1 on c-perp,
lambda_±=(1+m ± sqrt((1-m)^2+4||c||^2))/2.
```

With the Xi residual `m_L<=C_B exp(-B L)`, the isolated-line angle and residual
ratio tend to zero exponentially on a cofinal sequence.

This theorem is for the positive arithmetic residual Gram, not the actual
indefinite localized Weil matrix.

## 2. Exact non-ground boundary

The following finite statements are now proved.

### Generic theorem is false

`R-19848/R-19849` give an exact three-mode CCM counterexample with a simple even
interior line and roots `±i`, and prove that its positive CCM completion cone is
empty.

### Positive completion characterization

`T-19814` proves, in the exact real CCM convention,

```text
positive CCM completion with kernel xi
<=> quotient companion diagonalizable over R with real spectrum
<=> generic finite transform roots real and simple.
```

Therefore a positive completion for an arbitrary interior line is an equivalent
form of the finite real-zero problem, not a consequence of isolation.

### Constructive one-sign theorem

`L-19871` proves that if `xi_j>0`, `sum xi_j=1`, then

```text
Q_xi=diag(1/xi_j)-11^T
```

is an exact positive CCM completion with kernel `xi`, and the transform zeros
strictly interlace the lattice nodes.

`L-19872` constructs the unique minimal-degree real-rooted sign corrector for an
arbitrary nonzero real finite coefficient vector: insert one root in every gap
where the data change sign.

### Scalar Darboux firewalls

The centered CCM vector is `(-1)^k` times the centered Fourier sample.  Hence a
raw-positive Xi target alternates on the complete lattice.

`R-19852` proves the resulting dichotomy:

```text
polynomial phase correction
 -> degree at least 2N-Z_H
 -> asymptotically H L / pi on moving-Hardy schedules
 -> multiplied target escapes the cutoff;

zero-free exponential phase correction
 -> unique minimal phase is a half-interval translation
 -> fixed loss of at least half the L2 energy.
```

Thus the explicit scalar sign-groundification does not preserve the Xi limit.
Matrix-valued colligations are not excluded.

## 3. Approximate symmetrizer theorem

`L-19869` supplies the strongest correct non-ground replacement.  If

```text
Q_j>=0,
ker Q_j=C xi_j,
epsilon_j=1/2 ||Q_j^-1/2(Q_jT_j-T_j*Q_j)Q_j^-1/2|| ->0,
```

then every finite nonuniversal transform zero lies in
`|Im z|<=epsilon_j`.  Local uniform convergence to Xi then implies RH by
Hurwitz.

`L-19870` proves that optimizing over an unrestricted positive metric gives
exactly the finite spectral strip width.  Therefore the metric must be fixed by
source/arithmetic data before its defect is estimated.

`R-19850` proves that the isotropic residual limit is not such a metric: its
commutator defect is the parity area

```text
1/2 sqrt(||P Lambda xi||^2 ||P eta||^2
         - <P Lambda xi,P eta>^2),
```

and under CCM parity this equals

```text
1/2 ||P Lambda xi|| ||P eta||.
```

## 4. Moving-Hardy rate

`L-19868` proves the complete target-side rate.  With

```text
L -> infinity,
tau_L=1/2-1/sqrt(L),
N_L=ceil(kappa L^2),
kappa>8/pi^2,
m_L<=exp(-8L),
delta_L<=exp(-4L),
```

the four losses are

```text
exterior + complete periodization aliases;
finite Fourier cutoff;
residual isolated-line displacement;
directed enclosure.
```

The periodic endpoint mismatch is exactly zero.  Their sum is `O(exp(-cL))`, so
the finite residual line converges to Xi locally uniformly on every closed
substrip.

## Exact remaining theorem

The entire surviving proof burden is now one source-specific anisotropic
commutator estimate:

```text
construct Q_j from prime/pole/archimedean source data,
ker Q_j=C xi_j,
1/2 ||Q_j^-1/2(Q_jT_j-T_j*Q_j)Q_j^-1/2|| ->0.
```

Equivalently, construct a matrix-valued Darboux/CCM colligation whose positive
metric is source-bound and whose defect tends to zero.  No current theorem
supplies this estimate.

## Exact status

```text
positive residual-pencil isolated line             PROVED
actual localized-Weil isolated line                 OPEN
complete moving-Hardy target rate                   PROVED
generic isolated-interior real-zero theorem         FALSE
exact positive completion characterization          PROVED
one-sign non-ground CCM theorem                     PROVED
finite minimal real-rooted sign correction          PROVED
scalar centered Darboux preservation                BLOCKED BY EXACT FIREWALLS
source-bound anisotropic approximate symmetrizer    OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVED
```

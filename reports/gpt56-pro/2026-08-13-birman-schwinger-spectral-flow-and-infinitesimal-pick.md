# Birman–Schwinger spectral flow and the infinitesimal safe Pick hierarchy

Date: 2026-08-13  
Branch: `research/gpt56-pro/91900-birman-schwinger-spectral-flow`  
Parent: PR #430 / radial spectral-type programme  
RH status: **unproved**

## Executive result

The radial programme contained a valid conditional theorem but an overstrong
motivating inference.  A diffuse source does not by itself prevent pure-point
outputs: nonlocal feedback can create a bound state.  The exact correction is
to distinguish two possible conclusion mechanisms:

```text
interval-locality mechanism:
    prove an L-infinity(depth)-module source lock;

feedback mechanism:
    identify the completed return loop and prove gain <= 1.
```

This pass develops the second mechanism and obtains one genuine unconditional
finite-order advance: the linearized safe Xi Carathéodory kernel is positive on
every packet of size one or two.  A rational high-off-line control shows that
three nodes are the first possible obstruction.

## I. Exact correction to the radial intuition

`R-91900` uses the rank-one Friedrichs model

\[
H_t=M_r-t|1\rangle\langle1|
\quad\text{on }L^2([1,2],dr).
\]

The open medium is purely absolutely continuous.  Nevertheless a negative
bound state appears at

\[
t_c=1/\log2,
\]

and the negative-index spectral flow has the atom `delta_(t_c)`.

The coupling is nonlocal:

\[
P_I|1\rangle\langle1|P_J\ne0
\]

for disjoint intervals.  This pinpoints the missing assumption in RLSL.

## II. Birman--Schwinger and small gain

`L-91900` proves for

\[
H=A-G^*G,
\qquad A\succeq cI,
\]

that

\[
-\kappa\in\sigma_p(H)
\Longleftrightarrow
1\in\sigma_p\bigl(G(A+\kappa)^{-1}G^*\bigr).
\]

At zero energy,

\[
n_-(H)=\#\{\lambda(K(0))>1\}.
\]

The Schur complement gives

\[
H+\kappa\succeq0
\Longleftrightarrow
K(\kappa)\preceq I.
\]

Thus an off-line obstruction may be viewed as a unit-gain feedback event,
not as an atom transported from the open source.

## III. The exact safe Xi return operator

For a safe rational packet,

\[
C_{ij}=\frac1{1+u+q_i+q_j},
\qquad
D_{ii}=\frac{\xi(1+q_i)}{\xi(1+u+q_i)},
\]

and

\[
P=C-DCD.
\]

`L-91901` defines

\[
K=C^{-1/2}DCDC^{-1/2}
\]

and proves

\[
P\succeq0
\Longleftrightarrow
K\preceq I.
\]

Subject to the continuation interface of `T-91006`, RH is equivalent to this
small-gain condition on every finite rational packet.

This is an unusually concrete final operator:

```text
finite dimensional;
all Xi samples real and >1;
negative failure certified by one eigenvalue >1;
no zero data or Gram capture.
```

## IV. Cauchy-covariant bounded-real flow

`L-91902` proves the moving-metric identity

\[
P'-\Gamma^*P-P\Gamma
=-[(\nabla D)^*CD+D^*C\nabla D].
\]

A positive right side propagates the Pick cone from `P_0=0`.

`L-91903` classifies every compatible connection as

\[
\Gamma=\frac12C^{-1}C'+C^{-1}J,
\qquad J^*=-J,
\]

so the completed connection problem is one finite affine LMI in a skew gauge.
It has finite primal and dual certificates.

`R-91901` proves that the canonical metric connection alone is too rigid.  A
strictly positive rational contraction has an indefinite canonical
instantaneous remainder.  The skew source channels are load bearing.

## V. Infinitesimal linearization

At `u=0`, the finite-displacement Pick matrix vanishes and

\[
P_0'
=\left(
 \frac{\xi'/\xi(1+q_i)+\xi'/\xi(1+q_j)}
      {1+q_i+q_j}
 \right)_{i,j}.
\]

`L-91904` proposes the exact countable criterion:

\[
\mathrm{RH}
\Longleftrightarrow
P_0'[\mathbf q]\succeq0
\quad\text{for every finite positive rational tuple.}
\]

The reverse direction uses Carathéodory interpolation to continue the centered
logarithmic derivative `Xi'/Xi` as a positive-real function on the right
half-plane.  An off-line zero would be an interior pole.

This removes the nonlinear quotient and the entire horizontal flow from the
statement of the sign problem.

## VI. Unconditional order-two theorem

`L-91905` groups the centered Hadamard product orbit by orbit.  For a critical
zero the contribution to `F(x)/x` is

\[
2m/(x^2+\gamma^2).
\]

For an off-line quadruple `a+ib`, it is

\[
4m\frac{x^2-a^2+b^2}
{(x^2-a^2+b^2)^2+4a^2b^2}.
\]

The rigorous low-zero verification supplies only the weak fact `|b|>1`.
Every orbit then has two properties:

```text
contribution to F(x)/x   strictly decreases;
contribution to x F(x)   strictly increases.
```

Summation gives, for `1/2<x<y`,

\[
\frac xy
<\frac{F(y)}{F(x)}
<\frac yx.
\]

This is exactly the positivity condition for the two-node Carathéodory matrix.
Hence all one- and two-node infinitesimal safe Pick matrices are positive
without RH, subject to review of the grouped product argument.

## VII. Sharp order-three control

For the high off-line orbit

\[
a=2/5,
\qquad b=14,
\]

`R-91902` constructs the rational safe nodes

\[
3/5,\quad8,\quad36
\]

and obtains

\[
\det H
=-\frac{201516024836691562500}
{1055839030806150723363641645963}<0.
\]

Thus order two is sharp.  The first possible actual-Xi obstruction in the
linearized hierarchy is order three.

## VIII. Verification

The retained verdict is

```text
PASS_BIRMAN_SCHWINGER_SPECTRAL_FLOW
```

Selected controls:

```text
Friedrichs threshold                 1.4426950408889634
bound-state kappa at coupling 2      0.5414940825367983
safe Xi Pick minimum eigenvalue      2.0765892e-10
safe Xi return singular values       0.99999992, 0.99988606, 0.97282104
canonical remainder minimum          -5.4506935e-7
rational control det(P)              0.0788980...
rational control det(R)              -1.8485673e-9
planted orbit three-node determinant -1.9085866e-10
```

The exact rational controls are theorem checks.  The finite Xi evaluations are
diagnostics only.

## IX. Priority after this pass

1. Hostile-review the unconditional order-two theorem.
2. Attack the actual-Xi order-three determinants, the first unresolved level.
3. Construct the skew connection from the completed Julia source rather than
   from target positivity.
4. Retain RLSL only as the stronger interval-local alternative.

## Exact boundary

```text
radial diffuse-only conclusion                 REFUTED
Birman--Schwinger feedback theorem              EXACT
safe-real finite return operator                EXACT
covariant connection/LMI                        EXACT
infinitesimal RH criterion                      PROPOSED COMPLETE
orders one and two                              PROPOSED UNCONDITIONAL
order-three planted obstruction                 EXACT
actual Xi order three and higher                OPEN
all-packet small gain                           OPEN / RH-EQUIVALENT
Riemann Hypothesis                              UNPROVED
```

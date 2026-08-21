# Replacement full proposal: boundary exponential B-spline and reflected renewal

Agent: `gpt56-02-r`  
Date: 2026-08-08  
Status: **SERIOUS FULL PROPOSAL; ONE EXPLICIT SOURCE CONTRACTION OPEN; RH NOT PROVED**

## 1. Review absorbed

The frozen carry proposal on PR #243 used a false conditional-Hankel step. The
review supplied the exact obstruction

\[
 f''(0)f''''(0)-f'''(0)^2=-233/64.
\]

The zero-mass qualifier does not repair that determinant. This report therefore
does not defend `L-23603.15`; it replaces the mechanism.

The following algebra survives and is reused:

- the exact carry matrix and average-binomial prime-power identity;
- the affine Möbius contraction;
- the closed triangular inverse;
- the continuum profile and reciprocal-zeta Mellin transform;
- dyadic Euler alignment;
- positive inverse coefficients and generalized prime weights;
- digital endpoint identities;
- the first-cell Mertens firewall.

The reviews also show that the global carry profile, Gamma-carry density, and
resolvent state are one function in different normalizations. No claim of
independent evidence is made from those parallel coordinates.

## 2. New object: integrate before imposing positivity

The carry Green kernel

\[
 h(t)=8e^{t/2}-7-\frac32t
\]

is the differential image

\[
 h=(\partial+1/2)(\partial+3/2)q
\]

of

\[
 q(t)=4e^{t/2}-4-2t\ge0.
\]

The function `q` has zero value and derivative at the causal boundary. This is
the correct level at which to apply dyadic finite differences.

With `L=log 2`,

\[
(I-\sqrt2\tau_L)(I-\tau_L)^2q
=\mathbf1_{[0,L]}*\mathbf1_{[0,L]}*
 e^{t/2}\mathbf1_{[0,L]}.
\]

The right side is a positive compact exponential B-spline. Positivity is now a
literal convolution statement, not an invalid Hankel assertion.

Higher order is obtained by further positive convolutions. The window remains
compact, smooth to any prescribed finite order, and has transform zeros only on
the two boundary lines of the critical strip.

## 3. Exact aligned arithmetic source

The dyadic boundary filter corresponds in the zeta coordinate to

\[
R_R(x)=(1-\sqrt2x)^{R+2}(1-2x)^{R+1}.
\]

Thus the aligned inverse-zeta source is

\[
B_R(s)=R_R(2^{-s})/\zeta(s).
\]

Its inverse has positive coefficients. Its generalized von Mangoldt sequence
is nonnegative. The generalized Selberg forcing is coefficientwise positive.
No off-line zeta pole is canceled because the new numerator zeros occur only on
`Re s=1/2` and `Re s=1`.

The eta coefficient `epsilon(n)=(-1)^(n+1)` gives the exact finite forcing

\[
\varepsilon*b_R=d_R,
\]

where `d_R` is supported on finitely many powers of two. This is stronger than
a small endpoint estimate: the entire unbounded source is converted into one
bounded digital recurrence.

## 4. Valid boundary expansion

The aligned state obeys

\[
Q_R^\partial(t)
=\sum_{k\ge1}(-1)^{k+1}k^{-1/2}U_R(t-\log k).
\]

Pairing `2m` with `2m+1` gives the exact transport identity

\[
U_R(t)=Q_R^\partial(t)
+\int_{\cup_m[2m,2m+1]}
 x^{-3/2}(\partial+1/2)U_R(t-\log x)dx.
\]

The transport mass is

\[
2(1-\eta(1/2))<1.
\]

For higher cancellation, the finite Euler identity is exact:

\[
\mathcal A(a)=
\sum_{j<M}2^{-j-1}\Delta^ja_1
+2^{-M}\mathcal A(\Delta^Ma).
\]

Every finite difference has a Peano representation against a nonnegative
cardinal B-spline. The differential column is

\[
x^{-j-1/2}
\prod_{\ell<j}(\partial+\ell+1/2)U_R(t-\log x).
\]

This is the legitimate boundary B-spline expansion requested by the review. It
uses one-variable finite-difference positivity only.

## 5. New proposed closing theorem

The single remaining theorem is `BSRC(R,M)` in `L-26203`.

Use short blocks of length

\[
 B=\frac14\log2
\]

and the strict delay

\[
 \delta=\log2-B=\frac34\log2.
\]

Define

\[
\mathcal E_{R,M}(J)=
\sum_{j=0}^M16^{-j}
\int_J^{J+B}|\mathcal D_jU_R|^2.
\]

The target is

\[
\mathcal E_{R,M}(J)
\le C(1+J)^A
+\theta\left[1+
\max_{u\le J-\delta}\mathcal E_{R,M}(u)
\right]
\]

for one fixed `theta<1`.

The short block is essential: every nonforcing column is delayed by at least
`log 2`, so the entire current block maps strictly below `J-delta`.

The proposed proof must combine:

1. exact Peano boundary cells;
2. the finite eta forcing before widening;
3. the actual aligned source pair;
4. the reflected Selberg **modulus square**;
5. all ratio, cutoff, and noncoprime chains;
6. a strict source LMI.

This is not a generic operator theorem. The claim is only for the actual
aligned inverse-zeta vector.

## 6. Completion if the hinge holds

The fixed strict delay and `theta<1` give polynomial short-block graph energy.
A linear number of short blocks covers `[0,X]`, so the fixed compact Möbius shell
has subexponential `L2` growth. Its Laplace transform is holomorphic in
`Re z>0`.

The explicit transform contains

\[
1/\zeta(z+1/2)
\]

and its numerator has no zero in the open strip. Any zeta zero to the right of
the critical line would therefore create a forbidden pole. Functional-equation
symmetry yields RH.

## 7. Relationship to signed carry transport

The endpoint-projected carry Gram already gives an exact signed correction of
all finite constraints. Signed certificates do not require nonnegative carry
coefficients. Those facts remain useful, but the exact objective projection is
the prime-ramp scalar itself; finite transport geometry alone cannot prove its
smallness.

The boundary-spline proposal therefore attacks the common Möbius source before
that scalar projection. It seeks a lower-scale energy recurrence rather than a
new finite feasibility algorithm.

## 8. Falsifiability

The proposal should be rejected if review finds:

- any reuse of the false conditional-Hankel kernel;
- an omitted `n=2` delayed boundary column;
- an unsigned Euler remainder;
- a scalar square in place of a reflected modulus square;
- a lost noncoprime chain;
- removal of the first fixed-ratio Mertens shell;
- a current block not separated from its claimed past destination;
- a contraction constant that depends on support or approaches one without a
  usable rate.

The exact source LMI is the entire hinge. No reviewer is being asked to invent a
missing packet definition or normalization.

## 9. Status

```text
conditional-Hankel carry closure       REFUTED
carry-Mobius inversion                 RETAINED EXACT
positive boundary exponential spline  PROPOSED EXACT
aligned eta renewal                    PROPOSED EXACT
Peano boundary expansion               PROPOSED EXACT
source-specific reflected contraction OPEN
conditional deduction to RH            COMPLETE
Riemann Hypothesis                      UNPROVED
```

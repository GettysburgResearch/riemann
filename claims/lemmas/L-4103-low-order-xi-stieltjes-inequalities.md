# L-4103 — Low-order differential inequalities for `xi'/xi`

Claim ID: L-4103  
Title: Explicit one-point differential inequalities implied by the shifted-Stieltjes hierarchy  
Status: PROPOSED  
Authoring agent: `gpt56-05-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: `L-4102`  
Scope: scalar and `2 x 2` finite xi-jet counterexample certificates  
Related counterexample candidates: none

## Statement

Use the notation of `L-4102`:

\[
 H(u)=H_T(u)=\frac1{\sqrt u}
 \operatorname{Re}F\!\left(\frac12+\sqrt u+iT\right),
 \qquad u>0.
\]

If RH holds, then the following inequalities hold at every point where the
expressions are defined:

### Complete-monotonicity signs through order three

\[
 H\ge0,
 \qquad
 H'\le0,
 \qquad
 H''\ge0,
 \qquad
 H'''\le0.
\]

### First Hankel determinant

\[
 H H''-2(H')^2\ge0.
\]

### First localizing scalar

\[
 H+uH'\ge0.
\]

Equivalently,

\[
 \operatorname{Re}F'(s)
 +\frac1x\operatorname{Re}F(s)\ge0,
 \qquad s=1/2+x+iT,\quad u=x^2.
\]

### First localizing determinant

Define

\[
 L_0=H+uH',
\]

\[
 L_1=-H'-\frac u2H'',
\]

and

\[
 L_2=\frac12H''+\frac u6H'''.
\]

Then

\[
 L_0\ge0,
 \qquad
 L_2\ge0,
 \qquad
 L_0L_2-L_1^2\ge0.
\]

Consequently, a rigorous interval enclosure proving the strict failure of any
one displayed inequality at an exact point in `Re(s)>1/2`, together with a
certified nonzero `xi` denominator, disproves RH.

The localizing scalar is existentially complete by `L-4101`. The determinant
conditions are additional finite tests; no claim is made that they enlarge the
witness basin in every off-line configuration.

## Motivation

`L-4102` gives a generic moment-matrix hierarchy, but an initial ball
implementation benefits from explicit low-order targets:

- the scalar localizer needs a second-order `xi` jet;
- the Hankel determinant needs `F''`, hence a third-order `xi` jet;
- the localizing determinant needs `F'''`, hence a fourth-order `xi` jet.

These formulas let Issue #39 test the normalization and interval propagation
before designing a general matrix schema or rationalizing eigenvectors.

## Proof

Under RH, `L-4102` gives

\[
 m_n=\frac{(-1)^n}{n!}H^{(n)}\ge0.
\]

The first four signs follow immediately.

The order-one Hankel matrix is

\[
 A_1=
 \begin{pmatrix}
 m_0&m_1\\
 m_1&m_2
 \end{pmatrix}
 =
 \begin{pmatrix}
 H&-H'\\
 -H'&H''/2
 \end{pmatrix}.
\]

Positive semidefiniteness gives

\[
 0\le\det A_1
 =\frac12HH''-(H')^2,
\]

which is the stated Hankel inequality.

The order-one localizing matrix is

\[
 B_1=
 \begin{pmatrix}
 m_0-u m_1&m_1-u m_2\\
 m_1-u m_2&m_2-u m_3
 \end{pmatrix}.
\]

Using

\[
 m_0=H,
 \quad
 m_1=-H',
 \quad
 m_2=H''/2,
 \quad
 m_3=-H'''/6,
\]

this is exactly

\[
 B_1=
 \begin{pmatrix}
 L_0&L_1\\
 L_1&L_2
 \end{pmatrix}.
\]

Positive semidefiniteness gives both diagonal inequalities and

\[
 \det B_1=L_0L_2-L_1^2\ge0.
\]

Finally, the identity between `L_0` and the differential expression follows
from `L-4102`:

\[
 L_0=(B_0)_{00}=\frac12\left(
 \operatorname{Re}F'(s)+\frac1x\operatorname{Re}F(s)
 \right).
\]

A strict certified failure contradicts a necessary consequence of RH. ∎

## Certificate consequence

A low-order certificate may avoid matrix serialization entirely. It should
contain:

1. exact dyadic `x,T` and proof `x>0`;
2. a directed `xi` jet through the order required by the selected inequality;
3. proof that the `xi` denominator excludes zero;
4. exact rational reconstruction of the required `F` jet and `H` derivatives;
5. one outward real interval for the chosen left-hand side;
6. a status accepted only when the upper endpoint is strictly negative.

For products such as `L_0L_2-L_1^2`, interval dependency can be severe. A
producer may instead nominate a small dyadic vector and certify the equivalent
quadratic form from `L-4102`; the two proof routes should agree when both
resolve.

## Analytic domain audit

Inherited from `L-4102`. All derivatives are with respect to positive real `u`
at fixed `T`. The evaluation point must avoid zeros of `xi`.

## Dependency audit

Only the finite matrices `A_1` and `B_1` and their positive semidefiniteness
from `L-4102` are used. No additional moment theorem is imported.

## Gap audit

- The Hankel inequality contains the factor `2`:
  `H H''-2(H')^2`, not ordinary log-convexity with coefficient `1`.
- The localizing off-diagonal is
  `-H'-uH''/2`.
- The bottom-right localizing entry has a **plus** sign before `uH'''/6`
  because `m_3=-H'''/6`.
- A determinant interval containing zero is unresolved.
- Passing the first few inequalities is not evidence for RH.
- The direct `H` derivatives should be reconstructed from an audited `F` or
  `xi` jet, not finite differences of sampled values.

## Adversarial tests

1. Compare every formula with matrices assembled from exact synthetic on-line
   moments.
2. Delete the factor `2` in the Hankel inequality and require the symbolic
   matrix identity to fail.
3. Flip the sign of `uH'''/6` and require disagreement with the direct
   localizing sum.
4. Test a rank-one single-ordinate synthetic measure, for which both `2 x 2`
   determinants vanish exactly.
5. Use the off-line quartet control from X-4101 and require the scalar localizer
   to be negative while `Re F` remains positive.

## Remaining uncertainty

No mathematical gap is known. Which low-order inequality gives the best
conditioning for actual high-height `xi` evaluations is unknown.

## Suggested next attack

Implement the scalar localizer first, then the two determinant inequalities at
increasing precision. Compare them with exact-vector `2 x 2` quadratic forms to
distinguish genuine analytic margins from interval dependency artifacts.
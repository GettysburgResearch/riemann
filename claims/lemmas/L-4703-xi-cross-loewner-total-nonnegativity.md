# L-4703 — Cross-Loewner total nonnegativity for the xi response

Claim ID: L-4703  
Title: Under RH every value-only cross-Loewner minor of the horizontal xi response is nonnegative  
Status: PROPOSED  
Authoring agent: `gpt56-05-d`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-3201; L-4701  
Scope: derivative-free multi-point determinant certificates  
Related counterexample candidates: none

## Statement

Fix real `T` and use

\[
 J_T(u)=\sqrt u\,\operatorname{Re}F\!\left(\frac12+\sqrt u+iT\right),
 \qquad F=\frac{\xi'}\xi.
\]

Let

\[
 0<u_1<\cdots<u_m,
 \qquad
 0<v_1<\cdots<v_n,
\]

and assume `u_i!=v_j` for every pair. Define the value-only cross-Loewner
matrix

\[
 \mathcal L_T(U,V)_{ij}
 =\frac{J_T(u_i)-J_T(v_j)}{u_i-v_j}.
\]

If RH holds, then this rectangular matrix is **totally nonnegative**: for every
`k<=min(m,n)` and every increasing row and column index set of size `k`,

\[
 \det\left(
   \mathcal L_T(U,V)_{i_pj_q}
 \right)_{1\le p,q\le k}\ge0.
\]

Consequently, a rigorous negative enclosure for any exact cross-Loewner minor
is a finite unconditional counterexample witness to RH. The certificate uses
only values of `xi'/xi` at the distinct points represented by `U` and `V`.

Every `1x1` minor is the L-4701 secant. Therefore the hierarchy is
existentially complete. Higher minors can nevertheless improve discovery: a
minor may be negative even when every sampled entry is positive.

In exact horizontal-offset coordinates `u_i=x_i^2` and `v_j=y_j^2`,

\[
 \mathcal L_{ij}
 =\frac{
   x_i\operatorname{Re}F(\frac12+x_i+iT)
   -y_j\operatorname{Re}F(\frac12+y_j+iT)
 }{x_i^2-y_j^2}.
\]

## Motivation

A scalar secant can be masked by a large positive critical-line background at a
coarse sample location. Multi-point Loewner minors test whether all secants can
come from one positive zero-resolvent measure. This is stronger than checking
each entry independently and still avoids every xi derivative.

The theorem supplies a finite-data bridge among:

- the scalar passivity witness in L-3201;
- the Pick matrix in L-3202;
- the one-point Stieltjes moment matrices in L-4102;
- the derivative-free divided differences in L-4702.

Unlike a fitted Loewner model, the final minor is reconstructed directly from
rigorous xi values.

## Resolvent factorization under RH

Assume RH and set

\[
 a_\gamma=(T-\gamma)^2.
\]

L-4701 gives, for `u!=v`,

\[
 \frac{J_T(u)-J_T(v)}{u-v}
 =\sum_\gamma
 \frac{a_\gamma}{(u+a_\gamma)(v+a_\gamma)}.
\]

Group equal positive values of `a_gamma` and let `c_a>0` be `a` times their
combined multiplicity. Values `a=0` contribute zero to every secant and may be
removed. Then

\[
 \mathcal L_T(u,v)
 =\sum_{a>0}\frac{c_a}{(u+a)(v+a)}.
\]

This is a cross Gram factorization through the Cauchy functions `(u+a)^-1`.

## Proof of total nonnegativity

First retain only finitely many distinct positive atoms

\[
 0<a_1<\cdots<a_N.
\]

For a chosen `k x k` minor with increasing row nodes
`r_1<...<r_k` and column nodes `s_1<...<s_k`, write

\[
 P_{p\ell}=\frac1{r_p+a_\ell},
 \qquad
 Q_{q\ell}=\frac1{s_q+a_\ell},
 \qquad
 C=\operatorname{diag}(c_{a_1},\ldots,c_{a_N}).
\]

The finite minor matrix is `PCQ^T`. Cauchy--Binet gives

\[
 \det(PCQ^{\mathsf T})
 =\sum_{1\le \ell_1<\cdots<\ell_k\le N}
 \left(\prod_{j=1}^{k}c_{a_{\ell_j}}\right)
 \det\left(\frac1{r_p+a_{\ell_j}}\right)_{p,j}
 \det\left(\frac1{s_q+a_{\ell_j}}\right)_{q,j}.
\]

For increasing positive `z_1<...<z_k` and increasing
`b_1<...<b_k`, the Cauchy determinant is

\[
 \det\left(\frac1{z_p+b_j}\right)_{p,j}
 =\frac{
   \prod_{p<q}(z_q-z_p)
   \prod_{p<q}(b_q-b_p)
 }{
   \prod_{p,j}(z_p+b_j)
 }>0.
\]

Both determinants in every Cauchy--Binet summand are therefore positive, and
all weights are positive. Every finite-truncation minor is nonnegative.

For the complete zero set, each matrix entry converges absolutely because the
summand is `O((T-gamma)^-2)`. Take any exhaustion by finite grouped atom sets.
The finite matrices converge entrywise to the complete matrix, and determinants
are continuous polynomials in their entries. The limiting minor is therefore
nonnegative.

## Why positive entries are not enough

Total nonnegativity couples different secants. A `2x2` certificate can have

\[
 \mathcal L_{11},\mathcal L_{12},
 \mathcal L_{21},\mathcal L_{22}>0
\]

but

\[
 \mathcal L_{11}\mathcal L_{22}
 -\mathcal L_{12}\mathcal L_{21}<0.
\]

X-4701 gives an exact Gaussian-rational finite-zero example of precisely this
phenomenon. Thus the determinant hierarchy can expose an off-line component on
a sampled region where every individual secant passes the first-order test.

## Certificate schema

A value-only minor certificate should contain:

1. exact dyadic `T`;
2. separately increasing exact dyadic offset lists `x_i` and `y_j`;
3. proof that all squared row and column nodes are cross-disjoint;
4. xi or zeta balls excluding zero at every sampled point;
5. real balls for every `Re F` value;
6. exact reconstruction of
   \[
   \mathcal L_{ij}
   =\frac{x_iR_i-y_jS_j}{x_i^2-y_j^2};
   \]
7. an outward interval determinant for one explicitly selected square minor;
8. a final determinant upper endpoint strictly below zero;
9. a producer fingerprint and exact node-order metadata.

For `2x2` and `3x3` minors the checker can expand the determinant directly.
For larger minors it should use an inclusion-monotone interval elimination or a
verified exact-coefficient expansion, never a midpoint determinant.

## Analytic domain audit

- Every sample lies in `Re(s)>1/2` and is proved zero-free before division.
- Row and column squared nodes are positive and cross-disjoint, so no derivative
  is hidden in a diagonal limit.
- Under RH the grouped resolvent atoms have nonnegative locations and positive
  weights.
- The complete entry sums converge absolutely.
- The infinite-minor statement follows from finite determinants and entrywise
  convergence; no interchange of an infinite determinant is used.
- No complex logarithm, root choice beyond the positive real square root, or
  contour occurs.

## Dependency audit

- D-3201 fixes `F`.
- L-4701 supplies the secant resolvent kernel.
- Cauchy--Binet and the elementary Cauchy determinant are proved or displayed
  explicitly here; no external total-positivity theorem is required.

## Gap audit

1. The row nodes and column nodes must each be stored in increasing order.
   Silently sorting them can change a determinant sign convention and conceal a
   malformed certificate.
2. Cross-equal nodes require derivatives and are excluded from the value-only
   schema.
3. Group repeated `a_gamma` values before using the strictly ordered Cauchy
   determinant; multiplicity belongs in the positive weight.
4. A negative determinant of a fitted or rounded Loewner matrix is not a
   certificate. Every entry must be reconstructed from direct balls.
5. Entrywise positivity does not license determinant positivity numerically;
   the minor interval itself must be certified.
6. Interval determinant dependency can be severe. Freeze a small minor and
   escalate precision rather than trusting an interval eigensolver.
7. The theorem does not claim strict positivity when there are too few distinct
   positive atom locations.

## Adversarial tests

1. For finite on-line zero sets, compare every `2x2` and `3x3` minor with the
   exact Cauchy--Binet expansion.
2. Use repeated ordinates and multiplicities; require nonnegative, possibly
   zero, minors after atom grouping.
3. Reverse a row or column node list and require schema rejection.
4. Make one row node equal one column node and require rejection rather than an
   implicit derivative.
5. Use X-4701's off-line quartet plus on-line background: require all four
   entries positive and the selected `2x2` determinant negative.
6. Mutate one exact determinant numerator and require verifier rejection.
7. Widen one `F` ball until the determinant interval contains zero and require
   `UNRESOLVED`.

## Remaining uncertainty

The finite and limiting determinant arguments appear complete. It remains an
empirical question which node geometries give the best negative margin for the
actual xi function and whether a `2x2` or `3x3` minor materially outperforms the
scalar secant in high-height reconnaissance.

## Suggested next attack

Add a `2x2` cross-Loewner mode to Issue #39's value-only Arb producer. Use
floating Loewner or rational-interpolation algorithms only to nominate two row
and two column offsets; freeze the exact nodes, reevaluate all values directly,
and certify the determinant independently.

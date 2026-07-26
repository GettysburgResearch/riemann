# L-9314 — Positive-anchor one-moment extension and two-sided Schur gate

Claim ID: `L-9314`  
Title: Adding one positive direct-xi node raises the full half-line response degree by one and is decided by two scalar Schur bounds  
Status: `PROPOSED`  
Authoring agent: `gpt56-04-e`  
Created: 2026-07-26  
Dependencies: L-9308, L-9309, L-9310, and the strict old-cone certificate on the chosen node table  
Scope: one exact positive node adjoined to a finite direct-xi response table  
Related counterexample candidates: the X-9312 positive-anchor nomination ladder

## Setup

Let

\[
 0<u_1<\cdots<u_n
\]

be distinct old response nodes and put

\[
 D(y)=\prod_{i=1}^n(y+u_i).
\]

For a zero-sum coefficient vector `beta`, use the L-9308 response map

\[
 P_\beta(y)
 =-\sum_{i=1}^n\beta_i\frac{D(y)}{y+u_i}.
\]

For `0<=k<=n-2`, let `beta^(k)` be the unique old portfolio with

\[
 P_{\beta^{(k)}}(y)=y^k,
\]

and write

\[
 a_k=L_{\rm old}(y^k)
 =\sum_i\beta_i^{(k)}F(u_i).
\]

Assume `n=2m+2`, so the old response degree is `2m`, and assume the old
functional is **strictly positive** on every nonzero real polynomial of degree
at most `2m` that is nonnegative on `[0,infinity)`. Equivalently, the two old
L-9310 Hankel matrices are positive definite. This strict hypothesis is exactly
what the retained PR #116 certificate supplies for the PR #103 table.

Adjoin one exact node

\[
 w>0,
 \qquad w\notin\{u_1,\ldots,u_n\},
\]

and put

\[
 \widetilde D(y)=(y+w)D(y).
\]

Let

\[
 b_k=L_{\rm new}(y^k),
 \qquad 0\le k\le2m+1,
\]

be the new monomial response moments.

## The one-new-moment recurrence

For every `0<=k<=2m`, zero-extend the old portfolio `beta^(k)` by assigning
coefficient zero to the new node. Its scalar contraction is still `a_k`, while
its new response polynomial is

\[
 -\sum_i\beta_i^{(k)}
   \frac{(y+w)D(y)}{y+u_i}
 =(y+w)y^k.
\]

Therefore

\[
 \boxed{a_k=b_{k+1}+w b_k\qquad(0\le k\le2m).}
\]

Consequently every new moment is affine in the sole new scalar `b_0`:

\[
 \boxed{
 b_k=(-w)^k b_0+
 \sum_{j=0}^{k-1}(-w)^{k-1-j}a_j
 \qquad(1\le k\le2m+1).}
\]

Thus adding an arbitrary positive node, just like adding the zero anchor in
L-9311, introduces exactly one new analytic datum.

## Adapted polynomial basis

For polynomials of degree at most `m`, use

\[
 \phi_0(y)=1,
 \qquad
 \phi_{i+1}(y)=(y+w)y^i
 \quad(0\le i<m).
\]

This is a basis because its change-of-basis matrix from the monomial basis is
triangular with diagonal entries `1`.

Define vectors

\[
 r_0=(a_0,\ldots,a_{m-1})^T,
 \qquad
 r_1=(a_1,\ldots,a_m)^T,
\]

and `m by m` Hankel-type matrices

\[
 (C_0)_{ij}=a_{i+j+1}+w a_{i+j},
 \qquad 0\le i,j<m,
\]

\[
 (C_1)_{ij}=a_{i+j+2}+w a_{i+j+1},
 \qquad 0\le i,j<m.
\]

In the adapted basis, the two new L-9310 moment matrices are congruent to

\[
 \boxed{
 \widetilde H_0(b_0)=
 \begin{pmatrix}
   b_0&r_0^T\\
   r_0&C_0
 \end{pmatrix},}
\]

and

\[
 \boxed{
 \widetilde H_1(b_0)=
 \begin{pmatrix}
   a_0-wb_0&r_1^T\\
   r_1&C_1
 \end{pmatrix}.}
\]

Indeed,

\[
 L_{\rm new}((y+w)y^i)=a_i,
\]

\[
 L_{\rm new}((y+w)^2y^{i+j})=a_{i+j+1}+wa_{i+j},
\]

and the same calculation after multiplication by `y` gives the second matrix.

## Strict positivity of the inherited blocks

For a nonzero polynomial `r` of degree at most `m-1`,

\[
 r^TC_0r=L_{\rm old}((y+w)r(y)^2)>0,
\]

because `(y+w)r^2` is nonzero, nonnegative on the half-line, and has degree at
most `2m-1`.

Likewise,

\[
 r^TC_1r=L_{\rm old}(y(y+w)r(y)^2)>0,
\]

because the latter polynomial has degree at most `2m`. Hence

\[
 \boxed{C_0\succ0,\qquad C_1\succ0.}
\]

No pseudoinverse or singular range condition is needed in the strict old-cone
regime.

## Complete two-sided gate

Define the exact scalar thresholds

\[
 \boxed{\theta_0(w)=r_0^TC_0^{-1}r_0,}
\]

and

\[
 \boxed{
 \theta_1(w)=
 \frac{a_0-r_1^TC_1^{-1}r_1}{w}.}
\]

The Schur complement theorem gives

\[
 \widetilde H_0(b_0)\succeq0
 \iff b_0\ge\theta_0(w),
\]

and

\[
 \widetilde H_1(b_0)\succeq0
 \iff b_0\le\theta_1(w).
\]

Combining this with L-9310 proves the exact equivalence

\[
 \boxed{
 L_{\rm new}(P)\ge0
 \text{ for every real }P\ge0\text{ on }[0,\infty),\ \deg P\le2m+1
 }
\]

if and only if

\[
 \boxed{\theta_0(w)\le b_0\le\theta_1(w).}
\]

Thus a positive anchor creates a **two-sided scalar trap**. The zero anchor is
the degenerate limit in which the upper gate becomes an inherited old matrix and
only the lower Schur inequality contains the new scalar.

## Explicit failed-gate witnesses

Put

\[
 x_0=C_0^{-1}r_0,
 \qquad
 x_1=C_1^{-1}r_1.
\]

Define

\[
 q_0(y)=1-(y+w)\sum_{i=0}^{m-1}(x_0)_i y^i,
\]

\[
 q_1(y)=1-(y+w)\sum_{i=0}^{m-1}(x_1)_i y^i.
\]

Direct contraction in the adapted basis gives

\[
 \boxed{L_{\rm new}(q_0^2)=b_0-\theta_0(w),}
\]

and

\[
 \boxed{L_{\rm new}(yq_1^2)=w\{\theta_1(w)-b_0\}.}
\]

Therefore:

- if a directed enclosure proves `b_0<theta_0(w)`, then `q_0^2` is an explicit
  half-line-nonnegative RH-disproof response;
- if it proves `b_0>theta_1(w)`, then `y q_1^2` is an explicit such response.

The corresponding exact L-9308 portfolio on the augmented nodes is recovered
from either response polynomial `P` by

\[
 \boxed{
 \beta_i=-\frac{P(-u_i)}{\prod_{j\ne i}(u_j-u_i)},}
\]

where the augmented node list includes `w`.

## Rank-one affine-pencil interpretation

In the ordinary monomial basis, changing `b_0` by `delta` changes the moments by

\[
 \delta b_k=(-w)^k\delta.
\]

Hence

\[
 \delta H_0=\delta vv^T,
 \qquad
 v=(1,-w,w^2,\ldots,(-w)^m)^T,
\]

while

\[
 \delta H_1=-w\delta vv^T.
\]

The lower and upper constraints are therefore two opposite rank-one Schur gates
attached to evaluation at the exterior point `y=-w`. This is the finite
Geronimus-transform geometry behind the recurrence.

## Exact interval use

The threshold formulas are exact when the old moments are exact. For directed
old-moment intervals, a proof producer should not invert interval matrices
naively. It should instead:

1. select exact rational witness vectors from midpoint `C_0,C_1`;
2. contract the complete old-moment and `b_0` boxes exactly;
3. promote a negative only when the resulting upper endpoint is strictly below
   zero;
4. use a robust exact LDL-plus-radius argument if full positivity of the new cone
   is desired.

A midpoint outside a midpoint gate is only a nomination until this interval
replay is complete.

## Analytic domain audit

- All nodes and response variables lie in `u>=0`; the added node satisfies
  `w>0` and is distinct from the old nodes.
- The result is finite-dimensional exact algebra. It introduces no logarithm,
  square root, contour, branch, zero, or limiting interchange.
- The RH implication is inherited from L-9308 and from the exact direct-xi and
  count-deflation semantics used to produce the scalar functional.

## Gap audit

1. The theorem assumes strict positivity of the old degree-`2m` cone. A merely
   semidefinite old cone requires pseudoinverse range conditions and is not
   silently covered.
2. The new direct-xi primitive must use the same completed-xi normalization,
   common scale, ordinate, and count-deflation profile as the old table.
3. A discovery midpoint is not a candidate claim.
4. An exact response witness still requires an independently reviewed direct-xi
   producer and the inherited canonical-product/count-deflation theorem chain.

## Suggested next attack

Use the PR #103 exact old moment table and evaluate a short ladder of rational
square anchors. The first operational nominees are `w=1` (`x=1`) and `w=4`
(`x=2`). Each requires only one new direct completed-xi rectangle, while the old
fifteen moments and both Schur blocks are reused exactly.

# L-12101 — Positive-anchor one-moment transform and two-sided Schur gate

Claim ID: L-12101  
Title: Adding one positive direct-xi node introduces one new moment and two opposing rank-one half-line constraints  
Status: PROPOSED  
Authoring agent: `gpt56-03-i`  
Created: 2026-07-26  
Dependencies: L-9308; L-9309; L-9310; L-9311 for the zero-anchor specialization  
Scope: finite count-deflated direct-completed-xi response tables  
Related counterexample candidates: none

## Statement

Let

\[
 0<u_1<\cdots<u_n
\]

be an old direct-xi response table. Under the inherited RH-conditional response
representation, write its moment functional as

\[
 a_k=\int_0^\infty y^k\,d\mu(y),
 \qquad 0\le k\le d,
\]

for a positive measure `mu`. In the PR #103 / PR #112 specialization,
`d=n-2=14`.

Fix a positive rational anchor

\[
 w>0,
 \qquad w\notin\{u_1,\ldots,u_n\},
\]

and adjoin it to the node table. The new response denominator gains the factor
`y+w`. Define

\[
 b_k=\int_0^\infty\frac{y^k}{y+w}\,d\mu(y).
\]

Then

\[
 \boxed{a_k=b_{k+1}+w b_k}\qquad(0\le k\le d),
\]

or equivalently

\[
 \boxed{b_{k+1}=a_k-wb_k}.
\]

Thus all `d+2` new moments are determined by the single new scalar `b_0`.
Explicitly,

\[
 \boxed{
 b_k=(-w)^k b_0+
 \sum_{j=0}^{k-1}(-w)^{k-1-j}a_j
 }
 \qquad(k\ge1).
\]

For `w=0`, this becomes the zero-anchor identity `b_(k+1)=a_k` of
L-9311.

## Rank-one moment pencils

Put

\[
 c_0=0,
 \qquad
 c_k=\sum_{j=0}^{k-1}(-w)^{k-1-j}a_j
 \quad(k\ge1),
\]

and let

\[
 z_r=(-w)^r.
\]

For the new degree bound `D=d+1`, define

\[
 H_0(b_0)=(b_{i+j})_{0\le i,j\le\lfloor D/2\rfloor},
\]

\[
 H_1(b_0)=(b_{i+j+1})_{0\le i,j\le\lfloor(D-1)/2\rfloor}.
\]

With the corresponding truncations of `z`,

\[
 \boxed{H_0(b_0)=C_0+b_0zz^{\mathsf T}},
\]

\[
 \boxed{H_1(b_0)=C_1-wb_0zz^{\mathsf T}},
\]

where `(C_0)_(ij)=c_(i+j)` and `(C_1)_(ij)=c_(i+j+1)`.
The same scalar therefore repairs `H_0` in the positive direction and `H_1`
in the negative direction. This is the essential difference from the zero
anchor, where the second pencil is independent of `b_0`.

## Exact admissible interval from any interior reference

Choose any rational `t` for which both exact matrices

\[
 H_0(t)\succ0,
 \qquad
 H_1(t)\succ0
\]

are certified positive definite. Put

\[
 q_0=z^{\mathsf T}H_0(t)^{-1}z,
 \qquad
 q_1=z^{\mathsf T}H_1(t)^{-1}z.
\]

Both numbers are positive rationals. The complete degree-`D` half-line cone is
positive semidefinite exactly when

\[
 \boxed{
 t-\frac1{q_0}\le b_0\le t+\frac1{wq_1}.
 }
\]

In particular, one positive anchor produces a **two-sided scalar gate**.

### Proof of the lower gate

Write `b_0=t+h`. Then

\[
 H_0(b_0)=H_0(t)+hzz^{\mathsf T}.
\]

Congruence by `H_0(t)^(-1/2)` reduces this to

\[
 I+hvv^{\mathsf T},
 \qquad
 \|v\|^2=q_0.
\]

Its eigenvalues are one copy of `1+hq_0` and the remaining copies of `1`.
Hence it is positive semidefinite precisely when

\[
 h\ge-1/q_0.
\]

### Proof of the upper gate

Similarly,

\[
 H_1(b_0)=H_1(t)-whzz^{\mathsf T}.
\]

After congruence by `H_1(t)^(-1/2)`, positivity is equivalent to

\[
 1-whq_1\ge0,
\]

which gives the upper bound.

## Explicit polynomial witnesses

The scalar gates come with exact fixed witnesses.

Let

\[
 x_0=H_0(t)^{-1}z,
 \qquad
 p_0(y)=\sum_j(x_0)_j y^j.
\]

Then

\[
 L(p_0^2)=q_0+(b_0-t)q_0^2.
\]

Therefore a strict upper enclosure

\[
 b_0<t-1/q_0
\]

certifies the nonnegative response polynomial `p_0(y)^2` as a finite negative
witness.

Likewise, with

\[
 x_1=H_1(t)^{-1}z,
 \qquad
 p_1(y)=\sum_j(x_1)_j y^j,
\]

one has

\[
 L(yp_1^2)=q_1-w(b_0-t)q_1^2.
\]

Thus

\[
 b_0>t+1/(wq_1)
\]

certifies the nonnegative response polynomial `y p_1(y)^2` as a finite
negative witness.

No eigensolver, fitted zero, or numerical SDP solution is required in either
certificate. A numerical solver may nominate `t` and a witness, but the final
checker uses exact rational matrices and vectors.

## Direct-xi formula for `b_0`

Let

\[
 D(y)=\prod_{i=1}^n(y+u_i),
\]

and let `F(u)` be the count-deflated logarithmic modulus used by L-9308. On the
extended nodes `w,u_1,...,u_n`, the response-`1` coefficient of the new anchor
is

\[
 \boxed{\beta_w=-\frac1{D(-w)}}.
\]

The old-node part has response polynomial

\[
 \boxed{
 P_\gamma(y)=\frac{1-D(y)/D(-w)}{y+w}.
 }
\]

Indeed,

\[
 -\beta_wD(y)+(y+w)P_\gamma(y)=1.
\]

Hence the exact new scalar is

\[
 b_0=\beta_wF(w)+\sum_i\gamma_iF(u_i).
\]

The coefficients sum to zero, so a common completed-xi power-of-two scale
cancels exactly.

## Reduced one-point replay

Fix one old reference node `u_r`. Add `beta_w` to the old coefficient at that
node, obtaining a zero-sum old-node vector. Its response polynomial is

\[
 \boxed{
 P_r(y)=
 \frac{1-D(y)/D(-w)}{y+w}
 +\frac{D(y)}{D(-w)(y+u_r)}.
 }
\]

The leading terms cancel, so `deg P_r<=n-2`. Writing

\[
 P_r(y)=\sum_{k=0}^{n-2}p_{r,k}y^k,
\]

one obtains

\[
 \boxed{
 b_0=\beta_w\bigl(F(w)-F(u_r)\bigr)
      +\sum_{k=0}^{n-2}p_{r,k}a_k.
 }
\]

At `w=0`, this is exactly the reduced zero-anchor formula of L-9313.

A production certificate should compute `b_0` both from the full extended-node
barycentric contraction and from this reduced formula. The two directed
intervals enclose the same scalar and must overlap; their intersection may be
used as the final enclosure.

## Complete degree-15 specialization

For the sixteen-node PR #103 table, `d=14`. One positive anchor produces
moments `b_0,...,b_15` and two `8 x 8` matrices

\[
 H_0=(b_{i+j})_{0\le i,j\le7},
 \qquad
 H_1=(b_{i+j+1})_{0\le i,j\le7}.
\]

By L-9310, these matrices are positive semidefinite if and only if every real
response polynomial of degree at most fifteen that is nonnegative on
`[0,infinity)` has nonnegative value. A strict failure of either matrix is
therefore a finite direct-xi counterexample witness through the inherited
analytic gates.

## Interval certificate

For directed old moments and a directed `b_0` enclosure, a checker must not
substitute midpoint values into the threshold formulas and call the result a
proof. It must instead do one of the following:

1. freeze an exact rational square witness and prove its interval quadratic-form
   upper endpoint is negative; or
2. freeze rational midpoint matrices, prove exact positive pivots after a
   rational spectral shift, and show the complete interval-box operator radius
   is smaller than that shift.

Any zero-touching result is unresolved.

## Gap audit

1. The anchor must be positive and distinct from every old node.
2. `F(w)`, the old moments, the reference residual, count profile, ordinate, and
   completed-xi normalization must be identical across the two replays.
3. Raw interval width in `b_0` is not a scale-free measure of spectral
   sensitivity; large anchors can create algebraically tiny scalar gates.
4. A positive result closes only the declared table, anchor, count profile, and
   degree bound.
5. Any strict negative still requires independent completed-xi reproduction and
   review of the inherited canonical-product and total-count implications.

## Suggested production targets

For the exact PR #103 ordinate, the cheapest new calculations are anchors

\[
 w\in\left\{\frac18,\frac{3}{16},\frac14,
             \frac38,\frac12,\frac34,1\right\}.
\]

Each requires one new direct completed-xi rectangle at
`x=sqrt(w)`. The anchor `w=1` lies at `Re(s)=3/2`, where direct zeta evaluation
is comparatively benign. The multi-anchor use of this set is developed in
L-12102.
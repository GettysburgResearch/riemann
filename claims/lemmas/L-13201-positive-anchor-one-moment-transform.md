# L-13201 — Positive-anchor one-moment transform and two-sided Schur gate

Claim ID: L-13201  
Title: A positive direct-xi anchor introduces one moment and two opposing rank-one gates  
Status: PROPOSED  
Authoring agent: `gpt56-03-i`  
Created: 2026-07-26  
Dependencies: L-9308, L-9309, L-9310; zero-anchor specialization L-9311  
Scope: finite count-deflated direct-completed-xi response tables  
Related counterexample candidates: none

> Canonical-ID note: this claim supersedes the temporary authoring ID
> `L-12101`, withdrawn after concurrent PR #125 allocated that identifier.

## Statement

Let

\[
 a_k=\int_0^\infty y^k\,d\mu(y),\qquad 0\le k\le d,
\]

for a positive measure `mu`. Fix a positive rational anchor `w` distinct from
the old direct-xi nodes and define

\[
 b_k=\int_0^\infty\frac{y^k}{y+w}\,d\mu(y).
\]

Then

\[
 \boxed{a_k=b_{k+1}+wb_k},
 \qquad
 \boxed{b_{k+1}=a_k-wb_k}.
\]

Thus every new moment is determined by the single scalar `b_0`, explicitly

\[
 \boxed{
 b_k=(-w)^kb_0+
 \sum_{j=0}^{k-1}(-w)^{k-1-j}a_j.
 }
\]

For `w=0`, this reduces to L-9311.

## Opposing rank-one pencils

Let

\[
 z_r=(-w)^r,
\]

and let `D=d+1`. The complete half-line moment matrices are

\[
 H_0(b_0)=(b_{i+j})_{0\le i,j\le\lfloor D/2\rfloor},
\]

\[
 H_1(b_0)=(b_{i+j+1})_{0\le i,j\le\lfloor(D-1)/2\rfloor}.
\]

Writing the constant parts as `C_0,C_1`, one has

\[
 \boxed{H_0(b_0)=C_0+b_0zz^{\mathsf T}},
\]

\[
 \boxed{H_1(b_0)=C_1-wb_0zz^{\mathsf T}}.
\]

The same scalar improves the first matrix and worsens the second.

## Exact two-sided gate

Choose any rational `t` such that both `H_0(t)` and `H_1(t)` are positive
definite. Put

\[
 q_0=z^{\mathsf T}H_0(t)^{-1}z,
 \qquad
 q_1=z^{\mathsf T}H_1(t)^{-1}z.
\]

Then the complete degree-`D` half-line cone is positive semidefinite exactly
when

\[
 \boxed{
 t-\frac1{q_0}\le b_0\le t+\frac1{wq_1}.
 }
\]

### Proof

If `b_0=t+h`, then

\[
 H_0(b_0)=H_0(t)+hzz^{\mathsf T}.
\]

Congruence by `H_0(t)^{-1/2}` gives `I+hvv^T` with `||v||^2=q_0`, whose only
nontrivial eigenvalue is `1+hq_0`. Hence the lower gate is necessary and
sufficient. Likewise

\[
 H_1(b_0)=H_1(t)-whzz^{\mathsf T}
\]

has nontrivial congruence eigenvalue `1-whq_1`, yielding the upper gate. ∎

## Explicit witnesses

Set

\[
 x_0=H_0(t)^{-1}z,
 \qquad
 p_0(y)=\sum_j(x_0)_jy^j.
\]

Then

\[
 L(p_0^2)=q_0+(b_0-t)q_0^2.
\]

Thus `b_0<t-1/q_0` gives an explicit negative square response. Similarly, with
`x_1=H_1(t)^{-1}z`,

\[
 L(yp_1^2)=q_1-w(b_0-t)q_1^2,
\]

so `b_0>t+1/(wq_1)` gives an explicit negative `y`-times-square response.

## Direct-xi contraction

Let

\[
 D(y)=\prod_{i=1}^n(y+u_i).
\]

The new-node response-one coefficient is

\[
 \boxed{\beta_w=-1/D(-w)}.
\]

Using one old reference node `u_r`, define

\[
 P_r(y)=
 \frac{1-D(y)/D(-w)}{y+w}
 +\frac{D(y)}{D(-w)(y+u_r)}.
\]

The leading terms cancel, so `deg P_r<=n-2`. If

\[
 P_r(y)=\sum_{k=0}^{n-2}p_{r,k}y^k,
\]

then

\[
 \boxed{
 b_0=\beta_w(F(w)-F(u_r))+
 \sum_{k=0}^{n-2}p_{r,k}a_k.
 }
\]

A production certificate computes `b_0` both from the full extended-node
barycentric contraction and this reduced contraction, and requires directed
overlap.

## Degree-15 specialization

For the sixteen-node PR #103 table, `d=14`. One positive anchor yields moments
`b_0,...,b_15` and two `8 x 8` matrices. By L-9310, their positivity is
necessary and sufficient for every degree-at-most-15 real response polynomial
nonnegative on `[0,infinity)`.

## Proof boundary

- The anchor is positive and distinct from every old node.
- Every primitive, old moment, count profile, ordinate, and normalization must
  be source-bound.
- A midpoint threshold is not a proof input; the final object is a directed
  fixed-vector sign or an interval positive-definiteness certificate.
- A strict negative still requires independent completed-xi reproduction and
  review of the inherited response and count-deflation gates.

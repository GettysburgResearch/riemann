# L-9315 — Reduced one-new-point contraction for a positive anchor

Claim ID: `L-9315`  
Title: A positive-anchor response-1 moment is reconstructed from one new point, one old reference point, and the old monomial moments  
Status: `PROPOSED`  
Authoring agent: `gpt56-04-e`  
Created: 2026-07-26  
Dependencies: L-9308, L-9309, L-9314  
Scope: exact producer/checker reduction for one additional direct-xi node  
Related counterexample candidates: X-9312 anchor nominations

## Setup

Use distinct old nodes `u_1,...,u_n`, an added node `w>0`, and the direct-xi
residual values `F(u)` from the same normalization and count-deflation profile.
Let `b_0` be the new scalar moment whose response polynomial is `1` on the
augmented node set.

The exact response-1 coefficients are

\[
 \boxed{
 \widetilde\beta_i
 =-\frac{1}{\prod_{j\ne i}(u_j-u_i)},}
\]

where the augmented list is

\[
 u_0=w,u_1,\ldots,u_n.
\]

In particular,

\[
 \boxed{
 \widetilde\beta_w
 =-\frac{1}{\prod_{i=1}^n(u_i-w)}.}
\]

Direct evaluation of all `n+1` terms can suffer severe barycentric cancellation.
The following exact reduction removes that requirement.

## Reduced contraction

Choose any old reference index `r`. Define an old-node vector `gamma` by

\[
 \gamma_i=\widetilde\beta_i\quad(i\ne r),
\]

and

\[
 \gamma_r=\widetilde\beta_r+\widetilde\beta_w.
\]

Because the augmented coefficient vector sums to zero,

\[
 \sum_{i=1}^n\gamma_i=0.
\]

Let its old response polynomial be

\[
 P_\gamma(y)
 =-\sum_{i=1}^n\gamma_i\frac{D(y)}{y+u_i}
 =\sum_{k=0}^{n-2}p_k y^k.
\]

Then, exactly,

\[
 \begin{aligned}
 b_0
 &=\widetilde\beta_wF(w)
   +\sum_{i=1}^n\widetilde\beta_iF(u_i)\\
 &=\widetilde\beta_w\{F(w)-F(u_r)\}
   +\sum_{i=1}^n\gamma_iF(u_i)\\
 &=\boxed{
   \widetilde\beta_w\{F(w)-F(u_r)\}
   +\sum_{k=0}^{n-2}p_k a_k.}
 \end{aligned}
\]

Thus the positive-anchor extension needs only:

1. one new direct-xi residual at `w`;
2. one already committed old residual at the reference node;
3. the already certified old monomial moments `a_k`;
4. exact rational coefficients.

No new full `n+1`-point barycentric contraction is required.

## Proof

The first equality is the definition of the new response-1 moment. Add and
subtract `widetilde beta_w F(u_r)`. The remaining old-node coefficient vector is
`gamma`, which is zero-sum and therefore has a unique old response polynomial of
degree at most `n-2`. Expanding that polynomial in the monomial basis and using
linearity gives

\[
 \sum_i\gamma_iF(u_i)=\sum_kp_ka_k.
\]

This proves the formula.

## Directed width budget

Suppose directed intervals are available for `F(w)`, `F(u_r)`, and every old
moment. Exact interval arithmetic gives

\[
 \operatorname{wid}(b_0)
 \le
 |\widetilde\beta_w|
 \{\operatorname{wid}F(w)+\operatorname{wid}F(u_r)\}
 +\sum_k|p_k|\operatorname{wid}(a_k).
\]

Let

\[
 d_-(w)=b_0^{\rm mid}-\theta_0(w),
 \qquad
 d_+(w)=\theta_1(w)-b_0^{\rm mid}
\]

be discovery midpoint distances. After subtracting the exact old-moment width
budget `E_old`, the quantities

\[
 \boxed{
 \mu_-(w)=\frac{d_-(w)-E_{\rm old}}{|\widetilde\beta_w|},
 \qquad
 \mu_+(w)=\frac{d_+(w)-E_{\rm old}}{|\widetilde\beta_w|}}
\]

measure the remaining repair distance in units of the new primitive. They are a
better production ranking than raw Schur gaps: a tiny raw gap can still be easy
to decide when the new-point coefficient is tiny.

## Exact checker protocol

A proof-producing run should:

1. bind the new point to the old ordinate, normalization, common xi scale, and
   count profile;
2. evaluate it at two directed precisions and require nesting;
3. compute `F(w)-F(u_r)` with directed logarithm and deflation arithmetic;
4. add the old moment intervals with the exact `p_k`;
5. contract the L-9314 lower and upper rational Schur witnesses;
6. emit a counterexample nomination only when one complete quadratic interval
   has upper endpoint strictly below zero.

The direct `n+1`-point contraction should be retained as an independent overlap
check when computationally affordable.

## PR #103 specialization

For the committed PR #103 table:

\[
 u_i=2^{-40},2^{-38},\ldots,2^{-10},
\]

and the natural reference is `u_r=2^-40`. At `w=4`, the new horizontal point is
exactly

\[
 x=\sqrt w=2,
 \qquad
 s=\frac52+iT.
\]

The new barycentric coefficient has magnitude approximately

\[
 |\widetilde\beta_w|
 \approx2.329064546211943\times10^{-10}.
\]

The exact old-moment box contributes less than `7.071e-33` to `b_0`, while the
midpoint gate width is about `9.510e-12`. Therefore a very modest directed width
on the single new point is enough to decide the nomination.

## Analytic and dependency audit

- The reduction itself is exact finite rational algebra.
- It does not prove that a supplied residual interval is analytically valid.
- The old reference and new point must use identical deflation shells; mixing
  profiles invalidates the subtraction.
- The count-deflation and RH implication remain inherited theorem gates.

## Suggested next attack

Generate direct completed-xi rectangles at `x=1` and `x=2` at 512 and 640 bits,
then run both the reduced replay and the direct augmented contraction. The `x=2`
case is numerically attractive because `Re(s)=5/2`, far inside the absolutely
convergent zeta half-plane.

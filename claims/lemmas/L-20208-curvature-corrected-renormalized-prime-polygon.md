# L-20208 — Curvature-corrected renormalized prime polygon

Claim ID: `L-20208`  
Title: The prime-positive compact-cell criterion is exactly a prime-mass polygon margin minus one Bregman curvature penalty  
Status: `PROPOSED — COMPLETE CONVEX-ALGEBRAIC IDENTITY; COFINAL SIGN OPEN`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `L-20207`; the decomposition `Psi=F-G` and prime-prefix notation of PR #219  
Scope: fixed `0<a<b<log 2`, integer `r>=2`

## 1. Renormalized archimedean barrier

Write the exact zeta screw function as

\[
 \Psi(T)=F(T)-G(T),
 \qquad
 G(T)=\sum_q a_q(T-\nu_q)_+,
 \qquad
 a_q={\Lambda(q)\over\sqrt q},
 \quad \nu_q=\log q.
 \tag{1}
\]

Fix

\[
 I=[a,b]\subset(0,\log2)
\]

and an integer `r>=2`. On the dilated interval `rI`, define

\[
 \boxed{
 H_r(T)=F(T)-r^2F(T/r).}
 \tag{2}
\]

Since `G(T/r)=0` for `T/r in I`, the compact-cell defect is exactly

\[
 \boxed{
 \mathcal D_r(T/r)=G(T)-H_r(T).}
 \tag{3}
\]

The curvature is

\[
 H_r''(T)=F''(T)-F''(T/r)>0
 \tag{4}
\]

because `F''` is strictly increasing on the positive half-line. Hence `H_r` is strictly convex on `rI`.

## 2. Prime polygon and knot margins

List all prime powers in increasing order and define

\[
 A_j=\sum_{i\le j}a_i,
 \qquad
 B_j=\sum_{i\le j}a_i\nu_i.
 \tag{5}
\]

At a knot `T_j=nu_j`, the newly arriving ramp is zero, so either left or right prefix convention gives

\[
 G(T_j)=A_jT_j-B_j=A_{j-1}T_j-B_{j-1}.
 \tag{6}
\]

Put

\[
 M_{r,j}=\mathcal D_r(T_j/r)=G(T_j)-H_r(T_j).
 \tag{7}
\]

Together with the two fixed endpoint rows, `L-20207` proves that these are the only possible compact-cell minima.

## 3. Exact dual margin minus Bregman penalty

Let

\[
 \tau_{r,j}=(H_r')^{-1}(A_j)
 \tag{8}
\]

whenever `A_j` lies in the derivative range of `H_r` on the chosen extended convex domain. Define the dual prime-polygon reserve

\[
 \boxed{
 P_{r,j}=H_r^*(A_j)-B_j.}
 \tag{9}
\]

The Bregman divergence of `H_r` is

\[
 \mathfrak B_r(x,y)
 =H_r(x)-H_r(y)-H_r'(y)(x-y)\ge0.
 \tag{10}
\]

Then the knot value has the exact decomposition

\[
 \boxed{
 M_{r,j}
 =P_{r,j}-\mathfrak B_r(T_j,\tau_{r,j}).}
 \tag{11}
\]

Indeed,

\[
 H_r^*(A_j)=A_j\tau_{r,j}-H_r(\tau_{r,j}),
\]

and substitution into (6)--(7) gives (11) term by term.

Thus ordinary polygon domination

\[
 H_r^*(A_j)\ge B_j
\]

is necessary but not sufficient for the compact-cell sign. It must carry enough reserve to pay the exact curvature cost of placing the atomic prime mass at `T_j` rather than at the reference quantile `tau_(r,j)`.

The exact sign condition is

\[
 \boxed{
 H_r^*(A_j)-B_j
 \ge
 \mathfrak B_r(T_j,\tau_{r,j}).}
 \tag{12}
\]

## 4. Quantile-transport recurrence

Let the prime quantile step be

\[
 \nu_{\rm pp}(A)=T_j
 \quad\text{for }A_{j-1}<A\le A_j,
 \tag{13}
\]

and let

\[
 \tau_r(A)=(H_r')^{-1}(A).
 \tag{14}
\]

Because `(H_r^*)'=tau_r`, the dual reserve increments by

\[
 \boxed{
 P_{r,j}-P_{r,j-1}
 =\int_{A_{j-1}}^{A_j}
   [\tau_r(A)-T_j]\,dA.}
 \tag{15}
\]

This is an exact equal-mass transport ledger: the prime atom transports mass `a_j` to the location `T_j`, while the archimedean comparator transports the same mass through its increasing quantile `tau_r`.

The primal knot recurrence is the dual statement in physical coordinates:

\[
 \boxed{
 M_{r,j}-M_{r,j-1}
 =\int_{T_{j-1}}^{T_j}
   [A_{j-1}-H_r'(u)]\,du.}
 \tag{16}
\]

Equations (15) and (16) retain the cumulative cancellation that is destroyed by entrywise prime estimates.

## 5. Exact block transport certificate

For any consecutive block of atoms `p<j<=q`, summing (15) gives

\[
 P_{r,q}-P_{r,p}
 =\int_{A_p}^{A_q}
   [\tau_r(A)-\nu_{\rm pp}(A)]\,dA.
 \tag{17}
\]

Therefore a proof-producing block may contain locally unfavorable prime arrivals. It is enough to certify:

1. an incoming reserve `P_(r,p)`;
2. a directed lower bound for the block transport integral in (17);
3. a directed upper bound for every intra-block Bregman penalty in (10).

If the resulting reserve dominates every intra-block penalty, all knot values in the block are nonnegative. A cofinal partition with a subexponential residual proves the compact-cell criterion of `T-20205`, hence RH.

## 6. Curvature-only sufficient gate

Suppose on the relevant interval

\[
 0<m_r\le H_r''(T)\le L_r.
 \tag{18}
\]

Then

\[
 |T_j-\tau_{r,j}|
 \le {|H_r'(T_j)-A_j|\over m_r}
 \tag{19}
\]

and

\[
 \mathfrak B_r(T_j,\tau_{r,j})
 \le {L_r\over2m_r^2}
      |H_r'(T_j)-A_j|^2.
 \tag{20}
\]

Hence the explicit scalar inequality

\[
 \boxed{
 P_{r,j}
 \ge {L_r\over2m_r^2}
      |H_r'(T_j)-A_j|^2}
 \tag{21}
\]

is sufficient for the knot sign. This gate is deliberately conservative; the exact Bregman integral in (10) is preferred for production.

## 7. Relation to the global prime polygon

PR #219 uses the unrenormalized barrier `F` and identifies the full screw depth with the vertical deficit of the polygon through `(A_j,B_j)`. The present lemma uses the renormalized barrier

\[
 H_r(T)=F(T)-r^2F(T/r)
\]

forced by the dilation defect. It explains precisely how the two global attacks compose:

```text
prime polygon reserve
    minus
atomic-placement Bregman cost
    equals
prime-positive compact-cell defect.
```

This is stronger than merely observing that both routes involve the same prefix moments. It gives one common transport certificate that can be consumed by the square-screw, dilation, and polygon programmes.

## 8. Proof boundary

- All identities are exact convex algebra.
- No prime transport lower bound is proved here.
- A phase-blind PNT estimate does not control the order-one reserve in (12).
- The inverse derivative in (8) must be handled by endpoint subgradients if `A_j` lies outside a chosen restricted derivative range.
- Finite positive blocks do not establish the cofinal transport statement.

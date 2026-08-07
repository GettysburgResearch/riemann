# T-24501 — Parabolic carry transport proposal: corrected status

Claim ID: `T-24501`  
Status: `SUPERSEDED AS PRIMARY PROPOSAL BY T-24503; signed PNC remains an alternative open route`  
Scope: full Riemann Hypothesis conditional on a signed correction theorem  
Issue: #245

## 1. Prime ramp and seed

Define

\[
S_X=\sum_{q=p^a\le X}\frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
\]

For every real vector `b`, not necessarily nonnegative, `L-24501/L-24508` give

\[
J_X(b)=\sum_{q=p^a\le X}\Lambda(q)v_q(b).
\]

Hence the coordinate inequalities

\[
v_q(b)\le q^{-1/2}\log(X/q)
\]

imply `J_X(b)<=S_X` without a sign condition on `b`.

The explicit parabolic seed satisfies

\[
J_X(b_X^{(0)})\ge4\sqrt X-6\log X+O(1).
\]

## 2. What survived from the original PNC proposal

The tapered divisor-comb ledger of `L-24503` remains exact:

- noncoprime interactions are nonpositive;
- only coprime determinant-one equations `ad-bq=+-1` can create harmful cross-interaction;
- signed adjacent transport has exact cost weight `log(j^2/(j^2-1))`.

`L-24507` now proves that the uncorrected seed is already feasible for

\[
q\ge X/28
\]

once `X>=104301`. Thus a surviving two-stage PNC need only originate in the low-ratio block.

A sufficient signed PNC statement would construct a flow `F` such that

\[
v_q(b_X^{(0)}+\nabla^*F)\le w_X(q)
\quad(q=p^a\le X)
\]

and

\[
\sum_jF_j\log\frac{j^2}{j^2-1}=O(\log^2X).
\]

Coefficientwise positivity of the corrected `b` is no longer required.

## 3. Withdrawn components

The following parts of the first proposal are withdrawn:

1. the monotone Divisibility Cover, refuted by `R-24501`;
2. preservation of `b_m>=0` as an RH obligation, removed by `L-24508`;
3. the assertion that Jacobi convergence is the uniquely preferred closure.

The endpoint-projected Gram identity of `L-24509` supplies a cleaner primary proposal, `T-24503`, reducing the route to one explicit Green energy.

## 4. Conditional RH chain

Any signed correction satisfying the displayed constraints and `O(log^2 X)` cost gives

\[
S_X\ge4\sqrt X-O(\log^2X),
\]

and the existing square-screw/Landau transfer implies RH.

This conditional deduction remains valid. No such all-scale signed correction is proved in this file.

## Mandatory firewall

The exact scalar pairing

\[
J_X(b_X^{(0)})-S_X
=
\sum_{q=p^a}\Lambda(q)
\left[v_q(b_X^{(0)})-w_X(q)\right]
\]

must remain intact. A proof that replaces the signed residual by its positive part pays square-root cost by `R-24501` and cannot close the route.

## Status boundary

This file is retained as the corrected transport architecture. `T-24503` is the current primary full proposal. RH is not proved.

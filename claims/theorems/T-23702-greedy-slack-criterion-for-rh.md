# T-23702 — Greedy slack criterion for RH

Claim ID: `T-23702`  
Title: Polylogarithmic total slack in the canonical greedy carry packing implies the Riemann Hypothesis  
Status: **PROPOSED COMPLETE CONDITIONAL THEOREM; SLACK ESTIMATE OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Dependencies: `L-23701`, `L-23702`, `L-23705`, `L-23706`; square-screw/Landau transfer on PRs #202/#218  
Scope: corrected minimal form of the Digital Blocker Theorem

## 1. Canonical slack

Let `d_X` be the exact minimum-ratio greedy vector of `L-23701` and put

\[
\Sigma_X
=
\sum_{q=2}^X
\left[
 q^{-1/2}\log(X/q)
 -\sum_{n=q}^Xd_X(n)\beta_{nq}
\right].
\tag{T-23702.1}
\]

Every summand is nonnegative.

## 2. Corrected arithmetic theorem

Assume that, for some fixed `A`,

\[
\boxed{
\Sigma_X=O(\log^A(2X)).}
\tag{T-23702.2}
\]

Then `L-23705` gives automatically

\[
\sum_n d_X(n)(\log(n+1)+3)=O(\log^2X)
\tag{T-23702.3}
\]

and

\[
\sum_n n d_X(n)
=8\sqrt X-2\Sigma_X+O(\log^2X).
\tag{T-23702.4}
\]

The entropy transfer of `L-23702` therefore yields

\[
\boxed{
\sum_{q=p^k\le X}
 {\Lambda(q)\over\sqrt q}\log{X\over q}
\ge
4\sqrt X-O(\log^{\max(A,2)}X).}
\tag{T-23702.5}
\]

## 3. RH deduction

Insert (T-23702.5) into the exact square-screw identity at `X=N^2`. The negative
part of the square-screw statistic is polylogarithmic, hence subpolynomial. The
square-sampling interpolation and Landau one-sign transfer on PRs #202/#218 give
rightmost-zero exponent zero. Functional-equation symmetry then gives

\[
\boxed{\mathrm{RH}.}
\tag{T-23702.6}
\]

Thus the original two-part DBT is replaced by the one scalar Greedy Slack
Theorem (T-23702.2).

## 4. Exact blocker form

By `L-23706`, (T-23702.2) is exactly

\[
\boxed{
\sum_{n=2}^X
 {n-1\over n+1}
 \left[
 {\rho_X^{(n)}(n)\over\beta_{nn}}
 -\min_{\beta_{nq}>0}
  {\rho_X^{(n)}(q)\over\beta_{nq}}
 \right]
=O(\log^A X).}
\tag{T-23702.7}
\]

This is the sole independent arithmetic estimate left in the greedy proposal.

## 5. Review boundary

Closed conditionally:

```text
polylogarithmic greedy slack
-> sharp carry mass and automatic lower-order mass
-> prime ramp lower bound
-> square-screw/Landau
-> RH.
```

Open:

- (T-23702.2), equivalently (T-23702.7);
- RH.

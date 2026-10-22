# T-27202 — Balanced carry slack criterion for RH

Claim ID: `T-27202`  
Title: A nonnegative balanced carry flow with subpower total unweighted slack implies the sharp prime ramp and the Riemann Hypothesis  
Status: **PROPOSED COMPLETE CONDITIONAL THEOREM PENDING REVIEW**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-27203`; reviewed square-screw/Landau transfer  
Scope: finite elementary front end plus one analytic terminal transfer

## 1. Hypothesis

Fix one `eta>0`. Suppose that for every sufficiently large `X` there are
coefficients

\[
d_{n,j}\ge0,
\qquad
\eta n\le j\le(1-\eta)n,
\]

such that

\[
v(q)=\sum_{n,j}d_{n,j}\chi_{n,j}(q)
\le q^{-1/2}\log(X/q)
\]

for every integer `2<=q<=X`, and the total unweighted slack satisfies

\[
\boxed{
\Sigma_X=
\sum_{q=2}^{X}
\left[q^{-1/2}\log(X/q)-v(q)\right]
=X^{o(1)}.}
\tag{T-27202.1}
\]

Exact MFT is the special case `Sigma_X=0`.

## 2. Sharp prime ramp

`L-27203` gives

\[
\sum_{q=p^a\le X}\frac{\Lambda(q)}{\sqrt q}\log(X/q)
\ge4\sqrt X-X^{o(1)}.
\tag{T-27202.2}
\]

No pointwise Carry Saturation, global carry-profile positivity, or capacity
lower bound is required.

## 3. RH transfer

At square endpoints `X=N^2`, the exact square-screw formula converts
(T-27202.2) to a subpower upper envelope for the RH-sensitive screw statistic.
The reviewed square-mesh interpolation and Landau one-sign theorem exclude every
zeta zero with real part greater than `1/2`. The functional equation excludes
the reflected half.

Hence

\[
\boxed{\mathrm{RH}.}
\]

## 4. Status boundary

The implication is complete subject to review of the inherited square-screw
normalization. The construction of the flow in (T-27202.1) remains the sole
arithmetic hinge.

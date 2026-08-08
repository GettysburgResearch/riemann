# R-32302 — Fixed third-Abel positivity of the average-carry inverse is false

Claim ID: `R-32302`  
Title: The positivity seen for square-root hinge inverses does not extend to the quadratic-prefix / third-cumulative cone  
Status: **EXACT FINITE REFUTATION**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Scope: blocks a generic total-positivity/finite-Abel proof of SHARP; does not refute SHARP

## 1. The candidate shortcut

Let `B=(beta_(nq))` be the upper-triangular average-carry matrix from `L-32303`.
A tempting route to SHARP is to prove that `B^(-1)` is positive on a fixed finite cumulative cone and then use complete monotonicity of `q^(-1/2)`.

The natural third-cumulative test is the quadratic-prefix target

\[
W_T(q)=\binom{T-q+2}{2},
\qquad 2\le q\le T.
\tag{R-32302.1}
\]

Let `a_T(n)` be its unique triangular inverse:

\[
W_T(q)=\sum_{n=q}^{T}a_T(n)\beta_{nq}.
\tag{R-32302.2}
\]

If all `a_T(n)` were nonnegative, every third cumulative of every inverse row would be nonnegative.

## 2. Exact counterexample

At

\[
T=1000,
\qquad n=11,
\]

use the exact multiples-Möbius state

\[
u_m=\sum_{k\le1000/m}\mu(k)W_{1000}(mk)
\tag{R-32302.3}
\]

and the exact adjoint formula

\[
a_T(j)=
\frac{(j+1)[j u_j-(j-2)u_{j+1}]
      +2\sum_{m=j+2}^{T}u_m}
     {j(j-1)}.
\tag{R-32302.4}
\]

All quantities in (R-32302.3)--(R-32302.4) are integers before the final rational division.  Direct exact evaluation gives numerator

\[
-312716
\]

and hence

\[
\boxed{
a_{1000}(11)=-\frac{156358}{55}<0.
}
\tag{R-32302.5}
\]

Therefore the fixed third-Abel positivity theorem is false for the average-carry inverse.

## 3. Consequence for SHARP

The directed square-root hinge certificates through `T=10^6` cannot be explained by a source-blind statement such as

```text
B^(-1) preserves all decreasing targets;
B^(-1) preserves every convex target;
B^(-1) preserves a fixed third-cumulative cone.
```

The square-root exponent is load bearing.  A proof of SHARP must exploit the actual fractional/Stieltjes structure of

\[
q^{-1/2}-T^{-1/2},
\]

or an equivalent source-specific arithmetic identity.

This mirrors the repository-wide lesson from the failed fixed Abel producers: increasing a generic smoothing order does not remove the reciprocal-zeta obstruction.

## 4. Proof boundary

Refuted exactly:

- fixed third-Abel / quadratic-prefix positivity of the average-carry inverse.

Unaffected:

- the exact square-root hinge reduction;
- the directed SHARP nominations;
- the weaker half-power Cycle-Debt reduction;
- RH, which remains unproved.

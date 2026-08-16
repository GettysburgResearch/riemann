# T-96301 — Positivity of one explicit scalar component row implies RH

Claim ID: `T-96301`  
Status: **PROPOSED COMPLETE CONDITIONAL IMPLICATION — SCALAR PRODUCER OPEN**  
Created: 2026-08-17  
Depends on: `L-96301`; Landau's theorem for Mellin transforms  
RH status: **unproved because scalar positivity remains open**

Assume that

\[
\boxed{
\mathcal R_X=5c_X(2)+3c_X(3)\ge0
\qquad(X\ge X_0).
}
\tag{T-96301.1}
\]

Adding or subtracting the compact initial interval does not affect the Mellin abscissa argument, so one may suppose the function is nonnegative on its complete domain.

Landau's theorem says that the real abscissa of convergence of its Mellin transform must be a singularity unless the defining integral is holomorphic farther left. But `L-96301` gives a transform analytic at every positive real `s`, and its numerator is nonzero at every open-strip zeta zero. Therefore an off-line zero would create a pole inside the holomorphy half-plane of the defining nonnegative Mellin integral, a contradiction.

Hence (T-96301.1) implies RH.

The open scalar producer is:

```text
SPRP — Single Positive-Row Producer

Prove 5 c_X(2)+3 c_X(3) >= 0 for every sufficiently large integer X.
```

This is strictly smaller than the former requirement that every component row be nonnegative, and smaller than the two-row producer `LPTRP_23` of PR #546.

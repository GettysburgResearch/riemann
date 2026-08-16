# L-96202 — Two nonnegative fixed rows and their reciprocal-zeta transforms exclude off-line zeros

Claim ID: `L-96202`  
Status: **PROPOSED COMPLETE COMPOSITION OF EXACT INPUTS — REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `L-96200`, `L-96201`, PR #542 `L-96000`

For `j=2,3`, let

\[
f_j(X)=c_X(j).
\]

The finite initial-prime identity and triangular support turn `L-96200` into

\[
f_j(X)\ge0\qquad(X\ge1).
\tag{L-96202.1}
\]

PR #542 proves, initially in an absolute-convergence half-plane and then by meromorphic continuation,

\[
\mathcal C_j(s)=\int_1^\infty f_j(X)X^{-s-1}dX
 ={C_j\over s^2}+{P_j(s+1/2)\over s^2\zeta(s+1/2)}.
\tag{L-96202.2}
\]

The right side is analytic at every positive real `s`. For a nonnegative locally integrable function, Landau's theorem says that a finite real abscissa of convergence is a singularity unless the defining transform continues through it. Hence (L-96202.1) and (L-96202.2) imply that both defining Mellin integrals are holomorphic in `Re s>0`.

If `zeta(rho)=0` with `Re rho>1/2`, put `s_rho=rho-1/2`. By `L-96201`, at least one of `P_2(rho),P_3(rho)` is nonzero. The corresponding right side of (L-96202.2) has a nonremovable pole at `s_rho`, contradicting holomorphy of the nonnegative Mellin integral in `Re s>0`.

Thus there is no zero to the right of the critical line. The functional equation excludes the reflected left half, yielding the proposed RH conclusion.

No estimate of `F_Lambda`, native endpoint deficit, factor-67 recursion, Target–Lorenz transport, CPBD, First-Hermite exclusion, or Mertens square-root cancellation occurs in this composition.

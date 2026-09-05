# R-105116 - An active strict radius budget has no minimizer

Claim ID: R-105116

Status: **EXACT REFUTATION**

Created: 2026-08-23

RH status: **unproved**

Suppose \(0<R\le\sum_jv_j\) and replace the closed budget in L-105116 by

\[
\sum_jv_j\varepsilon_j<R.
\]

At any feasible point, at least one epsilon is below one.  Increasing such
coordinates slightly while preserving the strict inequality decreases
\(\Phi\).  Therefore no feasible point minimizes the objective; the closed-
budget optimum is only the infimum.

This is why L-105116 builds strict geometric slack into
\(R_\delta=(1-\delta)d/2\) and then optimizes over the closed budget
\(S_{\rm nom}\le R_\delta\).  The resulting disk radius still obeys the
strict geometric inequality \(2S<d\).

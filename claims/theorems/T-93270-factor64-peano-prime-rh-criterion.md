# T-93270 - Factor-64 Peano prime criterion for the Riemann Hypothesis

Claim ID: `T-93270`
Status: **PROPOSED COMPLETE TRANSFER THEOREM; PRIME BOUND OPEN**
Created: 2026-08-16
Depends on: `L-93270`; the classical RH square-root prime error; Mellin inversion and the standard pole-exclusion converse
Scope: full RH criterion

Define

\[
\mathcal P_{64}(X)
=\sum_{n\le X}\Lambda(n)W_{64}(n/X),
\tag{T-93270.1}
\]

where `W_64` is the compact curvature kernel of `L-93270`.

Its Mellin transform is

\[
\int_1^\infty \mathcal P_{64}(X)X^{-s-1}\,dX
=\widehat W_{64}(s)
\left(-\frac{\zeta'}{\zeta}(s)\right)
\tag{T-93270.2}
\]

initially in the half-plane of absolute convergence, after the usual normalization of the Riesz variable.

By `L-93270`, `widehat W_64` is nonzero at every nontrivial zeta zero. Thus every zero with `Re rho>1/2` creates a nonremovable pole in the half-plane reached by a square-root bound.

The proposed criterion is

\[
\boxed{
RH
\iff
\mathcal P_{64}(X)
=O\!\left(\sqrt X\,(\log(2X))^A\right)
\quad\text{for some fixed }A.
}
\tag{T-93270.3}
\]

## RH implies the bound

Under RH, the von Koch estimate

\[
\psi(X)=X+O(\sqrt X\log^2(2X))
\tag{T-93270.4}
\]

and one Stieltjes integration by parts against the compact piecewise-polynomial kernel give (T-93270.3), with a fixed logarithmic exponent.

## The bound implies RH

If (T-93270.3) holds, the Mellin transform of the normalized error extends holomorphically to `Re s>1/2`, modulo the declared elementary kernel poles outside the open critical strip. An off-line zero would produce the nonremovable pole described above, contradiction. Functional-equation symmetry gives RH.

## Boundary

The transform and pole audit are proposed complete. The unconditional square-root bound for `P_64` is not proved. Positivity of the underlying potential `Phi_64` does not imply it, by `R-93270`.

# L-97603 — Completed-parity scalar coupling is an exact finite Lorenz primal-dual problem

Claim ID: `L-97603`  
Status: **PROVED EXACT FINITE-DIMENSIONAL REDUCTION**  
Created: 2026-08-17  
RH status: **unproved; the uniform arithmetic inequality remains open**

Fix a real endpoint `X` and fully expand the finite owner ledger of `L-97601`.
Let the actual even atoms have capacities `a_i>=0`, target coordinates `t_i>0`
and scalar coordinates `r_i`.  Let the complete odd target and scalar demand be
`T_O` and `R_O`.

A target-exact scalar-superordinate common-source coupling exists exactly when
there are coefficients

\[
0\le u_i\le a_i,
\qquad
\sum_i t_i u_i=T_O,
\qquad
\sum_i r_i u_i\ge R_O.
\]

Define

\[
\Phi_X(T)=\max\left\{\sum_i r_i u_i:
0\le u_i\le a_i,\ \sum_i t_i u_i=T\right\}.
\]

Then feasibility is equivalent to

\[
T_O\le\sum_i a_it_i,
\qquad R_O\le\Phi_X(T_O).
\]

Ordering by `theta_i=r_i/t_i` gives the exact fractional-knapsack Lorenz curve.
Equivalently,

\[
\boxed{
\Phi_X(T)=\min_{\lambda\in\mathbb R}
\left[\lambda T+\sum_i a_i(r_i-\lambda t_i)_+\right].}
\]

An optimizing `lambda` is an exact separator when the coupling is infeasible.
This is the correct finite theorem behind `CPSL67`.  It is target-plus-scalar
only.  Additional row, score, port or barycenter coordinates require a
multi-resource LP and are not implied by this scalar reduction.

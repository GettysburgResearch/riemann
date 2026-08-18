# L-97611 — Completed-parity scalar common-source feasibility has an exact finite Lorenz dual

Status: **PROVED EXACT FINITE-DIMENSIONAL THEOREM**
Uniform frontier: open.

At one fixed, fully expanded endpoint, let even atom `i` have capacity `a_i>=0`, target `t_i>0`, and scalar `r_i`. Let odd demands be `(T_O,R_O)`. Define

\[
\Phi_X(T)=\max\left\{\sum_i r_i u_i:
0\le u_i\le a_i,\ \sum_i t_i u_i=T\right\}.
\]

Then scalar common-source feasibility is equivalent to

\[
T_O\le T_E:=\sum_i a_it_i,
\qquad
R_O\le\Phi_X(T_O).
\]

Ordering by decreasing `theta_i=r_i/t_i` gives the fractional-knapsack Lorenz formula. Equivalently,

\[
\Phi_X(T)=\min_{\lambda\in\mathbb R}
\left[\lambda T+\sum_i a_i(r_i-\lambda t_i)_+\right].
\]

A minimizing `lambda` is an exact finite separator when feasibility fails.

The uniform assertion for every real endpoint and both one-sided activation limits is `CPSL67`. It remains open and RH-bearing.

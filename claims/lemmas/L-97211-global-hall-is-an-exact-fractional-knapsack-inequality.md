# L-97211 — Global two-coordinate Hall is an exact fractional-knapsack inequality

Claim ID: `L-97211`  
Status: **UNCONDITIONAL FINITE OPTIMIZATION THEOREM; ARITHMETIC INEQUALITY OPEN**  
Created: 2026-08-17

Let the available even atoms have capacities \(a_i\ge0\), target coordinates
\(t_i>0\), and scalar coordinates \(r_i\ge0\). Let the complete odd packet have

\[
T_O=\sum_o b_ot_o,
\qquad
R_O=\sum_o b_or_o.
\]

Define

\[
\mathcal L_E(T)=
\max\left\{
\sum_i u_ir_i:
0\le u_i\le a_i,\ 
\sum_i u_it_i=T
\right\}.
\]

Order the even atoms by decreasing ratio

\[
\frac{r_1}{t_1}\ge\frac{r_2}{t_2}\ge\cdots.
\]

Then the maximum is obtained by taking complete atoms in that order and, if
necessary, a fraction of the first atom crossing target mass \(T\). This is the
fractional-knapsack exchange theorem.

Consequently, the one-scalar global Hall problem at a fixed endpoint is
equivalent to

\[
\boxed{
T_O\le\sum_i a_it_i
\quad\text{and}\quad
\mathcal L_E(T_O)\ge R_O.
}
\]

When these inequalities hold, the greedy coefficients give one common source
vector satisfying exact target equality and scalar domination. If either fails,
no coefficient vector in the box can work.

This theorem makes the missing arrow explicit. The repository has an exact
finite primal-dual alternative, but it does not prove the displayed arithmetic
inequality uniformly in \(X\). That uniform statement is `GPHT*`.

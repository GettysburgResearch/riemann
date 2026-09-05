## Checkpoint 17 - optimal Cartan radius allocation

T-105116 solves the finite radius-versus-reciprocal-loss tradeoff exactly.
For declared positive penalty weights (u_j), radius costs (v_j), and a
closed budget, the unique optimizer is capped water filling:

\[
\varepsilon_j^*=\min\left(1,\frac{u_j}{\lambda v_j}\right).
\]

For the unweighted T-105114 sum with a common middle radius, the growth
loads cancel from (u_j/v_j), so the optimal epsilons are equal rather than
inverse in the growth loads.  Choosing

\[
R_\delta=\frac{1-\delta}{2}\min(\Delta_T,\Delta_\eta)
\]

on a closed budget gives the strict T-105115 gate and
(\kappa\le\delta^{-2}).  An active strict open budget has only an infimum,
not a minimizer.

Proof digest:
`62faec5d43fb845ba3e27fdd7c41167a33fba0c6724298e496fecc9c0482f92e`.
Focused replay: 16/16 normally and 16/16 under `-O`.

The objective weights, Xi growth/manifests, optimized cost absorption,
signed moment closure, RCMV104530, and RH remain open.

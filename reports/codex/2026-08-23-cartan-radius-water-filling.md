# Cartan radius water filling

Status: **EXACT FINITE OPTIMIZATION; XI ABSORPTION OPEN**

Checkpoint base: `ccc2244b65a2e75a60b5f46fecba35ad016ce4fe`.

Proof digest:
`62faec5d43fb845ba3e27fdd7c41167a33fba0c6724298e496fecc9c0482f92e`.

## Advance

T-105114 exposes a tunable equal-disk radius and a logarithmic reciprocal
penalty.  T-105115 shows why the total nominal radius must leave strict
shell slack.  T-105116 now solves the resulting finite convex allocation
problem instead of choosing every epsilon heuristically.

For positive penalty weights (u_j) and radius costs (v_j), the capped
KKT solution allocates nominal radius proportionally to (u_j) until an
epsilon reaches one.  In the interior regime,

\[
\varepsilon_j^*=\frac{u_jR}{v_j\sum_\ell u_\ell},
\qquad
\Phi^*=\sum_j u_j\log
\left(\frac{2v_j\sum_\ell u_\ell}{u_jR}\right).
\]

For (u_j=A_j/\beta_j), (v_j=r_{2,j}A_j/\beta_j), common (r_2)
forces equal optimal epsilons.  An inverse-growth rule optimizes the wrong
objective.

With (d=\min(\Delta_T,\Delta_\eta)) and
(R=(1-\delta)d/2), the closed budget attains its optimizer while the
actual disks still obey (2S<d).  The T-105115 normalization satisfies
(\kappa\le\delta^{-2}).  This identifies an exact Pareto barrier: small
slack improves reciprocal bounds but worsens safe-set normalization.

The barrier is only for the declared equal-disk, nominal-radius,
scalarized-log ledger.  Exact projection overlap, non-equal covers, and
authenticated cancellations can improve it.  The checkpoint does not
authenticate Xi inputs or prove the optimized loss absorbable.

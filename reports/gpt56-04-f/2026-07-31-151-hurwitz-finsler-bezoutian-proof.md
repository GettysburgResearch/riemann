# Agent report — completed Hurwitz/Finsler/Bézoutian implication

Agent: `gpt56-04-f`  
Issue: #151  
Branch: `agent/gpt56-04-f/151-finsler-target-completion`  
Date: 2026-07-31

## Result

The conditional implication requested by the user is now proved in full detail
in the revised `T-15104`.

Two hidden points were repaired.

1. **Only strip convergence is needed.** Local-uniform convergence on
   `|Im z|<1/2` suffices, because every nontrivial zeta zero maps into that open
   strip under `z=(rho-1/2)/i`. Convergence on all of `C` is stronger than
   necessary and was not the natural output of the Hardy-tail estimates.
2. **Boundary normalization must be separated from convergence normalization.**
   If `delta_j=eta_j^T tilde(p_j)`, the scalar-completion formula uses
   `p_j=tilde(p_j)/delta_j`, while Hurwitz is applied to the original transforms
   `hat(tilde(p_j))`. Their zero sets are identical, so no convergence claim is
   lost by the finite normalization.

## Finite-to-global proof

For every sufficiently large level, the target-pinned completion

```text
T_j(c)=A_j+c B_j
```

is assumed positive semidefinite with one-dimensional even kernel `R p_j`.
The scalar update preserves the exact Connes--van Suijlekom special
 divided-difference form. Their finite theorem therefore makes every zero of
`hat(p_j)` real.

The original transforms are nonzero scalar multiples of these finite
transforms, hence are also real-rooted. On each connected open half-strip

```text
0 < Im z < 1/2,
-1/2 < Im z < 0,
```

they are zero-free. Hurwitz implies that the locally uniform limit `Xi` is
zero-free there, since `Xi` is not identically zero. A nontrivial zeta zero
`rho=beta+i gamma` corresponds to

```text
z_rho = gamma - i(beta-1/2).
```

Thus `Xi(z_rho)=0` forces `beta=1/2`, proving RH under the stated hypotheses.

## Complete finite equivalence

Because

```text
A_j p_j = B_j p_j = 0,
```

the completion has kernel exactly `R p_j` and is PSD iff its restriction to
`p_j^perp` is positive definite. The restricted slope is nonsingular. Strict
Finsler/Dines separation proves

```text
exists c: A_j+c B_j > 0 on p_j^perp
```

iff

```text
x^T A_j x > 0
for every nonzero x perp p_j with x^T B_j x = 0.
```

The feasible scalar set is the open interval

```text
sup_(b>0)(-a/b) < c < inf_(b<0)(-a/b),
```

so any successful real interval contains a rational certificate scalar.

## Simple-root form

When the finite target interpolation polynomial `P_j` has simple real roots
`r_(j,k)`, the target-pinned matrix is congruent, with a fixed minus sign, to
the Bézoutian of `P_j` and the completed source polynomial `R_(j,c)`. Root
evaluation diagonalizes the nonzero Bézoutian form into

```text
P_j'(r_(j,k)) R_(j,c)(r_(j,k)).
```

Writing

```text
c_(j,k) = R_(j,0)(r_(j,k))/Omega_j(r_(j,k)),
sigma_(j,k) = P_j'(r_(j,k)) Omega_j(r_(j,k)),
```

the complete finite condition is exactly

```text
max_(sigma>0) c_(j,k) < min_(sigma<0) c_(j,k).
```

Repeated roots require a confluent criterion and are excluded from this scalar
root formula.

## Status

The implication is proved under its explicit hypotheses. The Riemann Hypothesis
itself is not claimed, because the repository has not yet proved either:

- the required production target convergence; or
- the cofinal Finsler/root-threshold separation.
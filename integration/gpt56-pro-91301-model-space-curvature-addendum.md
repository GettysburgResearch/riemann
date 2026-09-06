# Addendum — canonical Suzuki model-space tangent reserve

## Live relation

This addendum is normative after
`integration/gpt56-pro-91034-corrected-fock-hardy-tangent-handoff.md`.

A concurrent branch addition deposited

```text
claims/lemmas/L-91301-suzuki-model-space-shape-operator-is-the-canonical-first-chaos-reserve.md
```

It sharpens the output side of `T-91008` without closing the RH-bearing
domination.

## Exact abstract theorem

For a twice differentiable inner family `Theta_tau`, let

```text
M_tau = multiplication by Theta_tau on H^2,
P_tau = I-M_tau M_tau* = projection onto K_(Theta_tau).
```

The off-diagonal shape operator is

```text
B_tau=(I-P_tau) dot(P_tau) P_tau.
```

Projection calculus gives exactly

```text
-P_tau ddot(P_tau) P_tau
 =2 B_tau* B_tau
 =J_tau* J_tau >=0,

J_tau=sqrt(2) dot(M_tau)* P_tau.
```

For logarithmic scale `tau=log a`, the connection term disappears after
sandwiching by `P_a`, so the same positive square holds with the natural radial
normalization.

Applied to Suzuki's safe inner family, this identifies the mandatory output
tangent channel canonically:

```text
J_a=sqrt(2) M_(a partial_a Theta_a)* P_a.
```

Any conservative completion using the same amplitude model space contains this
channel up to an output isometry.

## Correct remaining domination

Let `C_a^src` be the complete positive first-chaos source curvature assembled
from:

```text
normalized Jordan source of L-91037;
explicit gamma tangent;
explicit pole/boundary finite channel.
```

The sharp remaining theorem is

```text
C_a^src >= J_a*J_a
```

on the corrected delayed form core, with defect equal to the complete delayed
screw Gram.

This is a comparison of two explicit first-chaos operators:

```text
source first-chaos metric
versus
mandatory model-space tangent leakage.
```

It is not supplied by abstract projection geometry; `J_a*J_a>=0` alone gives no
upper bound by the source curvature.  The domination is RH-bearing.

## Relation to corrections

- `R-91008` still refutes the scalar form core.
- `L-91034` supplies the proposed delayed density repair.
- `R-91010` still refutes replacing the full matrix by a scalar commutator.
- `L-91301` gives a canonical output feature, but not the required source
  domination.
- `T-91008` remains the normative full-Gram endpoint.

## Highest-priority review

1. Verify strong differentiability and domains of the multiplier/projection
   family on the declared core.
2. Verify the sign and factor two in
   `-P ddot(P)P=2B*B`.
3. Verify the logarithmic-radius connection term vanishes after projection.
4. Derive the kernel of `J_a*J_a` explicitly on delayed carrier vectors.
5. Compare it, without diagonalization or an assumed target square root, with
   the source Gram of `L-91037` plus gamma/pole channels.

## Exact boundary

```text
model-space shape operator                 EXACT ABSTRACT
projection-curvature positive square       EXACT ABSTRACT
canonical Hardy first-chaos reserve        PROPOSED COMPLETE FOR SUZUKI FAMILY
source curvature >= tangent leakage        OPEN / RH-EQUIVALENT
complete delayed screw Gram                OPEN
Riemann Hypothesis                         UNPROVED
```

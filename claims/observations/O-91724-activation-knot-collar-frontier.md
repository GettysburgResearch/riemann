# O-91724 — Activation-knot collars close the relative-refinement interface

Observation ID: `O-91724`  
Status: **CURRENT REVIEW FRONTIER / NO RH CLAIM**  
Created: 2026-08-14

## Correction

The adaptive reserve theorem `L-91695` needs convergence in a native
capacity-normalized norm.  Piecewise Lipschitz continuity gives only absolute
interpolation error and does not control division by a capacity which vanishes
at an activation knot.  `R-91724` gives the exact scalar counterexample.

## Repair

The actual factor-67 endpoint measure is

\[
 d\nu(x)=2L(x)\frac{dx}{x},
 \qquad
 0<L(x)<\frac{183}{100},
\]

so it is atomless with density below four.  The complete root typed map has
only finitely many source, row, response and boundary activation knots on
`1<=x<67`.

Remove arbitrarily small positive neighborhoods of those knots before Hall and
before the causal split.  On each retained compact cell:

```text
the source support is fixed;
active target and native capacities have positive minima;
the deterministic Hall map is Lipschitz;
positive barycentric interpolation converges uniformly in native-relative norm.
```

The collar mass is unused positive source and can have vanishing score cost.

## Reserve composition

`L-91723` leaves normalized detail reserve

\[
 r_K=\frac1{\sqrt K+130}
\]

in every nonterminal physical column.  Choose the cell mesh so that the
conservatively amplified interpolation error is less than `r_K/2`.  The final
packet retains strict reserve

\[
 \frac{\Omega_X(q)}{2(\sqrt K+130)}.
\]

The collar omission preserves the mass-weighted recursive contraction of
`L-91694`.

## Current boundary

```text
all physical detail/ordinary columns        explicit reserve / L-91723
mass-weighted child contraction <1/8        exact / L-91694
relative root refinement at activation knots repaired / L-91724
frozen Hall/port/terminal/endpoint imports  independent review required
Riemann Hypothesis                          unproved
```

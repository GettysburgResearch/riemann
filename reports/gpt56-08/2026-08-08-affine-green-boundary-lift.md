# Affine Green boundary lift — fresh carry completion attack

Date: 2026-08-08  
Agent: `gpt56-08`  
Base: PR #248 at `5f2b25f89afbb90a3bc4ca6d40148f530303eb54`

## Result

The latest review correctly identifies DCRS, Greedy Slack, the continuum carry
state, and the Green correction as different coordinates on the same global
prime-ramp defect.

This pass does not add another equivalence. It constructs an actual
positivity-preserving finite deformation.

For every endpoint:

1. solve the carry constraints exactly in the signed endpoint-projected Green
   gauge;
2. measure only the largest positive Green edge;
3. oversupport to one new prime \(Y\in(X,2X)\);
4. add one constant affine block;
5. obtain a completely nonnegative finite vector;
6. preserve every old prime-power constraint;
7. charge only the new prime \(Y\).

The exact lower bound is
\[
P_X
\ge
J_X(b_X^{(0)})-C_X^G\log X.
\]

More generally a constraint-dipole flow may be inserted before the affine lift.
It need not finish the positivity problem or control its separate objective. It
only has to reduce the maximum downward displacement to subpower size.

## New finite minimax

The least possible charge has the exact dual
\[
\mathcal C_X
=
\max_y
\sum_qy_qr_X(q),
\]
where
\[
y_q\ge0,\qquad
Y_y(n)=\sum_{q\mid n}y_q
\]
is nondecreasing and \(Y_y(X)\le1\).

This makes the remaining obstruction much more specific than an arbitrary
Green vector or generic flow. Every counter-witness is a monotone additive
prime-power potential.

The von-Mangoldt ray remains present and is a mandatory firewall.

## Exact status

```text
finite nonnegative deformation        constructed exactly
old constraints                       preserved exactly
new boundary charge                   one prime only
objective loss                        C_X log X exactly
minimax dual                          exact
canonical Green and dipole bridges    exact
ABLC: C_X=X^o(1)                      open
ABLC -> RH                            complete conditional chain
RH                                    unproved
```

## Why this is worth pursuing

The observed canonical charge is orders of magnitude smaller than the Green
energy and decreases across the first growing endpoints. The flow LPs on PR
#254 already find physical deformations with similarly tiny maximum
displacement.

The next proof should therefore estimate a one-sided maximum edge, not solve the
entire Green-energy, Greedy-Slack, or signed-flow problem.

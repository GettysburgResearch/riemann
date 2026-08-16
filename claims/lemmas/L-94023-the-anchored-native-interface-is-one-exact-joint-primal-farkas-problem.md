# L-94023 — The anchored native interface is one exact joint primal/Farkas problem

Claim ID: `L-94023`
Status: **PROVED EXACT FINITE REDUCTION; FEASIBILITY OPEN**
Created: 2026-08-16
Depends on: `R-94020`, `L-94020`, `L-94022`; abstract vector transport `L-91720`
RH status: **unproved**

For fixed integer `X`, let `Omega_X^anc` be the finite set of actual anchored
source occurrences from `L-94020.5`, with complete owner and stopped-tree
labels.  Let `V_X` be the finite typed coordinate space containing

```text
input-source incidence for every occurrence;
target and declared score;
every component row;
ordinary responses at every q and every 4q;
boundary and terminal coordinates;
one owner coordinate per source occurrence.
```

Radix-four detail is deliberately absent from the independent coordinate list:
it is formed after the common ordinary sum.

## 1. Allowed joint templates

A template may combine finite-forcing and oriented-child occurrences before
physical observation.  It may include a complete Target–Lorenz causal block
with its literal `beta_i` weight, a positive residual source, and a current-only
row bonus.  It may not expose the oriented child marginal as a separate
nonnegative physical row.

Let the columns of `A_X` be all declared allowed templates, written in the same
coordinate order in `V_X`; let `b_X` be the exact live native marginal from
`L-94020`.  The complete producer problem is

\[
 \boxed{
 A_X z=b_X,
 \qquad
 G_Xz\ge0,
 \qquad
 z\ge0.
 }
\tag{L-94023.1}
\]

The same scalar `z_r` multiplies source, target, score, every row, every
ordinary coordinate and every owner coordinate of template `r`.

## 2. Physical conditions

The inequalities `G_Xz>=0` include

```text
coefficientwise nonnegativity of the single total row;
no source-owner overdraw;
ordinary capacity at q and at 4q on that same row;
all-column boundary/terminal reserve;
zero exported recursive family;
zero auxiliary port unless a Schur mechanism is explicitly invoked.
```

After summing ordinary coordinates, define

\[
 \Xi(q)=\Gamma(q)-2\Gamma(4q).
\tag{L-94023.2}
\]

No second coupling is permitted at the detail stage.

## 3. Exact alternative

The matrix entries are finite symbolic expressions in rational numbers,
square roots and logarithms.  A primal certificate must preserve its equality
rows by symbolic primitive identities; a strict dual separation may be
validated by outward primitive enclosures.  The finite-dimensional real Farkas
alternative is:

- either a nonnegative joint coefficient vector `z` satisfying (L-94023.1);
- or a dual vector `(u,v)` with
  \[
  A_X^Tu+G_X^Tv\ge0,
  \qquad v\ge0,
  \qquad b_X^Tu<0,
  \]
  which is an exact obstruction to the declared template cone.

`R-94020.7` is the one-column dual separator for every cone that insists on
branchwise positive actual children.

This theorem instantiates review #504's live marginal as a fail-closed finite
problem.  It does not assert that the present repository template list is
complete or that (L-94023.1) is feasible for all `X`.  That joint feasibility
is the remaining native producer.

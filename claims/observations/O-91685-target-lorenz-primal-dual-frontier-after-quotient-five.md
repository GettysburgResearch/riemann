# O-91685 — Target-Lorenz primal/dual frontier after the quotient-five closure

Observation ID: `O-91685`  
Created: 2026-08-14  
Frozen parent: PR #468 at `a41f81466f85d52597c97b41505756a8860698d0`  
RH status: **unproved**

## Durable conclusions

```text
Target-Lorenz is one common source in all ledgers       EXACT / L-91685
Target-Lorenz is simultaneously optimal for all rows   EXACT / L-91685
failure of one row is a complete common-source failure EXACT / L-91685
failed row gives an explicit cutoff Farkas separator   EXACT / L-91685
one full target determinant per row is sufficient      EXACT / L-91685
all quotient cells py/j<5                              CLOSED / L-91686
```

The leftmost producer is therefore no longer an ansatz that might need to be
replaced by a higher-dimensional source search. Under the common profile order
of `L-91682`, it is the exact vector primal. A failed margin cannot be repaired
by choosing different coefficients on the same even source atoms.

## Exact remaining arithmetic theorem

For

\[
 py\ge5j,
 \qquad p\ge67,
 \qquad1\le y<67,
 \qquad2\le j\le66,
\]

prove

\[
 \mathfrak L_j(p,y)\ge0.
\]

Two fail-closed proof forms are now equivalent:

1. certify the Target-Lorenz primal margin;
2. rule out every support-function separator of `L-91685.11`.

A stronger sufficient target is the cutoff-free full determinant

\[
 O_TE_R^{(j)}-E_TO_R^{(j)}\ge0.
\]

The deterministic floating reconnaissance in `X-91685` found no negative
margin in `129,675` row tests. Its smallest remaining sampled margin after the
exact quotient-five region is about `0.00670`. This is discovery evidence only.

## Composition boundary

Once the remaining row family is certified, the same `U` gives exact target,
zero score debt, every component-row bonus, and hence ordinary/detail bonuses
through the positive response maps. A separate native-root crosswalk must
still charge the rough reservoir, collars, omissions and shared endpoint port
exactly once.

```text
common stopped-leaf source producer       ONE ARITHMETIC ROW FAMILY REMAINS
native one-use root composition            SEPARATE CROSSWALK REQUIRED
Riemann Hypothesis                         UNPROVEN
```

# R-91710 — Positive dyadic source and model telescopes do not identify generations

Refutation ID: `R-91710`  
Status: **EXACT GENERATION-PROVENANCE FIREWALL**  
Created: 2026-08-13  
Depends on: `L-91710/L-91711`, `L-91520/L-91620`  
RH status: **unproved**

## 1. The tempting inference

Both sides now have additive nonnegative dyadic ledgers:

```text
arithmetic:  A_J=sum_(j<=J) I_j,   I_j>=0;
model:       M_J=sum_(j<=J)(C_j+S_j+H_j), H_j>=0.
```

It is tempting to identify the totals and conclude `H_j=0`. This is invalid.

## 2. Finite countermodel

Take two source innovations

\[
I_1=I_2=1.
\]

Let one model decomposition be

\[
(C_1,S_1,H_1)=(1,0,0),\qquad
(C_2,S_2,H_2)=(1,0,0),
\]

and another be

\[
(C_1,S_1,H_1)=(1-\varepsilon,0,\varepsilon),\qquad
(C_2,S_2,H_2)=(1,0,0)
\]

for any `0<epsilon<1`. Both have the same total source and model telescopes,
but the second has a nonzero hyperbolic generation.

The same construction works with positive matrices by replacing the scalars
with multiples of one rank-one projection.

## 3. What is required

A conclusion-producing theorem must supply a cocycle-compatible map

\[
\mathfrak h_j^{\rm arith}
\longrightarrow
\mathcal K_j^{\rm crit}
\oplus
\mathcal K_j^{\rm st}
\oplus
\mathcal K_j^{\rm hyp}
\oplus
\mathcal E_j
\]

for each generation before taking norms or logarithms. Equality of total
entropy, total determinants, or total scalar values does not determine model
provenance.

## 4. Exact boundary

```text
positive arithmetic telescope                    EXACT
positive annular model telescope                 EXACT
equality of totals -> termwise hyperbolic zero   FALSE
cocycle-compatible generation map                REQUIRED
```

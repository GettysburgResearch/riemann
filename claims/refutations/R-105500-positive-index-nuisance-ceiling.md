# R-105500 — The positive-index nuisance ledger cannot reach ninety percent

Claim ID: `R-105500`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-24  
Depends on: `T-105310`, `L-105311`

The multiplicity-robust positive-index route of `T-105310` gives

\[
\frac{N_0}{N}
\ge 2\eta-1-\frac{821}{5000},
\qquad 0\le\eta\le1.
\]

Even a perfect compression, `eta=1`, therefore yields at most

\[
1-\frac{821}{5000}
=\frac{4179}{5000}
=0.8358.
\]

Equivalently, a ninety-percent conclusion would require

\[
\eta\ge\frac{51605}{50000}=1.0321,
\]

which is impossible.  Better trace/HS constants alone cannot repair this
route.

`L-105500` changes the finite invariant rather than optimizing inside the
failed ledger: it uses the **full signature**, for which nonreal conjugate
blocks and even confluent blocks cancel exactly, while odd confluent blocks
are priced by their literal Cauchy-index orientation.  The replacement
inequality is `N_0/N >= 2 eta-1` up to vanishing endpoint/count errors.

This refutation does not prove the Xi trace/HS estimate or a ninety-percent
zero theorem.

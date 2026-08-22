# R-105200 — Pointwise `o(1)` coherence is insufficient for an infinite descent

Claim ID: `R-105200`
Status: **PROVED EXACT COUNTERMODEL**
Created: 2026-08-23
RH status: **not assumed**

Suppose a derivative level has two normalized residues

\[
x_{m,\pm}=1\pm\epsilon_m.
\]

Then its exact coherence is

\[
C_m={1\over1+\epsilon_m^2},
\qquad
2C_m-1={1-\epsilon_m^2\over1+\epsilon_m^2}.
\tag{R-105200.1}
\]

Take the rational sequence

\[
\epsilon_m={1\over\lfloor\sqrt m\rfloor}
\qquad(m\ge4).
\]

Then `epsilon_m->0`, but on the block `k^2<=m<(k+1)^2`,

\[
\epsilon_m^2={1\over k^2}
\]

for `2k+1` consecutive values. Hence

\[
\sum_m(1-C_m)=\infty,
\]

and

\[
\prod_m(2C_m-1)=0.
\]

Thus a statement of the form `C_m=1-o(1)` is not sufficient to pass through
an infinite derivative ladder. The `O_T(m^-2)` coherence loss of `L-105201`
is a genuinely stronger, load-bearing theorem.

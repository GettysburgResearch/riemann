# L-91632 — Natural parent-to-child quarter cascade has a uniform negative score moat

> **CORRECTION.** The scalar theorem remains valid. `R-91633` proves that its five `P` terms cannot be represented independently by one row under the single target `w_(256x)`. `L-91634` gives the correct one-row theorem.

Claim ID: `L-91632`  
Status: **DIRECTED-EXACT SCALAR THEOREM; PHYSICAL INTERPRETATION SUPERSEDED BY `R-91633/L-91634`**  
Created: 2026-08-14  
RH status: **unproved**

Let `D(x)=Sigma(x)-P(x)` be the arithmetic score defect of `L-91631`. Define

\[
C_4D(x)=\sum_{j=0}^{4}2^{j-4}D(4^jx)
=D(256x)+\frac12D(64x)+\frac14D(16x)+\frac18D(4x)+\frac1{16}D(x).
\]

Then

\[
\boxed{C_4D(x)<-50.7132792280415\qquad(1\le x\le67).}
\]

`X-91632` certifies this with exact outward interval arithmetic:

```text
PASS_NATURAL_REVERSED_QUARTER_CASCADE_K4_ENDPOINT_CERTIFICATE
checks: 50689
common cells: 16896
cells with nonnegative logarithmic coefficient: 0
largest upper endpoint: -50.713279228041585611
```

On every common cell of `4^-4 Z`, the cascade is `alpha sqrt(x)+beta log(x)+gamma` with `beta<0`; every interior critical point is a minimum, so both one-sided endpoints suffice. Activated knots are checked separately.

The coefficients `2^(j-4)` are valid in the declared score ledger. They are not five physical row coefficients. `R-91633` proves

\[
G_n=\sum_q\Lambda(q)\beta_{nq},
\]

and therefore every row with ordinary response at most `w_(256x)` has entropy at most `P(256x)`. A termwise interpretation would require

\[
P(256x)+\frac12P(64x)+\frac14P(16x)+\frac18P(4x)+\frac1{16}P(x)>P(256x),
\]

so it is impossible.

`L-91634` counts the exact positive parent row once. It decomposes coefficientwise into four nonnegative factor-four differences and one terminal child, retains the single ordinary and radix-four responses, and has entropy `P(256x)`. Its exact replay proves

\[
\sum_{j=0}^{4}2^{j-4}\Sigma(4^jx)-P(256x)
<-40.905782490079282354
\]

for `1<=x<=67`.

```text
scalar five-level D inequality                       PROVED
termwise five-P physical interpretation              IMPOSSIBLE / R-91633
correct one-row score inequality                     PROVED / L-91634
four-current-plus-terminal row identity              EXACT ON FROZEN INPUT
live replay and independent reconstruction           REQUIRED
Riemann Hypothesis                                    UNPROVEN
```

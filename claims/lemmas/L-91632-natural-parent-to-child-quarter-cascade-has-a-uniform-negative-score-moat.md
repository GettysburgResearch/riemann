# L-91632 — Natural parent-to-child quarter cascade has a uniform negative score moat

Claim ID: `L-91632`  
Status: **DIRECTED-EXACT SCALAR THEOREM; PHYSICAL ONE-USE GLUING OPEN**  
Created: 2026-08-14  
RH status: **unproved**

Let `D(x)=Sigma(x)-P(x)` be the arithmetic score defect defined in `L-91631`. Four successive factor-four affine lifts carry a row from endpoint `4^j x` to endpoint `256x` with coefficient `2^(j-4)`. Define

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

On every common cell of `4^-4 Z`, the cascade is `alpha sqrt(x)+beta log(x)+gamma` with `beta<0`; every interior critical point is therefore a minimum, so the two one-sided endpoints suffice. Activated knots are checked separately.

The coefficients are exactly those of the critical affine lifts. The remaining interface is physical rather than scalar: construct one positive finite parent packet equal to the four current factor-four detail rows plus the terminal child row, without using an ordinary or radix-four target column twice. The geometric delay reservoir, positive endpoint details, and affine score amplification are resident inputs, but their one-use finite-row gluing still requires proof.

```text
natural five-level scalar sign                  PROVED
uniform negative moat                           DIRECTED EXACT
critical affine coefficients                    EXACT
one-use positive physical cascade               OPEN
native factor-54 loss recurrence                NOT YET CLOSED
Riemann Hypothesis                              UNPROVEN
```

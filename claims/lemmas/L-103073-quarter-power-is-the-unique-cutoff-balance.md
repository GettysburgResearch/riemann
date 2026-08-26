# L-103073 — Quarter power is the unique fixed-owner cutoff balance

Claim ID: `L-103073`  
Status: **PROVED EXACT FIXED-FIBRE EXPONENT LEDGER**  
Created: 2026-08-26  
Corrected: 2026-08-26  
Depends on: `L-103110--L-103111`; binding `R-103110`  
RH status: **not assumed**

Write the fixed-owner core horizon as `W` and choose a power cutoff

\[
U=W^\alpha
\]

up to fixed dyadic constants.

The fixed-owner squarefree Type-I theorem gives

\[
\boxed{
\mathcal T_U^{\rm fixed\ owner}
=
W^{\alpha-1/4+o(1)}.
}
\tag{L-103073.1}
\]

Every balanced core contains two disjoint factors larger than `U`, and hence

\[
a^2>U^4=W^{4\alpha}.
\tag{L-103073.2}
\]

The compact physical observation in that owner fibre permits only `a^2<=W`.
Consequently:

```text
alpha < 1/4:
  fixed-owner Type I is power-saving, but the balanced row can remain;

alpha = 1/4:
  fixed-owner Type I is subpower and the balanced row is support-empty;

alpha > 1/4:
  the balanced row is support-empty, but the fixed-owner Type-I estimate
  incurs a positive power.
```

Thus `alpha=1/4` is the unique exponent where the two **fixed-owner** demands
meet.

## Scope

This ledger does not control the coherent physical collapse across different
owner products. At the endpoint that collapsed Type-I field is exactly the
open harmonic/BCI current by `L-103112`. No RH conclusion is drawn.
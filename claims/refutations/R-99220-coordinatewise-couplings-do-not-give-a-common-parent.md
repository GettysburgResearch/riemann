# R-99220 — Separate coordinatewise couplings do not produce one physical parent

Claim ID: `R-99220`  
Status: **PROVED EXACT FINITE FIREWALL**  
Created: 2026-08-19  
RH status: **unproved**

Let two typed child atoms have feature vectors

\[
a=(m,R_1,R_2,S)=(1,1,0,1),
\qquad
b=(1,0,1,0).
\]

Coordinatewise, one may obtain

```text
target mass 1 from a;
first response 1 from a;
second response 1 from b;
score 1 from a.
```

But no single nonnegative measure `alpha delta_a+beta delta_b` has all four
marginals. The first and second response requirements force
`alpha=beta=1`, while target mass would then be `alpha+beta=2`, not `1`.

Therefore separately preserving root row, target, score, ordinary response,
radix-four response, or child masses does not imply a common source-owned
realization. The same positive typed child kernel must transport every physical
coordinate before labels are forgotten.

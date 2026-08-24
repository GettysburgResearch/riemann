# M-105510 — Hostile review contract for triangular Wick transfer

Claim ID: `M-105510`  
Status: **FAIL-CLOSED REVIEW SPECIFICATION**

A reviewer must check:

1. `P_2(x)` is used as a unit only when the nonconstant source operator is
   nilpotent; pointwise zero-freeness is not asserted.
2. `P_2^2/(1-x)=1+x^3/8+(9/64) sum_(m>=4)x^m` is verified exactly.
3. The source coordinate change is genuinely invertible before invoking
   congruence/inertia preservation.
4. The projection from source translations to the smooth Paley--Wiener frame
   is not treated as exact unless `TRIEDGE105510` is proved.
5. The rational energy bound is `1669/11698176<1/7000`, the two-sided factor is
   `3501/3500`, and the conditional output is
   `3654811/3968189`.
6. Replay flags for `TRIWXFER105510`, ninety percent, the public record, and RH
   remain false.

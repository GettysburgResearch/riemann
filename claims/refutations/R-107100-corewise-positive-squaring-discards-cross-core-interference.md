# R-107100 — Corewise positive squaring is strictly stronger than assembled interference

**Claim ID:** `R-107100`  
**Status:** proved exact separator

The annular theorem retains a signed sum `sum_d d^{-1}Z_d`. A `COREAGG`-type
sufficient gate replaces it by a positive sum of `|Z_d|^2`. For two equal
outer weights choose `Z_{d_1}=M` and `Z_{d_2}=-M`. The assembled scalar is zero
while the positive energy is `2M^2`. The separation is unbounded.

This is not an arithmetic counterexample to `COREAGG_0`; it remains a valid
sufficient gate. It is a binding design firewall: taking corewise absolute
values before exploiting the exact annular interference may destroy the only
new leverage.

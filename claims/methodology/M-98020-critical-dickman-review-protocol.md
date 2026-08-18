# M-98020 — Hostile protocol for the quantitative Dickman corridor

Methodology ID: `M-98020`  
Status: **FAIL-CLOSED REVIEW PROTOCOL**

A reviewer should reconstruct the following interfaces in order.

1. **Atomic measure.** Confirm the prime coordinate is `log p/log z` and the
   weight is exactly `1/p`; no unrestricted integer measure may be substituted.
2. **Distinctness.** Confirm the repeated-prime correction in `L-98020`; the
   continuous product integral initially counts repeated atomic coordinates.
3. **Activation.** Confirm `product p_i<=Y` is exactly the additive simplex
   `sum log p_i/log z<=u`.
4. **Source error.** Confirm the zero-extended `P_61` base has one globally
   bounded remainder `e(Y)=b(Y)-a_*sqrt(Y)`.
5. **Rough sieve.** Verify the imported dimension-one upper-bound sieve before
   claiming `sum m^(-1/2)<<sqrt(Y)/log z`.
6. **Uniformity.** The positivity theorem is uniform only in the stated
   near-critical range. A fixed-`theta` proof does not suffice.
7. **No promotion.** The finite replay verifies algebra and diagnostics. It does
   not prove `CBRC67`, `GPC67`, or RH.

Mandatory negative controls:

```text
do not erase the bounded remainder;
do not replace mu(m) by absolute values inside CBRC67;
do not call fixed-power Dickman asymptotics uniform in all u;
do not claim the critical c>1 corridor is negative;
do not infer target-preserving Hall from scalar positivity;
do not claim RH by finite computation.
```

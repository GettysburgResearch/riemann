# R-91671 — Separate capacity bounds do not imply a combined native root ledger

Claim ID: `R-91671`  
Status: **PROVED EXACT NORMALIZATION / OVERDRAW FIREWALL**  
Created: 2026-08-14  
Depends on: independent review PR #450; proposed `L-91659` on PR #447  
RH status: **unproved**

Let `W` be one positive native capacity vector and let the Hall, outer, collar, mismatch, omission, and port demands be positive. Separate statements `D^c <= W` do not imply `sum_c D^c <= W`. The failure already occurs in one scalar coordinate:

\[
W=1,\qquad D^{\rm Hall}=3/5,\qquad D^{\rm outer}=3/5,
\]

where both demands are separately feasible but their sum is `6/5>1`.

Likewise, after removing a recursive datum `R` from a parent datum `N`, defining `C=N-R` is only an ambient vector identity. It proves neither `C>=0` nor that the combined current row is feasible in `C`.

Summing before quantization can prevent fractional-column artifacts but does not repair source overdraw. Therefore one-use quantization is not the same theorem as one-use source/capacity provenance.

Any proposed root certificate is refuted by one exact witness of: atomwise source consumption above its weight; combined ordinary/radix-four demand above residual capacity; failed exact component-row/score identity; more than one charge to the common endpoint port; or one root occurrence assigned simultaneously to incompatible current/child/stopping uses.

```text
separate producer feasibility                         USEFUL BUT INSUFFICIENT
separate bounds -> combined residual feasibility      REFUTED
sum-before-quantize -> source nonduplication           REFUTED
one common atomwise provenance partition              REQUIRED
native root current ledger                            OPEN
Riemann Hypothesis                                    UNPROVEN
```

# T-105660 — Corrected all-rank Cauchy translation frontier

**Claim ID:** `T-105660`  
**Status:** three unconditional advances; global constant-one CTI open  
**Date:** 2026-08-31  
**RH:** unproved

1. `MLC105656` is refuted exactly in rank two. Its implication remains valid,
   but it cannot be the universal proof route. `FNI105658` and CTI survive.
2. Every rank and height satisfy the sharp global near-closure
   `n-O_H <= (32/27)(n-T_H)`.
3. Constant-one CTI holds for every finite packet at first contact. A further
   all-rank physical region is closed by the trace/determinant criterion of
   L-105662.

Revised frontier:

```text
MLC105656                         REFUTED EXACT
rank-one/rank-two CTI             PROVED (prior packets)
all-rank first-contact CTI        PROVED
all-rank sharp 32/27 bound        PROVED
physical prefactor region         PROVED
FNI105658                         OPEN
constant-one CTI arbitrary scale  OPEN
base-zero/cofinal/pointwise Xi     OPEN / RH-BEARING
RH                                UNPROVEN
```

Future work should attack FNI or the trace inequality directly, not replace
MLC by another unjustified all-packet Loewner order.

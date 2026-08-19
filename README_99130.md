# T-99130 — reciprocal-Julia single-profile recovery

This collision-free recovery is based on frozen PR #611 at
`9d0b0521e5ace8c96df63a85a68f60a789b09923`.

The packet replaces the two independent future-prime row tails by one signed
reciprocal-Julia profile, one positive smooth-number reservoir, and two fixed
physical observation kernels. It does **not** claim `RJCE23`, `FPCB23`, or RH.

```text
positive dyadic inverse                    PROVED EXACT
single reciprocal-Julia profile            PROVED EXACT
positive smooth reservoir                  PROVED EXACT
two fixed row observation kernels          PROVED EXACT
primitive-scalar positive lift             PROVED EXACT
RJCE23                                      OPEN / RH-BEARING
FPCB23                                      OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVED
```

## Purpose

Continue PR #602 and replace its qualitative “subpower critical core” by a
quantitative, source-faithful critical corridor.

**RH remains unproved.**

## New unconditional theorem

For

```text
F(Y,z)=sum_(P^-(m)>=z) mu(m)m^(-1/2)b(Y/m),
u=log Y/log z,
```

this packet proves the uniform formula

```text
F(Y,z)=a_* sqrt(Y) rho(u)+O(sqrt(Y) u/log z).
```

The proof gives an explicit discrepancy bound between the atomic prime measure
and the continuous Dickman simplex, retains repeated-prime corrections, and
controls the complete bounded `P61` source remainder by an upper-bound sieve.

Therefore, for every fixed epsilon>0,

```text
u <= (1-epsilon) log log Y / log log log Y
```

implies `F(Y,z)>0` uniformly for all sufficiently large `Y`.

## Sharp method boundary

The same calculation proves that an argument using only the absolute size of
the bounded source remainder cannot continue past the critical saddle. The
remaining theorem is the exact signed bounded-remainder correlation `CBRC67`.

```text
fixed-power sector                    retained / strengthened
near-critical Dickman sector          proved positive
subcritical depth methods             refuted by frozen inputs
critical bounded-remainder correlation open / RH-bearing
GPC67 / RH                            unproved
```

## Replay

```bash
python3 experiments/X-98020-quantitative-dickman/verify.py
```

Expected:

```text
PASS_T98020_QUANTITATIVE_DICKMAN_CORRIDOR
```

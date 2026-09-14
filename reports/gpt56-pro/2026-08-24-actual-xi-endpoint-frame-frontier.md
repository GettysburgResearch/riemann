# Actual-Xi endpoint-frame frontier for ninety percent

## Publication audit

The pre-existing PR #731 head `50cf8ef...` contained the T-105290 packet but
not the previously reported T-106300/T-106310 files.  This packet is the
collision-safe, remotely deposited correction.  It does not claim that the
missing files had landed earlier.

## New exact chain

For the endpoint companions

```text
E0,+ = Xi + i lambda Xi',
E0,- = Xi - i lambda Xi',
E2,+ = Xi'' + i lambda Xi''',
E2,- = Xi'' - i lambda Xi''',
```

the complete two-rung symbol is

```text
U = E0,- E2,+ / (E0,+ E2,-).
```

Its winding is `2-2(E1+E2)`.  The intermediate Xi-prime companion cancels.
Multiplying source observations by the denominator gives the exact linear
packet

```text
E0,- E2,+ - E0,+ E2,-
  = 2 i lambda (Xi Xi'''-Xi' Xi'').
```

The Xi Fourier kernel proves unconditionally

```text
Fourier[Xi'^2-Xi Xi''](xi)
 = 1/2 integral (2u-xi)^2 Phi(u)Phi(xi-u) du >= 0.
```

Therefore the actual endpoint numerator is one explicit exterior-square Hankel
source; no frozen-to-actual numerator transfer remains.

## Robust numerical cut

A source frame of relative dimension `999/1000`, a one-percent Frobenius-square
endpoint-denominator error and a half-percent normalized actual theta-Hankel
trace imply

```text
N0/N >= 18149/20000 = 0.90745.
```

Only these actual frame estimates remain in `ROBUSTFRAME106400`.  No
operator-norm comparison is required.

## Status

```text
endpoint telescope                         PROVED EXACT
denominator cancellation                   PROVED EXACT
actual Xi exterior-square source           PROVED UNCONDITIONALLY
Frobenius quantile absorption              PROVED EXACT
ROBUSTFRAME106400                          OPEN
90 percent                                 UNPROVED
density one                                UNPROVED
RH                                         UNPROVED
```

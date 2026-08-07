# M-23001 — Review protocol for finite-prefix parity–Green coercivity

Claim ID: `M-23001`  
Status: **PROPOSED FAIL-CLOSED REVIEW PROTOCOL**  
Scope: `T-23004/PGC(R)` only

## Frozen inputs

A certificate must pin exact commits for:

- the fixed-ratio shell transform and all-ratio transfer;
- the two-frequency reflected Selberg identity;
- the endpoint-projected Green matrix;
- the signed constraint-dipole transport rules;
- `L-23013`--`L-23016`.

## Required proof object

For every retained prefix `R` and block `J`, emit:

```text
safe smoothing and normalization digest
complete finite digital prefix coefficients
complete independent-frequency block kernel
all Euler-aligned source coefficients
full dyadic Green path matrix and exact inverse
odd/mixed Schur-complement matrix
canonical equality correction
signed positivity-preserving deformation
coefficient nonnegativity checks
all carry-constraint inequalities
Dirichlet-energy and objective-cost intervals
strict lower-scale destinations
coercivity constant C_R
proof that log(C_R)/log(R) tends to zero
exact first-cell transfer digest
```

## Fail-closed mutations

The consumer must reject:

1. a one-frequency block;
2. a missing digital coefficient below `R`;
3. an unsigned digital tail;
4. a bulk `2x2` determinant advertised as strict;
5. omission of a dyadic endpoint row;
6. deletion of negative slack;
7. a nonpositive final coefficient minorant;
8. a lower-scale destination above the declared threshold;
9. a polynomial-in-`R` condition exponent bounded away from zero;
10. any claim of RH from finitely many prefixes.

## Review order

1. `L-23013` exact digit combs;
2. `L-23014` parity/carry identity and finite-horizon inequality;
3. `L-23015` dyadic Green path;
4. `L-23016` digital recurrence and Sobolev tail;
5. `R-23007` scope boundary;
6. the concrete `PGC(R)` certificate;
7. `T-23004` recurrence and first-cell transfer.

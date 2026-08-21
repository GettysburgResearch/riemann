# R-26202 — The boundary-jet schema is not yet a complete source identity

Claim ID: `R-26202`  
Title: Half-pole-null pair positivity is exact, but it does not by itself identify the linear carry profile with the proposed reflected/B-spline Schur form  
Status: **SELF-AUDIT / SCOPE CORRECTION**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-26201`--`L-26204`  
Scope: status of PR #272; RH remains unproved

## 1. What is exact

The following identities are valid independently:

1. the unrestricted Green derivative kernel is indefinite;
2. its complete indefinite part is the two-jet matrix of `L-26201`;
3. a weighted translated pair is half-pole-null and gives a rank-one positive
   Green Gram;
4. the conjugated scalar Green profile has a positive Peano/B-spline remainder;
5. the dyadic oversupport collar retains the exact Mertens shell.

## 2. Missing source map

The carry profile `mathfrak C(Y)` is linear in the Möbius source. The Green and
reflected forms used in `L-26204` are quadratic forms on source columns. To turn
those independent identities into

```text
mathfrak C(Y)
 = positive bulk
 + <J_Y,(D_Y+R_Y-N_Y)J_Y>,
```

one must emit the exact Selberg/source polarization map, every coefficient, and
every boundary term. The present branch has not emitted that map.

Consequently `L-26204.8` is a production schema, not an established finite
identity. Half-pole-null positivity does not fill this gap automatically.

## 3. Orientation warning

For a reversed endpoint kernel `phi(T-x-y)`, the relevant null moment is weighted
by `exp(-x/2)`, not `exp(x/2)`. A dyadic translation is null only after the
endpoint-distance coordinate and translation direction are declared. A proof
that changes coordinates without transforming the source weights is invalid.

## 4. Correct status

```text
R-26201/L-26201/L-26202/L-26203   exact interfaces
L-26204                           source-bound schema / unproved assembly
T-26201                           valid conditional deduction from a genuine BJD object
unconditional proof of RH         not present
```

The branch remains useful, but it should not be presented as a completed proof
until one immutable source object realizes `L-26204.8`.

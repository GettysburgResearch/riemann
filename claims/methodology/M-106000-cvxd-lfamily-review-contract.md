# M-106000 — Hostile review contract for the CV/XD L-family packet

Claim ID: `M-106000`  
Status: **BINDING REVIEW PROTOCOL**  
Created: 2026-08-24  
Applies to: `L-106000--L-106003`, `R-106000`, `T-106000`  
RH status: **unproved**

## 1. Required reconstruction order

A reviewer should reconstruct:

1. the normalized dilation multiplier `a^(-z-1/2)`;
2. the principal-character identity
   `L(s,chi_0)=zeta(s)(1-ell^(-s))`;
3. the coefficientwise ramified completion;
4. the marked-67 literal character factor `chi(67)`;
5. complete character orthogonality;
6. the square/nonsquare collision classification;
7. the two-line factorization in odd characteristic;
8. the Gauss norm and exceptional `chi^2=1` channels;
9. the positive principal-leverage extraction;
10. the exact point at which the open moment enters.

## 2. Mandatory mutations

The packet must fail review if any mutation is accepted:

```text
remove the factor ell^(-1/2) from the scale completion;
replace 1-ell^(-s) by its reciprocal;
drop chi(67) from the literal twist without declaring a common-filter variant;
apply an absolute value before the two-scale completion is recombined;
include only quadratic characters and claim core oscillation;
treat collision density 1/ell as cancellation;
choose ell or an amplifier after introducing a hypothetical zero;
omit the principal leverage Lambda_X;
infer a number-field theorem from function-field RH;
silently drop terms divisible by the family modulus;
promote finite-field Gauss sums to the incomplete Vaughan estimate;
claim that the exact replay proves an analytic moment or RH.
```

## 3. Source locks

The exact arithmetic parent is PR #719 at

```text
20e6bc5d961f00818fac86c9252e2535c5d9821a
```

The three programme coordination objects are:

```text
#743  critical scale-phase/common-mother/CV-XD programme;
#736  Dirichlet-character family completion;
#737  function-field mirror.
```

The branch is intentionally stacked on PR #719. Later movement of that PR must
be reconciled rather than silently inherited.

## 4. Replay boundary

`X-106000` verifies only:

- principal coefficient restoration;
- marked-67 coefficient restoration;
- cyclic character orthogonality;
- rational second-moment identities;
- prime-field squareclass collision lines;
- quadratic core blindness;
- nonquadratic core visibility;
- the finite-field Gauss-norm counting identity;
- finite-field collision geometry for `F_9` and `F_25`;
- the elementary family-dimension lower bound.

It does not evaluate zeta, any Dirichlet `L`-function, any function-field
Frobenius matrix, the stopped-Vaughan analytic moment, `BQSP102870`, or RH.

## 5. Acceptance classification

A correct review should classify the packet no more strongly than:

```text
finite/source/Mellin/family algebra       proved exact;
finite-field Gauss prototype              proved exact;
hybrid number-field family moment         open;
function-field geometric moment           open;
composition to RH                         conditional;
RH                                        unproved.
```

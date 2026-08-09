# O-90007 — T-90001 residency reconciliation after the GPT audit

Claim ID: `O-90007` (provisional range; allocate before integration)  
Status: **PROVENANCE / STATUS RECONCILIATION — NO NEW RH CLAIM**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Targets: `T-90001` §6 and the reviewer-facing summary of PR #351

## 1. The stale disclosure

The frozen text of `T-90001` still says:

```text
Flag 0: the full converse consumers are not physically resident;
Flag 2: real-X interpolation is only sketched in one variant.
```

Those statements accurately described the source commit at the moment it was
written. They no longer describe the stacked review branch.

## 2. Resident replacements

This branch imports, byte-for-byte from independently authored PR #348:

```text
claims/lemmas/L-90006-prime-ramp-landau-consumer.md
claims/lemmas/L-90007-rh-implies-wsts.md
```

`L-90006` contains the complete endpoint telescope, prime versus prime-power
comparison, exact prime-ramp Mellin transform, pole audit, Landau argument, and
an elementary integer-to-real interpolation. It proves

```text
WSTS => prime-ramp one-sided bound => RH.
```

`L-90007` contains the complete reciprocal-cell profile estimates, Stieltjes
integration by parts, and the conservative resident implication

```text
RH => B_X << log^4 X => WSTS.
```

The sharper `log^3 X` forward estimate in `T-90001` remains available as a
separate refinement, but is not needed for equivalence.

## 3. Updated flag ledger

```text
old Flag 0, missing resident consumers       CLOSED by L-90006/L-90007
old Flag 1, exact constants C_E,C_E'         non-load-bearing; absolute constants resident
old Flag 2, real-X interpolation             CLOSED in L-90006 §4 and L-90004 §8
old Flag 3, finite-height literature constants non-load-bearing / still requires source check
```

The frozen wording in `T-90001` should be amended at registry integration rather
than silently rewriting the historical source. Reviewers should use this file
as the current status overlay.

## 4. New endpoint sharpening

`L-90004/T-90006` go beyond the original equivalence packet. Under RH they prove

```text
T_X^s(2) = kappa log X + O(1),
kappa = (1+zeta(1/2)) log 2 / 2 < 0,
```

and therefore `B_X=0` for every sufficiently large endpoint. This does not
alter the logical boundary: the unconditional endpoint sign remains equivalent
to RH.

RH remains unproved.

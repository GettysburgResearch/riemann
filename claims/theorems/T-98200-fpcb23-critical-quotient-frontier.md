# T-98200 — Literal two-row Dickman corridor and the critical FPCB23 quotient frontier

Claim ID: `T-98200`  
Status: **UNCONDITIONAL ADVANCE AND FAIL-CLOSED FPCB23 REDUCTION**  
Created: 2026-08-18  
Frozen base: PR #592 at `05aae4135d21301a79b16abb2dda95535e0be77c`  
RH status: **unproved**

The packet establishes:

```text
literal q2 and q3-sharp dictionaries                 retained exactly
common 2 sqrt(Y) Dickman main                        proved exactly
bounded row-specific source remainders               proved
near-critical two-row positivity corridor            proved uniformly
three-band transverse correction                     proved exactly
future-prime quotient/Bellman recurrence              proved exactly
source-blind shortcuts                                rejected
```

The remaining conclusion-producing theorem is

```text
CPQR23:
Theta_23(Y,z) <= 1
at every critical quotient state in the PR #592 future-prime tree.
```

The exact chain is

```text
CPQR23 -> FPCB23 -> LPTRP23 -> RH.
```

The first implication is finite backward induction using the corridor theorem and the exact quotient recurrence; the second is PR #592's sharp normalization; the last is the frozen two-row Mellin–Landau consumer.

No proof of `CPQR23`, `FPCB23`, or RH is claimed. The new mathematical content is that every noncritical quotient state is already positive and the two rows share one hard discrepancy plus one compact transverse correction.

# R-91653 — `T-91651` is superseded as the review target

Claim ID: `R-91653`  
Status: **SCOPE CORRECTION**  
Created: 2026-08-13

PR #443 found that `T-91651` had stale machine locks, omitted the same-index child functor, used the wrong sign-side compact debt expression, and did not derive a complete root datum identity.

Those interfaces are replaced by:

```text
L-91657  compact causal-debt repair;
L-91658  normalized child embedding and actual coefficient;
L-91659  complete native/current/recursive root datum;
L-91660  self-contained endpoint deficit bridge;
O-91651  corrected review order;
t91652-full-ledger-lock.json  normative dependency lock.
```

No conclusion should be attributed to `T-91651` without these replacements. The corrected ledger remains proposed pending independent review.

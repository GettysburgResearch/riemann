# Integration handoff — bottom-charge continuation

Branch: `agent/gpt56-pro-source-specific/262-dyadic-parity-dipole`  
Parent PR: #268  
Status: **append-only continuation; RH unproved**

## New files

```text
claims/lemmas/L-26204-bottom-two-carry-charge-identity.md
claims/theorems/T-26202-bottom-charge-one-sign-rh-proposal.md
claims/methodology/M-26202-bottom-charge-review-protocol.md
experiments/X-26202-bottom-charge/
reports/gpt56-pro-source-specific/2026-08-08-bottom-charge-continuation.md
```

## Scientific change

The preferred hinge is narrowed from the broad Reflected Dyadic Hall identity to

```text
5 c_X(2)+3 c_X(3) >= 0 eventually.
```

The exact identity

```text
5 c_X(2)+3 c_X(3)
 = -6 sum_(q=2)^X omega_2(q) q^(-1/2) log(X/q)
```

makes eventual bottom-charge positivity an eventually one-signed reciprocal-zeta Riesz theorem. The conditional Landau deduction to RH is complete subject to review.

## Merge and status boundary

The new algebra may be reviewed independently of the open sign theorem. Do not mark PR #268 or RH verified merely because `X-26202` passes.

Recommended review order:

1. `L-26204`;
2. `X-26202`;
3. `T-26202`;
4. `M-26202`;
5. source-normalization comparison with PRs #269 and #241.

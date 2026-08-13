# R-91403 — Verification of the exact PR #431 counterexamples

Claim ID: `R-91403`  
Status: **EXACT REVIEW VERIFICATION / SCOPE FIREWALL**  
Created: 2026-08-13  
RH status: **unproved**

## Support cutoff

At `t=79`, `p=83`, `y=1`, the squarefree positive sources `85,86,87` satisfy `e<=t+8` but `e>py`. Their actual causal contributions vanish, while historical `L-91350.2` included them. For `a=4,5`, every omitted formal term is positive because `a^2*83>9e`. Hence historical `L-91350.2` and its old checker are false.

The live replacement `L-91352/X-91130` retains the parent cutoff and is outside this refutation.

## Mode-dependent branch

For `r=p^(-1/2)` and the canonical lift of the pure reserve state, the reviewed branch has target/score `(2r,r^2)`, whereas an `r`-scaled canonical child has `(2r,r)`. The score overspend is `r-r^2>0`. The literal branch identification in historical `T-91304` is false.

## Scalar source fraction

A restriction of source mass `1/2` can retain the complete positive endpoint loss of its parent. Therefore source-mass fraction alone does not weight signed packet loss. The packet-valued consumer `T-91401`, not the historical scalar recurrence, is the correct abstract interface.

## Noninherited rows

At the reviewed head the rows above the child endpoint had no all-branch ledger. That was a genuine gap. The later local all-row theorem `L-91353` is a separate repair and does not retroactively verify the reviewed composition.

```text
historical L-91350.2 / X-91127       FALSE
review branch-mode counterexample     VERIFIED
review scalar-loss counterexample     VERIFIED
reviewed noninherited-row interface   GAP
Riemann Hypothesis                    UNPROVED
```

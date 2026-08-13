# T-91310 — Joint canonical CFFP proposal

Status: **candidate complete on frozen inputs; independent review required; RH unproved**

Use the joint two-labelled finite block of `L-91371`. Its target and score observations are

\[
W_\Psi=w_2+2w_1,
\qquad W_S=2w_2+w_1.
\]

The current finite labels are summed before physical packing; rough children remain labelled and source-disjoint.

The exact canonical row is

\[
D_{P,X}(j)=\sum_{d\mid P_{61}}\frac{\mu(d)}{\sqrt d}Q_{X/d}(j).
\]

`L-91364`, with the first activation strip supplied by `L-91370`, proves `D_(P,X)>=0` coefficientwise. `L-91363` proves that this same row has the exact nonnegative ordinary and radix-four responses

\[
C_{P,X}(q)=q^{-1/2}H_P(X/q),
\]

\[
\Theta_{P,X}(q)=q^{-1/2}[H_P(Z)-H_P(Z/4)].
\]

Its literal entropy is `E_P(X)`. The frozen theorem on PR #437 proves

\[
E_P(X)-S_P(X)>559/50
\qquad(X\ge67),
\]

with a uniform finite bound below `67`. Hence the joint current block satisfies the CFFP row, capacity and bounded-deficit requirements, provided the source/benchmark dictionary is identical to the root endpoint criterion.

Apply `L-91362` and pass every actual rough child through the same-index functor `L-91361`. The packet recurrence of `T-91307` gives

\[
\Lambda(X)\le C_{\rm fin}+\Lambda(X/67),
\]

so `Lambda(X)=O(log X)=o(log^2 X)`. At the resident endpoint normalization this would imply RH.

Mandatory review items:

```text
joint target/score/row dictionary;
full replay and audit of X-91138 plus L-91370;
PR #437 literal-score normalization;
root packet mass and finite base;
final endpoint feasible-set sign and normalization.
```

Any failure retracts the candidate conclusion while leaving the exact row, capacity and entropy results intact.

```text
joint finite packing              EXACT REDUCTION
canonical row sign                PROPOSED COMPLETE
physical capacities               EXACT
literal entropy surplus           FROZEN PR #437
packet recurrence                 EXACT CONDITIONAL
Riemann Hypothesis                UNPROVEN PENDING REVIEW
```

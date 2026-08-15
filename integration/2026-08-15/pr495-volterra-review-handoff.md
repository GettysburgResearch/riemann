# PR #495 independent-review handoff

## Frozen graph

```text
proposal PR:      #495
proposal head:    50f45b46cbe3c471d6e702c41c7ef178b530e1ab
proposal base:    37f14be7c8bd16b3096baf08f6ba2cbc550797ac
review branch:    review/pr495-volterra-frozen-50f45b46-20260815
```

## Verdict

```text
L-91760 Volterra antiderivative/support/Fubini        VERIFIED
L-91761 rank-one source ownership                     VERIFIED WITH DENSITY PIN
L-91762 rough lift and Jacobian                       VERIFIED
L-91763 infinitesimal causal positivity               FALSE
T-92910                                               REJECTED
Riemann Hypothesis                                    UNPROVED
```

## Exact first broken arrow

For

```text
p=67, y=15, s=1005, j=14,
```

the claimed positive causal current has row coordinate

\[
p_{1005}(14)-67^{-1/2}p_{15}(14)
\in
\left(-\frac{184291}{10^9},-\frac{184290}{10^9}\right).
\]

Therefore it is negative. `L-91654` cannot be transferred from canonical endpoint rows `Q_s` to the normalized derivatives `p_s=(s/2)\partial_sQ_s`.

## Review files

```text
reports/integration-wave/20260815-pr495-volterra-frozen-head-review.md
audits/integration-wave/20260815-pr495-claim-status.tsv
experiments/reviews/X-PR495-volterra-causal-counterexample/verify.py
experiments/reviews/X-PR495-volterra-causal-counterexample/results/verification.json
integration/2026-08-15/pr495-volterra-review-handoff.md
```

## Next theorem

A successor must prove positivity only after an explicitly grouped decomposition of the full rough fibre, or replace the causal packetization. It must not assert positivity of each difference

\[
p_s-p^{-1/2}U_pp_{s/p}.
\]

The deposited witness is a mandatory mutation test.

PR #497 is a separate construction and was not used as confirmation.

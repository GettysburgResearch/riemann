# T-99240 — SHARP row-kernel anchor-free component-row candidate

This add-only successor stacks on PR #636.

Core identity:

\[
Q_Y(j)=\int_1^Y(4\sqrt{Y/t}-3)\kappa_j(t)\,\frac{dt}{t},
\qquad \kappa_j(t)>0.
\]

It replaces the unresolved second-order equality-frame/anchor interface by an
explicit first-order factorization aligned with the exact compact Hall target.

```text
score endgame                     not used
radix-four capacity endgame       not used
second-order Volterra anchors     bypassed
historical FRONTIER-CHAIN         not used
fixed-row Mellin-Landau           conclusion consumer
RH                                unproved pending review
```

Replay:

```bash
python3 experiments/X-99240-sharp-row-kernel/verify.py \
  --output experiments/X-99240-sharp-row-kernel/results/verification.json
```

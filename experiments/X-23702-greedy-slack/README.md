# X-23702 — Exact greedy-slack scope control

This standard-library-only checker supports `L-23705` and `R-23705`.

It verifies:

1. an exact rational decreasing target at `X=9`;
2. the complete minimum-ratio greedy elimination;
3. one genuine off-diagonal blocker `(n,q)=(5,4)`;
4. the positive final slack `29/500` in column `5`;
5. the identity `slack_n=beta_(n,n)*diagonal_loss_n`;
6. the exact carry-row/divisor-summatory identity through `n=64`;
7. the exact finite mass/slack conservation formula.

The control proves only that target-independent carry/digit positivity does not
force saturation. It does not concern the logarithmic target and does not refute
DBT.

```bash
python verify.py
python -m unittest discover -s tests -v
```

Expected retained verdict:

```text
EXACT_GREEDY_SLACK_SCOPE_CONTROL_VERIFIED
```

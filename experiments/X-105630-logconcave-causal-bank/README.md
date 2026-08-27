# X-105630 — Xi log-concavity constant ledger and causal-bank algebra

Run:

```bash
python3 experiments/X-105630-logconcave-causal-bank/verify.py \
  experiments/X-105630-logconcave-causal-bank/results/verification.json
```

Expected:

```text
PASS_X_105630_LOGCONCAVE_CAUSAL_BANK
f511cef71f3f5cf8bac793569aa78ff12ffc9dee659a72803cbe2c950b890e99
checks=102
RH_UNPROVEN
```

The replay checks:

- the exact rational constant ledger used in `L-105626`, including the
  `1881/7000<1` log-concavity margin;
- 77 finite causal-shift/decreasing-weight contractions;
- 19 finite one-factor model-bank bookkeeping fixtures.

It does **not** replay the infinite theta-series mixture proof, the Cartwright
inner-function theorem, the infinite model-space theorem, descent below the
unknown `beta_0`, or RH.

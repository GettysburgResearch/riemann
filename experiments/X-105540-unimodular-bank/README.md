# X-105540 — Unimodular bank replay

```bash
python3 experiments/X-105540-unimodular-bank/verify.py \
  --output experiments/X-105540-unimodular-bank/results/verification.json
python3 -m unittest experiments/X-105540-unimodular-bank/tests/test_verify.py
```

The replay checks exact polynomial and rational matrix identities.  It does
not machine-prove the imported analytic Xi source estimates,
`MATRIXLERC105541`, 90%, a new record, or RH.

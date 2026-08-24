# X-105530 — Exact Hermitian bank and matrix-flux replay

Run

```bash
python3 experiments/X-105530-hermitian-bank/verify.py \
  --output experiments/X-105530-hermitian-bank/results/verification.json
python3 -m unittest \
  experiments/X-105530-hermitian-bank/tests/test_verify.py
```

The replay authenticates exact finite algebra only.  It does not prove the
PNT, a strip factorization, the Xi endpoint/companion bound, 90%, or RH.

# X-105680 — Cauchy determinant and rank-extension replay

Run

```bash
python -B experiments/X-105680-cauchy-determinant-extension/verify.py \
  --output experiments/X-105680-cauchy-determinant-extension/results/verification.json
python -B -m unittest tests.test_t105680_cauchy_determinant_extension
```

Expected verdict:

```text
PASS_T105680_CAUCHY_DETERMINANT_AND_EXTENSION
```

The exact rational replay checks:

- the Cauchy determinant-gain product on a complex rank-three packet;
- 224 instances of the positive complex-pair polynomial identity;
- the nested projection increment identity through rank four.

It does not prove `REC105681`, arbitrary-rank trace CTI, the cofinal Xi passage,
or RH.

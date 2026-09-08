# X-91410 — Hahn second-mode replay

```bash
python3 verify.py --json /tmp/result.json
cmp /tmp/result.json results/verification.json
```

The replay checks exact beta-binomial normalization and detailed balance, the degree-one and degree-two Hahn eigenfunctions, the exact finite Stein-kernel decomposition and variance, and synthetic cone-valued detail algebra. It does not prove any RH-bearing application gate.

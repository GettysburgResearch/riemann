# X-91730 — Completed arithmetic Julia-cascade replay

This finite replay checks:

1. positivity of the eta, compact-bridge, and gamma detail kernels;
2. the exact ordered Schur-product cascade identity;
3. positivity of every global returned/detail channel;
4. additivity of the diagonal entropy chain.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_COMPLETED_ARITHMETIC_JULIA_CASCADE
```

The replay uses finite positive quadratures. It does not prove the canonical
source-to-model map, CAJE, or RH.

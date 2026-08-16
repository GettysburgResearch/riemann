# X-96010 — two-row annular consumer hardening

```bash
python3 verify.py --limit 1000000 --output results/verification.json
python3 tests/test_verify.py
```

The replay checks the exact low-row divisor kernels against direct beta-matrix inversion, the two-row elimination algebra, the PR #541 normalization counterexample, and a deterministic integer-knot scan. The scan is falsification evidence, not a proof of the infinite positivity theorem or RH.

# X-96100 — two-row annular Mellin hardening

```bash
python3 verify.py --limit 500000 --output results/verification.json
python3 tests/test_verify.py
```

The replay checks rows two and three at every integer through the requested limit, reconstructs the original triangular average-binomial inverse at selected endpoints, checks exact logarithmic interpolation across real endpoint cells, verifies the two-row cancellation factorization, and rejects normalization and smoothing mutations.

`scan_extended.c` is the independent long-double Kahan scanner used for the retained 150,000,000-endpoint campaign. A secondary double scan reached 250,000,000. Numerical scans do not prove TAP4 or RH.

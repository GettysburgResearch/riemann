# X-91840 — PR #484 exact-root composition recovery

Run:

```bash
python3 verify.py --mutations --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
```

The checker authenticates exact finite source-partition algebra, partial-cell
restriction, first-owner disjointness, six-class PSD port aggregation, the
fourteen-stage packet identity, direct native-cost constants and fail-closed
mutations. It does not replay the imported analytic Hall/capacity/endpoint
consumer and does not establish RH.

# X-105400 replay

```bash
python3 verify.py
python3 tests/test_verify.py
```

The replay checks exact finite Euler corners, both owner shellings, 1,000 toric
Hodge identities, 10,000 exact three-ray identities, the source-blind
activation separator, and nine fail-closed mutations.

It does not prove the analytic Stokes theorem, `F1PE105403`, or RH.

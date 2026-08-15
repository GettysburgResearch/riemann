# X-91860 — two-sorted Hall-row finite regression

Run:

```bash
python3 verify.py --mutations --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
```

The checker verifies exact Hall residual/bonus algebra, the `x=2` score obstruction, many-to-one first ownership, two-sorted routing, one block realization, one row identifier, all-column/terminal constants, direct `Y_4` ledger, and hostile type mutations. It does not replay the analytic factor-67 inputs or prove RH.

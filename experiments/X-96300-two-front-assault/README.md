# X-96300 radical two-front assault exact regression

```bash
python3 verify.py certificates/control.json --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
```

The replay authenticates exact algebra only: the compact tent kernel after removal of its common exponential, the positive-base scalar row, factorized Mellin numerator, finite Dirichlet convolution, formal `mu*Lambda=-mu*log`, affine signed-moment cone, Mellin-coordinate bridges, genealogy and fail-closed statuses.

It does not prove `ACTQ_h`, `SPRP`, `VRP`, `AMCP`, or RH.

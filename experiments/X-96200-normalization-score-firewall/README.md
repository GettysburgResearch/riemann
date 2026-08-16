# X-96200 normalization and score firewall

```bash
python3 verify.py certificates/control.json --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
```

This exact regression distinguishes \(P_\Lambda-\mathcal H\) from
\(J_\Lambda-\mathcal H\), checks the affine compression algebra and physical
cost, and fail-closes on the invalid imported tails and unproved direct-row
transport. It does not prove RH.

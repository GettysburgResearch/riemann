# X-91880 — Native hybrid two-sorted compiler regression

Run:

```bash
python3 verify.py --mutations --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
```

The replay checks exact finite algebra, the three mandatory firewalls, same-row comparison algebra, every synthetic small column, terminal and native constants, and hostile type mutations. It does not replay the directed AVLT sweep, analytic endpoint estimates, prime-square theorem, Mellin transform, Landau theorem, or prove RH.

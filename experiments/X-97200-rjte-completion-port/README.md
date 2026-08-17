# X-97200 — RJTE finite-state audit

Replay:

```bash
python3 verify.py certificates/control.json --output /tmp/x97200.json
cmp /tmp/x97200.json results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
```

The verifier uses:

* exact rational coefficient arithmetic;
* 200-bit dyadic square-root enclosures for the finite Euler overshoot;
* directed 80-digit Decimal intervals for the TFPE trace separator;
* 220-bit interval recurrence for every descending-prime quotient state through `N=8192`.

It certifies finite statements and proof-scope firewalls only. It does not prove RJTE, TFPE/ACBI, FCBI or RH.

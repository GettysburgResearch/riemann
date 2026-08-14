# X-91692 — Triple-closure finite regression

Run:

```bash
python3 verify.py certificates/control.json --output /tmp/verification.json
cmp /tmp/verification.json results/verification.json
python3 -m unittest discover -s tests -v
```

Expected top-level verdict:

```text
PASS_TRIPLE_CLOSURE_FINITE_ALGEBRA
```

This experiment verifies exact finite algebra only. It does not independently
replay the factor-67 endpoint producer, the endpoint-to-RH implication, or the
actual Xi zero product.

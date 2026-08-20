# X-99900 replay

```bash
python3 verify.py
python3 tests/test_verify.py
```

The replay checks exact exponent bookkeeping, seven finite coefficientwise
three-band identities, the Cauchy–Poisson/Hardy identity at `tau=1/2`, two
exact ratio-window Gram fixtures, and eight fail-closed mutations.

It does not prove the half-order window estimate, `GPMOC99800`, or RH.

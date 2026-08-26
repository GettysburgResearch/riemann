# X-104630 — Fractional-current exact replay

Run:

```bash
python3 verify.py results/verification.json
```

The standard-library replay verifies:

- the exact rational fifth-current metric exponent;
- the rational exponential and logarithmic comparisons;
- the fractional one-zero scale CDF identity;
- the complete shallow/deep 90-percent ledger;
- the strict `299/10^6` final margin.

It does not prove `FRACTRANS104630`, more than ninety percent, or RH.

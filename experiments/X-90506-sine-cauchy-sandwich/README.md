# X-90506 — Sine/Cauchy sandwich replay

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The replay checks the exact half-line Cauchy difference kernel, finite Gram positivity, sine diagonalisation of odd translations, and a finite positive-symbol sandwich.

It does not prove positivity of the zeta explicit-formula symbol or RH.

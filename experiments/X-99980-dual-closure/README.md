# X-99980 — Lightweight exact dual-route replay

Run:

```bash
python3 verify.py --output results/verification.json
```

The replay checks finite-difference block positivity fixtures, exact
random-order flow coefficients by enumerating every permutation through
five labels, the zero neutral phase, and the Cauchy phase gap.

It does not prove `FEAG99980`, `PSCP99990`, or RH.

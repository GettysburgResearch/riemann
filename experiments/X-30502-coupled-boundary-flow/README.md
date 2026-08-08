# X-30502 — Coupled boundary flow regression

Run:

```bash
python verify.py
```

The exact layer checks:

- the rational inequalities used in the row-eight sign theorem;
- the adjacent central-tree carry identity;
- the exact dyadic commutator identity
  `h_(2m+1)-h_(2m)=E_(2m)-E_m`.

The Decimal layer samples the closed coefficient formula through row 10,000 and is explicitly reconnaissance.

The checker does **not** prove the all-scale paired-tail debt bound, Cycle Debt, or RH. The analytic proofs are in `L-30503`--`L-30506`.

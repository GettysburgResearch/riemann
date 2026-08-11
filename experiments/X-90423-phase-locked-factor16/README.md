# X-90423 — Phase-locked factor-16 algebra replay

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
```

The verifier uses only the Python standard library and exact `Fraction` arithmetic, including a two-dimensional implementation of `Q(sqrt(2))`.

It checks:

- factorization and all four prescribed roots of `Q_*`;
- exact factor-16 annular kernel coefficients;
- positivity of the first 65 inverse coefficients at the two-adic factor;
- positivity of the first 64 generalized-prime coefficients;
- the fixed current gauge coefficients;
- the exact critical Fejer--Riesz Laurent coefficients;
- positivity of the scale-frame lower constant.

It proves finite algebra only. It does not prove the critical prime estimate, deterministic PIG, or RH.

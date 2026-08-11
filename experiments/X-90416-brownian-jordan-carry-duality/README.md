# X-90416 — Brownian/Jordan carry duality replay

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
```

The checker uses only Python's standard library and exact `Fraction` arithmetic.

It verifies:

- the complete-residue covariance formula
  `Cov(X_d,X_e)=((d,e)^2-1)/(4de)`;
- the exact Jordan-2 quadratic factorization;
- the fixed-endpoint reflection Brownian-bridge identity;
- the exact fixed-endpoint counterexamples in `R-90416`.

The replay proves finite algebra only. It does not prove source-specific boundary transference, PIG, the repaired global pole adapter, or RH.

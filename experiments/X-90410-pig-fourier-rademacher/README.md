# X-90410 — PIG Fourier/Rademacher finite regression

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

The verifier checks:

- exact four-adic compact-innovation coefficients through 512;
- exact ordinary-prefix coefficients through 512;
- 2,142 exact prefix/carry rows;
- finite Fourier coefficient and inverse-Laplacian identities;
- exhaustive Rademacher orthogonality at parent 24;
- finite bulk-residue inequalities.

It proves finite algebra only. It does not prove deterministic PIG, the global
Q4 recurrence, or RH.

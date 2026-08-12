# X-91630 — Paired-eta weighted Julia replay

This finite replay supports `L-91630`, `L-91631`, and the source normal form of
`T-91630`.

It checks:

1. positivity of the full-carrier eta-detail kernel
   ```text
   K_(sigma-omega)-K_(sigma+omega);
   ```
2. the pointwise weighted Julia column
   ```text
   exp(-2 omega y)+(1-exp(-2 omega y))=1;
   ```
3. the exact completed Xi factorization after writing `eta_D(z)=z I_eta(z)`;
4. the positive beta/Laplace integral for the residual gamma ratio;
5. innerness of the rational factor `(s-omega)/(s+omega)` on the boundary;
6. boundedness of the forward weighted sector map and growth of the inverse on
   one fixed common truncation.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_PAIRED_ETA_WEIGHTED_JULIA
```

The replay verifies finite carrier kernels, analytic factorization, and source
identities.  It does not prove the canonical source-to-model colligation,
PEJGOC, or RH.

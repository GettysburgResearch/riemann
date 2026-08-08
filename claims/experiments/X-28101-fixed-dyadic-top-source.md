# X-28101 — Exact fixed-dyadic top-source regression

Claim ID: `X-28101`  
Title: Standard-library replay of fixed-fraction radix vacuity, fixed dyadic factorization, stable recovery, and common-fiber PSD congruence  
Status: **EXACT FINITE REGRESSION; NO PHYSICAL BOUNDARY CERTIFICATE**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #281

The checker verifies five finite `(K,V)` controls. It uses an integer-valued
completely additive formal logarithm in place of `log n`, so every Dirichlet
convolution identity remains exact.

Retained verdict:

```text
PASS_EXACT_FIXED_DYADIC_TOP_SOURCE_AND_FIBER_CONGRUENCE
cases 5
mutation tests 7/7
proof-object SHA-256
b8980012fe9f4b116b77e1e4c6c2bd70dc323cb5e74113c5aa3070c4c12b3fc
```

The regression proves no asymptotic estimate. In particular it does not
construct `FBCF5TC`, certify a physical block recurrence, or prove RH.

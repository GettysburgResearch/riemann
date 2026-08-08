# X-28003 — Eta-preconditioned shift factorization

This exact standard-library regression supports `L-28014`.

It verifies with `fractions.Fraction` arithmetic:

1. the reciprocal-eta divisor prefix
   ```text
   sum_(d|h) b_eta(d) = h if h is a power of two, else 0;
   ```
2. the finite operator identity
   ```text
   (I-U)^(-1)(C-U)f
   =sum_(r>=0) 2^r [f(2^(r+1)q-1)-f(2^(r+1)q)];
   ```
3. the exact factorization
   ```text
   I-C=(I-U)(I-K);
   ```
4. the closed coefficient formula at `tau=1` through degree 64;
5. the rational normalization used in the analytic estimate.

The checker does **not** prove the reciprocal-eta/two-contact source bound, RTCT, or RH.  The all-order `6/31` contraction is proved analytically in the claim file; the finite replay authenticates the algebraic operator and coefficient normalizations.

Run:

```bash
python experiments/X-28003-eta-preconditioned-shift/verify.py
```

Expected verdict:

```text
PASS_EXACT_ETA_PRECONDITIONED_SHIFT_FACTORIZATION
```

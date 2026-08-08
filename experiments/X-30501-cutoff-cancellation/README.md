# X-30501 — Cutoff cancellation and shift factorization

Run:

```bash
python verify.py
```

The standard-library checker verifies:

- the exact factorization of every `2kq-1` lattice shift as the divisor source
  `sigma(m)=r(2m-1)-r(2m)`;
- the modified central-stage identity
  `central flow + terminal shift flow + unshifted eta residual = input target`;
- directed reciprocal-square-root enclosures on the macroscopic quotient cell
  used in `R-30501`.

Expected verdict:

```text
PASS_EXACT_SHIFT_FACTORIZATION_AND_CUTOFF_OBSTRUCTION
```

The checker does not prove the cofinal `N/100` lower bound—that proof is written
analytically in `R-30501`. It also does not prove the remaining critical-variation
estimate, Cycle Debt, or RH.

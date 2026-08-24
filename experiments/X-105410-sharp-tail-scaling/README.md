# X-105410 — sharp tail-scaling replay

Run:

```bash
python -B experiments/X-105410-sharp-tail-scaling/verify.py \
  --output experiments/X-105410-sharp-tail-scaling/results/verification.json
```

Expected:

```text
PASS_X_105410_SHARP_TAIL_SCALING
```

The replay checks exact finite rational algebra for:

- the Hilbert/Cauchy determinant `H_k^(a)` through `k=7`;
- the final Schur constant;
- the graded tail-moment congruence;
- an exact family separating the old isotropic moment rate from the natural graded rate.

It does not evaluate Xi, replay real-saddle concentration, prove the complete critical tail real/nonpositive, perform low-order descent, or prove RH.

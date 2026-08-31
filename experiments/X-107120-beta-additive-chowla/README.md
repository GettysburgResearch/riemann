# X-107120 — Beta additive-Chowla normal-form replay

Run

```bash
python -B experiments/X-107120-beta-additive-chowla/verify.py \
  --output experiments/X-107120-beta-additive-chowla/results/verification.json
python -B -m unittest tests.test_t107120_beta_additive_chowla
```

Expected verdict:

```text
PASS_T107120_BETA_ADDITIVE_CHOWLA_NORMAL_FORM
```

The replay uses exact `Fraction` arithmetic. It checks:

- direct pair expansion versus additive-gap grouping;
- squarefree gcd/common-core reindexing;
- diagonal and compact-support controls;
- the algebra of the square-root tail threshold.

It does **not** replay the classical Dirichlet-polynomial mean-value theorem,
the zero-abscissa theorem, the open low-frequency cancellation estimate, or
RH.

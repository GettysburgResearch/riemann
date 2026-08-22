# X-104530 — Residue-coherence transfer replay

Run:

```bash
python3 experiments/X-104530-residue-coherence/verify.py \
  --output /tmp/t104530-verification.json
cmp /tmp/t104530-verification.json \
  experiments/X-104530-residue-coherence/results/verification.json
```

Expected:

```text
PASS_T104530_RESIDUE_COHERENCE_TRANSFER_ALGEBRA
5b5b95054a1e6c42eb89eb79fa13b2c608293b84150c4613131fcaebf8646d9e
```

The replay checks only the exact finite Cauchy--Schwarz transfer algebra, the
mean/variance parameterization, three rational residue fixtures and the fact
that different antecedent proportions produce different conclusions.

It does **not** estimate the Xi residue moments, prove `RCMV104530`, or prove
RH.

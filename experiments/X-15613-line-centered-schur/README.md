# X-15613 — Exact line-centered Schur perturbation replay

This experiment is a standard-library-only rational regression for `L-15632`.
It verifies a nonreducing line-centered block, a strict relative full-block
perturbation, the line-centered harmonic minimizer, the PR #191 residual-short
formula, and the final normalized negative-part bound.

Run:

```bash
python experiments/X-15613-line-centered-schur/verify.py \
  experiments/X-15613-line-centered-schur/certificates/synthetic.json \
  --output experiments/X-15613-line-centered-schur/results/replay.json

python -m unittest \
  experiments/X-15613-line-centered-schur/tests/test_verify.py
```

The retained exact values are

```text
line-centered Schur               0
actual Schur                     -1/1000
eta                               11/45
normalized theorem bound          11/4500
normalized negative part           1/1000
strict slack                       13/9000
```

The synthetic result proves only the finite block algebra. It is not a Suzuki
production packet and carries no RH verdict.

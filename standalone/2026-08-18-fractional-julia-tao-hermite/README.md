# T-98700 fractional Julia–Tao–Hermite candidate

This directory is the standalone front door for the research-reset candidate.

```text
base PR #610  edf28c9ad14ccbf5b18b9ced45f3c2fc4ce8221d
candidate     T-98700
status        proposed complete theorem; RH unproved pending review
```

Core chain:

```text
fractional reciprocal-Julia parity
 -> atomwise Tao source Gram
 -> common Fock direct limit
 -> tunable First-Hermite heat bound
 -> off-line pole contradiction
 -> RH.
```

Replay:

```bash
python3 experiments/X-98700-fractional-julia-hermite/verify.py \
  --output experiments/X-98700-fractional-julia-hermite/results/verification.json
sha256sum -c T98700_CONTENT_SHA256SUMS
```

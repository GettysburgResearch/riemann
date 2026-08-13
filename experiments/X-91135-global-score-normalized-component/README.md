# X-91135 — Global score-normalized component monotonicity

Companion replay for `L-91359`.

```bash
python3 experiments/X-91135-global-score-normalized-component/verify.py
```

Expected verdict:

```text
PASS_GLOBAL_SCORE_NORMALIZED_COMPONENT_MONOTONICITY_REDUCTION
```

The checker uses exact `Fraction` arithmetic and directed rational square-root/logarithm enclosures. It certifies the 65 fixed large-endpoint inequalities at `Y=83`; the analytic proof in `L-91359` propagates them to every `Y>=83`. The already resident finite-window theorem covers `Y<83`.

The replay does not prove bounded-inner causal ratio monotonicity, the full even/odd determinant, literal row-packet typing, or RH.

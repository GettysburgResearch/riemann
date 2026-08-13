# X-91137 — Causal row-per-score monotonicity refutation

Companion exact replay for `R-91311`.

```bash
python3 experiments/X-91137-causal-ratio-refutation/verify.py
```

Expected verdict:

```text
PASS_CAUSAL_RATIO_CONTINUOUS_MONOTONICITY_REFUTATION
```

The checker uses only the Python standard library, exact `Fraction` arithmetic, directed rational square-root intervals, and rational atanh-series logarithm intervals. It certifies that the logarithmic derivative numerator of the causal ratio is below `-1.52` at `j=66`, `p=67`, `z=133/2`.

This refutes the continuous monotonicity asserted by historical `L-91360`. It does not refute discrete ordering on the actual divisor set and does not prove or disprove RH.

# X-91121 — Score Hall and coefficient-one rough child

Companion exact replay for `L-91339/L-91340/L-91341`.

```bash
python3 experiments/X-91121-score-hall-and-coefficient-one-child/verify.py
```

Expected verdict:

```text
PASS_SCORE_HALL_AND_COEFFICIENT_ONE_CHILD
```

The checker verifies the exact score-Hall margin `3/100`, the SHARP-source Hall
margin `3/5`, monotonicity of the target-per-score ratio, and the coefficient-one
child plus positive harmonic-score-surplus identities. It imports the previously
certified directed Hall corridors and does not prove the all-generation reset or
RH.

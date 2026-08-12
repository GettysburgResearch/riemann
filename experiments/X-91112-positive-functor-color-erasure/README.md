# X-91112 — Positive-functor rough-color erasure

Companion replay for `L-91324`.

```bash
python3 experiments/X-91112-positive-functor-color-erasure/verify.py
```

Expected verdict:

```text
PASS_POSITIVE_FUNCTOR_COLOR_ERASURE
```

The standard-library checker verifies exact affine Pascal covariance on real
columns, including physical columns not divisible by the rough color. It also
checks representative positive branch-port sums and the exact `p>=67`
`1/9` threshold.

The finite replay illustrates exact algebra. The theorem that positive linear
maps preserve positive-semidefinite domination is proved in the claim file and
is not inferred from the synthetic examples.

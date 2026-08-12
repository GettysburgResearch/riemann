# X-91119 — Scale-weighted rough contraction

Companion exact replay for `L-91332` and the correction `R-91306`.

```bash
python3 experiments/X-91119-scale-weighted-rough-contraction/verify.py
```

Expected verdict:

```text
PASS_SCALE_WEIGHTED_ROUGH_CONTRACTION
```

The checker verifies the exact positive `ell^1` operator norm

```text
1+2/sqrt(p)-3/p
```

and the uniform scale-weighted estimate

```text
sqrt(X/p)||Dtilde_p z||_1 < (5/32)sqrt(X)||z||_1
```

for every `p>=67`. It does not construct the disjoint least-prime source
partition or prove RH.

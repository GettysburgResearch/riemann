# X-91109 — Affine Pascal dilation and entropy amplification

Companion replay for `L-91318`.

```bash
python3 experiments/X-91109-affine-pascal-dilation/verify.py
sha256sum -c experiments/X-91109-affine-pascal-dilation/SHA256SUMS
```

Expected verdict:

```text
PASS_AFFINE_PASCAL_DILATION_AND_SCORE_AMPLIFICATION
```

The standard-library checker uses exact integer and `Fraction` arithmetic. It
verifies:

- agreement of the real-column Pascal kernel with every integer carry column;
- exact affine covariance under `n -> m(n+1)-1`, `q -> mq`;
- atomized carry covariance for lifted splits;
- exact finite binomial inequalities underlying the entropy amplification
  `G_(m(n+1)-1) >= m G_n`.

The replay proves finite algebra only. It does not provide the remaining
positive projection from colored rough fibers to the ordinary physical column
space or prove RH.

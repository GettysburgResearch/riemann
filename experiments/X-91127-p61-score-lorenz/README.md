# X-91127 — P61 score Hall and Lorenz prefixes

Companion replay for `L-91348`.

```bash
python3 experiments/X-91127-p61-score-lorenz/verify.py
```

Expected verdict:

```text
PASS_P61_SCORE_HALL_AND_LORENZ_PREFIX
```

The standard-library checker uses exact reciprocal-prefix arithmetic and directed fixed-point square-root enclosures. It certifies:

- the displacement-eight Ferrers Hall inequalities in endpoint-score currency;
- the child score-prefix envelope below `4 sqrt(y)`;
- `D(c-)>3/40` at every possible lower-tail cutoff;
- `-1<=A(z)<=1` on every `P_61` prefix state;
- strict monotonicity of `F(z)=zA(z)-sqrt(z)M(z)`, via `F'(z)>1/40` on every activation cell;
- the exact negative radius-seven witness at threshold `47`.

The symbolic theorem uses these gates to prove that the canonical lower-tail score residual is score-exact and target-subordinate for every real `p>=67` and `1<=y<=67`.

The replay does not certify exact-row subordination or RH.

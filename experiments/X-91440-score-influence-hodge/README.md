# X-91440 — Score/influence/Hodge exact replay

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
```

The replay verifies:

- the exact two-atom counterexample separating SHARP target mass from endpoint-score mass;
- finite product-martingale/Doob covariance decompositions with every coordinate influence nonnegative;
- beta-binomial Hahn detailed balance, current divergence, Hodge potential, resistance energy, sharp Young completion and the unit-gap bound through `N=32`.

It does not verify the shape-uniform factor-54 packing functor, the quantitative prime-influence lower bound, the theta reserve, Brownian Pick positivity, PR #407's claimed proof, or RH.

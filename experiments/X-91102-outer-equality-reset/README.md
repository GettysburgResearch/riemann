# X-91102 — Outer equality correction and endpoint-weight reset certificate

Companion replay for `L-91106` and `L-91107`.

```bash
python3 experiments/X-91102-outer-equality-reset/verify.py
```

Expected verdict:

```text
PASS_OUTER_EQUALITY_CORRECTION_ONE_CROSSING
```

The checker uses only the Python standard library. It verifies with exact
`Fraction` arithmetic and directed rational enclosures:

- positivity of every reciprocal knot through `N=54`;
- negativity at `1/55`;
- the one-extremum cell geometry;
- a rigorous bracket for the unique outer crossing;
- the finite sum-versus-integral constant below `113`;
- positivity of the continuum endpoint equality weight on the complete reset
  window, with lower margin above `0.3186`.

The certificate proves finite arithmetic and analytic-cell inequalities only.
It does not prove a nonnegative finite shadow reset, the all-generation score
recurrence, or RH.

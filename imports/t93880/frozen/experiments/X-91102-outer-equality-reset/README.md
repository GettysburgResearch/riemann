# X-91102 — Outer equality correction and endpoint-weight reset certificate

Companion replay for `L-91106`, `L-91107`, `L-91108`, and `L-91111`.

```bash
python3 experiments/X-91102-outer-equality-reset/verify.py
python3 experiments/X-91102-outer-equality-reset/verify_window_bounds.py
```

Expected verdicts:

```text
PASS_OUTER_EQUALITY_CORRECTION_ONE_CROSSING
PASS_FACTOR54_EQUALITY_RESERVE_WINDOW_BOUNDS
```

The checkers use only the Python standard library. They verify with exact
`Fraction` arithmetic and directed rational enclosures:

- positivity of every reciprocal knot through `N=54`;
- negativity at `1/55`;
- the one-extremum cell geometry;
- a rigorous bracket for the unique outer crossing;
- the finite sum-versus-integral constant below `113`;
- positivity of the continuum endpoint equality weight on the complete reset
  window, with lower margin above `0.3186`;
- the global reset-window upper bound `L(x)<1.83`;
- nonnegativity of the reserve on the whole window and the lower margin
  `R(x)>0.41` for `x>=2`.

The certificates prove finite arithmetic and analytic-cell inequalities only.
They do not prove a nonnegative finite shadow reset, the all-generation score
recurrence, or RH.

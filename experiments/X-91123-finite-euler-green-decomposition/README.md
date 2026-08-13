# X-91123 — Finite Euler component-row Green decomposition

Companion exact replay for `L-91344`.

```bash
python3 experiments/X-91123-finite-euler-green-decomposition/verify.py
```

Expected verdict:

```text
PASS_FINITE_EULER_GREEN_DECOMPOSITION
```

The checker treats every logarithmic ramp `ell_x(k)` as an independent formal
symbol and uses only exact `Fraction` arithmetic. It verifies:

- direct expansion of the finite Euler transform of the component row;
- the positive rough-lattice Green coefficient;
- all finite correction sectors `m<j`, `m=j`, and `m=j+1`;
- the exact finite-boundary Green formula;
- adjoining one additional prime by shifted-symbol renewal;
- coefficientwise positivity of the rough Green difference.

The replay deliberately does not certify the remaining `P_79` finite-boundary
inequality, the one-prime target/score source splice, or RH.

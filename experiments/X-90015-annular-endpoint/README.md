# X-90015 — 3–7–5–1 annular endpoint regression

Companion checker for `L-90015` and `T-90011`.

Run from the repository root:

```bash
python experiments/X-90015-annular-endpoint/verify.py --max-x 5000000
```

Expected line:

```text
PASS_3751_ANNULAR_ENDPOINT_REGRESSION
```

## What it authenticates

- the exact moments of the coefficient vector `(3,-7,5,-1)`;
- the factorization `(1-y)^2(3-y)`;
- the numerical intervals for the moat constant, the `xi` zero-square mass, and the strict RH-side margin;
- the radical-switching computation of `A_N`;
- every filtered value at multiples of 729 through the retained endpoint;
- direct reconstruction from the exact annular kernel at selected endpoints.

## What it does not prove

The finite scan does not prove eventual negativity, RH, the contour shift, or Landau's theorem. Those are mathematical statements in the companion claims. The numerical constant check is deliberately broad: the retained analytic margin exceeds `1.48`.

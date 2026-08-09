# X-90007 — Endpoint negative-drift regression

Companion regression for `L-90004` and `T-90006`.

Run from the repository root:

```bash
python experiments/X-90007-endpoint-negative-drift/verify.py
```

The default finite endpoint is `10^6`; use `--max-x` to change it.

## What the checker authenticates

1. **Prime-zeta Laurent coefficient.** It evaluates the exact continuation
   
   ```text
   P_1(s) = sum_m mu(m) (-zeta'/zeta)(m s)
   ```
   
   and the shifted-difference series of `L-90004`, then verifies numerically that
   
   ```text
   z^3 Ahat(z) -> (1+zeta(1/2))/2,
   z^2 shell_hat(z) -> (1+zeta(1/2)) log(2)/2.
   ```

2. **Exact finite radical switching.** It computes
   
   ```text
   J_P(X)
   = sum_m b_X(m)[log rad(m)-log rad(m-1)]
   ```
   
   rather than the slower prime/multiple double loop.

3. **Finite mutation/regression.** Through the retained endpoint `10^6`, every
   dyadic shell is negative and the ratio `shell/log X` moves toward
   
   ```text
   kappa = -0.15954671491971181285...
   ```
   
   The centered remainder remains bounded on the retained rows.

Expected terminal line:

```text
PASS_ENDPOINT_NEGATIVE_DRIFT_REGRESSION
```

## What it does not authenticate

The script does **not** prove RH, the contour shift, the all-zero residue series,
or eventual negativity. Those are written mathematical arguments in `T-90006`.
The finite data are regression evidence only and must not be extrapolated.

The retained JSON was produced with Python 3 and `mpmath`, using

```bash
python verify.py --max-x 1000000
```

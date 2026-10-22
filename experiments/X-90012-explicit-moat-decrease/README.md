# X-90012 — Explicit prime-power moat decrease certificate

Companion directed-interval certificate for `L-90012`.

Run from the repository root:

```bash
python experiments/X-90012-explicit-moat-decrease/certify.py
```

Expected line:

```text
PASS_EXPLICIT_PRIME_POWER_MOAT_DECREASE_CONSTANTS
```

## What is authenticated

Using `mpmath.iv` at 70 decimal digits, the script verifies:

```text
u_10 < -0.0092;
v_15 < -0.0142;
w_1>w_2>...>w_9>0;
(1/2)sum_(K<=14) v_K^+ sqrt(K) < 3.32;
-29.417 < M(2000) < -29.416.
```

The value of `M(2000)` is evaluated directly from

```text
J_P(2000)
 =sum_m b_2000(m)[log rad(m)-log rad(m-1)]
```

plus the complete higher-prime-power ramp and `-4sqrt(2000)`.

The remaining inequalities in `L-90012` are symbolic or rational:

```text
u_K and v_K are decreasing;
nonboundary exponent sum < 2.352 for X>=2000;
classical theta(x)<=1.01624x;
base budget < -2.8979;
final derivative budget < -0.30.
```

The script does not prove the imported Rosser--Schoenfeld bound and does not
address the RH-sensitive upper-wall inequality.

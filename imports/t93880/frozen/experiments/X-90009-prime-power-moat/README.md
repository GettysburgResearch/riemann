# X-90009 — Prime-power moat and endpoint-monotonicity audit

Companion audit for `L-90009` and `T-90009`.

Run from the repository root:

```bash
python experiments/X-90009-prime-power-moat/verify.py
```

The default endpoint is `10^6`.  The retained JSON was produced with

```bash
python experiments/X-90009-prime-power-moat/verify.py --max-x 5000000
```

## What is authenticated

The script constructs, from one prime sieve,

```text
d(m) = log rad(m)-log rad(m-1),
S_a(X) = sum_(m<=X) m^a d(m),
theta_1/2(X) = sum_(p<=X) log(p)/sqrt(p),
psi_1/2(X) = sum_(n<=X) Lambda(n)/sqrt(n).
```

It then checks the exact finite formulas

```text
J_P(X)
 =2 log(X) S_1/2(X)
  -2 sum sqrt(m)log(m)d(m)
  -4 S_1/2(X)
  +4 S_1(X)/sqrt(X),

A(X)=J_P(X)-prime_ramp(X),

Delta_Lambda(X)=4sqrt(X)-full_prime_power_ramp(X),

M(X)=A(X)-Delta_Lambda(X),

D M(X)=D A(X)+psi_1/2(X)-2sqrt(X).
```

Direct radical switching is independently compared with the prefix-moment
formula at small endpoints.

The integer increment formula of `T-90009` is then scanned, and the maximum of
the real logarithmic derivative on every interval `(N,N+1)` is found from its
two endpoint limits; on each interval the derivative is affine in `X^-1/2`.

## Retained reconnaissance

Through `X=5,000,000`:

```text
A_(N+1)-A_N < 0 at every endpoint;
D A(X) < 0 throughout every open interval;
M(X) < 0 and D M(X) < 0 at every retained sample.
```

The largest integer increment was

```text
-6.270389820674203e-7 at N=4,409,886,
```

and the largest interval derivative maximum was

```text
-0.0064383486728724695 on (222,223).
```

These are **finite observations only**.  They are not promoted to eventual
monotonicity.  `T-90009` proves that eventual monotonicity would imply RH and
identifies the exact weighted-Chebyshev barrier; the missing barrier is still
open.

## Expected line

```text
PASS_PRIME_POWER_MOAT_AND_MONOTONICITY_RECONNAISSANCE
```

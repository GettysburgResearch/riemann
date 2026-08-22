# X-90014 — Global prime-power moat finite base

Directed finite-base certificate for `L-90014`.

Run:

```bash
python experiments/X-90014-global-moat-base/certify.py
```

Expected line:

```text
PASS_GLOBAL_PRIME_POWER_MOAT_FINITE_BASE
```

The script constructs directed interval prefixes for

```text
d(m)=log rad(m)-log rad(m-1),
S_1/2(N), S_1(N),
theta_1/2(N), psi_1/2(N),
C_N=2S_1/2-theta_1/2+psi_1/2.
```

On each interval `(N,N+1)` it evaluates the exact maximum of

```text
D M(X)=C_N-2S_1(N)/sqrt(X)-2sqrt(X)
```

at the candidate prescribed by `L-90014`:

```text
sqrt(N), sqrt(S_1(N)), or sqrt(N+1).
```

All intervals `2<=N<2000` are certified negative. The least-negative upper
endpoint is below `-2.82842712474619`, at `N=2`.

The certificate covers only the finite base. `L-90012` supplies the analytic
tail `X>=2000`.

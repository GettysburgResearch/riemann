# X-9514 — Exact Volterra–virial totient regression

This standard-library checker verifies the finite-cell algebra in `L-9514` over
the formal ring

```text
Q[C],  C=1/zeta(2)=6/pi^2.
```

## Run

```bash
python verify.py --limit 64 --output results/verification.regenerated.json
cmp results/verification.json results/verification.regenerated.json
```

## Exact check

On each unit interval the analytic part is represented as

```text
A(x)=q0(x)+C*q1(x),
q0(x)=sum_(n<=m) phi(n)-x sum_(n<=m) phi(n)/n,
q1(x)=x^2/2.
```

The checker integrates exactly and verifies, coefficient by coefficient in
`Q[C]`,

```text
2 integral_1^N A(x)^2 dx
=
integral_1^N [E_phi(x)^2-x^2 f(x)^2] dx
+[x A(x)^2]_1^N
```

for every integer endpoint `2<=N<=64`.

The retained verdict is

```text
PASS_EXACT_L9514_VOLTERRA_VIRIAL_IDENTITY
```

and the proof-object SHA-256 is

```text
8c6a2dfa0425ff479c096519091babe922927bbd0637957d76e69e32422b58f5
```

## Proof boundary

The checker authenticates only the exact finite-cell identity. It does not prove
that the joint total-minus-arithmetic remainder is
`O_epsilon(X^(2+epsilon))`, and it does not prove RH.

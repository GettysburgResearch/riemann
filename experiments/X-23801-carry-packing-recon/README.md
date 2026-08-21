# X-23801 — Carry-packing exact algebra and reconnaissance

This experiment supports the finite carry-packing proposal of Issue #238.
It deliberately separates exact algebra from discovery-only asymptotics.

## Exact checks

Using only Python integers and `fractions.Fraction`, `verify.py` checks:

1. the closed carry formula against the floor-sum formula;
2. the affine Möbius transform
   ```text
   sum_(k<=n/m) mu(k) beta_(n,mk)=(2m-n-1)/(n+1);
   ```
3. the uniform finite lower bound
   ```text
   sum_(q<=n) beta_(nq)/q >= 1/16.
   ```

The retained run checks all relevant pairs through `n=50`:

```text
beta/floor identities       1225
Mobius affine identities    1225
minimum sum beta/q          1/6
```

## Reconnaissance only

The script also evaluates, in ordinary binary64 arithmetic:

- the exact-inverse coefficient formula through `X=10^5`;
- its weighted mass relative to `8 sqrt(X)`;
- the proposed row potential
  ```text
  sum_q (2-q^(-1/2)) beta_(nq) <= n
  ```
  through `n=5000`.

These values nominate the Greedy Carry Mass theorem and the pivot potential.
They are not directed, interval certified, or an all-order proof.

## Run

```text
python3 verify.py > results/verification.regenerated.json
```

The retained payload digest is

```text
360ec03a58044125a68fcf754e12277146420178c56c092ac43ca53aaa8579be
```

## Proof boundary

This experiment does **not** prove:

- positivity of the exact triangular inverse;
- the Greedy Carry Mass theorem;
- the proposed row-potential inequality for all `n`;
- a subpolynomial final residual potential;
- the Riemann Hypothesis.

Its exact part checks finite identities only. Its large-endpoint part is labelled
`BINARY64_RECONNAISSANCE_ONLY` in every output row.

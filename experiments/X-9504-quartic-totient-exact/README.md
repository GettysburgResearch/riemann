# X-9504 — Exact quartic totient/Bernoulli regression

This standard-library experiment verifies the finite algebra in `L-9508`.

## Run

```bash
python verify.py --limit 100 --output results/verification.regenerated.json
cmp results/verification.json results/verification.regenerated.json
```

## Exact checks

1. Direct finite quartic cell sums agree with the Bernoulli formula at five
   rational controls, including integer and noninteger endpoints.
2. For every integer `2 <= x <= 100`, direct exact evaluation of

   \[
   \frac1x\sum_{n<x}\frac{\varphi(n)}n(1-(n/x)^2)^2
   \]

   agrees with the exact finite Möbius/Bernoulli decomposition.
3. All arithmetic uses Python integers and `fractions.Fraction`.

The retained proof-object SHA-256 is

```text
b39d7cb81881d6fcf6abbb14f4d2fbb202535911e9640fdab487be93acdcf7f1
```

## Proof boundary

The verifier checks the finite algebra only. It does not prove the Mertens
estimate, the asymptotic error in `T-9502`, or RH.

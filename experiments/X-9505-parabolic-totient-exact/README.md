# X-9505 — Exact parabolic totient/Bernoulli regression

This standard-library experiment verifies the finite algebra in `L-9510`.

## Run

```bash
python verify.py --limit 100 --output results/verification.regenerated.json
cmp results/verification.json results/verification.regenerated.json
```

## Exact checks

1. Direct parabolic cell sums agree with the Bernoulli formula at five rational
   values, including integer and noninteger endpoints.
2. For every integer `2 <= x <= 100`, direct exact evaluation of

   \[
   \frac1x\sum_{n<x}\frac{\varphi(n)}n(1-(n/x)^2)
   \]

   agrees with the finite Möbius/Bernoulli decomposition.
3. All arithmetic uses Python integers and `fractions.Fraction`.

The retained proof-object SHA-256 is

```text
dd484b080dde97f31881a86af9c1031bb13548309d32b0ce9c042848b3d873b1
```

## Proof boundary

The verifier checks finite algebra only. It does not prove the Mertens estimate,
the asymptotic error in `T-9503`, or RH.

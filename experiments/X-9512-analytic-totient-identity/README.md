# X-9512 — Exact analytic-totient identity replay

This standard-library verifier checks `L-9512` over the formal affine ring

```text
Q[C],  C = 1/zeta(2) = 6/pi^2.
```

It does not numerically evaluate `pi`. For every exact rational input `x>=1`,
it independently constructs:

1. the finite parabolic Riesz state
   \[
   \sum_{n<x}\frac{\varphi(n)}n(x-n)-\frac C2x^2;
   \]
2. the Kaczorowski–Wiertelak analytic part
   \[
   \frac12\left(1+\sum_d\mu(d)\{x/d\}^2\right),
   \]
   with the infinite tail collapsed exactly to
   \[
   x^2\left(C-\sum_{d\le\lfloor x\rfloor}\frac{\mu(d)}{d^2}\right);
   \]
3. the Möbius floor identity
   \[
   \sum_d\mu(d)\lfloor x/d\rfloor=1.
   \]

Acceptance requires exact coefficientwise equality in `Q[C]`.

The retained deterministic grid has 72 integer and noninteger rational points.
Its proof-object SHA-256 is

```text
04f1e99374e955983c67b1414bdd412d6aee647899ca2fd66be6de48f1399ee1
```

Expected verdict:

```text
PASS_EXACT_L9512_ANALYTIC_TOTIENT_IDENTITY
```

## Proof boundary

The checker validates the finite algebraic identity only. It does not prove the
Mellin abscissa transfer, the critical energy estimate, or RH.

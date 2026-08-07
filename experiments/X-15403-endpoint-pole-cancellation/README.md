# X-15403 — Exact endpoint pole-cancellation regression

Status: exact finite synthetic regression; Riemann prime-window producer pending  
Agent: `gpt56-05-l`  
Issue: #154  
Claims: `L-15404`, `T-15402`

## Purpose

The scalar supersolution obstruction has an exponentially negative potential
mean. `L-15404` shows why this is not a negative Weil direction: endpoint prime
reflections have a zeta-pole main term which is the exact rank-one opposite of
the negative polar channel.

For a continuous profile, the identity is

```text
integral exp(-u/2) (phi*phi)(u) du
= |integral exp(-r/2) phi(r) dr|^2.
```

X-15403 verifies the finite rational analogue and keeps an arbitrary
pole-subtracted discrepancy separate from the cancelling main term.

## Synthetic control

Use

```text
profile       (1,-2,3)
laplace ratio 1/2
pole scale    7/3
```

The exact convolution is

```text
(1,-4,10,-12,9).
```

Therefore

```text
sum_u (1/2)^u convolution_u = 9/16
(sum_r (1/2)^r profile_r)^2 = (3/4)^2 = 9/16.
```

The retained prime-pole and polar terms are

```text
+21/8
-21/8,
```

and cancel exactly. A separate signed discrepancy row evaluates to

```text
-288/35.
```

This last number is a synthetic residual only. It is not a prime sum or a zeta
value.

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

Eight adversarial tests pass.

## Production object

A proof-grade endpoint packet must bind:

1. an exact rational spline profile;
2. exact same-end autocorrelations and endpoint convolutions;
3. every prime power with `log n<=R`;
4. every prime power in the moving terminal window
   `exp(2a-2R)<=n<=exp(2a)`;
5. the exact polar rank-one term;
6. cancellation-safe archimedean intervals;
7. a fixed rational vector and a strict final interval.

No prime power in the middle interval contributes to the endpoint packet.

## Proof boundary

The checker validates finite convolution algebra only. The PNT limit, smoothed
explicit formula, Suzuki normalization, and any Riemann-zeta sign require
independent analytic and numerical review.

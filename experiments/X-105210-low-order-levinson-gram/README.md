# X-105210 — Exact low-order Levinson Gram replay

This lightweight replay checks finite algebra behind `R-105201` and
`L-105206--L-105208`.

## Run

```bash
python3 experiments/X-105210-low-order-levinson-gram/verify.py \
  --output /tmp/x105210.json
cmp /tmp/x105210.json \
  experiments/X-105210-low-order-levinson-gram/results/verification.json
```

Expected verdict:

```text
PASS_X_105210_LOW_ORDER_LEVINSON_GRAM
```

## What is authenticated

Using exact `Fraction` arithmetic and Gaussian rationals, the checker verifies:

- the derivative-ladder quotient telescope;
- the exact correction
  `CRDB = off-real count + nonnegative coherence slack`;
- exterior-square feature Gram identities for symmetric finite positive
  Fourier packets;
- nonnegative quadratic forms and two-by-two Schur inequalities;
- linewise mean-orientation algebra for positive exponential tilts;
- the zero-Fourier-mode phase sum rule.

## What is not authenticated

The replay does not prove:

- the classical positive Fourier representation of Xi;
- the analytic passage from finite packets to Xi;
- the proposed natural-scale saddle theorem;
- a fixed-height argument or maximum-principle estimate;
- `HLOC105210`;
- the Riemann Hypothesis.

Arithmetic class:

```text
EXACT_GAUSSIAN_RATIONAL_FINITE_FOURIER_PACKETS
```

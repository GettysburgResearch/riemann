# X-92202 — Xi Schwarzian and order-two Loewner replay

Run:

```bash
python3 verify.py
```

Retained verdict:

```text
PASS_XI_SCHWARZIAN_ORDER_TWO
```

The standard-library replay checks the exact Gaussian-rational identity

```text
2 p' p''' - 3 (p'')^2
 = 6 sum_(a,b) w_a w_b (s_a-s_b)^2/((t+s_a)^4(t+s_b)^4),
```

the verified-height angle and domination margins, and a hostile conjugate-pole
cluster attached to a lower real anchor.

The replay checks finite algebra and numerical margins only.  It does not
certify the full zeta zero-product, the published external computations, the
analytic summation argument, `L-92202`, `T-92201`, or RH.

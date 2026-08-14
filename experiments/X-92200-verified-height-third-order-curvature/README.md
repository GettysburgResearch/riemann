# X-92200 — Verified-height third-order curvature replay

This standard-library replay checks the finite algebra and constant margins used by
`L-92200/L-92201`.

Run:

```bash
python3 verify.py
```

Retained verdict:

```text
PASS_VERIFIED_HEIGHT_THIRD_ORDER_CURVATURE
```

The replay checks:

1. the exact Gaussian-rational identity
   `p p''-2(p')^2 = sum_{a,b} w_a w_b (s_a-s_b)^2/((t+s_a)^3(t+s_b)^3)`;
2. the exact negative self-interaction of one conjugate off-line pair;
3. the published-height local-count gate;
4. the separated-pair and anchor-pair angle margins;
5. the domination inequality at
   `H=3,000,175,332,800`;
6. a hostile finite cluster of conjugate high poles coupled to one lower real anchor.

Immutable Git blob bindings at the retained branch state:

```text
verify.py                    791cdbc99f7c7cec5f04bcf5579dea3a7eab478c
results/verification.json    a7a47a02ca67bc88ef8d463155f9a45a8047c77d
```

## Boundary

The exact rational equalities and the printed numerical margins are finite checks.  The
replay does not certify:

- the centered Hadamard product and normal-convergence passage;
- the external Platt–Trudgian and Trudgian source results;
- the global angle/local-row proof for every zeta zero;
- the theorem `T-92200`;
- the Riemann hypothesis.

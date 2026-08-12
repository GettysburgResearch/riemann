# X-91530 — Compact dyadic pole-bridge replay

This finite replay supports `L-91530`, `L-91531`, `R-91530`, and the
normal-form part of `T-91530`.

It checks:

- the exact eta / finite-interval / residual-gamma factorization of the
  horizontal completed Xi quotient at three complex points;
- removal of both dyadic/gamma endpoint singularities;
- the compact Hardy norm formula for the pole bridge;
- the full-carrier tilt unitary on a four-carrier packet;
- positivity of the finite bridge Gram;
- growth of the analogous paired-eta tail multiplier on increasing
  truncations.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_COMPACT_DYADIC_POLE_BRIDGE
```

Selected controls:

```text
completed factorization error    5.31e-71
compact Hardy norm error         1.81e-71
carrier-unitary Gram error       5.55e-17
bridge Gram minimum eigenvalue   1.77e-8
eta-tail multiplier norm:
  N=10                           1.99
  N=10000                        9.76
```

The replay validates exact finite identities and numerical integral controls.
It does not construct the remaining eta-tail–beta/gamma graph map, prove EBOC,
or prove RH.

# X-91900 — Birman–Schwinger, covariant-flow and infinitesimal Pick replay

This finite replay supports:

- `L-91900` — abstract Birman--Schwinger/small-gain theorem;
- `L-91901` — safe-real Xi return operators;
- `L-91902/L-91903` — covariant connection identities and firewalls;
- `L-91904/L-91905` — infinitesimal Carathéodory criterion and the unconditional two-node theorem;
- `R-91900`--`R-91902` — the nonlocal-feedback, canonical-connection and three-node controls.

It checks:

1. the exact rank-one Friedrichs bound-state equation and threshold;
2. one three-node safe Xi Pick packet and its return singular values;
3. the indefiniteness of the canonical Cauchy-connection remainder on that sampled packet;
4. an exact rational strict-contraction control with indefinite instantaneous remainder;
5. positive two-node infinitesimal Xi matrices at three representative node pairs;
6. the exact negative determinant of the rational high-off-line three-node control;
7. the perturbation-determinant/feedback-entropy integral.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_BIRMAN_SCHWINGER_SPECTRAL_FLOW
```

The rational controls are exact.  The Xi packet evaluations are high-precision
finite diagnostics only.  The replay does not prove the universal safe-real
small-gain inequality, the completed skew connection, all-node infinitesimal
positivity, or RH.

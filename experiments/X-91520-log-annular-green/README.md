# X-91520 — Logarithmic annular Green replay

This finite replay supports `L-91520`, `L-91521`, and the normal-form part of
`T-91520`.

It checks on a synthetic nested right-half-plane zero packet:

- exact additivity of logarithmic Blaschke mass;
- the weighted nonlinear telescope recovered after exponentiation;
- the quantitative one-zero Green lower bound;
- the exact Green–Laplace representation of each zero charge.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_LOG_ANNULAR_GREEN
```

Selected controls:

```text
final logarithmic mass             0.012781524368417814
final hyperbolic mass              0.006431778589943663
maximum Green-Laplace error        1.05e-71
minimum quantitative-moat slack    8.64e-9
```

The zero packet is synthetic. The replay validates the model identities and
bounds; it does not identify the zeta arithmetic source log, prove LONAIE, or
prove RH.

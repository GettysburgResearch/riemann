# X-91420 — One-node annular exhaustion replay

This finite replay supports `L-91420`, `L-91421`, `R-91407`, and the model
bookkeeping of `T-91404`.

It checks:

- the exact nested-Blaschke annular telescope at one fixed interior node;
- nonnegativity of every annular increment;
- the Cauchy shift eigenvector and Hadamard parity identity;
- automatic one-node domination of the long odd port by the even port;
- the fixed-node Green alignment
  ```text
  Theta_a(1)=q_a H_(2a)(q_a), q_a=1/2-a;
  ```
- positivity of the explicit dyadic prime innovation
  `F(a)-F(2a)`.

The synthetic Blaschke packet is a model control, not zeta data.  The replay
does not construct the arithmetic source-to-model annular isometry and does
not prove RH.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_ONE_NODE_ANNULAR_EXHAUSTION
```
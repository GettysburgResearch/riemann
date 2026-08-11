# X-91014 — Source/scattering coefficient-one assembly

This replay checks finite identities behind `L-91014` through `L-91018`:

- exact generalized-Jordan coefficient cocycle;
- divisor-splitting probabilities and logarithmic coproduct;
- fixed-axis Cauchy all-pass first column and complex orthogonality;
- hyperbolic trace excess and Lyapunov depth integral;
- exact pole-residue and pole-subtracted sieve recurrence;
- finite positive-tail identity;
- physical two-port square and positive carrier Gram.

Run:

```bash
python3 verify.py --json /tmp/verification.json
```

Expected verdict:

```text
PASS_SOURCE_SCATTERING_COEFFICIENT_ONE_ASSEMBLY
```

The replay proves finite algebra and high-precision synthetic controls only. It does not prove the critical-boundary inherited-state intertwiner, the dyadic Cauchy-square gate, or RH.

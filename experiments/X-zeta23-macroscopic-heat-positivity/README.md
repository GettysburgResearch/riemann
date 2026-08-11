# X-zeta23-macroscopic-heat-positivity

Finite controls for the unconditional partial-sign theorem stacked on PR #379.

The replay checks:

- the centre-uniform paired-logarithm inequality;
- the scaled annulus lower bound producing `q^-3/2 log(1/q)`;
- superexponential small-`q` decay of the all-integer prime envelope;
- logarithmic growth of the positive gamma surrogate at fixed `q` and large centre;
- the elementary `O(1/q)` pole bound.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_MACROSCOPIC_FIRST_HERMITE_POSITIVITY
```

This finite diagnostic does not prove the global digamma estimate, Guinand--Weil, the diagonal growing-resolution sign, or RH.

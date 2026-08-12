# X-91026 — Canonical coisometry and norm-exhaustion equivalence

This exact finite regression checks:

- the four-term half-plane product-kernel decomposition;
- the positive rank-one formula for one crossed Blaschke pole;
- positive-semidefinite/rank-one port minors;
- exact critical-plus-stable norm exhaustion when the pole factor is constant;
- strict failure of exhaustion when a nonconstant pole factor is omitted.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_CANONICAL_COISOMETRY_EXHAUSTION_EQUIVALENCE
```

The replay proves finite rational model-space algebra only. It does not identify
the arithmetic tangent source with the model-space source, remove any actual
xi-zero port, or prove RH.

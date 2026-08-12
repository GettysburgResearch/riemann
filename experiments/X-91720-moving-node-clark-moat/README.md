# X-91720 — Moving-node Clark-moat replay

This finite replay checks:

1. the closed-form optimizing node;
2. equality of the optimized moat formulas;
3. the lower bound on a synthetic zero packet;
4. the resulting zero-count inequality;
5. the asymptotic `1/Y` scale.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_MOVING_NODE_CLARK_MOAT
```

The replay proves no source/model exhaustion and does not prove RH.

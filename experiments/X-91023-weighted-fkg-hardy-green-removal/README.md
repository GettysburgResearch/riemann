# X-91023 — Weighted FKG, Hardy squares, and Green removal

This replay checks:

- exact weighted Harris–FKG consequences for decreasing rational weights;
- the fixed symmetric-square conjugacy of the Cauchy all-pass;
- the general causal Hardy transfer and zero-mass identity;
- positivity of the exact Green-removal density on the first logarithmic cell;
- the explicit eventual-positivity threshold;
- discovery-only finite scans of the arithmetic boundary density.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_WEIGHTED_FKG_HARDY_GREEN_REMOVAL
```

The replay proves finite algebra and exact finite inequalities only. The
boundary-density scan is floating reconnaissance. It does not prove CJHI or RH.

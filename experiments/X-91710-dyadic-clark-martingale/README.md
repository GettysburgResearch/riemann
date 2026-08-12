# X-91710 — Dyadic Clark martingale replay

This finite replay checks:

1. the exact normalized Jordan cocycle;
2. the eight-section base-scale expansion;
3. positivity of one dyadic innovation Gram;
4. positivity of the innovation's real part;
5. zero entropy loss at a resonant prime atom.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_DYADIC_CLARK_MARTINGALE
```

The replay checks finite identities and diagnostics. It does not prove the
generationwise source-to-model map, DCAI, or RH.

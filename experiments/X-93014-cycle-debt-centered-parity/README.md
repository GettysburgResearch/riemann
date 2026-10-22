# X-93014 — Cycle-Debt centered parity replay

Arithmetic class: `EXACT_RATIONAL_AND_Q_SQRT2_WITH_FORMAL_RADICAL_SUPPORT`.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_93014_CYCLE_DEBT_CENTERED_PARITY
```

The replay checks exact finite centered/asymmetric dual fixtures, weighted-variation identities, the gauge-corrected dyadic source pairing in `Q(sqrt(2))`, doubled carry-column support, and hostile factor/sign mutations.

It does not prove the cofinal centered dyadic parity bound, polylogarithmic Cycle Debt, or RH.

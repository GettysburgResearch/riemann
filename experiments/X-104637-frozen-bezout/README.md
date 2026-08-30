# X-104637 — Frozen-carrier Bézout replay

Run:

```bash
python3 verify.py results/verification.json
```

Expected:

```text
PASS_L104637_FROZEN_CARRIER_BEZOUT
92f79f86099dd90aff8065576e1134bac6b4a681932910cb055d33c5e1591259
```

The replay proves the exact polynomial source-module identity and degree-six
bound. It does not promote the identity to model-space containment and does
not prove the fractional transport gate, more than ninety percent, or RH.

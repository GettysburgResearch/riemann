# X-106140 — Wick-centered family repair

Standard-library exact replay for:

- complete Gauss atomic weight ledgers;
- constant/mean-zero sign-pair operator decomposition;
- bilateral four-channel tensor decomposition;
- Wick normal ordering;
- Boolean half-source square;
- least-prime cutoff and two-square recurrence.

Run:

```bash
python3 verify.py
```

Expected verdict:

```text
PASS_X_106140_WICK_CENTERED_FAMILY_REPAIR
exact_checks=23035
proof_object_sha256=d4b5920eb5a4a68210ba2c22c9ed426de6ef9b46bc37749ef73947cd9a9e07ef
```

The replay does not prove `WCADD106140`, `WCKUM106140`, `BCI102990`, or RH.

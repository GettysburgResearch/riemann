# X-93017 - Cycle-Debt carry discrepancy

This lightweight exact replay supports `L-93017`.

It checks:

- the triangular carry-coordinate basis;
- exact split-defect discrepancies;
- exact target/objective pairing;
- small finite asymmetric-dual versus one-sided-discrepancy LP values;
- the centered baseline relation;
- nonpositivity of the `q=2` bottom contribution;
- the factor-one-half dyadic objective split;
- hostile mutations of the basis, inherited coefficient, and bottom sign.

Arithmetic is `fractions.Fraction` only. Vertex enumeration is restricted to
`X <= 6`.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_93017_CYCLE_DEBT_CARRY_DISCREPANCY
```

The replay does not prove OPB, polylogarithmic Cycle Debt, or RH.

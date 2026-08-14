# X-92110 — Projective passive-string gluing regression

Run:

```bash
python3 verify.py --json results/verification.json
```

Expected verdict:

```text
PASS_PROJECTIVE_PASSIVE_STRING_GLUING
```

The exact `Fraction` checks cover:

- the anchor-weight normalization used in the weak-* compactness proof;
- the continuous kernel-ratio identity `(r+s)/(z+s)`;
- a positive atomic truncation family and an exact geometric tail majorant;
- the firewall that arbitrary PSD packet matrices need not come from one scalar Cauchy/Stieltjes kernel.

The experiment does not construct the arithmetic Xi string and does not prove RH.

# X-19843 — Isolated interior CCM line firewall

This standard-library exact replay supports:

- `R-19848`: a parity-invariant exact CCM/Loewner matrix with a perfectly
  isolated simple even interior eigenline whose transform numerator is
  `z^2+1`;
- the finite Schur-complement arithmetic used in `L-19867`.

Run:

```bash
python3 verify.py > /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_ISOLATED_INTERIOR_CCM_FIREWALL
```

The replay uses only integers and `fractions.Fraction`.  It verifies finite
algebra; the general finite real-zero theorem and its scope are supplied by the
written proof and the cited CCM/Caratheodory--Fejer source.

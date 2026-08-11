# X-91001 — Fractional-part Li / Brun projector exact replay

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_X_91001_FRACTIONAL_PART_LI_BRUN
```

The script verifies only:

- `(1+z)Q_r(z)=1-z^r` for twenty even depths;
- 128 exact probability mixtures of even-depth Brun projectors;
- near-minimal ordered-factor bounds through depth seven on the factor-four diagonal;
- nine exact rational instances of the reciprocal-Li modulus identity;
- the elementary symbolic ingredients of the `3/4` safe-line bound.

It does **not** prove Diagonal Brun Positivity, the fractional-part moment bound, PIG, RH, or any assertion about actual zeta-zero data.

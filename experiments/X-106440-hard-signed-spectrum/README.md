# X-106440 — Hard-band signed-spectrum replay

Run:

```bash
python3 experiments/X-106440-hard-signed-spectrum/verify.py \
  --output experiments/X-106440-hard-signed-spectrum/results/verification.json
```

Expected classification:

```text
PASS_T106440_HARD_BAND_SIGNED_SPECTRAL_REDUCTION
```

The replay checks:

- the exact finite-circle formula
  `||H_U P_d||_HS^2=sum_m min(d,m)|u_(-m)|^2`;
- the corresponding complementary and signed trace split;
- the family `U_m=z^(-m)`, which has zero analytic numerator-difference
  Hankel energy but visible quotient energy `min(d,m)`;
- the visible/complement residue-kernel partition;
- the exact margins `73/1250` and `851/15000`.

It does **not** evaluate the actual Xi endpoint quotient, prove the visible
`1/600` estimate, prove `HARDSIGNED106440`, establish ninety percent, density
one, or RH.

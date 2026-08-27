# X-105380 — Xi origin source-moment layers

This standard-library replay authenticates the exact algebra in
`L-105380--L-105383`.

Run:

```bash
python -B experiments/X-105380-xi-source-moment-layers/verify.py \
  --output experiments/X-105380-xi-source-moment-layers/results/verification.json
```

Expected verdict:

```text
PASS_X_105380_XI_SOURCE_MOMENT_LAYERS
```

The checker performs 122 exact rational checks:

```text
30  odd tilted-law quotient coefficients and two determinants;
30  even regularized quotient coefficients and cotangent calibration;
32  low-order concentration implications;
30  tangent/cotangent Stieltjes moment coefficients.
```

The replay verifies the formulas

```text
odd:
  a_0=1,
  a_1=x/3,
  a_2=x^2/6-y/30,
  a_3=x^3/12-11xy/360+z_3/840;

even:
  a_0=(3-hx)/6,
  a_1=(15x-10hx^2+3hy)/360,
  a_2=(105x^2-42y-70hx^3+42hxy-3hz_3)/15120.
```

It also checks the sufficient source thresholds

```text
odd:  E[X^2]/E[X]^2 <= 35/27;
even: E[X]E[X^(-1)] <= 15/7.
```

These thresholds are not established for the actual Xi tilted laws by this
replay. Nor does it authenticate any critical-residue capacity estimate,
`CRVH105330`, `OSCC105371`, `BRP105220`, or RH. All conclusion-facing flags in
the stored result are false.

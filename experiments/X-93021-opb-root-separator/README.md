# X-93021 - OPB root separator

This lightweight exact/directed replay supports `R-93021` and `L-93021`.

It checks:

- the all-scale dyadic root floor identity;
- every quarter-balanced root split defect through endpoint 256;
- an exact rational primal/dual root-face fixture;
- an exact root-neutral Farkas counterexample;
- one symbolic and outward-directed positive full-target flow at `X=20`;
- the outward-directed actual separator `mathfrak B_40 > 1/200`;
- an exact symbolic and outward-directed positive interior flow for the minimally root-completed `X=40` target;
- five hostile mutations.

Arithmetic uses only the Python standard library:

```text
fractions.Fraction
decimal.Context with ROUND_FLOOR / ROUND_CEILING
integer carry matrices
```

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected classification:

```text
PASS_X_93021_OPB_ROOT_SEPARATOR
```

The replay does not prove CRCTP, OPB, Cycle Debt, or RH.

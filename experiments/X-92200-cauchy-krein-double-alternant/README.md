# X-92200 — Cauchy–Krein double-alternant replay

The checker verifies the all-order determinant identity in `L-92200` over
exact rational arithmetic for orders one through eight.

It also verifies the order-four Newton divided-difference reduction of
`L-92201` and checks the expected sign pattern on a finite Stieltjes control.

## Run

```bash
python3 verify.py --json /tmp/verification.json
cat /tmp/verification.json
```

Expected verdict:

```text
PASS_CAUCHY_KREIN_DOUBLE_ALTERNANT
```

The replay proves only finite algebra.  It does not establish the actual-Xi
order-four alternant signs or RH.

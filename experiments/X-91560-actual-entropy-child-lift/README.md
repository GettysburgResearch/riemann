# X-91560/61 — Actual entropy and child-lift repair

This standard-library replay checks the exact finite algebra behind:

- `R-91560`: the same-index typed child is not the affine Pascal lift;
- `R-91561`: `target - declared score` is not the actual row-entropy debt;
- `L-91560`: monotone same-index detail-target inclusion;
- `L-91561`: the coefficient collapse `K_m=log m` and the directed base bound at `67`.

Run:

```bash
python3 verify.py --json results/verification.json
```

The replay proves finite identities and directed inequalities.  The analytic
cell argument and the native producer composition remain written proofs to be
reviewed independently.

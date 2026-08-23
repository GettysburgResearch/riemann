# X-105323 — Derivative-invariant residue temperature replay

Run:

```bash
python -B experiments/X-105323-residue-temperature/verify.py \
  --output experiments/X-105323-residue-temperature/results/verification.json
```

Expected:

```text
PASS_X_105323_RESIDUE_TEMPERATURE
de47366ec7a4145b645cd864ca855fef228f7fb8b328d26602fba4c516a935e0
RH_UNPROVEN
```

The replay uses exact `Fraction` arithmetic on four monic real-rooted
polynomial derivative chains. It checks 20 identities:

- invariance of `V_2/[d(d-1)]` under monic differentiation;
- exact first-residue mass
  `A_d=(d-1)T/d`;
- exact adjacent ratio
  `A_(d-1)/A_d=d(d-2)/(d-1)^2`.

It does not replay canonical-product passage to Xi, positivity at a nonreal
level, the low-order inverse-curvature variance budget, the moving complex
saddle, or RH.

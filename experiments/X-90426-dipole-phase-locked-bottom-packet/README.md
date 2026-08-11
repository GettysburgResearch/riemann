# X-90426 — Dyadic dipole / phase-locked bottom-packet replay

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
```

The standard-library verifier uses exact `Fraction` arithmetic. It checks:

- factorization of the phase-locked source into the dyadic dipole and its critical adjoint;
- the complete two-row carry image of `omega_2`;
- the complete fourteen-row image of `b_*`;
- the exact piecewise formulas for rows `2,...,15`;
- vanishing of every row from `16` onward;
- prefix-potential cancellation;
- the aligned three-scale relation to the bottom charge.

It proves finite algebra only. It does not prove the critical-growth theorem or RH.

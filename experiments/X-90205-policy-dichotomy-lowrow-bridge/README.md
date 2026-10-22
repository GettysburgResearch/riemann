# X-90205 — Policy dichotomy and two-low-row bridge replay

Run:

```bash
python verify.py
```

The package checks:

1. the exact uniform Pascal hitting law;
2. the explicit Hurwitz-zeta deterministic transfer;
3. the row-two/row-three zero-safe symbol collapse;
4. the finite arithmetic source identity;
5. the exact Volterra bridge between critical-log and square-root-hinge low-row scalars;
6. the uniform continuum characteristic.

A successful replay prints

```text
PASS_X_90205_POLICY_DICHOTOMY_LOWROW_BRIDGE
```

This is a regression package for `L-90208/L-90209`. It does not certify the analytic simultaneous-approximation theorem, an eventual sign, SHARP, or RH.

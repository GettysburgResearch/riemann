# X-91306 — Covariant tail-Hankel completion replay

This finite replay supports `L-91306`, `L-91307`, `R-91301`, and `T-91301`.

It checks:

- the exact ordinary-prime scattering-score derivative on a finite Euler model;
- the nonconstant coefficient mismatch between the Jordan curvature and the
  Suzuki scattering score;
- the safe-scale bound `4(-zeta'/zeta(9/2)) < 85/196 < 1`;
- an exact rational tail-Hankel Julia/Pythagorean identity;
- its fully polarized bilinear form;
- exact finite Laurent/Hankel coefficient matching;
- a finite moving-unitary covariant-tangent identity.

The replay proves finite algebra and numerical analytic controls only. It does
not prove completed Fisher-curvature domination, identify the Julia auxiliary
with the full zeta screw defect, or prove RH.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_COVARIANT_TAIL_HANKEL_COMPLETION
```

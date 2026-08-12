# X-91306 — Covariant tail-Hankel completion replay

This finite replay supports `L-91306`, `L-91307`, `L-91313`, `L-91401`,
`R-91301`, `R-91402`, `T-91301`, and the corrected scope of `T-91302`.

It checks:

- the exact ordinary-prime scattering-score derivative on a finite Euler model;
- the nonconstant coefficient mismatch between the Jordan curvature and the
  Suzuki scattering score;
- the safe-scale bound `4(-zeta'/zeta(9/2)) < 85/196 < 1`;
- an exact rational tail-Hankel Julia/Pythagorean identity;
- its fully polarized bilinear form;
- exact finite Laurent/Hankel coefficient matching;
- a finite moving-unitary covariant-tangent identity;
- the vector-valued Fisher-Hankel score projection;
- the exact scalar-plus-orthogonal-auxiliary Pythagorean identity;
- failure of raw model-space delay invariance in a finite shift model;
- the exact compressed-delay decomposition `S_j=T_j+M_Theta R_j`;
- the compressed semigroup law for `T_j`;
- the leakage cocycle for `R_j`;
- the fully polarized mixed-delay Pythagorean identity.

The replay proves finite algebra and numerical analytic controls only. It does
not construct the renormalized map from the prime Poisson/Julia source to the
completed Fisher-Hankel source, identify its auxiliary with the delayed zeta
screw defect, or prove RH.

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

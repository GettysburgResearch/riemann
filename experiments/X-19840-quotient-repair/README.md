# X-19840 — Quotient-energy repair regressions

This packet checks exact/synthetic algebra used by the adversarial repair:

```bash
python3 experiments/X-19840-quotient-repair/verify.py
```

It verifies:

- the two exact signed source constraints for the displayed `d_4` and `d_6`
  vectors;
- that a tiny source-map singular value increases the induced quotient energy;
- the exact first/rest alias identity
  `|F+H|^2=1+(F*H+H*F)+|H|^2`;
- exact finite Mellin interpolation with the source-integral correction;
- the model first-versus-later radial phase separation;
- exact same-branch cancellation under complex displacement.

It does **not** verify:

- prolate/Hermite asymptotics;
- the exact radial Liouville coefficients;
- WKB or Airy error bounds;
- endpoint operator estimates;
- zeta local factorization;
- the growing source-rank theorem;
- the relative operator local-Weyl law;
- the CCM finite-real-zero theorem;
- RH.

Result class:

```text
EXACT_SYNTHETIC_QUOTIENT_REPAIR_ALGEBRA
```

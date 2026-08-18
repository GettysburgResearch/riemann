## Purpose

Continue PR #580 at exact head `812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05`
and sharpen its sole Q4 gate without claiming a cancellation theorem that has
not been proved.

## New mathematics

- Proves the lower side of SACF is automatic from `A^2=D+X_cross` and the
  polylogarithmic diagonal.
- Replaces absolute polylog SACF by the strictly weaker conclusion-producing
  condition `UOSACF: S_H(X)<=X^o(1)`.
- Compresses every exact band-pair common-divisor kernel into fifteen universal
  squarefree power-log moments and gives an exact lcm-based moment formula.

## Replay

```bash
python3 experiments/X-95510-one-sided-sacf/verify.py
```

Expected:

```text
PASS_T95510_ONE_SIDED_SUBPOWER_AND_MOMENT_COMPRESSION
```

## Boundary

```text
UOSACF                 OPEN / RH-BEARING
Riemann Hypothesis     UNPROVEN
```

# X-18508 — Exact deficit-projector bridge

This standard-library-only checker verifies the finite bridge from a declared
positive symbol deficit to its canonical high-deficit spectral augmentation.

The input binds

```text
G, D, Q0, theta, Y_D, Y_C, source_Y.
```

The consumer reconstructs

```text
G0 = Q0* G Q0,
D0 = Q0* D Q0,
```

and requires

```text
Y_C* G0 Y_D = 0,
Y_C* D0 Y_D = 0,
Y_D* (D0-theta G0) Y_D > 0,
Y_C* (theta G0-D0) Y_C > 0.
```

It then certifies `Q_D=Q0 Y_D` as the exact spectral range above `theta` and
checks whether the proposed source flag spans that same range.

The aligned control is certified as

```text
CERTIFIED_SOURCE_EQUALS_DEFICIT_CANONICAL
```

with verification SHA-256

```text
01028984231587ea44ce9502d323333ebe060cfe1490a81ec5c5c291c1a57708.
```

The same-rank misaligned control is certified as

```text
CERTIFIED_DEFICIT_CANONICAL_SOURCE_NOT_IDENTIFIED
```

with verification SHA-256

```text
69cf1b5e8e6ed0d603d65fc89dc0cfbaa289ef1536a5f2d4e43ce3a1670a225f.
```

Nine adversarial tests pass. No production Suzuki `D_lambda` is included; the
checker defines the exact trust boundary for the missing emitter.

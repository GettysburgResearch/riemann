# X-18509 — complete finite spectral deficit at `(c,N)=(10,2)`

This experiment consumes one actual X-18507 cutoff-free D-0001 primitive
matrix and emits the full finite lower-model packet

```text
G,D,g,Gamma,Q_0,Y_D,Y_C,P_D enclosure.
```

The key result is that the X-18507 source-valid flag is **not** the exact
high-deficit spectral range. The true rank-two canonical projector is enclosed
within `1e-52` in the declared `G`-operator norm, and the existing direct short
proves its finite block strictly positive.

## Run

```bash
python verify.py \
  certificates/c10-N2-p1024-primitive.json \
  config.json \
  --output results/c10-N2-verification.json

python compare_precisions.py \
  certificates/c10-N2-p768-primitive.json \
  certificates/c10-N2-p1024-primitive.json \
  --output results/precision-comparison.json

PYTHONPATH=. python -m unittest -v tests/test_verify.py
```

The primitive files contain every prime power through `10`, the complete pole
block, and the cutoff-free archimedean block.

## Trust boundary

The standard-library consumer uses only integers and `fractions.Fraction`. It
reconstructs every contraction, interval LDL pivot, source-cross refutation,
residual/projector radius, and direct-short floor. The exact spectral projector
is defined by functional calculus and enclosed around an emitted dyadic center.

## Scope

This is a complete finite spectral deficit. It is not an emitter for the global
infinite-dimensional symbol-deficit operator, and it proves no cofinal result.

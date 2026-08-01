# X-18507 — First real common profile-soft ledger

This experiment joins three already-reviewed production streams at one actual
cutoff-free D-0001 support:

1. the immutable MPFR-384 prime/pole/archimedean matrix from `X-18505`;
2. twenty proof-grade critical-line zero balls from `X-20702`;
3. the direct residual-short/LDL machinery of `L-18512` and PR #191.

The retained support is

```text
c = 5
N = 1
even coordinates = [e0, (e-1+e1)/sqrt(2)]
prime powers = 2, 3, 4, 5
```

## Actual source and profile objects

The finite source/localization map is the exact identity on the two even
coordinates. The certified `Q_E` column of X-18505 is used as the rational soft
coordinate and `Q_W` as the hard/ambient coordinate. Their exact metric Grams
are equal and their cross Gram is zero.

For each of the first twenty certified critical-line ordinates, the producer
reconstructs the exact D-0001 evaluation row and its logarithmic-support
derivative using 320-bit outward fixed-point arithmetic. It forms

```text
D = 2 sum v_gamma v_gamma^T
K = 2 sum (v_gamma v_gamma^T + dot(v_gamma) dot(v_gamma)^T).
```

Thus `D` is an actual finite zero-profile Gram and `K` is its amplitude/support-
derivative graph Gram. The graph LMI is certified by

```text
K <= M^2 G,
M^2 <= 23.182530707354535.
```

## Buffered soft export

At the exact rational threshold

```text
tau = 1/1000
```

the determinant of `D - tau G` is strictly negative, so exactly one generalized
eigenvalue lies below the threshold. The declared rational soft coordinate has

```text
D_soft/G <= 4.455631615505132e-5,
D_hard/G >= 0.1966252348022867,
projector graph-angle upper <= 0.009133890853533.
```

This is a fail-closed one-dimensional buffered soft export. It is not inferred
from a floating eigensolver.

## Complete Weil matrix and PR #191 direct short

The arithmetic block is bound byte-for-byte to

```text
experiments/X-18505-real-d0001-direct-block/
  certificates/c5-N1-p384.json
SHA-256 1fbbb15004dbfc2af84e6ab71d88ba7e8098535f88182236f9ee1eceb0d6e350
```

and therefore contains every prime power through `c=5`, the complete pole and
archimedean terms, and the certified MPFR tail enclosures.

For the profile-soft replay, the original positive `Q_W` block is the hard
ambient block and the original `Q_E` block is the soft low block. With

```text
h = 1/4,
m_soft = 1/100000,
trial solve X = 0,
```

the Fraction consumer proves

```text
C_hard - h G_hard > 0,
D_soft = A_soft - Z^2/(h G_hard),
D_soft - m_soft G_soft > 0.
```

Normalized directed lower endpoints are

```text
direct lower       > 5.28425779831317e-5
shifted LDL pivot  > 4.28425779831317e-5
exact Schur        > 5.28425873087804e-5
negative part      = 0
```

Verdict:

```text
CERTIFIED_FIRST_REAL_COMMON_PROFILE_SOFT_LEDGER
```

## Replay

```bash
python build_ledger.py \
  --certificate artifacts/certificate.json \
  --summary artifacts/summary.json
python verify.py artifacts/certificate.json \
  --repo-root ../.. \
  --output artifacts/verification.json
PYTHONPATH=. python -m unittest -v tests/test_verify.py
```

The workflow also reruns the original X-18505 arithmetic consumer and checks the
bound arithmetic SHA before accepting this ledger.

## Unbounded parameterization

The integrated producer extends without changing the finite algebra:

```text
c_j = ceil(exp(j)),
N_j = j,
K_j = ceil(4 j^2) certified line-zero rows,
all prime powers q <= c_j,
adaptive tau_j chosen in a directed generalized spectral gap.
```

At level `j`, X-18506 emits the source-canonical arithmetic block, the profile
producer emits the `K_j`-row `D_j/K_j` Grams and buffered soft graph, and the same
PR #191 consumer tests the final shifted LDL pivot. This is an explicit
unbounded production schedule; no claim is made here that every level passes or
that the finite zero-profile Gram is already the complete CCM/Suzuki profile
object needed by the cofinal RH theorem.

## Proof boundary

This is the first **real common calibration ledger**: source identity, directed
profile and derivative Grams, buffered soft export, complete zeta arithmetic,
and direct harmonic short all coexist in one proof object.

It is still the cutoff-free D-0001 finite hierarchy and uses a twenty-zero
profile Gram. It is not yet the complete augmented Suzuki/CCM growing profile
ledger, and it does not prove RH.

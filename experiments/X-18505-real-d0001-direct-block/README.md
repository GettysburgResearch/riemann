# X-18505 — First real D-0001 direct-complement artifact

This experiment is the first immutable, directed instance of the `L-18512 / T-18504`
shorting interface on non-synthetic zeta arithmetic.

It uses the cutoff-free D-0001 finite Weil block at

```text
c = 5
N = 1
sector = even
coordinates = [e0, (e_{-1}+e_1)/sqrt(2)]
prime powers = 2, 3, 4, 5
```

The producer emits, in one declared metric,

```text
Q_W, P_W, E_W, Z_W, C, X_N, R_N, G_W.
```

Here `P_even=W_02-W_r` is the cutoff-free pole/archimedean block,
`E_even=-W_p` contains every prime-power term through `c=5`, and
`Q_even=P_even+E_even` is the complete D-0001 matrix.

## Declared decomposition

The exact integer columns are

```text
Q_W = (116689468362578147411353556252846438487,
       170141183460469231731687303715884105728)^T

Q_E = (170141183460469231731687303715884105728,
      -116689468362578147411353556252846438487)^T.
```

They are Euclidean-orthogonal and have the same exact Gram

```text
G_W=G_E
=42564454336070175247068506510526655294049404524605727438921137001538557259153.
```

The trial harmonic solve is deliberately the exact finite choice

```text
X_N=0,
R_N=Z_W.
```

The ambient metric is `M=G_E`, with the directed coercivity choice

```text
h=1/100000.
```

## Directed verdict

The producer is replayed at MPFR-256 and MPFR-384. Both runs use outward arithmetic for every elementary operation,
300,000 terms for the complex digamma/trigamma series, and explicit analytic
bounds for both special-function tails and the geometric cutoff-free tails.

The exact `Fraction` consumer reconstructs every compression and proves

```text
C-hM > 0,
D_N = B_W-h^{-1} R_N^* M^{-1}R_N,
D_N-(1/4)G_W > 0.
```

Normalized directed intervals:

```text
C/G_E                    [5.2842803836373976e-5, 6.3010523376687320e-5]
D_N/G_W                  [0.26076162878924794, 0.26078326344080501]
LDL pivot / G_W          [0.01076162878924794, 0.01078326344080501]
exact Schur floor / G_W  [0.26076620660564458, 0.26078326344080501]
```

Therefore

```text
Delta_{c=5,N=1}=0
```

for this real finite block, with the stronger certified moat `m=1/4`.

## Independent replay

A separately written 100-decimal `mpmath` implementation evaluates the same
cutoff-free formulas using native `digamma`/`polygamma`. All eight primitive
`P_even/E_even` midpoint entries lie inside the 384-bit directed MPFR intervals.
All 32 higher-precision intervals are nested inside the corresponding 256-bit
intervals.
This replay is independent ordinary high precision, not a second directed
backend.

## Scope

This is an actual cutoff-free D-0001 zeta-data packet and closes the direct LDL
sign at one real finite support. It is **not** yet the complete augmented Suzuki
low hierarchy required for the cofinal RH theorem. The next production step is
to export the analogous objects for the canonical augmented packet and repeat
the same consumer; no further Schur algebra is needed.

## Replay

```bash
gcc -O2 -std=c11 directed_producer.c -lmpfr -lgmp -o directed_producer
./directed_producer > certificates/c5-N1-p256.json
gcc -O2 -std=c11 -DPREC=384 directed_producer.c -lmpfr -lgmp -o directed_producer_p384
./directed_producer_p384 > certificates/c5-N1-p384.json
python compare_precisions.py certificates/c5-N1-p256.json certificates/c5-N1-p384.json \
  --output results/precision-comparison.json
python verify.py certificates/c5-N1-p384.json \
  --output results/c5-N1-verification.json
python independent_mpmath_replay.py certificates/c5-N1-p256.json \
  --output results/independent-mpmath-replay.json
PYTHONPATH=. python -m unittest -v tests/test_verify.py
sha256sum -c SHA256SUMS
```

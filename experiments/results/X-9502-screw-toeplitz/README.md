# X-9502 screw FIR / Toeplitz artifacts

Classification: mixed `EMPIRICAL` reconnaissance and one directed positive
control.  No counterexample is claimed.

## Files

- `recon.json` — binary64 exact-resonance table, Toeplitz eigenmode, dyadic
  freeze, and binomial-filter values at `h=log(2)/3`, `n=53`.
- `p128.json`, `p192.json`, `p256.json` — directed MPFR primitive `Psi(kh)`
  rows and Rayleigh intervals for the same exact dyadic vector.
- `verification.json` — standard-library exact contraction, cross-precision
  nesting, and independent manifest recount.
- `zero-attribution-600.json` — approximate mpmath/binary64 attribution of the
  raw mode to the first 600 positive critical-line zeros.  This is search
  guidance only; none of those decimal ordinates is used as a certificate.
- `SHA256SUMS` — hashes of source and result artifacts.

## Exact directed case

```text
h                         = log(2)/3
matrix size               = 53
maximum sampled t         = 53 log(2)/3
prime-power cutoff        = 208063
exact threshold at row k  = q^3 <= 2^k
prime count               = 18640
prime-power count         = 18778
vector denominator        = 2^24
manifest SHA-256          = 18224939cfbd3d221695e8883e7eabf2d4201697ef6b154c0260b1b9e7cff0d2
```

The integer cutoff identity checked by both producer and verifier is

```text
208063^3 <= 2^53 < 208064^3.
```

The 256-bit producer interval is

```text
[1.928553622308640188310963997625878557364125578418042806481204260290997513959522403925111843e-05,
 1.928553622308640188310963997625878557364125578418042806481204260291025054537139777586645641e-05].
```

The independent checker contracts the outward decimal primitive rows with
exact `Fraction` arithmetic and obtains a nested strictly positive interval.
The verdict excludes only the committed vector.

## Build and reproduction

With development headers:

```bash
cc -O3 -std=c11 -Wall -Wextra \
  experiments/screw_toeplitz_mpfr.c \
  -o screw_toeplitz_mpfr \
  -lmpfr -lcrypto -lgmp -lm
```

The project container used the source's documented minimal ABI fallback
because the MPFR runtime was installed without `mpfr.h`:

```bash
cc -O3 -std=c11 -Wall -Wextra \
  experiments/screw_toeplitz_mpfr.c \
  -o screw_toeplitz_mpfr \
  -l:libmpfr.so.6 -lcrypto -lgmp -lm
```

Produce the three precisions:

```bash
./screw_toeplitz_mpfr 128 > p128.json
./screw_toeplitz_mpfr 192 > p192.json
./screw_toeplitz_mpfr 256 > p256.json
```

Verify:

```bash
python experiments/verify_screw_toeplitz_certificate.py \
  --recount-manifest \
  --json-out verification.json \
  p128.json p192.json p256.json
```

Reproduce the discovery freeze:

```bash
python experiments/screw_fir_toeplitz_recon.py \
  --step-prime 2 \
  --denominator 3 \
  --matrix-size 53 \
  --freeze-bits 24 \
  --json-out recon.json
```

The optional command

```bash
python experiments/screw_fir_toeplitz_recon.py --zero-count 600
```

recomputes the approximate zero-attribution experiment.  It uses
`mpmath.zetazero` and is intentionally outside the trusted proof boundary.

## Trusted-boundary note

The exact checker verifies the integer filter, autocorrelations, primitive-row
contraction, manifest count/hash, and cross-precision nesting.  It does not
independently reproduce MPFR logarithms, square roots, exponentials, or the
smooth explicit-formula series.  A future negative certificate must receive a
second directed special-function implementation; the present positive control
is not promoted beyond its finite scope.

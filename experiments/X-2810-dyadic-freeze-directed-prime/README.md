# X-2810 — Dyadic freeze and directed fixed-vector prime pilot

Experiment ID: X-2810  
Agent: `gpt56-01-d`  
Issue: #28  
Status: **certified finite positive pilot within the stated producer contracts; no counterexample**

## Research question

Can the exact proof architecture of PR #49 be exercised end to end on a real complete-prime carrier vector before launching the 4,118,082,969-term target?

The pilot answers **yes** at `c=10^8`, `K=1024`. It:

1. regenerates a complete-prime discovery vector;
2. freezes it to exact 96-bit dyadic coordinates;
3. computes exact Gaussian-dyadic autocorrelations;
4. evaluates every prime-power scalar term with directed MPFR arithmetic;
5. converts the outward endpoints to exact rational numbers;
6. composes them with the exact PR #49 correction formula;
7. obtains a strict positive full interval for this fixed vector.

This is a positive exclusion result, not evidence for RH and not a counterexample.

## Parameters and coverage

```text
cutoff c                 100000000 = 10^8
carrier T                4709203636353.65 = 94184072727073/20
cells K                  1024
vector fractional bits   96
MPFR precision           192 bits and independent 256-bit repeat
primes                    5,761,455
higher prime powers       1,404
total prime powers        5,762,859
```

No prime-density or tail approximation replaces the finite stream.

## Frozen vector

The discovery implementation uses complete prime coverage and the D-0801 Hermitian Toeplitz matrix. It fixes the global phase by making the largest-magnitude coordinate real and positive, then rounds real and imaginary coordinates independently to the nearest multiple of `2^-96`.

```text
vector SHA-256
ed06e5102a57d6446087ec1bb9fa60727b988877260eb5f5a668fea48d3e4133
```

Exact verification reconstructs the norm and all 1,024 autocorrelations using Python integers only. The autocorrelation fingerprint is

```text
08d1c5e0238041eaca009e9d66dfab8a94f2d73037d86f53c296c8cd07a44765
```

The crude exact L-2810 rounding bound for this pilot is `<1.858006488204201e-22` for the normalized leading Rayleigh value.

## Directed prime result

The MPFR producer evaluates the scalar formula of L-2811. Every logarithm, square root, multiplication, division, knot fraction, sine, cosine, and running sum is outward rounded. Sine and cosine are evaluated at a rounded midpoint and widened by the larger outward distance to either phase endpoint; this avoids assuming that a rounded midpoint is the exact interval center.

The 192-bit and 256-bit runs produced identical outward binary64 endpoints. Those endpoints are interpreted as exact dyadic rationals. The complete prime Rayleigh interval is approximately

```text
[4.3450780390771451, 4.3450780390771460]
```

and the alpha interval is approximately

```text
[4.3517199520883176, 4.3517199520883185].
```

Because the vector is not exactly unit length, the exact checker multiplies the alpha interval by the exact dyadic norm before subtraction.

## Exact final interval

The exact leading quadratic interval is approximately

```text
[0.006641913011173628, 0.006641913011175405].
```

The rational L-2803 correction radius for this vector is approximately

```text
4.760226693637145e-10.
```

Therefore the exact composed full interval is approximately

```text
[0.006641912535150959, 0.006641913487198074].
```

Its lower endpoint is strictly positive. Conditional on review of the producer and inherited normalization/correction lemmas, this rigorously excludes this fixed vector. It does not assert positivity for another vector, cutoff, or carrier.

## Files

```text
regenerate_freeze.py       complete-prime discovery and dyadic freezing
exact_vector.py            integer-only vector/autocorrelation routines
export_autocorr.py         exact common-scale Gaussian-integer export
directed_prime_shard.c     shardable directed MPFR scalar producer
mpfr_compat.h              official-header preference plus MPFR-4 fallback ABI
build_pilot_certificate.py exact-rational schema construction
verify_vector.py           exact vector and rounding-bound verifier
tests/                     algebra, digest, scalarization, and target bounds
results/                   compact manifests, intervals, hashes, and transcript
```

## Reproduction

```bash
python regenerate_freeze.py --cutoff 100000000 \
  --carrier 4709203636353.65 --cells 1024 --bits 96 \
  --segment-size 20000000 --output /tmp/pilot-vector.json

python export_autocorr.py /tmp/pilot-vector.json /tmp/pilot-autocorr.txt

gcc -O3 -std=c11 -I. directed_prime_shard.c \
  /path/to/libmpfr.so.6 -lgmp -lm -o directed_prime_shard

./directed_prime_shard \
  100000000 4709203636353.65 /tmp/pilot-autocorr.txt \
  20000000 0 5 1 /tmp/pilot-shard.json 192

python build_pilot_certificate.py /tmp/pilot-vector.json \
  results/mpfr-prime-c1e8.json /tmp/pilot-certificate.json

python -m unittest discover -s tests -v
```

The certificate is compatible with `riemann.piecewise-carrier-fixed-vector.v1` from PR #49.

## Proof boundary

Repository promotion still requires:

1. independent review of `directed_prime_shard.c` and its MPFR semantics;
2. an independent rerun or backend;
3. review of T-2801 and L-2803;
4. attachment of the T-2801 normalization fingerprint to production artifacts.

The target `c=10^11` vector is not reconstructed here because the complete Toeplitz coefficients from PR #44 were not retained. L-2810 proves that once regenerated, 80 dyadic fractional bits are sufficient; L-2811 and T-2810 make the 4,118,082,969-term proof pass scalar and shardable.

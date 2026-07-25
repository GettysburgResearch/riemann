# X-2805 — Directed fixed-vector prime shard producer

Experiment ID: `X-2805`  
Agent: `gpt56-04-c`  
Issue: #28  
Status: complete dual-precision target certificate; fixed vector certified positive
Date: 2026-07-23

## Question

Can every huge carrier phase and every fixed-vector prime-power contribution be
enclosed with directed rounding, while retaining the coverage-checked sharding
architecture needed for the `4,118,082,969`-term optimized carrier target?

## Complete production result

On 2026-07-25, `gpt56-07` regenerated the 50 missing discovery shards, froze a
96-bit replacement vector, and replayed all 50 ranges at both 192 and 256 bits.
Every precision pair overlapped and narrowed. The normalization-bound exact
checker returned:

```text
CERTIFIED_POSITIVE_FIXED_VECTOR
```

The correction-composed quadratic interval is approximately

```text
[+2.67235355540268630118e-4, +2.67236285346077990744e-4].
```

This rigorously excludes the frozen vector; it is not a counterexample and says
nothing universal about RH. The complete result, all 100 directed shards,
resource logs, hashes, and proof boundary are retained under
`results/target-c1e11/`.

## Producer

`directed_prime_shard.cpp` evaluates one exact dyadic vector over one declared
prime segment range. It uses GNU MPFR for:

- directed `log(p)` and `log(c)`;
- exact-rational carrier conversion;
- directed `sqrt(q)` and amplitudes;
- the huge phase `T*m*log(p)`;
- correctly rounded sine and cosine with internal argument reduction;
- outward interval arithmetic and accumulation.

A phase interval `[phi_-,phi_+]` is evaluated at `phi_-` and widened by its full
width using the global one-Lipschitz bounds for sine and cosine. This makes the
phase enclosure independent of any manually selected multiple of `2*pi`.

Support coordinates are also intervals. If one touches a cell knot, every
intersected affine autocorrelation piece is evaluated and hulled. A midpoint is
never silently rounded to one lag.

`prepare_autocorrelation.py` computes all vector autocorrelations exactly over
the common dyadic denominator and binds them to:

- the canonical vector digest;
- the fixed parameter digest used by L-2804;
- the D-0801 normalization digest.

The C++ producer fails if the normalization digest, decimal-power cutoff, or
total-segment formula differs from the reviewed values.

## Build

Requirements:

- a C++17 compiler;
- GMP development headers/library;
- GNU MPFR 4.2.2 or a reviewed later version.

Example:

```bash
g++ -O2 -std=c++17 directed_prime_shard.cpp \
  -lmpfr -lgmp -o directed_prime_shard
```

## Pilot reproduction

Prepare the exact autocorrelation manifest:

```bash
python prepare_autocorrelation.py \
  certificates/pilot-vector.json \
  --cutoff-power10 5 \
  --segment-size 20000 \
  --output pilot-autocorrelation.txt
```

Evaluate all five segments and the unique higher-power stream:

```bash
./directed_prime_shard \
  --manifest pilot-autocorrelation.txt \
  --start-segment 0 --end-segment 5 \
  --include-higher-powers \
  --precision 192 \
  --output pilot-192.json

./directed_prime_shard \
  --manifest pilot-autocorrelation.txt \
  --start-segment 0 --end-segment 5 \
  --include-higher-powers \
  --precision 256 \
  --output pilot-256.json
```

The retained pilot contains every prime and higher prime power through `10^5`:

```text
ordinary primes       9,592
higher prime powers     108
total terms           9,700
```

The 192-bit interval width is approximately `1.63459e-54`; the 256-bit width is
approximately `8.80868e-74`. The latter is strictly nested in the former. Both
contain the independently arranged 100-decimal value

```text
-0.1133099482610300093554196495233908192581057802956499386971708073912527014079675612886902217966347712
```

A separate complete `c=10^7` pilot enclosed all `665,134` terms at 192 bits.
The observed single-process runtime was about 10.4 seconds in the retained
container environment; this is a performance observation, not a proof claim or
a target-scale runtime promise.

## Target sharding

For the optimized target, use the same 5,000 segment indices and 50 shard ranges
as PR #44. Run each range twice, for example at 192 and 256 bits. Exactly one
range additionally uses `--include-higher-powers`.

Each output records:

- exact segment endpoints and term counts;
- vector, parameter, and normalization fingerprints;
- MPFR version and precision;
- knot-hull count;
- a maximum phase-width diagnostic;
- exact rational lower and upper endpoints from `mpfr_get_z_2exp`.

After overlap/width checks, embed one precision level's shard intervals in
`riemann.piecewise-carrier-fixed-vector.v1`, together with the X-2802 alpha
interval, and run the L-2804 checker.

## Tests

```bash
PYTHONPATH=. python -m unittest discover -s tests -v
```

The Python suite checks the exact autocorrelation manifest, parameter binding,
term counts, precision nesting, and independent pilot containment. The retained
C++ binary was built against system MPFR 4.2.2 and GMP; the source itself must
be rebuilt and independently reviewed on a proof platform.

## Proof boundary

The producer closes the directed phase and scalar-accumulation design. The
historical PR #44 vector remains absent, but a replacement vector and its full
regeneration input are now retained with the complete target run.

Any RH-level use of a future negative verdict would also require review of
T-2801 and an independent producer/backend reproduction.

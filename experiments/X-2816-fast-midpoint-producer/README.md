# X-2816 — Fast binary80/binary128 midpoint producer

Status: compiled synthetic implementation, exact global moat checker, and overlap controls; production K=1024 run pending  
Agent: `gpt56-05-h`  
Issue: #81  
Claims: L-2815--L-2818

## Purpose

X-2815 proves that the unfinished high ranges do not need per-prime logarithm or square-root evaluations. A fully outward MPFR interval implementation of every algebraic operation is valid, but its synthetic target-segment runtime remained close to the direct transcendental backend.

X-2816 uses a different proof architecture:

1. evaluate one **nearest midpoint** for every prime;
2. export every shard midpoint as an exact binary rational;
3. add one theorem-backed target-wide error moat exactly once.

The midpoint program uses:

- MPFR only for segment setup, roots of unity, and exact-dyadic conversions;
- binary80 for amplitudes, support interpolation, complex contractions, and pairwise sums;
- binary128 for segment-relative huge-phase arithmetic;
- the same `M=32768`, cubic phase grid;
- balanced binary-carry pairwise summation.

No transcendental function is called per prime.

## Arithmetic contract

The executable rejects a platform unless

```text
FLT_RADIX            = 2
LDBL_MANT_DIG        = 64
sizeof(long double)  = 16
rounding mode        = FE_TONEAREST
```

Build with

```bash
g++ -O3 -march=native \
  -frounding-math -ffp-contract=off -fno-fast-math \
  -std=gnu++17 fast_prime_shard.cpp \
  -lmpfr -lgmp -lquadmath -o fast_prime_shard
```

A production build must preserve the source digest, compiler version, target ABI, flags, MPFR version, and manifest fingerprints.

## Global moat

L-2818 audits the fixed straight-line program and proves a per-term binary80 allowance below

```text
4096 * 2^-64.
```

For fewer than `4.2e9` terms, balanced pairwise depth at most 64, and the existing phase/algebraic moats, `verify_fast_budget.py` proves by exact rational arithmetic

```text
term evaluation       < 1 / 1,070,000
pairwise summation    < 1 / 25,000,000,000
complete fast moat    < 1 / 1,000,000
```

Thus, after exact rational addition of all midpoint shards,

```text
prime value in [midpoint - 1e-6, midpoint + 1e-6].
```

This global moat is added once, not once per shard. Exact alpha and nonprime corrections are composed afterward by the existing X-2805/X-2801 checker.

## Synthetic target-sized control

A synthetic `K=4` manifest at the exact production cutoff and carrier was evaluated over segment `2800:2801`, containing `808,754` primes.

```text
fully directed algebraic runtime  7.96 s
fast midpoint runtime              0.79 s
observed ratio                    10.08 x
phase-boundary diagnostics             0
support-boundary diagnostics           0
```

The fast midpoint was

```text
-15345311203639713961 / 9444732965739290427392
```

and lay inside the independently produced directed algebraic interval

```text
[-65907609767319354715519624827,
 -65907609765831752896490379928]
/ 40564819207303340847894502572032.
```

The directed interval width was approximately `3.6672e-14`.

A second small-cutoff control compared the fast midpoint with the direct MPFR log/sqrt/sin-cos backend. The midpoint differed from the direct interval by approximately `1.41e-14`; the theorem-level `1e-6` moat contains it by a very large margin.

These are synthetic implementation controls, not Riemann-xi evaluations.

## Output schema

Each shard records:

- exact segment range and prime count;
- vector, parameter, and normalization digests;
- phase-grid and series orders;
- setup precision and MPFR version;
- arithmetic-contract string;
- exact binary-rational midpoint;
- exact binary-rational absolute-term-sum diagnostic;
- phase and support boundary diagnostics.

The midpoint schema deliberately does not claim to be an interval. The final assembler must add the unique hash-bound L-2818 moat.

## Reproduction

```bash
python verify_fast_budget.py
python -m unittest discover -s tests -v

# Production compiler command above, then:
./fast_prime_shard \
  --manifest ../X-2805-directed-prime-producer/results/target-c1e11/vector/target-autocorrelation.txt \
  --start-segment 2800 \
  --end-segment 2900 \
  --phase-grid 32768 \
  --setup-precision 192 \
  --output shard-2800-2900-fast.json
```

Before production use, run one range already available from the direct MPFR backend and require its directed interval to lie inside the fast midpoint plus the global moat.

## Production estimate

The synthetic target-sized segment took approximately `0.8` seconds on the recorded local environment. A linear single-core projection for the remaining 2,100 segments is about 28 minutes. This is scheduling evidence only; actual K=1024 runtime and host behavior must be measured and recorded.

## Proof boundary

- The exact global moat checker is complete algebra once L-2818's static operation audit and platform contract are accepted.
- The committed producer compiled and passed synthetic controls locally.
- It has not yet been run on the actual K=1024 autocorrelation object.
- The complete fixed-vector prime midpoint, correction-composed interval, and final sign remain pending.
- No counterexample or `Z-####` candidate is claimed.
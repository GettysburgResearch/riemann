# Session report — fast midpoint completion backend

Agent: `gpt56-05-h`  
Date: 2026-07-25  
Issue: #81  
Branch: `agent/gpt56-05-h/65-segment-algebraic-phase-grid`

## Objective

Turn the analytic segment-centered accelerator into an operational proof-compatible backend for the recovered production object

```text
c                  = 100000000000
T                  = 94184072727073 / 20
K                  = 1024
vector bits        = 96
vector SHA-256     = 3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297
normalization SHA  = 65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be
```

without requiring one outward MPFR transcendental evaluation for every one of the billions of ordinary primes.

## Moving production state

During this session, the primary direct PR #65 advanced repeatedly:

```text
initially observed direct coverage   0:2000 and 4900:5000
next checkpoint                      0:2800 and 4900:5000
latest checkpoint                    0:4400 and 4900:5000
```

At the latest checkpoint, only

```text
4400:4900
```

remains: 500 of 5,000 segments, exactly ten percent of the integer cover. The direct run is therefore now the shortest path to the first primary verdict. The new backend remains valuable as independent reproduction and as a fail-safe if the final direct ranges stall.

## L-2818: one midpoint plus one global moat

A fully directed algebraic implementation was valid but still performed many interval operations per prime. L-2818 instead audits one fixed straight-line midpoint program under the recorded arithmetic contract:

```text
binary radix                         2
long-double mantissa                 64 bits
long-double storage                  16 bytes
quad mantissa                       113 bits
basic arithmetic rounding            nearest
fast-math/reassociation/contraction disabled
```

The producer uses:

- MPFR for segment setup, roots of unity, and exact dyadic conversions;
- binary80 for amplitude, support interpolation, complex contractions, and pairwise sums;
- binary128 for segment-relative huge-phase arithmetic;
- the `M=32768,R=3` phase grid;
- balanced binary-carry pairwise summation.

The static range audit proves every ordinary-prime term has hardware midpoint error below

```text
4096 * 2^-64.
```

With fewer than `4.2e9` terms, pairwise depth at most 64, the exact phase-grid moat, the exact algebraic moat, and a conservative binary128 phase allowance, X-2816 proves

```text
complete fast-backend moat < 1e-6.
```

This moat is added exactly once after exact rational addition of all midpoint shards.

## Operational producer

`fast_prime_shard.cpp` was compiled locally with

```bash
g++ -O3 -march=native \
  -frounding-math -ffp-contract=off -fno-fast-math \
  -std=gnu++17 fast_prime_shard.cpp \
  -lmpfr -lgmp -lquadmath -o fast_prime_shard
```

The executable:

- rejects an incompatible long-double ABI or rounding mode;
- reads the same exact autocorrelation manifest as X-2805;
- binds vector, parameter, and normalization digests;
- uses one segment-centered log and reciprocal-square-root setup;
- uses binary128 segment-relative phase-grid selection;
- exports exact binary-rational shard midpoints;
- records absolute-sum and boundary-distance diagnostics.

## Target-sized synthetic control

A synthetic `K=4` autocorrelation was evaluated at the exact target cutoff, carrier, and segment `2800:2801` containing `808,754` primes.

```text
fully directed algebraic interval runtime   7.96 s
fast midpoint runtime                        0.79 s
observed ratio                              10.08 x
```

The fast midpoint

```text
-15345311203639713961 / 9444732965739290427392
```

lay inside the independently produced directed algebraic interval

```text
[-65907609767319354715519624827,
 -65907609765831752896490379928]
/40564819207303340847894502572032.
```

The directed interval width was approximately `3.6672e-14`. No phase-grid or support-knot near-boundary diagnostic was triggered.

A second small-cutoff control compared the midpoint against the original direct MPFR log/sqrt/sin-cos producer. The distance was about `1.41e-14`, far inside the theorem's global `1e-6` moat.

These controls are visibly synthetic. They validate code paths and proof architecture, not the production K=1024 sign.

## Exact hybrid assembler

`assemble_fast_certificate.py` accepts both schemas:

- directed interval shards from X-2805;
- exact midpoint shards from X-2816.

It fails closed unless it proves:

- contiguous exact segment coverage `0:5000`;
- exactly one higher-prime-power stream;
- exact global counts `4,118,054,813 + 28,156 = 4,118,082,969`;
- exact vector, parameter, and normalization fingerprints;
- exact fast algorithm parameters and arithmetic contract.

It adds the X-2816 moat once and emits a complete prime interval. Alpha and nonprime corrections remain a separate final composition through the existing X-2805/X-2801 checker.

## Validation

The branch includes:

- 4 exact moat tests;
- 3 synthetic overlap/data-boundary tests;
- 5 hybrid assembler fail-closed tests;
- local C++ compilation;
- two independent synthetic producer comparisons.

The assembler tests explicitly reject gaps, duplicate higher-power streams, arithmetic-contract mutation, and count mutation, and verify that the global moat is not multiplied by the shard count.

## Strategic conclusion

The production obstacle is no longer analytic truncation or backend design. The direct run now needs only five 100-segment shards. The fast backend demonstrates that a full independent midpoint reproduction is computationally practical after the primary verdict: the target-sized synthetic benchmark projects a short single-core pass, although actual K=1024 timing must be measured rather than assumed.

## Honest proof boundary

- No production K=1024 X-2816 shard has been generated.
- No complete `0:5000` prime interval has yet been assembled.
- No alpha/correction-composed sign exists.
- No counterexample or `Z-####` candidate is claimed.
- A future strict negative still requires independent reproduction and adversarial review of T-2801 before unconditional RH-disproof promotion.

## Immediate next action

Finish direct ranges `4400:4900`, assemble the complete 192-bit interval, and compose exact alpha and nonprime corrections. Then run X-2816 on one or more complete ranges—or the whole target—as independent reproduction of the first verdict.
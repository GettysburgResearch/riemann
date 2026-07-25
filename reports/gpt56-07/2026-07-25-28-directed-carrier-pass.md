# Complete dual-precision directed carrier pass

Agent: `gpt56-07`  
Issue: #28 / #42  
Branch: `cursor/pr49-directed-carrier-pass-7f09`  
Date: 2026-07-25

## Starting hypothesis

The missing `c=10^11`, `K=1024`, `T=4709203636353.65` result could be
decided by regenerating the complete X-0801 coefficient stream, freezing a
replacement vector exactly, and replaying every prime-power term with PR #49's
directed MPFR producer and exact correction composition.

## Approaches attempted

1. Inspected every remote branch and available Actions artifact. The historical
   PR #44 vector and complete X-0801 shards were not present.
2. Began an 80-bit simultaneous-coefficient fallback, then stopped it when the
   full production protocol was supplied. That fallback did not satisfy the
   requested PR #49 vector schema and 192/256-bit replay contract.
3. Checked out PR #49 as the stacked base and ran focused tests for X-0801 and
   X-2801 through X-2805. A stale test-fixture import was repaired; all 75
   focused tests then passed.
4. Regenerated all 50 X-0801 discovery shards over segment ranges
   `[100i,100(i+1))`, segment size `20,000,000`, with higher powers in shard
   zero only.
5. Froze and bound a 96-fractional-bit Gaussian-dyadic replacement vector, then
   generated its exact autocorrelation manifest.
6. Built `directed_prime_shard_fast.cpp` against GNU MPFR 4.2.2 and GMP 6.3.0.
   The official MPFR archive signature was verified and all 198 upstream MPFR
   tests passed.
7. Ran all 50 directed ranges at 192 bits and immediately assembled the exact
   checker result.
8. Repeated every range at 256 bits. Every paired interval overlapped, and every
   256-bit width was no larger than its 192-bit counterpart.
9. Assembled the intersected dual-precision certificate and reran the
   normalization-bound exact checker.

## New results

Certified computational fact for this finite vector:

```text
verdict = CERTIFIED_POSITIVE_FIXED_VECTOR
```

The exact correction-composed quadratic interval has approximate display

```text
[+2.672353555402686301179777537247481857e-4,
 +2.672362853460779907438812865701168062e-4].
```

Its lower endpoint is strictly positive. The prime-power stream contains
exactly:

```text
4,118,054,813 ordinary primes
       28,156 higher prime powers
4,118,082,969 total terms
```

The 96-bit vector digest is:

```text
3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297
```

The empirical replacement-vector discovery margin was
`+2.691184519925116e-4`; it was used only for selection and not for the exact
sign decision.

## Candidate counterexamples

None. This computation excludes the supplied exact frozen vector. It does not
support an RH counterexample and does not establish RH.

## Certified computations

- 50 complete discovery ranges with exact coverage/count metadata.
- Exact 96-bit dyadic vector and exact autocorrelations.
- 50 directed 192-bit scalar intervals.
- 50 directed 256-bit scalar intervals.
- Pairwise overlap and precision narrowing for all 50 ranges.
- Exact alpha composition, exact L-2803 correction widening, and strict
  rational sign classification.
- Canonical normalization fingerprint:
  `65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be`.

## Failed approaches

- The original PR #44 vector could not be recovered because it was never
  committed.
- The initial one-pass 80-bit fallback was stopped after the stricter PR #49
  dual-precision protocol became available.
- Ubuntu's MPFR 4.2.1 package was below PR #49's reviewed requirement. A signed
  MPFR 4.2.2 source build replaced it before any retained directed shard ran.

## Potential errors and proof boundary

- The exact checker certifies finite interval composition and declared segment
  coverage. It does not independently prove producer correctness.
- An independent backend reproduction is still required.
- T-2801, D-0801 admissibility, and the Guinand--Weil normalization require
  independent theorem-level review before any RH-level implication.
- The positive result applies only to this frozen vector and finite carrier
  object.

## Files changed

Primary artifacts are under:

```text
experiments/X-2805-directed-prime-producer/results/target-c1e11/
```

Review first:

1. `final/run-summary.json`
2. `final/verdict-dual-p192-p256.json`
3. `final/certificate-dual-p192-p256.json`
4. `vector/frozen-vector-b96.json`
5. `directed-192-SHA256SUMS`
6. `directed-256-SHA256SUMS`
7. `build/build.log`

## Claims affected

- `X-2804`: instantiated with a complete replacement vector.
- `X-2805`: complete dual-precision production run, certified positive for the
  fixed vector.
- No `Z-####` claim was created.

## Recommended next actions

1. Reproduce all directed shards with an independent implementation or
   arithmetic backend.
2. Independently audit the exact vector digest, autocorrelation convention,
   phase sign, and correction composition.
3. Treat this carrier cell as a rigorously closed positive near miss and direct
   future search effort to a new vector/cell rather than promoting it.

## Organizational improvement ideas

Long computations should commit hash-bound shard checkpoints as they complete.
Discovery runs must preserve either all coefficients or the exact selected
vector before temporary data are removed. Production manifests should also pin
the minimum reviewed special-function library version, not merely the library
name.

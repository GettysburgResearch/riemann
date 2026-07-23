# X-2813 — Full directed `c=10^11` Toeplitz target

Experiment ID: `X-2813`  
Agent: `gpt56-01-e`  
Issue: #28  
Status: active proof-production run; no counterexample claim before the final exact interval

## Purpose

This experiment executes the full production chain for

```text
c = 100000000000
T = 4709203636353.65 = 94184072727073/20
K = 1024
```

without depending on the uncommitted historical PR #44 eigenvector.
`L-2812` permits one complete directed pass to produce simultaneous boxes for
all 1,024 Toeplitz lags.  Only after those boxes exist does the merge job:

1. assemble the midpoint Hermitian Toeplitz matrix;
2. select its leading vector;
3. fix its global phase and round it to 96-bit Gaussian dyadics;
4. contract the same simultaneous boxes exactly against that vector;
5. multiply the exact `L-2805` carrier interval by the exact vector norm;
6. subtract the complete prime interval;
7. widen by the exact `L-2803` correction radius;
8. make a strict rational sign decision.

## Complete coverage

The workflow uses the original fifty half-open integer ranges with segment size
`2,000,000,000`.  Matrix job `j` covers segment `[j,j+1)`.  Exactly shard zero
also enumerates every higher prime power `p^a <= c`, `a>=2`.

The merge job fails unless it receives:

```text
4,118,054,813 primes
28,156 higher prime powers
4,118,082,969 total prime-power terms
```

with contiguous segment indices `0,...,49`, common parameters, no ambiguous
support lag, and exactly one higher-power stream.

## Directed arithmetic

Each shard uses MPFR with 80-bit working precision.  Every logarithm, square
root, division, support position, huge phase, sine, cosine, hat deposit, and
coefficient accumulation is outward rounded.  Each final MPFR lag endpoint is
rounded outward once more to IEEE-754 binary64 and then interpreted by the
merge job as an exact dyadic rational.

A complete `c=10^8` calibration gave a selected-vector coefficient-box width of
about `5e-8` at this precision.  The target run is accepted only if the final
rational interval is strictly signed.  `UNRESOLVED` is a fail-closed outcome and
requires a higher-precision rerun.

## Logical boundary

A strict negative final interval supplies the finite analytic object required
by the carrier-Weil route.  Its RH implication still requires the independent
admissibility and Guinand--Weil normalization review recorded in T-2801 and the
project claim registry.  A strict positive interval rigorously excludes the
post-selected vector and closes this numerical basin; it is not evidence for
RH outside the supplied finite object.

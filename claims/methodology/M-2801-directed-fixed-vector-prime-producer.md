# M-2801 — Directed fixed-vector prime producer protocol

Proposal ID: M-2801  
Title: Proof-producing segmented evaluation of a frozen D-0801 vector  
Status: PROPOSED  
Authoring agent: `gpt56-04-c`  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801; L-0801; L-2804  
Scope: the remaining analytic producer for Issue #28

## Problem with the current process

The optimized carrier search has complete integer coverage metadata, but its
huge phases, accumulation, vector, and eigensolve are ordinary numerical
objects. Re-running a full interval matrix eigensolver would be unnecessarily
expensive and would mix discovery with proof. A fixed-vector certificate needs
only one scalar interval per prime shard.

## Proposed producer

### 1. Freeze the discovery vector

Export the selected `K`-component complex vector to dyadic coordinates:

```text
scale_bits
real_numerators[K]
imag_numerators[K]
```

The proof evaluates this rounded vector itself. No perturbation theorem is
required merely to preserve the discovery eigenvector: a different exact vector
is acceptable if its recomputed complete interval has the desired sign.

Compute its canonical SHA-256 digest exactly as X-2801 does. Every shard must
carry that digest.

### 2. Precompute exact dyadic autocorrelations

For `0<=d<K`, compute

\[
 a_d=\sum_{j=0}^{K-1-d}x_{j+d}\overline{x_j},
 \qquad a_K=0,
\]

using exact integer arithmetic over the common dyadic denominator. These values
are shared read-only input to every shard.

### 3. Enumerate the complete finite source

Use a segmented sieve over a declared integer partition of `[0,c]` for ordinary
primes. Generate all higher powers `p^m<=c`, `m>=2`, in exactly one separately
flagged shard. Every shard records:

- half-open segment range;
- prime count;
- higher-power count;
- total count;
- vector and parameter digests;
- numerical backend and precision;
- directed scalar interval.

The merger must reject gaps, overlaps, parameter drift, mixed vectors, and any
number of higher-power streams other than one.

### 4. Evaluate one term with balls

For `q=p^m`, define

\[
 u=\log q=m\log p,
 \qquad r=\frac{Ku}{L},
 \qquad b_q=\frac{\log p}{\pi\sqrt q}.
\]

The fixed-vector prime term is

\[
 b_q\operatorname{Re}\left(
 e^{-iTu}\{(1-f)a_d+fa_{d+1}\}
 \right),
\]

where `d=floor(r)` and `f=r-d`.

A rigorous producer must enclose `log p`, `u`, `L`, `r`, `b_q`, the complex
phase, and the final real product with directed balls.

#### Knot rule

A ball for `r` may not be rounded to one integer lag unless it lies wholly
inside one open knot interval. If it intersects an integer:

1. increase precision until the side is resolved; or
2. evaluate both adjacent linear pieces on their intersected subintervals and
   hull the results.

At the support endpoint `r=K`, use the exact zero overlap.

#### Huge-phase rule

Do not compute `T*u` in binary64 and reduce it manually. Use a ball library
whose sine and cosine routines include certified argument reduction for the
entire phase ball. Record the library and version in every shard.

### 5. Accumulate scalar intervals, not matrices

For the frozen vector, sum term balls directly into one real shard interval for
`x^*S_r x`. This avoids `K^2` matrix storage and an interval eigensolver. Use a
balanced or library-native ball sum and precision escalation until the shard
width meets its assigned budget.

### 6. Certify the leading scalar

Independently enclose

\[
 \alpha(T)=\frac{\log(T/(2\pi))}{2\pi}.
\]

Export one rational/dyadic interval. X-2801 multiplies it by the exact vector
norm squared.

### 7. Merge with the exact checker

Inline or collect the shard intervals in

```text
riemann.piecewise-carrier-fixed-vector.v1
```

and run `verify_fixed_vector_certificate.py`. The checker recomputes the
L-2803 correction radius and emits positive, negative, or unresolved.

## Precision escalation

Run at two increasing ball precisions. A shard is retainable only when:

1. both output intervals overlap;
2. the higher-precision interval is no wider than the declared shard budget;
3. knot classifications are stable or explicitly hulled;
4. term counts and digests are identical;
5. no exception, indeterminate ball, or non-finite endpoint occurred.

At the optimized target, the empirical margin is much larger than the
`1/2000000000` correction gate. The producer should still use a user-declared
width budget rather than infer safety from that decimal.

## Producer/checker separation

The producer may depend on Arb or another audited ball library. The checker must
remain standard-library exact arithmetic and must not call the producer's
special-function code. A genuine negative should be reproduced with a second
backend or implementation before candidate promotion.

## Expected benefit

- removes the interval eigensolver from the proof path;
- makes billions of terms shardable;
- binds every shard to one exact vector and parameter set;
- exposes knot and phase failures instead of silently rounding them;
- allows a compact exact checker to decide the final quantitative sign.

## Possible cost or risk

- complete interval enumeration through `10^11` is computationally expensive;
- overly wide phase balls can destroy the margin;
- a shared library defect can affect every shard;
- segment coverage metadata does not itself prove correct sieve code;
- the logical normalization and admissibility gates remain separate.

## Trial procedure

1. Validate at `c=10^5` against direct high-precision summation.
2. Reproduce a small ordinary X-0801 cell with both midpoint and ball output.
3. Freeze the PR #44 target vector and run several independent segments.
4. Measure width growth and set a global error allocation.
5. Complete the coverage-checked stream only after the pilot intervals are
   comfortably narrower than the target moat.

## Success criterion

A complete certificate accepted by X-2801 whose full exact interval is strictly
separated from zero, followed by independent analytic and numerical review.

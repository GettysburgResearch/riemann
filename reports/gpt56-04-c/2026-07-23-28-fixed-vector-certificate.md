# Agent continuation report — sharded fixed-vector carrier certificate

Agent: `gpt56-04-c`  
Issue: #28  
Branch: `agent/gpt56-04-c/28-piecewise-carrier-exact-corrections`  
Date: 2026-07-23

## Starting point

L-2801 through L-2803 reduced the omitted D-0801 source corrections to an exact
operator moat below `1/2000000000` at the optimized PR #44 target. The remaining
quantitative proof obligation was a directed interval for one complete-prime
fixed-vector value.

## Work completed

1. Proved L-2804, the exact interval-composition theorem for a frozen dyadic
   complex vector.
2. Defined schema `riemann.piecewise-carrier-fixed-vector.v1`.
3. Implemented `verify_fixed_vector_certificate.py` using only integers,
   `fractions.Fraction`, JSON, and SHA-256.
4. Bound every shard to one canonical vector digest and one parameter digest.
5. Added contiguous segment-coverage checks with gap and overlap rejection.
6. Required exactly one separately flagged higher-prime-power stream.
7. Required exact prime/higher/total count identities per shard.
8. Composed the alpha interval, scalar prime intervals, exact vector norm, and
   L-2803 correction radius into one full exact quadratic interval.
9. Added strict positive, strict negative, and unresolved verdicts.
10. Added twelve adversarial tests and synthetic positive, negative, and
    zero-touch fixtures.
11. Recorded M-2801, a fail-closed Arb producer protocol.

## New result

A real analytic producer can now emit only scalar fixed-vector shard intervals;
it does not need an interval matrix or interval eigensolver. Discovery may use
ordinary linear algebra to choose a vector, but proof evaluates the rounded
exact vector itself.

The checker rejects:

- segment gaps and overlaps;
- vector or parameter drift;
- duplicated or missing higher-power streams;
- count mismatches;
- zero vectors;
- booleans masquerading as integer counts;
- and any final interval meeting zero.

A synthetic strict negative passes only after the exact L-2803 correction moat
is included. The synthetic object is not a Riemann candidate.

## Candidate counterexamples

None. No real vector or analytic prime interval has been supplied. No `Z-####`
identifier is allocated.

## Certified computations

The checker arithmetic and synthetic outputs are exact finite computations.
The analytic provenance of a future shard interval remains outside the checker
and must be proved by its producer.

## Missing artifact

The optimized PR #44 `c=10^11`, `K=1024` discovery vector is not preserved in a
committed machine-readable artifact visible to this branch. It must be exported
before the target can enter the proof pipeline.

## Recommended next actions

1. Ask the PR #44 agent to commit the vector as dyadic coordinates or at least a
   high-precision decimal source plus rounding policy.
2. Independently recompute the vector if the original is unavailable.
3. Implement M-2801 with Arb/python-flint or another audited ball backend.
4. Pilot on small cutoffs and compare midpoint results with X-0801/X-0901.
5. Run the 50 coverage segments at `c=10^11`, carrying exactly one higher-power
   stream.
6. Merge through the exact checker.
7. Submit any strict negative first as a proposed candidate pending logical-gate
   review and independent numerical reproduction.

## Organizational improvement

Discovery PRs should preserve every retained minimizing vector. A small vector
artifact is often more valuable than a large matrix summary because it makes a
fixed-vector proof pass possible without rerunning the entire eigensolve.

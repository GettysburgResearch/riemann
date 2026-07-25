# Integrator patch — gpt56-05-h / Issue #81

Append-only, merge-order-aware proposal. It does not edit concurrent root registries.

## CLAIMS.md additions

```text
L-2815 | PROPOSED | Segment-centered atanh enclosure of log(q) | gpt56-05-h | L-2806; L-2813
L-2816 | PROPOSED | Segment-centered reciprocal-square-root enclosure | gpt56-05-h | L-2815
L-2817 | PROPOSED | Certified nearest phase-grid assignment and fallback | gpt56-05-h | L-2813; L-2815
M-2815 | PROPOSED | Hybrid direct/algebraic completion of c=10^11 pass | gpt56-05-h | L-2804; L-2813--L-2817
X-2815 | exact rational bound checker plus empirical regression | gpt56-05-h | L-2815; L-2816
```

## CURRENT_STATE.md proposed addition

```text
The exact PR #65 production vector and normalization are recovered. Direct 192-bit MPFR shards are committed for ranges 0:2000 and 4900:5000. The remaining high ranges admit a rigorous segment-centered accelerator: four odd atanh terms enclose log(q), a degree-five binomial encloses q^-1/2, and the M=32768,R=3 phase grid removes per-prime trigonometric calls. X-2815 proves the entire algebraic truncation moat below 1/90e12 and the phase-grid-plus-algebraic moat below 1/19.995e9, less than one quarter of the 2.5e-10 nonprime gate. Production implementation and the final sign remain pending.
```

## OPEN_PROBLEMS.md addition

```text
Q-2815 — Implement and overlap the segment algebraic phase-grid backend

Implement the L-2815--L-2817 backend for one complete target range. Require an outward interval overlapping the direct MPFR producer, exact term-count equality, unique-bin/fallback counters, and matching vector/parameter/normalization fingerprints. If successful, complete ranges 2000:4900 and assemble the final PR #65 certificate.
```

## NEGATIVE_RESULTS.md addition

```text
The exact acceleration-budget theorem is not a production sign. The current GitHub-hosted completion workflow remains queued or fails before step execution. No missing range has yet been replaced by an accelerated directed shard.
```

## Dependency edges

```text
L-2813,L-2806 -> L-2815
L-2815 -> L-2816
L-2813,L-2815 -> L-2817
L-2804,L-2813,L-2814,L-2815,L-2816,L-2817,T-2801 -> M-2815
L-2815,L-2816 -> X-2815
```

## Immediate handoffs

1. PR #65: preserve all committed direct shards; do not restart completed ranges.
2. PR #73: use X-2815's algebraic evaluator underneath the existing phase grid.
3. PR #74: if hosted execution begins and completes first, retain it as the direct verdict and use the accelerated backend for independent reproduction.
4. PR #79: once complete lag boxes or a strict fixed-vector interval exist, continue postselection only from hash-bound source intervals.
5. Integrator: keep the exact analytic moat distinct from implementation correctness and the eventual final sign.

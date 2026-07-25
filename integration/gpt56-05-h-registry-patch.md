# Integrator patch — gpt56-05-h / Issue #81

Append-only, merge-order-aware proposal. It does not edit concurrent root registries.

## CLAIMS.md additions

```text
L-2815 | PROPOSED | Segment-centered atanh enclosure of log(q) | gpt56-05-h | L-2806; L-2813
L-2816 | PROPOSED | Segment-centered reciprocal-square-root enclosure | gpt56-05-h | L-2815
L-2817 | PROPOSED | Certified nearest phase-grid assignment and fallback | gpt56-05-h | L-2813; L-2815
L-2818 | PROPOSED | Binary80/binary128 fast-midpoint global moat below 1e-6 | gpt56-05-h | L-2813--L-2817
M-2815 | PROPOSED | Hybrid direct/accelerated completion of c=10^11 pass | gpt56-05-h | L-2804; L-2813--L-2818
X-2815 | exact rational analytic-budget checker plus empirical regression | gpt56-05-h | L-2815; L-2816
X-2816 | compiled fast midpoint producer, exact moat checker, and hybrid assembler | gpt56-05-h | L-2818; X-2805
```

## CURRENT_STATE.md proposed addition

```text
The exact PR #65 production vector and normalization are recovered. Direct 192-bit MPFR shards now cover 0:4400 and 4900:5000, leaving only 4400:4900 (500 of 5000 segments). L-2815--L-2817 prove a segment-centered algebraic/phase-grid accelerator whose analytic moat is below 1/19.995e9. L-2818 and X-2816 provide a faster proof architecture: one binary80/binary128 midpoint pass plus an exact target-wide moat below 1e-6. The compiled producer was approximately 10x faster than the fully directed algebraic prototype on a target-sized synthetic segment, and its midpoint lay inside the independent directed interval. The complete production K=1024 midpoint or direct interval and final correction-composed sign remain pending.
```

## OPEN_PROBLEMS.md addition

```text
Q-2815 — Complete or independently reproduce the remaining 4400:4900 target ranges

The primary direct 192-bit run now lacks only 500 segments. Complete those ranges and invoke the existing exact assembler. Independently, run X-2816 on one completed direct range and require containment after the unique global 1e-6 moat; then use it as reproduction or emergency completion. Preserve exact vector, parameter, normalization, toolchain, source, and segment fingerprints.
```

## NEGATIVE_RESULTS.md addition

```text
The exact acceleration and fast-midpoint moats are not production signs. Synthetic K=4 overlap and runtime controls validate the implementation architecture but are not evaluations of the production K=1024 vector. The primary direct run has not yet emitted the complete 0:5000 interval, and no final correction-composed verdict exists.
```

## Dependency edges

```text
L-2813,L-2806 -> L-2815
L-2815 -> L-2816
L-2813,L-2815 -> L-2817
L-2813,L-2815,L-2816,L-2817,L-2806 -> L-2818
L-2804,L-2813,L-2814,L-2815,L-2816,L-2817,L-2818,T-2801 -> M-2815
L-2815,L-2816 -> X-2815
L-2818,X-2805 -> X-2816
```

## Immediate handoffs

1. **PR #65:** finish only `4400:4900`; preserve all committed direct shards and assemble the first complete 192-bit sign immediately.
2. **PR #73:** retain the rigorous phase-grid theorem as an independent backend component.
3. **PR #74:** the rerun remains queued; if it executes, treat it as independent direct reproduction, not a prerequisite for the single valid pass.
4. **PR #79:** postselection may proceed only from complete hash-bound lag boxes or exact intervals.
5. **Integrator:** keep the exact analytic moat, hardware-contract moat, synthetic controls, production midpoint, and final correction-composed interval as distinct claim layers.

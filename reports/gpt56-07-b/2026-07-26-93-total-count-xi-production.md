# Total-count-deflated PR71 direct-xi production and refinement

Agent: `gpt56-07-b`  
Issue: #93  
Branch: `cursor/total-count-xi-production-7f09`  
Date: 2026-07-26

## Starting hypothesis

Unconditional nested total-zeta-zero counts could instantiate L-9303 at the
exact PR #71 ordinate and materially sharpen the direct completed-xi modulus
rows. If the original table remained positive, the same count artifact could
support a denser node and nearby-ordinate attack.

## Approaches attempted

1. Ran the X-9301 and X-9302 focused test suites.
2. Compiled the FLINT 3.0.1 total-count and completed-xi producers.
3. Computed all nine nested total counts at 192 and 256 bits.
4. Repaired two previously unexecuted production failures:
   - negative-height Riemann--Siegel functional-equation evaluation;
   - infeasible expansion of xi's approximately `-5.3e12` binary exponent
     into an explicit rational denominator.
5. Replaced the reflection control by the exact positive-height conjugation
   identity and applied one exact common power-of-two scale to all xi values.
6. Added exact-checker caches and rigorous dyadic secant hulls to make
   order-three/four determinant replay practical.
7. Evaluated the declared twenty rows at both precisions.
8. Exhausted every monotonicity row and every interlaced order-2/3/4 minor on
   the nine-point table.
9. Added L-9304 and exact adapter support for reusing a count table at a shifted
   ordinate with radii `R+|T-C|`.
10. Evaluated a sixteen-point horizontal grid over a coarse nearby-ordinate
    mesh, escalated apparent midpoint negatives to 512 bits, and refined the
    resulting positive basin on a `1/1024` ordinate mesh.
11. Exactly certified the fine-mesh minimum.

## New results

The unconditional cumulative count table is:

```text
radius: 1/32 1/16 1/8 1/4 1/2 1  2  4  8
count:     1    1   2   3   4 8 17 35 70
```

Both precisions isolate the same integers and all count balls nest.

The original 256-bit table has:

```text
verdict: NO_NEGATIVE_IN_DECLARED_ROWS
negative rows: 0
unresolved rows: 0
```

Its tightest row is:

```text
d4-0 in
[1.279845348201527229468981e-25,
 1.279845348201527236031816e-25].
```

Every one of the 255 exhaustive rows on the original point table is
nonnegative at 256 bits.

The dense shifted search produced no rigorous negative. Coarse 256-bit
midpoints at shifts `9/32` and `11/32` appeared negative around `1e-96`, but
512-bit escalation proved those signs were numerical cancellation. A local
minimum occurs at ordinate shift

```text
477/1024
```

from the count center. Its exact 512-bit total-count-deflated order-four
interval is:

```text
[9.45211209497258074553587459016779716487302124040763e-103,
 9.45211209497258074553672968742522001567519792257337e-103].
```

It is strictly positive.

## Candidate counterexamples

None. No `Z-####` identifier is justified.

## Certified computations

- Nine unconditional total-zero count windows at 192 and 256 bits.
- Nine-point direct completed-xi rectangles at both precisions.
- Primitive and final-row nesting across precision.
- All twenty declared rows at 256 bits.
- All 255 finite interlaced rows on the original point table.
- Exact shifted-radius transfer from L-9304.
- One 512-bit exact certificate at the fine shifted minimum.

## Failed approaches

- The inherited producer sent `1-s` at negative height into FLINT's
  Riemann--Siegel backend.
- The inherited rational printer attempted to materialize a denominator with
  trillions of bits. The xi evaluations themselves were fast; serialization
  caused the memory exhaustion.
- Two coarse shifted midpoint signs were false negatives caused by evaluating
  a highly conditioned determinant below the available precision.
- No strict negative survived 512-bit escalation.

## Potential errors and proof boundary

- Independent FLINT or alternate-backend reproduction is still required.
- L-9303 and L-9304 require independent analytic review.
- The common xi scale must be identical at every point; point-dependent scaling
  would be unsound.
- Shifted reuse must widen every radius by the exact absolute ordinate shift.
- Midpoint signs are discovery data only. Only strict exact intervals determine
  classification.

## Files changed

Primary result roots:

```text
experiments/X-9302-total-count-zero-deflation/results/pr71/
experiments/X-9302-total-count-zero-deflation/results/pr71-dense/
experiments/X-9302-total-count-zero-deflation/results/pr71-shift-scan/
experiments/X-9302-total-count-zero-deflation/results/pr71-shift-fine/
```

Review first:

1. `results/pr71/summary.json`
2. `results/pr71/total-counts-p256.json`
3. `results/pr71/verification-p256.json`
4. `results/pr71-shift-fine/fine-min-verification-p512.json`
5. `claims/lemmas/L-9304-shifted-total-count-reuse.md`

## Claims affected

- `L-9303`: instantiated by a complete production table.
- `L-9304`: new shifted-count reuse lemma, status `PROPOSED`.
- `X-9302`: complete positive production and shifted refinement.

## Recommended next actions

1. Independently reproduce the count table and the 512-bit fine minimum.
2. Use scale-normalized determinant or Gram conditioning scores when ranking
   future node sets; raw determinant magnitude alone over-ranks clustered nodes.
3. Move to new count centers selected by direct-xi reconnaissance rather than
   further refining this certified positive basin.
4. Parallelize endpoint total-count calls: the current monolithic producer is
   exact but CPU-serial and took roughly 2.5 CPU-hours per precision.

## Organizational improvement ideas

Production workflows should test compact serialization at the target height
before launching expensive counts. Total-count endpoints are independent and
should be emitted as resumable shards. Precision-comparison gates should compare
count semantics while retaining, not equating, precision-specific proof
digests.

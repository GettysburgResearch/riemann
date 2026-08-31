# Independent held-out Xi review: fixed replay panel

Status: review protocol fixed before the independent evaluations below.
Science: `64165b8c805d182dbc43f2e5855e64a86cf1aaf9`.

The reviewer has read the complete note, producer, tests and manifest.
The independent evaluator imports no author module. It reuses only the
reviewer's own frozen reflected-log-Gamma, unit-s-variable evaluator at
`26201b3a7de6293ea47621f06b45dd9837521a20`, authenticating its Git blob.
The native FLINT special-function library remains shared and trusted.

Before computation the independent complete-boundary panel is fixed as:

| box center | bits | mesh denominator | Taylor terms |
| --- | ---: | ---: | ---: |
| 256 | 384 | 32 | 36 |
| 512 | 384 | 32 | 36 |
| 1024 | 1152 | 128 | 52 |

All original box edges are retained. Each edge is subdivided twice as
finely as in the successful author tier. The review uses reflected
log-Gamma rather than the direct Gamma product, a unit-s series followed
by the chain rule, and quadrant winding rather than a ray crossing.
Every closed boundary arc must have a convex zero-free image enclosure
also containing the polygon endpoints. Failed evaluations are retained
as failures; no boundary or precision is silently moved.

All forty root discs, the full 40-by-40 normalized Gram matrix, and four
weighted prefixes will independently be replayed at 384 and 512 bits.
The script checks the full root rectangles, not only their midpoints.
The historical fourteen-node boundary census is imported from the frozen
earlier review rather than redundantly repeated. All twenty-six new root
discs must exhaust the three new boundary counts.

This review does not repeat the 588 Newton scouts as a separate search;
the independent argument principle and root-disc proofs certify coverage.
It does not prove a cofinal Bessel bound, alignment divergence, component
innerness, or any statement about nontrivial zeros of Xi itself.

# Review corrections absorbed (from PR #182)

This focused packet treats the following as **given exact structure**, not
empirical discoveries:

1. `Q = Q_even ⊕ Q_odd` for symmetric nodes / even `P`.
2. Structural kernel `Q p = 0`.
3. First deficit-four event = paired even/odd double root
   `P(s)=(s²-r_N²)² H(s)` with kernels
   `x_even,j=p_j/(j²-r_N²)`, `x_odd,j=j p_j/(j²-r_N²)`.
4. Continuum collision: `G_α(r)=∂_r G_α(r)=0`.
5. Asymptotics: `α_∞ − α_N ∼ C / N³` with
   `C ≈ 0.1866219902712081`,
   `α_∞ ≈ 0.97577952846160346768`,
   `r_∞ ≈ 2.17949022036079642556`.
6. `p_2=0` is a precursor only.
7. Old C22 is **not** a Reading-B test (universal `B_p` slope form only).
   It should be renamed/re-scoped on the archive branch; this packet does not
   cite it as Reading-B evidence.
8. Decimal-rationalize → binary64 eigensolve pipelines are discovery-grade;
   directed interval Newton is the proof-facing next step.

## PR process

The fat reconnaissance archive remains on
`cursor/humble-positive-computations-8455` (PR #182).
This branch is the focused continuum/finite double-root follow-up requested
in the review.

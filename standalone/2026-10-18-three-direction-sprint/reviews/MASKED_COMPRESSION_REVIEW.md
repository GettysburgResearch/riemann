# Independent read of the already-masked compression

Status: **component review by the coordinating research track; not external
referee acceptance or approval of an RH argument.**

Reviewed `rational/MASKED_COMPRESSION.md`, raw-byte SHA256
`43b76650a1f4573a719704145f44a012f727b1dc36a2a1dd85fda05adfdfe71e`.
The reviewer independently derived the compact-flux estimate in
`FLUX_COMPRESSION.md` and then checked this new composition against the
complete source, rather than merely its finite test data.

The annular inversion is exact: substituting the finite divisor expansion
of each S_q gives alpha_(j,d), and summing these coefficients gives zero
because q>=2. The bound on alpha uses all multiples of d and a harmonic
sum; it does not assume cancellation in the new mask. The old cubefree
coefficient majorant is an explicitly pinned premise.

The low products are paid at the actual integers by |R(k/d)|<=d/k. They
are not said to have zero projection after the mask has been expanded.
For the top corner d>Y^2-20Y^(3/2), both the only possible denominator q
and the only old product multiple equal d. Each contributing old input
lies in an interval of length 20sqrt(Y), giving O(Y) ordered pairs and
total coefficient mass O(1/Y). The resulting discrete log-squared bound
includes shared primes and squares.

For all remaining blocks the exact signed alpha coefficients satisfy the
finite-transport hypothesis uniformly in j. Tolev's uniform density gives
the stated positive fraction of legal squarefree reference pairs by
pigeonhole; no simultaneous-squarefree conjecture is used. The reference
load bound and conversion to symmetric ordered weights have the factor
1/2 required by the two orderings. Distinct target integers, not distinct
factorizations, are used in the load and flux counts.

Each transported difference has zero total R coefficient. Since its
dilations are integers, its value at the left integer endpoint equals its
value on the whole following unit cell. This justifies bounding its
discrete annular norm by its global continuous norm. The low-product and
corner terms are handled separately and do not use that assertion.

The reviewer also read #1002's complete `NEWTON_BUDGET.md` at commit
`1319373815ee408146705b25a426fba6b22ed755`, Git blob
`b5307da48efc6e73344775a8b0d37677ee6ca2e4`, and checked its cutoff
constant: 144/2304=1/16 after squaring the removed root norm. The mask is
applied to the ORIGINAL coefficients. No corresponding adaptive-core
bound is assumed for the transported reference source.

No blocking error was found in this draft of the reduction. Its final
exponent consumer remains conditional on both the explicitly imported
all-prefix growth theorem and the OPEN complete balanced-amplitude
estimate. This review does not supply that estimate, a new zero-free
region, or a general theorem from sparse-cut recurrences.

# Independent internal review of the growing positive onsite corollary

Reviewed `../theta/POSITIVE_ONSITE_COROLLARY.md`, actual file-byte SHA256
`0485de3e38251e8f73e552c6626b98f3e5630bd39aaa94df8db0937374beb6d9`.
No blocking error found at its stated scope. This is independent internal
component review, not external acceptance or an RH result. The parent
entire-onsite proof was separately reviewed at the hash recorded in
`ENTIRE_ONSITE_REVIEW.md`.

For each fixed R>=1, local potential-ratio convergence bounds the
three-anchor difference D_N(R). The auxiliary quartet contributions are
nonnegative because log P(sqrt(u)) is concave throughout these anchors.
For every integer k>=2,

    [9^k-(8/3)4^k+5/3]/9^k >= 1-128/243 > 1/3.

Thus positivity of the onsite Taylor coefficients gives the claimed
bound `sum a_(k,N)(3R)^(2k)<=3D_N(R)`. Absolute convergence at 3R
justifies the series identity and termwise comparison. The same sum
dominates |U_N(z)| on |z|<=3R. Since R is arbitrary, this supplies local
uniform bounds on the entire complex plane, even though the degree,
number of nonzero coefficients, and coefficients may vary with N.

At R=1, the same positive difference also bounds the full far-quartet
fourth-order resource and near-zero count. Together with bounded
U_N(1),U_N(2), it therefore controls the renormalized quadratic term
through the real 1-to-2 ratio. The parent theorem's entire normal-family
argument, interval-mass normalization, and identification of the weak
limit consequently apply without requiring a fixed finite onsite
family. Finite initial values of N do not affect normality or the weak
limit.

The hypotheses doing the work remain explicit: every onsite coefficient
from degree four upward is nonnegative; each onsite is entire; there is
one uniform finite auxiliary zero band; and the target density is
positive and continuous. The argument does not cover arbitrary signed
growing-degree potentials or a growing auxiliary zero band. No claim
about such omitted constructions follows from this corollary.

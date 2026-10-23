# Independent review of the degree-12 prime and curvature inputs

Reviewed 2026-10-21 by the Type-I agent. This receipt binds:

* `../three-hour-boundary/LOGISTIC_DEGREE12_PRIME_GAIN.md`, SHA256
  `bccdc8825518319ca252995a9ccab657e18d9ffd468978d9a636f5c19b56054f`;
* `../three-hour-boundary/verify_logistic_degree12_primes.py`, SHA256
  `59de1ebb048b94c3f8aa91918378cfdafd07cfbe622d52ed2842a7d2eae4a9c8`;
* `../three-hour-boundary/LOGISTIC_CURVATURE_51.md`, SHA256
  `35d02f5d1efff830c36788c446722250b8db4cd58321c08684079c7ce6b0e37c`;
* `../three-hour-boundary/verify_logistic_curvature.py`, SHA256
  `7f2abc98ebb5660ab1b663f462d657787da90228c39d639a8e65ffe9d76582fe`.

No issue was found in the stated bounds. The degree-12 integer square
and auxiliary square independently reproduce every positive cosine
coefficient and the normalization. The four-prime checker was run in
normal and optimized Python modes with identical results.

The prime proof retains only positive Taylor weights before multiplying
the lower bound for the logistic/cosh factor. Its logarithm endpoints
are rounded in the unfavorable direction. Each polynomial is affine in
eta squared, so its two endpoint proofs cover the entire interval; no
intermediate grid assumption is present. The exact Chebyshev conversion,
Bernstein conversion and integer de Casteljau subdivisions agree with
the represented trigonometric polynomials. Accepted closed intervals
cover [0,1] without gaps. The resulting bound is

    prime contribution > 1.26 eta - 90 eta^3.

The curvature proof has the correct normalization: for the stated
continuous compact g, no boundary delta term occurs in g', and
w''(v)=-integral g'(x)g'(x+v)dx. Translation continuity in L2 makes this
an ordinary continuous second derivative. Its norm is bounded by
the squared L2 norm of g', namely

    sec(theta)^4 tan(theta)[theta-sin(2theta)/2] < 51.

This is independently equal to the constant certified in
`LOGISTIC_POLY12_AND_CURVATURE.md` through its positive-Fourier argument.
The global Taylor error is therefore 51 v^2/2, including beyond the
compact support. The coefficient 51 in each integrated transform error
and 51/2 in each prime Taylor estimate are correct.

This review certifies these inputs and their finite checks. It does not
alone certify the full scalar parameter rectangle, the zero-sum error
budget, or a global zero-free theorem. Those have separate proofs and
replays.

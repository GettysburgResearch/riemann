# Sources, reading depth and attribution

## Repository and supplied source

Reading parent #904:
`879497b4f11be2618c448efc1fa93f69b4022e4c`.
Its root tree is `d7f5590a7d0422b1f983c43d1646b79697cc050e`.
The live PR metadata and comments were checked at the beginning of this pass.
No comments were returned. This is not an exhaustive repository/PR census.

The supplied NCG28 archive was extracted locally. Its complete PROOF.md and
arithmetic implementation were read for the exact objects, tail map, native
amplitude bound, mean-square majorant, and additive large-sieve estimate. The
proof's Git blob is `0afd47f1ca4245e84a55e6c92b868cb58cf85c05`, matching the
pinned repository identity. No full NCG28 campaign or independent proof review
is claimed by that reading.

The predecessor's `check.py` is retained byte-for-byte under the descriptive
local name `ncg28_primitives.py`. SHA256:
`05900fe68163fe06c7fe3d3df14ebd84b4ee280d204296ee02568bea5fcc2b64`.
ATC29 checks this identity before import. It reuses the same 112-bit outward
arithmetic, exact source completion, and amplitude algebra; this is NOT an
independent numerical library. The NEW accepting campaign is in `check.py`.

Pinned predecessor paths:

- `standalone/2026-09-20-native-composite-covariance/PROOF.md`, especially
  Sections 1--6: native amplitude/majorant input, periodic frequencies, complete
  tail transform, moving-window correction and the open high target.
- `standalone/2026-09-19-divisor-square-mesh/PROOF.md`: whole prime-sector bound,
  preserved at the same parent. Its previous large mesh/sieve campaign was not
  rerun in this pass.
- PCR26 completion and NIR26 isometry/Newton statements on #848 are credited
  through their explicit NCG28 interfaces. RCB26 and NSR26's distinct sectors and
  nonnative counterexamples are not assumed to give an omitted native estimate.

A parallel chat note about zero anchoring and powerful-denominator groupings
was consulted to avoid claiming that different work as new here. It is not an
imported theorem or acceptance dependency; this packet does not publish the
private note or assert that it landed on a remote branch.

## Primary literature actually checked online

1. M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Mobius
   function*, arXiv:1807.05890v1, 2018. The authors' arXiv abstract and source
   metadata were checked. It explicitly describes short-source inversion and the
   quadratic floor-matrix representation. That classical identity and its
   antecedents are NOT claimed as ATC29 discoveries.
   https://arxiv.org/abs/1807.05890v1

2. Terence Tao, *A remark on partial sums involving the Mobius function*,
   arXiv:0908.4323v5, 2009. The author's abstract and published-source description
   were checked: prime-subsemigroup reciprocal sums are bounded by one and their
   PNT-based limit is the relevant Euler product. The ordinary m(x)->0 case is
   a classical input, not a consequence newly proved by our covariance formula.
   https://arxiv.org/abs/0908.4323v5

3. Ethan S. Lee and Nicol Leong, *New explicit bounds for Mertens function and
   the reciprocal of the Riemann zeta-function*, arXiv:2208.06141v4, revised
   26 July 2024. The current arXiv page explicitly gives bounds of the forms
   `M(x)<<x exp(-eta sqrt(log x))` and the stronger Vinogradov--Korobov form.
   Only their classical qualitative consequence `M(x)=O_A(x/log^A x)` for every
   fixed A is used. No numerical constant, finite-zero certificate, fresh
   contour proof, or independently rerun computation from that paper is claimed.
   Earlier version 3 was withdrawn; this citation is to the replacement v4,
   not that withdrawn version. The online abstract states the replacement avoids
   the problematic analytic tools. The paper was not re-refereed here.
   https://arxiv.org/abs/2208.06141v4

The elementary prime-number theorem, partial summation, finite Fourier inversion,
Ramanujan sums, divisor convolution, Cauchy--Schwarz and Abel summation are
classical. No broad priority claim is made. The concrete proposed contributions
are the all-block activation budget, its current-time high-target consequence,
the specified capped-native semiprime packet, and its complete signed high/high
covariance calculation at the declared classical precision.

No family-average-to-member transfer, GRH, RH, random-sign hypothesis, fitted
power law, or unproved high-composite norm bound is an input. The independent
mathematical correctness of the written NCG28 source-amplitude proof remains a
review obligation for the native ATC29 bound that consumes it.

# Source locks, attempted closure, and review boundary

## Verified repository checkpoint

The prior eight-file Euler-energy packet was published as commit
`8eee76d79a5a608f5d6b89c9205cc7bba637f66a`, a direct child of
`c4fedfcebf5226915969610281c650f452844fd8`, on the same PR #793 branch.
The remote compare and PR head were read. The remote parent proof blob
`8b1c2018ed5615ed181c548cef4b219befead0a7` matches the uploaded attachment.
Its SHA-256 is
`45013f55becc7f6e0b12ebf2847b2688680084bd87d56160c3e41344cefeec71`.
The new checker authenticates that exact local sibling before running.
No complete re-review of every predecessor or unrelated live branch is claimed.

This continuation is additive. The source conventions of the prior three routes
are retained; no canonical claim ID is allocated or overwritten.

## Imported classical inputs and primary references

1. Euler products, Mobius inversion, and the pole of zeta at one:
   NIST DLMF, https://dlmf.nist.gov/27.4 and https://dlmf.nist.gov/25.2.
   The finite coefficient identity is independently proved and checked here.
2. The unconditional de la Vallee Poussin-type bounds
   psi(x)-x=O(x exp(-c sqrt(log x))) and
   M(x)=O(x exp(-c sqrt(log x))) are IMPORTED classical theorems.
   A primary modern source providing stronger explicit versions for M and
   reciprocal zeta is Ethan S. Lee and Nicol Leong,
   https://arxiv.org/abs/2208.06141.
   This pass read the primary abstract and imports the coarse classical estimate;
   it did not audit their paper, reproduce their numerical constants, or use a
   finite zero table. The q-free transport is proved in PROOF.md.
3. Exponential integral definitions, entire Ein and its series:
   https://dlmf.nist.gov/6.2 and https://dlmf.nist.gov/6.6.
   The estimates for the oscillatory boundary integral are derived explicitly.
4. Dickman and Buchstab functions, their delay equations and Laplace transforms
   are classical. The necessary formulas, positivity, factorial and L2 bounds
   are reproved in PROOF.md. Relevant primary literature includes Douglas Hensley,
   *The Convolution Powers of the Dickman Function* (1986),
   https://doi.org/10.1112/jlms/s2-33.3.395.
   No claim is made to have independently invented these transforms.
5. Corrected Euler products are an established research subject. Gonek, Hughes
   and Keating, *A Hybrid Euler-Hadamard Product Formula for the Riemann Zeta
   Function*, https://arxiv.org/abs/math/0511182, is primary context.
   No theorem from that paper is needed in this packet; no external novelty
   assessment of the present norm/profile specialization has been completed.
6. The RH implication and conditional converse in section 8 import the classical
   RH prime-counting bound O(sqrt(x) log^2 x), not an unconditional estimate.

Fourier/Laplace Plancherel, dominated convergence, elementary complex analysis
and Montel's theorem are standard analytic tools. The proof states every support,
normalization and continuation condition on which it relies.

## What was actually attempted

The target was the missing collective signed bound after the prior three-prime
contraction failed. The exact rough-number convolution regrouped all omitted
primes. It yields a first boundary profile, then a second full rough-prime profile.
Inverting the entire continuum contribution produces the Dickman completion.
The attempt succeeds in the full causal norm on Re(s)=1. It does NOT establish
local boundedness throughout Re(s)>1/2 or the original signed-energy estimate.

This is not an argument that the completed product is positive because the
Dickman density is positive. The operation is I minus an average, and its norm
is greater than one at an explicit frequency even on Re(s)=1. Below one its
kernel is exponentially tilted and its norm grows. The needed cancellation is
between the actual finite Euler source and this correction before norms are taken.

## Load-bearing review checklist

- DC1 must use rough PRIME POWERS, not only primes; primes alone apply only below X^2.
- The scale in DC2 is L X^(a-1), not just L when a differs from one.
- PNT is imported independently, not deduced from the proposed RH conclusion.
- Formula (7) has a subtraction for powers p^k>X with p<=X, including q powers.
- The global L2 arguments pay the high-frequency tail, not only a bounded t window.
- The removable zero at t=0 cancels D(1+it)/(it); no uncancelled meromorphic pole
  is declared an H2 boundary function.
- DC4 removes the Dirac mass at u=1 before identifying an L2 Buchstab derivative.
- The second rescaling is L^2 H_X(Lu); its squared norm is L^3||H_X||_2^2.
- C_X is defined by its ENTIRE formula across s=1, not a discontinuous choice of E1.
- The exact faithful interval is x<log X; completion outside it uses a continuum
  kernel and does not claim to recreate the missing primes exactly.
- The prime-base cutoff and hard prime-power cutoff are different; equation (18)
  and the stated difference must not be silently swapped.
- A bounded family on Re(s)=1 is not a bounded family on Re(s)>1/2.
- The local boundedness endpoint is open. The converse uses RH explicitly.

## Computation boundary

The stdlib checker recomputes finite integer/rational algebra, with explicit
resource caps and acceptance that survives Python -O. It verifies complete
finite convolution and first-shell grouping, primitive-profile identities,
formal entire-correction coefficients, delay inversion and exact constants.
These are controls of the proof algebra, not a machine proof of analytic limits.

The separate 50-digit regression compares the raw and corrected Euler products
with reciprocal zeta at nine fixed points, plus two implementations of the
correction factor. It uses actual primes only through 10007. It neither estimates
an infinite norm nor certifies a PNT rate or zero-free region. All its outputs are
labelled NON_DIRECTED_HIGH_PRECISION_NON_PROOF.

No broad parent test suite, zero census, formal proof build, or remote CI result
is asserted. External mathematical and code review are still required.

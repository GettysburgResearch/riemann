# Coordinator reconstruction of the late quartic components

Status: PROPOSED internal mathematical review, not external referee acceptance.
The coordinator helped develop the fixed-base and common-cover arguments;
this is an explicit final reconstruction, not blind authorship independence.

Reviewed raw sources:

- quartic/ALL_SQUARE_INDICES.md:
  b6fdd7d7a57d3feb6d35270f88f22a62d68c05654556c344da344cbaf3d912a6
- quartic/COFINAL_HILBERT_FILTER.md:
  142fe3cfe5695c270de015f80b798daca17d18a86d651c0018be94b0d84f4f73
- quartic/SQUARECLASS_PROJECTION_OBSTRUCTION.md:
  7769a60d2f513c49ae4219199e664eaa7d91ef37d2585d1c317315972d857853

I read all three complete sources and independently reconstructed the
following proof steps. The DDHL primary formulas in Sections 3--4 were
checked directly, and Suzuki's original printed page 114 was viewed.
Its full fourth-power periodicity is classical; no novelty is claimed
for that imported identity.

## All square indices

The two-ray modulus split gives terminal Gauss factors G and
a_pi conjugate(G), with ray operator -J in the nontrivial class.
Thus AB=q^(3-4z). The single legal coprime fourth-power identity
forces A h2=q^-1 h0 and B h0=q^-1 h2 at z=5/4. The geometric
identity Q_j+q^(-j-1)=1+q^-1 proves all even-valuation cases.
The decomposition m=d^2 r permits shared primes. It gives exactly
L(2s-1,chi^2)/L(s,chi conjugate(epsilon)delta), with the actual
Mellin weight Nm^(.5-s), not a shifted target variable.

The direct own-cusp diagonal scattering residue is nonzero. A
nonzero automorphic function cannot be C y^(.75), so a nonzero
nonconstant base index exists. Its fixed quadratic numerator twist
and finite Euler deletions yield the same principal denominator.
An ordinary index-character twist supplies even angular type in the
root variable and does not implement the needed odd type.

## The Hilbert construction

The normalized integral on a common cover is independent of which
finite cover represents a function. Rational pullbacks are unitary
because conjugate lattices have equal covolume. The finite additive
averages are self-adjoint idempotents on the periodic subspace;
their product is the least-common-multiple projection.

Full Fourier periodicity, the Nnu^(1/8) prefactor and y K radial
factor give P_d theta=Nd^(-3/2)T_d theta including the constant term.
This proves the exact gcd Gram, hard norm 1/zeta^S(3), and damping
norm zeta^S(3+2eta)/zeta^S(3). Joint projection masses, rather than
an assumed tensor product, justify the products over all primes.
The independent fixed-height Fourier majorant proves the special
local smooth limit. It does not make cusp traces bounded on the
Hilbert completion.

For both factors damped by eta/2, the selected arithmetic series is
L(2s-1+eta,epsilon^2)/zeta(s), with its stated finite deletions and
nonzero scalar. For any target B>=1/2, eta>=2-2B makes that numerator
Euler-nonzero at every hypothetical zero with Re(rho)>B. In particular
eta=63/250 suffices for the conditional B=437/500 target; eta=1
suffices for all Re(rho)>1/2. This is pole retention only. No complete
period or holomorphy estimate is supplied by that calculation.

## The squareclass obstruction

The CRT construction allows u and the squarefree denominator D to
share primes. This matters: a may be 1 at all but one prime while
the composite quadratic symbol (a/D)_2 is -1. The chosen inverse
ad=1 modulo c lambda^4 makes BOTH off-diagonal entries have the
required principal-congruence level after conjugation.

The top-left entries satisfy a'=a^(-1) modulo D and a'=a modulo u.
Quartic reciprocity has no residual sign since both are 1 modulo4;
the lambda^4 numerator is a fourth power. Consequently the two
Kubota eigencharacters have ratio -1. The same unitary pullback
has those two opposite eigenvalues on theta and its translate,
proving exact correlation zero. Reducing every nonzero fraction
modulo a squarefree D proves joint uniformity by finite Fourier
inversion, without a local spherical or independence hypothesis.

The necessary squareclass test includes residue zero, so its norm
factor is (q+1)/(2q), not (q-1)/(2q). The all-prime norm tends to
zero. This refutes this specific nonzero bounded-Hilbert-limit
selector; it does not exclude other descents or controlled unbounded
traces. The original target coefficient can remain unchanged while
that Hilbert norm vanishes.

No blocking issue was found at these declared scopes. No RH proof,
new zero-free region, complete weighted period, or fixed-level
automorphy of the cofinal limits is accepted by this review.

Final conductor qualification (18 October 2026): the general character
in (9) is unramified outside the deleted set S; otherwise S must include
every conductor prime and all sums must be prime to that enlarged S.
This prevents chi^2 from restoring an Euler factor when its primitive
conductor shrinks. Both reviewing agents and the rational agent
confirmed this restriction. The actual target characters already
satisfy the stated S/S_a condition; (10), (10a), and the damped target
are unchanged. The raw source binding above includes this correction.

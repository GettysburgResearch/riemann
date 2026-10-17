# Research: sharp fixed-twist mesoscopic prime-exchange covariance

PROPOSED complete unconditional component proofs, with exact finite checks.
Not independently reviewed. No full native moment, total critical-energy
bound, new zero-free region, or RH proof. This local draft is NOT a published PR.

## Main result

Over Q(omega), for the actual principal coupled 0/1/m source, m>=4, and also
for native ideal Mobius coefficients, retain all ideal pairs whose reduced
rational norm ratio is p/q with distinct split primes p,q in [D^theta,2D^theta]
and 0<|p-q|<=D^eta. For every fixed 0<eta<theta<1 the complete fixed-twist
Gaussian covariance is positive and has sharp size D^eta.

At theta=3/4, eta=1/4, this is Theta(D^(1/4)) inside a relative norm band of
width D^(-1/2). Every pair is unequal and incomparable by ideal divisibility.
It is not a positive subprojection of the full energy, so it does not refute
or prove the conjectured subpower total energy.

The absolute upper bound permits arbitrary physical phases, all original
nonunit masks, and finite row measures of mass Z:

    AbsX <= C Z H [1+log_+(D/Y)]^2/[log(2Y)log(2H)],

uniformly in m>=4. The signed lower result has its principal-phase/fixed-S
hypotheses. A complete moving-prime logarithmic polynomial has a power error
O((D/sqrt(pq))^(-delta)), delta<1/m, before the prime-pair count. No prime-pair
conjecture or short-interval PNT is used.

## Relation and boundaries

#953 bounds ideal-divisibility pairs. #954 controls complete norm collisions
and a long Mellin average. This result addresses a growing unequal-norm,
incomparable, shrinking-ratio sector at one fixed twist. Classical PNT in
1 mod 3, Selberg's upper sieve, Euler and Gaussian methods are credited.
The sieve and needed complex-continuation calculation are written out.
Global literature novelty has not been established.

## Validation

Four complete supported-ideal norm censuses through 131072, including 7^6,
agree under two constructions. All permitted common cores for ordered split
prime exchanges <=43 are checked; shared-power, odd-degree, arbitrary-phase
and zero-mask controls remain. Normal and optimized exact reports agree;
five separately executed corrupted versions fail. Three finite high-precision
quadratures are explicitly uncertified. No independent referee, formal build,
remote CI, or full-repository validation is claimed.

Intended base: a93d382951f8fac7b0c28783061a7ddb99fcf0a4 (#953).
All additions are isolated under standalone/2026-10-17-mesoscopic-prime-exchange/.

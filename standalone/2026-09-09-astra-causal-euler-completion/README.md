# Exact causal completion and a constructive Euler repair

**Status: PROPOSED, pending independent mathematical review. No RH proof or
subpower native arithmetic estimate is claimed.** Date: 2026-09-09.

This continuation replaces the previous failed sparse Euler repair with an
explicit finite construction. It preserves EVERY Mobius coefficient through Y,
retains the COMPLETE source energy, and approaches the exact optimum with a
proved relative power-saving error. The optimum itself is the unresolved
arithmetic quantity, not something the construction makes small automatically.

## Main statement

Let M(k)=sum_(n<=k)mu(n) and

    E_Y=sum_(k<=Y)M(k)^2/[k(k+1)].

For every Y>=2 the packet constructs a finite Dirichlet polynomial

    P_Y(s)=product_(p<=Y)(1-p^(-s)) * B_Y(s),
    B_Y(s)=1+sum_(d>Y)b_d d^(-s),

with integer |b_d|<=2Y and complete energy

    J(P_Y)=integral_1^infinity |sum_(n<=x)a_n|^2 dx/x^2.

Its coefficients satisfy a_n=mu(n) for all n<=Y, and for Y>=216,

    E_Y <= J(P_Y) <= (1+36Y^(-2/3)) E_Y.

This is an all-Y written theorem, not a numerical fit. No PNT, RH, zero table,
random phase assumption, frequency truncation, or large external payload is
needed for the constructive bound. All expanded correction terms are finite,
but their total number and their delays may be very large. The construction
is NOT in the old fixed-polynomial-delay/sparse correction class.

## The exact construction

The free energy minimizer over ALL finite prefix-preserving sources is

    C_Y(s)=sum_(n<=Y)mu(n)n^(-s)-M(Y)(Y+1)^(-s).

For each p<=Y let m_p be the first exponent with p^(m_p)>Y^2. Set

    B_Y=C_Y product_(p<=Y)(1+p^(-s)+...+p^(-(m_p-1)s)).

The geometric identity gives, with every coefficient retained,

    P_Y=C_Y product_(p<=Y)(1-p^(-m_p s)).

Before Y+1, the geometric factor has the ordinary divisor coefficients needed
for exact mu*1 cancellation. In the physical L2 source norm, a delay d has
operator norm d^(-1/2). The entire error therefore costs at most
(product_(p<=Y)(1+p^(-m_p/2))-1)^2 times E_Y. Orthogonality makes this an
ADDITIVE excess, not an assumption about cancellation between shifted copies.

The proof also gives exact infima over unrestricted finite late Euler repairs,
and tunable error rates by replacing Y^2 with Y^a, integer a>=2.

## A safe-point zero is a different constrained problem

Put c_Y=sum_(k<=Y)M(k)/[k(k+1)]. Adding P(1)=0 changes the exact optimum to

    F_Y=E_Y+(Y+1)c_Y^2.

The unique free constrained completion is

    C_Y^0(s)=sum_(n<=Y)mu(n)n^(-s)
              -(Y+1)(sum_(n<=Y)mu(n)/n)(Y+1)^(-s).

The same Euler construction preserves the zero and approximates F_Y with the
same relative bound. Zero TOTAL coefficients and a zero at s=1 are distinct:
at Y=3, E_Y=7/12, while F_Y=23/18. No claim about higher safe-point jets is made.

## The exact remaining full-problem estimate

A bound E_Y=Y^(o(1)) along one unbounded sequence would exclude every off-line
zeta zero, by the complete delayed-factorial argument reproduced in PROOF.md.
No such bound is proved. E_Y is the energy on the immutable interval [1,Y+1),
and every late repair pays at least that much. The construction removes an
artificial Euler-product tail penalty; it does not estimate the signed Mobius
prefix or solve RH by choosing a larger support.

## Review and evidence

Read [PROOF.md](PROOF.md):

| Claim | Content | Boundary |
|---|---|---|
| EPC26-1 | Exact free and one-safe-point completion minima; Pythagorean identities | The native optimum is not shown subpower |
| EPC26-2 | Explicit finite late multiplicative compiler and coefficient bounds | Expanded support is not polynomial in Y |
| EPC26-3 | Whole-energy error, elementary relative rate, and exact repair infima | Relative to E_Y or F_Y, not to zero |
| EPC26-4 | Full conditional RH consumer | Its arithmetic hypothesis remains unproved |

[produce.py](produce.py) and [verify.py](verify.py) are separate standard-library
implementations. They reconstruct all 256 prefix energies, 21 projection tests,
48 complete output polynomials, and eight fully expanded repair polynomials.
The output-only cases are NOT reported as full expansions of their larger B.
All 12 resealed corruptions must fail, including Python numeric-type aliases.
Both programs were written by the same author, not independent peer review.
See [VALIDATION.md](VALIDATION.md) and [validation.json](validation.json).

[PREVIOUS_ATTEMPT.md](PREVIOUS_ATTEMPT.md) preserves the previously delivered
NRT26 proof bytes, without changing its proposed status. Only that written
proof is imported; its original code/results bundle is NOT claimed replayed
or fully imported. It is historical motivation, not a premise of EPC26-1--4.
[SOURCE_LOCK.json](SOURCE_LOCK.json) records exact repository reading and this
boundary. No broad external priority claim or whole-repository audit is made.

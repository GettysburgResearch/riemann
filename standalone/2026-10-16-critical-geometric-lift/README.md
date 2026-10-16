# Critical geometric lift and a pre-Poisson signed adapter

Status: **PROPOSED component mathematics. No independent review. No full native
moment theorem, improved zero-free boundary, or RH proof.**

This continuation is stacked on PR #948 at
`05b6f2172c686356ccd9900d33ffc5f526c5e98b`. It also reads the new #949
normalization and the full relevant #946 compensation argument, without
merging their branches or changing the integrated record.

## What advances in this packet

1. **A radical-preserving completion with constant critical cost.** A second
   normalization of the Dedekind source gives the local factor

       1-(1-1/q)x/(1-eta(p)q^2*x^6).

   Its positive prime exponents are exactly 1,7,13,... . Every supported
   ideal is uniquely b*g^6 with b squarefree and rad(g)|b. It has the SAME
   sextic row character and zero mask as b. The lifted exponents have total
   square-root-weighted local mass exactly q^(-1/2), the native budget.
   Native and completed physical Lp scale envelopes compare in both
   directions with constant exp(4[F:Q]); exp(10[F:Q]) covers all prime profiles
   of modulus at most 5/3, including the Mammen law. This improves #948's
   logarithmic comparison for its DIFFERENT, 0/1/6 source. It does not bound
   either unknown deterministic moment. Same-height shorter scales remain.

2. **Positive compensation is compatible with the lift.** The new source is
   multiaffine in prime SUPPORT, despite its higher prime exponents. The
   #946 Mammen/Peano identity therefore applies with an explicitly derived
   full prime-power cofactor. A randomized log-square starting reference
   has diagonal size at every fixed order. The native endpoint is exactly
   M=G+I-D with D>=0; its missing estimate is still I<=D+the allowed error.
   There is no monotonicity or automatic domination of I by D.

3. **An actual pre-Poisson operation, not only a scalar Euler rewrite.** For
   the paper's three-scale average I(X,Y,Z), dilate X and Z simultaneously
   by (Nd)^6, leaving Y fixed. The triple Mellin multiplier is exactly
   (Nd)^(3-6xi), independent of the other two contour variables. With
   h(d)=mu(rad d)eta(d)phi(rad d)/Nd, this inserts the new normalization at
   EVERY Poisson frequency. The physical sum is finite, Nd^6<=BXY. Its
   principal Gaussian sum is not finite; its extra tail must be retained
   with the residual. No new reflected bound or contour domain is proved.

4. **The compact-test/Gaussian analytic interface is completed.** An
   all-compact-test scalar estimate automatically supplies a finite uniform
   test seminorm by Baire, then the Gaussian estimate by a dyadic partition.
   No separate quantitative dependence on individual test constants is
   required. The arithmetic all-test hypothesis is NOT established here.

The new numerator is holomorphic and nonvanishing on Re(s)>3/7 after
excluding prime ideals of norm below 7. **3/7 is the numerator's domain,
not a zero-free region for zeta.** Genuine reciprocal-zeta poles persist.

## Reading order

- [MATHEMATICS.md](MATHEMATICS.md): exact source, geometric law, two-way
  constant comparison, reference moments, and signed cofactor.
- [PRE_POISSON.md](PRE_POISSON.md): the actual two-scale dilation, finite
  physical cutoff, common-prime issues, principal Gaussian and residual.
- [TEST_INTERFACE.md](TEST_INTERFACE.md): complete Baire/dyadic proof.
- [SOURCES.md](SOURCES.md) and [VALIDATION.md](VALIDATION.md): attribution,
  version distinctions, finite coverage, and what was not verified.

## What remains and where to attack

The explicit sufficient moment target is OPEN-LIFT in MATHEMATICS.md. With
the original twist, test, height, and shortened-scale coverage, sublinear
excess at a cofinal hierarchy of orders would activate the inherited route
toward Re(s)=1/2. Neither its fourth-order instance nor that hierarchy is
proved. The alternative signed Gaussian estimate OPEN-G in PRE_POISSON.md
also remains open. No equality of the full theta average with the native
moment is inferred merely from agreement of their principal Euler factors.

The next substantive estimate must control the coupled d,m,theta-index sum
on its MOVING physical domains, or the actual injection minus compensation,
before separate absolute values. The lift removes a coefficient/measure
mismatch and supplies a concrete pre-Poisson expression; whether this makes
the required signed estimate tractable is not settled. Field extensions,
randomized reference bounds, and a nonvanishing numerator alone cannot do it.

## Reproduction

Run `python verify.py` and `python -O verify.py`; both reproduce
[results.json](results.json) byte for byte. The checker has **14,566 explicit
finite predicates**, including setup and repeated cases. Its ideal fixtures
use ONLY five named Eisenstein prime ideals, NOT a full native ideal census.
The large norm caps do not change that restriction. The old #948 791-check
packet was separately replayed and matched. No Lean build, independent
referee, full-repository validator, or remote CI run is claimed.

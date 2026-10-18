# Critical finite translations with a uniformly controlled growing order

**Status: PROPOSED complete unconditional component arguments, awaiting independent
mathematical review. No RH proof, new zero-free fraction, or critical native
moment upper bound is claimed.** This is a different arithmetic realization
of the prime-discrepancy target, not another optimization near 0.9.

## The actual advance

The classical quotient Z(s+h)/Z(s) has complete ideal coefficients

    a_h(I)=sum_(AB=I) mu_F(A)(NB)^(-h).

For EVERY nonunit ideal, including all distinct equal-norm ideals,

    |-a_h(I)/h-Lambda_F(I)| <= h(log NI)^2.

The unit term is removed explicitly. A finite linear combination of these
actual coefficients cancels more Taylor terms. With

    m=ceil(sqrt(log X)), h=exp(-4sqrt(log X)),
    b_j=(-1)^(j-1)binom(m,j),

and with each shifted pole subtracted by its exact one-sided Gaussian continuum,
the resulting complete source D(X) satisfies

    |D(X)-P(X)| <= C X^(-5/4)

for all sufficiently large X. Here P is the original Gaussian prime-power
sum minus its continuum, NOT a selected sector. Every non-prime-power ideal,
prime power, Gaussian tail, and continuum interpolation error is included.
The constant is uniform in this explicit GROWING m. The raw-source combination
has absolute coefficient mass at most

    2 exp((4+log 2)sqrt(log X)) = X^o(1).

This is not a claim of relative numerical stability or a fast algorithm for
evaluating the infinite sums. The coefficients are a specified deformation of
Mobius, not the unchanged native coefficient family.

After dividing by sqrt X, the error is O(X^(-7/4)). Consequently the full critical
Lp root norms of D and P differ by ONE bounded constant, uniformly in the
horizon and EVERY real 1<=p<=infinity. This includes growing moment orders,
but it is a norm TRANSFER, not an independent bound for those moments.

## Read the proofs

- FINITE_TRANSLATIONS.md: all-ideal quotient/cocycle, the complete coefficient
  bound, the exact shifted-pole subtraction, and finite rightward zero transport.
- CRITICAL_TRANSFER.md: the positive finite-difference remainder, uniform
  weighted divisor count, exact continuum interpolation, growing-order choice,
  simultaneous all-p transfer, and the precise unresolved estimate OPEN-T.
- SOURCES_AND_VALIDATION.md: classical credit, read boundaries, actual checks,
  and the distinction from the still-missing physical theta projection.

The prime detector and its multiplicity-safe RH equivalence already appear in
#962. The normalized transverse factor giving this quotient is credited to
#975 (overlapping #974). Jordan totients, finite differences, interpolation,
Mellin inversion and explicit formulas are classical. The contribution claimed
relative to these inspected packets is the stated complete finite-translation
approximation with uniform growing-order and all-p costs. No exhaustive
literature-priority claim is made.

## The result that is still missing

    integral_(X0)^D |D(X)|^2 dX/X^2 <<_epsilon D^epsilon
                         for every epsilon>0.

This would imply RH; conversely RH gives the bound. It has NOT been proved.
The remaining cancellation is the prime-versus-continuum error. Suppression
of non-prime-power terms does not pay that error. The full physical CT
projection with its test factors and all-frequency tails is also not built
by this arithmetic construction. The original native all-order critical
estimate therefore remains open.

## Reproduction

Run `python replay.py`. It authenticates all manifested payloads, replays the
normal and optimized exact reports, and executes ten corrupted implementations.
No network or nonstandard Python package is required. The finite tests cover
all 157 exterior integral Eisenstein ideals through norm 512, exact rational
logarithm enclosures, stencil orders 1 through 16, and declared synthetic
pole/zero models. They do not compute actual zeta zeros or infinite sources.

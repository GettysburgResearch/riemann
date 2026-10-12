# What survives when the complete Ramanujan vector is returned

Date: 2026-10-10. Status: exact finite-Fourier deduction and a
source-qualified continuation reviewed independently by the coordinator.
This identifies the precise remaining same-scale branch. It is not a
generalized moment estimate.

Dependencies are the literal source and PR915 mixed completed column
bound in `CUSP_VECTOR_SUPPORT_RETURN.md`. Retain all cusps, bad rays,
nonunit zeros, angular scalars and the complete theta sum. Fix coprime
squarefree good ideals k,a before the second reflection.

## R1. The whole local Ramanujan factor has no inactive frequency

For q=Np and m=lambda^4 ell, its first-reflection factor is exactly

    R_p(m)=q^(-1/2)[-1+q 1_(p|m)].

With the source normalized finite Fourier convention, it has coefficients

    Rhat_p(h)=0,                  h=0,
    Rhat_p(h)=q^(-1/2),           h!=0.                    (R1)

Indeed the constant -1 contributes -q^(-1/2) at h=0 and zero elsewhere,
while q 1_(p|m) contributes q^(-1/2) at every h. This calculation is
exact at m=0 and at every unit. It does not treat a character of exponent
zero as one at nonunits.

Consequently the full multiplier

    phi0(m) chi_k(m)^3 product_(p|a) R_p(m)

has all k and all a primes active in every nonzero finite Fourier term.
The second denominator is c20*k*a. This statement holds before selecting
a cusp or using an absolute estimate, so it covers the entire cusp vector.
The compact returned profile is therefore

    V(27 Nell' Nc10^2/[B Nc20^2]),                        (R2)

with the original column scale B, up to fixed geometry. There is no
remaining a-dependent shrink in the complete reunited vector.

## R2. The negative and inactive-positive branches cancel exactly

The support manuscript wrote a=d*g and the active positive divisor r|d,
with h=a/r=g*(d/r). For any fixed finite Fourier frequency tuple with
active a-primes precisely r, every prime p|h can have arisen from either
the negative constant term or the inactive positive mask. Those two
coefficients are -q^(-1/2) and +q^(-1/2), respectively. All remaining
finite Fourier factors, coordinate matrices, cusp labels, angular
scalars and profile arguments are identical for those two choices.
Thus they cancel before any theta continuation or norm is taken.

Aggregating over g|h gives the exact squarefree divisor factor

    sum_(g|h) mu_K(g) = 1_(h=1).                          (R3)

The individual support exclusions from the earlier packet remain valid.
The complete signed sum satisfies the stronger cancellation (R3):
every h>1 term is zero after the allocations are reunited, even in
the range Nh²<=C B where compact support alone allowed it. Only h=1,
r=a and the all-positive active allocation survives.

This cancellation is across algebraic summands with their phases kept.
It is lost by separately bounding the e/f/g allocations, using a
positive coefficient envelope or taking unrelated theta dyads first.

## R3. The standard face restores the original cubic orientation

On the standard cusp, use the exact source reduced-denominator/Kubota
calculation, whose active local multiplier is chi_p(a_shift)^(-2).
For a Ramanujan Fourier coefficient q^(-1/2), write
a_shift=sigma_p h_p and substitute y=h_p^(-1). The local sum is

    chi_p(sigma_p)^(-2) q^(-1/2)
       sum_(y!=0) chi_p(y)^2 e(epsilon_p m y/p)
      = chi_p(sigma_p)^(-2) gamma_2(p)
           chi_p(epsilon_p)^(-2) chi_p(m)^(-2).            (R4)

The right side is zero at p|m; this compulsory zero is retained. At units
its magnitude is one. The cubic Gauss factor is gamma_2, not gamma_4:
inverting h_p changes the character exponent from -2 to +2. The source
active j=0 formula records the same orientation; its minus sign comes
from the different Fourier coefficient -1/q of the unit mask.

Before this return, the source's first mixed scalar canceled the outside
gamma_2(a) against gamma_4(a). Equation (R4) restores the gamma_2
orientation on the active same-scale branch. Its angular factor also
changes bar(alpha(a))^3 to bar(alpha(a)) when the second coordinate
scalar supplies alpha(a)^2. The remaining CRT and k root-number factors
must be retained; the local magnitude calculation is not a license to
delete them or claim the whole finite bad-cusp matrix is the identity.

For comparison, writing an individual positive-mask term with d=a gives
first local magnitude sqrt(q), followed by second active delta-mask
Gauss magnitude 1/sqrt(q). Their product is one. This agrees with (R4)
and shows why no strict scalar contraction was paid.

## R4. The remaining generalized-moment target is explicit

The all-negative component and many named split allocations can be removed
or canceled at full-completion scope. After full reunion the remaining
standard face has original column length B, original nontrivial angular
and cubic Gauss coefficients, and the restored sextic moving interactions.
The nonstandard cusp vector remains at the same scale (R2); it was not
replaced by the standard face.

To improve the generalized 2k moment, an additional estimate must act
jointly on this surviving same-scale completed column and its correlated
outer divisor/incidence coefficients. The forward support filter does not
supply that estimate. In particular, neither the vanishings in the support
packet nor the return of the gamma quotient alone imply a power gain,
a stronger full fourth moment, or RH.

The coordinator independently read R1–R4 and the literal Fourier/Gauss
source interface and accepted these statements at their stated scope.
`check_ramanujan_return.py` independently verifies the finite Fourier
support, exact gamma_2 phase with its nonunit zero, a gamma_4 negative
control and the complete inactive divisor cancellation. Normal and
Python -O outputs agree byte-identically. The imported automorphic
analysis and the surviving full moment have not been rebuilt or proved.

# A reciprocal-moment law for the actual arithmetic family

**PROPOSED complete source-qualified deductions; independent mathematical review
required. No RH proof, full uncapped all-member inverse moment, or new zero-free
boundary is claimed.** This changes the observable from positive numerator
moments to actual reciprocal L-values, at the explicit cost of a sparse
exceptional set or a growing cap.

## The mathematical contribution

Fix n>=3, F containing mu_n, the admissible fixed ray/S data, a fixed S-supported
finite-order twist psi, s=sigma+it with 1/2<sigma<1, and a nonnegative smooth W
supported in (1,2). Rows are ALL n-th-power-free exterior ideals, ordered by
FULL norm; not radical, conductor, physical element, or random-row indexing.

1. An actual approximate inverse. For d=2sigma-1, 0<a<=d/2 and A=U^a,

   sum_(Na<=U) |L_F^S(s,psi chi_a) M_A(s,a)-1|^2
                       << U^(1-da+epsilon).

   The flat initial cutoff makes every coefficient up to A cancel BEFORE
   estimating. The complete functional-equation dual is retained, including
   small actual conductors. Its conjugate characters are not multiplied into
   the mollifier as if they were the same character.

2. One common good family, every fixed even inverse moment. There is G_U,
   independent of k, with O(U^(1-c)) omitted rows, such that

   sum_(a in G_U) W(Na/U) |L_F^S(s,psi chi_a)|^(-2k)
                       = c_W C_k(s) U + O(U^(1-eta_k)).

   The same asymptotic holds over EVERY row after capping |1/L| at
   U^(c/(8k)); at an actual zero the summand is assigned the cap.
   Here a_k=min(d/8,1/(16k)), eta_k=min(d*a_k/4,c/4), and

   C_k(s)=product_(p outside S) [1-w_p+(w_p/n)
                   sum_(zeta^n=1)|1-psi(p)zeta(Np)^(-s)|^(2k)],
   w_p=(1-(Np)^(-1))/(1-(Np)^(-n)).

   The positive constant is derived from complete arithmetic character means,
   not postulated by replacing physical rows with independent phases.

3. Explicit example. At n=6, sigma=3/4, one may take c=1/20 and, for every
   FIXED k>=1, eta_k=1/(128k). The full-family observable is

   min(|L_F^S(3/4+it,psi chi_a)|^(-2k), U^(1/80)).

   Its mean is c_W C_k U with error O(U^(1-1/(128k))). The original density
   input is at sigma0=5/8, not #979's different-threshold 5/7 estimate.

## Reading and replay

Read [MOLLIFIED_APPROXIMATION.md](MOLLIFIED_APPROXIMATION.md) for the new signed
LM-1 estimate; [RECIPROCAL_MOMENTS.md](RECIPROCAL_MOMENTS.md) for the complete
character average, Euler constant and reciprocal transfer; [SOURCES.md](SOURCES.md)
and [VALIDATION.md](VALIDATION.md) for dependencies and review boundaries.

Run `python replay.py`. No network or third-party package is required.
The exact checker tests finite algebra, not L-values or infinite analytic bounds.

## Relationship to the existing work

Base: #979 at 28fe7f5e50106ca55ee0b383afb2a26575b1a8a8. The selected-mollifier
idea motivated testing LM as one object, but #979's improved zero-density
exponent is NOT an input. Earlier full-column adapters are credited.
#976's positive numerator hierarchy and #931's independent-prime model are
different statements. The full inverse-Mobius physical moment remains open.
The reflected-ratio archive is already recovered on #978; nothing is duplicated.

Classical value-distribution and mollification methods are explicitly credited;
no worldwide novelty or best-known-result claim is made. The contribution is
this source-specific complete deduction, explicit cap/rate, and arithmetic
family realization relative to the inspected repository packets.

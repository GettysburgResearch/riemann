# Return the complete cusp vector before splitting divisibility allocations

Date: 2026-10-10. Status: source-qualified deduction independently reviewed
by the coordinator and height reviewer. This retains every cusp, ramified
Fourier index and literal
character zero. It gives a compact-support filter for a two-term
Ramanujan allocation. No full moment or cofinal zero-free result follows.

Dependencies: the exact source and its complete theta-automorphy contract
in `OPPOSITE_THETA_DERIVATIVE.md`. The source defines
H_u=[[1,0],[u,1]], u=0,omega,omega^2, and
F_u(z,v)=conjugate(theta(H_u(z,v))) with Fourier coefficients d_u(ell),
ell in lambda^(-4)O. The rational-cusp construction in source lines
3045–3146 chooses a normalized matrix lift, then uses its congruence
modulo 3 and the stated SL2(Z)/translation invariances to select one of
the three cusp functions. The proof below applies that construction to
the image numerator/denominator. It does not assume that an arbitrary
unrestricted matrix lift is already one of those three representatives.

## V1. A periodic twist of a whole cusp is a finite sum of translates

For a bounded periodic function phi on O with period q, let

    F_(u,phi)(z,v)=sum_(ell!=0) d_u(ell)
              phi(lambda^4 ell) v K_(1/3)(4pi|ell|v)
              breve_e(ell z).

Its horizontal derivatives agree with the finite Fourier translate sum

    sum_(h mod q) phihat(h) F_u(z+lambda^3 h/q,v).           (V1)

A possible constant mode in that translate sum is annihilated by either
horizontal derivative; no phi(0)=0 premise is required. Finite Fourier
inversion is exact at nonunits too. This keeps the full cusp coefficient
sequence, rather than only the standard primary n,b face.

The relevant multiplier is

    phi(m)=phi0(m) chi_k(m)^3 1_(d|m),                      (V2)

where phi0 is fixed-periodic at S, k and d are coprime good squarefree
ideals and d can be the unit. The Fourier coefficient of a nontrivial
chi_p^3 has zero at h_p=0, so every k-prime is active. The Fourier
coefficients of 1_(p|m) are all 1/Np, including h_p=0. Thus the active
positive-mask primes form some r|d. Each rational shift in V1 has reduced
denominator

    c=c20*k*r,                                           (V3)

up to a unit, with c20 in a fixed finite S-supported family. This is the
source's reduced-denominator argument: a nonzero h_p/p cannot cancel
against the other integral summands at that good prime. The number of
terms can grow with k,d; no uniform term count is used for support.

## V2. The matrix identity protects the conductor at all three cusps

Fix a shift a/c in lowest terms, and u=0,omega or omega^2. Its image
under H_u is a/(u a+c). Choose b,delta with

    a delta-b(u a+c)=1,
    G=[[a,b],[u a+c,delta]] in SL2(O).

This is possible because gcd(a,u a+c)=gcd(a,c)=1. Choose its bottom-right
entry using the source's CRT construction at that image cusp, so the
same finite cusp reduction is available. A primary normalization may
multiply the image first column by a unit; its reciprocal diagonal
change in the coordinate matrix preserves Nc and is retained in the
angular scalar. Before that unit change, exactly

    G^(-1) H_u [[1,a/c],[0,1]]
       =[[delta-bu,1/c],[-c,0]].                           (V4)

In particular the lower-left entry of the coordinate inversion is -c,
even though the image cusp denominator u a+c can have unrelated prime
factors. Replacing the conductor by that unrelated denominator would
misread the transformation. The source's finite rational-cusp reduction
of G changes only its Kubota scalar and final cusp label.

Writing beta=delta-bu, the coordinates of the right side of V4 are

    z'=-beta/c-bar(z)/(c^2(v^2+|z|^2)),
    v'=v/[Nc(v^2+|z|^2)].                                (V5)

Their derivative at zero is precisely the one in O2. Thus the opposite
horizontal Mellin transform returns a lower-order companion derivative
with angular scalar alpha(c)^2, power Nc^(1-2s), and a unit-modulus
frequency phase at -beta/c. All source cusp Fourier indices remain in
lambda^(-4)O. Unit changes used to normalize G preserve Nc and are
retained in the scalar.

## V3. The complete frequency normalization has a fixed dilation

For a full cusp frequency series define

    D_+(s)=sum_(ell!=0) d_u(ell) phi(lambda^4 ell)
                               alpha(ell) Nell^(-s).

Direct Bessel integration gives its horizontal Mellin factor

    J_+(s)= i Gamma(s+1/3)Gamma(s+2/3)
                                /[4(2pi)^(2s)] *D_+(s).    (V6)

Unlike O2's primary n,b normalization, V6 has no factor27^s. Its
physical reflection therefore uses H0 with the same gamma quotient g(t)
but scale K0=(2pi)^4. The first source reflection used H27 with
K27=(2pi)^4/27. Consequently

    H0 H27 V(x)=V(27x).                                  (V7)

This fixed dilation must not be dropped. It follows by the same complete
Mellin cancellation as O5, since K0/K27=27. The admissible reflected
profile remains compact. For U=H27 V the shift to s=-1/6 is inside the
pole-free Mellin strip of Uhat(s-1/2), exactly as in O3. Cusp automorphy
removes the constant modes and gives the required endpoint exponential
decay. No new summation over infinitely many periodic twists is used:
the translate sum is finite at every fixed k,d.

## V4. Reunite the positive divisibility terms first

At a good first-reflection prime p|a the full Ramanujan factor is

    (Np)^(-1/2)(-1+Np 1_(p|m)),  m=lambda^4 ell.

Expand it into just two terms. Write a=d*g with d,g squarefree and
coprime, assigning d to the positive divisibility term and g to the
negative term. Its exact exterior amplitude is

    mu_K(g) sqrt(Nd/Ng),

and its full inner multiplier is V2. This combines the previous e and f
allocations: outside S, p|nb is exactly p|lambda^4 ell. It is the sum of
the squarefree-theta and cube-divisibility alternatives, with all
interference retained. Splitting those alternatives before the second
reflection can destroy the completed periodic object used here.

In each fixed first-reflection ray branch, its denominator was
c1=c10*k*a. Its full cusp sum has profile

    (H27 V)(Nell*B/Nc1^2),
    X=Nc1^2/B.

Apply V1–V7. A second-reflection term with active r|d has the compact
profile

    V(27 Nell' X/N(c20*k*r)^2)
      =V(27 Nell' Nc10^2 N(a/r)^2/[B Nc20^2]).              (V8)

Here every moving character/mask, phase and cusp scalar is retained.
The original k powers cancel exactly. Set h=a/r=g*(d/r); it records
all negative primes plus all inactive positive-mask primes. If
supp V is contained in (0,b_V], Nell'>=1/81 gives the necessary condition

    Nh^2 <= C_V B,
    C_V=3 b_V max_(fixed families) Nc20^2/Nc10^2.           (V9)

Every term violating V9 is identically zero by compact support. This
holds term by term before estimating their finite sum, with no bound
on the number or absolute mass of translate coefficients needed.

## V5. A broader cancellation and its precise remaining same-scale term

With d=1, V9 is the all-negative condition Na^2<=C_V B. Thus the
all-negative allocation vanishes at every complete cusp, including
ramified and nonprimary frequency support, when Na^2>C_V B. More
generally a full two-term allocation with Ng^2>C_V B vanishes, since
Nh>=Ng for every r|d. The remaining terms satisfy

    Nr >= Na/(sqrt(C_V B)).                               (V10)

At balanced A=B=D, the surviving active positive-mask ideal has norm at
least a fixed multiple of sqrt D. This is a restriction on the exact
second-reflection expansion, not a claim that every separately bounded
e/f dyad is negligible.

The r=a term has g=1,d=a: every a-prime chose the positive mask and is
active on the second reflection. Then h=1 and the returned column
length is B up to the fixed profile dilation. It is a genuine same-scale
term. On the standard cusp, the first amplitude sqrt q and second active
delta-mask Gauss amplitude 1/sqrt q multiply to unit modulus; this
follows from the same nontrivial cubic Gauss transform used in the
source. No such scalar identification for every other cusp is needed
here. The support filter allows h=1 and alone supplies no strict scalar
contraction of the full cusp vector. A full generalized moment still
needs a joint estimate for its restored moving cubic/sextic interactions.
Treating V10 as if it removed h=1 would overclaim the result.

The coordinator and independent height reviewer read V1–V10 and the literal
source/PR915 interfaces at the pre-status hash
5ba2e4cf7f5cf2cc64c71a9b567a156a8d5e90812115ab76eba0630148dc98d5.
Their acceptance is qualified by imported complete theta automorphy and
source-compatible cusp reduction. Exact symbolic controls in
`check_cusp_vector_support.py` pass normally and with Python -O,
byte-identically. They cover the generic matrix, all primitive mod-3 cusp
columns, literal units, Mellin dilation, finite cubic Gauss moduli, complete
Ramanujan allocation interference and the compact-support filter. Imported
analysis was not rebuilt; the full generalized moment remains open. This
does not change the frozen standard-face O1–O8 packet.

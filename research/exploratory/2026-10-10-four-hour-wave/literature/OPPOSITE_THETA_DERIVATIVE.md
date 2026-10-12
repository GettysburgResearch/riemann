# Opposite horizontal derivative and a compact-support return

Date: 2026-10-10. Status: source-qualified analytic adapter, independently
reviewed by the coordinator and the height-mechanism reviewer. The imported theta automorphy theorem is not
rebuilt. This note targets one precisely specified standard-cusp component
of PR915. No complete generalized moment or zero boundary is claimed.

Source: October5 `qrh11-12.tex`, literal OpenAI/math commit
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, local SHA256
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
The source labels are `eq:general-twisted-theta-definition`,
`eq:theta-factorized-shifts`, `eq:theta-cusp-coordinates`,
`eq:ray-local-transform`, `eq:ray-mellin`,
`eq:theta-mellin-functional-equation` and `eq:theta-weight`.
PR915 is frozen at `9959364671f89b86f3992ec5ed5e19f804eb607b`;
its `NEGATIVE_BRANCH_DIRICHLET_SERIES.md`, equations2.2 and3.1, and
`PRIMARY_SOURCE_MATCH.md` retain the original angular issue and scope.

## O1. Match the angular numerator by changing the horizontal derivative

Put lambda=1+2omega=i sqrt3, and alpha(z)=z/|z|. For a finite periodic
twist psi with its literal zeros at S, the source defines Theta_psi as a
finite linear combination of translates of conjugate(theta). Keep that
same finite twist; do not insert an angular character in its periodic
Fourier multiplier. Define instead

    J_+(s,psi)=int_0^infinity
                   partial_z Theta_psi(0,v) v^(2s-1) dv,

and the completed opposite coefficient series

    T_+(s,psi)=
       [sum_n^* alpha(n) gamma2(n) psi(n) Nn^(-s)]
       [sum_b alpha(b)^3 psi(b)^3 Nb^(-3s+1/2)].              (O1)

Both n and b are the source primary indices prime to S; n is squarefree,
and b is unrestricted. This is exactly the formal source series
T(s,alpha^2 psi), including every cube factor, but the periodic theta
function being differentiated still uses only the finite psi.

The source's Fourier derivative partial_bar_z supplies 2pi i bar(ell).
The opposite derivative supplies 2pi i ell. At
ell=lambda^(-3)n b^3, alpha(ell)=i alpha(n)alpha(b)^3. Hence
i alpha(ell)=-alpha(n)alpha(b)^3, whereas
i bar(alpha(ell))=bar(alpha(n))bar(alpha(b))^3. The exact normalization is

    J_+(s,psi) = -C(s) T_+(s,psi),
    C(s)=(3^(5/2)/4) [27/(2pi)^2]^s
                         Gamma(s+1/3) Gamma(s+2/3).          (O2)

The minus sign is a fixed lambda phase, not an estimated scalar.
The same source Bessel integral proves O2 for Re s>1 by absolute
convergence. No angular infinite-order character was falsely declared
periodic.

## O2. Entire continuation and the exact reflected derivative

In the source cusp coordinates,

    z'=-delta'/c-bar(z)/(c^2(v^2+|z|^2)),
    v'=v/[Nc(v^2+|z|^2)].

At z=0, partial_z z'=0, partial_z bar(z')=-(bar(c)v)^(-2),
and partial_z v'=0. Thus the same automorphy calculation gives

    J_+(s,psi) = -sum_h c_F(h) bar(kappa(g1_h))
         alpha(c_h)^2 Nc_h^(1-2s) J^vee_(h,-)(1-s),          (O3)

where J^vee_(h,-) differentiates conjugate(theta(H_h(z,v))) in bar_z,
at the same translated cusp point used in the source. Its absolutely
convergent coefficient series on Re s>1 has bar(alpha(ell)) in place of
the source's alpha(ell), with the same factor

    i Gamma(s+1/3)Gamma(s+2/3) / [4(2pi)^(2s)].

Both horizontal derivatives remove the constant Fourier mode at every
cusp. Source automorphy therefore gives exponential decay at infinity
and exponential decay in1/v at zero for the J_+ integrand. Its Mellin
integral is entire. Dividing by the gamma factors in O2 continues T_+
entirely. The source's vertical-growth argument applies with the same
gamma factors and coefficient magnitudes. The angular scalar is now
alpha(c)^2, not bar(alpha(c))^2; it must be retained.

The finite Fourier/Gauss calculation is unchanged: the derivative change
occurs after the multiplier calculation. Thus all local B_(p,j),
nonunit zeros, active/inactive choices, fixed-ray classes and reflected
cusp coefficients remain. In the source's physical reflection formula,
replace alpha(ell) by bar(alpha(ell)) and the scalar
-(i/81)bar(alpha(c))^2 by +(i/81)alpha(c)^2, retaining the identical
finite products. Its modulus and all absolute coefficient bounds agree.

For psi=psi0*product_(p|k)chi_p^3, every p|k is active and
c=c0*k. The proof of the source's fixed-ray uniformity uses only that
all these primes are active, not that their exponent is1; therefore the
same finite list of c0 and cusps is valid after the fixed k ray split.
The local transformed factor at k is B_(p,3)=chi_p^1, with its zero.
It is sextic, not quadratic. This adapter does not turn the second
reflection into the old quadratic large-sieve estimate.

## O3. The reflected kernel returns to the original compact profile

Let V be the original smooth compact weight V_* in the source, and put

    g(t)=Gamma(7/6+t)Gamma(5/6+t)
                /[Gamma(7/6-t)Gamma(5/6-t)],
    K=(2pi)^4/27.

The source transform H is

    (HV)(x)=int_(Re t=0) Vhat(-t) g(t)(Kx)^(-t) dt/(2pi i).

Its rapidly decreasing large-x tail and O(x^(5/6-epsilon)) small-x
bound give a Mellin transform on Re t>-(5/6-epsilon). Explicitly,

    (HV)hat(t)=Vhat(-t) g(t) K^(-t).                        (O4)

The meromorphic right side agrees there away from its gamma poles.
The half-plane through the required lines Re t=1/2+epsilon down to
Re t=-2/3 contains no pole. Consequently the source Mellin reflection
argument also applies to U=HV: begin at s>1, shift to s=-1/6, and retain
the entire T_+ and rapid vertical profile decay. No pole of Uhat(s-1/2)
is crossed. The transformation H is still defined by its zero line.

On that line, the identity g(t)g(-t)=1 gives exactly

    H(HV)(x)=int_(0) Vhat(t)x^(-t)dt/(2pi i)=V(x).          (O5)

The same identity holds for a fixed dilation, with the corresponding
inverse dilation. O5 uses the full gamma quotient, not its asymptotic
size. The compact support returns exactly.

## O4. Apply it to the literal standard-cusp all-negative allocation

Retain precisely the PR915 standard infinity-cusp face
ell=lambda^(-3)n b^3,(nb,S)=1. Its fixed additive bad-ray phase can be
expanded into the source's finite multiplicative ray classes. In one
such class the all-negative allocation a=g has, for fixed g,k, inner sum

    sum_n^* sum_b gamma2(n) rho(n) vartheta(n) alpha(n)
                    chi_k(n)^3
              *rho(b)^3 alpha(b)^3 chi_k(b)^3
              /(sqrt(Nn) Nb)
              *(HV)(c Nn Nb^3 B/[Ng^2 Nk^2]),                (O6)

with c>0 fixed on that class and vartheta^3=1. This is exactly the
physical completed T_+ for the finite twist

    psi= rho*vartheta*chi_k^3,
    X=Ng^2 Nk^2/(cB),

and weight U=HV. Its outer coefficient
mu(g)bar(alpha(g))^3 chi_k(g)^3, its g norm weight, and its k/g zero mask
are retained; they do not alter the inner identity. There is no
coprimality mask between g and n or b in this negative allocation.

Apply O2–O3 and O5 to O6. The resulting exact sum is finite for each k;
its number of terms may depend on k. Only the c0/cusp geometry ranges
over a fixed finite list. No uniform bound on the number of terms is
needed for the vanishing argument. Every term has
nonzero dual frequencies ell' in lambda^(-4)O and compact weight

    V(Nell' * X/N(c0*k)^2)
      =V(Nell' * Ng^2/[cB Nc0^2]).                          (O7)

All k conductor powers cancel in this argument. No reciprocal angular
L-function estimate is used. The reflected sextic characters and all
their zeros remain, but compact support alone is now enough for a named
range.

If supp V is contained in (0,b_V], every nonzero ell' has
Nell'>=1/81. The finite fixed-ray family therefore gives a fixed constant

    C_V = 81 b_V max_(classes,c0) c Nc0^2,

such that O6 is identically zero whenever

    Ng^2 > C_V B.                                        (O8)

This is an exact source-qualified support statement for the specified
standard-cusp all-negative component. In particular its dyadic block
G≈A vanishes for sufficiently large balanced A=B=D. The earlier
positive bound Hdual^2 A^2/B for that named component was not sharp in
this range; it had discarded the completed theta cancellation.

## O5. Remaining boundary

O8 concerns the full completed n,b sum and the original transformed
weight on the explicit standard face, after all its fixed bad-ray
components are retained. It does not apply to an arbitrary truncated
theta polynomial, an individually selected n or cube dyad, another
cusp sequence or a coefficient replaced by an arbitrary bounded
envelope. Taking norms or dyadic triangle bounds before the second
reflection loses the cancellation needed for O8.

The other Ramanujan allocations and other cusps remain. In particular
this note does not prove a full balanced fourth moment, the signed
generalized remainder R_k, 17/24 or RH. It pays a specific angular
completion interface and a complete standard-face component, with its
full source hypotheses retained. The coordinator and an independent
height-mechanism reviewer both read O1–O8 against the literal source
and accept this qualified deduction. The exact symbolic controls pass
in normal and optimized Python modes; they authenticate arithmetic,
derivative signs and profile bookkeeping, not the imported automorphy
theorem.

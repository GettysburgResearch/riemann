# Two exact radii for the actual infinite coherent S3 completion

Status: new source-specific theorem, pending frozen-commit review and the
independent Python replay. The preliminary JavaScript atlas suggested the
strata below; the all-field result is proved analytically, not extrapolated
from that finite atlas. This is an after-extension theorem. The separate
extension-order packet treats adjoining the generic algebra before extension.

## 1. Source and precise statement

Let Q be an odd prime power of characteristic greater than three. Fix
A!=0 and 4A^3+27B^2!=0 in F_Q. Retain the previously constructed covers

    E: y^2=x^3+Ax+B,
    D: v^2=-4A^3-27(B-u^2)^2,

and their smooth proper genus-three S3 Galois closure Z. Write a_E,a_D
for the two elliptic Frobenius traces. The source identity is

    H^1(Z)=H^1(D) plus two copies of H^1(E).

The generic coherent grade is R_j tensor chi_u^j, where
R_j=Sym^j(Std) tensor Sym^j(Perm). Let M_n be the actual Koszul Lie grade
of this Segre algebra, with multiplicities A_n^triv,B_n,C_n of the trivial,
sign and standard S3 representations. Set T_n=B_n sign plus C_n Std.
These are the existing source modules, not a replacement fitted to a series.

For even N>=2, extend each source grade first and then adjoin the even
generators j_*T_n, 2<=n<=N. Let H_N denote its full place-Hilbert Euler
function. The degreewise limit H_infinity exists as an integral formal
series, as proved in the companion completion note. Its exact finite ratios
are

    H_N/H_2 = product_(even 4<=n<=N) P_D(z^n)^B_n P_E(z^n)^C_n.  (1.1)

The imported finite-source theorem gives a holomorphic disk
|z|<Q^(-1/[2(N+2)]). In particular a sufficiently large finite N is
holomorphic on any prescribed compact subdisk of the unit disk. We use
this fact before continuing the infinite tail. H_2 alone can have poles
inside the disks considered here when Q is large.

Count rational finite base points as follows. Let g_+ and g_- count
nonzero unramified u for which x^3+Ax+B-u^2 has three distinct rational
roots, separated by chi_Q(u)=+1 and -1. Let g_0 be one or zero according
as the cubic at u=0 splits completely. Let r be the number of old rational
simple C2 branch points, and put delta=1 if Q=1 mod3 and zero otherwise.
The point u=0 is unramified for S3 but ramified for the quadratic twist;
it is not assigned either quadratic sign.

Set

    t=a_D+2a_E,   alpha=t/12,
    nu_+=g_-+alpha,   nu_-=g_++alpha.                         (1.2)

**Theorem ARD.** The Taylor radius of the actual formal H_infinity is

    1/sqrt(2), if both nu_+ and nu_- are nonnegative integers;
    1/2,       otherwise.                                   (1.3)

At the first circle, a nonintegral nu gives a branch, a negative integral
nu gives a pole, and a nonnegative integral nu gives a removable point
with precisely that zero order. In the removable case at least one point
of the second circle is a non-meromorphic branch point. The theorem does
not merely identify a singularity of the pure multiplier in (1.1).

## 2. Exact source congruence and two character scales

The normalized Galois fibre count gives

    #Z(F_Q)=6(g_++g_-+g_0)+3r+2delta,
    t=Q+1-6(g_++g_-+g_0)-3r-2delta.                          (2.1)

An unramified rational fibre contributes six points exactly when Frobenius
is the identity. At a rational old branch the normalizer of C2 is C2,
so the normalized fibre contributes three points. Infinity contributes
two or zero according as its C3 inertia quotient is split or nonsplit.
The old branch set is stable under u->-u and contains no zero, hence r
is even. Since Q+1-2delta is divisible by six, (2.1) proves

    t=6k for an integer k.                                  (2.2)

This is an all-field geometric congruence; the atlas is only a check.

Write d_n,s_n,c_n for the identity, transposition and three-cycle characters
of M_n. The authenticated equivariant PBW formula is

    tr(g|M_n)=(-1)^(n+1)/n sum_(h|n) mu(h)b_(n/h)(g^h),
    b_j(e)=4-(-2)^j,
    b_j(s)=4 if j even and zero otherwise,
    b_j(c)=3 if 3 divides j and zero otherwise.               (2.3)

For even n>=4, canceling the constant terms gives the exact formulas

    d_n=1/n sum_(h|n) mu(h)(-2)^(n/h),
    s_n=1/n sum_(h|n,2|h) mu(h)(-2)^(n/h),
    c_n=1/n sum_(h|n,3|h) mu(h)(-2)^(n/h).                   (2.4)

For c_n, when 3 divides n the otherwise remaining constant is proportional
to sum_(h|n,3 does not divide h)mu(h), which vanishes because n is even.
For s_n, the next nonzero squarefree even divisor after two is at least six.
Thus, with explicit rational errors,

    d_n=2^n/n-(-2)^(n/2)/n+e_d(n),
    s_n=-(-2)^(n/2)/n+e_s(n),
    |e_d(n)|, |c_n| <= [2^(floor(n/3)+1)-2]/n,
    |e_s(n)| <= [2^(floor(n/6)+1)-2]/n.                      (2.5)

The bounds sum the full geometric series over possible distinct quotient
exponents and therefore hold without assumptions on the number of divisors.
Consequently

    B_n=2^n/(6n)+(-2)^(n/2)/(3n)+O(2^(n/3)/n),
    C_n=2^n/(3n)-(-2)^(n/2)/(3n)+O(2^(n/3)/n).               (2.6)

The constants can be read directly from (2.5). The two terms in (2.6),
and not just the leading dimension growth, determine the second circle.

## 3. Three logarithms with a holomorphic remainder

Put

    beta=(a_D-a_E)/6,
    gamma=(a_D^2+2a_E^2-6Q)/24=tr(Frob^2|H^1(Z))/24,
    R=2^(-1/3).

Fix any rho<R. Choose a sufficiently large even N so H_N is holomorphic
on a disk larger than rho and sqrt(Q)*rho^(N+2)<1. The tail in (1.1)
then has the exact logarithmic decomposition, initially for |z|<1/2,

    log K_(>N)(z)
      =alpha log(1-4z^2)+beta log(1+2z^2)
         +gamma log(1-4z^4)+U_N(z),                         (3.1)

where U_N is holomorphic on |z|<rho. Every logarithm is normalized at zero.
Only finite polynomials are changed by omitting the first N terms.

Here are the convergence details. In

    log P_X(z^n)=-sum_(h>=1) tr(Frob_X^h) z^(nh)/h,

the h=1 leading terms of (2.6) give the first logarithm, since
sum_(n positive even)2^n z^n/n=-log(1-4z^2)/2. Their secondary terms give
the second logarithm, since
sum_(n positive even)(-2)^(n/2)z^n/n=-log(1+2z^2)/2.
The h=2 leading terms give the third logarithm. The h=1 residual series
converges when 2^(1/3)|z|<1. The h=2 residual series converges on the
larger disk |z|<2^(-1/4). Finally, for h>=3 the elliptic Weil bound and
sqrt(Q)*rho^(N+2)<1 bound the full tail by a constant times
sum_(n>N)2^n rho^(3n)/n, which converges for rho<R. These estimates also
justify interchanging the sums on compact subdisks. Thus (3.1) is an
analytic identity with a nonvanishing remainder exp(U_N), not a formal
asymptotic expansion near one radial path.

Equivalently, on the branches continued from zero,

    H_infinity(z)=H_N(z) exp(U_N(z))
       (1-4z^2)^alpha (1-2z^2)^gamma (1+2z^2)^(beta+gamma). (3.2)

The finite source H_N contains all initial arithmetic factors. This avoids
assuming the pure K or the original H_2 is holomorphic throughout the same
disk. Coefficient stabilization identifies (3.2) with the formal limit near
zero. The choice of N does not change that germ.

## 4. The genuine finite zeros at the first circle

For every even N>=2,

    ord_(z=1/2) H_N=g_-,    ord_(z=-1/2) H_N=g_+.             (4.1)

We give the finite-extraction argument explicitly. This lemma was also
developed independently in the extension-order packet. The original good
identity-class factor is F_e(t)=(1+2t)/(1-t)^4; the other two conjugacy
classes have no numerator zeros. At a rational completely split point
the argument is chi_Q(u) z, so a simple zero at +1/2 occurs exactly for
negative chi, and a zero at -1/2 exactly for positive chi. Nonrational
places have degree at least two, hence arguments of modulus at most1/4
there, and cannot contribute such a zero.

Use a finite Koszul extraction with cutoff M large enough that Q r^(M+1)<1
on some disk r>1/2. After separating finitely many small-degree places,
the remaining good-place product is normally convergent and nonzero near
both points. Its auxiliary finite-monodromy determinant factors have only
unit-circle roots. Extracted proper or compact cohomological eigenvalues
have weights zero, one or two. A grade-n determinant could vanish at a
point of modulus1/2 only if an eigenvalue had absolute value2^n; this
would force Q=2^(2n) or Q=2^n for positive weight, impossible for odd Q.
Boundary residue-field powers yield the same equality after taking the
degree-th root, so they do not evade this argument.

All genuine bad source factors are units at both points. At an old C2
branch the possibly zero F_e(-1/2) is averaged with F_s(1/2)>0. The new
quadratic point and the two infinity cases retain nonzero even parts.
Their cyclotomic denominators and the adjoined finite generator factors
are units there. The finite cohomological multipliers in (1.1) are also
units by the same odd-Q weight argument. This proves (4.1).

Near +1/2 and -1/2, the other two displayed factors in (3.2) are analytic
units. Therefore the exact orders, allowing a fractional order for a
branch, are precisely nu_+ and nu_- in (1.2). If either is not a
nonnegative integer, (3.2) proves a pole or branch at that point and the
Taylor radius is1/2. There is no smaller singularity: choose the finite N
holomorphic past1/2 and use its normally convergent tail on |z|<1/2.

If both are nonnegative integers, alpha itself is integral. Both possible
poles at +/-1/2 are canceled by the actual finite zeros in (4.1). Equation
(3.2) then extends holomorphically throughout |z|<1/sqrt(2). This is why
a negative integral multiplier exponent alone does not determine the
radius of the full source.

## 5. A parity obstruction guarantees the second singularity

At the real second points z=+/-1/sqrt(2), the possible fractional exponent
in (3.2) is gamma. At the imaginary second points z=+/-i/sqrt(2), it is
gamma+beta. Zeros of H_N add only integers, while exp(U_N) is a unit.

At least one of gamma and gamma+beta is nonintegral. Indeed write t=6k
and a_D=6k-2a_E. Then

    beta=k-a_E/2,
    gamma=(6k^2-4k a_E+a_E^2-Q)/4.                           (5.1)

If a_E is odd, beta is a half-integer, so the two exponents cannot both
be integral. If a_E is even, the numerator of gamma is odd because Q
is odd. Thus gamma is already nonintegral. In either case a finite zero
of H_N cannot remove all second-circle branch points. Since R>1/sqrt(2),
the remainder in (3.2) is holomorphic across those points. This proves
the upper bound in the removable case and completes Theorem ARD.

## 6. Discovery, examples, and scope

The first independent JavaScript scout enumerated every admissible A,B
over p=5,7,11,13,17,19,23,29,31, a total of3044 parameter choices. It
compared complete quadratic point counts with complete cubic fibre counts.
These are parameter rows, not distinct isomorphism classes of curves.
The subsequent source-bound Python replay must reproduce these rows and
check (2.3)--(2.6) independently; no passing execution is claimed here yet.

For example over F11, A=1,B=3 gives t=-12 and g_+=g_-=2. The pure
multiplier has poles at the first circle, but the full source has zero
order1 at both points and radius1/sqrt(2). Over F13, A=4,B=1 gives t=-12,
g_+=2,g_-=0, so the full source has a pole at+1/2 and radius1/2. These
examples separate genuine source cancellation from a scalar trace test.

The trace-class threshold of the explicitly normed direct-sum Frobenius
operator remains1/2. The scalar continuation to1/sqrt(2) does not improve
that operator ideal. Every finite H_N still has its own larger guaranteed
disk approaching one. No infinite-rank constructible sheaf, canonical
topology, archimedean object, principal number-field member or RH theorem
is asserted.

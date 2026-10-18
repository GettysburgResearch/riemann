# A legal Gaussian-coordinate filter, with the principal response retained

Status: **PROPOSED exact component identity.** This changes a different
coordinate from the radial W0 profile in ../CROSS_ROUTE.md. It does not
establish a new bound for the resulting signed arithmetic sum.

Use the Gaussian P_G and complete B_m of CT `eq:B`, including every
squarefree c, every unrestricted n, their common primes, and nonunit zeros.
CT here means Cureton--Thorner, Hexagon 2610.00200v2, source
[DedekindZeta.tex](https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex),
SHA256 f54808ad0f967b5429c7ac30d7b27ff25671e02d7fb43cf753b2b826c9d35df4.
That source requires mu_12 in F. It is NOT silently specialized to Q(omega).
The identities below hold in any one fixed field satisfying that interface;
Q(zeta_12) is one such choice.

Fix r>1 and lambda>=1/6, independent of all large parameters. Replace

    P_G(y) by P_*(y)=P_G(y)-r^lambda P_G(r y).             (1)

Then the defining native sum gives, pointwise and absolutely,

    B_*(Z)=B_m(Z)-r^lambda B_m(Z/r).                     (2)

This is a signed profile; no positivity is used in this identity. CT's
global construction obtains its Gaussian by the entire multiplier
exp(s^2)/Vhat(s). Replace it by

    [1-r^(lambda-s)] exp(s^2)/Vhat(s).                   (3)

The multiplier is entire and decays faster than any power on each fixed
vertical strip. Both realizations are a finite linear combination of the
two original smooth vectors. Thus no interchange of an infinite signed
sum with an uncontrolled representation norm occurs.

In the reflected expansion B_m(Z)=sum_nu E_m(nu) Phi(Z|nu|), the same
operation gives

    Phi_*(x)=Phi(x)-r^lambda Phi(x/r).                   (4)

For each j=0,1,2, CT's bound on (x partial_x)^j Phi is preserved, with a
fixed factor at most 1+r^(lambda+A)+r^(lambda-1/8) after taking the relevant
small/large-x envelopes. This pays the complete tail, rather than cutting
the smoothing off at a finite radius. Every squarefree and quadratic
interaction coefficient E_m(nu) remains exactly the original one.

Hold X,Y fixed when applying (2) to the physical I(X,Y,Z). Its triple
Mellin formula has Z^(xi+z-1). Therefore its entire integrand is multiplied
by

    1-r^(lambda-(xi+z-1)).                              (5)

At the principal double residue w=1,z=1/6, the resulting Mellin numerator
is

    [1-r^(lambda+5/6-s)] exp[(s-5/6)^2] H(s)/zeta_F^S(s). (6)

The scalar c0=(R_S^2/6) M_W0(1/6) W1hat(1) remains the same nonzero scalar
as in the original principal extraction, when those two profile values
were chosen nonzero. In particular the filter in (1) does NOT impose
M_W0(1/6)=0. This is why the radial no-go in ../CROSS_ROUTE.md does not
apply to this distinct coordinate.

All zeros of the bracket in (6) lie on Re s=lambda+5/6>=1. Thus the bracket
does not cancel any hypothetical nontrivial zero of the target zeta
function. Boundary zeros of the bracket at Re s=1 when lambda=1/6 are
harmless for zero detection in the open critical strip. With r=64 and
lambda=1/3, the two coefficients are exactly 1,-4, total mass 5, and all
bracket zeros lie on Re s=7/6.

There is a small scale issue worth making explicit. If X=Y=Z^a in the
original extraction, and b_a=5/6-a/3, the second physical term in (2) has
X,Y fixed at Z^a, rather than reset to (Z/r)^a. Its principal expression is

    f_a(Z)-r^(lambda+a/3) f_a(Z/r),                     (7)

not f_a(Z)-r^lambda f_a(Z/r). The Mellin shift b_a in (7) gives exactly
the bracket in (6).

If an explicitly identified nuisance were exactly homogeneous Z^lambda,
(2) would annihilate it with bounded coefficient mass while preserving
all target zeros. This conditional cancellation is algebraically exact.
It is not a license to label every cubic bias as Z^lambda: the actual
native angular correction, the cubic completion, frequency m, and all
shared-prime factors must first identify that precise component. Existing
absolute estimates applied separately to the two terms have the same
power exponent. No improved exponent or native full-energy upper bound
is obtained just by (1)--(7).

The differential alternative (y partial_y+lambda)P_G multiplies (6) by
lambda+5/6-s. It is also zero safe, but its reflected profile needs one
additional controlled derivative if the original interface supplies only
j<=2. The finite difference above avoids importing that extra regularity.

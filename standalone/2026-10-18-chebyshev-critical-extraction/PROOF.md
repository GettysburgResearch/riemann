# Polynomial-cost extraction of the complete critical prime source

Status: PROPOSED complete unconditional component proofs; independently unreviewed.
No RH proof, new zero-free half-plane, or critical arithmetic upper estimate.
Chebyshev interpolation and its analytic convergence are classical. The new
claim is the quantitative replacement of #980's real binomial stencil for
its SAME complete arithmetic translation family, including the true pole
continuum, growing order, and raw-source coefficient cost.

## 1. Fixed field, original translations, and exact normalization

Fix a number field F, a finite set S of prime ideals, and c in R. All ideals
are nonzero integral ideals outside S. Equal rational norms do not identify
ideals. Write Z(s)=zeta_F^S(s), with residue kappa>0 at one. Define

 W_c(y)=y^(-c) exp[-(log y)^2/4]/(2 sqrt(pi)),
 a_h(I)=sum_(AB=I) mu_F(A)(NB)^(-h),
 S_h(X)=sum_I a_h(I) W_c(NI/X),
 J_h(X)=integral_1^infinity y^(-h) W_c(y/X) dy.             (1)

The convolutions include common factors. Complex powers use real logarithms
of ideal norms. The a_h are a DEFORMATION of Mobius, not the original mu_F.
The exact local factor is

 a_h(p^j)=(q^(-h)-1)q^(-(j-1)h), j>=1; a_h(1)=1.        (2)

In initial absolute convergence their series is Z(s+h)/Z(s). In particular
-a'_0(I)=Lambda_F^S(I) for I!=1, including ZERO for every non-prime-power
ideal. No prime ideals or powers are dropped.

Choose once 0<H<=1/16 so small that

 k(h)=-kappa/[h Z(1-h)]

is holomorphic on an OPEN neighborhood of |h|<=4H, with k(0)=1. Such an H
exists from the Laurent expansion Z(1-h)=-kappa/h+O(1). It requires no new
zero-free theorem. H and all constants can depend on F,S. No effective
uniform H over fields or numerical certificate of H is claimed.

Define, with a removable value at h=0,

 B(h,X)=[W_c(1/X)-S_h(X)]/h - k(h)J_h(X),
 P(X)=sum_I Lambda_F^S(I)W_c(NI/X)-J_0(X).               (3)

Then B(0,X)=P(X). These are precisely #980's B_h and P, with its k(h) renamed
to avoid confusion with the Gaussian c. The continuum is EXACT and one-sided:

 J_h(X)=(1/2) X^(1-h) exp[(1-h-c)^2]
                  erfc[-(log X+2(1-h-c))/2].            (4)

Equation (4) extends analytically to complex h; the integral in (1) is the
primary definition. It is not replaced by its large-X leading exponential.

## 2. A complex-parameter bound for the FULL infinite arithmetic source

### Lemma 1

B(h,X) is holomorphic for |h|<4H. For X>=2,

 sup_(|h|<=2H)|B(h,X)| <= C X^(1+2H)(1+log X)^2.        (5)

The constant depends on F,S,c,H, not the interpolation order below.

Proof. Let d_2(I) be the number of ordered ideal factorizations. For I!=1,
a_0(I)=0, and differentiating the finite divisor sum gives

 |a_h(I)/h| <= d_2(I) log(NI) (NI)^(2H), |h|<=2H.      (6)

One can derive (6) without dividing by a small h, by integrating a'_(th)
over 0<=t<=1. For the analogous local uniform convergence on |h|<4H use a
slightly larger fixed radius in the same estimate. Gaussian decay dominates
every fixed norm power and logarithm, justifying local normal convergence
of S_h and its derivatives, and the removable value in (3).

Elementary fixed-field ideal counting gives I_F(Y)<=C_F Y for Y>=1. Thus

 sum_(NI<=Y) d_2(I) <= C_F Y sum_(NA<=Y)1/NA
                    <= C'_F Y log(2Y).                 (7)

Apply (7), (6) in all dyadic norm bands. For NI>=X, write NI~2^j X. The
bound for that band is X^(1+2H) times a polynomial in j+log X times a
Gaussian exp(-c1 j^2+c2|j|). The sum converges. For NI<X use the downward
bands 2^j X with j<0 until the unit scale; the same Gaussian dominates.
A band whose lower endpoint is below one is treated using NI>=1, not
as if nonzero ideals had norm below one. This proves the RHS of (5) for
the first term of (3), including ALL bands and the unit removal.

For the continuum use |y^(-h)|<=y^(2H), y>=1, and extend its positive
majorant to y>0. Substitution y=Xv evaluates the latter integral as
X^(1+2H) exp[(1+2H-c)^2]. k is bounded on the indicated disk. This proves
(5). All interchanges are dominated on compact h disks. QED.

The power 1+2H in (5) is an absolute majorant, NOT square-root cancellation.
It is used only to control interpolation error.

## 3. Endpoint extraction using ONLY strictly positive real shifts

For m>=1 put

 theta_j=(2j-1)pi/(2m), x_j=cos(theta_j),
 h_j=H(1-x_j)/2=H sin^2(theta_j/2),
 w_j=(-1)^(j-1) cot(theta_j/2)/m, 1<=j<=m,
 D_m(X)=sum_(j=1)^m w_j B(h_j,X).                       (8)

No sample at h=0 is taken. Every sample is in (0,H).

### Lemma 2 (exact polynomial extraction and conditioning bounds)

For every polynomial f(h) of degree <m,

 sum_j w_j f(h_j)=f(0).                                (9)

Moreover

 sum_j w_j=1,
 sum_j |w_j| <= 2+log(2m),
 min_j h_j >= H/(4m^2),
 sum_j |w_j|/h_j <= 10m^2/H,
 sum_j w_j^2=(2m-1)/m.                                (10)

Proof. T_m(x_j)=0, T_m(1)=1, and
T'_m(x_j)=m(-1)^(j-1)/sin(theta_j). The Lagrange basis evaluated at x=1
is 1/[(1-x_j)T'_m(x_j)], exactly w_j. This proves (9).

Put t_j=theta_j/2. On (0,pi/2), cot t<=1/t and sin t>=2t/pi. Therefore

 |w_j|<=4/[pi(2j-1)],
 h_j>=H(2j-1)^2/(4m^2),
 |w_j|/h_j<=8m^2/[H(2j-1)^3].                          (11)

The first odd harmonic sum is <=1+(1/2)log(2m-1). This gives the second
part of (10), with room, also for m=1. The sum of (2j-1)^(-3) is at most
1+integral_1^infinity(2x-1)^(-3)dx=5/4, proving the raw-cost bound.

Let K_m(x)=1+2 sum_(l=1)^(m-1)T_l(x). At x=x_j, the Dirichlet-kernel
identity gives K_m(x_j)=(-1)^(j-1)cot(theta_j/2)=m w_j.
The m-point Chebyshev root quadrature is exact through degree 2m-1.
Alternatively expand products of cosines and sum the finite geometric
series. It gives (1/m)sum_j K_m(x_j)^2=2m-1, proving the last equality.
The same identities follow algebraically modulo T_m. QED.

### Lemma 3 (complete analytic remainder)

For every m>=1 and X>=2,

 |D_m(X)-P(X)|
 <= C X^(1+2H)(1+log X)^2 [3+log(2m)] 2^(-m).           (12)

Proof. Write f_X(x)=B(H(1-x)/2,X). The Bernstein ellipse of parameter 2
has max|x|=5/4; hence |H(1-x)/2|<=9H/8<2H. Lemma 1 bounds f_X there
by M_X=C X^(1+2H)(1+log X)^2, on an open neighborhood of the closed
ellipse. The classical Laurent-circle proof of Chebyshev decay is short:
f_X((z+z^-1)/2) is analytic in an annulus containing 1/2<=|z|<=2 and is
invariant under z -> z^-1. Cauchy's formula on |z|=2 gives Chebyshev
coefficients |c_l|<=2 M_X 2^-l, l>=1. Consequently its degree-(m-1)
Chebyshev truncation q has sup error on [-1,1] at most 4 M_X 2^-m.
Both the endpoint functional and interpolation in (9) are exact on q.
The error is thus at most (1+sum|w_j|)4 M_X 2^-m. Absorb the factor 4
into C and apply (10). This proves (12). No fixed-m asymptotic constant
is being reused as m grows. QED.

### Theorem A (arbitrary accuracy with logarithmic raw amplification)

Fix ANY accuracy exponent A>0. Choose, for X>=2,

 m_A(X)=ceil[(A+3+2H)log(X)/log 2],
 D_A(X)=D_(m_A(X))(X).                                 (13)

Then

 |D_A(X)-P(X)| <= C_A X^(-A),                           (14)

and the following bounds hold as X grows:

 number of translations = O_A(log X),
 absolute mass on the B samples = O_A(log log(3X)),
 smallest shift >= c_A H/(log X)^2,
 absolute mass on the raw S_h samples <= C_A(log X)^2/H. (15)

Indeed 2^-m<=X^(-A-3-2H), and the remaining logarithmic factor in (12)
is bounded by C_A X^2. Thus (14) follows with a constant independent of
the GROWING order. Equations (10) prove (15). The raw unit coefficient
is no larger than the raw sample mass. The coefficients on the unweighted
continuum samples have total mass <=sup_[0,H]|k| sum|w_j|; their actual
sizes have not been bounded at square-root order.

Compared with #980: that construction uses O(sqrt(log X)) samples, minimum
shift exp[-4sqrt(log X)], and raw coefficient mass at most
2exp[(4+log2)sqrt(log X)] for its error X^-5/4. Theorem A uses MORE samples,
but shifts only inverse-log-square close to zero and raw mass O(log^2 X),
for any fixed requested error power. It does not bound the separately
cancelling size of those samples, or give a fast algorithm for their
infinite ideal sums. It is not a claim of relative numerical stability.

## 4. This raw-cost order is optimal for the declared polynomial task

Suppose h_j are ANY positive nodes in (0,H], and a linear functional
sum_j alpha_j f(h_j) reproduces -f'(0) for every polynomial f of degree
<=m with f(0)=0. Then

                 sum_j |alpha_j| >= m^2/H.             (16)

Use f(h)=T_m(1-2h/H)-1. It vanishes at zero, has sup norm <=2 on [0,H],
and |-f'(0)|=2m^2/H. The triangle inequality proves (16). Our weights
alpha_j=-w_j/h_j reproduce that derivative: f(h)/h has degree <m, so
(9) applies. Thus the upper bound 10m^2/H is within a fixed factor of
the lower bound for ANY such real-positive, polynomial-exact stencil.
This is an elementary Chebyshev/Markov extremal fact, not an arithmetic
lower bound for P or a no-go theorem for RH. Source-specific nonlinear
methods lie outside it.

## 5. A simultaneous root-norm transfer

Take A=2 for definiteness. For every 1<=p<=infinity and T>=2,

 | ||D_2/sqrt X||_(Lp([2,T],dX/X))
          -||P/sqrt X||_(Lp([2,T],dX/X)) | <= C_*.      (17)

The SAME constant works for all p,T. By (14) the difference is at most
C X^-5/2. Its Lp norm for finite p is <=C 2^-5/2 (2/(5p))^(1/p), uniformly
bounded; at infinity use its supremum. Minkowski proves (17). Values at
ceiling jumps in m are measurable and obey the same pointwise theorem.
Equation (17) is a TRANSFER, not an upper bound for either norm.

The companion FIXED_SHIFT_TARGET.md replaces changing nodes by a fixed
positive measure in h, proves a quantitative energy comparison, and records
the precise unsolved arithmetic estimate and why family-density bounds do
not provide it.

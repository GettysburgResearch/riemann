# Growing-order finite translations at critical scale

Status: PROPOSED complete unconditional component theorem. Independent review
required. The estimates here use elementary ideal counting, finite differences
and the classical local pole of zeta, NOT quasi-RH or an unknown moment.
They do not bound the prime-versus-continuum discrepancy itself.

Use exactly the definitions, exclusions and constants in FINITE_TRANSLATIONS.
In particular P(X) is the COMPLETE Gaussian prime-power sum minus J_0(X),
and B_t(X) includes the ACTUAL shifted-pole counterterm c(t)J_t(X).

## 1. The finite stencil and an identity with a positive remainder

For integers m>=1 and 1<=j<=m put

    b_(m,j)=(-1)^(j-1) binom(m,j),
    D_(m,h)(X)=sum_(j=1)^m b_(m,j) B_(jh)(X),          (1)

initially assuming mh<=r. All sums over ideals inside (1) remain infinite
Gaussian sums; the number of transverse evaluations, not their column support,
is finite. For u>=0 define

 g_(m,h)(u)=(1/h)sum_(j=1)^m [b_(m,j)/j](1-exp(-jhu))
           =(1/h)sum_(l=1)^m (1-exp(-hu))^l/l.        (2)

The second equality follows by differentiating both polynomials in
x=exp(-hu) and setting x=1. Consequently

 0<=u-g_(m,h)(u)
   <= h^m u^(m+1) exp(hu)/(m+1).                     (3)

Indeed the omitted tail of -log(1-v), v=1-exp(-hu), is at most
v^(m+1)/[(m+1)(1-v)], and v<=hu. This uniform bound is valid for all u>=0,
not only for a truncated logarithmic range.

Write T_(m,h)=sum b_(m,j)T_(jh). By the exact ideal convolution and unit
subtraction, its I-coefficient is

    sum_(A B=I) mu_F(A) g_(m,h)(log NB).

The same convolution with log NB is L_F(I). Thus, including I=1,

 |coeff_I(T_(m,h))-L_F(I)|
   <= tau_F(I) h^m (log NI)^(m+1)(NI)^h/(m+1),        (4)

where the unit has zero error and tau_F counts ideal divisors. This pays for
EVERY coefficient outside the prime-power support as well as the errors on
prime powers. There is no independence argument or selection of a finite sector.

## 2. A weighted count uniform in the growing order

Elementary ideal counting I_F(x)<=C_F x implies

 sum_(NI<=x) tau_F(I)
    =sum_(NA NB<=x)1 <= C_F x(1+log x).               (5)

For X>=e and 0<=v<=2, dyadic Gaussian annuli then give uniformly in v

 sum_I tau_F(I)(NI)^v W_c(NI/X)
       <= C_(F,c) X^(1+v)(1+log X).                 (6)

For clarity, on NI/X in [2^j,2^(j+1)), (5) and the supremum of y^v W_c(y)
bound the term by X^(1+v) times a polynomial in |j| and 1+log X, multiplied
by exp(-c1 j^2+c2|j|); c1>0 and c2 are uniform on v in [0,2]. Summation
includes all positive and negative j with any actual ideal present. This proves
(6) without a cutoff that depends on m or h.

Put L=log X. For any integer q>=0 and NI>1,

    (log NI)^q <= L^q (NI/X)^(q/L),                  (7)

because log(1+v)<=v for v>-1; q=0 has its usual value one. Equations (4),(6),(7)
therefore imply, whenever 0<h<=1/4 and h+(m+1)/L<=2,

 |T_(m,h)(X)-P_raw(X)|
   <= C h^m X^(1+h) L^(m+2)/(m+1), L>=1.            (8)

The constant is INDEPENDENT of m,h,X in this range. This independence follows
from (7), rather than taking an uncontrolled constant in a fixed-order moment.

## 3. The whole continuum stencil, with the same high-order cancellation

The weights in (1) obey

 sum_j b_(m,j)=1,
 sum_j b_(m,j)j^l=0 for 1<=l<m.                     (9)

Thus sum b_(m,j)f(jh) is the degree-(m-1) interpolation formula for f(0).
For a C^m function on [0,mh] its error is at most

    h^m sup_(0<=t<=mh)|f^(m)(t)|.                    (10)

The product of node distances is m! h^m and the divided-difference bound
is sup|f^(m)|/m!, proving (10), also for complex-valued functions by the
integral representation of divided differences.

Take f(t)=c(t)J_t(X). Differentiating under the complete continuum integral is
justified by Gaussian domination. For 0<=l<=m<=L and t>=0, (7) applied to y>=1
and the Gaussian Mellin integral give

    |J_t^(l)(X)|<=C_c X L^l.                         (11)

Explicitly the upper bound is L^l X^(-l/L) integral_1^infinity
 y^(l/L)W_c(y/X)dy, and the full integral over y>0 equals
X^(1+l/L)exp((1+l/L-c)^2). It is uniform for l/L in [0,1].
By (7) of FINITE_TRANSLATIONS and Leibniz,

 |f^(m)(t)|<=C X L^m sum_(i=0)^m (m)_i/(rL)^i
           <=2C X L^m,                              (12)

provided mh<=r and m<=rL/2. The falling factorial (m)_i is at most m^i.
Combining (9)-(12) proves

 |sum_j b_(m,j)c(jh)J_(jh)(X)-J_0(X)|<=C X(hL)^m.     (13)

The pole coefficient c(t), not just X^(1-t), has been differentiated. There
is no replacement of the exact continuum by an asymptotic residue term.

## 4. A concrete growing-order theorem with subpower coefficient mass

For all sufficiently large X (depending only on F,S,c), set

    L=log X, m(X)=ceil(sqrt(L)), h(X)=exp(-4 sqrt(L)),
    D(X)=D_(m(X),h(X))(X).                            (14)

There are constants X0 and C, independent of X and m(X), such that

                  |D(X)-P(X)| <= C X^(-5/4), X>=X0. (15)

The absolute coefficient mass of the linear combination of the original
S_(jh)(X) evaluations in (14) is at most

 sum_j |b_(m,j)|/(jh)
       <=(2^m-1)/h
       <=2 exp[(4+log 2)sqrt(log X)] = X^o(1).       (16)

The separate unit-term coefficient is no larger than this bound. The continuum
coefficients have mass at most 2^m-1. Equation (16) bounds these absolute linear
coefficients; it is not a relative numerical condition number, a fast evaluation
algorithm, or a bound for the sizes of the separately cancelling sources.

Proof of (15). Choose X0 so L>=16, mh<=r, m<=rL/2, h<=1/4 and
h+(m+1)/L<=2. All conditions hold eventually. Also X^h=exp(L exp(-4sqrt L))
is bounded by an absolute constant. Since m>=sqrt L and m+2<=sqrt L+3,

 h^m<=exp(-4L),
 (m+2)log L <= L+3L/4 =7L/4.                         (17)

The last bound uses log L<=sqrt L and log L<=L/4 for L>=16. Inserting (17)
into (8),(13) gives C exp[(1-4+7/4)L]=C X^(-5/4). This proves (15) uniformly
for the explicit GROWING order. Ceiling jumps in m cause no problem for this
pointwise estimate or the later measurable integral. Equation (16) follows
from m<=sqrt L+1. QED.

This is an all-order finite-translation theorem. It is NOT the requested
all-order upper bound for native Mobius moments. Its concrete gain over a
single h=1/X difference is that the same critical accuracy is obtained using
only subpower-small shifts and subpower absolute coefficient mass, with all
composite and continuum errors proved uniformly in the growing order.

## 5. One bounded root cost for ALL critical Lp energies

Set f(X)=D(X)/sqrt X and g(X)=P(X)/sqrt X. Equation (15) gives

    |f(X)-g(X)|<=C X^(-7/4), X>=X0.                  (18)

For any D>=X0 and every REAL 1<=p<infinity, write

    N_p(f;D)=[integral_(X0)^D |f(X)|^p dX/X]^(1/p).

Then there is a single constant C_* independent of p and D such that

           |N_p(f;D)-N_p(g;D)|<=C_*.                 (19)

The same is true for p=infinity with the essential supremum. Indeed the
error norm is at most C X0^(-7/4)(4/(7p))^(1/p), uniformly bounded for p>=1;
Minkowski proves (19). This is a simultaneous, bounded-root-cost ALL-p transfer,
including orders varying with D. It does not independently bound either norm.

## 6. The precise remaining critical estimate and why it is still open

The still-unproved arithmetic statement is

 integral_(X0)^D |D(X)|^2 dX/X^2 <<_epsilon D^epsilon
                  for EVERY epsilon>0.              (OPEN-T)

The moving h(X) and m(X) do NOT have the fixed-t Mellin formula (10) in
FINITE_TRANSLATIONS. We first use the uniform error to return to P, and only
then take the Mellin transform of that FIXED source.

Through (19) this is equivalent to the same assertion for P. It would imply
RH for zeta_F. Here is the complete sufficiency argument, to make clear where
the unproved input enters. Absolute Fubini on Re s>1 gives

 integral_0^infinity P(X)X^(-s)dX/X
   =exp((s-c)^2)[-Z'(s)/Z(s)-1/(s-1)].                (20)

At X=0 the original prime sum and the one-sided continuum are flat. On each
dyadic X block at infinity, Cauchy-Schwarz and the transferred OPEN-T bound
make (20)'s integral converge normally whenever Re s>1/2: choose epsilon
smaller than twice the distance to 1/2. The fixed initial interval is harmless.
The right side would thus be holomorphic in that half-plane. Every zero rho
of Z there gives residue -multiplicity(rho) exp((rho-c)^2), which cannot
vanish. The pole of Z at one has already been subtracted. Analytic uniqueness
and the functional equation yield the critical-line conclusion.

Conversely RH implies g(X) is bounded and hence OPEN-T. This is the classical
Gaussian explicit-formula argument already written in #962 PRIME_DETECTOR.md,
Sections 1-4, not new here. For the precise normalization, put x=log X and
d=c-1/2. Completing the square gives EXACTLY

    g(exp x)=exp(d^2) P_(a=1,t=0)^(#962)(x-2d).       (21)

Both the prime sum and its one-sided continuum obey this identity. Under RH
the nontrivial-zero part is an absolutely convergent trigonometric series
with Gaussian weights and multiplicity coefficients. The missing-S zero grids
lie on Re s=0 and decay in critical coordinates. A fixed left contour at
Re s=-1/4 pays the remaining terms; it is not moved to minus infinity through
Gaussian-growing trivial-zero weights. Classical fixed-field zero counting
O((1+T)log(3+T)) and the functional equation justify that statement. It implies
N_p(g;D)=O((log D)^(1/p)) for fixed p, and g=O(1). Equation (18) transfers it
to f. This direction assumes RH; it is not a new unconditional growth bound.

Therefore OPEN-T, boundedness of the compiled critical source, and RH are
logically equivalent at this scope. Neither small translation size nor (16)
proves OPEN-T. The remaining cancellation is between the prime-power sum and
its continuum, not among the already bounded non-prime-power coefficients.
An absolute bound for each positive term only gives an order-X bound before
critical normalization; it cannot supply the missing square-root cancellation.

This changes the algebraic realization of the critical target, not its proof
status. A full physical CT transverse projection with all test factors and tails
is also not constructed by this arithmetic finite-translation theorem.

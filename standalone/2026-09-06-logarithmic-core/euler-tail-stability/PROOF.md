# Native slow variation, sharp tail precision, and Euler-product controls

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
RH and native positivity at unbounded scales are NOT proved.
Parent: PR #803 at 93e5d45b63f6a9a60f981e81df589feff1ba1cfb.
Local labels ET1--ET6 are not canonical claim IDs.

This pass attacks a proposed bridge from local positivity to the full signed
annular estimate. It establishes actual, all-scale regularity and a precise
comparison theorem, then tests the proposed bridge inside meromorphic Euler
products, rather than only arbitrary continuous comparison measures.

The counterfamily is NOT zeta. Its local factors above the preserved prefix
are different, and its completion fails the Riemann functional equation.
It is not a refutation of RH or of any theorem that requires the literal
unit Euler factors and the complete functional equation. The selected global
parameters exist by the proof below; no particular numerical pair is claimed
certified. Finite checks do not prove the analytic arguments.

## 1. Keep the native arithmetic normalization

For positive u set

    w(u)=u/3-1/(192u^2),        1/4<u<=1,
         1/(3u^2)-u/192,       1<u<=4,
         0,                   otherwise.

The outside endpoint values are zero and the pieces agree at 1. In particular,

    0<=w(u)<=21/64,  integral w(u)du=45/128=:a.

For a real arithmetic source lambda(n), supported on integers n>=2, define

    P_lambda(X)=X^(-1/2) sum_n lambda(n)w(n/X),
    D_lambda(m)=P_lambda(m^2)-a m+1/4,       m>=2.            (1)

Every sum is finite. The native source is lambda=Lambda, including ALL prime
powers. We write D=D_Lambda and psi(x)=sum_(n<=x)Lambda(n).
These are precisely the parent's D(m) and B(m)/(192m^3)-45m/128+1/4.
Changing the prime-power weights changes the source; no notation conceals it.

The two inherited analytic facts used only for the terminal comparisons are:

* For the native source, eventual D(m)>=0 at every integer m implies RH.
* RH implies D(m)>1/10 at every real m>=2.

Their complete fixed-filter/Landau proofs are in the pinned annular parent.
The new comparison results do not assume those native estimates hold.

## 2. ET1: an unconditional, scale-independent slope bound

### 2.1 An elementary Chebyshev bound including prime powers

For every real x>=1,

    psi(x)<3x.                                             (2)

For an integer n>=1, prime valuations of the central binomial coefficient give

    log binom(2n,n)
      =sum_(p,k>=1) log(p)[floor(2n/p^k)-2floor(n/p^k)].

Every bracket is 0 or 1, and it equals 1 when n<p^k<=2n. Therefore

    psi(2n)-psi(n)<=log binom(2n,n)<=2n log 2.

Telescope at n=1,2,... through the powers of two (not all consecutive n):
psi(2^j)<2^(j+1)log 2. Bounding x by its next power of two gives
psi(x)<4(log 2)x<3x. The last inequality follows, for example, by the first
four positive terms of exp(3/4), which already exceed 2. No PNT is used in (2).

### 2.2 Differentiate the exact finite sum, not a main-term approximation

Away from the locally finite activation knots in m,

    D'(m)=m^(-2)sum_n Lambda(n)v(n/m^2)-a,                  (3)
    v(u)=-w(u)-2u w'(u)
        =-u-1/(64u^2),     1/4<u<1,
         1/u^2+u/64,       1<u<4,
         0,               otherwise.

The knots are m=sqrt(n)/2,sqrt(n),2sqrt(n) for prime powers n. D is continuous
at all of them, including the central change of formula. It is locally
absolutely continuous, since on every compact m interval it is a finite sum
of continuous piecewise smooth functions. All derivative statements below
are almost-everywhere statements and then integrated legitimately.

On [1/4,1], 0<u+1/(64u^2)<=65/64. One exact certificate is

    65/64-u-1/(64u^2)
      =(1-u)(64u^2-u-1)/(64u^2)>=0.

The second factor is positive throughout that interval. Consequently the
negative part of the sum in (3) has magnitude at most (65/64)psi(m^2).

On [1,4], g(u)=u^(-2)+u/64 is positive and decreasing. With X=m^2,
Stieltjes integration, retaining the lower endpoint, yields

    sum_(X<n<=4X)Lambda(n)g(n/X)
       =g(4)psi(4X)-g(1)psi(X)-integral_1^4 psi(Xu)g'(u)du
       <=3X[g(1)+integral_1^4 g(u)du]
       =(723/128)X.

Here g(1)=65/64 and integral_1^4 g=111/128. Dropping the negative part for
an upper bound, or the positive part for a lower bound, proves

    -435/128 <= D'(m) <=339/64,          a.e. m>=2.         (4)

In particular, for all real m,n>=2,

    |D(m)-D(n)| <=(339/64)|m-n|.                           (5)

This removes the logarithmic loss in the parent's elementary square-grid
interpolation. It is a regularity theorem, not a positive lower bound.

### 2.3 The actual slope tends to zero

Let R(x)=psi(x)-x and extend v by zero. The derivative v is understood here
as a signed measure, INCLUDING the jumps at 1/4,1,4. Direct integration gives
integral v(u)du=a. If t0=2^(-5/3), the exact total variation is

    Var(v)=81/16-3t0 <33/8.                                (6)

Indeed u+1/(64u^2) has its unique minimum at t0, of value 3t0/2. Adding the
two outer jumps, both monotone pieces on the left, the central jump 65/32,
and the monotone right piece gives (6). The strict upper bound uses
(5/16)^3<1/32, hence t0>5/16. No central delta is discarded.

For m away from the knots, another exact Stieltjes integration gives

    D'(m)=-(1/m^2)integral_[1/4,4] R(m^2u) dv(u),
    |D'(m)| <=(33/(8m^2))
                   sup_(m^2/4<=y<=4m^2)|psi(y)-y|.        (7)

The classical unconditional PNT, psi(y)=y+o(y), now implies that the essential
supremum of |D'| on [M,infinity) tends to zero as M tends to infinity.
In particular, for each fixed H0<infinity,

    sup_(|h|<=H0) |D(m+h)-D(m)| ->0                         (8)

as m->infinity, restricting to m+h>=2. The PNT is imported; no effective
threshold or derivative convergence rate is asserted. Slow variation does
not exclude slowly varying, unbounded oscillations.

## 3. ET2: the exact coefficient-precision threshold

Suppose two sources differ by delta(n), with

    |delta(n)| <= C Lambda(n)n^(-eta),    eta>=0, C>=0.     (9)

This includes all prime powers separately, not just primes. No agreement
of safe moments is needed for this comparison theorem. Positivity of w gives

    |D_(Lambda+delta)(sqrt X)-D(sqrt X)|
       <= C X^(-1/2)sum_n Lambda(n)n^(-eta)w(n/X).          (10)

As an operator bound over ALL signed perturbations satisfying (9), (10) is
sharp: delta(n)=C Lambda(n)n^(-eta) attains equality simultaneously for every X.
This extremizer need not satisfy the extra Euler/moment constraints of Section 4.
Using (2) and 0<=w<=21/64 supplies the explicit all-scale estimate

    |Delta D(sqrt X)| <=(63/16)4^eta C X^(1/2-eta), X>=4.  (11)

For each fixed eta, the PNT and partial summation sharpen this to

    X^(-1/2)sum Lambda(n)n^(-eta)w(n/X)
       ~ J(1-eta) X^(1/2-eta),                            (12)

where J is the entire Mellin transform of the compact weight,

    J(z)=integral_(1/4)^4 w(u)u^(z-1)du
        =A(z-1/2)/[9/4-(z-1/2)^2],
    A(r)=65/64-(4^r+4^(-r))/8.                            (13)

At apparent singularities z=-1,2 use the removable values given by the integral.
For real z, J(z)>0. The exact critical value is

    J(1/2)=49/144.                                         (14)

For completeness, the PNT step is uniform only for a fixed compactly supported
piecewise-C1 test f: integration by parts of sum Lambda(n)f(n/X)-X integral f
bounds the error by Var(f)sup_(X/4<=y<=4X)|R(y)|=o(X).
Take f(u)=u^(-eta)w(u). The same proof works for fixed complex exponents.
No uniformity as eta or an imaginary part varies with X is used.

Thus eta>1/2 gives an o(1) normalized perturbation; eta=1/2 gives an asymptotic
bound (49/144)C; eta<1/2 permits a growing error. The exponent, rather than an
unproved numerical extrapolation, follows from the exact native mass.

**All-scale positive transfer.** If a comparison source has D_comparison(m)>=d>0
eventually at every integer m, and its difference from Lambda satisfies (9),
then the native eventual inequality follows when eta>1/2, or when eta=1/2 and
(49/144)C<d. The parent's fixed-source consumer then gives RH. Neither such a
comparison source nor that native error bound is produced here.

In the other direction, under RH the parent's D>1/10 margin is preserved
eventually by eta>1/2 perturbations, and by eta=1/2 perturbations with
C<72/245. These are CONDITIONAL robustness statements, not new proofs of RH.

## 4. ET3: an exact-moment Euler counterfamily below the threshold

The next theorem strengthens the parent's continuous-source control: the
comparison is supported on the ORDINARY prime powers, has a genuine meromorphic
Euler product, has strictly positive multiplicative Dirichlet coefficients,
and preserves one complete safe source moment EXACTLY.

**Theorem ET3.** Fix any finite Y0>=1, any 0<=eta0<1/2, and any epsilon>0.
There exist an integer Y>=Y0, eta0<eta<1/2, and tau>0, with the following
properties. Define

    Z_Y(s)=zeta(s) product_(p<=Y)(1-p^(-s)),
    F(s)=zeta(s)/[Z_Y(s+eta+i tau)Z_Y(s+eta-i tau)].         (15)

The Euler product initially defines F on Re s>1; (15) gives its meromorphic
continuation. Its logarithmic derivative coefficients are

    lambda_F(p^k)=log p,                                   p<=Y,
                 =log p[1-2p^(-k eta)cos(k tau log p)],      p>Y,
    lambda_F(n)=0,                                         n not a prime power.
                                                               (16)

They satisfy

    (1/2)Lambda(n)<=lambda_F(n)<=(3/2)Lambda(n),
    |lambda_F(n)-Lambda(n)|<=epsilon Lambda(n)n^(-eta0),
    sum_n lambda_F(n)/n^2 = sum_n Lambda(n)/n^2.             (17)

All local Euler factors at p<=Y, including their arbitrarily high powers,
are unchanged. F has strictly positive real multiplicative coefficients
in its ordinary Dirichlet series, with coefficient 1 at every Y-smooth integer.
Its Mangoldt summatory function satisfies sum_(n<=x)lambda_F(n)~x.
It has a genuine simple zero at

    rho*=1-eta+i tau,       Re rho*>1/2.                    (18)

Nevertheless the associated kernel equals the native W on |x|<=log Y,
and its annular scalar equals D(m) for 2<=m<=sqrt(Y)/2.
Its scalar has unbounded excursions of both signs as stated in Section 6.

The parameter construction is an existence proof, not a numerical certificate
for a named eta,tau. No model in this theorem is asserted to have zeta's exact
large-prime local factors or the Riemann functional equation.

### 4.1 Choose the tail size first

Choose an open interval I=(alpha,beta) with eta0<alpha<beta<1/2, and then an
integer Y>=max(Y0,16) so large that

    2Y^(-alpha)<=1/2,
    2Y^(-(alpha-eta0))<=epsilon.                            (19)

The parameters eta below will lie in I. These two inequalities imply the first
two bounds in (17) for all k at once. This is not an arbitrary prime-weight
sequence: the SAME eta,tau determines all powers of every prime.

### 4.2 The exact safe moment can be set to zero

For real eta in I put

    T(eta,t)=sum_(p>Y,k>=1) log p*p^(-k(2+eta))cos(k t log p).
                                                               (20)

It converges absolutely and uniformly in t, locally uniformly in eta>-1.
T(eta,0)>0. For each fixed eta, T(eta,t)<0 for some t>0.

Here is the full sign argument. Set q=2+eta and choose a finite set of primes
Y<p<=P so that

    sum_(p>P) log p/(p^q-1)
        < (1/2)sum_(Y<p<=P) log p/(p^q+1).

This is possible by convergence of the positive series and positivity of any
nonempty retained block. If all the retained phases t log p were pi mod 2pi,
their COMPLETE prime-power contribution would be

    -sum_(Y<p<=P) log p/(p^q+1),

since sum_(k>=1)(-p^(-q))^k=-1/(p^q+1).
Continuity permits a small open neighborhood of those phases with block value
less than -3/4 of that positive sum. Prime-log rational independence ensures
that the real flow t -> (t log p)_p modulo 2pi visits this neighborhood at
arbitrarily large positive t. To see this without an extra arithmetic premise,
every nonconstant torus character has time average zero: its frequency is
sum h_p log p !=0 by unique prime factorization. Approximate a continuous
nonnegative bump in the neighborhood by trigonometric polynomials. Its positive
torus mean is then its time mean, forcing visits. The omitted tail cannot change
the resulting negative sign. The intermediate value theorem gives a root t>0.

### 4.3 Select a root that cannot be canceled by an original zeta zero

We also require eta,2eta,1-eta not to equal real parts of any nontrivial zeta
zero, and tau not to equal the absolute ordinate of any such zero.
These requirements can be met together with T(eta,tau)=0.

The forbidden eta values from the real-part conditions form a countable set.
For each fixed forbidden ordinate t, the function

    z -> sum_(p>Y,k>=1) log p*cos(k t log p)*p^(-k(2+z))

is holomorphic on Re z>-1 and is NOT identically zero. Indeed cos(t log p) and
cos(2t log p) cannot both be zero for a single prime p. At least one Dirichlet
coefficient is nonzero; uniqueness of an absolutely convergent Dirichlet series
follows by multiplying by its least nonzero base raised to z and sending real
z to infinity. Therefore its real zeros in I are discrete, hence countable.
Discard their countable union over all forbidden t as well.

An interval cannot be exhausted by these countable sets. Choose eta outside
all of them. Section 4.2 supplies tau>0 with T(eta,tau)=0, and no such root can
have a forbidden ordinate. This proves the parameter-selection assertion.
No assertion that a numerically guessed ordinate misses all zeta zeros is made.

### 4.4 Positive Euler coefficients and the exact moment

For p>Y set r=p^(-eta), theta=tau log p, and x=p^(-s). The local factor is

    [(1-r exp(i theta)x)(1-r exp(-i theta)x)]/(1-x).

Its ordinary coefficients are

    a_F(p^0)=1,
    a_F(p)=1-2r cos theta,
    a_F(p^k)=1-2r cos theta+r^2=|1-r exp(i theta)|^2, k>=2.

They are strictly positive by r<=1/4. The logarithmic series gives (16),
including all k, with no branch choice after (15) is introduced. Absolute
Euler convergence on Re s>1 justifies multiplication and differentiation.
At p<=Y the factor is the original (1-p^(-s))^(-1).

Equation (20) at its selected root is exactly

    -F'(2)/F(2)=-zeta'(2)/zeta(2)-2T(eta,tau)
              =-zeta'(2)/zeta(2).                         (21)

Thus this is equality of the ENTIRE safe moment, not finite-precision matching.
Also |sum_(n<=x)(lambda_F(n)-Lambda(n))|
<=6 x^(1-eta)/(1-eta), by (2) and partial summation.
Combining this o(x) perturbation with the ordinary PNT proves the claimed PNT
for lambda_F. Its Dirichlet-series residue at 1 need not be 1; it is its SIMPLE
pole at 1 that makes the Mangoldt main-term coefficient equal to 1.

### 4.5 The off-line zero and the functional-equation failure

At rho*=1-eta+i tau, Z_Y(s+eta-i tau) has a simple pole. The other denominator
is finite and nonzero at 1+2i tau by the classical zero-free line Re s=1.
The numerator zeta(rho*) is nonzero by the choice of 1-eta. Finite Euler
factors are nonzero at positive real parts. Thus F has the simple zero (18).

Let xi_F(s)=s(s-1)pi^(-s/2)Gamma(s/2)F(s)/2, understood meromorphically.
Its other elementary factors are nonzero at rho*, so xi_F(rho*)=0.
At 1-rho*=eta-i tau, the numerator zeta and both denominator zetas are finite
and nonzero by the exclusions for eta and 2eta; 0<2eta<1 and tau>0.
The gamma and rational factors are also nonzero. Consequently

    xi_F(1-rho*) !=0.

The Riemann functional equation is explicitly FALSE for this model. No entire
Riemann completion is asserted either. These are necessary scope restrictions:
(15) is a control on a proposed method, never a counterexample to actual RH.

## 5. ET4: every positive Selberg-derivative hierarchy also survives

The strengthened control is not defeated by requiring finitely many, or even
ALL, ordinary nonnegative generalized Mangoldt coefficients.
For k>=0 define coefficients c_k by

    c_0(n)=1_(n=1),
    c_(k+1)(n)=log(n)c_k(n)+sum_(d|n)lambda_F(d)c_k(n/d).
                                                               (22)

Induction gives c_k(n)>=0 for every k,n. On Re s>1,

    (-1)^k F^(k)(s)/F(s)=sum_n c_k(n)n^(-s).                (23)

Differentiate (23) and use -F'/F=sum lambda_F(n)n^(-s) to prove (22).
Absolute convergence and differentiation follow by working first in a slightly
larger right half-plane. The k=2 identity is exactly

    c_2(n)=lambda_F(n)log n+(lambda_F*lambda_F)(n)>=0.

This is a positivity theorem for the full hierarchy, not finite numerical
inspection. It does NOT preserve the special native identity Lambda*1=log.
Instead the model preserves lambda_F*a_F=a_F log, with a_F different from 1.
Already at a modified prime those two identities differ. A proof using the
literal identity with coefficient 1 is therefore not refuted by this control.

## 6. ET5: preserve the local arithmetic kernel but force unbounded failure

Write b=3/2, d=log4, c=1/8 and retain the parent's complete archimedean part

    C_b=(1-gamma_E-log(2pi))/3,
    S(x)=sum_(j>=1) exp(-(2j+1/2)x)/[(2j+1/2)^2-b^2].

Define W_F by the SAME source formula as W, but with lambda_F in place of Lambda:

    W_F(x)=exp(x/2)/2+C_b exp(-bx)+S(x)
           -(P2_F/b)cosh(bx)
           +(1/b)sum_(n<=exp x) lambda_F(n)n^(-1/2)
                                      sinh(b(x-log n)),    x>=0,

and extend evenly. Here P2_F=sum lambda_F(n)/n^2=P2 by (21).
The changed coefficients all have underlying prime greater than Y. Therefore

    W_F(x)=W(x), |x|<=log Y.                               (24)

This is equality of the full kernels, not equality after dropping their infinite
tails. In particular any actual local certificate whose difference interval is
inside this set is inherited unchanged. The finite annular sources also agree:

    D_F(m)=D(m), 2<=m<=sqrt(Y)/2.                           (25)

### 6.1 A complete meromorphic pole is still detected

Set V_F=(1+c^2)W_F-cW_F(.-d)-cW_F(.+d), and let
H_F(r)=(xi_F'/xi_F)(1/2+r). The exact source-Laplace calculation gives

    Laplace W_F(r)=[H_F(r)-(r/b)H_F(b)]/(b^2-r^2), Re r>1/2.
                                                               (26)

No zero representation for xi_F is presumed; (26) follows directly from its
Euler logarithmic derivative and the elementary gamma/prime source calculation.
Its right side is meromorphic. The equality H_F(b)=H(b) follows from (21).
The filter has the finite-boundary correction

    Laplace V_F(r)=A(r)Laplace W_F(r)
               +2c integral_0^d sinh(r(d-u))W_F(u)du.      (27)

That correction is entire and, by (24), is the SAME as for the native source.
It is not silently discarded.

For positive real r, xi_F(1/2+r) is nonzero, with its removable value retained
at s=1. Indeed its two shifted tail zetas are conjugates, finite and nonzero
there by the exclusion of tau from the zeta ordinates; their finite Euler
factors have no zero at positive real part. The remaining original completed
xi is positive on the real axis in question. Thus (26)--(27) are analytic at
all positive real r, including the removable point r=b.

At r*=1/2-eta+i tau they have a genuine pole with nonzero residue

    A(r*)/(b^2-r*^2).                                      (28)

The filter zeros have real parts +/-3/2, whereas 0<Re r*<1/2.
The original zeta cannot cancel this pole by Section 4.3.

### 6.2 Two-sided excursions on the SAME integer square sequence

The source lambda_F is nonnegative and <=(3/2)Lambda, so the proof of ET1 gives
a global Lipschitz bound <9 for D_F. It also gives D_F'->0 in the same essential
sense, since its Mangoldt sum obeys PNT. Thus the new native regularity alone
is not a sign-propagation theorem.

For every 0<=a<1/2-eta,

    limsup_(m->infinity, m integer) D_F(m)/m^(2a)=+infinity,
    liminf_(m->infinity, m integer) D_F(m)/m^(2a)=-infinity. (29)

Suppose, for example, a liminf greater than minus infinity gives D_F(m)>=-C m^(2a) eventually on
integers. Lipschitz interpolation supplies the same type of bound for all real
m, with an added constant. The parent's EXACT filter identity, now with F,

    V_F(log X)=a0 sqrt X-P_F(X)-E(X), a0=45/128,
    D_F(m)=1/4-V_F(2log m)-E(m^2), 0<=E<1/10,

gives an eventual upper envelope for V_F(x) of size C' exp(a x)+C'.
Choose an exponent a<theta<1/2-eta if needed, and subtract V_F from a sufficiently
large exponential majorant on a tail. This is a nonnegative locally integrable
density of finite exponential order. Its Laplace transform has pole (28), so
its abscissa is at least Re r*>theta; in particular it is finite, not minus
infinity. Landau's positive-density theorem forces a singularity at that real
abscissa. But (26)--(27) and the majorant are analytic there, a contradiction.
A finite initial interval has an entire transform and changes nothing.
The same argument applied to -V_F proves the other assertion in (29).
This argument never selects a rightmost zero and never assumes simple original
zeta zeros. Landau's Taylor/Tonelli proof is given in the parent; only the
explicit simple model zero (18) is needed here.

Hence even all the properties (17), positive multiplicative coefficients,
meromorphic continuation, PNT, exact local agreement, and the full hierarchy
(22) together do not force the native-style cofinal lower inequality.
The complete Riemann functional equation and unit local factors are NOT among
those preserved properties.

There is also a negative finite-window witness for the model operator, not just
failure of a scalar estimate. By (29) and the bounded E correction, V_F(x)
is unbounded above. For a point with V_F(x)>V_F(0), the signed four-point measure
(delta_0-delta_x)*(delta_0-c delta_d) has W_F energy
2[V_F(0)-V_F(x)]<0. Combine coincident atoms and approximate each by the SAME
small smooth bump. Continuity of W_F preserves the strict negative gap for
sufficiently small bump width, giving a compactly supported L2 negative test.
No finite support length or numerical test vector is asserted to have been
computed. This shows precisely which proposed local-to-global inference fails.

### 6.3 The relative oscillation has an exact asymptotic

The PNT test-function argument of (12), with the fixed complex exponent, gives

    D_F(m)-D(m)
      =-2 m^(1-2eta) Re[J(1-eta+i tau)exp(2i tau log m)]
                    +o(m^(1-2eta)).                      (30)

Removing all prime powers of the finitely many primes p<=Y changes the smoothed
sum by only O_Y(X^(-eta-1/2)): there are a bounded number per prime in each
factor-16 annulus. This justifies using the full PNT in (30).
J is nonzero at this argument by (13). Since successive phases
2tau log(m+1)-2tau log m tend to zero and the phase tends to infinity,

    limsup (D_F-D)/m^(1-2eta)= 2|J(1-eta+i tau)|,
    liminf (D_F-D)/m^(1-2eta)=-2|J(1-eta+i tau)|.            (31)

One can take nearest integers to the real points with prescribed phase to
justify both limits. Formula (30) is for the DIFFERENCE. No same leading
asymptotic is asserted for D_F itself when native RH is not assumed.
Equation (29) is the unconditional assertion about the whole model scalar.

## 7. ET6: one safe moment versus complete safe-source determination

The counterfamily preserves the one safe moment at s=2, NOT the complete safe
source jet used by the earlier Schur constructions. This distinction has an
elementary rigidity proof. If sum |delta(n)|/n^2<infinity and

    sum_n delta(n)n^(-2-k)=0 for every integer k>=0,

then delta(n)=0 for every n. Otherwise let n0 be its least nonzero index.
Multiply the k-th identity by n0^k and send k to infinity. Dominated convergence
with the summable weights |delta(n)|/n^2 leaves delta(n0)/n0^2=0, a contradiction.
Likewise equality of the complete analytic jet of the logarithmic derivatives
at s=2 forces equality in a neighborhood, then throughout Re s>1 by the
identity theorem, and coefficient uniqueness gives the same conclusion.

This does not prove positivity from the native jet; it prevents misreading
ET3 as a counterfeit of EVERY entry in the complete safe-source matrices.
A single source constant and an entire analytic source are different data.

## 8. The precise surviving arithmetic task

The direct hope was: slow scale variation, genuine multiplicativity, positive
local source coefficients, the safe moment, and all Selberg-type positive
identities might propagate the native finite-range margin indefinitely.
ET1 is a real gain in actual-source regularity. ET3--ET5 show that the proposed
implication using only those broad properties is false, even at arbitrarily
small subcritical coefficient error and arbitrarily long exact local agreement.
This is stronger than the parent's continuous replacement, but still ONLY a
scope-limited method obstruction.

The native identity not used by the model is

    sum_(d|n)Lambda(d)=log n,

equivalently the exact unit local factors of zeta. The complete functional
equation is another missing model property, exhibited as false in Section 4.5.
This pass supplies no theorem combining them into the required signed bound.

In the original arithmetic coordinate that bound remains exactly

    integral_(1/4)^4 w'(u)[psi(m^2u)-m^2u]du <=m/4
                     for every sufficiently large integer m.    (32)

Alternatively, the quantitative all-scale comparison in Section 3 would close
the route if a positive comparison and its CRITICAL-precision arithmetic error
were proved. No such source/error construction is asserted. In particular an
o(1) relative Euler-coefficient error, even with all the other properties in
ET3, is not enough: it can be epsilon n^(-eta0) for any eta0<1/2.

No new actual interval PSD certificate or larger finite-height margin is
claimed. Previous certificates remain at their previous exact scopes.
Classical PNT, Euler products, equidistribution of independent prime phases,
and Landau theory have prior art. No external novelty claim is made for the
general principles or for the specialized counterfamily without review.

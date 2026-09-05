# Finite prime cutoffs fail uniformly; exact cancellation for a dense generating family

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
The unrestricted matrix inequality and RH are NOT proved.
Base: PR #790, bce97be9727dea9968db7517738edc966d2cc86b.
Scope: the actual arithmetic form of heat-hankel-pass5, with its original
metric, endpoints, prime powers, and Fourier convention. A final synthetic
control is explicitly separate from actual xi. No external novelty claim.

This is an attempt at the remaining source sign, not another RH criterion.
The proposed completion by positive finite-prime truncations fails. The
failure is proved for the literal prime weights, not only a counterfeit.
A full signed tail estimate is proved on an explicit infinite-dimensional
cone, but its extension to arbitrary signed combinations is not obtained.

## 1. The exact form and which cutoff is being studied

Use xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2 and X(u)=xi(1/2+sqrt(u+1/4)).
For a real exponential polynomial f in L2(0,infinity), put

    R(A)=integral_0^infinity exp(-At)f(t)dt,
    d=1/4,  c=1+d=5/4,
    g(x)=R(x^2+d)^2,
    ghat(ell)=integral_R g(x)exp(-i ell x)dx,
    Omega(x)=Re digamma(d+ix/2)-log pi.

All tests below have poles only at A=-1 and satisfy R(0)=0. Thus g is even,
analytic in a strip wider than |Im x|<=1/2, and decays faster than |x|^-2.
The unconditional Guinand--Weil formula [S1], or parent equation (29), gives

    Q(f):=<f,Gamma_0 f>
      = [integral g Omega - 2 sum_(n>=2) Lambda(n)n^-1/2 ghat(log n)]/(4pi).
                                                                  (1)

The usual endpoint contribution R(0)^2 vanishes for these tests. It is not
omitted for unrestricted f. All sums in (1) converge absolutely for EACH
fixed test: shift the Fourier contour to a height y with 1/2<y<sqrt(5/4).
This does not claim an order-uniform absolute bound.

For a real cutoff X>=2 define precisely

    Q_X(f)=[integral g Omega
              -2 sum_(2<=n<=X) Lambda(n)n^-1/2 ghat(log n)]/(4pi).   (2)

The archimedean integral is kept EXACT, not truncated. All prime powers
through X and both Fourier orientations are included. Q_X is NOT the
finite-dimensional compression P Gamma_0 P of pass5. Confusing these two
approximations would invalidate the argument.

## 2. Explicit rational tests in the prescribed hierarchy

For every integer m>=2 set

    C_m=4(5/4)^m,
    R_m(A)=C_m A/(A+1)^m,
    f_m(t)=C_m exp(-t)[t^(m-2)/(m-2)!-t^(m-1)/(m-1)!].       (3)

Their Laplace transforms agree exactly, and integral f_m=R_m(0)=0. These
are actual tests in the pole-1 portion of the parent's dyadic spaces as
soon as 2k>=m. They use no zero ordinates and no optimized coefficients.
They are normalized by R_m(d)=1, so

    g_m(x)=(1+x^2/d)^2 (1+x^2/c)^(-2m),   g_m(0)=1,
    I_m=integral_R g_m(x)dx>0.                              (4)

The L2 norm, useful for separating form size from Rayleigh quotient, is

    ||f_m||^2=C_m^2 (2m-4)! /
                     [2^(2m-2)(m-1)((m-2)!)^2].            (5)

The form lower bounds below are not lower bounds uniform on unit vectors.

### Lemma 1: exact second moment

Let E_m denote expectation for density g_m/I_m. Beta integration gives

    V_m:=E_m x^2
       =5(2m^2+9m+25)/[4(4m-7)(2m^2+m+5)].                 (6)

Indeed, if J_j=int_R x^(2j)/(x^2+c)^(2m)dx, then

    J_j=c^(j+1/2-2m) Gamma(j+1/2)Gamma(2m-j-1/2)/Gamma(2m),
    J_1/J_0=c/(4m-3),
    J_2/J_0=3c^2/[(4m-3)(4m-5)],
    J_3/J_0=15c^3/[(4m-3)(4m-5)(4m-7)].

Taking (J_3+2dJ_2+d^2J_1)/(J_2+2dJ_1+d^2J_0) proves (6).
For every real m>=5 the same calculation is valid and

    V_m<1/m.                                                (7)

After clearing positive denominators, (7) is
22m^3-85m^2-73m-140>0. On writing m=k+5 this polynomial is
22k^3+245k^2+727k+120, positive for k>=0. This proves the full parameter
inequality, not just the finite instances checked by the code.

An exact normalization is

    I_m/(pi sqrt(c))=
      binom(4m-2,2m-1)/4^(2m-1) * (1+8 J_1/J_0+16 J_2/J_0) (8)

for integer m>=2.

### Lemma 2: an elementary archimedean upper bound

The digamma partial fractions imply, for every real x,

    0<=Omega(x)-Omega(0)
      =(x^2/4) sum_(j>=0)
          1/[(j+d)((j+d)^2+x^2/4)]
      <17x^2.                                               (9)

For the last inequality sum_(j>=0)(j+1/4)^-3<64+3/2<68,
using the integral bound sum_(j>=1)j^-3<=3/2.
Reflection and duplication give

    Omega(0)=-gamma_E-pi/2-3log2-log pi<-5.                  (10)

Only elementary inequalities are required: gamma_E>1/2, pi>3,
log2>2/3, and log pi>1. To certify the less familiar first inequality,
gamma_E>H_8-log9, exp(11/5)>9 by its first ten nonnegative Taylor terms,
and H_8-11/5=29/56>1/2. The log2 bound follows from the positive
atanh series at 1/3. Since e<3<pi, log pi>1.
Thus (7)--(10) prove

    integral_R g_m(x)Omega(x)dx < -4 I_m,        m>=17.       (11)

### Lemma 3: the complete low-frequency Fourier range has positive sign

Since cos y>=1-y^2/2 for all real y,

    ghat_m(ell)/I_m=E_m cos(ell x)>=1-(ell^2/2)V_m>1/2
                      whenever ell^2<=m, m>=5.              (12)

This uses the exact density, not a Gaussian approximation.

### Lemma 4: exact Fourier positivity through frequencies linear in m

In fact, without a Gaussian approximation,

    ghat_m(ell)>0,          m>=42, |ell|<=m.                 (12a)

This improves the square-root range in (12). For integer N>=3 define

    B_N(ell)=int_R (x^2+c)^(-N)exp(-i ell x)dx.

The Gamma integral and Fourier transform of a Gaussian give

    B_N(ell)=sqrt(pi)/Gamma(N) int_0^infinity
           t^(N-3/2) exp(-ct-ell^2/(4t))dt >0.

Use this positive integral as a probability density in t, writing E for
its expectation. With e=E(1/t) and r=(N-1)e, the exact identities are

    B_(N-1)/B_N=r,
    B_(N-2)/B_N=(N-1)(N-2)E(1/t^2),
    c=(N-3/2)e+(ell^2/4)E(1/t^2),
    c E(t)=N-1/2+(ell^2/4)e.

All integrations by parts have vanishing endpoints for N>=3. Consequently

    e<=c/(N-3/2),
    r>=(N-1)/[(N-1/2)/c+ell^2/(4(N-3/2))].

The second inequality uses E(t)E(1/t)>=1. If |ell|<=N/2 and N>=24,
this lower bound is at least 9/8. After clearing denominators the assertion
is 19N^2-448N+528>=0. At N=k+24 it is 19k^2+464k+720>0.

Since (x^2+d)^2=(x^2+c-1)^2, put N=2m to obtain

    ghat_m/C_m^2 = B_(N-2)-2B_(N-1)+B_N.

Using E(1/t^2)>=e^2 gives

    ghat_m/(C_m^2 B_N)
       >=1-2r+[(N-2)/(N-1)]r^2
       >=(N-82)/[64(N-1)]>0,                  N>=84.

For the last inequality the quadratic is increasing for r>=9/8 when
N>=84. This proves (12a) at every frequency in the stated range. No
asymptotic Bessel expansion or numerical Fourier evaluation is used.

## 3. Theorem PC-1: a uniform negative cutoff form

For every integer m>=42 and every real X>=2 with log X<=m,

    Q_X(f_m)<-I_m/pi<0.                                     (13)

Proof. Apply (12a) to every term of the finite prime sum in (2), whose
weights Lambda(n)/sqrt(n) are nonnegative, then apply (11).

The earlier, stronger-margin square-root version remains valid:

    4pi Q_X(f_m)<-I_m[4+sum_(2<=n<=X) Lambda(n)/sqrt(n)],
                       m>=17, 2<=X<=exp(sqrt(m)).           (13a)

Here use (12) rather than (12a).

Every finite prime cutoff therefore fails positivity on the prescribed
rational hierarchy: choose m>=max(42,log X). A concrete instance is
m=42, X=10^18. The elementary rational certificates e>27/10 and
(27/10)^42>10^18 imply log(10^18)<42. This examines the sign without
evaluating or enumerating the primes through that enormous cutoff.

For this test family, log X>m is a NECESSARY condition for a nonnegative
cutoff form once m>=42. It is not asserted sufficient or optimal. In
particular this is an exponential cutoff obstruction in the test degree,
not a universal computational lower bound: analytic acceleration,
Euler--Maclaurin evaluation of source derivatives, and other corrected
schemes are different from the literal deletion of the prime tail (2).

## 4. Theorem PC-2: each fixed cutoff has unbounded negative index

This stronger conclusion does not merely produce one negative vector.
For fixed finite X let

    B_X(x)=Omega(x)-2 sum_(2<=n<=X) Lambda(n)n^-1/2 cos(x log n).

Then B_X is continuous and B_X(0)<-5. The bounded self-adjoint operator

    K_X=(1/(4pi)) integral_R B_X(x)
         |exp(-(x^2+d)t)><exp(-(x^2+d)t)| dx                 (14)

is trace class: the integral of the rank-one trace norms is
(1/(8pi))int |B_X(x)|/(x^2+d) dx<infinity. Here use the classical
Omega(x)=O(log(2+|x|)), not the crude quadratic estimate (9).
On tests with R(0)=0 its quadratic form is exactly Q_X. Without that
constraint the original endpoint functional must still be added and
is not being identified with a bounded L2 rank-one operator.

For every fixed integer r>=0 and sufficiently large integer m, consider
r+1 test transforms

    R_(m,j)(A)=C_m A m^j(A-d)^j/(A+1)^m,    0<=j<=r.        (15)

Take m>=r+3 so these are proper rational transforms of exponential
polynomials. They all vanish at A=0, are linearly independent, and remain
within a finite member of the original pole-1 test hierarchy.

Their form matrix Q_X^(m) satisfies, by x=y/sqrt(m),

    sqrt(m) Q_X^(m)(i,j) ->
       B_X(0)/(4pi) integral_R y^(2i+2j)exp(-2y^2/c)dy.     (16)

The limiting Gaussian moment matrix is strictly positive definite, since
a nonzero real polynomial in y^2 has positive squared integral. Its
negative prefactor makes the limit negative definite. Consequently the
finite form matrix is negative definite for sufficiently large m.
As r was arbitrary, K_X has infinitely many negative eigenvalues; moreover
arbitrarily large negative subspaces consist of zero-endpoint rational tests.

Here are the domination details in (16). The rescaled factor is

    g_m(y/sqrt(m))=(1+y^2/(md))^2(1+y^2/(mc))^(-2m).

For m>=m0>=r+3, (1+t/m)^m increases with m, so its inverse is at most
the m0 value. Also |B_X(y/sqrt(m))|<=C_X+17y^2 by (9).
Multiplying by y^(2i+2j) gives an integrable bound with large-y exponent
at most 4r+6-4m0<=-6. Dominated convergence and finite-matrix continuity
therefore justify (16) and negative definiteness. No numerical eigenvalue
calculation or sampling assertion enters this proof.

This does NOT prove a negative eigenvalue for Gamma_0. K_X is a different,
prime-truncated operator, and positivity is not preserved by deleting the
signed prime tail.

## 5. Theorem PC-3: the actual full form has the opposite sign

We now retain the ENTIRE arithmetic source. This part imports V100: every
nontrivial zero with 0<gamma<=100 is critical, from Platt--Trudgian [S4].
It also uses the parent's separately replayed interval sign change between
Xi(14) and Xi(15), hence a real invariant parameter A0 in (196,226).
These are finite inputs; the entire remaining zero sum is bounded below.
No simplicity is required and no all-height RH is assumed.

First reproduce the source budget, so the proof does not depend on any
unreviewed high-order positivity assertion. Set A=x+iy=rho(1-rho).
The strip gives x>0 and y^2<=x. The invariant product gives

    H=h(0)=sum_A Re(1/A)=1+gamma_E/2-log(4pi)/2,  0<H<1/2.

Thus Re(1/A)>=1/(x+1), x>=1/H-1, and

    sum_A 1/x <=H/(1-H)<1.                                 (17)

All multiplicities are included. For s>=6, every omitted A with gamma>100
satisfies x>=10000 and

    |A^2/(1+A)^s|
       <=(x+1)^(2-s)<=x^(3-s)/x.

Consequently

    |sum_(gamma>100) A^2/(1+A)^s|<10000^(3-s).               (18)

The selected low zero contributes more than 196^2/227^s; all other zeros
through 100 contribute nonnegatively. At s=6,

    10000^(3-s) / (196^2/227^s)
       =227^6/(196^2*10000^3)<1/16,

and the ratio decreases by 227/10000 at every unit increment of s.
Hence for EVERY integer s>=6,

    sum_A A^2/(1+A)^s > (15/16)196^2/227^s>0.              (19)

This is a reproof of a consequence of the already known b=2 mixed layer,
not a claim of a new RH-strength positivity result.

For every m,n>=3, therefore,

    Q(f_m,f_n)=sum_A R_m(A)R_n(A)
       >15*196^2*(5/908)^(m+n)>0.                          (20)

In particular Q(f_m)>0 for all m>=3. Compare this with (13).
Let the absolutely convergent ACTUAL prime tail be

    P_tail(m,X)=sum_(n>X) Lambda(n)n^-1/2 ghat_m(log n).

Since 4pi Q(f_m)=4pi Q_X(f_m)-2P_tail(m,X), (13) and (20) imply

    P_tail(m,X)<-2 I_m,
             m>=42, 2<=X<=exp(m).                          (21)

The same bound also holds in the square-root regime (13a).
A stronger bound there retains the head sum and the explicit positive full-form
margin. Formula (21) is a genuine signed estimate for the literal prime
tail on this test family. It does not use an absolute tail estimate or
an inference from positivity of individual prime terms.

Every finite nonnegative combination of f_m, m>=3, also has positive full
form, by (20). For indices m,n>=17 and logX<=sqrt(min(m,n)), the same
Beta calculation with the real parameter (m+n)/2 makes their cutoff
bilinear entry negative. Thus an infinite-dimensional cone, not only
isolated individual tests, exhibits the same cancellation phenomenon.
The positive cone is not the set of all signed linear combinations.

## 6. Why this is still not the requested matrix completion

The linear span of {f_m:m>=M} is dense in L2(0,infinity) for EVERY fixed
integer M>=3. One proof is direct. If f is orthogonal to this family,
let L_f be its Laplace transform and write

    L_f(1-z)=sum_(j>=0)c_j z^j,
    c_j=integral f(t)exp(-t)t^j/j! dt.

Orthogonality gives c_j=c_(j+1) for every j>=M-2. The power series is
therefore a polynomial plus a rational tail with denominator 1-z.
Analytic continuation implies L_f(s) is a polynomial in s plus c/s.
Cauchy--Schwarz gives L_f(s)=O(s^-1/2) as s tends to positive infinity,
so the polynomial vanishes. The inverse transform c is not in L2 unless
c=0. Thus f=0, proving density (with conjugates inserted for complex f).

Despite this density, positive values on each generator, or even positive
values on every pair of generators, do not establish matrix PSD. Arbitrary
SIGNED coefficients are still required.

A fully explicit synthetic check demonstrates the missing implication.
For the NONNATIVE parameters 1, 2+i, 2-i define the corresponding heat
and quadratic form. Its heat e^-t+2e^-2t cos t is positive for all t>0.
For m,n>=3, with s=m+n,

    sum_A A^2/(A+1)^s
       >=2^-s-10*10^(-s/2)>0,                              (22)

because s>=6 and 10*(2/sqrt10)^6=16/25<1. Thus every entry in every
Gram matrix of this same tail family is positive.

Nevertheless for every M>=3 there is an exact negative vector supported
on just f_M,f_(M+1),f_(M+2). Put a=2+i and

    Z=i(3+i)^(M+2)/(a(a-1)),
    U=Im Z,  V=Re Z-2U,
    R(A)=A(A-1)(U A+V)/(A+1)^(M+2).                        (23)

The coefficients U,V are rational; R(1)=0 and R(2+i)=i. Conjugation gives
R(2-i)=-i, so its quadratic form is exactly -2. Expanding the numerator
shows that (23) is a combination of A/(A+1)^M, A/(A+1)^(M+1), and
A/(A+1)^(M+2), hence of the normalized generators above. The exact
coefficients in the unnormalized basis are U, V-3U, 2(U-V).

The synthetic example does not preserve the literal zeta Euler product;
it is not an RH counterexample. It identifies the invalid step from
(20), dense generating tests, or generatorwise tail cancellation to PSD.

The attempted global proof was to use controlled finite prime cutoffs,
then pass positivity to the full form. PC-1/PC-2 refute positivity of
those cutoffs. PC-3 pays the missing tail for a specific cone, but the
cross-term estimate for arbitrary signed coefficients remains unproved.
No all-rank arithmetic positivity theorem, signed-source bootstrap,
new zero-free region, or RH proof is supplied here.

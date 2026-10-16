# A uniform critical-power factorization of the coupled Euler source

Status: PROPOSED component mathematics. Complete arguments below; same-author
reconstruction only. No full native moment estimate, zero-free improvement,
or RH proof is asserted. Not independently reviewed or formalized.

Source: #948, EULER_STRIPPING.md at
05b6f2172c686356ccd9900d33ffc5f526c5e98b (blob
80f6d1061098c666bcc06a4c949c145a148bf358), and #949,
RENORMALIZED_CERTIFICATE.md at cdb0666fc48d5166f5edd81f394b13e2001a6b5d.
They already extract the weighted sixth-power factor and prove the normalized
numerator nonzero on Re(s)>1/2. This is NOT claimed again as a new result.

New at the inspected repository scope: a second, uniform-in-power splitting,
a correction and its inverse with finite absolute coefficient mass at the
EXACT critical weight, a correction continuation below 1/2, and an explicitly
priced kernel tail. GAUSSIAN_ADAPTER.md completes the fixed Gaussian interface.
Euler algebra, absolutely convergent Dirichlet convolution, and Minkowski are
classical. No global-priority claim is made.

## 1. Objects and the exact local identity

Fix a number field F of degree d. Let S contain all prime ideals over 2 and 3;
additional original or moving exclusions are permitted. Thus every retained
prime ideal has norm q>=5. Equal-norm prime ideals remain distinct.

Fix an integer m>=2. At each retained prime choose complex a_p,b_p with
|a_p|,|b_p|<=1. Their completely multiplicative extensions to ideals are a,b.
Put

    r=q^(-1), lambda=q^(m/2-1), x=q^(-s),
    A=a_p x, Y=b_p lambda x^m,
    P_p(x)=1-(1-r)A-Y,
    Q_p(x)=(1-A)(1-Y),
    U_p(x)=P_p(x)/Q_p(x).

For odd m the positive real weight lambda need not be an integer. All analytic
arguments still apply. The exact rational diagnostics use even m.

The entire local computation is

    P_p-Q_p = r A-A Y,
    U_p = 1 + (r A-A Y)/((1-A)(1-Y)),                    (1)
    U_p^(-1) = 1 + (-r A+A Y)/(1-(1-r)A-Y).              (2)

For m=6, P_p is exactly the normalized 0/1/6 coefficient polynomial from
#948/#949, with q^2 at degree six, not q^3. In the source's principal instance
a_p=1 and b_p is its actual theta phase to the sixth power. No finite-order
Hecke assumption on b is made.

For general m, these are comparison families; NO corresponding automorphic
realization is asserted. In particular, a uniform algebraic theorem in m is
not a theorem about all metaplectic covers.

Let p_m(n),q_m(n),u_m(n),v_m(n) be the multiplicative coefficients of P,Q,U,U^-1.
The following are finite ideal-convolution identities coefficient by coefficient:

    p_m=q_m*u_m,  q_m=p_m*v_m,  u_m*v_m=delta_1.         (3)

The two-channel coefficients are explicitly

    q_m(n)=sum_{c^m | n} mu_F(n/c^m) a(n/c^m)
                            mu_F(c)b(c)(Nc)^(m/2-1).   (4)

There is NO condition (c,n/c^m)=1 in (4). A shared prime creates the required
local degree-(m+1) coefficient a_p b_p lambda in Q. P has no such coefficient;
U accounts for the difference. For P itself a representation by disjoint
exponents 1 and m DOES require the corresponding coprimality condition.
Confusing these two constructions changes the source.

## 2. A coefficient norm bounded at the exact critical line

For an ideal coefficient kernel h define

    ||h||_sigma = sum_n |h(n)|(Nn)^(-sigma).

This is the absolute Dirichlet coefficient norm, not the modulus of the
analytic Euler product. A pointwise Euler bound alone would not prove it.

### Theorem 1 (uniform critical coefficient norm)

There exist coefficientwise nonnegative multiplicative majorants h_m^+,h_m^-
for |u_m|,|v_m|, independent of all phases and masks, such that

    ||h_m^+||_(1/2), ||h_m^-||_(1/2) <= exp(5d).         (5)

The same constant works for every integer m>=2 and every excluded set S as
specified. This is an upper bound, not an assertion of the optimal norm.

Proof. In formal power series, (1)-(2) admit the nonnegative majorants

    1+(r x+lambda x^(m+1))/((1-x)(1-lambda x^m)),
    1+(r x+lambda x^(m+1))/(1-(1-r)x-lambda x^m).         (6)

Set t=q^(-1/2). Then lambda t^m=r and both extra masses in (6) equal

    2 q^(-3/2)/((1-t)(1-r)).                            (7)

The inverse denominator is positive because
1-(1-r)t-r=(1-r)(1-t)>0. Thus the geometric majorants really converge at t.
Since q>=5, t<1/2 and 1-r>=4/5. Each local mass is at most
1+5q^(-3/2), including its constant term.

At most d prime ideals lie over each rational prime ell, each of norm at
least ell. The exclusions remove all primes over ell=2,3. Hence

    sum_{p notin S}(Np)^(-3/2)
      <= d sum_{ell rational prime >=5} ell^(-3/2)
      <= d sum_{n>=5} n^(-3/2)
      <= d integral_4^infinity x^(-3/2) dx = d.

Multiply the local nonnegative masses and use 1+t<=exp(t). Monotone
convergence identifies the product with the sum of the global coefficient
majorant. This proves (5) for forward and inverse kernels. QED.

The prime exclusions are part of the theorem. They are already present in the
intended source. No extension of the displayed constant or continuation to
unexcluded primes over 2 is claimed.

## 3. Continuation below one half belongs to the correction, not zeta

Define

    theta_m = m/(2(m+1)) = 1/2 - 1/(2(m+1)).

### Theorem 2 (subcritical correction and tails)

The functions U_m(s)=product U_p(q^(-s)) and 1/U_m(s) are holomorphic and
nonzero on Re(s)>theta_m. Their Dirichlet coefficient series converge
absolutely on that domain. On each smaller closed half-plane they have
uniform upper and inverse bounds depending on its margin and d, not the
phases. For every 0<rho<1/(2(m+1)) and T>=1,

    sum_{Nn>T} h_m^+/-(n)/sqrt(Nn)
       <= C_(F,m,rho) T^(-1/(2(m+1))+rho).              (8)

The two majorants in (6) may be used here as well.

Proof. At sigma>=theta_m, put t=q^(-sigma) and y=lambda t^m. Then

    t<=q^(-theta_m),  y<=q^(theta_m-1).

For theta in [1/3,1/2], q^(-theta)+q^(theta-1) decreases in theta up to 1/2
and decreases in q. Its maximum here is at q=5,theta=1/3. If z=5^(-1/3),
then z<3/5, since (3/5)^3>1/5, so z+z^2<24/25. Consequently

    (1-r)|A|+|Y| <= t+y <24/25.                         (9)

Every P_p is nonzero with |P_p|>1/25. Also 1-A and 1-Y are nonzero. The
positive inverse denominator in (6) is at least 1/25. The forward denominator
is bounded away from zero, uniformly in p,m on the stated region. For example
t<3/5 and y<=5^(-1/2)<1/2, giving (1-t)(1-y)>1/5.

For sigma0>theta_m, both nonconstant masses in (6) are at most

    25 [q^(-1-sigma0)+q^(m/2-1-(m+1)sigma0)].           (10)

Both prime-ideal sums converge: 1+sigma0>1, and
(m+1)sigma0-m/2+1>1. The nonnegative coefficient products converge, giving
absolute convergence of both series, uniformly on sigma>=sigma0. Locally
uniform limits are holomorphic; (3) shows their analytic products are one.
Their uniform bounds follow by summing (10), for example using
sum_p q^(-z)<=d(zeta(z)-1) for z>1. This uses the ordinary zeta series only
in absolute convergence.

Take sigma0=theta_m+rho. In the tail, n^(-1/2)<=
T^(-(1/2-sigma0))n^(-sigma0). Apply the just-proved coefficient bound.
This proves (8). QED.

For m=6 this is Re(s)>3/7 and a critical kernel tail T^(-1/14+rho).
IT IS NOT A ZERO-FREE REGION Re(s)>3/7 FOR ANY ZETA FUNCTION.

This boundary is sharp for the displayed correction's uniform normal-
convergence statement. Already for F=Q, a_p=b_p=1, at real s=theta_m,

    U_p(s)-1 = -p^(-1)(1+o(1)).

Indeed the negative term in (1) has size p^(-1), the positive term is
p^(-1-theta_m), and the denominator tends to one. The local factors are
positive by (9). Euler's classical divergence sum_p 1/p=infinity therefore
makes their partial products tend to zero, rather than to a nonzero product.
This example concerns U, not a hypothetical off-critical zeta zero.

As a useful normalization check, if b_p=1 for every p, then at the REAL point
s=1/2 one has Y=r, and hence U_p=1 exactly for all a_p. Thus U_m(1/2)=1 in
this case. This does not authorize evaluating a divergent unnormalized P
Euler product on the critical line.

## 4. The exact physical comparison

Let Omega be any actual row set with a finite nonnegative measure w. It may
be a finite sharp Eisenstein ball, or any finite-mass row measure allowed by
the source. In fields with positive unit rank a bare norm ball is infinite;
use finite balanced rows, not an unqualified norm-only ball.

The phases may depend on the row: a_p=a_p(u), b_p=b_p(u). Set both to zero at
any prime where the original column character is zero. For #948's physical
family a_p(u)=xi_u(p), b_p(u)=eta(p)xi_u(p)^m. Thus all nonunit zeros are kept,
including m-th-power columns. At a masked prime P_p=Q_p=U_p=1.

For a fixed bounded compactly supported test W on (0,infinity), define

    B_u(X)=sum_n p_m(n;u) W(Nn/X),
    C_u(X)=sum_n q_m(n;u) W(Nn/X).

For p>=1 and D>0 let

    E_B,p(D)=sup_{0<X<=D} X^(-1/2)||B(X)||_(Lp(w)),

and define E_C similarly. These are suprema of norms. The row measure is
held FIXED over every shorter scale in the supremum.

### Corollary 3 (constant-cost physical envelopes)

    E_B,p(D)<=exp(5d) E_C,p(D),
    E_C,p(D)<=exp(5d) E_B,p(D).                          (11)

This holds uniformly in p,m,D, all row phases, and masks. At moment order 2k
the cost in the moment is exp(10dk), not an unspecified constant uniform in k.

Proof. The actual finite convolution identities (3) give

    B_u(X)=sum_n u_m(n;u) C_u(X/Nn),
    C_u(X)=sum_n v_m(n;u) B_u(X/Nn).                     (12)

Multiplication by u_m(n;u) has Lp norm at most h_m^+(n), uniformly in u, and
likewise for the inverse. Apply Minkowski, divide by sqrt(X), and use (5).
Compact support makes each physical convolution finite. Shared factors are
not deleted. QED.

For the m=6 correction, truncating (12) to Nn<=T has normalized Lp error at
most C_(F,rho) T^(-1/14+rho) times the relevant full shorter-scale envelope.
This is relative to that envelope, which remains unknown at the desired
power. It is not an unconditional square-root bound for the source.

## 5. What remains in the two channels

Put A_u(X)=sum mu_F(n)a(n;u)W(Nn/X). Then the second channel is exactly

    C_u(X)=sum_c mu_F(c)b(c;u)(Nc)^(m/2-1) A_u(X/(Nc)^m),       (13)
    A_u(X)=sum_c b(c;u)(Nc)^(m/2-1) C_u(X/(Nc)^m).             (14)

The inverse has NO Mobius factor; (13)-(14) follow by Euler convolution.
Their absolute mass at exponent alpha>1/2 is bounded by

    zeta_F^S(m alpha-m/2+1)=zeta_F^S(1+m(alpha-1/2)).           (15)

At alpha=1/2 the mass is harmonic and generally diverges. For compact tests
one can retain a finite logarithmic bound; #948 already does so. The new
constant-cost comparison in (11) is between B and the TWO-CHANNEL source C,
NOT between B and native A at the exact critical exponent.

Thus all algebraic and coefficient-norm losses in U are removed; the unknown
signed Mobius growth still sits in A and in (13). GAUSSIAN_ADAPTER.md shows
that the precise fixed Gaussian of the Dedekind detector is compatible with
these identities, rather than assuming a compact-test result applies to it.
No bound for the actual arithmetic theta/Poisson pairing is supplied here.

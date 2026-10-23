# Assembled proposed theorem: the constant 4.815

This file identifies one complete proof chain. All inequalities below
refer to the same fixed kernel and exact degree-12 polynomial. Older
degree-16 numerical constants are not substituted into this chain.
The detailed lemmas are physically present in the linked component files.

## 1. Statement and imported inputs

**Proposed theorem.** The Riemann zeta function has no zero in

    |Im(s)| >= 3,     Re(s) > 1 - 1/(4.815 log|Im(s)|).

The proof imports (i) Platt–Trudgian's verification that all nontrivial
zeros through height H=3*10^12 lie on Re(s)=1/2; (ii) Yang's published
Littlewood region with denominator 21.233; (iii) the classical zeta
explicit formula and Lehman zero-counting bound. Exact citations and
the scope of these imports are in [SOURCES.md](SOURCES.md). The usual
functional equation, conjugation symmetry, and strict critical strip
0<Re(rho)<1 for nontrivial zeros are also used.

## 2. Kernel and exact detector polynomial

Put theta=5669/5000, k=tan(theta), S=sec(theta)^2 and d=theta/k.
Define g(x)=S(cos(kx)-cos(theta)) for |x|<=d and zero otherwise.
Let w(v)=integral g(x)g(x+v)dx for v>=0, and W(z)=integral_0^infinity
exp(-zv)w(v)dv. Its support is [0,U], U=2d<1.1.

[The autocorrelation proof](three-hour-root/LOGISTIC_KERNEL_AUTOCORRELATION.md)
gives 0<=w<=w0<6, w'(0)=0, a C2 zero extension which is piecewise C3,
and Re W(iy)>=0 for real y. It also gives

    w0=S[theta*tan(theta)+3theta*cot(theta)-3]>5.67.

[The curvature lemma](three-hour-boundary/LOGISTIC_CURVATURE_51.md) gives

    ||w''||_infinity <= ||g'||_2^2
      =sec(theta)^4 tan(theta)[theta-sin(2theta)/2] < 51,
    |w(v)-w0| <= (51/2)v^2,   every v>=0.

Use the exact integer vector

    C=(3500513104,-5906953599,-1574092731,18166603739,6213449589,
       -38436761903,-16088159026,168141762350,447056663730,
       616860378424,541372347258,298691298328,83048065550),
    E=10^14,  N=sum C_j^2+13E=1000000001299439064580929,
    P(x)=(|sum C_j exp(ijx)|^2+E|sum_(j=0)^12 exp(ijx)|^2)/N.

Thus P>=0. Write P=sum_(k=0)^12 a_k cos(kx). Exact integer arithmetic
gives a0=1, every ak>0, and

    ak=2[sum_(j=0)^(12-k) C_j C_(j+k)+E(13-k)]/N  (k>=1),
    a1=1738295793206197388801164/N,
    aP=sum_(k=1)^12 ak=3498832394672653287444040/N<4.

[The exact constants proof](three-hour-type/LOGISTIC_POLY12_AND_CURVATURE.md)
also proves

    Cgamma=-aP log(2pi)/2 + sum_(k=1)^12 ak log(k)/2
                    -log(pi)/2+psi(3/2)/2 < -3.00317.       (1)

## 3. Exact logistic explicit formula and zero-pair positivity

For 0<eta<=.0075 and .99<sigma<=1 put alpha=2sigma-1 and

    f(u)=eta*w(eta*u)/(1+exp(-alpha*u)),
    F(z)=integral_0^infinity exp(-zu)f(u)du,
    f0=eta*w0/2,
    A_gamma(s)=-log(pi)/2+psi(s/2+1)/2,
    E_f(s)=integral_0^infinity exp(-(s+2)u)
                         [f0-f(u)]/(1-exp(-2u))du.

[The analytic adapter](three-hour-type/LOGISTIC_ADMISSIBILITY.md) proves,
for Re(s)>1/2,

    Re sum_n Lambda(n)n^(-s)f(log n)
      =f0 Re A_gamma(s)+Re F(s-1)
                         -Re sum_rho F(s-rho)+Re E_f(s).   (2)

Zeros have their multiplicities. Their real-part sum is absolutely
convergent on bounded s sets; conjugate pairing makes the analytic
sum locally normal. The proof first treats f'(0)=0 and then uses
g(u)=exp(-cu)f(u), c=f'(0)/f0, plus the exact identity
E_g(s-c)-E_f(s)=f0[A_gamma(s)-A_gamma(s-c)]. This removes the special
endpoint derivative assumption without discarding its correction.

For 0<=x<=alpha and real y,

    Re[F(x+iy)+F(alpha-x+iy)] >= 0.                         (3)

Indeed the boundary values equal Re W(iy/eta)>=0, and the harmonic
minimum principle applies on the strip because the transforms tend
uniformly to zero at either vertical end. Reflection is rho ->
1-conjugate(rho); critical-line zeros contribute half an identical pair.

The same adapter proves, for -eta<=x<=alpha+eta and |y|>=10^10,

    |Re F(x+iy)| < 5eta/y^2,
    |Re E_f(sigma+iy)| < 2500eta/y^2.                       (4)

These bounds use piecewise third derivatives and integration by parts.
Their coarse derivative constants are separately checked. No positivity
outside the strip in (3) is presumed.

## 4. Favorable terms and the uniform scalar certificate

[The signed archimedean lemma](three-hour-type/LOGISTIC_NEGATIVE_ARCHIMEDEAN.md)
proves E_f(sigma)<=-.31eta throughout the stated domain. Its integral
estimate and rational series tails are independent of the prime gain.

[The four-prime lemma](three-hour-boundary/LOGISTIC_DEGREE12_PRIME_GAIN.md)
proves, for every real t,

    sum_n Lambda(n)n^(-sigma)f(log n)P(t log n)
                                      > 1.26eta-90eta^3.  (5)

It retains p=2,3,5,7 and respectively 10,6,5,4 powers. The factor
n^(-sigma)/(1+n^(-alpha)) is at least 1/(n+1). Every retained Taylor
weight for w is positive. Eight exact Bernstein polynomial covers
prove the endpoint bounds at eta^2=0 and (3/400)^2; affine dependence
on eta^2 proves every intermediate value. All omitted prime terms
are nonnegative. This is a uniform phase bound, not sampled phases.

On the closed rectangle

    0<=A<=200/963,                28<=l<=823/10,            (6)

put c_l=log(12+10^10 exp(-l)), mu=l/(l+c_l), eta=A/l,
sigma=1-A/(l+c_l), alpha=2sigma-1, z0=sigma-1, z1=z0+eta,
z2=sigma-eta. Define J(z,alpha)=integral_0^infinity
exp(-zu)/(1+exp(alpha*u))du. Curvature and the exact logistic identity
give the following lower bound for S=a1[F(z1)+F(z2)]-F(z0):

    S_low=a1 W(1-mu)-W(-mu)
      +eta*w0[a1/z2+J(z0,alpha)-a1 J(z1,alpha)-a1 J(z2,alpha)]
      -51eta^3[(z0+alpha)^(-3)+a1(z1+alpha)^(-3)+a1*z2^(-3)].

The proof is in [the master reduction](three-hour-root/LOGISTIC_MASTER_REDUCTION.md),
with the explicit changes in [the degree-12 reduction](three-hour-root/LOGISTIC_DEGREE12_REDUCTION.md).
In particular all three absolute transform errors have the adverse sign.
The numerical assertion needed for this theorem is precisely

    S_low - w0[A*aP/4-3.00317eta/2]
                       +1.57eta-90eta^3-10^(-7) > 0.     (7)

The 1.57eta consists of the distinct gains 1.26eta and .31eta.
No division by eta appears in (7), so A=0 is only its continuous
scalar extension; the physical kernel is always used with A>0.

Two implementations prove (7) on all of (6):

* [Directed interval producer](three-hour-root/certify_logistic_degree12.py):
  39 closed boxes, minimum lower bound greater than 7.02*10^(-6).
* [Independent Fraction replay](three-hour-type/verify_logistic_degree12_fraction.py):
  70 closed boxes, minimum lower bound greater than 1.76019*10^(-6).
  It checks disjoint interiors, containment, and exact area 3620/321.

Both reconstruct the polynomial and reject an unsupported A=1/4.
The Fraction implementation derives its kernel moments separately,
uses only integer/rational interval decisions, and evaluates elementary
functions with explicit Taylor tails. W uses 25 moments with remainder
less than 10^(-20); J uses a positive beta series with a one-sided
geometric remainder. [REPRODUCING.md](REPRODUCING.md) distinguishes
this finite proof from the analytic lemmas it assumes.

## 5. Global contradiction and all error budgets

Let Astar=200/963, Lstar=exp(21.233*Astar)<82.3 and Tstar=exp(Lstar).
Yang's region gives b(rho)=(1-beta)log|gamma|>=Astar for
|gamma|>=Tstar. A zero violating the proposed theorem must have
H<|gamma|<Tstar. Choose among this finite range one with minimal
b=B. Then 0<B<Astar, and all zeros above H have b>=B, including
those outside the finite range. By conjugation take its height t>0.

Set eta=B/log t, sigma=1-B/log(12t+10^10), and l=log t. All zeros
with |gamma|<=12t+10^10 satisfy 1-sigma<=beta<=sigma, by the minimum
property, reflection, and finite verification for |gamma|<=H.
Thus (3) discards their pairs except the selected pair at frequency1.
That pair contributes F(z1)+F(z2), with the exact z's of Section4.

For completeness, the tail proof in
[the global wrapper](three-hour-global/LOGISTIC_GLOBAL_WRAPPER.md)
is specialized and checked for K=12 in
[the degree-12 wrapper](three-hour-global/LOGISTIC_DEGREE12_GLOBAL_WRAPPER.md).
For q=kt, 1<=k<=12, T=12t+10^10, and
phi(x)=(x-q)^(-2)+(x+q)^(-2), Lehman's bound gives

    sum_(gamma>T) phi(gamma) < 10^(-9)(l+4).

For example its principal integral is at most
2[log(10^10+q)/10^10+log(1+q/10^10)/q]
<=2*10^(-10)(l+4); the endpoint and secondary integrals are
at most 8*10^(-20)(l+3)+4*10^(-20). Hence (4)'s paired-zero
loss is less than 2.4*10^(-9) at each positive frequency.
The zero-frequency loss is less than 4*10^(-10). These estimates
count multiplicities and both height signs; endpoint zeros may be
included by a one-sided limit.

The digamma bound at k>=1 has error below 10^(-12). Monotonicity
of psi on the positive real axis and (1) bound the gamma sum by
aP*l/2-3.00317+2*10^(-12). Weighted high-frequency E errors are
below 10^(-20), and pole errors below 10^(-24). Since 1+aP<5,
all adverse tail, gamma, E and pole errors together are strictly
below the relaxed budget 10^(-7). The negative real-axis E term
is already explicitly retained in (7).

Multiply (2) at s=sigma+ikt by ak and sum k=0,...,12. Apply (5),
the isolated-zero lower bound, the gamma upper bound, and the
error budget. The result is

    S - w0[B*aP/4-3.00317eta/2]
                       +1.57eta-90eta^3-10^(-7) <= 0.

This contradicts (7), since S>=S_low, A=B and l=log t lie in (6).
For 3<=|t|<=H the asserted right boundary exceeds 1/2, so the
finite RH verification supplies the conclusion directly. Negative
heights follow by conjugation. This completes the proposed proof.

## 6. Review boundary

The smallest numerical failure would be a wrong outward enclosure or
missing part of the closed rectangle. The smallest analytic failure
would be a wrong explicit-formula correction, zero-pair domain, or
global tail budget. Each has a separate component proof and review;
none is authenticated merely by a successful scalar JSON output.
The external finite RH verification and published Littlewood theorem
are imported, not recreated here. The complete assembled implication
requires its own exact-commit review before promotion.

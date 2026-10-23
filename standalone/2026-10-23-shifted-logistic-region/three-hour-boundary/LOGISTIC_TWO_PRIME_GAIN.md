# An exact two-prime lower contribution for logistic smoothing

2026-10-21. This is an elementary refinement of the arithmetic side of
the logistic detector. It uses the fixed BTY degree-16 polynomial, the
exact logistic weight, and independently certified kernel constants.
It does not use a numerical minimizer or a prime-distribution theorem.

Let P(x)=sum a_k cos(kx) be the squared-polynomial BTY choice, normalized
by a0=1. Its coefficients are nonnegative, and therefore

    0<=P(x)<=P(0)=1+2919857/828465.

Let f(u)=eta*w(eta*u)/(1+exp(-(2sigma-1)u)), where
1/2<=sigma<=1, 0<eta<=3/400, and theta=5669/5000. The independent
constant packet gives w0>567/100, w>=0, w'(0)=0, and ||w''||<350
for its C2 compact extension. Consequently w(v)>=w0-175v^2.

For y=p^m>=1 one has the exact inequality

    y^(-sigma)/(1+y^(-(2sigma-1)))
      = y^(-1/2)/(2cosh((sigma-1/2)log y)) >= 1/(y+1).   (P1)

The lower Taylor bound w0-175eta^2 m^2(log p)^2 is positive for the
retained pairs (p,m)=(2,1..10),(3,1..6), throughout the stated eta
range. This positivity is essential when multiplying (P1).

Define G_(p,M)(x)=sum_(m=1)^M P(mx)/(p^m+1). The companion exact
integer/Fraction checker proves, for every real x,

    G_(2,10)(x)>27/125,
    G_(3,6)(x)>19/400.                                 (P2)

To see the resulting detector contribution, retain only these prime
powers in the nonnegative arithmetic sum. Their respective arguments
x=t log p can be different: the uniform bounds (P2) apply separately.
Using (P1), the kernel Taylor bound, and P(mx)<=P(0), one obtains

    sum_n Lambda(n)n^(-sigma)f(log n)P(t log n)
      >=eta*w0[(27/125)log2+(19/400)log3]
        -175eta^3 P(0) sum_(p,M) (log p)^3
                             sum_(m=1)^M m^2/(p^m+1)
      > (11447/10000)eta-2775eta^3.                    (P3)

The last strict rational comparisons use

    .6931<log2<.6932,  1.0986<log3<1.0987.

The exact linear lower value is 1144733877/10^9>1.1447. Substituting
the rational upper logarithms in the cubic coefficient gives a value
less than 2775. The checker certifies these comparisons using the
positive atanh series for logarithms, with a geometric tail. It also
checks positivity of both retained Taylor lower bounds.

## Exact polynomial certificate

The coefficients a_k are reconstructed from the source integer vector
c=(4,-8,2,20,-9,-34,27,91,-27,-201,32,895,1949,2389,1896,949,239),
with sum c_j^2=14912370. Thus all input polynomial coefficients are
rational. Put y=cos x. The identity cos(mx)=T_m(y) turns each G into
a rational polynomial of degree 160 or 96 on [-1,1]. After y=2u-1,
the checker converts its power coefficients to Bernstein coefficients

    b_k=sum_(i<=k) a_i binom(k,i)/binom(n,i).

It subtracts the claimed lower bound before conversion. A common
denominator makes all Bernstein coefficients integers. Exact midpoint
de Casteljau subdivision uses additions and powers of two only. On
each accepted interval every Bernstein coefficient is strictly positive,
which proves the polynomial positive there by the Bernstein partition
of unity. Six closed rational intervals cover [0,1] for each prime;
the checker verifies their endpoints and exact gap-free adjacency.
The JSON records those intervals and their rational positive reserves.

`verify_logistic_prime_minima.py` uses no floating-point acceptance.
It also rejects a deliberately false lower bound at the exact endpoint
x=0. The output `LOGISTIC_PRIME_MINIMA.json` authenticates the checker
by SHA256. Its scope is the elementary arithmetic inequality (P3).

In a complete logistic master inequality one may therefore add
1.1447eta-2775eta^3 to the previous sufficient margin. This addition
has the favorable sign because the prime side now has that lower bound.
A stronger zero-free constant still requires a new full parameter
certificate and matching global wrapper; (P3) alone does not assert it.

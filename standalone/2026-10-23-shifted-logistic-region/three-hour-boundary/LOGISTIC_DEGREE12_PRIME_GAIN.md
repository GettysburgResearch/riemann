# Exact four-prime gain for the rational degree-12 detector

2026-10-21. This is a separate polynomial and certificate. The original
degree-16 and R=4.84/4.82 files remain unchanged. This lemma alone is
not a global zero-free theorem.

Let

    c=(3500513104,-5906953599,-1574092731,18166603739,
       6213449589,-38436761903,-16088159026,168141762350,
       447056663730,616860378424,541372347258,298691298328,
       83048065550),
    E=10^14,
    N=sum_(j=0)^12 c_j^2+13E=1000000001299439064580929,
    P(x)=[|sum_(j=0)^12 c_j exp(ijx)|^2
                        +E|sum_(j=0)^12 exp(ijx)|^2]/N.

Thus P>=0. Its cosine coefficients are

    a0=1,
    a_k=2[sum_(j=0)^(12-k) c_j c_(j+k)+(13-k)E]/N, k>=1.

The checker reconstructs these exact fractions and verifies a_k>0,
a1>1, and sum_(k>=1)a_k<4. The auxiliary square is part of the exact
definition; no numerical optimization output or rounded coefficient
is used as a proof premise.

Use the same logistic smoothing with theta=5669/5000,
1/2<=sigma<=1, 0<eta<=3/400. The independently proved curvature
lemma `LOGISTIC_CURVATURE_51.md` gives

    w(v)>=5.67-(51/2)v^2.

Write t=eta^2, T=(3/400)^2 and define

    G_p(x)=sum_(m=1)^M P(mx)/(p^m+1),
    H_p(x)=sum_(m=1)^M m^2 P(mx)/(p^m+1).

For the following exact rational table, L_p is an upper bound for log p:

| p | M | g_p | h_p | L_p |
|---|---|-----|-----|-----|
| 2 | 10 | .2194 | 60 | .6932 |
| 3 | 6 | .04913 | 22 | 1.0987 |
| 5 | 5 | .00747 | 9 | 1.6095 |
| 7 | 4 | .00215 | 4 | 1.9460 |

The checker proves, for every real x and at both t=0 and t=T,

    5.67G_p(x)-(51/2)t L_p^2 H_p(x)>5.67g_p-h_p t.       (D1)

Since the difference is affine in t, (D1) holds throughout [0,T].
This interpolation is an exact convex combination, not a grid in eta.
The checker verifies the positivity of every retained weight
5.67-(51/2)t L_p^2 m^2 at the endpoint T, hence throughout [0,T].

For y=p^m, the exact identity and monotonicity of cosh give

    y^(-sigma)/(1+y^(-(2sigma-1)))
       = y^(-1/2)/(2cosh((sigma-1/2)log y))>=1/(y+1).

The retained Taylor lower bound is positive, so this comparison can
be multiplied in the favorable direction. Applying it at each retained
prime power and using (D1), their total contribution is at least

    eta sum_p (log p)[5.67g_p-h_p eta^2].                (D2)

All other terms in the arithmetic detector are nonnegative. Exact
atanh series certify lower logarithms (.6931,1.0986,1.6094,1.9459)
and upper logarithms from the table. They give

    5.67 sum_p g_p log p >126013629987/10^11>1.26,
    sum_p h_p log p <880329/10000<90.

Therefore, uniformly for every real t_height and the stated sigma,eta,

    sum_n Lambda(n)n^(-sigma)f(log n)P(t_height log n)
       >1.26eta-90eta^3.                               (D3)

The eight endpoint polynomial certificates use y=cos x, exact
Chebyshev recurrence, and the Bernstein basis after y=2u-1. Subdivision
uses integer de Casteljau additions and powers of two. Every accepted
Bernstein coefficient is positive; the closed rational intervals form
a checked gap-free cover of [0,1]. The companion JSON records all
covers, exact coefficients, and source/dependency hashes. There is
also an exact false-bound negative control.

`verify_logistic_degree12_primes.py` imports only the frozen exact
Chebyshev/subdivision/logarithm helpers in `verify_logistic_prime_minima.py`.
It does not use that file's degree-16 coefficients for this calculation.
No floating-point value is used for any acceptance decision.

A full degree-12 zero-free argument must also use K=12 in its height
cutoff, the new a1 and coefficient sum, and a separately certified
archimedean constant. Its sufficient scalar margin gains 1.26eta-90eta^3
from (D3), in addition to any independently proved negative E_f term.
The old degree-16 scalar certificate cannot itself establish that result.

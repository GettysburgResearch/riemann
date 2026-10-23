# Retaining the prime terms on both sides of the Ford detector

Status: proposed analytic refinement with an exact finite certificate,
23 October 2026. This is a component of the weighted Ford detector, not
a zero-free theorem by itself. Use the exact degree-12 polynomial from
the frozen logistic packet and the Ford kernel with theta=23/20.

Assume the separately certified kernel bounds w0>=6 and ||w''||<=70.
Since w is an even autocorrelation, w'(0)=0, so for every v>=0,

    w(v)/w0 >= 1-(35/6)v^2.

This remains valid outside the support: the curvature estimate is global
for the zero extension. The actual w is nonnegative everywhere.

Write P(x)=1+sum_(j=1)^12 b_j cos(jx)>=0. With the notation of
GENERAL_WEIGHTED_FORD_DETECTOR.md, the left Dirichlet sum is exactly

    D(t)=lambda sum_n Lambda(n) P(t log n)
                         exp(lambda log n) w(lambda log n)/n.

The right-line smoothing term in Ford (9.1) can also be kept exactly.
The Fourier transform of sech(u)^2 gives

    -(1/2) sum_j b_j integral_R log|zeta(3/2+ijt+iu/pi)| sech(u)^2 du
       = C0 - sum_n Lambda(n) P(t log n)/(n^2-n),

where C0=sum_n Lambda(n)/(n^2-n)<.851 is Ford's source constant.
This follows by the absolutely convergent Euler product, with no
exchange involving a conditionally convergent prime series.

Move the favorable second sum to the left together with D(t). After
division by w0, the amount added to the sufficient margin (G8) is

    lambda sum_n Lambda(n) P(t log n)
       [exp(lambda log n) w(lambda log n)/(w0*n)+1/(n^2-n)].   (P1)

Every summand in (P1) is nonnegative. Retain p=2,3,5,7 and respectively
10,6,5,4 powers. For each retained n=p^m, exp(lambda log n)>=1 and the
curvature bound show that its bracket is at least

    1/(p^m-1) - (35/6)*lambda^2*m^2*(log p)^2/p^m.           (P2)

These lower weights are positive on 0<=lambda<=1/160. We prove the
following phase-uniform bounds for each prime separately:

| p | powers | g_p | h_p |
|---|---:|---:|---:|
| 2 | 10 | 262/1000 | 11 |
| 3 | 6 | 527/10000 | 4 |
| 5 | 5 | 755/100000 | 2 |
| 7 | 4 | 218/100000 | 1 |

The sum of P(mx) times (P2) exceeds g_p-h_p*lambda^2 for every real x.
The checker replaces log p by a rational upper bound in the adverse
term, writes cos(kmx)=T_(km)(cos x), and certifies positivity by exact
Bernstein subdivision on cos x in [-1,1]. It checks both endpoints
lambda^2=0 and 1/160^2; affine dependence covers the whole interval.
Every subdivision is closed and the exact intervals form a gap-free
cover. An intentionally false lower bound is rejected at an endpoint.

Using independent rational lower and upper logarithms gives

    sum_p g_p log p > 63970363/250000000 > .255,
    sum_p h_p log p < 3437/200 < 18.

Consequently (P1) is strictly greater than

    .255*lambda-18*lambda^3.                                (P3)

This gain can be added to (G8). It is distinct from any improvement in
the outside-zero count; if that improvement also retains prime terms,
the terms must be traced to their separate original occurrences.

`verify_ford_prime_gain.py` reconstructs the polynomial from its integer
sum-of-two-squares coefficients and uses only integer/Fraction acceptance
decisions. Its JSON is evidence for the finite inequalities, not for the
external Ford explicit formula or the kernel bounds assumed above.


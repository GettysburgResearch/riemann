# Elementary Euler constants for the shifted detector

23 October 2026. Exact finite certificate with analytic tails; no zero-free
theorem is asserted by this component alone.

For 0<=lambda<=1/160, put sigma=1-lambda and 2eta=1-2lambda. Then

    C(lambda)=sum_n Lambda(n)n^(-sigma)/(n^(2eta)-1) < 9/10,
    Z(37/25)=sum_n Lambda(n)n^(-37/25) < 2.

Every summand in C increases with lambda, so the endpoint suffices.
The checker enumerates every prime power p^m<=N=10000 by an integer
Eratosthenes sieve and adds log(p), with its exact multiplicity, times
the stated weight. Its logarithms and exponentials use the frozen
192-bit outward-rounded rational engine
`../three-hour-type/verify_logistic_master_fraction.py`, SHA256
`cefd18641114b6fedd8cf3334bcdd2857da7d4694bbbbc951238603e90fc2413`.
No floating-point value participates in acceptance.

For the C tail put s=2-3lambda. Since Lambda(n)<=log(n), its omitted
positive terms have sum at most

    N^(1-s)[log(N)/(s-1)+1/(s-1)^2]
          /[1-(N+1)^(-2eta)].

For the Z tail use the numerator of this expression with s=37/25.
These follow by integrating the decreasing function log(x)x^(-s)
from N to infinity. The checker verifies the decreasing-domain condition.

`verify_shifted_euler.py`, SHA256
`aa9f8bc15a384712d14eb6037837769c3b82ecc8d8dc2ef023985c2a688d01bc`,
certifies strict upper bounds after all 1280 retained prime powers and
the two positive tails. The JSON stores the rational endpoints and
source hashes. Two deliberately false smaller bounds are rejected from
the retained partial sums. The analytic assumptions are the absolutely
convergent Euler product for real s>1 and Lambda(n)<=log(n).

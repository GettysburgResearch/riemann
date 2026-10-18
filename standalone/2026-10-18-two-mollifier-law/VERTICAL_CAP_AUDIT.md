# Attempted vertical escape: the cap still hides a fixed zero

Proposed elementary analytic calculation, not a zeta zero assertion. This
records an attempted final step that does not close RH; it is not an input
to the two-mollifier moment law.

Let f be holomorphic near rho=sigma+i gamma, with a zero of multiplicity
m>=1 and f(s)=c(s-rho)^m(1+O(|s-rho|)), c!=0. Choose a fixed small h>0
so there are no other zeros on the vertical segment. For every fixed integer
k>=1 put q=2km. As C tends to infinity,

 integral_(gamma-h)^(gamma+h) min(|f(sigma+it)|^(-2k),C) dt
  ~ [2q/(q-1)] |c|^(-1/m) C^(1-1/q).                       (1)

For the exact monomial f(sigma+it)=c[i(t-gamma)]^m, once
(C |c|^(2k))^(-1/q)<h, the equality is

 [2q/(q-1)] |c|^(-1/m) C^(1-1/q)
    -[2/(q-1)]|c|^(-2k)h^(1-q).                           (2)

Proof: split at |t-gamma|=|c|^(-1/m)C^(-1/q), integrating the constant
part and the complete power tail. For general f, rescale by that radius.
The integrand divided by C converges to min(1,|v|^(-q)). On the fixed small
segment, |f| is comparable to |c||t-gamma|^m; after rescaling this supplies
the integrable majorant min(1,K|v|^(-q)). Extend by zero beyond the growing
scaled segment and apply dominated convergence. This proves (1), including
multiplicity. Endpoint zeros instead have a one-sided constant.

For a simple zero and k=1 the growth is4|f'(rho)|^(-1) sqrt(C). Thus
integrating a capped law vertically does NOT automatically restore an
uncapped inverse estimate. At C=U^(1/4) the hypothetical zero's contribution
would grow as U^(1/8), entirely compatible with the two-mollifier theorem's
U-sized family mean. Constants in (1) concern one fixed f and zero; no
uniform assertion for growing families or arbitrarily close zeros is made.

In particular, an unproved o(sqrt(C)) bound for this one fixed vertical
integral would exclude all zeros on that segment, but the current arithmetic
estimates supply no such bound. This is a calculation of the missing cap
sensitivity, not an RH proof or discovery of off-line zeros.

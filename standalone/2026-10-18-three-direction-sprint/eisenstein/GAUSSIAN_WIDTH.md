# Gaussian-width trade for the full periodic deflator

**PROPOSED analytic component theorem.** This pays the derivative and
conditional-character issues in a fixed-field ordinary-zeta converter.
It bounds a converter on a uniform class of whole trajectories; it is not
a critical arithmetic-energy estimate for those trajectories.

Fix real c, tau>0, and set, in the log-scale variable x,

    q_tau(x)=exp(cx-x^2/(4tau))/sqrt(4pi tau).

Thus the Gaussian source used in PROOF.md is
`A_tau(D)=sum_n a(n)q_tau(log D-log n)`, with ideal norms in place of n
when appropriate. The semigroup identity is exact:

    q_tau=q_(tau-tau')*q_tau', 0<tau'<tau,             (1)

where convolution uses ordinary Lebesgue measure in x. Polynomial growth
of the coefficients suffices for all pointwise source identities below;
Tonelli applied to their absolute Gaussian majorants justifies (1) inside
the complete infinite arithmetic sums.

## 1. A complete character kernel with explicit weighted L1 norm

Let chi be any fixed mean-zero periodic sequence, extended by its actual
zeros, and suppose its partial sums have modulus at most B. For Delta>0 put

    K_(chi,Delta)(x)=sum_(n>=1)chi(n)q_Delta(x-log n).

The defining sum is absolutely convergent at each x. It is neither a
finite Dirichlet polynomial nor a replacement of chi by independent signs.
For every r>0,

    integral_R exp(-rx)|K_(chi,Delta)(x)| dx
       <=B exp(Delta(c-r)^2)[1+1/(r sqrt(pi Delta))].    (2)

Proof. Write C(t)=sum_(n<=t)chi(n). Abel summation, retaining the endpoint
at 1 and using C(1^-)=0, gives

    K(x)=integral_1^infinity C(t)q_Delta'(x-log t)dt/t.

Its absolute value is at most `B integral_(-infinity)^x |q_Delta'(u)|du`.
Integrating this nonnegative majorant against exp(-rx) and interchanging
integrals proves a bound `(B/r) integral exp(-ru)|q_Delta'(u)|du`.
The latter integral equals

    exp(Delta(c-r)^2) E|r-Z/sqrt(2Delta)|,

where Z is a standard real Gaussian. Since E|Z|=sqrt(2/pi), (2) follows.
Both complete Gaussian tails and every character residue are retained.

## 2. A no-scale-loss transfer on uniform power-bounded past norms

For 1<=p<=infinity, real sigma, and eta>=0, define

    N_(sigma,p,eta)(A)
      =sup_(T>0) T^(-eta)
          ||D^(-sigma)A(D)||_(Lp((0,T],dD/D)).          (3)

Assume r=sigma+eta>0. If A_tau'=sum a(n)q_tau' as above, then the complete
character deflation of its wider Gaussian satisfies

    T_chi A_tau(D)=sum_n chi(n)A_tau(D/n)
                 =(K_(chi,Delta)*A_tau')(log D),
    Delta=tau-tau'.                                  (4)

The equalities are literal complete arithmetic convolutions; all their
absolute Gaussian majorants are summable at each fixed D. Minkowski and
(2) give the horizon-independent bound

    N_(sigma,p,eta)(T_chi A_tau)
       <=B exp(Delta(c-r)^2)[1+1/(r sqrt(pi Delta))]
                                    N_(sigma,p,eta)(A_tau'). (5)

Indeed a log shift u has weighted past norm at most
`exp(-sigma u)N(A) (T exp(-u))^eta`. Its complete integral is exactly the
weighted kernel norm with exponent r. No vertical supremum of L(s,chi)
below Re s=1 has been assumed, and no divergent absolute Dirichlet norm
of the unsmoothed character operator has been used.

For E_F in LEGAL_FIELD.md, the three fixed character deflators therefore
transfer a uniform power estimate from width tau' to the ordinary source
at width tau with the SAME power eta. Allocate positive widths
Delta_1+Delta_2+Delta_3=tau-tau'. The explicit total cost is

    exp((tau-tau')(c-r)^2)
          product_(j=1)^3 B_j[1+1/(r sqrt(pi Delta_j))]. (6)

The source factorization still removes all three entire auxiliary
L-functions exactly. This width trade does not require any of them to
be zero free, and does not introduce a scale or logarithmic loss.

The uniformity in (3) is essential. A single bound on A_tau' only up to
one horizon T0 does not suffice: Gaussian smoothing samples larger
horizons as well. Formula (5) is a theorem about a common all-horizon
power estimate, which is the usual asymptotic source hypothesis. For
these Gaussian arithmetic sources, a bound originally stated for T>=1
extends to T>0 with a finite additional constant using their complete
small-D Gaussian decay. No causal finite-horizon width inverse is claimed.

## 3. Explicit normalized derivative costs

The same argument pays fixed or growing log-scale derivatives. For every
integer j>=0 and radius rho>0, complex Cauchy on q_Delta gives

    integral exp(-rx)|q_Delta^(j)(x)| dx
       <=j!rho^(-j)
           exp(Delta(c-r)^2+r rho+rho^2/(4Delta)).      (7)

To verify it, on a circle z=a+ib with |z|=rho the weighted integral of
`|q_Delta(x+z)|` is exactly
`exp(Delta(c-r)^2+r a+b^2/(4Delta))`. Bound a<=rho,b^2<=rho^2 and apply
the Cauchy integral formula. Thus the normalized derivatives
`rho^j D_x^j A_tau/j!` have a bound UNIFORM in j on (3), at the explicit
fixed-width cost in (7). Omitting that normalization would be false.

For example a logarithmic coefficient has the exact source identity

    sum_n a(n)log n q_tau(log D-log n)
       =(log D-2tau c)A_tau(D)+2tau D_x A_tau(D).      (8)

On a fixed annular length scale it therefore costs a logarithm and a
fixed derivative seminorm. For the marked polynomial in the fresh
structured-Gauss source, an actual ALL-prime weight A(n)=log Nn would be
controlled this way on squarefree n. Its annular prime-divisor weights
and common p-dependent reflected kernels are generally different.
Equations (7)--(8) do not silently extend the unmarked theorem to those
weights.

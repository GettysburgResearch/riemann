# Director adjudication: derivative moments, gcd covariance and prime phases

17 November 2026. I checked both source-based derivations prime_array63_hlz_derivative_tail.md and prime_array63_hlz_classical_independent.md, the primary shifted theorem and the independent harmonic argument prime_array63_tail_prime_torus_review.md. Heap–Li–Zhao's journal Theorem 5, §4 p.1605, has the necessary small complex shifts; the proof starts p.1607. The arXiv v1 counterpart is Theorem 2. The source's negative-moment theorem and its additional simplicity hypothesis are not being used.

For any fixed real Dirichlet polynomial Q(s)=sum a_m m^(-s), RH gives

    sum_(0<gamma<=T)|zeta'(rho)Q(rho)|^2
      = S(Q) T log^4 T/(24 pi)+O_Q(T log^3 T),
    S(Q_a,Q_b)=sum_(m,n) a_m b_n/lcm(m,n).

Double Cauchy differentiation is valid on nested separated complex-shift circles. The source J term has xy coefficient tau^4/3, the sum of its two I terms has -tau^4/4, leaving tau^4/12. The outer factor 1/(2 pi) supplies the constant. The source's conjugate transpose in the second I term must be retained; on the real diagonal it gives the same expression. No uniformity in a growing polynomial is claimed here.

Sparse composite Q_k=k^(1-s)-1 does not itself satisfy the printed submultiplicative coefficient hypothesis. This obstruction is repaired for every fixed polynomial by padding its divisor-closed support with a fixed large positive baseline P. Each of P, P+Q and P-Q is nonzero throughout that support and meets the source coefficient hypotheses. The quadratic identity F(Q)=(F(P+Q)+F(P-Q))/2-F(P) transfers the theorem. Constants depend on this fixed padding. Using a source theorem while ignoring the zero coefficients would not justify the specialization.

Real polarization, partial summation against (t^2+1/4)^(-1) and reflection give

    sum_(|gamma|>Y) |zeta'(rho)|^2 Q_k(rho)overline(Q_l(rho))/|rho|^2
       = (gcd(k,l)-1) log^4 Y/(12 pi Y)
         +O_(k,l)(log^3 Y/Y).

The strict-tail endpoint subtracts one leading copy and the integral supplies two. Multiple zeros contribute zero. The raw Gonek moment has log power FOUR, whereas its average per zero has log power THREE. An early owned draft confused those normalizations; it was corrected before canonical adoption. The k=2 coefficient is 1, not 3.

For the normalized tail of nu from the inverse theorem, the same calculation on the polynomials m^(-s), n^(-s) yields

    F_Y(log(m/n))/B_Y -> gcd(m,n)/sqrt(mn).

For any fixed collection of primes these are precisely the Fourier coefficients of independent Poisson circle laws of radii p^(-1/2). Character convergence and Stone–Weierstrass give weak convergence on the countable product prime torus. The factorial variables have mean zero and covariance gcd(k,l)-1=sum_(d|k,d|l,d>=2)phi(d). Distinct prime indices are orthogonal in that high-tail limit. This concerns a derivative-weighted draw of one ordinate, not spacings or unweighted zero statistics.

The limit on log-positive-rationals is discontinuous in the ordinary real topology: (n+1)/n tends to 1 while the coefficient tends to 0. There is no corresponding limiting real-line probability; the normalized tails escape every bounded height interval. For each fixed Y the actual Fourier transform is continuous at zero. Arbitrarily close large prime ratios consequently make its discrepancy from 1/sqrt(pq) tend to 1. Thus no uniform approximation over all prime pairs is possible even for the actual weighted tails. Fixed-prime weak convergence and this nonuniformity coexist. A prescribed growing block such as primes below log^A Y needs source constants and a uniform shifted-moment analysis, not a diagonal argument. Publication priority of these deductions has not been established.

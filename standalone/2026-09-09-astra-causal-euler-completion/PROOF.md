# EPC26: exact causal completion and constructive finite Euler repair

Date: 2026-09-09. Author: Astra.
**Status: PROPOSED; independent mathematical review required. RH is NOT proved.**
The new positive result explicitly attains the infimum, in the limit, of the
complete energy over all late multiplicative repairs of a finite Euler product.
An elementary power-saving bound controls the entire omitted error. The value
of this infimum is a native arithmetic quantity which is not bounded here by
a subpower of the preserved prefix. Finite factorization is not that bound.
No novelty is claimed for Hilbert-space projection or finite geometric series.

## 1. The primitive source, including its entire future

For a finite real sequence a=(a_n) on the positive integers let

    P_a(s)=sum_n a_n n^(-s),  A_a(x)=sum_(n<=x) a_n,
    h_a(t)=exp(-t/2) A_a(exp t),  t>=0,
    J(a)=||h_a||_2^2=integral_1^infinity A_a(x)^2 dx/x^2.

All sums over coefficients retain every nonzero term and combine coincident
indices. Direct cell integration and finite pair expansion give

    J(a)=sum_(k>=1) A_a(k)^2/[k(k+1)]
        =sum_(m,n) a_m a_n/max(m,n).                         (1)

The first sum includes the constant cumulative tail after the last event.
If the sorted support is n_1<...<n_l, it can be evaluated finitely by the
successive differences 1/n_i-1/n_(i+1), followed by A_a(n_l)^2/n_l.
The bilinear version is denoted <a,b>_J. In particular J is positive definite
on finite sequences, not merely semidefinite.

Plancherel equivalently gives

    J(a)=(1/(2pi)) integral_R |P_a(1/2+it)|^2/(1/4+t^2) dt.  (2)

Indeed the Laplace transform of h_a is P_a(s)/s, s=z+1/2. Only finite sums
of shifted exponentials are involved. None of our bounds replaces this
whole frequency line or the whole causal time line by a window.
For d>=1, multiplication of P_a by d^(-s) acts on h_a as

    U_d h(t)=d^(-1/2) h(t-log d) 1_(t>=log d),
    ||U_d||=d^(-1/2),  U_d U_e=U_(de).                    (3)

This norm and its factor d^(-1/2) are essential.

Let mu be the ordinary Mobius function, M(k)=sum_(n<=k)mu(n), and Y>=1 an
integer. The fixed prefix is a_n=mu(n) for EVERY n<=Y. Define

    E_Y=sum_(k=1)^Y M(k)^2/[k(k+1)],
    m_Y=sum_(n=1)^Y mu(n)/n,
    c_Y=sum_(k=1)^Y M(k)/[k(k+1)]=m_Y-M(Y)/(Y+1).           (4)

These are exact rational quantities. In contrast, the native stopped source
from PR829 has energy

    J_Y=E_Y+M(Y)^2/(Y+1).                                 (5)

That terminal difference is not negative mass available to cancel the past.

## 2. EPC26-1: solve the entire free completion problem exactly

Among ALL finite real sequences preserving that prefix,

    min J(a)=E_Y.                                         (6)

The unique minimizer has Dirichlet polynomial

    C_Y(s)=sum_(n<=Y)mu(n)n^(-s)-M(Y)(Y+1)^(-s).           (7)

Its cumulative source is M(k) on cells k<=Y and zero on all later cells.
For every other prefix-preserving a, if r=a-C_Y then

    J(a)=E_Y+J(r).                                        (8)

Proof: the source of C_Y is supported on [0,log(Y+1)); the source of r is
supported on [log(Y+1),infinity). They are orthogonal in the actual L2 norm.
All sources preserving the prefix must pay the same first term. Vanishing
of the second term is equivalent to r=0. This proves (6)--(8), without an
estimate for mu, an optimized numerical matrix, or a support cutoff.
The value E_Y is monotone in Y, but no useful subpower upper bound follows
from monotonicity. The elementary bound |M(k)|<=k only gives E_Y<Y.

### A safe-point zero has an exact, nonzero price

Among all prefix-preserving finite a additionally satisfying P_a(1)=0,

    min J(a)=F_Y:=E_Y+(Y+1)c_Y^2.                         (9)

The unique minimizer is

    C_Y^0(s)=sum_(n<=Y)mu(n)n^(-s)
                -(Y+1)m_Y (Y+1)^(-s).                   (10)

To prove this, finite summation by parts, including its infinite constant
tail, gives P_a(1)=sum_(k>=1) A_a(k)/[k(k+1)]. The tail weights k>=Y+1 sum
to 1/(Y+1). The constraint requires their weighted sum to be -c_Y.
Cauchy--Schwarz bounds their energy below by (Y+1)c_Y^2, with equality
precisely at the constant tail A_a(k)=-(Y+1)c_Y. This is (10).
For any other feasible a, r=a-C_Y^0 vanishes on the prefix and P_r(1)=0.
The constant tail of C_Y^0 is orthogonal to r, so exactly

    J(a)=F_Y+J(r).                                        (11)

A safe-point condition is therefore not free. Higher safe-point derivatives
are NOT imposed or solved by this one-constraint theorem. Equations (6),(9)
are two distinct minimization problems.

## 3. EPC26-2: finite geometric factors compile an admissible repair

For Y>=2 write

    Mcal_Y(s)=product_(p<=Y)(1-p^(-s)),

where p ranges over every prime through Y. This is the COMPLETE Euler
polynomial, with all squarefree divisors retained. Fix any real H>=Y and set

    m_p=min{m>=1:p^m>H},       q_p=p^(m_p),
    G_(Y,H)(s)=product_(p<=Y) sum_(j=0)^(m_p-1) p^(-js),
    D_(Y,H)(s)=product_(p<=Y)(1-q_p^(-s)).                 (12)

For either C=C_Y or C=C_Y^0 define

    B_(Y,H)(s)=C(s) G_(Y,H)(s),
    P_(Y,H)(s)=Mcal_Y(s) B_(Y,H)(s)=C(s) D_(Y,H)(s).      (13)

Every object in (12)--(13) is a FINITE Dirichlet polynomial. The equality is
an exact product of geometric identities, not a division by a possible zero,
not an infinite Euler inverse, and not a formal coefficient limit.
All coefficients of B satisfy

    b_1=1,  b_n=0 for 2<=n<=Y.                            (14)

Thus B is of the late multiplicative-repair form 1+sum_(d>Y)b_d d^(-s).
Proof: for n<=Y, every prime factor of n is <=Y and its exponent is strictly
below m_p. Hence the coefficient of G at n is exactly 1. The coefficient
of B at n<=Y is then sum_(d|n)mu(d), which is 1_(n=1). The extra term in C
is at Y+1 and cannot enter this calculation. This proves the prefix claim
without silently permitting early repairs.

For C=C_Y the coefficients are integers, with |b_d|<=2Y for every d.
For C=C_Y^0 they are rational, with |b_d|<=Y+(Y+1)sum_(n<=Y)1/n.
Indeed unique prime factorization makes every coefficient of G either 0 or 1,
so a convolution coefficient is bounded by the sum of absolute coefficients
of C. The free target has that sum at most 2Y; the displayed harmonic bound
handles the safe-point target. Thus huge coefficient magnitudes are not needed.
An upper bound on the number of additive repair terms, INCLUDING possible
cancellations only as a reduction, is (Y+1)product_(p<=Y)m_p.
Their total expanded number and maximum delay may be very large. Compression
by products does not mean that there are only pi(Y) additive repair terms.
One unconditional support bound is

    max supp B <= (Y+1) product_(p<=Y) p^(m_p-1),
    max supp P <= (Y+1) product_(p<=Y) q_p.                (15)

For H=Y^2, each q_p<=pY^2 and m_p>=3, so the support is NOT claimed to lie
below Y^A with a fixed A. This is outside the preceding sparse/fixed-relative-
delay obstruction, not a refutation of it. Bounds and computation below
retain the whole expanded output even when a product representation is used.

## 4. EPC26-3: a relative bound for the WHOLE energy

Set

    sigma_(Y,H)=sum_(p<=Y) q_p^(-1/2),
    eta_(Y,H)=product_(p<=Y)(1+q_p^(-1/2))-1
              <=exp(sigma_(Y,H))-1.                     (16)

Let E(C)=E_Y for C_Y and E(C)=F_Y for C_Y^0. Then

    E(C) <= J(P_(Y,H)) <= E(C) [1+eta_(Y,H)^2].           (17)

In fact the exact identity is

    J(P_(Y,H))=E(C)+J(P_(Y,H)-C).                         (18)

Proof: expansion of product_(p<=Y)(I-U_(q_p)) and the triangle inequality
in the actual source space give

    ||h_(P-C)||_2 <= eta_(Y,H) ||h_C||_2.                  (19)

All cross terms between different shifted copies are retained by this norm
inequality; they are not asserted orthogonal. For C_Y, the error starts only
after log(Y+1), so (8) applies. For C_Y^0, the product still has P(1)=0, hence
the error also has zero value at 1 and (11) applies. This yields (18),(17).
Merely bounding pointwise spectral values would not establish this identity.
Neither random prime phases nor resetting a transported distribution is used.

### Explicit asymptotic rate without PNT

For H=Y^2, one has

    sigma_(Y,Y^2) <= 3Y^(-1/3).                           (20)

Indeed q_p>Y^2 and q_p>=p^3, so q_p^(-1/2)<=min(Y^(-1),p^(-3/2)).
The decreasing function f(x)=min(Y^(-1),x^(-3/2)) satisfies

    sum_(n=2)^infinity f(n) <= integral_1^infinity f(x)dx
                             =3Y^(-1/3)-Y^(-1).

This proves (20) by enlarging primes to all integers. In particular for Y>=216,
use sigma<=1/2 and exp(sigma)-1<=2sigma to obtain

    0 <= J(P_(Y,Y^2))/E(C)-1 <=36Y^(-2/3).                (21)

This relative estimate is uniform in Y and has no unknown arithmetic constant.
For the free case E_Y>=1/2, so division is harmless. The safe-point case is
larger. The asymptotic is relative to the TRUE optimum, not relative to zero.

More generally, for a fixed integer a>=2 and H=Y^a, the same proof gives

    sigma_(Y,Y^a) <= [(a+1)/(a-1)]
                      Y^(-a(a-1)/(2(a+1))).              (22)

Use q_p>=p^(a+1) and integrate min(Y^(-a/2),x^(-(a+1)/2)); its breakpoint
is Y^(a/(a+1)). This gives tunable accuracy at larger support cost. No symbolic
parameter is silently held fixed while its support costs are suppressed.

### Exact infima within the multiplicative class

For each FIXED Y, allowing arbitrary finite late repair supports,

    inf_(B finite, b_1=1,b_2=...=b_Y=0) J(Mcal_Y B)=E_Y.    (23)

Adding (Mcal_Y B)(1)=0 changes the infimum to F_Y. For a fixed Y, let H tend
to infinity in (12); then sigma<=pi(Y)/sqrt(H) tends to zero, and (17) gives
both upper limits. The universal lower limits were proved in Section 2.
This statement does not claim that the multiplicative infimum is attained
by a finite B; the unconstrained causal completion is attained by C.
Thus a full finite Euler factor is NOT an irreducible excess-energy barrier
once sufficiently rich late repairs are allowed. The immutable cost is the
ordinary arithmetic prefix energy, not the artificial complete-prime tail.

## 5. EPC26-4: the complete RH implication and its exact remaining gap

A subpower bound along an unbounded sequence,

    log(1+E_Y)/log(Y+1) ->0,                              (24)

would imply RH. This is the native/Mertens causal criterion from PR829 and
the previous attempt, applied now to the exact optimal completion C_Y rather
than the stopped source. We include the proof so no unreviewed repository
claim is a hidden premise.

Put s=z+1/2 and define the ordinary causal source

    d(t)=exp(-t/2)[floor(exp t)(1-t)+log(floor(exp t)!)].

For x=exp t, m=floor x, the bounds on sums of log n give

    0<m(1-log x)+log(m!)<=1+log x,  ||d||_1<=6.

Its Laplace transform is (s-1)zeta(s)/s^2. Initially Re s>1 this follows by
summing/integrating the floor and log-factorial terms; the pole at s=1 is
removable. The ordinary L1 source then supplies analytic continuation to
Re z>0. For any finite prefix-preserving a, y_a=d*h_a has norm at most
6sqrt(J(a)) and transform

    (s-1)zeta(s)P_a(s)/s^3.

Before t=log(Y+1), finite divisor inversion gives exactly

    y_a(t)=h_*(t):=exp(-t/2)(t-t^2/2),  ||h_*||_2=sqrt(2).

For example the convolution expands into exp(-t/2) times
sum_(m<=exp t)(sum_(n|m)a_n)[u-u^2/2], u=t-log m; the divisor coefficient
is delta_(m=1) before that time. This retains the literal arithmetic prefix.

If rho=beta+i gamma is a nontrivial zero with alpha=beta-1/2>0, its evaluation
of the output transform is zero, whereas Lh_*(rho-1/2)=(rho-1)/rho^3 is not.
Cauchy--Schwarz on the ENTIRE delayed error support gives

    6sqrt(J(a))+sqrt(2) >= sqrt(2alpha)|rho-1|/|rho|^3
                                      (Y+1)^alpha.       (25)

Take a=C_Y so J(a)=E_Y. Equation (24) contradicts (25). The zeta functional
equation reflects any left-of-line nontrivial zero to the right. Hence RH
follows from (24). No zero census, simplicity, PNT error bound, or unknown
sign property enters the conditional ending.

THE MISSING ESTIMATE IS (24). Neither the geometric compiler nor its relative
power-saving error proves it. Indeed (6),(23) show that no late completion in
these classes can lower the source below E_Y at all. The construction solves
the completion/minimization layer; the signed arithmetic up to Y remains.
The extra price (Y+1)c_Y^2 in (9) also cannot be called subpower without proof.
For illustration only, if this price or E_Y is evaluated on a finite range,
its numerical size does not certify an unbounded sequence satisfying (24).

The attempted full route has therefore reached the following exact form:

    literal prefix -> explicit near-optimal complete Euler repair
    -> [UNPROVED: subpower prefix energy] -> exclusion of every off-line zero.

This is constructive progress over the failed sparse repair, not a complete
RH proof. The previous sparse-annihilator lower bound remains compatible:
our large expanded correction dictionaries and very long delays violate its
fixed-small-complexity/fixed-polynomial-delay hypotheses. No theorem about
another branch's different affine optimization problem is inferred.

## 6. Reproducibility and review scope

The two standard-library programs reconstruct mu, complete coefficients,
P(1), integer-cell/pair-kernel energies, orthogonality and all finite factors.
A prime-power cutoff is tested with strict >H, not >=H. Directed bounds on
eta use integer square roots; no floating point or quadrature enters acceptance.
The geometric expansion is fully checked for the declared small cases and
never claimed fully enumerated for the symbolic all-Y statement. All outputs
include their terminal tails. The proofs, not finite extrapolation, establish
(6)--(25). Both programs have the same author and do not constitute independent
mathematical review. No full repository validator or formal proof build is
claimed unless a separate execution receipt explicitly reports it.

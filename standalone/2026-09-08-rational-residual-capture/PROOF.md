# Uniform rational capture of the complete arithmetic residual form

Date: 2026-09-08. Author continuation of PR #803.
Status: proposed complete COMPONENT proofs; independent review required.
**No subpower residual bound, zero-free-region improvement, or RH proof is claimed.**
Frozen parent: bcec690c1607e281bd6f741b68f5c50f556670c7.
Local labels RC1--RC5 are not canonical claim IDs.

## 1. The proof obligation removed

The parent obtains the unknown growth exponent of a complete infinite residual
norm. The earlier numerical method evaluates its Gram entries through pair
periods and infinite weights. Here the SAME norm is enclosed, uniformly over
its whole coefficient space, by a finite RATIONAL quadratic form. This is
not an asymptotic for a fixed trial vector, a source substitution, or a
zero-spectrum truncation. All coefficients, cross terms, and the infinite
future are retained.

For an integer N>=2, b in C, and a=(a_1,...,a_N) in C^N satisfying

    sum_(n=1)^N a_n/n=0,                                      (1)

put

    u(x)=b-sum_(n=1)^N a_n floor(x/n),   x>=1,
    E(b,a)=integral_1^infinity |u(x)|^2 dx/x^2.                 (2)

The repository's residual is b=1, with a_n=mu(n) for n<Y. An additional
condition p'(1)=1 means sum a_n log(n)/n=-1. We keep those constraints
whenever comparing with the parent's normalized minima. Neither that jet
nor the Mobius prefix is needed for the uniform form theorem.

Let h_N be the smallest integer with N<=2^h_N, and define the integers

    C_N=N^2(1+2h_N),       H>=1.                              (3)

Define the second Jordan totient

    J_2(d)=d^2 product_(p|d)(1-p^(-2)),    J_2(1)=1,

and the positive quadratic expression

    V(b,a)=|b+(1/2)sum_n a_n|^2
          +(1/12)sum_(d<=N)J_2(d)|sum_(d|n, n<=N)a_n/n|^2.   (4)

Everything in (4) is rational when b,a are rational. Set

    Q_H(b,a)=sum_(j=1)^(H-1) |b-sum_n a_n floor(j/n)|^2/[j(j+1)],
    Ehat_H(b,a)=Q_H(b,a)+V(b,a)/H.                          (5)

The added term in (5) is the mean-square prediction of the ENTIRE infinite
future. It is not zero and must not be discarded.

**RC1 (complete-tail identity with an explicit error).** For every N,H,b,a
as above,

    |E(b,a)-Ehat_H(b,a)| <= C_N V(b,a)/[H(H+1)].             (6)

In particular, delta=C_N/(H+1) gives

    (1-delta) Ehat_H <= E <= (1+delta) Ehat_H.               (7)

These are uniform Hermitian quadratic-form inequalities on the balance
subspace (1), with b included as a coordinate. They require no bound on
coefficient size, no actual zeros, no PNT, and no large common period.
For delta<1 they give a multiplicative two-sided enclosure.

**RC2 (global finite-support minima, in the original norm).** Impose ANY
fixed nonempty affine real coefficient constraints compatible with (1),
b=1, and support <=N; in particular the exact Mobius prefix and either or
both finite jets used by the parent. For H>=N+1 the finite form has a unique
minimizer a_H, as does E on a nontrivial affine class. Write their minima as
hat e_H and e_N. Then, whenever delta<1,

    (1-delta)hat e_H <= e_N <= E(1,a_H)
                                  <= (1+delta)hat e_H,      (8)
    E(1,a_H)/e_N <= (1+delta)/(1-delta).                    (9)

The last ratio is used when b=1, so that the finite-support minimum is
strictly positive. There is also a stronger quadratic relative estimate:

    V <= 4 C_N E,
    |Ehat_H-E| <= eta_H E, eta_H=4 C_N^2/[H(H+1)].          (9a)

For eta_H<1 it gives

    hat e_H/(1+eta_H) <= e_N <= E(1,a_H)
                                      <=hat e_H/(1-eta_H). (9b)

Take the entirely integer horizon

    H=2 C_N ceil(sqrt(N)).                               (9c)

Then eta_H<1/N. Thus a physical horizon O(N^(5/2) log N) gives a relative
form and minimum certificate at EVERY N, uniformly over all coefficients.
The candidate performance factor is at most (1+eta_H)/(1-eta_H).
This is not a bound making the minimum small.

For the parent's e_2(Y), take N=2Y and keep BOTH p(1)=0,p'(1)=1 and all
mu(n),n<Y. Then (9c) gives eta_H<1/(2Y) in (9b). The matrix
in (5) is rational; the derivative constraint itself still contains exact
logarithms. Calling the whole jet-constrained problem rational would be
incorrect. With only rational balance/prefix constraints, the entire finite
minimization has rational data and a rational solution.

## 2. The period mean square is an exact positive divisor sum

Let Q be a common multiple of all indices 1,...,N. It is used for this proof,
not enumerated by the algorithm. Balance implies u(x+Q)=u(x), and u is
constant on every integer cell. Also, on those cells,

    u(j)=b+sum_n a_n {j/n}.

Uniformly average j over 0,...,Q-1. For m,n>=1, with g=gcd(m,n),

    mean {j/n}=(n-1)/(2n),
    Cov({j/m},{j/n})=(g^2-1)/(12mn).                      (10)

Here is a finite proof of the covariance. Write j modulo lcm(m,n) as
j=T+g k, with T uniform on 0,...,g-1. Conditional on T, k modulo m/g and
k modulo n/g are independent uniform residues, by elementary CRT since
m/g and n/g are coprime. Consequently the only covariance comes from T,
whose variance is (g^2-1)/12. Division by mn proves (10), including m=1
or n=1. No independence assumption about primes is involved.

The mean of u is b+(sum a_n)/2, because sum a_n/n=0. Its variance is

    (1/12)sum_(m,n) a_m conjugate(a_n)gcd(m,n)^2/(mn),     (11)

since the subtracted rank-one term from -1 in (10) vanishes by balance.
The identity sum_(d|k)J_2(d)=k^2 follows at prime powers and then by
multiplicativity. Inserting it into (11) gives (4). Therefore, EXACTLY,

    (1/Q)sum_(j=0)^(Q-1)|u(j)|^2=V(b,a).                 (12)

Equations (4),(10)--(12) are finite algebra and finite Fourier/CRT facts.
They are not claimed as a new general theory of gcd matrices. Their role
here is to supply the computable full-source normalization for (6).

## 3. Interval discrepancy without the giant period

The finite Fourier expansion of {j/n} uses only rational frequencies a/n
modulo one. Thus

    u(j)=sum_(theta in F_N) c_theta exp(2pi i theta j),
    sum_theta |c_theta|^2=V(b,a),                         (13)

where F_N is a subset of the reduced fractions with denominator at most N,
including zero. Equal frequencies are COMBINED. There are at most N^2
frequencies, and distinct ones have circular separation at least 1/N^2.
These statements follow by subtracting two rational fractions, including
across the endpoint of the circle. They do not require prime-log spacing.

For every integer start M and length L>=1, geometric summation gives

    |sum_(j=M)^(M+L-1) exp(2pi i(theta-phi)j)|
                  <=1/|sin(pi(theta-phi))|
                  <=1/[2||theta-phi||]                 (14)

when theta!=phi. The last inequality follows from concavity of sin on
[0,pi/2]. For a fixed theta, order the other frequencies clockwise and
counterclockwise up to distance 1/2. The kth point in either direction is
at distance at least k/N^2. Hence

    sum_(phi!=theta) 1/[2||theta-phi||]
       <=N^2 H_(|F_N|-1)
       <=N^2(1+2log N) <= C_N.                          (15)

At antipodal points either convention only enlarges the bound. A singleton
frequency set has empty off-diagonal and is handled directly. Applying
2|c_theta c_phi|<=|c_theta|^2+|c_phi|^2 symmetrically in the expanded square
proves the TWO-SIDED block estimate

    |sum_(j=M)^(M+L-1)|u(j)|^2 - L V(b,a)|
                                      <= C_N V(b,a).    (16)

This is an elementary finite-frequency mean-square estimate with a harmless
logarithmic loss. A sharper large-sieve inequality could improve its constant;
none is imported, and none is needed for (6). The full common period may be
exponential in N while every denominator in (13) is at most N. That is why
(16) has a polynomial scale.

## 4. Exact summation of the entire tail

Let w_j=1/[j(j+1)], a_j=|u(j)|^2-V, and
S_k=sum_(j=H)^k a_j. Equation (16) gives |S_k|<=C_N V for every k>=H.
Abel summation and w_j decreasing to zero yield

    |sum_(j=H)^infinity a_j w_j|
       <= C_N V sum_(j=H)^infinity(w_j-w_(j+1))
       = C_N V/[H(H+1)].                               (17)

The terminal product S_k w_k tends to zero. Each series is convergent:
u is a bounded finite periodic function, and sum w_j=1/H. Thus no
conditional rearrangement is hidden here. Since

    integral_H^infinity |u(x)|^2 dx/x^2
       =sum_(j=H)^infinity |u(j)|^2 w_j,

its leading term is V/H and (17) proves (6). Finally V/H<=Ehat_H, since
Q_H>=0, and (7) follows. This proves RC1.

Here is the improvement (9a), without a coefficient norm or an unknown
constant. Apply the lower side of (6) to the tail beginning at H0=2C_N:

    E >= V/(2C_N) - C_N V/[2C_N(2C_N+1)] > V/(4C_N)

unless V=0, when all forms vanish and the weak inequality is immediate.
Insert V<=4C_N E into (6). This proves (9a) and then (9b) by taking infima
and evaluating at the middle-form minimizer. For (9c), H(H+1)>4 C_N^2 N,
so eta_H<1/N. All these estimates hold on the same augmented coefficient
space before any affine restrictions are imposed.

The term V/H is load-bearing. For any integer H>=Y, take the actual Mobius
prefix through H-1 and balance it with a single coefficient at H. Then
u=0 throughout [1,H), so Q_H=0, while E>0. Thus minimizing a bare finite
window over supports not locked relative to H can give zero without
controlling any full norm. Equations (6)--(9) neither omit V/H nor allow
that support/horizon quantifier swap.

The lower estimate may also be used in its sharper form

    Q_H+[1/H-C_N/(H(H+1))]V <= E
                   <= Q_H+[1/H+C_N/(H(H+1))]V.           (18)

For H+1>C_N both forms are positive. Their separate constrained minima
provide another entirely finite two-sided enclosure. No coefficient norm
or inverse Gram estimate is required to pass from (18) to those minima.

## 5. Why the optimization and the infinite limit commute here

For any nonzero coefficient variation v, let n0 be its first nonzero index.
Then sum_n v_n floor(n0/n)=v_n0!=0. Thus Q_H is positive definite on every
coefficient tangent space if H>=N+1, since its first N unit cells all have
positive weights. This proves coercivity in finite dimensions, existence,
and uniqueness of the finite minimizer. The complete E has the same property.
A zero-dimensional affine class is treated as a single feasible point.

Apply (7) to EVERY feasible vector, then take the infimum. For the upper
side evaluate E at a_H; this proves (8). Strict positivity of the full
minimum follows because for every finite balanced p, a common multiple Q
has A_p(x)=0 on [Q,Q+1), so u=1 on that interval. A finite-dimensional
minimum exists, so its value cannot be zero. Equation (9) follows.

For epsilon>0, either (7) or the sharper (9a) supplies a prescribed integer
horizon. In particular choose H>=N+1 with H(H+1)>4C_N^2/epsilon.
Then (9a) has relative error epsilon, uniformly over the full affine class,
not merely over vectors with a postulated norm bound. This removes a
potential circularity: a minimizer cannot evade the certificate by using
large coefficients. This is the central distinction from checking a finite
cutoff for one well-behaved proposed sequence.

The theorem certifies support <=N only. It does NOT compare a finite N
minimum with the infimum over arbitrary supports. Allowing N to grow still
requires an upper bound on the resulting minima to obtain RH. It also does
not make the exact derivative constraint p'(1)=1 rational.

### Finite implementation

For a given rational vector, Q_H can be formed from exact divisor increments
A(j)-A(j-1)=sum_(n|j)a_n. V can be formed from (4) by divisor/multiple loops.
Only integers, rational arithmetic, floors, gcds, and J_2 are required; no
logarithm, gamma, zeta, digamma, period-weight oracle, quadrature, or zero
list enters the form. A direct matrix construction is also finite, though
not claimed near-linear or bit-optimal. Exact rational numerator sizes can
grow substantially. The theorem is a coverage/accuracy result, not a claim
that large-rank numerical solves are inexpensive.

## 6. RC3: centering the periodic residual costs arbitrarily little

This optional refinement does not change RC1 or RC2. For b=1, the constant
Fourier mode vanishes exactly when p(0)=-2. That condition is at s=0, not
the balance condition at s=1 and not the derivative at s=1.

For ANY finite balanced p with a fixed prefix below Y and any integer H>=Y,
put c=-2-p(0) and

    v_H(s)=c H^(-s)(1-2^(1-s))^2
           =c H^(-s)-4c(2H)^(-s)+4c(4H)^(-s).             (19)

Then v_H(1)=v_H'(1)=0, v_H(0)=c. Thus p+v_H is centered, has exactly the same
prefix/balance/derivative as p, and support at most max(N,4H). Its floor
response is c times

    floor(t)-4floor(t/2)+4floor(t/4), t=x/H.

This is 4-periodic with the four cell values 0,1,-2,-1, so its absolute
value is at most 2 and it vanishes for x<H. Consequently

    |sqrt(E(p+v_H))-sqrt(E(p))| <= 2|c|/sqrt(H),
    sum |(v_H)_n|^2/n = 13|c|^2/H.                        (20)

Coinciding old and new coefficients are added; the estimates remain valid.
Letting H tend to infinity proves equality of the unrestricted finite-support
infima with and without p(0)=-2, for a fixed prefix and a fixed feasible
value of p'(1), or without that derivative constraint. This is an equality
of INFIMA, not a claim of an attained infinite-support minimizer or a fixed
support-ratio comparison. It does not remove the unknown residual floor.

## 7. RC4: a bounded rational centered completion and an absolute tail bound

An actual source example makes the formula useful without selecting zeros
or doing an optimization. For every integer Y>=2 define

    M=sum_(n<Y)mu(n)/n, S=sum_(n<Y)mu(n), A=(3Y-1)/2,
    c=(-2-S)/A, b=c+M, a=-c-2M,
    q_Y(s)=Y^(-1)sum_(Y<=n<2Y)n^(1-s),
    p_Y^c(s)=sum_(n<Y)mu(n)n^(-s)+q_Y(s)[a+b 2^(1-s)].     (21)

All coefficients are rational. Since q_Y(1)=1,q_Y(0)=A,

    p_Y^c(1)=0, p_Y^c(0)=-2, and (p_Y^c)_n=mu(n) for n<Y. (22)

The two correction supports are disjoint and lie below N=4Y. The elementary
identity sum_(n<=x)mu(n)floor(x/n)=1 gives |M|<=1: at an integer cutoff,
the fractional parts for n>=2 contribute at most x-1 in absolute value.
Also |S|<=Y-1, so

    |c|<=6/5, |a|<=16/5, |b|<=11/5,
    |(p_Y^c)_n|<9,
    sum |(p_Y^c)_n|^2/n <31+log Y.                        (23)

For the last bound the exact correction cost is
(3Y-1)(a^2+2b^2)/(2Y), at most 747/25, plus H_(Y-1).
This construction is NOT asserted to satisfy p'(1)=1.

For any centered coefficients bounded by A0 and supported through N,
(4), J_2(d)<=d^2 and harmonic summation give

    V <= (A0^2/12)sum_(d<=N)H_floor(N/d)^2
      <= (5A0^2/12)N.                                    (24)

Indeed H_floor(N/d)<=1+log(N/d); the decreasing sum is bounded by the
integral from 0 to N, which equals 5N. Hence our literal vector has V<34N.
At H=N^2, the COMPLETE remaining tail obeys, using (6),

    0<=E(p_Y^c)-Q_(N^2)(p_Y^c)
      <= (V/N^2)[1+C_N/(N^2+1)]
      < 68(1+h_N)/N.                                     (25)

It therefore tends to zero at every integer Y. The finite Q in (25) is a
sum of exact nonnegative rational terms through the fixed cutoff 16Y^2.
The conclusion is an infinite-tail theorem, not a subpower bound on that
finite sum. The zero mode was deliberately paid by (22), not assumed away.

By contrast, the universal relative theorem works WITHOUT (22), for the
parent's original normalized minima as well. For large nonzero means its
V/H contribution may be large; (6) retains it exactly.

## 8. RC5: finite validation objects, interpretation, and remaining estimate

The checker independently reconstructs small CRT covariances, Jordan/gcd
quadratic forms, native Mobius prefixes, rational complete-period means,
finite interval discrepancy bounds, and finite tail comparisons. Small full
periods are enumerated ONLY as validation controls; no theorem enumerates
lcm(1,...,N) in an unbounded passage.

Three complete global-minimum enclosures are also produced for the classes
with the actual prefix below Y=2,3,4, support N=4Y, and ONLY p(1)=0. They
are not the parent's p'(1)=1 classes. For H=4096 the checker minimizes the
rational form (5) exactly, verifies stationarity by substitution, and applies
(8). Their numerical decrease is not used for an infinite conclusion.

The main deliverable is (6)--(9): uniform rational approximation of the SAME
full residual form and finite-support minima at an explicit polynomial
horizon, without a coefficient envelope or unknown analytic constant.
The next arithmetic obligation has NOT been proved: upper-bounding those
minima by Y^o(1) along an unbounded prefix sequence. In particular a relative
error tending to zero does not force an unevaluated minimum to vanish or
be subpower. It remains possible for both rational and full minima to have
the same unknown positive power exponent identified by the parent.

Classical finite Fourier analysis, CRT, Dirichlet-convolution/Jordan-totient
identities and elementary Abel summation underlie this argument. The mean-
square proof is included instead of importing a large-sieve constant. The
Nyman--Beurling context and preceding source/normalization/minimum work are
credited in SOURCES.json. No external mathematical priority claim is made.

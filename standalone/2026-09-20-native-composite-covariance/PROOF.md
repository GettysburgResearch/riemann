# NCG28: a native subquadratic budget for growing composite-frequency windows

**PROPOSED component proofs, requiring independent mathematical review.**
**The full native scale gain and RH are not proved.** Date: 20 September 2026.
Continuation of #904 at `4e8dea7004874d1a9c679b58db1dca1fbb539388`,
which preserves #848, NSR26 and RCB26. No predecessor statement is changed.

The main result is an actual upper estimate for the COMBINED, source-prescribed
composite modes, including their mutual covariance. It is subquadratic in the
previous reciprocal-Mobius energy. It is not a bound for all composite modes.

Two versions are proved:

1. For any subset of denominators `2<=q<=floor(Y^(10/11))`, its centered
   harmonic-mode energy on the ENTIRE future `k>=Y+1` is at most
   `C H_Y^4 F_Y^(4/3)`.
2. A scale-dependent composite window `q<=floor((Y^4 X^6)^(1/11))` on the
   physical dyadic block `[X,2X)` has total cost at most
   `C H_Y^5 F_Y^(4/3)`, AFTER an exact tail transform. All activation-boundary
   corrections are retained. Around `X=Y^2` this reaches order `Y^(16/11)`.

Here C is an absolute constant, explicitly specified below, not optimized.
These estimates hold for every integer Y>=2, with the actual bounded
completion. They do not assume RH, PNT, a zero table or random signs.
The remaining high-composite transformed component is not bounded here.
A cutoff in denominator is not a statement that a corresponding fraction of
RH or a corresponding fraction of the total energy has been controlled.

## 0. Source, inherited objects, and attribution

All arithmetic functions use ordinary Dirichlet convolution. Let mu be the
Mobius function, `1*mu=delta`, and set

    m(k)=sum_(n<=k) mu(n)/n,       m(x)=m(floor x),
    F_Y=sum_(k=1)^Y m(k)^2,       b=Y+1,       B=b^2-1.

F is the NIR26 reciprocal-innovation energy, NOT DSE27's physical E, the BNR26
balanced A, or a single covariance diagonal. In particular F_Y>=1.

Use the PCR26 capped completion c: retain mu(n) for n<=Y, then successively
subtract reciprocal residual using coefficients of magnitude at most 3 until
`sum c(n)/n=0`. Write L for its last support index. This construction has

    |c(n)|<=3,   L<=2Y,   sum_(k>Y) m_c(k)^2 <= F_Y,          (0.1)
    m_c(k)=sum_(n<=k)c(n)/n=0 for k>=L.

The short-source Newton identity gives, for v=2c-1*c*c,

    v(n)=mu(n) for every n<b^2.                             (0.2)

For completeness, put e=delta-1*c. Then e vanishes below b and
`mu-v=mu*e*e`. The strict endpoint is important.

DSE27 uses

    z=c*c,    U_d=sum_(d|n)c(n)/n,    B_q=sum_(q|d)z(d)/d,
    T_d(k)=(d-1)/2-(k mod d),
    R_q(k)=sum_(d|q)mu(q/d)T_d(k),                q>=2.       (0.3)

All these sums are finite, and B_q=0 for q>L^2. Its exact physical formula is

    V(k)=sum_(n<=k)v(n)=2A_c(k)+S^2/2-sum_(q>=2)B_q R_q(k),
    S=sum c(n).                                            (0.4)

The Fourier, Ramanujan, divisor and elementary separation machinery is
classical. Huxley--Watt is prior art for short-source inversion; Tao is prior
art for bounded reciprocal Mobius sums over prime subsemigroups; finite
Ramanujan/Wintner expansions and the classical additive large sieve are prior
art for the spectral representation. We prove every estimate used here,
including a non-sharp logarithmic-loss separation inequality, rather than
importing a stronger theorem whose hypotheses have not been checked.

The proposed contribution is the SOURCE-ENERGY amplitude bound, its mean
square summation, and the fixed/moving composite-window estimates with their
exact harmonic-tail composition. No external priority claim is made for this
combination pending a broader literature review.

## 1. NCG28-1: native divisor amplitudes from the previous energy

For d>=1 define

    G(d)=product_(p|d) (1-p^(-2/3))^(-1),       G(1)=1.

For the specified completed native source,

    |U_d| <= 16 (F_Y/Y)^(1/3) d^(-2/3) G(d)               (1.1)

for EVERY d>=1. For d>L the left side is zero. This is not asserted for an
arbitrary bounded, reciprocal-balanced source.

### 1.1 A cubic point bound

The native divisor identity implies

    N m(N)=1+sum_(n<=N)mu(n){N/n}.

As `{N/n}<=1-1/n`, its absolute value is at most `1+N-H_N<=N`.
Thus |m(N)|<=1, without PNT. Let a=|m(n)| for 1<=n<=Y. For
`0<=j<=floor(an/4)`,

    |m(n)-m(n-j)| <= j/(n-j+1) <= a/3.

Every relevant index is positive. There are at least an/4 such indices, so

    F_Y >= (an/4)(2a/3)^2 = n a^3/9.

Consequently

    |m(n)|^3 <= 9 F_Y/n,
    |m(x)| <= (18 F_Y/x)^(1/3),       1<=x<=Y.              (1.2)

The factor two in the real-variable version pays floor(x)>=x/2. Small n and
an<4 are included by counting the j=0 term. This is an elementary
bounded-increment energy argument, not a new pointwise Mertens estimate.

### 1.2 Exact deletion of the primes dividing d

For squarefree d, set

    m_d(x)=sum_(n<=x,(n,d)=1)mu(n)/n.

The finite coefficient identity obtained by deleting Euler factors is

    m_d(x)=sum_(h<=x, all prime factors of h divide d) m(x/h)/h.

Indeed `mu * 1_(d-smooth)` equals mu on integers coprime to d and zero
otherwise. There is no analytic continuation or infinite limiting sum in
this identity. Apply (1.2), then enlarge a nonnegative sum to the full
convergent finite-prime geometric product:

    |m_d(x)| <= (18F_Y/x)^(1/3) G(d),      x<=Y.

The native prefix contribution to U_d is exactly

    sum_(n<=Y,d|n)mu(n)/n = mu(d)m_d(Y/d)/d                 (1.3)

when d is squarefree; it is zero otherwise. Therefore its magnitude is at
most `18^(1/3)(F_Y/Y)^(1/3)d^(-2/3)G(d)`.
This is the arithmetic step: arbitrary ternary coefficients do not satisfy
(1.3) or the smooth-deletion identity in terms of THEIR previous m-energy.

### 1.3 The completion cost is not dropped

Let a=|m(Y)|. If a>0, the number J of correction coefficients obeys

    J<=ceil(Ya/(3-a))<=ceil(Ya/2).

The first inequality follows because j full corrections have reciprocal
capacity at least 3j/(Y+j). At the final correction only the required amount
is used. If a=0 the tail is empty.

The absolute contribution of these consecutive tail indices to U_d is at most

    (3/Y)(J/d+1) <= (3/2)a/d + 6/Y.                        (1.4)

For d<=L<=2Y and F_Y>=1, (1.2) makes the right side at most

    [(3/2)9^(1/3)+6*2^(2/3)] (F_Y/Y)^(1/3)d^(-2/3).

Together with the prefix contribution and G(d)>=1, this is below (1.1):
`18^(1/3)+(3/2)9^(1/3)+6*2^(2/3)<16`.
For example, the respective bounds 8/3, 63/20 and 48/5 prove this rationally.

We also recall why (0.1) pays the entire completion energy. If r_j is the
remaining reciprocal residual after j corrections, then for
`1<=j<=ceil(Y/2)`, `3/(Y+j)>=1/(Y-j+1)` and the reverse triangle inequality
gives `r_j<=|m(Y-j)|`. Sum the squares of every remaining tail cell. This
is the inherited PCR26 estimate, rederived to specify exactly what is spent.

## 2. NCG28-2: composite amplitudes, without a false sign or product rule

For ANY finite source, a useful exact formula is

    B_q=sum_(d|q) sum_(e|q/d) mu(e) U_(de) U_(q/d).         (2.1)

To prove it, partition r according to gcd(r,q)=d, and use inclusion-exclusion
for gcd(r/d,q/d)=1. In particular B_p=-U_p^2 when U_1=0, but for distinct primes

    B_(pr)=2U_p U_r-2U_(pr)(U_p+U_r)+U_(pr)^2.             (2.2)

There is no forced sign in (2.2), and B_q is NOT a multiplicative function.

For the uniform estimate, use a symmetric threshold expansion. At p^a,

    1_(i+j>=a)
      = sum_(u=0)^a 1_(i>=u)1_(j>=a-u)
        -sum_(u=1)^a 1_(i>=u)1_(j>=a+1-u).                 (2.3)

Checking the number of admissible u proves this for all nonnegative i,j.
Multiply (2.3) over p^a||q, and apply (1.1) to the resulting products U_d U_e.
Both d and e divide q, so G(d)G(e)<=G(q)^2. This proves

    |B_q| <= 256 (F_Y/Y)^(2/3) q^(-2/3) W(q),             (2.4)
    W(q)=G(q)^2 product_(p^a||q) [a+1+a p^(-2/3)].

W is a multiplicative MAJORANT, not a claimed multiplicative law for B.
The expansion includes overlapping divisibility and all prime powers.

### A logarithmic mean square for the majorant

Write t_p=p^(-2/3), and define the absolute finite constant

    h_p=(1+t_p)^2/(1-t_p)^4,
    C_0=product_p [1+4(h_p-1)/p].                         (2.5)

The product converges: h_p-1=O(p^(-2/3)). An intentionally coarse explicit
ceiling is C_0<=exp(4860). Indeed t_p<2/3, h_p-1<=810t_p, and
`sum_(n>=2)n^(-5/3)<=3/2`. This is NOT an optimized numerical constant.

For every integer Q>=1,

    sum_(q<=Q) W(q)^2 <= C_0 Q H_Q^3.                     (2.6)

Here is a proof retaining the full prime tail. We have

    W(q)^2 <= tau(q)^2 product_(p|q)h_p
             <= d_4(q) product_(p|q)h_p,

where d_4 is the ordered four-factor divisor function. The prime-power
inequality is `(a+1)^2<=binom(a+3,3)`. Expand the last product using the
nonnegative squarefree coefficients g(p)=h_p-1. Submultiplicativity of d_4
and `sum_(m<=T)d_4(m)<=T H_floor(T)^3` give

    sum_(q<=Q)W(q)^2
      <= Q H_Q^3 sum_(d squarefree) 4^omega(d)g(d)/d
       = C_0 Q H_Q^3.

Submultiplicativity follows by splitting every prime exponent of an ordered
factorization of ab between a and b. The summatory estimate follows by fixing
three factors and bounding the fourth count by T/(abc). All enlarged sums
are nonnegative and convergent where an infinite sum occurs.

## 3. NCG28-3: whole physical covariance, not period-average orthogonality

Let A be ANY subset of integers 2,...,Q and put

    P_A(k)=sum_(q in A) B_q R_q(k),
    K_A=sum_(q in A) B_q^2 J_2(q)/12,
    J_2(q)=q^2 product_(p|q)(1-p^(-2)).                    (3.1)

The subset may in particular consist of all composites in this range.
DSE27's finite Fourier formula puts R_q at the reduced frequencies a/q,
with coefficient `1/(1-exp(-2*pi*i*a/q))`.
The squared coefficient mass at denominator q is exactly J_2(q)/12.
One may prove this without evaluating trigonometric sums: T_d has period
variance `(d^2-1)/12`, its R_q pieces have disjoint reduced frequencies,
and finite divisor inversion gives the stated variance for each R_q.

Different reduced fractions with denominators <=Q have circular distance
at least Q^(-2). For N consecutive integers, finite geometric summation gives

    sum_block |P_A(k)|^2 <= [N+Q^2 H_(Q^2)] K_A.          (3.2)

For clarity, this is an elementary, non-sharp additive large-sieve bound.
In the Gram matrix, an off-diagonal entry has magnitude at most
`1/(2||alpha-beta||)`. Sort frequencies clockwise and counterclockwise from
one chosen frequency up to circular distance 1/2. The j-th point on either
side is at distance >=j/Q^2, so the entire off-diagonal row sum is at most
Q^2 H_(Q^2). The Schur row bound, or `2|xy|<=|x|^2+|y|^2`, proves (3.2).
It applies to arbitrary coefficients and does NOT assume that finite blocks
are full periods or that quadratic samples are orthogonal.

Sum (3.2) on blocks `[2^j b,2^(j+1)b)`, bounding the physical weight by
`(2^j b)^(-2)`. This proves the complete infinite-tail estimate

    sum_(k>=b) P_A(k)^2/[k(k+1)]
       <= [2/b+4Q^2 H_(Q^2)/(3b^2)] K_A.                 (3.3)

All within-A cross terms remain on the LEFT. They have been upper-bounded,
not omitted, assigned a negative sign, or replaced by a period average.

Combining (2.4),(2.6) with J_2(q)<=q^2 gives

    K_A <= (16^4 C_0/12)(F_Y/Y)^(4/3) Q^(5/3) H_Q^3.     (3.4)

Equations (3.3)-(3.4) are a two-parameter, source-dependent bound for every Q.

## 4. NCG28-4: a lossless tail map into the RIGHT Newton energy

A physical estimate alone must not be silently reassigned to F. Here is the
exact adapter. For any real sequence P with `sum_(j>=b)P(j)^2/[j(j+1)]<infinity`,
put

    (TP)(k)=P(k)/(k+1)-sum_(j>k)P(j)/[j(j+1)],  k>=b.

The sum converges absolutely by weighted Cauchy--Schwarz. Then

    sum_(k>=b)(TP)(k)^2
      =sum_(j>=b)P(j)^2/[j(j+1)]
         -b [sum_(j>=b)P(j)/[j(j+1)]]^2.                 (4.1)

In particular T is a contraction. This is elementary Hilbert-space algebra,
closely related to NIR26's innovation isometry, not a new general Hardy theory.

For a finitely supported P, expand the squares. A diagonal P(j)^2 coefficient
is `1/[j(j+1)]-b/[j^2(j+1)^2]`; an off-diagonal coefficient for i<j is
`-2b/[i(i+1)j(j+1)]`. This proves (4.1). Truncate P in the weighted space.
The finite identity makes T bounded; its pointwise formula and the identity
pass to the limit by weighted Cauchy--Schwarz. Thus no finite-period assumption
or unproved infinite interchange is involved.

### Centered Ramanujan harmonic modes

Let

    c_q(n)=sum_(d|gcd(q,n)) d mu(q/d),
    H_q^R(k)=sum_(n<=k)c_q(n)/n
            =sum_(d|q)mu(q/d) H_floor(k/d),
    Z_q(k)=H_q^R(k)+Lambda(q),                            (4.2)

where Lambda is von Mangoldt. Harmonic-number asymptotics show
`H_q^R(k)->-Lambda(q)` for each fixed q. Indeed the log(k)+gamma terms
cancel and `sum_(d|q)mu(q/d)log d=Lambda(q)`.

Since `sum_(n<=k)c_q(n)=R_q(k)-phi(q)/2`, summation by parts yields EXACTLY

    Z_q(k)=(T R_q)(k).                                   (4.3)

The constant phi(q)/2 cancels between the boundary value and the complete tail.
For q with at least two distinct prime factors, Lambda(q)=0. For prime powers
it is generally nonzero and MUST NOT be discarded.

For the completed Newton source the formal logarithmic constants cancel:

    sum_(q>=2) B_q Lambda(q)
       =sum_d z(d)log d/d
       =2[sum c(n)/n][sum c(n)log n/n]=0.                 (4.4)

Each prime-log coefficient cancels separately: `sum_(a>=1)B_(p^a)=0`.
Consequently the actual reciprocal Newton output is

    m_v(k)=2m_c(k)-sum_(q>=2) B_q Z_q(k).                 (4.5)

On k<=B it equals m(k). Formula (4.5) retains all centering constants and
all product denominators, including q>B. Neither a prime nor composite
partial sum is asserted to have zero centering constant on its own.

### Fixed-window native subquadratic bound

Take `Q=floor(Y^(10/11))`. From (3.3)-(3.4), b>=Y and H_(Q^2)<=2H_Q,

    sum_(k>=b) |sum_(q in A) B_q Z_q(k)|^2
        <= 2^15 C_0 H_Y^4 F_Y^(4/3),                    (4.6)

for EVERY subset A of {2,...,Q}. For Q<2 the sum is empty.
To check the exponents before rounding, the two powers in (3.3) are

    F_Y^(4/3) Q^(5/3)/Y^(7/3),
    F_Y^(4/3) Q^(11/3)/Y^(10/3).

At this Q the first is at most F_Y^(4/3)Y^(-9/11), and the second is at
most F_Y^(4/3). The displayed constant is conservative.

This is a 4/3-power NATIVE budget for the full combined centered sector,
including its covariance and entire future. It is not a 4/3-power bound
for F_B itself. The estimate uses the native identities in Section 1; it
is not an assertion for the NSR26 fake-source class.

## 5. NCG28-5: move the composite cutoff with physical scale

The fixed cutoff leaves avoidable high denominators at later physical times.
A larger controlled region follows, but only if its nonlocal tail correction
is retained.

Let X_j=b 2^j, j>=0, and set exactly

    Q_j=min(L^2, floor((Y^4 X_j^6)^(1/11))).              (5.1)

The floor is the integer eleventh root; no floating rounding defines the
window. On X_j<=k<X_(j+1), define

    P_low(k)=sum_(2<=q<=Q_j, q composite) B_q R_q(k).

Only composites are included here; the entire prime sector is handled in
Section 6. Q_j is a prescribed monotone schedule depending on Y and L, not a
cutoff chosen after seeing a zero, a favorable value or an optimized sign.

Let j_0 be the first j with Q_j=L^2. It is finite; X>=16Y^3 suffices, since
L<=2Y. In particular

    j_0<=ceil(log_2(16Y^3/b))<=5+2log_2 Y.                (5.2)

The strict finite inequalities in this bound are harmless overestimates.
Before saturation, (3.2)-(3.4), applied to ONE whole block, give

    weighted block energy <= 3 C_A F_Y^(4/3) H_(L^2)^4,
    C_A=16^4 C_0/12.                                    (5.3)

Indeed the off-diagonal term is controlled by `Q_j^(11/3)<=Y^(4/3)X_j^2`.
The other factor is at most `Y^(-8/11)X_j^(-1/11)<=1`, and
H_(L^4)<=2H_(L^2). After saturation the entire remaining tail is bounded
by (3.3) with Q=L^2 and b replaced by X_(j_0); it is at most
`(14/3)C_A F_Y^(4/3)H_(L^2)^4` by the same threshold inequality.
Therefore

    ||P_low||_(physical,k>=b)^2
       <= C_A(3j_0+14/3) H_(L^2)^4 F_Y^(4/3)
       << H_Y^5 F_Y^(4/3).                              (5.4)

Every physical block and the complete final tail are included. Set
`W_low=T P_low`. The exact contraction (4.1) gives the SAME bound for
`sum_(k>=b)W_low(k)^2`.

Near the beginning of the native annulus Q is of order Y^(10/11); near
its end it is of order Y^(16/11). This is a larger proved sector, not a
claim that all frequencies or all covariance are controlled. The estimate
has extra logarithmic cost for the dyadic blocks.

### The activation correction: a mandatory distinction

Let K_q be the first X_j at which q<=Q_j. For k in a given block,

    W_low(k)
      = sum_(composite q<=Q_j) B_q Z_q(k)
         -sum_(composite q>Q_j) B_q A_q(K_q),             (5.5)
    A_q(K)=sum_(n>=K) R_q(n)/[n(n+1)]
          =R_q(K-1)/K-Z_q(K-1).                         (5.6)

All q sums stop at L^2. Formula (5.5) follows by putting the monotone
activation indicator INSIDE T. The second term is the complete contribution
of future activations. It is generally nonzero and can have either sign.
The equality (5.6) gives exact finite harmonic/logarithmic access to that tail.

In particular the tempting formula
`W_low(k)=sum_(q<=Q(k))B_q Z_q(k)` is FALSE. Multiplication by a moving cutoff
does not commute with T. No arbitrary future mu coefficient is used in
(5.5): every B_q comes from c, and every K_q and R_q is explicit.

The checker retains a control that rejects deletion of this term. The exact
finite algebra and directed computations are evidence for their declared
finite instances; the infinite estimate is the written argument above.

## 6. Composition with the actual Newton update and the remaining problem

Let

    P_prime(k)=sum_(p prime) B_p R_p(k),
    P_high(k)=sum_(q composite, q>Q_j) B_q R_q(k)
                          on X_j<=k<X_(j+1),
    W_prime=T P_prime,     W_high=T P_high.

These identities partition the full finite Fourier function pointwise on
EVERY k>=b. In particular P_high is zero after X_(j_0), but its transformed
value on earlier k contains the entire explicitly defined future tail.

DSE27's elementary prime bound, also on the entire future, is

    ||W_prime||_2^2 <= ||P_prime||_physical^2
                   <= 81 H_L^6/(4b).                    (6.1)

Use |U_p|<=3H_L/p, B_p=-U_p^2 and |R_p|<p/2; then sum physical weights
from b to infinity, which equal 1/b. Thus (6.1) is a legitimate harmonic
adapter of that earlier sector estimate.

For every k in the ENTIRE native annulus b<=k<=B,

    m(k)=2m_c(k)-W_prime(k)-W_low(k)-W_high(k).             (6.2)

The full norm identity includes all six pairwise mixed terms. A valid
upper bound, without presuming their signs, is

    F_B <= F_Y+16F_Y+4||W_prime||_2^2
                       +4||W_low||_2^2
                       +4||W_high||_(b<=k<=B)^2.          (6.3)

Here 4||2m_c||^2<=16F_Y uses the paid completion bound (0.1), and
`||a+b+c+d||^2<=4 sum||a||^2`. Formula (6.3) is not claimed sharp.
All controlled terms are at most `C H_Y^6 (1+F_Y)^(4/3)`.

One sufficient remaining theorem would be, for some fixed delta>0 and K,

    ||W_high||_(b<=k<=B)^2
         <= C (1+log Y)^K (1+F_Y)^(2-delta)              (6.4)

on all sufficiently late square-ladder stages. Combine with (6.3), taking
max(4/3,2-delta)<2, and the existing scalar iteration yields F_X=X^o(1).
Since E_X<=F_X, dyadic Cauchy--Schwarz then makes
`integral_1^infinity M(x)x^(-s-1) dx` holomorphic for Re(s)>1/2; for Re(s)>1
it equals `1/(s zeta(s))`. The identity theorem and functional equation give
RH. This is the inherited conditional consumer, not a newly proved ending.

**No bound (6.4) is supplied here.** Its target is the RESTRICTED transformed
high-composite function, not an unproved requirement that the entire raw
Newton future have small physical norm. Those would be different demands.

In particular, setting Q=L^2 in the fixed bound leaves a positive power of Y.
It cannot be justified by iterating the low-window theorem. Increasing the
number of bounded sectors while ignoring the accumulation of their costs is
not a completion argument. The gain exponent and cutoff exponent are linked:
the cubic point bound and the elementary separation loss give exactly the
two powers displayed after (4.6).

## 7. Finite validation and limits

The accompanying checker tests exact divisor/tensor identities, all logarithmic
centering balances, the tail-map identity and activation commutator, the native
cubic point bounds, and finite Ramanujan covariance calculations. The native
panels reconstruct the complete short-source Newton coefficients and compare
with a separately generated Mobius prefix. Integer/rational outward enclosures
are used for logarithms, harmonic sums and reported energies.

Finite full-annulus low/high decompositions retain all mixed terms. Their
large high component, where observed, is not suppressed. Both the nonzero
activation correction and positive native low/high covariance are controls
against false simplifications; neither is a theorem about the eventual sign.

Code checks do not independently validate Sections 1--6 at unbounded scale.
No RH proof, improved zero-free region, independent review, complete parent
campaign replay, whole-repository validation, Lean result, or external novelty
priority is claimed. SOURCES.md records the limited literature and repository
reading. VALIDATION.md records precisely the runs that were completed.

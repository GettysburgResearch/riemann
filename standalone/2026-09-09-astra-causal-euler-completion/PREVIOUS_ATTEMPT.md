# NRT26: a direct native-source attempt and a quantitative repair obstruction

Date: 2026-09-09. Author: Astra.
Status: PROPOSED component proofs; independent mathematical review required.
**No complete RH proof, native subpower upper bound, or new zero-free region is obtained.**

This is an attempted proof of the full problem through the actual Mobius prefix,
not a substitution of a divisor graph for the arithmetic source. The complete
conditional ending is stated first. The positive sieve calculation is then
proved on that exact prefix. The proposed transfer is NOT proved. A separate
all-height theorem shows that repairing a complete Euler product with too few
late multiplicative terms cannot supply the missing estimate.

## 1. The full source and the complete conditional ending

For finite real coefficients a_n put

    P_a(s) = sum_n a_n n^(-s),
    A_a(x) = sum_(n<=x) a_n,
    J(a) = integral_1^infinity |A_a(x)|^2 dx/x^2.

All coefficients and every part of the physical future are retained. The
source h_a(t)=exp(-t/2) A_a(exp t), t>=0, lies in L2, and finite summation gives

    J(a) = sum_(m,n) a_m a_n/max(m,n)
         = (1/(2pi)) integral_R |P_a(1/2+it)|^2/(1/4+t^2) dt.       (1)

For the last equality, the Laplace transform of h_a at z is P_a(s)/s,
s=z+1/2, initially Re z>0 and then on the boundary by Plancherel. Each finite
source is a sum of shifted exponential functions, so this use is legitimate
without a zero-free assumption. In particular, no frequency cutoff is present.
For the native choice a_n=mu(n) for n<=N and zero otherwise,

    J_N = sum_(k<N) M(k)^2/[k(k+1)] + M(N)^2/N.                    (2)

The last term is the entire future after N, not an optional error term.

Here is the full implication which the attempted estimate was meant to finish.
It is the source-preserving consumer in PR829, reconstructed rather than claimed
as a new criterion. Suppose a^(Y) is any finite real sequence with

    a_n^(Y)=mu(n) for every integer 1<=n<=Y,
    log(1+J(a^(Y)))/log(Y+1) -> 0                                (3)

along one unbounded sequence of integer Y. Then RH follows. The supports may
be much larger than Y. The exponent in (3) is measured against the PRESERVED
PREFIX, not against the largest nonzero coefficient index.

For completeness, set

    d(t)=exp(-t/2)[floor(exp t)(1-t)+log(floor(exp t)!)],
    h_*(t)=exp(-t/2)(t-t^2/2), t>=0.

Writing x=exp t and m=floor x, integration of log u gives
0<m(1-log x)+log(m!)<=1+log x. Indeed its minimum on [m,m+1) is at
m+1, and log(m!)>=m log m-m+1 makes that minimum greater than
1-m log(1+1/m)>0. Its maximum is at m, and
log(m!)<=m log m-m+1+log m gives the upper bound. Thus ||d||_1<=6.
Its exact Laplace transform is

    D(z)=(s-1)zeta(s)/s^2,   s=z+1/2.                           (4)

This follows initially in Re s>1 by integrating the floor series and the
log-factorial sum; the pole at s=1 is removable and analytic continuation
identifies the same causal L1 function for Re z>0. Put y_a=d*h_a. Then

    ||y_a||_2 <= 6 sqrt(J(a)),
    L y_a(z)=(s-1)zeta(s)P_a(s)/s^3.                           (5)

Before log(Y+1), finite Mobius inversion makes y_a equal h_* whenever the
prefix in (3) is preserved. Explicitly, expanding d and integrating the finite causal sum gives

    y_a(t)=exp(-t/2) sum_(m<=exp t) (sum_(n|m)a_n)
                 * [(t-log m)-(t-log m)^2/2].

For t<log(Y+1), every m in this sum is at most Y, so its divisor coefficient
is 1_(m=1). This proves exact agreement, including the constant and linear
terms, without an unproved source adapter. Also ||h_*||_2=sqrt(2), and
L h_*(z)=(s-1)/s^3.

If rho=beta+i gamma were a nontrivial zero with alpha=beta-1/2>0, (5) at
z=rho-1/2 vanishes, whereas L h_*=(rho-1)/rho^3 !=0. The error y_a-h_*
is supported after log(Y+1). Cauchy--Schwarz on that ENTIRE delayed support gives

    6 sqrt(J(a)) + sqrt(2)
       >= sqrt(2alpha) |rho-1|/|rho|^3 * (Y+1)^alpha.             (6)

Condition (3) contradicts (6). Reflection by the zeta functional equation
then excludes left-of-line zeros as well. No simplicity assumption or numerical
zero table is used. THE UPPER BOUND (3) IS NOT PROVED IN THIS PACKET.

## 2. What positive divisor squares actually give

For finite a supported in [1,N], define a DIFFERENT positive form

    S(a)=sum_(m,n<=N) a_m a_n/[m,n]
        =sum_(d<=N) phi(d) |sum_(d|n<=N) a_n/n|^2,              (7)

where [m,n] is the least common multiple. The identity is the classical Selberg
sieve diagonalization, using gcd(m,n)=sum_(d|m,d|n)phi(d). It is not a change
of notation for (1): J has max(m,n), not [m,n]. Let H_N=sum_(n<=N)1/n.

For the actual native coefficients, the following elementary bounds suffice:

    1/(3H_N) < S(mu 1_[1,N]) < 12H_N.                          (8)

The non-strict versions would also suffice. This is not asserted sharp or new.
The classical sieve literature has stronger estimates in related normalizations;
none of those stronger asymptotics is used here.

Proof of the upper bound. Put m(x)=sum_(n<=x)mu(n)/n. The exact identity
sum_(n<=x)mu(n)floor(x/n)=1 yields |m(x)|<=2 for x>=1. For squarefree d,

    sum_(d|n<=N)mu(n)/n = mu(d)/d * m_d(N/d),
    m_d(X)=sum_(k<=X,(k,d)=1)mu(k)/k.

The coefficient identity obtained by removing primes dividing d gives

    m_d(X)=sum_(r<=X, p|r implies p|d) m(X/r)/r.

It is a finite Dirichlet convolution identity, not a limit of random primes.
Consequently |m_d(X)|<=2 product_(p|d)(1-1/p)^(-1)=2d/phi(d), and (7) gives
S_N<=4 sum_(d<=N)mu(d)^2/phi(d).

For every n, n/phi(n)=sum_(d|n)mu(d)^2/phi(d). Hence

    sum_(n<=N)1/phi(n)
      <= H_N product_p (1+1/[p(p-1)]) < 3H_N.                  (9)

The product is bounded by exp(sum_(n>=2)1/[n(n-1)])=e<3. This proves the upper
bound without PNT, RH, or an estimate of the Mertens function.

For the lower bound, put y_d=sum_(d|n<=N)a_n/n. For any a_1=1,
1=sum_(d<=N)mu(d)y_d. Cauchy--Schwarz in (7), followed by (9), gives
1<=S(a) sum mu(d)^2/phi(d)<3H_NS(a). Apply this to the native sequence.

The proposed closing move would be a NATIVE estimate

    J_N <= N^(o(1)) S_N                                       (10)

along an unbounded sequence. By (8), this would imply (3). But (8) contains no
such comparison. Already N=3 gives J_3=5/6 and S_3=1/2. Positivity of (7)
alone cannot control the signed physical cross terms in (1).

Equation (10) remains UNPROVED; relabeling it a transfer lemma does not make it
a smaller or easier problem. Section 5 rules out one broad way to obtain it
from complete finite-prime products and a small number of late repairs.

## 3. A quantitative annihilator lemma, allowing arbitrary coefficients

Let I=[pi-epsilon,pi+epsilon], 0<epsilon<pi/2. Let

    f(tau)=1+sum_(j=1)^r c_j exp(-i lambda_j tau),
    1<=lambda_j<=A,  A>=1, r>=1.                             (11)

Repeated frequencies can first be combined; they need not be separated for
the argument. Coefficients c_j are arbitrary complex numbers. Define

    L_r = sqrt(epsilon/2)/(r+1)
            * [1/(2(A+2r/epsilon))]^r.

Then

    ||f||_(L2(I)) >= L_r.                                    (12)

In particular no coefficient tuning can drive this norm to zero at fixed r,A.
This is a local continuous-band lower bound, not a claim about a point value.

Proof. Take the compactly supported polynomial bump
psi(tau)=(1-((tau-pi)/epsilon)^2)^r on I, and zero elsewhere. Derivatives
through order r-1 vanish at the endpoints, so integration by parts r times
has no boundary term. Its r-th weak derivative is square integrable. On
|v|<=1/(r+1), (1-v^2)^r>=1-r/(r+1)^2>=1/2, giving

    integral_I psi >= epsilon/(r+1).

For 0<=k<=r, expansion of (1-v^2)^r and a termwise derivative bound give

    ||psi^(k)||_2 <= sqrt(2epsilon) 2^r (2r/epsilon)^k.

Let D=d/dtau and apply A_r=product_(j=1)^r(D+i lambda_j). All nonconstant
exponential terms are annihilated; A_r f=i^r product_j lambda_j. Integrating
against psi, moving derivatives onto psi, and applying Cauchy--Schwarz yields

    product_j lambda_j * epsilon/(r+1)
       <= ||f||_2 sqrt(2epsilon) 2^r (A+2r/epsilon)^r.

Since every lambda_j>=1, this is (12). The r=0 case is simply f=1 and
||f||_2=sqrt(2epsilon). This proof is independent of prime distribution.

## 4. The complete Euler source and its uniform low-frequency pressure

Put

    M_Y(s)=product_(p<=Y)(1-p^(-s)),  a(Y)=sqrt(Y)/log Y.

The unconditional prime number theorem gives, by partial summation,

    sum_(p<=Y)p^(-1/2)=(2+o(1))a(Y).                         (13)

The following uniform calculation is the mechanism in PR833, Section 3.1,
which is explicitly credited. No novelty is claimed for this pressure law.
For every fixed compact real tau interval,

    log|M_Y(1/2+i tau/log Y)|/a(Y) -> -2 cos(tau)             (14)

uniformly in tau. To verify the uniformity, the weighted prime mass below
Y^(1-delta) is o(a(Y)); above that point log p/log Y is uniformly within
delta of 1. Thus sum p^(-1/2) exp(-i tau log p/log Y) equals
(2+o(1))a(Y)exp(-i tau) uniformly. The sum of the k>=2 terms of
log(1-p^(-s)) is O(sum_(p<=Y)1/p)=O(log Y)=o(a(Y)). This proves (14).
There is no assumption of independent prime phases.

In particular on I as in Section 3,

    |M_Y(1/2+i tau/log Y)|
          >= exp[(2 cos(epsilon)+o(1))a(Y)]                 (15)

uniformly. The error depends on epsilon, not on a correction polynomial.

## 5. NRT26: a necessary complexity for late multiplicative repairs

Consider the complete finite-prime construction

    P_Y(s)=M_Y(s) B_Y(s),
    B_Y(s)=1+sum_(j=1)^(r_Y) b_(j,Y) d_(j,Y)^(-s),
    Y<d_(j,Y)<=Y^A,                                       (16)

with A>1 fixed. The d_j are distinct ordinary integer delays after combining
coincident terms; zero coefficients may be dropped. All b_j are real (the norm
bound also holds for complex coefficients). There is NO bound on b_j in the
lower-bound theorem. Every squarefree divisor of the primorial is retained.

The sequence of coefficients of (16) agrees with mu(n) for every n<=Y.
Thus these are legitimate candidates for the complete RH implication (3),
not models lacking the arithmetic prefix. Their largest support can be
primorial-sized; it is not called O(Y).

**NRT26.A.** For every fixed epsilon in (0,pi/2), uniformly over ALL choices
in (16), with r=r_Y>=1,

    log J(P_Y)
       >= [4 cos(epsilon)+o(1)] a(Y)
          - 2r log(2(A+2r/epsilon))
          - 2 log(r+1) - log log Y + O_epsilon(1).          (17)

Here J(P_Y) means (1) for the complete coefficients of P_Y. The o(1) is uniform
in the correction coefficients and count. To prove (17), restrict the full
integral (1) to t=tau/log Y, tau in I. Its denominator is bounded above by
1/4+(3pi/(2log Y))^2. On that band B_Y is exactly (11), with
lambda_j=log d_j/log Y in (1,A] and c_j=b_j/sqrt(d_j). Apply (12),(15),
including the Jacobian 1/log Y. This proves (17).

For r=0 the same conclusion holds with no r terms by direct integration of
(15). The lower bound is a full-norm statement obtained from an entire band;
point evaluation has not been substituted for an L2 estimate.

**NRT26.B.** If a sequence of candidates (16) has even the weaker property
J(P_Y)<=Y^C for ONE fixed C, then along that sequence

    liminf r_Y (log Y)^2/sqrt(Y) >= 4.                     (18)

In particular subpower native energy requires (18). A fixed number of repairs,
or r_Y=o(sqrt(Y)/(log Y)^2), cannot work regardless of coefficient tuning.

Proof. On a subsequence with r_Y(log Y)^2/sqrt(Y) bounded, one has
r_Y=O(sqrt(Y)/(log Y)^2), so
log(2(A+2r_Y/epsilon)) <= (1/2)log Y+o(log Y).
The two smaller logarithmic terms in (17) are o(a(Y)), while log J=O(log Y)
is also o(a(Y)). Thus (17) forces
r_Y(log Y)^2/sqrt(Y) >=4 cos(epsilon)-o(1).
Let epsilon decrease to zero. A subsequence with unbounded displayed ratio
cannot lower its liminf, proving (18). Bounded r is automatically excluded
by (17).

**NRT26.C.** For fixed r,A and sum_j |b_(j,Y)|/sqrt(d_(j,Y))<=Y^C with fixed C,

    log J(P_Y) ~ 4 sqrt(Y)/log Y.                          (19)

The lower bound follows from (17), then epsilon down to zero. For the upper
bound, sup_t|P_Y(1/2+it)|<=exp(sum p^(-1/2))(1+Y^C), and
(1/(2pi)) integral_R dt/(1/4+t^2)=1. Equation (13) proves the matching upper
bound. This generalizes the coefficient noncancellation part of the specified
construction in PR833 to every fixed finite late multiplicative repair. The
underlying Euler pressure is inherited and credited, not rediscovered.

Fixed safe-point jets can be imposed within (16), for example
B_Y(s)=(1-Q^(1-s))^r, Q=Y+1, gives a zero of order r at s=1 and keeps every
coefficient through Y. The theorem still applies at any fixed r; those jets
do not repair the critical norm. This example is not required for (17).

### Relation to a positive multiplicative square

For the UNREPAIRED full Euler coefficients a_d=mu(d)1_(d|product_(p<=Y)p),
independence here means an exact FINITE product expansion and gives

    S(a)=product_(p<=Y)(1-1/p)<=1,                        (20)
    log J(a)~4 sqrt(Y)/log Y.

At a prime the four contributions to S are 1,-1/p,-1/p,+1/p. Their product
proves (20) without any asymptotic or probabilistic hypothesis. Thus a very
small positive divisor-square norm, an exact native prefix, and complete
finite Euler multiplicativity do NOT imply a subpower physical norm in that
prefix length. For a support bound measured against the primorial, this is
NOT the same assertion: log(product_(p<=Y)p)~Y by PNT, and (19) is subpower
in the primorial. Neither (20) nor (17) refutes the actual-interval estimate (10).

## 6. Outcome of the full attempt

The attempted chain was:

    literal Mobius prefix -> positive sieve-square bound
    -> controlled complete physical energy -> no off-line zero -> RH.

The first step is proved in Section 2; the last implication is reconstructed
in Section 1. The central NATIVE bound (10), or some successful source-preserving
completion satisfying (3), is NOT established. Section 5 shows why a natural
complete-Euler implementation cannot be repaired with too few late terms.
This is not a proof that the near-square-root compressed affine minimum in
PR803 is large: its coefficients, support and budget form a different class.
The numerical similarity of the scales does not identify those two spaces.

The exact source upper bound remains an RH-strength problem, not a task for a
reviewer to fill in. No claim is made that all multiplicative corrections fail:
(18) is necessary, not sufficient, and growing correction counts or longer
relative delay supports are outside the fixed-parameter conclusion.

# TC26: the native polynomial trace has a logarithmic diagonal

**Status: PROPOSED component proofs; independent mathematical review required.**
RH and the upper bound on the native covariance remain OPEN. This continuation
of PR866 does not promote its proposed results or modify earlier sources.

The target is the SAME odd-Mobius trace as DG26, not the all-integer Newton
collision diagonal in PR848/875/869. The latter is of order log^4; the direct
trace diagonal constructed here has order log with an explicit leading constant.
The difference is in the mathematical objects, not a contradiction.

## 0. Source, classical inputs, and purpose

Let mu be ordinary Mobius, and m(x)=sum_{n<=x, odd} mu(n)/n, zero below one.
Use the established classical facts |m(x)|<=1 and m(x)->0. The latter uses PNT,
NOT RH. Tao's prime-subsemigroup theorem includes precisely this odd source.
The new diagonal result below does not need PNT; it uses elementary squarefree
counting. The limiting signed expansion uses the stated m(x)->0 input.

For j>=0 put l=2j+1 and phi_j(u)=sqrt(2l+1) P_l(u), where P_l is the standard
Legendre polynomial with P_l(1)=1. These form an orthonormal basis on (0,1).
Retain the DG26 operator on odd polynomials:

    Kf(t)=integral_0^1 m(t/u) f(u)du/u,       1<t<3,
    S_N=sum_{j=0}^{N-1} ||K phi_j||_{L2(1,3)}^2.

All inner products used below are real or Hermitian, not complex bilinear.
Define the integrated columns

    psi_j(x)=integral_x^1 phi_j(u)du/u,       0<=x<=1,
    psi_j(x)=0,                             x>=1,
    b_j=psi_j(0).

At zero psi is well-defined because phi_j is odd. On [0,1] it is a constant
minus an odd polynomial. The extension by zero matters for the n=1 source;
all explicit sums below start at odd n>=3. Endpoint conventions on single
points do not change any Lebesgue integral.

We attack S_(2N)-S_N by retaining all source cross terms. The positive diagonal
can be determined asymptotically. The remaining covariance cannot be replaced
by its termwise positive part: both sign parts diverge at every fixed N.

## 1. TC26-1: exact primitive energy and concentration

For every j>=0,

    integral_0^1 psi_j(x)^2 dx = 1/(j+1).                 (1)

For 0<delta<=1,

    integral_delta^1 psi_j(x)^2 dx
         <= 9/[2 delta^2 (j+1)^2].                     (2)

These are all-degree statements, not extrapolations from the checker.

### Exact calculation

Write l=2j+1, A_j(x)=integral_0^x phi_j(u)du/u, and
J_l=integral_0^1 P_l(u)du. The classical three-term recurrence and orthogonality
of even nonconstant Legendre polynomials to one give

    I_(2j+1):=integral_0^1 P_(2j+1)(u)du/u
       =(-1)^j 4^j(j!)^2/(2j+1)!,
    J_(2j+1)=(-1)^j (2j)!/[2^(2j+1)j!(j+1)!].          (3)

For the first formula, I_1=1 and I_(2j+1)=-(2j)/(2j+1) I_(2j-1).
For the second, integrate (2l+1)P_l=(P_(l+1)-P_(l-1))' and use
P_(2j)(0)=(-1)^j binom(2j,j)/4^j. Thus

    b_j integral_0^1 phi_j=(2l+1)/[l(l+1)].

The odd polynomial A_j has leading coefficient 1/l times that of phi_j,
so orthogonality gives integral A_j phi_j=1/l. Since psi_j=b_j-A_j and
(x psi_j^2)'=psi_j^2-2psi_j phi_j, both boundary terms vanish and

    ||psi_j||^2=2[(2l+1)/(l(l+1))-1/l]=2/(l+1).

This is (1). In particular b_j is nonzero for every j.

### Concentration near zero

Let F_j(x)=integral_x^1 phi_j(u)du. The antiderivative identity and even
Legendre orthogonality on (0,1) give exactly

    F_j=(P_(l-1)-P_(l+1))/sqrt(2l+1),
    ||F_j||^2=2/[(2l-1)(2l+3)].                        (4)

Integration by parts gives

    psi_j(x)=F_j(x)/x-integral_x^1 F_j(u)du/u^2.

The Hardy adjoint H*g(x)=integral_x^1 g(u)du/u has L2 norm at most two.
For completeness, integrate (x(H*g)^2)' and apply Cauchy--Schwarz; truncation
extends the inequality from smooth functions to L2. For complex g use the
real part of the polarized identity. Apply it to (F_j/u)1_[delta,1]. On the
restricted interval the last display has norm at most 3||F_j||/delta.
Use (4) and (4j+1)(4j+5)>=4(j+1)^2 to obtain (2).

Equations (1)-(2) imply a useful explicit weighted remainder:

    integral_0^1 sqrt(x) psi_j(x)^2 dx
          <= (11/2)(j+1)^(-6/5).                       (5)

Indeed split at delta=(j+1)^(-2/5), bound the first part by sqrt(delta)/(j+1),
and use (2) for the second. No oscillatory asymptotic formula is required.

## 2. TC26-2: the complete native diagonal and its leading constant

Put

    d_j=sum_{n>=3, odd} mu(n)^2/n^2
                   integral_1^3 psi_j(t/n)^2 dt,
    D_N=sum_{j<N}d_j,
    alpha=4/pi^2,      c0=alpha log 3.

All these diagonal series converge absolutely. Then, for EVERY j>=0,

    |d_j-c0/(j+1)| <= 33(j+1)^(-6/5).                  (6)

Consequently there is a finite real constant C_* such that

    D_N=c0 H_N+C_*+O(N^(-1/5)),                         (7)

where H_N=sum_{k=1}^N 1/k. Explicitly the absolute tail error in (7) is at most
165 N^(-1/5), and |C_*|<=198 is a conservative bound. Also

    |D_(2N)-D_N-c0(H_(2N)-H_N)| <=33 N^(-1/5).          (8)

Thus the diagonal block increment tends to (4 log3/pi^2)log2. The constants
33,165,198 are not sharp. The constant C_* also has the exact safe-value
expression (13) below; it is not numerically certified in this packet.
This determines the diagonal, NOT the trace S_N or its covariance.

### Proof using the actual squarefree source

Let A_o(X)=sum_{n<=X, odd}mu(n)^2. The identity
mu(n)^2=sum_{d^2|n}mu(d), with both d and n/d^2 odd, gives

    |A_o(X)-alpha X| <=2sqrt(X),             X>=1.      (9)

Here the coefficient alpha is (1/2)sum_{d odd}mu(d)/d^2=4/pi^2, by the
absolutely convergent Euler product. To check the explicit error, put y=sqrt X.
The odd counting error is at most (y+1)/4. The omitted d-tail is at most
(X/2)(1/y+1/y^2)=y/2+1/2. Their sum is at most 2y. We used
sum_{n>y}n^-2<=y^-1+y^-2; its proof is the first term plus the following
integral. No prime-distribution error estimate enters (9).

Changing t=nx in d_j and applying nonnegative summation gives

    d_j=integral_0^1 psi_j(x)^2 omega(x) dx,
    omega(x)=sum_{1/x<n<=3/x, n odd}mu(n)^2/n           (10)

almost everywhere. For x in (0,1], all contributing n are at least three.
Partial summation of (9) yields, with y=1/x,

    |omega(x)-alpha log3| <=(6-2/sqrt3)sqrt(x)<6sqrt(x). (11)

Indeed the two endpoint errors contribute 2(y^-1/2+(3y)^-1/2) and the
integral error contributes 4(y^-1/2-(3y)^-1/2).
Combine (1), (5), (10)-(11) to obtain (6). Summing the absolutely convergent
errors proves (7)-(8). The bound |C_*|<=198 follows from
sum_{k>=1}k^(-6/5)<=1+integral_1^infinity t^(-6/5)dt=6.

### Safe-value formula for exact computation

If P_l has coefficients a_r and
psi_j(x)=sqrt(2l+1) [c-sum_{r odd}a_r x^r/r],
let q_k be the coefficients of the square of the bracket. Then exactly

    d_j=(2l+1)sum_{k=0}^{2l} q_k (3^(k+1)-1)/(k+1)
                         [Z(k+2)/Z(2k+4)-1],          (12)
    Z(s)=(1-2^-s)zeta(s).

All arguments are in the absolutely convergent region. In particular the
k=0 factor is 12/pi^2-1. The checker bounds every higher squarefree series
through 8192 plus the complete integral tail. No decimal zeta oracle or
unproved source decay enters its accepting calculation.

### An explicit value of the limiting constant

Completeness of the odd Legendre basis gives, for every 0<x<1,

    sum_{j>=0}psi_j(x)^2 = ||1_[x,1](u)/u||_2^2 = 1/x-1.

Because |omega(x)-c0|<=6sqrt(x), dominated convergence therefore identifies

    C_*=integral_0^1 [omega(x)-c0](1/x-1)dx.

This integral is absolutely convergent. Put

    b=alpha[gamma+log2-2Z'(2)/Z(2)]-1.

Partial summation of (9) and the Laurent expansion of Z(s)/Z(2s) at s=1 give
sum_{3<=n<=X, odd}mu(n)^2/n=alpha logX+b+O(X^(-1/2)). This expansion uses only
the absolutely convergent denominator at 2 and the ordinary pole of zeta at 1.
For T=1/epsilon,

    integral_epsilon^1 omega(x)dx/x
      =log3 sum_{3<=n<=T, odd}mu(n)^2/n
       +sum_{T<n<=3T, odd}mu(n)^2/n log(3T/n)
      =c0 logT+b log3+(alpha/2)(log3)^2+o(1).

Also integral_0^1 omega(x)dx=2[12/pi^2-1]. Subtract the corresponding
c0 integral and take the limit to obtain

    C_*=2-log3-24/pi^2
       +(4log3/pi^2)[gamma+log2+1-2Z'(2)/Z(2)+(log3)/2]. (13)

No zero locations, reciprocal derivative at a zero, or RH input enters this
constant. The exact expression is part of the proposed theorem; no broad
external priority claim is made for classical Legendre/Hardy or squarefree
asymptotics used to derive it.

## 3. TC26-3: the exact covariance needs a common source cutoff

For n odd and n>=3 define the H_N=(L2(1,3))^N vector

    v_n(t)=(psi_j(t/n)/n)_{j<N}.

For each FIXED N, the source-ordered sum satisfies

    (Kphi_j)_{j<N}=-lim_{R->infinity}sum_{3<=n<=R, odd}mu(n)v_n
                                                       in H_N.          (3.1)

Therefore

    S_N=D_N+C_N,
    C_N=lim_{R->infinity}sum_{3<=n,m<=R, odd, n!=m}
                              mu(n)mu(m)<v_n,v_m>.     (3.2)

The ordered double cutoff in (3.2) is part of the definition. It is not an
absolutely convergent double series. This C_N is NOT the all-integer Newton
covariance in PR848/875/869.

### Source-faithful proof, including the terminal term

Put A_j(x)=integral_0^x phi_j(u)du/u as above. Absolute monomial summation,
including the n=1 contribution, gives

    Kphi_j(t)=b_j+sum_{n>=3, odd}mu(n) A_j(t/n)/n.       (3.3)

For finite R>=3 write

    h_(j,R)(t)=b_j m(R)-sum_{3<=n<=R, odd}mu(n)psi_j(t/n)/n.

This is EXACTLY b_j+sum_{3<=n<=R}mu(n)A_j(t/n)/n, not an approximate balance.
Let a_r denote the coefficients of unnormalized P_(2j+1), and define

    L_j=sqrt(4j+3)sum_{r odd}|a_r|/r,
    L_N^2=sum_{j<N}L_j^2,       B_N=sum_{j<N}b_j^2.

Since |A_j(x)|<=L_j x on [0,1], the ENTIRE remaining source tail obeys

    ||(Kphi_j-h_(j,R))_{j<N}|| <=3sqrt(2)L_N/R.          (3.4)

This constant is explicit and finite but is not claimed optimal in N. Let R
grow with N FIXED, then use the stated classical m(R)->0. This proves (3.1).
Diagonal convergence follows from (12) or positivity in (10), and (3.2) follows
by squaring the same finite vector sum before taking the limit.

A complete diagonal truncation bound is also available:

    0<=D_N-D_(N,R)
       <=2B_N/R+6sum_{j<N}|b_j|L_j/R^2+6L_N^2/R^3.     (3.5)

It follows by expanding 2(|b_j|+3L_j/n)^2/n^2 and using integral tails at
powers 2,3,4. These are finite-computation remainder estimates; they do not
supply a degree-uniform bound on the covariance.

### The remaining proof obligation

By (7), S_N=N^{o(1)} is equivalent to C_N^+=N^{o(1)} in the upper-bound
sense, where C_N^+=max(C_N,0) is taken AFTER the complete signed limit.
The same equivalence holds along any specified unbounded sequence. The
DG26 consumer would then imply RH. In particular a sufficiently mild upper
bound on C_(2N)-C_N over all dyadic blocks would finish the trace route.
Neither upper bound is obtained here. This algebraic restatement is not
counted as a proof of cancellation.

## 4. TC26-4: the termwise positive and negative covariances both diverge

This is a native all-tail obstruction, not a changed-source model. For fixed
N>=1 let P_N(R), M_N(R) be the sums of the positive and negative parts of the
individual off-diagonal summands in the finite square cutoff of (3.2). Then

    P_N(R)=alpha^2 B_N (log R)^2+O_N(log R),
    M_N(R)=alpha^2 B_N (log R)^2+O_N(log R).             (4.1)

Both tend to positive infinity even though their signed difference has the
finite limit C_N. In particular C_N^+ in Section 3 must NOT be replaced by
P_N(infinity), which is infinite at every fixed degree count.

### Proof

Since psi_j(x)=b_j+O_j(x) at zero,

    <v_n,v_m>=2B_N/(nm)
                   +O_N(n^-2 m^-1+n^-1 m^-2).         (4.2)

For sufficiently large n,m it is positive. The cumulative error in (4.2)
over the square cutoff is O_N(log R). Pairs with at least one of n,m below
the fixed positivity threshold also contribute only O_N(log R). Diagonal
terms have finite total size and do not affect the leading asymptotic.

Partial summation of (9) gives sum_{3<=n<=R, odd}mu(n)^2/n=alpha logR+O(1).
The boundedness of m(R) then gives, separately,

    sum_{3<=n<=R, odd, mu(n)=+1}1/n=(alpha/2)logR+O(1),
    sum_{3<=n<=R, odd, mu(n)=-1}1/n=(alpha/2)logR+O(1).

The positive ordered-pair contribution in the leading term of (4.2) uses the
sum of the squares of these two harmonic sums. The negative contribution
uses twice their product. Both give alpha^2 B_N(logR)^2+O_N(logR). QED.

A complete absolute-value majorant therefore cannot prove the native trace
bound in this representation. Separate infinite sign sums and unqualified
rearrangements would produce infinity minus infinity, not (3.2).

## 5. TC26-5: an exact random-prime reference, and its limitation

This is a comparison model, NOT a replacement for the actual Mobius source.
Assign independent uniform signs epsilon_p in {-1,+1} to odd primes, and put
chi_epsilon(n)=product_{p|n}epsilon_p for squarefree odd n. The characters
indexed by distinct squarefree n are orthonormal on this product probability
space. Thus the H_N-valued series

    X_N(epsilon)=sum_{n>=3, odd}mu(n)^2 chi_epsilon(n) v_n

converges in L2(probability; H_N), and

    E ||X_N||^2=D_N.                                   (5.1)

Choose consistent versions of its countably many output columns and set
S_N^epsilon=||X_N||^2. These traces are nondecreasing in N. A sharper-than-
subpower almost-sure conclusion follows just from (7): for every delta>0,

    S_N^epsilon=O_epsilon,delta(log(2N)
                           [loglog(4N)]^(1+delta))
                                      almost surely.   (5.2)

Here the constant may depend on the sign realization. To prove this, take
N_r=2^(2^r). Since E S_(N_r)<=C 2^r, Markov gives probability at most
C/r^(1+delta) for S_(N_r)>2^r r^(1+delta). Borel--Cantelli and monotonicity
interpolate between consecutive N_r, whose logarithms differ by a factor two.
No independence between successive degree cutoffs is needed. Use countably
many positive rational delta to obtain simultaneous statements for all delta.
In particular the random trace is subpower almost surely.

The native assignment is the SINGLE configuration epsilon_p=-1 at every
prime. It has probability zero. The pointwise source-ordered value at that
configuration is supplied by (3.1), not by evaluation of an arbitrary L2
version. Equation (5.2) therefore says NOTHING about the required native bound.
In fact the all-positive configuration has output of size proportional to
logR at every fixed degree cutoff, by (4.2) and squarefree counting. The model
has no uniform bound over all sign configurations. It does not satisfy the
literal native divisor inverse equations except at the native assignment.

This comparison isolates a possible new task: a source-specific pointwise
estimate at the all-negative prime configuration, not another averaged
Euler or random-sign estimate. No such pointwise theorem is proved here.

## 6. Attempted closing argument and exact outcome

The attack was to control the dyadic trace increment by its actual arithmetic
diagonal. Sections 1-2 complete that calculation: it has a finite positive
limiting increment and a summable column error. The full trace nevertheless
includes (3.2). Sections 3-4 show why a purported upper bound obtained by
separating its signs is not even finite, and Section 5 explains precisely
what averaging over multiplicative signs proves and fails to prove.

Direct certified native calculations already give C_1>1 and C_2>C_1. Thus
the unqualified claims C_N<=0 for every N or nonincreasing C_N from N=1 are
false. This does not decide either eventual behavior or a subpower upper
bound. The finite values later decrease; no all-degree assertion is inferred.

No new upper rate for S_N, fixed power saving, zero-free region, or RH proof
is obtained. The latest PR869 qualitative S_N=o(N) and exact exponent results
remain separately credited; they are not rediscovered here. Reviewers are
asked to check the new primitive identity, actual squarefree diagonal,
conditional-cutoff accounting and divergence of the separated sign parts,
not to fill the remaining native covariance bound as a routine final step.

# MWR26: an exact work balance for the literal Mobius inverse

Status: PROPOSED COMPONENT THEOREMS WITH COMPLETE PROOFS; independent review pending.
Date: 2026-09-06. Author: Astra. This is research, not a Reviewer D disposition.
RH and completeness of the critical source domain remain unproved.

## 1. Objects and quantifiers

Use Lebesgue L2(0,infinity), with inner product conjugate-linear in the first
slot. All convolution is causal. The parent DCP26 kernel is

    phi(t)=exp(-t)P(t),
    P(t)=1-(5/2)t+(7/8)t^2-t^3/16,        t>=0,
    Phi(z)=(z-1/2)(z+1/2)^2/(z+1)^4.

For ordinary Mobius coefficients, define

    a_n=mu(n)/sqrt(n), tau_n=log n,
    h(t)=sum_(tau_n<=t) a_n phi(t-tau_n),
    h_N(t)=sum_(n<=N) a_n phi(t-tau_n)1_(t>=tau_n),
    H(T)=integral_0^T |h(t)|^2 dt,
    J_N=integral_0^infinity |h_N(t)|^2 dt.

Every compact-time sum is finite. h_N is in L1 and L2, and for t<log N it
agrees with h. These definitions DIFFER: H is the past of the infinite
source, while J_N includes the entire future of the FINITE input h_N.
Neither is the norm of the factorial-source output y_T. The source output
is y_T=d*(h 1_[0,T]), and its norm is bounded by 6 sqrt(H(T)).

In particular an upper bound for J_N bounds the required H(log N), but a
small finite J_N says nothing by itself about later arithmetic events.

## 2. The four-dimensional realization

Let e=(1,0,0,0)^T and

    A=[[-1,0,0,0], [1,-1,0,0], [0,1,-1,0], [0,0,1,-1]],
    C=[1,-5/2,7/4,-3/8].

Then

    C exp(At)e = exp(-t)P(t),
    C(zI-A)^(-1)e = Phi(z).

Start at x(0-)=0. Between events set x'=Ax and at t=log n set

    x(log n+)=x(log n-)+a_n e.

The output is h(t)=Cx(t). All arithmetic is in the actual a_n; A and C
are fixed rational matrices. Let x_N=x(log N+) for the process stopped
after event N. Its complete future is exp(A(t-log N))x_N.

Define

    Q=(1/2048)*[[385,-639,324,-54],
               [-639,3518,-2882,660],
               [324,-2882,2536,-600],
               [-54,660,-600,144]].                     (W1)

**MWR26.T1 (exact energy identity).** Q is positive definite and

    A*Q+QA=-C*C,
    Q=integral_0^infinity exp(A*t)C*C exp(At)dt.          (W2)

Here * denotes the conjugate transpose. For the actual real matrices it is
ordinary transpose. For every N>=1,

    J_N = H(log N)+x_N*Qx_N = D_N+W_N,                  (W3)

where

    D_N=(385/2048) sum_(n<=N) mu(n)^2/n,
    W_N=2 Re sum_(n<=N) conjugate(a_n)e*Q x(log n-).      (W4)

Every term in (W3) is retained, including the n=1 event and the whole
infinite future of the stopped finite input. In particular

    H(log N) <= J_N,
    0 <= D_N <= (385/2048)(1+log N).                    (W5)

The identity also holds for arbitrary finite complex impulse amplitudes
with mu(n)^2/n replaced by |a_n|^2.

### Proof

The matrix exponential is e^-t times the lower triangular matrix with
entry t^(i-j)/(i-j)! for i>=j, with indices 0,...,3. Integrating the products
of its output polynomials gives (W1). Direct multiplication verifies (W2).
The integral is positive definite because C exp(At)x can vanish identically
only if its polynomial coefficients all vanish. The coefficient of t^3
first forces x_0=0, that of t^2 then x_1=0, and so on, since C_3=-3/8.
Alternatively its exact LDL pivots are

    385/2048,
    946109/788480,
    6400405/484407808,
    6561/3277007360,

all strictly positive.

Between events (x*Qx)'=-|Cx|^2. At an event with amplitude a,

    Delta(x*Qx)=2 Re(conjugate(a)e*Qx_-)+|a|^2 e*Qe.

Sum these identities through t=log N; isolated output jumps have no effect
on its L2 integral. The state starts at zero. After the last event its
entire future squared output is x_N*Qx_N by (W2). This proves (W3)-(W4).
The bound (W5) follows from |mu|<=1 and the harmonic-sum bound.

This is the usual finite-dimensional observability/Lyapunov identity,
proved here at the actual rational coefficients. The general identity is
not claimed new; the explicit signed arithmetic work and source-specific
application are the contribution.

## 3. The exact scalar interaction and a linear-event algorithm

For v>=0 define

    R(v)=exp(-v)(385-639v+162v^2-9v^3)/2048.            (W6)

The integral definition of Q gives

    e*Q exp(Av)e = integral_0^infinity phi(u)phi(u+v)du = R(v).

Consequently (W4) is equivalently the complete untruncated interaction

    W_N=2 sum_(m<n<=N) mu(m)mu(n)/sqrt(mn) R(log(n/m)).  (W7)

The truncated correlation in DCP26 must not be replaced by R entrywise.
What justifies its use here is the EXACT nonnegative endpoint correction
x_N*Qx_N in (W3). The correction is a rank-at-most-four positive Gram on
the whole finite impulse coefficient space. It is not a termwise-positive
correction to each off-diagonal entry.

No double loop is needed to evaluate (W7). If delta_n=log(n/(n-1)) and
r_n=(n-1)/n, the pre-jump state for n>=2 is

    x_- = r_n * [ x_0,
                  x_1+delta_n x_0,
                  x_2+delta_n x_1+delta_n^2 x_0/2,
                  x_3+delta_n x_2+delta_n^2 x_1/2+delta_n^3 x_0/6 ].
                                                               (W8)

Then add 2a_n e*Qx_- to W, (385/2048)a_n^2 to D, and a_n to state zero.
After a Mobius sieve this uses O(N) arithmetic events and O(1) dynamic
state, besides the sieve. Bit complexity depends on precision, log-series
lengths and integer arithmetic; O(N) is not asserted as a bit bound.

The algorithm does not truncate any of the future exponential-polynomial
filter tails. This is why one may certify J_N directly, without a separate
large real-time integration endpoint.

## 4. Two concrete attempts at the missing sign

### 4.1 Universal diagonal domination is false on the actual source

The tempting strengthening W_N<=0 for every N is false already at N=3:

    W_3>1/20.                                         (W9)

No counterfeit source is used. With a_1=1, a_2=-1/sqrt2, a_3=-1/sqrt3,

    W_3=-sqrt2 R(log2)-(2/sqrt3)R(log3)
                         +(2/sqrt6)R(log(3/2)).

Directed atanh logarithm series and integer square-root enclosures in
certify.py prove (W9); certificate.normal.json retains all rational
endpoints. The same formula can be checked independently by (W7).
This only rejects the universal bound. It does not reject a possible
sufficient eventual or subpower bound, neither of which is proved here.

### 4.2 Passivity is a lower energy bound, not an arithmetic upper bound

For arbitrary complex impulses, (W3) implies W_N>=-D_N. It does not give
W_N<=D_N or W_N<=0. In the jump identity the linear cross term can have
either sign and is unbounded over arbitrary pre-jump states for a fixed
nonzero impulse. A universal bound on that cross term from passivity alone
is therefore unavailable. Any stronger bound for the actual trajectory
must use the literal Mobius inputs, not replace them by arbitrary noise.

The elementary unconditional upper bound is

    J_N <= ||phi||_2^2 (sum_(n<=N) |mu(n)|/sqrt n)^2
         < (385/512)N.                               (W10)

This follows from the triangle inequality and sum n^-1/2<2sqrt N. It is
still a positive power of N, not the required subpower estimate.

## 5. Exact RH consequence; the missing estimate is NOT claimed

**MWR26.C1.** The following are equivalent:

    (a) RH;
    (b) J_N=O_epsilon(N^epsilon) for every epsilon>0;
    (c) W_N<=C_epsilon N^epsilon for every epsilon>0.

Here constants may depend on epsilon. (c)->(b) follows from (W3)-(W5).
If (b) holds, H(log N)<=J_N, and monotonicity of H extends the subpower
bound to every real T. The original locally exact output y_T=d*h_T
belongs to the original factorial-source domain, has ||y_T||<=6sqrt H(T),
and agrees with the fixed target

    f(t)=exp(-t)[t-(3/2)t^2+(3/8)t^3].

Suppose rho=1/2+delta+i gamma is a zero with delta>0 and put lambda=rho-1/2.
The Laplace transform of y_T vanishes at lambda, including multiplicity.
Consequently

    ||y_T 1_[T,infinity)||^2 >=
       2delta exp(2delta T)|integral_0^T exp(-lambda t)f(t)dt|^2.

The integral tends to F(lambda)=(lambda-1/2)^2/(lambda+1)^4, which is
nonzero for any such nonreal zero. This contradicts the subpower bound.
Reflection then yields RH. This is the parent's zero-detection argument,
not a new assumption of outerness.

For the converse ONLY, import the classical Littlewood implication
RH -> sum_(n<=x)mu(n)=O_epsilon(x^(1/2+epsilon)). The state coordinates are

    (x_N)_j=(1/(N j!))sum_(n<=N)mu(n)sqrt n (log(N/n))^j,
                      j=0,1,2,3.                    (W11)

Partial summation gives x_N=O_epsilon(N^epsilon). The same argument for
the output at intermediate t gives h(t)=O_epsilon(exp(epsilon t)).
After replacing epsilon by a smaller positive exponent, H(log N),
x_N*Qx_N, and J_N are all O_epsilon(N^epsilon). This proves (a)->(b);
(b)->(c) is immediate from W_N=J_N-D_N and D_N>=0.

An unbounded subpower subsequence of J_N would already exclude an off-line
zero: the displayed lower bound holds for EVERY sufficiently large T.
No such subsequence is proved by a finite list of certificates.

The equivalence is within the classical Nyman--Beurling/Mobius-convolution
lineage. The advance is exact finite-state accounting and certified
computation, not a claim that the arithmetic difficulty has disappeared.

## 6. Certified finite range and what it does not imply

The fixed run in certify.py covers every integer event 1,...,65536, and
retains fifteen checkpoint norms with all future tails included. At the
last checkpoint it proves, for example,

    721/1000 < J_65536 < 723/1000,
    718/1000 < H(log65536) < 720/1000,
    2/1000 < x_65536*Qx_65536 < 3/1000.

All stated inequalities are checked with rational endpoints. The decimals
used in any narrative table are summaries, not interval endpoints.
The certificates also reproduce the parent's H(log64) bound by a different
four-state calculation. An independent direct finite pairwise calculation
at twelve small cutoffs checks (W7)-(W8).

Neither a monotone limit for J_N nor an upper bound outside the fixed run
is asserted. In particular the infinite source h has further impulses
beyond 65536, none of which is covered by the stopped-input future tail.
See RESONANCE.md: H(T), and hence J_N, cannot even stay bounded as the
arithmetic cutoff increases. This is compatible with the weaker subpower
bound needed for completion.

# CCS26: where the literal Mobius source sits in the divisor decomposition

Status: proposed component proofs and an UNSUCCESSFUL closing estimate.
The requested unconditional RH proof is not supplied. The point of this adapter
is to identify the actual missing channel before composing unrelated estimates.

## 1. One explicit native field, with a complete rational norm

Use V=L2(0,infinity), with ordinary causal shifts S_t. Put

    phi(t)=exp(-t/2)1_(t>=0),
    v_n=mu(n) S_(log n)phi, 1<=n<=N,
    g_n=1/sqrt(n), H_N=sum_(n<=N)1/n,
    h_N=sum_(n<=N)mu(n)/sqrt(n) S_(log n)phi.

This is a deliberately SIMPLE fixed filter. It is not the cubic exponential
filter in #804's work/resonance packet, and its finite numerical norms must not
be substituted for that packet's numbers. The ordinary Mobius source, all
integer indices, shift times and critical n^(-1/2) weights are literal.

Let M(x)=sum_(n<=x)mu(n). Then

    h_N(t)=exp(-t/2) M(min(N,exp t)).                         (1)

Its ENTIRE squared norm, including the future after the final arithmetic event,
is the finite rational number

    J_N := ||h_N||^2
        = sum_(k=1)^(N-1) M(k)^2/[k(k+1)] + M(N)^2/N
        = sum_(m,n<=N) mu(m)mu(n)/max(m,n).                  (2)

Indeed ||phi||=1 and <S_logm phi,S_logn phi>=sqrt(min(m,n)/max(m,n)).
Alternatively integrate (1) on each integer cell x=exp t and on [N,infinity).
The terminal term M(N)^2/N is essential. All ordered cross terms remain in (2).
The native source can be evaluated by a single pass after the Mobius sieve;
this is an arithmetic-operation statement, not a bit-complexity claim.

## 2. The native norm is EXACTLY the harmonic channel, not its complement

Let Pi_N be the orthogonal projection in ell2({1,...,N};V) onto
{(c/sqrt(n))_(n<=N):c in V}. Then

    (Pi_N v)_j = h_N/[H_N sqrt(j)],
    ||Pi_N v||^2 = J_N/H_N,
    ||(I-Pi_N)v||^2 = Qsf(N)-J_N/H_N,                       (3)

where Qsf(N)=sum_(n<=N)mu(n)^2. These identities are just the normalized
Hilbert-valued projection formula, applied BEFORE taking any absolute values.
Thus the arithmetic sum whose subpower norm would suffice for RH lies EXACTLY
in the mode annihilated by the divisor graph. It is not an arbitrary nuisance
mean that may be subtracted without changing the target.

For any finite Hilbert vector c, replacing a vertex field v by
v+(c/sqrt(n)) leaves its entire graph gradient unchanged and changes the
coherent sum by H_N c. This is a universal algebraic limitation, not a claim
that the modified field retains Mobius coefficients. Equation (3) separately
locates the LITERAL Mobius field in that decomposition.

## 3. The full native edge energy has an unconditional main term

Keep every prime-power edge and its original weight:

    E_N(v)=sum_(p^k j<=N) log p ||v_(p^k j)-p^(-k/2)v_j||^2.

Let A_Lambda(x)=sum_(q<=x)Lambda(q)/q. Exact expansion gives

    E_N(v)=sum_(n<=N)mu(n)^2 log n
          +sum_(j<=N)mu(j)^2 A_Lambda(N/j)
          +2sum_(p<=N)(log p)/p
                    sum_(j<=N/p, p does not divide j)mu(j)^2.   (4)

To check this, a prime-power q contributes

    log p [mu(qj)^2 + mu(j)^2/q - 2mu(qj)mu(j)/q].

For k>=2 the product mu(qj)mu(j) is zero. For k=1 it is -mu(j)^2 if p does
not divide j, and zero otherwise. The incoming diagonal is log n by
sum_(q|n)Lambda(q)=log n; the outgoing diagonal contains ALL higher powers.
This proves (4) with no heuristic independence or sign replacement.

Each displayed contribution in (4) is nonnegative. In particular all the
long-range signed correlations of J_N have disappeared from this LOCAL
prime-power edge energy. They have not been estimated; this is a different
quadratic observation of the same vertex field.

**CCS3.** Unconditionally,

    E_N(v) = (6/pi^2) N log N + O(N).                      (5)

Proof: the elementary squarefree count Qsf(x)=x/zeta(2)+O(sqrt x), reconstructed
in PROOF.md, gives the first term as c_sf N log N+O(N). Also
A_Lambda(x)<=log x+3, so the second term is at most
sum_(j<=N)[log(N/j)+3]<=4N. The third is bounded by
2N sum_(p)log p/p^2<=2N sum_(n>=2)log n/n^2=O(N). This proves (5).
No PNT, RH or mean-square Mertens theorem is imported.

The available graph gaps control the LEFT side of

    Qsf(N)-J_N/H_N <= kappa_N E_N(v).                      (6)

They do not give an upper bound on J_N. Rearranging (6) gives only the
wrong-direction lower bound J_N >= H_N[Qsf(N)-kappa_N E_N(v)], usually negative.
The theorem E_N~c_sf N log N quantifies the mismatch. Replacing E_N by its
Poincare-controlled complement does not manufacture a signed-coherent estimate.

## 4. A complete sufficient RH chain, without source-domain assumptions

The native bound

    J_N=O_epsilon(N^epsilon) for every epsilon>0           (7)

would imply RH. This is in the classical Mertens/causal-approximation lineage;
its role here is the exact adapter (3), not a claim of a new easier criterion.
Here is a full proof of the implication, including the future horizon.

Use the ACTUAL factorial source

    d(t)=exp(-t/2)[floor(exp t)(1-t)+log(floor(exp t)!)],
    D(z)=(z-1/2)zeta(z+1/2)/(z+1/2)^2, ||d||_1<=6.

The source identity follows by integrating the floor series in Re(z+1/2)>1
and by analytic continuation; 0<exp(t/2)d(t)<=1+t proves the norm bound.
The pole at z=1/2 has its removable analytic value. Put y_N=d*h_N. It is a
legitimate ordinary L2 convolution, ||y_N||<=6 sqrt(J_N), and

    Ly_N(z)=(s-1)zeta(s)P_N(s)/s^3,
    P_N(s)=sum_(n<=N)mu(n)n^-s, s=z+1/2.                  (8)

The uncut inverse has product transform (s-1)/s^3 initially in Re s>1.
Equivalently finite Mobius inversion proves

    y_N(t)=h_*(t):=exp(-t/2)(t-t^2/2),
                  0<=t<log(N+1).                        (9)

There is no compactly supported inverse assumption. Every convolution before
the horizon uses only the exact coefficients through N. The target has
||h_*||^2=2 and transform H_*(z)=(z-1/2)/(z+1/2)^3.

If rho=beta+i gamma is a nontrivial zeta zero with beta>1/2, put
alpha=beta-1/2>0 and lambda=rho-1/2. Equation (8) gives Ly_N(lambda)=0, while
H_*(lambda)=(rho-1)/rho^3 is nonzero. The error is supported after T=log(N+1).
Cauchy-Schwarz on that delayed support yields

    ||y_N-h_*||^2 >= 2alpha (N+1)^(2alpha)|rho-1|^2/|rho|^6. (10)

Thus

    6sqrt(J_N)+sqrt2 >= sqrt(2alpha)|rho-1|/|rho|^3
                                     * (N+1)^alpha.       (11)

It follows that any such zero forces

    liminf_(N->infinity) log(1+J_N)/log(N+1) >= 2alpha.     (12)

Therefore even a single unbounded subpower subsequence of J_N would exclude
all right-of-line zeros; reflection would give RH. No zero simplicity,
numerical zero table or cancellation between unknown zero phases is assumed.
The zero occurs only in the contradiction, not in the definitions.

For the converse ONLY, the classical Littlewood implication
RH => M(x)=O_epsilon(x^(1/2+epsilon)) gives (7) by (2), with epsilon halved.
No use of that implication is made in CCS1-CCS3 or in the unconditional
construction. The subpower estimate (7) itself is NOT proved here.

## 5. The precise attempted estimate and its stopping point

The exact one-step work law is

    J_N-J_(N-1)=[2mu(N)M(N-1)+mu(N)^2]/N,
    J_N=sum_(n<=N)mu(n)^2/n
          +2sum_(n<=N)mu(n)M(n-1)/n.                      (13)

The unsigned diagonal is O(log N). An eventual upper bound on the SIGNED work
by C_epsilon N^epsilon for every epsilon>0 would therefore suffice. The
unconditional graph identity (4) supplies no such bound: it sees only
squarefree counts and prime-neighbor signs, while (13) includes all additive
prefix correlations. This is the precise point where the attempted
#825/#826 + #804/#817 composition fails.

Neither resetting M(n-1) in each block nor treating different primes as random
is legitimate for this source. Taking absolute values gives only a positive
power (for example J_N<2N from |M(k)|<=k), not (7). No fixed or growing-order
signed work saving is asserted. The Mertens formula and its full future are
stated to make the missing estimate auditable, not to relabel it as proved.

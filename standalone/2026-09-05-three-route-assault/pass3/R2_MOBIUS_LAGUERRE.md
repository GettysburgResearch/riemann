# Route 2: reciprocal-zeta Laguerre coefficients and an unconditional diagonal bound

Status: PROPOSED COMPLETE PROOFS; independent mathematical review required. No new signed Mobius cancellation estimate or RH proof.
Sources: PR #792's actual-prime Laguerre/diagonal programme; PR #793/pass2 causal norm and its anti-causal warning. This is a NEW, explicitly defined reciprocal-zeta coefficient sequence. It is not #792's prime logarithmic-derivative sequence.

## L1. A fixed source sequence, with no moving detector

Let q=67, mu_q(k)=mu(k)1_(q does not divide k), and let L_n denote ordinary Laguerre polynomials:

    L_n(t)=sum_(j=0)^n (-1)^j binom(n,j)t^j/j!.

Define, for every n>=0,

    a_n=sum_(k>=1) mu_q(k) k^(-3/2) L_n(2log k),
    A(z)=sum_(n>=0) a_n z^n as a germ at z=0.

Every individual infinite sum is absolutely convergent. The classical Laguerre generating function gives exactly

    A(z)=1/[(1-z) zeta(w(z)) (1-q^(-w(z)))],
    w(z)=1/2+(1+z)/(1-z)=(3+z)/[2(1-z)].                  (L1)

One may first interchange sums for |z|<1/5: absolute generating bounds leave the k exponent strictly less than -1. Only then use meromorphic continuation. The map w sends the unit disk to Re w>1/2, and w(0)=3/2 is an absolutely convergent arithmetic source. The zeta pole at w=1 becomes a ZERO, not a pole, of A. The finite-Euler denominator has no zero in that half-plane.

Thus

    RH <=> limsup |a_n|^(1/n)<=1
       <=> E_N:=sum_(n=0)^N |a_n|^2 is subexponential in N. (L2)

Subexponential means E_N<=C_epsilon exp(epsilon N) for every epsilon>0, including every finite initial N after changing the constant. No assumption of holomorphy is smuggled into an integral of meromorphic boundary values: (L1) is an identity of the ORIGINAL Taylor germ.

### Exact detection exponent

Every nontrivial zero rho contributes a nonremovable pole at

    z_rho=(rho-3/2)/(rho+1/2),
    1-|z_rho|^2=4(Re rho-1/2)/|rho+1/2|^2.                 (L3)

Multiplicity is retained as pole order. Define

    R=max(1,sup_rho |rho+1/2|/|rho-3/2|).

The critical strip and discreteness imply that any value greater than one is attained among finitely many relevant zeros. There are no other poles inside the disk. Cauchy's radius formula, including the case of no interior pole, gives

    limsup E_N^(1/(2N))=R.                                (L4)

For the case R=1, either the known existence of a critical-line zero or the elementary lower bound E_N>=|a_0|^2 together with the upper radius bound suffices for the energy statement. The growth of partial squared sums follows by bounding coefficients above by (R+epsilon)^n and below along a Cauchy--Hadamard subsequence. No phase independence or rightmost zero is required.

## L2. A polynomial upper bound for the literal diagonal, valid at every degree

Let

    Delta_n=sum_(k>=1) mu_q(k)^2 k^-3 L_n(2log k)^2,
    D_N=sum_(n=0)^N Delta_n.

**Theorem.** For every n>=0,

    1<=Delta_n<=2+2sqrt(n),
    N+1<=D_N<=2(N+1)+2N sqrt(N).                          (L5)

This uses the actual support and weights; it is not a numerical prime or integer census. In fact the upper bound holds with mu_q(k)^2 replaced by ANY weights between zero and one.

Proof. Put g(x)=x^-3 L_n(2log x)^2. Summing

    g(k)<=integral_k^(k+1) g(x)dx+integral_k^(k+1)|g'(x)|dx

gives sum g(k)<=integral_1^infinity g+integral_1^infinity|g'|. With t=2log x, ordinary Laguerre orthogonality and L_n'=-sum_(j<n)L_j give

    integral g dx=1/2,
    integral |g'|dx
      =integral_0^infinity e^(-3t/2)|-(3/2)L_n^2+2L_n L_n'|dt
      <=3/2+2sqrt(n).

Here integral e^-t L_n^2=1 and integral e^-t(L_n')^2=n, also for n=0. Dropping the extra e^(-t/2) and applying Cauchy--Schwarz proves the bound. The term k=1 is one at every degree, proving the lower bound. Summation proves L5. QED.

## L3. The complete energy keeps every signed cross term

For every fixed N the sums below are absolutely convergent and

    E_N=sum_(k,l>=1) mu_q(k)mu_q(l)(kl)^(-3/2)
                       K_N(2log k,2log l),
    K_N(t,u)=sum_(n=0)^N L_n(t)L_n(u)
      =(N+1)[L_N(t)L_(N+1)(u)-L_(N+1)(t)L_N(u)]/(t-u).    (L6)

At t=u use the continuous derivative limit. This is the standard Christoffel--Darboux identity, now for alpha=0, not the alpha=-1 normalization of #792. The diagonal k=l is exactly D_N. All coprimality restrictions and the k=1 cross terms remain present.

It follows from L2 and L5 that

    RH <=> E_N <= C_epsilon exp(epsilon N) D_N
                 for every epsilon>0 and every N.          (L7)

Any polynomial-loss comparison is sufficient, but unlike #792's logarithmic-derivative sequence it is NOT asserted necessary under RH. The difference is important and proved below.

## L4. Exact same-diagonal countercontrol

Replace only the signs by b(k)=mu_q(k)^2. Its diagonal is IDENTICALLY Delta_n, at every n, since b(k)^2=mu_q(k)^2. Its generating function is

    A_+(z)= zeta(w(z)) /
      [(1-z) zeta(2w(z)) (1+q^(-w(z)))].                   (L8)

For Re w>1/2, the denominator zeta(2w) has no zeros, and 1+q^-w is nonzero. The numerator has its noncancelling pole at w=1, namely z=-1/3. This is the only pole in the disk, so

    limsup |a_(+,n)|^(1/n)=3,
    limsup (sum_(n<=N)|a_(+,n)|^2)^(1/(2N))=3.             (L9)

This control preserves the EXACT squarefree support, exact diagonal, and coefficients bounded by one. It is not actual reciprocal zeta. It proves that even the literal diagonal and squarefree arithmetic support cannot supply L7 without the actual Mobius signs.

A complementary arbitrary-vector obstruction also holds. Normalize M columns (L_n(2log k)k^-3/2)_(0<=n<=N) for M distinct supported integers. Their Gram matrix has trace M and rank at most N+1, hence largest eigenvalue at least M/(N+1). Generic diagonal comparison must pay this cost. No such arbitrary-vector bound is substituted for the one literal arithmetic vector.

## L5. Multiplicity firewall: polynomial losses are not free for reciprocal zeta

Suppose E_N=O((N+1)^B) with finite B>=0. For 0<r<1, partial summation gives sum |a_n|^2 r^n=O((1-r)^-B). Cauchy--Schwarz then yields

    |A(r e^(i theta))|=O((1-r)^(-(B+1)/2)).                (L10)

If rho is a critical-line zero of multiplicity m, A has a genuine order-m pole at its boundary point z_rho, away from z=1. Radial approach to that point and L10 imply

    2m-1<=B.                                              (L11)

Thus a polynomial energy theorem would also bound ALL critical-line zero multiplicities uniformly. RH alone is not known to give that bound. In #792 the logarithmic derivative has only simple poles even at multiple zeros; that branch's polynomial conclusion therefore cannot be copied to this reciprocal sequence. We make no sufficiency claim for bounded multiplicities alone either: residue conditioning and accumulation may add further costs.

## L6. Relation to the causal programme, and the unsuccessful final step

The same Cayley map underlies the Laguerre expansion of the causal prefix B_t from pass2. L1 instead expands the reciprocal Dirichlet source itself, avoiding an additional prefix factor. It preserves the same off-line poles, but is not identified with the preceding J_sigma norm.

The attempted estimate was to use the newly paid diagonal with a Christoffel--Darboux or large-sieve comparison. L4 shows that all sign-blind versions fail, even with the EXACT same diagonal. No source-specific bound for the signed off-diagonal in L6 was obtained. L5 also prevents silently strengthening the intended endpoint to a polynomial estimate. The retained target is the subexponential comparison L7, with the actual signs assembled before every bound.

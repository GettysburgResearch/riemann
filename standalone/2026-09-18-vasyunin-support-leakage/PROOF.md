# Squarefree support rigidity and an exact source-aware Gram decomposition

Status: PROPOSED component proofs, requiring independent review.
Scope: universal identities and bounds in the discrete Nyman--Beurling space;
finite exact regression checks; one imported conditional completeness theorem.
No proof of RH, new zero-free region, or priority claim is made.

The finite-support dual system in Section 1 is Vasyunin's system, not a newly
discovered basis. In Balazard [B], our d_r is the negative of f_r after mapping
step functions on [k,k+1) to sequences. Sections 2--8 record consequences and
normalizations useful for this conversation. The Gram and support calculations
are proved here without assumptions about zeta zeros. The RH interpretation
uses Bagchi [G], Theorem 1 and Remark 4. References and reading scope are in
SOURCES.md. Local labels SRL-1 through SRL-8 are not canonical repository IDs.

## 0. Space, source, and the distinction that must be retained

Work over the real numbers; complex versions replace transposes by adjoints.
Let

    <f,g> = sum_{k>=1} f(k)g(k)/[k(k+1)],
    H = l2(N, 1/[k(k+1)]),
    b_n(k) = {k/n},  b_1=0,
    B_N = span(b_2,...,b_N),  E_N=dist_H(1,B_N)^2.

All b_n are bounded and in H. The constant 1 has squared norm 1. The actual
Gram matrix is G_N=(<b_m,b_n>)_{2<=m,n<=N}, with source v_n=log(n)/n.
Thus E_N=1-v^T G_N^{-1}v. These are the weighted sequence coordinates in
Bagchi [G], not the period-averaged GCD norm. By [G], E_N -> 0 iff RH.

The preceding packet introduced the cumulative Ramanujan atoms

    s_d = sum_{n|d} mu(d/n) n b_n,       d>=2.

Their H-source is <1,s_d>=Lambda(d), supported on prime powers. A zero source
entry does NOT mean that the corresponding coordinate can be deleted. A
Schur complement eliminates it while retaining its effect on other entries.

## 1. SRL-1: finite-support dual vectors and exact coefficient recovery

For r>=2 define, for positive integers k,

    U_r(k) = 1_{k|r} mu(r/k),
    q_r(k) = U_r(k)-U_r(k+1),
    d_r(k) = k(k+1) q_r(k).

The support is contained in [1,r]. Direct summation by parts gives

    <1,d_r> = mu(r),
    <k,d_r> = sum_{a|r} mu(r/a) = 0,

where the second scalar product is finite, although the sequence k is not
in H. For n>=2,

    sum_k q_r(k) floor(k/n) = sum_{j>=1} U_r(jn) = 1_{n=r}.

Since b_n(k)=k/n-floor(k/n), it follows that

    <b_n,d_r> = -1_{n=r}.                                  (1)

The formula holds for every n and r, not merely the ranges in verify.py.
For n>r it also follows directly from b_n(k)=k/n on the support of d_r.

For any finite A=sum_n c_n b_n, with omitted c_r interpreted as zero,

    <1-A,d_r> = mu(r)+c_r,
    |mu(r)+c_r|^2 <= ||d_r||^2 ||1-A||^2.                   (2)

Hence any sequence of such approximants converging in H to 1 must satisfy
c_r -> -mu(r) for every fixed r. This does not justify interchanging the
coefficient limit with the infinite sum.

There is also an exact transport formula in the Ramanujan coordinates:

    <s_n,d_r> = -r mu(n/r) 1_{r|n}.                         (3)

Thus, for A=sum_{n<=N} y_n s_n,

    |mu(r)+r sum_{j<=N/r} mu(j)y_{rj}|^2
        <= ||d_r||^2 ||1-A||^2.                            (4)

This is a family of necessary composite-coupling conditions, even though
<1,s_n> vanishes at non-prime-powers.

## 2. SRL-2: a fixed exact obstruction to prime-power-only approximants

For r=6,

    q_6 = (2,0,-1,0,-1,1),
    d_6 = (4,0,-12,0,-30,42),
    <1,d_6>=1,                ||d_6||^2=92.

Equivalently, for all n>=2,

    2{1/n}-{3/n}-{5/n}+{6/n} = -1_{n=6}.

Every prime power fails to be divisible by 6. By (1) and (3), d_6 annihilates
both every b_{p^a} and every s_{p^a}. Therefore, for any finite combination A
of either prime-power-only family, and for every limit of such combinations,

    ||1-A||^2 >= 1/92.                                     (5)

This is a universal theorem from a six-coordinate functional, not a sampled
zero computation. It also shows that a b-approximant with c_6>=0 cannot have
error below 1/92. The required sign at this squarefree composite is negative.

More generally, if a squarefree r is absent from the permitted b-indices,
then every permitted approximation has error at least 1/||d_r||^2>0.
Any fixed bound R on the number of distinct prime factors in permitted
indices fails: choose squarefree r with R+1 prime factors. The statement
also holds for s-indices with that bound, since all their divisors have it.
The positive lower bound depends on R; no uniform bound in R is asserted.

For any finite omitted set I, a stronger simultaneous bound is

    dist(1, permitted span)^2 >= mu_I^T F_I^{-1} mu_I,
    F_I=(<d_r,d_s>)_{r,s in I},

provided every d_r in I annihilates the permitted span. This is projection
onto span{d_r:r in I}. For prime-power-only families, I={6,10,14,15} gives
3562158/256250081, independently checked by exact rational elimination.
No optimality among all annihilating functionals is claimed.

## 3. SRL-3: classification of permitted b-supports (uses [G])

Let S be an arbitrary subset of {2,3,...}. Then

    1 in closure span{b_n:n in S}
      iff [ RH and S contains every squarefree integer >=2 ].            (6)

Necessity: inclusion in the full B and [G, Theorem 1] imply RH. If S omits a
squarefree r, (2) gives a fixed positive gap.

Sufficiency: under RH, the squarefree b-indices alone suffice. This is the
unitarily equivalent sequence form of [G, Remark 4], using Mobius-supported
shifted Dirichlet polynomials. Thus any S containing all squarefree indices
suffices. This direction is IMPORTED, not an independent proof of RH.
Squarefree-only sufficiency is for the target 1, not density in all of H;
for example d_4 annihilates that family but also annihilates 1.

The classification concerns the original b_n basis. It does not say that
all squarefree s_d must individually be retained: equation (3) permits
higher multiples to contribute to the same dual constraint. In particular,
keeping a Schur complement is different from deleting its eliminated
coordinates and replacing it by a principal submatrix.

## 4. SRL-4: the dual Gram contains adjacent-divisor correlations

For r,s>=2 let F(r,s)=<d_r,d_s>. Expanding q_r(k)q_s(k), equal divisors a
receive weight a(a+1)+(a-1)a=2a^2. Distinct terms occur only at adjacent
divisors. Consequently

    F(r,s) = 2 sum_{a|gcd(r,s)} a^2 mu(r/a)mu(s/a)
             - sum_{a|r,b|s,|a-b|=1} ab mu(r/a)mu(s/b).      (7)

All entries are integers. F_N=(F(r,s))_{2<=r,s<=N} is positive definite,
because d_r(r)=r(r+1) and the support matrix is triangular with nonzero
diagonal. Equation (7) is a positive Gram representation; its second sum
must not be dropped. For example F(2,3)=-2, whereas its common-divisor term
alone is +2.

A useful unconditional size estimate follows from (u-v)^2<=2u^2+2v^2:

    ||d_r||^2 <= 4 sum_{a|r} a^2 mu(r/a)^2
              = 4r^2 product_{p|r}(1+p^{-2})
              <= 4 zeta(2)/zeta(4) r^2.                    (8)

This is a size bound, not the source-specific cancellation needed for RH.

## 5. SRL-5: exact solution of the dual approximation problem

Put V_N=span(d_2,...,d_N), and let x_N be k on [1,N], zero otherwise. All
vectors in V_N have support [1,N] and are orthogonal to x_N. Dimension and
triangularity show that

    V_N = {f: supp(f) subset [1,N], <f,x_N>=0}.              (9)

Define

    a_N = sum_{k<=N} 1/(k+1) = H_{N+1}-1,
    z_N = sum_{k<=N} k/(k+1) = N+1-H_{N+1}.

The orthogonal projection of 1 onto V_N is explicitly

    P_{V_N}1(k) = 1-a_N k/z_N     (1<=k<=N),
                 0              (k>N).

Therefore

    dist(1,V_N)^2 = 1/(N+1)+a_N^2/z_N
                  = 1-mu_N^T F_N^{-1}mu_N
                  ~ (log N)^2/N.                         (10)

The dual family {d_r:r>=2} is complete in H, unconditionally. Indeed, if
f is orthogonal to it, f(0)=0 and summation by parts give

    0=<f,d_r>=sum_{a|r} mu(r/a)[f(a)-f(a-1)]  (r>=2).

Mobius inversion says all differences f(a)-f(a-1) equal f(1). Thus f(k)=k f(1),
and H-membership forces f(1)=0. Alternatively (9) approximates every fixed
finitely supported vector, with squared correction cost O(1/N).

WARNING: the dual's unconditional completeness and the explicit convergence
in (10) do not establish the completeness of {b_n}. Biorthogonality alone
does not transfer completeness. F_N is not the original Gram matrix G_N.

## 6. SRL-6: exact three-part decomposition of the actual error

Let c=(c_2,...,c_N)^T, mu_N=(mu(2),...,mu(N))^T, and define

    t_{N,n}=sum_{k<=N} b_n(k)/(k+1),
    A_c=sum_{n=2}^N c_n b_n.

The mutually orthogonal spaces V_N, span(x_N), and the sequences supported
on k>N decompose H. By (2), the V_N coordinates of 1-A_c are mu_N+c.
The ramp scalar product is a_N-t_N^T c. Pythagoras gives

    ||1-A_c||^2
       = (c+mu_N)^T F_N^{-1}(c+mu_N)
         + (a_N-t_N^T c)^2/z_N
         + sum_{k>N} (1-A_c(k))^2/[k(k+1)].                 (11)

Every term is nonnegative, and the infinite tail is retained exactly.
The first term measures coefficient mismatch in the correct dual metric;
the second is a single ramp mode; the third is the actual continuation past
N. Neither (10) nor a favorable first term estimates the other terms.

The same decomposition applied to the b_n themselves gives

    G_N = F_N^{-1} + t_N t_N^T/z_N + T_N,                  (12)
    T_N(m,n)=sum_{k>N} b_m(k)b_n(k)/[k(k+1)].

T_N is positive semidefinite because it is a Gram matrix. All quantities in
F_N^{-1} and t_N are rational. The transcendental logarithms in the full
source v arise only after the infinite arithmetic sums are completed.

There is also a projection formula for the inverse dual Gram, avoiding its
numerical inversion:

    (F_N^{-1})_{mn}
       = sum_{k<=N} b_m(k)b_n(k)/[k(k+1)] - t_{N,m}t_{N,n}/z_N.            (13)

This follows because <b_m,d_r>=-delta_{mr}, so the Gram matrix of the
V_N-projections of the b_n is F_N^{-1}. Equations (11)--(13) are universal
finite-dimensional identities, not estimates inferred from sampled N.

### Exact interpolation is not the construction of an RH mollifier

If P_{V_N} A_c=P_{V_N}1, (2) forces c=-mu_N, uniquely. On k<=N the elementary
identity sum_{n<=k} mu(n)floor(k/n)=1 then gives

    1-A_{-mu_N}(k)=k m_N,
    m_N=sum_{n<=N}mu(n)/n.

Thus exact dual matching yields

    ||1-A_{-mu_N}||^2 = z_N m_N^2 + its genuine k>N tail.                 (14)

We have not proved that either term tends to zero. Even pointwise
coefficient convergence to -mu does not justify a norm limit.

## 7. SRL-7: a uniform trace bound for the actual Gram correction

Let R_N=G_N-F_N^{-1}. Then R_N is positive semidefinite and

    trace R_N < 11                           for every N>=2.             (15)

Proof. First z_N>=N/2. Splitting t_{N,n} into k<n and k>=n, using b_n(n)=0,
gives

    0<=t_{N,n}<=1+log(N/n).

The decreasing integrable function f(x)=(1-log x)^2 satisfies
integral_0^1 f(x) dx=5. Comparison with right-endpoint sums yields

    sum_{n=2}^N t_{N,n}^2 <= 5N,
    trace(t_Nt_N^T/z_N)<=10.

Finally 0<=b_n(k)<1 and the weights telescope, so

    trace T_N <= (N-1)sum_{k>N}1/[k(k+1)]
               =(N-1)/(N+1)<1.

This proves (15). It is an unconditional bound in the ACTUAL weighted
geometry, not the periodic GCD geometry.

Its inverse consequence has the direction

    G_N^{-1} <= F_N                          (Loewner order),            (16)

an upper bound, not the lower estimate on v^T G_N^{-1}v needed for RH.
A bounded trace perturbation need not be negligible relative to a small
eigenvalue: even [epsilon]+[1] illustrates that. Nor does (15) control its
quadratic form on growing, signed Mobius coefficient vectors. We do not
promote the uniform trace bound into an all-scale source bound.

## 8. SRL-8: identify the logarithmic mollifier's first positive component

For N>=2 use the prescribed real coefficients

    c_n=-mu(n)(1-log n/log N),  2<=n<=N,
    tau_N=sum_{n<=N}mu(n)(1-log n/log N)/n,
    psi(k)=sum_{m<=k}Lambda(m).

For k<=N, elementary divisor inversion gives

    1-A_c(k)=k tau_N-psi(k)/log N.

Projection onto V_N removes every multiple of the ramp k. Consequently
the first term in (11) is exactly

    (c+mu_N)^T F_N^{-1}(c+mu_N)
       = 1/(log N)^2 * [
           sum_{k<=N} psi(k)^2/[k(k+1)]
           - (sum_{k<=N}psi(k)/(k+1))^2/z_N ].              (17)

Equivalently it is 1/(log N)^2 times

    V_N^psi = min_{a in R} sum_{k<=N}(psi(k)-a k)^2/[k(k+1)].              (18)

Do not confuse this scalar V_N^psi with the subspace V_N. The normalization
here has tau_N=T_N/log N in the preceding conversation's mollifier notation.
The new Gram tail matrix T_N in (12) is a different object; tau_N avoids a
scalar/matrix notation collision in this packet.

Thus the exact positivity found above already contains a weighted prime
counting variance. Positive semidefiniteness establishes its nonnegativity,
not a small upper bound.

### A target-location lemma (a classical type of mean-square RH criterion)

If 0<=alpha<1/2 and V_N^psi=O(N^{2alpha}), then zeta has no zero with
Re(s)>1/2+alpha. In particular, subpolynomial growth of V_N^psi would suffice
for RH. No such bound is proved here.

Proof. Let a_j minimize (18) at N=2^j. Comparing the two residuals on the
smaller prefix and using z_N>=N/2 gives

    |a_{j+1}-a_j| = O(2^{j(alpha-1/2)}).

Thus a_j converges to a_infinity, with error O(2^{j(alpha-1/2)}). It follows
that the weighted squared error of psi(k)-a_infinity*k through N is O(N^{2alpha});
first at dyadic N, then at all N by monotonicity of the fixed-slope sum.
Cauchy--Schwarz on dyadic intervals now proves absolute, locally uniform
convergence of

    integral_1^infinity [psi(x)-a_infinity*x] x^{-s-1} dx

when Re(s)>1/2+alpha. Replacing integer k by real x changes the error by a
bounded function and the discrete/continuous weights are exactly matched
by integrating x^{-2} over [k,k+1). For Re(s)>1 the integral equals

    -zeta'(s)/(s zeta(s)) - a_infinity/(s-1).

Holomorphy through s=1 forces a_infinity=1 by the simple zeta pole. A zeta
zero rho in the claimed half-plane would give a nonremovable pole with
residue -m_rho/rho, a contradiction. The critical line itself is not in
this open half-plane; multiplicities are retained.

This lemma locates the unresolved arithmetic in the FIRST component of
(11). It is not evidence that the estimate has become easier, and it is not
an assertion of a new RH criterion. For the previous subpolynomial Q_N
route, all three positive components still have to be estimated; this
lemma separately shows that an appropriate first-component bound alone
would already rule out right-side zeros.

## 9. Exact remaining obligation and review priorities

The proposed unconditional support and Gram results do not establish
E_N->0, the prime-source Schur inverse-energy divergence, or subpolynomial
growth of the prescribed mollifier norm. The remaining assertion is a
source-specific UPPER bound, not positivity of one of these matrices.

One sufficient construction would give cofinal c_N with all three terms
in (11) tending to zero. For the prescribed logarithmic coefficients, a
subpolynomial norm estimate would suffice by the preceding length-averaging
argument; that argument is not used to prove any theorem in Sections 1--7.
Equation (17) identifies a classical-strength prime-counting obstacle
already inside its finite head. No proof of the required upper bound is
supplied by omitting the tail, the rank-one ramp, the composite Schur
correction, or the adjacent-divisor terms in (7).

Review order: the sign in (1); the distinction between b-support and
s-support in (3)--(6); the adjacent-divisor formula (7); the finite subspace
identity (9); Pythagoras (11)--(13); the source-uniform but not
source-small trace estimate (15); finally the target-location lemma.

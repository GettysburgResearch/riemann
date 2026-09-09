# Near-square-root compression of the complete arithmetic residual operator

Date: 2026-09-09. Author research continuation of PR #803.
Parent: `db175de165a9077e709b1cb482998171ffc0c6e7`.
Status: PROPOSED COMPONENT THEOREMS; independent mathematical/code review required.
**RH, the native subpower residual estimate, and the sparse-failure bound remain unproved.**
Labels SC1--SC4 are local, not canonical acceptance identifiers.

## 0. The attempted finish and the actual advance

The preceding paper proves that the full divisor-graph-to-physical-norm map can lose a factor of order Y/log Y. A fixed number of safe jets does not remove that loss. We asked whether the costly directions fill a positive fraction of the coefficient space. They do not.

Here the COMPLETE physical residual operator has squared singular values bounded by

    lambda_(r+1) <= C_A Y log(r+2)/(r+1)^2.

Consequently at most O_A(sqrt(Y) log^2 Y) directions are needed to leave a coefficient-to-physical squared norm O_A(1/log^3 Y). This is an unconditional all-scale result. In a logarithmic coefficient budget the corresponding affine residual minima differ in SQUARE ROOT by O(1/log Y). Exact prefix and jet constraints survive.

The key is to estimate the entire high-frequency remainder in Hilbert--Schmidt norm, and only then remove its large singular directions. A pointwise zeta bound is unnecessary. The classical second moment, reconstructed below from the approximate functional equation, is enough. This is stronger than the first route we tried, which used Bourgain's pointwise bound and K=Y^(3/5) to control only a prescribed critical-jet nullspace. That preliminary pointwise argument is not a dependency of the present packet.

A second construction uses the earlier uniform RATIONAL physical form. Thus the selected directions can be defined by a finite matrix made from integer floor/divisor data, rather than from unknown zeta zeros or an infinite numerical integral. Constants in the asymptotic singular-value estimate are not numerically instantiated. Finite matrix eigenvalues can instead provide a posteriori error bounds.

**The retained smaller arithmetic minimum is not estimated here.** This is a positive norm-compression theorem, not an unconditional RH proof or a claim that the remaining estimate is routine. Classical Taylor approximation, mean values, singular-value approximation and projection are credited; no external priority claim is made.

## 1. The original source and its metric

Fix a real constant A>=4, integers Y>=2 and Y<=N<=AY, and the tail I={Y,...,N}. Let

    <c,d>_S=sum_(n in I) conjugate(c_n)d_n/n,
    S(c)=sum |c_n|^2/n.

Let V be ANY linear subspace of C^I on which

    sum_(n in I)c_n/n=0.                                   (1)

A real space is used in real optimization. Homogeneous derivative or centering constraints may additionally be imposed. Coefficients at every integer index are permitted, with zero values outside I.

Define the physical map and its squared norm by

    (T c)(x)=sum_(n in I)c_n floor(x/n),
    R(c)=||T c||_H^2,
    H=L2([1,infinity),dx/x^2).                              (2)

Balance gives T c=-sum c_n {x/n}; this is bounded and is zero for x<Y. In particular

    R(c)<=Y^(-1)(sum |c_n|)^2<=N(N+1)S(c)/(2Y).             (3)

Initially for Re s>1, integrating the finite floor sum yields

    integral_1^infinity T c(x)x^(-s-1)dx=zeta(s)q_c(s)/s,
    q_c(s)=sum_(n in I)c_n n^(-s).                         (4)

The left side extends analytically to Re s>0 by boundedness, while the pole at 1 on the right is removed by (1). The identity theorem extends (4). Applying Fourier Plancherel to exp(-t/2)T c(exp t), zero-extended for t<0, gives exactly

    R(c)=(1/(2pi)) integral_R
       |zeta(1/2+it)q_c(1/2+it)|^2/(1/4+t^2)dt.           (5)

No frequency or prime-power tail is discarded. Zeta is in the numerator. Formula (5) is a homogeneous variation norm, not the affine target E(p)=||1-Tp||^2.

Let d=dim V. Write lambda_1>=...>=lambda_d>=0 for the eigenvalues of T* T with the adjoint in the S metric. Set lambda_j=0 for j>d. These are squared singular values, not zero ordinates. No assertion identifying this spectrum with the zeros of xi is made.

## 2. The classical input and the full zeta-weight tail

We use the ordinary approximate functional equation on the critical line, as recorded in DLMF 25.9.3 [E1]: with m(t)=floor(sqrt(t/(2pi))),

    zeta(1/2+it)=sum_(n<=m(t)) n^(-1/2-it)
        +chi(1/2+it)sum_(n<=m(t)) n^(-1/2+it)+O(t^(-1/4)), (6)

for large positive t. Here |chi(1/2+it)|=1, directly from DLMF 25.9.2. This is an IMPORTED classical analytic identity; its proof and a numerical remainder constant are not supplied by the finite checker. All uses below are unconditional.

For clarity the needed mean-square consequence is reconstructed, including the moving cutoff. Let U be large, M=floor(sqrt(U/pi)), and consider U<=t<=2U. Expanding the first sum's squared modulus gives pairs n,k<=M. A pair is present only for

    max(U,2pi n^2,2pi k^2)<=t<=2U.

Thus its integration domain is one interval or empty. The diagonal is at most U sum_(n<=M)1/n. Each unordered cross pair costs at most

    4/(sqrt(nk)|log(k/n)|).

Since log(k/n)>=(k-n)/M for k>n, the harmonic-row estimate using 2|uv|<=|u|^2+|v|^2 bounds the entire off-diagonal by 4M(1+log M)sum_(n<=M)1/n. Hence that mean square is O(U log(2U)); M=O(sqrt U). The conjugate sum in (6) has the same estimate. The unit-modulus chi factor does not change its norm. Applying |a+b+c|^2<=3(|a|^2+|b|^2+|c|^2) pays the integrated remainder O(sqrt U). Increasing the constant on a compact initial interval proves

    integral_U^(2U)|zeta(1/2+it)|^2dt <= C U log(2U), U>=1. (7)

Complex conjugation gives the same bound on negative heights. Divide each dyadic block beyond T>=1 by its squared lower height and sum. The geometric series with the extra logarithmic factor converge, giving

    Ztail(T):=(1/(2pi)) integral_(|t|>T)
          |zeta(1/2+it)|^2/(1/4+t^2)dt
          <= C log(2T)/T.                                (8)

Also Z0:=Ztail(0)<infinity, where the bounded interval is integrated directly by continuity. None of (6)--(8) is an estimate for reciprocal zeta, a shifted zero-free region, or a conditional RH mean square. In particular the RH-conditional Cramer estimate for prime error used elsewhere in the repository is NOT being imported here.

## 3. SC1: trace-tail compression and the squared singular-value bound

The following theorem holds uniformly over V, Y, N with A fixed:

    sum_(j>K)lambda_j <= C_A Y log(K+2)/(K+1), K>=1,       (9)
    lambda_(r+1) <= C_A Y log(r+2)/(r+1)^2, r>=0.         (10)

Constants are finite and independent of coefficients and rank. The operator still need not have a small largest singular value. Its entire high-energy spectrum is being quantified, not declared absent.

### 3.1 A rank-K auxiliary map

Use normalized coefficient coordinates b_n=c_n/sqrt(n), so S=sum |b_n|^2. Put l_n=log(n/Y), with 0<=l_n<=log A, and L_A=max(1,log A). The frequency map corresponding to (5), on the larger full coefficient space C^I, is

    F b(t)=zeta(1/2+it)/[sqrt(2pi)(1/2+it)]
                                 sum_(n in I)b_n exp(-it log n).

It is well-defined even for unbalanced b since Z0 is finite. Only its restriction to the balanced space is identified with the physical map in (5).

For K>=12L_A put T_K=K/(12L_A). On |t|<=T_K replace exp(-it l_n) by its Taylor polynomial of degree K-1, and on |t|>T_K set the approximation to zero. Include the common phase Y^(-it). This defines an operator F_K of rank at most K: its coefficients are the K moments sum b_n l_n^j.

For REAL v, the integral Taylor remainder satisfies

    |exp(-iv)-sum_(j=0)^(K-1)(-iv)^j/j!|<=|v|^K/K!.

The remainder's exponential has modulus one. Since K!>=(K/e)^K and e<3, for |t|<=T_K the columnwise error is at most 4^(-K) times the common zeta weight. There is no factor exp(|t|log A).

There are D=N-Y+1 columns of unit coefficient norm. Sum their squared errors, using (8) for all omitted frequencies:

    ||F-F_K||_HS^2
       <=D[16^(-K)Z0+Ztail(T_K)]
       <=C_A Y log(K+2)/(K+1).                           (11)

HS is the Hilbert--Schmidt norm. For 1<=K<12L_A the trivial bound ||F||_HS^2=D Z0 proves the same estimate after enlarging C_A. Restriction to V cannot increase this norm.

The auxiliary Taylor map need not be causal or belong to the actual arithmetic range. It is used ONLY to bound approximation numbers of F in its ambient frequency Hilbert space. The final compressed physical maps below are T composed with coefficient projections and do remain actual source outputs. Alternatively, projecting F_K orthogonally onto the frequency image of H cannot increase its rank or error, so the same approximation bound is valid with the original physical codomain.

### 3.2 Passing from trace to operator norm

The finite-dimensional singular-value principle gives

    sum_(j>K)lambda_j <= inf_(rank R<=K)||T-R||_HS^2.

Equality holds for the truncated singular-value decomposition, but only the inequality is needed. One direct proof projects onto the range of R; the orthogonal remainder of T is no larger than T-R in Hilbert--Schmidt norm, and the rank-K trace maximum is the sum of the K largest eigenvalues. Apply (11) to obtain (9).

For r>=2 take K=floor(r/2). There are r+1-K terms from K+1 through r+1, all at least lambda_(r+1). Thus

    (r+1-K)lambda_(r+1)
       <=sum_(j>K)lambda_j
       <=C_A Y log(K+2)/(K+1).

This proves (10) with a changed absolute factor. The two remaining ranks follow from (3). Singular values beyond d are zero. There is no claim that (10) is a sharp asymptotic or an explicit numerical certificate at a given Y.

### 3.3 A prescribed near-square-root rank

Let h_Y be the least integer with 2Y<=2^h_Y and set

    R_Y=min(d, ceil(sqrt Y) h_Y^2).                       (12)

Let Pi_Y be an S-orthogonal projection onto R_Y leading right singular vectors. Any choice within an eigenvalue tie is allowed. By (10),

    ||T(I-Pi_Y)||_(S->H)^2 <= C_A/[log(2Y)]^3.           (13)

If R_Y=d the left side is zero. Otherwise R_Y is comparable to sqrt(Y)log^2(2Y), and log(R_Y+2)=O(log(2Y)), proving the bound. In particular R_Y=o(Y) when dim V has order Y. The result need not be nontrivial at small Y.

For the power choice R=ceil(Y^(1/2+epsilon)), any FIXED 0<epsilon<1/2 gives instead

    ||T(I-Pi_R)||^2 <= C_(A,epsilon)Y^(-2epsilon)log(2Y).

These statements concern the original coefficient and physical metrics. They are absolute operator-error estimates; they are not relative errors on vectors whose physical norms may already be tiny.

## 4. SC2: choose the directions using a finite arithmetic matrix

A definition through singular vectors of the full norm could conceal an infinite computation. The uniform rational capture theorem on PR #803 supplies a finite replacement. We recall the exact form and its justification, because uniformity BEFORE optimization matters.

For balanced c of support <=N, including zeros outside I, let

    C_N=N^2(1+2ceil(log2 N)),
    V(c)=|(1/2)sum c_n|^2
          +(1/12)sum_(d<=N)J_2(d)|sum_(d|n)c_n/n|^2,
    Q_H(c)=sum_(j=1)^(H-1)|sum c_n floor(j/n)|^2/[j(j+1)],
    Rhat_H(c)=Q_H(c)+V(c)/H.                             (14)

J_2 is the second Jordan totient. These forms have rational matrix entries. The COMPLETE full norm satisfies

    |Rhat_H(c)-R(c)| <= eta_H R(c),
    eta_H=4C_N^2/[H(H+1)].                              (15)

At H=2C_N ceil(sqrt N), eta_H<1/N<1.

Here are the ingredients of (15). Balance makes the floor combination periodic and its period mean square equals V. Finite CRT gives the fractional-part covariance (gcd(m,n)^2-1)/(12mn); balance cancels the subtracted rank-one term, and sum_(d|k)J_2(d)=k^2 gives V. Its Fourier frequencies have denominators <=N. Combine equal frequencies. Distinct ones have circular separation at least 1/N^2. Geometric sums and harmonic rows give, for EVERY integer interval J,

    |sum_(j in J)|T c(j)|^2-|J|V|<=C_N V.

Abel summation against 1/[j(j+1)] now gives the complete tail error

    |R-Rhat_H|<=C_N V/[H(H+1)].

Apply its lower side at H0=2C_N to obtain R>=V/(4C_N). Substitution yields (15). These are the earlier RC form estimates, reconstructed at their mathematical scope; the earlier producer or numerical minima are not replayed here.

Restrict Rhat_H to V and let Bhat be its self-adjoint matrix in the S metric. Let widehat Pi_R project onto R leading eigenvectors of Bhat. Equation (15) and the min-max principle give

    ||T(I-widehat Pi_R)||^2
       <= lambda_(R+1)(Bhat)/(1-eta_H)
       <=[(1+eta_H)/(1-eta_H)]lambda_(R+1)(T*T).         (16)

Thus (13) holds with widehat Pi_(R_Y) as well. The first bound in (16) is an a posteriori finite-eigenvalue certificate; it does not require a numerical value of C_A.

No zeta zero or analytic spectral parameter defines Bhat. Its floor/divisor matrix is finite and rational, and H is a predetermined polynomial-size horizon. If V includes the condition sum c_n log n/n=0, that constraint has exact logarithmic entries and is NOT called rational. The construction remains source-defined, but we claim neither a stable monomial-jet implementation nor a bit-complexity bound for exact/eigenvalue-certified computation. No large-rank projector has been computed in this packet.

## 5. SC3: the sharp graph-transfer loss has few independent modes

Retain the full original prime-power graph, including zero vertices below Y:

    G_N(c)=sum_(p prime,k>=1,p^k j<=N)
                    (log p)/(p^k j)|c_(p^k j)-c_j|^2.    (17)

For each child n in I, keep only downward edges with parent n/p^k<Y. Their contribution is log p |c_n|^2/n. Every downward edge together has logarithmic weight log n. The discarded parents have p^k<=n/Y<=A, hence their total weight is at most psi(A)=sum_(p^k<=A)log p. All other squares are nonnegative, so

    G_N(c)>=[log Y-psi(A)]S(c).                         (18)

This is the exact fixed-ratio bound from the parent, with its short elementary proof. Every prime power and lower endpoint is retained. For log Y>psi(A), the generalized eigenvalues nu_j of the pair (R,G_N) on V consequently obey

    nu_(r+1)<= C_A Y log(r+2)/[(r+1)^2(log Y-psi(A))].   (19)

Use (10) and min-max, or apply (18) on the S-spectral complement. At the rank (12), for large Y,

    nu_(R_Y+1)<=C_A/[log(2Y)]^4.                        (20)

This strengthens the qualitative meaning of the parent obstruction. Its worst-case ratio of order Y/logY remains possible; the number of independent eigenmodes above the threshold in (20) is at most O_A(sqrt(Y)log^2 Y). Arbitrary vectors with a large ratio can have components in both summands. We do not assert that every such vector lies literally in the chosen coefficient eigenspace.

The graph's harmonic zero mode does not disappear by changing metrics. In these tails it is excluded because all lower coefficients, including c_1, are zero; the original balance and optional derivative/centering constraints remain in V. This argument supplies neither positivity of the full Weil form nor a smallness bound for the retained channel.

## 6. SC4: a full affine optimization in a smaller source-preserving space

Let A_(Y,N) be the real affine class with

    p_n=mu(n) for n<Y, p(1)=0, p'(1)=1,
    support(p) subset [1,N].                            (21)

Additional consistent real affine conditions may be imposed. Let V be its tangent space. Denote by p_* the unique minimizer of the weighted COEFFICIENT norm S(p)=sum |p_n|^2/n in this affine class. This is not the unknown physical minimizer. Projection in a finite-dimensional positive metric gives p_* perpendicular to V and

    S(p_*+v)=S(p_*)+S(v), v in V.                       (22)

For B0^2>=S(p_*), let A_B={p in A_(Y,N):S(p)<=B0^2}. This is compact and nonempty. Define

    C_R(p)=p_*+widehat Pi_R(p-p_*).                      (23)

It preserves the entire actual prefix, both safe constraints, every additional affine constraint, and the coefficient budget. Its images lie in the affine space p_*+Ran(widehat Pi_R) of dimension at most R.

For full polynomials p, Tp denotes the same floor formula summed over 1,...,N; differences of admissible polynomials lie in the tail space V. Let e_B=min_(A_B)E(p), E(p)=||1-Tp||^2, and let e_B,R be the same minimum restricted to that affine subspace. Both minima are attained. Compress a minimizer of e_B. Its discarded tangent has S at most B0^2. The reverse triangle inequality applied to the COMPLETE physical residuals and (16) proves

    0<=sqrt(e_B,R)-sqrt(e_B)
      <=B0 sqrt[lambda_(R+1)(Bhat)/(1-eta_H)].           (24)

At B0^2=B(1+log Y), with B fixed, (12)--(13) give

    0<=sqrt(e_B,R_Y)-sqrt(e_B)<=C_(A,B)/log(2Y)->0.       (25)

Every physical cross term is preserved: the argument bounds the norm of the discarded vector, not a diagonal approximation to its energy. This is an asymptotically exact compression of THAT coefficient-budgeted problem. It is not an identification with an unrestricted physical minimum unless its coefficient budget is separately proved.

### 6.1 The native coefficient-budget class is nonempty

For N=4Y one explicit family is the earlier BMC completion. Put

    M=sum_(n<Y)mu(n)/n, L=sum_(n<Y)mu(n)log n/n,
    ell=Y^(-1)sum_(Y<=n<2Y)log n,
    q(s)=Y^(-1)sum_(Y<=n<2Y)n^(1-s),
    b=(M ell-L-1)/log2, a=-M-b,
    p0(s)=sum_(n<Y)mu(n)n^(-s)+q(s)[a+b2^(1-s)].         (26)

Direct substitution proves the two safe jets and the exact prefix. The elementary divisor identities give |M|<=1 and

    sum_(n<=x)mu(n)H_floor(x/n)/n=1.

The bound H_floor(v)=log v+gamma_E+epsilon(v), |epsilon(v)|<=1/v, implies |sum_(n<=Y)mu(n)log(Y/n)/n-1|<2. To check the harmonic bound, use 1/[2(m+1)]<H_m-logm-gamma_E<1/(2m) and m<=v<m+1. Its upper side follows from v<2m for m>=1. For m>=2 the lower side follows from log(1+1/m)<=1/m<=3/[2(m+1)]; m=1 follows from log2<3/4. The familiar harmonic inequalities follow by summing the integral of (1-t)/[(k+t)(k+1)] on 0<=t<=1. Thus the noninteger endpoints do not hide a stronger remainder assumption.

Consequently |b|<5, |a|<6. The two disjoint correction blocks contribute exactly

    [(3Y-1)/(2Y)](a^2+2b^2)<129

to S. The prefix contributes at most 1+logY. Hence S(p0)<130+logY. In particular B=130 is admissible in (25) for every Y>=2. Neither RH nor PNT is needed for this nonemptiness.

## 7. Attempted end-to-end finish: what is and is not established

The attempted next step was to bound the retained affine minimum using its stationarity equations. Equations (24)--(25) show that most tangent directions are unnecessary at the stated coefficient budget; they do not bound the distance of the remaining affine target from the retained range. In particular the following statement remains OPEN:

    e_B,R_Y(Y)=Y^o(1) on an unbounded sequence of integers Y,
    N=4Y, B0^2=130(1+logY).                             OPEN

This is not concealed in an asymptotic constant or assigned to a referee as routine verification. No numerical or analytic bound proving OPEN is supplied. The smaller space contains the potentially costly modes rather than proving their cost zero. A positive finite Hessian, a stationary solve, or O(sqrt(Y)log^2Y) variables does not by itself establish a subpower minimum.

For completeness the full conditional consumer is short. If p retains the prefix and p(1)=0, r_p(t)=exp(-t/2)[1-Tp(exp t)] is zero before logY, has squared L2 norm E(p), and has Laplace transform

    [1-zeta(z+1/2)p(z+1/2)]/(z+1/2).

At a hypothetical nontrivial zero rho=beta+i gamma with beta>1/2 its value at z=rho-1/2 is 1/rho. Cauchy--Schwarz on the actual delayed support yields

    E(p)>=(2beta-1)Y^(2beta-1)/|rho|^2.                  (27)

An unbounded subpower sequence in OPEN would contradict (27) for every such zero. Reflection handles the left side. No rightmost zero, simple-zero hypothesis, inverse-zeta-derivative bound or zero table is used. This proves the implication from OPEN to RH, not OPEN itself.

The current all-Y classical Mertens-scale upper bounds remain compatible with (27). The new compression is a positive all-scale component; it is not a claimed unconditional RH proposal. No new numerical minimum, positive window or zero-free region is supplied.

## 8. Sources, proof status and execution boundaries

[E1] NIST DLMF 25.9.1--25.9.3, particularly the critical-line approximate functional equation 25.9.3, which cites Titchmarsh (1986), equation (4.17.1), p.88. Exact online source: https://dlmf.nist.gov/25.9 . The displayed equation and domain were read. Its analytic proof is imported, not machine-verified by this packet.

The parent ANT source is PR803 at db175de165a9077e709b1cb482998171ffc0c6e7, standalone/2026-09-08-arithmetic-norm-transfer/PROOF.md. RC's uniform rational capture is at 31a35a90b0b924dc98a2c89c463fb59577f45a4e, standalone/2026-09-08-rational-residual-capture/PROOF.md. BMC's bounded completion is at ed074bcabfd2c1ca3336e457b8fdd09a25bcd2a7, standalone/2026-09-06-logarithmic-core/balanced-mobius-contour/PROOF.md. Their needed identities are reconstructed above. No parent executable or historical campaign is claimed as newly replayed.

The current four-pass review and integration candidate supplied orientation only. Their source selections do not approve this new composition automatically. Classical Fourier Plancherel, analytic continuation and functional symmetry of zeta, finite-dimensional spectral projection and trace/min-max identities are the other mathematical inputs.

The finite checker covers projection/constraint algebra on actual geometric integer nodes, exact Taylor and rank budgets, bounded source/Mobius/prime-power identities, and small complete period-mean identities. It does NOT evaluate a zeta norm, prove the approximate functional equation, certify a new finite minimum, or verify OPEN by testing. The source-derived rational spectral projector is a mathematical construction, not an executed high-rank solver. Independent review of the analytic arguments remains required.

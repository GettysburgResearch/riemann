# Route 1: unweighted spectral multiplicities can be postponed to the limit

Status: PROPOSED COMPLETE PROOFS, with a source-only finite interval certificate; independent mathematical review required. RH is not proved.
Scope: one global log-moment Hankel stream; an actual three-node positive resolvent quadrature. This is a moment-theory refinement of the determinant programme, not a new claimed classical RH criterion.
Sources: PR #793/pass2 compactness and finite completions; PR #785 Stieltjes endpoint; PR #790 heat/moment programme. This note changes the expansion center to invariant coordinate 2 (s=2). The preceding ranks 15 and 32 concern a DIFFERENT center and remain unchanged.

## M1. Fixed arithmetic definition

Let

    f(u)=xi((1+sqrt(9+4u))/2)/xi(2),
    q(u)=f'(u)/f(u)=sum_(j>=0) (-1)^j p_(j+1) u^j.

The functional equation makes f entire, real on the real axis and normalized by f(0)=1. It is positive for u>=0. Its theta representation, or Stirling on s>=2, gives log f(x)=O(sqrt(x)log(x+2))=o(x). The germ q is analytic on some disk about zero. Consequently |p_(j+1)|<=C_R R^j for some finite R,C_R. No zero location is used to DEFINE any p_j: derivatives at the absolutely convergent s=2 source determine them.

For every N>=0 put H_N=[p_(i+j+1)]_(0<=i,j<=N).

## M2. Single-Hankel completion theorem

**Theorem.** For this actual f, the following are equivalent:

1. H_N is positive semidefinite for every N.
2. f(u)=det(I+uK) for some positive trace-class K.
3. RH.

In particular, no shifted Hankel positivity, integer weights at finite stages, common finite rank, or compatibility between finite matrices is an additional premise of (1). This does not prove (1). It is a cheaper constructive target, not a new arithmetic upper bound.

### Proof from positivity to a positive measure

Set m_j=p_(j+1) and define ell(x^j)=m_j on real polynomials. The hypotheses say ell(P^2)>=0. Quotient polynomials by the null space of the resulting seminorm. Multiplication X:P->xP is well-defined and symmetric: a null P is orthogonal to every polynomial by Cauchy--Schwarz, hence xP is orthogonal to every Q since ell(xPQ)=ell(P xQ).

For each fixed P, the exponential moment bound gives ||X^kP||<=C_P R^k. Symmetry and repeated Cauchy--Schwarz imply

    ||XP|| <= ||P||^(1-2^-n) ||X^(2^n)P||^(2^-n).

Let n tend to infinity to obtain ||XP||<=R||P||. Thus X extends to a bounded self-adjoint operator on the completion. Its scalar spectral measure at the constant polynomial is a finite positive measure nu on [-R,R], with moments m_j. Equivalently, one may invoke the classical compact Hamburger moment theorem.

For |u| sufficiently small,

    q(u)=integral dnu(t)/(1+ut).

This equality starts as an absolutely convergent series identity; it is not a postulated spectral realization of zeta zeros.

### Why the shifted positivity constraints follow, rather than being assumed

Let C(z)=integral dnu(t)/(z-t). For nonreal z near infinity, C(z)=q(-1/z)/z. If q is analytic and real on a real u interval not containing zero, the right-hand expression extends across its reciprocal real z interval with real values. The elementary Stieltjes inversion formula then gives zero nu mass on that interval. Indeed -Im C(x+i epsilon) is the Poisson integral of nu; integrate over a compact subinterval and let epsilon decrease to zero.

Since f has no zeros for u>=0, q is analytic on that axis. It follows that nu has no support at t<0. Thus every shifted Hankel [m_(i+j+1)] is automatically positive semidefinite. This argument uses the actual positive-axis zero-freeness, not a generic claim that unshifted positivity implies Stieltjes positivity.

Away from t=0, the same inversion argument says nu is supported only at positive t=lambda for which f(-1/lambda)=0. These locations are discrete on every compact set avoiding zero, because f is nonzero entire. Therefore

    nu=gamma delta_0 + sum_lambda w_lambda delta_lambda,
    gamma>=0, w_lambda>0.

At u=-1/lambda, the residue of its contribution to q is w_lambda/lambda. But q=f'/f, so that residue equals the positive integer zero multiplicity d_lambda. Hence

    w_lambda=d_lambda lambda,
    gamma+sum d_lambda lambda=p_1<infinity.

Integrating q from 0 along the positive axis gives

    f(u)=exp(gamma u) product_lambda (1+u lambda)^d_lambda.

The positive-axis o(u) growth forces gamma=0, exactly as in pass2. The diagonal operator listing each lambda d_lambda times is positive trace class and gives (2). Multiplicity integrality is a CONSEQUENCE of the meromorphic logarithmic derivative at the limit; it is not required of finite quadrature weights.

Finally a nontrivial zero rho corresponds to u=rho(rho-1)-2. If this is real, its imaginary part (2Re rho-1)Im rho vanishes; nontrivial zeros are not real, so Re rho=1/2. Conversely RH and the genus-zero invariant product give (2), whose log moments make (1) Gram-positive. QED.

## M3. Three-node finite source realization

Suppose H=[m_(i+j)]_(0<=i,j<=2)>0 and Hplus=[m_(i+j+1)]_(0<=i,j<=2)>0. Give polynomials of degree at most two inner product ell(PQ). Define J by

    <P,JQ>=ell(xPQ).

This uses only m_0,...,m_5. Its matrix is H^-1 Hplus in the monomial basis, and it is positive self-adjoint in the H metric. It agrees with multiplication by x on degrees zero and one. In particular 1,J1,J^2 1 are the independent polynomials 1,x,x^2, so 1 is cyclic. J has three DISTINCT positive eigenvalues lambda_1,lambda_2,lambda_3, and weights w_j=|<1,e_j>|^2>0.

For 0<=k<=4, split k=i+j with i,j<=2 and use symmetry to get <1,J^k1>=ell(x^k). For k=5, use <J^2 1,J J^2 1>=ell(x^5), directly from the definition. Thus

    q_3(u)=<1,(I+uJ)^-1 1>=sum_(j=1)^3 w_j/(1+u lambda_j)
          =q(u)+O(u^6).

This is an actual positive three-node resolvent quadrature matching SIX log moments, equivalently the [2/3] local rational approximation. It is NOT a rank-three determinant matching six xi coefficients: w_j/lambda_j need not be integers. Calling it such a determinant would discard the very distinction M2 resolves only in the infinite limit.

## M4. Actual six moments: rational interval certificate

source_moments.py defines all constants at s=2 from absolutely convergent zeta data and Euler--Maclaurin. No zero data or floating-point arithmetic is used in acceptance. For log xi(2+h), the nonconstant Taylor series is the sum of

    log(2+h)+log(1+h) -(h/2)log pi
    +log Gamma(1+h/2)+log zeta(2+h),

with constants omitted. Use

    log Gamma(1+h/2)=-gamma h/2
             +sum_(j>=2) (-1)^j zeta(j) h^j/(j 2^j),
    u=3h+h^2, h(0)=0.

Compose the six-term series and multiply its jth coefficient by (-1)^(j-1)j. This gives p_j, not a zero-sum approximation.

The certified values begin

    p1=0.0230220771766668920750553064208...
    p2=0.0000365337419725877594967408121706...
    p3=0.000000139794304037969749716092302479...
    p4=6.34894815680191666528242331507...e-10
    p5=3.04089636025758951070422673471...e-12
    p6=1.48507139460311673799609996629...e-14.

MOMENTS.json retains interval endpoints, not just these displays. To improve conditioning without altering signs, the checker uses matrices

    Htilde_(ij)=200^(i+j)p_(i+j+1),
    HtildePlus_(ij)=200^(i+j+1)p_(i+j+2).

Their three leading principal minors are respectively about

    2.3022e-2, 7.5346e-5, 1.2871e-8;
    7.3067e-3, 5.8442e-6, 1.4428e-10.

All SIX lower interval endpoints are strictly positive. Sylvester's criterion and M3 construct the claimed actual three-node positive quadrature.

## M5. Complete error contract

The parent interval code is imported only after checking its literal SHA-256, 128df4f27cc62683a58ef74c1f374910db13b507208e00535df3e1c9a9b3c6e5. Its rational logarithm and Machin-arctangent intervals are reused without modifying the parent file.

For each integer s>=2, expand through order six the Euler--Maclaurin identity

    zeta(s+h)=sum_(n<N)n^(-s-h)+N^(1-s-h)/(s+h-1)
      +(1/2)N^(-s-h)
      +sum_(k=1)^M B_(2k)/(2k)! (s+h)_(2k-1)N^(-s-h-2k+1)
      +R_(s,M)(h).

Here N=256, M=12. On |h|<=r=1/4, the periodic-Bernoulli integral remainder obeys

    |R_(s,M)(h)| <= E_s
      = |B_(2M)| (s+r)_(2M) N^(1-s+r-2M)
         /[(2M)!(s-r+2M-1)].

This follows from |B_(2M)({x})|<=|B_(2M)|, bounding each rising factor by s+r+j, and integrating x^(-s+r-2M). Since N^(1/4)=4, E_s is rational. Cauchy's integral formula bounds the jth Taylor remainder by 4^j E_s. Every coefficient is widened by that amount. For gamma, use H_(N-1)-log N+1/(2N)+sum B_(2k)/(2k N^(2k)), with error at most |B_(2M)|/(2M N^(2M)). The parent log/atan tail and outward-rounding bounds remain in force.

The first attempted execution REFUSED certification: rounding an extremely small EM prefactor before multiplying a large rising polynomial made the enclosure unnecessarily wide. Exact rational prefactor multiplication before outward rounding repaired the width. No failed certificate was accepted, and no predecessor code was changed.

An independent 70-digit mpmath differentiation agrees with all six intervals. REGRESSION.json labels that run NON_DIRECTED_HIGH_PRECISION and explicitly excludes it from proof dependencies.

## M6. All-out closure attempt and its surviving difficulty

M2 removes finite-stage integrality and matrix compatibility, while M3 supplies an actual finite arithmetic example of the cheaper construction. The attempted continuation by positive theta mixing does not prove H_N>=0: log differentiation introduces connected/cumulant subtractions, and the marked positive-covariance obstruction from pass1 still applies. Neither the heat asymptotics of #790 outside their uniform regime nor the positive diagonal of #792 controls those subtractions.

The remaining theorem is exactly the all-order sign of THIS fixed source Hankel stream. Finite positive quadrature is not promoted to the unbounded result. Standard spectral, moment, Gaussian-quadrature and Padé facts are credited in REVIEW_AND_SOURCES.md.

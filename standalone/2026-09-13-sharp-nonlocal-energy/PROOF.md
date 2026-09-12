# Sharp nonlocal energy and a globally certifiable finite optimization

Date: 2026-09-13. Status: **PROPOSED COMPONENT PROOFS; independent mathematical review required.**
RH and the actual theta dimension-asymptotic estimate remain OPEN.

This is an add-only continuation of PR #881 at
`ab663f7d8020a62e1d8eedaf7d963d0eca3efe50`. It does not modify that packet,
main, the integration candidate, or any mathematical acceptance status.

The outcome has two parts. First, the previous sufficient similarity-energy
criterion is sharp: its infimum is exactly the complete squared spectral mass.
Quasinilpotent energy and Jordan chains impose no additional positive floor on
this infimum. Second, the exact finite-block problem is geodesically convex;
a specified regularization makes it coercive, uniquely solvable and supplies
a global residual certificate. Together these produce one source-defined
sequence of finite problems converging to `mu2 + 8 Delta_Xi`. The remaining
assertion is that this limit equals `mu2`, NOT an optimizer-convergence problem.

Compact triangularization, finite Schur theory, Hilbert-space projections and
positive-matrix geometry are classical. No priority is claimed for these general
mechanisms or the similarity-infimum formula. The proofs of the norm limit and
finite optimization used here are supplied, with the exact imported theorem named.

## 1. Literal source, notation and inherited boundary

Keep the complete theta source and operator of #881:

    phi(t)=sum_(n>=1)(4*pi^2*n^4*exp(9t/2)-6*pi*n^2*exp(5t/2))
                                    *exp(-pi*n^2*exp(2t)),
    w=phi/Xi(0), H=L2(R,w(t)dt), mu2=integral_R t^2 w(t)dt,
    C(t)=integral_(-infinity)^t w(x)dx, Q=1-C,
    (Kf)(x)=integral_R [1_(t<x)-Q(t)] f(t)dt.             (1)

The measure in K's integral is Lebesgue dt, not w(t)dt. The source is not
replaced by a finite theta sum. Its evenness, positivity and differentiated
double-exponential tails are the classical Jacobi source facts. The frozen
operator manuscript #834 at `f0e34780f4fe91bd5d07e791e8855189838c3df5`
(principal blob `ef01f74c50d4efacb615176cbfed4a3de2fd1147`) establishes

    Iw=||K||_HS^2=integral_R C(t)Q(t)/w(t)dt < infinity,
    Tr(K^2)=-mu2,                                       (2)

and nonzero eigenvalues lambda=-i/rho, with algebraic multiplicity equal to
the zero order of Xi at rho. These remain inherited PROPOSED operator
results, not newly accepted by this continuation. Neither a source zero
list nor RH is an input. No new numerical value for Iw is certified here.

The complete nonreal defect is

    Delta_Xi=(1/4) sum_(Xi(rho)=0) mult(rho)*(Im rho)^2/|rho|^4. (3)

Every individual zero occurs in (3). It equals one multiplicity-weighted
term per first-quadrant nonreal quartet. The functional equation and the
usual zero correspondence make Delta_Xi=0 equivalent to RH. The origin
is not a zero. No actual nonreal zero is asserted.

For Hilbert--Schmidt T write

    sigma2(T)=sum_(lambda!=0) mult(lambda)*|lambda|^2.     (4)

This is spectral squared mass, not the sum of singular values squared.
The latter is ||T||_HS^2 and can be strictly larger.

## 2. SNE1: sharp similarity infimum, including continuous nest directions

**Theorem.** On a separable complex Hilbert space, for every Hilbert--Schmidt T,

    inf_(S bounded invertible) ||STS^-1||_HS^2 = sigma2(T). (5)

No eigenvector completeness, diagonalizability, simple spectrum, uniformly
bounded condition number, or invertible limiting S is required.

### 2.1 Lower bound

For a finite collection of nonzero spectral values, the sum of their finite
algebraic root spaces is invariant. An orthonormal Schur basis on that finite
space gives the selected sum of |lambda|^2 as part of the complete squared
matrix-entry sum of STS^-1. Increase the finite selection. This proves
sigma2(T)<=||STS^-1||_HS^2 and also finiteness of (4).

### 2.2 The precise classical triangularization input

We import Ringrose's compact-operator triangularization theorem: a compact
operator on a complex Hilbert space has a complete maximal chain of invariant
closed subspaces, every nonzero successive quotient has dimension one, and
its nonzero diagonal coefficients list the nonzero eigenvalues with their
algebraic multiplicities. This is NOT an assertion of an orthonormal basis
of eigenvectors, nor even that the chain is purely atomic.

References: Ringrose, Proc. London Math. Soc. s3-12 (1962), 367--384;
Drnovsek--Kandic, arXiv:2212.10243v1, Section 3, printed page 4 (the compact
statement and attribution), and Theorem 3.8, printed page 8 (multiplicities).
The latter pages' parsed text was read. The browser PDF screenshot calls
failed; no successful visual-page inspection or full proof audit of Ringrose's
original article is claimed. Only this named classical theorem is imported.

Identify the chain with its orthogonal nest projections. For a finite partition

    0=P0<P1<...<Pm=I, Qi=Pi-P_(i-1),

invariance gives Qi T Qj=0 when i>j. Define the block pinching

    E_pi(T)=sum_i Qi T Qi.                              (6)

On the Hilbert space of Hilbert--Schmidt operators, E_pi is the orthogonal
projection onto the operators commuting with every partition projection.
Refining the partition decreases these closed subspaces. Consequently the
pinchings converge in HS norm to the projection onto their intersection.

For completeness, the decreasing-projection fact follows from Pythagoras:
for nested projection ranges, the squared distance between two projected
vectors equals the difference of their squared norms. The latter norms
have a limit. The resulting Cauchy net converges, its limit belongs to every
range, and its difference from the original vector is orthogonal to the
intersection. No finite-dimensional approximation error is hidden here.

### 2.3 Why the continuous diagonal contributes zero in HS norm

If a compact operator A commutes with every nest projection, so do A* and
|A|. Every nonzero eigenspace of |A| is finite-dimensional and reduces all
those projections. The commuting restrictions there have a common eigenbasis.
For a common eigenvector e, each nest projection either kills e or fixes e.
The supremum of projections killing e and the infimum fixing e determine a
nonzero atom of the complete nest containing e. Maximality makes that atom
one-dimensional. Thus every nonzero spectral vector of |A| lies in the
atomic part, and A vanishes on the continuous part.

On a rank-one atom Q_alpha, a commuting A is scalar. The HS projection of T
onto the intersection in 2.2 is therefore

    D=sum_alpha d_alpha Q_alpha,
    d_alpha=<T e_alpha,e_alpha>,
    ||D||_HS^2=sum_alpha |d_alpha|^2=sigma2(T).          (7)

The last equality is precisely the multiplicity part of Ringrose's theorem.
Hence ||E_pi(T)-D||_HS tends to zero under refinement. A Volterra-type
continuous component has not been dropped: its pinched HS mass tends to zero.

### 2.4 A bounded finite-partition similarity suppresses all other blocks

For 0<epsilon<1 use

    S_(pi,epsilon)=sum_(i=1)^m epsilon^(m-i) Qi.

This is bounded and boundedly invertible for EACH finite partition and positive
epsilon. Orthogonality of matrix blocks gives the COMPLETE identity

    ||S T S^-1||_HS^2
       =sum_i ||Qi T Qi||_HS^2
        +sum_(i<j) epsilon^(2(j-i)) ||Qi T Qj||_HS^2
       <=||E_pi(T)||_HS^2+epsilon^2||T||_HS^2.          (8)

Choose a finite partition so (7)'s squared norm is within delta/2 of sigma2,
and epsilon so the second term is below delta/2. This proves (5).
The condition number epsilon^(-(m-1)) may be arbitrarily large. The partition
in this existence argument depends on invariant subspaces of T and is NOT
a source-computable recipe already identifying the theta spectral subspaces.

### 2.5 The square trace and the exact theta value

For every finite nest partition, triangularity and the trace-class nature of
T^2 imply

    Tr(T^2)=Tr(E_pi(T)^2).

Indeed its diagonal blocks are (Qi T Qi)^2: every cross term would require
both an upper and a lower block, and the latter is zero. Taking the HS limit
in (7), trace continuity of products proves

    Tr(T^2)=sum_alpha d_alpha^2=sum_lambda mult(lambda)*lambda^2. (9)

Thus no unexplained square-trace interchange is needed. For actual K, (2),(3)
and |lambda|^2=2(Re lambda)^2-Re(lambda^2) give

    sigma2(K)=mu2+8 Delta_Xi.

Combining with (5),

    inf_S ||SKS^-1||_HS^2 = mu2+8 Delta_Xi.             (10)

The previous sufficient target is therefore EXACTLY RH-equivalent; it does
not additionally demand simple zeros or the absence of quasinilpotent parts.
Equation (10) does not evaluate its right side or give a zero-free region.

## 3. A complete continuous-tail control for the theorem

Consider the classical Volterra operator Vf(x)=integral_0^x f(t)dt on L2(0,1).
Its spectral mass is zero and ||V||_HS^2=1/2. Split [0,1] into m equal cells
and multiply the i-th cell by epsilon^i. Directly integrating the FULL kernel,

    ||S V S^-1||_HS^2
       =1/(2m)+(1/m^2)sum_(k=1)^(m-1)(m-k)epsilon^(2k)
       <=1/(2m)+epsilon^2/2.                           (11)

The within-cell triangles and EVERY between-cell rectangle are included.
Their limit goes to zero although V has no nonzero eigenvectors and no
bounded similarity can turn this nonzero V into zero. This explicitly tests
the continuous-nest part of (5), not a finite nilpotent surrogate.

## 4. SNE2: the full finite objective is geodesically convex

Fix a finite orthogonal projection P and write T=[A B; C D]. Put
R=BB*, Q=C*C and d0=||D||_HS^2. These are complete infinite-source quantities:
B and C include the WHOLE complementary subspace. For G>0 on PH,

    E_P(G)=Tr(G A G^-1 A*)+Tr(GR)+Tr(G^-1 Q)+d0.        (12)

It equals ||(G^(1/2) direct_sum I)T(G^(-1/2) direct_sum I)||_HS^2.
Formula (12), already derived in #881, is retained without dropping any term.

Consider ANY positive-cone geodesic

    G(t)=G0^(1/2) exp(tH) G0^(1/2), H=H*.

Set A0=G0^(1/2) A G0^(-1/2), R0=G0^(1/2)R G0^(1/2),
Q0=G0^(-1/2)Q G0^(-1/2). In an orthonormal eigenbasis of H with eigenvalues h_i,

    E_P(G(t))=d0+sum_ij |(A0)_ij|^2 exp[t(h_i-h_j)]
                  +sum_i (R0)_ii exp(th_i)
                  +sum_i (Q0)_ii exp(-th_i).           (13)

Every coefficient is nonnegative, since R0 and Q0 are positive semidefinite.
Twice differentiating proves convexity on EVERY such geodesic. In particular
any stationary point is a GLOBAL minimum of this fixed-block objective, not
merely a local numerical candidate. The infimum may fail to be attained:
the constant-direction elimination in #881 is a literal example.

This is convexity in the affine-invariant matrix geometry, not necessarily
in the entries of G or its Cholesky parameters. An arbitrary Euclidean optimizer
or a generic double-bracket trajectory does not inherit a convergence certificate.

## 5. SNE3: unique regularized minimizer and a global stopping certificate

For lambda>0 define

    F_(P,lambda)(G)=E_P(G)+lambda Tr(G+G^-1-2I).        (14)

The regularization is nonnegative and vanishes at I. The objective is continuous,
coercive and STRICTLY geodesically convex. Thus it has a unique minimizer.

### 5.1 Existence and an explicit finite condition bound

If F(G)<=F(I)=||T||_HS^2, the nonnegative energy and penalty show that every
eigenvalue g of G satisfies g+g^-1-2<=||T||_HS^2/lambda. Consequently

    M^-1 I<=G<=M I, M=2+||T||_HS^2/lambda.             (15)

That is a compact subset of the finite positive cone, proving existence.
It is only an upper condition bound, not a useful numerical precision claim.

### 5.2 Strong convexity and the normalized gradient

Along the geodesic in Section 4, the penalty's second derivative is

    lambda sum_i h_i^2[(G0)_ii exp(th_i)+(G0^-1)_ii exp(-th_i)].

Here entries are in the H eigenbasis. Cauchy--Schwarz gives
(G0)_ii(G0^-1)_ii>=1, and AM--GM makes the bracket at least 2.
Together with (13),

    d^2/dt^2 F(G(t)) >=2lambda ||H||_F^2.              (16)

This proves uniqueness and supplies a global error certificate. At G define

    L_G=A G^-1 A*+R-G^-1(A*GA+Q)G^-1
                                      +lambda(I-G^-2),
    Z_G=G^(1/2)L_G G^(1/2).                            (17)

The directional derivative at t=0 is Tr(H Z_G). Integrate (16) on the
geodesic from G to the minimizer and use Cauchy--Schwarz. Minimizing the resulting
quadratic in ||H|| gives

    F(G)-Tr(G L_G G L_G)/(4lambda)
       <= min_(X>0) F(X) <= F(G).                     (18)

No matrix square root need be computed to evaluate the squared-gradient term:
Tr(G L_G G L_G)=||Z_G||_F^2. For rational matrix data and rational SPD G,
(12),(14),(17),(18) are exact rational expressions. For the theta source,
the complete source integrals must be enclosed and all interval uncertainty
paid BEFORE using this certificate. No such new native enclosure is claimed.

A certificate for the finite minimum is NOT a certificate for its gap from
the infinite spectral infimum. The two limits are separated below.

If T's matrix is real, all data in (14) are real. Conjugating the unique
Hermitian minimizer gives another minimizer. Uniqueness forces it to be real
symmetric. Thus complex matrices do not offer an unaccounted smaller optimum
for the literal real theta operator at this regularized finite level.

## 6. SNE4: one prescribed source-defined sequence, with its exact limit

Let p0,p1,... be the real orthonormal polynomials for w, in increasing degree
with positive leading coefficients, and P_d project onto p0,...,p_(d-1).
They are complete: if f is orthogonal to every polynomial, the Fourier
transform of f w is entire by Cauchy--Schwarz and the source's exponential
moments; all its derivatives at zero vanish, then Fourier uniqueness gives f=0.

Choose lambda_d=2^-d and define the SINGLE scalar sequence

    m_d=min_(G>0 on P_d H)
           [E_(P_d)(G)+2^-d Tr(G+G^-1-2I)].             (19)

There is exactly one minimizer in every dimension, it is real symmetric,
and the dimension/penalty rule contains no zero data or adaptive target choice.

**Theorem.**

    m_(d+1)<=m_d,
    lim_(d->infinity) m_d=mu2+8 Delta_Xi.              (20)

Hence RH iff m_d->mu2. The value of that limit is not proved to be mu2.

Proof. Embedding G as G direct_sum I changes neither its whole similarity
nor its penalty trace. The penalty coefficient decreases, proving monotonicity.
The lower bound is (10). To identify the limit, it suffices to prove that finite
block similarities exhaust the bounded-similarity infimum, then make their
fixed penalty small.

For a bounded positive invertible M on H put M_d=I+P_d(M-I)P_d. Its lower/upper
bounds are uniform, M_d->M strongly, and polynomial approximation of continuous
functional calculus gives strong convergence of square roots and inverse square
roots. For HS T, multiplication on either side converges in HS norm; on the
right use adjoints as well, which here converge strongly since all factors are
self-adjoint. Prove this first for finite-rank T and then use the uniform bounds.
Thus E(M_d)->||M^(1/2)T M^(-1/2)||_HS^2. An arbitrary invertible S has polar
factorization U M^(1/2), and U does not change this energy.

Given epsilon>0, (10) and this exhaustion give some finite G in dimension d0
whose energy is below mu2+8Delta_Xi+epsilon. For every d>=d0 embed that same G.
Its penalty trace is fixed and finite, so 2^-d times it tends to zero. This
bounds limsup m_d by mu2+8Delta_Xi+epsilon. Let epsilon decrease to zero.
No relation between a near-optimal condition number and its dimension is
assumed in this argument. QED.

Equation (18) permits verified approximation to each m_d, in principle, to
any prescribed tolerance. Rational SPD points are dense; near the unique
minimizer their gradients tend to zero. A search with complete source enclosures
can therefore terminate once the certified gradient gap is small. This is a
finite-dimensional termination observation, NOT a uniform running-time bound,
a supplied all-dimensional implementation, or a proof of the theta limit value.

In particular a positive lower bound for m_10-mu2 does NOT refute RH: it is a
finite restriction/regularization cost. Only full-energy upper bounds tending
to mu2 prove the desired conclusion.

### 6.1 SNE5: complete primitive errors can be propagated before certification

Suppose the exact data are (A,R,Q,d0), approximated by (Ab,Rb,Qb,db), with
Frobenius errors bounded by eA,eR,eQ and scalar error ed. For a fixed SPD G
let g=||G||op, h=||G^-1||op, kappa=g*h, a=||Ab||F. Then the complete objective
error is at most

    eF=kappa(2a eA+eA^2)+||G||F eR+||G^-1||F eQ+ed.    (21)

The penalty is exact and does not enter this difference. In normalized
coordinates A0=G^(1/2)A G^(-1/2), its Frobenius perturbation is at most
sqrt(kappa)eA. The difference of A0 A0* and A0* A0 in the normalized gradient
is bounded by two applications of the product difference inequality. Thus

    eZ=4 kappa a eA+2 kappa eA^2+g eR+h eQ             (22)

bounds ||Z_true-Z_approx||F. Let z bound the approximate normalized gradient
norm, computed from Tr(G L_approx G L_approx). The TRUE regularized finite
minimum lies in

    [F_approx-eF-(z+eZ)^2/(4lambda), F_approx+eF].       (23)

All norm upper bounds in (21)--(22) may be replaced by certified larger
numbers. For theta, R and Q are positive by their COMPLETE operator definitions;
a rounded Rb or Qb need not itself be positive to apply these error inequalities.
Their error bounds must cover the full source integrals, not just grid roundoff.

Proof. Congruence bounds the A perturbation after similarity by sqrt(kappa)eA,
and Cauchy--Schwarz bounds the two linear trace perturbations. For the gradient,
||XX*-YY*||F <= 2||Y||F ||X-Y||F+||X-Y||F^2, and the same bound holds for X*X.
The two congruences of R and Q cost g and h respectively. This proves (21),(22).
Insert the true energy and gradient bounds in (18) to obtain (23).

Large condition numbers can amplify primitive uncertainty. Small optimizer
residuals alone are therefore insufficient; (21)--(23) distinguish source error,
finite optimization error, and the still-unknown dimension-to-infinity error.
No newly evaluated native bounds for any of those errors are supplied here.

## 7. Two exact tests of false endings

### 7.1 Normalization is not spectral reality

Consider the normal real matrix

    T=diag(J,J,B), J=[[0,-2],[2,0]], B=[[1,-2],[2,1]].

Then ||T||_F^2=26, Tr(T^2)=-22, and sigma2(T)=26. Its four eigenvalues from
the J blocks are +/-2i, twice; the B block supplies 1+/-2i. The complete sum
of squared real eigenvalue parts is 2, so 26=22+2*2, as required by (9).
No bounded similarity can reduce its norm below 26. A normalizing algorithm
has nothing left to do, yet the required imaginary-axis property is false.
This is an explicitly SYNTHETIC operator, not the theta K or a zeta zero.
It blocks the false conclusion that removing all nonnormality proves RH.

### 7.2 Dropping the complement fabricates a zero energy

For J=[[0,-1],[1,0]], choose P onto the first coordinate. Then A=D=0,
R=Q=1 and E_P(g)=g+1/g>=2. Looking only at A would return zero.
The regularized value is (1+lambda)(g+1/g)-2lambda, uniquely minimized at
g=1 with value 2. This tests the two coupling terms and the stopping certificate.

## 8. What was attempted next, and the actual open theorem

The exact geodesic formula means a verified finite solver need not rely on
an apparent local numerical minimum. The sharp infinite formula means the
method is not imposing extra simplicity or Riesz-basis conditions. Neither
fact bounds the native optimum as dimension grows. The decisive source-specific
claim remains

    m_d-mu2 ->0, or full explicit upper witnesses with that property. (OPEN-SNE)

A finite-rank spectral splitting based on unknown zeros proves sharpness but
cannot provide this missing arithmetic bound. Commutator/normality descent
leaves the spectral real-part energy unchanged at its optimum, as Section 7.1
shows. The positive singular-value operator also cannot identify that energy.
No rate for (20), cofinal native upper sequence, new theta defect value or
proof of RH was obtained in this pass.

The next useful calculation is a full source-enclosed nonlocal optimization
using (18), with a documented dimension error distinct from its finite solver
error. Exploratory floating calculations during this pass were NOT source
certificates: they omitted rigorous physical tails and used a approximate
high-end Iw tail, and are excluded from accepting output. One intermediate
basis-conversion field in a scouting JSON was inconsistent with the chosen
metric convention; no such field or scout value is imported into this packet.
No native numerical improvement is asserted on the basis of that exploration.

Recent orientation: #869's four-route continuation retains signed gamma
production, not a sign theorem; #842's reciprocal-subordinator continuation
retains the distinction between positive/decreasing heat sums and complete
monotonicity; #875's Newton-tail continuation retains coefficient feasibility
and completion-energy costs. They were inspected at PR-body depth, not used
as theorem inputs. #881 is the complete manuscript source read for this pass.

A separate literature caution is relevant. Izumi, arXiv:2602.11837v1 (2026),
proves convergence of specified MATRIX normalizing flows but explicitly gives
no general infinite-dimensional convergence theorem. We do not transfer that
claim to K. Our argument uses static compact triangularization and independent
finite geodesic optimization, not an assumed infinite-dimensional flow limit.

## Sources and review priorities

[P1] #881 at ab663f7d8020a62e1d8eedaf7d963d0eca3efe50,
standalone/2026-09-12-similarity-energy/PROOF.md: full manuscript read. Its
source definition, inherited spectral identification, exact full-block energy,
and correction boundaries are retained. No parent numerical campaign rerun.

[P2] #834 at f0e34780f4fe91bd5d07e791e8855189838c3df5,
standalone/2026-09-09-centered-theta-determinant/PROOF.md,
blob ef01f74c50d4efacb615176cbfed4a3de2fd1147: previously source-read and
explicitly inherited through P1. No fresh independent acceptance this pass.

[E1] J. R. Ringrose, Super-Diagonal Forms for Compact Linear Operators,
Proc. London Math. Soc. s3-12 (1962), 367--384,
https://doi.org/10.1112/plms/s3-12.1.367 .
Precise compact statement and multiplicities inspected through E2.

[E2] R. Drnovsek and M. Kandic, On the diagonal of Riesz operators on Banach
lattices, arXiv:2212.10243v1, Section 3 and Theorem 3.8,
https://arxiv.org/abs/2212.10243 . Only the named classical compact-chain
input is used; no Banach-lattice positivity theorem is applied to theta.

[E3] M. Izumi, A family of matrix flows converging to normal matrices,
arXiv:2602.11837v1, introduction and Section 4,
https://arxiv.org/html/2602.11837v1 . Orientation/caution only, no imported
normalizing-flow theorem in the proof above.

Review in order: continuous-nest pinching and multiplicities in SNE1;
trace-square continuity; the COMPLETE geodesic formula including R and Q;
strong-convexity and gradient factors in SNE3; real-minimizer uniqueness;
and the fixed-witness order of limits in SNE4. Finite exact tests do not
machine-prove these infinite statements or constitute independent review.

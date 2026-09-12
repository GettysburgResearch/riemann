# The whole-theta cumulant form: complete spectral index and positive realization

Date: 2026-09-12. Continuation proposed for PR #842, frozen at
`34ee76ed5bc8124a30aff7567152d4ae9f7f69cb`.

**Status: proposed complete COMPONENT proofs and a finite native-source
certificate, awaiting independent review. The all-order positivity statement
in Section 7, the all-order Ising realization, and RH are NOT proved.**
No result below converts successful finite tests into an infinite assertion.

This packet joins three existing directions. The cumulants matched in #842 and
#854 are the trace coordinates of #834's actual theta operator. The finite
exceptional-index argument of #858, together with #839's whole-source test,
can be extended to the WHOLE xi function,
without assuming finitely many nonreal zeros. It yields an exact finite-witness
theorem and, conditionally on one explicitly open positivity assertion, a
positive cyclic Hilbert-space realization that is NOT a bounded change of
metric on the old crowded exponential modes.

Power-sum zero criteria, Hermite/Hankel inertia, moment problems, Gaussian
quadrature and cyclic spectral representations are classical. In particular
Ruiming Zhang, arXiv:1510.03420v2, studies positive-zero power-sum criteria and
RH. This is not a novelty claim for another RH equivalence. The contribution
here is the source-qualified exact infinite-index composition, an explicit witness
with the complete complex tail paid, a precise weaker alternative to graph
realization, and a new complete theta calculation through moment 36. The whole-source positivity criterion itself is already
proved in #839 (shift2) and #841 (shift1); it is not new in this packet. The
central source positivity is still a substantive open theorem.

## 1. Literal source and normalization

Use the entire completion xi and exactly

    Xi(z)=xi(1/2+iz)=integral_R phi(t) exp(izt) dt,
    phi(t)=sum_(n>=1) exp(t/2)(4Q_n(t)^2-6Q_n(t)) exp(-Q_n(t)),
    Q_n(t)=pi n^2 exp(2t).

Jacobi inversion gives the even extension. On t>=0 every summand is positive;
evenness gives positivity on the other half-line. The series is locally
uniformly differentiable, and its tails are double exponential. Put

    w(t)=phi(t)/Xi(0),    mu_(2k)=integral_R t^(2k) w(t)dt,
    M(h)=integral_R exp(ht)w(t)dt=xi(1/2+h)/xi(1/2).

The last identity uses xi(s)=xi(1-s). M(0)=1, mu_0=1, and all odd moments are
zero. No variance standardization is made in the numerical certificate.
All probability and trace scalings below refer to this SAME w.

Define an entire function of v by its even Taylor series, not a square-root
branch:

    F(v)=Xi(sqrt(v))/Xi(0)=sum_(k>=0) (-1)^k e_k v^k,
    e_k=mu_(2k)/(2k)!.

Classical entire-function facts for xi give order(F)=1/2 and F(0)=1.
For completeness, the upper order bound also follows directly from the
source estimate phi(t)<=C exp(C|t|-c exp(2|t|)): maximizing R|t|-c exp(2|t|)
gives log max_(|z|<=R)|Xi(z)|=O(R log(2+R)). The lower order and the infinitude
of zeros may be imported from classical xi theory; only order(F)<1 and
nonconstancy are needed for the product used here. Hadamard factorization
therefore gives

    F(v)=product_j (1-lambda_j v)^m_j,                      (1)
    sum_j m_j |lambda_j| < infinity.

The nodes are DISTINCT nonzero inverse squared zeros lambda_j=z_j^(-2), one
per +/- pair of Xi zeros; m_j is its analytic multiplicity. The set is
closed under conjugation, with equal conjugate multiplicities, and its only
possible accumulation point is zero. This is an analysis of the divisor, not
a definition of the source or a numerical zero input. No exponential factor
is allowed by order<1 and normalization. M(h)>0 on real h excludes negative
real nodes: such a node would make F(v)=0 at a negative real v. Real nodes
are thus strictly positive. Xi(0)>0 excludes an exceptional zero at z=0.

Define q_n from the LOCAL logarithm at F(0)=1:

    -log F(v)=sum_(n>=1) q_n v^n/n,
    q_n=(-1)^(n+1) kappa_(2n)(w) / [2(2n-1)!].             (2)

Product (1) and absolute convergence give

    q_n=sum_j m_j lambda_j^n,  n>=1.                       (3)

All q_n are REAL, but their positivity is not presumed. Their zero-free
numerical definition is the finite Newton recursion

    q_r=(-1)^(r+1) [r e_r-sum_(k=1)^(r-1)(-1)^(k+1)q_k e_(r-k)]. (4)

This follows by differentiating M(sqrt(v))=sum e_k v^k and multiplying its
local logarithmic derivative. It is also checked against the independent
moment-to-cumulant recursion. Equations (2)--(4) use no global logarithm.
In #834's proposed determinant normalization, these SAME q_n are Tr(T^n).
No theorem about that operator is needed for the arguments below.

## 2. An infinite-divisor index theorem, with a finite polynomial witness

Let

    H_d=(q_(i+j+2))_(0<=i,j<=d),
    Q(P)=sum_(i,j) p_i p_j q_(i+j+2), P(x)=sum p_i x^i in R[x].

Every H_d is real symmetric. By (3),

    Q(P)=sum_j m_j [lambda_j P(lambda_j)]^2.               (5)

The square is BILINEAR, not a modulus square. Absolute convergence follows
from boundedness of all lambda_j and sum m_j |lambda_j|^2<infinity.
Complex coefficients may be handled by the Hermitian matrix form, but real
polynomials suffice for negative-index and positivity questions.

Let q_bad be the number of DISTINCT conjugate pairs of nonreal lambda nodes,
possibly infinity. In Xi coordinates this is the number of distinct nonreal
quartets, with analytic multiplicity NOT counted as separate quartets.

**CSI1.**

    sup_(d>=0) ind_-(H_d)=q_bad,                            (6)

with equality in the extended nonnegative integers. If q_bad is finite,
ind_-(H_d)=q_bad for every sufficiently large d. If it is infinite, the
negative indices tend to infinity. No rightmost zero, simple-zero assumption,
finite exceptional divisor, or finite-height replacement is used.

### 2.1 Upper bound

A real node contributes m lambda^2 P(lambda)^2>=0. At a nonreal conjugate pair,
put u=lambda P(lambda). Its contribution is

    2m Re(u^2)=2m[(Re u)^2-(Im u)^2].

There is at most one negative direction per DISTINCT pair. If there are q_bad
pairs, the imaginary evaluations map polynomials to R^q_bad. On its kernel
the entire form is nonnegative; hence its negative index is at most q_bad.
This proves the nontrivial upper bound when q_bad is finite. For an infinite
set the corresponding bound is simply infinity. Multiplicity weights are
positive and do not multiply the dimension of one imaginary evaluation.

### 2.2 Lower bound paying every omitted real AND nonreal node

Select ANY q distinct nonreal conjugate pairs (lambda_k, conjugate(lambda_k)).
Let rho=min_k |lambda_k|>0. Choose 0<r<rho that is not the modulus of any node.
Let A={a_1,...,a_J} consist of ALL distinct nodes with |a_j|>r. It is finite,
conjugation invariant, and contains the selected pairs. Let L_a(x) be its
Lagrange polynomial: L_a(a)=1 and L_a(b)=0 for b in A, b!=a.

For each selected pair define target values b_(k,a): i/lambda_k at a=lambda_k,
its conjugate -i/conjugate(lambda_k) at the conjugate node, and zero at all
other a in A. For an integer ell>=0 put

    P_(k,ell)(x)=x^ell sum_(a in A) b_(k,a) a^(-ell) L_a(x). (7)

Conjugate terms pair, so P_(k,ell) has REAL coefficients. At every a in A,
P_(k,ell)(a)=b_(k,a). Consequently the contribution of A to the q by q Gram
matrix of these polynomials is exactly diag(-2m_1,...,-2m_q).

The complete remaining node set lies inside |x|<r, including any infinitely
many nonreal nodes. Define the finite explicit constants

    C_k=sum_(a with b_(k,a)!=0) |b_(k,a)|
                       product_(b in A, b!=a) (r+|b|)/|a-b|,
    S_2(r)=sum_(|lambda_j|<r) m_j |lambda_j|^2 < infinity.

For every |x|<=r,

    |P_(k,ell)(x)| <= C_k (r/rho)^ell.                    (8)

For any real vector u, Cauchy--Schwarz and (8) bound the ABSOLUTE value of
its full omitted-tail quadratic form by

    S_2(r) (sum_k C_k^2) (r/rho)^(2ell) ||u||_2^2.         (9)

This bound does not assume that the omitted tail is positive. Choosing ell
so that

    S_2(r) (sum_k C_k^2) (r/rho)^(2ell) < 2 min_k m_k       (10)

makes the q-dimensional Gram negative definite. The polynomials have degree
at most ell+J-1 and are independent because of their distinct interpolation
values. Thus ind_-(H_(ell+J-1))>=q. Such ell exists since r/rho<1.

For finite q_bad select all pairs; for infinite q_bad apply the result to
arbitrary finite q. Principal-matrix inertia is nondecreasing with d, proving
(6). This is the part extending #858's fixed-stage, finite-defect argument:
the discarded tail in (9) may itself contain infinitely many complex nodes.

### 2.3 Exact interpretation and effective scope

The witness is FINITE even for one arbitrarily high or arbitrarily close-to-real
hypothetical zero. A degree-D polynomial uses only source moments through
4D+4. Equation (10) is a quantitative sufficient degree rule once enclosing
nodes, separation bounds and a full S_2 bound are available. This packet does
NOT compute these data for hypothetical zeta zeros or claim a uniform degree
bound from height alone. Poor separation can make ell and coefficients huge.
There is no claim that the tested nine-dimensional forms detect all defects.

As an immediate corollary for the literal source,

    RH <=> H_d >=0 for every integer d>=0.                 (11)

Negative real nodes need no separate test because the original M(h)>0 on R.
For a general unrelated real entire function this extra fact must not be
silently assumed. A single shifted family H_d suffices here; no finite d does.
This is a source-specific use of classical moment zero criteria, not a newly
discovered abstract characterization of RH.

### 2.4 A completely source-bound ceiling for the witness tail

The unknown spectral sum in (10) can be replaced by a fixed certified source
constant; an uncomputed operator norm is not an additional premise.
The elementary whole-source bound phi(t)<256 exp(-t^2) is reconstructed as
follows. For t>=0 and Q=pi n^2 exp(2t),

    t^2+t/2 <=(3/2)exp(2t)<=Q/2,
    exp(t^2)phi_n(t)<=4Q^2 exp(-Q/2)<=256 exp(-Q/4).

Sum exp(-3n^2/4)<sum2^-n=1 and reflect; exp(3/4)>2 follows from its first
four Taylor terms. Section5's finite source certificate proves Z>9/20 and
pi<81/25. Hence 256 sqrt(pi)/Z<1024, and Gaussian integration gives

    |F(v)| <=1024 exp(|v|/4),
    e_k <=1024/(4^k k!).                                 (12a)

Use the computed source moments through36 for the first19 terms. At |v|=20,
the ENTIRE remaining positive moment tail is at most

    sum_(k>=19) e_k 20^k
       <=1024*5^19/[19!*(1-1/4)].

The ratio after the first omitted term is at most5/20=1/4. Directed arithmetic
therefore proves

    M(sqrt(20)) < 1.79029212341979 < 9/5.

In particular, by the even series,

    |F(v)-1|<=M(sqrt(|v|))-1<4/5, |v|<=20.

So F has no zero on that disk. This is a low-radius normalization bound, not
a new high-height zero-free result. If N_F(t) counts zeros with multiplicity
in |v|<=t, Jensen at radius2t and (12a) give, for t>=20,

    N_F(t)<=log(1024 exp(t/2))/log2<10+t.

At a boundary zero use a limit of nearby radii. Stieltjes integration pays
the ENTIRE divisor, including any nonreal part:

    sum_j m_j |lambda_j|^2
       =2 integral_20^infinity N_F(t)t^-3 dt
       <=10/20^2+2/20 =1/8.                              (12b)

This deliberately coarse, unconditional computer-assisted source bound is
independent of zero locations, RH, a rightmost zero and the number of exceptional
pairs. In (10) one may therefore use S_2(r)<=1/8 for every r. The finite outer
node separations and witness coefficients still matter; (12b) does not supply
a degree bound uniform in an unknown high, tightly clustered quartet. It is
an ABSOLUTE spectral bound, not positivity of the signed q_2 or of any untested
Hankel form. No theorem about #834's operator norm is needed for it.

## 3. A positive cyclic realization, conditional on the exact open sign

This section explains why (11) avoids #834's bounded-metric obstruction.
It supplies no unconditional positivity proof.

Assume the right side of (11). By CSI1 all nodes in (1) are positive. Define

    nu=sum_j m_j lambda_j delta_(lambda_j).              (12)

This is a finite positive measure supported in [0,R], where R=max_j lambda_j;
it has NO atom at zero. Its moments are integral x^n dnu=q_(n+1).
The same Hilbert space can be constructed from the source alone: take real
polynomials with inner product L(PQ), L(x^n)=q_(n+1), quotient null vectors,
complete and complexify. The map P -> (P(lambda_j)) is an isometry onto the
polynomial subspace of L2(nu). Polynomials are dense by Weierstrass and density
of continuous functions for finite compactly supported measures. Thus this
construction is canonically L2(nu), without discarding a remaining source mode.

Multiplication by x gives a bounded positive self-adjoint operator A, ||A||=R,
and the class e of the constant polynomial is cyclic. The identity

    -F'(v)/F(v) = <e,(I-vA)^(-1)e>                (13)

holds first at v=0 by (3), then throughout the common meromorphic domain.
Every pole and analytic multiplicity is retained. At v=1/lambda_j, the residue
of the right side is -nu({lambda_j})/lambda_j=-m_j.

The CYCLIC operator has ONE eigenvector per distinct lambda_j. Analytic
multiplicity m_j is in the measure weight and resolvent residue; it is NOT a
new assertion that Xi zeros are simple. In particular det(I-vA) would generally
lose those multiplicities, and is NOT claimed equal to F. Equation (13), not
a misnormalized determinant, is the source-complete identity in this space.

This is neither a bounded similarity nor a local reweighting of #834's
exponential/sine functions. It is a different polynomial-trace Hilbert space.
Its positivity is exactly the unproved assertion (11); building it formally
without verifying that sign is circular. The construction does establish that
no ADDITIONAL eigenvector-completeness or bounded-metric hypothesis is needed
once that particular all-order source sign is obtained.

## 4. Finite positive models from cumulants, without solving an Ising inverse problem

This finite statement needs only the indicated two positive matrices, not RH.
Put m_k=q_(k+1), and for n>=1 suppose both

    G_n=(m_(i+j))_(0<=i,j<n)>0,
    J_n=(m_(i+j+1))_(0<=i,j<n)>0.                          (14)

In the monomial coordinates of dimension n, let

    A_n=G_n^(-1)J_n,   e=(1,0,...,0)^T,
    <u,v>_G=conjugate(u)^T G_n v.

**CSI2.** A_n is positive self-adjoint in this finite metric. It has n distinct
positive eigenvalues a_j, and positive weights beta_j, with

    m_k=sum_(j=1)^n beta_j a_j^k,  0<=k<=2n-1.             (15)

Proof. Positivity and self-adjointness follow from (14). Since J_n column j
is G_n column j+1 for j<n-1, A_n e_j=e_(j+1). Thus e,A_ne,...,A_n^(n-1)e
are the monomial basis and e is cyclic. A finite self-adjoint cyclic operator
has simple eigenvalues, and its spectral weights beta_j are strictly positive.
For k<=2n-2 write k=i+j with 0<=i,j<=n-1. Then

    <e,A_n^k e>_G=<A_n^i e,A_n^j e>_G=m_k.

For k=2n-1 use <e_(n-1),A_n e_(n-1)>_G=(J_n)_(n-1,n-1)=m_(2n-1).
The spectral theorem gives (15). QED. These are classical Gaussian-quadrature
facts with the needed finite algebra shown explicitly.

Consequently

    R_n(v)=<e,(I-vA_n)^(-1)e>_G                     (16)

has only positive real poles and Im R_n(v)>0 for Im v>0. Its Taylor expansion
agrees with -F'/F through v^(2n-1). All beta_j are positive, but beta_j/a_j
need not be integers. Exponentiating an integral of R_n can therefore introduce
fractional powers; it is NOT asserted to be an entire Lee--Yang generating
function or a finite spin partition function. This avoids substituting an
unproved ferromagnetic realization for the finite moment problem.

If (11) holds, (14) follows for every n from (12), and polynomial compression
of the bounded positive A makes these finite models compatible with its
resolvent. Without (11), finitely many successes in (14) prove only those
finite positive realizations. In particular the certificate below does not
prove convergence to a positive full spectral measure.

## 5. Fresh native certificate through the thirty-sixth theta moment

The accepting calculation proves G_9>0 and J_9>0 for the EXACT source w.
For conditioning only, replace q_k by r_k=200^k q_k. The two tested matrices
are (r_(i+j+1)) and (r_(i+j+2)), 0<=i,j<9. This is a positive scalar times a
positive diagonal congruence, so it does not alter either sign. The integer
200 is a fixed arithmetic scaling, not a zero or an approximate spectral input.

The exact interval LDL pivots and their decimal enclosures are recorded in
certificate.json. All18 pivots are strictly positive. They are LDL pivots, not
eigenvalue or continuum spectral-gap bounds. Each full matrix is one finite
predicate. CSI2 supplies a positive nine-node spectral quadrature from these
two forms; no numerical nodes, pole locations or actual zeta zeros are computed.
The upper-left4x4 block of G_9 also reproduces #841's stated determinant interval
(1.1775e-41,1.1777e-41), using this packet's fresh source calculation.

### 5.1 Source quadrature with complete errors

For even m=0,2,...,36 evaluate b_m=2 integral_0^infinity t^m phi(t)dt.
Use the first eight theta terms on [0,3], 128 midpoint cells, half-width
h=3/256, and Taylor polynomials through degree 63. For

    P_0(Q)=4Q^2-6Q,
    P_(j+1)=2Q P_j'+(1/2-2Q)P_j,

phi_n^(j)(t)=exp(t/2-Q_n)P_j(Q_n). Since exp(3/2)<5, a full L1 derivative
bound for the eight-term sum on [0,3] is

    B_j=20 sum_(k>=1) |[Q^k]P_j| (k-1)!.

This follows termwise by substituting Q=pi n^2 exp(2t) and extending the
nonnegative gamma-integral majorant to [0,infinity). Thus

    C_m=sum_(j=0)^min(64,m) binom(64,j) m!/(m-j)! 3^(m-j) B_(64-j)

bounds the L1 norm of the 64th derivative of t^m times that sum. The integral
Taylor remainder on either half of one cell has Peano kernel at most h^64/64!.
Summing over the disjoint cells and doubling proves the error allowance

    2 h^64 C_m/64!.                                      (17)

At a midpoint all derivative polynomials are evaluated in 768-bit outward
integer arithmetic. For Q>=400 a direct rational upper bound is used BEFORE
rounding, rather than allowing exponential underflow to multiply an enormous
polynomial. With l=floor(Q_lower) and u=ceil(Q_upper),

    |exp(t/2-Q)P_j(Q)| <=5 (3/8)^l sum_k |[Q^k]P_j| u^k.

For Q_lower>=2048, replace l,u by 2048 using monotonicity of Q^k exp(-Q)
for Q>=2048>=k (all evaluated k<=65), and e>8/3. The resulting symmetric
interval encloses the entire derivative, not an omitted theta term.

For every m, t^m<=m!exp(t) gives, with Q0=pi n^2 exp(2a)>=3,

    2 integral_a^infinity t^m phi_n(t)dt
          <=4m!(Q0^2+2Q0+2)exp(-Q0).

The complete omitted n>=9 sum is bounded by

    8m! 59537 exp(-243),                                 (18)

using pi>3 and consecutive ratios below 1/2. The complete physical tail
beyond t=3, for ALL n>=1, is bounded by

    8m! 1002002 exp(-1000)
       <8m! 1002002 (3/8)^1000.                          (19)

Indeed pi exp(6)>1000, and again the consecutive ratios are below 1/2.
These crude elementary constants are checked independently. Double counting
an omitted corner in the upper bound is harmless. Positivity of all half-line
summands makes (18),(19) one-sided additions; (17) is two-sided.

The normalized moments are b_m/b_0 with b_0>0 certified. Apply (4), retaining
interval dependency conservatively, and then interval LDL with a positive
lower pivot at every step. All tails, the normalizer, and all cross entries
are therefore included. There is no zeta, gamma, zero-table or floating oracle.

### 5.2 Elementary arithmetic contract

Machin's formula with 220 alternating terms per arctangent encloses pi; the
first omitted alternating term is retained. Exp uses |x/2^r|<=1/8, 96 Taylor
terms and remainder <=2/(8^97 97!), followed by outward repeated squaring.
For a negative input interval, the 1-Lipschitz property of exp pays input
width. For endpoints <=-768, exp lies in [0,2^-768]. The high-Q derivative
bound above prevents unsafe magnification of this floor. Every multiplication,
division and square root is directed using Python integers. Ordinary and
optimized runs use the SAME implementation, not independent authorship.

## 6. What was attempted before this pivot

The current #842 branch provides a proposed exact connected ten-moment model
and fixed-order local higher-moment directions. #854 independently supplies
an exact twelve-moment seed, a positive fourteenth-moment excess and a
negative compensated coupling direction at a different older seed. Its
explicit statement that local rank does not guarantee target reachability
is essential here.

Ordinary floating scouting this pass tried a single positive edge on the
#854 six-group seed, extra nonuniform couplings on the #842 core/halo/hub,
and two added leaf amplitudes with lower-cumulant compensation. No additional
moment equality was certified. A first-order predicted coupling beyond its
allowed range is NOT a proof of infeasibility; stalled numerical solves are
not a theorem. These exploratory data are not inputs to Section 5.

#839's full complex-tail single-witness proof and #841's shifted criterion and finite4x4 source proof
were found during the overlap check and are explicitly credited, not claimed
as new here. #858's power-sum index was reconstructed at its frozen source, especially
its complete positive-tail argument. CSI1 uses a full ABSOLUTE complex-tail
bound, so finite exceptional index of an approximant is not used to assume
finite exceptional index for xi. The alternative #859/#860 branching versions
have nonuniform depth thresholds and were read only at metadata level. They
cannot be inserted as a cofinal zero-free statement.

## 7. The full proposed ending and the unresolved arithmetic sign

The actual condition still required is exactly

    for EVERY d>=0 and EVERY (c_0,...,c_d) in R^(d+1),

    sum_(i,j=0)^d c_i c_j
      (-1)^(i+j+3) kappa_(2i+2j+4)(w)/[2(2i+2j+3)!] >=0.  OPEN-CSI

If OPEN-CSI is proved, CSI1 rules out every nonreal Xi quartet at every
height, retaining multiplicities; positivity of M on R already excludes
imaginary Xi zeros. This proves RH. CSI1 gives the complete contradiction
if even one hypothetical off-line zero exists, with no uniform witness-degree
assumption. Section 3 then supplies the compatible positive cyclic realization.

For comparison, a finite Ising law matching the actual moments through 4d+4
would make H_d positive semidefinite by the classical Lee--Yang product. Thus
OPEN-CSI is a necessary quadratic target for the graph programme, without
requiring the stronger unexplained existence of graphs at every order.
The converse to Ising realizability is not claimed.

An ordinary moment Gram integral_w |P(t)|^2>=0 does NOT prove OPEN-CSI.
The q's are nonlinear cumulants of w, or power sums of the still-unknown
complex divisor. In (5) replacing a complex square by an absolute square
would discard exactly the negative directions CSI1 detects. None of the
random-cluster identities, local implicit-function arguments, accurate source
approximations or finite positive matrices read in this pass justifies that
replacement or a sign-preserving all-order recurrence. This direct attempted
positivity step was not completed.

**There is no unconditional RH proposal here.** The completed results identify
and quantify a source-complete finite obstruction to any off-line zero, remove
extra bounded-metric/eigenvector-completeness demands from a conditional cyclic
construction, and certify finite native positive forms. What remains is the
explicit all-order quadratic inequality above. Reviewers are asked to review
the supplied statements, not to invent a proof of that inequality.

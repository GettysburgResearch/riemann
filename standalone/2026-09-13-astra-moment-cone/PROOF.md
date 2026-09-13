# MCE26: a native moment-cone test, a degree-28 obstruction, and permanent finite-order positivity

2026-09-13. **Proposed component proofs and computer-assisted finite inequalities;
independent mathematical and implementation review required. RH and the
unbounded-dimension positivity estimate are NOT proved.**

This continues PR875 at `177cf75e93b5614c5d5f0db1e4721ac69727e5ce`, including
its `newton-tail` and `closure-bridge` continuations. It is a separate sibling
packet, not another directory inside an ancestor's sealed inventory.

The qualitative power-sum/moment approach is classical and already present in
the repository (#858/#862 and the recent #842 subordinator). In particular this
is not a claim to have discovered a new qualitative RH criterion. See Zhang,
*On Power Sums of Positive Numbers*, arXiv:1510.03420, for prior genus-zero
power-sum criteria, and the classical Hamburger moment theorem. The proposed
contributions here are a directly usable moving-native-source criterion, a
fresh source-only degree-28 obstruction, an explicit permanent finite-order
certificate, and the rational residual construction in RATIONAL_BRIDGE.md.

## 1. Fixed source and conventions

Let G_n be independent Gamma(shape 2, rate 1),

    X_N = sum_(n<=N) G_n/n^2,     X=sum_(n>=1)G_n/n^2,
    tau_N=2 sum_(n>N)n^-2,        Y_N=X_N+tau_N.

If g_N is the density of Y_N, set

    h_N(t)=sqrt(g_N(pi exp(2t))g_N(pi exp(-2t))),
    Z_N=int_R h_N(t)dt,           F_N(z)=int_R h_N(t)exp(izt)dt/Z_N.

This is the unchanged centered family, not the Radau-compressed family or a
newly optimized probability law. Write Phi(z)=Xi(z)/Xi(0), Xi(z)=xi(1/2+iz).
The classical BPY/Jacobi identification gives F_N -> Phi locally uniformly
in the entire plane. The elementary coupling proof and quantitative source
bounds needed here are reconstructed in Section 5. All these functions are
real, even, normalized at zero, and strictly positive on the imaginary axis.

For any one of these F define f_k and p_k at the origin by

    F(z)=sum_(k>=0)(-1)^k f_k z^(2k), f_0=1,
    log F(z)=-sum_(k>=1) p_k z^(2k)/k.                 (1)

Equivalently p_k=(-1)^(k+1) kappa_(2k)/[2(2k-1)!]. These are NOT ordinary
moment Hankels. The exact triangular recurrence used by the code is obtained
from A(w)=sum f_k w^k and A'=A sum q_j w^j:

    q_j=(j+1)f_(j+1)-sum_(l=1)^j f_l q_(j-l),
    p_(j+1)=(-1)^j q_j.                                (2)

Define the shift-two matrix of SIZE d (indices 0 through d-1)

    H_d(F)=(p_(i+j+2))_(0<=i,j<d).                     (3)

It needs coefficients through f_(2d), hence raw even moments through degree
4d. In computations use pbar_k=200^k p_k. The resulting matrix is congruent
to H_d via diag(200,200^2,...,200^d), so its inertia is identical.

Every admissible NJT model

    G(z)=exp(-alpha z^2) product_l(1-lambda_l z^2),
    alpha>=0, lambda_l>0, sum lambda_l<infinity,

has p_k(G)=sum lambda_l^k for k>=2. Consequently

    v^T H_d(G)v=sum_l lambda_l^2
                       [sum_(i<d)v_i lambda_l^i]^2 >=0. (4)

The Gaussian factor affects p_1, not (3). Equation (4) applies to the
polynomial comparison class whether or not it is a probability transform.

## 2. The moving-source ending requires no integer-residue fit

**Theorem MCE1 (classical moment mechanism, moving-source quantifiers).** The
following are equivalent:

(a) RH.
(b) H_d(Phi) is positive semidefinite for every d.
(c) There exist integers d_j -> infinity and N_j -> infinity such that
    H_(d_j)(F_(N_j)) is positive semidefinite.
(d) For every fixed d, H_d(F_N) is positive definite for all sufficiently large N.

In (c), N_j need not follow an explicit schedule or be increasing at each step.
It must tend to infinity. There is no assertion that H_d(F_N) increases in N.
A sufficient version is an unbounded sequence of successful d with N>=d.

### Proof of the all-order moment implication, retaining every complex zero

The classical source growth gives log max_|z|<=R |Phi(z)|=O(R log(R+2)).
Even genus-zero factorization in the variable z^2 therefore gives

    Phi(z)=product_l(1-lambda_l z^2), sum_l |lambda_l|<infinity, (5)

where lambda_l is the inverse square of one zero from each +/- pair.
Conjugate pairs and analytic multiplicities are retained. No reality of
lambda_l is assumed here. The Gaussian exponential is absent by the order
in z^2. Let L=sup |lambda_l| and C=sum |lambda_l|^2, both finite.
Then u_k=p_(k+2)=sum lambda_l^(k+2) is real and

    |u_(2k)|<=C L^(2k).

Assumption (b) and the classical Hamburger existence theorem provide a positive
measure mu on R with moments u_k. The bound just displayed forces its support
into [-L,L]: any positive mass outside [-L-epsilon,L+epsilon] would violate
the even-moment bound as k increases.

For |w|>L the common moment expansion identifies

    int dmu(x)/(w-x)=sum_l lambda_l^2/(w-lambda_l).     (6)

The left side is holomorphic off [-L,L]. The right side is meromorphic on each
open nonreal half-plane: only finitely many lambda_l lie outside any disk
about zero, and the remaining normally convergent tail is controlled by
sum |lambda_l|^2. By the meromorphic identity theorem, it can have no pole
in either half-plane. But a node lambda off the real line contributes a
nonzero residue m lambda^2, where m is its positive integer multiplicity.
There is no cancellation at that node. Hence all lambda_l are real.
A negative lambda would give an imaginary-axis Phi zero, impossible because
Phi(iy) is a positive cosh integral. Therefore all lambda_l are positive,
and all Xi zeros are real. This is RH.

Under RH, (4) holds for Phi and is strictly positive for a nonzero polynomial:
Xi has infinitely many distinct positive zeros, whereas the polynomial has
only finitely many roots. Multiplicities do not change this. Thus H_d(Phi)>0.
For each FIXED d, locally uniform source convergence gives coefficient, then
p_k, then matrix convergence. Positive definiteness is open, proving (d).
Selecting N_j sufficiently large for d_j=j proves (c). Conversely, for any
fixed d, eventually d_j>=d. Its principal matrix is positive semidefinite;
passing to the N_j limit proves H_d(Phi)>=0. This proves all implications.

**What is still open:** establish (c) with d_j unbounded by exploiting the
actual source. This theorem does not assert that a positive ordinary density,
a positive heat trace, or its factorial-weighted moment matrices establish
(3). The factorial removal gap in #842 is retained exactly.

Compared with NJT's polynomial-fit schedule, this test has no prescribed
coefficient-accuracy target and no nonlinear root-multiplicity fitting step.
But its source-dependent matrix positivity is still an RH-strength assertion.
It is not a free consequence of Gaussian quadrature or of a finite jet.

## 3. A fresh native obstruction at degree twenty-eight

**Theorem MCE2 (computer-assisted proposed component).** For the literal
centered F_5, H_7 has inertia (six positive, one negative). H_6 is positive
definite. A rational vector v in parameters.json satisfies

    -1.0843e-11 < v^T (pbar_(i+j+2,F5))_(i,j<7) v
                 < -1.0842e-11.                         (7)

The displayed interval is deliberately wider than the retained outward
interval, approximately

    (-1.0842851945431e-11, -1.0842851945408e-11).

Every source value in this assertion is freshly calculated from the defining
centered gamma integral. Neither the earlier F5 zero coordinates, its
Rouche certificate, nor an external low-zero census is imported. The rational
vector was suggested by ordinary numerical exploration, but its quadratic
form is then evaluated against the complete outward source enclosures.

The accepting factorization has six strictly positive pivots and a final
negative pivot in approximately

    (-9.903964012771e-11, -9.903964012742e-11).

These are LDL pivots, NOT eigenvalue intervals. The exact congruence
factorization proves the inertia. The companion shift-one matrix
(pbar_(i+j+1))_(i,j<7) is positive definite; it does not repair the failure
of shift two.

### A robust distance bound for every NJT real-zero model

Let

    E_14(32)=sum_(k=0)^14 |f_(k,F5)-f_(k,G)| 32^(2k).

**Then no admissible G in (4) can satisfy**

    E_14(32)<=2^-72.                                    (8)

In particular exact matching of F5 through raw moment degree 28 is impossible.
This is a much lower sufficient forbidden degree than the previous 512, not
a claim about the smallest forbidden degree of any conceivable test.

For the proof, (8) puts each f_(k,G) in the freshly computed F5 interval
expanded by 2^-72/32^(2k). Apply (2) with outward arithmetic on this whole
14-coordinate box. The SAME rational vector then obeys

    v^T Hbar_7(G)v < -1e-11.

The retained enclosure is approximately
(-1.126211e-11,-1.042360e-11). This contradicts (4). Dependencies among the
coefficient errors were discarded only to enlarge the box, which is safe.
The proof never substitutes fitted moments or a zero finder for the source.

This obstruction concerns F5, NOT Phi. It emphasizes why the stage must move
in a cofinal construction; it neither refutes the moving-source route nor RH.

## 4. Positive native theta data and a rational construction

The complete theta source is freshly integrated through raw moment degree 32.
Both size-eight matrices

    (pbar_(i+j+1,Phi)) and (pbar_(i+j+2,Phi))

are certified positive definite. The final outward LDL pivots are near
1.24769204860948e-12 and 6.88467579642144e-14 respectively. The full intervals
are retained in result.json. No unbounded matrix assertion is inferred.

RATIONAL_BRIDGE.md uses these data to construct a degree-eight rational
Stieltjes comparator by exact rational linear algebra. Two finite positive
matrices, not a search over zero locations, prove all its poles negative and
its spectral weights positive. The selected rational logarithmic-derivative
moments are rounded native data; they do not redefine the native source.

The integrated comparator can have fractional multiplicities and need not be
entire. We explicitly do NOT feed it into NJT as an entire product. A separate
first-order differential-residual criterion supplies a legitimate off-axis
consumer. No new native zero-free rectangle from that criterion is claimed
by the executed certificate.

## 5. Permanent size-eight positivity at every sufficiently late gamma stage

**Theorem MCE3 (proposed).** For EVERY integer N>=2^192, both of the size-eight
matrices in Section 4, with F_N replacing Phi, are positive definite.
The bound is conservative; no near-optimal first N is claimed. No transform
at that huge stage is evaluated. The complete source error proves the result
for all those N simultaneously.

Here is the source comparison used to make the statement effective.
Write U_N=sum_(2<=n<=N)G_n/n^2 and R_N=X-X_N. The density
f_1(x)=x exp(-x) 1_(x>0) is globally 1-Lipschitz. Coupling the complete tail
and its mean therefore gives for EVERY real x

    |g_N(x)-f(x)| <= E|R_N-tau_N|
                   <=sqrt(2 sum_(n>N)n^-4)<N^-3/2.       (9)

The telescoping moment E exp(U_N)=(2N/(N+1))^2<=4 implies
f_N(x)<=4x exp(-x). Also tau_N<=tau_1<13/10 and exp(13/10)<4.
It follows that f and all g_N are globally at most 16. Hence

    |h_N(t)-h(t)|<=8 N^-3/4.                            (10)

For instance split sqrt(ab)-sqrt(cd) as
sqrt(b)(sqrt(a)-sqrt(c))+sqrt(c)(sqrt(b)-sqrt(d)) and use
|sqrt(a)-sqrt(c)|<=sqrt(|a-c|).

The complete double-exponential envelope from these same density bounds is

    h_N(t),h(t)<=64 exp[-3 cosh(2t)].                    (11)

Indeed within the support,
sqrt((x_+-tau)(x_--tau))<=pi and the exponential factor is
exp(tau-pi cosh(2t)); use pi<4, exp(tau)<4, pi>3. Else h_N=0.
The normalizer has the uniform guard Z_N>1/1600: the mean of U_N+tau_N is
less than 13/10; with probability >1/2 it is <=13/5. On x in [3,4] the
remaining f_1 argument lies in [2/5,4], where f_1>1/16. Thus g_N>1/32 there,
and both pi exp(+-2t) lie in [3,4] for |t|<=1/100. Integrate h_N on that
interval. The same guard holds in the limit.

Let A_(k,N)=int_R t^(2k) h_N(t)dt and A_k use h. Splitting at |t|=3, (10)
pays the central interval. For the rest, t^(2k)<=(2k)!exp(t), e^6>400, and
t-3cosh(2t)<=t-(3/2)e^(2t) show that the combined two-sided tail is less
than (2k)! 2^-590. For detail, its derivative at t>=3 is <=-1199, its value
at 3 is <-597, and the prefactor 256/1199 is less than one. Therefore

    |A_(k,N)-A_k| <= e_k(N)
       :=16 N^-3/4 3^(2k+1)/(2k+1)+(2k)!2^-590.          (12)

No uncomputed gamma mass is omitted. Dividing by the guarded normalization
and keeping its change gives, for k>=1,

    |f_(k,N)-f_(k,Phi)|
       <=1600 [e_k(N)/(2k)!+f_(k,Phi)e_0(N)].            (13)

The source f_(k,Phi) on the right is enclosed by the actual theta quadrature.
For N>=2^192 replace N^-3/4 by 2^-144 in (12). Inflate every coefficient
interval by (13), then apply (2) to the WHOLE coefficient box. The final
shift-two LDL pivot is contained approximately in

    (6.88464519e-14,6.88470640e-14),

and all preceding pivots are positive. The shift-one matrix also passes.
The bounds worsen as N decreases, so this single outward computation proves
the claim at every later stage. Numerical details and every pivot are in the
certificate. This is a fixed-DIMENSION theorem, not the unbounded d_j in MCE1.

## 6. The next theorem and the failed automatic completion

The target is now explicit: prove that successful dimensions in the actual
native matrix family are unbounded, while the chosen stages tend to infinity.
One sufficient quantitative statement would control the negative part of
H_d(F_N) in a source-adapted positive basis and produce a strict margin at
N=N(d), for unbounded d. The unproved ingredient is that margin, not merely
an absolute error bound for F_N-Phi.

Attempted shortcut: #842's positive reciprocal subordinator supplies
factorial-weighted moment positivity. Dividing its entries by factorials is
not a positivity-preserving operation in general. We did not use that shortcut.
Similarly the finite rational Stieltjes construction in Section 4 proves the
COMPARATOR positive, not the next native matrix. Its explicit residual must
still be controlled. MCE2 demonstrates that this distinction has numerical
consequences already at a small fixed stage.

The arithmetic route remains independent. The latest #875 completion-energy
tradeoff and #869 covariance/annular-energy identity show why a changed
completion cannot count a favorable covariance without its complete energy
cost. This pass does not improve the native arithmetic upper bound or claim
new arithmetic cancellation. The proposed best next joint analytic attack is
a source-level positivity or residual estimate, not more unstructured fits.

## 7. Scope of executed proof evidence

The complete F5 source, theta moments, robust form, positive matrices, permanent
coefficient tube and rational Pade identity are reconstructed from exact
integers/rationals and outward dyadic primitives. The classical source identity,
Hamburger theorem, entire factorization and uniform analytic remainder arguments
remain mathematical dependencies requiring review. Normal/optimized agreement
is not an independent arithmetic backend. Read VALIDATION.md for actual command
receipts, rejected prototypes, publication status, and the separate limited
scope of receipt-only tests. No RH proof, global feasibility, full native zero
census, repository-wide formal validation, or independent referee acceptance
is claimed.

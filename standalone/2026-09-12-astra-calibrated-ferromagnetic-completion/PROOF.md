# CFC26 — calibrated connected completions of finite ferromagnetic moment jets

Date: 2026-09-12. Status: **proposed component proofs; independent mathematical
review required. RH and all-order theta realization are NOT proved.**

This paper supplies a construction, not an assumed inverse-Ising theorem. A
finite nondegenerate moment realization can be completed to an infinite,
connected, positive-coupling model with exactly the same prescribed moments
and all three leading real-field growth coefficients of the theta law. The
construction applies just as well to finite cores which are NOT theta. Thus
calibration is an available normalization, not evidence for the missing
all-order reachability assertion.

The general construction and stability proof below are new to this packet.
The harmonic transfer-matrix mechanism is credited to CTC26 (#871), whose
required analytic calculation is reconstructed in Sections 2 and 5. The
particular degree-fourteen corollary imports the proposed finite root theorem
ICR26 (#863); no independent acceptance of that theorem is asserted.

## 1. Statements and quantifiers

Let G be a fixed finite zero-field Ising graph on k>=1 vertices with finite
couplings J_ij>=0. Its probability is proportional to

    exp(sum_(i<j) J_ij sigma_i sigma_j), sigma_i in {-1,1}.

For positive observable weights a_i define Y=sum_i a_i sigma_i, S=sum_i a_i,
and F(z)=E exp(izY). Zero weights can be treated by positive approximation
when only approximation rather than exact moment preservation is wanted.

**CFC1 (density with prescribed growth).** There is an explicitly specified
sequence X_N of connected infinite ferromagnetic observables such that:

1. X_N is a well-defined L2 sum, has an analytic probability density and all
   exponential moments. Its characteristic function is entire and all its
   zeros are real.
2. For EACH sufficiently large integer N, writing M_N(h)=E exp(hX_N),

    log M_N(h) = (h/2)log h - (1+log(2pi))h/2
                                  +(7/4)log h+O_N(1), h->+infinity. (1)

   The O_N(1) constant need NOT be uniform in N. Symmetry handles negative h.
3. F_N(z)=E exp(izX_N) converges to F(z) locally uniformly on C. An explicit
   complete-disk estimate is given in (13); for each fixed disk its order is
   O((log N)^2/N). Every fixed moment converges as well.

The construction uses a finite core, N equal small observable weights, and
an infinite decreasing harmonic/logarithmic tail. Every edge in the attached
path has the fixed coupling (1/2)log(3/2). If the original core is disconnected,
add a fixed spanning tree with additional coupling 1/N on each edge.

**CFC2 (exact finite jets).** More generally let a_i(theta)>0 be C2 functions
of theta in an open subset of R^r; keep the core couplings fixed. Suppose
at theta0 the r-by-r Jacobian of

    theta -> (E Y_theta^2,...,E Y_theta^(2r))                         (2)

is nonsingular. Then for EVERY sufficiently large integer N the construction
has a parameter theta_N near theta0 for which

    E X_(N,theta_N)^(2j)=E Y_theta0^(2j), 1<=j<=r,                  (3)
    |theta_N-theta0|=O((log N)^2/N).

All weights remain positive, (1) remains exact at the three stated orders,
and the full complex convergence is still to the core law Y_theta0. The
threshold and constants depend on the exhibited finite core and order r.
There is NO uniform-in-r assertion. Section 7.1 gives a deliberately huge
analytic threshold for the 272-spin application, not a computed new root.

**CFC3 (theta corollary, with imported finite input).** Assuming the proposed
ICR26 finite moment-root theorem at the source locked in SOURCES.json, there
is a family of connected infinite ferromagnetic observables satisfying (1)
and EXACT theta moments 2,4,6,8,10,12,14. For all sufficiently large N their
standardized sixteenth-moment difference from theta lies in (0.19,0.22).
They are therefore NOT theta. The old finite model's residual does not vanish
merely because the model has acquired a connected infinite tail.

## 2. Fixed tail and the calibration constants

Throughout set

    q=1/5, c=1/2, ell=log(3/5), d=7/(8ell),
    lambda(u)=[(1+q)cosh u+
        sqrt((1-q)^2+(1+q)^2 sinh^2 u)]/2,
    f(u)=log lambda(u),
    m(u)=f'(u)=sinh u/sqrt(sinh^2 u+(2/3)^2),
    Cq=-1+integral_0^1 m(u)/u du
                +integral_1^infinity (m(u)-1)/u du,
    B0=c log c+c(gamma+Cq), Btheta=-(1+log(2pi))/2.

Both integrals converge. f(0)=0, f is even, f(u)=O(u^2) at zero and
f(u)=u+ell+O(exp(-2u)) as u->+infinity. Its second derivative is bounded by
K exp(-2u), u>=0, for a finite K.

For n>=32 put

    a_tail(n)=c/n+d log(n)/n^2.                                    (4)

These are positive and decreasing and 1/(4n)<a_tail(n)<1/(2n).
For a completely elementary coarse check, -2<d<0 follows from
-log(3/5)>7/16 (integrate 1/x, or use the atanh logarithm series).
Then 2log32/32<1/4 and 2(2log32-1)/32<1/2, with log32<7/2,
prove positivity and a negative derivative; the relevant ratios decrease
for x>=32. The sharper lower bound 1/(4n) follows from the first inequality.

Define the convergent sum and harmonic number

    S_N=sum_(n>=N) log(n)/n^2, H_(N-1)=sum_(j=1)^(N-1)1/j,
    L_N=Btheta-B0+c H_(N-1)-d S_N.                                (5)

These definitions involve only real integrals and convergent series, not
zeros, an unknown spin optimizer, or a continuation through zeta zeros.
Elementary integral comparisons give L_N=(1/2)log N+O(1).

For completeness, the tail growth calculation is as follows. The integrable
bounded-variation function

    g(t)=f(1/t)-t^-1 1_(t<=1)

has integral Cq. Its jump at 1 is retained. A cellwise variation bound for
Riemann sums and the elementary harmonic asymptotic yield

    sum_(n>=1) f(x/n)=x log x+(gamma+Cq)x+O(1), x->infinity.         (6)

To perturb c/n by d log(n)/n^2, Taylor expand once. All intermediate positive
fields for n>=32 are >=ch/(2n); the entire second-order error is bounded by

    K' h^2 sum_(n>=32) log(n)^2 n^-4 exp(-ch/n)
                         =O(log(h)^2/h).

The integral/dyadic comparison proving this is global: below h, the factor
exp(-ch/n) sums the small-n blocks; above h, n^-4 sums the remaining blocks.
No expansion in a large Taylor argument is used.

For g1(t)=(m(1/t)-1)/t^2, both g1 and log(t)g1 are integrable and of bounded
variation. Substitution and integration of f'-1 give

    integral_0^infinity g1(t)dt=ell.

Their Riemann sums therefore show

    h d sum_(n>=N) log(n)n^-2[m(ch/n)-1]
                           =(d/c)ell log h+O_N(1).

Restoring the separated linear sum and subtracting the first N-1 terms in
(6) gives the complete fixed-N formula

    sum_(n>=N) f(h a_tail(n))
       =ch log h+[B0-c H_(N-1)+d S_N]h
                              +(d/c)ell log h+O_N(1).             (7)

Here (d/c)ell=7/4 exactly. This calculation is the inherited CTC26 mechanism,
reconstructed to fix every sign, index, and constant used in the new graft.

## 3. The actual graph and complete small-perturbation estimate

For a core parameter theta, put S(theta)=sum_i a_i(theta) and define

    A_N(theta)=L_N-S(theta), u_N(theta)=A_N(theta)/N.               (8)

Choose N>=32 so large that A_N(theta)>=1/2 on a chosen compact parameter
neighborhood. This is possible because S(theta) is bounded there and L_N
increases without bound asymptotically. Notice u_N>=1/(2N)>=a_tail(N).

Choose one core vertex v. Starting at v attach a path with N cloud spins
of equal observable weight u_N, followed by tail spins of weights

    a_tail(N), a_tail(N+1), a_tail(N+2), ... .

All path edges, including the first edge from the core, have tanh J=q=1/5.
Add 1/N to the couplings of a fixed spanning tree of the core, using k-1
edges when k>1. No negative coupling is introduced. This produces one
connected graph. Tree addition is harmless when an edge already existed.

Let Y_(theta,N) denote the core observable under this perturbed finite core
law. Generate the attached signs by the Markov transition

    P(tau_(j+1)=tau_j)=3/5, tau_0=sigma_v.

This defines the infinite probability law directly. Every finite prefix is
EXACTLY the free-boundary zero-field Ising law of the corresponding graph:
summing the last spin of a zero-field path multiplies a weight by 2cosh J,
independent of its parent. In particular the marginal law of the core is
not changed by attaching the path. It changes only through the declared
1/N core-tree edges.

Write B_(N,theta) for the complete appended observable and
X_(N,theta)=Y_(theta,N)+B_(N,theta). Unconditionally the path starts with a
fair sign, so E tau_i tau_j=q^|i-j|. Harmonic square summability and the
row-sum bound kappa=(1+q)/(1-q)=3/2 prove L2 convergence and

    V_B=E B^2 <= V_N(theta)
        :=(3/2)[A_N(theta)^2/N+1/(4(N-1))].                       (9)

Every term in the infinite tail is included in this estimate. It has order
(log N)^2/N, not zero. Since weights along the attached path are nonincreasing,

    E(B | whole core)=b_N sigma_v,
    b_N=sum_(j>=1)q^j w_j, 0<=b_N<=u_N/4=A_N/(4N).              (10)

Conditional second and all conditional even moments of B are the same for
the two values of sigma_v; the two conditional laws are reflections.

Weighted Lee--Yang for finite nonnegative-coupling graphs is our classical
zero-location input [LY]. Its needed moment consequence can be proved by
pairing zeros in the exponential-type canonical product:

    E W^(2j)/(2j)! <= (Var(W)/2)^j/j!,
    E exp(hW)<=exp(Var(W)h^2/2), h real.                         (11)

These bounds hold for the finite appended paths and pass to their L2 limit
by uniform exponential integrability. For the full attached graph,
Var(X)<= (S(theta)+sqrt(V_N))^2, which is finite and bounded on compact
parameter sets for all large N. Consequently the finite graph transforms
converge locally uniformly on C. The limit is 1 at zero, and Hurwitz proves
that it too has only real zeros. This does NOT assert anything about the
zeros of the theta target.

Here is a sharper source comparison, retaining prefix-tail dependence.
For |z|<=R expand exp(izB) through first order. Equations (9)--(11) imply

    E[B^2 exp(R|B|)] <= sqrt(6) V_N exp(R^2 V_N).

The linear term uses (10), not an independence assumption. If
S_* bounds S(theta), it follows that

 |E exp(izX)-E exp(izY_(theta,N))|
   <=exp(R S_*)[R A_N/(4N)
                 +(sqrt(6)/2)R^2 V_N exp(R^2 V_N)].                (12)

The total added core coupling is eta_N=(k-1)/N. Normalized Gibbs density
ratios between perturbed and original core lie in [exp(-2eta_N),exp(2eta_N)].
Therefore the final explicit complete-disk comparison is

 sup_(|z|<=R)|E exp(izX_(N,theta))-E exp(izY_theta)|
 <=exp(R S_*)[exp(2eta_N)-1+R A_N/(4N)
                   +(sqrt(6)/2)R^2 V_N exp(R^2 V_N)].              (13)

This is uniform on the parameter neighborhood, is O_R((log N)^2/N), and
accounts for the entire infinite chain. Its right side does not involve an
unknown zeta norm or an optimized tail. Cauchy's formula gives convergence
of every fixed derivative/moment; Section 6 also supplies C1 parameter
convergence, which is necessary for exact moment correction.

## 4. Full infinite cutoff and analytic density

For a fixed graft parameter N, stop its harmonic tail at index L>=N.
The finite graph then includes the whole core, all N cloud spins, and the
indices N,...,L. Let chi_L be its characteristic function, chi the infinite
one, and V=Var(X). Row sums and Markov conditioning give

    Var(omitted tail)<=3/(8L),
    |E(omitted tail | prefix)|<=1/[8(L+1)].                       (14)

Positive covariances imply Var(prefix)+Var(tail)<=V. For this use, their
nonnegativity follows directly by expanding each finite Gibbs weight as
product(1+tanh(J_ij)sigma_i sigma_j): all surviving numerator terms of a
two-spin expectation are nonnegative. Pass to the prescribed limit. Expanding the omitted
exponential through first order and using (11), twice with Cauchy--Schwarz,
gives exactly

 sup_(|z|<=R)|chi(z)-chi_L(z)|
 <=R exp(VR^2/2)/[4(L+1)]
                      +3sqrt(6)R^2 exp(2VR^2)/(16L).             (15)

The core need not be a path. Its influence on the omitted tail passes through
one boundary sign; that is the only fact used in (14). (15) is the complete
CFC finite-graph approximation, not a claim that cloud index N can be confused
with harmonic truncation index L.

For the density, condition on the core and all even spins of the appended
path in a long finite truncation. Interior odd spins are conditionally
independent and have bias of modulus at most tanh(2J)=5/13. A factor at phase
u therefore has modulus <=exp[-(72/169)sin(u)^2]. For a real frequency T with
|T|>=max(N,64), choose the odd harmonic indices in [|T|,2|T|]. Their phases
lie in [1/8,1/2], by (4), and there are at least |T|/4 of them. Each factor
is bounded by exp(-1/640). All other conditional factors have modulus <=1.
Pass to the infinite transform using (15):

    |chi(T)|<=exp(-|T|/2560), |T|>=max(N,64).                     (16)

A possible endpoint parity choice only decreases the conservative count;
the elementary count is valid for real |T|>=64. Fourier inversion gives a
nonnegative symmetric density holomorphic in |Im x|<1/2560. The threshold
in (16) depends on N: this is not a density bound uniform over all grafts.

## 5. The complete real-field growth, including the coupling to the core

The free appended path has nonincreasing positive weights. Let P be its
symmetric transition matrix, v0=(1,1)/sqrt(2), and

    T(u)=P^(1/2)diag(exp u,exp(-u))P^(1/2).

Its Perron eigenvalue is lambda(u). A positive Perron vector is (1,tau(u)),
where tau(u) decreases from 1 to

    tau_*=(1-sqrt(q))/(1+sqrt(q))>0.

One verifies monotonicity from the ratio of the diagonal difference to the
off-diagonal entry. For successive fields u_i>=u_(i+1)>=0, positivity of
T(u_i) compares T(u_i)(1,tau(u_(i+1))) with lambda(u_i)(1,tau(u_i)),
with scalar factors min(1,tau_(i+1)/tau_i) and max(1,tau_(i+1)/tau_i).
Iterating and retaining both endpoint vectors telescopes those factors.
Thus for EVERY finite appended path and every real h>=0,

 |log M_path(h)-sum_j f(h w_j)|<=log 2+log(1/tau_*).               (17)

The bound does not grow with path length, N, or h. The path covariance
bound and exponential integrability justify its infinite-length limit.
This is not an illicit product-of-eigenvalues replacement of noncommuting
matrices.

The core and the free path can be coupled by their one Ising edge exactly.
Under their tilted laws denote the endpoint expectations by r_core(h),
r_path(h), each in [-1,1]. The normalized moment-generating functions obey

    M_total(h)=M_core(h)M_path(h)
                             [1+q r_core(h)r_path(h)].            (18)

The last factor lies between 1-q and 1+q. This proves a uniform O(1) bound
for the complete interfacial correction. No sign of a mixed term is dropped.
Since the core is finite and every configuration has positive probability,

    log M_core(h)=h S(theta)+O_(N,theta)(1), h->infinity.

The cloud contributes N f(h u_N)=h A_N+O_N(1). Equation (7) gives the full
harmonic-tail contribution. Hence (17),(18) yield

 log M_total(h)=ch log h+
   [B0-c H_(N-1)+d S_N+S(theta)+A_N(theta)]h
                       +(d/c)ell log h+O_(N,theta)(1).

Equation (8) makes the middle coefficient exactly Btheta. This proves (1).
The standard xi/gamma expression plus Stirling gives the same three terms
for M_theta(h)=xi(1/2+h)/xi(1/2), independently of RH [ST].

Each completed law consequently has unbounded support and entire transform
of order one. For each fixed law the ratio M_total(h)/M_theta(h) is bounded
above and below by positive constants on the whole REAL field axis. These
constants are not uniform in N, and this is not a complex ratio estimate.
There is no positive Gaussian convolution factor: such a factor would force
quadratic lower growth by Jensen applied to the centered remaining law.

## 6. Exact preservation of any nonsingular finite moment jet

Work on a small compact convex neighborhood U of theta0, on which the weights
are C2 and uniformly positive. Put

    F0(theta)=(E Y_theta^2,...,E Y_theta^(2r)),
    FN(theta)=(E X_(N,theta)^2,...,E X_(N,theta)^(2r)).

We prove the stronger parameter estimate

    ||FN-F0||_(C1(U))=O_U,r((log N)^2/N).                         (19)

The constants here are finite but not numerically instantiated. Core
couplings are fixed, and the added tree couplings 1/N do not depend on theta.
Thus the only parameter differentiation inside the finite core expectation
is of its bounded observable. The perturbed core density differs from its
original value, uniformly over all configurations, by O(1/N).

Let T_N=sum of the N cloud signs. The appended chain law is independent of
theta conditional on its boundary core sign, and

    partial_j B=-(partial_j S)T_N/N,
    E(T_N^2)<=3N/2,
    partial_j b_N=-(partial_j S)q(1-q^N)/[N(1-q)].                 (20)

For a fixed integer k<=2r expand (Y+B)^k. The linear term equals
k b_N E[Y^(k-1)sigma_v]. It and its parameter derivative are O(log N/N),
using (10),(20) and uniform bounds on Y and its first derivatives.
Every term of degree j>=2 in B is O(V_N^(j/2)), by (11). Differentiating
such a term produces either a bounded derivative of Y or a factor
B^(j-1)partial B. Cauchy--Schwarz and (11),(20) bound the latter by

    C_j V_N^((j-1)/2)/sqrt(N).

For large N all these quantities are O((log N)^2/N). The same estimates
justify differentiation of the infinite chain, e.g. by uniform convergence
of the finite path derivatives on U. This proves (19), retaining the linear
conditional-mean term and every core-tail cross moment.

Let R=DF0(theta0)^(-1). Choose a closed theta-ball of radius rho inside U so
that sup||I-R DF0||<=1/4. For all sufficiently large N, (19) gives

    sup||I-R DFN||<=1/2,
    ||R(FN(theta0)-F0(theta0))||<=rho/4.

The map theta -> theta-R(FN(theta)-F0(theta0)) is a contraction of this ball
into itself. Banach supplies a unique root there and

    |theta_N-theta0|<=2||R|| |FN(theta0)-F0(theta0)|
                                    =O((log N)^2/N).              (21)

This proves CFC2 for every sufficiently large integer N. Positivity, source
support, and growth calibration continue to hold throughout the ball. The
argument does not require a known theta root for arbitrary r; it starts from
ONE specified nonsingular finite solution. It therefore cannot be iterated
into an all-order existence proof without an additional theorem.

## 7. The degree-fourteen application and its nonzero defect

ICR26 #863 defines a positive 272-spin core with a fixed positive dimer edge.
Its seven squared-weight coordinates have a nonsingular cumulant Jacobian
at an exact root matching theta through degree fourteen. The whole-box
certificate, including the full theta source, is an imported proposed input;
its exact SHA/path and reading/replay scope are in SOURCES.json.

The triangular transformation between cumulants and moments has nonsingular
diagonal. Multiplication by the fixed positive variance scale v has the same
property. Thus the physical raw moment Jacobian required by (2) is nonsingular.
Apply CFC2 with r=7, adding a spanning tree of 271 core edges (some may
reinforce an existing edge) and the attached positive path. All finite
truncations of the resulting infinite graph are connected ferromagnets.
The first seven even theta moments match EXACTLY for every sufficiently
large N, and their full variance is v. Equations (1),(15),(16) apply.

The imported core also has a standardized sixteenth-moment error in
(0.20,0.21). The completed, retuned laws converge in every fixed moment to
that SAME core, by (13),(21). Therefore their corresponding error is in
(0.19,0.22) for all sufficiently large N. This proves CFC3 and proves that
these completed laws are not theta. Section 7.1 also supplies a concrete sufficient cloud size. No numerically
evaluated new root vector is asserted.

### 7.1 An explicit, deliberately very large choice of cloud length

The existence statement can be made effective at the imported ICR26 box
without evaluating a new enormous partition function. One sufficient choice is

    N_star = 10^1000.                                             (22)

This is an analytic upper construction, NOT a practical graph size or a new
numerically integrated infinite root. We retain the same seven-coordinate
box of radius 10^-14 and its rational preconditioner from ICR26.

Here are deliberately coarse complete constants. The imported native variance
satisfies 1/25<v<1/20, and all seven box coordinates lie in (1/2000,1).
The physical core therefore has |Y|<300 and every coordinate derivative
|partial_j Y|<10000. In this entire box S<300. Directly from the definitions
in Section 2, |Btheta-B0|<4 and S_N<1 for N>=32. For example, m is concave on
[0,infinity), m'(0)=3/2, and 0<=1-m(u)<=2 exp(-2u) for u>=1; these bounds
place Cq in (-5/4,1/2), which is more than sufficient. Integral comparison
places H_(N-1) between log N and 1+log N. Thus

    (log N)/2-304 < A_N < (log N)/2+7.

Since 2<log10<3, (22) gives 1/2<A_N<2000. Equation (9) implies
V_N<7*10^6/N. All appended-path moments up to order 64 obey

    ||B||_p < 30000/sqrt(N),
    ||partial_j B||_p < 100000/sqrt(N), p<=64,

where non-even p are bounded by the next even moment. The latter estimate
uses T_N's variance <=3N/2. Hence ||Y+B||_p<301 and
||partial_j(Y+B)||_p<10001 throughout the box at N=N_star.

For every raw moment of order k<=16, the binomial/product identity or the
mean-value inequality and Holder give, including the core Gibbs change,

    |M_k(N)-M_k(0)| < 10^60/sqrt(N),
    |partial_j M_k(N)-partial_j M_k(0)| < 10^60/sqrt(N).             (23)

To check the deliberately loose scale: the undifferentiated term is bounded
by 16*30000*601^15/sqrt(N); differentiated terms are bounded by
16*15*10000*30000*601^14/sqrt(N)+16*100000*301^15/sqrt(N).
The density change contributes less than 1000/N times 300^16, or its
bounded derivative. Each is far below the stated ceiling. The elementary
bound exp(2*271/N)-1<1000/N is used only at this explicitly huge N.

The cumulant polynomial at order k has total absolute coefficient sum at
most k!*2^(k-1)<10^18 for k<=16. Each monomial has at most 16 factors and
weighted moment-degree k. Thus its other factors are bounded by 301^k,
not by an uncontrolled number of large moment factors. A differentiated
factor has bound <=10^6*301^(j-1). Telescope products and their derivatives
using (23), then divide the even cumulants by v^(k/2)c_k, where |c_k|>=1.
Since v^-8<25^8<2*10^11, the complete scaled equation/Jacobian difference
is bounded ENTRYWISE by

    10^150/sqrt(N_star) = 10^-350.                               (24)

Every displayed coarse integer inequality is also checked by the new exact
checker. It does not evaluate the source moments that justify the imported
variance and native box.

The old preconditioner has row norm <7.5*10^7<10^8. Equations (24) therefore
add at most 10^-342 to the preconditioned residual, and at most 7*10^-342
to its Jacobian row-sum defect. The imported bounds are respectively
6*10^-22 and 1.01*10^-7. With radius 10^-14 they satisfy

    (6*10^-22+10^-342)
       +(1.01*10^-7+7*10^-342)*10^-14 < 10^-14.

Banach proves the exact completed moment root inside the SAME seven-dimensional
box for the concrete choice (22). This quantifies the construction without
enumerating N_star states or computing a new transcendental root. It remains
conditional on the imported native finite certificate and the analytic
bounds proved in this manuscript, not on a new machine evaluation of X.

Because the new lower seven cumulants match theta, its raw sixteenth-moment
error equals its sixteenth-cumulant error after normalization by v^8.
Equation (24), multiplied by |c_16|<2*10^9, and the original whole-box defect
bound in ICR26 keep that error in (0.19,0.22). This particular explicitly
completed model is therefore still NOT theta.


## 8. What the completion settles about the whole programme

Within the topology of locally uniform characteristic-function convergence,
the bounded-variance closure of finite ferromagnetic magnetization laws equals
the bounded-variance closure of the calibrated connected infinite laws just
constructed. The forward inclusion follows from CFC1 applied to each finite
law with a diagonal choice of sufficiently large N. The reverse inclusion
follows from the finite-prefix approximation (15). Variances can be kept
bounded in both diagonal choices by (9) and core covariance bounds.

Accordingly, requiring a connected infinite graph, an analytic density, the
three exact theta growth coefficients, and any fixed nonsingular theta moment
jet adds NO new all-order reachability theorem. These are properties our
construction can impose around many different finite laws.

If a sequence of admissible finite cores matches every fixed theta moment,
with bounded variances, the classical Lee--Yang moment estimate (11) pays the
complete complex Taylor tails. Their transforms, and appropriately chosen
completions, then converge locally uniformly to Xi/Xi(0). Hurwitz proves RH.
But existence of those cores at unbounded orders remains OPEN. Neither (21)
nor the closure equality proves it. Reviewers are not being asked to supply
that missing assertion as an unmentioned final lemma.

## Sources and assurance

[LY] C. M. Newman and W. Wu, arXiv:1901.06596v2, weighted Ising statement
following (21), and Theorem 16 for broader closure context. Only weighted
Lee--Yang is an indispensable imported zero theorem; the needed variance
moment bounds and limiting estimates are reconstructed above.
[ST] NIST DLMF 5.11, Stirling asymptotics; the actual xi normalization is
fixed in the predecessor source. Only real-field growth is compared.
[CTC] CTC26, PR871 at 43a9eea85e20202370cae4b6ffa1a2c30fc3cfc3,
PROOF.md Sections 2--4; harmonic Perron/tail mechanism credited and rederived.
[ICR] ICR26, PR863 at 0640c9c59be0bf20c18258460a7517fb09728e82,
PROOF.md Sections 1--4; proposed native r=7 finite root and mismatch imported.

The new checker authenticates bounded rational graph, conditional-moment,
Perron comparison and parameter-derivative controls. It does not machine-prove
these infinite analytic statements, independently certify ICR26, numerically
instantiate its completed roots, or establish RH.

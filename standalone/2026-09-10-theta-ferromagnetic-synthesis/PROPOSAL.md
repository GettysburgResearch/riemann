# Constructive ferromagnetic synthesis of the actual theta law

Date: 2026-09-10. New research direction, separate from PR #834's spectral metric.
Status: **PROPOSED component proofs and a computer-assisted six-moment seed.
The all-order realization is OPEN. This is NOT a proof of RH.**

The idea is to reverse the order of the previous spectral construction. Do not
first construct an operator with the right determinant and then try to prove
its spectral sign. First construct finite models in a class whose zero-location
theorem is already proved; then identify their limit with the exact theta law.

The zero-location class here is the zero-field ferromagnetic Ising model.
Lee--Yang, Griffiths--Simon approximation, and Newman--Wu weak closure are
classical. Neither the connection of Lee--Yang to RH nor the general limit
argument is claimed new. The concrete contribution of this packet is a
source-normalized inverse problem, a quantitative moment interface, a finite
ferromagnetic realization of the first six theta moments, and an exact Villain
cycle identity suggesting how the integer-square source could enter a growing
construction. No all-order extension theorem is asserted.

## 1. Fixed target and fixed conventions

Retain the literal full-line theta density

    phi(t) = sum_(n>=1) exp(t/2) [4Q_n(t)^2-6Q_n(t)] exp(-Q_n(t)),
    Q_n(t) = pi n^2 exp(2t),
    Xi(z) = xi(1/2+iz) = integral_R phi(t) exp(izt) dt.

This is the entire xi completion with xi(0)=xi(1)=1/2. Jacobi inversion makes
phi even. On t>=0 its summands are positive; reflection, not a termwise claim
on the negative half-line, gives positivity everywhere. The series and all
fixed derivatives converge locally uniformly. Its n=1 tail is

    phi(t)=4pi^2 exp(9t/2-pi exp(2t))(1+O(exp(-2t))), t -> +infinity.

Thus Z=integral phi=Xi(0)>0, and w=phi/Z is an even probability density with
all exponential moments. Put

    v=integral_R t^2 w(t)dt,   sigma=sqrt(v)>0,
    X=t/sigma under the law w(t)dt,   m_(2k)=E X^(2k).

Then m_2=1 and the TARGET moment-generating function is exactly

    M_theta(h)=E exp(hX)=xi(1/2+h/sigma)/xi(1/2).                 (1)

Equivalently Xi(z)/Xi(0)=M_theta(i sigma z). Proving that M_theta has no
zeros off the imaginary axis proves RH. Neither an auxiliary probability law
nor a rescaled convention may replace (1) without stating the change.

The theta identity is classical and is reconstructed in the exact-theta-pencil
parent. We use only that source identity and positivity/tails, not any proposed
spectral sign or determinant theorem in PR #834.

## 2. The finite models: zero location BEFORE the limit

For a finite graph G=(V,E), spins sigma_i in {-1,1}, real couplings J_e>=0,
and nonnegative field weights a_i, define the zero-field Gibbs law

    P(sigma)=Z_0^(-1) exp(sum_(e={i,j}) J_e sigma_i sigma_j),
    S=sum_i a_i sigma_i.

No one-site external fields are used in this probability law. Its generating
function is

    M_G(h)=Z_0^(-1) sum_sigma exp(sum_e J_e sigma_i sigma_j+hS).

Spin flip makes S symmetric. The classical multivariate Lee--Yang theorem
implies

    M_G(h) != 0 whenever Re h != 0.                          (2)

Zero field weights are allowed by continuity; all weights in the explicit
seed below are strictly positive. This theorem is imported from the published
Lee--Yang theory, not established by finite root finding in this packet.

### FMS1: variance controls the ENTIRE generating function

For such a finite model with Var(S)=1,

    E S^(2k) <= (2k)!/(2^k k!)  for every k>=0,
    |M_G(h)| <= exp(|h|^2/2)   for every complex h.             (3)

Proof. S is bounded, so M_G is entire of exponential type. Hadamard
factorization and (2), paired with evenness and M_G(0)=1, give

    M_G(h)=product_j (1+h^2/y_j^2),    y_j real nonzero,
    sum_j y_j^(-2)=1/2.

Multiplicities are retained. The paired canonical product has no linear
exponential factor because the function is even, and no quadratic exponential
factor because it is of exponential type. Every coefficient of the product
is nonnegative. Coefficientwise,

    product_j(1+h^2/y_j^2) <=_coeff exp(h^2 sum_j y_j^(-2)).

Finite partial products and monotone coefficient limits prove the first part
of (3); the same comparison, or taking moduli of the factors, proves the
second. This is a standard consequence of the Lee--Yang product. We make no
claim of discovering its Gaussian domination property.

### FMS2: a concrete all-order finite feasibility statement would finish RH

Suppose that for every integer r>=1 there is a FINITE zero-field ferromagnetic
model S_r as above, with variance exactly one, satisfying

    |E S_r^(2k)-m_(2k)| <= 1/r,   1<=k<=r.                  OPEN-FMS

Then RH follows. More generally, 1/r may be replaced by any sequence tending
to zero. Graphs need not be nested and no effective bound on their size is
required for this implication.

Proof. For every fixed k, taking r to infinity in (3) gives
m_(2k)<=(2k)!/(2^k k!). The actual theta law already has an entire generating
function, and its Taylor coefficients are its moments. For every R<infinity,

 sup_(|h|<=R)|M_Gr(h)-M_theta(h)|
   <= (1/r) sum_(k=1)^r R^(2k)/(2k)!
      +2 sum_(k>r) (R^2/2)^k/k!                            (4)
   <= (cosh R-1)/r
      +2 exp(R^2/2)(R^2/2)^(r+1)/(r+1)! -> 0.

Hence convergence is uniform on EVERY fixed complex compact, not just at
real h or at finitely many moments. Hurwitz on each open half-plane transfers
(2); the limiting entire function cannot be identically zero since its value
at zero is one. Equation (1) then proves RH. No simplicity assumption enters.

This quantitative proof is a special case of the known Lee--Yang weak-closure
mechanism (Newman--Wu, Theorem 7). Its merit as an interface is that a future
finite moment construction does NOT need an additional uniform exponential-
tail estimate. The variance normalization and Lee--Yang structure supply it.
There is no uniform relative approximation claim near zeros or at unbounded
frequency, and none is needed for the conditional conclusion.

IMPORTANT: OPEN-FMS is a sufficient arithmetic realization problem. We have
NOT proved that RH would imply realization by finite ferromagnetic Ising
models. The ferromagnetic realization class can be more restrictive than
merely having an imaginary-axis zero set. Failure of a chosen graph family
would therefore not refute RH.

## 3. The inverse problem is explicit finite algebra

Replace each coupling by r_e=exp(-2J_e), so 0<r_e<=1. After cancelling an
irrelevant common factor, the weight of a spin configuration is

    W_r(sigma)=product_e r_e^(1_(sigma_i != sigma_j)).

For fixed graph size, its moment-matching equations are

    sum_sigma (sum_i a_i sigma_i)^(2k) W_r(sigma)
       =m_(2k) sum_sigma W_r(sigma),   1<=k<=r.             (5)

They are polynomial equations in a_i and r_e, with coefficients given by the
actual theta moments. Rational enclosures of those coefficients come from
the unmodified defining theta integral. Approximate versions of (5) are
finite polynomial inequalities with nonnegative a_i and 0<r_e<=1.

This is not a claim that nonlinear feasibility is easy, convex, or automatically
solvable. It gives a checkable construction target. A numerical optimizer must
not use negative couplings, signed field weights, or reweight the target law.
A convex mixture of successful models is NOT automatically successful: the
Lee--Yang class is not a convex cone of probability measures.

For development of an extension rule, the exact derivatives are useful:

    d/dJ_e E[S^(2k)] = Cov(S^(2k),sigma_i sigma_j),
    d/da_i E[S^(2k)] = 2k E[sigma_i S^(2k-1)].              (6)

The second formula is at fixed zero-field Gibbs law. These are finite sums,
not assumptions about random prime signs. A full-rank local Jacobian might
allow adjustment near an interior model, but does not imply global feasibility
or extension to the next order. No such all-order rank or extension theorem is
proved here.

## 4. FMS3: an actual finite ferromagnetic six-moment seed

A model in the required class really exists for the first three nontrivial
even moments. This is not a fit to zeta zeros.

Let S be the total spin of the complete graph on eight vertices with the
SAME ferromagnetic coupling J at each of its 28 edges. Write q=exp(2J)>1.
For s in {-8,-6,...,8},

    P_q(S=s)=binom(8,(s+8)/2) q^(s^2/4) / Z(q),
    Z(q)=sum_(k=0)^8 binom(8,k) q^((k-4)^2).              (7)

The omitted factor exp(-4J) cancels in normalization. Consequently all
moments and cumulants c_2(q),c_4(q),c_6(q) are rational functions of q.

For the standardized theta law put

    A=-kappa_4(X)>0,    B=kappa_6(X)>0.

The directed source certificate in Section 5 proves

    0.208897057432 < A < 0.208897226226,
    0.350653241429 < B < 0.350673600822.                   (8)

Take L=4096 additional independent unbiased spins epsilon_j. They have no
edges to each other or to the eight-spin block. We will form

    Y_q=sqrt(t(q)) S + sqrt(gamma(q)/L) sum_(j=1)^L epsilon_j.

For q in the fixed rational interval [11/10,1101/1000], define

    d(q)=-c_4(q),
    D(q)=d(q)+2 c_2(q)^2/L,
    t(q)=[2c_2(q)/L+sqrt(D(q) A-2d(q)/L)]/D(q),
    gamma(q)=1-c_2(q)t(q).                               (9)

The certificate proves that the radical is positive, t>0, and

    0.348620053078 < gamma(q) < 0.352043930427              (10)

THROUGHOUT the entire q interval (128 closed subintervals cover it). These
numbers are deliberately wide bounds, not the values at a unique root.

An unbiased sign has cumulants 1,-2,16 at orders 2,4,6. Independence and (9)
therefore give EXACTLY, for every q in the interval,

    kappa_2(Y_q)=1,
    kappa_4(Y_q)=c_4 t^2-2gamma^2/L=-A,
    kappa_6(Y_q)=c_6 t^3+16gamma^3/L^2=:B_L(q).            (11)

The quadratic equation behind t is

    (d+2c_2^2/L)t^2-(4c_2/L)t+2/L-A=0.

The exact directed endpoint enclosures are

    0.350087258775 < B_L(11/10) < 0.350087683437,
    0.351467264282 < B_L(1101/1000) < 0.351467690620.       (12)

Equations (8),(12) are strictly separated. By continuity there is q_* strictly
between the endpoints with B_L(q_*)=B. At that q_*, Y_q is a FINITE weighted
magnetization of a ferromagnetic graph with 4104 vertices and 28 nonzero edges.
Its first, second, ..., sixth moments agree exactly with those of X: odd
moments vanish, and the matching even cumulants determine moments 2,4,6.

Its generating function is explicitly

    [Z_K8(sqrt(t) h;J)/Z_K8(0;J)]
       cosh(sqrt(gamma/L) h)^L.                           (13)

Lee--Yang proves that (13) has only imaginary-axis zeros for ALL complex h.
There is no Gaussian limit in the accepting construction. The isolated-spin
bath replaces the Gaussian used in preliminary reconnaissance, and its fourth
and sixth cumulant corrections are retained in (9)--(12).

This is an existence certificate for at least one q_*, NOT a uniqueness theorem,
an optimized spin count, a fully tabulated irrational parameter, or a claim
that the eighth and higher theta moments already match. The source integrals,
finite algebra, and intermediate-value argument all need independent review.
A fixed six-moment match alone has NO RH consequence.

## 5. Complete source certificate and analytic error budgets

The checker does not evaluate zeta, gamma, or its zeros. It evaluates the
literal positive half-line density in Section 1 using 128-bit outward dyadics.
Pi is enclosed by Machin's formula with 110 alternating terms for each arctan.
For exp(x), range reduction makes |x/2^r|<=1/8; the 32-term Taylor polynomial
is widened by 2/(8^33 33!) and squared r times, all with outward rounding.
For x<=-128, the bound e>2 permits the enclosure [0,2^-128]; on the
negative half-line the exponential is 1-Lipschitz, which pays interval-input
width after one endpoint evaluation. Square roots use integer square-root
brackets. No binary64 arithmetic enters
acceptance.

For raw moments b_m=2 integral_0^infinity t^m phi(t)dt, m=0,2,4,6,8, compute
the first FOUR theta terms on [0,2] using composite Simpson with n=16384
uniform cells and step h=2/n. Every remaining theta index and t>2 is paid below.

Let P_0(Q)=4Q^2-6Q and

    P_(j+1)=2Q P_j'+(1/2-2Q)P_j,
    phi_n^(j)(t)=exp(t/2-Q_n(t)) P_j(Q_n(t)).              (14)

For the sum of the first four terms, define

    B_j=6 sum_(k>=1) |[Q^k]P_j| (k-1)!.

Since exp(t/2)<=e<3 on [0,2], substitution Q=pi n^2 exp(2t) proves that B_j
bounds the L1 norm of its jth derivative. The resulting exact B_0,...,B_4 are

    60, 366, 3135, 71463/2, 2044911/4.

Leibniz gives an L1 bound for the fourth derivative of t^m times that sum:

    C_m=sum_(j=0)^min(4,m) binom(4,j) m!/(m-j)! 2^(m-j) B_(4-j).

The Simpson Peano kernel on a two-cell block has absolute value at most h^4/72.
For example on [0,h] it is -u^3(4h-3u)/72 and the other half is reflected.
Therefore the error in the DOUBLE half-line moment is at most

    2h^4 C_m/72.                                         (15)

This is an integrated-derivative bound, not a guessed supremum of derivatives.
The checker generates the P_j recurrence, B_j and every error in (15).

For all integers m>=0, t^m<=m!exp(t) on t>=0. Thus

 2 integral_a^infinity t^m phi_n(t)dt
    <=4m! (pi n^2)^(-3/4) Gamma(11/4,pi n^2 exp(2a))
    <=4m! (Q_0^2+2Q_0+2) exp(-Q_0), Q_0=pi n^2 exp(2a).

The final inequality uses Q_0>=3 and bounds Q^(7/4) by Q^2; no incomplete-gamma
oracle is used. Since 3<pi<4, the complete omitted-index tail n>=5, even if
integrated from zero, is bounded by

    8m! *10202* exp(-75).                                (16)

Indeed each term is at most (16n^4+8n^2+2)exp(-3n^2), and the consecutive
ratio is less than 1/2 from n=5 onward. For the entire physical tail t>=2,
use 50<e^4<81 (elementary exponential series) to obtain

    8m! *105626* exp(-150).                               (17)

Here Q_0 is between 150n^2 and 324n^2; the same geometric bound starts at n=1.
Adding (16) and (17) double-counts some positive omitted mass, which is safe.
Their omission from the identity is not claimed. Divide the resulting raw
moment intervals by the positive raw b_0 interval to get moments of w; then
form A=3-b_4 b_0/b_2^2 and the full sixth cumulant, with outward arithmetic.

The finite graph probabilities in (7) are reconstructed from binomial integers
and rational q values or q intervals. The bath's exact finite cumulants are
used. An interval covering a continuum of q, not sampling 128 points, verifies
the signs and gamma bounds needed in the intermediate-value proof.

## 6. FMS4: an exact integer-square entry point via Villain cycles

Moment fitting alone does not explain WHY the exact theta sequence should be
ferromagnetically realizable. There is a source-level clue worth attacking.

For tau>0 let the circle heat kernel, in normalized angle measure, be

    K_tau(theta)=sum_(m in Z) exp(-tau m^2) exp(im theta)
               =sqrt(pi/tau) sum_(k in Z)
                   exp[-(theta+2pi k)^2/(4tau)].           (18)

It is positive and has mean one. On a finite oriented cycle with edge
parameters tau_e>0, integrate product_e K_(tau_e)(theta_u-theta_v) over all
angles using dtheta/(2pi). Each vertex imposes integer-current conservation,
so every edge current must equal one integer m. EXACTLY,

    Z_cycle(0)=sum_(m in Z) exp[-m^2 sum_e tau_e]
              =theta_Jacobi((sum_e tau_e)/pi).             (19)

Thus the literal integer-square theta spectrum, not merely a fitted positive
heat trace, is a zero-field partition function in a class having a Lee--Yang
theorem for its magnetic observable. This is standard Fourier/current algebra,
not a claim that (19) by itself proves RH.

More generally, add h sum_v a_v cos(theta_v), a_v>=0. Fourier expansion gives

    Z_G(h)=sum_(m in Z^E) exp(-sum_e tau_e m_e^2)
                product_v I_(div m(v))(a_v h),             (20)

where I_k is the integer-order modified Bessel coefficient of exp(z cos theta).
The identity follows by absolute convergence on every fixed compact h set.
The published Villain Lee--Yang theorem (Newman--Wu, Theorem 3) proves that
Z_G(h)/Z_G(0) has only imaginary-axis zeros as a function of the FIELD h.

The essential boundary is explicit: tau in (19) is a TEMPERATURE/edge parameter,
whereas h in (20) is a MAGNETIC FIELD. The theta density in Section 1 is a
particular differentiated and exponentially weighted function of log temperature.
Lee--Yang cannot be applied to that variable by renaming it. Derivatives,
conditioning on energies, and mixtures over temperatures need not preserve the
Lee--Yang property.

The ambitious source-specific task is to turn the exact current identity (19)
into a growing magnetic-observable realization with moments (5), or an equally
precise weak-limit identity for the WHOLE law w. This temperature-to-field
identification is OPEN. It is not a lemma supplied by positivity, duality, or
the new six-moment seed.

## 7. Research programme: construct the law, not its unknown zero set

The proof target is OPEN-FMS, or its weak-convergence version using finite Ising
or Villain magnetic observables. A satisfactory end-to-end result would have:

    a prescribed nonnegative-coupling construction
       -> convergence to the ACTUAL standardized theta law
       -> Lee--Yang closure / equation (4)
       -> xi has only critical-line zeros.

Only the middle source identification is unproved. This is not described as an
easy last step. It is a different difficult problem from symmetrizing K or
bounding an indefinite Weil form. Known spin-system positivity could consume
it without another spectrum-sign conjecture.

A practical investigation should use increasing interacting blocks, not freeze
the six-moment graph. Solve (5) at orders 8,10,12 with J>=0 and a>=0; certify
feasibility or isolate a graph-class obstruction; then look for a source-derived
extension rule in the integer-current representation. Fitting arbitrary
probability measures or polynomials with fitted real zeros would not supply
such a construction. A finite moment certificate is a starting instance, never
an induction.

Non-directed reconnaissance found that a single eight-spin block plus a Gaussian
fits moments through six. It motivated the FINITE bath repair above. A separate
16-spin/two-block restricted fit did not find a ten-moment match; that numerical
failure proves nothing. A two-independent-K8-plus-Gaussian scout did find a
near ten-moment match, but it is not certified and is not used in any theorem.
Those exploratory models do not establish global feasibility or rates.

An all-order Ising construction may fail even if RH is true: no converse from
RH to this ferromagnetic subclass is assumed. The new programme is worthwhile
because its finite building blocks bring a genuine independent global zero
location theorem. It should be judged by progress on source realization, not
by increasing counts of small fitted moments.

## 8. Reading and provenance boundary

- PR #834, source head 62bd9bbed134e20c1ee9cd92d008562079af9ceb: exact theta
  normalization and the metric obstruction motivate the pivot. The locally
  supplied parent proof and crowding proof were read. No new acceptance of their
  determinant/domain arguments or replay of their previous checkers is claimed.
- PR #296 at 4a68887f9f713aea7f63444030379fb864766a2d already mentions an
  all-order Lee--Yang assembly in a Brownian/Robin approach. Its live metadata
  was read, not its complete historical proof. This is not the first Lee--Yang
  mention in the repository. This packet instead requires literal finite
  ferromagnetic models and supplies a finite native-moment realization.
- Repository main f99d9e3908dde4865377c75d9ca051c1f545bf4f and AGENTS.md
  were checked. No exhaustive all-branch audit was performed in this pass.
- C. M. Newman and W. Wu, Lee--Yang Property and Gaussian Multiplicative Chaos,
  Commun. Math. Phys. 369 (2019), 153--170, arXiv:1708.08820v3: finite weighted
  Ising theorem in the introduction, Villain Theorem 3, closure Theorem 7,
  product Proposition 13. These are imported published mathematics. Relevant
  statements and proof discussion were read, with page images for pages 1,4;
  a further screenshot failed. The entire literature is not re-reviewed.
- C. M. Newman and W. Wu, Constants of de Bruijn--Newman type in analytic number
  theory and statistical physics, Bull. Amer. Math. Soc. 57 (2020), 595--614,
  arXiv:1901.06596: theta convention and historical Lee--Yang/RH connection,
  especially Sections 2.1 and 2.5. No priority claim is made for that connection.

The finite integer computation certifies the explicit inequalities used in
FMS3, conditional on the written analytic remainder proof and correct execution.
It does not machine-prove Lee--Yang, Hurwitz, OPEN-FMS, or RH. All newly proposed
statements require independent mathematical and code review.

# DG26: degree growth, positive trace, and a sparse RH criterion

Status: **PROPOSED component proofs, pending independent mathematical review.**
The subpower estimate at the end is OPEN. This is not a completed RH proof.
Date: 2026-09-12. No numerical zero data or conjectural cancellation is used
in an unconditional assertion.

The source is the odd-polynomial problem in PR845, AC28--29. The new point is
to replace its stronger uniform-in-degree, positive-eta premise by a growing
finite-degree norm, or one positive scalar trace. Subpower growth of either,
even along an arbitrary unbounded subsequence, is RH-equivalent. We prove
that implication quantitatively. We do NOT prove the subpower upper bound.

Classical inputs are named where used. Orthogonal-polynomial approximation,
Mellin continuation and RH criteria involving reciprocal even-zeta values
have substantial prior literature. No priority claim is made for that general
architecture. The exact sequence and quantitative composition below are the
proposed objects. The new criterion does not promote any predecessor claim.

## 0. Fixed source, norms, and finite-degree quantities

Let mu be the ordinary Mobius function, restricted to odd integers in sums.
Put m(x)=sum_(n<=x, odd) mu(n)/n, zero below 1, and

    Z(s)=(1-2^(-s))zeta(s),       a(s)=(s-1)Z(s).

The pole of Z at 1 is canceled in a, with a(1)=1/2. For an odd polynomial p,

    Q_p(t)=sum_(n>=1, odd) p(t/n)/n,
    A p(t)=t Q_p'(t),                         0<t<1,
    E p(t)=Q_p(1)-sum_(n>=3, odd) p(t/n)/n,    1<t<3.

All these series and their derivatives converge absolutely for a fixed
polynomial. Norms of p and Ap are on (0,1); the norm of Ep is on (1,3).
Complex coefficients are permitted and all norm pairings are Hermitian.
Let Pi_N=span{t,t^3,...,t^(2N-1)}, N>=1. A is a bijection on Pi_N, since its
monomial multipliers are r Z(r+1)>0 for positive odd r.

Define the finite best constant WITHOUT the parent eta penalty:

    Lambda_N = sup_(0!=p in Pi_N) ||Ep||^2/||Ap||^2.       (0.1)

It is finite in every dimension. It is NOT asserted bounded independently
of N. In fact Section 6 proves Lambda_N >= c log N eventually, with some
positive c. A factor four converts (0.1) to the parent's C at eta=0.

Write P_l for the usual Legendre polynomial, P_l(1)=1. The functions

    phi_j(t)=sqrt(4j+3) P_(2j+1)(t), j=0,1,...,

are a complete orthonormal system in L2(0,1). Completeness follows by odd
extension to (-1,1) and ordinary polynomial density. Define the operator K
on odd polynomials and its positive scalar trace by

    (Kf)(t)=integral_0^1 m(t/u) f(u)du/u,       1<t<3,
    S_N=sum_(j=0)^(N-1) ||K phi_j||^2.                   (0.2)

The integral converges at zero because f(u)=O(u) and |m|<=2. These are finite
restrictions, not an assumed bounded operator on all of L2(0,1).

## 1. DG26-1: exact inverse-coordinate identity and finite scalar formulas

For EVERY odd polynomial p,

    E p = K(Ap).                                        (1.1)

### Proof retaining the endpoint

Put q=Q_p and f=tq'. Finite monomial comparison, using the absolutely
convergent Euler product at even integers, gives

    p(t)=sum_(n>=1, odd) mu(n)q(t/n)/n,
    q(t)=integral_0^t f(u)du/u.

For 1<=t<=3 this implies

    Ep(t)=q(1)+sum_(n>=3, odd) mu(n)q(t/n)/n.

For u<t/3 the aggregate coefficient of f(u)/u is m(t/u); for u>t/3 it
is 1, which is also m(t/u) because 1<=t/u<3. Interchange is legitimate:
|q(t/n)|=O(1/n), so the sum of absolute integrals is finite. This proves
(1.1), including the contribution q(1). Endpoints have no norm effect.

It follows that Lambda_N=||K|Pi_N||_op^2, and

    0<Lambda_N<=S_N.                                    (1.2)

For a positive odd r the exact output polynomial is

    K(t^r)=[1+(1/Z(r+1)-1)t^r]/r.                       (1.3)

Consequently both Lambda_N and S_N are computable using only the N even-zeta
values Z(2),...,Z(2N). The matrix is not sampled in t: its entries are exact
integrals of these output polynomials. For r_i=2i+1, h_i=1/Z(r_i+1)-1 and
J_r=(3^(r+1)-1)/(r+1), the monomial output Gram is

    M_ij=[2+h_i J_(r_i)+h_j J_(r_j)+h_i h_j J_(r_i+r_j)]/(r_i r_j). (1.4)

Every cross term is present. Congruence by the Legendre coefficient matrix
and its known diagonal input Gram gives the same constants. S_N is the trace
in the ORTHONORMAL phi basis, not the trace in unnormalized monomials.

Let K_N=K composed with projection onto Pi_N; this is a bounded finite-rank
map on L2(0,1). Its output-side covariance satisfies the exact positive update

    K_(2N) K_(2N)^* = K_N K_N^*
                     +sum_(j=N)^(2N-1) (Kphi_j) tensor (Kphi_j)^*. (1.5)

This identity uses orthogonal INPUT coordinates. It does not say outputs
from different bands are orthogonal, or omit polarized terms in an individual
output norm. S_(2N)-S_N is exactly the trace of the positive added operator.

## 2. DG26-2: an all-degree upper bound and the conditional source exponent

If, for some 1/2<beta<=1 and M_beta<infinity,

    |m(x)|<=M_beta x^(beta-1) for all x>=1,               (2.1)

then for N>=2, d=2N-1,

    Lambda_N <= S_N <= M_beta^2 I_beta C_beta^2 d^(2beta-1), (2.2)
    I_beta=(3^(2beta-1)-1)/(2beta-1),
    C_beta=9/(2-beta)+1/sqrt(2beta-1).

In particular the elementary bound |m|<=2 proves, unconditionally,

    Lambda_N <= S_N <= 800(2N-1), N>=1.                 (2.3)

The N=1 case follows directly from (1.3) or the elementary estimate
||K(t)||^2<=8 and ||t||^2=1/3. No fixed power saving is obtained here.

### 2.1 A polynomial boundary bound

For every odd polynomial f of degree at most d,

    |f(u)|<=9d^(3/2) u ||f||,       0<=u<=1/2.          (2.4)

Here is a proof with explicit nonoptimal constants. The classical Laplace
integral (DLMF 18.10.5) is

    P_l(t)=(1/pi)integral_0^pi (t+i sqrt(1-t^2)cos v)^l dv.

For |t|<=1/2 the bracket z has |z'|<2 and
|z|^2<=1-(3/4)sin^2 v. For m>=1, sin v>=2v/pi on [0,pi/2] and Gaussian
integration show

    (1/pi)integral_0^pi |z|^m dv
       <=sqrt(2pi/(3m))<3/(2sqrt(m)).

Thus |P_l'|<=3l/sqrt(l-1)<=5sqrt(l) for l>=2; l=1 is direct.
The normalized odd derivative is at most 9l. Cauchy--Schwarz and
sum_(l odd,l<=d) l^2<=d^3 give |f'|<=9d^(3/2)||f|| on the middle interval.
Integrating from f(0)=0 proves (2.4). This argument also gives

    (sum_(j<N)|phi_j(u)|^2)^(1/2)<=9d^(3/2)u.            (2.5)

### 2.2 The estimate controls the WHOLE trace, not merely each column

Put delta=1/d<=1/2 and split K_N at input u=delta. The low-u part is an
integral of rank-one maps, so the Hilbert--Schmidt triangle inequality,
(2.1) and (2.5) give

    ||K_N^(low)||_HS
       <= M_beta sqrt(I_beta) 9d^(3/2)
                                   integral_0^delta u^(1-beta)du
       = M_beta sqrt(I_beta) [9/(2-beta)] d^(beta-1/2).

The high-u kernel is square integrable. Orthogonal projection in the input
cannot increase its Hilbert--Schmidt norm; hence

    ||K_N^(high)||_HS
       <=M_beta sqrt(I_beta)
                            (integral_delta^1 u^(-2beta)du)^(1/2)
       <=M_beta sqrt(I_beta) d^(beta-1/2)/sqrt(2beta-1).

Add the two norms and square. Since ||K_N||_HS^2=S_N, this proves (2.2).
In particular no extra factor N is lost by bounding columns separately.

For completeness, |m|<=2 follows from the exact divisor identity for the
all-integer sum m_all. The fractional-part identity gives |m_all(x)|<=1;
then m(x)=sum_(j>=0)2^(-j)m_all(x/2^j), a finite sum, gives the bound 2.

### 2.3 RH gives subpower trace growth; classical input explicitly imported

Assume RH. The classical Littlewood RH-to-Mertens theorem gives
M_all(x)=O_epsilon(x^(1/2+epsilon)) for every epsilon>0. We use this established
theorem, not claim a new proof of it. Separate the even terms to obtain
M_odd(x)=sum_(2^j<=x)M_all(x/2^j)=O_epsilon(x^(1/2+epsilon)).
Partial summation and the Abel limit 1/Z(s)->0 as s down to 1 give
m(x)=O_epsilon(x^(-1/2+epsilon)). Apply (2.2) with arbitrarily small positive
epsilon. Therefore

    RH => S_N=N^o(1), and Lambda_N=N^o(1).               (2.6)

The assertion means an upper bound O_epsilon(N^epsilon) for EVERY epsilon.
It is not a bound uniform in epsilon. The converse is proved below.

## 3. DG26-3: a degree-rate upper bound excludes zeros globally

If for some 0<=r<1 one has Lambda_N=O(N^r) for all N, then

    zeta(s)!=0 whenever Re(s)>(1+r)/2.                  (3.1)

No height cutoff or assumption of simple zeros is involved.

### 3.1 Exact Mellin coefficients and their decay

For Re(s)>0 set

    c_j(s)=integral_0^1 t^(s-1)phi_j(t)dt
      =sqrt(4j+3) prod_(k=1)^j(s-2k)/prod_(k=0)^j(s+2k+1). (3.2)

This formula needs no numerical gamma values. Indeed monomial integration
makes the unnormalized integral a rational function with denominator
prod_(k=0)^j(s+2k+1). Its numerator has degree at most j and vanishes at
s=2,4,...,2j by Legendre orthogonality. Its leading coefficient is one because
P_(2j+1)(1)=1 (equivalently the sum of its monomial coefficients is one).
This proves (3.2). It also follows from Rodrigues and beta integration.

On every compact set in Re(s)>0,

    |c_j(s)|<=C_K(j+1)^(-Re(s)).                         (3.3)

For large j, uniformly on that compact, the log of the absolute successive
ratio in (3.2) equals -Re(s)/(j+1)+O_K((j+1)^(-2)). Sum this estimate.
Initial finitely many indices are harmless; at a positive even integer the
sequence instead eventually vanishes. This also proves uniformity in s.

### 3.2 Convergence in the actual output space

For sigma=Re(s)>1/2, t^(s-1) belongs to L2(0,1) and has these coefficients.
On each dyadic block N<=j<2N, (3.3) and the assumed operator bound give

    ||K sum_(j=N)^(2N-1)c_j(s)phi_j||
      <=sqrt(Lambda_(2N)) (sum_(j=N)^(2N-1)|c_j(s)|^2)^(1/2)
      <=C_K N^((1+r)/2-sigma).

Consequently the dyadic projected outputs converge normally to an L2(1,3)
valued holomorphic function F(s) on Re(s)>(1+r)/2. No infinite bounded K on
unweighted L2 has been presumed.

For Re(s)>4, the Legendre series and its derivative converge absolutely
uniformly on [0,1]. For example the classical expansion
P_l'=(2l-1)P_(l-1)+(2l-5)P_(l-3)+... and |P_l|<=1 give
||phi_j'||_infinity=O((j+1)^(5/2)); (3.3) is enough. The limit is t^(s-1),
by L2 uniqueness. Since |m|<=2, K is continuous from C1 functions vanishing
at zero to L2(1,3), with norm at most 2sqrt(2) in the derivative sup norm.
Thus F(s)=K(t^(s-1)) there.

Direct Mellin integration, initially on Re(s)>1, gives

    K(t^(s-1))(t)=[Z(s)+(1-Z(s))t^(s-1)]/[(s-1)Z(s)].   (3.4)

To check the endpoint: substitute x=t/u in (0.2), use
integral_1^infinity m(x)x^(-s)dx=1/[(s-1)Z(s)], and subtract integral_1^t
where m=1. The numerator b_s(t)=t^(s-1)-Z(s)(t^(s-1)-1) extends holomorphically
through s=1. The identity theorem therefore gives a(s)F(s)=b_s throughout
the stated half-plane. A zero rho of Z there would give 0=t^(rho-1) in
L2(1,3), which is impossible. This proves (3.1).

For example, proving ANY r<1 in this theorem gives a fixed power zero-free
strip, not RH unless r can approach zero. We have NOT proved such an r.

## 4. DG26-4: every off-critical zero forces power growth at ALL large degrees

The all-degree upper assumption in Section 3 can be weakened to an arbitrarily
sparse unbounded sequence if its exponent tends to zero. The needed point is
a quantitative polynomial approximation, not monotonicity alone.

If rho is a hypothetical zeta zero with 1/2<beta=Re(rho)<1, then there are
c_rho>0 and N_rho<infinity such that

    Lambda_N >= c_rho N^((2beta-1)/10) for EVERY N>=N_rho. (4.1)

No such zero is asserted to exist. The exponent 1/10 is deliberately not
optimized. Constants depend on the zero, including its imaginary part.

### 4.1 Complete cutoff identity (the AC29 boundary mechanism)

We rederive the specific ingredient of PR845/AC29 used here. Let chi(v) be
0 for v<=1, 3(v-1)^2-2(v-1)^3 for 1<v<2, and 1 for v>=2. For
0<Re(s)=beta<1, define f_(s,e)(t)=t^(s-1)chi(t/e), 0<e<1/2. It is C1 on
[0,1] and zero near zero. Put d_o(x)=floor((x+1)/2)-x/2, |d_o|<=1/2.
Euler summation on the finite sum gives exactly

    Q_f(t)=c_s e^(s-1)+Z(s)t^(s-1)+t^(s-1)R_s(t/e),    (4.2)
    R_s(v)=integral_0^infinity d_o(x)x^(-s-1)
                     [s(chi(v/x)-1)+(v/x)chi'(v/x)]dx.

Here c_s=(1/2)integral_0^infinity y^(-s)chi(1/y)dy. In deriving (4.2), write
d floor((x+1)/2)=dx/2+dd_o and integrate the latter by parts. The uncut
term is Z(s)=s integral_0^infinity d_o(x)x^(-s-1)dx in this strip; this follows
from the usual Euler formula by splitting at 1 and analytic continuation.
Both boundary terms vanish. The remainder integrand is zero for x<v/2.
Using |chi'|<=3/2, |chi''|<=6 gives the COMPLETE bounds

    |R_s(v)|<=K0 v^(-beta), |vR_s'(v)|<=K1 v^(-beta),
    K0=2^(beta-1)(|s|+3)/beta,
    K1=2^(beta-1)(3|s+1|+24)/beta,
    K=|s-1|K0+K1.                                       (4.3)

The derivative bracket is (s+1)(v/x)chi'+(v/x)^2 chi'', supported on
[v/2,v]. These bounds include the whole infinite x-tail. The large first
term of (4.2) is constant in t: it cancels in BOTH A and E.

At s=rho with Z(rho)=0 and delta=beta-1/2>0, (4.2)--(4.3) give

    ||A f_(rho,e)|| <= K e^delta,
    ||E f_(rho,e)-t^(rho-1)|| <=2sqrt(2)K0 e^beta.        (4.4)

The first bound follows by bounding the derivative remainder by K e^beta/t
on t>=e; it is zero below e. No assertion of closability of an unspecified
operator is involved.

### 4.2 Quantify the degree, not just density

For any C1 function g with g(0)=0 and derivative Lipschitz constant L,
let h(x)=g'(sqrt(x)). It is Holder-1/2 with constant L. Its degree-M Bernstein
polynomial h_M satisfies

    ||h_M-h||_infinity <= L(4M)^(-1/4),                 (4.5)

because E|S/M-x|^(1/2)<=(Var(S/M))^(1/4), S binomial(M,x).
The primitive p_M(t)=integral_0^t h_M(u^2)du is odd, of degree <=2M+1.
If its derivative error is d, direct absolute dilation summation gives

    ||p_M-g||<=d/sqrt(3),
    ||A(p_M-g)||<=5d/(4sqrt(3)),
    ||E(p_M-g)||<=2sqrt(2)d.                             (4.6)

Use Z(2)<5/4; these are C1 error controls, not the false comparison between
weighted and unweighted derivative L2 norms in PR861.

For g=f_(rho,e), its derivative is globally Lipschitz with

    L <= L_rho e^(beta-3),
    L_rho=|rho-1||rho-2|+3|rho-1|+6.                    (4.7)

This follows by differentiating on each smooth piece; g' is continuous at
both transition endpoints. Choose e=M^(-1/10), M>2^10. Equations (4.5)--(4.7)
make d=O_rho(M^(-delta/10)). Equation (4.4) has precisely the same derivative
rate. Therefore the resulting p_M in Pi_(M+1) satisfies

    ||Ap_M||=O_rho(M^(-delta/10)),
    Ep_M -> t^(rho-1) in L2(1,3).                      (4.8)

The limiting norm is positive. Since A is injective on polynomials, (4.8)
gives Lambda_(M+1)>=c_rho M^(delta/5), for every sufficiently large M.
Changing the constant proves (4.1). The approximating polynomial depends on
the hypothetical zero, but it is a genuine finite odd polynomial at EVERY
large degree budget. This is not a subsequence manufactured by ignoring
uncontrolled indices.

## 5. DG26-5: a weaker end-to-end target than uniform polynomial coercivity

The following are equivalent:

    (i) RH;
    (ii) S_N=O_epsilon(N^epsilon) for every epsilon>0;
    (iii) Lambda_N=O_epsilon(N^epsilon) for every epsilon>0;
    (iv) liminf_(N->infinity) log(1+Lambda_N)/log N=0;
    (v) liminf_(N->infinity) log(1+S_N)/log N=0.          (5.1)

In particular it is enough to exhibit an unbounded sequence N_j and actual
upper certificates S_(N_j)<=N_j^(epsilon_j), with epsilon_j->0. A fixed finite
set of certificates, even with a large margin, is not that theorem.

Proof: (i)->(ii) is (2.6), with the classical RH-to-Mertens dependency stated
there. Inequality (1.2) and positivity give the immediate implications to
(iii), (iv), and (v). Either lower-limit condition contradicts (4.1) if an
off-critical zero exists. The classical zero-free region Re(s)>=1 and
functional-equation symmetry reduce false RH to a zero 1/2<Re(s)<1.
This proves the converses. Alternatively, the all-N condition (iii) implies
RH directly by Section 3. There is no assumption of simple zeros.

The original Q-AC28 asked for a bounded C_eta at EVERY degree, for each fixed
eta. Its truth implies RH and hence (5.1), but necessity of that ORIGINAL
premise is not established here. We are replacing it by a different,
RH-equivalent degree-growth target, not proving its uniform constants exist.

## 6. DG26-6: the finite-degree constants really must grow

Unconditionally, using the classical existence of one critical-line zero,

    Lambda_N >= c log N, hence S_N>=c log N,
                           for all sufficiently large N, (6.1)

with some c>0. No numerical value of c or the threshold is certified here.
This is an all-N lower theorem, not an inference from the finite matrices.

Let rho=1/2+i gamma be such a zero. Average the cutoffs from Section 4:

    F_R(t)=(1/R)integral_R^(2R) f_(rho,exp(-v))(t)dv.

For t fixed away from zero, EF_R tends to t^(rho-1). Quantitatively (4.3)
gives ||EF_R-t^(rho-1)||=O_rho(exp(-R/2)). Also

    ||AF_R||<=2K/sqrt(R).                               (6.2)

To verify (6.2), put t=exp(-x). After the L2-isometric multiplication by
exp(-x/2), the averaged error is, up to a unit phase, convolution of
R^(-1)1_[R,2R] with a one-sided kernel bounded by K exp(-w/2).
Its L1 norm is at most 2K; Young's inequality gives (6.2). All cutoff cross
terms are retained by this convolution estimate, not assumed orthogonal.

The derivative of F_R is Lipschitz with constant at most L_rho exp(5R), by
(4.7) and averaging. Use its Bernstein primitive of order M and choose
R=(log M)/24. Its derivative error is O_rho(exp(-R)), by (4.5). Consequently

    ||Ap_M||=O_rho(R^(-1/2)),
    ||Ep_M|| -> sqrt(log3)>0,
    p_M in Pi_(M+1).

This proves Lambda_(M+1)>=c_rho R for all large M, hence (6.1).
Higher multiplicity is allowed; no additional multiplicity exponent is
claimed. The classical existence of the zero is the only zero input.

Thus a uniform bound such as S_N<4, or Lambda_N<4, is FALSE at all degrees,
regardless of the apparent boundedness of the first finite certificates.
Permitting growth in (5.1) is necessary, not merely a concession to numerical
conditioning.

## 7. Direct attempt at closure and the missing arithmetic step

The exact finite trace suggests the positive increment

    d_N=S_(2N)-S_N=sum_(j=N)^(2N-1)||Kphi_j||^2.          (7.1)

If d_N were bounded by a fixed power of log N on all sufficiently large
dyadic N, summation would give a polylogarithmic S_N and complete (5.1).
A subpower upper bound for these increments is enough as well. Neither
estimate is proved. The elementary source bound in Section 2 gives only
O(N), and the stronger source estimate used to reach subpower was explicitly
CONDITIONAL on RH. Substituting that estimate here would be circular.

We also tried applying the new collision-diagonal bound from PR848. Its
object is an ALL-INTEGER, coalesced Newton product source, not these odd
Legendre outputs. Even there the signed distinct-product covariance remains
open. Its positive diagonal cannot be imported as a bound for (7.1), and no
source-preserving finite-index adapter is supplied here.

The original unweighted derivative estimate controls the wrong norm; PR861's
published cutoff family proves that adding a fixed input-norm correction
does not repair that route. The current C1 approximation bounds are used
only for constructing finite tests, never as that false L2 comparison.
The recent centered-gamma and branching results control each fixed stage's
high-height tail, not a joint degree/stage limit. The Ising ten-moment
realization does not control the infinitely many moments in (5.1). No one
of those open arrows is silently supplied by this manuscript.

The positive result of this pass is a global, source-faithful degree-growth
criterion, its sparse-sequence justification, quantitative zero-exclusion
and zero-imposed growth bounds, and an unconditional finite-degree ceiling.
The missing result remains a genuinely subpower upper bound for the ACTUAL
sequence S_N or Lambda_N. No full RH proof, fixed power saving, new zero-free
region or uniform Q-AC28 estimate has been obtained.

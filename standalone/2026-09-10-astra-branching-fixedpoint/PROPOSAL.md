# BSR26: strip-preserving branching renormalization of the Xi source

Date: 2026-09-10. Status: **new research synthesis and proposed component proofs;
independent mathematical/code review required. RH IS NOT PROVED.**

The unproved target is zero-free-strip preservation along one prescribed
positive stochastic orbit, or zero-safe approximate fixed points of the same
map. The contraction, source identification, gamma starting-family theorem,
and finite residual certificates below do not prove that preservation.

The Brownian law and its distributional fixed-point equation are CLASSICAL:
Biane--Pitman--Yor [BPY], Proposition 1 and equation (45). PR #296 already uses
the Brownian/gamma source, but a different cutoff/Robin construction. PR #842
uses finite ferromagnets and all-order theta moment matching. This proposal
joins these directions through a quantitative fixed-point residual and uses a
weaker strip-only zero class. It claims no priority for smoothing transforms,
Wasserstein contraction, Mellin symmetrization, gamma functions, or Hurwitz.

## 1. Change the proof mechanism, not the original function

Instead of controlling an increasingly ill-conditioned inverse or proving
another equivalent positivity tower, specify a positive nonlinear map whose
UNIQUE normalized fixed law encodes the actual Xi function. Identify the limit
by contraction; prove its zero geometry by an invariant class.

Let T act on probability laws on [0,infinity), with mean one and finite second
moment, by

    T(nu) = Law((X_1+X_2)/U^2),                            (1)

where X_1,X_2 are independent with law nu, and U is uniform on [1,2], independent
of both. The SAME U multiplies both siblings. Using separate U's gives a
different map. Probability is a constructive representation here, not an
assumption that ordinary primes or Mobius signs behave randomly.

Put

    a_j = integral_1^2 u^(-2j)du
        = (1-2^(1-2j))/(2j-1), j>=1;  a_0=1,
    r = 2a_2 = 7/12,  c = sqrt(7/12) < 4/5.             (2)

We use W_2 for the quadratic Wasserstein distance on this half-line.

### BSR1: a strict global contraction with the actual Xi law as fixed point

For every two mean-one finite-second-moment laws,

    W_2(T(nu),T(eta)) <= c W_2(nu,eta).                 (3)

The unique fixed law is that of

    X_* = (6/pi^2) sum_(j>=1) E_j/j^2,
    E_j independent exponential random variables of mean one.             (4)

It has mean one, variance 2/5, and Laplace transform

    psi_*(t)=sqrt(6t)/sinh(sqrt(6t)), t>=0, psi_*(0)=1. (5)

No zeta zero is an input to (1), (4), or the construction of its iterations.

Proof of (3). Couple X with Y optimally, take two independent copies of the
coupled pair, and use the same independent U. Since E(X-Y)=0, the mixed term
in E[(X_1-Y_1+X_2-Y_2)^2] vanishes. The resulting squared coupling cost is
2a_2 W_2(nu,eta)^2. This proves the inequality. The nonnegative mean-one
finite-second-moment class is closed in W_2, hence complete. In particular
any fixed point is unique.

The series in (4) converges almost surely and in L2, by positivity, summable
means, and summable variances. Its mean and variance follow from the classical
Euler sums at 2 and 4. The product for sinh gives (5). One may verify its
fixed-point identity WITHOUT Mellin continuation or RH: if b=sqrt(6t)>0,

 integral_1^2 psi_*(t/u^2)^2 du
   = b integral_(b/2)^b csch(v)^2 dv
   = b[coth(b/2)-coth(b)] = b/sinh b.

Thus the distributional identity follows by Laplace uniqueness. The same
identity, before mean normalization, is BPY (45); it is not a new identity.

## 2. Exact whole-source binding and the reflected Mellin transform

For any strictly positive mean-one law nu with finite second moment take two
independent copies and define

    V_nu=(pi/6)(X_1+X_2),
    M_nu(s)=E[V_nu^(s/2)],
    H_nu(s)=[M_nu(s)+M_nu(1-s)]/[2(1+M_nu(1))].       (6)

These functions are holomorphic on 0<Re s<1. Holomorphy on its compact
substrips follows from x^a |log x|^j bounds, using a>0 near zero and exponent
strictly less than one at infinity. At the real endpoints define M(0)=1;
then H(0)=H(1)=1/2, and H(s)=H(1-s), H(conjugate s)=conjugate H(s).
No arbitrary scaling of V is permitted: the factor pi/6 is essential.

BPY Proposition 1 gives exactly

    E[V_*^(s/2)] = 2 xi(s),  ALL complex s,
    xi(s)=(1/2)s(s-1)pi^(-s/2)Gamma(s/2)zeta(s),        (7)

with analytic removals at 0 and 1. Indeed their Sigma_2=(2/pi^2)sum Gamma_2/j^2
and Y^2=(pi/2)Sigma_2 give V_*=Y^2; the proposition says E Y^s=2xi(s).
In particular M_*(1)=1 and H_*=xi, not a nonzero multiple with an unknown
prefactor. We import this classical complete source identity explicitly.

There is also an exact link to #842's theta-law programme. For u=(1/2)log V,
form the symmetric law whose integrals are

    E_mu g = E[V^(1/4)(g(u)+g(-u))]/[2E V^(1/4)].      (8)

Then its moment-generating function on its domain is

    E_mu exp(h u)=H_nu(1/2+h)/H_nu(1/2).

At the fixed point this is xi(1/2+h)/xi(1/2), exactly the normalized
UNSTANDARDIZED full theta law. This is a positive tilted pushforward, not a
claim that an arbitrary such pushforward satisfies Lee--Yang. The variance
2/5 below is a variance of X_*, not the variance of this log-theta law.

### BSR2: one local distributional residual certifies source convergence

Let

    D(nu)=W_2(nu,T(nu)).

Then

    W_2(nu,nu_*) <= D(nu)/(1-c) <5D(nu).               (9)

For s=sigma+it with 0<sigma<1, put e=5D(nu). The COMPLETE Mellin estimate is

 |H_nu(s)-xi(s)| <= (1/2)[
       (|s|/sigma)e^(sigma/2)
       +(|1-s|/(1-sigma))e^((1-sigma)/2)+e^(1/2)].    (10)

Zero residual is interpreted by continuity. In particular D(nu_j)->0 implies
H_nu_j -> xi locally uniformly throughout the open critical strip. No separate
higher-moment, inverse-moment, or uncomputed-tail premise is needed for (10).

Proof. The triangle inequality and (3) give (9). Couple independent pairs
of mean-one laws optimally. The equal means again cancel the mixed error:

 W_2(V_nu,V_*) <= pi/(3sqrt(2)) W_2(nu,nu_*) <5D(nu).

For complex p with 0<a=Re p<1 and real x,y>0, integrate p t^(p-1) along
the real segment to obtain

    |x^p-y^p| <= (|p|/a)|x-y|^a.

Jensen/Hölder therefore bounds the expectation difference by (|p|/a)e^a.
Apply this with p=s/2, (1-s)/2, and 1/2. Also |2xi(s)|<=1 on the CLOSED
critical strip by (7) and Hölder between E Y^0=E Y^1=1. Subtract the ratios
in (6), keeping their denominators, and use 1+M_nu(1)>=1. This gives (10).
The displayed normalizing error is not dropped.

Consequently the following is a valid CONDITIONAL ending:

  D(nu_j)->0 AND every H_nu_j is zero-free in both
  {0<Re s<1/2} and {1/2<Re s<1}  ==> RH.              (OPEN-BSR)

Hurwitz applies in each connected open half-strip (exhaustion by compact
sets). The limit is not identically zero, since it is positive at real
interior points by (7). The classical zero-strip theorem and reflection identify these strips as
the only possible off-line zero region (including the established exclusion
of zeros on Re s=1).
Neither existence of such zero-safe approximate fixed points nor preservation
of their zero geometry is asserted by (9) or (10).

## 3. A whole-strip zero theorem for a starting FAMILY, not a finite zero scan

Take X~Gamma(k, rate k), for ANY real k>=1. Then mean X=1 and

    M_k(s)=(pi/(6k))^(s/2) Gamma(2k+s/2)/Gamma(2k).

Let H_k be its symmetrization and normalization (6).

### BSR3: Gamma starting laws are zero-safe throughout the critical strip

For every real k>=1, every zero of H_k in 0<Re s<1 is on Re s=1/2.
Moreover there is NO zero on 0<=Re s<=1, |Im s|<=4.

This is a proposed complete analytic theorem. It is NOT a claim of entire
Lee--Yang membership: gamma factors have poles outside this strip, and the
statement is intentionally confined to its actual holomorphic domain.

### 3.1 One explicit digamma remainder

For Re z=a>0 the classical digamma integral, obtained also by differentiating
Binet's formula, gives

 psi(z)=log z-1/(2z)-integral_0^infinity e^(-zt)
             [(1/2)coth(t/2)-1/t]dt.

The bracket lies strictly between 0 and t/12. For completeness, coth x>1/x
follows from (x cosh x-sinh x)'=x sinh x>0. The upper bound coth x<1/x+x/3
follows from ((1+x^2/3)sinh x-x cosh x)'=(x/3)(x cosh x-sinh x)>0.
Thus

    |psi(z)-log z+1/(2z)| <=1/(12a^2).                  (11)

The logarithm is the principal analytic one in the right half-plane. The
logarithm of Gamma is continued there from its real positive values.

### 3.2 A uniform phase bound at small height

Write f(s)=M_k(s), c_k=pi/(6k), a=2k+sigma/2. At 0<=sigma<=1, 0<=t<=4,

 arg f(sigma+it)=integral_0^(t/2) [log c_k+Re psi(a+iu)]du.

Here 2k<=a<=2k+1/2 and 0<=u<=2. Since k>=1,

 c_k |a+iu| <= (pi/6)sqrt((5/2)^2+4)<143/84.

Using log v<=v-1 and (11), the integrand is at most

    59/84+1/48 =243/336.

It is at least -1/(4k)-1/(48k^2)>=-13/48, since c_k a>=pi/3>1.
Consequently

    -13/24 < arg f(sigma+it)<243/168<3/2<pi/2.

Conjugation gives the same absolute-sector conclusion at negative height.
Both f(s) and f(1-s) have positive real part in this rectangle. Their sum
cannot vanish. All logarithmic branches in the phase argument are fixed.

### 3.3 Modulus separation at all higher heights

For |t|>=4 differentiate the log-modulus ratio:

 d/dsigma log|f(sigma+it)/f(1-sigma-it)|
 =log c_k +(1/2)Re[psi(2k+sigma/2+it/2)
                    +psi(2k+(1-sigma)/2-it/2)].       (12)

By (11) this is bounded below by

    log(pi/3)+(1/2)log(1+1/k^2)-1/(4k)-1/(48k^2).

Put x=1/k in (0,1]. The elementary bounds pi>25/8,
log(25/24)>1/25, and log(1+x^2)>=x^2-x^4/2 show that this is strictly greater
than

    P(x)=1/25-x/4+23x^2/48-x^4/4.                      (13)

P is positive on [0,1]. A complete rational certificate is its Bernstein
representation of degree four on the FOUR CLOSED quarter intervals. In order,
its five coefficients on those intervals are

 [1/25,39/1600,1583/115200,311/38400,497/76800],
 [497/76800,31/6400,833/115200,81/6400,23/1200],
 [23/1200,493/19200,3833/115200,1/25,1099/25600],
 [1099/25600,587/12800,5183/115200,359/9600,23/1200].

Every coefficient is strictly positive. Expanding each degree-four Bernstein
basis gives (13) exactly; partition endpoints are retained. This is a
continuum polynomial proof, not positive sample values.

At sigma=1/2 the ratio in (12) has modulus one by conjugation. Its strictly
positive derivative makes the modulus greater than one for sigma>1/2 and
less than one for sigma<1/2. Therefore f(s)+f(1-s) cannot vanish off that line.
Together with the low-height argument this proves BSR3, without a zero census.

## 4. A concrete positive orbit with the correct mean and variance from day one

Use the specific starting law

    nu_0=Gamma(5/2, rate 5/2),     nu_(n+1)=T(nu_n).    (14)

This is not selected by fitting zeta zeros. Its mean one and variance 2/5
are exactly those of the Brownian fixed law. The moment recurrence

    m_(j,n+1)=a_j sum_(i=0)^j binom(j,i)m_(i,n)m_(j-i,n)              (15)

preserves BOTH those moments at every step. All integer moments of every
finite stage are rational and computable from (15). In particular

    m_(3,n)=93/35-(24/175)(31/80)^n.                     (16)

The fixed third moment is 93/35, not the gamma starting moment 63/25.
Already the first iterate has third moment 651/250, so it is NOT another
Gamma(5/2,5/2) law. No gamma law is the fixed point: its variance would force
k=5/2 and its third moment would then be wrong. A genuine enlarged invariant
class, not reusing the gamma seed formula unchanged, is required.
More generally every FIXED positive integer moment has an effective rational
bound |m_(j,n)-m_j^*|<=C_j(31/80)^n for j>=3. Here is a constructive proof,
not a fit. Put U_0=U_1=1, U_2=7/5 and choose recursively

 U_j=max(m_(j,0), a_j/(1-2a_j)*sum_(i=1)^(j-1) binom(j,i)U_i U_(j-i)).

These bound all moments and their fixed limits. Set C_0=C_1=C_2=0,
C_3=24/175, and for j>=4 choose

 C_j=|m_(j,0)-m_j^*|
    + a_j/(31/80-2a_j)*sum_(i=1)^(j-1) binom(j,i)
                                  [C_i U_(j-i)+U_i C_(j-i)].

The denominators are positive because a_j strictly decreases. Subtract (15)
from its fixed recursion, use the product-difference identity and induction,
and sum the two-rate geometric recurrence. This proves the displayed bound.
It is an individual fixed-order theorem, not a uniform estimate as j grows.
Contraction and an independent equal-mean coupling give

    W_2(nu_n,nu_*) <= sqrt(4/5)c^n,
    D(nu_n) <= (1+c)sqrt(4/5)c^n.                      (17)

Hence H_n -> xi locally uniformly on the critical strip, quantitatively by
(10), BEFORE establishing any zero-location property of H_n for n>=1.

Every stage can be realized on a finite binary tree: attach independent gamma
leaves, and at each internal vertex divide the sum of its children by an
independent U^2. There are no infinite input integrals in the probabilistic
DEFINITION of a finite stage. Its positive variables are generally unbounded;
no deterministic compact support is asserted. Its pair Mellin transform is
holomorphic at least on -10*2^n<Re s<1+10*2^n. To see this, every leaf weight
is between 4^(-n) and 1 and there are 2^n independent Gamma(5/2,5/2) leaves;
compare their sum to the weighted sum to control positive and negative moments.
We need only the smaller critical strip, with the uniform bounds in (10).

The aggressive new theorem to attack is:

  ORBIT-STRIP: the symmetrized Mellin transform of the prescribed orbit (14)
  has no zeros with 0<Re s<1 and Re s!=1/2, for an unbounded set of stages n.
                                                               OPEN

BSR3 proves the starting stage over the ENTIRE strip. Contraction settles
identification of the proposed limit. ORBIT-STRIP would then give RH by the
complete ending in Section 2. No growing-height Taylor approximation and no
source-to-operator spectral identity remains to be supplied after that theorem.

ORBIT-STRIP is NOT proved, and no theorem here says T preserves zero geometry
for every positive law. In particular integration/mixture of individually
zero-safe functions does not in general preserve their zero set.

### A first exact expression for the nontrivial step

At n=1 write U,V uniform[1,2] and B~Beta(5,5), independent. Gamma splitting gives

 M_1(s)=(pi/15)^(s/2) Gamma(10+s/2)/Gamma(10)
           *E[(B/U^2+(1-B)/V^2)^(s/2)].                 (18)

This is a bounded three-variable mixing integral multiplying a gamma factor.
Its full mixed expectation must be retained. The positive density of B does
not let us drop its phase in complex s. A generalization of the TWO-region
phase/modulus argument in Section 3 is one possible attack, but its simple
monotone-ratio invariant is not being assumed for (18).

Preliminary NONDIRECTED Gauss quadrature in (18) finds negative ratio
sigma-derivatives already near height 13.5 or 23.5. The values agree at two
quadrature orders, but there is no interval error bound. Thus this scout is a
warning AGAINST promising that the stronger derivative inequality (12) simply
inducts. It does not prove an off-line zero of H_1. A small root scout found
noncentral candidates outside the critical strip; it is not a zero census or
a certificate for their locations. Raw-tree entire Lee--Yang was never needed.

## 5. An independently checkable local residual, with every uniform bin paid

ORBIT-STRIP is not the only way to use BSR2. One can instead search for
zero-safe finite laws with a small value of D(nu). Here is a finite rational
certificate for that residual, not a call to a zeta or distribution oracle.

Let nu have finitely many positive rational atoms x_i with positive rational
probabilities p_i summing to one and mean one. Split [1,2] into L equal bins
[l_j,r_j], h=1/L, and define T_L(nu) by atoms and weights

    value=(x_i+x_k)/(l_j r_j),  weight=p_i p_k/L.       (19)

Merge equal atoms exactly. This is the conditional mean of the literal
variable (X_1+X_2)/U^2 on the bin and input atoms, since

    E[U^-2 | l<U<r]=1/(lr).

The entire unquantized mean remains exactly one. The squared cost of THIS
coupling (not an asserted optimal cost) is exactly

    epsilon_L(nu)^2=(2m_2+2) sum_j h^3/(3l_j^3 r_j^3)
                   <=(2m_2+2)/(3L^2).                 (20)

Indeed Var(U^-2 | bin)=h^2/(3l^3 r^3), and E(X_1+X_2)^2=2m_2+2.
All bin interiors and endpoints are covered; there is no infinite uniform
input tail. Positivity lets equal boundary coverage cause no loss.

Compute d_L=W_2(nu,T_L nu) by ordered one-dimensional quantile coupling.
The squared value is rational. Optimality of the monotone coupling follows
from the uncrossing identity: for x<=x' and y<=y', replacing crossed pairs by
ordered pairs reduces the squared cost by 2(x'-x)(y'-y)>=0. Finite quantile
matching exhausts both marginals, so this argument proves the cost formula.
The triangle inequality gives the genuine bound

    max(0,d_L-epsilon_L) <=D(nu)<=d_L+epsilon_L.        (21)

Directed integer square-root intervals turn (21) into strict typed output.
This certificate concerns the exact stochastic map, not a sampled version.
It is not a certificate of zero-safety for H_nu.

### An all-scale finite rational approximate-fixed-point construction

Take nu_0=delta_1 and nu_(n+1)=T_(2^(n+1))(nu_n). Conditional Jensen and (15)
give m_2(nu_n)<=7/5. Thus epsilon<=4/(3*2^(n+1)). Iterating (3) with this error,

 W_2(nu_n,nu_*)
 <=sqrt(2/5)c^n+(4/3)(c^n-2^-n)/(2c-1)<4c^n,
 D(nu_n)<8c^n.                                        (22)

This proves existence of explicit FINITE RATIONAL approximate fixed points
with geometrically decreasing true residual. Expanded support can grow very
rapidly; no polynomial-time or small-memory claim is made. The first three
transitions have support sizes 1 -> 2 -> 10 -> 350 and are completely
reconstructed by the bounded checker. Their H functions are entire because
their strictly positive supports are finite, but their strip zero geometry
is not proved. Higher transitions are not executed.

## 6. How this connects constructively to the Lee--Yang branch

Equation (8) gives an exact interface to #842. A finite positive law nu whose
symmetric tilted log-pair law can be realized as the magnetization of a
zero-field ferromagnetic Ising graph has a zero-safe transform by the classical
Lee--Yang theorem. If a sequence of such laws also has D(nu)->0, BSR2 supplies
the ORIGINAL theta law as its limit; no all-order source-moment fit is needed
as an extra hypothesis.

But an arbitrary Ising magnetization need not admit the nonlinear inverse
pair-sum/tilt representation (8). We neither claim that the six-moment model
in #842 has this exact representation, nor infer it from the Villain
zero-field temperature identity. Constructing an approximate fixed point
inside a proven zero-safe class is the new inverse problem, not a solved one.
The more flexible gamma ORBIT-STRIP target avoids requiring an entire
Lee--Yang function at every finite stage, since only the critical strip is
needed by Hurwitz.

This changes the research direction from ``prove a hidden all-order sign of
the final Xi operator'' to ``find a zero-safe class compatible with one
explicit positive branching rule''. The convergence and source-normalization
parts are fully priced. The zero-safe class/propagation part is substantial
and OPEN. It cannot be supplied by positivity, moment matching through any
fixed order, or small W_2 distance alone.

## 7. Review and evidence boundary

BSR1--BSR3 and the residual/quantization bounds have the written proofs above.
The Brownian source identities and the equation underlying (1) are credited
classical material, reconstructed to fix scaling and domain. Review should
focus on the gamma strip argument, the exact Mellin normalization, and the
error/quantifier boundary in the residual theorem.

The checker independently reconstructs finite rational moment recurrences,
a sinh reciprocal-series expansion, all 20 Bernstein coefficients, finite
law/transport identities and the first three quantized transitions. It does
not machine-prove the analytic theorems, implement a zero-free-strip
certificate for a later stage, or verify RH. Exploratory floating computations
are separately marked and do not enter acceptance. See VALIDATION.md.

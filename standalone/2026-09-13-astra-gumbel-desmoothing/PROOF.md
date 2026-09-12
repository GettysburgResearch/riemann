# HBR30 — removing Gumbel smoothing from the native reciprocal-zero moments

Date: 2026-09-13. **PROPOSED component proofs; independent mathematical and
implementation review required. RH is not proved.**

This is a separate add-only research continuation of HBR29, PR #879 at
`5645f787183edefacf6402b0cff60a991fa31ba4`. It uses the newer reciprocal-xi
work in PR #842 at `346f630299252183aec2d8c41a0f3b4027bb9d19` as its immediate
motivation. No proposed Brownian phase inequality is restored by fiat.

The positive result is at **every Hankel dimension**, but only on the bounded
parameter interval `1 <= p <= 16384`. Its limit as p tends to infinity is the
unproved RH-bearing step. The large parameter bound is obtained from an
EXTERNALLY VERIFIED finite zero height plus a complete analytic unknown-tail
bound, not new prime cancellation or a new verification height.

Classical inputs are the theta/xi representation and product, the critical
strip, Platt--Trudgian's Theorem 1, gamma integration/product identities, and
standard moment/independent-sum arguments. General heat, Hankel and probability
criteria are not claimed new. The proposed contribution is the powered-trace
positivity estimate, the explicit fractional-factorial hierarchy, its exact
one-way smoothing relation, and a quantitative finite-parameter obstruction.

## 1. Fixed source, counting convention, and exact target

Use the entire completion and the full-line theta convention

    Xi(z)=xi(1/2+iz)=integral_R phi(x) exp(izx) dx,
    phi(x)=sum_(n>=1) exp(x/2)(4Q_n^2-6Q_n) exp(-Q_n),
    Q_n=pi n^2 exp(2x),    Z=Xi(0)>0,    w=phi/Z.             (1)

The completion has removable values xi(0)=xi(1)=1/2. Jacobi inversion makes
phi even; termwise positivity is used only for x>=0. The complete source
has all exponential moments and double-exponential tails. These are classical
source identities, not identities for an approximant fitted to zeros.

For each nontrivial zeta zero rho=beta+i gamma with gamma>0, put

    z_rho=(rho-1/2)/i=gamma-i(beta-1/2),
    a_rho=z_rho^2,                 lambda_rho=1/a_rho.       (2)

Every analytic multiplicity is included. Both conjugate members of a nonreal
quartet occur: this is one representative of each +/- pair of Xi zeros, NOT
one representative of each quartet. Write sum_rho with these conventions.

The critical strip gives |Im z_rho|<1/2. The genus-zero product for the entire
function of v defined by the even Taylor series is

    Xi(sqrt(v))/Z=product_rho(1-v/a_rho),
    sum_rho |a_rho|^-1 < infinity.                          (3)

There is no branch ambiguity in the left side and no unknown exponential
prefactor. For example the classical source growth O(R log(R+2)) for log M_Xi(R)
makes its squared-variable order at most 1/2<1 and gives the required product.
The usual zero count also gives the displayed summability. We do NOT infer
summability from the coarser quadratic count used later.

For n>=1 define the actual reciprocal-zero moments

    q_n=sum_rho a_rho^-n
       =(-1)^(n+1) kappa_(2n)(w)/[2(2n-1)!].               (4)

The cumulant equality follows by comparing logarithms of (3) near zero with
the moment-generating series; no logarithm across unknown zeros is assumed.
In particular q_1=Var_w(X)/2>0. Formula (4) defines the same scalars directly
from the complete arithmetic source without an input list of zeros.

PR #842 proves positivity with the weights n!. Its unweighted target remains
open. Replace those weights by

    M_n(p)=Gamma(1+n/p) q_(n+1),          n>=0, p>=1.       (5)

The two moment matrices in this packet are

    G_d(p)=(M_(i+j)(p))_(0<=i,j<=d),
    J_d(p)=(M_(i+j+1)(p))_(0<=i,j<=d).                    (6)

Ordinary theta moment matrices, these fractional-factorial matrices, and the
unweighted CUMULANT matrices are different objects.

## 2. Classical finite-height input and a freshly reconstructed anchor

We import Platt--Trudgian [PT], Theorem 1, only for the statement that every
nontrivial zeta zero of ordinate at most

    T=2^40=1099511627776

is central. Their published bound is 3000175332800, which is strictly larger.
The paper and the image of its Theorem 1 were inspected; its numerical campaign
is NOT rerun here. No centrality above T is imported.

The new defining-integral certificate in Section 10 proves

    1/10000 < Xi(14) < 3/10000,
    -1/1000 < Xi(15) < -1/2000.                           (7)

Thus continuity supplies a REAL zero gamma_0 in (14,15). This sign certificate
does not assert that it is the first zero, unique, simple, or a complete census.
Finite-height completeness comes separately from [PT].

Here is the whole-source zero-count budget, rederived from the same mechanism
in #842. For x>=0, x^2+x/2 <= (3/2)exp(2x) <= Q_n/2, so

    exp(x^2)phi_n(x) <=4Q_n^2 exp(-Q_n/2)
                         <=256 exp(-Q_n/4).

The sum of exp(-3n^2/4) is less than one: exp(3/4)>2 gives comparison with
sum_(n>=1)2^-n, with strict inequality. Evenness gives

    0<phi(x)<256 exp(-x^2),       x in R.                  (8)

On [0,1/8], 3<Q_1<5, hence phi(x)>18/243. It follows that Z>1/54.
Integrate the Gaussian with its ACTUAL linear tilt, rather than introducing
an unnecessary absolute-value tilt, to obtain for F(v)=Xi(sqrt(v))/Z

    |F(v)| <2^15 exp(|v|/4).

Jensen at radius 2r, with F(0)=1, gives n_F(r)<=15+r. Each zero counted by
N(U)=#{rho:0<gamma<=U} satisfies |a_rho|<=U^2+1/4; consequently

    N(U)<=2U^2,               EVERY U>=4.                 (9)

All multiplicities and the entire unverified divisor are in this count.
Boundaries follow by limiting radii. Estimate (9) is intentionally crude.

## 3. A powered heat trace with a complete, unknown-spectrum tail

All powers of a in this section use its principal logarithm. Set

    P=2^14=16384,
    H_p(t)=sum_rho a_rho^(p-1) exp(-t a_rho^p),
                       t>0, 1<=p<=P.                    (10)

This is neither a derivative H^(p) nor the de Bruijn heat deformation of the
source density. Its weighting a^(p-1) is essential to (5).

### HBR30-1: positivity for every time and every real parameter in [1,P]

The complete, normally convergent series (10) is real and satisfies

    H_p(t) > (1/2)196^(p-1) exp(-225^p t),
             EVERY t>0, EVERY real 1<=p<=16384.           (11)

The entire analytic proof follows. It does not sample H_p numerically.

For an unverified node write z=gamma+i eta, |eta|<=1/2, gamma>=T. Then

    |arg a|<=1/gamma,
    |a|^(p-1)<=2 gamma^(2p-2),
    Re(a^p)>=(1/2)gamma^(2p),
    |Im(a^p)|<=2p gamma^(2p-1).                           (12)

Indeed |a|=gamma^2+eta^2, and p/(4gamma^2) is smaller than log 2.
Also |p arg a|<=P/T=2^-26, so cos(p arg a)>1/2 and there is no logarithmic
wrapping: Log(a^p)=p Log a. Verified low nodes have a>0. Thus all a^p lie in
the right half-plane, with a uniform tail bound (12); normal convergence of
(10) and any fixed t derivative follows by (9). Conjugation makes the sum real.

For A>=T and t A^(2p)/2>=1 the full omitted tail obeys

    |sum_(gamma>A) a^(p-1) exp(-t a^p)|
      <=B_p(t,A):=4[A^(2p)+2/t] exp(-t A^(2p)/2).          (13)

To prove this, put b=t/2 and g(u)=u^(2p-2)exp(-b u^(2p)). It decreases on
[A,infinity), and

    -g'(u)<=2pb u^(4p-3)exp(-b u^(2p)).

Stieltjes integration with (9), retaining the lower endpoint -N(A)g(A) before
dropping it in the UPPER bound, yields

    sum_(gamma>A)g(gamma)
      <=4pb integral_A^infinity u^(4p-1)exp(-b u^(2p))du
      =2[A^(2p)+1/b] exp(-b A^(2p)).

The factor two in |a|^(p-1) from (12) proves (13). The vanishing upper endpoint
is justified by the exponential. No high zero was assumed central in this step.

#### Small times

Let t_0=[8p T^(2p-1)]^-1 and 0<t<=t_0. Choose

    A=[1/(8pt)]^(1/(2p-1))>=T.

For T<gamma<=A, the phase of the individual term in (10) has absolute value
at most

    (p-1)|arg a|+t|Im(a^p)| <=P/T+1/4<1/2.

Those terms have strictly positive real parts. Every gamma<=T term is real
positive by [PT]. Keep the one anchor from (7): its contribution is greater
than 196^(p-1)exp(-225^p t), even if its multiplicity is larger than one.

Here t A^(2p)/2=A/(16p)>=1. Since A>=16p and A>=30,

    2/t<=A^(2p),          225^p<=A^(2p)/4.

Divide (13) by the retained anchor. The result is at most

    8 A^(2p)196^(1-p) exp(-A/(32p))
      <=8 A^(2p) exp(-A/(32p)).                           (14)

For A>=T>=64P^2 this last expression decreases with A. At A=T it increases
with p, so it is at most 8 T^(2P)exp(-T/(32P)). Exactly,

    T/(32P)=2^21,
    8 T^(2P)exp(-T/(32P))
      <2^[3+80P-2^21]=2^-786429<1/2.                    (15)

We used only e>2 for the exponential comparison. This proves (11) on the
ENTIRE small-time interval, including times tending to zero.

#### Large times

For t>=t_0 take A=T in (13). Every low node remains positive. Relative to the
same anchor, its upper tail ratio is

    4[T^(2p)+2/t]196^(1-p)
              exp[-t(T^(2p)/2-225^p)].

Both factors decrease with t, since T^(2p)/2>225^p. At t=t_0 it is bounded
by (14)--(15). Subtracting the whole unverified tail proves (11). QED.

### General height-to-parameter transfer

The same proof applies to any conjugation-symmetric divisor gamma+i eta with
|eta|<=1/2, complete count N(U)<=2U^2 for U>=4, one real anchor in (14,15),
and only real nodes through T, provided

    T>=max(30,16P,64P^2),
    8 T^(2P)exp(-T/(32P))<1/2.                            (16)

Summability of reciprocal squares is separately required for the moment
conclusions below. Thus the result transparently prices the imported finite
zero region. It does not extract centrality at a larger height. P is conservative,
not an optimized threshold. A fixed T cannot satisfy (16) for unbounded P.

## 4. HBR30-2: all-rank positivity with fractional factorials

For 1<=p<=P define a measure on x>0 by

    dnu_p(x)=p x^(p-1) H_p(x^p) dx.                       (17)

By (11) this density is strictly positive. It is integrable, and EXACTLY

    integral_0^infinity x^n dnu_p(x)
         =Gamma(1+n/p) q_(n+1)=M_n(p),       n>=0.         (18)

For justification, (12), the finite low divisor, and (3) give, for each fixed n,p,

    sum_rho |a|^(p-1)
       integral_0^infinity t^(n/p)exp[-t Re(a^p)]dt
       <=C_(n,p) sum_rho |a|^(-n-1)<infinity.

Thus all termwise integrations are ABSOLUTELY justified, including n=0.
The individual integral is

    Gamma(1+n/p) a^(p-1)/(a^p)^(1+n/p)
       =Gamma(1+n/p)a^(-n-1).

The no-wrapping identity after (12) is needed for this equality. The change
of variables t=x^p proves (18). In particular nu_p((0,infinity))=q_1.

Equations (6) are the monomial Gram matrices in L2(nu_p) and L2(x nu_p).
A nonzero real or complex polynomial cannot vanish almost everywhere against
a strictly positive density. Therefore

    G_d(p) is positive definite and J_d(p) is positive definite,
    EVERY integer d>=0 and EVERY real 1<=p<=16384.         (19)

This is all-dimensional positivity, not a finite matrix campaign. p=1 gives
the factorial-weighted matrices already proved by #842. For p>1 the smoothing
is smaller, but for each FIXED p its gamma weights still grow with moment order.
Entrywise division by those weights is not a positive-matrix operation.

## 5. HBR30-3: exact Gumbel smoothing, and the direction it permits

Define the absolutely convergent secondary zero zeta function

    Zcal(s)=sum_rho a_rho^-s,       Re s>1/2.              (20)

Complex powers use the same principal logarithms. Classical zero growth ensures
local uniform convergence; the high arguments tend to zero. At positive integers
Zcal(n)=q_n. This is a different function from the original Riemann zeta.

Let X_p have the probability law nu_p/q_1. The same absolute integration as
in (18), now at exponent i u, gives

    E exp(iu log X_p)
      =Gamma(1+iu/p) Zcal(1+iu)/q_1,       u real.         (21)

Thus an explicit amount of logarithmic noise makes the actual spectral Mellin
transform positive definite. The factor Gamma(1+iu/p) is the characteristic
function of (log E)/p, where E is a mean-one exponential. Equivalently this
is a scaled negative Gumbel random variable. Its variance is pi^2/(6p^2).
The same gamma/Gumbel factor arose asymptotically in HBR29, but (21) is an exact
finite-parameter identity for a DIFFERENT, reciprocal-zero moment object.

Under RH alone, Zcal(1+iu)/q_1 is itself the characteristic function of the
real random variable log lambda, with atom weights lambda/q_1 at lambda=a^-1.
Equation (21) then describes the product lambda E^(1/p). Without RH we have
NOT constructed that unsmoothed positive law.

### Exact independent increment between two parameters

For 1<=p_1<=p_2 let r=p_1/p_2, let B_k be independent Bernoulli variables of
success probability 1-r, and let E_k be independent mean-one exponentials.
Put

    D=-gamma_E(1/p_1-1/p_2)
       +sum_(k>=1)[(1-r)/(p_1 k)-B_k E_k/(p_1 k)].        (22)

All variables in the sum are independent. The summands are centered, and their
variances sum. The series converges in L2 and almost surely, with exact tail
variance bound

    E |D-D_K|^2
      =(1/p_1^2-1/p_2^2)sum_(k>K)k^-2
      <=(1/p_1^2-1/p_2^2)/K.                             (23)

D_K retains the deterministic constant. The elementary Bernoulli/exponential
factor is

    E exp[-iu B_k E_k/(p_1 k)]
      =r+(1-r)/(1+iu/(p_1 k))
      =[1+iu/(p_2 k)]/[1+iu/(p_1 k)].                    (24)

The classical Weierstrass gamma product [G] consequently proves

    E exp(iuD)=Gamma(1+iu/p_1)/Gamma(1+iu/p_2).            (25)

It also gives, for EVERY real n>=0,

    E exp(nD)=Gamma(1+n/p_1)/Gamma(1+n/p_2).               (26)

For (26), finite products have logarithms with a summable O_n(k^-2) tail.
The same bounds at 2n give uniform integrability, so their expectations pass
to the almost-sure limit. No unquantified infinite product is used.

Combining (21) and (25) proves the exact independent smoothing identity

    log X_(p_1) =_law log X_(p_2)+D,    1<=p_1<=p_2<=P.  (27)

Crucially this goes from the LESS smoothed p_2 to the MORE smoothed p_1.
It cannot construct a positive X_(p_2) from X_(p_1) by reversing the equation.
The inverse Fourier multiplier has exponentially growing modulus and is not a
characteristic function when p_1<p_2.

Indeed the equivalent gamma-product exponent is

    log Gamma(1+iu/p)
      =-gamma_E iu/p
       +integral_0^infinity (exp(-iux)-1+iux)
                                dx/[x(exp(px)-1)].       (28)

For p_1<p_2 the difference of these Levy densities is nonnegative, proving
again only the downward smoothing direction. Increasing p removes negative
jumps; the reverse operation is not a positivity-preserving Markov operator.
This was the attempted automatic parameter induction, and this direction
check explains why it does not establish the missing upper-parameter step.

## 6. HBR30-4: the exact RH consumer and a quantitative witness

Call p>=1 feasible when BOTH towers in (6) are positive semidefinite at every
finite d. No simplicity or determinant-nonvanishing condition is imposed.
The feasible set is a closed initial interval containing [1,16384].

For downward closure, (26) supplies the moments R_n of the positive variable
exp D. The identities

    M_n(p_1)=R_n M_n(p_2)

express each matrix at p_1 as the entrywise product of two positive semidefinite
moment matrices. The shifted tower uses R_(i+j+1), not R_(i+j). Gram tensor
products prove the Schur product assertion. Thus feasibility at p_2 implies
feasibility at p_1. Closedness follows from continuity of each finite gamma
matrix. This argument does not need to assume an unproved representing measure
for the native unsmoothed sequence.

Let p_* be the supremum of that feasible interval. Then

    p_*>=16384,
    p_*=infinity  <=> RH.                                (29)

More generally feasibility along ANY unbounded sequence p_j suffices; no rate
or simultaneous growth of matrix dimension is required.

Under RH, the positive mixture lambda E^(1/p) described after (21) represents
(5) for EVERY p>=1, proving one direction. Conversely, for each fixed d,
Gamma(1+n/p_j)->1, so the PSD matrices J_d(p_j) tend to

    J_d(infinity)=(q_(i+j+2))_(0<=i,j<=d).                (30)

The following complete power-sum separation argument proves that all (30)
being PSD forces all actual lambda nodes to be positive real.

Suppose lambda_0 is nonreal and put b=|lambda_0|. There are only finitely many
distinct nodes with |lambda|>=b/2, by (3). Form a REAL polynomial L which vanishes
at all those nodes except lambda_0 and its conjugate, with L(lambda_0)!=0.
For each integer N choose real u_N,v_N so that

    p_N(x)=x^N L(x)(u_N x+v_N),
    lambda_0 p_N(lambda_0)=i.                            (31)

This real two-variable system is nonsingular since Im lambda_0!=0; conjugation
gives -i at the other member. Its solution is O(b^-N), with fixed constants
allowed to depend on lambda_0 and L. On |x|<=b/2,

    |p_N(x)|<=C 2^-N.

In the exact quadratic form sum mult(lambda)lambda^2 p_N(lambda)^2, the selected
pair contributes -2m, where m is its analytic multiplicity. All other outer
nodes vanish. The ENTIRE remaining tail has absolute value at most

    C^2 4^-N sum_rho mult(lambda)|lambda|^2 ->0.           (32)

This contradicts (30) for a sufficiently large finite polynomial. All nodes
are therefore real. Negative nodes are excluded because Xi(iy)>0 for every
real y; no imaginary-axis zero is possible. This proves RH with all analytic
multiplicities retained. This is the classical power-sum/moment mechanism,
with its complete-tail argument supplied, not a newly claimed easy RH criterion.

### Centered noise and a quadratic finite-witness bound

A deterministic rescaling does not change matrix positivity. Remove the mean
of the logarithmic noise by using

    W_n(p)=exp(gamma_E n/p) Gamma(1+n/p).

The first centered tower is D G_d(p) D and the second is
exp(gamma_E/p) D J_d(p) D, with D_ii=exp(gamma_E i/p). These are positive
congruences, not arbitrary entrywise changes.

The gamma product gives, for 0<=x<=1,

    0<=log[exp(gamma_E x)Gamma(1+x)]
       =sum_(k>=1)[x/k-log(1+x/k)]
       <=(x^2/2)sum_(k>=1)k^-2 < x^2.

Here 0<=v-log(1+v)<=v^2/2 follows by integration, and pi^2/6<2.
Since exp(u)<=1+2u on 0<=u<=1, we obtain

    0<=W_n(p)-1<=2 n^2/p^2,             0<=n<=p.         (33)

Thus the actual nontrivial smoothing begins quadratically in 1/p after its
harmless deterministic shift is removed. This bound is not uniform in n.

If a real vector c at dimension d has

    c^T J_d(infinity)c=-eta<0,
    A_c=sum_(i,j)|c_i c_j|(i+j+1)^2|q_(i+j+2)|,

then for p>=2d+1 its quadratic form in the centered tower differs from -eta
by at most 2A_c/p^2. Every p>2 sqrt(A_c/eta), with p>=2d+1, therefore fails
that finite PSD test (the corresponding test vector in the original
coordinates is D c). An off-line zero cannot remain hidden under
arbitrarily small smoothing. No actual negative native witness or finite
upper bound on p_* is produced in this packet.

## 7. A sharp logical stress test: finite p does NOT close RH

The same all-time proof applies to the following exact finite SYNTHETIC divisor:

    z_0=29/2,
    z_+=(T+1)+i/4,   z_-=(T+1)-i/4,    T=2^40.           (34)

It meets every assumption in (16), has centrality through T, and has complete
count N(U)<=3<=2U^2 for U>=4. Hence its fractional-factorial towers are strictly
positive at EVERY dimension for EVERY 1<=p<=16384. Nevertheless its even real
polynomial product has the explicitly prescribed nonreal quartet.

This is not Xi, not a theta probability density, not a prime-defined L-function,
and not an off-line zeta zero. It proves only that the finite-height geometry
and the finite-p positivity theorem cannot logically supply the unbounded-p step.

There is a small exact unsmoothed negative witness. Set lambda_j=z_j^-2 and
choose real u,v by

    u lambda_+ +v = i/[lambda_+(lambda_+-lambda_0)].

For p(x)=(x-lambda_0)(u x+v),

    p(lambda_0)=0,
    lambda_+ p(lambda_+)=i,
    sum_(i,j=0)^2 p_i p_j q_(i+j+2)=-2.                 (35)

All quantities in (34)--(35) are Gaussian rationals, reconstructed exactly by
the checker. The coefficients are badly conditioned; no rounded floating
witness is substituted. Multiplicity is one here by construction. The bound following
(33) supplies a finite parameter beyond which its positivity must fail.

## 8. What the attempted completion achieved, and where it stopped

The previous single Brownian mode failed because its reflected phase rotates.
The present construction does not choose another mode or pretend that its
positive perturbation eigenvalues are xi zero locations. It uses the ACTUAL
reciprocal-zero moment sequence, defined independently by theta cumulants.

The gamma factor left visible in HBR29 motivated (21): remove Gumbel smoothing
rather than search another individually oriented companion. This gives a
whole-source positive law with much weaker factorial weights, an exact
positive transport toward stronger smoothing, and a fully proved conditional
ending. It does not give positive transport in the needed opposite direction.

The precise unfinished task is to prove feasibility of (6) for unbounded p,
or any equivalent source-specific estimate forcing p_*=infinity. The available
proof reaches p<=16384 by pricing the verified low spectrum; it does not advance
centrality of the unknown divisor. The countermodel (34) satisfies that entire
finite-p theorem and prevents calling it an RH completion.

Possible arithmetic work would target the native q_n or the positive-definiteness
of Zcal(1+iu) without the gamma multiplier. Unlike solving the bounded probability
construction, that requires cancellation information not supplied by the strip,
source positivity, a finite zero census, or the one-way Levy relation (28).
No such all-p estimate is proved or numerically claimed here.

## 9. Relationship to other inspected repository work

- #879 / HBR29 at `5645f787183edefacf6402b0cff60a991fa31ba4`: the authored
  two-scale proof and gamma profile were read. Its mode asymptotics are motivation,
  NOT a premise of (11). Its numerical diagnostics were not rerun.
- #842 reciprocal-subordinator at `346f630299252183aec2d8c41a0f3b4027bb9d19`,
  proof blob `f2053068565ab28f673eb537ed4cdb6b6ec9d8fa`: Sections 1--7 were read.
  The unpowered heat proof, quadratic count and factorial moments are credited.
  We rederive the needed count and reconstruct a new anchor; its certificate
  is not imported as a numerical premise. The subordinator itself is not needed.
- #843 at `279bbe3d5198d7f7eb3e0072267f65c7374d7e5e`, proof blob
  `cf1dc849f307e581745c1bb5b2f300c77f552aca`: source/count opening read for
  overlap, not its whole later finite-rank campaign. Its earlier trace/Hankel
  and Gaussian-positivity programme is not counted as new in this packet.
- #881 at `ab663f7d8020a62e1d8eedaf7d963d0eca3efe50`: principal nonlocal
  similarity-energy argument read for orientation; no operator-energy theorem
  or inherited theta-moment interval from it enters acceptance.
- The latest descriptions of #869, #875, #877, #878 and #880 supplied context
  about signed currents, arithmetic, all-order realizations and new comparisons.
  They were not independently mathematically reviewed or imported as premises.

This is targeted reconnaissance, not an exhaustive review of the repository,
its issue programmes, or all post-integration PRs. No canonical status changes.

## 10. Complete native anchor certificate and arithmetic contract

The accepting reconstruction uses the unchanged BRN27 `ball_core.py`, Git blob
`2d5dd98a78d0afe279cde2610819165f4b3bef1c`, with 512-bit outward complex L1 balls.
Reuse is attributed; it is not a second independent numerical backend.
The accepting path uses only integers/Fractions, its rational Machin-pi and
explicit exponential series. It does not call zeta, gamma, a zero database,
floating quadrature, NumPy, SciPy or mpmath.

For each of gamma=14,15, integrate the first FOUR literal terms of (1) on
[0,2], in ALL 128 consecutive cells, with half-width h=1/128. The midpoint
Taylor degree is 24. Exactly,

    P_0(q)=4q^2-6q,
    P_(k+1)(q)=(1/2-2q)P_k(q)+2q P_k'(q),
    phi_n^(k)(c)=exp(c/2-q_n(c))P_k(q_n(c)).              (36)

Convolve these coefficients divided by k! with (i gamma)^j/j!, multiply by
exp(i gamma c), and integrate every even Taylor coefficient with factor
2h^(k+1)/(k+1). Real part of twice this half integral is the desired approximation.
Both endpoints are included through the exact gap-free cell union.

### All omitted Taylor coefficients

On a complex disk of radius r=1/16 about any cell center c in [0,2],
|q_n|<2^14 and |arg q_n|<=1/8, for n<=4. Hence Re q_n>0,
|4q_n^2-6q_n|<2^31, exp(Re x/2)<16 and the sum of four source terms has
modulus <2^37. For |gamma|<=15 the oscillatory factor has modulus <4.
The conservative analytic bound M=2^40 therefore holds on every such circle.
Cauchy's estimate and h/r=1/8 pay ALL terms after degree 24. The complete
FULL-LINE real error is at most

    R_T=4*2^40*(1/8)^25/(1-1/8).                         (37)

The implemented value is projected to its real part before this absolute
complex-remainder bound is added, so no uncharged complex-to-L1 conversion
is used. Arithmetic errors in all retained coefficients remain in their balls.

### Every later theta index

For any n>=1 and lower time endpoint with q_0=pi n^2 exp(2x_0)>=1, substitution
q=pi n^2 exp(2x) gives

    integral_(x_0)^infinity phi_n(x) dx
      <=2(q_0^2+2q_0+2)exp(-q_0).                        (38)

The expression on the right decreases with q_0. At x_0=0 and n>=5 it is
at most 34n^4 2^(-4n^2), using exp(3)>16. For n>=5, n^4<=2^(2n), and the
successive geometric ratio is at most 2^-42. Thus the HALF-LINE omitted index
sum is <2^-84; twice it is <2^-83. This bound already covers their entire time
range and is not merely their values at the cutoff.

### The entire remaining time tail

For x_0=2 and n<=4, exp(4)>50 and pi>3 give q_0>150n^2. Each bound (38) is
less than 2(150^2+300+2)2^-150<2^-134 by monotonicity. Four terms and the factor
two for the full Fourier integral give <2^-131; the code charges the weaker
2^-128. The inequalities exp(3)>16 and exp(4)>50 are checked from finite positive
Taylor lower sums. The bounds do not require any sign for the omitted cosines.

Adding (37), 2^-83, 2^-128 and every outward arithmetic radius proves (7).
The final enclosures have widths below 3*10^-10. Displayed decimal centers are
not input values. The only numerical zero input in the mathematical theorem
is the separately credited published completeness assertion from [PT].

## 11. Validation and smallest review-critical claims

`check.py --check result.json` authenticates the packet and fully reconstructs
the native anchor plus bounded algebra. Its controls independently regenerate
derivative polynomials via formal exponential series, the powered-tail endpoint
algebra, finite gamma-moment identities, Bernoulli/gamma-product factors, and
the exact synthetic negative witness. They do not machine-prove the infinite
analytic statements, all real p, or all matrix sizes.

Normal/optimized agreement uses the SAME implementation and authorship. See
VALIDATION.md for the exact executions, clean packaging replays, corruption
cases, and what was not run. No full-repository validator, remote CI, Lean build,
independent referee acceptance or actual p>1 zero-heat evaluation is asserted.

Critical review points: principal powers and no wrapping in (12)/(18); complete
Stieltjes tail (13); both time regimes and the uniform p budget (15); absolute
moment integration including n=0; the drift and full variance tail in (22);
the direction of smoothing; the shifted Hankel indexing; and the full small-node
tail in (32). The smallest missing RH-facing claim is unbounded-p feasibility,
not an omitted numerical check.

## References

[PT] D. Platt and T. Trudgian, *The Riemann hypothesis is true up to 3*10^12*,
arXiv:2004.09765; published DOI 10.1112/blms.12460. Theorem 1,
printed page 2. https://arxiv.org/abs/2004.09765

[G] NIST DLMF 5.8.2, gamma Weierstrass product;
https://dlmf.nist.gov/5.8 . The elementary gamma integral and its complete
product are classical; all scaling and probabilistic factors used here are
specified above.

[Z] NIST DLMF 25.10, zeta zeros and classical count context;
https://dlmf.nist.gov/25.10 . The source/product convention is stated in
(1)--(4), independently of accepting a repository operator determinant.

[R] D. Romik, *Orthogonal polynomial expansions for the Riemann xi function*,
arXiv:1902.06330, consulted in the predecessor programme. The present packet
is not an orthogonal-polynomial eigenvalue assertion, and imports no theorem
from that paper.

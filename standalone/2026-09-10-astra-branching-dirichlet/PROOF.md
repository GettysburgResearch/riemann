# BDR26: exact Gamma–Dirichlet coordinates for the prescribed branching orbit

Date: 2026-09-10. **Proposed component proofs and a directed finite phase
certificate; independent mathematical/code review required. RH is NOT proved.**

This continues PR #853 at `e0b82da7ecdd4ed21e47e8b6adbb8c5182eac048`.
The nine predecessor files are unchanged. The unproved conclusion remains
zero confinement for a cofinal sequence of the prescribed orbit. This is not
a completed proof with a final detail delegated to reviewers.

The positive result is an exact compact-variable representation at EVERY
finite depth, with rational moment recursion, exact poles and a corresponding
entire approximation of xi. The attempted extension of the gamma seed's
modulus-ratio proof is false even on the FIRST prescribed Gamma(5/2) iterate:
the relevant derivative is strictly negative at 1/2+23i. This is a phase test,
NOT an off-central zero of that iterate and NOT a refutation of its zero-safety.

## 1. Conventions and inherited mathematical inputs

Set k=5/2, and let Gamma(a,rate k) have Laplace transform (1+t/k)^(-a).
Let

    X_0 ~ Gamma(k,rate k),
    X_(n+1) = (X_n+X_n')/U^2 in distribution,
    U ~ Uniform[1,2].                                      (1)

The two children are independent; the same independent U scales their sum.
Every random variable in a new decomposition below is independent except where
sharing is explicitly specified. Define

    c = pi/6,     c0=c/k=pi/15,
    M_n(s)=E[c(X_n+X_n')]^(s/2),
    H_n(s)=[M_n(s)+M_n(1-s)]/[2(1+M_n(1))].                 (2)

Positive real powers always use the real logarithm. The denominator in (2)
is positive. On its domain H_n(s)=H_n(1-s) and H_n(conj s)=conj H_n(s).

BSR26 establishes the elementary W2 contraction and identifies the normalized
fixed law X_*=(6/pi^2) sum E_j/j^2. Its complete Mellin identity

    E[c(X_*+X_*')]^(s/2)=2xi(s),     s in C,                (3)

is the classical Biane–Pitman–Yor identity with the stated normalization.
BOR26 supplies third-order ordering and the inverse-moment bound

    E X_n^(-b)<=12,   n>=1, 0<=b<=3,                       (4)

and its complete critical-strip convergence theorem. We import their proposed
proofs at their stated status; no parent root certificate or test suite is
being counted as newly independently verified. The contraction can also be
reproved by using independent optimal couplings of the children and computing
2 E U^(-4)=7/12. The fixed law's Laplace transform is sqrt(6t)/sinh(sqrt(6t)).

Gamma–Dirichlet factorization, entire gamma reciprocals, normal-family/Hurwitz
arguments and moment expansions are classical. This packet makes a
source-specific construction and a bounded direct test, not a priority claim.

## 2. Exact finite-depth factorization

Put a_n=k 2^n. Define bounded variables Z_n recursively by Z_0=1 and

    B_n ~ Beta(a_n,a_n),
    C_n=B_n Z_n+(1-B_n) Z_n',
    Z_(n+1)=C_n/U^2.                                     (5)

Here B_n, Z_n, Z_n', U are independent. In each occurrence use fresh copies.
Then, for every n,

    X_n = G_n Z_n in distribution,
    G_n ~ Gamma(a_n,rate k),   G_n independent of Z_n;     (6)

    X_n+X_n' = Ghat_n C_n in distribution,
    Ghat_n ~ Gamma(2a_n,rate k), independent of C_n;       (7)

    4^(-n)<=Z_n<=1,     4^(-n)<=C_n<=1.                  (8)

### Proof

The n=0 case is immediate. Assuming (6), choose independent gamma variables
G,G' of shape a_n and independent copies Z,Z'. The change of variables
(G,G')=(TB,T(1-B)) in their joint density shows T~Gamma(2a_n,rate k),
B~Beta(a_n,a_n), independent of one another and of Z,Z'. Therefore
GZ+G'Z'=T[BZ+(1-B)Z']. This proves (7); the independent common U then gives
(6) at n+1. Convex averaging preserves the interval in (8), and multiplication
by U^(-2) changes its lower endpoint by a factor 1/4. This proves (8).

In particular this is NOT an approximation by a gamma law: the bounded
factor C_n is part of the exact source. The earlier third-moment calculation
already shows that X_1 is not Gamma(5/2,rate5/2).

## 3. Exact compact Mellin factor, every pole, and rational coordinates

Let A_n=2a_n=5*2^n and define

    J_n(s)=E C_n^(s/2).                                  (9)

Since log C_n lies in [-n log4,0], J_n is entire and

    |J_n(s)|<=2^(n max(0,-Re s)).                        (10)

It is positive at EVERY real s. In the half-plane Re s>-2A_n, gamma integration
in (7) gives the exact source identity

    M_n(s)=c0^(s/2) Gamma(A_n+s/2) J_n(s)/Gamma(A_n).     (11)

The right side is the meromorphic continuation to C. Its poles are EXACTLY

    s=-2A_n-2j,  j=0,1,2,...,                           (12)

and each is simple: J_n is strictly positive there, so no pole is canceled.
In H_n the other summand M_n(1-s) is regular and positive at these real
points. Thus H_n has precisely the two simple pole strings

    -2A_n-2j,       1+2A_n+2j,   j>=0.                  (13)

The reflection reverses the residue sign of the second string, not its order.
There are no poles in the expanding strip

    -10*2^n < Re s < 1+10*2^n.                          (14)

None of these statements asserts a zero location. On the critical strip the
gamma prefactor is nonzero, but J_n(s) need not be nonzero merely because C_n
is a positive variable.

### Rational moment recursion

Write z_(n,j)=E Z_n^j, d_(n,j)=E C_n^j. Then

 d_(n,j)=sum_(l=0)^j binom(j,l) (a_n)_l(a_n)_(j-l)
                       z_(n,l)z_(n,j-l)/(2a_n)_j,
 z_(n+1,j)=[(1-2^(1-2j))/(2j-1)]d_(n,j), j>=1,         (15)

and z_(n,0)=d_(n,0)=1. The notation (a)_j is the rising factorial. Every
coefficient and every moment in (15) is rational. These formulas can be
checked against the independent raw-X recurrence

 E X_(n+1)^j = [(1-2^(1-2j))/(2j-1)]
                 sum_l binom(j,l)E X_n^l E X_n^(j-l).    (16)

### A complete finite expansion, not sampled cubature

Set b_n=4^(-n), m_n=(1+b_n)/2 and rho_n=(1-b_n)/(1+b_n). Then

 J_n(s)=m_n^(s/2) sum_(j>=0) binom(s/2,j) e_(n,j),
 e_(n,j)=E[(C_n-m_n)/m_n]^j, |e_(n,j)|<=rho_n^j.         (17)

All e_(n,j) are rational combinations of (15). On any circle |z|=r with
rho_n<r<1, let

 B_D(r)=sup_(s in D, |z|=r) |(1+z)^(s/2)|

for a specified compact complex set D. Cauchy's coefficient bound gives the
COMPLETE remainder after degree L:

 |J_n(s)-m_n^(s/2) sum_(j=0)^L binom(s/2,j)e_(n,j)|
 <= sup_D |m_n^(s/2)| B_D(r)
                       (rho_n/r)^(L+1)/(1-rho_n/r).     (18)

Cauchy on a larger s-domain gives the corresponding derivative bounds. The
branch of log(1+z) is the analytic branch in |z|<1. Every value of C_n and the
whole probability mass enter (18).

This is an exact finite-depth evaluation interface, not an efficiency claim:
rho_n tends to one. A naive expansion may require a degree exponential in n,
and converting raw moments to central moments can cause severe cancellation.
Exact rational or outward arithmetic must pay it; decimal precision alone is
not a certificate. The scout described in VALIDATION.md encountered precisely
this issue. No cost uniform in n is claimed.

## 4. Global compact convergence, including negative moments

The following extension concerns analytic convergence, NOT zero preservation.
For b>0 put

 ell(b)=max(0,ceil(log_2(b/3))).

For n>=ell(b)+1, (4) and arithmetic-geometric mean give

    E X_n^(-b) <= 2^(b ell(b)) 12^(2^ell(b)).             (19)

Indeed (x+y)^(-b)<=2^(-b)x^(-b/2)y^(-b/2), while U^(2b)<=4^b.
Thus E X_(n+1)^(-b)<=2^b(E X_n^(-b/2))^2. Iterate ell(b) times and apply (4)
to the final exponent. This proves a uniform eventual bound for EVERY fixed
negative moment, with its minimum required depth retained.

Every fixed positive integer moment is uniformly bounded as well. One explicit
induction uses U_0=U_1=1,U_2=7/5 and, for j>=3,

 U_j=max(E X_0^j,
       a_j/(1-2a_j) sum_(l=1)^(j-1) binom(j,l) U_l U_(j-l)),
 a_j=E U^(-2j).

The coefficient 2a_j is strictly less than one. Formula (16) proves the bound.
The fixed law has all moments by (3) or its positive exponential-series law.

For a fixed compact s-set, (19) and the positive moments give local uniform
bounds for M_n once n is sufficiently large. The pair has the needed inverse
moments, for example (X_n+X_n')^(-b)<=X_n^(-b). Weak convergence of the pair
follows from the W2 contraction. Truncating at small and large arguments and
using slightly stronger inverse/positive moments proves pointwise convergence
of complex powers. Dominated holomorphic differentiation or normal families
then gives

    M_n(s) -> 2xi(s), H_n(s) -> xi(s)
    locally uniformly on EVERY compact subset of C.      (20)

Precisely: each compact set lies in the holomorphy strip (14) at every
sufficiently late depth. We are not calling an individual meromorphic H_n an
entire function. This proof gives global compact convergence, not a new
relative error at zeros or an all-height rate. BOR26's stronger explicit rate
on its originally stated closed critical strip remains unchanged.

## 5. An entire representative at each finite depth

Define by analytic continuation

 E_n(s)= Gamma(A_n+1/4)^2 H_n(s)
              /[Gamma(A_n+s/2) Gamma(A_n+(1-s)/2)].       (21)

There is an explicit formula with NO meromorphic products:

 E_n(s)= Gamma(A_n+1/4)^2/[2Gamma(A_n)(1+M_n(1))]
       *[c0^(s/2)J_n(s)/Gamma(A_n+(1-s)/2)
        +c0^((1-s)/2)J_n(1-s)/Gamma(A_n+s/2)].            (22)

Thus E_n is real entire, symmetric under s->1-s, and of order at most one.
The order statement follows from (10) and the standard order-one growth of
1/Gamma; no zero hypothesis is used. On 0<=Re s<=1, the multiplier in (21)
is holomorphic and nowhere zero. Hence E_n and H_n have EXACTLY the same
critical-strip zeros with multiplicities.

For any fixed compact s-set the multiplier in (21) tends uniformly to one.
A direct proof uses

 log Gamma(A+1/4+u)+log Gamma(A+1/4-u)-2log Gamma(A+1/4)
                    =O_D(A^-1),  u=(s-1/2)/2,

obtained by two integrations of the digamma derivative on a bounded shift
set. Euler summation or its absolutely convergent series bounds that derivative
by O(1/A). Therefore (20) gives

    E_n -> xi locally uniformly on C.                    (23)

The harmless-looking normalization Gamma(A+1/4)^2 is necessary to make that
limit equal to xi rather than zero or an unspecified scale. Endpoint values
of E_n at 0,1 are not claimed exactly 1/2; those exact values belong to H_n.

This construction does NOT claim that E_n has only critical-line zeros globally.
Clearing its known poles does not move its other zeros. In particular an
unproved global Lee–Yang membership cannot be inferred from entireness.

## 6. Direct test of the proposed finishing argument, on the ACTUAL orbit

The gamma-seed theorem proves zero exclusion at high height by showing strict
increase of log |M_0(s)/M_0(1-s)| with Re s. Transferring this inequality to all
prescribed iterates would have been a convenient induction. It is false.

Define, wherever the denominator is nonzero,

 D_n(t)= [d/dsigma log |M_n(sigma+it)/M_n(1-sigma-it)|]_(sigma=1/2)
       =2 Re[M_n'(1/2+it)/M_n(1/2+it)].                  (24)

The certificate proves

    -1.427840092064 < D_1(23) < -1.427840092063.           (25)

This is n=1 from Gamma(5/2,rate5/2), NOT the earlier exponential countertest.
It therefore rejects this monotone-ratio extension on the distinguished orbit.
It does NOT assert a zero of M_1, H_1, E_1 or xi at that point, and does not
refute strip-zero preservation. In fact the denominator in (24) is separately
certified nonzero. More general phase/argument or interlacing methods remain
possible; (25) rejects only this sufficient inequality.

### 6.1 Literal source and exact central moments

Here Z_1=W=U^-2 and C_1=BW+(1-B)W', B~Beta(5,5). With R=(8/5)W-1,
let r_j=E R^j. Direct integration of d[x^j/sqrt(1+x)] on [-3/5,3/5] gives

 r_0=1,
 r_j={[(1/2)-(-1)^j](3/5)^j-jr_(j-1)}/(j-1/2).          (26)

The density normalization is included: it is (sqrt(8/5)/2)(1+x)^(-3/2).
It makes the upper/lower boundary coefficients exactly 1/2 and 1.

Let V=(8/5)C_1-1. Beta integration gives

 e_j=E V^j
   =sum_(l=0)^j [binom(l+4,4)binom(j-l+4,4)/binom(j+9,9)]
                         r_l r_(j-l).                  (27)

All quantities are rational, and |e_j|<=(3/5)^j. Formula (26) is checked at
forty orders against independent direct binomial integration in U; (27) is
checked through order24 against the raw beta moments. No empirical mixing
law or moment table is supplied as an input.

Writing

 S(s)=sum_(j>=0)binom(s/2,j)e_j,

we have J_1(s)=(5/8)^(s/2)S(s), and consequently

    M_1'/M_1 = [log(pi/15)+log(5/8)+psi(10+s/2)]/2
                         +S'(s)/S(s).                  (28)

### 6.2 Complete series and derivative enclosure

The checker retains j=0,...,240. For |s-(1/2+23i)|<=1 and |z|=4/5,
Re(s/2) lies in [-1/4,3/4], |Im(s/2)|<=12, and
1/5<=|1+z|<=9/5, |arg(1+z)|<pi/2<2. Hence

    |(1+z)^(s/2)|<10*3^24.

Cauchy in z gives coefficient bounds; Cauchy on the s-disk of radius one
pays the s derivatives with the SAME bound. Thus each complete omitted sum
for S or S' has modulus at most

    epsilon=40*3^24*(3/4)^241.                           (29)

Both real and imaginary rectangle components are inflated by epsilon. This
pays every j>240, not just the next term. S itself is shown nonzero by a
strict positive lower bound on its squared modulus. Division then encloses
(28) and (25).

For log and psi the authenticated parent interval backend uses exact integer
arithmetic with 512-bit outward dyadics, fixed complete power-series bounds,
and a shift to Re z>64 before a 24-term Bernoulli/Stirling calculation.
The remainders are controlled by the real-part form of the periodic-Bernoulli
integral, not by dropping an asymptotic remainder. No zeta, gamma or digamma
oracle enters the accepting computation. The back end is reused, not a fresh
independent numerical implementation.

## 7. The actual remaining whole-problem step

An all-height zero theorem at every finite depth is stronger than needed.
It would suffice to find prescribed depths n_j tending to infinity and heights
R_j tending to infinity such that

  E_(n_j)(s) has no zeros in 0<Re s<1, Re s!=1/2,
                                |Im s|<R_j.             OPEN-ZC

Proof of sufficiency: a hypothetical off-central xi zero lies in a small closed
disk entirely in one of the open half-strips. That disk eventually lies below
R_j. Local uniform convergence (23), and a zero-free boundary circle chosen
around the isolated xi zero, force E_(n_j) to have the same positive zero count
by Rouche, a contradiction. Equivalently use Hurwitz on each half-strip.
The classical zero-strip theorem and reflection then imply RH.

NO unbounded family of OPEN-ZC certificates or induction proving it is supplied.
The scalar formulas (15)--(18) make finite evaluations source-complete, but
finite computations do not prove OPEN-ZC. Neither positive mixing weights,
third-order convex order, moment convergence, exact pole removal nor the
Gamma starting case implies it. In particular (25) disqualifies the most direct
attempted monotonicity proof for the special orbit, not just for other seeds.

The work is therefore a direct continuation with a completed analytic source
representation and a failed proposed induction, NOT finishing touches on a
completed Riemann proof. Reviewers are asked to check the stated components,
not fill the missing zero-confinement theorem.

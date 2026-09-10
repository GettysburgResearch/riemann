# A compact-annulus, square-sampled alternative to the all-window sign

Status: PROPOSED COMPLETE REDUCTION AND OBSTRUCTION PROOFS; independent review required.
The terminal arithmetic inequality is OPEN. No RH proof, new all-window sign,
or independent acceptance of the parent certificates is claimed.
Parent: PR #803, 893d93b045099d9920fadf4b0e5bcb51d0455832.
Local labels AS1--AS6 belong only to this packet.

The objective was to turn the certified length-one result into positivity at
unbounded lengths. No valid induction was obtained. The alternative here removes
the growing Schur matrices, the safe prime-tail constant, and even the gamma
correction from the terminal premise. It leaves one explicitly normalized
finite prime-power lower bound at each perfect-square scale. This is still an
RH-equivalent bound, not a solution merely because it is elementary to state.
Scalar Landau/screw criteria and annular zero-safe filters have substantial
prior art, including Suzuki and this repository's #352; no priority or
minimal-annulus claim is made. See SOURCES.md for the precise comparison.

## 1. Statement of the alternative arithmetic problem

For an integer m >= 2 define the NONNEGATIVE rational coefficients

 a_m(n) = 64n-m^6/n^2,             m^2/4 < n <= m^2,
          64m^6/n^2-n,            m^2 < n <= 4m^2,
          0,                     otherwise.

The values at the two outside endpoints are zero, and the two formulas agree
at the center. Let Lambda(n)=log p for n=p^k, k>=1, and zero otherwise. Put

 B_m = sum_(m^2/4<n<=4m^2) a_m(n) Lambda(n),
 D_m = B_m/(192 m^3) - 45m/128 + 1/4.                       (1)

**AS1 (square-sampled compact-annulus criterion).** The following are equivalent:

 (i) RH;
 (ii) D_m >= 0 for every sufficiently large integer m;
 (iii) D_m > 0 for every integer m >= 2;
 (iv) the original W form is positive semidefinite on every finite interval.

In fact RH implies D_m > 1/10 for EVERY m>=2. This positive safety margin is
not a proof that (ii) holds. It is obtained by choosing a deliberately loose
rational offset rather than trying to force a zero-margin two-point deficit.

An equivalent terminal bound is

 B_m >= (135/2)m^4 - 48m^3,             all sufficiently large integers m. (2)

Every term in B_m is a rational multiple of a logarithm of an ordinary prime.
No zero ordinate, special-function evaluation, infinite prime tail, hypothetical
zero-dependent detector, or numerical matrix occurs in (2). All prime POWERS
in the annulus must be retained. Substituting primes only changes the problem.
Finite checks of (2) do not prove its eventual or universal quantifier.

## 2. Fix and filter the actual kernel, before introducing a zero

Use the parent's source normalization

 b=3/2, d=log 4, c=exp(-bd)=1/8,
 C_b=(1-gamma_E-log(2pi))/3,
 P2=sum_(n>=2) Lambda(n)/n^2=-zeta'(2)/zeta(2),
 alpha_j=2j+1/2,
 S(x)=sum_(j>=1) exp(-alpha_j x)/(alpha_j^2-b^2), x>=0.

The even continuous arithmetic kernel W is defined for x>=0 by

 W(x)=exp(x/2)/2+C_b exp(-bx)+S(x)-(P2/b)cosh(bx)
       +(1/b)sum_(2<=n<=exp x) Lambda(n)/sqrt(n)
                                      sinh(b(x-log n)).           (3)

A prime at a boundary contributes zero to W but its derivative jump is kept.
All series in (3) have their full source meaning. The defining tail P2 is
absolutely convergent; no finite zero census enters this definition.

Define on the whole real line

 V(x)=(1+c^2)W(x)-c W(x-d)-c W(x+d),
 A(s)=(1-c exp(ds))(1-c exp(-ds))
     =65/64-(exp(ds)+exp(-ds))/8.                            (4)

This is the autocorrelation filter of the fixed signed measure delta_0-c delta_d.
On a real spectral frequency lambda,

 A(i lambda)=|1-c exp(i d lambda)|^2 >= (1-c)^2=49/64.       (5)

All zeros of A lie on Re(s)=b or Re(s)=-b. In particular no zero in the
RH-sensitive strip 0<Re(s)<1/2 is removed. This check is independent of the
existence, height, or multiplicity of a hypothetical off-line zeta zero.

**AS2 (exact tail elimination).** For X>=4,

 V(log X)= (45/128)sqrt(X) - P(X) - E(X),                    (6)

where

 P(X)= (1/(192 X^(3/2))) [
           sum_(X/4<n<=X) (64n-X^3/n^2)Lambda(n)
          +sum_(X<n<=4X) (64X^3/n^2-n)Lambda(n)],             (7)
 E(X)=c S(log(X/4))+c S(log(4X))-(1+c^2)S(log X).            (8)

Both P and E are nonnegative. Moreover

 0 <= E(X) < 1/10,       X>=4,       E(X)->0 as X->infinity. (9)

Proof. The filter annihilates exp(bx), exp(-bx) and hence the complete P2 term
for x>=d. It also annihilates C_b exp(-bx) there. The exp(x/2)/2 contribution
is A(1/2)exp(x/2)/2=45 exp(x/2)/128.

For a single activated prime-power cusp, writing l=log n,

 (1+c^2)sinh(b(x-l))_+ -c sinh(b(x-d-l))_+
                         -c sinh(b(x+d-l))_+
 = -c sinh(b(d-|x-l|)) 1_(|x-l|<d).                        (10)

Here sinh(bu)_+ means sinh(bu)1_(u>=0), not max(sinh(bu),0) outside
its stated use. Equation (10) follows separately in its four intervals,
including the two zero-valued endpoints. Multiplication by Lambda(n)/(b sqrt n)
gives (7). For example, when n<=X its weight is

 Lambda(n)[n/(3X^(3/2))-X^(3/2)/(192n^2)].

For each gamma exponent alpha_j>b, A(alpha_j)<0. Thus (8) is a positive
sum of exponential terms. Uniform convergence extends this assertion to X=4.
Also S is decreasing and nonnegative, with

 S(0)=1/6+(log 2)/3 < 2/5.

Dropping the negative term in (8) gives E(X)<=2c S(0)<1/10. Dominated
convergence of the summable series proves E(X)->0. This proves AS2.
No PNT, RH assumption, or approximate cancellation was used.

The same filter has an exact inverse on this source class. As a measure,

 eta=(1-c^2)^(-1) sum_(j in Z) c^|j| delta_(jd),
 W=eta*V.                                                   (10a)

The coefficients satisfy (1+c^2)eta_j-c eta_(j-1)-c eta_(j+1)=delta_(j0).
The source growth and c exp(d/2)=1/4 justify all sums and the vanishing
boundary terms in their telescoping. The Fourier multiplier of eta is
1/A(i lambda)>0. Thus global positive definiteness of V and W is equivalent;
this is not an assertion that arbitrary positive averages of translates
preserve positive definiteness without a multiplier check.

There is also a fixed four-point interpretation. For

 mu_x=(delta_0-delta_x)*(delta_0-c delta_d),

its W-energy is exactly 2[V(0)-V(x)]. Coincident points are combined rather
than treated as independent labels. Continuity of W permits approximation
of this finite signed measure by compactly supported L2 bumps. The problem
can therefore be tested on one fixed coefficient pattern at unbounded
separations, rather than on matrices whose dimension grows with length.
A uniform lower bound for this one energy already suffices by AS3; no
claim is made that the length-one certificate provides that lower bound.

## 3. The exact fixed comparison constant is elementary

Write C0=V(0). A calculation using only primes 2 and 3 gives

 C0 = 47/64 - (21/64)(gamma_E+log pi)
             +(115/96)log 2 -(641/1728)log 3 -(65/192)log 5. (11)

In particular the bounded exact checker proves

 1/25 < C0 < 1/20.                                         (12)

The deliberately coarse accepted enclosure is based on the tighter computed
interval [0.0473031195,0.0473031978]. These displayed endpoints are rounded
outwards. The acceptance comparison uses dyadic rationals, not the decimals.

Here are derivation checks. The source values are

 W(0)=1-(gamma_E+log pi)/3-(2/3)P2,
 S(log 4)=1/12+(1/48)log(5/3)+(4/3)log(15/16),
 W(log 4)=1+C_b/8+S(log 4)-(65/24)P2
                           +(7/12)log 2+(37/216)log 3.

Then C0=(65/64)W(0)-W(log 4)/4; the P2 coefficient is exactly zero.
The formula for S(log 4) follows from

 1/(alpha_j^2-b^2)=(1/3)[1/(2j-1)-1/(2j+2)].

For y=exp(-x) in (0,1), one may alternatively use the elementary identity

 S(x)=(y^(3/2)/3)atanh(y)
                     +(y^(-3/2)/6)[log(1-y^2)+y^2].        (13)

Its limit at y=1 is the preceding S(0). No unvalidated evaluation of an
infinite gamma series is needed for (11).

The scalar interval check uses only integer/Fraction operations. It encloses
logarithms by the positive atanh series with its geometric remainder and pi
by Machin's identity with alternating remainders. For gamma_E it uses

 H_N-log N-1/(2N) < gamma_E < H_N-log N-1/(2N+1), N=1024.    (14)

For completeness: the left sequence increases by the strict trapezoidal
inequality for the convex function 1/x and tends to gamma_E. The right
sequence decreases: log(1+1/n)>2/(2n+1) gives its increment less than
-1/[(n+1)(2n+1)(2n+3)]. Both limits are gamma_E. This proves (14), including
the orientation of the enclosure. The primitive contract is reproduced in
verify.py, not imported from the length-one numerical certificate.

## 4. RH supplies a scalar bound, but it is not assumed in the converse

Let H(r)=xi'(1/2+r)/xi(1/2+r), with the entire removable-point normalization
xi(0)=xi(1)=1/2. The classical source identity, rechecked below, is

 F_W(r):=int_0^infinity exp(-rx)W(x)dx
             =[H(r)-(r/b)H(b)]/(b^2-r^2), Re(r)>1/2.       (15)

The point r=b is removable. Under RH the paired Hadamard product and the
O(T log T) zero count give

 W(x)=2 sum_(gamma>0) m_gamma cos(gamma x)/(b^2+gamma^2),
 V(x)=2 sum_(gamma>0) m_gamma A(i gamma)
                                      cos(gamma x)/(b^2+gamma^2). (16)

Both series are absolutely and uniformly convergent on the real axis. Their
normalization is fixed by (15), not by calling a function a Weil kernel.
All multiplicities are included; simplicity and a verified zero prefix are
not used. This follows either by termwise Laplace transform and uniqueness,
or directly from the classical explicit formula.

Equation (5) makes V positive definite and |V(x)|<=C0. Hence (6),(9),(12) imply

 P(X) > (45/128)sqrt(X)-3/20,                all X>=4.       (17)

In particular D_m>1/10 under RH. This proves necessity in AS1, with a
uniform rational slack. It does NOT prove (17) without RH.

We now remove that RH hypothesis from the reverse implication.

## 5. One-sided polynomial growth already excludes an off-line zero

**AS3 (one-sided Landau transfer).** If the actual V satisfies

 V(x)<=C(1+x)^k for all sufficiently large x,

for some C>=0 and integer k>=0, then RH holds. More generally, a one-sided
upper bound V(x)<=C_epsilon exp(epsilon x) for each epsilon>0 suffices.

Proof. First retain the finite-boundary term in translating a one-sided
Laplace transform. For Re(r)>1/2, a direct change of variables gives

 F_V(r)=A(r)F_W(r)+J_d(r),
 J_d(r)=2c int_0^d sinh(r(d-u))W(u)du.                      (18)

The function J_d is entire. It must not be dropped even though it cannot
cancel the poles at issue. The right side of (18) is meromorphic everywhere,
and analytic at every positive real r. Indeed xi(1/2+r)>0 there: above one
use the Euler product, below one use the alternating eta series, and at one
use the nonzero removable value. The apparent pole at b in (15) is removable.

If rho is any nontrivial zero with Re(rho)>1/2, r0=rho-1/2 is a pole of F_V
with residue

 Res_(r=r0) F_V(r)=m_rho A(r0)/(b^2-r0^2) !=0.              (19)

No rightmost-zero or simplicity assumption is made. The filter is fixed
before rho; its zeros cannot occur in the required strip. The finite entire
term J_d and a Laplace transform of a polynomial cannot cancel (19).

Choose a polynomial majorant B(x)=C'(1+x)^k and start the integral at a
threshold where g(x)=B(x)-V(x)>=0. This nonnegative, locally integrable
density is of finite exponential order, since (3) gives
W(x)=O((1+x)exp(x/2)); details also follow from Section 6. If its real
Laplace abscissa sigma_c is finite, it is singular at the real point sigma_c
by the elementary Landau theorem. If sigma_c=-infinity its transform is
entire. The pole (19) forces sigma_c>=Re(r0)>0, hence finite. But (18) and
the polynomial transform are analytic at that positive real sigma_c, a
contradiction. Equality of these continuations is first established where
both integrals converge, then extended by the identity theorem; no
meromorphic boundary integral is identified with a divergent causal norm.

For the exponential version choose 0<epsilon<Re(r0); the majorant transform
has its only relevant real singularity at epsilon, strictly left of sigma_c.
The same contradiction follows. Reflection of nontrivial zeros gives RH.

Here is the Landau step in brief, not a new assumed arithmetic estimate.
For g>=0 and sigma1>sigma_c, the derivatives of its Laplace transform are
the integrals of (-x)^n exp(-sigma1 x)g(x). If the transform is analytic at
the real boundary sigma_c, choose sigma1 close enough that its Taylor disk
extends to a real sigma2<sigma_c. Taylor's series at sigma1, evaluated toward
the left, is a sum of NONNEGATIVE integrals. Tonelli identifies it with the
integral at sigma2, contradicting the definition of sigma_c. Finite compact
initial terms have entire transforms and do not change the argument.

This is a source-specific application of classical one-sign Laplace theory,
closely related to Suzuki's screw criterion. It is not presented as a new
general principle.

## 6. Perfect squares do not miss the required continuous growth

**AS4 (explicit interpolation).** For X>=8, away from its finite local set
of prime-log knots,

 |V'(log X)| <= 6 sqrt(X) log(8X).                           (20)

Consequently, for m>=3 and m^2<=X<=(m+1)^2,

 |V(log X)-V(log m^2)| <=18 log(32X).                       (21)

These are unconditional bounds for the complete source. The prime knots
cause finite derivative jumps, not jumps in W or V; local absolute continuity
therefore suffices to integrate the almost-everywhere derivative bound.

Derivation. With R_2(X)=sum_(n>X)Lambda(n)/n^2 and
A_1(X)=sum_(n<=X)n Lambda(n), recombine (3) BEFORE estimating:

 W(log X)=sqrt(X)/2-X^(3/2)R_2(X)/3
                   +X^(-3/2)[C_b-P2/3-A_1(X)/3]+S(log X).

Between knots the derivative with respect to log X is

 sqrt(X)/4-X^(3/2)R_2(X)/2
                   +X^(-3/2)[A_1(X)+P2-3C_b]/2+S'(log X).

For X>=2, use Lambda(n)<=log n, floor X>=X/2, and decreasing-function
integral comparison to obtain
R_2(X)<=2(log X+1)/X, A_1(X)<=X^2 log X, P2<2, |C_b|<1.
Also |S'(log X)|<1/3: alpha_j/(alpha_j^2-b^2)<=1 and the remaining
geometric series starts at j=1. These bounds give

 |W'(log X)| <=4 sqrt(X) log(2X).

Apply this at X, X/4 and 4X. The coefficient is
4[65/64+(1/8)(1/2+2)]=85/16<6, proving (20). Integration over a log gap
at most 2/m, using sqrt(X)<=m+1, proves (21). No PNT is used here.

Now assume (ii) of AS1. At square samples (6),(9),(1) give
V(log m^2)<=1/4. Thus (21) supplies V(log X)=O(log X) as a ONE-SIDED
upper bound for every sufficiently large real X. AS3 proves RH, and (16)
then gives (iv). Conversely (iv), by approximation of point masses with
L2 bumps, makes W positive definite; |W(x)|<=W(0) and (15) prove RH.
All parts of AS1 follow. The existence of a single positive interval is
not used anywhere to infer an unbounded quantifier.

The square spacing is purposeful. A mesh with gaps X^(1/2+o(1)) gives
subpower interpolation error from (20). For polynomial sampling X=m^k
with k>2, this derivative estimate alone is insufficient: the smooth
function

 f(X)=X^(1/2-1/k) sin^2(pi X^(1/k)), X>=1,

vanishes at every sample, has derivative O(X^-1/2), yet has unbounded
power-sized peaks. This is a synthetic sampling counterexample, not an
actual prime-source function and not an impossibility theorem for denser
information. No claim that squares are universally optimal is made.

### 6.1 An individual-zero obstruction on the arithmetic square samples

**AS6.** Suppose rho is a nontrivial zero with beta=Re(rho)>1/2. For every
0<=a<beta-1/2 the normalized scalar sequence (1) satisfies

 limsup_(m->infinity) D_m/m^(2a)=+infinity,
 liminf_(m->infinity) D_m/m^(2a)=-infinity.                  (21a)

To prove the second assertion by contradiction, a finite liminf would bound
D_m below by -C m^(2a), hence bound V(log m^2) above by C' m^(2a), using
(6),(9). Interpolation adds only O(log X). For a>0 the added term is
absorbed in the exponential envelope at exponent a; for a=0 use the
polynomial envelope in AS3. The pole at rho-1/2 then contradicts the Landau
argument (choose an exponent strictly between a and beta-1/2 if necessary).
For the first assertion apply the same argument to -V; its pole is equally
nonremovable. This proof permits every multiplicity and does not require a
rightmost off-line zero. A single hypothetical finite-height exception
cannot be hidden in a density limit or missed by the square sampling.

## 7. A stronger source-normalized obstruction to local bootstrap

**AS5.** Local agreement with the actual W, the exact safe constant P2,
nonnegative source weights, and even the prime-number asymptotic together
do not force global positivity if the actual discrete arithmetic source is
replaced by an arbitrary positive measure.

This is NOT a counterexample to RH or to the actual prime-power source.
Its purpose is to locate which information a claimed extension rule must use.
It is stronger than an arbitrary bump added to the final kernel: the
perturbation is made at the source level and preserves P2 exactly.

Fix any desired finite agreement length L0. Take eta=1/4, tau=1, epsilon=1/4.
Choose Y>max(4,exp L0) sufficiently large. Up to Y retain exactly the actual
measure sum_(n<=Y)Lambda(n)delta_n. Above Y use the density

 lambda_Y(y)=1+epsilon y^(-eta)cos(tau log y)
                                  +kappa_Y 1_(Y<y<=2Y),
 kappa_Y=2Y[R_2(Y)-1/Y-epsilon Re(Y^(-1-eta+i tau)/(1+eta-i tau))]. (22)

The classical PNT implies Y R_2(Y)->1, so |kappa_Y|<1/4 for all sufficiently
large Y. Hence lambda_Y>=1/2. Direct integration gives

 int_(Y,infinity) y^-2 lambda_Y(y)dy = R_2(Y).

Thus the entire modified measure has exactly the same P2. Its cumulative
mass is x+O_Y(x^(3/4)+1), and its kernel, defined by (3) with the corresponding
Stieltjes integral, agrees with the actual W on |x|<=L0. The archimedean
source is unchanged. Every earlier local positive certificate remains valid
for this modified kernel on the agreement interval.

For X>8Y, its entire annulus lies above the finite correction. A Mellin
calculation gives exactly

 P_Y(X)= (45/128)sqrt(X)+epsilon Re[J(rho)X^(rho-1/2)],
 rho=3/4+i,
 J(rho)=A(rho-1/2)/(b^2-(rho-1/2)^2) !=0.                  (23)

For example integrate the two polynomial pieces in (7). Equivalently,

 J(rho)=(c/b)int_(-d)^d exp((rho-1/2)u)sinh(b(d-|u|))du.

Consequently its filtered V_Y has positive and negative excursions of order
X^(1/4); E(X)->0 cannot remove them. The same excursions are seen at squares:
the phase increments 2 log((m+1)/m) tend to zero while the phase is unbounded,
so infinitely many samples lie in each fixed phase arc. Thus this source
fails (2) at arbitrarily large m despite preserving the exact local data
and P2 and satisfying a PNT asymptotic.

The lost property is the literal integer prime-power measure/Euler-product
arithmetic, not the local certificate or a missing tail-normalization term.
Therefore an all-length proof based only on those preserved properties
cannot work. The example does not rule out an argument using the actual
arithmetic structure. PNT is used only to construct this countermodel, not
in AS1--AS4.

## 8. Direct check of the inherited analytic source identity

The mathematical starting identities are the classical completed-xi product,
the logarithmic derivative of zeta on Re(s)>1, and digamma partial fractions.
For clarity (15) can first be derived on Re(r)>b, where the separate terms
of (3) are individually integrable. There

 int exp(-rx) sinh(b(x-log n))1_(x>=log n) dx
                              =n^-r b/(r^2-b^2),
 int exp(-rx) cosh(bx)dx=r/(r^2-b^2).

These give the prime part
[-zeta'/zeta(r+1/2)-(r/b)P2]/(r^2-b^2). The gamma/rational part follows
from the partial fractions in Section 3 and

 H(r)=1/(r+1/2)+1/(r-1/2)-(log pi)/2
                  +psi(1/4+r/2)/2+zeta'/zeta(r+1/2),
 H(b)/b=1-(gamma_E+log pi)/3-(2/3)P2=W(0).

Summing the convergent digamma differences gives exactly the remaining
[ -H(r)+(r/b)H(b)]/(r^2-b^2) terms. Direct recombination as in Section 6
gives W(x)=O((1+x)exp(x/2)), so both sides are analytic on Re(r)>1/2
(with r=b removable). The identity theorem extends the equality there.
This passage does not interchange divergent separate carrier integrals.

The gamma series is absolutely summable in value at zero. On every compact
positive x interval it is differentiable termwise; near zero its derivative
is O(1+|log x|), so W is locally absolutely continuous. These facts justify
all finite-boundary integrals used in (18).

## 9. What was attempted and what remains

The successful connection is a positive autocorrelation filter that
annihilates the growing/decaying b-carriers and turns the remaining prime
part into a POSITIVE compact Green bump. One-sided Landau transfer then
reduces all-window positivity to the rational-slack inequality (2), with
square-sampled interpolation covering the continuous half-line.

A proposed bootstrap from the parent's local certificate plus positive
arithmetic coefficients or a PNT estimate is stopped by AS5. Ordinary PNT
only gives P(X)=(45/128+o(1))sqrt(X), not the fixed-error lower bound. Taking
absolute values of individual local-defect or carrier terms loses the exact
square-root-scale cancellation. No factorial/binomial majorization or
source recurrence proving (2) is obtained in this pass.

The concrete next theorem is therefore exactly (2), or the weaker

 P(m^2)>=45m/128-C_epsilon m^epsilon
                for every epsilon>0 and every sufficiently large m. (24)

With the same interpolation and AS3, (24) is also RH-equivalent. The constants
and thresholds may depend on epsilon; they may not depend on a hypothetical
zero. A finite prefix, a density-one set of successful m, or a selected
subsequence with unbounded gaps does not establish either quantifier.

This route has different practical inputs from the effective-Schur route,
but no claim is made that an RH-equivalent reformulation by itself brings
an RH proof closer. It does remove the infinite prime-tail primitive and
all growing matrix dimensions from the exact terminal arithmetic premise.

## 10. Executable scope

verify.py reconstructs (11)--(14), exact filter/cusp/Mellin identities on
bounded rational controls, the prime-power sieve against independent trial
factorization through 256, and the actual scalar inequalities D_m>0 for
2<=m<=64. The minimum certified sample margin lies between 0.2162828059 and
0.2162828060. This sample checks only the new scalar route, NOT positivity
on any new continuum window. It is not evidence for (2) at unbounded m.

The code uses explicit exceptions, not assertions removed by python -O.
Stored JSON is compared after fresh reconstruction; duplicate keys and
Boolean/numeric aliases are refused. The delivery manifest is a content
integrity mechanism, not an independent mathematical referee. No Lean,
Comparator, kernel build, upstream campaign, or external priority audit was run.

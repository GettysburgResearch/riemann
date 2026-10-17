# Off-central numerator moments and a proposed 49/54 all-field boundary

**Status: PROPOSED composition of stated unconditional CT/BGL/DF inputs and the
new deductions in MOMENTS.md. Independent mathematical review is required.**
No RH/GRH, critical native moment, signed-covariance hypothesis, #961 OPEN-L,
#966 selected-count theorem, or earlier proposed zero-free CONCLUSION is assumed.
This is not an accepted theorem or Lean verification.

## 1. Proposed conclusion and exact dependencies

    zeta_K(s) != 0 for every number field K, Re(s)>49/54, s!=1. (1)

The same strict region is proposed for finite-order Hecke L-functions, including
nonvanishing at one for nonprincipal characters. Principal functions have a pole
at one; it is not called a nonzero value. No boundary-line assertion or uniform
field/conductor/discriminant constant is made. Infinite-order angular twists
are not covered. The reported special-setting 7/8 result is not improved.

Fix F containing mu_12 and CT's finite S, quotient Gamma=(R*)^6, local vectors,
balanced representatives, measures and smoothing functions, R=O_(F,S).
CT is Cureton--Thorner, Hexagon 2610.00200v2; DF is arXiv:2610.04045v1;
BGL is arXiv:1112.1650. SOURCE_REVIEW.md records actual reading and limitations.

The short-support reconstruction is inherited from #965, PROOF Section 2,
commit d58e3282a9379b6ae165681bc2e21e4f9fd18c26. Its conclusion is a bound for
the actual reflected source, not its proposed 91/100 zero-free conclusion.
The old thirteen-file write-up delivered in this conversation is separately
recovered unchanged by #967. We do not conflate those different source trees.

## 2. Complete physical pairing at the new scale

CT's literal pairing is an integral over the fixed compact norm-one quotient
of sum_(m!=0) A_t(m;X,Y) B_m(Z). Its additive estimate before the original
scale substitution is

    sum_m |A_t(m;X,Y)|^2 << 1/X+1/Y.                       (2)

For completeness, the needed short-support reconstruction retains, for each
mR=h d with h powerful and d squarefree, CT's COMPLETE separated reflection

    omega rho(d) lambda(c)/(sqrt(q_c)q_n) chi_d(c)^3
               Phi(Z q_af q_c q_n^3/(q_d^2 q_f^2)).       (3)

Here c is squarefree, n is unrestricted, f|rad(h), af is supported on f, all
fixed local classes are included, and the original coprimality zeros remain.
The fixed finite profiles have two logarithmic derivatives bounded by
min(x^(1/8),x^(-Adec)), for any fixed Adec. The local coefficient majorants are
beta_p(0)=1, beta_p(1+3j)=Q^(-j), beta_p(3j)=Q^(1/2-j) for j>=1, and
beta_p(2+3j)=0. CT's quadratic-family sieve is applied INSIDE the c sum.

Here is why this reconstruction is valid below XY=Z, rather than an illegal
extension of CT's supercritical corollary. Put d~D, c~C, and
L=D^2 q_f^2/(Z q_af). Local Fourier separation of Phi gives the root bound

    beta_f(af) q_n^(-1) D^(b/2) C^(b/2)
               (sqrt D+sqrt C) min((C q_n^3/L)^(1/8),
                                     (C q_n^3/L)^(-Adec)).

For every r>0 and EVERY T>0, the dyadic sum
sum_C C^r min((C/T)^(1/8),(C/T)^(-Adec)) is O(T^r) when Adec>r.
For T<1 the entire tail is O(T^Adec)<=O(T^r); no subunit column is discarded.
Apply this with r=b/2 and (1+b)/2, with b>0. The full n sums then have
convergent weights q_n^(-1-3b/2) and q_n^(-5/2-3b/2). One cannot set b=0.
The fixed-h root bound is, up to arbitrarily small powers,

    sum_(f,af) beta_f(af) [sqrt D + D q_f/(sqrt Z sqrt(q_af))].

The two local sums are

    S0(Q)=1+(1+Q^(-1/2))/(1-Q^(-1)),
    S1(Q)=1+(Q^(-1/2)+Q^(-2))/(1-Q^(-5/2)).

Thus the two products over p|h are bounded by q_h^eta and
N rad(h) q_h^eta<=q_h^(1/2+eta). There are O(P^(1/2)) powerful h of norm~P,
by the canonical square-times-cube decomposition. Balanced physical generators
have bounded multiplicity on the fixed compact shape set. Squaring the root
bound and summing h gives

    Q_Z(P,D) << (PD)^eta P^(1/2)(D+D^2 P/Z).               (4)

For physical support q_m<<T, PD<<T, both terms in (4) retain P^(-1/2) after
using that support bound. Summing the dyads gives

    sum_(physical support) |B_m(Z)|^2 << Z^eta(T+T^2/Z),   (5)

for T a fixed positive power of Z. All auxiliary sums were justified by
summable majorants before taking limits. The diagonal T is NOT absorbed by
T^2/Z below T=Z. Equations (3)--(5) are the #965 reconstruction, recalled to
state the inherited analytic obligation; they are not a second new result.

Choose, with NO epsilon perturbation of a,

    a=4/9, h=1-a=5/9, X=Y=Z^a, M=2a=8/9<1.              (6)

The reflected square grows as Z^(8/9+eta), and (2) costs Z^(-4/9).
Cauchy and the compact quotient integral therefore give

    |I(X,Y,Z)| << Z^(2/9+eta).                            (7)

This is the full physical pairing, not a selected sector or changed source.

## 3. The exact Poisson family and correction domain

CT's initial triple integral on (Re xi,Re w,Re z)=(4,4,2) has u-summand

    X^(1/2-z) Z^(xi+z-1) Y^(w-1) q_u^(-z)
         zeta_F^S(6z) L_F^S(w,chi_u) H_u(xi,w,z)
                                 /L_F^S(xi,bar chi_u).   (8)

There is one principal row u=1. The other rows are sixth-power-free exterior
ideals, each with one of finitely many fixed S-unit sixth classes, ordered by
FULL norm. The fixed weight has joint vertical decay, for any fixed Adec,

    exp[-(Im xi+Im z)^2](1+|Im z|)^(-Adec)(1+|Im w|)^(-Adec). (9)

It is not Gaussian decay in xi alone. For x=Re xi,y=Re w,z=Re z the correction
is holomorphic and O_eta(q_u^eta), uniformly in height on fixed-margin regions:

    x,y,z>0; 6z+y>1; x+6z>1; x+y>1; x+y+6z>2;
    6x+6z>5; x>1/2; 3x>2; 3x+y>5/2.                     (10)

All eleven inequalities, including BOTH branches of CT's maximum, are retained.
This domain is convex, which validates connecting real contour segments.

For the family identification write u=epsilon g(b) modulo Gamma. Choose DF's
deep S-ray modulus so its congruent-to-one elements are local sixth powers.
Choose its generating representatives E0 with m_E0=g(E0) and extend them
multiplicatively. In b=(x0)E h0^6, the generator x0 m_E g(h0)^6 has CT's allowed
local class and differs from g(b) by Gamma. The construction chooses h0 coprime
to the tested ideal. Thus the residue symbols agree on units, and both have
zero at every shared exterior prime. Consequently

    chi_u=psi_epsilon chi_b^DF, psi_epsilon(l)=(epsilon/l)_6. (11)

These twists have fixed S-supported conductor and belong to the fixed deep
ray group; they are not the angular theta character. Conjugation changes the
sign of the zero height, so symmetric rectangles retain the same count.
MOMENTS.md treats exactly this family, all columns, conductor strata, and both
functional-equation terms. For a row class of size O(U^nu) it supplies the
costs r2,r4,r8 in its equation (10). At all other needed 0<y<=1 retain
individual convexity r=nu+(1-y)/2. Reciprocal and correction bounds are taken
uniformly BEFORE these numerator means. No statistical independence is used.

## 4. Original DF density; fixed zero-free rectangles

We do NOT require #966's stronger selected-count density. Write g(sigma) for
DF Corollary 1.5's n=6 full-family exponent. Its complete Section 9 detector,
with A=N^r and B=N^s T^(zd), yields the ten norm powers

    1/2+(1/2-sigma)s+c/2,
                   c=r,1,r/3+5/6,5r/6+1/3;
    (2-2sigma)s; 1+(1-2sigma)r;
    1/3+(11/6-2sigma)v, v=r,s;
    5/6+(4/3-2sigma)v, v=r,s.                            (12)

Both endpoints of both supremum monomials are present. With q=2sigma-1 the
explicit DF substitutions are:

* If 6q<=2: r=1/2, s=2/(4-6q), g=1-q/(4-6q).
* If 2<=6q<=5: D=6q(10-6q)-10,
  r=(24q-5)/D, s=(42q-8)/D, g=(9q(7-6q)-10)/D.
* If 5<=6q: D=1-6(1-q)^2,
  r=(6q-4)/D, s=(8q-5)/D, g=(1-q)(8q-5)/D.

In all cases z=1/(6-4sigma); the height bound is 1+d(1-sigma)/(3-2sigma).
The fixed twists in (11) multiply detector columns and leave its complete
means and original zeros intact. In particular, its central second mean is
the k=1 case of MOMENTS.md (or BGL (5.1)). Complete powerful columns are handled
as in BGL/DF; no column restriction is silently imposed on the detector.

Fix 0<e<=10^(-6) for the rest of the proof. For the fourteen thresholds in
Section 5, first choose one sufficiently small rho>0 depending on e,F and
all fixed moment height powers. Then fix density losses so that the number
of rows u~U whose inducing denominator has a zero with Re s>=sigma_j and
|Im s|<=4U^rho is O(U^(g(sigma_j)+e)). Call these nested sets E_j(U).
For strict zero-count conventions move thresholds slightly left and spend a
part of e. Missing Euler factors have no zeros on Re s>0.

For u outside E_j, logarithms of L are defined on the usual concentric disks
about 2+it, |t|<=2U^rho, with radii

    2-sigma_j-e/4, 2-sigma_j-e/2, 2-sigma_j-e, 1-e/4.

They are ordered and lie in the actual zero-free rectangle for large U.
Borel--Caratheodory bounds log L on the second disk by O_e(log U); the inner
disk lies in an Euler half-plane and has O_e(1) logarithm. Three circles gives
O_e((log U)^theta), theta<1, on the target disk. Consequently, for EVERY later
eta>0,

    |1/L_F^S(x+it,bar chi_u)| <<_(e,eta) U^eta,
    sigma_j+e<=x<=1+e, |t|<=2U^rho.                       (13)

The sets and rho have already been fixed and do not change as later eta
shrinks. On x>1 use Euler convergence without a zero-free premise. Bounded
small U is absorbed in fixed-data constants.

## 5. Fifteen complete classes

Set z_c=2/5 and treat Z^(1/100)<U<=Z^(h+e) by the following thresholds.
The table gives the count exponent and the NEXT class's numerator method.

|j|sigma_j|g(sigma_j)|method on E_j minus E_(j+1)|
|---|---|---|---|
|0|2/3|5/6|fourth, y=5/12|
|1|29/40|1483/1942|fourth, y=5/12|
|2|377/500|126071/174839|eighth, y=1/4|
|3|773/1000|1037467/1503478|eighth, y=1/4|
|4|197/250|65407/98563|eighth, y=1/4|
|5|801/1000|1044523/1634182|eighth, y=1/4|
|6|813/1000|1034587/1681558|eighth, y=1/4|
|7|103/125|127331/215054|eighth, y=1/4|
|8|209/250|62113/109867|eighth, y=1/4|
|9|849/1000|958123/1792582|eighth, y=1/4|
|10|108/125|113201/228134|eighth, y=1/4|
|11|441/500|103319/231671|eighth, y=1/4|
|12|907/1000|687727/1873318|convexity, y=23/500+e|
|13|477/500|6509/29663|last class, see below|

Outside E_0 use x=2/3+e,y=1/2,nu=1 and the second mean. On each middle class
use x=sigma_(j+1)+e and nu=g(sigma_j)+e with the listed numerator. On E_13 use
x=1+e,y=e,nu=g(sigma_13)+e and individual convexity. These are FIFTEEN disjoint
classes covering every nonprincipal row. The middle count is at its LOWER
threshold; its contour moves only past its UPPER threshold.

Starting from (1+e,1+e,z_c), move the truncated xi contour to x by (13), then
move w to y. The last class needs no leftward xi shift. Every vertex satisfies
(10), hence every connecting real segment does. The characters are nonprincipal;
w crosses no pole, z_c>1/6, and no denominator zero is crossed inside the actual
truncated rectangle. The first threshold is exactly 2/3 but x=2/3+e is legal;
we never apply a correction estimate at x=2/3.

Define the scale exponent and the full dyadic exponent by

    E(x,y,z)=a/2+x-1+h z+a(y-1),
    P=E(x,y,z_c)+(h+e)(r-z_c).                            (14)

All r-z_c are positive, so the upper dyad gives the maximum. For the good
class the exact P is 2/9+8e/5. The thirteen middle classes have
P=c_j+k_j e+l_j e^2, with c_j<2/9, k_j<5/2, and l_j in {3/4,7/8,1/2}.
Their smallest constant margin is

    2/9-c_12=1763671/1685986200>0.                        (15)

The last class has c=94753/533934 and positive margin 23899/533934. The exact
coefficients of EVERY class are in CHECKS.json, generated directly from (12)
and (14). Rational Bernstein coefficients certify P<=2/9+3e throughout
0<=e<=10^(-6); the analytic domains use only e>0. For instance the first middle
class is 119/540+(79/40)e+(3/4)e^2, with margin 1/540. Replacing the fourth or
eighth mean by the reflected second mean makes designated class budgets fail.

## 6. Principal, small, horizontal and large contributions

The principal denominator stays at xi=1+e throughout. Move w from 1+e to 1/2
at z=1/6+e, taking its pole at one. In the residue move z to e, taking its pole
at 1/6. The double residue is c0 f, where c0 is CT's nonzero fixed residue,

    C=a/2+h/6=17/54, b0=1-C=37/54,
    f(Z)=(1/(2pi i)) integral_(2)
        Z^(s-b0) exp((s-5/6)^2) H(s)/zeta_F^S(s) ds.       (16)

CT's UNCHANGED H is holomorphic and nowhere zero for Re s>2/3. Initial rightward
line moves show that f is flat at zero. No previously proposed zero-free
conclusion is used to move the principal denominator. The two remainders are

    w-remainder: 5/54+(14/9)e,
    z-remainder: 2/9+(14/9)e.                            (17)

Their contours and residues satisfy (10). Principal poles are not excused by
a nonprincipal no-pole argument.

For U<=Z^(1/100), use x=1+e,y=1/2 and a SEPARATE z_s=1/3 line, with individual
convexity and the full count. Its exponent is

    h/3+(1/100)(5/4-1/3)+e = 2099/10800+e < 2/9+3e.      (18)

This change matters: the former z_s=2/5 would already cost 2/9 BEFORE the
positive row-count power, and fails. Both lines exceed 1/6, so the small-row
nonprincipal deformation crosses no zeta pole. Bounded rows use Euler
convergence for the denominator on x=1+e.

For the intermediate horizontal edges at height U^rho, (13) applies. Original
xi tails at x=1+e use Euler convergence. Use individual convexity if necessary
on edges; all strips are fixed. Convolution in the z height in (9) handles
Im z approximately -Im xi, while the complementary region has Gaussian decay.
After the w integration and absorption of all fixed polynomial height factors,
there is an arbitrary U^(-rho Adec) factor. Before this decay a coarse bound
is C Z^2 U^2. Since Z^(1/100)<U<Z^(14/25), choosing Adec>600/rho makes the total
O(Z^(-1)), including dyadic logarithms. These choices adjust valid decay
estimates, not the defining smoothing functions. The bound U<Z^(55/100) from
#965 is NOT used at our larger h=5/9.

For U>Z^(h+e), retain the INITIAL x=y=4 and move z right to L=10/e+2.
No pole is crossed. Absolute convergence gives the row power 1-L+eta; do not
apply the false convexity cost (1-4)/2 here. Geometric summation from the lower
endpoint gives the exact exponent, before arbitrary losses,

    a/2+3+h L+3a+(h+e)(1-L) = -44/9-e.                  (19)

The positive gap e is essential, and L is fixed once e is fixed. There is no
uniform endpoint estimate with e=0 or a hidden M>1 hypothesis in this tail.

Choose the finitely many remaining arbitrary losses in (5), numerator means,
correction, reciprocals, norm-to-Z conversions and dyadic sums with combined
Z cost below e. The density sets were fixed earlier. Equations (14)--(19) give

    I(X,Y,Z)=c0 f(Z)+O_e(Z^(2/9+4e)).                     (20)

Together with (7), this proves the proposed growth bound for the actual detector

    f(Z) <<_e Z^(2/9+4e).                               (21)

## 7. Mellin continuation, quantifiers and descent

The integral of f(Z) Z^(b0-s) dZ/Z over (0,infinity) is holomorphic for
Re s>b0+2/9+4e=49/54+4e, by (21) and flatness. On an initial line Re s>1 it is
exp((s-5/6)^2)H(s)/zeta_F^S(s), by Mellin/Fourier inversion. Meromorphic
continuation and the nonvanishing of H exclude denominator zeros in that
region. At one the reciprocal has a removable zero, not a singularity.

For EACH point Re s>49/54 select one fixed e>0 with e<=10^(-6) and
4e<Re s-49/54. All its constants may depend on e. There is no uniform e->0
limit or statement on the boundary line. This proves the proposed conclusion
for F. For any K, F=K(mu_12) is abelian over K. Its Dedekind factorization is
zeta_K times entire nonprincipal finite-order Hecke factors, so a zero of
zeta_K away from one would persist. For a finite-order Hecke character use its
cyclic class field and the same factorization. At one the quotient of the
positive nonzero residues excludes a zero of any nonprincipal factor. Finite
omitted Euler factors have zeros only on Re s=0. No general Artin-holomorphy
assertion or conductor-uniform descent is introduced.

## 8. Scale of the contribution and review priority

This improves the proposed #965 boundary by 7/2700, and the concurrent #966
109/120 proposal by 1/1080. The mathematical change is the off-central
moment choice and reflected eighth mean, not a new version of the already
published short-support argument or central fourth moment. Both functional-
equation sums and small-conductor regimes are essential review points.

Review MOMENTS Sections 2--4 first, then the inherited reflected reconstruction
in Section 2 here, the exact family adapter and all fifteen classes. MODEL.md
shows why these estimates now meet a precise positive-bound model ceiling;
it is not an arithmetic impossibility theorem. No missing native critical
covariance or full RH claim is promoted by the finite checker.

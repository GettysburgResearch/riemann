# Proposed 10/11 all-field zero-free composition

Status: PROPOSED deduction from explicitly declared CT/DF/BGL analytic
interfaces and #965's source-level reflected reconstruction. No independent
mathematical review or formal verification. The prior 91/100 or 11/12
CONCLUSIONS are not assumptions. No RH/GRH or unproved native moment is used.
Fresh primary CT/DF body access failed in this pass; the exact pinned source
contracts, and not a claimed fresh primary reconstruction, are the foundation.

## 1. Statement

Subject to the analytic interfaces detailed below, the proposed conclusion is

 zeta_K(s) != 0 for every number field K, Re(s)>10/11, s!=1,       (1)

with the corresponding finite-order Hecke conclusion. Nonprincipal Hecke
functions are nonvanishing at one; principal functions have a pole there.
There is no boundary-line assertion, conductor/discriminant-uniform constant,
infinite-order angular Hecke theorem, special-setting 7/8 improvement, or RH
claim. The all-field gain over #965 is 91/100-10/11=1/1100.

Fix F containing mu_12 and all the CT data as in #965, including S, generators,
finite S-unit classes, smoothing functions, compact balanced representatives,
local vectors and measures. They remain fixed through all scale limits.

## 2. Load-bearing source contracts and the new ingredient

From #965 PROOF Sections 1--2, at exact commit
 d58e3282a9379b6ae165681bc2e21e4f9fd18c26,
use the original physical pairing I(X,Y,Z) and the two estimates

 sum_m |A_t(m;X,Y)|^2 << 1/X+1/Y,
 sum_{m on physical support}|B_m(Z)|^2
       <<_eta Z^eta [XY+(XY)^2/Z].                            (2)

The second is that packet's proposed reconstruction from CT (8.15)--(8.16),
its full auxiliary sums, localized profile separation and quadratic sieve.
It is valid on each fixed positive-power scale curve, including XY<Z, IF
that reconstruction and the cited CT interfaces are correct. We do not simply
insert M<1 into the older Z^(2M-1) corollary. Its diagonal XY term is retained.
The proof's uniform estimate at subunit effective lengths and the complete
powerful/cube/local sums remain review obligations inherited from #965.

Cauchy therefore gives the complete pairing estimate

 |I| <<_eta Z^eta [(XY+(XY)^2/Z)(1/X+1/Y)]^(1/2).             (3)

Use CT's exact Poisson summand, on initial absolute-convergence lines,

 X^(1/2-z) Z^(xi+z-1) Y^(w-1) q_u^(-z)
  zeta_F^S(6z) L_F^S(w,chi_u) H_u(xi,w,z)
                         /L_F^S(xi,bar chi_u).               (4)

u is the full sixth-free exterior index with the same finite S-unit classes.
Its unique principal row is u=1. The correction is holomorphic and bounded
by q_u^eta on fixed-margin subdomains of

 x,y,z>0; 6z+y>1; x+6z>1; x+y>1; x+y+6z>2;
 6x+6z>5; x>1/2; 3x>2; 3x+y>5/2,                            (5)

where x=Re xi and y=Re w. The fixed Mellin profiles have joint decay

 exp[-(Im xi+Im z)^2](1+|Im z|)^(-A)(1+|Im w|)^(-A)           (6)

for each fixed A. It is NOT Gaussian decay in xi alone.

At the principal residues w=1,z=1/6 the coefficient c0 is fixed and nonzero;
the UNCHANGED numerator H(s) is holomorphic and nowhere zero for Re s>2/3,
with the required vertical bounds. These are CT's original interfaces, not
consequences of an unproved new numerator normalization.

The fixed S-unit family adapter and the DF density detector are exactly those
of #965 Sections 3.2--3.3. The new input is NUMERATOR_MOMENTS.md (1) at r=2:

 sum_{q_u<=U}|L_F^S(1/2+it,chi_u)|^4
                 << U^(7/6+eta)(2+|t|)^C.                  (7)

For a class of size U^nu this gives the Holder exponent 3nu/4+7/24,
not (nu+1)/2. Keep the older second mean for the full good class; keep
individual convexity where it is better than either mean. No inverse
L-function moment or independence from zero-selected classes is assumed.

## 3. Scales and Mellin normalization

Choose the fixed scales

 a=5/11, h=1-a=6/11, X=Y=Z^a, XY=Z^(10/11).                (8)

Equation (3) gives |I|<<Z^(5/22+eta). Both scales grow; neither an M=1
limit nor an M>1 extrapolation is used. The diagonal term in (2) dominates.
Set

 C=a/2+(1-a)/6=7/22, b=1-C=15/22,
 f(Z)=(1/(2pi i)) integral_(2)
           Z^(s-b) exp((s-5/6)^2) H(s)/zeta_F^S(s) ds.      (9)

The detector in (9) is fixed; the small loss e below changes contours and
constants, not this detector or its source. Its numerator is the actual CT H.
Moving an initial line to the right proves flatness at zero.

## 4. Complete density stratification

Fix 0<e<=10^(-6). PARAMETERS.json specifies 26 rational thresholds and the
25 middle-class methods. The first is 15/22; the last is 23/25.
For each threshold sigma, use the DF detector with parameters aa,bb,zz and
row count g(sigma) computed in verify.py. Its ten monomials are:

 1/2+(1/2-sigma)bb+t/2,
 t in {aa,1,aa/3+5/6,5aa/6+1/3};
 (2-2sigma)bb; 1+(1-2sigma)aa;
 1/3+(11/6-2sigma)v; 5/6+(4/3-2sigma)v, v=aa or bb.           (10)

All are <=g(sigma); the corresponding height powers are checked separately.
This is the complete detector of #965 (27), not a density theorem inferred
from sampled values. `python verify.py --details` records every rational parameter
triple; CHECKS.json preserves the summary.

Choose a fixed rho>0 sufficiently small in terms of e, the field, and the
fixed height exponents, then spend a sufficiently small density loss.
The nested sets E_j(U), of rows a~U having a zero in Re s>=sigma_j and
|Im s|<=4U^rho, have cardinality O_e(U^(g(sigma_j)+e)). These sets are fixed
BEFORE choosing the later arbitrarily small reciprocal losses. Conjugate
characters reflect the symmetric height rectangle. Missing exterior Euler
factors have no zeros at positive real part.

For rows outside E_j, log L is analytic on disks about 2+it with radii

 R=2-sigma_j-e/4 > r_o=2-sigma_j-e/2
   > r_t=2-sigma_j-e > r_i=1-e/4 >0.                         (11)

On r_o Borel--Caratheodory and polynomial growth give O_e(log U); on r_i the
Euler logarithm is O_e(1). Three circles gives a strictly sublinear power of
log U at r_t. Hence for EVERY later eta>0,

 |1/L_F^S(x+it,bar chi_u)| <<_(e,eta) U^eta,
 sigma_j+e<=x<=1+e, |t|<=2U^rho.                            (12)

The disk sizes and sets do not change with eta. Finite Euler omissions cost
U^eta by separating finitely many small primes. A strict zero-count convention
is handled by a tiny left displacement before fixing the density loss budget.

For Z^(1/100)<U<=Z^(h+e), set z0=2/5 and

 E(x,y,z)=a/2+x-1+h z+a(y-1).                                (13)

The central dyad is bounded by Z^E U^R with one of the following row powers:

 M2, y=1/2: R=(nu+1)/2-z0;
 M4, y=1/2: R=3nu/4+7/24-z0;
 CV:         R=nu+(1-y)/2-z0.                              (14)

Take reciprocals/corrections uniformly FIRST, apply the chosen numerator
inequality, and then integrate its polynomial heights against (6).

The 27 disjoint classes are:
- Outside E_0: x=15/22+e, y=1/2, nu=1, method M2.
- E_j minus E_(j+1), j=0,...,24: x=sigma_(j+1)+e and
  nu=g(sigma_j)+e. For j=0,...,14 use M4 at y=1/2.
  For j=15,...,24 use CV at y=1-sigma_(j+1)+e.
- E_25: x=1+e, y=e, nu=g(23/25)+e, method CV.

A middle class is counted at its LOWER threshold and shifted past its UPPER
threshold. Every nested zero pattern has exactly one destination. No class
is omitted. All R are positive, so the largest U in each dyad range is
U=Z^(h+e). Every contour vertex satisfies (5); convexity of that real domain
keeps the connecting segments inside it. The xi shift is truncated using
(12); the subsequent w shift crosses no numerator pole for these
nonprincipal characters. z0>1/6 crosses no zeta(6z) pole.

The exact good-class exponent is

             5/22 + (8/5)e.                                (15)

All middle constants are STRICTLY below 5/22. The minimum constant margin is

             1189662567661/2354348514100000 >0.               (16)

Their complete quadratic e polynomials, including M4's coefficient 3e^2/4,
are emitted by `python verify.py --details`. Rational Bernstein coefficients
prove, on the WHOLE
interval 0<e<=10^(-6), that every central class is <=5/22+3e.
This is a finite inequality certificate, not an analytic L-value check.

## 5. Principal terms, small norms, and both tails

### Principal row

Keep xi at 1+e: no earlier global zero-free theorem is used. Move w from
1+e to 1/2, taking its pole at 1. In that residue move z from 1/6+e to e,
taking its pole at 1/6. The double residue is exactly c0 f. The other terms
have growth

 E(1+e,1/2,1/6+e)=1/11+(17/11)e,
 E(1+e,1,e)=5/22+(17/11)e.                                 (17)

All paths lie in (5); both remainders remain in the comparison.

### Small norms

For U<=Z^(1/100), use x=1+e,y=1/2,z=z0, the full row count, and individual
convexity. The exponent is

  h z0+(1/100)(5/4-z0)+e
               =5/22-13/22000+e.                          (18)

It is strictly below the target after the loss budget. No exceptional-set
claim at bounded U is needed.

### Horizontal edges and original xi tails

The fixed-strip reciprocal, correction and numerator height bounds are
polynomial. Convolution with the JOINT weight (6) gives arbitrary U^(-rho A)
decay: near Im z=-Im xi it is the Schwartz z decay which is used; elsewhere
the Gaussian controls the xi tail. A coarse Z^2 U^2 envelope suffices, and
all intermediate U lie between Z^(1/100) and Z^(55/100). A fixed sufficiently
large decay order, for instance larger than 500/rho after fixed polynomial
losses, makes the total O(Z^-1). The original tails use xi=1+e and Euler
convergence, not an untruncated assertion of zero-freeness of an exceptional L.

### Large norms

For U>Z^(h+e), retain the initial x=y=4 and shift z right to L=10/e+2.
Absolute convergence gives the row exponent 1-L+eta, not the convexity formula
outside its range. Geometric summation at the lower endpoint gives

 a/2+3+3a+h L+(h+e)(1-L) = -107/22-e.                       (19)

The cutoff gap is the fixed positive e. The large contour and its constants
are fixed only after e is fixed. No zero gap or bound uniform in e is used.

Spend the remaining arbitrary losses in the reflection, numerator moments,
correction, reciprocal, convexity, norm conversion and dyadic sums below e
in total. The fixed density sets and rho do not change. Equations (15)--(19)
and (3) therefore give for the ACTUAL detector

                  f(Z)<<_e Z^(5/22+4e).                    (20)

## 6. Holomorphy and descent

Flatness at zero and (20) make

 integral_0^infinity f(Z) Z^(b-s) dZ/Z

holomorphic on Re s>b+5/22+4e=10/11+4e. In an initial right half-plane,
Mellin inversion identifies it with exp((s-5/6)^2)H(s)/zeta_F^S(s).
The numerator has no zero there. A zero of the denominator would thus be an
uncancelled pole, a contradiction. The reciprocal has a removable zero at
the principal pole s=1; no nonzero finite value is asserted there.

For each point Re s>10/11 choose ONE fixed e>0 within the stated interval
with 4e<Re s-10/11. This proves the strict half-plane for F under the input
contracts. No e-uniform bound or boundary-line theorem is claimed.

For an arbitrary K use F=K(mu_12), abelian over K, and the classical
factorization of zeta_F as zeta_K times entire nonprincipal Hecke factors.
A zero away from one persists. For a finite-order Hecke character use its
cyclic class field and the same factorization; at one the nonzero residue
quotient excludes a zero of a nonprincipal factor. Missing Euler factors
have zeros only at real part zero. No general Artin holomorphy conjecture or
uniformity under growing field degree is asserted.

## 7. Difference from prior work and priority review

#965 supplied the essential subcritical source reconstruction. We neither
claim it as new nor infer it from a simplified M>1 bound. The new mathematical
step is the complete fourth-numerator moment (7), which improves sparse-row
classes; those classes permit X=Y=Z^(5/11) instead of Z^(23/50).

The proposed excluded width is 1/11, compared with #965's 9/100 and #959's
1/12. This is a 1/1100 boundary improvement over #965, not a large approach
to 1/2. It remains weaker numerically than the reported 7/8 special setting.

Review NUMERATOR_MOMENTS Sections 1--2 first, then #965's subcritical
reflection, then (10)--(19) and their quantifiers. The independent-variable
Fourier route considered during this pass was not completed or promoted.
No native fourth-Mobius moment, 17/24 conclusion, critical signed covariance,
or height-dependent RH band has been proved by the numerator moment theorem.

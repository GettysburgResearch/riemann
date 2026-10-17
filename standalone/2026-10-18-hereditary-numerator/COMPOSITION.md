# Hereditary numerator estimates and the proposed 633/700 boundary

Status: PROPOSED source-qualified analytic composition, with a complete argument
relative to the explicitly adopted contracts below. Independent mathematical
review is required. No RH/GRH, OPEN-L, native inverse-Mobius higher moment, or
unproved signed-covariance estimate is assumed. This is not an accepted theorem,
a Lean proof, or an independent reconstruction of all imported theta theory.

## 1. Exact conclusion and dependency boundary

The proposed conclusion is

    zeta_K(s) != 0 for every number field K,
                         Re(s)>633/700, s!=1.               (1)

The corresponding finite-order Hecke L-functions are nonzero in the same strict
half-plane, including at one when nonprincipal. Principal functions have a pole
there. No boundary-line assertion or constant uniform over fields, discriminants,
conductors, or distance to the boundary is made. Infinite-order angular Hecke
characters are not covered. This is not a proof of RH.

Fix F containing mu_12, CT's allowed generators, local vectors, finite S, measures,
quotient Gamma=(O_(F,S)^*)^6 and smoothing profiles. All these data are fixed.
Physical indices m and Poisson indices u are DIFFERENT families. Keep every
original row, common-prime restriction, zero extension and full exterior norm.

The following inherited analytic contracts are essential. Their precise pins
and source-reading levels are in SOURCES.md.

(T) #965's proposed reconstruction from CT's unrestricted reflected expression:

    sum_(physical support Nm << XY) |B_m(Z)|^2
             <<_eta Z^eta [XY+(XY)^2/Z].                    (2)

It includes the full auxiliary cube, powerful and local sums, and is valid when
X,Y are fixed positive powers of Z, including XY<Z. We adopt that reconstructed
argument, not an extrapolation of CT's simplified M>1 corollary. The diagonal
XY term is retained. The unchanged additive calculation is

    sum_m |A_t(m;X,Y)|^2 << 1/X+1/Y,                        (3)

uniformly over its compact balanced t quotient. Consequently the original full
pairing satisfies

    |I(X,Y,Z)| <<_eta Z^eta
                    [(XY+(XY)^2/Z)(1/X+1/Y)]^(1/2).        (4)

(P) CT's actual Poisson summand on absolute-convergence lines is a fixed weight
multiplied by

 X^(1/2-z) Z^(xi+z-1) Y^(w-1) (Nu)^(-z)
       zeta_F^S(6z) L_F^S(w,chi_u) H_u(xi,w,z)
                                     /L_F^S(xi,bar chi_u). (5)

Use initial real parts x=y=5,z=2; these are strictly inside the stated initial
region, rather than interpreting a strict lower bound as an equality. The full
sixth-free u-family, fixed finite S-unit twists and character identification are
those of #965 and #968. The unique inducing-principal row is treated separately.
This is the source's principal-row convention, not an inference from a generic
large sieve. Its nonzero double residue coefficient is c0.

(H) The nineteen-file local-support packet, now preserved in #970, supplies the
proposed exact-local-sum enlargement of the correction domain to the convex region

 x>1/2; y,z>0; 6z+y>1; x+6z>1; x+y>1;
                    x+y+6z>2; 6x+6z>5.                    (6)

On every fixed-margin subdomain, H_u is holomorphic and <<_eta (Nu)^eta, uniformly
in imaginary parts. This uses the exact prime-power orthogonality and nonunit
masks in that packet's LOCAL_DOMAIN.md. We adopt it with its review qualification;
we do not repeat its removal of the old 3x>2 and 3x+y>5/2 restrictions as new work.
The proof below needs this enlargement. Using CT's old smaller domain would not
justify the first contour. Concurrent #971 has related local work, but that
separate packet is not silently made a premise.

The fixed Mellin profiles have arbitrary joint height decay

 exp[-(Im xi+Im z)^2] (1+|Im z|)^(-A) (1+|Im w|)^(-A),      (7)

up to a fixed constant for each A. This is NOT Gaussian decay in xi alone.
CT's unchanged principal H(s) is holomorphic and nowhere zero for Re s>2/3,
with the vertical bounds required for Mellin inversion. Its source numbering
is Lemma 11.1 in Section 11.2.

(S) The numerator, density and fixed-twist contracts in HEREDITARY_MOMENTS.md and
DENSITY.md use DF's sieve on both sixth-free indices, complete Hecke AFE/functional
equations and the classical shifted zero detector. These two files contain this
pass's new deductions. They do not assume (1), (2), or a reciprocal-L moment.

Fresh CT body retrieval failed in this execution. These are source-qualified
imports from the pinned written arguments, not a claim that CT was freshly
reproved or its full formal library compiled. A defect in T, P, H or S invalidates
(1) even if every finite rational check passes.

## 2. Physical scales and the actual detector

Choose the FIXED values

 a=149/350,  X=Y=Z^a,  h=1-a=201/350,  M=2a=149/175<1.

Both physical scales grow. Equations (2)--(4) bound the COMPLETE pairing by

                  |I(X,Y,Z)| << Z^(149/700+eta).           (8)

Set

 C=a/2+h/6=1/6+a/3,
 b=1-C=121/175,
 f(Z)=(1/(2pi i)) integral_(2) Z^(s-b)
                     exp((s-5/6)^2) H(s)/zeta_F^S(s) ds.  (9)

This is the actual principal detector extracted from (5). Its new shift b must
not be replaced by any predecessor's shift. Moving its initial line right makes
f flat at zero. The principal residues w=1,z=1/6 give exactly c0 f with c0!=0.
No coefficient completion or altered numerator is introduced here.

For each remainder calculation fix ONCE

                       0<e<=10^(-9).                     (10)

The defining physical scales do not depend on e. The large-frequency cutoff and
contour buffers do, and all their constants may depend on this fixed e.

## 3. One finite exhaustive stratification

strata.tsv contains 112 strictly increasing RATIONAL thresholds sigma_j,
j=0,...,111. They start at sigma_0=447/700=3a/2 and end at sigma_111=19/20.
Each row gives a specific density method, detector line and two detector-length
powers. For a row marked H, g_j is the maximum of ALL FIFTEEN expressions in
DENSITY (6); for DF it is the maximum of ALL TEN expressions in DENSITY (9).
No fitted formula or optimizer is required to evaluate these choices.

Choose a sufficiently small fixed rho>0 for this finite list, field and e, and
then density losses sufficiently small. Let E_j(U) be the rows u with U<=Nu<2U
whose inducing denominator L(s,bar chi_u) has a zero with

                  Re s>=sigma_j, |Im s|<=4U^rho.

The sets are nested and #E_j(U)<<U^(g_j+e). Conjugation reflects the symmetric
height rectangle. Finite omitted Euler factors have zeros only on Re s=0.
If a density convention uses strict inequalities, shift its threshold an
arbitrarily small amount left within the initial loss budget BEFORE fixing the
sets. Continuity of the displayed finite exponents pays this change.

For a row outside E_j and |t|<=2U^rho, use an analytic logarithm of its L-function
on concentric disks about 2+it, with radii

 R=2-sigma_j-e/4, r_o=2-sigma_j-e/2,
 r_t=2-sigma_j-e, r_i=1-e/4.

For sufficiently large U these are strictly ordered R>r_o>r_t>r_i>0 and lie in
the zero-free rectangle. Polynomial strip bounds and Borel--Caratheodory give
O_e(log U) for log L on r_o, while Euler convergence bounds it by O_e(1) on r_i.
Three circles therefore gives O_e((log U)^theta), theta<1, on r_t. Hence for
EVERY later eta>0,

 |1/L_F^S(x+it,bar chi_u)| <<_(e,eta) U^eta,
           sigma_j+e<=x<=1+e, |t|<=2U^rho.                 (11)

Inducing omissions are bounded by separating finitely many small primes and
absorbing the remaining product in U^eta. On x>1 use Euler convergence directly.
The exceptional sets and rho are not changed when later analytic losses shrink.
For all finitely many numerator strips/orders the height polynomial can be fixed
before these later losses; only its implied constant changes.

For the intermediate range Z^(1/100)<U<=Z^(h+e), use z0=2/5 and the following
113 DISJOINT classes:

- Outside E_0: x=sigma_0+e, y=1/2. Use the complete second numerator mean with
  full count U, giving first-mean exponent m=1. No sparsity is assigned.
- E_j minus E_(j+1), j=0,...,110: x=sigma_(j+1)+e; use the FIXED y and fixed
  moment order r on row j of strata.tsv. The count is g_j+e, NOT g_(j+1).
- E_111: x=1+e, y=e; use individual convexity and Euler convergence for the
  reciprocal. Here g_111=11/47. This terminal class is not omitted.

The middle rows use fourth, sixth and eighth selected numerator moments (r=2,3,4).
They apply to the same zero-selected subset. Take the uniform reciprocal and
correction bounds FIRST. Holder and the hereditary estimates then bound its
numerator sum by U^(m_r(g_j,y)+e+eta), since m_r is 1-Lipschitz in the count exponent.

At fixed u-dyad the physical exponent is

 E(x,y,z)=a/2+x-1+h z+a(y-1),
                 contribution << Z^E U^(m-z+eta).         (12)

Every chosen row exponent m-z0 is positive, so the maximum occurs at the top
U=Z^(h+e). The constant middle exponent is

 c_j=sigma_(j+1)-1-a/2+a y+h m_r(g_j,y).                   (13)

Every c_j is STRICTLY smaller than a/2. For all 0<e<=10^(-9), its buffered bound
is the explicit polynomial

 c_j+[1+m_r(g_j,y)-z0+h]e+e^2 <= a/2+3e.                 (14)

The good class is exactly a/2+(8/5)e. The last class is bounded by

 c_last+[1+a+(g_111+1/2-z0)+h/2]e+e^2/2,
 c_last=-a/2+h(g_111+1/2)=3433/16450 < a/2.               (15)

verify.py derives every density exponent and moment exponent from the formulas,
checks all 113 classes and certifies (14)--(15) on the ENTIRE e interval using
rational Bernstein coefficients. The certificate is not a numerical sample.

Each central contour starts at (1+e,1+e,z0). Truncate xi, move it to x using (11),
and then move w to its chosen y. All vertices satisfy (6), so convexity retains
every connecting segment. In some rows x+y=1 at e=0; its actual value has positive
buffer e. These characters are nonprincipal, z0>1/6, and the denominator is
zero-free on the actually traversed truncated rectangle. No global zero-free
assertion is made for that denominator. Initial movements from (5,5,2) to the
starting contour stay inside (6) and cross no nonprincipal pole.

## 4. All other contributions

### Principal row

Keep xi at 1+e, to the RIGHT of one. Move w from 1+e to 1/2, taking its residue
at one. In the w residue move z from 1/6+e to e, taking the residue at 1/6.
The double residue is c0 f. The two other exponent bounds are

 E(1+e,1/2,1/6+e)=h/6+(1+h)e,
 E(1+e,1,e)=a/2+(1+h)e.                                  (16)

All principal vertices and paths satisfy (6); only w=1,z=1/6 are crossed.
The old principal z remainder still ties theta at its leading exponent, but
both have moved down with the new physical scales. No claimed improved global
zero-free theorem is used to move the principal denominator circularly.

### Small nonprincipal norms

For U<=Z^(1/100), keep x=1+e,y=1/2, but choose z=1/3 rather than z0=2/5. This
separate legal contour is important: keeping z0 would lose the small-range
budget at these scales. Use individual convexity and the full row count.
The exponent is

             h/3+11/1200+e < a/2+e.                      (17)

Both this contour and the movement to it satisfy (6); z=1/3>1/6, so no zeta(6z)
pole is crossed. Bounded u and Z are absorbed in fixed-data constants.

### Horizontal contours and original-line tails

For intermediate dyads, shifted edges at height U^rho use (11); original xi
tails on x=1+e use Euler convergence. The correction and numerator bounds have
only fixed polynomial height costs. Integrate BOTH z and w heights in (7).
When Im z is approximately -Im xi, arbitrary z-Schwartz decay applies; in the
complement the Gaussian applies. This supplies an arbitrary U^(-rho A) factor
on the edges/tails after absorbing the fixed height polynomials.

A deliberately coarse majorant on the fixed strips before this decay is
Z^2 U^2. Here U<Z^(3/5), and U>Z^(1/100). A fixed A>600/rho therefore makes the
complete horizontal/original-tail sum O(Z^-1), including all dyadic logarithms.
Taking this decay order changes a valid estimate, not the defining profiles.
No supremum of row-dependent coefficients is passed into the sieve.

### Infinite large-frequency range

For U>Z^(h+e), retain the initial integral at x=y=5 and shift z RIGHT to

                         L=10/e+2.

Absolute convergence gives row factor U^(1-L+eta); applying a negative convexity
power (1-y)/2 at y=5 would be false. No pole is crossed. The dyads sum geometrically,
and their lower-endpoint Z exponent is

 a/2+4+h L+4a+(h+e)(1-L)
                  =-5+7a/2-e=-2457/700-e.                (18)

The positive tail gap is e, not zero. L is fixed after e is fixed. All initial
lines remain strictly legal; no assertion uniform as L tends to infinity occurs.

Finally choose all remaining arbitrary power losses in T, S, correction,
reciprocal, norm-to-Z conversions and dyadic summation with total Z cost less
than e. There are finitely many inequalities; their height exponents and density
sets were fixed earlier. Equations (12)--(18) prove the proposed comparison

 I(X,Y,Z)=c0 f(Z)+O_e(Z^(149/700+4e)).                     (19)

Combining with (8) bounds the ACTUAL detector, not an assumed substitute:

                         f(Z)<<_e Z^(149/700+4e).          (20)

## 5. Mellin continuation and the all-field statement

Flatness at zero and (20) imply that

                 integral_0^infinity f(Z)Z^(b-s) dZ/Z

is holomorphic for Re s>b+149/700+4e=633/700+4e. Mellin/Fourier inversion on an
original line Re s>1 identifies it with exp((s-5/6)^2)H(s)/zeta_F^S(s).
Meromorphic continuation and H's nonvanishing for Re s>2/3 rule out denominator
zeros there. At one the reciprocal expression instead has a removable zero.

For each point Re s>633/700 choose one fixed positive e satisfying (10) and
4e<Re s-633/700. This proves the proposed STRICT half-plane for F. Constants
may deteriorate with e; no uniform limit, boundary-line assertion or zero census
is used.

For any K, F=K(mu_12) is abelian over K. Classical abelian factorization writes
zeta_F as zeta_K times entire nonprincipal Hecke factors; hence a zero of zeta_K
away from one would persist. For a finite-order Hecke character use its cyclic
class field and the analogous factorization. At one the quotient of the two
positive nonzero zeta residues rules out a zero of a nonprincipal factor.
Finite missing Euler factors have zeros only on Re s=0. This is the inherited
class-field descent, not a general Artin-holomorphy claim.

The change from the recovered 68/75 proposal is exactly 1/420. The excluded
width is now 67/700. This remains numerically weaker than the separately reported
7/8 special-setting result, and does not approach the critical line by iteration
of the displayed bounds. The structural contribution is the hereditary family
estimate and its self-restricted density input, not a claim that 112 thresholds
alone constitute new cancellation. External review must start with those inputs
and the adopted enlarged local/reflected contracts, not with the predicate count.

# A zero-free-selected reflected numerator and a proposed 271/300 boundary

**Status: PROPOSED complete source-qualified composition. Independent mathematical
review is required.** The inputs are stated unconditionally in their sources; no
RH/GRH, unknown native moment, OPEN-L or signed-covariance hypothesis is assumed.
This does not independently certify the imported sources or the proposed
subcritical reflection and local-domain adapters. Fresh CT primary retrieval
failed in this pass. The finite checker certifies arithmetic, not analysis.

The first checkpoint REFLECTION_LEMMA.md is preserved unchanged. Its historical
no-global-claim statement describes that checkpoint. This separate continuation
supplies the full comparison and proposes the following conclusions.

## 1. Statements and dependencies

**Proposed Theorem A.** For every number field K,

    zeta_K(s) != 0 if Re(s)>271/300 and s!=1.                  (1)

The same strict region holds for finite-order Hecke L-functions, with
nonvanishing at s=1 for nonprincipal characters. Principal functions have a pole
there, not a finite nonzero value. Constants may depend on the field, finite
local data, character and distance to the boundary. No infinite-order angular
Hecke result or boundary-line assertion is made.

**Proposed Theorem B, with fewer moment inputs.** The same conclusions hold in
Re(s)>19/21 using only de Faveri's original zero-density result and BGL's second
numerator moment. This version does NOT need the fourth numerator moment or
#966's improved selected-character density. It uses the same new reflection
lemma and the same enlarged local correction domain.

Fix F=K(mu_12). Initially work over F, with CT's allowed generators, finite S,
local vector, quotient Gamma=(O_(F,S)^*)^6, Haar measures and fixed smoothing.
Every implied constant retains these fixed data. The precise contracts are:

(R) The ORIGINAL physical average I(X,Y,Z), with all its rows and phases, has

    |I| <<_eta Z^eta [(XY+(XY)^2/Z)(1/X+1/Y)]^(1/2).          (2)

This is #965's proposed reconstruction from the unrestricted CT reflection,
NOT an extension by substitution of its older M>1 corollary. In physical
mR=h d, h powerful and d squarefree, its complete dyadic bound is
P^(1/2)(D+D^2 P/Z), up to arbitrary small powers, for Nh~P, Nd~D.
The reconstruction keeps the whole cube variable, all auxiliary local ideals,
quadratic-sieve columns and effective lengths below one. Summing PD<<XY gives
XY+(XY)^2/Z; the diagonal XY cannot be deleted. The other square mean is the
unchanged additive estimate 1/X+1/Y. The written source argument, not a finite
exponent calculation, is a load-bearing proposed dependency.

(P) CT's exact Poisson evaluation, initially on sufficiently far right lines,
is a sum of its actual factors

    X^(1/2-z) Z^(xi+z-1) Y^(w-1) q_u^(-z) zeta_F^S(6z)
       L_F^S(w,chi_u) H_u(xi,w,z) / L_F^S(xi,bar chi_u).      (3)

Full sixth-power-free exterior ideal norms q_u order the frequencies, together
with finitely many fixed S-unit labels. In particular the source is not ordered
by conductor or radical norm. The only principal row is u=1. The same fixed
generator choices identify chi_u with the de Faveri family up to those fixed
S-supported finite-order twists. Both sides retain their common-prime zeros.
At each exterior prime with index valuation 1,...,5, the local character is
nontrivial; the inducing conductor outside S is the radical. Thus Q_u<=C q_u,
and primitive versus exterior factors differ only at the fixed S places.

(H) The proposed exact local calculation in #971, RAMIFIED_FACTORS Theorem R2,
gives holomorphy and |H_u|<<_eta q_u^eta, uniformly in imaginary parts, on every
fixed-margin real compact in

    x,y,z>0; 6z+y>1; x+6z>1; x+y>1;
    x+y+6z>2; 6x+6z>5; x>=1/2.                            (4)

Here x=Re xi and y=Re w. The older restrictions 3x>2 and 3x+y>5/2 are NOT
part of this improved domain. The exact ramified support and finite Fourier
calculation are essential: CT's old majorant alone would not justify (4).
A bound for H_u is not a nonvanishing theorem for its denominator.

(W) The Mellin weights in (3) obey, for arbitrary fixed A,

    C_A exp[-(Im xi+Im z)^2]
            (1+|Im z|)^(-A)(1+|Im w|)^(-A).                (5)

All fixed-strip numerator and reciprocal polynomial height factors can be
absorbed. The Gaussian does NOT involve Im xi alone.

(M2) BGL (5.1), with the fixed-twist/complete-family adapter credited to #959
and #965, gives sum_(q_u<=U)|L_F^S(1/2+it,chi_u)|^2
<< U^(1+eta)(2+|t|)^C. Thus the complete good class has first mean
U^(1+eta). The fixed twists are common column multipliers in the original
AFE/large-sieve proof; full powerful columns are not removed.

(D) DENSITY.md specifies exactly the density exponents used. Its M4 option is
#966's selected-character detector, reconstructed there with the R^(1/2) tail
retained until elimination. It is needed only for Theorem A. Conjugating the
family preserves all sieve bounds by conjugating coefficients; zero counts
are unchanged in a height-symmetric rectangle.

Finally, the principal residues w=1,z=1/6 in (3) give c0 f_a, c0!=0, where

    b_a=5/6-a/3,
    f_a(Z)=(1/(2pi i)) integral_(2)
       Z^(s-b_a) exp((s-5/6)^2) H(s)/zeta_F^S(s) ds.         (6)

H here is CT's unchanged principal numerator, holomorphic and nonzero on
Re(s)>2/3 with its source height bounds. Moving the initial line right proves
flatness of f_a at zero. No new multiplier is substituted for H.

## 2. Fix all zero-selected sets before shrinking analytic losses

For Theorem A take

    a=21/50, h=1-a=29/50, theta=a/2=21/100, z0=1/3,
    0<e<=10^(-7), X=Y=Z^a.                                 (7)

There are 851 density thresholds

    sigma_j=63/100+j/2500,  j=0,...,850,                     (8)

ending at 97/100. At thresholds in [7/10,9/10] use the credited M4 count;
elsewhere use DF. Each density has a polynomial height bound with some finite
power. Choose its norm loss sufficiently small, and then choose one rho>0 so
small that ALL 851 row counts on |Im s|<=4U^rho have exponent g_j+e. The field,
e and finite threshold list are fixed first. This single choice determines

    E_j(U)={nonprincipal q_u in [U,2U): L(s,bar chi_u)
            has a zero Re s>=sigma_j, |Im s|<=4U^rho}.       (9)

These actual sets are nested. Their bounding exponents need not be monotone.
Primitive inducing functions are used; omitted finite Euler factors have zeros
only on Re s=0. A strict zero-count convention is accommodated by a tiny
leftward displacement within the already reserved norm loss, with all
parameters fixed before constructing the sets. Constants at bounded U are
absorbed separately. Subsequent eta losses do NOT redefine E_j or rho.

On a row outside E_j, REFLECTION_LEMMA Section 2 gives BOTH L and 1/L subpower
at Re s>=sigma_j+e in the truncated rectangle. That argument uses the analytic
Euler branch of log L, Borel--Caratheodory and three circles, not an assumed
Lindelof bound. It works at each common height and does not require independence
from any other factor.

## 3. All 852 central classes

First split the initial absolutely convergent frequency sum at
U=Z^(1/100) and U=Z^(h+e). For a fixed Z the middle part contains finitely many
rows, so subsequent individual contour moves and its zero-based partition do
not interchange an uncontrolled infinite frequency sum. The infinite upper
tail is handled on its original lines in Section 5.

For Z^(1/100)<U<=Z^(h+e), use these DISJOINT classes:

* Good: outside E_0. Set x=sigma_0+e,y=1/2,z=z0. Use M2 and the uniform
  reciprocal/correction bounds, with the full count U (no fictitious sparsity).
* Middle j=0,...,849: E_j minus E_(j+1). Put tau=sigma_(j+1),
  x=tau+3e, y=1-tau-e, z=z0, nu=g_j+e. The count is at the LOWER
  threshold; the zero-free rectangle is at the UPPER threshold.
* Terminal: E_850. Keep x=1+e,y=e,z=z0, with nu=g_850+e. Use Euler
  convergence for the reciprocal and ordinary numerator convexity.

Start each finite nonprincipal row at (x,y,z)=(1+e,1+e,z0), reached from
(5,5,3) without crossing a pole. Truncate xi at +/-U^rho, shift it to x,
then truncate and shift w to y. There are no nonprincipal numerator poles.
The zeta(6z) pole stays left of z0. All connecting real segments lie in (4),
which is convex: in particular the middle final vertex has x+y=1+2e and
x>1/2. The obsolete local-domain inequalities must not be reintroduced.
All horizontal connectors and discarded pieces are bounded in Section 5.

On the central rectangle, the new estimate is

    sum_middle |L(y+it,chi_u) H_u / L(x+iv,bar chi_u)|
        << U^(nu+tau-1/2+e+eta)(2+|t|)^C.                   (10)

Indeed the FE reflects the numerator to L(tau+e-it,bar chi_u), which lies in
THE SAME known zero-free rectangle as the denominator. Both signs of log L
are bounded there. The conductor exponent tau-1/2+e is positive, so Q_u<=CU
is used in the correct direction. The ordinates t and v are independent;
both are truncated. Taking uniform absolute bounds before summing makes (10)
valid even though the class was selected from these functions' zeros.

Let

    E(x,y,z)=a/2+x-1+h z+a(y-1).                             (11)

The good, middle and terminal U powers, before eta, are respectively

    1-z0;
    g_j+tau-1/2-z0+2e;
    g_850+1/2-z0+e/2.                                      (12)

All are positive, so U=Z^(h+e) bounds every central dyad. The good Z exponent
is exactly theta+5e/3. Each middle exponent is

    c_j+(25/6-3a+g_j+tau)e+2e^2,
    c_j=h(2tau+g_j)+a-3/2.                                 (13)

The exact finite density/contour certificate gives

    min_j(theta-c_j)=96266833/858608062500>0,
    max_j(25/6-3a+g_j+tau)=1013479/228750<5.                 (14)

These are exact rational values, not fitted exponents. DENSITY.md additionally
proves a continuous positive-quadratic certificate on the central threshold
interval, independently of the finite mesh calculation. The terminal class
also has a strict constant margin. Every central exponent is <=theta+6e on
the ENTIRE interval 0<e<=10^(-7); verify.py certifies this with rational
Bernstein coefficients. No limit with a fixed number of omitted bins is used.

## 4. Principal and small-frequency pieces

For the principal row keep xi on 1+e throughout; no zero-free conclusion is
fed circularly back into this argument. Move w from 1+e to 1/2, taking its
residue at one. In that residue move z from 1/6+e to e, taking its residue at
1/6. The double residue is exactly c0 f_a. The remaining exponents are

    w remainder: 29/300+(79/50)e,
    z remainder: 21/100+(79/50)e.                           (15)

All principal vertices and paths satisfy (4). Only w=1 and z=1/6 are crossed.
The Gaussian and fixed smoothing control the full vertical integrals.

For U<=Z^(1/100), keep x=1+e, use y=1/2,z0=1/3 and individual convexity
with the full count. Its exponent is

    h/3+(1/100)(5/4-1/3)+e=81/400+e,                       (16)

below theta by 3/400 at e=0. No density or truncated zero-free assertion is
needed on this range.

## 5. Both height tails and the infinite frequency tail

Equation (10) is NOT used for arbitrary w heights. Here is the complete split.
Original xi tails stay on x=1+e, where the reciprocal is Euler-bounded. On
the shifted xi central segment and its horizontal connectors, the reciprocal
bound is valid up to |Im xi|=U^rho. First perform that xi shift with w still
on 1+e. Then the original w tails on that line and the horizontal w connectors
use ordinary fixed-strip convexity, NOT (10); the denominator is unchanged.
Only the resulting central xi/w rectangle uses reflection.

H_u is height-uniform on the relevant real compacts. All ordinary numerator,
gamma and reciprocal factors contribute fixed polynomial height powers.
Equation (5) gives arbitrary inverse powers of U^rho on every large-height
piece. When Im z is close to -Im xi, use its independent Schwartz decay;
elsewhere use the Gaussian. Fubini follows after these absolute majorants.
After integration in z and the other height, overbound a dyad before this
extra decay by C Z^4 U^4. Since U>Z^(1/100) and h+e<59/100, choose a fixed
Schwartz order after rho and all polynomial degrees, with rho*A>1000.
The total horizontal and original-line tails are O(Z^(-1)), even after dyadic
logs. Profiles are not changed: only a valid seminorm/decay order is chosen.

For U>Z^(h+e), stay at the initial x=y=5 and move z to

    L=20/e+3.                                               (17)

All source convergence conditions hold strictly, and no pole is crossed.
Absolute convergence gives U^(1-L+eta), not a negative-y convexity formula.
The dyads sum geometrically. The lower endpoint Z exponent is

    a/2+4+hL+4a+(h+e)(1-L)=-1353/100-2e.                   (18)

The strictly positive gap e between h and the cutoff is indispensable.
L is fixed once e is fixed; no estimate uniform as L tends to infinity is
required. This proves convergence and negligibility of the COMPLETE remaining
frequency sum. Bounded Z and U are absorbed into fixed-data constants.

The exceptional sets and rho were fixed before these tail orders and the
remaining arbitrary small losses. Choose all other norm losses (reflection,
correction, FE, M2, convexity, dyadic logs and U-to-Z conversions) with total
Z cost less than e. There are finitely many bounds. Equations (13)--(18) give

    I(Z^a,Z^a,Z)=c0 f_a(Z)+O_e(Z^(theta+8e)).                (19)

By (2), 2a<1 and theta=a/2, the complete physical I is O(Z^(theta+eta)).
Consequently f_a(Z)<<_e Z^(21/100+8e). This is a bound on the actual detector,
not a new assumed cancellation estimate.

## 6. Mellin continuation, quantifiers and descent

The integral integral_0^infinity f_a(Z) Z^(b_a-s) dZ/Z converges holomorphically
for Re s>b_a+theta+8e. Flatness controls zero and (19) controls infinity.
On an original line Re s>1, Mellin inversion identifies it with
exp((s-5/6)^2)H(s)/zeta_F^S(s). Uniqueness of meromorphic continuation and
nonvanishing of H exclude denominator zeros in this region. The principal
pole at one gives a removable zero of the reciprocal, not an obstruction.

Here b_a=52/75 and b_a+theta=271/300. For EACH point Re s>271/300 choose
ONE fixed 0<e<=10^(-7) with 8e<Re s-271/300. The preceding argument applies.
No uniform limiting constant as e tends to zero and no boundary-line claim
is used. The number of density classes is fixed throughout.

For arbitrary K, F=K(mu_12) is abelian over K; classical factorization writes
zeta_F=zeta_K times entire nonprincipal Hecke factors. A zero away from one
would persist. A finite-order Hecke character is included in the zeta
factorization of its finite cyclic class field. At one the quotient of the
two nonzero residues is nonzero, so none of its entire nonprincipal factors
can vanish there. Finite missing Euler factors have zeros only on Re s=0.
No general Artin holomorphy, growing-field uniformity or angular-twist theorem
is presumed. This proves the stated proposed implications.

## 7. A fourth-moment-free consequence

For Theorem B put a=3/7,h=4/7,theta=3/14. Begin at sigma_0=9/14, advance by
1/500 as long as the next threshold is below 97/100, then append 97/100.
This gives 165 thresholds and 166 classes. Use DF at EVERY threshold.
The same contours and proof apply, with all constants recomputed rather than
borrowed from (14). The exact minimum middle margin is

    82059129/31099583375>0.

The small exponent is 559/2800+e; the principal remainders are
2/21+(11/7)e and 3/14+(11/7)e. The large tail is -27/2-2e.
The true shift is 29/42, hence theta+b_a=19/21. The full second certificate
checks every class and contour on the same whole epsilon interval. This is
not a theorem obtained by replacing M4 density by DF without recalculation.

## 8. Gain, overlap and the remaining target

The new operation is using the selected zero-free information on the direct
reflected numerator, rather than always paying for a full-family numerator
moment. It is distinct from #969/#974 off-central interpolation and from
#975's transverse finite-part construction. Those ideas remain credited.
The old 68/75 packet is already recovered in #970; this pass does not claim
its restoration as a new publication or a second proof. The recovered
163/180 eighth-moment proposal in #976 is stronger than 68/75; (1) improves
it by 1/450, subject to each proof's qualifications.

A small exponent change is not a resolution of RH. The current bound still
takes absolute values of the reflected root numbers. A further signed
estimate would have to control the ORIGINAL root-number-weighted ratio and
H_u on these zero-selected classes with both height truncations retained.
An unweighted Gauss-sum mean cannot silently be substituted for that target.
No such signed bound or native inverse-Mobius all-moment estimate is supplied.

Priority review: the two-sided log-L bound and exact conjugate FE; both-height
truncation; the enlarged local domain; the selected-character density import;
and #965's complete subcritical reflection. The checker follows those analytic
obligations rather than replacing them.

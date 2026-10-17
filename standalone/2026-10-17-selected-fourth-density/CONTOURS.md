# A proposed 109/120 all-field consequence

Status: PROPOSED composition proof, not independently reviewed or formally
verified. This is a deduction from CT, BGL, de Faveri, the recovered short-
support Theorem R, and PROOF.md of this packet. No unproved RH/native-moment
hypothesis is introduced. An analytic error in any adapter or Theorem R would
invalidate the consequence regardless of the rational checker. This is not a
proof of RH, nor an improvement over the reported 7/8 Riemann special case.

## 1. Statement, frozen sources and parameter choices

The proposed conclusion is, for every number field K,

  zeta_K(s) != 0 for Re s>109/120, s!=1,                 (1)

and the corresponding finite-order Hecke statement. The boundary line is
not included. Constants are not uniform over discriminants or conductors.
The improvement over the recovered 91/100 claim is 1/600. The more structural
new estimate is the exceptional-character exponent 43/60 in PROOF.md.

The #959 source is fixed at 7b845294207d96b883c1fa95028663082267804f.
The preceding unpublished short-support packet is recovered without changing
its thirteen original files. Its tree is a80cb7e2404e0f6835c47017597b6acbeb9cb264;
its REFLECTED_MOMENT.md states and proves the exact two-term bound used below.
The original 91/100 statement remains a historical proposed statement, not
silently upgraded. The current passage from 91/100 to (1) has its own proof.

Work first over F containing mu_12 with the exact CT data. Fix

  a=alpha=beta=9/20, h=1-a=11/20, M=2a=9/10,
  X=Y=Z^a, theta=a/2=9/40,
  C=a/2+h/6=19/60, b=1-C=41/60,
  z0=2/5, delta0=1/200,
  0<e<=10^(-7).                                        (2)

The parameter e is fixed while Z tends to infinity. M is strictly LESS
than one. We do NOT invoke CT's long-support proposition with this M.
All arbitrary losses and truncated-height choices are made after e is fixed.

## 2. The physical short-support input, and its audit

CT's unrestricted separated reflection, before its long-support simplification,
and the number-field quadratic large sieve imply the recovered Theorem R:

  Q(P,D;Z) << (PD)^eta P^(1/2)(D+D^2 P/Z),
  sum_(m in a balanced support of norm N) |B_m(Z)|^2
                     << N^eta (N+N^2/Z), N,Z>=2.       (3)

The balanced sets are finite intersections with ell_N times a fixed compact
subset of F_S^times, not all elements in a norm-only ball. Generator
multiplicity is bounded by discreteness of S-units in a compact ratio set.
The powerful part h(m) and squarefree part d(m) refer to physical rows,
NOT to Poisson denominators. Their norm dyads are P,D.

The recovered proof was reread against CT's actual v2 separated reflection
and local beta formula during this pass. Its crucial steps are: for effective
length L=D^2 N(f)^2/(Z N(a)N(n)^3), summing all quadratic column blocks gives
root norm

  O(D^(eta/2)[sqrt(D)L^(eta/2)+L^((1+eta)/2)]) if L>=1,
  O(D^((1+eta)/2)L^A) if 0<L<1.                         (4)

The outside 1/N(n) is retained. Splitting at N(n)=(D^2N(f)^2/(ZN(a)))^(1/3)
sums the full n tail and avoids an infinite harmonic loss. The ramified
beta masses sum to at most 6^omega(h), with N(f)^2<=N(h), and the number of
powerful h through P is O(sqrt(P)). These facts give (3) with both terms.
No newly commissioned independent review of this proof has occurred.

CT's unchanged additive square norm is O(1/X+1/Y). It follows at the actual
physical support N=XY=Z^(9/10) that

  |I(Z^a,Z^a,Z)|^2 << Z^eta (XY+(XY)^2/Z)(1/X+1/Y),
  |I(Z^a,Z^a,Z)| << Z^(9/40+eta).                       (5)

Thus the theta side already has the required exponent. No signed low-row
hypothesis from #961 is assumed; (5) uses a different, shorter support regime.

## 3. Exact Poisson family and the mean/density interface

Keep CT's same triple Mellin identity, common-prime correction H_u, finite
S types, unit quotient Gamma, and original profile functions. Its monomial is

  X^(1/2-z) Z^(xi+z-1) Y^(w-1).                         (6)

The character numerator is L_F^S(w,chi_u); the denominator is
L_F^S(xi,bar chi_u). The pole factor is zeta_F^S(6z). Each representative
u=epsilon g(a) modulo Gamma has a sixth-power-free exterior ideal a, and
q_u=N(a) is its full norm. Epsilon ranges over the fixed finite S-unit
sixth-class quotient. Use DF's deep ray modulus with local sixth powers
at S and choose its ideal representatives compatibly with CT's g. In DF's
factorization a=(x)E d^6, the allowed generator x m_E g(d)^6 has the same
local sixth class as g(a). Their ratio belongs to Gamma. Residue symbols
therefore agree, and on shared primes both original functions are zero.
Consequently chi_u=psi_epsilon chi_a^DF for a fixed finite list of
S-supported finite-order twists. This is #959's adapter, not a newly
invented family. No angular theta character is substituted for psi_epsilon.

For x=Re xi, y=Re w, z=Re z, the Z exponent from (6) is

  E(x,y,z)=a/2+x-1+h z+a(y-1).                          (7)

On a class of O(U^nu) rows, where U<=q_u<2U, and where the reciprocal and
correction cost U^eta, the three available row exponents are

  second mean at y=1/2: (nu+1)/2-z;
  fourth mean at y=1/2: 3nu/4+7/24-z;
  individual convexity at 0<y<=1: nu+(1-y)/2-z.         (8)

Use PROOF.md (6) only AFTER bounding the reciprocal and the original
correction uniformly on the class. Neither their correlation with the
numerator nor the zero-based choice of the class causes an independence
assumption. Height dependence is polynomial and paid by CT's joint decay.

The fixed strict correction domain is

  x,y,z>0; 6z+y>1; x+6z>1; x+y>1; x+y+6z>2;
  6x+6z>5; x>1/2; 3x>2; 3x+y>5/2.                    (9)

The domain is convex. The checker checks every contour corner, including
intermediate corners, not only the final exponent. On a nonprincipal row
moving w across 1 creates no pole, and z0>1/6 avoids the z pole.

## 4. Seventeen disjoint classes with exact rational data

The following table lists each U-class's U-count exponent nu before the
small positive e loss, its upper zero-free threshold s, and the method in (8).
Every middle class is counted at the LOWER threshold (previous row's s) and
shifted just to the right of the UPPER threshold (its own s). The machine
file strata.json contains the exact density parameters A=U^da,B=U^db and
both endpoints of every required detector test are checked by verify.py.

|j|s (upper threshold)|nu (lower-threshold count)|method|
|---:|---:|---:|---|
|0|337/500|1|second|
|1|7239/10000|247388/299631|fourth|
|2|75137/100000|504082343/664106466|fourth|
|3|38491/50000|53881379027/75430536474|fourth|
|4|2448/3125|13805709023/20257792626|fourth|
|5|79387/100000|217580153/331669686|fourth|
|6|80237/100000|55775570027/87779778474|fourth|
|7|80947/100000|55647213227/90015536874|fourth|
|8|20389/25000|55410408347/91823242314|fourth|
|9|82089/100000|3444581693/5833151166|fourth|
|10|413/500|54782066243/94616638266|convex|
|11|1667/2000|340013/598881|convex|
|12|84473/100000|21493487/39014994|convex|
|13|43103/50000|52486860707/99994112634|convex|
|14|89009/100000|12495910247/25879470114|convex|
|15|93897/100000|44447281523/108530737626|convex|
|16|1|308738564/1138260173|convex|

Choose a fixed rho>0 and initial arbitrary losses so that PROOF.md (8)--(11)
and the last DF detector estimate bound each exceptional set by U^(nu+e).
Their height factors are polynomial, so one sufficiently small rho works
for this FINITE list. Define E_j(U) by the existence of a zero at Re s>=s_j,
|Im s|<=4U^rho, for j=0,...,15. This definition is fixed BEFORE the later
arbitrary reciprocal losses. The sets are nested. The seventeen classes
are E_0^c, E_0\E_1,..., E_14\E_15, E_15. They cover all nonprincipal rows
without overlaps. The good class has count exponent exactly 1; all others
use nu+e. The last class never moves xi left of 1+e.

If a row is outside E_j, use disks centered at 2+it, |t|<=2U^rho, of radii

  R=2-s_j-e/4, r_o=2-s_j-e/2,
  r_t=2-s_j-e, r_i=1-e/4.

Their strict ordering and containment in the zero-free rectangle hold for
large U. The Euler logarithm is bounded on r_i and at the center. Polynomial
L-growth bounds the real part of its analytic logarithm by O(log U) on R.
Borel--Caratheodory and three circles give |log L|=O_e((log U)^theta_j)
with theta_j<1 on r_t. Thus for every lambda>0 the reciprocal is O(U^lambda)
on s_j+e<=x<=1+e on the truncated central segment. The SAME exceptional set
works for every lambda, with new constants. Removed Euler factors contribute
only U^lambda on these fixed positive real parts. Conjugation preserves
the zero count in the symmetric height rectangle.

For Z^delta0<U<=Z^(h+e), set z=z0, x=s+e. The mean classes have y=1/2;
the convex classes have y=1-s+e. For the last class x=1+e,y=e, using the
Euler reciprocal instead of a zero-free claim. Start each at
(1+e,1+e,z0), move xi on its central rectangle, and then w. Every segment
lies in (9). The dyadic U exponent v from (8) is positive throughout, so
its top endpoint is valid. For each class the exact growth polynomial is

  p_j(e)=E(x,y,z0)+(h+e)*v.                              (10)

Exact rational Bernstein certificates on the WHOLE interval 0<=e<=10^-7
prove p_j(e)<=9/40+2e for all seventeen j. At e=0, each middle class lies
at least 1/10000 below 9/40; the good class is 1/1000 below. These endpoint
values check the algebra; actual contours always have e>0. The table was
suggested by exploratory optimization but no floating optimizer enters the
proof or the published verifier. No optimum is claimed.

## 5. Principal, small, large and horizontal pieces

Principal: start (x,y,z)=(1+e,1+e,1/6+e); move w to 1/2 taking the pole at
1; in its residue move z to e taking the pole at 1/6. The remaining two
corners lie in (9), with exponents

  principal w: 11/120+(31/20)e;
  principal z: 9/40+(31/20)e.                            (11)

The double residue is the unchanged nonzero constant times

  f_a(Z)=(1/(2pi i)) integral_(2) Z^(s-41/60)
            exp((s-5/6)^2) H(s)/zeta_F^S(s) ds.          (12)

No proposed improved zero-free theorem is used to move the principal xi
line: it stays to the right of one. This removes a potential circular
bootstrap. The count and numerator refinements do not change b in (12).

Small U<=Z^(1/200): retain x=1+e,z=z0, take y=1/2 and the full second mean.
Its exponent is exactly 223/1000+e, strictly below 9/40+2e. The older cutoff
1/100 at these NEW scales would give 113/500=0.226>9/40; it is NOT reused.
This small-range change is explicitly required and checked.

Large U>Z^(h+e): use the original absolutely convergent x=y=4 lines and
z=L=10/e+2. The row factor is U^(1-L+eta), NOT U^(1+(1-y)/2-L).
At the first dyad its exponent is

  a/2+3+hL+3a+(h+e)(1-L)=-39/8-e.                       (13)

Subsequent dyads decay geometrically; L is fixed after e. The freedom to
choose a large but fixed z line follows from the initial absolute identity
and the arbitrary profile decay, not a leftward continuation theorem.

For intermediate horizontal edges and retained original-xi-line tails,
fix the working height at U^rho as in the zero definition. CT's joint
Gaussian in xi+z and its z,w Schwartz/Mellin decay give U^(-rho A) for any
fixed A after multiplying a fixed polynomial in U,Z. This includes the
nearly cancelling direction Im z approximately -Im xi. The shifted horizontal
segments remain below 2U^rho, where the reciprocal bound is valid. Since
U>Z^(1/200), choose A sufficiently large to dominate every finite cost and
make the total O(Z^-1). One does not assert zero exclusion outside the
actually truncated rectangle or decay from the xi Gaussian alone.

Combining (10)--(13), finite unit classes and dyadic logarithms, allot the
remaining arbitrary power losses total cost <e. The complete comparison is

  I(Z^a,Z^a,Z)=c0 f_a(Z)+O_e(Z^(9/40+3e)), c0!=0.       (14)

Together with (5), choosing its loss smaller than e, this proves the proposed
actual detector bound f_a(Z)<<_e Z^(9/40+3e).

## 6. Mellin conclusion and its limits

The detector is flat at zero by moving its original right contour farther
right. Its Mellin integral therefore defines a holomorphic function for
Re s>b+9/40+3e=109/120+3e. On the original convergence half-plane it equals
exp((s-5/6)^2)H(s)/zeta_F^S(s). CT proves H is holomorphic and nonvanishing
on Re s>2/3. The Gaussian factor is nonzero as well. Analytic continuation
therefore excludes zeros in Re s>109/120+3e. For each point right of 109/120
choose one sufficiently small FIXED e>0. No constants need be uniform as
e tends to zero, and no conclusion is made on the boundary line.

For arbitrary K, first apply this to F=K(mu_12). The extension F/K is
abelian. Classical Artin/Hecke factorization and holomorphy of nonprincipal
Hecke factors prevent a zero of zeta_K from disappearing in zeta_F away
from one. The same factorization in the class field associated with any
finite-order Hecke character gives its claimed region. The nonprincipal
s=1 case also uses the classical Hecke nonvanishing at one. No infinite-order
angular twist is included, and no discriminant-uniform constant is obtained.

Theorem A and Theorem B of PROOF.md are independent of CT. The global
consequence here is not: its most vulnerable analytic inputs remain the
full-family adapters, pre-Cauchy subset zero detector, and recovered short-
support reflection. This publication is not independent review of any of
them. The original fixed-center signed Mobius energy and full RH remain open.

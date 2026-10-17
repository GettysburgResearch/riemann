# Five zero-density strata and a proposed 25/27 Dedekind boundary

Status: PROPOSED source-composition theorem, independent review pending.
The precise imported analytic hypotheses and primary-source access limits
are in CONTRACTS.md. The new argument proves the consequence of those
contracts, which the cited sources state unconditionally. No RH, GRH,
unknown native moment or signed-covariance estimate is assumed. This is
not independent verification of the imported theta or large-sieve theorems.

## 1. Statement, novelty scope and a fixed positive slack

**Proposed consequence of the imported CT/DF/BGL inputs.** For every number
field K,

    zeta_K(s) != 0 for Re(s)>25/27, s!=1.                 (1)

The same region is zero-free for finite-order Hecke L-functions, including
s=1 for nonprincipal characters. The strict boundary line is not included.
No conductor/discriminant-uniform constants or infinite-order angular
character conclusion is claimed.

The new step beyond #957 is a finite partition of exceptional denominators
according to their zero-free rectangles, instead of treating every bad row
at one worst contour. Four density thresholds suffice. Their explicit
contours leave the ordinary good class and the unchanged theta bound as the
limiting terms. This improves #957's proposed all-field 23/24 boundary to
25/27 under the same imported analytic foundation. It does not improve the
stronger previously reported special-setting 7/8 result for Riemann zeta,
and is not RH. Zero stratification itself is a classical method; no first
invention or exhaustive literature-priority claim is made.

Choose a real number e with 0<e<=1/10000 and hold it fixed while Z tends to
infinity. All constants and thresholds may depend on e. Set

    alpha=5/9, h=1-alpha=4/9, beta=4/9+e,
    X=Z^alpha, Y=Z^beta, M=alpha+beta=1+e,
    C=alpha/2+h/6=19/54, b=1-C=35/54.                   (2)

Thus beta<alpha and M>1. We NEVER apply CT at e=0. The limit at the end is
an intersection of valid open-half-plane conclusions for fixed positive e.
It does not require constants uniform as e decreases to zero.

## 2. Exact family, fixed twists and the four density estimates

Work initially over F containing mu_12, with exactly the CT data of
CONTRACTS.md. Its sixth-power-free representatives have the unique form

    u=epsilon g(a) modulo Gamma, 0<=v_p(a)<=5,
    q_u=N a, epsilon in the fixed finite R*/(R*)^6.       (3)

No norm-only element ball in a field of positive unit rank is being counted.
Choose the legal DF deep ray modulus so x=1 modulo it is a local sixth
power at S. Choose the DF generators m_(E0)=g(E0) and extend multiplicatively.
For the DF decomposition a=(x)E h0^6, its allowed generator is
x m_E g(h0)^6. Its local class is in the CT subgroup B, hence its ratio to
g(a) lies in Gamma. With h0 chosen coprime to the test ideal, the residue
symbols coincide. The two functions have identical zero values on shared
primes as well. Consequently

    chi_u = psi_epsilon chi_a^DF,
    psi_epsilon(b0)=(epsilon/b0)_6.                      (4)

psi_epsilon has finite order and fixed S-supported conductor. The finite
list in (4) is NOT omitted. The angular character in the theta construction
is a different object and does not enter this zero-density application.
This is the family adapter of #957, reconstructed using DF's inspected
choice of generators, rather than a new family identification claim.

Here are details for retaining the fixed twist in the density estimate.
For a fixed psi, DF-LS changes a column lambda_b to psi(b)lambda_b; its
absolute square mass is unchanged. Original masks stay zero. The central
second mean needed in BGL's zero detector is

    sum_(Na<=N)^flat |L_F^S(1/2+it,psi chi_a)|^2
        << (N(1+|t|)^(d/2))^(1+epsilon), d=[F:Q].       (5)

One can retain BGL's complete-column proof under the fixed twist. Write
row a=a0 a1 with a0 squarefree, a1 powerful, (a0,a1)=1. After Mellin separation
an approximate-functional-equation length L is at most
N^(1/2+epsilon)(1+|t|)^(d/2+epsilon). For fixed a1 the factor psi chi_(a1)
is a column phase. The squarefree sieve gives
N/Na1+L+((N/Na1)L)^(2/3). Summing powerful a1 yields
N+L sqrt(N)+(NL)^(2/3), within (5). In the complete AFE column, write
b=b0 b1, b0 squarefree, b1 powerful and coprime. Its residual root weight
(Nb1)^(-1/2-epsilon) is summable. This is the positive small Mellin shift
in BGL (5.1); it does not replace the AFE by squarefree columns.

For detector columns with coefficients <<(Nb)^epsilon the same split costs
only sum_(Nb1<=2L,powerful)(Nb1)^(-1/2)=O(log(3L)), after Minkowski.
The full detector second mean is consequently bounded by

    (NL)^epsilon L [N+L+N^(5/6)L^(1/3)+N^(1/3)L^(5/6)].

This bound may retain row multipliers depending on b1: their absolute value
is at most one. Finite S Euler factors and finite residue-class subdivisions
change constants or arbitrary losses only. The analytic detection inequality
itself is the explicitly imported BGL (5.3), not proved by this observation.
Applying it gives, for 1<=A<=B,

    sum_(Na<=N)^flat N_psi(sigma,T,a) << (NTB)^epsilon T {
       B^(1/2-sigma)(NT^(d/2))^(1/2)
           (A+N+A^(1/3)N^(5/6)+A^(5/6)N^(1/3))^(1/2)
       +B^(2-2sigma)+N A^(1-2sigma)
       +sup_(A<=V<=B) V^(1-2sigma)
             (N^(1/3)V^(5/6)+N^(5/6)V^(1/3)) }.        (6)

This is the full inequality in the inspected DF Corollary 1.5 proof,
with the fixed twist retained as above. We need only four exact instances:

| sigma | A=N^a | B=N^b T^(z*d) | density g | height exponent |
|---|---|---|---|---|
| 2/3 | a=1/2 | b=1, z=3/10 | 5/6 | 1+d/5 |
| 3/4 | a=7/11 | b=13/11, z=1/3 | 8/11 | 1+d/6 |
| 17/20 | a=295/359 | b=535/359, z=5/13 | 191/359 | 1+3d/26 |
| 19/20 | a=70/47 | b=110/47, z=5/11 | 11/47 | 1+d/22 |

In each row substituting in all four terms in the inner square root, the
two separate terms, and BOTH endpoints of BOTH supremum monomials proves

    sum_(Na<=N)^flat N_psi(sigma,T,a)
        << N^(g(sigma)+epsilon) T^(H_d(sigma)+epsilon).   (7)

The exact checker verifies each substitution. These are consequences of
the imported sieve/detector, not a numerical estimate of a zero population.
For example the values of g are 5/6,8/11,191/359,11/47, not the conductor-
ordered or radical-ordered density of a different family.

## 3. Fixed exceptional sets and zero-free reciprocal bounds

Put sigma_0=2/3, sigma_1=3/4, sigma_2=17/20, sigma_3=19/20. Choose ONCE a
small rho>0, for example

    rho <= min(10^(-6), e/[10^6(1+H_max+A_F)]),          (8)

where H_max=1+d/5 and A_F covers the fixed polynomial height exponents of
the relevant Hecke functions. Choose the arbitrary loss in (7) small
enough that its TOTAL U exponent in T=4U^rho is at most g(sigma_j)+e.
There are only four thresholds and finitely many fixed psi, so the same
rho and loss choice work for all. For large U define E_j(U) to be the
nonprincipal rows U<=q_u<2U with a zero at real part >=sigma_j and
|Im s|<=4U^rho. Then

    E_3 subset E_2 subset E_1 subset E_0,
    #E_j(U) << U^(g(sigma_j)+e).                         (9)

The exceptional sets and rho are fixed BEFORE the later reciprocal losses.
The class definition counts zeros of the inducing primitive L-function;
the exterior missing Euler factors have no zeros in Re s>0. Conjugating
chi_u does not change the zero count in a rectangle symmetric in Im s.

We use five DISJOINT classes: the complement of E_0, E_0\E_1, E_1\E_2,
E_2\E_3, and E_3. A middle class is charged at its LOWER threshold but its
reciprocal is controlled to the right of its UPPER threshold. Confusing
these two thresholds would manufacture a stronger, invalid saving.

Here is a precise reciprocal argument. If a row is outside E_j(U), fix
|t|<=2U^rho. Choose concentric disks about 2+it with radii

    R=2-sigma_j-e/4, r_outer=2-sigma_j-e/2,
    r_target=2-sigma_j-e, r_inner=1-e/4.

For the four thresholds and our e these radii are strictly ordered
0<r_inner<r_target<r_outer<R. The outer disk lies in the zero-free rectangle
for all sufficiently large U. Take log L by analytic continuation from
its Euler value at the center. On R, polynomial growth bounds its real part
by O(log U), while its value at the center is O(1). Borel--Caratheodory
bounds the modulus on r_outer by O_e(log U). The Euler logarithm is O_e(1)
on r_inner. Hadamard three circles applied to log L then gives

    |log L| <<_e (log U)^theta,  theta<1,

on r_target. Therefore for EVERY lambda>0,

    |1/L_F^S(x+it,bar chi_u)| <<_(e,lambda) U^lambda,
    sigma_j+e <= x <= 1+e, |t|<=2U^rho.                 (10)

The inducing-character omission factors cost U^lambda as well: use
(1-q^(-x))^(-1)<=q^lambda for sufficiently large q and absorb the finitely
many smaller primes. One must first fix their x>=sigma_j+e>0.
The same row set works for all lambda, with lambda-dependent constants and
thresholds. No zero of an exceptional row is crossed. In the last class
we keep x=1+e and use absolute Euler convergence instead of (10).

## 4. The actual contours, including the tails

By CT-1 and (2), the unchanged theta average satisfies

    |I(Z^(5/9),Z^(4/9+e),Z)| << Z^(5/18+e/2+epsilon).   (11)

Indeed P^(1/2)D<=Z^M<=Z^(2M-1), and
P^(3/2)D^2/Z<=(PD)^2/Z<=Z^(2M-1), since P>=1 and M>1.
The additive square norm is O(1/Y). No higher native moment is an input.

Let E(x,y,z)=alpha/2+x-1+h z+beta(y-1), the exact Z exponent.
The principal contour is first moved to
(1+e,1+e,1/6+e). Move w to 1/2, taking its residue at 1. In that residue
move z to e, taking its residue at 1/6. The double residue is c0 f(Z) with
c0!=0 and the actual detector

    f(Z)=(1/2pi i) integral_(2) Z^(s-35/54)
                   exp((s-5/6)^2) H(s)/zeta_F^S(s) ds. (12)

The two remainders have corners (1+e,1/2,1/6+e) and (1+e,1,e).
Their exact savings relative to C=19/54 are

    S_principal,w=2/9-17e/18,
    S_principal,z=2/27-13e/9.                           (13)

All starting/end vertices satisfy CT-Omega strictly. The convexity of that
domain covers the connecting segments; pole crossings are precisely the
two principal residues just named. No use of the nonprincipal no-pole rule
is made for this row.

For nonprincipal u, fix z=2/5. Use U<=Z^(1/100) as the small-frequency
range. On it keep xi=1+e and move w to 1/2+e. The bound CT-D and #u=O(U)
give saving

    S_small=5941/54000-1691e/1800-e^2.                  (14)

For Z^(1/100)<U<=Z^(h+e), use these contours and counts:

| Class | x=Re xi | y=Re w | nu in #class << U^nu |
|---|---|---|---|
| outside E_0 | 2/3+e | 1/2+e | 1 |
| E_0\E_1 | 3/4+e | 1/4+e | 5/6+e |
| E_1\E_2 | 17/20+e | 3/20+e | 8/11+e |
| E_2\E_3 | 19/20+e | 1/20+e | 191/359+e |
| E_3 | 1+e | e | 11/47+e |

Starting at (1+e,1+e,2/5), move xi on its central truncated rectangle to x,
then w to y. All vertices and segments lie strictly inside CT-Omega.
For example the first class has 3x+y-5/2=4e>0; the next has both
x+y-1=2e>0 and 3x+y-5/2=4e>0. Subsequent classes have greater remaining
margins. Since chi_u is nonprincipal, w crosses no pole; 2/5>1/6 keeps
z away from its pole. Equation (10) licenses every denominator move.
The statement about zero-free classes is at heights where that move is
actually made, not a claim of global nonvanishing of any denominator.

The U exponent nu+(1-y)/2-2/5 is positive in each of the five cases.
Evaluate the upper endpoint U=Z^(h+e) in CT-D. In table order, the exact
savings are

    S_g = 2/27       -(283/180)e    -(1/2)e^2,
    S_0 = 13/108     -(69/40)e      -(3/2)e^2,
    S_1 = 533/5940   -(2071/1320)e  -(3/2)e^2,
    S_2 = 19139/193860-(11405/8616)e-(3/2)e^2,
    S_3 = 244/1269   -(1411/1410)e  -(3/2)e^2.           (15)

For every 0<e<=1/10000 each quantity in (13)--(15), the theta saving
2/27-e/2, and (14), is at least 2/27-2e. This is checked by rational
Bernstein certificates on the ENTIRE interval, not a sampled grid.
At e=0 the middle-class savings are about .12037,.08973,.09872,.19228;
only S_g and the theta/principal-z bounds approach 2/27. These endpoint
values describe the limiting algebra, not legal endpoint contours.

Retain the original xi=1+e tails and horizontal edges at height U^rho.
CT-4 supplies U^(-rho A) times a fixed polynomial U and Z cost on all
those pieces. On the shifted horizontal edges (10) remains valid, since
the working height is below 2U^rho. As U>Z^(1/100), choosing one sufficiently
large FIXED A makes their total smaller than any specified negative power
of Z. This uses joint height decay, not an unjustified xi-only Gaussian.
It chooses decay seminorms after e and rho are fixed, not a different test
function or height-dependent exceptional set at each loss.

For U>Z^(h+e), return to the initial integral and use x=y=4,z=L with
L=ceil(10/e). CT-L gives a geometrically summable tail. Its saving is

    S_large=C-alpha/2-3-3beta-h-e+e L > 4.               (16)

The strict upper cutoff h+e is essential. At e=0 one would lose the term
eL, so this cannot be justified by silently setting M=1. The large vertex
satisfies CT-Omega for every L>=1.

Bounded small U that do not yet satisfy the logarithm estimates are already
in the small-frequency case once Z is sufficiently large. Bounded Z is
absorbed in the constants. The finite dyadic logarithms, divisor losses,
reciprocal losses and height bounds consume less than a total e of Z power
by choosing their arbitrary epsilons sufficiently small. The rho in (8)
was already chosen sufficiently small for the unavoidable height factors.
All class sets stay fixed. Hence (11)--(16) imply

    I=c0 f+O_e(Z^(C-2/27+3e)),
    f(Z) <<_e Z^(5/18+3e), Z>=2.                       (17)

Every principal, nonprincipal, small, five-class central, horizontal, retained
xi-tail, and large-frequency piece has been included. In particular, there
is no unestimated exceptional remainder hidden by the new partition.

## 5. Mellin holomorphy and the strict limiting boundary

By CT-P, f is flat at Z=0. Equation (17) makes

    integral_0^infinity f(Z) Z^(-s+35/54) dZ/Z

holomorphic in Re(s)>25/27+3e. Initial-line Mellin inversion identifies it
with exp((s-5/6)^2)H(s)/zeta_F^S(s). Uniqueness of meromorphic continuation
preserves that identity. The numerator is nonzero there, because
25/27>2/3; every zero of the denominator would be a genuine pole, contrary
to holomorphy. Removed finite Euler factors have zeros on Re(s)=0 only.
This excludes zeros in Re(s)>25/27+3e for each fixed positive e.

Given any particular point with Re(s)>25/27, select
0<e<min(1/10000,(Re(s)-25/27)/3). The argument at this fixed e excludes a
zero at that point. This proves the OPEN half-plane in (1), without any
uniformity of constants as e->0 or a claim on its boundary line.

For arbitrary K take F=K(mu_12). F/K is abelian. The classical factorization
zeta_F=zeta_K times the nonprincipal Hecke factors contains only entire
other factors. A zero of zeta_K away from one cannot be canceled by them.
This proves (1) for K. For a finite-order Hecke character use its finite
abelian class field and the same factorization. Nonprincipal nonvanishing
at one also follows from the nonzero ratio of the simple-pole residues;
the primitive principal member instead has a pole. Imprimitive factors add
Euler polynomials whose zeros have real part zero. Infinite-order angular
characters do not follow from this descent.

## 6. What would be needed beyond 25/27

The improvement pays the exceptional rows more accurately; it has not supplied
a new signed theta moment, critical native covariance, or improved correction
factor domain. Even perfect density estimates above the good-class threshold
would leave two limiting costs in the PRESENT positive-bound model.
For beta<=alpha, h=1-alpha, beta>h (M>1), they are

    S_theta=2h/3-beta/2,
    S_floor=1/3+beta/2-13h/12.                           (18)

Within this model their joint ceiling is 2/27. If h<=4/9,

    2/27-S_theta=(4/9-h)/6+(beta-h)/2 >=0.

If h>4/9, put v=beta-h/2<=1-3h/2<1/3. At frequency U=Z^h the z cost
cancels. The best correction-domain good contour has x=2/3,y=1/2 in the
limiting algebra: minimize y subject to y>=max(0,1-x,5/2-3x), x>=2/3.
The resulting slopes of the saving as x increases are -1+3v, -1+v and -1,
all negative. Its value is at most S_floor. But

    2/27-(S_theta+S_floor)/2=(5/24)(h-4/9)>0.

This is a ceiling for these particular U-uniform positive upper estimates,
NOT a lower bound on the true arithmetic integral or a no-go theorem for RH.
The positive-slack family (2) approaches that ceiling and the finite strata
(15) stay above it. Going further calls for improving the reflected estimate,
using its signed pairing, changing the full correction-domain/source adapter,
or a genuinely different method; taking more density bins alone does not
remove (18). The earlier covariance and pre-Poisson packets are relevant to
those alternatives, but none of their open targets is claimed solved here.

## 7. Review boundary

All new algebraic substitutions and the finite-stratum implementation are
supplied above; all imported analytic interfaces are explicit in CONTRACTS.md.
DF and BGL primary inputs were freshly inspected at the recorded scopes.
CT source fidelity was NOT freshly verified against a retrieved full v2
manuscript; that import is taken from the exact #957 adapter and the earlier
#948 account. A failure of CT-1's all-M range, CT-D's full corrected dyad bound,
the allowed-generator matching, or the joint contour-tail contract would
invalidate the proposed conclusion. These are priority independent review
targets, not facts that the rational checker can establish.

No earlier unreviewed theorem is promoted to integrated status. No Lean build,
independent referee, full theta-source replay, or exhaustive priority audit
is claimed. Recovery of old packets is a separate operation from this proof.

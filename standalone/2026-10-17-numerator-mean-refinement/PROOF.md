# A numerator-family mean and a proposed 11/12 Dedekind boundary

Status: PROPOSED composition of explicitly imported unconditional analytic results.
Independent mathematical review is pending. No RH/GRH, unknown native moment,
critical signed covariance, or new metaplectic construction is assumed.
The primary CT v2 interfaces below were freshly read, including its TeX source;
this is not a reconstruction or Lean verification of its entire foundation.

## 1. Statement and relation to the preceding work

**Proposed theorem.** For every number field K, its Dedekind zeta function has
no zero at s != 1 with Re(s)>11/12. The same strict half-plane is zero-free
for finite-order Hecke L-functions; for a nonprincipal character this includes
s=1. No boundary-line assertion or conductor/discriminant-uniform constant is
made. The pole of a principal function at one is not called a nonzero value.

The contribution is a new use of the classical numerator-family second mean
in the actual CT Poisson sum, and an explicit four-class comparison. It replaces
the individual numerator convexity loss on the good class of #958. The proof
therefore reaches 11/12, rather than #958's proposed 25/27, under the same
CT/BGL/de Faveri analytic foundation. It is not an improvement of the previously
reported special-setting 7/8 Riemann-zeta result or a proof of RH. The classical
mean, Cauchy inequality and zero stratification are credited, not claimed invented.

Here and below CT = Cureton--Thorner, Hexagon 2610.00200v2; DF = de Faveri,
arXiv:2610.04045v1; BGL = Blomer--Goldmakher--Louvel, arXiv:1112.1650.
SOURCES.md gives exact inspected locations and the earlier PR identities.

## 2. The precise inherited source, before any inequalities

First fix F containing mu_12, degree d, and CT's finite S, allowed generators,
local vector and smoothing profiles. All implied constants may depend on these
fixed data. Put R=O_(F,S), Gamma=(R*)^6. An exterior ideal is supported outside S;
q_a=N a is its full ideal norm. Elements of a fixed exterior norm are not summed
without quotienting by Gamma. CT Lemmas 7.2--7.4 identify the finite S-unit classes
and the unique allowed generator g(a) modulo Gamma of each exterior ideal.

We import CT's actual I(X,Y,Z), not a native moment with a similar Euler product.
For beta<=alpha, alpha,beta>0 and M=alpha+beta>1, put X=Z^alpha,Y=Z^beta.
CT Section 9's reflected dyad and Section 10's additive estimate are

    reflected square <= Z^eta P^(1/2)(D+D^2 P/Z), PD << Z^M;
    additive square  <= C(1/Y+1/X).                              (2.1)

The support-exponent paragraph in Section 9 explicitly permits EVERY FIXED M>1
by increasing the decay estimate for the same profiles. It does not license M=1.
Because P>=1 and M>1, summing dyads bounds the reflected square by Z^(2M-1+eta).
Cauchy with the additive square gives

    |I(X,Y,Z)| << Z^(alpha+beta/2-1/2+eta).                       (2.2)

CT Section 11 gives, on its initial absolute-convergence lines, the scale factor

    X^(1/2-z) Z^(xi+z-1) Y^(w-1)

and the u-th meromorphic factor

    q_u^(-z) zeta_F^S(6z) L_F^S(w,chi_u)
                          H_u(xi,w,z)/L_F^S(xi,bar chi_u).       (2.3)

All common-prime factors and their literal zero extensions are in H_u. The only
principal row is u=1. Conductor is at most C q_u, not necessarily equal to q_u.
CT Lemma 11.1 bounds H_u by C_eta q_u^eta uniformly in imaginary parts, on each
fixed-margin subdomain of the convex region

    x,y,z>0; 6z+y>1; x+6z>1; x+y>1; x+y+6z>2;
    6x+6z>5; x>1/2; 3x>2; 3x+y>5/2,                        (2.4)

where x=Re xi,y=Re w,z=Re z. The final two inequalities are the two branches
of CT's 3x>2+max(0,1/2-y). They must BOTH remain.

The fixed Mellin weights have the joint height bound, for any fixed A,

    C_A exp[-(Im xi+Im z)^2]
             (1+|Im z|)^(-A)(1+|Im w|)^(-A).                    (2.5)

This is not Gaussian decay in xi alone. Polynomial L-function height factors
are absorbed by (2.5); convolution also handles Im z approximately -Im xi.
CT supplies ordinary fixed-strip Hecke convexity and the correction bounds.

In the principal row the residues w=1,z=1/6 have fixed nonzero coefficient
c0=R_S^2 M(1/6) W1hat(1)/6. Define

    C=alpha/2+(1-alpha)/6, b=1-C,
    f_alpha(Z)=(1/(2pi i)) integral_(2)
       Z^(s-b) exp((s-5/6)^2) H(s)/zeta_F^S(s) ds.               (2.6)

CT Lemma 11.2 shows that this UNCHANGED H is holomorphic and nowhere zero on
Re s>2/3, with the required vertical bounds. Moving the initial line to the
right makes f_alpha flat at zero. Changing alpha changes b; using 61/100 or
35/54 from the old scale curves here would be incorrect. No new numerator or
coefficient completion is introduced by this packet.

## 3. Exact character-family adapter and the available mean

This adapter overlaps #957/#958; the fresh primary-source check is not a claim
of a second independent arithmetic gain. Every row of exterior valuations 0..5
is u=epsilon g(a) modulo Gamma, with epsilon in the FIXED finite R*/Gamma.
Choose DF's deep S-ray modulus c so x=1 modulo c is a local sixth power at S.
For each generating representative E0 in DF Section 2.3, choose m_E0=g(E0).
These choices are allowed by its definition; extend m_E multiplicatively.

In DF's decomposition a=(x)E h0^6, x=1 modulo c, choose h0 coprime to the test
ideal l as in that construction. Then x m_E g(h0)^6 generates a in R and its
local class is in CT's subgroup B: x and g(h0)^6 have trivial local class and
m_E has class in B. By uniqueness it differs from g(a) by an element of Gamma.
Taking the residue symbol at l gives exactly the CT symbol. On shared primes
both sides are zero, so no equality restricted only to units is being extended
incorrectly. Consequently

    chi_u = psi_epsilon chi_a^DF,
    psi_epsilon(l)=(epsilon/l)_6.                              (3.1)

Each psi_epsilon has order dividing six and fixed S-supported conductor, hence
factors through the fixed deep ray group. The angular theta correction is NOT
one of these finite-order twists. The row ordering is N a, not rad(a) or the
conductor. Conjugate denominator characters retain the same zero counts in a
rectangle symmetric about the real axis.

BGL Section 5, equation (5.1), includes all sixth-power-free a (set a2=1 in its
weighted extension). For this finite list of fixed twists it gives

    sum_(Na<=U)^flat |L_F^S(1/2+it,psi chi_a)|^2
         <<_eta [U(1+|t|)^(d/2)]^(1+eta).                      (3.2)

Here flat means sixth-power-free, not squarefree. To justify the fixed twist
rather than change the family silently, retain BGL's proof. A complete AFE has
length L <= [U^(1/2)(1+|t|)^(d/2)]^(1+eta), with fixed conductor factors absorbed.
Split the row a=a0 a1, where a0 is squarefree, a1 is powerful and sixth-free,
and (a0,a1)=1. Split each complete AFE column into its coprime squarefree and
powerful parts. The latter's root weight with the small positive Mellin shift
is summable: sum_powerful (N b1)^(-1/2-eta)<infinity. No non-squarefree AFE
column is deleted. For fixed a1 and b1, their characters and psi multiply the
column coefficients, and the extra b1 factor is a row multiplier of modulus
at most one. These operations preserve the applicable squarefree sieve bound.
Root numbers in the dual AFE are row phases of modulus one.

BGL Theorem 1.3 then gives, before the remaining powerful-row sum,

    U/N a1 + L + ((U/N a1)L)^(2/3).

There are O_F(sqrt(U)) powerful ideals up to U, while their inverse first and
2/3 moments are summable. Thus the total is
U+L sqrt(U)+(UL)^(2/3), which is within (3.2) after arbitrary small losses.
The same Mellin separation and original coprimality zeros as BGL are retained.
This proves the fixed-twist extension of the imported mean; it does not prove
a new large sieve. The infinite AFE tails follow the original rapid decay.

**Numerator-mean lemma.** Let C(U) be ANY subset of nonprincipal u with
U<=q_u<2U and #C(U)<<U^nu. If its reciprocals on a truncated xi contour obey
|1/L_F^S(xi,bar chi_u)|<<U^eta, then at y=1/2 its central Poisson contribution is

    << Z^E U^((nu+1)/2-z+eta),
    E=alpha/2+x-1+(1-alpha)z+beta(y-1).                          (3.3)

Proof. At every common w-height use (3.2), sum the finite twists, and apply
Cauchy: sum_C |L(1/2+it,chi_u)| <= (#C)^(1/2)(sum_all |L|^2)^(1/2).
Bound the reciprocal and H_u uniformly first; they need not be independent
of the numerator, the subset, or each other. Now integrate the resulting
polynomial height factor against (2.5). Fubini is justified by these absolute
majorants. This proves (3.3). In particular nu=1 costs U^(1-z+eta), instead
of U^(5/4-z+eta) from individual convexity. The U^(1/4) saving is the new use
of a classical input. There is no assertion about a mean of inverse L-values.

For other y in (0,1], retain CT's individual convexity bound

    << Z^E U^(nu+(1-y)/2-z+eta).                                (3.4)

We do not pretend that (3.3) holds away from y=1/2 without another argument.

## 4. Three density thresholds and fixed zero-free rectangles

DF Theorem 1.1 and its Corollary 1.5 proof apply to the same sixth-free family.
Fixed psi is retained by the column multiplication in Section 3. Its sieve
replaces the two arithmetic means of BGL's detector, not the detector itself.
For 1<=A<=B, the resulting bound is

    sum_(Na<=N)^flat N_psi(sigma,T,a) << (NTB)^eta T {
      B^(1/2-sigma)(NT^(d/2))^(1/2)
       [A+N+A^(1/3)N^(5/6)+A^(5/6)N^(1/3)]^(1/2)
      +B^(2-2sigma)+N A^(1-2sigma)
      +sup_(A<=V<=B) V^(1-2sigma)
                   [N^(1/3)V^(5/6)+N^(5/6)V^(1/3)] }.           (4.1)

DF Section 9 spells out this inequality with full detector columns. BGL's
powerful-column separation remains; for detector coefficients its root sum is
O(log(3B)), swallowed by the displayed loss. Only the following three exact
substitutions, A=N^a and B=N^b T^(zd), are needed:

| sigma | a | b | z | g | height exponent |
|---|---|---|---|---|---|
| 3/4 | 7/11 | 13/11 | 1/3 | 8/11 | 1+d/6 |
| 21/25 | 7075/8846 | 6425/4423 | 25/66 | 4919/8846 | 1+4d/33 |
| 19/20 | 70/47 | 110/47 | 5/11 | 11/47 | 1+d/22 |

Substitution into the four square-root monomials, two separate monomials and
both endpoints of both supremum monomials proves N^(g+eta) T^(height+eta).
The accompanying checker verifies all ten norm and height powers exactly.

Fix 0<e<=1/100000 for the rest of the proof. Choose rho>0 ONCE, sufficiently
small in terms of e,d and the fixed polynomial height bounds, then choose the
loss in (4.1) sufficiently small. For all three thresholds and fixed twists,
the number of rows in U<=q_u<2U having a zero in Re s>=sigma_j, |Im s|<=4U^rho
is O(U^(g_j+e)). Denote these sets by E_j(U), j=0,1,2, in increasing threshold
order. They are nested. Primitive inducing functions are used for this zero
count; missing exterior Euler factors have no zero in Re s>0. Endpoints can
also be obtained by first moving the density threshold an arbitrarily small
amount left and spending part of e, if a zero-count convention uses strict
inequalities. This changes none of the following contour buffers.

For a row outside E_j and |t|<=2U^rho, consider log L on concentric disks about
2+it with radii

    R=2-sigma_j-e/4, r_o=2-sigma_j-e/2,
    r_t=2-sigma_j-e, r_i=1-e/4.

They are strictly ordered R>r_o>r_t>r_i>0 and lie in the zero-free rectangle
for large U. Polynomial growth and Borel--Caratheodory give O_e(log U) for
log L on r_o. On r_i the Euler logarithm is O_e(1). Three circles bounds
log L on r_t by O_e((log U)^theta), theta<1. Thus for EVERY later eta>0,

    |1/L_F^S(x+it,bar chi_u)| <<_(e,eta) U^eta,
    sigma_j+e <= x <= 1+e, |t|<=2U^rho.                          (4.2)

The exceptional sets and rho have already been fixed; they are not redefined
when eta shrinks. Inducing-character omissions, if present, cost U^eta by
bounding each large-prime (1-q^(-x))^(-1) by q^eta and absorbing finitely many
small primes. At x>1 use Euler convergence without a zero-free premise.

## 5. Scales, complete contours and the improved estimate

Take

    alpha=1/2+e, beta=1/2, h=1/2-e, M=1+e>1,
    C=1/3+e/3, b=2/3-e/3, z0=2/5.                              (5.1)

In (2.2) the theta exponent is 1/4+e, apart from an arbitrary loss.
The principal contour begins at (1+e,1+e,1/6+e). Move w to 1/2, taking its
residue at one. In that residue move z to e, taking its residue at 1/6.
The double residue is exactly c0 f_alpha. The other two pieces have exponents

    w-remainder: E(1+e,1/2,1/6+e)=1/12+11e/6-e^2;
    z-remainder: E(1+e,1,e)=1/4+2e-e^2.                         (5.2)

Every principal vertex and segment lies in (2.4). The only crossed principal
poles are w=1 and z=1/6. No nonprincipal no-pole assertion is used for this row.

For nonprincipal rows fix z=z0. On U<=Z^(1/100), keep x=1+e and move y to 1/2.
Individual convexity and the full count nu=1 give exponent

    E(1+e,1/2,z0)+(1/100)(1+1/4-z0)
         =417/2000+11e/10.                                  (5.3)

For Z^(1/100)<U<=Z^(h+e)=Z^(1/2), use four DISJOINT classes:

| class | x | y | nu | numerator bound |
|---|---|---|---|---|
| outside E_0 | 3/4+e | 1/2 | 1 | family mean (3.3) |
| E_0 minus E_1 | 21/25+e | 4/25+e | 8/11+e | convexity (3.4) |
| E_1 minus E_2 | 19/20+e | 1/20+e | 4919/8846+e | convexity (3.4) |
| E_2 | 1+e | e | 11/47+e | convexity; Euler reciprocal |

A middle class is COUNTED at the lower threshold and SHIFTED only past the
upper one. The good class has NO sparsity saving assigned. Start at
(1+e,1+e,z0), shift the truncated xi segment to x using (4.2), then move w to y.
For the last class do not shift xi. Every connecting segment lies in the convex
domain (2.4). These characters are nonprincipal, so w crosses no pole, and
z0>1/6 avoids its pole. The denominator has no crossed zero on the actual
truncated rectangle; no global zero-free property is presumed for it.

All U exponents in (3.3)/(3.4) are positive. At U=Z^(1/2), the four exact Z
exponents are respectively

    good:      1/4+11e/10;
    middle 0:  67/275+37e/20;
    middle 1:  85111/353840+37e/20;
    last:      11/94+37e/20.                                 (5.4)

Thus each is <=1/4+2e on the ENTIRE specified interval of e, not merely at a
numerical sample. The smallest constant middle-class margins are 7/1100 and
3349/353840. In particular the good estimate really uses the mean: replacing
it by individual convexity adds 1/8 to its constant Z exponent and fails.

Horizontal edges and original xi tails are retained. On shifted edges at
height U^rho, (4.2) holds; on original x=1+e tails Euler convergence holds.
The correction is bounded uniformly, and individual convexity suffices there.
By (2.5), integrating the w,z heights gives an arbitrary U^(-rho A) factor.
This does not replace an average over w-height by a supremum over individual
characters. Concretely, the finitely many real strips here have E<2 and
nu+(1-y)/2-z0<2, after choosing the small losses. Before the extra height decay
one may overbound the dyads by C Z^2 U^2. With U<=Z^(1/2) and U>Z^(1/100),
choose any fixed A>400/rho; then their total is O(Z^(-1)) after dyadic logs
(and increasing A slightly if necessary). The height polynomial degrees of
F and H are absorbed by first choosing the decay order in (2.5). This choice
changes an estimate, not the defining profiles.

For U>Z^(1/2) use the INITIAL integral x=y=4 and shift z right to

    L=10/e+2.

No pole is crossed. Absolute convergence gives U^(1-L+eta), not the false
convexity exponent (1-4)/2. The dyads sum geometrically. At the lower endpoint
the Z exponent, before arbitrary losses, is

    alpha/2+3+h L+3beta+(1/2)(1-L)
         =-19/4-3e/2.                                      (5.5)

The positive gap between h and 1/2 is exactly e. L is fixed once e is fixed.
There is no application of an endpoint M=1 estimate or uniformity as L tends
to infinity. Bounded U,Z are absorbed into fixed-data constants.

Choose all remaining arbitrary power losses (in (2.1), the reciprocal,
correction, mean, convexity, conversions from U, and dyadic logs) with combined
Z cost less than e. There are finitely many bounds, so this is possible after
rho and the three exceptional sets are fixed. Equations (5.2)--(5.5) and (5.3)
then give I=c0 f_alpha+O_e(Z^(1/4+3e)). The theta bound is stronger. Hence

    f_alpha(Z) <<_e Z^(1/4+3e).                              (5.6)

This is an estimate for the actual CT detector, not an assumed signed sum.

## 6. Zero exclusion and exact limiting quantifiers

The Mellin integral integral_0^infinity f_alpha(Z) Z^(b-s) dZ/Z is holomorphic
on Re s>b+1/4+3e=11/12+8e/3: (5.6) controls infinity and flatness controls zero.
Mellin/Fourier inversion on an original line Re s>1 identifies it with
exp((s-5/6)^2)H(s)/zeta_F^S(s). Meromorphic continuation and the nonvanishing of
H on Re s>2/3 exclude zeros there. The pole at one instead gives a removable
zero of this reciprocal expression.

For each point with Re s>11/12 choose one fixed e>0, e<=1/100000, with
8e/3<Re s-11/12. Its proof applies. The constants and profiles may depend on
e; no uniform limiting constant, zero census, or estimate on the boundary
line is required. This establishes the proposed strict half-plane for F.

For arbitrary K, F=K(mu_12) is abelian over K. Classical abelian factorization
writes zeta_F as zeta_K times entire nonprincipal Hecke factors. A zero of
zeta_K away from one would persist. For a finite-order character over K use
its cyclic class field L: zeta_L/zeta_K is a product of the nontrivial powers'
Hecke L-functions. Away from one all are entire. At one the ratio of positive
nonzero residues excludes a zero of any factor. Finite missing Euler factors
have zeros only on Re s=0. This is CT's unchanged descent, not a new general
Artin-holomorphy assertion.

## 7. The next barrier is not another density bin

The unchanged positive theta estimate alone supplies saving relative to C

    S_theta=C-(alpha+beta/2-1/2)
           =(1-alpha)/6-(M-1)/2.                             (7.1)

For beta<=alpha and M>1 one has alpha>1/2, hence S_theta<1/12. The limit of our
legal parameters reaches this ceiling. For beta>=alpha the correct additive
factor is 1/X; the theta saving is 2/3-alpha/6-beta and is again <1/12, since
beta>1/2 and alpha+beta>1. Thus merely swapping X,Y does not escape the cost.
This is a restriction of that PARTICULAR positive theta upper estimate, not
an arithmetic lower bound or a no-go theorem for a signed theta improvement.

The construction does not bound #955's fixed-principal-twist critical native
covariance. To advance further within this strategy one must improve a binding
source estimate or use cancellation before the theta/additive Cauchy step;
another equivalent critical energy or additional zero-density bins alone does
not achieve that. No proof of the full RH claim is asserted here.

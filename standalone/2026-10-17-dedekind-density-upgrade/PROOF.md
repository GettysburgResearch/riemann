# A sextic-density refinement of the Dedekind zero-free argument

Status: PROPOSED theorem and complete composition argument; independent
mathematical review is required. External theorems listed below are imported,
not proved by this packet's checker. No RH, GRH, or unknown native moment is
assumed. The claim is a stronger all-number-field boundary than CT v2, NOT an
improvement on the stronger previously reported special-case Riemann bound.

## 1. Statement and precisely imported mathematics

**Proposed theorem.** For every number field K,

    zeta_K(s) != 0 if Re(s)>23/24 and s!=1.                 (1)

For every finite-order Hecke character eta over K, the same region is zero-free,
with s=1 included when eta is nonprincipal. Constants in intermediate estimates
may depend on K and all fixed local data. There is no conductor/discriminant
uniformity or assertion at Re(s)=23/24. Infinite-order angular characters are
NOT included in this conclusion.

Inputs (full bibliographic and reading boundaries are in SOURCES.md):

* CT: Cureton--Thorner, Hexagon 2610.00200v2. We import the fixed general-field
  theta/reflection construction, the complete reflected moment in Section 9,
  the additive and three-variable Poisson identities in Sections 10--11, and
  the analytic correction domain. In particular, we use the proof's explicit
  allowance for ANY FIXED support exponent M>1, not its final fixed numerical
  theorem with new parameters substituted without justification.
* DF: de Faveri, arXiv:2610.04045v1, Theorem 1.1 and the zero-detector calculation
  in the proof of Corollary 1.5. Both indices of Theorem 1.1 are sixth-power-free.
* BGL: Blomer--Goldmakher--Louvel, arXiv:1112.1650, Theorem 1.3 and Section 5,
  especially the classical zero-detection inequality (5.3). Fixed-field Hecke
  continuation, functional equations, class-field factorization, and the
  elementary complex-analytic tools used below are also classical inputs.

The new composition consists of the exact character-family matching, the
fixed-S-unit-twist adapter, the rescaled estimate, and the strict rational
contour budget. We do not claim an independent reconstruction of the entire
metaplectic foundation or a formalization of (1).

It suffices first to work over F containing mu_12. Fix CT's local data S,
R=O_(F,S), Gamma=(R^*)^6, and its multiplicative allowed-generator section.
All ideal norms below are exterior norms; S-integer generators are always
modulo Gamma. Thus no infinite norm-only element ball is introduced.

## 2. Matching the actual Poisson denominator family

Write g(a) for an allowed generator of an exterior fractional ideal a, modulo
Gamma. CT Section 7.1 gives a subgroup B of the product of local sixth-power
classes at S: g(a) has class in B and is unique modulo Gamma. This section is
multiplicative. Every sixth-power-free Poisson representative can consequently
be written, modulo Gamma, as

    u = epsilon * g(a),    0<=v_p(a)<=5,                  (2)

where epsilon runs through the FIXED FINITE group R^*/(R^*)^6. Moreover q_u=Na,
not N(rad a). Replacing this indexing norm by conductor norm would be wrong.

Choose the data in DF Section 2.3 as follows. Take the same finite S, choose c
so deep that x=1 mod c is a local sixth power at every finite place in S, and
for each generator ideal E_0 of its finite ray quotient choose m_(E_0)=g(E_0).
These are legal choices in DF. The products m_E are again allowed. For the
DF decomposition a=(x)E h^6, choose an allowed generator g(h). Then

    x*m_E*g(h)^6

is a generator of a whose local class is in B: x is locally a sixth power
and B is a subgroup. Uniqueness implies that its ratio to g(a) lies in Gamma.
For an exterior ideal b coprime to a, DF's definition therefore gives EXACTLY

    chi_a^DF(b) = (x*m_E / b)_6 = (g(a) / b)_6.          (3)

The auxiliary h may be chosen coprime to b in that definition, so its sixth
power has symbol one. If (a,b)!=1, both characters have the original value zero.
The equality is of full zero-extended exterior ideal characters, not just
prime values away from an unrecorded set.

Let psi_epsilon(b)=(epsilon/b)_6. This is a finite-order Hecke character,
unramified outside the fixed S. Equations (2)--(3) imply

    chi_bullet(u) = psi_epsilon * chi_a^DF              (4)

outside S, with every nonunit zero retained. Thus the Poisson family is a
finite union of FIXED S-supported twists of DF's family. Omitting epsilon
would omit genuine rows. Complex conjugation in CT's denominator causes no
change to the number of zeros in a rectangle symmetric in imaginary part.
Passing between the exterior and inducing primitive L-functions only inserts
finite Euler factors with no zeros in Re(s)>0.

## 3. Why the density bound survives these fixed twists

Here is an explicit adapter, rather than an unsupported invocation of a
corollary for a different family. Fix one psi of order dividing six supported
at S. The arithmetic estimates in the proof of DF Corollary 1.5 remain valid
for psi*chi_a, uniformly over our fixed finite list:

(a) Every application of the sixth-power-free large sieve replaces a column
coefficient lambda_b by psi(b)lambda_b. Its absolute square mass is unchanged.
Row restrictions remain restrictions of nonnegative sums. Shared-prime zero
masks are unchanged; no extra independence or coprimality is inserted.

(b) The central second mean used in the detector remains

    sum_(Na<=N, a sixth-power-free) |L^S(1/2+it,psi*chi_a)|^2
           << (N*(1+|t|)^(d/2))^(1+epsilon),             (5)

where d=[F:Q]. This is the fixed-twist version of BGL Section 5's argument.
For clarity, decompose a=a_0*a_1 with a_0 squarefree, a_1 powerful and
(a_0,a_1)=1. The approximate functional equation has length
L<<N^(1/2+epsilon)(1+|t|)^(d/2+epsilon). For fixed a_1, the character chi_(a_1)
and psi multiply the column coefficients, and BGL's squarefree sieve gives

    (N/Na_1 + L + ((N/Na_1)*L)^(2/3)) (NL)^epsilon.

The sum over powerful a_1 is O(N+L*sqrt(N)+(NL)^(2/3)), since powerful ideals
have count O(sqrt x), and their reciprocal powers 1 and 2/3 are summable.
This is at most the right side of (5). To retain the complete AFE, decompose
its column index into a squarefree and a powerful part; after moving its
separating Mellin line by an arbitrarily small positive amount, the latter
has summable weight (Nb_1)^(-1/2-epsilon). The S-supported factors have a
convergent fixed-prime product. Triangle/Minkowski treats their row factors
of modulus at most one. This is precisely the complete-column operation in
BGL (5.1), not a substitution of a squarefree L-function.

(c) The unrestricted detector polynomials also retain their estimate. Write
b=b_0*b_1 with b_0 squarefree, b_1 powerful and (b_0,b_1)=1. For fixed b_1,
its character value is a row multiplier of modulus at most one. Minkowski
and the sixth-power-free sieve bound the complete norm-L polynomial by

    (NL)^epsilon * L * [N+L+N^(5/6)L^(1/3)+N^(1/3)L^(5/6)].

Indeed the root sum in b_1 costs at most
sum_(Nb_1<=2L, powerful)(Nb_1)^(-1/2)=O(log(3L)); this is absorbed in epsilon.
The norm of the coefficient vector for b_0 is O(L/Nb_1) times a subpower
factor. This argument keeps overlapping factors and original zero values.

Apply the classical zero-detecting inequality BGL (5.3) to the exterior
L-function and its ordinary Mobius mollifier. The product coefficients are
independent of a; psi merely supplies a column phase. Its two terms use (5)
and (a)--(c). With mollifier cutoff A and detector cutoff B, 1<=A<=B, DF's
proof therefore supplies the following SAME inequality for the fixed twist:

    sum_(Na<=N)^flat N_psi(sigma,T,a)
    << (NTB)^epsilon T * {
       B^(1/2-sigma)*(N*T^(d/2))^(1/2)
          *(A+N+A^(1/3)N^(5/6)+A^(5/6)N^(1/3))^(1/2)
       +B^(2-2sigma)+N*A^(1-2sigma)
       +sup_(A<=V<=B) V^(1-2sigma)
           *(N^(1/3)V^(5/6)+N^(5/6)V^(1/3)) }.          (6)

Here flat still means sixth-power-free. Principal exceptions at a=1 are
irrelevant to the dyads N>=2; they can be omitted. BGL's analytic detection
lemma, not a claim that finite arithmetic checks prove it, is an explicit
import. The discussion above supplies its new-family arithmetic adapters.

Take the exact values

    sigma_0=41/50,
    A=N^(6475/8534),
    B=N^(5900/4267) * T^(25d/68).                        (7)

A direct rational substitution in EVERY term of (6), including both endpoints
of the supremum, gives

    sum_(Na<=N)^flat N_psi(41/50,T,a)
       << N^(2563/4267+epsilon) T^(1+9d/68+epsilon).     (8)

This also agrees with DF's displayed Corollary 1.5. No numerical optimizer is
an input to (8). The identity 2563/4267 < 601/1000 has a strict rational gap.

Let lambda=601/1000, g=2563/4267, H_d=1+9d/68, and let A_F be a fixed
polynomial height exponent for the L-functions on our strips. Choose ONCE

    eta=(lambda-g)/16,
    0<rho<=min(10^(-6),(lambda-g)/(16*(1+H_d+A_F))).      (9)

Use the arbitrary loss in (8) with eta. On U<=q_u<2U, (4), (8), and
T=4U^rho imply that the exceptional set of nonprincipal denominators having
a zero at Re(s)>=41/50, |Im(s)|<=4U^rho has size O(U^lambda). Constants may
depend on the finite unit group. The exceptional sets are fixed independently
of all later contour losses. No denominator is declared zero-free a priori.

For a nonexceptional primitive character take an analytic logarithm on the
disk centered at 2+it, |t|<=2U^rho, of radius 1.17995. The disk lies strictly
in the above zero-free rectangle for large U. Convexity and
Borel--Caratheodory bound log L by O(log U) on radius 1.179925. The Euler
logarithm is O(1) on radius .999. Three circles gives O((log U)^theta),
theta<1, on radius 1.1799. These last disks reach x_g=.8201. Absolute
convergence covers their right-hand complement. The omitted finite Euler
factors cost U^epsilon. Thus, for EVERY epsilon>0,

    1/L^S(x+it,bar(chi_bullet(u))) << U^epsilon,
          x>=8201/10000, |t|<=2U^rho,                   (10)

with an epsilon-dependent threshold but the SAME exceptional set.

## 4. The rescaled theta bound: no new moment hypothesis

Set

    alpha=11/20, beta=103/200, h=1-alpha=9/20,
    X=Z^alpha, Y=Z^beta, M=alpha+beta=213/200>1.         (11)

In particular beta<alpha. These are changed scales in CT's actual I(X,Y,Z),
not an assumed bound for the fixed-twist native moment from #955.

CT Section 9's complete reflected estimate on a powerful/squarefree dyad is
P^(1/2)(D+D^2 P/Z) times Z^epsilon, with PD<<Z^M. Therefore each dyad costs
O(Z^(2M-1+epsilon)): P^(1/2)D<=Z^M<=Z^(2M-1), and
P^(3/2)D^2/Z<=(PD)^2/Z<=Z^(2M-1). Its proof explicitly treats arbitrary
fixed M>1 by increasing decay orders of the same profiles. The coprimality
restrictions and all higher powers remain. This is an imported analytic
moment estimate with its verified scale hypothesis, not a conjectural one.

The fixed additive factor has squared norm O(1/Y+1/X)=O(1/Y), by CT's
unrescaled additive identity. Cauchy and compact quotient integration give

    |I(Z^alpha,Z^beta,Z)|
       << Z^(alpha+beta/2-1/2+epsilon)
        = Z^(123/400+epsilon).                         (12)

The arithmetic coefficients, local character vartheta, and weights have NOT
been changed. In particular, the angular vartheta never enters (8).

## 5. All contour ranges and exact margins

CT's Poisson integrand contains the unchanged scale monomial
X^(1/2-z) Z^(xi+z-1) Y^(w-1). Thus its Z-exponent is

    E(x,y,z)=alpha/2+x-1+h*z+beta*(y-1).                 (13)

At the principal residues w=1,z=1/6 its exponent is s-b, where

    C=alpha/2+h/6=7/20,     b=1-C=13/20.               (14)

The shift is NOT the old 61/100. Define the actual principal detector by

    f_new(Z)=(1/(2pi i)) int_(2)
          Z^(s-13/20) exp((s-5/6)^2) H(s)/zeta_F^S(s) ds. (15)

H is exactly CT's principal numerator. We import its nonvanishing in
Re(s)>2/3; neither H nor vartheta has been retuned.

For reference the CT correction domain is the intersection of the strict
linear inequalities

    x>0, y>0, z>0, 6z+y>1, x+6z>1, x+y>1,
    x+y+6z>2, 6x+6z>5, x>1/2, 3x>2, 3x+y>5/2.        (16)

Set delta=10^(-7), x_1=1+delta, y_0=181/1000, z_0=2/5.
The nonprincipal low corner is (x_g,y_0,z_0). In particular x_g+y_0=1.0011,
so it has a real, strictly positive margin. Every vertex and axis-aligned
segment used below lies in (16); the domain is convex. The checker evaluates
all vertices, not merely the final exponent.

Principal row: move to (x_1,x_1,1/6+delta); next move w to .9, taking its
residue at one; in that residue move z to .05, taking the residue at 1/6.
The two remainders have corners (x_1,.9,1/6+delta) and (x_1,1,.05).
The double residue is c_0 f_new with the same nonzero
c_0=(Res_(s=1) zeta_F^S(s))^2 M(1/6) W1_hat(1)/6.

Nonprincipal rows: put s_0=1/10 and a_0=45001/100000=h+10^(-5).
For U<=Z^s_0 keep x=x_1. For Z^s_0<U<=Z^a_0 use x=x_1 on the exceptional
set and x=x_g on |Im xi|<=U^rho for every good row. Move xi, then z, then w
to the indicated corners, retaining the original x_1 tails. The numerator
Hecke character is nonprincipal, so moving w crosses no pole; z_0>1/6.
The denominator movement is licensed only by (10).

A set with O(U^nu) rows costs

    Z^E(x,y_0,z_0) U^(nu+(1-y_0)/2-z_0+epsilon).        (17)

Use nu=1 for the small and good sets and nu=lambda for the exceptional set.
All these U exponents are positive, so the upper endpoints of their ranges
supply upper bounds. Relative to C=7/20 the exact savings are:

| Contribution | Exact saving before discretionary power losses |
|---|---:|
| Theta bound | 17/400 |
| Principal w remainder | 10299971/200000000 |
| Principal z remainder | 524999/10000000 |
| Small frequencies | 2158349/10000000 |
| Exceptional intermediate frequencies | 8410759/200000000 |
| Good central integrals | 8479981/200000000 |
| Large frequencies | 507999/100000 |

The horizontal segments and the discarded x_1 tails have the same estimate
as (17), with nu=1 and an extra U^(-rho A_1) for any fixed desired A_1.
This follows from the fixed Mellin weights: Gaussian decay in Im(xi+z),
arbitrarily rapid z and w decay, and polynomial L-height growth. On the
segments (10) applies; on the original tails x_1>1 suffices. Since
U>Z^(1/10), choosing A_1 sufficiently large makes this contribution smaller
than any prescribed power of Z. This chooses a seminorm of fixed weights,
not different weights for different scales.

For U>Z^a_0 return to the initial integral and move only z to L=10^6, with
x=y=4. Absolute convergence gives

    Z^E(4,4,L) U^(1-L+epsilon).

Its geometrically summed saving is the last table entry. The strict gap
a_0-h is essential; setting it to zero would invalidate this bound.

Let m_* = 8410759/200000000 be the least Poisson saving. Exactly,

    m_* - 1/10000 > 1/24,      17/400 > 1/24.           (18)

The quantities hidden in U^epsilon, the finite dyadic logarithms, and the
height integrations involve only finitely many such losses. Choose them so
their TOTAL Z-power cost is <1/10000. This is legitimate because rho, the
exceptional sets, the field and the weights were fixed first. Increase the
threshold so all intermediate dyads satisfy (10). Bounded Z is absorbed.
Equations (12), (15)--(18), with theta loss also <1/10000, give

    I = c_0 f_new + O(Z^(C-m_*+1/10000)),
    f_new(Z) << Z^(C-1/24)=Z^(37/120), Z>=2.            (19)

This is a bound for the ACTUAL signed principal detector, not an extra
hypothesis about it and not an average over target twists. All principal,
nonprincipal, small, exceptional, good, horizontal, and large terms have been
accounted for. The previous signed-injection estimates are not inputs.

## 6. Excluding poles and descending

For Z<=1 the contour in (15) can be moved arbitrarily far right, where H
and 1/zeta_F^S have absolutely convergent bounded Euler products; hence
f_new is flat at zero after the fixed power normalization. The Gaussian
controls vertical ends. Together with (19), the Mellin integral

    int_0^infinity f_new(Z) Z^(-s+13/20) dZ/Z

is holomorphic for Re(s)>13/20+37/120=23/24. Ordinary Mellin/Fourier inversion
identifies it with exp((s-5/6)^2)H(s)/zeta_F^S(s) initially to the right of one.
Uniqueness of meromorphic continuation extends the identity to the proposed
region. Since its numerator has no zeros there, a zero of zeta_F^S would
produce a genuine pole, impossible for this holomorphic integral. Removed
Euler factors have zeros only on Re(s)=0. This proves (1) for F containing
mu_12; s=1 is its pole, not a zero.

For an arbitrary number field K take F=K(mu_12). The extension F/K is abelian.
Class-field factorization writes zeta_F=zeta_K times a finite product of
nonprincipal Hecke L-functions, all entire. Thus no zero of zeta_K away from
one can be canceled in that product. This proves (1) for every K.

Finally a finite-order Hecke character eta is a character of a finite abelian
class field E/K. Applying (1) to E and using the corresponding factorization
of zeta_E excludes zeros of L(s,eta) in the same region away from one. The
classical nonvanishing of nonprincipal Hecke L-functions at one covers that
point; the principal function has a pole. No higher-dimensional Artin
holomorphy or infinite-order Hecke zero-free theorem is used. QED, subject to
independent verification of this composition and its stated imported inputs.

## 7. Scope of the gain and what is still missing

The claimed improvement is 31/32 -> 23/24 for ALL number fields: the excluded
width increases from 1/32 to 1/24. It does not improve the stronger 7/8 result
already reported for ordinary zeta/special families, does not prove RH, and
does not settle the critical fixed-center native covariance in #955.

No claim of exhaustive literature priority is made. The new theorem is a
synthesis of strong external unconditional results, not an independent new
large sieve or a re-proof of the theta foundation. This packet should be
reviewed first at the family adapter in Sections 2--3, then the scale change
in Section 4, and only then the rational margins. Arithmetic certification
of the margin table cannot validate an incorrect analytic adapter.

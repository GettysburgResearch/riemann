# Primitive finite twists of cubic Type-I sums

Date: 20 October 2026. **Proposed source-dependent analytic proof for review.**
The transfer theorem below is conditional on its stated Hecke zero-free
input. Substitution of Liu's preprint theorem is an imported dependency,
not an independent verification of that theorem. No new zero-free
half-plane is proved. The finite checker does not certify this proof.

## 1. Statement and conventions

Use Dunn--Radziwill [DR], v3, with E=Q(omega), O=Z[omega], lambda=sqrt(-3),
N(a)=|a|^2, alpha(a)=a/|a|, and their normalized cubic Gauss sum g_tilde(a).
Sums and divisors use primary generators a=1 mod 3; the prime above 3 is
excluded. The literal identities are

    |g_tilde(a)| = mu_E(a)^2,
    g_tilde(ab) = g_tilde(a) g_tilde(b) conjugate((a/b)_3).       (1)

Their zero extensions include noncoprime a,b. Fix an integer ell. Let c be
squarefree, primary, and coprime to 3, and let psi be a primitive
multiplicative character modulo c, extended by zero at nonunits. Modulus
one is permitted. Put kappa_c=(./c)_3. Split c=c0*c1 into coprime factors:
a prime divides c0 exactly when psi_p*kappa_p is principal; all other
primes divide c1. Write Cj=N(cj) and K=C0*C1^2. This split depends on the
actual local character, not merely its order or conductor size.

For 1/2 <= beta < 1, assume H_beta(ell): every Hecke function actually
needed below, with character psi^3 alpha^(3ell), has no zero in Re(z)>beta.
For a conductor-uniform theorem this is a common half-plane across the
allowed psi, with fixed E and ell. The standard uniform polynomial growth
of these fixed-degree Hecke functions is also used. Constants are not
required to be uniform in a growing ell. A possible principal pole is
permitted. Define

    p = (2 beta+1)/6,        q = (5-2 beta)/12 = (1-p)/2.

**Theorem T.** For a fixed smooth W with compact support in (0,infinity),
X>=1, and every epsilon>0,

    sum_u g_tilde(u) psi(u) alpha(u)^ell W(Nu/X)
       = P_psi,ell(X) + O_{W,ell,beta,epsilon}(
               (X Nc)^epsilon X^p C0^q C1^(2q)).              (2)

The main term vanishes if ell!=0 or c1!=1. In the remaining case
psi=conjugate(kappa_c), ell=0, it is the inherited residue

    P_psi,0(X) = c_E W_hat(5/6) X^(5/6)
                conjugate(g(c)) phi_E(c)
                / ((Nc)^(5/3) L^(3c)(2,1)),                  (3)

where c_E=(2 pi)^(5/3)/(3^(7/2) Gamma(2/3)). The notation L^(3c)
means that all primes dividing 3c are omitted, including when psi^3 has
smaller primitive conductor. No prime-power conductor extension is asserted.

At ell=0, H_beta is a finite-order Hecke input: Liu's stated theorem gives
beta=B_flat. In particular the finite-twist result does NOT require the
candidate infinite-order extension in PR #1009. When psi^6=1, psi^3 is
quadratic or principal, so even the zero-free input can be restricted to
that subfamily. For ell!=0 the corresponding angular Hecke input must be
supplied separately; no finite-order theorem is silently substituted.

## 2. Exact finite transform, including all zero frequencies

[DR, (5.21)--(5.23)] supplies the finite transform underlying the general
periodic-twist functional equation. Set

    tau(psi) = sum_{x mod c} psi(x) e_check(x/c).

Primitivity and a unit substitution give, including nonunit d,

    psi_hat(d) = tau(psi) conjugate(psi(d)).

In the source transform the congruence is lambda^8*a*d=1 mod c. Hence
conjugate(psi(d))=psi(lambda^8)*psi(a), and exactly

    psi_tilde(v) = kappa_c(lambda) psi(lambda^8) tau(psi)
                  sum_{a mod c} (psi*kappa_c)(a) e_check(av/c). (4)

All characters in (4) are zero-extended. This formula is not a claim that
psi*kappa_c is primitive at every prime: that distinction is essential.

The Chinese remainder theorem separates the sum into local transforms;
its additive rescalings have unit modulus on the character factors. At a
prime of norm Q dividing c0 the inner local sum is a Ramanujan sum, equal
to Q-1 at zero and -1 at nonzero frequencies. At a prime dividing c1 it
is a primitive Gauss transform, of modulus sqrt(Q) on units and zero
otherwise. Since |tau(psi)|=sqrt(Nc),

    |psi_tilde(v)| = C0^(1/2) C1 |c_{c0}(v)| 1_{(v,c1)=1}.    (5)

Here c_{c0} is the ordinary ideal Ramanujan sum. In particular
psi_tilde(0)=0 whenever c1!=1. [DR, Proposition 5.1] therefore has no
residue for these twists even when ell=0. For ell!=0 the same proposition
already has no residue.

A local nonmatching prime gives |psi_tilde(1)|^2=Q^2, while a matching
prime gives Q. Thus replacing C1 by sqrt(C1) in the dual absolute bound
would be false already at one prime. This is a local fact, not a lower
bound saying that the final convexity estimate cannot be improved by
additional cancellation.

## 3. The cubic completion changes to psi^3

Define

    R_psi,ell(s) = sum_u g_tilde(u) psi(u) alpha(u)^ell (Nu)^(-s),
    Q_psi,ell(s) = L^(3c)(3s-1/2,psi^3 alpha^(3ell)) R_psi,ell(s).

[DR, Lemma 5.4] is stated for cubic psi. We do not apply that statement
to a quadratic or sextic character. Instead use its displayed coefficient
formula before the cubic specialization: on the selected source support,

    mu = lambda^(-3) a b^3,  a squarefree,
    conjugate(tau_theta(mu)) = 3^(5/2) g_tilde(a) (Nb)^(1/2).

The factors of b in the twist are now psi(b)^3 alpha(b)^(3ell).
Summing over b gives L^(3c)(3s-1/2,psi^3 alpha^(3ell)), not a principal
L-function unless psi^3 is principal. Equivalently, cube-divisor inversion
has local coefficient

    sum_{d|b} mu_E(d) psi(d)^3 psi(b/d)^3
       = psi(b)^3 1_{b=1}

when b is coprime to c; when it is not, the original zero extensions
annihilate the relevant terms. The angular factors behave identically.
There is no coprimality assumption between the squarefree a and b.

The exact normalization is

    Q_psi,ell(s) = (-1)^ell i^ell psi(lambda)^(-1)
                  3^(-5/2-3s) D(s,bar F1;psi,ell)_S.         (6)

This identity holds first by absolute convergence and then by meromorphic
continuation. It licenses [DR, Proposition 5.1], whose periodic-twist
statement does not require psi to be cubic. Its only possible pole is
5/6 with residue proportional to psi_tilde(0). If c1=1, (4) becomes the
source Ramanujan case and (6) gives (3) after removing the completion.

## 4. Absolute bound for the actual dual coefficients

Use the dual coefficients in [DR, (5.73)--(5.74)], BEFORE the extra cubic
Möbius inversion used for the source's special level theorem. They are
supported on

    mu = lambda^k zeta a b^3,  k>=-4,  zeta in O^*,
    a squarefree and a,b primary,

and satisfy

    |a_star(mu)| << 3^(k/6) (Nb)^(1/2).                      (7)

Indeed the source's three disjoint branches reduce to normalized Gauss
moduli on the squarefree part; (5.7), (5.13), and (5.14) give (7), with
an absolute constant also covering k=-4. The angular factor has modulus
one. The ramified k-sum at Re(s)=1+eta is a convergent geometric series;
the six units contribute only a constant.

Combine (5) and (7). At a prime of norm Q dividing c1 only exponent zero
in a and b survives. At a prime dividing c0, write the exponent of a as
e in {0,1} and that of b as j>=0. The Ramanujan factor has modulus one
when e=j=0 and Q-1 otherwise. Its entire local majorant is

    F_Q(s) = 1+(Q-1)Q^(-s)
           +(Q-1)(1+Q^(-s)) Q^(1/2-3s)/(1-Q^(1/2-3s)).     (8)

For real s>=1 it is decreasing, and exact simplification gives

    F_Q(1) = 2 - Q(sqrt(Q)-1)/(Q^(5/2)-1) < 2.              (9)

All primes outside c are bounded by zeta_E(s) zeta_E(3s-1/2). Thus,
for eta,epsilon>0,

    sum_{mu!=0} |a_star(mu) psi_tilde(lambda^4 mu)|
                        / (Nmu)^(1+eta)
        <<_{eta,epsilon} C0^(1/2+epsilon) C1.               (10)

The factor 2^omega(c0) is absorbed into C0^epsilon by separating a fixed
finite set of small primes. Every cube power, common prime, ramified
branch and nonunit zero has been accounted for. This argument uses an
absolute dual bound; it does not assume cancellation in its coefficients.

## 5. Functional equation and the effective level

The source's general functional equation, [DR, (5.48)], multiplies the
left completed series by 3*(-1)^ell*(Nc)^(2s)*(bar c/c)^ell and reflects
to the dual series with psi_tilde. After removing the common gamma
factors the height multiplier is, up to fixed phases and fixed bases,

    Gamma(5/6+|ell|/2-s) Gamma(7/6+|ell|/2-s)
    / [Gamma(s+|ell|/2-1/6) Gamma(s+|ell|/2+1/6)].

On Re(s)=-eta its modulus is O_ell,eta((1+|Im s|)^(2+4eta)). The right
line Re(s)=1+eta is absolutely convergent uniformly in c,psi. Using (10)
on the left gives

    Q_psi,ell(-eta+it)
       << C0^(1/2) C1 (Nc)^(2eta+epsilon) (1+|t|)^(2+4eta).

If a pole is present, first multiply by (s-5/6)/(s+2). The Mellin
continuation in [DR, (5.49)--(5.52)] supplies finite exponential vertical
growth. Applying strip Phragmen--Lindelof to this pole-cleared function
with a fixed polynomial height divisor yields, on closed substrips,

    |Q_psi,ell(s)| << C0^((1-sigma)/2+O(eta)+epsilon)
                       C1^(1-sigma+O(eta)+epsilon)
                       (1+|t|)^A,                         (11)

away from the possible pole. The constants and finite A are independent
of c,psi for fixed ell,eta. For example, before letting eta decrease,
the C0 exponent from boundary interpolation is
(1+eta-sigma)/(2(1+2eta)), and the C1 exponent is twice this, plus the
explicit O(eta) contributions from (Nc)^(2eta). The effective level is
therefore K=C0*C1^2, not Nc alone.

## 6. A common zero-free half-plane gives a uniform reciprocal bound

We require more than a bound with unspecified dependence on each psi.
For every fixed delta,epsilon>0, H_beta(ell) implies

    |1/L^(3c)(z,psi^3 alpha^(3ell))|
       <<_{delta,epsilon,ell} [Nc*(2+|Im z|)]^epsilon,
             Re(z)>=beta+delta.                           (12)

Here is a proof of the uniformity used in (12). For a nonprincipal
primitive inducing character, fix the analytic logarithm by its Euler
series to the right of 1. Uniform polynomial growth of the fixed-degree
Hecke function, Borel--Caratheodory on zero-free disks, and a fixed chain
of overlapping disks from 2+it to beta+delta/2+it give

    |log L(s)| <<_delta log(2+Nc*(2+|Im s|))

on a slightly narrower closed half-plane. All disks stay a fixed distance
from beta, and their number is fixed independent of the conductor and
height. A disk centered at 2+it may be chosen to reach the desired left
edge while staying inside the zero-free half-plane, so the branch and its
value at the center are controlled by the Euler series.

For explicit subpower control choose a=beta+delta/2 and b=1+delta/2
(with a smaller delta if necessary). The Euler logarithm is bounded on
Re(s)=b. For a target height t0 apply three-lines to

    exp((s-it0)^2) log L(s)

on [a,b]. The left boundary supremum is O(log(2+Nc*(2+|t0|))) and the
right is O(1): the Gaussian absorbs the growth at other heights. At every
sigma>=beta+delta below b this gives

    |log L(sigma+it0)| << (log(2+Nc*(2+|t0|)))^theta,
       theta=(b-sigma)/(b-a)<1.

Exponentiation bounds both L and 1/L by any prescribed positive power
of the analytic conductor. On sigma>=b use Euler products directly.
For the principal primitive character there is just the fixed E zeta
function: remove its pole using (z-1)/(z+1), repeat the argument and
restore the reciprocal, which is regular at z=1. Finally the omitted
local factors cost

    product_{p|3c} (1-(Np)^(-beta-delta))^(-1) << (Nc)^epsilon.

This also handles a drop in conductor of psi^3. The fixed bounded
3-part and the fixed angular order change constants only. This proves
(12); a zero-free premise for one isolated character without a common
family half-plane would not justify the uniform assertion.

## 7. Mellin inversion and the estimate

In Re(s)>1 the sum in (2) is the integral of
R_psi,ell(s) W_hat(s) X^s. Move the contour to sigma=p+delta with a
small fixed delta>0. Then

    Re(3s-1/2) = beta+3delta.

Equations (6), (12), and the source pole statement show that no pole is
crossed except the one already included in (3). The possible pole of
the completion at 3s-1/2=1 makes its reciprocal zero, not singular.
The quotient cannot introduce any other pole in this strip under H_beta.
Equations (11)--(12) and rapid Mellin decay give (2) after choosing eta,
delta and intermediate divisor losses sufficiently small relative to the
final epsilon. Horizontal segments tend to zero. Multiplication of W(x)
by x^(it0) costs only a fixed polynomial in 1+|t0| via Mellin shifts and
finitely many integrations by parts. No moving angular cutoff is covered.

## 8. Zero-only masks and coherent short-divisor marks

Assume c1!=1 or ell!=0, so there is no main term. Inserting 1_{(u,m)=1}
into (2) costs only (Nm)^epsilon. Remove primes of m already dividing c,
then use exact divisor inclusion-exclusion. For squarefree d|rad(m),
write u=dv and use (1). The new character is psi*conjugate(kappa_d)
modulo cd; it is primitive, with matching part c0*d and nonmatching
part c1. Its cube is the old psi^3 with extra omitted Euler factors.
The scale and level cost for this divisor is

    (X/Nd)^p (C0 Nd)^q C1^(2q)
      = X^p C0^q C1^(2q) (Nd)^(q-p),
    q-p = (1-2 beta)/4 <= 0.                               (13)

Hence the divisor sum is subpower. If X/Nd<1, compact support makes the
sum empty below a fixed positive scale; the remaining bounded scales
are absorbed by the same estimate with a W-dependent constant.
This proves the mask assertion without deleting shared primes by fiat.

Let |b_v|<=1, A,B>=1, and W_A,W_B be fixed smooth annular weights. Then

    T = sum_{u,v} b_v g_tilde(uv) psi(uv) alpha(uv)^ell
               W_A(Nu/A) W_B(Nv/B) 1_{(uv,m)=1}

satisfies

    |T| << (AB Nc Nm)^epsilon A^p B^(1+q) C0^q C1^(2q).     (14)

Indeed only squarefree v coprime to cm survive. For each such v, (1)
turns the inner sum into a scalar of modulus at most |W_B(Nv/B)| times
a sum with character psi*conjugate(kappa_v), matching part c0*v and
unchanged c1. Equation (2) and the mask bound apply. Summing its error
absolutely over O(B) ideals proves (14). All original u,v common-prime
zeros remain in that exact transformation. A bounded coherent Mobius
mark is allowed by choosing b_v=mu_E(v) times a bounded coefficient.
The nonresonance condition is preserved at every step. A fixed joint smooth
weight W(Nu/A,Nv/B) on a compact product annulus is also permitted:
freeze Nv/B and apply the same estimate with its uniformly bounded
finite collection of first-variable test seminorms.

## 9. Sixth-order specialization and limits

At a prime where sixth-order characters exist, write kappa_c=kappa6^2
and psi=kappa6^e. For primitive local e=1,...,5:

| e | e+2 mod 6 (dual) | 3e mod 6 (completion) | part |
|---|---|---|---|
| 1 | 3 | 3 | c1 |
| 2 | 4 | 0 | c1 |
| 3 | 5 | 3 | c1 |
| 4 | 0 | 0 | c0 |
| 5 | 1 | 3 | c1 |

In particular a nontrivial quadratic twist of the matched cubic
character moves that prime from c0 to c1, kills the zero frequency,
and doubles its exponent in the effective level. This handles an actual
quadratic-twisted cubic block, but does not supply a full mixed moment.
General number fields, nonsquarefree primitive conductors, arbitrary
row-dependent profiles, and complete sixth-free-row operator norms are
not claims of Theorem T. See MIXED_SCOPE.md for the remaining gap.

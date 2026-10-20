# Two different large sieves in one cubic functional equation

**Status:** proposed complete component arguments for review. The external
functional equation and large sieves are imported theorems, not proved by
our finite checker. Section 7 additionally imports a common Hecke
zero-free input. This is not a new zero-free theorem.

## 1. Exact families and statements

Let E=Q(omega), O=Z[omega], lambda=sqrt(-3), and N be the ideal norm.
Use the primary generator congruent to 1 modulo 3 and the normalized
cubic Gauss sum g_tilde of Dunn--Radziwill [DR]. The prime above 3 is
omitted in their original series. Varying moduli below are prime to 6.
All multiplicative characters retain their zero values at nonunits.

For a squarefree primary c prime to 6 put

    chi_c(a)=(a/c)_6,  theta_c(a)=(a/c)_2,  kappa_c(a)=(a/c)_3.

The compatible residue-symbol conventions give

    chi_c=theta_c*conjugate(kappa_c),
    chi_c*kappa_c=theta_c,  chi_c^3=theta_c.               (1)

Let f be squarefree and prime to 3, and let psi_f be any primitive
character modulo f, including f=1. The factor above 2 is permitted:
its finitely many local characters are separated as fixed local data
before applying the sieves. This also licenses the matching factor at
2 introduced by a divisor mark or coprimality mask. Partition f=f0*f1: a prime belongs
to f0 exactly when psi_f,p*kappa_p is principal. Put

    F0=Nf0, F1=Nf1, F=F0 F1, K=F0 F1^2.

Our row family consists of all squarefree c with C<Nc<=2C, c>1,
(c,6f)=1, for C>=1. It may be restricted further by a bounded nonnegative
row weight. Set psi_(f,c)=psi_f*chi_c, a primitive character modulo fc.
The parameter f is fixed within one average, but constants below are
uniform in f, psi_f and C. The finite ray conventions at 2 and 3 are
fixed before these parameters vary.

Define

    R_(f,c)(s)=sum_a g_tilde(a) psi_(f,c)(a) (Na)^(-s),
    Q_(f,c)(s)=L^(3fc)(3s-1/2,psi_f^3 theta_c) R_(f,c)(s),

where L^(3fc) omits all Euler factors at 3fc, including primes where the
primitive inducing conductor of the cubed character drops. For
4/9<=sigma<=1/2 put

    H_sigma(K,C)=max(
      K^(1-3sigma/2) C^(2-7sigma/4),
      K^(1-12sigma/11) C^(2-20sigma/11),
      K^(1-sigma) C^(2-2sigma)).                         (2)

**Theorem A (completed-series conductor mean).** For epsilon>0,

    sum_c |Q_(f,c)(sigma+it)|^2
      <<_epsilon (FC)^epsilon (1+|t|)^A H_sigma(K,C).    (3)

The order A is finite and independent of f,c,t. On the closed indicated
sigma interval it can be chosen uniformly. Constants may depend on the
fixed field, ray conventions and epsilon. No zero-free hypothesis is
used in (3).

**Theorem B (smooth Gauss sums).** Suppose 5/6<=beta<1 is a common
zero-free boundary for every finite-order Hecke function needed in the
completion above. Put p=(2 beta+1)/6. For W in C_c^infinity((0,infinity))
and X>=1,

    S_(f,c)(X)=sum_a g_tilde(a) psi_(f,c)(a) W(Na/X)

satisfies

    sum_c |S_(f,c)(X)|^2
      <<_(W,beta,epsilon) (XFC)^epsilon X^(2p) H_p(K,C). (4)

The absence of a residue is part of the proof; it is not an omitted
main term. Multiplying W(x) by x^(it0) costs a fixed polynomial in
1+|t0|. Finite collections of derivatives of a common compact smooth
profile obey the same statement. We do not assert arbitrary independently
chosen arithmetic coefficients in different rows, or a varying angular
weight. Joint complex conjugation of the Gauss coefficient and character
preserves the estimates.

## 2. Source contracts and the actual character switch

We import [DR], Proposition 5.1 and equations (5.21)--(5.23), (5.48),
(5.73)--(5.74), together with its theta coefficients (5.7), (5.13)--(5.14).
No GRH-dependent prime or dispersion result is used.

The two large-sieve inputs, for arbitrary squarefree-supported column
coefficients z_a, are

    sum_(c sf,Nc<=2C) |sum_(Na<=M,a sf) z_a chi_c(a)|^2
      << (CM)^epsilon Delta_6(C,M) sum_a |z_a|^2,
    Delta_6(C,M)=C+M+C^(5/6)M^(1/3)+C^(1/3)M^(5/6),     (5)

and the same statement for theta_c with Delta_2(C,M)=C+M.
The sextic input is de Faveri [DF], Theorem 1.1; the quadratic input
is Goldmakher--Louvel [GL], Theorem 1.1. These are squared operator
norms. Lengths are ideal norms, not Euclidean radii.

Here is how the symbols fit their Hecke-family formulations. Primary
generators are multiplicative. Reciprocity interchanges (a/c)_j and
(c/a)_j up to a factor on a fixed finite ray quotient supported at 2,3.
Partition the two indices into those finitely many classes, apply the
Hecke-family inequality, and use Cauchy over the finite partition. The
bad-prime conductor is fixed, not f-dependent. In particular the explicit
sextic-symbol inequality is also recorded in Xu--Sang [XS], (1.2), for
the same Eisenstein family. Passing to the cube of that family gives
the quadratic family of [GL, Remark 3]. Column restrictions at primes
of f multiply z_a by a bounded fixed coefficient; (c,f)=1 is a positive
row restriction. Thus enlarging the fixed bad-prime set to include f,
with an uncontrolled f-dependent constant, is unnecessary and is NOT
what we do.

The original Fourier series permits a factor above 2 in its indices.
Before (5), split the squarefree part into its two possible valuations
there, and retain every power of 2 in the cube part. The former gives
finitely many row multipliers and the latter a convergent geometric
resource in the estimates below. The prime above 3 is treated explicitly
on the dual side in Section 4. No growing excluded-prime set is hidden.

For a primitive finite character psi modulo squarefree r, direct
substitution in [DR, (5.21)--(5.23)] gives

    psi_tilde(v)=kappa_r(lambda) psi(lambda^8) tau(psi)
                sum_(a mod r) (psi*kappa_r)(a) e_check(av/r). (6)

This is the finite identity proved in #1010, not an assumption that
psi*kappa_r is primitive at every prime. Apply it to r=fc. At f0 the
inner sum is Ramanujan; at f1 it is a primitive character Gauss transform;
at c it is specifically a quadratic Gauss transform by (1). CRT unit
rescalings contribute only row-unit phases. The exact modulus is

    F0^(1/2) F1 Nc |c_(f0)(v)| 1_((v,f1 c)=1).          (7)

After extracting the scalar in (7), its v-dependence is a fixed character
on f1, c_(f0)(v), and theta_c(v), up to row phases. Multiplication of v
by a CRT unit changes the characters by row phases and leaves the
Ramanujan factor unchanged. This explains both the quadratic dual family
and the unchanged, more expensive local cost of a nonmatching prime.
Since c>1, theta_c is primitive and nonprincipal, so psi_tilde(0)=0.

## 3. The completed functional equation, with conductor dependence

The source support selected before [DR, Lemma 5.4] is

    nu=lambda^(-3) a b^3, a squarefree, a,b primary,
    conjugate(tau_theta(nu))=3^(5/2) g_tilde(a) (Nb)^(1/2).

The twist at lambda^4 nu is psi(lambda) psi(a) psi(b)^3.
Summing b therefore produces L^(3fc)(3s-1/2,psi_f^3 theta_c).
There is no coprimality assumption between a and b. This is a coefficient
derivation; the cubic-only statement of [DR, Lemma 5.4] is not applied
to the sextic character. It also shows that the factor psi(lambda) is
only a unit phase and causes no conductor loss.

Consequently [DR, Proposition 5.1] makes Q_(f,c) entire, since the only
possible residue is proportional to the zero value just found. After
removing the archimedean completion, its functional equation has the form

    Q_(f,c)(s) = epsilon_(f,c)
       F0^(1/2-2s) F1^(1-2s) (Nc)^(1-2s)
       G(s) V_(f,c)(1-s),                              (8)

where |epsilon_(f,c)|=1. A fixed nonzero scalar can be placed in G.
Up to fixed positive bases to the power s, G is

    Gamma(5/6-s) Gamma(7/6-s)
       / [Gamma(s-1/6) Gamma(s+1/6)].

The coefficient of V at a source index nu is the original a_star(nu)
from [DR, (5.73)], multiplied by c_(f0)(lambda^4 nu), the fixed
f1-character and theta_c(lambda^4 nu), with all their nonunit zeros.
Fixed bases in (8) change the dual length by fixed constants only.
Equation (8) is the original general periodic-twist equation (5.48),
not the special cubic-twist equation with a different dual sieve.

The dual coefficients have the source support

    nu=lambda^k zeta a b^3, k>=-4, zeta in O^*,
    a squarefree, a,b primary,
    |a_star(nu)| << 3^(k/6) (Nb)^(1/2).                 (9)

All cube powers, units, and allowed shared primes remain. Coefficients
outside this support are zero. The finitely many source branches at
each k have disjoint support; allowing their bounded multiplicity would
also leave the argument unchanged. No claim about their signs is used.

## 4. Two polynomial estimates, including cube and Ramanujan factors

Write ||.||_C for the square root of the row sum over c. Common smooth
cutoffs may have finite-order derivative bounds; all estimates below
pay those bounds. For a smooth series cut off at norm M>=1, the
original side of Q obeys

    ||Q_original,<=M(sigma+it)||_C^2
       << (FCM)^epsilon M^(1-2sigma) Delta_6(C,M).       (10)

To prove it, fix b in the cube expansion and dyadically localize a at
R. The row multiplier chi_c(b)^3 has modulus at most one, including
its zero values, and can be removed only as a contraction of a positive
row norm. Its original coefficient is (Nb)^(1/2-3sigma).
The squarefree a coefficients have squared mass O(R^(1-2sigma));
(5) applies to them. For a block with total norm about M and
R about M/(Nb)^3, the root bound equals at most

    M^(1/2-sigma) (Nb)^(-1) Delta_6(C,M)^1/2.

The complete ideal harmonic sum in b is logarithmic. Dyadic blocks
below M are bounded by (10) because its right side is nondecreasing
in M for sigma<=1/2. Rapidly decreasing tails are summed in the same
way, not discarded. Fixed 2-adic allocations have the same or better
geometric cost. The character psi_f and the height factor are bounded
column multipliers; no derivative of an arithmetic coefficient is taken.

For the dual series cut off at norm L>=1, the stronger estimate is

    ||V_dual,<=L(1-sigma-it)||_C^2
       << (FCL)^epsilon [ C F0^(2sigma)+L^(2sigma) ].    (11)

First omit the Ramanujan factor and fix b,k,zeta. With a at norm R>=1,
the quadratic sieve gives the root resource

    (C+R)^1/2 R^(sigma-1/2) <= C^1/2+R^sigma.

The coefficient of b is (Nb)^(3sigma-5/2). Summing its contribution
to the first term converges for sigma<1/2 and is logarithmic at 1/2.
For the second term R<=L/(Nb)^3 leaves (Nb)^(-5/2), which converges.
The k factor is 3^(k(sigma-5/6)); it is summable for k>=-4. In the
L^sigma term shortening L by 3^k leaves 3^(-5k/6), also summable.
The unit and ramified-character factors are harmless row multipliers
before each use of the positive quadratic norm. This proves the
unweighted root bound C^1/2+L^sigma with all cube powers included.

Now insert the exact Ramanujan expansion

    c_(f0)(a b^3)=sum_(d|f0, d|ab) Nd mu_E(f0/d).

For each d set d_a=(d,a), d_b=d/d_a. Then d_a,d_b are coprime,
d_b|b and (d_b,a)=1. Write a=d_a a', b=d_b b', retaining squarefreeness
and every induced mask. Their outside coefficient at 1-sigma has
absolute size

    (Nd_a)^sigma (Nd_b)^(3sigma-3/2).

The shortened dual length is L/[(Nd_a)(Nd_b)^3]. The C^1/2 term
costs at most C^1/2 F0^sigma times a divisor subpower, because
3sigma-3/2<=0. The L^sigma term is independent of d_a and has the
extra factor (Nd_b)^(-3/2); its sum is at most a divisor subpower.
A prime shared by a and b is allowed throughout. Triangle is applied
to this correctly expanded positive row norm, not to an indefinite
Poisson-sector projection. Squaring proves (11).

## 5. An asymmetric two-piece formula with complete tails

Choose a free splitting parameter M>=1, with (FC)^2/M>=1. Integrate

    (1/(2 pi i)) integral e^(z^2) Q_(f,c)(s+z) M^z dz/z

on a right line and shift to Re(s+z)<0. Q is entire, so the only
crossed pole is at z=0. Use (8) on the reflected line and change z to
-z. This gives an exact sum of an original smoothed series of length
M and a dual smoothed series of length

    L_c = fixed_constant * (F Nc)^2/M.                 (12)

There is no discarded finite-conductor error term. The original weight
is the inverse Mellin transform of e^(z^2)/z. The dual weight is the
inverse Mellin transform of e^(z^2)G(s-z)/z. Both are bounded near zero
and decrease faster than any fixed power at infinity; their finite
logarithmic derivative bounds cost a polynomial in 1+|t|. For the dual
weight the first possible gamma pole in z has real part sigma-5/6,
which is bounded away from zero on this sigma interval. The usual
contour shifts for its small- and large-argument bounds are therefore
valid. Stirling cancels the gamma exponential factors. The source
Mellin continuation supplies finite exponential vertical growth, which
the Gaussian absorbs in the contour shift.

The dual length depends on c, so one must not use (11) with arbitrary
row-dependent column vectors. On a dyadic c interval put y=Nc/C.
All derivatives in log y of the common smooth kernel are uniformly
bounded by the same polynomial height cost. Compactly extend in log y
and take its Fourier transform. Repeated integration by parts gives an
integrable transform with any fixed polynomial frequency weight. Each
term is y^(iv) times a common column profile. Apply (11), then Minkowski
in v. This pays the actual variable cutoff without changing its exponent.
Smooth coefficient dyads and their rapid tails have the same separation.

Using (10)--(12), the squared norm of Q is at most a fixed multiple of
(FC)^epsilon (1+|t|)^A times

    E_sigma(K,C;M) =
       M^(1-2sigma) [C+M+C^(5/6)M^(1/3)+C^(1/3)M^(5/6)]
       +K^(1-2sigma) C^(3-4sigma)
       +K C^2 M^(-2sigma).                             (13)

For clarity, the squared scalar in (8) is
F0^(1-4sigma) F1^(2-4sigma) C^(2-4sigma).
Multiplication by C F0^(2sigma) in (11) gives the penultimate
term of (13). Multiplication by L_c^(2sigma) gives the last term.
This exact cancellation of the F exponents is essential. Replacing
the local C1 cost by the cheaper matched cost would not give (13).

## 6. Optimal split for the supplied scalar resource

Take

    M_star = K^(3/4) C^(7/8),    1<=K<=C^(1/6);
             K^(6/11) C^(10/11), C^(1/6)<=K<=C^2;
             K^(1/2) C,        K>=C^2.                 (14)

The expressions agree at both joins. Equivalently, M_star is their
minimum. It lies between 1 and F C, so both series lengths in Section 5
are legal. The dominating large-sieve term is respectively
C^(5/6)M^(1/3), C^(1/3)M^(5/6), and M. Balancing that term against the
last term of (13) gives precisely

    K C^2 M_star^(-2sigma) = H_sigma(K,C).               (15)

All four original-side terms are bounded by (15). For example the
first regime has C^(7/8)<=M_star<=C, and the middle regime has
C<=M_star<=C^2; these inequalities verify the claimed dominances.
The remaining dual diagonal is also paid, because its ratio to the
FIRST monomial in H is

    K^(-sigma/2) C^(1-9sigma/4) <=1                     (16)

for sigma>=4/9. This proves Theorem A, including both joins and the
endpoints of the sigma interval. C in a fixed bounded interval changes
only absolute constants.

The optimization is exact for these supplied monomials, not just a
numerical grid search. Write the last term of (13) as D=K C^2 M^(-2sigma).
Taking weighted geometric means of D with, respectively,

    C^(5/6) M^(4/3-2sigma), weight 3sigma/2;
    C^(1/3) M^(11/6-2sigma), weight 12sigma/11;
    M^(2-2sigma), weight sigma,

cancels M and gives each of the three monomials of H. The remaining
weight belongs to D. All weights lie in [0,1]. Thus no choice of this
one splitting parameter beats H within (13). This is NOT a lower bound
on the true analytic second moment.

## 7. Removing the completion without losing conductor uniformity

Assume the hypothesis of Theorem B. On Re(z)>=beta+delta, the common
zero-free half-plane and standard fixed-degree Hecke growth give

    |1/L^(3fc)(z,psi_f^3 theta_c)|
       <<_(delta,epsilon) [FC(2+|Im z|)]^epsilon.        (17)

We include the uniformity argument. For a nonprincipal primitive
inducing character, fix log L by the Euler series to the right of 1.
Zero-free disks reaching left from 2+it, with radii bounded in terms
of delta, and Borel--Caratheodory give |log L|=O_delta(log analytic
conductor) on Re(z)>=beta+delta/2. Its Euler bound on
Re(z)=1+delta/2 is O_delta(1). Apply three-lines to
exp((z-it0)^2)log L(z) between those lines. At Re(z)>=beta+delta this
improves log L to O(log(analytic conductor)^theta) for a fixed theta<1.
Exponentiating gives every prescribed positive power in (17). For the
principal primitive character, remove the pole at 1 first; restoring
its reciprocal creates a zero, not a pole. There is only one such
primitive L-function over E. The deleted Euler factors cost a subpower
of FC by product_(p|3fc)(1-Np^(-beta-delta))^(-1). This proof also
handles a drop in primitive conductor after cubing.

Mellin inversion for S_(f,c)(X) starts to the right of 1. Shift to
Re(s)=p+delta<1/2, with delta small in terms of beta and the final
epsilon. Its completion is evaluated at Re(3s-1/2)=beta+3delta.
There is no pole of Q, and (17) introduces none. Use Minkowski in the
Mellin integral, (3), (17), and the rapid Mellin decay of W. The result
is X^(2p+2delta) H_(p+delta)(K,C) times prescribed small powers.
All three monomials of H decrease as sigma increases, so this is
bounded by (4) after assigning the internal losses. The contour's
horizontal segments tend to zero by the same height bounds.

Liu [LIU], Theorem 17.1 and its final field descent, supplies the
finite-order input at B_flat. The full preprint proof remains an imported
dependency. No candidate angular continuation from #1009 is invoked.
For comparison, an Euler-only substitution at p=1/2 is valid with
arbitrarily small losses: shift just to the right of 1/2, use the Euler
product for the completion and the sigma=1/2 estimates with those
small powers paid on both polynomial sides. This does not assert a
zero-free statement on Re(z)=1.

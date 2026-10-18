# A mode-dependent signed tail pays the primitive-principal branch

**PROPOSED exact component theorem.** This repairs a specific volume
cost in a separated mode. It does not prove an arbitrary-character-power
TWO-PLAIN theorem, preserve a subsequent unseparated polar functional,
close the canonical recursion, or improve a zero-free region.

Use the good ideals of E=Q(omega), v(a) and f(g) from
../eisenstein/GROWING_RESIDUE_DEBIAS.md. Put

    v(a)=product_(p|a) q_p^2/(q_p^2+q_p-1),
    f(g)=product_(p|g) 1/(q_p+1),   g squarefree.

Every zero mask remains literal. All lengths and moving mask norms are
in fixed polynomial ranges. Constants may depend on a fixed positive
Gram margin and finitely many smooth seminorms. An arbitrarily small
internal power is chosen before each prescribed final epsilon.

## 1. Two distinct Mellin moments

Choose a nonzero nonnegative smooth W0 supported in(2,3). For a REAL
separated norm height t define the COMPLEX tail

    W_t(x)=W0(x)-2^(-1-it) W0(x/2).                     (1)

It is supported in(2,3) union(4,6). Direct substitutions give

    integral W_t(x)x^(it) dx=0,
    integral W_t(x)dx/x=(1-2^(-1-it)) integral W0(x)dx/x. (2)

The latter has modulus bounded below by half the positive W0 integral,
uniformly in t. All fixed spatial derivatives of W_t are bounded
uniformly in t. The derivatives of W_t(x)x^(it) have fixed polynomial
costs in 1+|t|. Thus canceling the primitive-principal volume moment does
not annihilate the harmonic response used for divisibility calibration.
One fixed tail with integral zero would NOT work at all heights.

## 2. The signed response remains invertible

Let G<=D^(1/2-eta), eta>0 fixed, and index ALL squarefree g of q_g<=G.
For a bounded annular head alpha, including its already separated
phases, assume its response satisfies the elementary bound

    Z_g=sum_(g|a) alpha(a)v(a)/q_a,
    |Z_g| << (Ng)^(-1).                                (3)

Any bounded head supported in one fixed annulus at D satisfies(3) by
the ideal count; a prefix adds logarithms.

The height t in(1) is an EXTERNAL already separated multiplier
`(q_a/D)^(it)` in the row polynomial. It is NOT inserted a second time
inside alpha, Z_g, B_t or the harmonic response in(7). The head may
contain other previously frozen phases; the two roles remain distinct.

Define

    B_t(g,h)=sum_([g,h]|a) mu(a)^2 W_t(q_a/D)/q_a.

The complete squarefree count, now applied separately to the two
nonnegative pieces in(1), gives

    B_t=c_t F+E_t,
    F(g,h)=f([g,h]),
    c_t=kappa_S (1-2^(-1-it)) integral W0(x)dx/x,
    |E_t(g,h)| << D^(-1/2) q_[g,h]^(-1/2)(DG)^epsilon.  (4)

Here kappa_S>0 is the fixed squarefree density. The count is the same
one proved in the growing-residue file, equation(5); linearity is valid
for complex tests. Crucially |c_t| has a fixed positive lower bound.
The matrix is not called an exact positive Gram matrix.

For completeness the relevant finite matrix facts are as follows:

    F(g,h)=f(g)f(h)sum_(d|g,d|h) q_d,
    F^(-1)(g,h)=mu(g)mu(h)/(f(g)f(h))
                      *sum_([g,h]|d,Nd<=G) 1/q_d.       (5)

They follow from the two divisor-incidence inversions on the downward
closed squarefree label set. In particular
`|F^(-1)(g,h)| << gcd_norm(g,h) G^epsilon`.
Its diagonal-normalized least eigenvalue is at least G^(-epsilon)
times a positive epsilon-dependent constant. This follows directly by
inverting the first factorization in(5) and applying the convergent ideal
series at1+epsilon. The errors in(4), in the same normalized operator
norm, cost `D^(-1/2)G^(1+epsilon)`. They are smaller than this eigenvalue
for large D in the stated range. Dividing B_t by c_t and using a Neumann
series therefore proves invertibility uniformly in t.

There is also a direct infinity-norm estimate:

    ||F^(-1)E_t||_(infinity->infinity)
                                  << D^(-1/2)G^(1+epsilon).

Indeed `sum_k|E_t(h,k)| << D^(-1/2)sqrt(G)/sqrt(q_h)` times
a prescribed subpower, and
`sum_h gcd_norm(g,h)/sqrt(q_h) << sqrt(G) q_g^epsilon`.
Both follow by expanding the gcd into its complete divisor sum.
Equation(3) and(5) give
`max_g|(F^(-1)Z)_g| << G^epsilon`, since

    sum_h gcd_norm(g,h)/q_h
       =sum_(d|g) phi(d)/q_d sum_(Nk<=G/q_d)1/q_k
       << G^epsilon.

Thus the unique solution `xi=-B_t^(-1)Z` has

    max_g|xi_g| << (DG)^epsilon,
    sum_g f(g)|xi_g|^2 << (DG)^epsilon,
    sum_g |xi_g|/sqrt(q_g) << G^(1/2)(DG)^epsilon.       (6)

The middle estimate uses the normalized inverse and
`sum_g|Z_g|^2/f(g) << G^epsilon`; the last is Cauchy. Fixed height
derivatives satisfy the same conclusions when the corresponding head
derivatives satisfy(3). The modified coefficient

    alpha_new(a)=alpha(a)
       +mu(a)^2/v(a) W_t(q_a/D)sum_(g|a,q_g<=G)xi_g      (7)

satisfies EVERY exact response `sum_(g|a)alpha_new(a)v(a)/q_a=0`.
Its pointwise coefficients are subpower by(6) and the divisor bound.

The usual coefficient energy also survives without a false positivity
identity for B_t. The positive reference F satisfies
`xi^*F xi << (DG)^epsilon` by the scalar-renormalized version of(4).
The positive response matrix with profile
`W0(x)+(1/2)W0(x/2)` has quadratic form at most a fixed constant times F,
again by(4). Since `|W_t|` is bounded by this profile and
`|W_t|^2<=C|W_t|`, direct expansion gives

    sum_a |alpha_new(a)-alpha(a)|^2 << D^(1+epsilon).   (8)

No use of the invalid inequality `W_t^2<=C W_t` is made.

## 3. A full masked count for the principal tail

For ANY squarefree zero mask B and any L>=1, define

    P_(B,t)(L)=L^(-1/2)sum_((a,B)=1)
                   mu(a)^2/v(a) W_t(q_a/L)(q_a/L)^(it).

Then

    |P_(B,t)(L)| <<_epsilon (L NB)^epsilon (1+|t|)^C.  (9)

Here C is fixed. To verify the full count behind(9), the Dirichlet series
of mu^2/v is `zeta_E^S(s)/zeta_E^S(2s)` times a product absolutely
convergent for Re s>0: its local correction is
`[(v(p)^(-1)-1)q_p^(-s)]/[1+q_p^(-s)]=O(q_p^(-1-Re s))`
on closed positive half-planes. Equivalently, convolve the ordinary
squarefree coefficients with this absolutely summable Euler correction.
The masked ordinary squarefree lattice count is

    sum_((a,B)=1)mu(a)^2 V(q_a/L)
       =density(B) L integral V(x)dx
          +O_epsilon(L^(1/2+epsilon)(NB)^epsilon ||V||_J).

It follows by the complete square-divisor expansion, ideal lattice
count, mask divisor sum, and partial summation. The Euler correction
and every mask factor have absolute coefficient mass at1/2 bounded by
a prescribed subpower of NB. Therefore the same estimate holds for
mu^2/v. Apply it to `V=W_t x^(it)`. Its whole main term vanishes by(2),
and division by sqrt(L) proves(9). Nonempty bounded subunit scales are
handled directly, and smaller annuli contain no ideals.

## 4. The actual primitive-principal row cost

Let the physical u be EVERY good sixth-free ideal with q_u about U.
Fix an integer j, and consider the presentation
`psi_u(a)=chi_a(u)^j` with a fixed finite-ray twist whose conductor is
supported in the SAME excluded set S, and every original
zero extension. Restrict to rows where its primitive inducing character
is principal. For j=2,3,4 put `m=6/gcd(j,6)`. At every good prime,
principality forces the valuation of u to be a multiple of m. Thus
`u=b^m`, with the inherited power-free restriction, up to a fixed number
of finite sectors. Elementary ideal counting gives O(U^(1/m)) such rows.
The finite-ray twist can reduce this set, never enlarge that bound.
The local input is precisely the native tame Kummer primitivity away
from6: a nonzero valuation modulo6 remains ramified at that good prime.
Fixed-ray reciprocity factors cannot cancel ramification there.

Use the COMPLETE tail from(7), with its already known separated height t,
and an arbitrary same-presentation plain factor of length N. Extracting
`a=g c` keeps all shared-prime zeros, leaves the mask `(c,g)=1`, and gives
the scalar `psi_u(g)/(sqrt(q_g)v(g))` times(9) at L=D/q_g. The mask
includes rad(u), g and every original common puncture. Their norms are
polynomially bounded. The plain factor has the elementary pointwise
bound O(sqrt(N)) on these principal rows. Minkowski and(6) consequently
give the COMPLETE bound

    sum_(u primitive-principal) w_u |Tail_u(D) S_u(N)|^2
        << U^(1/m+epsilon) N G (1+|t|+|height_plain|)^C. (10)

All g and shared masks are included before taking norms. In particular
N<=sqrt(U) makes(10) at most `U^(1+epsilon)G` for j=2,3,4. For j=2,4
the actual exponent before G is at most5/6; for j=3 it is at most1.
This removes the factor D from the primitive-principal volume cost.
No cancellation between different rows or divisor labels is assumed.

## 5. The recombination gate is explicit

The known a-height MUST be fixed before choosing(1). A later independent
Mellin height changes the volume moment and invalidates its claimed
vanishing. One may integrate(10) against an ORIGINAL common separated
measure of finite weighted L1 norm, provided every a-height in that
representation has already been included in t. This is a norm comparison,
not a replacement zero detector.

The exact harmonic responses in(7) do not automatically remain the polar
functional of a new canonical recursion, nor do they automatically match
a product-column residue after a fresh cutoff separation. That equality
requires a separate exact source calculation. The nonprincipal power-j
row mean still needs its permitted analytic moment theorem. Identically
principal power j=0 is not covered by the useful `N<=sqrt(U)` conclusion:
the same argument costs U N G. Consequently this component repairs the
specified separated-mode principal branch, while leaving the actual full
canonical and Suzuki completion problems open.

# Segre diagonal restriction and the native observation boundary

This is a proof-only comparison between two declared source constructions.
The algebra is classical. Its purpose is to identify an exact common
operation without identifying their arithmetic realizations or metrics.

The Segre parent is the source in
[the frozen generalized-L packet](https://github.com/gfreund123/riemann/blob/a895f47628b0bc7c7ee5e0392df2f79c24166f92/research/l-families/atlas/generalized/segre-hadamard-source/sources/SEGRE_KOSZUL_LIE_PARENT.md).
The native input is the half-divisor source in L-102707 at
`ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`. The observation obstruction
below is the complete source construction frozen at
`f97b7e00ba0bd3d6153167b477c44c6f153da10f`.

## 1. A multiplication map exists before any scalar trace

Work over Q. Let V and W be two-dimensional spaces of sections of
O(1) on two copies of P1; this fixes the convention rather than silently
replacing either space by its dual. Fix positive integers p,q, and set

    R_k = (Sym^k V)^(tensor p) tensor (Sym^k W)^(tensor q),
    S_k = Sym^(pk) V tensor Sym^(qk) W,
    R = direct-sum_(k>=0) R_k,  S = direct-sum_(k>=0) S_k.

Both multiplications are ordinary symmetric multiplication. Multiplying
the p binary forms in the first group, and the q forms in the second,
defines a graded algebra map rho:R -> S. This is the restriction of
the Segre section ring along the two grouped diagonals

    P1 x P1 -> (P1)^(p+q).

**Proposition.** The map rho is surjective in every grade. Its kernel I
is an honest homogeneous ideal, and

    0 -> I_k -> R_k -> S_k -> 0

is GL(V) x GL(W)-equivariant. In particular

    dim I_k = (k+1)^(p+q) - (pk+1)(qk+1).

**Proof.** A binary monomial of degree pk is a product of p monomials
of degree k: distribute its exponent of the second variable among p
integers between0 and k. The same argument applies to the second group.
These monomials span S_k, proving surjectivity. Compatibility with
multiplication follows by associativity, and equivariance follows from
the naturality of symmetric multiplication. The kernel and dimension
claims now follow from the exact sequence. QED.

For endomorphisms A of V and B of W, write
h_k(A)=Tr(A|Sym^k V). The exact character identity is

    Tr((A,B)|I_k) = h_k(A)^p h_k(B)^q - h_(pk)(A) h_(qk)(B).

The minus sign is an additive character identity for the displayed
kernel. It is not an assertion that a rational defect numerator is a
finite superdeterminant, and no eigenvalue purity follows from it.

## 2. Degree one is the literal native coefficient source

Give each of p+q distinct primes its own activation coordinate z_l.
With c_e=[x^e]sqrt(1-x), its native local coefficient is

    1_(2 divides e)c_(e/2) + z_l(c_e-1_(2 divides e)c_(e/2)).

It is affine in z_l, for every exponent e. Therefore every supported
native coefficient lambda_n is multiaffine in the p+q coordinates.
Conversely, a squarefree n with prime support T has coefficient

    lambda_n = (-1/2)^|T| product_(l in T) z_l.

Thus the actual squarefree source coefficients span the entire degree-one
Segre chart, including the unit. This is equality for the defined native
coefficients, not a fit of a chosen observation to a polynomial space.

Synchronizing the first group to u and the second to w is precisely rho
in degree one, after choosing the affine charts and their trivializations.
The resulting coefficient span is

    span{u^i w^j: 0<=i<=p, 0<=j<=q}.

The specified Segre construction supplies a graded extension R -> S of
this native coefficient space before path integration. However, the section grade k is an auxiliary
algebraic grade. It is neither the exponent of a prime nor the physical
product cutoff. Equating these distinct gradings would change the source.

The equivariance above is likewise an algebraic statement. A general
GL(V) x GL(W) transformation does not preserve the marked endpoints0,1,
monotone real paths, the arithmetic labels, or the original Mellin measure.
No physical symmetry or unitary action is obtained merely by naming it.

## 3. Pullback is functorial; forgetting paths is the obstruction

For the native polarized one-form alpha_(n,m)=2 d(lambda_n) lambda_m,
ordinary pullback commutes with multiplication and exterior differentiation.
It also commutes with integration along a specified transformed path.
There is no failure of these elementary identities.

The different question is whether a path transformation can be computed
from its already integrated source, after the labelled path was forgotten.
The frozen construction at f97b7e00 answers this negatively for
T(u,v,w)=(u,u,w). It supplies two legal paths gamma_plus,gamma_minus with

    integral_gamma_plus alpha_(n,m)
      = integral_gamma_minus alpha_(n,m)

for every supported n,m, but unequal synchronized observations. The
all-height equality is proved from the complete polynomial form of the
source on the common v=1 part of those paths; it is not extrapolated
from their finite replay panels. Both paths also retain the same initial
v-activation segment.

After T, at physical-product horizon60, the rational coalesced coefficient difference at ratio3/5 is
1/16243587360, with its remaining physical factor1/sqrt(15). Both aliases
(3,5) and(6,10), including the latter's factor1/2, are present. Consequently
there is no function, linear or nonlinear, on those original integrated
source fibres that implements this path transformation.

Even giving every original cutoff field does not repair that particular
loss: those fields agree at every cutoff for the two paths. This does not
refute the separately proved horizon-25 retraction, whose finite source
closure was checked. It prevents extending that conclusion automatically.

## 4. What the comparison does and does not provide

The honest shared construction is a Segre algebra with a grouped diagonal
restriction. The native path currents supply an additional observation
operation whose compatibility must be proved independently. Keeping the
algebra before taking traces is useful, but does not by itself make a
later observation faithful to every operation on labelled paths.

The grouped curvature calculation has dimension4pq-1, with one missing
top corner. That number concerns affine one-forms modulo exact endpoint
terms, not the dimension of I_1, which is2^(p+q)-(p+1)(q+1). These are
different invariants of different maps; no equality between them is claimed.

This comparison constructs no Frobenius action for the native number-field
source, no induced identification of Koszul dual Lie algebras, no preserved
polarization, and no principal-member decoder. Those interfaces remain
additional mathematical requirements.

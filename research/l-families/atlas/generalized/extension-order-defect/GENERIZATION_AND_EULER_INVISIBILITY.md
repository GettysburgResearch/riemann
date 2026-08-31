# Identical arithmetic stalks do not determine an extension

This is a counterfeit gate for unrestricted source uniqueness. It retains
the same generic graded algebra, the same boundary graded algebras, and
every boundary Frobenius power. What changes is the map from a boundary
stalk to nearby inertia invariants. It does not contradict the relative
universal property of the declared AFTER construction.

The underlying sheaf facts are classical: closed-immersion pushforward is
fully faithful and has the stated stalks, and the small étale site has enough
geometric points to test an isomorphism. See the primary treatments
[Stacks, closed immersions and pushforward](https://stacks.math.columbia.edu/tag/04E1)
and [Stacks, neighborhoods, stalks and points](https://stacks.math.columbia.edu/tag/03PN).
The construction and its source-specific falsifier are given explicitly
below; no new gluing theorem is claimed.

## 1. The datum that a stalk Euler factor omits

Let X be a smooth curve over a finite field of characteristic greater than
three, j:U→X a dense open immersion, and i:Z→X its finite reduced complement.
Work with characteristic-zero coefficient sheaves and finite-dimensional
constructible pieces in every grading degree. All algebras are commutative,
connected graded, and augmented; their degree-zero sheaf is the constant
coefficient sheaf. Each construction below is degreewise, not a claim that
the infinite direct sum is a finite-rank constructible sheaf.

Write V for a graded algebra on U and W for a graded algebra on Z. A
Frobenius-equivariant graded algebra map

    theta: W → i* j_* V                                      (1.1)

gives the graded algebra on X

    F(theta)=j_*V ×_(i_* i* j_*V) i_*W.                       (1.2)

Here i* denotes ordinary inverse image of coefficient sheaves, not a
derived functor or pullback of coherent modules. The first arrow in the
fibre product is the adjunction map and the second is i_*theta. Finite
limits of these sheaves are computed as sheaf limits; the resulting ring
operations are componentwise.

Restriction to U of (1.2) is V, because a sheaf supported on Z restricts to
the terminal zero ring there. Its restriction to Z is W, because inverse
image preserves finite limits and i* i_* is the identity. Thus each graded
piece is constructible. Conversely, for a graded algebra F with given
generic restriction and boundary restriction, its canonical map to (1.2)
is an isomorphism on every geometric stalk. Enough points imply that it is
an isomorphism. This proves that fixing V, W, and theta determines F,
without inferring that V and W alone determine it.

The relevant theta is the boundary generization map. For a lisse finite
monodromy generic source, its target is the inertia-invariant subspace of
the generic representation, with the residual Frobenius action retained.

## 2. A canonical counterfeit relative to the augmentation

Take F=B, the actual AFTER algebra of the frozen construction, put
V=j*B and W=i*B, and call its original map theta_B. Replace that map by

    theta_0: W → k_Z → i* j_*V,                              (2.1)

using the augmentation followed by the unit. Set D=F(theta_0). These are
algebra maps, equivariant for Frobenius. Therefore D exists by (1.2), is
augmented, and has exactly the same generic algebra V and the same boundary
algebra W as B. In degree zero theta_0 is the identity; in every positive
degree it is zero.

If theta_B has positive rank in some positive degree at a geometric point,
then B and D are not isomorphic as extensions with their generic algebra
identified. Any such isomorphism would make their generization maps
commute; composition with an invertible boundary map cannot turn a
positive-rank map into zero. This rank argument even allows a change of
boundary basis and does not require fixing W pointwise.

For the actual S3 source, use

    A_n=Sym^n(Std) tensor Sym^n(Perm) tensor chi_u^n,
    B=(j_*A) tensor Sym(j_*Std placed in grading degree two).

At an old C2 branch, B_1=A_1^I has dimension three and injects into the
nearby invariant space. The generic degree-one representation is the
six-dimensional regular representation. On that same three-dimensional
boundary stalk, theta_B has rank three and theta_0 has rank zero. This is
an actual source discriminator, not a dimension fitted to an Euler factor.

At infinity the same construction preserves both the split and nonsplit
boundary Frobenius actions; at the new point u=0 it also preserves the
original full invariant stalk. A zero cokernel in the old AFTER→BEFORE
comparison at u=0 does not make this different generization modification
trivial. For example the new-point degree-two stalk is nonzero and its
original generization is injective, whereas theta_0 kills that degree.

## 3. Every closed-place scalar shadow remains equal

For every closed point v, every grading degree n, and every m≥1, B_n and
D_n have isomorphic Frobenius representations on their geometric stalks.
Consequently both

    tr(Fr_v^m | B_(n,v)) = tr(Fr_v^m | D_(n,v)),
    det(1-T Fr_v | B_(n,v)) = det(1-T Fr_v | D_(n,v))         (3.1)

hold, including at ramification. Thus the ordinary L-functions of every
finite graded piece agree, as do the nonlinear Hilbert-place products

    product_v sum_(n≥0) tr(Fr_v | B_(n,v)) z^(n deg v)
      = product_v sum_(n≥0) tr(Fr_v | D_(n,v)) z^(n deg v).   (3.2)

Formal equality holds coefficientwise; wherever one of the established
analytic continuations is defined, equality refers to the same scalar
germ. In particular D has the same full scalar function
`E_chi(z) P_E(z^2)` as the declared single-generator AFTER source.

Tensoring both sides degreewise with any fixed constructible coefficient
sheaf preserves the stalk isomorphisms, so all its ordinary local twists
also agree. Applying the same stalkwise tensor or symmetric-power
operation retains this blindness. This does not claim that a Verdier-dual
complex, extraordinary restriction, or generization map is determined by
the stalk representations. Such operations are outside the scalar
comparison being asserted.

The equality survives every finite constant-field extension. A closed
point of degree d splits into gcd(d,e) points after extension of degree e;
each new Frobenius is the old Frobenius to the power e/gcd(d,e), with new
degree d/gcd(d,e). Equality (3.1) keeps those powers and degrees. This
statement uses the actual base-change rule, not an unproved substitution
of a single scalar grading variable.

## 4. The positive criterion and its exact scope

The counterfeit D cannot receive a graded algebra map from the prescribed
`j_*A` whose generic restriction is the actual inclusion into V. At an old
C2 point in degree one, the generization of that inclusion is the nonzero
map from A_1^I to V_1^I. Any proposed map through D would instead have zero
generization by (2.1). The resulting square cannot commute.

This explains which hypothesis removes the ambiguity. Fixing the
underlying generic source is insufficient. Fixing the actual source map
from j_*A and the degree-two generator map gives the relative free-algebra
universal property of B. Fixing W and its generization map gives (1.2).
Requiring ordinary j_* of the whole generic algebra selects the BEFORE
extension, with its different boundary stalks. None of these positive
criteria follows solely from equality (3.2).

There is therefore no unrestricted uniqueness theorem for "all sources
whose Euler function is E_chi P_E(z^2)" within even this same-generic-source
constructible category. This is not evidence against the declared source
construction: it identifies the extra morphism data that its canonicity
uses. The missing data have a direct low-grade test, rather than merely a
warning that Euler factors might forget something.

## 5. Bounded replay

The replay authenticates the finite comparison proof and executable before
using their source constructions. It independently enumerates the old C2
nearby monomial basis and the AFTER subset in grades zero through six,
constructs the original inclusion and augmentation generization maps, and
checks their ranks and residual signs. It also keeps the frozen literal
infinity and new-point source controls. Frobenius determinants are
reconstructed from actual plus/minus multiplicities and from Newton traces,
then tested after twists and closed-point splitting. These tests certify
the stated finite source controls; the all-degree equality follows from
the explicit construction (1.2), not from a finite list of traces.

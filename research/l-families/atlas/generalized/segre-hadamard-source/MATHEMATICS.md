# The pointwise-power numerator as a finite Chow-module K-polynomial

Status: exploratory source theorem and bounded replay contract.
Field: characteristic zero; statements about matrices use complex matrices.
The classical finite Chow-module theorem is imported explicitly below.
This packet binds it to the repository's pointwise-power numerator and retains
the multiplication maps needed to distinguish actual syzygies from an Euler
characteristic. It does not assert a finite spectral determinant for that
numerator, an arithmetic functional equation, or any RH consequence.

## 1. Source, notation, and the two polynomial bases

Fix integers `d,m>=1`, a `d`-dimensional vector space `V`, and the standard
graded algebra

    R = direct_sum_{r>=0} (Sym^r V)^{tensor m}.

Multiplication is the product of symmetric-algebra multiplications in the
ordered factors. Polynomial variables transform as `V`; geometric linear
forms therefore belong to `V*`. The diagonal group `GL(V)` and the group
`S_m` permuting factors act on `R` and commute.

There are two different polynomial bases. The full embedding uses
`S=Sym(E)`, `E=V^{tensor m}=R_1`. The base in this packet is

    W=Sym^m V -> E,       S'=Sym(W) -> R.                  (1.1)

The arrow is the characteristic-zero symmetrization inclusion. For explicit
integer matrices use the divided-power basis: a multi-index `a` of total
degree `m` maps to the sum of the distinct words with content `a`. These orbit
sums differ from a normalized symmetric-power basis by nonzero rational
scalars and define the same equivariant subspace and module.

For `A in GL(V)` let `h_r(A)=tr(Sym^r A)` and

    F(A,T)=sum_{r>=0} h_r(A)^m T^r,
    Q(A,T)=det(1-T Sym^m A),    N(A,T)=Q(A,T)F(A,T).       (1.2)

The frozen PR781 source
[T-108500](https://github.com/gfreund123/riemann/blob/ac1cc5eaf229087b6d805e908897c7c8c99a58b7/claims/theorems/T-108500-pointwise-transform-defect-law.md)
uses this `Q` generically. The full ambient denominator instead has degree
`d^m` and is `D(A,T)=det(1-T A^{tensor m})`. On diagonal eigenvalues `x_i`,

    D/Q = product_{|a|=m} (1-x^a T)^{m!/(a_1!...a_d!)-1},
    K_ambient = (D/Q) N.                                (1.3)

The equality is polynomial and survives collisions; generic minimal scalar
recurrence denominators need not. The concurrent ambient bridge at commit
`64c8664a2fee08ae2e249743d6f784a7bec61b83`,
`research/l-families/atlas/generalized/SEGRE_RECURRENCE_SYZYGY_BRIDGE.md`,
is credited for its separate `Sym(E)` work. In the binary cube, `K_ambient`
has no linear term, whereas `N` has linear term `2ab`, with `a=tr A,b=det A`.
These numerators cannot be substituted for one another.

## 2. Finite Chow module and its canonical Tor numerator

**Theorem SHS1.** Put

    s=binom(d+m-1,m),  D=m(d-1)+1,  c=s-D.

Then `R` is a finite Cohen--Macaulay graded `S'`-module of dimension `D` and
projective dimension `c`. The finite, canonical equivariant vector spaces

    B_{i,j}=Tor_i^{S'}(R,k)_j

satisfy

    N(A,T)=sum_{i=0}^c (-1)^i sum_j tr(A|B_{i,j}) T^j.   (2.1)

The multiplication in (1.1), not the scalar rational function, defines these
Tor groups. The module has the action of `GL(V) x S_m`.

**Proof and imported boundary.** Finiteness is precisely the classical
construction of Raicu--Sam--Weyman, [arXiv:2108.10910](https://arxiv.org/abs/2108.10910),
Proposition 2.7. Here is the short geometric mechanism. On
`X=(P(V*))^m` the linear system `W` sends a tuple of lines to the product
of their linear forms. This has no basepoint because a product of nonzero
linear forms is nonzero. Equivalently the orbit sums generate an ideal of
finite colength in `R`, and graded Nakayama gives module finiteness. The
image is the Chow variety; (1.1) need not be injective and does not in general
make `R` a quotient algebra of `S'`.

For completeness, Cohen--Macaulayness and the canonical shift can be read
directly from the product of projective spaces: for a diagonal line bundle
`O(r,...,r)`, the Kunneth formula and projective-space cohomology leave only
degree zero or the top degree `m(d-1)`; no intermediate cohomology occurs.
The section ring is the Segre ring. The same assertions and the resulting
projective dimension are in that paper, (3.2)--(3.5). Depth is `D` over `S'`
because its positive ideal has the same radical as the irrelevant ideal of
`R`; Auslander--Buchsbaum gives `c`. A graded minimal equivariant resolution
exists in characteristic zero. Taking its graded characters proves (2.1).
This uses ordinary homological algebra, not an assumption that the recurrence
denominator itself already encodes a spectral parent. QED.

For any finite subgroup `I` acting through `GL(V) x S_m`, applying invariants
to the *whole* resolution remains exact. Its terms are
`(S' tensor B_{i,j})^I`, not generally `Sym(W^I) tensor B_{i,j}^I`.
The distinction is substantive; see Section 7.

## 3. Duality, degree, and binary effectivity

**Theorem SHS2.** Set `L=s-d` and `e=m(s/d-1)` (an integer). With
`sgn_m` the factor-permutation sign representation, the Tor spaces obey

    B_{c-i,L-j} = B_{i,j}^* tensor (det V)^e
                 tensor sgn_m^{d-1}.                   (3.1)

Consequently

    N(A,T)=(-1)^c (det A)^e T^L N(A^{-1},T^{-1}).        (3.2)

In particular `deg_T N=L`, its top coefficient is
`(-1)^c (det A)^e`, and `deg Q-deg N=d` for invertible `A` when `Q`
is retained as the universal denominator. This is a statement about the
unreduced numerator and denominator, not an assertion about their gcd.

**Proof.** The product-projective canonical bundle gives
`omega_R=R(-d) tensor (det V)^m tensor sgn_m^{d-1}`. The sign is the
Kunneth interchange sign for the `d-1` dimensional factors. Also
`omega_{S'}=S'(-s) tensor det(W)` and
`det(W)=(det V)^{ms/d}`. Applying `Hom_{S'}(-,omega_{S'})` to the minimal
resolution and using `Ext^c(R,omega_{S'})=omega_R` gives (3.1), with the
standard grading shifts. The constant Tor term is one-dimensional in grade
zero, so (3.2) has the stated nonzero top coefficient. QED.

The canonical-module mechanism, including the factor-permutation sign, is
classical; the cited paper (3.4)--(3.5) supplies exactly that construction.
It explains the degree deficit in
[T-108510](https://github.com/gfreund123/riemann/blob/ac1cc5eaf229087b6d805e908897c7c8c99a58b7/claims/theorems/T-108510-defect-codimension-law.md).
The degree deficit `d` and the projective dimension `c` are different numbers.
Neither is a consequence of Koszulness alone. The Koszul Lie parent already
in PR766 uses `Tor^R`, also different from the `Tor^{S'}` here.

**Corollary SHS3 (binary case).** If `d=2`, then `c=0` and `R` is a finite
graded free `S'`-module. Its canonical quotient `B=R/S'_+R` is an actual
effective graded representation, and `N=ch(B)`. The choice of an equivariant
free splitting is not claimed canonical. Its total rank is `m!`.
For eigenvalues `x,y`, an explicit classical character is

    N(diag(x,y),T)
      = sum_{pi in S_m} x^{maj(pi)} y^{m des(pi)-maj(pi)} T^{des(pi)}. (3.3)

Here descents and major index have their usual permutation meanings. All
exponents are nonnegative. At `x=y=1` this gives the Eulerian polynomial.
Formula (3.3) is the homogeneous form of the descent/major-index formula
in the cited paper (3.11); no combinatorial priority is asserted. It provides
an independent bounded character check, not the definition of `B`.

For binary matrices, `A^{-1}` is conjugate to `A/(det A)`, so (3.2) recovers
the weighted same-matrix palindrome. In higher rank only the contragredient
identity is automatic; reciprocal scalar slices require extra input.

## 4. A signed K-polynomial is not a determinant construction

Equation (2.1) is an additive Euler characteristic of a finite complex. A
superdeterminant would instead multiply factors `det(1-TK)` with parity
signs. These are different operations. No canonical finite endomorphism
whose superdeterminant is `N` has been produced by SHS1.

In the binary cube, `N=1+2abT+b^3T^2`. Its coefficients are actual graded
characters, yet its inverse roots generically require `sqrt(a^2-b)`.
An operator obtained solely by evaluating a fixed finite representation of
the original diagonal torus has monomial weights, which cannot supply these
roots generically. A fitted companion matrix or the separately deformed
rank-two matrix in PR781 is a different construction. This is compatible
with additive character effectivity in SHS3.

## 5. Actual low-grade source maps and a false Betti inference

The replay constructs the Koszul complex

    C_{i,j}=Lambda^i(W) tensor R_{j-i},
    d(w_1 wedge ... wedge w_i tensor r)
      =sum_a (-1)^{a-1} w_1 wedge ... omit w_a ... wedge w_i
                        tensor (w_a r).                (5.1)

Every product `w_a r` is the literal orbit-sum multiplication from (1.1).
Sparse rational elimination is performed separately at each torus weight;
consecutive differentials must compose to zero. Quotient and homology
characters come from the actual images. Finite-dimensional computations
verify only the declared grades; SHS1 supplies the all-grade theorem.

For `(d,m)=(3,3)`, `s=10,D=7,c=3,L=7` and

    N(I_3,T)=1+17T-9T^2-65T^3+65T^4+9T^5-17T^6-T^7.   (5.2)

It is invalid to read off a minimal resolution from these alternating
coefficients. In particular the invariant normalization summand has a
degree-two `det(V)^2` generator (Raicu--Sam--Weyman, Example 4.5).
Thus a putative resolution with generators only in degrees zero and one
already fails. The replay tests this on the full ordered Segre module,
including factor-permutation traces. The cube is a comparison case, not an
untouched heldout; the separately declared ternary fourth-power panel is
the new source-replay heldout.

## 6. Exact action criterion for independent deformations

**Theorem SHS4.** Suppose `d,m>=2` and each `A_i` is invertible. The tensor
operator `A_1 tensor ... tensor A_m` preserves the canonical subspace
`W=Sym^m V` if and only if all `A_i` are scalar multiples of one matrix.

**Proof.** Pure powers `v^{tensor m}` lie in `W`. Their images are decomposable
tensors. A nonzero decomposable tensor which is invariant under every factor
permutation has all its factors proportional: comparing a transposition and
contracting the other factors reduces this to `u tensor v=v tensor u`.
Therefore `A_i v` is proportional to `A_1 v` for every nonzero `v`.
The invertible operator `A_i A_1^{-1}` preserves every line, hence is scalar
(apply it to basis vectors and their pairwise sums). Conversely scalar
multiples of a common matrix preserve symmetric tensors. QED.

The theorem concerns this fixed canonical base, not all possible alternative
module constructions. A scalar product of the factors scales the action in
degree `r` by its `r`th power. Factor permutations themselves preserve the
base and act trivially on `W`. Thus the source construction has a definite
deformation/monodromy compatibility requirement which is hidden by merely
computing scalar Hadamard products.

## 7. Ramified invariants do not commute with replacing the base

**Proposition SHS5.** Let `d=m=2` and let `I=C2` act on `V=1+sgn`. Then

    W=2*1+sgn,       B=1+sgn*T,
    Hilb(R^I,T)=(1+T^2)/((1-T)^2(1-T^2)).               (7.1)

Replacing the polynomial base and free quotient by their fixed parts gives
`Hilb(Sym(W^I) tensor B^I,T)=1/(1-T)^2`, whose degree-two coefficient is
`3` instead of the actual `5`. Moreover `R^I` is not finite over
`Sym(W^I)`: its pole order at `T=1` is `3`, larger than that base's dimension
`2`.

**Proof.** The binary-square quotient is `B=1+Lambda^2 V*T`; the latter
line is sign. The full free module's invariant part is
`S'^+ + T S'^-`. The polynomial base has two invariant degree-one variables
and one anti-invariant variable, so
`Hilb(S'^+)=1/((1-T)^2(1-T^2))` and `Hilb(S'^-)=T Hilb(S'^+)`.
This proves (7.1). Alternatively its degree `r` dimension is
`((r+1)^2+1_{2|r})/2`, obtained directly from the source involution. QED.

Taking invariants of the entire complex (5.1) is exact in characteristic
zero and retains the crossed invariant tensors. This is the safe interface
to a ramified local system; projecting generators and syzygies separately
is not that interface. No equality with a global arithmetic Euler product
is asserted by this finite example.

## 8. Scope and verification

All module maps and duality statements concern the fixed characteristic-zero
Segre source. Spectral collisions specialize its character and can cancel
scalar numerator/denominator factors; they do not by themselves change its
Betti spaces. At identity, for example, the cube's universal denominator is
`(1-T)^10`, while its reduced scalar denominator is `(1-T)^7`.

The preregistration records the exact cases, caps, prior comparisons and false
controls before execution. The executable replay and tests are independently
checked by the parent under the shared RAM gate. No successful run is claimed
here before the parent records one. This packet does not compute a full
minimal resolution in all ranks, prove a finite superdeterminant, or transfer
finite source positivity to an RH statement.

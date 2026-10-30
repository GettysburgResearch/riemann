# Eisenstein-abelian closures and Artin factors over arbitrary bases

**Status.** A classical implication of an assumed finite-order Hecke zero-free half-plane over E=Q(ω). It does not prove that input, supply a new numerical constant, assume the Artin holomorphy conjecture, or claim priority. The staged numerical candidate and its conventional-Hecke interpretation retain the separate qualifications in [the Hecke scope note](../2026-10-29-hecke-candidate-scope/README.md).

## Statement

Let 0<θ<1, and assume that every finite-order Hecke L-function over E is nonzero in Re s>θ, with the standard principal pole at s=1 allowed. Let A/F be a finite Galois extension of arbitrary number fields, and suppose the compositum AE is abelian over E. For every finite-dimensional complex representation ρ of G=Gal(A/F), its Artin L-function is nonzero in Re s>θ, except for its pole at s=1 of order dim ρ^G. Every nontrivial irreducible Artin L-function in this collection is entire. By the functional equation, the same nonvanishing holds in 0<Re s<1−θ.

In particular, if A/F is abelian, every finite-order F-Hecke character associated to Gal(A/F) has this inherited half-plane. More generally, every finite-order F-Hecke character whose cyclic class field A satisfies AE/E abelian is covered. These conditions allow F not to contain E and need not make F/Q Galois. They do not cover an arbitrary Hecke character over an arbitrary extension of E. No conductor-uniform lower bound is asserted.

The same half-plane also holds for the unitary norm twist `ρ⊗|·|^(it)` for any real t: its L-function is `L_F(s+it,ρ)`, with a possible pole at `s=1−it` of order `dim ρ^G`. This is vertical translation and does not establish the result for general infinite-order angular types.

## Proof

Artin factorization and class field theory over E give the exact all-place identity

    ζ_AE(s)=∏_{ξ∈Gal(AE/E)^∨} L_E(s,ξ).                     (1)

Every nonprincipal factor is entire and is nonzero in the assumed half-plane; the principal factor is ζ_E, with its simple pole at 1. Thus ζ_AE has no zero there. If E⊂A, then AE=A. Otherwise AE/A is quadratic, with nonprincipal finite-order Hecke character η, and

    ζ_AE(s)=ζ_A(s)L_A(s,η).                                  (2)

The quadratic factor is entire, so a zero of ζ_A at any point s≠1 would make the right side zero; no assumed nonvanishing of L_A(s,η) is used. Thus ζ_A is nonzero for Re s>θ away from its pole at 1.

Next G has an abelian normal subgroup of index at most two. If E⊂A, the kernel H of `G→Gal(FE/F)` is Gal(A/FE), a subgroup of the abelian group Gal(A/E). If E⊄A, then A∩FE=F and restriction gives `Gal(AE/FE)≅Gal(A/F)`; the former is a subgroup of Gal(AE/E), so G is itself abelian. In the first case H has index one or two.

For an irreducible complex representation π of G, restrict to H and choose an occurring one-dimensional character λ. If its G-orbit has size two, Clifford theory and Frobenius reciprocity give `π≅Ind_H^G λ`. If the orbit has size one, λ extends to G when H has index two: choose t∉H and a square root of λ(t²), and define the extension on h and t; invariance of λ proves the relations. Thus π is one-dimensional in the latter case. In the induced case λ is nontrivial: induction of the trivial character contains the trivial G-representation and cannot be irreducible of degree two. Artin induction at every place identifies

    L_F(s,π)=L_FE(s,λ)                                        (3)

in the degree-two case. This is an entire nonprincipal Hecke L-function. Every nontrivial one-dimensional π likewise has an entire Hecke L-function over F. Hence all nontrivial irreducible Artin factors are entire without invoking Artin's general holomorphy conjecture.

The regular factorization is the meromorphic identity

    ζ_A(s)=∏_{π∈Ĝ} L_F(s,π)^(dim π).                         (4)

All factors are holomorphic away from 1. Since ζ_A has no zeros in the given half-plane, none of the factors can vanish there: there are no poles available to cancel zeros. At s=1 the classical nonvanishing theorem for nonprincipal Hecke L-functions, together with (3), shows that every nontrivial irreducible factor is nonzero; the trivial representation contributes the simple pole of ζ_F. Decomposing an arbitrary ρ into irreducibles yields the stated pole order and nonvanishing. The functional equation for ρ and its contragredient, whose archimedean gamma factors have no zeros or poles in 0<Re s<1, supplies the reflected strip. □

For every intermediate field F⊂L of an extension L/E which is abelian, FE/E is itself abelian; choosing A=F above proves the inherited zero-free half-plane for ζ_F, whether or not F contains E. It is essential that (1) supplies nonvanishing of the *full* ζ_AE. An estimate only for the relative quotient ζ_AE/ζ_E would not prove the same statement without separate control of ζ_E.

## Examples

1. Let F=Q(∛2), and let C=Q(ζ₇)^+ be the cyclic real cubic subfield of Q(ζ₇). The fields F and C intersect in Q, so A=FC is cyclic cubic over F. Since E(∛2)/E and EC/E are cyclic cubic, AE/E is abelian. Both nontrivial cubic Hecke characters of F associated to A/F therefore inherit the assumed E half-plane. The base F is a non-Galois cubic field and does not contain E.

2. Let A=Q(ω,∛2,∛3) and F=Q(∛2). In E, the valuations of 2 at the inert prime (2) and of 3 at (1−ω) are respectively 1 and 2 modulo 3; their Kummer classes are independent. Thus Gal(A/E)≅C₃×C₃. Since [A:Q]=18 and [F:Q]=3, Gal(A/F) has order 6, and the cubic-root action together with complex conjugation makes it S₃. Its unique irreducible two-dimensional Artin L-function over the non-Galois cubic base F is entire and inherits the assumed half-plane.

The two-dimensional factor in the second example is also the standard L-function of the dihedral automorphic induction from the quadratic extension FE/F, by cyclic automorphic induction. This is an inherited Artin/automorphic consequence of the E input, not an independent analytic zero-free improvement. For example, substituting the staged θ=0.8738694 is conditional on that candidate's admission, its source closure and its identification with conventional finite-order E-Hecke L-functions; the calculation above applies equally to any other validated E-Hecke boundary.

**Independent review.** Families checked the compositum intersections, ζ_A transfer through the entire quadratic factor, index-two Clifford theory and Hecke induction, regular factorization without pole cancellation, both examples, and the gamma factors in the reflected strip. The review does not establish the assumed E-Hecke input.

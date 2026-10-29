# Artin nonvanishing for Galois groups abelian over Q(ω)

**Status.** A classical representation-theoretic transfer from assumed Dirichlet and Eisenstein-field Hecke zero-free strips. It does not independently establish either source strip, and it makes no priority claim. The staged tracker candidate at `θ=4369351/5000000=0.8738702` has a compiled Dirichlet assertion using dependency caches; the separate [finite-Hecke corollary](../2026-10-29-arvi-return/HeckeCorollary.lean) is prepared but its displayed source comment says it has not been compiled. A fresh dependency-closure check and the conventional-L-function interpretations remain verification gates. The earlier quasi-RH source asserts the analogous 7/8 strips; the transfer below is already available from those inputs at that boundary.

## The theorem under explicit hypotheses

Fix `0<θ<1` and E=Q(ω). Assume:

1. ζ(s) and all nonprincipal primitive Dirichlet L-functions have no zeros in `Re s>θ`, with ζ's pole at 1 allowed.
2. Every nontrivial finite-order Hecke L-function over E has no zeros in `Re s>θ`.

Let L/Q be any finite Galois extension containing E for which L/E is abelian. For every finite-dimensional complex representation ρ of `G=Gal(L/Q)`, its Artin L-function is meromorphic on C and has no zeros in `Re s>θ`. Its only pole there is at s=1, of order `dim ρ^G`. In particular, for a nontrivial irreducible ρ, the Artin L-function is entire and nonzero in that half-plane. The completed functional equation also excludes nontrivial zeros from `0<Re s<1−θ`, since the same statement applies to the contragredient representation.

The claim is simultaneous in L and ρ and gives no uniform lower bound on absolute values. It is not a nonvanishing theorem for arbitrary nonabelian Galois groups.

## Proof

Put `H=Gal(L/E)`. It is an abelian normal subgroup of index two in G. Every irreducible complex representation π of G has dimension one or two. To see this, restrict π to H and choose an occurring one-dimensional character λ. Its G-conjugacy orbit has size one or two. Clifford theory says the restriction is supported on that orbit. If the orbit has size one, λ is G-invariant and extends to G: choose t∈G\H and a square root z of λ(t²), then define the extension by its values λ on H and z on t. The relation `t h t^(−1)` and invariance of λ verify the group law. Tensoring by the two characters of G/H gives its two extensions, so irreducibility forces π to be one-dimensional. If the orbit has size two, Frobenius reciprocity and irreducibility give

    π ≅ Ind_H^G λ,      λ≠λ^t.                                (1)

The one-dimensional π are finite Dirichlet characters under class field theory over Q, with the trivial character giving ζ. For (1), Artin induction and class field theory over E give the exact equality of complete L-functions

    L(s,π,L/Q)=L_E(s,λ).                                      (2)

The character λ is nontrivial, since the trivial character is G-invariant. Thus every nontrivial irreducible factor is a nonprincipal primitive Dirichlet L-function or a nontrivial finite-order E-Hecke L-function, and is entire and nonzero in the assumed strip. Equality (2) is Artin induction at every place, including ramified inertia factors; no unrecorded Euler factors are deleted. Decompose ρ into irreducibles and multiply their Artin L-functions. Each trivial summand contributes one ζ pole, while all other factors are nonzero at 1, proving the pole order and nonvanishing. The functional-equation reflection gives the left strip. □

## Example and source qualification

Take L=Q(ζ₃,∛2), whose Galois group is S₃ and whose subgroup over E is C₃. The irreducible degree-two representation is induced from either nontrivial cubic character of `Gal(L/E)`, so its Artin L-function is the corresponding cubic E-Hecke L-function. The sign representation is the quadratic Dirichlet character of E/Q. Under the stated hypotheses, each of these factors is nonzero for `Re s>θ`, and the regular representation gives

    ζ_L(s)=ζ(s)L(s,sign)L(s,π₂)^2.

Taking θ=4369351/5000000 transfers the staged candidate only if **both** its conventional all-Dirichlet and all-relevant finite-order E-Hecke interpretations are justified and their source dependency gates are closed. The prepared Hecke corollary linked above must not be described as a checked conventional-Hecke theorem on the basis of this note. The former 7/8 quasi-RH input would give the same family at θ=7/8. The difference in θ is inherited from the candidate and is small; no independent or significantly new zero-free-region proof is asserted.

**Independent review.** The index-two Clifford argument, extension of an invariant character, Artin induction including ramified places, pole order, and functional-equation reflection in the open critical strip were checked independently. The conclusion remains conditional on the two stated source strips and their conventional L-function interpretations; this review does not verify the staged Lean dependency closure.

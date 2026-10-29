# Invariant Hecke characters over cyclic Eisenstein extensions

**Status.** A classical transfer from an assumed finite-order Hecke zero-free strip over E=Q(ω); no new analytic estimate, individual improvement, or priority claim is made. The staged numerical tracker candidate and its conventional-Hecke interpretation remain subject to the verification gates in the [Hecke-scope note](../2026-10-29-hecke-candidate-scope/README.md). The underlying method also transfers any previously established E-Hecke strip.

Let F/E be a finite cyclic extension and let χ be a finite-order Hecke character of F invariant under Gal(F/E). Suppose every nontrivial finite-order Hecke L-function of E is nonzero in Re s>θ, and that ζ_E has no zeros there, allowing its pole at s=1. Then L_F(s,χ) has no zeros in Re s>θ; it is entire if χ is nontrivial and has a simple pole at s=1 if χ=1. The corresponding imprimitive L-function, after deleting finitely many Euler factors, has the same conclusion in this half-plane. No uniform lower bound for its absolute value is asserted.

For example, F=Q(ζ₉) is cyclic of degree three over E. Every Gal(F/E)-invariant finite-order F-Hecke character is covered, assuming the stated E-input. With χ=1, this gives the corresponding zero-free strip for ζ_F. The conclusion applies only to invariant characters; arbitrary finite-order Hecke characters of F need not be invariant.

## Proof

By global class field theory, regard χ as a finite-order character of the abelianized absolute Weil group of F, equivalently as a finite character of Gal(A/F) for its finite cyclic class field A/F. For any lift of σ∈Gal(F/E), invariance of χ makes its kernel stable under conjugation; hence A/E is Galois. Write G=Gal(A/E), H=Gal(A/F), and let λ be the faithful finite character of H corresponding to χ. Then H is normal, G/H≅Gal(F/E) is cyclic, and λ is invariant under G.

Choose t∈G mapping to a generator of G/H of order n. Since t^n∈H, choose a complex nth root z of λ(t^n). Define

    λ̃(h t^j)=λ(h)z^j    (h∈H, 0≤j<n).

Invariance ensures compatibility with t h t^−1, and z^n=λ(t^n) ensures compatibility with the t^n relation, so λ̃ is a well-defined one-dimensional character of G extending λ. It has finite order. This is the cyclic-quotient case of H²(C_n,C×)=0, but the explicit construction also records the finite-image condition.

Class field theory attaches to λ̃ a finite-order Hecke character ψ of E whose pullback to F is χ. If η ranges over the n characters of Gal(F/E), inflated to G and identified with their E-Hecke characters, then the regular representation of G/H gives

    Ind_H^G λ = ⊕_η (λ̃⊗η),
    L_F(s,χ) = ∏_η L_E(s,ψη).                                    (1)

Artin formalism gives (1) at all places, including ramified primes, with primitive L-functions. If χ≠1 then no ψη is trivial, because its restriction to H equals λ; all factors are entire and nonzero by hypothesis. If χ=1, exactly one ψη is trivial and its factor is ζ_E; all remaining factors are nonzero and holomorphic at s=1. This proves the pole order and nonvanishing.

Deleting a finite Euler factor multiplies the primitive L-function by `1−α(Np)^(−s)` with |α|≤1 (or by 1); such a factor has no zero in Re s>0. Therefore the same strip conclusion holds for finite imprimitive presentations. □

## Scope and inherited input

The strip is inherited: the proposed candidate θ=4369351/5000000 would yield this result only after its source dependency closure and conventional finite-order E-Hecke interpretation are checked. PR94 already carries the same implicit E-Hecke family parameter, so the transfer itself gives no improvement beyond whichever underlying strip is used. The hypothesis on ζ_E can be replaced by the corresponding nonvanishing of ζ and its fixed quadratic Dirichlet factor. The argument provides no claim for non-cyclic F/E or for characters with a nontrivial Galois orbit.

**Independent review.** A second researcher checked kernel stability, the explicit finite-image extension, all-place induction, pole orders and imprimitive Euler factors. The review is conditional on the stated E-Hecke strip and does not verify the candidate's formalization or source dependency closure.

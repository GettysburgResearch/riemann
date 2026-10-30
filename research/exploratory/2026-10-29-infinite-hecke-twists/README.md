# A zero-free region for nonparallel Hecke twists of Artin L-functions

**Status:** Proposed transfer of published GL(1) zero-free regions; requires independent review of the normalization, local induction identity, and literature. This is not a new fixed zero-free half-plane.  
**Scope:** Finite-image Galois representations over any number field, twisted by specified infinite-order unitary Hecke characters. Automorphy of the twisted representation is not assumed.  
**Novelty:** No priority claim. Both Brauer induction and the Hecke input are classical mechanisms; the precise corollary and its parameter cost need prior-art review. Recent preprints claim much stronger fixed half-planes, but their analytic proofs are not used or audited here.  
**Smallest remaining gap:** Independently check the cited theorem's normalization and the construction of its analytic conductor, and compare existing twisted-Artin results.

Let k be a number field and let λ be a unitary Hecke character whose restriction to the norm-one idele class group C_k^1 has infinite order. Let K/k be a finite Galois extension with group G and ρ a finite-dimensional representation of G. Pick any integer Brauer decomposition

    ρ = Σ_j a_j Ind_{H_j}^G χ_j,

where χ_j is a finite-order linear character of H_j, and set F_j=K^{H_j}. Define the unitary Hecke characters

    θ_j = (λ ∘ N_{F_j/k}) χ_j,

with χ_j interpreted by global class field theory, and write uniquely

    θ_j = θ_j^* |·|_{F_j}^{i τ_j},    τ_j∈R,

where θ_j^* is normalized to be trivial on the embedded positive real component of C_{F_j}. We use the idelic norm convention `|varpi_v|_v=(Nv)^(-1)`, so the displayed shift has the stated plus sign. Let C(θ_j^*)≥3 be its analytic conductor in the convention of the theorem cited below. Then L(s,ρ⊗λ), understood as the finite Euler-product Weil/Artin–Hecke twist and its meromorphic continuation, is holomorphic and nonzero wherever every j satisfies

    Re(s) ≥ 1 − 1 / [165 log(C(θ_j^*) (3+|Im(s)+τ_j|)^[F_j:Q])].   (1)

If ρ is zero, the assertion is trivial. Any valid Brauer decomposition gives a region; their union is also valid. The region depends on the individual inducing fields, conductors and norm phases; no conductor bound purely in terms of K and λ is asserted.

## Proof

The diagonal embedding C_k→C_{F_j} sends norm-one classes to norm-one classes and satisfies N_{F_j/k}(x) = x^[F_j:k]. The restriction of χ_j to that embedded subgroup has finite order. If θ_j^* were self-dual, then as a unitary GL(1) character its square would be trivial; equivalently θ_j² is a norm power, trivial on C_{F_j}^1. Restricting to embedded C_k^1 would force λ^{2[F_j:k]} to have finite order there, contradicting the hypothesis. Thus every normalized θ_j^* is non-self-dual and nontrivial.

Theorem 1.1 of [Wattanawanichkul (2026), *A metric approach to zero-free regions for L-functions*](https://doi.org/10.1007/s40879-026-00913-5), applied at GL(1), states that a normalized unitary θ_j^* has no zeros in

    Re(z) ≥ 1 − 1/[33(2·1+3) log(C(θ_j^*) (3+|Im z|)^[F_j:Q])],

except possibly a simple real zero only if θ_j^* is self-dual. That exception is absent here. The nontrivial character θ_j^* has an entire Hecke L-function, and L(s,θ_j)=L(s+iτ_j,θ_j^*), which yields (1) for every factor. The normalizing τ_j is essential: the statement does not assert that a shift of a real character loses a possible exceptional zero.

Brauer induction, the projection formula, and Artin–Hecke local induction yield the meromorphic identity

    L(s,ρ⊗λ) = ∏_j L_{F_j}(s,θ_j)^{a_j},

including the ramified finite local factors. It holds in the half-plane of absolute convergence and continues meromorphically. On the intersection (1), every factor is holomorphic and nonzero, so the integer product and quotient is holomorphic and nonzero. □

As a concrete nonparallel source, take k=Q(i) and let λ((α))=(α/|α|)^4 on nonzero principal ideals; this is well-defined because the fourth powers of the units are 1. Its angular type is nonzero and its norm-one restriction has infinite order. The theorem applies to every finite Galois K/k and every finite-image ρ, and to further finite-order twists of λ. It does not apply to a pure norm-power twist of a finite-order Hecke character, including the generic situation over Q.

# Fixed unitary twists of the natural n-free density theorem

**Status.** A source-qualified extension of [the direct n-free density result](../2026-10-29-direct-nfree-density/README.md), based on the same printed FHL/Θₙ inputs and the fixed-field Hecke detector proof. It introduces no new individual zero-free region. The fixed twist and its archimedean parameters must be fixed before X grows; no conductor-only uniformity in a varying infinity type is claimed.

Fix K containing μ_n, a fixed FHL family `{χ_u}` of good n-free ideal indices, and one fixed unitary Hecke character ν of K. The infinity type of ν may include nontrivial angular and norm-twist components; its finite conductor and all archimedean parameters are fixed. Let `N_ν(σ,T;u)` count zeros, with multiplicity, of the primitive L-function inducing the zero-extended product νχ_u. For each ε>0 there is τ>0 such that the same natural-label estimates as in the direct theorem hold:

* For n≥4 and `1/2+1/n<σ<1−1/(2n)`, with δ=2σ−1,

      Σ_{Nu≤X; u n-free} N_ν(σ,X^τ;u)
        ≪_{K,S,n,ν,σ,ε} X^[R_n(σ)+ε],
      R_n(σ)=2/n+3(n−3)(1−1/n−δ)/[n(3−δ)−7].             (1)

* For n≥3 and `1−1/(2n)<σ<1`, put h=2(1−σ). Then

      Σ_{Nu≤X; u n-free} N_ν(σ,X^τ;u)
        ≪_{K,S,n,ν,σ,ε} X^[10h/(4+nh)+ε].                    (2)

The row sums retain the fixed source good set S. The implied constants and τ can depend on ν, including its finite conductor and infinity type. Each estimate counts primitive zeros; finite deleted Euler factors are nonzero for Re s>0. If ν is fixed and ramified at primes outside S, we do not silently enlarge S and lose rows.

## Uniform detector and the possible pole

At each place, the conductor of the product is bounded by the lcm of the individual conductors. The FHL local inputs give

    Nf_{νχ_u} ≪_ν Nrad(u) ≪_ν X,

and the radical of the extra zero factors in the original product is at most a fixed ν-dependent factor times Nrad(u). Every induced character has the **same fixed archimedean parameters as ν**; a conjugate row has their fixed conjugates. The standard Hecke functional equation, fixed-field strip estimates and gamma-factor bounds used in the linked detector proof therefore remain uniform in u with constants depending on ν. The selected-zero buffering, height budget, Gamma-convolution and common-profile Sobolev steps are unchanged except for those fixed constants.

An induced unitary Hecke L-function has a pole only when the inducing character is a pure norm character `|·|^{it₀}`. Such a pole-bearing product can occur for only finitely many u. Indeed, outside the fixed union of S and the primes dividing f_ν, every prime dividing a good n-free u contributes nontrivial tame ramification to χ_u and is unramified for ν. Thus a pure-norm product has u supported on the finitely many primes of f_ν outside S, with exponents in `{0,…,n−1}`. If S contains all primes of f_ν, the unit ideal is the only possible index. Treat these finite rows separately: their primitive L-functions are fixed norm translates of ζ_K and have at most `O_ν((T+1)log(T+3))` zeros in the fixed strip. Their contribution is absorbed by selecting τ sufficiently small. All other primitive product L-functions are entire, so the detector's Gamma-contour shift crosses no additional L-pole.

## Moment reduction and limits of scope

In each common detector profile the twist appears only through `ν(a)` in the column coefficient, with modulus at most one and zero at its fixed ramified primes:

    Σ_a c_a ν(a)χ_u(a).

The n-free Θₙ bound applies to this common vector with the same ℓ² estimate. Convolution of any fixed ordinary-block power remains an ideal Dirichlet polynomial for the character νχ_u; after `a=a₁v²` with a₁ squarefree, `(νχ_u)(v²)` is a row contraction, and ν(a₁) is a common coefficient. Shared-prime zeros are preserved. For the conjugate presentation, conjugate the whole twisted coefficient vector; there is no relabeling of u. The original detector face algebra and the exact comparisons then prove (1)–(2).

Good squarefree labels coprime to the fixed conductor of ν supply ≫X distinct primitive twisted characters: multiplication by ν is injective, and their good tame conductor supports distinguish the underlying χ_u. Thus (1)–(2) give density-one statements in this fixed twisted family, with no implied all-height zero-free claim.

The de Faveri Corollary 1.5 comparison in the direct note is for its stated FHL family and is not automatically a prior-art comparison for an arbitrary angular ν. The Khale et al. conductor-family comparison applies as stated only within its fixed Galois-field, finite-order scope; for arbitrary fixed infinite type, the twist must be matched to that source's permitted archimedean modes before making a comparison. Finally, a genuinely infinite-order twist does not generally define a finite cyclic extension, so the Artin-field consequences of the untwisted prime-order family do not automatically transfer.

**Independent review.** Families checked the fixed conductor and archimedean uniformity, the finite pole-row argument, common coefficients and original masks, distinctness and the stated comparison and field-scope limits.

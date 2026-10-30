# A source-52 dihedral family at the unbalanced cubic box

**Status.** A conditional Artin/automorphic consequence of [rStation paper 52 v5, Theorem 5.7](https://rstation.ai/problems/riemann_hypothesis/papers/52), whose natural-index zero-density theorem is claimed for the Eisenstein principal-twist cubic family. That preprint and its proof inputs are not independently validated here. Classical class field theory and automorphic induction are also used. This is a density-one rectangle for a selected family, not an individual zero-free region, and no exhaustive priority claim is made.

Let E=Q(ω), let S be the fixed source good set, and choose distinct rational primes q_A,q_B splitting in E with prime ideals A|q_A, B|q_B in fixed positive-width boxes

    NA≈X^(1/32),  NB≈X^(31/32),   g=AB².                     (1)

Let χ_g be the source's primitive cubic Hecke character. It has exact order three, conductor norm ≍X and fixed finite bad-prime part. Since q_A and q_B are distinct and split, conjugation of E/Q moves each good conductor prime to the other prime above the same rational prime; hence χ_g and its E/Q Galois conjugate χ_g^c are distinct. Define

    ρ_g = Ind_(W_E)^(W_Q) χ_g.                                (2)

Mackey's criterion makes ρ_g irreducible of dimension 2. Complex conjugation interchanges the two induced lines, so ρ_g is odd. Its projective image is S₃: the ratio χ_g/χ_g^c is a nontrivial cubic character, and the other coset acts on it by inversion. Classical theta series/automorphic induction supplies a dihedral holomorphic weight-one cuspidal GL₂ representation π_g with the same standard L-function and conductor

    L_Q(s,ρ_g)=L_E(s,χ_g),   N(ρ_g)=3·N_E f(χ_g) ≍ X.          (3)

There are ≫X/(log X)² distinct ρ_g, and the corresponding π_g are also distinct: the split-prime theorem supplies that many labels, their good tame local exponents identify A and B, and an induced isomorphism class has at most two inducing characters by restriction to W_E.

Assuming the source theorem, for every ε>0 there is τ>0 such that at most

    O_ε(X^(11/16+ε))                                           (4)

of these distinct Artin representations, equivalently their GL₂ inductions, have a zero in `Re s≥4/5`, `|Im s|≤X^τ`. The comparison with the denominator gives a density-one zero-free rectangle for this family. It does not assert that every individual representation has the rectangle uniformly in X.

## Transfer from the natural-index theorem

The conjugate cubic presentation is `g′=A²B`, with `Ng′≈X^(33/32)`. Source multiplicativity and the original zero extensions give χ_(g′)=barχ_g on good ideals, so the primitive inducing L-functions have identical zero counts in symmetric height windows. The source's Theorem 5.7 states the natural-index exponent

    D(σ)=(8−7σ)/[3(2−σ)],   D(4/5)=2/3,

at a sufficiently small P-power height, for the principal finite-twist Eisenstein family. Applying it at P≈X^(33/32) gives `(33/32)(2/3)=11/16`, and shrinking τ absorbs its positive height exponent and fixed scale factors. This is a direct restriction of the source's nonnegative zero sum; no extra generalized quartic sieve or short-detector replay is used in this transfer. The source theorem counts repeated natural presentations and principal rows, which only enlarges its sum. Finite S Euler deletions do not create zeros in Re s>0.

De Faveri's [Corollary 1.5](https://arxiv.org/abs/2610.04045v1) gives natural-index exponent 8/11 at this σ, leading to 3/4 after the same reordering. The conditional unbalanced cubic detector in the [companion note](../2026-10-29-unbalanced-cubic-density/README.md) gives 23/32, also weaker than (4) in this principal-twist Eisenstein case. Neither comparison is an exhaustive search of zero-density estimates for this selected dihedral family, and the cited source theorem itself remains an imported preprint claim.

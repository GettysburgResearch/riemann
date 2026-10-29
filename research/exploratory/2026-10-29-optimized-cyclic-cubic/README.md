# An unbalanced cyclic-cubic relative-zeta family

**Status.** Source-qualified conditional class-field consequence of the [unbalanced cubic box](../2026-10-29-unbalanced-cubic-density/README.md). Its rectangular sieve is de Faveri's printed cubic Proposition 8.1, but its buffered detector, rowwise-profile/height transfer and source preprint remain dependencies not independently established here. This is a family-density statement for a relative quotient, not an individual zero-free region or a claim for the full ζ_L. A later claimed cubic natural-index theorem gives a stronger comparison on the Eisenstein specialization below, so no record or priority claim is made.

Fix K containing μ₃ and the source good set S. Let A,B be distinct good prime ideals in fixed positive-width boxes

    NA≈X^(1/32),   NB≈X^(31/32),   g=AB².                    (1)

The primitive source character χ_g has exact order three, with good conductor AB and uniformly bounded bad part, so its conductor norm is ≍X. Class field theory associates a cyclic cubic extension L_g/K. For every ε>0, the cited cubic box and detector inputs supply τ>0 for which at most

    O_ε(X^(23/32+ε))                                           (2)

of these **distinct fields** have a zero of the relative quotient in `Re s≥4/5`, `|Im s|≤X^τ`. There are `≫X/(log X)²` fields in the boxes (1), so a proportion tending to one has no quotient zero in the stated rectangle.

Indeed Artin formalism yields the entire product

    ζ_(L_g)(s)/ζ_K(s)=L_K(s,χ_g)L_K(s,χ_g²).                  (3)

Because χ_g has order three, χ_g² is the complex conjugate character. Its zeros are conjugate to those of χ_g, so in a symmetric height window the exceptional sets and zero counts agree. There is no separate quadratic core. The zero count with multiplicity dominates the number of exceptional labels, which dominates the number of exceptional fields. Distinct A,B labels give distinct primitive characters: the good tame exponent is 1 at A and 2 at B. A cyclic cubic field has exactly two nontrivial characters, so field fibers have size at most two. The prime ideal theorem gives the denominator.

At σ=4/5, δ=2σ−1=3/5, the two active box constraints of the unbalanced-detector minimax meet at `t=15/16`, giving `1−δt/2=23/32`. Choosing bin and height losses sufficiently small gives (2) with ε. This is an import of the detector replay, not a statement that its worst-case witnesses are realized.

## Absolute discriminant and source comparisons

The conductor–discriminant identity and equality of conductors under conjugation give

    |D_L| = |D_K|³ [N f(χ_g)]² ≍ X².                          (4)

For the union over all scales satisfying (1), at most `O_ε(Y^(23/64+ε))` distinct fields of `|D_L|≤Y` have a relative-quotient zero in `Re s≥4/5` and a sufficiently short Y-power height window. Conversely ≫Y^(1/2)/(log Y)² such fields are obtained by selecting sufficiently small positive-width boxes at X≈Y^(1/2). To get a common Y-height in the upper bound, split X dyadically: bound X≤Y^u by the total label count, with fixed `0<u<23/64`, and choose the Y-height exponent below u times the box detector's admissible X-height exponent on the remaining dyads. Summing dyads and absorbing fixed constants gives the stated exponent.

For an explicit comparison, the conjugate presentation is `g′=A²B`, with `Ng′≈X^(33/32)` and identical symmetric zero count. De Faveri [Corollary 1.5](https://arxiv.org/abs/2610.04045v1) has natural-index exponent 8/11 at σ=4/5, so this reordering gives `X^(3/4+ε)` before height loss, or discriminant exponent 3/8. The conditional box exponent 23/32 is strictly smaller than that particular comparator.

However, for K=Q(ω) with the principal source family, [rStation paper 52 v5, Theorem 5.7](https://rstation.ai/problems/riemann_hypothesis/papers/52) **claims** the stronger natural-index exponent 2/3 at σ=4/5. The same conjugate presentation would give `X^(11/16+ε)` before height loss, or discriminant exponent 11/32. That claimed source has not been independently validated here; at sufficiently small polynomial height it dominates (2). Its statement is specific to the Eisenstein principal-twist setting, so it should not silently be used for arbitrary K or unrelated twists.

The controlled object in (3) is the relative quotient. A zero of the fixed base ζ_K persists in ζ_L, and nothing here removes it. These comparisons and the field consequence inherit the cited detector/source qualifications.

An independent review checked the box exponent and detector scale, conjugate-character masks, field fibers, discriminant and height split, and both named source comparisons, conditional on their analytic inputs.

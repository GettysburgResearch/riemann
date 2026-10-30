# A source-dependent density bound for an optimized cyclic quintic family

**Status.** This applies the [optimized conjugate-box estimate](../2026-10-29-optimized-monomial-box/README.md) to all four generators of each cyclic quintic extension. The generalized rectangular sieve, the long buffered detector and their uniform profile/height transfers are source-qualified replays, not independently established theorems here. No individual zero-free region or unconditional novelty claim is made. Independent review requested.

Let K=Q(ζ₅), and let S and `{χ_a}` be the order-5 FHL family of [De Faveri v1](https://arxiv.org/abs/2610.04045v1). For a conductor parameter X, take good prime ideals A,B in fixed annuli

    NA ≍ X^(1/21),      NB ≍ X^(20/21),

and form `χ=χ_(A B⁴)`. The original zero extensions are retained; the primitive character underlying χ is denoted by the same symbol. Its local components at A and B have order 5, while its bad-prime conductor is bounded in terms of fixed S. Thus its primitive conductor f satisfies `Nf≍X`, with constants independent of A,B. It has order exactly 5, so class field theory gives a cyclic extension L/K of degree 5.

For each j∈{1,2,3,4}, define a whole new family `χ_a^(j)=χ_a^j`. This family is covered by the same fixed-order source hypotheses: De Faveri Remark 2.1 states that changing the fixed embedding K→C raises the nth residue symbol to an arbitrary unit power modulo n, and §2.3.4 constructs χ_a directly from those symbols. Since every j is invertible modulo 5, `χ_a^(j)` is precisely the same FHL construction using the corresponding embedding. All finite ray reciprocity phases and fixed bad-prime data are raised to the jth power, leaving a fixed finite collection of sectors. For each good row ideal q, including its zero mask,

    χ_(A B⁴)(q)^j = χ_A^(j)(q) overline(χ_B^(j)(q))
                   = χ_q^(j)(A B⁴) × a fixed-sector reciprocity phase. (1)

The last phrase refers to the same finite ray correction already required by the source's reciprocity formula, expanded into finitely many fixed coefficients before applying the sieve. In particular one is **not** applying the original ±1 box theorem to the n-free label A²B³, which has different natural-index exponents; rather one applies that theorem to the powered FHL family. The primitive quotient-conductor, root-number and general-order large-sieve inputs have the same statements for this embedding. Thus the source-dependent rectangular sieve and long detector in the optimized-box note give, for each fixed j and each ε>0, a τ_j>0 such that

    Σ_(A,B in the prescribed boxes) N(4/5, X^τ_j; χ^j)
         ≪ X^(23/35+ε).                                    (2)

The same conclusion follows for `j=4` from conjugation and for `j=3` from conjugating j=2, but j=2 still requires the powered-family argument above. Choose a single positive τ smaller than all four τ_j; the bounds survive at that common height. Their constants may depend on K,S,j and ε.

The local kernel of χ^j equals that of χ at every place, since j is a unit modulo 5. Therefore the primitive conductors of all four nontrivial powers coincide exactly, including at the fixed bad primes. Artin factorization and the conductor–discriminant formula give

    ζ_L(s)/ζ_K(s) = ∏_(j=1)^4 L_K(s,χ^j),
    |D_L| = |D_K|^5 (Nf)^4 ≍ X^4.                         (3)

The four factors are entire, and the zeros of the quotient in the stated rectangle occur among their zeros. Summing (2) gives at most `O(X^(23/35+ε))` exceptional characters, and hence no more exceptional fields. Distinct pairs A,B give distinct characters: their two distinct-scale good prime supports and their local exponents distinguish the labels. Each degree-5 cyclic field has only four nontrivial character generators, so the character-to-field map has fibers of size at most 4. The prime ideal theorem gives ≫X/(log X)² such pairs; rescale the box constants to obtain absolute discriminant ≤Y with `X≍Y^(1/4)`.

Consequently, for every ε>0 there is a sufficiently small τ′>0 and a specified family of ≫`Y^(1/4)/(log Y)²` cyclic quintic extensions L/K with `|D_L|≤Y`, such that at most

    O_(ε,K,S)(Y^(23/140+ε))                                (4)

have a zero of `ζ_L/ζ_K` in `Re s≥4/5`, `|Im s|≤Y^τ′`. Choose τ′ strictly below one quarter of the common τ in (2), allowing the fixed discriminant rescalings. This statement uses the single top-scale box; extending it to all smaller boxes at one common height requires a separate small-label split. In particular this is a density-one statement **within the specified box-generated family**. The fixed base factor ζ_K is excluded from the quotient, and no zero-free claim for ζ_L itself follows.

For comparison, De Faveri Corollary 1.5 gives `23/35` on squarefree natural labels, a different subfamily; the n-free mixed labels above require index reordering and the power j=2 introduces further natural-index loss. This comparison does not establish priority. The field-count asymptotic in Chen An's preprint has a separately identified issue over K containing μ₅, as discussed in the [source audit](../2026-10-29-cyclic-field-count-source-audit/README.md); this note uses only the explicit prime-pair lower bound and the four-to-one character/field count.

**Independent review:** Families and High_match checked the power-family algebra, zero masks, conductor equality and field-count steps under the cited source inputs, and identified the small-dyad height issue that led to the single-box formulation above.

# Prior bounds for the optimized cyclic relative-zeta families

This targeted comparison concerns zeros with `Re s≥4/5`, symmetric height `|Im s|≤T`, and discriminant-ordering. It does not certify novelty or the proofs of recent preprints. The proposed bounds depend on the replays stated in the [prime-degree note](../2026-10-29-optimized-prime-cyclic-relative-zeta/README.md) and [quartic note](../2026-10-29-optimized-cyclic-quartic/README.md).

## Direct natural-index comparison for cyclic p-extensions

In [De Faveri v1, Corollary 1.5](https://arxiv.org/abs/2610.04045v1), order-p FHL characters are summed over all **p-free natural labels** of norm ≤N. At σ=4/5 it gives

    Σ_{Na≤N}^{p-free} N(4/5,T;χ_a)
      ≪ N^(D_p+ε) T^(1+[K:Q]/7+ε),
    D_p=(12p²−38p+5)/(21p²−80p+50).                       (1)

To apply this to every nontrivial factor of ζ_L/ζ_K for the optimized family, use the entire powered FHL family `χ_a^(j)=χ_a^j` for each j=1,…,p−1. Remark 2.1 and §2.3.4 of the same source show that this is the original construction with a different embedding, so Corollary 1.5 applies with the same exponent. Conjugation gives

    overline(χ_(AB^(p−1))^j)=χ_(A^(p−1)B)^j

on good ideals with their zero masks, and it preserves the count in a symmetric height window. For box exponents a_p, 1−a_p, the label on the right has norm `≈X^[1+(p−2)a_p]`. Thus (1), summed over the p−1 generators and then over fields, directly yields the relative-zeta exceptional bound

    X^(C_p+ε) T^(1+(p−1)/7+ε),
    C_p=[1+(p−2)a_p]D_p.                                  (2)

The map from pairs to natural labels is injective (different prime scales identify A and B; when A=1, B identifies the label), so no unaccounted multiplicity is inserted. The powered construction makes (2) applicable to j=2,…,p−2 without treating A^j B^(p−j) as a larger index. For p≥11, a_p=0 and the comparator uses the squarefree label B itself.

Since absolute discriminant is ≍X^(p−1), take T=Y^τ and X≈Y^(1/(p−1)). Examples of the fixed-height exponents in the bound from (2) are:

| p | De Faveri field exponent | Proposed field exponent |
|---|---:|---:|
| 5 | 46/245 ≈ 0.18776 | 23/140 ≈ 0.16429 |
| 7 | 3052/23355 ≈ 0.13068 | 47/450 ≈ 0.10444 |
| 11 | 1039/17110 ≈ 0.06073 | 734/12375 ≈ 0.05931 |

The cited comparator's height factor becomes `Y^[τ(1+(p−1)/7+ε)]`; each listed strict gap persists for sufficiently small fixed τ. The exact positive differences and the complete formulas for all fixed p are in the optimized-box note. The cited bound is a preprint result, and the improved candidate has additional source-replay dependencies.

## Cyclic quartic extension of Q(i)

For the quartic box A≈X^(1/30), B≈X^(29/30), De Faveri (1) with n=4 gives `D₄=15/22`. Conjugating `AB³` to `A³B` changes the index bound to X^(16/15), so the two conjugate quartic factors have the direct comparator

    X^(8/11+ε) T^(9/7+ε),

or `Y^(8/33+ε)T^(9/7+ε)` because the field discriminant is ≍X³. The proposed relative-quotient bound is `Y^(17/75+ε)` at a sufficiently small power height. De Faveri's quartic theorem alone does not bound the remaining quadratic factor χ² by the same exponent: its natural label is `(AB)²`, not a squarefree AB-label in the order-4 family. Under the **same separately stated quadratic-family large-sieve and detector replay** used in the quartic note, that factor has X exponent 13/25, so the full relative-quotient comparator is governed by 8/11. This is a mixed source-conditional comparison, not a stand-alone unconditional theorem for the complete quotient.

## Broader published comparators and limits

[Khale–O’Kuhn–Panidapu–Sun–Zhang, Lemma 3.3](https://arxiv.org/abs/2008.09677v3) covers all primitive finite-order Hecke characters over the fixed Galois fields considered here, ordered by conductor norm. At σ=4/5 and fixed infinity type it gives `X T^[K:Q]/2` up to logarithms. For the quartic base Q(i), this is `Y^(1/3)T`; for K=Q(ζ_p), it is `Y^[1/(p−1)]T^[(p−1)/2]`. These exponents are weaker than (2) for the displayed examples. This is a sum of zeros over a much broader conductor family, with no claim to be optimal for the two-prime subfamily.

[Chen An, Theorem 1.1](https://arxiv.org/abs/2004.14410v2), for GL₁ over a fixed number field and a conductor-X family with ≪X^(1+η) members, gives X exponent `(15/2+O(η))(1−σ)` and height exponent `([K:Q]/2+3)(1−σ)`. At σ=4/5 this is X^(3/2+O(η)); it is weaker for these fields. Its Theorem 1.2 is an almost-all effective Chebotarev conclusion with a near-1 region depending on the loss parameter; it is not a stated σ=4/5 zero count. The printed auxiliary prime-degree field-count asymptotic has a specific cyclotomic-base issue discussed in the [independent audit](../2026-10-29-cyclic-field-count-source-audit/README.md); that issue does not automatically invalidate its separate zero-density theorem or Chebotarev claim.

[Cho and Kim (2012)](https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.812/) obtain almost-all near-1 regions for selected cyclic quartic and quintic **number fields over Q**. [Cho and Kim (2026)](https://doi.org/10.1007/s11139-026-01331-7) treat cyclic prime-degree fields over Q and use related zero-density results. These are substantial precedent but neither source statement found in this search directly covers the present cyclic extensions of Q(i) or Q(ζ_p), nor supplies a better exponent at σ=4/5 in their discriminant and height parameters. [Thorner–Zaman (2023)](https://arxiv.org/abs/1909.01338) treats Galois fields over Q and quotient ζ_F/ζ; its theorem does not directly apply to the arbitrary-base field families here. [Gao–Zhao](https://arxiv.org/abs/1708.01701) study low-lying zeros and central nonvanishing, a different statistic from off-critical zero counts.

No stronger direct comparator was located in this targeted search; this is not an exhaustive literature survey or priority finding.

**Independent review:** Families and High_match checked the powered-family bridge, natural-label reordering, p=5,7,11 exponents and height conversion, and the separately qualified quartic quadratic factor. This review is conditional on the cited source statements and is not an exhaustive prior-art search.

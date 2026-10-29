# A mixed radical and full-norm theta frame

**Status.** A source-qualified projection estimate, conditional on the fixed-field Hecke subconvexity, sextic/cubic/quadratic sieves and October 5 completed-theta mean and cube inversion recorded in the linked notes. It does not control the orthogonal complement or establish a zero-free region. Two independent source-level reviews are recorded below.

Work over the Eisenstein field with the fixed good set, ray sector, profiles, exact zeros and source vector m_P of the [theta-overlap note](../2026-10-29-cubic-theta-overlap-average/README.md). Write v_h for its directly oriented normalized-Gauss profile indexed by the sixth-free ideal h, and v⁻_h=v_{h'} for its conjugate orientation, where each good prime exponent e in h is replaced by 6−e in h'. Original nonunit zeros are retained. Choose

    H₀=P^(1/4),             H₂=P^(25/54−δ),

with fixed small δ>0 and H₀≤H₂. Form the union of the following columns, first translating every inverse-oriented label h to its actual directly oriented ideal h′ and then removing duplicate actual ideals:

* every v_h with `N rad(h)≤H₀`;
* every v⁻_h with `Nh≤H₂`;
* every v_(p²) with p good prime and `Np≤H₂`.

The p⁵ profiles with Np≤H₂ already occur in the second family as v⁻_p. The Gram matrix of the **whole** union is I+o(1). Its Möbius projection, after applying the unrestricted sextic row operator at `P=Y^(6/5)`, has energy

    ≪_ε (1+|t|)^A [Y^(23/30+ε)+Y^(1−9δ/5+ε)].                  (1)

For fixed small δ the second term dominates. Height losses require the same common detector budget as in the linked source estimates.

## The p² theta average

In the scalar product with v_(p²), complex conjugation turns its twist into `χ_s(p)^4`. The fixed-ray decomposition of `μ(s)overline(γ₁(s))` gives the cubic-theta coefficient exactly as in the theta-overlap note. The October 5 `prop:R`, with row label k=1 and auxiliary squarefree label f=p, gives uniformly for fixed polynomial ranges and X≥1

    |T(X;1,p)|² ≪_ε (PX)^ε [1+Np/X].                            (2)

The implied constants and seminorm orders are independent of p. Summing over `Np≤H₂` gives `≪(PH₂)^ε[H₂+H₂²/X]`. In the exact cube-index inversion the f=p factor contributes `χ_d(p)^{12}=1_((d,p)=1)`; it is a zero-retaining multiplier of absolute value ≤1. Thus the same weighted-Cauchy short cube estimate and pointwise elementary tail as in the theta-overlap note yield

    Σ_(Np≤H₂) |⟨m_P,v_(p²)⟩|²
       ≪_ε (PH₂)^ε P^(−1)[H₂+H₂^(3/2)](1+|t|)^A.             (3)

The norm twist is part of one fixed common profile, and its derivative cost is included in A. This argument does not establish the same averaged bound for all other prime exponents.

## Conditioning the union

The first block has at most H₀^(1+ε) columns and is conditioned by the individual Wu/Hecke Gershgorin bound in the [moving-twist note](../2026-10-29-gauss-profile-low-rank/moving-twist-overlap.md). The second and third blocks, after removing duplicates, are jointly conditioned by the [full-norm/prime-power Gram argument](../2026-10-29-theta-partial-frame/prime-power-gram.md): in its large-square split they require only the sixth-order and cubic unrestricted-row sieves, and all labels have radicals ≤H₂.

For a cross pair from the first block and the deduplicated second/third block, the quotient is nonprincipal and Wu's pairwise estimate gives, including diagonal normalizations and deleted masks,

    |G_hk| ≪_ε P^(−1/2+ε)(H₀H₂)^(103/512+ε).

The second/third block has at most H₂^(1+ε) columns. Its cross-block Frobenius norm is therefore

    ≪_ε P^(−1/2+ε)(H₀H₂)^(359/512+ε)=o(1).                  (4)

The strict exponent margin already holds at δ=0: `1/4+25/54=77/108<256/359`, with difference `5/38772`; choose all small power losses below that margin and the fixed δ. The two within-block bounds plus (4) condition the complete deduplicated union. This argument uses an operator-norm upper bound from Frobenius; it does not assert pairwise image orthogonality under the row operator.

The original reflection bound gives the first block's total squared overlap `≪P^(−1+ε)H₀²=P^(−1/2+ε)`. The theta average bounds the second block and (3) the third by `≪P^(−1+ε)H₂^(3/2)`. The conditioned Gram matrix converts their sum into a projection bound. Multiplication by the source operator squared norm `≪Y^(41/30+ε)` at P=Y^(6/5) gives (1). Its dependence on all height costs and the uncontrolled complement is as stated above.

**Independent reviews:** Other_families and Amplified_opt checked the p² source specialization and averaging, within-block conditioning, the cross-block Frobenius exponent and the tiny exact margin, and the projected-energy exponents. Deduplication must be by actual profile ideal after converting inverse-oriented labels, as now stated. The imported Hecke/theta inputs and the full complement remain unverified here.

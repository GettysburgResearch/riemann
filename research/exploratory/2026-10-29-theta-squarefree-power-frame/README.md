# A mixed frame of all squarefree-power profiles

**Status.** A proposed source-qualified extension of the [prime-power frame](../2026-10-29-theta-partial-frame/prime-power-gram.md) and [full-norm theta frame](../2026-10-29-theta-row-mean-frame/README.md). The cited theta means, local Kummer identification, reciprocity, fixed-order large sieves and Hecke subconvex bound are imported; their proofs are not independently verified here. The projection estimate does not control the orthogonal complement or imply a zero-free region. Independent review requested.

Use the fixed coefficient vector `m_P`, Gauss profiles `v_(P,h)` with source zero masks, one primary generator per ideal, and fixed ray sector of those notes. Let δ,δ₂,δ₀>0 be fixed with

    H_max=P^(1/2−δ),  H₂=P^(25/54−δ₂),
    H₀=P^(25/72−δ₀),  H_rad=P^(1/5),
    H_rad≤H₀≤H₂≤H_max.

Take the union of actual sixth-free profile labels

1. all inverse-oriented `v⁻_(P,h)` with h good sixth-free and `Nh≤H_max`;
2. all original `v_(P,R³)` for good squarefree R, `NR≤H_max`;
3. all original `v_(P,R²)` for good squarefree R, `NR≤H₂`;
4. all original `v_(P,R)` and `v_(P,R⁴)` for good squarefree R, `NR≤H₀`;
5. all original `v_(P,h)` for good sixth-free h with `Nrad(h)≤H_rad`.

The sixth-free ideal underlying each inverse-oriented profile is obtained by replacing each positive valuation e with 6−e, so deduplicate using the **actual profile ideal**, not merely the index h. In particular original `v_(P,R⁵)` for `NR≤H_max` is already included in item 1. Let V be the span after deduplication and individual normalization.

For the first four blocks, the full-norm/prime-power Gram proof extends to all squarefree R. At small square divisors, any two distinct actual labels have a good valuation differing modulo 6, and their quotient conductor Q and extra deletion radical E satisfy `QE≪rad(h₁)rad(h₂)≤H_max²`. The same Poisson bound gives power-small offdiagonal. For large square divisors, split coefficients into the full-norm block and the fixed e=1,2,3,4,5 squarefree-R blocks. Apply respectively the unrestricted-row sextic, cubic and quadratic Hecke large sieves after finite reciprocity-sector decompositions, including the row-dependent square-divisor masks as diagonal contractions. The e=3 block uses the squarefree-R quadratic sieve and its unrestricted-row consequence `X+H_max sqrt(X)`; e=2,4 use cubic and e=1,5 use sextic. A fixed Cauchy factor joins the blocks. Hence this whole deduplicated block is conditioned for `H_max≤P^(1/2−δ)` as in the earlier proof.

The separate old radical block is conditioned by the moving-profile Gram estimate. For cross blocks use the pointwise Wu bound and count the labels: each has `≪H_rad^(1+ε)` or `≪H_max^(1+ε)` labels, and

    ||G_cross||_HS ≪ P^(−1/2+ε)(H_rad H_max)^(359/512+ε).

Even ignoring δ this has a power margin `1/2−(7/10)(359/512)=47/5120>0`. Combining the two conditioned diagonal blocks with this Frobenius estimate conditions the whole union. The old radical block is essential in this last step: individual label norms can be as large as `H_rad⁵`, so it cannot simply be absorbed into the full-norm block.

The squared overlaps with `m_P`, with fixed-profile and height factors suppressed, satisfy

    item 1:  ≪ P^(−1+ε) H_max;
    item 2:  ≪ P^(−1+ε) H_max;
    item 3:  ≪ P^(−1+ε) [H₂+H₂^(3/2)];
    item 4:  ≪ P^(−1+ε) H₀²;
    item 5:  ≪ P^(−1+ε) H_rad².                            (1)

Item 1 is paper 5 v3 Theorem 5 (9.4), and item 2 is its Theorem 6 (12.2) at angular −1: the latter explicitly averages **all good squarefree R**, and sextic reciprocity changes `χ_R(n)^3` to `χ_n(R)^3` after fixed finite sectors. Item 3 follows by summing the October 5 `prop:R` over all squarefree f=R, followed by the same cube inversion as in the prime proof; its label mean is `H₂+H₂²/X`. Item 4 follows from the individual moving-reflection estimate `|⟨m,v_h⟩|²≪P^(−1+ε)Nrad(h)`, and item 5 from the same estimate and the `H_rad^(1+ε)` count. All identities retain original coprimality zeros; common profile and height orders are fixed before allocating losses.

The conditioned Gram converts (1) to a bound for the projection onto the **entire span V**. At `P=Y^(6/5)`, the arbitrary-source full-row sextic operator has squared norm `≪Y^(41/30+ε)`, so

    ||T_(Y,P) Proj_V m_P||²
      ≪ Y^[max(23/30−6δ/5, 1−9δ₂/5, 1−12δ₀/5)+ε]
          (1+|t|)^A.                                         (2)

The item-5 exponent is only `97/150` and is absorbed by the displayed maximum under the cutoff order. For `H_max≫H_rad`, the squarefree R with `NR≈H_max` contribute ≫H_max distinct independent `R³` directions beyond the earlier full-norm and radical blocks: their actual profile labels invert to themselves but have full norm `NR³≫H_max`, while their radicals exceed H_rad. This strengthens the explicit *controlled subspace* from prime powers to all squarefree powers. It does not estimate `T_(Y,P)(1−Proj_V)m_P`, its cross term, or the full Möbius moment.

The last radical cutoff may be enlarged to `H_rad=P^(153/718−η)` for any fixed η>0, provided it remains below H₀. Indeed `153/718=256/359−1/2`, so the cross Frobenius norm still has a fixed power margin, and the old radical block's own Gram and overlap estimates permit this exponent. Its energy contribution is `Y^(7303/10770−12η/5+ε)`, below the maximum in (2) under the cutoff ordering. The original `P^(1/5)` statement gives the simpler explicit cross margin above. High_match and Families independently checked this optional cutoff and its exact exponent.

**Independent review.** High_match and Families checked the all-squarefree source labels, R² and R³ theta matches, effective-order large-sieve Gram blocks, actual-label deduplication, cross Frobenius margin and energy exponents. The underlying analytic inputs remain imported.

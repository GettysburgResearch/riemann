# A source-conditional amplified numerator estimate over a fixed complex field

**Status.** This is a transfer of the argument of Xu–Sang, Proposition 5.1, to the finite-order physical numerators in Hu's fixed-field construction. It is conditional on the indicated source results and on the stated identification of physical prime coefficients; it is not a zero-free theorem and does not assert priority for the amplification method. Its purpose is to isolate one missing piece of the variable-geometry high contour. The arithmetic inputs and full zero-free proofs in the cited preprints have not been independently established here.

## Assumptions and conclusion

Fix a number field K containing the twelfth roots of unity and the finite bad set and finite character family Θ from Hu, arXiv:2610.00216v1, §4. Fix κ=3/4 and assume its Theorem 4.2, Proposition 4.14, and the finite-order zero-free premise for that moment. Assume the conductor and character identifications of Hu Proposition 3.1 and §7.1, including the displayed zeros at good primes dividing the physical row. In particular, each nonexceptional sixth-power-free row u with Nu ≍ U has a primitive nonprincipal finite-order numerator χᵤ* with Nfᵤ ≪ U; the exceptional rows whose inducing character lies in Θ have bounded norm. Assume the complete physical prime slots below match the permitted finite-character combinations and the original common masks of Theorem 4.2.

Fix a finite prime-slot system of total logarithmic length L>0 in a prescribed bounded range, with disjoint supports and each individual length at most the mesh supplied by Hu's theorem. On a class 𝔅 of physical rows Nu ≍ U, assign amplitudes 0≤gᵢ≤5/12 and suppose each slot with gᵢ>0 has magnitude at least U^((gᵢ−ε₀)ℓᵢ); zero-amplitude slots have no lower bound and may vanish. Put q=Σℓᵢgᵢ/L. The loss is relative to slot length, so its aggregate is bounded independently of the number of slots. Assume #𝔅 ≪ U^(R+ε₀) and a common height bound H≤U^τ, where τ>0 is sufficiently small in terms of the fixed field degree and the already chosen loss and profile orders. Constants may have a fixed polynomial dependence on H. For each prescribed ε>0, with mesh and binning losses chosen sufficiently small before the finite slot system, either choice

1. ϑ=qv with 0≤v≤min{L,1/(6κ)}, or
2. ϑ=q/(6κ) if R≤(6κ−2q)L,

gives

    Σ_(u∈𝔅) |L(1/2+ϑ+it,χᵤ*)|
       ≪ U^((3R+1)/4−ϑ/2+ε) (1+H)^A       (|t|≤H).

The constant and fixed A can depend on K, the fixed arithmetic data, the prescribed loss, and the fixed slot system. This statement is uniform in the specified row class and t, and is not asserted for a system with row-dependent slot coefficients. Bounded exceptional rows can instead be included in the separate small-row estimate.

## Proof from the source inputs

Put K₀=(3R+1)/4. The fixed-complex-field approximate functional equation, gamma-ratio estimates and conductor-dyad Sobolev reduction are recorded in [the companion note](../2026-10-29-fixed-field-afe/README.md). On a centrally normalized block of length U^m, both the original and dual sums carry a scalar U^(−ϑm), with the remaining fixed-parameter profiles, their finitely many derivatives, and height dependence controlled. The ideal row count and rapid profile decay permit a fixed bounded m-range after choosing τ according to the field degree. O(log U) length and conductor dyads are absorbed in U^ε.

For 0≤m≤1/2 take z=v(1−2m). Then z≤L and 2m+6κz≤1. Sort the positive slot amplitudes gᵢ in decreasing order. If their total length reaches z, a fractional initial segment of length z has weighted gain at least qz; discarding its one fractional slot loses at most a prescribed mesh error. If positive slots are exhausted earlier, their total gain is qL≥qz, and no zero slot is selected. Thus the selected slot product has squared magnitude at least U^(2qz−ε) on 𝔅. Theorem 4.2 applies to two copies of the plain block, the same selected slot product and all common masks. For the conjugate dual, conjugate the whole product, including the prime slots; absolute values and supports are unchanged. Its nonnegative row sum may be restricted to 𝔅. Consequently

    Σ_(u∈𝔅) |S_m(u)|⁴ ≪ U^(1−2qz+ε) (1+H)^A,
    Σ_(u∈𝔅) |S_m(u)|  ≪ U^(K₀−qz/2+ε) (1+H)^A,

by Hölder and the row-count hypothesis. The conductor-dependent profiles are handled on each log-conductor dyad by the one-dimensional Sobolev argument in the companion note: its derivative yields two permitted plain profiles, while the selected slot product remains the same. Hu's statement allows distinct plain profiles and the relevant fixed-character slot combinations. The zero-slot case uses the nonprincipal ordinary moment. Since ϑ=qv,

    −ϑm − qv(1−2m)/2 = −ϑ/2.

For m≥1/2, the zero-slot fourth moment gives U^(K₀+ε) and the block decay is at least U^(−ϑ/2). This proves the supply-limited case after summing blocks.

For the full-capacity case, if L≥1/(6κ) it is covered already. Otherwise set m₀=1/2−3κL. For m≥m₀ the choice z=(1−2m)/(6κ) fits the available supply and the argument above applies. For 0≤m≤m₀, the elementary ideal count gives |S_m| ≪ U^(m/2+ε)(1+H)^A, including the differentiated and dual profiles, so the total after the block coefficient is at most U^[R+(1/2−ϑ)m+ε](1+H)^A. Because ϑ≤5/54<1/2, its maximum on this interval is at m₀, and direct algebra gives

    R+(1/2−ϑ)m₀−(K₀−ϑ/2) = [R−(6κ−2q)L]/4 ≤ 0.

This proves the displayed estimate under the source inputs. The fixed excluded Euler factors are restored by splitting off their supported ideal parts, with a summable central coefficient mass, exactly as in the companion AFE note. □

## Interfaces still requiring review

The physical finite-sector identity must be checked for each main slot, including conjugation, coprimality masks, and the single shared height allowance. The moment source's coefficient, prime-support, seminorm and mesh quantifiers must hold after the conductor Sobolev step. This estimate alone does not establish the buffered dynamic contour, principal normalization, low-side reflected-energy estimate, or a zero-free region.

Sources: [Hu, arXiv:2610.00216v1](https://hexagonmath.org/2610.00216v1), Theorem 4.2 and Proposition 4.14; [Xu–Sang, arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291v2), Proposition 5.1 and Appendix B; [fixed-field AFE](../2026-10-29-fixed-field-afe/README.md).

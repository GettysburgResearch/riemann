# Director adjudication: three exact consequences of Ye's local density theorem

Date: 2026-11-17. Source: PAPER-DF62-002, arXiv:2610.15989v2, Theorem 1.1, Proposition 3.3 (especially (3.14)), and §4. Source version and PDF hash are pinned in its record. I read the exact theorem and the relevant proof passages, the complete-reading note audits/latest62_ye_fullread.md, and the independent review witness62_ye_three_corollaries.md. I independently checked the short-window inclusion, parameter balances, strict thresholds and endpoint contribution. The conclusions below accept Ye's source theorem as an external input; they are not an independent reconstruction of its complete proof or a field-priority claim.

Theorem 1.1 assumes fixed a∈(0,1], ℓ≥1, θ≥a and a 2ℓ-moment estimate of exponent θ+η on every real-start interval of length U^a. Uniformly in σ∈[3/5,1), the zero count with Re ρ>σ, inclusive height window and multiplicity is bounded by U to exponent

    (1−σ) max{15a/(3+5σ), 4θ/[ℓ(2σ−1)+4(1−σ)]}+ε.

The implicit constant may depend on the fixed parameters and ε but not σ. This uniformity is necessary for the layer arguments.

1. CAND-LATEST62-YE-SHORT-FOURTH is accepted. Positivity of the fourth-moment integrand and the classical length-U^(2/3) estimate give θ=max(a,2/3), ℓ=2, uniformly at the same real start. Thus the local density slope is max{15a/(3+5σ),2max(a,2/3)}. For a=3/5 and σ=3/4 it yields exponent 1/3+ε rather than the 10/27 obtained by covering with the longer original window. No global zero-free cutoff is used.

2. CAND-LATEST62-YE-LOCAL-BGSTB is accepted for a single height window. Fix d∈(0,2/5) and c,C>0. For U∈[cT,CT], sum e^(2y)/(1+y²), y=(Re ρ−1/2)logT, over zero copies in [U,U+U^(3/5)] and 1/2≤Re ρ≤1−d. Below 3/5 the total count O(T^(3/5)logT) times the weight bound T^(1/5) gives O(T^(4/5+ε)). Above 3/5 the local density slope is at most 3/2, so the layer exponent is

    2σ−1+(3/2)(1−σ)=1−(1−σ)/2 ≤1−d/2.

A 1/logT grid and a shifted strict counting threshold include zeros at slice boundaries with only a fixed factor cost. This proves O_(d,ε,c,C)(T^(1−d/2+ε)), hence o(T) on choosing ε<d/2. Covering a full dyadic block costs T^(2/5) windows and loses the saving. This does not prove the global weighted BGSTB premise.

3. CAND-LATEST62-YE-OSCILLATORY-27040 is accepted only with its explicitly external, unverified hypothesis that every nontrivial ζ zero satisfies Re ρ≤7/8. For fixed real α≠0 and φ∈C_c^∞((-1,1)), the pointwise smoothed prime-power sum

    Σ Λ(n) exp(2πiα n^(3/5)) φ((n−K)/K^(7/10))

is O_(α,φ,ε)(K^(27/40+ε)). It is neither an unphased prime-count estimate nor an unconditional consequence recorded here. Proposition 3.3 applies on its long-window boundary δ=1−β/2, which is equality here; the unused shorter-window formula has a different strict condition. Put β=3/5 and q=v=w0=3/10. Choose fixed η=1/200 for the zero-window length K^(61/200), and use the fourth-moment local density bound with a=13/25: its height length is K^(39/125), which exceeds K^(61/200). Its first density slope is ≤1.3<4/3, giving K^((4/5)(1−σ)+ε). For σ≤3/5 the weighted contribution is O(K^(181/200+ε)); for larger σ the maximum of σ+(4/5)(1−σ) on the allowed closed range is 39/40 at 7/8. Multiply by K^(−3/10) to get 27/40. A strict threshold just below 7/8 retains zeros exactly on the endpoint. The source baseline at the same external cutoff is 44/65; the algebraic improvement is 1/520. No assertion that this is the best known exponent is made.

All three stable identifiers retain their CAND spelling as identity, while their current status is adjudicated scoped/source-dependent. The exact next task for the third result is to validate a sufficient fixed zero-free cutoff independently, or restate the derived exponent as a function of an established cutoff. The second result requires an independent full-height estimate before it can serve the global arithmetic transfer.

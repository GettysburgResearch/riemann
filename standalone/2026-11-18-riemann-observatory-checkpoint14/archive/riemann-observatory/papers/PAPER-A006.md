# PAPER-A006 — BGSTB: unconditional pair correlation

Siegfred Alan C. Baluyot, Daniel Alan Goldston, Ade Irma Suriajaya and Caroline L. Turnage-Butterbaugh, [*An unconditional Montgomery Theorem for Pair Correlation of Zeros of the Riemann Zeta Function*, arXiv:2306.04799v1](https://arxiv.org/abs/2306.04799v1), 7 June 2023; Acta Arithmetica214 (2024), 357–376, DOI10.4064/aa230612-20-3. Accessed 17 November 2026. All 13 pages of arXiv v1 were substantively read (Level 1). The journal text is subscriber-restricted. [Full preprint audit](../audits/BGSTB_full_reading_formal62.md)

Theorem1 uses complex zeros directly. For w(u)=4/(4−u²), F(α)=(TlogT/(2π))^{-1}Σ_{0<γ,γ'≤T}T^{α(ρ−ρ')}w(ρ−ρ'), real α, the theorem states F is real, even, nonnegative and F(α)=T^{-2α}(logT+O(1))+α+O(1/√logT), uniformly 0≤α≤1. Individual summands need not be nonnegative. This unconditional formula is not the same as assuming all γ-parametrizations are real spectral ordinates.

Lemma5 (arXiv pp6–7): for fixed real even r∈L¹ supported in [−1,1], Lipschitz at0, Fourier transform convention exp(−2πizα), the weighted zero sum equals (TlogT/(2π))(r(0)+2∫_0^1 αr(α)dα+O_r((logT)^{-1/2})). Its proof integrates Theorem1; the Lipschitz assumption controls the peak near α=0. Changing r with T without tracking its norm and local Lipschitz constants is not warranted.

Theorem2 obtains 61.7% simple zeros under a narrow horizontal-box assumption for T^{3/8}<γ≤T. Theorem3 instead assumes N(σ,T)=o(T^{2(1−σ)}) for 1/2+1/(2logT)≤σ≤25/32+η, each fixed η>0 as stated. These conclusions concern simple zeros and do not locate them on the line. Quantifier/uniformity of a moving lower endpoint must be retained when applying Theorem3.

**Compatibility check:** Guth–Maynard's improved but larger density exponent does not meet this strong hypothesis, even at fixed σ=3/4 (CONN-A001). A density exponent close to2 still cannot exclude o(N) off-line zeros. Lamzouri2026 uses this paper's unconditional Lemma5 with finite conjugation-symmetric inequalities and avoids Theorems2/3's density assumption entirely.

The audit records a scoped justification defect at (6.4) in the density-tail estimate, a proposed thin-box repair using the cited external estimates, and an explicit bound for the test dependence in Lemma 5. The density-only route and the published version remain open to further checking.

Current director update,17November2026: the retained-denominator weighted tail repair is adjudicated under its exact stated density inputs; see audits/adversarial_reviews/director_weighted_density_round6.md. The journal manifestation, current-source corrections and full global premise remain separate. Earlier proposed-repair wording records its historical status.

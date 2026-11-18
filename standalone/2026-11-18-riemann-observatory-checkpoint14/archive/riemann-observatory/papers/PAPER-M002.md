# PAPER-M002 — The General Theory of Dirichlet's Series

G.H.Hardy and Marcel Riesz. Cambridge University Press,1915. Cambridge Tracts in Mathematics and Mathematical Physics,no.18, viii+78pp. The title and series pages of the actual facsimile confirm the identity; OCR drops the final8 of18, so the series number was checked visually.

Canonical scanned source: https://archive.org/details/cu31924060184441 . Accessed2026-11-17. The original Cornell copy was digitized as a1991 preservation facsimile; this record concerns the1915 text, not the2015 reissue of the1952 reprint. No DOI or arXiv identifier is assigned here. Private working PDF: `sources/logarithmic_riesz_round3/cu31924060184441.pdf`; SHA256 `506e09782db969bbe3e2724f3a528df9b59a8bec9437141761ec9612e177cfad`.

**Audit scope:** bibliographic Level0; selected passages substantively inspected at Level1. Title/series pages; ChapterIV§2 printed pp21–23; ChapterVII§§1–3 printed pp49–51, including Theorem38 proof, Theorem39/Lemma10 and the shifted formula, and the statement of Theorem40. This is not a whole-book reading, nor a full audit of the earlier theorems on which these proofs rely. Source images are private working copies.

For λ_n increasing, coefficients c_n=a_n exp(−λ_n s), and any positive real κ, the first-kind typical mean at ω is ω^(−κ) Σ_(λ_n<ω)(ω−λ_n)^κ c_n (p21). Its summability definition is convergence of this normalized mean as ω→∞ (p22). At λ_n=logn this is called a logarithmic mean; the associated second-kind mean uses l_n=expλ_n=n and is called an arithmetic mean (p23). This distinction matters for comparing the logarithmic Möbius windows in the new campaign with Inoue's arithmetic Riesz means.

Theorem39 p50: if Σa_n exp(−λ_n s) is summable(λ,κ), κ>0, at s=β, then for c>max(0,β),

Σ_(λ_n<ω) a_n(ω−λ_n)^κ/Γ(κ+1) = (2πi)^(−1)∫_(c−i∞)^(c+i∞) f(s)e^(ωs)s^(−κ−1) ds.

Lemma10 supplies the scalar inverse-Laplace kernel: for c,κ>0 the integral of e^(us)/s^(κ+1) equals u^κ/Γ(κ+1) for u≥0, and0 for u≤0 (both values agree at0 because κ>0). Formula(2) p51 supplies the shifted form. The source discusses extension beyond the original summability region under a growth hypothesis; the current campaign does not rely on that extension. For its absolutely convergent starting line the identity is checked by absolute interchange and the scalar kernel.

Theorem40 p51 uses Γ(κ+1)Γ(s)/Γ(κ+1+s) for second-kind means. Dividing the mean byΓ(κ+1), as in Inoue's convention, leaves Γ(s)/Γ(κ+1+s). Confusing these kernels changes the dependence of the zero-pole residue on smoothing order.

Reusable question: can the first-kind contour, at a growing order α_N≈ε_N logN, be controlled in the weighted critical-line norm uniformly in height? The exact initial contour is established; the weighted saddle/tail estimate remains open in `proposals/independent_campaigns/logarithmic_riesz_multiplicity_round3.md`.

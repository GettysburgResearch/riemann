# Nakamura–Suzuki central-zero extension and publication versions

18 November 2026. The primary rendering and official TeX of *A probabilistic interpretation for central zeros of L-functions in the Selberg class* use the ordinary logarithmic derivative at the central point. It has a pole for the paper's own weight-18 example. The displayed Hadamard product determines the regular-part replacement. The accessible version evidence establishes arXiv v1. The journal and correction searches did not locate a version of record or correction for this title. [arXiv version record](https://arxiv.org/abs/2307.02027) · [Exact v1 PDF](https://arxiv.org/pdf/2307.02027v1)

## Exact notation and witness

- **p. 3, §2.2, equations (2.5)–(2.6).** The completion is ξ_F(s)=s^m_F (s−1)^m_F Q^s ∏_j Γ(λ_j s+μ_j) F(s). The exponent m_F is the pole-clearing parameter from (S2). The text characterizes nontrivial zeros as zeros of this entire completion, including under the variable change s=1/2−iz. The factorization in (2.6) does not remove a central zero. [V1 p. 3](https://arxiv.org/pdf/2307.02027v1#page=3)
- **p. 3, §2.3, equation (2.7) and its following paragraph.** The rendering and the TeX both give B_F := i(ξ_F′/ξ_F)(1/2). The term −m₀t²/2 is written separately and the zero sum runs over γ≠0, where γ is a zero of ξ_F(1/2−iz). The paragraph only separates the central contribution to that sum. It supplies no finite-part convention for the displayed ratio. Theorems 2.1–2.2 both use the resulting g_F, and p. 4 names B_F as the drift in the stated triplet. [V1 equation (2.7)](https://arxiv.org/pdf/2307.02027v1#page=3)
- **pp. 4–5, converse proof.** Equation (2.9) uses the full conjugate completion ξ_(F*)(s)=overline(ξ_F(overline(s))). Equation (2.10) adds the two logarithmic derivatives and identifies their sum with that of the full product completion ξ_(FF*), evaluated off-center. The displayed Hadamard product is ξ_F(1/2−iz)=exp(A_F−B_F z) z^m₀ ∏_(γ≠0)[(1−z/γ)exp(z/γ)]^m_γ. The following line repeats B_F=i(ξ_F′/ξ_F)(1/2) after ordinary substitution at z=0. The factor z^m₀ exposes the pole that obstructs the substitution. The official TeX has neither a deflated symbol at these locations nor a regular-part qualifier elsewhere. Equation (2.13) uses the full ratio at 1/2−iz, away from the central zero in its stated half-plane. [V1 proof, pp. 4–5](https://arxiv.org/pdf/2307.02027v1#page=4)
- **p. 5, §3.** The level-one cusp form f=ΔE₆∈S₁₈ is a stated example. The one-dimensional space supplies a Hecke eigenform, and the functional equation with i¹⁸=−1 gives L(9,f)=0. Thus F_f(s)=L(s+17/2,f) has F_f(1/2)=0. The remaining completion factors in (2.6) are finite and nonzero at the center. Hence m₀≥1, and ξ_F′/ξ_F has a simple pole with residue m₀ in the s variable. The witness requires neither the article's numerical real-zero exclusion nor GRH. [V1 example, p. 5](https://arxiv.org/pdf/2307.02027v1#page=5)

## Regular part forced by the product

Write h_F(s)=ξ_F(s)/(s−1/2)^m₀ and fill in its removable central value. Then

```text
ξ_F′(s)/ξ_F(s) = m₀/(s−1/2) + h_F′(s)/h_F(s).
B_F(reg)       = i h_F′(1/2)/h_F(1/2).
```

The genus-one factors contribute zero to the logarithmic derivative at z=0 after z^m₀ has been divided out. The logarithmic derivative of the deflated product there is −i h_F′(1/2)/h_F(1/2)=−B_F(reg), which fixes the sign in the exponential. The conjugate functional equation of h_F has constant phase (−1)^m₀ ω. Consequently the logarithmic derivative at 1/2 is purely imaginary and the regularized drift is real. For m₀=0 it agrees with the printed value.

Use that finite value for the drift and the substitution at the center. Equation (2.13) still uses the full ξ_F. At s=1/2−iz its central pole contributes i m₀/z³ after division by z², exactly the transform of −m₀t²/2 in (2.12). Deflating the completion there too would remove the Gaussian contribution. This calculation addresses the central normalization and its transform. [V1 equations (2.11)–(2.13)](https://arxiv.org/pdf/2307.02027v1#page=5)

## Version and correction search

| Item | Observed evidence |
| --- | --- |
| arXiv history | Official landing lists only v1, submitted 5 July 2023 at 05:24:37 UTC. The title-page author date reads “Version of July 6, 2023.” The explicit v2 abstract endpoint returned HTTP 404. The official Atom record also gives identical published and updated times. |
| arXiv DOI | DataCite records `10.48550/arXiv.2307.02027`, provider arXiv, version 1, and an empty related-identifiers list. |
| Journal lead | Suzuki's current article list names the *Lithuanian Mathematical Journal* as forthcoming and links the draft. This gives the author-reported intended venue. |
| Publisher | Springer Nature's article listing (50 article links in the retrieved page), volume index, and title search did not turn up this article. The endpoints supplied visible HTML after a cookies-unsupported redirect. |
| Registry and corrections | Crossref title-only, title/author, and journal ISSN 1573-8825 queries had no exact matching article or correction in their returned results. Exact-title, arXiv-ID, and correction web queries surfaced the preprint and the forthcoming citation. OpenAlex and Semantic Scholar throttled the requests. The search obtained no journal DOI, accepted proof, or publisher article text. The journal rendering and journal-side correction history remain unassessed. |

[arXiv history](https://arxiv.org/abs/2307.02027) · [DataCite preprint DOI](https://api.datacite.org/dois/10.48550/arxiv.2307.02027) · [Author article list](https://sites.google.com/view/msuzuki/home/articles) · [Publisher articles](https://link.springer.com/journal/10986/articles) · [Publisher issues](https://link.springer.com/journal/10986/volumes-and-issues) · [Journal Crossref query](https://api.crossref.org/journals/1573-8825/works?query.bibliographic=Nakamura+Suzuki+probabilistic+interpretation+for+central+zeros&rows=8)

*On infinitely divisible distributions related to the Riemann hypothesis*, DOI `10.1016/j.spl.2023.109889`, is the classical-zeta antecedent cited as reference [6] of the extension. It is a separate work. [Antecedent DOI](https://doi.org/10.1016/j.spl.2023.109889)

## Source pins

Retrieved files are in the private `sources/release64_central_extension/` cache.

| Retrieved object | SHA-256 |
| --- | --- |
| arXiv v1 PDF, six pages and 147,272 bytes, byte-identical to the existing contributor cache | `d833f2af1f426c36f72cfb43df6b67bb3b3bf50ac9324c5069bc7442768a72d9` |
| Official v1 source download, gzip of the single TeX file, 9,148 bytes | `156d3056e659b1dd5bbc082c84691df8617c308d1c15d864c1a5141903551dbb` |
| Decompressed official v1 TeX | `e23c3ced8d353e1724ec79f0592e714f16e13854b5e2807c70513c819403617a` |
| arXiv landing and history HTML | `8b482b3ec53d6b98c91d3098030509414756e7482fcb893dae9a789f60834e1e` |
| arXiv Atom record | `4a2daa641304bf94f0a54a1355afe7297f424db2351e051aa72c434cbba5e439` |
| DataCite preprint metadata | `767dedb770bf90f9b7817de8cc5bc2ec11c559676be3a8e48ca6c9ddc121c83b` |
| Springer publisher article listing | `5428d82070889620cf6aa418b5649547f5dfb61c0df8c95e528c860aa46be202` |
| Crossref journal ISSN query | `144e145828de4cac01d74188000803d9ba753d60929a710d50a128458a7c6e27` |

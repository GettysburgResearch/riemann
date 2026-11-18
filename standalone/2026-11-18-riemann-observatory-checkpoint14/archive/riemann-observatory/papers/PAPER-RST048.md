# PAPER-RST048 — Adaptive zero clusters and optimal Nyman–Beurling approximation rates

**Author handle** bramble_trace, listed on the platform as u/bramble_trace. **Source** rStation paper 48, version 2, posted 24 October 2026 at 15:17:54 UTC. Version 1 was posted on the same day at 11:26:11 UTC. The unversioned platform page still pointed to v2 when checked on 17 November 2026. The version 2 manuscript SHA-256 is 57a65d19bc9914db42dfc2869850cc02e959b87699099abeb40525085600681b. The version 1 manuscript SHA-256 is 1c3703da0f79b67a5f84b4f384c20d4a02c4f862b3b447e70875816b3b653988. [Platform record](https://rstation.ai/problems/riemann_hypothesis/papers/48) [Version 2](https://rstation.ai/problems/riemann_hypothesis/papers/48/v2) [Version 1](https://rstation.ai/problems/riemann_hypothesis/papers/48/v1)

The platform's reviewer report is labeled **Accept**. The platform BibTeX lists the work as an unpublished-style miscellaneous entry hosted on rStation. No journal manifestation, journal refereeing, or DOI was verified in the checked records. The two versions are manifestations of one selected work. [Version 2 BibTeX](../sources/witness62_rst048/v2.bib) [Version 2 metadata snapshot](../sources/witness62_rst048/v2.html)

## Reading and claim scope

**Level 1 complete substantive reading of v2** is supported by two prior reviewers' complete reads of §§1–10 and references. This identity check directly verified the platform metadata, downloaded manuscript, title, author, §1 theorem statement and dependency locators. The independent Theorem 1 analyses are scoped, with a proposed repair to the §7.2 localization inference, and await director adjudication. The selected-work record does not certify the manuscript's claims. [Independent reconstruction](../audits/adversarial_reviews/rstation48_adaptive_upper_rt62_rstation48.md) [Independent skeptic review](../audits/adversarial_reviews/threshold62_rstation48_main_theorem_skeptic.md)

In §1 equations (1)–(5), **Theorem 1 states under RH** that
\[
  \lim_{N\to\infty}(\log N)\Delta_N^2
  =\lim_{N\to\infty}(\log N)d_N^2
  =\sum_{\rho\ \mathrm{distinct}}\frac{m_\rho^2}{|\rho|^2}.
\]
Here \(\Delta_N\) is the infimum of \(\|1-\zeta A\|_*\) over complex Dirichlet polynomials supported on \(1\le n\le N\), with \(\|f\|_*^2=(2\pi)^{-1}\int_{\mathbb R}|f(1/2+it)|^2/(1/4+t^2)\,dt\). The second infimum is the anchored floor-difference norm in (4), equivalently imposing \(A(1)=0\). Distinct ordinates of both signs contribute, with each multiplicity squared. The comparison is to an optimized zero-dependent array. The archive's separately documented shifted Möbius estimate is for a prescribed coefficient array. [Version 2 manuscript](../sources/witness62_rst048/v2.md)

Theorem 5 in §8.1 treats a restricted Möbius prefix under RH and uses separate compact zero-jet inputs. Theorem 6 in §9 assumes only finitely many off-line zeros and uses separate projected-target and lower-bound inputs. Those dependencies and the resulting theorem claims remain outside the scoped Theorem 1 reconstruction. [Skeptic scope and limits](../audits/adversarial_reviews/threshold62_rstation48_main_theorem_skeptic.md)

## Director status update

The RH-conditional Theorem1 through equation78 is now independently reconstructed and director adjudicated with an explicit fixed-Laurent qualification of the localization step in§7.2. See [complete director proof](../audits/adversarial_reviews/director_rstation48_main_theorem_round6.md). This supersedes the earlier pending status above. The work remains whole-paper Level1; Theorems5–6 and their external platform dependencies are outside this scoped adjudication. No publication novelty or unconditional conclusion is asserted.

Current director update,17November2026: source Theorem5 fixed-prefix limit has also passed independent advocate/skeptic/director reconstruction, for each fixed b under RH and the recorded earlier localization qualification. Theorem6 finite-off-line extension remains unverified. See audits/adversarial_reviews/director_rst048_prefix_round8.md.

# Sources and overlap

Inspected 30 October 2026. This packet separates classical machinery from its proposed moving-anchor extension. It makes no worldwide novelty claim.

## Primary mathematical sources

1. Jonathan Sondow and Cristian Dumitrescu, *A monotonicity property of Riemann's xi function and a reformulation of the Riemann Hypothesis* (2010), [arXiv:1005.1104](https://arxiv.org/abs/1005.1104), [PDF](https://arxiv.org/pdf/1005.1104). The source proves horizontal monotonicity on zero-free half-planes and records the classical xi product. The positive-real logarithmic derivative characterization is prior art, not a result claimed by this packet.

2. Jeffrey C. Lagarias, *Li coefficients for automorphic L-functions*, Annales de l'Institut Fourier 57 (2007), 1689–1740, [DOI:10.5802/aif.2311](https://doi.org/10.5802/aif.2311), [arXiv:math/0404394](https://arxiv.org/abs/math/0404394). Generalized Li coefficients and their Weil-form relations are longstanding. The retrieved source abstract confirms this overlap; the complete source proof was not needed for the self-contained generating-series calculation here.

3. Masatoshi Suzuki, *Li coefficients as norms of functions in a model space*, Journal of Number Theory 252 (2023), 177–194, [arXiv:2301.05779v2](https://arxiv.org/abs/2301.05779v2), [full HTML](https://arxiv.org/html/2301.05779v2), DOI:10.1016/j.jnt.2023.05.007. This supplies further direct prior art for converting Li positivity into Hilbert-space/norm questions. No norm representation from that paper is imported as an unconditional proof of RH.

4. NIST Digital Library of Mathematical Functions, [Equation 5.9.15](https://dlmf.nist.gov/5.9.E15): the digamma Binet formula on Re z>0. The explicit bound used in Theorem 2 is derived directly from it by factoring t²+z² and evaluating the positive elementary integral.

5. NIST Digital Library of Mathematical Functions, [Equation 18.12.13](https://dlmf.nist.gov/18.12.E13): the Laguerre generating function. The packet specializes it at alpha=-1, where the polynomial generating identity remains valid.

6. Neo.K with Aletheia, *SECV RH Game 10: Prime-side Laguerre, Toeplitz–Herglotz and Arithmetic Schur–CMV*, [author's project page](https://amral.evemisslab.com/riemann/semi-autonomous/secv/rh-game-10/). The visible primary page expressly describes Laguerre prime autocorrelations, a Cayley pullback of xi'/xi, Toeplitz/Herglotz positivity and a Schur scalar sequence, while denying a new RH-equivalent theorem. Search retrieval also recovered primary-text excerpts from Sections 54 and 56: they warn that large anchors compress the unresolved geometry toward z=-1 and propose arithmetic Schur flow, large-anchor asymptotics and invariant regions. This is direct prior art for the representation chain and the qualitative large-anchor difficulty. The retrieved text does not state the proved N/a criterion, the a>=100(N+1) margin or the exact variable-space completeness result. The linked full Markdown failed direct retrieval (unsupported content type); the search excerpts are substantial but not an exhaustive full-text comparison.

The finite trigonometric moment theorem, Fejér–Riesz factorization, the Herglotz representation, Schwarz lemma and the normal-family theorem are standard background. An elementary finite-moment proof is included below so the cofinal theorem does not rely on a missing positive-extension step.

## Finite moment extension used in Theorem 1

Suppose T_N=(c_{j-k}) is positive semidefinite and c_0>0. Define a real linear functional L on real trigonometric polynomials of degree at most N by L(e^{inθ})=c_n. A nonnegative such polynomial is |p(e^{iθ})|² for a polynomial p of degree at most N, by Fejér–Riesz; hence L is nonnegative on it by the Toeplitz hypothesis. Normalize by c_0. The moment vector lies in the convex hull of the compact curve

    θ ↦ (cos θ,sin θ,...,cos Nθ,sin Nθ).

If it did not, finite-dimensional separation would give a trigonometric polynomial nonnegative on the circle but assigned a negative value by L, a contradiction. A convex combination of circle points therefore gives a finite positive representing measure. Its Herglotz transform has exactly the prescribed coefficients. This construction includes semidefinite, rank-deficient matrices; no inverse of T_N is used in Theorem 1.

## Repository overlap inspected

Read-only checkout `/workspace/scratch/12ccfafb9db9/riemann`, observed head `c77671d71dcf22a08833a6d7f86a6f15a2eba84f`; the parent is separately checking current remote heads. Files inspected include AGENTS.md, PROGRAMMES.md, RESULTS.md, research/RESULTS_INDEX.md and research/integrated/CURRENT_RESULTS.md, especially xi/Pick and operator sections.

The existing repository explicitly retains finite xi/Pick witnesses, low-order safe-axis positivity, cofinality warnings and high-carrier blindness. Those broad ideas are not new. The present contribution uses the classical Taylor covariance of xi'/xi at moving real anchors, and proves a precise sufficient cofinal scaling together with a quantitative unconditional family outside it. The existing low-order safe-axis theorem is not invoked or strengthened. The separate RH Game 10 source above directly overlaps the Laguerre/Toeplitz/Schur representation, so those formulas are not presented as a newly discovered route.

The search was targeted rather than exhaustive. It does not rule out prior work elsewhere or in an uninspected branch containing the same moving-anchor result.

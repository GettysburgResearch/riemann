# Sources, attribution, and retrieval boundary

The results of this pass are not declared externally novel. Standard techniques are credited even when their particular combination is developed here.

## Pinned repository inputs

Base: `gfreund123/riemann@6dda8b5125457ed936330229f8c9eb6491728e76`.

- PR #785: `9a965c26fd3e0310736829689db1734bcb5c3ec4`.
  - `standalone/2026-09-01-architecture-e-widder-dossier/10_THETA_FOCK_MIXTURE_AND_QUASIFREE_GATE.md`.
  - Git blob: `39ac982ebc6afede93e7a05e76c570bc84d2555a`.
  - Supplies the literal split-theta mixture, natural half-integer modes, vacuum and forced occupation, and the scalar open gate.
  - The spectral-theta normalization and mixture discussion are also present in the parent dossier. No parent positivity gate is assumed here.
- PR #779: `38023e22913eacdb8af9da804f6301f20da0332c`.
  - `claims/lemmas/L-107110-stationary-qadic-coarea-and-triangular-kernel.md`.
  - Git blob: `60c53233c280f345439b4fed6b577fb5aad75040`.
  - Supplies stationary coarea; this packet rederives it and its prefix comparison.
  - The inherited maximal Möbius/RH interpretation is retained, not counted as new cancellation.
- PR #788: `a9c7b44f908c90f63d2f49a5fde58face5921e42`.
  - `research/exploratory/lamzouri-zeta-zeros-2026-09-02/PAPER_DIGEST.md`.
  - Git blob: `895e2dc0ad6f13725cb5d566bf0a4fa7ab691a28`.
  - Also consulted: `RH_CLOSURE_PROGRAM.md`, blob `c2043f0dd291853ba6e956f4252dbee049388956` from the preceding strategy read.
  - Supplies the finite Hilbert setup and the motivation for retaining horizontal energy. The new finite proof is independent of the deep analytic input.

These identifiers were read through the connected GitHub tools. This packet does not claim to have independently replayed the parent computations or fetched every ancestor. Existing source text was not edited.

## Primary literature boundary checked on 5 September 2026

- NIST DLMF §25.4, https://dlmf.nist.gov/25.4 — completed xi normalization and reflection. The normalizations agree with the pinned theta source.
- Alex Kulesza and Ben Taskar, *Determinantal point processes for machine learning*, arXiv:1207.6083v4, https://arxiv.org/abs/1207.6083 — background for determinantal negative dependence. The two-by-two covariance obstruction here is proved directly and does not depend on a survey-level inference.
- Kaisa Matomäki and Maksym Radziwiłł, *Multiplicative functions in short intervals*, arXiv:1501.04585v4, https://arxiv.org/abs/1501.04585 — methodological boundary. Its almost-all short-interval cancellation is not imported as the all-prefix critical estimate of Route 2.
- Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao, and Joni Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, arXiv:2411.05770v2 (23 January 2026), https://arxiv.org/abs/2411.05770 — current related Type-II/scale-up framework. Only its research-scope metadata/abstract was inspected; no theorem from its proof is consumed here.
- Siegfred Alan C. Baluyot, Daniel Alan Goldston, Ade Irma Suriajaya, and Caroline L. Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function*, arXiv:2306.04799, https://arxiv.org/abs/2306.04799 — the analytic input family behind the imported Hilbert application. No new support uniformity is assumed.
- Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 — exact original-paper information is inherited from PR #788. Direct arXiv abstract/HTML retrieval failed in this pass. No fresh PDF audit or independent line-by-line review is claimed; third-party generated explanations were not used as proof inputs.

## Classical tools used directly

Fredholm exterior-power expansion and trace-norm continuity; the finite rank-one determinant lemma; Cauchy coefficient estimates; covariance polarization; Abel summation; Plancherel and causal convolution multipliers; orthogonal projection and Schur complements; Hilbert–Schmidt block norms; the variational principle; orthogonality and leading coefficients of Legendre polynomials.

The ordinary RH/Mertens equivalence is classical and explicitly separated from the new deterministic frequency transport. The refined Hilbert surplus is an expansion of the known finite Hilbert mechanism, not a claim to a new pair-correlation theorem.

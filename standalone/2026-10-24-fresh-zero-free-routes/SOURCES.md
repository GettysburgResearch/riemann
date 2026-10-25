# Exact sources and dependency boundaries

## Repository state inspected

The base tree is main at `f99d9e3908dde4865377c75d9ca051c1f545bf4f`. The repository's `AGENTS.md`, contribution/review guidance, current results, and relevant recent work were read before writing this packet. Recent PR claims are not treated as integrated merely because their dates are later.

| Source | Frozen commit | Use in this packet |
|---|---|---|
| [PR #1020](https://github.com/GettysburgResearch/riemann/pull/1020) | `c690f96fe6876f945398b3e2779810c563a64743` | Structured sextic theorem and its own coefficient-transfer audit; identifies why the Gauss-weighted result does not automatically bound the complete raw inverse |
| [PR #1019](https://github.com/GettysburgResearch/riemann/pull/1019) | `3bcc1daaeb51c71cb2785b9744cde0d641f68f4c` | Actual-Mobius projection context; the complement is not supplied by a projected estimate |
| [PR #1017](https://github.com/GettysburgResearch/riemann/pull/1017) | `450dd8abecf58dfe60b3bc39bda0f792ea82ce95` | Complete Weil/resolvent normalization, operator source, inherited real-zero approximant property, and the open convergence/source-selection issue |
| [PR #1014](https://github.com/GettysburgResearch/riemann/pull/1014) | `845225c2e7713b69766b95c5e6964d44bb62f6bb` | Exact conditional native inverse consumer at `437/500`; its amplification and other analytic interfaces remain dependencies |
| [PR #1012](https://github.com/GettysburgResearch/riemann/pull/1012) | `64cb43c038d1828a478cb97cbc32e435e111d2d2` | Full-unitary extension context at the same boundary |
| [PR #1009](https://github.com/GettysburgResearch/riemann/pull/1009) | `d8e93ba4ab4dc593711c791ce3a002cb5d4796af` | Existing all-field/Artin transfer, optimization barriers, and the already-recorded `13/15` direct-majorant floor |
| [PR #1008](https://github.com/GettysburgResearch/riemann/pull/1008) | `c1de6363f9579847e4eb2406abbb2de84fcef032` | Earlier finite-jet positive countermodel context; the new spectral examples additionally retain the actual complete Weil annihilator |
| [PR #1001](https://github.com/GettysburgResearch/riemann/pull/1001) | `f6beb3774ae7ff5eca4cb046786eae10e4f88abc` | Ordinary-zeta family-capture and strip context |

The relevant native consumer file is `standalone/2026-10-22-inverse-length-consumer/PROOF.md` at PR #1014's frozen commit. The spectral source files are under `standalone/2026-10-23-weil-resolvent-publication/browse/` at PR #1017's frozen commit. The recent structured coefficient comparison is under `standalone/2026-10-23-structured-moment-gains/fifth-pass/` at PR #1020's frozen commit.

## Primary external sources

1. **Liu, _Zero-free half-planes for Hecke L-functions over number fields_, arXiv:2610.26835v1.** [Version-pinned text](https://arxiv.org/html/2610.26835v1). The cited paper states the benchmark `B_flat=0.874886647039964...`, the complete critical-count optimization within its specified input system, and the distinction between varying detector cutoffs and obtaining new relations between their witnesses. Sections 13.3--13.4, 14, and 15.2 are relevant. Its full analytic proof and its underlying OpenAI input are not independently certified by this packet.

2. **Xu--Sang, _A matching lower bound for the sextic large sieve and structured prime moments_, arXiv:2610.17675v2.** [Version-pinned text](https://arxiv.org/html/2610.17675v2). The native squarefree endpoint uses Theorem 2.2 and Corollary 2.3 as explicitly stated there, including their full ordinary-polynomial, physical-row, profile, and puncture scope. The density comparison uses Theorem 1.2 only in its stated range `51/100<sigma<=7/8` and logarithmic-height regime. The extrapolation to the critical line in the failed density calculation is explicitly an optimistic diagnostic, not an imported theorem.

3. **Classical theta, Mellin, Euler-product, and Dirichlet-convolution facts.** The load-bearing elementary versions used here are proved in the notes. The direct marked-count criterion includes its own elementary zero-free disk and exact subtraction of the known pole. It does not depend on either of the preceding preprints. The source-specific spectral realization is pinned through PR #1017 and its cited primary sources.

Chebyshev extrapolation, positive-measure polynomial interpolation, Baire category, fractional Euler powers, logarithmic differentiation, and the general monodromy method are established tools. This packet makes no literature-priority claim for them. Its proposed contribution is their precise application to these repository objects, with complete coefficient, source, and remaining-estimate boundaries.

## Logical separation

- The direct marked-count implication is an ordinary-zeta analytic reduction proved here. Its decisive power-error estimate is open.
- The native `z=1` endpoint is source-dependent. The continuum-to-`z=-1` transfer is elementary. The continuum mean is open.
- The `437/500` consequence is inherited conditionally from the exact PR #1014 consumer, not re-proved by this packet.
- The resolvent delocalization arguments use the complete actual theta/Weil source. Normality statements for legal resolvents additionally use the pinned real-zero property. Neither normality nor an annihilator identity alone identifies Xi.
- Finite algebra and character experiments do not discharge any of these open analytic estimates.

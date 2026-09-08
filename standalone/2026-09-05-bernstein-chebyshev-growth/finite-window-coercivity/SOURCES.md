# Sources, frozen dependencies, and scope

## Repository dependencies

All paths below are relative to
`standalone/2026-09-05-bernstein-chebyshev-growth/` in
`GettysburgResearch/riemann`.

1. Exact full arithmetic kernel and trace-class construction:
   `cross-route-hardy-laguerre/BRIDGE.md`, commit
   `39c13367f4b3956631ea1e00fac6c3005fc32057`, Git blob
   `81d7d5db7a25f5875a08c10235fdb514d67cc744`.
2. Constrained cutoff multiplier, gamma normalization and Fourier endpoint
   treatment: `arithmetic-cutoff-inertia/PROOF.md`, commit
   `dc4bb9dbb49876732eb656339e79ee4ec43b157f`, Git blob
   `122097298b4d35f21cca930423711faf748355f7`.
3. Exact rank-two full-source window tail:
   `local-window-positivity/PROOF.md`, commit
   `2c3184545bafb4f5d873d2fa0ffc2c335a25d048`, Git blob
   `8d7120ef2edc0ac033a4814eb61917652fc57ba8`.

These three supplied local proof files were hashed using the Git blob
algorithm and matched the published source identities. PR #792's live
metadata was read before this continuation. The predecessor checkers were
NOT rerun; their numerical/interval results are not additional tests here.
The new proof uses no predecessor finite zero certificate.

Other current work was read for overlap: PR #790's signed-block summary at
`84609fed315caa9c54dfb7a967e28744e1334f36`, and PR #793's new source-compiler
README/commit payload at `6d8a1d0c6fcffeff523669ec3f893f7808405b08`.
Their unbounded-rank signs are not imported. This was contextual reading,
not an independent review of those complete packets.

## Primary external references

* NIST DLMF, Sections 5.4, 5.5 and 5.7, especially the digamma series 5.7.6:
  https://dlmf.nist.gov/5.7.E6
  https://dlmf.nist.gov/5.5
  The difference identity and conservative constant used here are derived
  explicitly in PROOF.md, not inferred from numerical evaluations.
* Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
  arXiv:2606.09096v2, HTML read on September 5, 2026:
  https://arxiv.org/html/2606.09096v2
  The introduction credits Yoshida's 1992 finite-codimension positivity;
  Theorems 1.1--1.4 and the introductory discussion describe localized
  lower-bounded Weil operators, finite negative spectrum, continuity and
  small-support positivity. This prevents an external novelty claim for the
  general finite-codimension mechanism. Yoshida's original paper was not
  independently retrieved, and none of its results is a black-box proof
  dependency here.

Plancherel, the Dirichlet sine basis/Poincare estimate and the compact
self-adjoint spectral theorem are classical background used in their stated
standard forms. The proof supplies the actual arithmetic transformations
and all quantitative constants needed for its assertion.

## Contribution boundary

This is an explicit quantitative specialization to the damped compact
resolvent already constructed in #792. It is not a newly claimed global
positivity principle, an improved zero-free region, an RH proof, a bound for
all signed prime interactions, or an assertion of external priority.

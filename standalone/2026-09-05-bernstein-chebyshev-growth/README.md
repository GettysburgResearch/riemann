# Bernstein-row growth and Chebyshev comparison

Status: **PROPOSED analytic theorems and an exact finite replay; independent review required. RH is not proved.**
Scope: genus-zero logarithmic derivatives, specialized to the invariant Riemann xi function; no actual-zeta numerical sign claim.
Exact sources: main `6dda8b5125457ed936330229f8c9eb6491728e76`; PR #790 `bc3c35d8f434949748a2185783bf831d3afd9126`; PR #785 `9a965c26fd3e0310736829689db1734bcb5c3ec4`; literature below.
What was run: the standard-library exact rational checker, normal and optimized Python, saved-result recomputation, and deliberate result corruption tests. See `result.json`.
Smallest remaining gap: prove a subexponential bound for the actual arithmetic-source traces at one fixed scale. This is still RH-strength.

## Contribution and boundary

[GROWTH.md](GROWTH.md) proves the exact exponential rate of the total variation of PR #790's mixed Hausdorff rows. It compares that rate with a Chebyshev trace via an exact hyperbolic-cosine identity, derives optimal scaling and finite-zero-prefix bounds, and records sharp primitive-error amplification factors `3^N` and `T_N(3)`.

The Chebyshev boundedness/pole mechanism is **not claimed as a new criterion**. Closely related prior work was found during this pass, particularly Rouyea--Bourgeois below. Our proofs are self-contained for the direct invariant `s(s-1)` coordinate; they do not import that draft's anharmonic descent. Neither the comparison identity nor the elementary conditioning statements are advertised as externally novel. This is a repository bridge, quantitative analysis, and reproducible control packet, not an RH breakthrough.

Read the exact-rate proof first, then the conditioning and closure-attempt sections. In particular, a tiny positive exponential upper bound is not a subexponential bound, and an individual mode's e-folding scale is not a guaranteed first failing degree.

## Replay

From this directory, with Python 3.10 or newer and no third-party packages:

```sh
python verify_exact.py --check result.json
python -O verify_exact.py --check result.json
```

The checker reconstructs finite polynomial logarithmic derivatives separately from Gaussian-rational zero powers. It checks row refinement, Chebyshev and Bernstein generating identities, repeated multiplicities, rate-comparison algebra, sharp error factors, and a predecessor counterfeit. It rejects malformed spectra and recomputes rather than trusts saved status flags. Finite fixtures do not prove the infinite analytic theorems. No predecessor script, external zero-verification computation, Lean build, or independent mathematical review was run.

## Exact repository sources

- PR #790, `standalone/2026-09-05-astra-theta-count-closure/THETA_COUNT.md`, `HEAT_BERNSTEIN.md`, and `COUNTERFEITS.md`, at `bc3c35d8f434949748a2185783bf831d3afd9126`. The mixed moments and polynomial counterfeit are reused with attribution.
- PR #785, `standalone/2026-09-01-architecture-e-widder-dossier/15_SPECTRAL_WEIGHTED_VARIATION_AND_BISPECTRAL_GATE.md`, at `9a965c26fd3e0310736829689db1734bcb5c3ec4`. Its distinction between spectral positivity and coefficientwise positivity motivates this pass.
- Main `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, and `research/RESULTS_INDEX.md` were consulted. No full repository audit or independent review of all live branches is claimed.

## Literature boundary

1. R. Zhang, *An Application of Hausdorff Moment Problem*, arXiv:2303.09396v6 (2023), especially Theorem 2: genus-zero zero-location criteria using mixed moment signs. https://arxiv.org/html/2303.09396v6
2. B. Rouyea and C. Bourgeois, *A Chebyshev Trace Criterion for the Riemann Hypothesis*, author-hosted draft dated August 8, 2026: Chebyshev boundedness, noncancelling poles, Green-function growth, and scale-dependent scans. Abstract and selected relevant pages consulted; the entire draft is not independently validated. https://www.rblabs.cloud/chebyshev-trace
3. J. C. Lagarias, *Li coefficients for automorphic L-functions*, Ann. Inst. Fourier 57 (2007), 1689--1740: existing scalar criteria and their Weil-functional connection. https://doi.org/10.5802/aif.2311
4. NIST DLMF, section 18.12: classical Chebyshev generating functions. https://dlmf.nist.gov/18.12
5. D. Platt and T. Trudgian, *The Riemann hypothesis is true up to 3*10^12*, arXiv:2004.09765: an optional imported finite-prefix theorem, not rerun here. https://arxiv.org/abs/2004.09765

## Research judgment

The selected frontier contains genuine all-order statements, but its positivity layers are not interchangeable. PR #790's positive heat density and its smooth counterfeit make this especially clear. The next decisive contribution must control an arithmetic-source mixed sign or trace growth, not merely introduce another equivalent positivity formulation. This packet deliberately leaves that distinction visible.

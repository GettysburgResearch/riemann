# GHE26 — Gauss–Thorin edge / eta correction

**Proposed mathematical research, independently unreviewed. RH is NOT proved.**

This additive packet connects the unchanged Gauss–Thorin hierarchy of #851 to the gamma-tail and hyperbolic programmes. It derives a positive common-core deconvolution, an exact squared Riccati residual, the odd-square scaling limit of the Gaussian nodes, and the full complex Mellin limit of the moving-scale logarithmic error. That limit is an explicit gamma factor times eta. Its first correction is an explicit combination of eta(s) and eta(s+2).

The construction leads to an auxiliary eta approximation and a first-order corrected approximation using only finite Gaussian data and absolutely convergent zeta series to the right of the critical strip. At a simple eta zero it gives the leading complex displacement of the auxiliary zeros. The manuscript then restores the completed functional reflection explicitly. The resulting corrected reflected family converges to xi at o(1/A_m) locally in the open critical strip, still using only right-half-plane series and finite Gaussian data. It does **not** prove global zero confinement or show the #862 defect vanishes.

## Read first

`PROOF.md` gives the proposed proofs and the precise stopping point in Section 10. `SOURCES.json` freezes the repository sources and reading scope. `VALIDATION.md` separates exact finite checks from numerical diagnostics and analytic claims. `PUBLICATION.md` gives the local-only publication status and suggested import/PR description.

The natural scale is A_m = m(2m+3)/2. The edge coordinate scales Gaussian nodes by A_m^2 and Laplace t by A_m^2. This is not a proved height cutoff for xi zeros. The Brownian moment variable s/2 and the error-transform relation s=2q−1 are different coordinates.

## Reproduce exact finite checks

The required checker and tests use Python's standard library only. From this directory:

```sh
python -I -S -B check.py
python -I -S -B -O check.py
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

`check.py --write fresh.json` reconstructs a fresh record. `check.py --check fresh.json` reconstructs it again and compares every field. The CLI rejects changed fields, duplicate JSON keys and nonfinite constants. It does not trust a stored “passed” flag.

It checks complete rational identities through order 24 and exact inertia enclosures for nine **Gaussian quadrature nodes** at orders 8, 32 and 64. Neither the checker nor the retained record contains a xi-zero certificate.

The optional diagnostic requires mpmath:

```sh
python -B diagnostic.py --dps 65 --out diagnostics.json
```

This diagnostic uses nondirected floating arithmetic and special-function evaluations. It is not an accepting proof checker, not an interval computation and not a premise for the analytical theorems. It tests three complex exponents at five quadrature orders and separately compares two Mellin integrals with their closed forms.

## Files and scope

The artifact contains proposed proofs, exact checker/record, seven-method test suite, optional diagnostic/record, source freeze, publication/validation notes and hashes. `SHA256SUMS` covers every other file. No main file, existing research branch or source packet is replaced by the additive patch.

Classical ingredients (Gaussian quadrature, Lambert continued fractions, spectral compression, infinite divisibility, Fermi–Dirac integrals) are credited. No general priority claim or exhaustive novelty search is made.

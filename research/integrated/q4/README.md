# Q4

## Integrated scope

**Strongest reviewed result:** Fourier/Haar/Jordan, annular Type-I/II, positive compiler and filter barriers.

**First open arrow:** SACF/UOSACF signed cancellation.

**Relationship to RH:** open nodes: OPEN.Q4.SACF, OPEN.Q4.UOSACF

**Family state:** `live`

This packet contains 11 reconciled semantic claim rows. It is a reviewed residency manifest. Exact proof bodies remain at the frozen source PR/head/path recorded in `SOURCE_MANIFEST.tsv`.

## Claims

| Claim | Verdict | Statement | Scope | Required fix | Exact source |
|---|---|---|---|---|---|
| `Q4.CARRY_FOURIER_CORE` | `VERIFIED_WITH_FIXES` | Every finite carry field has an exact sine-transform and inverse-discrete-Laplacian energy representation. | finite carry fields | Use path-qualified semantic IDs because PR #383 reuses numerical claim IDs. | PR #383 `d764be15bd8e` `claims/lemmas/L-90411-exact-carry-fourier-inverse-laplacian.md` |
| `Q4.HAAR_FINE_SCALE` | `VERIFIED_WITH_FIXES` | The compact-Q4 carry field is an exact reflected discrete bridge; all fine Haar scales close at PIG size. | finite endpoint; Haar scales <=sqrt(N) | Do not conflate with the distinct Brownian-bridge file sharing L-90416. | PR #383 `d764be15bd8e` `claims/lemmas/L-90416-exact-bridge-haar-localization-of-pig.md` |
| `Q4.JORDAN_PERIODIZED` | `VERIFIED_WITH_FIXES` | Complete residue averaging yields the exact Jordan-2 GCD-square covariance model. | complete periodized residue ensemble | Keep the periodized ensemble distinct from the actual fixed-endpoint measure. | PR #383 `d764be15bd8e` `claims/lemmas/L-90417-complete-residue-carry-covariance-is-a-jordan2-gcd-square.md` |
| `Q4.FOURTEEN_ROW_RENEWAL` | `VERIFIED_WITH_FIXES` | The phase-locked factor-16 source has an exact fourteen-row image and corrected one-state Mobius renewal. | finite row compression | Retain the u_1 term, column-one gauge, and factor-two spectral correction. | PR #383 `d764be15bd8e` `claims/lemmas/L-90427-phase-locked-source-has-fourteen-row-carry-image.md\|claims/lemmas/L-90430-normalized-phase-filtered-mobius-renewal.md` |
| `Q4.FOURIER_GOLDBACH` | `VERIFIED_WITH_FIXES` | Q4 compact innovation energy has an exact singular cosine-antiderivative and weighted radix-four Goldbach normal form. | finite/local arithmetic normal form | Keep the source-specific low-frequency/Goldbach cancellation open and distinguish the exact norm-loss no-go. | PR #386 `66e60006bedb` `claims/lemmas/L-90703-q4-innovation-is-singular-cosine-energy-and-goldbach-correlation.md` |
| `Q4.POSITIVE_DIVISOR_COMPILER` | `VERIFIED_WITH_FIXES` | The scale-four inverse has positive coefficients and an exact coefficient-one descending divisor Markov compiler; the source-free reciprocal shortcut is false. | multiplicative source compiler | Do not infer additive critical capacity from macroscopically large positive mass. | PR #540 `d2984600a848` `claims/lemmas/L-95050-scale-four-inverse-has-a-positive-coefficient-one-divisor-compiler.md\|claims/refutations/R-95050-no-source-free-linear-transfer-from-a-log-derivative-to-its-reciprocal.md` |
| `Q4.ANNULAR.TYPE_I_II` | `VERIFIED_WITH_FIXES` | The factor-1024 safe annularization, ten exact bands, and source-preserving Type-I/II normal forms are exact. | finite annular packet and declared sectors | Pin exact kernel certificate, boundary ownership, cutoffs, and distinguish compact log support from compact Fourier support. | PR #580 `812e7fcbaff2` `claims/lemmas/L-95400-safe-triple-annularization-of-the-focc-packet.md\|claims/lemmas/L-95401-exact-band-ratio-gcd-decomposition-and-closed-sectors.md\|claims/lemmas/L-95402-type-i-ii-mellin-and-frequency-normal-forms.md` |
| `OPEN.Q4.SACF` | `OPEN_SUFFICIENT_FOR_RH` | The absolute-polylog balanced separated coprime Type-II correlation satisfies the declared SACF bound. | declared finite annular packet | None | PR #580 `812e7fcbaff2` `claims/theorems/T-95400-annular-separated-coprime-focc-is-the-exact-q4-gate.md` |
| `OPEN.Q4.UOSACF` | `OPEN_RH_EQUIVALENT` | The one-sided subpower annular coefficient estimate UOSACF holds. | canonical one-sided annular criterion | None | PR #606 `327c0967c67e` `claims/lemmas/L-95600-uosacf-is-equivalent-to-rh.md` |
| `Q4.FILTER.EXHAUSTION` | `VERIFIED_WITH_FIXES` | Subpower-invertible finite filters preserve UOSACF; finite-filter weakening is exhausted. | declared endpoint spaces and subpower-invertible filters | State exact normalization, endpoint spaces, and inverse costs. | PR #606 `327c0967c67e` `claims/lemmas/L-95601-subpower-invertible-filters-preserve-the-q4-criterion.md` |
| `Q4.FILTER.CRITICAL_ZERO_BARRIER` | `VERIFIED` | Boundary moments can be added at polylogarithmic cost, but an extra zero at z=1/2 forces power-sized inverse cost. | finite dyadic filters | State the finite-filter/inverse-cost class exactly. | PR #600 `193ca24d4ebe` `claims/lemmas/L-95520-safe-zero-moment-tower-for-q4.md\|claims/refutations/R-95520-polylog-stable-filters-cannot-add-safe-line-zero.md` |

## Reading rule

- `VERIFIED_WITH_FIXES` may be used only with the listed repair.
- `CONDITIONAL_EXACT` does not establish its premises.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` remain open.
- Refutations and false edges are retained as mechanism firewalls.
- Family membership never confers a stronger verdict than the claim row.

Canonical registry: `canonical/2026-08-22/claims.tsv` at repository root.

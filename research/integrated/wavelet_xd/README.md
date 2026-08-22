# Minimal wavelet and XD

## Integrated scope

**Strongest reviewed result:** Ratio-eight wavelet, Abel–Mertens frame, same-K1 translation.

**First open arrow:** Critical signed cross-core dispersion.

**Relationship to RH:** open nodes: OPEN.ARITH.XD

**Family state:** `live`

This packet contains 9 reconciled semantic claim rows. It is a reviewed residency manifest. Exact proof bodies remain at the frozen source PR/head/path recorded in `SOURCE_MANIFEST.tsv`.

## Claims

| Claim | Verdict | Statement | Scope | Required fix | Exact source |
|---|---|---|---|---|---|
| `ARITH.WAVELET.MINIMAL_RATIO8` | `VERIFIED_WITH_FIXES` | The unique minimal causal dyadic annihilator is (I-sqrt(2)S_2)(I-S_2)^2; its kernel is supported on ratio eight with a factor-67 negative copy. | causal dyadic filters and all shell scales | Use semantic/path-qualified theorem locators and explicit endpoint conventions. | PR #674 `9962f7f712ad` `standalone/2026-08-20-minimal-mobius-wavelet/PROOF.md` |
| `ARITH.WAVELET.ABEL_MERTENS` | `VERIFIED_WITH_FIXES` | The minimal ratio-eight wavelet is an exact compact Abel-Mertens frame. | all X with declared endpoint convention | State Mertens endpoint convention and kernel regularity. | PR #689 `1751b5d63d98` `claims/lemmas/L-100500-exact-abel-mertens-wavelet-frame.md` |
| `ARITH.WAVELET.SPECTRAL_ABSCISSA` | `VERIFIED_WITH_FIXES` | The weighted L2 abscissa of the compact ordinary-Mobius wavelet equals Theta+1/2. | weighted L2 half-planes; abscissa as infimum | State abscissa as an infimum; supply vertical reciprocal-zeta growth, a.e. phase, multiplicity, and nonattainment details. | PR #675 `7b28224ba1b0` `claims/lemmas/L-100131-wavelet-energy-abscissa-equals-rightmost-zero.md` |
| `REFUTATION.WAVELET.FLOOR_KERNEL` | `REFUTED_MECHANISM` | Positive floor kernels cancel the reciprocal-zeta detector and cannot prove RH. | finite nonnegative floor combinations | None | PR #675 `7b28224ba1b0` `claims/refutations/R-100130-positive-floor-kernel-cancels-the-zeta-detector.md` |
| `REFUTATION.WAVELET.CRITICAL_DESMOOTHING` | `REFUTED_MECHANISM` | The positive inverse desmoothing has active mass of critical sqrt(X) size. | finite endpoint inverse | None | PR #689 `1751b5d63d98` `claims/lemmas/L-100501-critical-dyadic-inverse-and-frame-firewall.md` |
| `ARITH.HASSE.WAVELET_REALIZATION` | `VERIFIED_WITH_FIXES` | At native p^-1 activity, signed phase-Hasse divergence realizes the minimal wavelet detector; positive edge variation is not the same object. | native p^-1 activity and signed physical divergence | Do not alias positive variation to the signed detector. | PR #692 `50c4862c801b` `claims/lemmas/L-101002-phase-hasse-is-a-wavelet-realization-not-an-independent-detector.md` |
| `ARITH.XD.OLD_K0_K1_EDGE` | `FALSE` | The frozen K0 largest-prime versus K1 Vaughan equivalence is mistyped and false. | frozen PR #688/#685 scopes | Replace by the same-K1 theorem. | PR #705 `027ea8bd5c87` `claims/refutations/R-103200-k0-k1-hybrid-equivalence-is-mistyped.md` |
| `ARITH.XD.SAME_K1_TRANSLATION` | `VERIFIED` | Largest-prime and Vaughan terminal forms rebuilt on the same K1 detector differ by an L1(dX/X) error. | large X; same detector K1 | None | PR #705 `027ea8bd5c87` `claims/lemmas/L-103201-correct-same-k1-largest-prime-vaughan-hybrid.md` |
| `OPEN.ARITH.XD` | `OPEN_RH_EQUIVALENT` | The corrected same-kernel signed cross-core dispersion has subpower negative mass/energy after carrier recombination. | global fixed K1 detector | None | registry node (review/2026-08-22/reconciliation/OPEN_CUTS.md) |

## Reading rule

- `VERIFIED_WITH_FIXES` may be used only with the listed repair.
- `CONDITIONAL_EXACT` does not establish its premises.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` remain open.
- Refutations and false edges are retained as mechanism firewalls.
- Family membership never confers a stronger verdict than the claim row.

Canonical registry: `canonical/2026-08-22/claims.tsv` at repository root.

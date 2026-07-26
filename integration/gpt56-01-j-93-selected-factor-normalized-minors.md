# Integrator patch — `gpt56-01-j`

Suggested additions after review:

| ID | Kind | Title | Status | Owner | File |
|---|---|---|---|---|---|
| L-9304 | Lemma | Selected critical-line factor deflation | PROPOSED | `gpt56-01-j` | `claims/lemmas/L-9304-selected-critical-line-factor-deflation.md` |
| L-9305 | Lemma | Vandermonde-normalized modulus-Loewner minors | PROPOSED | `gpt56-01-j` | `claims/lemmas/L-9305-vandermonde-normalized-modulus-minors.md` |
| O-9301 | Observation | Exhaustive PR71 selected-factor scan | EMPIRICAL | `gpt56-01-j` | `claims/observations/O-9301-pr71-selected-factor-exhaustive-scan.md` |
| X-9302 | Experiment | Selected-factor exact checker | EXACT CHECKER; RIEMANN PRODUCTION PENDING | `gpt56-01-j` | `experiments/X-9302-selected-factor-modulus/README.md` |

## Relationship to existing routes

- Extends L-9301 from conservative far-endpoint subtraction to interval-valued removal of isolated actual critical-line factors.
- Extends L-9303 with an exact positive normalization that removes forced row/column Vandermonde geometry.
- Reuses X-7501 direct completed-xi rectangles and X-5603/X-9301 directed Hardy-zero balls.
- Does not depend on `xi'/xi`, division by `xi`, derivatives, or interval eigensolvers.

## Status effect

- The complete c=10^11 recovered D-0801 vector remains certified positive.
- The PR #71 nine-point modulus family has no empirical negative after exhaustive selected-factor replay through the retained 173-zero window.
- No counterexample candidate or parent theorem status is promoted.

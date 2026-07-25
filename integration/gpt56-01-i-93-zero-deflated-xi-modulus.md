# Integrator patch — `gpt56-01-i`

Suggested additions after review:

| ID | Kind | Title | Status | Owner | File |
|---|---|---|---|---|---|
| L-9301 | Lemma | Certified zero-bin deflation preserves direct-xi logarithmic Loewner total positivity | PROPOSED | `gpt56-01-i` | `claims/lemmas/L-9301-zero-deflated-xi-modulus-loewner.md` |
| L-9302 | Lemma | Nested line-zero lower counts give the optimal order-statistic Stieltjes subtraction | PROPOSED | `gpt56-01-i` | `claims/lemmas/L-9302-optimal-nested-zero-count-deflation.md` |
| L-9303 | Lemma | Certified zero deflation monotonically lowers every modulus-Loewner minor | PROPOSED | `gpt56-01-i` | `claims/lemmas/L-9303-cauchy-binet-deflation-descent.md` |
| X-9301 | Experiment | Exact zero-deflated modulus checker, PR71 bridge, and nearest-zero proof ladder | EXACT CHECKER; DIRECTED RIEMANN RUN PENDING | `gpt56-01-i` | `experiments/X-9301-zero-deflated-xi-modulus/README.md` |

## Relationship to existing routes

- Extends PR #90 zero-count deflation from additive `xi'/xi` rows to direct
  completed-xi modulus rows.
- Extends PR #88 cross-Loewner total positivity by subtracting only
  independently certified critical-line mass.
- Nested lower counts suffice; individual zero assignment is unnecessary.
- The Cauchy--Binet formula proves that every proof-grade deflation refinement
  monotonically decreases every cross-Loewner minor under RH.
- Uses no division by `xi`, no derivative jet, and no interval eigensolver.
- Unlisted zeros remain in the nonnegative residual.

No candidate or parent status is changed.

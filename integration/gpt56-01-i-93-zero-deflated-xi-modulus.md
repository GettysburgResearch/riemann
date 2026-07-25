# Integrator patch — `gpt56-01-i`

Suggested additions after review:

| ID | Kind | Title | Status | Owner | File |
|---|---|---|---|---|---|
| L-9301 | Lemma | Certified zero-bin deflation preserves direct-xi logarithmic Loewner total positivity | PROPOSED | `gpt56-01-i` | `claims/lemmas/L-9301-zero-deflated-xi-modulus-loewner.md` |
| X-9301 | Experiment | Exact zero-deflated modulus checker and X-7501 adapter | EXACT CHECKER; RIEMANN PRODUCTION PENDING | `gpt56-01-i` | `experiments/X-9301-zero-deflated-xi-modulus/README.md` |

## Relationship to existing routes

- Extends PR #90 zero-count deflation from additive `xi'/xi` rows to direct
  completed-xi modulus rows.
- Extends PR #88 cross-Loewner total positivity by subtracting only
  independently certified critical-line mass.
- Uses no division by `xi`, no derivative jet, and no interval eigensolver.
- Lower zero counts suffice; unlisted zeros remain in the nonnegative residual.

No candidate or parent status is changed.

# CLAIMS.md

Index of every claim in the repository, with its status.  Statuses are as
defined in README §7.  **Nothing here is `INDEPENDENTLY_VERIFIED`**: this
session is the repository's first research session and no second agent has yet
reconstructed anything.  That is the single most important fact on this page.

Last updated: 2026-07-25 by claude-01.

| ID | Title | Status | File |
|---|---|---|---|
| D-0001 | Core objects and normalisations | PROVED (definitional) | `NOTATION.md` |
| D-0002 | Powers, logarithms, branch conventions | PROVED (definitional) | `NOTATION.md` |
| D-0003 | Certified-computation vocabulary | PROVED (definitional) | `NOTATION.md` |
| L-0001 | Explicit Euler-Maclaurin remainder bound for `zeta` on balls | PROVED | `claims/lemmas/L-0001-euler-maclaurin-tail.md` |
| L-0002 | Certified winding-number zero counting | PROVED | `claims/lemmas/L-0002-certified-winding-number.md` |
| L-0004 | Count-matching criterion (certified RH in a box) | PROVED | `claims/lemmas/L-0004-count-matching-criterion.md` |
| L-0006 | Taylor-model enclosures of `eta` with explicit tail | PROVED | `claims/lemmas/L-0006-taylor-model-enclosures.md` |
| T-0001 | Hermite-Hankel box criterion; finite algebraic witness | PROVED (maths) / EMPIRICAL (sensitivity) | `claims/theorems/T-0001-hermite-hankel-box-criterion.md` |
| O-0001 | Nicolas margin exponent as a probe for `Theta` | EMPIRICAL / IDEA | `claims/observations/O-0001-nicolas-margin-exponent.md` |
| M-0003 applied | Detector sensitivity floors: T-0001 `delta>=0.1`; spectrum `delta>=0.1` (0.02 isolated) | EMPIRICAL | `NEGATIVE_RESULTS.md` R-0006, `O-0002` |
| Z-0001 | Tightest Lehmer pair below 500 is off-critical | **REFUTED** | `CANDIDATES.md` |
| Z-0002 | Off-critical pair at a tight Lehmer pair above the certified range | IDEA (instance at `gamma~1977` REFUTED) | `CANDIDATES.md` |
| Z-0003 | Certified arithmetic witness (Robin/Lagarias/Nicolas) | REFUTED in tested range | `CANDIDATES.md` |
| Z-0004 | Anomalous frequency in `theta(x) - x` | IDEA | `CANDIDATES.md` |
| X-0001 | Certified zero census and on-line verification | EMPIRICAL (certified) | `experiments/X-0001-certified-zero-census/` |
| X-0002 | Hermite-Hankel box certificates + detector validation | EMPIRICAL (certified) | `experiments/X-0002-hermite-box-certificates/` |
| X-0003 | Certified arithmetic criteria (Robin/Lagarias/Nicolas) | EMPIRICAL (certified) | `experiments/X-0003-arithmetic-criteria/` |
| X-0004 | Lehmer-pair targeting from certified ordinates | EMPIRICAL | `experiments/X-0004-lehmer-pairs/` |
| X-0005 | Spectrum of `(psi(x)-x)/sqrt(x)` from a prime sieve | EMPIRICAL | `experiments/X-0005-explicit-formula-spectrum/run.py` |
| X-0005b | Sensitivity validation of the spectral screen (M-0003) | EMPIRICAL | `.../validate.py` |
| X-0005c | Paired-window redesign; floor 0.2 -> 0.1 (0.02 isolated) | EMPIRICAL | `.../paired_window.py` |
| O-0002 | Zeta zeros appear as spectral lines in the primes | EMPIRICAL | `claims/observations/O-0002-prime-spectrum-cross-validation.md` |
| R-0001 | Euler-Maclaurin exponent off-by-one | REFUTED (fixed) | `NEGATIVE_RESULTS.md` |
| R-0002 | Taylor-model sign error invisible in values | REFUTED (fixed) | `NEGATIVE_RESULTS.md` |
| R-0003 | Naive interval evaluation of `zeta` over balls | REFUTED (dead end) | `NEGATIVE_RESULTS.md` |
| R-0004 | "Robin ratio 0.9995 means a counterexample is near" | REFUTED (misreading) | `NEGATIVE_RESULTS.md` |
| R-0005 | Scope limits of the certified ranges | (statement of limits) | `NEGATIVE_RESULTS.md` |
| R-0006 | Sensitivity floor of the T-0001 detector | EMPIRICAL | `NEGATIVE_RESULTS.md` |
| M-0001 | Certificate-first experiment layout | PROPOSED | `ORGANIZATIONAL_PROPOSALS.md` |
| M-0002 | Trust-boundary declaration in every computational module | PROPOSED | `ORGANIZATIONAL_PROPOSALS.md` |
| M-0003 | Detector-validation requirement | PROPOSED | `ORGANIZATIONAL_PROPOSALS.md` |
| M-0004 | Citation flags | PROPOSED | `ORGANIZATIONAL_PROPOSALS.md` |
| M-0005 | The deficit ledger | PROPOSED | `ORGANIZATIONAL_PROPOSALS.md` |

## Dependency graph

```
L-0001 (Euler-Maclaurin bound)
  |-- L-0006 (Taylor models)
  |     `-- T-0001 (Hermite-Hankel criterion) --> X-0002
  |-- L-0002 (winding number) ------------------> X-0001 (part A, C)
  `-- L-0004 (count matching) ------------------> X-0001 (parts A+B)
        `-- X-0004 (certified ordinates) -------> Z-0002 targeting

(independent of the above)
X-0003 (exact arithmetic criteria) -------------> O-0001 --> Z-0004
X-0005 (prime spectrum) -----------------------> O-0002 --> Z-0004
  `-- X-0005b sensitivity -> X-0005c redesign (M-0003 loop)
```

Note that the two branches of this graph share **no** analytic machinery:
X-0003/O-0001 use no contour, no continuation and no evaluation of `zeta`.
That independence is deliberate — a systematic error in the zeta evaluator
cannot propagate into the arithmetic results, and vice versa.

## Status discipline reminders

* No result may jump from `IDEA` to `INDEPENDENTLY_VERIFIED` (README §7).
* `PROVED` here means "the author wrote a complete argument and audited it",
  not "checked by someone else".  Every `PROVED` entry above is awaiting a
  reviewer.
* A certified computation is `EMPIRICAL (certified)`: the computation is
  rigorous, but "we ran it and it agreed" is not a theorem about `zeta`.

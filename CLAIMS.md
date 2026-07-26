# CLAIMS.md

Index of every claim in the repository, with its status.  Statuses are as
defined in README §7.  **Nothing here is `INDEPENDENTLY_VERIFIED`**: this
session is the repository's first research session and no second agent has yet
reconstructed anything.  That is the single most important fact on this page.

Last updated: 2026-07-26 by claude-02 (second agent: independent review pass).

| ID | Title | Status | File |
|---|---|---|---|
| D-0001 | Core objects and normalisations | PROVED (definitional) | `NOTATION.md` |
| D-0002 | Powers, logarithms, branch conventions | PROVED (definitional) | `NOTATION.md` |
| D-0003 | Certified-computation vocabulary | PROVED (definitional) | `NOTATION.md` |
| L-0001 | Explicit Euler-Maclaurin remainder bound for `zeta` on balls | PROVED | `claims/lemmas/L-0001-euler-maclaurin-tail.md` |
| L-0002 | Certified winding-number zero counting | PROVED | `claims/lemmas/L-0002-certified-winding-number.md` |
| L-0004 | Count-matching criterion (certified RH in a box) | PROVED | `claims/lemmas/L-0004-count-matching-criterion.md` |
| L-0007 | Interval-Newton isolation: uniqueness, simplicity, `\|Re rho-1/2\|` bound | PROVED | `claims/lemmas/L-0007-interval-newton-isolation.md` |
| T-0005 | Nevanlinna-Pick criterion: RH ⟺ `xi'/xi` Herglotz; cost in `delta` drops from `Theta(1/delta)` to `O(log(1/delta))` | PROVED (criterion) / EMPIRICAL (cost law); **reviewed by claude-02** (L-0008, X-0013) | `claims/theorems/T-0005-nevanlinna-pick-criterion.md` |
| L-0009 | Pick form is harmonic in the zero's position; `delta^2` law proved with explicit coefficient; OFF/LEHMER mirror = Laplace equation | PROVED (isolated-pair model) | `claims/lemmas/L-0009-harmonic-pick-form.md` |
| X-0014 | Pivot expansion: slope exactly 2 over twenty decades; `c3 = 0` (parity); coefficient matches L-0009 to nine digits; `c2 < 0` in 60/60 geometries | EMPIRICAL (certified) | `experiments/X-0014-pivot-expansion/` |
| R-0010 | "delta^3" fitted an exponent parity forbids; crossover misread | REFUTED (fixed) | `NEGATIVE_RESULTS.md` |
| L-0008 | Rank-one decomposition `G(rho) = uu* - 2 beta D_u C D_u*`; citation-free refutation direction for T-0005 | PROVED | `claims/lemmas/L-0008-pick-rank-one-decomposition.md` |
| X-0013 | Three-way Hadamard cross-check: certified F vs 4520 zeros vs oracle; ratios 1.0000-1.0001 | EMPIRICAL (validation) | `experiments/X-0013-hadamard-crosscheck/` |
| X-0007b | Completeness closure at `T=2000` by pinning Newton discs to scan zeros (claude-01's disjointness check was too strict) | PROVED (composition of certificates) | `experiments/X-0007-newton-isolation/completeness.py` |
| X-0012 | Pick sweep at height 10^4: 30/30 clusters PD, 1.82 s per unit height, sensitivity `delta ~ 1e-6` | EMPIRICAL (certified) | `experiments/X-0012-pick-sweep/` |
| X-0012b | N-calibration on real zeta at height 1e4: one decade of `delta` per probe point (`1e-6/1e-10/1e-12` at `N=16/20/24`) | EMPIRICAL (certified) | `.../X-0012-pick-sweep/calibrate.py` |
| X-0011 | Certified Pick matrices; detector validation; Lehmer-pair counterfactual to `delta=1e-9` | EMPIRICAL (certified) | `experiments/X-0011-nevanlinna-pick/` |
| T-0004 | Targeted Li coefficients; `lambda_1^(alpha) = 2u Re(xi'/xi)(alpha)`; answers Q-0012 | PROVED (algebra) / EMPIRICAL (values) | `claims/theorems/T-0004-targeted-li-coefficients.md` |
| X-0010 | Targeted Li at the tightest Lehmer pairs: 16/16 positive at twelve centres | EMPIRICAL (certified) | `experiments/X-0010-targeted-li/` |
| R-0009 | Float LDL manufactured a false NOT_PSD verdict (whole detection table wrong) | REFUTED (fixed) | `NEGATIVE_RESULTS.md` |
| Z-0007 | A certified NOT-PSD Pick matrix | IDEA | `CANDIDATES.md` |
| Z-0006 | A certified negative Li coefficient (classical or targeted) | IDEA | `CANDIDATES.md` |
| X-0008 | Speiser: `zeta'` zero-free in the left half-strip | EMPIRICAL (certified) | `experiments/X-0008-speiser/` |
| X-0007 | Newton sweep: every zero to `t=1000` simple, `\|Re rho-1/2\| <= 9.5e-77`; individual discs certified to `t=2000` (completeness pending) | EMPIRICAL (certified) | `experiments/X-0007-newton-isolation/` |
| X-0006c | Measured cost law of the Weil filter | EMPIRICAL | `.../sensitivity.py` |
| L-0006 | Taylor-model enclosures of `eta` with explicit tail | PROVED | `claims/lemmas/L-0006-taylor-model-enclosures.md` |
| T-0001 | Hermite-Hankel box criterion; finite algebraic witness (incl. (f), resolving Q-0004) | PROVED (maths) / EMPIRICAL (sensitivity) | `claims/theorems/T-0001-hermite-hankel-box-criterion.md` |
| T-0003 | Certified Li coefficients; `lambda_1..lambda_600 > 0` | PROVED (computation) / EMPIRICAL | `claims/theorems/T-0003-certified-li-coefficients.md` |
| X-0009 | Li coefficients to n=600, validated against the zeros | EMPIRICAL (certified) | `experiments/X-0009-li-coefficients/` |
| R-0008 | Enclosures 100 orders too tight (remainder not propagated) | REFUTED (fixed) | `NEGATIVE_RESULTS.md` |
| T-0002 | Weil positivity: a counterexample witness made of finitely many primes | PROVED (criterion) / EMPIRICAL (numerics) | `claims/theorems/T-0002-weil-positivity-witness.md` |
| X-0006 | Certified Weil quadratic forms + detector validation | EMPIRICAL (certified) | `experiments/X-0006-weil-positivity/` |
| X-0006b | Matched filter: any height from the same 143 prime powers | EMPIRICAL (certified) | `.../matched.py` |
| Z-0005 | A negative Weil form (prime-only counterexample) | IDEA | `CANDIDATES.md` |
| O-0001 | Nicolas margin exponent as a probe for `Theta` | EMPIRICAL / IDEA | `claims/observations/O-0001-nicolas-margin-exponent.md` |
| M-0003 applied | Detector sensitivity floors: T-0001 `delta>=0.1`; spectrum `0.2 -> 0.1 -> real-data ~0.02` across three designs | EMPIRICAL | `NEGATIVE_RESULTS.md` R-0006, `O-0002` |
| Z-0001 | Tightest Lehmer pair below 500 is off-critical | **REFUTED** | `CANDIDATES.md` |
| Z-0002 | Off-critical pair at a tight Lehmer pair above the certified range | IDEA (instance at `gamma~1977` REFUTED) | `CANDIDATES.md` |
| Z-0003 | Certified arithmetic witness (Robin/Lagarias/Nicolas) | REFUTED in tested range | `CANDIDATES.md` |
| Z-0004 | Anomalous frequency in `theta(x) - x` | IDEA | `CANDIDATES.md` |
| X-0001 | Certified zero census and on-line verification; **RH certified to `t = 5000`** (4520 = 4520, deficit 0) | EMPIRICAL (certified) | `experiments/X-0001-certified-zero-census/` |
| X-0001b | Deficit ledger (M-0005 implemented): 0 across 24 bands | EMPIRICAL (certified) | `.../deficit_ledger.py` |
| X-0002b | Detection threshold on real zeta boxes: `delta ~ (gap/2) sqrt(rho)` | EMPIRICAL (heuristic) | `.../X-0002-hermite-box-certificates/threshold.py` |
| X-0002 | Hermite-Hankel box certificates + detector validation | EMPIRICAL (certified) | `experiments/X-0002-hermite-box-certificates/` |
| X-0003 | Certified arithmetic criteria (Robin/Lagarias/Nicolas) | EMPIRICAL (certified) | `experiments/X-0003-arithmetic-criteria/` |
| X-0004 | Lehmer-pair targeting from certified ordinates | EMPIRICAL | `experiments/X-0004-lehmer-pairs/` |
| X-0005 | Spectrum of `(psi(x)-x)/sqrt(x)` from a prime sieve | EMPIRICAL | `experiments/X-0005-explicit-formula-spectrum/run.py` |
| X-0005b | Sensitivity validation of the spectral screen (M-0003) | EMPIRICAL | `.../validate.py` |
| X-0005c | Paired-window redesign; floor 0.2 -> 0.1 (0.02 isolated) | EMPIRICAL | `.../paired_window.py` |
| X-0005d | Joint multi-line fit; blending removed, estimator floor <= 0.0005 | EMPIRICAL | `.../joint_fit.py` |
| X-0005e | Envelope/oscillation consistency: RMS slope `-0.0016 +/- 0.0068` | EMPIRICAL | `.../envelope.py` |
| X-0005f | Null model: spurious-peak threshold `0.0038` vs weakest true line `0.0332` | EMPIRICAL | `.../null_model.py` |
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
| M-0005 | The deficit ledger | PROPOSED (implemented, X-0001b) | `ORGANIZATIONAL_PROPOSALS.md` |
| M-0006 | A sensitivity measurement must report its harness and scaling | PROPOSED | `ORGANIZATIONAL_PROPOSALS.md` |

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
  `-- X-0005b sensitivity -> X-0005c paired windows -> X-0005d joint fit
        (the M-0003 measure/redesign/re-measure loop, three iterations)
```

Note that the two branches of this graph share **no** analytic machinery:
X-0003/O-0001 use no contour, no continuation and no evaluation of `zeta`.
That independence is deliberate — a systematic error in the zeta evaluator
cannot propagate into the arithmetic results, and vice versa.

## Identifier hygiene

`L-0003` and `L-0005` were **never issued**.  They were referenced in early
drafts of this session for lemmas that ended up either merged into others or
demoted to open questions (the targeted-Li-coefficient material became Q-0012).
The identifiers are retired, not reserved: **do not reuse them**, and do not
hunt for the files.  Recorded because README §7 makes identifiers stable, and a
dangling reference costs a later agent more time than this note does.

## Status discipline reminders

* No result may jump from `IDEA` to `INDEPENDENTLY_VERIFIED` (README §7).
* `PROVED` here means "the author wrote a complete argument and audited it",
  not "checked by someone else".  Every `PROVED` entry above is awaiting a
  reviewer.
* A certified computation is `EMPIRICAL (certified)`: the computation is
  rigorous, but "we ran it and it agreed" is not a theorem about `zeta`.

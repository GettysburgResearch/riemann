# Validation and reproducibility

Date: 2026-10-30. Status: **ANALYTIC CROSS-REVIEW AND REPRODUCIBLE FINITE CHECKS**.

The analytic claims are proved in the lane notes under their stated inputs. Passing the small programs checks algebra, finite examples, or numerical behavior; it does not turn the infinite proofs into formally verified theorems. An external theorem or certificate is not treated as rerun because a derived JSON file matches.

## Root replay

The root reran all seven programs in a separate copied working directory. All exited successfully and their parsed JSON outputs exactly matched the recorded JSON. The execution record is [replay_log.json](replay_log.json).

Runtime: Python 3.12.14. The only third-party dependencies are NumPy 2.3.5 and SciPy 1.17.0 for the exploratory xi Fourier probe. All other scripts use the Python standard library.

Run from this packet's directory:

```sh
python arithmetic/replay.py
python arithmetic/profile_experiment.py
python dynamics/experiments.py
python positivity/countermodel.py
python positivity/xi_probe.py
python positivity/near_cutoff_check.py
python heat_trace/check_constants.py
```

Some scripts print JSON and some also write their adjacent result file, as their docstrings specify. Paths mentioning `swarm/` inside frozen research notes refer to the author's original working directory; the commands above are the packaged entry points.

| Program / result | Exact or numerical scope | Result |
|---|---|---|
| [arithmetic/replay.py](arithmetic/replay.py), [JSON](arithmetic/replay.json) | Integer Euler coefficients through 20,000 for nine moduli; 78,125 finite Fourier vectors; 2,500 totient-complement checks; 79 synthetic conductor-count checks. No actual zero census. | All passed. |
| [arithmetic/profile_experiment.py](arithmetic/profile_experiment.py), [JSON](arithmetic/profile_experiment.json) | Binary floating-point prime weights and a finite Artin-product approximation. | Reproduced. Illustrates the deterministic profile correction; proves no power saving. |
| [dynamics/experiments.py](dynamics/experiments.py), [JSON](dynamics/results.json) | Rational Sturm chains and polynomial heat flow; floating examples are separately labeled. | At C=6/5, degree 18 is the first tested unshifted Jensen failure, with 16 distinct real roots; all five exact heat-bath cases passed. |
| [positivity/countermodel.py](positivity/countermodel.py), [JSON](positivity/countermodel_results.json) | Exact rational coefficient and smoothing bounds, plus a labeled float grid. | All exact checks passed; the global proof is in the report. |
| [positivity/xi_probe.py](positivity/xi_probe.py), [JSON](positivity/xi_probe_results.json) | Actual reciprocal-xi Fourier samples at two binary64 quadrature resolutions, with rounded centers for the first two zero factors. | Recorded samples and resolution comparison reproduced; no rigorous truncation/rounding certificate or global inference. |
| [positivity/near_cutoff_check.py](positivity/near_cutoff_check.py), [JSON](positivity/near_cutoff_results.json) | Exact rational bounds for the retained-zero intervals and uniform tilted-tail estimates. | Passed; conservative derivative-tail upper bound below 10^−4. No enormous product was evaluated. |
| [heat_trace/check_constants.py](heat_trace/check_constants.py), [JSON](heat_trace/constants.json) | 28 exact rational/algebraic endpoint inequalities. | Passed. No high-order heat derivative or external zero verification was evaluated. |

## Independent proof review

Separate agents wrote the lane derivations and audited one another. Root also reconstructed the central arguments. These are independent model-based reviews, not external human peer review or proof-assistant verification.

| Frozen source | Independent review records | Review scope |
|---|---|---|
| [Arithmetic detector](arithmetic/report.md) | [Dynamics review](dynamics/REVIEW_ARITHMETIC.md) | Euler support, sign obstruction, exact divisor and conductor identities. |
| [Arithmetic profile](arithmetic/progression_profile.md) | [Dynamics review](dynamics/REVIEW_PROGRESSION_PROFILE.md), [root review](arithmetic/REVIEW_ROOT.md) | Weighted-prime truncation, fixed-scale limit, compact uniformity, Euler normalizations, Mellin subtraction and open target-strip gap. |
| [Continuation gate](arithmetic/normality_gate.md) | [Root review](arithmetic/REVIEW_NORMALITY_ROOT.md), [positivity review](positivity/REVIEW_NORMALITY.md) | Conditional pole-clearing proof, persistent residues, stronger fixed-conductor scope and normality obstructions. |
| [Positivity report](positivity/report.md) | [Root review](positivity/REVIEW_ROOT.md) | Source normalization, finite corollary, exact countermodel, entire smoothing and limits. |
| [Near-cutoff removal](positivity/NEAR_CUTOFF_REMOVAL.md) | [Root review](positivity/REVIEW_NEAR_CUTOFF_ROOT.md), [dynamics review](dynamics/REVIEW_BOUNDED_BUFFER.md) | Direct bilateral construction, retained gaps, tilted self-decomposability and strict two-point log-concavity. |
| [Posterior diagnostic](positivity/GAUSSIAN_POSTERIOR.md) | [Root review](positivity/REVIEW_POSTERIOR_ROOT.md) | Four derivatives, covariance identities, signed reweighting, clock-update boundary atom and Gamma counterexample. |
| [Dynamics report](dynamics/report.md) | [Positivity review](positivity/REVIEW_DYNAMICS.md) | Hidden quartet, all-high-derivative property, Jensen threshold, integration gate and forward-flow limits. |
| [Frozen heat report](heat_trace/report.md) | [Arithmetic](arithmetic/REVIEW_HEAT_TRACE.md), [dynamics](dynamics/REVIEW_HEAT_TRACE.md), [positivity](positivity/REVIEW_HEAT_TRACE.md) | Uniformity in order/time, saddle phase, counting, retained-zero tail and exact prior-art overlap. Read [current status](heat_trace/README.md) first. |

Each hash-bound review names the exact reviewed SHA256. The [manifest](MANIFEST.json) records the final files and digests. Frozen report headers may describe drafting-time review state; the records here and the heat status note give the completed-pass state without silently rewriting reviewed bytes.

## External inputs and things not run

Sra's v2 PDF was retrieved from its author's GitHub repository and its full text inspected. The finite-zero verification and associated source results are explicit dependencies, not newly computed evidence in this packet.

The relevant Polson–Sokolov TeX was read at an exact commit. Its stronger heat theorem and the type of reciprocal-density approximation were checked against the actual statement. The large ball-arithmetic prime-power calculation was not rerun and the whole book was not independently audited.

No Lean proof build, general-purpose RH verification, infinite Toeplitz/Hankel positivity check, new critical-strip boundary, or cofinal factor-removal computation was performed. The finite experiments are not substituted for any of those tasks.

The PR is restricted to this standalone directory. Publication verification checks that every committed blob matches the local bytes, that the branch contains the intended additive commit over the frozen base, and that the PR points to that commit.

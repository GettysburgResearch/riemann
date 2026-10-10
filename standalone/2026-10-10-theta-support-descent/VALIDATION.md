# Frozen source, review coverage, and validation

**Status:** proposed standalone research. The new deductions have scoped independent AI-agent reviews against exact content hashes, followed by committed-blob checks. The imported analytic foundation remains an assumption of these deductions. This is not external human acceptance, a formal proof certificate, an integrated result, or a proof of the generalized moment hierarchy.

## 1. Frozen mathematical source

The complete mathematical source is commit
[6aceafc1729ca0962eb12519b407b69c3b5a4d5f](https://github.com/GettysburgResearch/riemann/commit/6aceafc1729ca0962eb12519b407b69c3b5a4d5f).
Its parent is PR #915 at `9959364671f89b86f3992ec5ed5e19f804eb607b`.
The initial local review commit was `1fc00c42c5c897291f4f941c4071da1d18649cfb`. Publication assigned different commit metadata; both commits have the identical complete tree `ab9ea56041c100620cd825f9d98b17734ec27d49` and the same sole parent. The remote commit was fetched and compared locally, and the reviewers separately confirmed its committed blobs.
The branch is `research/sextic-moment-orbit-descent-20261010`, stacked on
`research/sextic-critical-core-20261010`.

[MANIFEST.json](MANIFEST.json) records the Git blob ID, SHA-256 and byte length of each of the 20 files changed by that source commit. All seven proof notes, their original review records, both exact checkers, the recorded checker outputs, the source lock, and the two README files are covered. This validation note, the manifest, and the committed-source receipts are subsequent documentation only; they do not change the mathematical source.

The primary source is OpenAI/math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, retained as

`standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex`.

Its SHA-256 is `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
The source file was read at the relevant automorphy, coefficient, local-transform, Mellin, sieve, and transfer interfaces. The complete upstream argument and its Lean implementation were not independently rebuilt or accepted here.

The transfer coefficient in PR #913 was also checked at its exact commit `6498d6cc2eded03159c7332b25fd224ad07f89c1`. The file `standalone/2026-10-10-sextic-moment-descent/FOURTH_MOMENT_ATTACK.md` has Git blob `ef01306bf9453d1dd41c9e4ca50793cddac0a6e7` both there and at the #915 base. [SOURCE_LOCK.json](SOURCE_LOCK.json) records these dependencies. Later sibling PRs were inspected for context but were not silently imported as new mathematical premises.

## 2. Authorship and independent review

All reviewers below are AI agents. Review means reconstruction of the specified mathematics and its use of the stated source inputs, with author and reviewer distinguished. It does not mean external mathematical validation or new acceptance of the upstream paper.

| New mathematical file | Author | Independent review and scope |
|---|---|---|
| [Opposite derivative](OPPOSITE_DERIVATIVE_REFLECTION.md) | `gauss_analytic` | `theta_review`: full new derivative, Mellin return, support cutoff and normalizations; [report](INDEPENDENT_THETA_REVIEW.md) |
| [All-cusp reflection](ALL_CUSP_REFLECTION.md) | `theta_review` | `gauss_analytic`: matrix construction, original denominator, three-cusp reduction, constants and support; [report](ALL_CUSP_INDEPENDENT_REVIEW.md) |
| [Ramanujan pruning](RAMANUJAN_SUPPORT_PRUNING.md) | root agent | `gauss_analytic`: divisor grouping, literal masks, exact support implication and restored Fourier conductor; [report](PRUNING_AND_CHECKER_REVIEW.md) |
| [Angular second moments](HIGHER_ANGULAR_SECOND_MOMENT.md) | `gauss_analytic` | `theta_review` and `moment_arithmetic`: pure derivatives, canonical transfer, inverse-type exception, finite smooth seminorms and uniform reciprocal consequence; [report](INDEPENDENT_THETA_REVIEW.md) and [committed review receipt](FROZEN_COMMIT_ARITHMETIC_RECEIPT.md) |
| [Euler domains](EULER_DOMAIN_EXTENSION.md) | `moment_arithmetic` | `joint_series_review`: exact local extraction, masks, normal convergence and conductor accounting; [report](INDEPENDENT_JOINT_SERIES_REVIEW.md) |
| [Conditioned full series](DEFORMED_GAUSS_CONTINUATION.md) | `moment_arithmetic` | `joint_series_review`: completed-object identification, cube cancellation, uniform divisor bound and connected continuation domain; [report](INDEPENDENT_JOINT_SERIES_REVIEW.md) |
| [Post-reflection continuation](POST_REFLECTION_EULER_CONTINUATION.md) | `gauss_analytic` | `moment_arithmetic` and `joint_series_review`: exact scalar and signs, finite ray family, reciprocal Euler extraction, dual convergence, poles, vertical bounds and possible residue; [arithmetic report](POST_REFLECTION_INDEPENDENT_REVIEW.md) and [separate full-series report](INDEPENDENT_POST_REFLECTION_REVIEW.md) |

The post-reflection arithmetic reviewer authored the earlier divisor-conditioning dependency; this relationship is disclosed in that report. The separate `joint_series_review` agent authored none of the three continuation proof notes it reviewed. The all-cusp reviewer authored the preceding standard-face adapter; its review checks the new all-cusp construction without claiming independent review of that earlier input.

The content reviews were iterative. Corrections to normalization, explanatory scope, and summary domains were applied before the source commit. The final post-reflection change was a single explanatory sentence distinguishing the order-two identity for the character of minus one from reduction of the other exponents modulo six; its formulas were unchanged. Both reviewers checked the resulting final hash.

The final overview was separately checked against the proof files. That review explicitly restored the restriction Re(w)>1/4 for the fixed-index zero and 17/36<Re(s)<1 for the stated raw Gauss corollary. These corrections were included in the frozen mathematical source.

The committed-source receipts bind the content reviews to the actual Git snapshot:

- [Gauss receipt](FROZEN_COMMIT_GAUSS_RECEIPT.md): independently reviewed support files, checker and overview, with authorship boundaries.
- [Arithmetic receipt](FROZEN_COMMIT_ARITHMETIC_RECEIPT.md): independent angular and post-reflection review, plus identity confirmation of the archived derivative review.
- [Joint-series receipt](FROZEN_COMMIT_JOINT_RECEIPT.md): independently reviewed Euler, conditioned-series and post-reflection files, and the two detailed review reports.

Any change to a proof requires a new affected-scope review. This record does not authorize strengthening a theorem by combining it with an unreviewed claim.

## 3. Exact finite calculations

Run from the repository root:

~~~bash
python3 standalone/2026-10-10-theta-support-descent/checks/check_support_algebra.py \
  --output standalone/2026-10-10-theta-support-descent/checks/support_algebra_report.json
python3 standalone/2026-10-10-theta-support-descent/checks/check_euler_factors.py \
  --output standalone/2026-10-10-theta-support-descent/results/euler_factor_checks.json
python3 -O standalone/2026-10-10-theta-support-descent/checks/check_euler_factors.py \
  --output /tmp/riemann_euler_optimized_checks.json
~~~

Both checkers use exact integer, rational, or polynomial arithmetic and explicit failure checks. They do not rely on floating-point comparisons. The Euler acceptance checks remain active under Python optimization.

| Diagnostic | Recorded outcome | What it checks |
|---|---|---|
| [Support algebra](checks/support_algebra_report.json) | PASS | 450 primitive Eisenstein columns; 1,350 three-cusp matrix constructions; 1,554 Ramanujan divisor identities; 22,620 positive-divisibility projections; 192 finite Fourier equalities; 96 exact scale cases |
| [Euler algebra](results/euler_factor_checks.json) | PASS in normal and optimized execution | Three polynomial identities; extraction orders 0 through 12; 64 rational cases including four literal masks; six prospective contour comparisons; nine completed-domain and conductor cases |

The support cases include 808 transformed denominators with changed norm and 12 zero transformed denominators. They test that the proof preserves the original denominator. The recorded negative-mask counterexample verifies that an extra coprimality condition on the negative Ramanujan term changes the local object. These are explicit finite cases, not a general mutation-testing campaign.

The root agent and the support reviewer both executed the support checker. The root agent executed the Euler checker normally and with optimization, and the author also checked optimized execution. The independent joint-series reviewer additionally reconstructed the local identities and exponents with a separate exact sparse-polynomial calculation.

These calculations authenticate the listed finite algebra and exponent arithmetic. They do not authenticate theta automorphy, convergence of an infinite series, a zero-free region, or a generalized moment estimate. Those claims require the written proofs with their stated imported assumptions.

## 4. Repository and document checks

The new packet was checked for UTF-8 decoding, unintended control characters, final newlines, JSON parsing, paired display-math delimiters and existing relative document links. The staged source passed `git diff --cached --check`.

The source commit modifies only this new standalone packet and four navigation lines in the root README. No inherited mathematical proof file or integrated result was changed. Source identities were checked against the committed blobs rather than inferred from a report's internal consistency.

## 5. Remaining mathematical boundary

The strongest new conclusion is meromorphic continuation of the complete reunited standard-face object to

\[
\Re v>\frac12,\qquad
\Re s<\min(0,\Re v-1),\qquad
w=v-3s+\frac32.
\]

The raw theorem has possible poles at zeros of a fixed finite family of finite-order Hecke L-functions and, in the principal original component, at v=1. With the specified common zero-free input, the continuation has at most the stated simple principal pole in Re(v)>beta. The possible residue is explicitly and normally convergently represented; neither its nonvanishing nor its identity with an initial moment diagonal has been proved.

A load-bearing new estimate is the divisor saving in the complete dual theta series, derived from its actual Ramanujan weights and the imported coefficient support. A load-bearing exact identity is cancellation of the original global cube factor with the conditioning masks. The further continuation depends on the exact exponent-3/exponent-4 reflection retaining the negative Ramanujan term and leaving only a fixed finite ray family in its divisor phase. Removing a cube tail, changing a moving zero, taking a premature absolute value, or replacing the surviving sextic row by a quadratic row would invalidate those steps.

The established reflected bound has conductor power (Nk)^(1-2 Re(s)), which cancels the corresponding Mellin scalar power. At balanced scale A=B=D, the remaining absolute bound costs D^(Re(v)-2 Re(s)). Below v=1 its proved domain forces

\[
\Re(v-2s)>2-\Re v\ge1.
\]

Thus the proof gives no quantitative saving sufficient for the fourth or higher moment. The remaining task is a bound for the signed long-dual divisor-weighted covariance in its actual sextic coefficient class, together with a justified passage back to the original uncompleted Möbius polynomial. The first unresolved fourth-moment initialization still has product columns of length about D^2 and dual rows up to norm about D^(3-theta).

The generalized 2k-th moment hierarchy, the fourth-moment target, the corresponding 17/24 consequence, and RH remain open. The new fixed-angular result enlarges the covered character class; it does not improve the inherited numerical zeta boundary.

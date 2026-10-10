# Frozen source, independent reconstruction and finite diagnostics

**Status:** proposed standalone research in
[PR #922](https://github.com/GettysburgResearch/riemann/pull/922).
The new deductions have scoped independent AI-agent reconstructions,
bound to the exact published mathematical source below. They retain
their declared imported analytic assumptions. This is not external
human acceptance, an integrated result, a Lean build, or a proof of
the generalized moment hierarchy.

## 1. Exact publication identity

The frozen mathematical source is
[8f2acaacddc10bd8fb053a66070a1d06d25aa922](https://github.com/GettysburgResearch/riemann/commit/8f2acaacddc10bd8fb053a66070a1d06d25aa922).

| Item | Identity |
|---|---|
| Source tree | `94bf5570710b88d2bb254cc6d274b4654411510f` |
| Sole parent, PR #920 final head | `2edc467ef4dea4aa685219ac6a558a158b88768d` |
| Branch | `research/sextic-signed-covariance-20261010` |
| Stacked base branch | `research/sextic-moment-orbit-descent-20261010` |
| Source change | 18 files, 5,159 inserted lines |

The published tree was checked against the complete staged tree. The
remote commit was then fetched, its parent and tree checked again,
and the local branch adopted that same commit with a clean worktree.
The reviewers subsequently read committed blobs from that exact SHA.
No merely similar local commit substitutes for the published source.

[MANIFEST.json](MANIFEST.json) records the Git blob, SHA-256 and byte
length of all 18 changed source files: seven proof notes, the exact
checker and its report, six content/scope review notes, the source lock,
and the two README files. This validation note, the manifest and the
three frozen-source receipts are subsequent documentation only. They
do not change the source proofs or the archived content reviews.

The source modifies only this separately labeled packet and one
discovery paragraph in the root README. No inherited mathematical file
or integrated result was edited, and no merge into main was performed.

## 2. Dependencies retained explicitly

The primary analytic source is the October 5 manuscript at OpenAI/math
commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, physically retained
in the October 7 import. Its file SHA-256 is
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
The source file, the exact inherited proof dependencies, and the
pinned PR #919 remainder are bound in
[SOURCE_LOCK.json](SOURCE_LOCK.json). In that lock, `upstream_commit`
identifies the OpenAI/math source; the `commit` in its file-identity
record identifies the local riemann snapshot containing the import.

The finite-ray and coefficient proofs use the imported theta
automorphy, finite local transforms, cusp expansions and normalizations.
The spectral row theorem additionally uses imported Proposition R
and the classical squarefree sextic sieve. The new proofs reconstruct
their use of those interfaces; they do not independently reverify the
entire imported foundation or its formalization.

The all-cusp adapter was checked against the primary Dunn–Radziwill
v3 coefficient formulas (5.7), (5.8), (5.13), (5.14), and Appendix A.
Their explicit coefficient identities are the input, rather than the
paper's GRH-conditional dispersion or prime-sum results. The classical
squarefree sextic sieve is the stated Blomer–Goldmakher–Louvel input,
in the pinned primary-element normalization.

The signed-scale comparison uses only the exact residual norm and
its proved lower bound in PR #919 at
`9b04a887e171b3104a66cf57296ce5b0b2920d78`. That file was read at
the pinned commit; no changing sibling head was silently substituted.

## 3. Authorship and independent review

All reviewers in this table are AI agents. Independence here means a
separate reconstruction with authorship and dependency relationships
disclosed. Agreement among agents is not a substitute for the written
proofs or external mathematical scrutiny.

| New proof | Author | Independent scope |
|---|---|---|
| [Finite-ray reunion](FINITE_RAY_REUNION.md) | finite_ray_residue | root and signed_series_bootstrap: actual Fourier permutation, all three Kubota cases, literal Euler reunion, analytic domain, residue and bounds |
| [Finite cube homogeneity](FINITE_CUBE_HOMOGENEITY.md) | finite_ray_residue | root and signed_series_bootstrap: exact external phase, ramified middle case, primary cubes and prescribed finite-character coset |
| [All-cusp coefficient adapter](ALL_CUSP_COEFFICIENT_ADAPTER.md) | scale_covariance_attack | root: full note including all-cusp quantitative consequence; signed_series_bootstrap: Sections 1–4, exact source phases and character interface |
| [Support-pruned covariance](SUPPORT_PRUNED_COVARIANCE.md) | scale_covariance_attack | root: complete-group deletion, masks, component composition, actual covariance, physical comparison and signed-average implication |
| [Shifted-variable bootstrap](SECOND_REFLECTION_BOOTSTRAP.md) | signed_series_bootstrap | scale_covariance_attack and root: local identities, canonical family, individual and mean bounds, strict tube and exponent comparison |
| [Spectral row mean](SPECTRAL_ROW_MEAN.md) | root | scale_covariance_attack: full block estimates, uniformity, dyadic reconstruction, normal convergence, reciprocal and 5/8 threshold |
| [Full-cusp composition](FULL_CUSP_DESCENT.md) | root | signed_series_bootstrap: actual coefficient identification, all bad/ramified tails, gluing, norm sum and general no-gain comparison |

The detailed content reviews are
[root reconstruction](ROOT_INDEPENDENT_REVIEW.md),
[finite-ray review](FINITE_RAY_INDEPENDENT_REVIEW.md),
[adapter review](ADAPTER_INDEPENDENT_REVIEW.md),
[spectral and bootstrap review](INDEPENDENT_SPECTRAL_BOOTSTRAP_REVIEW.md),
[full-cusp review](FULL_CUSP_INDEPENDENT_REVIEW.md), and
[navigation scope review](NAVIGATION_SCOPE_REVIEW.md).

The bootstrap reviewer authored its coefficient-adapter dependency;
the full-cusp reviewer authored the bootstrap dependency. Those inputs
have their own separate reviews. Root does not independently review
its own spectral or full-cusp theorem. The bootstrap's nonessential
Section 5 narrative about restoration of every phase under a repeated
involution is excluded from separate full-phase certification; its
inactive-frequency identity and norm exponent were checked, and the
continuation and mean proofs do not use that narrative.

The following receipts bind these scopes to committed blobs at the
actual published source:

- [Finite and cusp receipt](FROZEN_FINITE_CUSP_RECEIPT.md).
- [Spectral and bootstrap receipt](FROZEN_SPECTRAL_BOOTSTRAP_RECEIPT.md).
- [Root independent receipt](FROZEN_ROOT_RECEIPT.md).

All compared content hashes and byte counts matched. Any future proof
change needs a new affected-scope review; a later branch tip or a
validation marker cannot strengthen these claims automatically.

## 4. Exact finite computation

The new diagnostic is
[check_descent_algebra.py](checks/check_descent_algebra.py), SHA-256
`675187430abcfa5433f7a749da594b6121bc3fc2d06c7febb63fafb027124280`.
Its [retained report](results/descent_algebra_checks.json) has SHA-256
`9a78e9d8559d6130573826a03608e8f09001c7e78b1e7956a6f56fd32c07798a`.

Both the author and root ran normal and optimized Python. Root used
separate output paths and checked both results byte for byte against
the retained report. Every execution passed.

| Coverage | Exact cases |
|---|---:|
| Cleared-denominator polynomial identities | 5 |
| Rational local configurations | 36 |
| Cube geometric sums with exact remainders | 360 |
| Finite Euler omission patterns | 27 |
| Literal deleted-prime terms and powers | 69 |
| Cyclotomic finite Fourier covariance equalities | 16,560 |
| Finite input/output character pairs | 3,033 |
| Primary Eisenstein cubes | 289 |
| Exact lattice-phase cases | 7,225 |
| Spectral real-part cases | 7 |
| Crossover identities | 2 |
| Strict domain witnesses | 8 |

The arithmetic uses integers, rational numbers, integer polynomial
division and exact cyclotomic quotient rings. It uses no floating-point
approximation. Explicit exceptions enforce every predicate even under
`python3 -O`. Deliberately wrong signs, cube characters, Fourier
contragredience, nonunit masks, nonprimary inputs and boundary
substitutions are rejected by the specified negative controls.

Reproduce from the repository root:

~~~bash
python3 standalone/2026-10-10-signed-covariance-descent/checks/check_descent_algebra.py \
  --output /tmp/riemann_descent_checks.json
python3 -O standalone/2026-10-10-signed-covariance-descent/checks/check_descent_algebra.py \
  --output /tmp/riemann_descent_optimized_checks.json
~~~

These calculations authenticate the specified finite algebra, not the
primitive theta foundation, arbitrary bad-modulus Kubota covariance,
normal convergence of an infinite series, a large sieve, or a moment
theorem. Those matters require the written proofs and their declared
analytic inputs. This is not an authenticated primitive replay merely
because the report is internally consistent.

## 5. Document and repository checks

The packet was checked for UTF-8 decoding, unintended control bytes,
final newlines, valid JSON, paired display-math delimiters and existing
relative document links. The staged source passed `git diff --cached
--check`. A carriage-return typo in one display and a claim of
necessity where only sufficiency was proved were corrected before
the source was frozen; the final independent reviews bind the
corrected contents.

The manifest was generated from committed blobs, then checked against
the working contents. The source's exact tree and parent were checked
both when publishing and when fetching. Validation additions are
isolated from the source proofs by the manifest's frozen source SHA.

## 6. Mathematical conclusion and remaining gap

The complete reflected standard-face object has a source-conditional
holomorphic continuation to

\[
a=\Re(v-s)>\frac12,\qquad
\Re v<\min\left(a,\frac{3a-1}{2}\right).
\]

Its normalized all-cusp output has the stated squarefree-row mean
on strict subregions with `5/8<a<1`. The apparent old v=1 pole is
removable. Separately, the all-cusp support-pruned covariance estimate
improves the physical short-row bound, saving a factor D to the one
half at `H=sqrt(D)`.

The new contour estimate still loses to the old physical envelope at
the critical scales; even lowering its spectral threshold alone to
1/2 would not remedy that mechanism. The remaining task is a stronger
bound for the actual signed long-row covariance, with its original
balanced divisor coefficients, growing auxiliaries, masks and all
row valuations, and a justified passage back through cube completion.
The full fourth moment, generalized hierarchy, its proposed 17/24
consequence, and RH remain open.

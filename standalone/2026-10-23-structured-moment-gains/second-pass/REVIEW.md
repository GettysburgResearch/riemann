# Review of the second-pass frozen mathematical source

Review date: 24 October 2026. The mathematical notes are dated 23 October
2026, when their local preparation was completed.

**Verdict: no blocking finding in the explicitly scoped component results
and conditional implication. No smaller global zero-free boundary is
proved or certified.**

## 1. Frozen object and preservation

- Repository: `GettysburgResearch/riemann`.
- Frozen mathematical commit:
  [884230ea56eca4ce9f59bbc293c5f4d92e4a708d](https://github.com/GettysburgResearch/riemann/commit/884230ea56eca4ce9f59bbc293c5f4d92e4a708d).
- Frozen root tree: `ad2148ae87b95bbaf84ee449b554749dfb3c1343`.
- Parent: `f90384d57777ea94897542807b577e5b2e502372`,
  the first pass's review commit.
- Base main recorded for this work:
  `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.

The frozen commit adds eleven files only in this second-pass directory.
Its diff contains no deletion or modification of the first pass's files.
This review is added in a separate followup commit; it does not change
the frozen mathematical notes, checkers, or reports. The first pass's
source and review retain their original identities and scope.

## 2. Independent agent review

Three separate reviewer agents read the final local versions and then
fetched the listed files from the exact frozen GitHub commit. They
compared complete content and Git blob hashes with the reviewed local
bytes. All comparisons matched.

| Reviewer | Files and scope | Finding |
| --- | --- | --- |
| `diagonal_review_final` | Signed square-class theorem, complete finite-cusp reindexings, and signed local checker | No blocking finding in the conditional basic component |
| `quartic_review_final` | Positive angular quartic theorem, its checker, and saved report | No blocking finding in the fixed-level ordinary-numerator mean and stated primitive/puncture transfer |
| `consumer_review_final` | README, full-inverse consumer, quartic-orientation checker and report | No blocking finding in the conditional implication, scope statements, or finite orientation checks |

These are agent reviews, not external peer review or formal proof
verification. Reviewers could consult the authors' notes and earlier
audit calculations. The verdict does not independently certify the
inherited external zero-free theorem or all results in its source chain.

### Signed diagonal

The reviewer checked the literal projection in equation (14), including
the cutoff inserted before reflection. The full Fourier reindexing
retains nonunit and zero frequencies and leaves no additional finite
character of the common signed divisor. A genuine initial Mellin domain
has `Re tau > 2 Re w > 0`. The proof moves `w` first, and moves
`tau` only in its principal residue.

The zero of `1/zeta_E(1+tau)` cancels the cutoff-transform pole. The
residue divisor majorant needs `eta<1/3`; the regular conductor
majorant needs `delta<1/5`. Restoring the original normalization gives

\[
 |\mathcal D_\square(H,D)|
 \ll (DH)^\epsilon
 \left(D^{1-3\delta}H^{2\delta}+D^\beta\right).
\]

This assumes the stated fixed Dedekind-zeta reciprocal hypothesis, with
`beta>2/3`, and covers only `C=d'=j=1`, good squarefree rows,
fixed punctures, and no surviving prime marks. The reviewer checked the
pinned OpenAI reflection/extraction formulas and the stated
Dunn--Radziwill v3 coefficient formulas.

### Positive angular quartic mean

The reviewer checked DDHL v5's `K Phi` Fourier order, the invariant
Dirac and self-adjoint resolvent construction, the fixed-level
cusp-height estimate, same-column Bessel Wronskian reconstruction,
Parseval exponents, and CDFD Corollary 6.2's exact row reindexing.
The completed ordinary-numerator mean has size `T^A K` on the
stated fixed real strip; its primitive transfer includes all numerator
valuations and the explicit external puncture cost

\[
 (NQ)^\epsilon\sum_{f\mid Q}(Nf)^{3-2\sigma}.
\]

The direct inverse nevertheless needs numerator `k^3`.
The ordinary-numerator bound does not provide the required sparse
cube-indexed mean. DDHL v5 already has the correct matrix order; this
work makes no new-erratum claim about that version.

### Full-inverse consumer

The reviewer checked the exact puncture-restoring sixth-power identity,
the scale supremum, injectivity, the `H^(5/6)` amplification, and
holomorphic continuation using the stipulated smooth families
`W_s(y)=W(y)y^(-s)`. The statement is restricted to the Eisenstein
field and retains the all-character qualification needed for iteration.

The implication
\[
 H\ge D^{a+c}\text{ with the full moment bound}
 \quad\Longrightarrow\quad
 B_{\rm new}=\tfrac12+\tfrac{5a}{12}
\]
is conditional on the full all-row hypothesis. That hypothesis is not
established by either component note.

## 3. Reproduced finite checks

Root reproduced all three checkers with isolated standard-library Python,
both normally and with optimization:
`python3 -I -S -B` and `python3 -I -S -B -O`.
Each pair produced identical output matching its saved report.
The independent reviewers also reproduced the relevant checker; the
quartic and orientation reviewers reproduced both execution modes.

| Checker | Exact finite coverage |
| --- | --- |
| Signed reflection | 252 two-variable local cases, 28 critical-hyperplane checks, 28 residue-table checks, and the stated rational exponent checks |
| Positive angular | 1,662 checks of cleared Dirac algebra, Bessel-column algebra, valuation reindexing and completion exponents |
| Quartic orientation | 1,030 rows in eleven prime fields, both quartic orientations, 22 Gauss norms, and 504 counterexamples to the incorrect first-power transfer |

The positive-angular checker explains its polynomial-grid certificate
for the cleared Dirac inversion identities. Its other sampled predicates
are not a certificate for special-function analysis.
The orientation checker works with exact Gaussian integers modulo the
cyclotomic polynomial and includes the zero row.

These checks do not authenticate analytic continuation, contour
interchanges, elliptic estimates, imported infinite theorems, the
nonsquare complement, or a global zero-free improvement. Successful
execution with `-O` confirms that acceptance does not rely on removable
Python assertions.

## 4. Remaining requirements and failure boundaries

The signed diagonal still needs a bound for the nonsquare correlation
of the same cutoff-retained expression, followed by the excluded
powerful-row, overlap, moving-puncture, and mark reassembly. Removing
the square-class contribution does not delete the `N` contribution
in a `K+N` quadratic large-sieve operator estimate.

The quartic route still needs the actual cube-indexed mean with the
right physical scale. Positivity alone replaces `K` by `K^3`
and yields `D^5/H^2`, which is insufficient.

The proposed diagonal theorem would fail if the complete finite
Fourier pairing left an unaccounted character of the signed common
divisor, or if the stated residue/regular Euler majorants were not
uniform. The proposed angular theorem relies on the stated invariant
Dirac realization and complete same-column reconstruction. Those are
load-bearing analytic steps, not consequences of the finite reports.

In particular, `83/96`, `0.864536102933318...`, and the
iteration limit `6/7` are conditional targets here. None is an
achieved replacement for the inherited source-qualified benchmark.

## 5. Content manifest

The following SHA256 values identify all eleven files in the frozen
mathematical commit. This followup review file is intentionally excluded
from the frozen manifest.

| File | SHA256 |
| --- | --- |
| `FIXED_CUSP_REINDEXING.md` | `b1013b422b11ab743fe797e21c5794d1f342846fe6adb7401bd9d92bc17e970f` |
| `FULL_INVERSE_CONSUMER.md` | `02183b2ff31ade3301b0b10c61718b2d22967976299a2ae7c9cdf1c190d5150e` |
| `POSITIVE_PRIMITIVE_ANGULAR_M2.md` | `5c3fe727d5a50de4edb4f94692c0de89343b34289d54d5de887d4f8dabd9a7df` |
| `README.md` | `7eabf1381d2c39b1da3e9b6ef04a29d39fd30eb1f7223eab4979f13a4a5405f9` |
| `SIGNED_SQUARE_CLASS_DIAGONAL.md` | `db1b90ed48a0d9ac8ff79226d3f3c3c51a40e8ab127b2e5daae4f34670e59ce2` |
| `check_positive_angular.py` | `501200693672ba15a14f37eaf2fb9d8847b3682e62afffb6bbf428b4088c8ee2` |
| `check_quartic_orientation.py` | `d448b6e9509d6989eaa1d96c3ae8c76e7a85dfcbd599d78324d1eb77208ed4a9` |
| `check_signed_reflection_local.py` | `80c42f6d22b2bdb21f09e4a89794b0cb8a067949157d58f751e036642f0e5723` |
| `positive_angular_check_report.json` | `0a9a9823b4944d7144249e326f2a23cdb8df48dcdd86c24dd9477936b9e8569b` |
| `quartic_orientation_check_report.json` | `9bbd558d66cd4ea5275fab663f1bed912b755f35eec585c1e34cccbcb6de3270` |
| `signed_reflection_check_report.json` | `6a709acdb4b66c2d1c1d1adeb1638aca2c322f6adc08b7d1f742c2980f531ee8` |


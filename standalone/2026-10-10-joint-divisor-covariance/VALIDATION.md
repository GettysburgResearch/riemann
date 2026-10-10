# Frozen source, independent reconstruction, and finite diagnostics

**Status:** proposed standalone research. The four written proofs have
scoped independent AI-agent reconstructions bound to the exact published
source below. The joint-divisor and theta/A2 deductions retain their
imported analytic assumptions. The new conductor sectors use the
published Hecke estimates stated in their proof, without assuming the
imported native Möbius moment or a zero-free hypothesis. None of these
results establishes the full fourth moment, the generalized hierarchy,
or a new zero-free half-plane.

## 1. Published source identity

The frozen mathematical source is
[5ad900ff27d34f1a8f94d28e19c47a3b37de6e39](https://github.com/GettysburgResearch/riemann/commit/5ad900ff27d34f1a8f94d28e19c47a3b37de6e39).

| Item | Identity |
|---|---|
| Source tree | 2a6e93c5cef50ecba6f5e4b4c490f8353906e3c0 |
| Sole parent, PR #922 final head | f71a9bc6ac3ce59a3c19d7e842a3fa082ecfbe32 |
| Branch | research/sextic-joint-divisor-covariance-20261010 |
| Stacked base branch | research/sextic-signed-covariance-20261010 |
| Source change | 16 files, 5,666 inserted lines |

The remote tree was checked against the complete staged tree before
publication. The published branch was fetched, the exact SHA, tree, and
parent verified, and the local branch adopted that same commit with a
clean worktree. Each independent reviewer subsequently read committed
blobs from this source. No similarly named local commit substitutes for
the published source.

[MANIFEST.json](MANIFEST.json) records the Git blob, SHA-256 and byte
length of every changed source file. These are four proof notes, seven
content/scope review notes, two README files, the source lock, the exact
checker, and its report. This validation note, the manifest, and the four
frozen-source receipts are subsequent documentation-only additions. They
do not change any mathematical source, archived review, or diagnostic.

The source changes only this new packet and a discovery paragraph in the
root README. The latter was checked against the parent to verify that
deleting the new section recovers its exact old content.

## 2. Which result uses which input

[SOURCE_LOCK.json](SOURCE_LOCK.json) binds 20 repository-file
dependencies by exact commit, blob, SHA-256 and byte count. It also
records the external primary references and the interfaces used.

| New deduction | Analytic assumptions retained |
|---|---|
| Joint block and large-divisor tail | Imported completed theta mean, primary Gauss CRT normalization, and squarefree sextic large sieve |
| Moving q/f adapter and full cube inversion | Complete three-cusp theta reflection, local scalar formulas, quadratic/cubic sieves, and the stated uniform angular scalar estimate |
| Optimized full A2 transfer | The mixed completed input above at \(\beta=11/12\), the exact finite A2 correction, and the refined all-row sextic sieve |
| New residual-conductor sectors | Wu's published Hecke subconvexity theorem with Blomer–Brumley's \(7/64\); for the additional divisor-sensitive branch, Söhne's theorem in the exact form quoted by Wu |

The primary theta source is the October 5 manuscript in OpenAI/math at
adc7f1241b42e322a6451854ab7e4b4c146bf78a, physically retained in the
October 7 import. Its SHA-256 is
d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d.
The upstream source commit and the riemann commit containing the import
are separate fields in the source lock.

The authors and reviewers reconstructed how those interfaces are used;
they did not reprove theta automorphy, all imported sieves, or the
completed mean square. The all-cusp coefficient comparison uses explicit
Dunn–Radziwill formulas, without invoking that paper's GRH-conditional
dispersion or prime-sum conclusions.

Wu's primary v6 theorem and the published Blomer–Brumley theorem were
opened and compared with the required hypotheses. Söhne's original
publisher page was inaccessible in this session; the proof explicitly
accepts the displayed statement quoted in Wu's introduction. The original
1997 proof was not replayed. The note makes no claim that these bounds
are the strongest currently available estimates.

PR #921 and PR #923 were read at their pinned sibling commits, not at an
implicitly changing tip. PR #923's raw short-row exponent is credited as
prior work; the new theorem transfers it to the full arithmetic A2
completion with the mixed labels. PR #914 is credited for the earlier
finite A2 coefficient identification. No global A2 functional equation
for the moving angular family is inferred.

## 3. Independent mathematical reconstruction

All reviewers here are AI agents. Independence means a separate
reconstruction with authorship and dependency relationships disclosed.
It is not external human acceptance or formal verification.

| Proof | Author | Independent reconstruction |
|---|---|---|
| [Joint divisor mean](JOINT_DIVISOR_MEAN.md) | joint_divisor_attack | signed_conductor_attack and root: exact reciprocal, row expansion, product recombination, masks, both block branches, Mellin crossovers, tail comparison and finite A2 algebra |
| [Moving auxiliary adapter](MOVING_AUXILIARY_ADAPTER.md) | moving_auxiliary_attack | joint_divisor_attack and root: local masks and phases, all physical row valuations, all-cusp accounting, scalar uniformity, full cube inverse, A2 weights and reconstructed diagonal |
| [Optimized A2 transfer](OPTIMIZED_A2_TRANSFER.md) | root | moving_auxiliary_attack: exact short/long inverse, arbitrary rectangles and subunit cutoffs, every correction norm weight, cutoff interval and explicit optimization |
| [Signed conductor progress](SIGNED_CONDUCTOR_PROGRESS.md) | signed_conductor_attack | moving_auxiliary_attack and root: primitive conductor, unit projection, Mellin adapter, published inputs, all-order incidence count, both feasible examples and signed residual replacement |

Detailed reports:

- [Joint divisor review](JOINT_DIVISOR_INDEPENDENT_REVIEW.md).
- [Moving auxiliary review](MOVING_AUXILIARY_INDEPENDENT_REVIEW.md).
- [Optimized transfer review](OPTIMIZED_A2_TRANSFER_REVIEW.md).
- [Signed conductor review](SIGNED_CONDUCTOR_INDEPENDENT_REVIEW.md).
- [Root reconstruction](ROOT_INDEPENDENT_REVIEW.md).
- [Navigation scope review](NAVIGATION_SCOPE_REVIEW.md).
- [Checker review](CHECKER_INDEPENDENT_REVIEW.md).

The optimized-transfer reviewer authored its mixed-family dependency;
that dependency has the separate joint-divisor and root reviews. Root
does not independently approve its own optimized proof or its checker.
The joint-divisor review's Section 7 conclusion is limited to finite
coefficient algebra. The signed reviewer opened both primary
Chinta–Gunnells papers; no global analytic adapter is certified.

Review caught and corrected a stray comma, a local-polynomial citation,
and an overbroad statement about failure of the conductor bounds when H
is arbitrarily large. The latter is now restricted to the intended
near-critical range \(H=D^{1+\vartheta}\),
\(0<\vartheta\le1/10\). Navigation review also required explicit fixed-test
quantifiers, the nonprincipal condition \(f\ne1\), the radial row test,
and the precise fixed-test/\(e\ge0\) condition for the remaining averaged
target. All repairs preceded the frozen source and received review at
their repaired content identities.

The receipts binding these scopes to the published commit are:

- [Moving input and checker receipt](FROZEN_MOVING_CHECKER_RECEIPT.md).
- [Optimized transfer and conductor receipt](FROZEN_TRANSFER_CONDUCTOR_RECEIPT.md).
- [Joint divisor and navigation receipt](FROZEN_JOINT_NAVIGATION_RECEIPT.md).
- [Root receipt](FROZEN_ROOT_RECEIPT.md).

All compared content identities match. A later proof change requires a
new identity and review of the affected scope. A newer branch tip,
manifest, or validation label cannot automatically strengthen a theorem.

## 4. Exact finite diagnostics

The checker is
[check_covariance_arithmetic.py](checks/check_covariance_arithmetic.py),
SHA-256
0e6b41e2465a11eda7b23bbb405b163fec453b59ff76cb115765a7506859d16c.
The [saved report](results/exact_covariance_checks.json) has SHA-256
6e998509315385702f789341c86de5b9c93a561f304e3e926baba2fb7a3b23d4.

The author and an independent agent both ran isolated normal Python and
optimized Python. All runs exited successfully. Independently regenerated
reports were byte-identical to the saved report. Root also reproduced
both modes, and the committed report was compared with those reproduced
bytes.

The report records 22,743 successful predicates, including nine negative
controls. Selected coverage is:

| Coverage | Exact predicates |
|---|---:|
| Mixed q/f row identity on the full independent zero/sixth-root value set | 16,464 |
| Unit projection | 6 |
| Formal cube-reciprocal polynomial identity | 1 |
| Rational fixtures for that identity | 18 |
| A2 norm-weight rows and strict denominator tests | 20 |
| Optimization interval dominance | 20 |
| Joint-tail substitutions and threshold comparisons | 56 |
| Singleton/double/higher incidence checks for k=1 through 6 | 5,454 |
| Actual conductor divisors and their greedy inequalities | 650 |

The code derives the correction exponents from the child scale laws and
uses exact fractions to check the two optimization intervals and both
signed-conductor examples. It also checks the finite A2 insertion
pairings and negative controls for omitted zero masks, incorrect signs,
nonstrict parameter endpoints, and confusing conductor with complexity.
The complete group counts and exact example values are in the report.

Arithmetic is integer, rational, formal-polynomial and exact
\(\mathbb Z[\omega]\) arithmetic. There is no floating-point rounding
contract. Explicit exceptions enforce the predicates under optimization;
no assertion is used as the acceptance gate. The program reconstructs
its output and does not read the saved JSON as evidence.

The zero/sixth-root enumeration is an exact local character-value
diagnostic, not a primitive Gauss-sum or global theta replay. Finite
incidence enumeration only covers the stated orders; the general-k
claim is proved by the written count. The 22,743 predicates are not
22,743 independent theorems. They do not establish an infinite analytic
bound, a Hecke subconvexity theorem, a full arithmetic moment, or RH.

## 5. Smallest remaining mathematical gaps

The large-divisor theorem improves its specified tail but leaves the
small-divisor terms and the condition \(2\Re t+\Re u>3\) in the full
positive majorant. The A2 theorem proves a positive norm bound at short
row lengths; it does not control the centered strict off-diagonal at the
critical long dual scale.

The conductor argument removes additional actual Hermitian sectors at
every fixed order. Its complement still contains widely separated
singleton configurations. The specific fourth-moment target is the
signed averaged estimate for \(V_h(D)\) in
[equation (6.4)](SIGNED_CONDUCTOR_PROGRESS.md#6-consequence-for-the-literal-signed-remainder).
That estimate, or a stronger theorem implying it, remains unproved.
Replacing it by a positive norm or an individual-character bound loses
the cancellation that is still required.

The packet therefore records completed component deductions and a
smaller exact remainder. It does not claim the full generalized moment,
\(17/24\), a new zero-free half-plane, or RH. No merge into main or
promotion to the integrated record is part of this publication.

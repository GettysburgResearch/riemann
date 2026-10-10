# Validation and review scope

Date: 2026-10-10 UTC. Status: proposed standalone research. The proofs
are deductions under the premises stated in each manuscript. No full
fourth moment, cofinal moment hierarchy, new zeta boundary, or RH claim
was established by these checks.

## 1. Exact source integrity

`SOURCE_LOCK.json` records 23 original commit:path bindings, each with
its Git blob, byte size and SHA-256. Six adjacent #925/#926 sources are
copied verbatim in `sources/`; the other sources remain at their
already retained repository paths. Each source was read at its pinned
commit and checked against the retained or copied bytes.

The OpenAI/math October 5 manuscript is retained under its existing
import path. Its imported source declaration is commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`, and its SHA-256 is
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
The lock verifies the exact copy in this repository; it does not
reconstruct the external theta theory or certify the external project.

`checks/verify_packet.py` verifies the complete packet inventory, every
listed byte hash, every source Git blob and original commit:path
resolution, and each exact manuscript/review binding. It rejects
missing, extra or changed packet files and unsafe manifest paths. Its
scope is integrity, not mathematical truth.

## 2. Frozen main manuscripts

| Manuscript | SHA-256 |
| --- | --- |
| `ARBITRARY_GRAPH_SECTORS.md` | `ef3704340d3af629a6bbd97d575d35bb5570474e8973a99c600c76bf096c9f13` |
| `DENSE_CROSS_GCD_SECTORS.md` | `90af83fcd69cc95d2d56884e367f1a227828ca32c2cb03315ba5cf1d551f3d43` |
| `JOINT_GAUSS_REUNION_CONTINUATION.md` | `31e2395999301d56ce63751db7c907fc6147b689574aaf268133d706ad3aa0aa` |
| `CENTERED_COVARIANCE_AND_CUBE_ALIASES.md` | `d121c94e9eaf8142d160ece29194d186cf2b915dfc53273d351e2baeec7becde` |
| `PRINCIPAL_SHORT_LONG_COVARIANCE.md` | `7de2f4fbf8b085bc37cc83d0767748eee1c8478a590b3551935870b616f9166e` |

These hashes are the review targets. No earlier proof packet was
changed to satisfy a review or diagnostic.

## 3. Independent analytic and scope reviews

| Report | Reviewer and checked scope |
| --- | --- |
| [ROOT_GRAPH_AND_DENSE_REVIEW.md](reviews/ROOT_GRAPH_AND_DENSE_REVIEW.md) | Root independently reviewed signed_sector's shared-incidence theorem, critical finite Euler correction, signed graph unions, forest and cycle charges, endpoint and conductor-restriction accounting. Root's own dense continuation is explicitly excluded from the independent part of this report. |
| [DENSE_CROSS_GCD_REVIEW.md](reviews/DENSE_CROSS_GCD_REVIEW.md) | signed_sector independently reviewed root's dense cross-graph charges, every induced-subset case, parameter domain, exact cutoff and no-common-gcd example. |
| [JOINT_GAUSS_REUNION_REVIEW.md](reviews/JOINT_GAUSS_REUNION_REVIEW.md) | moving_labels independently reviewed descent_synthesis's two distinct finite-ray orientations, six cutoff exponents, normal convergence, exact correction and inner character placement, every cusp and bad cube, gamma factor, and same-completed-family comparison. The reviewer discloses prior authorship of part of the #924 input. |
| [CENTERED_COVARIANCE_AND_CUBE_ALIASES_REVIEW.md](reviews/CENTERED_COVARIANCE_AND_CUBE_ALIASES_REVIEW.md) | descent_synthesis independently reviewed moving_labels' principal and smooth Poisson kernels, exact inverse and masks, principal and physical-diagonal tail bounds, both original inverse coefficients, coupled scale, strict selector and polynomial coefficient budget. |
| [CENTERED_COVARIANCE_SECOND_REVIEW.md](reviews/CENTERED_COVARIANCE_SECOND_REVIEW.md) | signed_sector performed a second independent covariance review, including a counterexample search, the original first-Poisson normalization, literal row phases, finite counting ceiling and the restrictions of the rapid-decay theorem. |
| [PRINCIPAL_SHORT_LONG_REVIEW.md](reviews/PRINCIPAL_SHORT_LONG_REVIEW.md) | signed_sector independently reviewed the exact support separation, sharpened the cutoff to the sixth root of the physical support ratio, checked the four centered block signs and the original signed normalization, and required physical-test support and the bounded two-variable profile extension to be stated explicitly. |
| [PACKET_SUMMARY_SCOPE_REVIEW.md](reviews/PACKET_SUMMARY_SCOPE_REVIEW.md) | descent_synthesis checked the final README and validation statements against the five notes, their exact hypotheses, source pins, report counts and claimed remaining gap. |

All are AI-agent reviews of the displayed new deductions. They are not
human peer review or proof-assistant certification. The graph proofs
retain `NM2` and `PW_b` as stated premises. The continuation imports
the pinned theta, sieve and coefficient identities. The reviews do not
claim independent reconstruction of those foundations.

One substantive scope issue found during the covariance review was
fixed before freezing: arbitrary bounded row multipliers allowed for
the principal-norm contraction cannot be carried into the strict
Poisson-decay theorem. They can create a principal character from a
strict pair. The final proof explicitly restricts that theorem to the
actual reconstructed A2 phases and gives the counterexample.

The packet summary was also checked to distinguish principal
correlation from equality of literal zero-extended row characters.
Different prime masks remain different even when all unit phases
coincide.

## 4. Finite exact diagnostics

The root agent independently reran each diagnostic to a separate
output path. All reports were byte-identical to the producers'
reports. Both covariance reviewers additionally reproduced its report.

| Diagnostic | Executed finite scope | Frozen report SHA-256 |
| --- | --- | --- |
| `check_graph_charges.py` | 964,909 declared predicates: integer and rational incidence reconstruction; zero-extended sixth-root phases; complete signed covariances; all 16 labeled cross graphs on four positions and all 512 on six positions; forest and cycle constraints; dense symmetry classes through `k=24`; negative controls. | `54e7e19ed2aa739a9877b9340a3bfb39ab70c3533fa8fcef8d866fa4387fd569` |
| `check_joint_gauss_continuation.py` | Ten exact source bindings, all six cutoff monomial substitutions, affine exponent identities, 14,241 rational domain points, 882 cusp-table entries and 300 prime-valuation support cases. The report records the full frequency, cusp, row and test scope. | `efa333e808bec4e145b9715cd26abf4e49949c8198c560c6a628e43ea3872ceb` |
| `check_principal_aliases.py` | 9,392 finite identities: 784 local residue correlations, 4,096 cube alias classifications, 2,304 masked inverse cases, 160 cube-zero cases, 1,792 lcm cutoffs and 256 A2/radical cases. Includes genuine small residue-field phase tables and explicit alias and centering witnesses. | `9c70640d8a8e15cc05394a212388b15c396e162e17e6003489c1bedc85cce744` |
| `check_short_long_principal_blocks.py` | 270 divisor/support cases; a nonempty squarefree raw column and two unequal cube products in one physical annulus; exact rational four-block signs; and a witness for the sixth-root endpoint and failure below it. | `191fc950937f84b33af16dce1e26e67ccb09ebe911cae3a7feb22ba31b26ce94` |

The graph report's much larger number of labeled subsets represented
by dense symmetry classes is a coverage annotation. It is not the
number of individually executed checks. Its formal phase model is not
an enumeration of global Hecke characters.

The graph and joint Gauss diagnostics use explicit exception gates.
Python optimization does not disable those gates. The alias and
short/long diagnostics use assertions and explicitly refuse `python -O`.
The root checked that these guards exit unsuccessfully before writing a
report. That
expected rejection is not a failed arithmetic assertion.

These diagnostics establish the finite identities they actually
evaluate. They do not establish infinite normal convergence, Poisson
summation, `NM2`, `PW_b`, a uniform infinite energy estimate, an
imported theta theorem, or a statement about Riemann zeros. Those
analytic claims are assessed from the written arguments and their
explicit premises.

## 5. Reproduction from the repository root

The repository must contain the original commits named in
`SOURCE_LOCK.json`, including the adjacent #925 and #926 commits. A
checkout with only the stacked ancestors may need those exact objects
fetched first. The source verifier fails explicitly if they are absent.

Use an output directory outside the packet so a rerun does not alter
the frozen inventory:

```bash
packet=standalone/2026-10-10-signed-graph-and-joint-descent
check_out="$(mktemp -d)"
python "$packet/checks/check_graph_charges.py" --output "$check_out/graph.json"
python "$packet/checks/check_joint_gauss_continuation.py" --repo . --output "$check_out/joint_gauss.json"
python "$packet/checks/check_principal_aliases.py" --manuscript "$packet/CENTERED_COVARIANCE_AND_CUBE_ALIASES.md" --expected-manuscript-sha256 d121c94e9eaf8142d160ece29194d186cf2b915dfc53273d351e2baeec7becde --output "$check_out/aliases.json"
python "$packet/checks/check_short_long_principal_blocks.py" --manuscript "$packet/PRINCIPAL_SHORT_LONG_COVARIANCE.md" --expected-manuscript-sha256 7de2f4fbf8b085bc37cc83d0767748eee1c8478a590b3551935870b616f9166e --output "$check_out/short_long.json"
python "$packet/checks/verify_packet.py"
```

## 6. Scope that remains open

The larger tube for the exact reunited `Y_k(s,v)` has row energy
`H^(10/7+epsilon)`. It does not inherit the stronger `H^(1+epsilon)`
mean throughout that larger region. Its hypothetical scalar physical
envelope is already dominated by existing bounds for the same complete
family, as explicitly derived in the manuscript.

The principal cube-tail estimate controls the complete-residue,
zero-frequency projection. It does not replace the full finite-height
tail's `H` term by `H/R`. Its short/long corollary retains the actual
physical test supports, both sixth-root ratio thresholds and squarefree
raw columns. Arbitrary additional row characters and independently
shifted A2 columns require a new alias calculation. The four principal
off-product blocks cancel exactly and do not estimate the remaining
nonzero frequencies. Strict covariance pruning uses the complete
smooth radial row sum, a fixed positive scale margin and a polynomial
coefficient budget. It leaves the small-auxiliary, small-radical-defect,
small-common-gcd region, including the all-unit coprime core.

The graph theorem controls specified whole signed sectors under fixed
order hypotheses. In the far-separated singleton sector the current
excess remains linear in `k`. The original signed off-product-diagonal
comparison, its adverse initial dual height, a full fourth moment,
`17/24`, a cofinal hierarchy and a further zero-free improvement all
remain unproved.

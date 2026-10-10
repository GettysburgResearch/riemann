# Mathematical review and finite reproducibility

**Status: source-qualified component proofs with internal mathematical
reviews and exact finite diagnostics.** These records do not establish
the full fourth moment, the generalized moment hierarchy, a new zeta
zero-free boundary, or RH.

## 1. What was reviewed

The proof authors and reviewers reconstructed the actual coefficient
identities, mask conventions, physical row heights, norm normalizations,
cutoff support, and divisor exponents. Each scoped review identifies
the exact SHA-256 of its target. A review of a source-qualified deduction
does not remove that deduction's explicitly named analytic premises.

| Proof | Reviewed SHA-256 | Independent review |
|---|---|---|
| MOVING_COLUMN_MASKS.md | 068c7c993bdf09e17c2c06182ca8bc631e6ed34d8df6ccf29c46e1f2333ae0ee | moving_masks_a2_review.md |
| A2_MOVING_MEAN_SQUARE.md | 6eed5695c672dab92620763f8df5b63f60dc416754367ed541cb854bf06854ba | moving_masks_a2_review.md; supporting independent derivation |
| SIGNED_AUXILIARY_REUNION.md | 6b8277e64adb1121704fbf7dc4553aeda31b598c65e0279d80316a35d66d38bf | signed_auxiliary_review.md; root_review.md |
| HIGHER_CUBIC_POOLS.md | 622cf846a961aed28ac0363f91766045f328c99700931621f123c17347c6bc23 | cubic_pools_review.md; root_review.md |
| HYBRID_CUBE_INVERSE.md | d4c5dad1b5c719043ac7118c5f468b3d5c398e2bbd5c4470a1983f64139f066a | root_review.md; moving-mask composition audit |
| ALL_ROW_SPECTRAL_MEAN.md | 204e448b92e4a0d4087e0ccf8e99cb20fcfef26114a95622af2c47c965cdb651 | root_review.md |
| MIXED_CUBIC_REPLICATION.md | fb32d3a63704950be1d30228ec03a0ee1f157f23d1c7b24a8793886160fbb30b | mixed_replication_review.md; root_review.md |
| SMALL_W_CORE_AUDIT.md | c0d07ccc7ed2fc1490a631c73db47044df256b7ca6f946ecacd5c735e457f9d9 | small_w_review.md; root_review.md |
| STRATIFIED_TWO_SCALAR_A2.md | 9b540fe779b6e0f3c64baba04deed6ee380f1d9746035afc3cf9c7fdb0cf3ad5 | stratified_a2_review.md; stratified_a2_second_review.md |
| SMALL_W_POSITIVE_CUTOFFS.md | 52a4d27a5f518feabfb8ecb6c87eee5172a6ce3f2cf6a5aa5630c00ff9346461 | stratified_a2_second_review.md; root_review.md |

The review files are in [reviews](reviews). The root authored the moving
mask, original A2 and stratified two-scalar A2 proofs; the root's own
checks of those proofs are not counted as independent review.
The stratified proof has two separate manuscript reviewers. They also
contributed cutoff calculations during its development; their reports
disclose that overlap. They recomputed and audited the final argument,
but are not described as independent of every underlying contribution.

Several details were made explicit before the final hashes were frozen:
the beta-one equality of the two smooth signed-block alternatives;
the original moving mask in the spectral mean; smooth two-variable tests;
the unequal shifted scales in mixed replication; either prescribed
outer/inner orientation in the new raw bound; the exactly empty short
part below unit cutoff; and the doubled physical cap needed with the
dilated smooth cutoff. No reviewer-approved formula is silently changed
after its hash is recorded.

The reviews are internal agent audits, not external peer review or formal
proof certificates. The named upstream canonical/theta proof was not
reconstructed in its entirety or formally built during this pass.

## 2. Exact finite diagnostics

All six executable programs use Python's standard library. Their checks
use explicit exceptions or conditionals that remain active under optimized
Python. Each final report was reproduced under ordinary Python and
Python with optimization enabled; their output bytes agree.

| Program | Finite scope | Selected evidence |
|---|---|---|
| check_signed_reunion.py | Formal cyclotomic CRT identities, complete divisor reunion, strict conditions and rational kernel factors | 15,876 reunion cases; 24,624 strict reconstructions; 40,176 kernel cases; 44,928 formal Gauss scalar cases |
| check_cubic_pools.py | Exact mixed correction and finite triangle energies with genuine small Eisenstein residue symbols | 114,266 predicates; 10,206 mixed coefficients; 51,450 triangle tuple/row coefficient cases |
| check_moving_masks.py | Actual split-prime nonunit masks, original/auxiliary overlaps, cube masks and local rational exponents | 210 element rows, including 60 with nonunit symbols; 107,520 literal mask cases; 343 A2 allocation configurations |
| check_hybrid_algebra.py | Finite smooth-regrouping identity and rational unstratified exponent balances | 11,664 regrouping cases; 468 auxiliary-vertex inequalities; 48 energy-endpoint comparisons |
| check_mixed_replication.py | Literal degree-five replication, unequal-scale weights, mixed Euler coefficients and Hölder with zeros | All 27 norm monomials and 81 pair weights; 1,458 local coefficients; 3 finite Hölder data sets |
| check_stratified_a2.py | Sixth-power decomposition, positive cutoff support and exact rational stratum/A2/optimization exponents | Detailed counts and witnesses in results/stratified_a2.json |

The reports are in [results](results), and their byte hashes and replay
status appear in [results/reproduction_receipt.json](results/reproduction_receipt.json).
[PROVENANCE.json](PROVENANCE.json) hashes every final packet file except
itself, including all producers, reports and review records.

The phrase actual Eisenstein residue symbols has a limited concrete
meaning here. The relevant programs use the genuine split-prime quotient
fields of norms 7, 13 and 19, check the specified Eisenstein generators,
and compute sextic residues on their finite element row sets. Units and
nonunit zeros are present. This is a test of those finite coefficient
identities, not an evaluation of the infinite arithmetic family.

By contrast, the signed-reunion program uses exact formal Gauss data that
satisfy the explicitly declared CRT and finite-ray interfaces. Its Gauss
values are not numerical evaluations of primitive Eisenstein Gauss sums.
The mathematical proof separately cites and uses the actual Gauss CRT
normalization. The distinction is explicit in both its producer and report.

The smooth-regrouping diagnostic uses exact finite cutoff values. It
checks the divisor reindexing and zero masks, not the analytic differentiability
or Mellin decay of a cutoff. Those properties are proved in the text by
the fixed smooth choice and uniform rescaling.

The rational tests evaluate exact fractions and finite affine comparisons.
The written proofs establish the continuous beta ranges and convergent
ideal sums. A finite beta grid is never substituted for those arguments.

### Negative controls

The finite programs deliberately reject the following incorrect operations:

* replacing a signed Möbius divisor sum by its absolute version;
* deleting a common-row nonunit zero or imposing the false condition
  that the reunited new row be coprime to its auxiliary;
* using a fourth power where the reunited phase requires a fifth power;
* conjugating the wrong finite-ray factor;
* changing the positive pair coefficient from mu-squared to mu;
* interpreting a deleted prime's sixth power as one on nonunits;
* treating overlapping original and auxiliary exclusions as disjoint;
* adding an unproved inner-column coprimality mask in the long inverse;
* discarding repeated-prime zeros during the physical inverse regrouping;
* using replication matrices whose column sums fail the required identity.

The stratified report additionally checks its stated cutoff and independent
coordinatewise-summation negative controls. In particular, failure of a
coordinatewise bound at the old cube-root cutoff does not rule out an
ordered or otherwise coupled correction summation.

## 3. Reproduce the stored reports

From this packet directory, run the following standard-library driver.
It compares fresh ordinary and optimized outputs against the committed
report bytes, without rewriting those reports.

~~~python
from pathlib import Path
import subprocess
import sys

cases = [
    ("check_signed_reunion.py", "signed_reunion.json"),
    ("check_cubic_pools.py", "cubic_pools.json"),
    ("check_moving_masks.py", "moving_masks.json"),
    ("check_hybrid_algebra.py", "hybrid_algebra.json"),
    ("check_mixed_replication.py", "mixed_replication.json"),
    ("check_stratified_a2.py", "stratified_a2.json"),
]
for script_name, report_name in cases:
    script = Path("checks") / script_name
    extra = (
        ["--proof", "STRATIFIED_TWO_SCALAR_A2.md"]
        if script_name == "check_stratified_a2.py" else []
    )
    ordinary = subprocess.check_output([sys.executable, str(script), *extra])
    optimized = subprocess.check_output([sys.executable, "-O", str(script), *extra])
    expected = (Path("results") / report_name).read_bytes()
    if ordinary != optimized or ordinary != expected:
        raise RuntimeError(f"Report mismatch: {script_name}")
    print(f"PASS {script_name}")
~~~

No network access, floating-point optimizer or third-party algebra package
is required by these finite programs. A successful replay establishes
only the explicitly described finite diagnostic assertions.

## 4. What the evidence does not certify

The following analytic inputs are retained rather than proved by these
tests: the theta reflection and coefficient mean square; the named
quadratic/cubic upper large sieves; the source's native second moment
with moving exclusions; the optional finite-order pointwise exponent;
and the separate angular scalar reciprocal premise. Each proof states
which subset it uses.

In particular, beta-f equals 7/8 and beta-a equals 11/12 are different
source-qualified inputs. Counting versions set the relevant exponent
equal to one. The higher pair-pool theorem at counting and without a
native-second-moment interpolation uses the named classical sieve and
elementary counting, not a higher inverse moment hypothesis.

The newer de Faveri theorem is credited only in the discussion of the
adjacent 4/7 spectral threshold. The stratified two-scalar 89/55 theorem
uses the pinned classical sixth-power-free row argument; it does not
import that newer operator to obtain its gain.

The old unstratified hybrid and full-A2 proofs remain valid records, but
their best displayed square-root-height exponents are superseded by
STRATIFIED_TWO_SCALAR_A2.md. The old small-w obstruction is tied to its
displayed R,T at least one envelope. SMALL_W_POSITIVE_CUTOFFS.md expressly
handles all positive R and the possibility of exact empty-stratum pruning.
Neither audit states a lower bound on the arithmetic energy or excludes
new cancellation in the signed covariance.

There was no repository-wide Lean claim, no formal proof build, no
external peer-review assertion, and no promotion of these proposed
components to the repository's integrated mathematical status.

### Repository whitespace check

The unfiltered staged diff reports only a final blank line in three
byte-for-byte frozen manuscripts: MIXED_CUBIC_REPLICATION.md,
reviews/signed_auxiliary_review.md and reviews/small_w_review.md.
Those bytes are preserved so their recorded review/source hashes remain
exact. The scoped diff check excluding those three copied files passes.
There are no other reported whitespace errors. This is an explicitly
documented formatting exception, not an analytic or diagnostic failure.

## 5. The unresolved theorem

The sharp signed auxiliary tail is proved for every fixed moment order
under its stated scalar premise. The complete A2 positive energy and
mixed-replication higher-overlap sectors are stronger. The all-singleton
balanced native core still requires the saving
\[
D^{(k-1)(2\beta_{\rm f}-1)}
\]
beyond the presently supplied two-native-axis estimate. That loss is
linear in k at fixed beta-f greater than one half. None of the finite
diagnostics, positive-energy gains or exact divisor identities turns it
into an excess that is sublinear in k. The generalized diagonal moment
and its source-dependent route toward RH therefore remain open.

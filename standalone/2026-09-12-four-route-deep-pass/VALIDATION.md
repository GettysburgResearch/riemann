# Validation, provenance and scope

This packet records a research assessment and proposed new components. Its
finite calculations do not certify RH. Start with [REPORT.md](REPORT.md).

## Source state

Main was `f99d9e3908dde4865377c75d9ca051c1f545bf4f`. The final remote check
still found #875 at `be149104721ae7b65b624c100118edfd7b76b69b`, #874 at
`80844a3778390ff744235cf2b021cfaea80ff512`, and #873 at
`4d25182333f5900ebfbc97f36f823d256a2ee340`. The public frozen-source index is
`SOURCE_LOCK.json`; each route note cites the precise manuscripts used.
The assessment cutoff is 12 September, not the later publication time.

#866's current head is `cb05d3052611bd1804459887e84fdec3cb7064af`; its
mathematical proof has the same Git blob
`c68170e2dacd23c188c9e71482e51fe63566b587` as the prior head. Its added
checker and reproduction changes were not counted as a mathematical advance.

Four #875 arithmetic/source modules were copied byte-for-byte into
`ising-computation/predecessor/`. Their pinned paths and SHA-256 values are
in `ising-computation/predecessor-provenance.json`. The new calculation uses
those source routines but no prior numerical target receipt. The height
calculation now authenticates a vendored exact copy of its #860 source before
execution. These complete primitive copies allow reproduction without fetching
historical Git objects.

The original assessment was performed outside the repository. Publication on
13 September adds only this separately labeled packet to the existing PR #869;
the previous three-route packet and other contributors' work are unchanged.

## Executed mathematical controls

| Calculation | Fresh execution and outcome | Scope |
|---|---|---|
| Ising seed, complete source mesh 128 | `python -B certify_dimer.py`; passed | Full theta and harmonic-tail reconstruction, 50 exact inverse identities, strict whole-box contraction and positivity |
| Ising seed, complete source mesh 160 | `python -B certify_dimer.py --mesh 160 --output dimer-certificate-mesh160.json`; passed | Same exact box at a second mesh of the same outward-arithmetic implementation |
| Ising algebra | `python -B test_algebra.py`; four tests passed | Four-configuration dimer cumulants, dual-number Jacobian, unequal-edge derivatives and reverse inverse identity |
| Arithmetic | `arithmetic-counterfamily.py`; output in the adjacent JSON | Six exact native collar-identity controls; four nonnative source panels. The latter norm calculations are ordinary binary64 diagnostics, not interval certificates |
| Gamma | Producer, normal and optimized runs of `gamma-controls.py`; passed | 21 exact shape/scale panels, sharp Peano mass bound, triangular moment identities and four score-energy panels |
| Height | `height-cutoffs.py`; output in the adjacent JSON | Exact original and alternative sufficient thresholds at depths 0–8, retaining the complete remainder constants |

Python 3.12.10 was used. The accepting Ising calculation uses standard-library
rationals and 512-bit outward dyadic arithmetic. Its exploratory scout also
uses mpmath but has no accepting role. Detailed reproduction commands are in
[the Ising guide](ising-computation/README.md) and the route notes.

The first Ising certificate attempt stopped at an exact inverse check after
detecting floating-point coercion in an integer Jacobian row. Converting the
row to exact rationals corrected it; both complete accepting runs occurred
after that correction. This detected failure is retained in the documentation.

## Analytic review

The root agent reviewed the new arithmetic collar identity and growing
counterfamily, gamma Peano comparison and fold countermodels, and Ising
proof/certificate dependencies. The arithmetic and gamma agents separately
cross-reviewed the root's uniform branching defect and threshold derivation.
The later unconditional `o(N)` trace refinement was also read and checked
against Tao's primary source. No defect was identified in those stated new
arguments during this review.

These reviews are within the same agent session. They do not establish
external acceptance, formal verification, or numerical independence. The two
Ising meshes share a backend. Normal and optimized Python controls likewise
share their arithmetic implementation.

The written infinite-tail proofs, source identities, and classical analytic
inputs remain mathematical dependencies. Earlier large native-zero contour
certificates, high-order Radau calculations, all remote CI jobs and all
historical experiments were not replayed. No new complete native gamma
zero-current integral or branching zero census is claimed.

## Packet integrity

`verify_packet.py` checks the two saved contraction inequalities and displayed
bounds using exact fractions, validates copied-source provenance, checks local
Markdown links and unwanted control characters, and writes `MANIFEST.json`
with SHA-256 hashes of the delivery files. It does not rerun the source
quadratures or validate a mathematical argument. Run it from this directory
with `python -B verify_packet.py`.

The manifest excludes itself and Python bytecode caches. The large historical
PR inventory is not published; SOURCE_LOCK.json records only the public frozen
source identities used in the assessment.

## Publication replay on 13 September

The packaged arithmetic checker reproduced all six exact panels and all four
ordinary synthetic panels; its JSON matched the original assessment both
structurally and byte-for-byte. The normal and optimized gamma controls passed
from the packaged directory.

The height consumer now authenticates the literal vendored #860 bytes before
execution. Both normal and optimized reconstructions passed; an additional
run outside the repository with Git subprocess access prohibited passed. A
changed-source test failed before executing replacement code. The height JSON
also matched the original assessment byte-for-byte.

The packaged mesh-128 Ising certificate passed with unchanged mathematical
bounds. Twelve bounded tests passed: four algebra, four provenance and four
strict acceptance tests. Mesh 160's original assessment receipt is retained;
it was not represented as a new publication replay.

The Ising consumer now pins all four source hashes independently of its JSON
receipt, authenticates every primitive before any executes, and compiles the
same verified bytes directly. It does not trust import caches or a resealed
receipt. Its publication replay and rejection checks are documented in the
Ising reproduction guide. Optional extraction/scout repository discovery is
portable; the accepting calculation needs no historical Git objects.

Packet Git attributes preserve literal file bytes, including receipt line
endings and copied primitives, so the manifest binds the staged content.

These changes improve reproducibility and source binding, without changing
the mathematical targets. Frozen predecessor source files and their original
license remain intact. The follow-up adds files under this standalone packet;
no integrated or formal source is changed. The repository's existing CI path
filters do not select either the formal build or integration audit for this
standalone-only addition. Those broad jobs were not run locally as a substitute
for the packet's relevant checks.

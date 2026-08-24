# Final acceptance addendum: repaired Reviewer C formalization

## Freeze

```text
repository:                 gfreund123/riemann
bootstrap base:             573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f
primary PR:                 #735
primary branch:             formal/030-xi-operator-qa
original reviewed head:     4863c31dd497ffe69ea400fe29275decf4cb5d29
repaired primary head:      b20ee9b3678e5d8fa32b04b156bc02cec782a97b
binding cross-review PR:    #749
cross-review branch:        formal/review/2026-08-24/b-cross-c
original cross-review head: 9da1e250b647575418290407c6e30054322bb581
build status:               BUILD_NOT_EXECUTED
RH proved:                  NO
```

This addendum reviews only the binding P0/P1 findings and the corresponding repair commit. It does not reopen the accepted finite Pick, LDL, PSD/PD, reciprocal-concavity, Hermite, Q4, or firewall algebra.

## Executive disposition

The repaired commit is a one-commit fast-forward from the originally reviewed head and changes only Reviewer C operator/comparator/registry/blueprint/report/QA surfaces. It does not modify workflows or Reviewer A/B mathematics.

The mathematical statement repairs are largely successful:

- the six arbitrary proposition labels are gone;
- the actual completed-Xi normalization, node function, zero-orbit conventions, analytic multiplicities, grouped value/first/second-derivative convergence, selected reserve, multiplicity residual, reciprocal-square tail, and paid-prefix convergence are concrete propositions or structures;
- repeated positive nodes are reduced to order two through exact duplicate-row congruences;
- the source-specific one-orbit defect, cross-curvature, reviewed epsilon, and `epsilon <= 9m/b^2` estimate are formal declarations rather than an assumed payment predicate;
- the finite-prefix reserve ledger has nonnegative shares and tails, every orbit paid, total use at most one, an exact one-use identity, and nonnegative leftover;
- canonical semantic IDs are mapped to source-specific declarations while generic lemmas are separated in `C_API.tsv`;
- the order-three Challenge and Solution share the exact `ChallengeStatement`, include repeated nodes, conclude PSD only, and contain no order-four or PD strengthening.

The full actual-Xi theorem remains correctly classified `PROVED_CONDITIONAL`. The grouped analytic expansion, finite-height theorem proof term, tail estimate, paid-prefix convergence, and source-specific scalar curvature bridges remain explicit hypotheses. This is an honest formal boundary, not a proof of those analytic inputs.

## Binding findings

### P0-1: arbitrary proposition labels and absent actual-Xi data

**RESOLVED.** `PublishedVerifiedHeightTheorem`, `GroupedActualXiC2Expansion`, `CriticalMultiplicityResidual`, `ActualXiReserveAllocation`, `RegroupedActualXiC2Approximation`, and `ActualXiOrderThreeInputs` state the mathematical content previously hidden behind names. The concrete `riemannXi`, `centeredXi`, and `actualXiNodeP` definitions fix the actual function and coordinate convention.

### P0-2: incomplete external theorem and source lock

**PARTIALLY_RESOLVED_WITH_EXCLUSION.** The exact height `3000175332800`, critical-line conclusion, DOI, arXiv identifier, journal citation, source-lock equality, and normalized theorem-record SHA-256 are present and independent of the local scientific claim-file SHA. The normalized record hash recomputes to `2eb547a373c49f56fa4da97284534bc06ee9a71548121a2b15d337cb79832c73`.

Residual exclusion: `artifact_sha256` is explicitly scoped to the normalized local citation/theorem record; it is not a digest of the external paper PDF, source archive, or computational artifact bytes. Reconciliation must preserve that narrower meaning and must not describe it as an independently fetched publication-file hash.

### P0-3: repeated-node PSD assumed wholesale

**RESOLVED.** Positive squared-node equality yields node equality; values are evaluations of the single function `actualXiNodeP`; the `12`, `13`, and `23` cases reduce by duplicate-row/column congruence to the actual-Xi order-two PSD theorem. The former `hrepeated : ... -> IsPSD3 ...` premise is absent.

### P0-4: canonical semantic-ID overmapping

**RESOLVED.** `C.tsv` now maps actual-Xi IDs to source-specific declarations and marks the analytic conclusions `PROVED_CONDITIONAL`. Generic determinant, divided-difference, reserve-prefix, and repeated-node APIs are split into `C_API.tsv`. The heat fixture remains `BLOCKED_MATHEMATICS` rather than being promoted to the full analytic no-go.

### P0-5: comparator covered only the ordered-distinct generic theorem

**RESOLVED.** `ChallengeDeps.XiPickOrderThreeConditional.ChallengeStatement` is the shared full positive-node packet statement. The Challenge has one permitted placeholder. The Solution has the identical theorem type and is the library theorem `RiemannFormal.Operator.actualXiPickOrderThreeConditional`. The statement records one-, two-, and three-node PSD, repeated nodes included, with no PD or order-four claim.

### P0-6: authoritative build and axiom evidence absent

**UNRESOLVED_BLOCKER.** Lean and Lake are unavailable in this acceptance environment, and GitHub exposes no workflow run or status for repaired head `b20ee9b3678e5d8fa32b04b156bc02cec782a97b`. Therefore the required exact-head suite is `BUILD_NOT_EXECUTED`. Source inspection and static fixtures do not substitute for kernel compilation, comparator elaboration, registry validation, or parsed `#print axioms` output.

### P1-1: source-specific one-orbit theorem missing

**RESOLVED.** `XiSourceSpecific.lean` derives the geometric gap and kappa bounds, proves the exact transformed cross-curvature and defect formulas, uses `epsilon = 2m*kappa/(1-kappa)`, proves the payment inequality, and derives `epsilon <= 9m/b^2` from the concrete reflected-orbit and selected-reserve hypotheses.

### P1-2: reserve shares were not a genuine one-use allocation

**RESOLVED_BY_HONEST_DOWNGRADE.** The finite-prefix allocation is now fully typed and proved from `ReserveTailInputs`: shares and tails are nonnegative, every listed orbit is paid, total share is at most one, and leftover is nonnegative with an exact one-use identity. The infinite reciprocal-square tail and numerical budget remain explicit unproved inputs, so the canonical reserve node is correctly conditional rather than unconditional.

### P1-3: grouped actual-Xi reciprocal and companion conclusions were generic finite wrappers

**RESOLVED_BY_HONEST_DOWNGRADE.** Reciprocal energy of the concrete actual-Xi jet is derived from nonnegative source-faithful paid prefixes and componentwise local C2 convergence. The divided-difference reciprocal and companion conclusions are concrete fields of `ActualXiOrderThreeInputs` and are consumed by source-specific bridge theorems. They remain explicit analytic hypotheses; no generic finite lemma is mislabeled as their proof.

### P1-4: QA trusted booleans, leaf-name matching, incomplete axiom coverage, and inert bundles

**PARTIALLY_RESOLVED_WITH_EXCLUSION.** The repair adds Lean-environment `#check/#print` declaration auditing, registry-generated axiom audit inputs, exact Challenge/Solution type checks, source-lock hash joins, and explicit rejection of the former inert labels and repeated-node premise. The committed QA TSV no longer carries manual `statement_exists`, `source_locked`, `comparator_checked`, or `axiom_audited` booleans.

Residual exclusion: these mechanisms have not been executed at the repaired head here. In addition, unused-input detection is implemented as a source-level dependency-closure scan rather than a kernel-derived declaration dependency graph. It is a meaningful fail-closed regression check, but reconciliation should not call it authoritative dependency evidence until the full suite runs and its generated outputs are archived.

### P2: registry, blueprint, and report accuracy

**RESOLVED.** `content-C.tex`, `C_OPERATOR_QA.md`, `C_OPERATOR_QA.tsv`, and `C_REPAIR_RESPONSE.md` distinguish proved finite algebra, proved source-specific algebra, conditional analytic bridges, finite heat fixtures, and the unproved RH boundary. The build is explicitly reported as pending rather than passed.

### Trust boundary

**PARTIALLY_RESOLVED_WITH_EXCLUSION.** Exact repaired-diff inspection finds no added `axiom`, `opaque`, `unsafe`, or `admit` declaration. The only intended `sorry` is the single statement-only placeholder in the Challenge; the corresponding ChallengeDeps and Solution sources are sorry-free by inspection. A kernel-level axiom conclusion is withheld because `check_no_sorry.sh` and `check_axioms.sh` were not executed.

### Remote publication

**RESOLVED.** PR #735 is open, draft, unmerged, and points to repaired head `b20ee9b3678e5d8fa32b04b156bc02cec782a97b`. The repair is exactly one commit above the frozen reviewed head, contains all promised repair modules, registries, reports, and scripts, modifies no workflow, and has a repair-response comment on PR #749.

## Integration effect

The source-level P0 statement defects no longer justify rejection of the repaired formalization. The remaining integration blocker is procedural but binding: the exact repaired head has not completed the requested Lean build, comparator builds, registry/blueprint/source checks, no-sorry scan, and axiom audit. The external-source digest also has the narrower normalized-record scope stated above.

Reconciliation may prepare the branch and preserve the conditional/exclusion boundaries, but it should not mark the formal packet accepted or integration-ready until the exact-head suite passes and its generated evidence is attached.

RH remains unproved.

NOT_READY_FOR_RECONCILIATION

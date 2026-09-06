# Reviewer C — structure, schema and extraction plan

Baseline `8d16f8d9c475db290bc85e53d775b93b9bcdb336`; independent review PR #798. **Proposals only:** no main file, research branch, canonical ID, license, permission or setting is changed by this report. Science routing is pending integrator reconciliation, not a new scientific acceptance.

## 1. Preserve the useful existing structure

Keep `README.md` as a short scientific status/navigation front door; keep `AGENTS.md`, `CONTRIBUTING.md` and `docs/REVIEWING.md` as distinct operating guides. Their existing separation of exploration, exact-SHA review and integration is good. Keep machine contracts under their current stable paths: `canonical/registry.yaml`, `canonical/aliases.yaml`, `canonical/provenance.schema.json`. Do not silently replace a schema under the same version identifier.

The principal structural problem is not insufficient volume. A reader must be able to distinguish **reviewed source**, **later branch head**, **claim scope**, **artifact execution**, and **publication status** without reconstructing hundreds of PR discussions. A registry entry or a merged branch is not a substitute for the statement and proof being physically resident in an integrated packet.

## 2. Concrete documentation changes

| Proposed path | Concrete content / acceptance check |
|---|---|
| `docs/REPRODUCING.md` | Clean checkout at exact SHA; lightweight Python and Lean profiles; network/cache requirements; expected commands/outputs; normal and optimized checks; separate sidecars and prohibited broad campaigns. A non-owner can reproduce the bounded fixtures without private paths or secrets. |
| `docs/PUBLIC_LAUNCH.md` | Owner-only checklist from RELEASE_BLOCKERS, signed settings/rights review receipt, anonymous navigation/clone checks. Distinguish configured controls from desired controls. |
| `docs/STATUS_VOCABULARY.md` | Define proposed, reviewed, finite/local/global, conditional, synthetic, imported, refuted, superseded, replayed and kernel-checked. Examples: source-lock equality is not source verification; H^p meromorphic bounds are not analytic membership; finite matrix positivity is not an all-order sign. |
| `docs/EXTERNAL_SOURCES.md` | Table for every upstream repo/paper/data/compiler dependency with source/version, license/NOTICE, file-copy policy, exact toolchain, assumptions, independent build and permission status. #787–#791 are mandatory examples. |
| `research/PROGRAMMES.md` | One row for all eleven programme issues; objective, current controlling source SHA, older correction links, exact open gate and packet coverage. Preserve issue text as discussion, not authoritative immutable theorem storage. |
| `research/CHANGES_SINCE_2026_08_22.md` | Claim-level delta from the actual 139-row release source manifest, not from merge history alone. Show additions, corrections, refutations, scope reductions and unchanged historical alternatives separately. |
| `reviews/README.md` | Review roles, exact source requirement, conflict/author independence, coverage vocabulary, cross-review question template and integrator reconciliation procedure. |
| `SECURITY.md`, `LICENSE`, `NOTICE` or equivalent | Owner-approved reporting and licensing policy. C proposes the need, not a license grant or legal conclusion. |

Generate navigation from a validated source table. Do not promise all latest work is on main while live branch-only deposits remain outside extraction. Historical `gfreund123/riemann` URLs can remain as provenance; use the current owner in active navigation and stable repository ID in source records.

## 3. Identity and disposition schema

The existing alias policy already supplies the right immutable key:

```
(repository_id, source_pr, source_commit, source_path, legacy_id)
```

Extend it explicitly rather than reusing bare `T-107300` or silently choosing one filename. A new schema version should require:

```
record_id
repository_id
source_kind                 # git_file, issue_body, comment, attachment, external_artifact
source_pr_or_issue
source_commit               # 40 hex only for a real Git commit
source_path
source_blob
content_sha256
retrieved_at_utc
source_updated_at            # required for mutable issue/comment bodies
legacy_id
canonical_id                 # nullable until scoped integration
statement_digest
scope                        # finite/local/conditional/cofinal/global
hypotheses
normalization
reviewer
review_scope                  # metadata/header/proof/code/replay/kernel/semantic
verdict
publication_state            # independent of verdict
coverage_status
coverage_universe
coverage_exclusions
depends_on                    # source-qualified IDs
supersedes / invalidates / scope_limits
artifact_ids
execution_receipt_ids
license_and_attribution
```

`frozen_source` for an issue must point to an immutable captured body plus its platform ID/update time, not pretend to be a commit SHA. An attachment needs byte identity and durable residency, not only a title, URL or comment saying it was uploaded. Source references to an unresolved short SHA remain unresolved until uniquely checked.

Require strict parsing: reject duplicate JSON keys, duplicate semantic IDs, float aliases for integers, Boolean-as-integer aliases, invalid SHA syntax, missing mandatory records and unknown enum values. Separate unknown/not inspected from failed, and failure from refutation. The literal phrase **pending integrator reconciliation** means unfinished reconciliation, not an adverse verdict.

### Correction propagation

For each correction, store the source identity of the changed statement and the affected hypothesis/normalization, not just a replacement PR. Traverse reverse dependencies; assign each affected consumer `RECHECK_REQUIRED` until it explicitly shows unaffected scope or incorporates the repair. Preserve all old reviewed files and their verdicts as historical evidence. Never retroactively edit a reviewed source to make an old acceptance appear to cover a repair.

Priority cases: #719 carrier correction, #742 HCNC/BPOE consequences, #752 scout downgrade, #731 repeated supersessions, #771/#774 collisions, and #789's preliminary-versus-hostile external-source disposition. Distinct sources #715 and #722 must not be conflated; the final #722 head matches its actual merged source.

## 4. Computational acceptance contract

Every proof-producing packet should state the primitive source, producer, checker, coverage universe, arithmetic class, rounding software, imported analytic theorems, exact output and independently replayed subset. Hash consistency authenticates bytes; it does not prove that the primitive data are genuine, the universe is complete or an inequality is mathematically relevant.

Use separate commands such as:

```
python produce.py --config CONFIG --output OUT
python check.py --source-lock SOURCE_LOCK --artifact OUT
python -O check.py --source-lock SOURCE_LOCK --artifact OUT
python -m unittest discover -s tests
```

The checker should not overwrite the target result before comparing it. Refuse a changed primitive, omitted/duplicated cell, stale compiler/rounding library, altered normalization, narrowed coverage endpoint, wrong witness and a saved PASS flag without recomputation. Type/syntax and semantic/coverage rejection tests are different obligations.

For rounding, record whether exact rationals, directed intervals, non-directed high precision or mixed arithmetic enter **acceptance**, not merely discovery. Pin mpmath interval-Gamma or FLINT patches when they are trusted; identify which analytic remainder proves the infinite tail. A synthetic six-zero or finite-field fixture is useful algorithmic evidence but is not literal zeta verification.

Keep CI lightweight and explicit. Resource limits and serial bounded fixtures are suitable. Broad conductor/prime/zero campaigns, optimizer sweeps and million-cell reproductions require a separate approved environment and compact authenticated coverage artifacts; they were not launched in this review.

## 5. Formal statement and build contract

For every release-facing Lean declaration record:

```
source_claim_key
informal_statement_and_hypotheses
lean_declaration
lean_source_path_and_blob
statement_scope_match
extra_lean_hypotheses
unused_or_inert_inputs
import_closure
trusted_or_challenge_or_solution
axioms_reported
axiom_output_declaration_coverage
toolchain / mathlib / external_gitlinks
build_commands_and_targets
exit_codes / log_hashes / run_id / head_sha
independent_kernel_status
semantic_reviewer_verdict
```

A successful build proves that the actual formal statement follows in the selected environment. It does not show that the intended theorem was faithfully encoded. Explicit Prop arguments are not custom axioms, but must remain visible in the headline. Conversely a placeholder in an intentionally untrusted Challenge file is not a trusted proof hole unless the import graph reaches it.

For the inspected fixed-detector consumer, retain the missing Landau/holomorphy/pole/zero-strip/reflection assumptions. For Xi order-three, retain verified-height/grouping/reserve/multiplicity and C2 inputs; distinguish PSD from PD and a concrete reserve from a self-asserted existence flag. Check all denominators, intervals, fixedness, totalized inverses and order-of-quantifiers against the source statement.

Publish generated axiom output only with the exact executed command/head and expected declaration list. The parser's success on text is not proof that Lean emitted that text. Main's v4.33.0-rc2 is not interchangeable with an upstream v4.33.0 final or v4.34.0-rc2 environment. Keep external Challenge stubs and patched numerical sidecars out of the trusted import closure until explicitly reviewed.

## 6. Concrete extraction order

**Stage 0 — preserve and close the census.** Freeze all actual reviewed sources and latest heads, captures of discussions and attachments, branches not represented by a PR, and direct-main parents. Complete the 312 unperformed historical comparisons and the transitive reference scan. Resolve metadata truncation explicitly. Do not ask A/B's unpublished reports to supply this C provenance work.

**Stage 1 — identity and correction ledgers.** Extract aliases, supersessions, refutations and source-scope reductions first. Rewrite dependent IDs in newly versioned integration objects, never in old frozen packets. Review #731 and #771/#774 before any bare-ID merge. Keep #789's rejected proof and its corrective review distinct.

**Stage 2 — reproducible infrastructure.** Repair the canonical consumer acceptance gate, retain the tested axiom parser with execution binding, introduce bounded fixture profiles and immutable environment locks, then check documentation/setup. C owns this stage; infrastructure acceptance is not a scientific theorem verdict.

**Stage 3 — formal release spine.** Reconcile the final main source and formal-v0.1 declaration inventory, exact build coverage, source hypotheses and trusted imports. Extract reviewed finite algebra and conditional interfaces at their stated scope. Isolate #787/#788 incompatible toolchains and external assumptions. #791 remains an attributed reference.

**Stage 4 — reviewed mathematical components.** A/B reconcile exact statements independently. Prefer small coherent packets: finite algebra, counterexamples, explicit analytic identities and verified approximation lemmas with complete assumptions. Split mixed packets; do not promote proposed all-order inequalities alongside a passing finite fixture.

**Stage 5 — cofinal and RH-facing frontiers.** Deposit open estimates as open, together with all source adapters and known falsifiers. No source-tail cutoff, finite zero prefix, subspace positivity or high-degree asymptotic is silently upgraded to global closure. A theorem can be valuable without changing RH status.

**Stage 6 — public exploration library.** Archive remaining branch-only notes, imported literature and non-proof diagnostics with source/permission labels. Consolidate route summaries without erasing failed paths or countermodels. Keep test counts version-specific, not cumulative by copying old receipts.

**Stage 7 — owner launch.** Rights, history, access, workflows, anonymous clone and navigation sign-off. Only owners change visibility, teams and rules. Scientific reconciliation and public visibility are separate decisions.

## 7. Independent handoff questions

For A: Which exact versions of #742/#751/#756/#757/#758/#759/#762/#767/#780/#785/#786/#790/#793 survive their current hypothesis and counterexample boundaries? Which finite-field/representation claims from mixed packets should receive separate extraction IDs? Are #787's analytic assumptions faithfully stated?

For B: Which #719/#724/#726/#729/#731/#748/#752/#765/#768/#769/#770/#772/#776/#778/#779/#781/#782/#783/#784/#792 claims are affected by later corrections? Confirm the exact source of any alleged failed record checker before treating a historical assessment as fresh evidence. Do #788's headline hypotheses and #789's hostile correction match the precise statements being proposed for release?

For the integrator: Reconcile these routing suggestions with A/B's actual assigned coverage and source SHAs; they are not exclusivity claims. Resolve version conflicts, then commission only the narrowly identified additional checks. C's implementation findings stand independently, while C's explicit omissions remain open. No scientific acceptance should be inferred from merging this review PR.

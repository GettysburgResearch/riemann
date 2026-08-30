# M-0301 — Source provenance and claim-ID allocation protocol

Claim ID: M-0301  
Title: Source provenance and claim-ID allocation protocol  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: README operating rules  
Scope: organizational and citation methodology  
Related counterexample candidates: none

## Problem with the current process

The default branch initially contained the operating protocol but no durable
literature ledger, claim registry, or source inspection record.  Agent #1
independently bootstrapped root state files on its branch.  Concurrent agents
can therefore create merge conflicts or, worse, cite the same theorem in
different normalizations without recording which source text they inspected.

A bibliographic citation alone does not answer:

- whether the full theorem statement was seen;
- whether the source was original or a later restatement;
- which normalization, branch, or limiting convention was used;
- whether a repository proof is complete or merely imported;
- which claim-ID range an active branch is consuming.

## Proposed change

### 1. Reserve claim ranges per issue

An issue claiming substantial work should reserve a block in its claim
comment.  Issue #3 uses `03xx`; agent #1 uses `0001`-series identifiers.  The
integrator resolves collisions before merge.

### 2. Store a source ledger beside BibTeX

For every external dependency record:

```text
Reference key:
Original or later restatement:
Located URL/DOI/arXiv:
Inspection date:
Inspection level:
Exact theorem/equation used:
Normalization:
Unverified fields:
Claims depending on it:
```

`literature/source-ledger.md` is the initial implementation.

### 3. Separate three statuses

- **bibliographically verified** — the work and metadata were located;
- **statement verified** — the exact displayed statement was inspected;
- **repository verified** — an independent agent reconstructed the proof or
  certified computation.

Publication never automatically supplies the third status.

### 4. Require normalization fingerprints

Every imported explicit formula, completed `L`-function, Fourier/Mellin
transform, and zero sum should have a short fingerprint containing constants,
signs, transform convention, and zero-ordering rule.  Claims with different
fingerprints are not interchangeable.

### 5. Use integrator-ready patches instead of competing root files

When another active branch already owns `CLAIMS.md`, `CURRENT_STATE.md`, or
`LITERATURE.md`, contributors should place exact rows and prose under
`integration/` rather than recreate the root file from an older base.
The integrator can apply the patch after earlier PRs land.

## Expected benefit

- fewer fabricated or memory-completed references;
- explicit provenance for every imported theorem;
- fewer merge conflicts during early parallel bootstrapping;
- visible distinction between literature authority and repository review;
- deterministic dependency graphs for later formalization.

## Possible cost or risk

The ledger adds clerical work and may discourage broad exploration.  Mitigate
this by requiring full records only when a source supports a claim, proof step,
or search exclusion.  Speculative brainstorming may cite `UNVERIFIED` leads
without theorem status.

## Trial procedure

Apply this protocol to issue #3 and its theorem cards.  Ask the integrator and
one verifier to audit:

1. whether every theorem statement has an inspected source;
2. whether inspection levels are honest;
3. whether any root-file merge conflict was avoided;
4. whether another agent can locate the exact supporting passage.

## Success criterion

The protocol succeeds if an independent reviewer can reconstruct every
bibliographic and normalization dependency without private chat history and
can identify all remaining unverified steps in under one review pass.

## Gap audit

- A DOI proves metadata resolution, not theorem content.
- A later paper can misstate an earlier theorem; use the original whenever
  accessible and record the fallback explicitly.
- A theorem translated between normalizations needs a proof of equivalence.
- Claim-range reservations require integrator enforcement to prevent drift.

## Remaining uncertainty

The protocol has been exercised only on one literature-heavy branch.  It may
need a lighter-weight path for exploratory reports and a machine-readable
format before it scales to many simultaneous contributors.  The integrator
should decide whether ID blocks are permanent or only a bootstrap convention.

## Suggested next attack

Add a small validation script that checks unique claim IDs, presence of source
keys, and existence of registry rows.  Later, represent dependencies in a
machine-readable `claims/index.yaml` generated from claim headers.

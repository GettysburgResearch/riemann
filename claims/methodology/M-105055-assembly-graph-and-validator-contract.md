# M-105055 — The assembly-graph and fail-closed validator contract

Claim ID: `M-105055`
Status: **METHODOLOGY — machine contract for extending the canonical
implication graph; no mathematical content**
Created: 2026-08-22
Agent: swarm lane A1
Intended path: `claims/methodology/M-105055-assembly-graph-and-validator-contract.md`
Companions: `T-105050`, `assembly_graph.json`, `validator.py`.
RH status: **unproved, not addressed.**

## 1. Purpose

`assembly_graph.json` is the canonical machine graph of the transport
program's route lattice to RH, built to the union of Reviewer B's
fail-closed graph contract (`review/2026-08-22/cross-b-of-a/CROSS_REVIEW_REPORT.md`
+ `review/2026-08-22/cross-b-of-a/GRAPH_DEFECTS.tsv`,
`origin/review/2026-08-22/reviewer-b-cross-review-a` @
`945a6eec3406cce8f6cd63eba6c69fb60676c41d`) and Reviewer C's
path-qualified provenance mandate (`review/2026-08-22/coverage/INTEGRATION_HANDOFF.md`
+ `review/2026-08-22/coverage/PROVENANCE_DEFECTS.tsv`,
`origin/review/2026-08-22/coverage-genealogy-delta`
@ `a520556ac7f30290a11e1fcba7b6f6a24269153e`). `validator.py` is its
deterministic, stdlib-only, fail-closed checker. This file is the contract
a future integrator must honor to EXTEND either.

## 2. Data model

**Node** := `{semantic_id, kind, status, statement, coordinates,
required_fixes?, notes?}`.

- `kind in {claim, hypothesis, terminal}`. Exactly one terminal, `RH`,
  which may appear only as an edge conclusion (G-RH-TERMINAL-001).
  Every open/conditional/equivalent premise is a typed `hypothesis` NODE,
  never a bare string (G-DANGLE-001 / G-CONDITIONAL-001 repair).
- `status in {VERIFIED, VERIFIED_WITH_FIXES, CONDITIONAL_EXACT,
  OPEN_SUFFICIENT_FOR_RH, OPEN_RH_EQUIVALENT, REFUTED,
  DEPOSITED_UNREVIEWED}`.
  - `CONDITIONAL_EXACT`: the file's statement is a PROVED exact
    conditional/reduction; its open inputs MUST appear as hypothesis
    premises on every edge that uses it.
  - `DEPOSITED_UNREVIEWED`: present in the repo at the pinned SHA but
    without a review-wave ledger row. Never establishable in strict mode.
  - `REFUTED`: firewall; never establishable, never a premise (validator
    rejects).
- `statement`: one sentence with the actual inequality where applicable.
- `coordinates` := `{claim_id, path, branch, sha}` — exactly four fields;
  `sha` exactly 40 lowercase hex; `path` must exist at `sha`
  (`git cat-file -e sha:path`). Semantic IDs are path-qualified: two
  files sharing a claim number are two nodes (Reviewer C
  PROV.383.DUPLICATE_CLAIM_IDS disposition).
- `required_fixes`: verbatim reviewer fixes for VERIFIED_WITH_FIXES rows;
  extension into a canonical packet must apply them
  (CANONICAL_EXTRACTION_PLAN.md rule).

**Edge** := `{edge_id, premises, arity, conclusion, type,
source_coordinates, trust_mode, notes?}`.

- `premises`: JSON array (G-DELIM-001), nonempty, unique, every entry an
  existing node id; `arity` must equal `len(premises)` (G-ARITY-001);
  conclusion exists and is not a premise.
- `type in {PROVED_REDUCTION, CONDITIONAL_IMPLICATION,
  EQUIVALENCE_AFTER_DIAGONAL, HYPEREDGE}` with FIXED semantics:
  - `PROVED_REDUCTION` pointing at a hypothesis node is a reduction INTO
    the open interface and NEVER establishes it. This is the typed
    resolution of Reviewer A's convention (e.g. EDGE.VAUGHAN.HALF_FIELD
    concluding at the open HHFE interface) that Reviewer B's
    G-CONDITIONAL-001 flagged as mechanically ambiguous.
  - The other three types establish their conclusion when ALL premises
    are established (hypotheses: assumed or derived; claims: status in
    {VERIFIED, VERIFIED_WITH_FIXES, CONDITIONAL_EXACT}, plus
    DEPOSITED_UNREVIEWED only in `deposited` mode).
  - An `EQUIVALENCE_AFTER_DIAGONAL` equivalence is stored as its TWO
    directed instances, each with its own mechanism premises — never as
    an undirected edge.
- `trust_mode in {strict, deposited}`: `strict` = the EDGE ITSELF is
  reviewer-registered (a ROUTE_EDGES row at the frozen review SHA), with
  any mechanism-lemma ledger-row gaps recorded as provenance defects on
  the edge (never silently promoted — e.g. `E-HHFE-RH` is registered as
  ROUTE_EDGES line 16 while its mechanism lemmas L-100310..312 lack
  CLAIMS.tsv rows, a gap carried in the edge notes and
  `provenance_defects`); `deposited` = the edge registration itself is
  deposit-only (e.g. T-102110). Strict-mode results are the citable
  ones, WITH the recorded mechanism-gap defects disclosed alongside.
  (Amended per hostile review: the prior wording "every mechanism claim
  has a review-wave ledger row" contradicted the E-HHFE-RH instance.)
- `source_coordinates`: array of four-field coordinates pinning the
  reviewer registration (ROUTE_EDGES line) AND the mathematical source.
- Refuted historical edges (e.g. EDGE.NATIVE.ALPHA_PROMOTION) are NOT
  reproduced as live edges; they are recorded in the refutation node's
  notes. Keep false history, do not traverse it.

**Alias** := `{alias_id, canonical_semantic_id, targets[]}`, all targets
existing nodes (G-ALIAS-001). **provenance_defects** := append-only list;
defects are reported, never silently normalized (malformed SHAs,
dangling names, missing ledger rows).

## 3. Validator obligations (order is normative)

1. Structural node checks (unique ids, kinds, statuses, nonempty
   statements, exact coordinate shape).
2. Structural edge + alias closure checks.
3. Provenance: 40-hex SHA syntax, then LIVE `git cat-file -e` for every
   (sha,path) pair of every node and every edge source — BEFORE any
   reachability (G-PROVEN-001). `--offline` falls back to
   `recorded_checks.json` written by the last successful online run and
   fails closed on any pair not recorded. Any failure here aborts with
   verdict FAIL before reachability runs.
4. Reachability (monotone fixpoint per Section 2 semantics):
   (i) proved-only closure (no hypothesis assumed) — ASSERT RH
   unreachable and no hypothesis established, in BOTH trust modes;
   (ii) per-hypothesis conditional closure — emit which gates alone
   reach RH; (iii) minimal open cut by exhaustive subset search in
   increasing cardinality — ASSERT cardinality 1 for the current graph
   (update this assert only with an accompanying mathematical event);
   (iv) gate partial order `g => h iff h in closure({g})`, quotient by
   mutual implication, transitive reduction — emit Hasse data per mode.
5. Emit `verdict.json` (machine) and `REPORT.md` (human); exit 0 iff all
   asserts green. Determinism: sorted iteration, no timestamps.

## 4. Extension rules

- ADD a new proved claim: node with full four coordinates + ledger row
  citation in notes; re-run validator online.
- ADD a new sufficient gate: hypothesis node (statement = the inequality),
  its consumer edge(s) with reviewer registration in
  `source_coordinates`, and append the id to `meta.gates`; the per-gate
  assert then covers it.
- CLOSE a gate (a proof of the gate statement appears and is reviewed):
  do NOT delete the hypothesis node; add the reviewed producer claim and
  a CONDITIONAL_IMPLICATION edge `[producer...] -> gate-hypothesis`. The
  proved-only assert (i) will then FAIL LOUDLY — that failure is the
  designed signal demanding a full human re-audit before any RH-status
  text changes. RH status may never be changed by editing this file's
  asserts alone.
- REFUTE a claim: flip status to REFUTED (validator then rejects it as a
  premise, so every edge through it must be removed or re-sourced —
  fail-closed by construction).
- Never merge a finite certificate into a global implication edge; never
  point a reviewed node at a later unreviewed head; record — do not fix —
  upstream defects (Reviewer C dispositions).

## 5. Current instance facts (2026-08-22)

41 nodes / 12 edges / 34 aliases+coordinates verified; PASS. Proved-only:
RH unreachable. Each of the 8 hypotheses alone suffices for RH (strict).
Minimal open cut = 1. Strict Hasse: BPOE103300 -> {HHFE102010 <=>
HCNC103100}; FCHD67 -> ROWS23. Deposited adds {HHFE<=>HCNC} ->
CFBB102100 via unrowed T-102110. RH remains UNPROVED.

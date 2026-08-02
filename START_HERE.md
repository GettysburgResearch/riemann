# Start here

This page explains how to understand the repository without reconstructing its pull-request history.

## In ten minutes

1. Read the four-program table in the [README](README.md).
2. Read [RESEARCH_MAP.md](RESEARCH_MAP.md) for the mathematical landscape.
3. Read [FRONTIERS.md](FRONTIERS.md) for the actual missing steps.
4. Open one packet in [`research/integrated/`](research/integrated/README.md).
5. Follow that packet’s exact source and review links only when deeper provenance is needed.

## The three layers

### 1. Front stage

The root pages answer:

- what RH status the repository claims;
- what mathematics is physically present;
- which programs are active;
- what is finite, conditional, empirical, refuted, or open;
- where a human or agent should begin.

### 2. Research stage

An **integrated packet** is a readable, proof-bearing extraction from one or more exact reviewed source commits. It contains the theorem or finite result, proof or proof extract, source qualifications, known failures, and the next missing step.

Integrated does **not** mean “globally solves RH.” It means “the reviewed object now has a stable readable residence on `main`.”

Exploratory work remains freer. It may live in an issue, branch, PR, report, or experiment directory. It is not required to adopt the full integration schema.

### 3. Backstage

The first complete review-wave ledger, machine registry, alias records, timestamped state, and archival capture scripts are preserved under or indexed by [`internal/`](internal/README.md). Use them for exact provenance and integration work. Most researchers should not begin there.

## How to read status

Two dimensions matter: **review state** and **mathematical scope**.

### Review state

- **VERIFIED:** independently reviewed at an exact source commit and accepted within its stated scope.
- **VERIFIED WITH FIXES:** the core survives, but named repairs are required before clean integration or reuse.
- **GAP/BLOCKED:** a load-bearing theorem, source, domain, artifact, or inference is missing.
- **REJECTED:** the reviewed object is false as written or unsuitable as an integration unit.
- **PROPOSED:** new mathematics awaiting exact-SHA review.
- **EMPIRICAL:** ordinary numerical evidence or reconnaissance.
- **REFUTED:** a claim or general inference has a recorded proof of failure.
- **SUPERSEDED:** preserved historically but replaced for current use.

A source file may still say `PROPOSED` even when an exact-SHA review later classified its mathematical content `VERIFIED`. Integrated packets preserve both facts rather than rewriting the source.

### Scope

- **finite:** one declared matrix, interval, tree, point set, prime range, or integer range;
- **local:** one bounded support, ordinate slab, or neighborhood;
- **conditional:** an implication whose stated hypothesis is not established here;
- **cofinal:** an unbounded sequence or limiting family;
- **global:** the full theorem over every required object or scale.

Examples:

- an exact positive \(8\times8\) Pick box is **finite**;
- a theorem saying one strict negative Pick minor contradicts RH is a **finite conditional interface** whose RH necessity is reviewed;
- a theorem saying a cofinal lower envelope would imply RH is **conditional/cofinal**;
- proving the required cofinal envelope would be a major global step.

## What a proof-bearing packet guarantees

A packet guarantees that the repository states, in one place:

- the exact mathematical statement;
- the proof or a self-contained proof extract;
- the source PR, source commit, and source files;
- the review report and verdict;
- normalizations and imported sources;
- finite/global and conditional/unconditional boundaries;
- computation and replay status;
- known counterexamples, exclusions, or failed strengthenings;
- conflicts, alternatives, and the next unresolved step.

A packet does not silently fix its source. Any correction is identified as a distinct reviewed object.

## Suggested reading paths

### Arithmetic

1. [`research/integrated/robin/finite-robin-foundations.md`](research/integrated/robin/finite-robin-foundations.md)
2. the Robin section of [RESEARCH_MAP.md](RESEARCH_MAP.md)
3. the Robin frontier in [FRONTIERS.md](FRONTIERS.md)

### Finite \(\xi\) counterexample criteria

1. [`research/integrated/xi/derivative-free-pick-loewner.md`](research/integrated/xi/derivative-free-pick-loewner.md)
2. [`research/integrated/xi/finite-pick-controls.md`](research/integrated/xi/finite-pick-controls.md)
3. the \(\xi\) frontier in [FRONTIERS.md](FRONTIERS.md)

### Proof hygiene and corrections

1. [`research/integrated/corrections/proof-boundary-corrections.md`](research/integrated/corrections/proof-boundary-corrections.md)
2. the incompatibilities in [RESEARCH_MAP.md](RESEARCH_MAP.md)

### Weil/screw and kernel/operator programs

Begin with the program summaries in [RESEARCH_MAP.md](RESEARCH_MAP.md) and the exact missing statements in [FRONTIERS.md](FRONTIERS.md). Their detailed reviewed source graph remains backstage because a clean proof-bearing extraction is still a Round 2 target.

## A compact glossary

- **primitive:** an externally meaningful source object, such as a completed-\(\xi\) ball, zero count, zero ball, prime-power manifest, or Weil matrix.
- **directed interval:** an outward enclosure guaranteed to contain the true value under its arithmetic contract.
- **proof object:** compact data that a small checker can replay to establish a finite implication.
- **source-qualified:** accepted only after naming an external theorem, normalization, data source, or implementation whose full proof is not reproduced in the packet.
- **locality gate:** a theorem proving that a candidate’s failure must arise inside a declared local region.
- **coverage gate:** a proof that every required cell, zero shell, prime power, shard, or tree terminal is present exactly as declared.
- **cofinal:** extending through an unbounded sequence, not merely many finite examples.
- **Schur correction:** elimination of a positive block, subtracting a positive semidefinite cross term from the remaining block.

# Agent entrypoint

RH remains unsolved. This file is the minimum operating guide for a research agent working in this repository.

## Read before acting

1. [`START_HERE.md`](START_HERE.md)
2. [`RESEARCH_MAP.md`](RESEARCH_MAP.md)
3. [`FRONTIERS.md`](FRONTIERS.md)
4. the relevant packet under [`research/integrated/`](research/integrated/README.md)
5. current overlapping issues and pull requests

Do not begin with the archival PR ledger unless the task is integration or provenance reconstruction.

## Choose the type of contribution

### Exploration

Broad reformulations, reconnaissance, synthetic countermodels, unconventional connections, and failed attempts are welcome. They may stay on a research branch or PR and need only a short proof boundary:

```text
Status:
Scope:
Exact source/dependencies:
What was run:
What remains:
```

Exploration does not need the machine provenance schema.

### Reviewable mathematical object

State the exact theorem, lemma, refutation, algorithm, or finite predicate. Include its hypotheses, normalization, domain, finite/global scope, dependencies, and proof. Separate imported facts from native proof.

### Proof-producing computation

Bind the primitive source, normalization, complete coverage convention, arithmetic class, producer, checker, hashes, and strict verdict. A checker that validates only derived JSON is not an authenticated primitive replay.

### Integrated packet

Integration requires an exact frozen source commit and exact-SHA review. The packet must contain readable mathematics on `main`, not merely a registry pointer. A repair is a new object; it does not rewrite the reviewed past.

## Current programs

- **Robin/Nicolas arithmetic:** finite canonical reductions are strong; the unbounded tail is open.
- **Weil/screw/terminal-prime:** finite witnesses are possible; source normalization, coverage, and global/cofinal sign remain load-bearing.
- **Completed-\(\xi\)/Pick/Loewner/Stieltjes:** exact finite negative predicates are mathematically sharp; no strict Riemann-data violation is known.
- **Kernel/operator synthesis:** much finite algebra exists; the complete capturing hierarchy and cofinal corrected-kernel floor remain open.

Use [`FRONTIERS.md`](FRONTIERS.md) to select a task that actually removes a load-bearing gap.

## Non-negotiable boundaries

Never:

- describe RH as proved or disproved without a complete reviewed argument;
- turn a finite positive result into global evidence;
- turn a local zero census into a verdict on a global functional without a locality/complement theorem;
- call ordinary high precision directed or certified;
- call a workflow trigger a result;
- infer an infinite sequence from a finite ladder or fitted trend;
- silently strengthen a reviewed statement;
- recycle an old claim ID;
- hide missing source, domain, coverage, or artifact gates behind numerical margin.

## Before requesting review

Freeze the intended commit. List the exact files and load-bearing claims. Say what the checker authenticates, what it assumes, and what was not replayed. Identify the smallest statement whose failure would invalidate the result.

## Before extending an integrated packet

Preserve its source PR, exact commit, source files, review report, scope, and known misreadings. Put new mathematics in a separate proposed object and link it explicitly.

## Backstage material

Machine registries, the full 2026-08-01 ledger, and archival utilities are indexed under [`internal/`](internal/README.md). Use them when reconstructing provenance, collisions, reviews, or post-cutoff history—not as a substitute for reading the mathematics.

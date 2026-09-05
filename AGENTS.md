# Agent entrypoint

RH remains unsolved. This is the minimum operating guide for a research agent.

Contribution access is described in [CONTRIBUTING.md](CONTRIBUTING.md#join-and-start); shared review responsibilities are in [docs/REVIEWING.md](docs/REVIEWING.md). Publish work on your own branch through a PR. Only integrators or owners should update `main` through the review process. Branch permission is not permission to edit another contributor's work or promote an unreviewed claim.

## Reading path

1. Read [`README.md`](README.md).
2. Read this file.
3. Read one of:
   - [`research/RESULTS_INDEX.md`](research/RESULTS_INDEX.md) for repository-wide orientation;
   - the relevant packet under [`research/integrated/`](research/integrated/README.md) for proof-bearing mathematics.
4. Check current overlapping issues and pull requests before starting work.

Do not begin with the complete PR ledger unless the task is historical integration or provenance reconstruction.

## Choose the contribution type

### Exploration

Broad reformulations, reconnaissance, synthetic countermodels, unconventional connections, and failed attempts are welcome. A lightweight header is enough:

```text
Status:
Scope:
Exact sources or dependencies:
What was actually run:
Smallest remaining gap:
```

Exploration does not need the machine provenance schema.

### Reviewable mathematics

State the exact theorem, lemma, refutation, algorithm, or finite predicate. Include:

- hypotheses and quantifiers;
- normalization and analytic domain;
- finite/local/conditional/cofinal/global scope;
- native proof versus imported theorem;
- dependencies and known counterexamples;
- complete proof or an auditable proof extract.

### Proof-producing computation

Bind:

- the primitive source and normalization;
- complete coverage semantics;
- arithmetic class and rounding contract;
- producer and checker source;
- artifacts and content hashes;
- strict acceptance rule;
- what was independently reproduced.

A checker that accepts internally consistent derived JSON is not an authenticated primitive replay.

### Integrated packet

Integration requires:

- one exact frozen source commit;
- exact-SHA independent review;
- readable mathematics physically resident under `research/integrated/`;
- explicit source, review, scope, computation, and next-step boundaries.

A repair receives a new identity and review. It does not rewrite the reviewed past.

## Current programs

- **Robin/Nicolas arithmetic:** finite canonical reductions are strong; the unbounded tail remains open.
- **Weil/screw/carrier/terminal-prime:** finite criteria and controls exist; source normalization, coverage, and the cofinal sign remain load-bearing.
- **Completed-\(\xi\)/Pick/Loewner/Stieltjes:** finite negative predicates are sharp; no strict Riemann-data violation is known.
- **Kernel/operator synthesis:** much finite algebra has survived review; complete capture and the cofinal corrected-kernel floor remain open.

The [results index](research/RESULTS_INDEX.md) states the strongest source-pinned object and exact next burden in each family.

## Non-negotiable boundaries

Never:

- describe RH as proved or disproved without a complete reviewed argument;
- turn a finite positive result into global evidence;
- use a local zero census to decide a global functional without a locality or complement theorem;
- call ordinary high precision directed or certified;
- call a workflow marker a mathematical result;
- infer an infinite theorem from a finite ladder or fitted trend;
- silently strengthen a reviewed statement;
- recycle a historical claim ID;
- conceal a missing source, domain, coverage, or artifact gate behind numerical margin.

## Before requesting review

Freeze the intended head SHA. Identify the load-bearing files and claims. State what each checker authenticates, what it assumes, and what was not replayed. Name the smallest statement whose failure would invalidate the result.

## Before extending an integrated packet

Preserve its source PR, exact commit, source files, review report, scope, and known misreadings. Put new mathematics in a separately labeled proposed object.

## Backstage material

- Stable machine data: [`canonical/`](canonical/README.md)
- Historical snapshot and complete ledger: [`internal/archive/`](internal/archive/README.md)
- Offline archival and validation tools: [`internal/tools/`](internal/tools/README.md)

Use backstage material for provenance, collision, or integration work—not as a substitute for reading the mathematics.

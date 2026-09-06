# Agent entrypoint

RH remains unsolved. This is the minimum operating guide for a research agent.

Contribution access is described in [CONTRIBUTING.md](CONTRIBUTING.md#join-and-start); shared review responsibilities are in [docs/REVIEWING.md](docs/REVIEWING.md). Publish work on your own branch through a PR. Only integrators or owners should update `main` through the review process. Branch permission is not permission to edit another contributor's work or promote an unreviewed claim.

## Reading path

1. Read [README](README.md), [STATUS](STATUS.md) and the relevant part of [RESULTS](RESULTS.md).
2. Read this file and the [current statement and proof route](research/integrated/CURRENT_RESULTS.md) for the chosen result, then its full source and evidence.
3. Use [research navigation](research/RESULTS_INDEX.md) for earlier source-qualified components and [open tasks](OPEN_CUTS.md) for a bounded contribution.
4. Check [active issues and PRs](PROGRAMMES.md#active-research) before starting. A later branch head is not automatically integrated or reviewed.

Do not begin with the complete PR ledger unless the task is historical integration or provenance reconstruction. The public scientific account is cumulative: preserve inherited scope and apply the latest correction to the exact affected object.

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

A repair receives a new identity and review. It does not rewrite the reviewed past. Editorial consolidation does not approve a new composition of arguments or strengthen a statement; either requires its own review.

## Current programs

The [approach map](PROGRAMMES.md) covers Robin arithmetic, signed native/Möbius cancellation, xi geometry and derivative descent, full-source operators and heat, L-function families/generalized structures, and causal Euler corrections. The [results index](research/RESULTS_INDEX.md) preserves the wider inherited corpus.

Keep the distinctions sharp: fixed-P61 is not growing-prime control; supercritical SHARP is not the critical-power estimate; specified adaptable capture is not every predetermined hierarchy; a positive Galerkin upper section is not a lower certificate; and a family identity is not principal-member extraction.

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

- Stable machine data: [canonical](canonical/README.md)
- Integration and audit records: [integration](integration/README.md)
- Historical snapshot and complete ledger: [internal/archive](internal/archive/README.md)
- Offline archival and validation tools: [internal/tools](internal/tools/README.md)

Use backstage material for provenance, collision, or integration work—not as a substitute for reading the mathematics.

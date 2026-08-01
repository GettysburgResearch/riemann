# Repository model and continuing integration process

## Design goals

The repository needs two properties that can appear to conflict:

1. agents must remain free to explore broad, speculative, unconventional ideas;
2. canonical mathematical and computational claims must be auditable across branches, repairs, reviews, and integrations.

The proposed model applies strict metadata only when an object seeks canonical, proof-producing, or integration status. Exploratory PRs remain lightweight.

## Layered organization

The current repository structure can be retained. The integration adds an overlay rather than a disruptive migration.

### `claims/`, `experiments/`, `literature/`, `reports/`

These remain the working research layer.

- `claims/` contains authored theorem, lemma, definition, methodology, observation, and refutation cards.
- `experiments/` contains code, proof objects, reconnaissance, and artifacts.
- `literature/` contains source ledgers and imported interfaces.
- `reports/` and `audits/` contain append-only session and exact-SHA review records.

Objects here may be proposed or exploratory.

### `integration/YYYY-MM-DD/`

This is the timestamped operational state:

- cutoff and base commit;
- exact reviewed heads;
- present-head confidence and post-cutoff deltas;
- PR dispositions;
- synthesis, priorities, and handoff.

A new pass creates a new directory. It does not rewrite an old cutoff.

### `canonical/`

This is a small promotion layer, not a second copy of the repository.

- `registry.yaml` indexes reviewed canonical packets and their exact scope;
- `aliases.yaml` records collisions, renames, repairs, and supersessions append-only;
- `provenance.schema.json` defines the typed promotion contract;
- source theorem and artifact files remain in their original paths unless extraction materially improves clarity.

A registry entry may point to a frozen source path. Canonicalization does not require duplicating every proof file.

### Refutations and supersessions

Refutations should remain under `claims/refutations/` and be indexed canonically. A superseded claim is not deleted. Its registry record points to the replacement and preserves the old review.

## Status model

Status is multi-axis. A single word such as “verified” is not enough without scope.

### Mathematical kind

- `native_theorem`
- `imported_theorem`
- `conditional_implication`
- `finite_algebra`
- `finite_computation`
- `empirical_observation`
- `methodology`
- `refutation`
- `review_record`

### Review state

- `unreviewed`
- `reviewed_verified`
- `reviewed_verified_with_fixes`
- `reviewed_blocked`
- `reviewed_rejected`

### Scope

- `finite`
- `local`
- `conditional`
- `cofinal`
- `global`

### Lifecycle

- `active`
- `canonical_candidate`
- `canonical`
- `superseded`
- `refuted`
- `withdrawn`

These axes prevent a “verified finite computation” from being mistaken for a “verified global theorem.”

## Typed provenance contract

Every canonical or proof-producing object should bind the fields in `canonical/provenance.schema.json`.

### Identity and scope

- stable object ID;
- title and exact statement;
- object kind and scope;
- native/imported/conditional/empirical status;
- explicit finite-versus-global boundary.

### Source and review

- source PR;
- exact source commit;
- source paths;
- reviewer and review report;
- verdict at that commit;
- integration commit and timestamp.

### Dependencies and normalization

- claim dependencies by stable or context-qualified ID;
- external source qualification;
- normalization ID and fingerprints;
- Fourier/Mellin, ξ, Weil/Suzuki, metric, and sign conventions;
- domain or form-core assumptions.

### Primitive data

Each primitive records a type and authentication method.

#### Completed-ξ and logarithmic derivative

- exact point or rectangle;
- normalization and common scale;
- producer source hash;
- denominator/nonvanishing gate where division occurs;
- functional-equation or independent-assembly control.

#### Zeros and zero counts

- ordinate interval and endpoint convention;
- critical-line versus total-zero semantics;
- multiplicity and simplicity claims;
- count source and completeness;
- shell/slab coverage and exterior guards;
- exact zero-table or proof-grade bins.

#### Primes and prime powers

- finite support rule;
- complete manifest or deterministic generator;
- duplicate handling;
- shard boundaries and exact coverage;
- ordinary primes versus higher powers;
- producer and manifest hashes.

#### Weil/Suzuki normalization

- exact test-function/source definition;
- transform convention;
- support and admissibility;
- prime, pole, archimedean, gamma, and trivial-zero terms;
- source theorem and version.

#### Metrics, packet bases, and Schur maps

- basis and coordinate transform;
- metric Gram and normalization;
- parity/source constraints;
- block decomposition and map dimensions;
- assembly radius and directed Loewner bounds.

#### Interval and directed arithmetic

- arithmetic class;
- rounding mode;
- decimal serialization rule;
- precision ladder;
- enclosure nesting;
- exact checker source hash;
- strictness rule and zero-touch behavior.

### Artifacts and replay

- path or durable object location;
- content hash and size;
- storage/retention class;
- producer and consumer;
- replay command;
- replay level: schema, exact algebra, primitive recomputation, or independent backend;
- known missing segments or unavailable payloads.

A GitHub Actions artifact with a retention period is not immutable. The content hash may be stable while availability is temporary.

## Claim-ID collision policy

Never reuse or rewrite an old ID.

The canonical identity of a legacy claim is the tuple:

```text
(source PR, source commit, source path, legacy ID)
```

A collision receives a new canonical ID. `canonical/aliases.yaml` records:

- context-qualified legacy identity;
- collision set;
- canonical replacement if selected;
- supersession or refutation relation;
- migration date and integration commit.

Old review citations remain valid because the historical identity is preserved.

## Review process

1. Record the source head SHA before reading.
2. Review that exact commit.
3. Classify precise statements and artifacts, not merely the PR title.
4. Separate native proof, imported theorem, finite computation, empirical evidence, and later proposed material.
5. Inspect enough source and checker code to understand the trust boundary.
6. Use only small targeted executions unless a dedicated computation review is requested.
7. Publish a report with exact files, dependencies, fixes, and merge-order concerns.
8. Treat a later repair as a new object.

## Integration process

### Freeze

Record:

- UTC/local time;
- `main` commit;
- open PR numbers;
- exact review-recorded heads;
- directly refreshed current heads;
- uncertainty and post-cutoff deltas.

A commit-timestamp reconstruction may be retained as a hint only.

### Classify deltas

For every current head differing from a reviewed head, classify the delta:

- editorial only;
- review report;
- proposed connection;
- new theorem;
- artifact or workflow change;
- repair;
- unknown.

Only an independently reviewed delta can inherit canonical status.

### Extract

Prefer coherent packets:

- a definition plus its normalization;
- a theorem and exact checker;
- a finite artifact and replay record;
- a refutation plus corrected replacement;
- a review record;
- an empirical dataset with explicit non-proof status.

Do not merge an entire stacked history merely because one theorem is useful.

### Order

A sensible merge order is:

1. correction/refutation and review records;
2. shared definitions and source normalizations;
3. finite algebra and exact checkers;
4. source-qualified primitive producers;
5. finite production artifacts;
6. conditional or cofinal theorems;
7. exploratory observations.

### Validate

Normal integration checks are lightweight:

- parse JSON and schemas;
- validate SHA formats;
- check unique canonical IDs and context-qualified aliases;
- compare ledger population and review aggregate;
- verify internal links and source paths;
- run standard-library exact synthetic tests when small;
- do not rerun broad zero, prime, spectral, or special-function workloads.

### Handoff

Record unresolved source audits, incomplete artifacts, current-head deltas, settled/provisional organizational choices, and the exact first tasks for the next pass.

## Keeping exploration free

The canonical layer is a promotion gate, not an authoring gate. An agent may still:

- open a broad research PR;
- invent a new equivalent formulation;
- publish reconnaissance;
- test a speculative connection;
- use ordinary numerical tools for discovery;
- preserve a failed direction.

The stricter contract begins only when the object seeks a canonical or proof-producing status. This keeps the research culture creative without making the public mathematical state ambiguous.

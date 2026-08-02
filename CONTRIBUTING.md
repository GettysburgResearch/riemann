# Contributing

This repository supports both free exploration and exact mathematical integration. RH remains unsolved.

## Exploration is lightweight

Open broad or unconventional research PRs freely. They may contain conjectures, reconnaissance, synthetic models, failed attempts, literature connections, or prototype code.

Near the top, state:

```text
Status:
Scope:
Exact dependencies or sources:
What was actually run:
Smallest remaining gap:
```

Use accurate labels such as `PROPOSED`, `EMPIRICAL`, `SYNTHETIC_CONTROL`, `IMPORTED`, `REFUTED`, or `SUPERSEDED`.

Exploratory work does **not** need to satisfy the machine provenance schema.

## Minimum proof discipline

Do not:

- call ordinary floating point directed or certified;
- call a workflow marker a result;
- infer a global theorem from a finite ladder;
- infer a verdict on a global functional from a local zero census without a locality/complement theorem;
- present self-declared JSON status fields as proof of their external gates;
- reuse an existing claim ID;
- silently strengthen a reviewed statement.

Separate native proof, imported theorem, finite computation, and conditional consequence.

## Requesting exact-SHA review

Before requesting review:

1. freeze the intended commit and publish its full SHA;
2. identify the load-bearing files and claims;
3. state every hypothesis, normalization, analytic domain, endpoint, multiplicity, and coverage convention;
4. distinguish finite, local, conditional, cofinal, and global conclusions;
5. say what the checker recomputes and what it assumes;
6. bind primitive sources and artifacts where applicable;
7. record what was run and what was not run;
8. include adversarial tests that target proof gates, coverage, provenance, strictness, and common misreadings.

A review verdict applies only to that exact source commit and scope.

## What makes a packet integrable

A future packet under [`research/integrated/`](research/integrated/README.md) should contain:

- a precise statement;
- a proof or self-contained proof extract;
- exact source PR, commit, and files;
- review report and verdict;
- dependencies and source qualifications;
- normalization and notation;
- finite/global and conditional/unconditional boundaries;
- computation and replay status;
- refutations, alternatives, and supersessions;
- the smallest next missing step.

A packet must put readable mathematics on `main`. A machine registry pointer alone is not integration.

A later repair is a new reviewed object. It does not retroactively verify a flawed frozen result.

## Computational artifacts

Use explicit arithmetic classes:

- `EXACT_RATIONAL`;
- `CERTIFIED_INTEGER_COVERAGE`;
- `DIRECTED_INTERVAL`;
- `NON_DIRECTED_HIGH_PRECISION`;
- `FLOATING_RECONNAISSANCE`;
- `SYNTHETIC_CONTROL`;
- `MIXED`.

A proof-producing consumer should authenticate the primitive source, not merely validate a digest string or semantic flag asserted inside the same derived file. Coverage must establish the actual required stream: cells, zero shells, prime powers, shards, or tree terminals.

GitHub Actions artifacts are temporary transport. Record retention, durable hashes, and a reconstruction path.

## Claim identities and collisions

Treat historical claim IDs as permanent addresses. When an ID collides, refer to the old object by source context, for example:

```text
pr:152@bad48a79:claims/lemmas/L-14312-...
```

Then allocate a new ID for a repaired or integrated object. Append-only collision and supersession records are kept in [`internal/registry/aliases.yaml`](internal/registry/aliases.yaml).

## Machine provenance

The historical registry and optional schema are backstage under [`internal/registry/`](internal/registry/README.md). They are useful for canonical or proof-producing work but are not required for ordinary exploration.

## Pull-request description checklist

Include:

- exact base and head SHA;
- contribution and scope;
- claim IDs and statuses;
- finite versus global boundary;
- dependencies and imported sources;
- arithmetic class and artifacts;
- tests and replay commands;
- known gaps and adversarial targets;
- relationship to RH without overstatement;
- preferred review order.

## Integration

Integrators should extract coherent claim-level packets rather than merge branch histories indiscriminately. Preserve exact provenance, alternate proofs, refutations, and aliases. Keep timestamped ledgers and review-wave inventories backstage; keep the current scientific view in the root and research layer.

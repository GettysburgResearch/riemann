# Contributing

The repository is designed for both free exploration and auditable mathematical integration.

## Exploratory work

Open a research PR freely. It may contain speculative reformulations, reconnaissance, synthetic models, unproved connections, or unconventional approaches. State the proof boundary near the top of the PR and label each object as `PROPOSED`, `EMPIRICAL`, `IMPORTED`, `REFUTED`, or another accurate status.

Exploration does **not** require a complete canonical provenance record. It does require honesty:

- do not call ordinary floating-point output directed or certified;
- do not call a workflow trigger a result;
- do not infer a global conclusion from a finite ladder;
- do not use a local zero-count statement to retire an unrelated global functional;
- do not silently reuse a claim ID already present on another branch.

## Requesting exact-SHA review

Before requesting review:

1. Freeze the intended commit and put its full SHA in the request.
2. Identify the load-bearing claims and exact files.
3. Separate native proofs, imported theorems, finite computations, and conditional consequences.
4. List every source normalization, domain, and coverage convention.
5. State whether the checker authenticates primitive files or only validates a derived JSON object.
6. State what was actually run and what was not run.
7. Preserve a compact proof object or an independently regenerable, content-addressed artifact.
8. Include adversarial tests that mutate logical gates, provenance, coverage, and strictness—not only happy-path arithmetic.

A review verdict applies only to that SHA and scope.

## Seeking canonical integration

Canonical promotion is stricter. Add or propose one provenance record conforming to [`canonical/provenance.schema.json`](canonical/provenance.schema.json). The record should bind:

- object identity, kind, statement, and scope;
- source PR, frozen commit, and source paths;
- native/imported/conditional/empirical/refuted status;
- dependencies and normalization fingerprints;
- primitive artifacts, hashes, authentication method, and completeness;
- ordinate, support, point, endpoint, shell, and coverage conventions;
- arithmetic and rounding class;
- replay level and independent reproduction;
- review verdict, reviewer, and review location;
- integration commit and timestamp;
- aliases, repairs, refutations, and supersessions.

A repair receives a new record and review. It does not rewrite the old record.

## Claim IDs and aliases

Treat old identifiers as permanent historical addresses. Never recycle them.

When collisions exist, use a context-qualified legacy reference such as:

```text
pr:152@bad48a79:claims/lemmas/L-14312-...
```

Then allocate a new canonical ID and append a mapping to [`canonical/aliases.yaml`](canonical/aliases.yaml). Do not edit old reports merely to make current naming look clean.

## Computational artifacts

Distinguish:

- `EXACT_RATIONAL`;
- `DIRECTED_INTERVAL`;
- `CERTIFIED_INTEGER_COVERAGE`;
- `NON_DIRECTED_HIGH_PRECISION`;
- `FLOATING_RECONNAISSANCE`;
- `SYNTHETIC_CONTROL`.

A proof-producing consumer must authenticate the primitive source, not merely accept hashes or semantic flags asserted inside the same JSON. Coverage checks must establish the actual stream—prime powers, zero shells, shards, endpoints, or tree terminals—not just aggregate counts.

GitHub Actions artifacts are convenient transport, not permanent immutable storage. Record retention and availability explicitly, and preserve durable content hashes plus a reconstruction path.

## Pull-request description checklist

Include:

- exact source/base and head SHA;
- one-paragraph contribution;
- claim IDs and statuses;
- finite versus global boundary;
- dependencies and imported source qualifications;
- artifacts and replay commands;
- numerical/arithmetic class;
- known gaps and adversarial targets;
- relationship to RH without overstatement;
- preferred review order.

## Integration process

A later integrator should create a new timestamped state directory rather than overwrite an earlier snapshot. The integrator may extract claims from a PR instead of merging it whole, but must preserve the source PR, frozen SHA, review, aliases, and disposition.

The current process is documented in [`integration/2026-08-01/REPOSITORY_MODEL.md`](integration/2026-08-01/REPOSITORY_MODEL.md).

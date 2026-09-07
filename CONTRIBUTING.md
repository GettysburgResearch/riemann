# Contributing

This repository supports free exploration and exact mathematical integration. RH remains unsolved.

## Join and start

1. Read the [scientific status and route map](README.md), then choose a question that interests you. Check overlapping issues and PRs; coordination is useful, but you do not need permission to explore a new direction.
2. For direct repository access, [request contributor access](https://github.com/GettysburgResearch/riemann/issues/new?template=contributor-access.md) with your GitHub username and the project you want to work on. While the repository is private, ask the maintainer who invited you instead. An owner or authorized team maintainer adds you to `polymath-contributors`; accept any GitHub invitation. No email address, biography, or research proposal is required in the issue.
3. Work on your own branch and open a PR. Contributors have Write access to the project repository. Leave `main`, other people's branches, and frozen research records to the integration process. Public contributors can also use a fork and PR without joining the organization.
4. Give your contribution the short status header below and identify the question it advances. A useful counterexample, review, or precise obstruction is a contribution. You do not need a claimed proof of RH.

Using ChatGPT from a phone? Follow [the phone tutorial](docs/PHONE.md). Research agents should read [AGENTS.md](AGENTS.md). For reviewing someone else's work or requesting acceptance of a result, use [the review guide](docs/REVIEWING.md).

Use public-safe material: do not commit credentials, private chat transcripts, personal contact details, or local configuration containing secrets. Credit contributors by their chosen public name or GitHub username. Ordinary scholarly citations are welcome.

## Roles and responsibilities

Our intended division of access and responsibility is:

| Group | Access and responsibility |
|---|---|
| Contributors | Write access for research branches and PRs; review one another's work. Public fork contributions are also welcome. |
| Integrators | Write access plus permission to merge reviewed PRs into main; preserve claim status, dependencies and review scope. Repository Admin access is not needed. |
| Owners | Manage membership, settings and exceptional interventions; keep this group small. |

Owners configure GitHub permissions and branch protections separately; this table describes the working policy.

Interested in helping integrate? Start by reviewing contributions and preparing a small integration PR, then ask a maintainer about joining the integration team.

## Exploratory work is lightweight

Open broad or unconventional research PRs freely. They may contain conjectures, reconnaissance, synthetic models, failed attempts, literature connections, or prototype code.

Near the top, state:

```text
Status:
Scope:
Exact sources or dependencies:
What was actually run:
Smallest remaining gap:
```

Use accurate labels such as `PROPOSED`, `EMPIRICAL`, `SYNTHETIC_CONTROL`, `IMPORTED`, `REFUTED`, or `SUPERSEDED`. Exploration does not need the machine provenance schema.

## Minimum proof discipline

Do not:

- call ordinary floating point directed or certified;
- call a workflow marker a result;
- infer a global theorem from a finite ladder;
- infer a global-functional verdict from a local zero census without a locality or complement theorem;
- present self-declared JSON states as proof of external gates;
- reuse an existing claim ID;
- silently strengthen a reviewed statement.

Separate native proof, imported theorem, finite computation, and conditional consequence.

## Requesting exact-SHA review

Before requesting review:

1. freeze and publish the full intended head SHA;
2. identify the load-bearing files and claims;
3. state every hypothesis, normalization, domain, endpoint, multiplicity, and coverage convention;
4. distinguish finite, local, conditional, cofinal, and global conclusions;
5. say what the checker recomputes and what it assumes;
6. bind primitive sources and artifacts where applicable;
7. record what was run and what was not run;
8. include adversarial tests for proof gates, coverage, provenance, strictness, and common misreadings.

A verdict applies only to that exact source commit and scope.

## What makes a packet integrable

A packet under [`research/integrated/`](research/integrated/README.md) should contain:

- a precise statement and proof or self-contained proof extract;
- exact source PR, commit, and files;
- review report and verdict;
- dependencies, imported sources, normalization, and notation;
- finite/global and conditional/unconditional boundaries;
- computation and replay status;
- refutations, alternatives, and supersessions;
- the smallest next missing step.

A machine registry pointer alone is not mathematical integration. A later repair is a new reviewed object.

## Computational artifacts

Use explicit arithmetic classes:

- `EXACT_RATIONAL`
- `CERTIFIED_INTEGER_COVERAGE`
- `DIRECTED_INTERVAL`
- `NON_DIRECTED_HIGH_PRECISION`
- `FLOATING_RECONNAISSANCE`
- `SYNTHETIC_CONTROL`
- `MIXED`

A proof-producing consumer should authenticate primitive files, not merely accept a digest string or semantic flag inside the same derived object. Coverage must establish the actual stream of cells, zero shells, prime powers, shards, or tree terminals.

GitHub Actions artifacts are temporary transport. Record retention, durable hashes, and a reconstruction path.

## Claim identities

Historical claim IDs are permanent addresses. When IDs collide, use source context, for example:

```text
pr:152@bad48a79:claims/lemmas/L-14312-...
```

Allocate a new ID for a repaired or integrated object. Append-only collision and supersession records remain at [`canonical/aliases.yaml`](canonical/aliases.yaml).

## Stable machine contract

The established machine paths remain authoritative:

- [`canonical/registry.yaml`](canonical/registry.yaml)
- [`canonical/aliases.yaml`](canonical/aliases.yaml)
- [`canonical/provenance.schema.json`](canonical/provenance.schema.json)

They are backstage data contracts, not the human front door. Do not relocate or replace them with a different schema under the same filename.

## Pull-request checklist

Include:

- exact base and head SHA;
- contribution, claim IDs, status, and scope;
- finite-versus-global boundary;
- dependencies and imported sources;
- arithmetic class, artifacts, and replay commands;
- tests and known gaps;
- relationship to RH without overstatement;
- preferred review order.

## Integration

Integrators should extract coherent claim-level packets rather than merge branch histories indiscriminately. Preserve exact provenance, alternate proofs, refutations, aliases, and frozen review boundaries. Keep timestamped inventories backstage and the current mathematical view in `README.md` and `research/`.

## Contribution license

By submitting a contribution, you agree to license your original contribution under the [MIT License](LICENSE). Only include material you have the right to contribute; preserve third-party licenses, notices, and attribution.

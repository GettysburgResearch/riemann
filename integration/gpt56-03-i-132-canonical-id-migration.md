# Canonical ID migration — `gpt56-03-i` positive-anchor program

Concurrent PR #125 allocated the `L-12101`, `L-12102`, and `X-12101` identifiers
while this stacked branch was under active development. To preserve a unique
append-only registry, every canonical registration on this branch is moved to
the `132xx` namespace.

## Canonical claims

| Canonical ID | Temporary authoring ID | Title |
|---|---|---|
| `L-13201` | `L-12101` | Positive-anchor one-moment transform and two-sided Schur gate |
| `L-13202` | `L-12102` | Multi-anchor Christoffel ladder and divided-difference reconstruction |
| `L-13203` | `L-12103` | Certified line-mass budgets for multi-anchor responses |
| `O-13201` | `O-12101` | PR #103 positive-anchor reconnaissance |

The temporary claim files have been deleted. They must not be registered or
cited as canonical IDs.

## Canonical experiments

| Canonical ID | Legacy repository path | Meaning |
|---|---|---|
| `X-13201` | `experiments/X-12101-positive-anchor-ladder/` | exact ladder checker, controls, and empirical scout |
| `X-13202` | `experiments/X-12102-directed-positive-anchor/` | directed PA-1 producer and verifier |
| `X-13203` | `experiments/X-12103-anchor-line-mass-budget/` | exact line-mass budget checker |

The experiment directories retain their original paths to avoid destructively
rewriting committed certificates, digests, workflow paths, and the already-open
trigger PR #135. The canonical experiment ID is the `X-1320x` value in this
table. Integrators may rename directories at merge time, but must preserve file
bytes and retained digests.

## Canonical source graph

```text
L-9308 / L-9309 / L-9310
        |
        +--> L-13201 one positive anchor
        |        |
        |        +--> X-13202 directed PA-1
        |
        +--> L-13202 multi-anchor ladder
                 |
                 +--> X-13201 PA-3 / PA-7 tables
                 |
                 +--> L-13203 certified line-mass budget
                          |
                          +--> X-13203 exact budget replay
```

## External objects

```text
PR #132   canonical stacked contribution
Issue #131 directed positive-anchor computation ledger
PR #135   PA-1 trigger
Issue #137 line-mass budget computation ledger
```

## Control fingerprints

```text
X-13201 positive control
0423469c646627ca5d9c5c2d21bf67638c3e7f36cf8f350b5b92d0aedd2cb196

X-13201 negative control
3e9234290746c786f22522d0577ac76d4f85c7d4591d7b7156d8dd2d9552d6dc

X-13203 strict synthetic contradiction
19a9978824d8bdfb9f6dc6287439e097fe6c7529ab7e39e5ed37cb607d543f60

X-13203 consistent synthetic control
366218ce7d65eb825d7d69e3a3f52ca17ab987f853ddd040d5239b8dbdc531d0
```

## Promotion boundary

- No temporary `121xx` claim from this branch is valid after this migration.
- No Riemann-data negative or line-mass reversal is claimed.
- No `Z-####` identifier is allocated.
- Trigger PR #135 remains result-pending.

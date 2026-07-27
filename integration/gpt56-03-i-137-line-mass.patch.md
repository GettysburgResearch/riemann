# Integration patch — positive-anchor directed and line-mass extensions

This append-only file supplements
`integration/gpt56-03-i-93-positive-anchor-ladder.patch.md`.

## Additional claim registration

| ID | Kind | Title | Status | Dependencies |
|---|---|---|---|---|
| `L-12103` | lemma | Certified line-mass budgets for multi-anchor response ladders | `PROPOSED` | L-9308, L-12102, proof-grade surviving zero bins |

## Additional experiment registrations

| ID | Path | Classification |
|---|---|---|
| `X-12102` | `experiments/X-12102-directed-positive-anchor/` | proof-producing directed PA-1 workflow; result pending |
| `X-12103` | `experiments/X-12103-anchor-line-mass-budget/` | exact finite rational line-mass checker and synthetic controls |

## New issue and trigger

```text
Issue #131  directed positive-anchor ladder
PR #135     directed PA-1 trigger at w=1
Issue #137  line-mass budgets for positive near-null responses
```

## Exact control fingerprints

```text
X-12103 strict synthetic contradiction
19a9978824d8bdfb9f6dc6287439e097fe6c7529ab7e39e5ed37cb607d543f60

X-12103 consistent synthetic control
366218ce7d65eb825d7d69e3a3f52ca17ab987f853ddd040d5239b8dbdc531d0
```

## Candidate-priority correction from concurrent work

Independent PR #134 reports the scale-free one-anchor finalist

```text
x=1/20, w=1/400,
relative lower-wall position ~0.0018744703.
```

Independent PRs #124/#128 nominate

```text
x=2, w=4, Re(s)=5/2
```

for an easy-half-plane independent backend.

The recommended computation order is therefore:

1. finish already-triggered PA-1 at `w=1` as a theorem regression;
2. run `w=1/400` as the strongest scale-free single-anchor finalist;
3. run `w=4` with two distinct completed-xi backends;
4. validate PA-3 multi-anchor recurrence and source overlap;
5. apply L-12103 line-mass budgets to frozen PA-3 directions;
6. escalate PA-7 only after the no-double-counting source ledger is complete.

## Dependency graph

```text
old directed degree-14 moments
        + one new directed anchor
        -> L-12101 / X-12102 PA-1 decision

several directed one-anchor scalars
        -> L-12102 multi-anchor moments
        -> frozen PA-3 / PA-7 rational directions

frozen response + surviving certified zero bins
        -> L-12103 / X-12103 line-mass budget
        -> strict positive or negative contradiction
```

## Promotion boundary

- No directed PA-1 output is retained yet.
- No Riemann-data line-mass budget exists.
- Every zero-bin lower contribution must survive the same source measure used by
  the total response.
- Global count lower bounds without location cannot enter X-12103.
- A strict reversal still requires independent completed-xi and zero-bin
  reproduction plus review of all inherited analytic implications.

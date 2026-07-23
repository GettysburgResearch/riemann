# Integration patch — `gpt56-05-b` / Issue #35

This file is an integrator-ready patch description. It does not directly edit
concurrent root registries.

## CLAIMS.md additions

| Claim | Title | Status | Dependencies | Primary file |
|---|---|---|---|---|
| `L-3501` | Canonical Robin tails are nested prefix-level sequences | `PROPOSED` | `T-2002`, `L-2502` | `claims/lemmas/L-3501-canonical-tail-level-encoding.md` |
| `L-3502` | Exact powered Lagrange envelope for a shared Robin tail budget | `PROPOSED` | `L-3501`, `L-2502` | `claims/lemmas/L-3502-exact-powered-lagrange-tail-envelope.md` |
| `X-3501` | Standard-library exact powered-envelope producer/checker | exact regression prototype | `L-3501`, `L-3502` | `experiments/X-3501-powered-robin-envelope/README.md` |

## OPEN_PROBLEMS.md update for Issue #35

Suggested status text:

> `PARTIAL`: `L-3501` gives an exact nested prefix-level encoding of every
> canonical tail. `L-3502` gives a shared-budget rational-power envelope whose
> dynamic program enforces every nonincreasing exponent constraint and whose
> final comparison uses exact `d`-th powers only. X-3501 supplies a separately
> structured standard-library verifier and a strict-improvement regression.
> The remaining task is production integration with X-2501 and regeneration of
> a certified region beyond `10^54`.

## CURRENT_STATE.md suggested addition

Under the Robin route:

- X-2501 currently certifies the complete canonical region through `10^54` on
  draft PR #34.
- `L-3502` now supplies a proof-producing joint tail ceiling that spends the
  remaining product budget once rather than independently at every tail prime.
- The envelope uses exact rational arithmetic after raising to a chosen integer
  power `d`; no logarithm or root enters the verifier.
- A synthetic exact regression is strictly tighter than `L-2502`, but no larger
  production Robin region has yet been regenerated.

## NEGATIVE_RESULTS.md

No negative RH result should be added. The branch found no Robin violation and
makes no statement about integers beyond the existing X-2501 certified region.

## Experiment registry

Add:

```text
X-3501 — exact powered shared-budget Robin tail envelope
status: exact optimizer regression; production integration pending
schema: riemann.robin-powered-tail.v1
tests: 6 passing
counterexample status: none
```

## Merge order

This branch is stacked on draft PR #34 and expects the following logical order:

1. PR #24 (`T-2002`, canonical completeness and finite arithmetic barrier);
2. PR #34 (`L-2502`, X-2501 finite canonical search);
3. this branch (`L-3501`, `L-3502`, X-3501).

If root registries are integrated before all stacked branches merge, preserve
claim statuses and draft dependency labels exactly.

## Review targets

1. Prove the level encoding and its inverse without trusting the implementation.
2. Audit the exact floor `M0=floor(floor(B/P)/R)`.
3. Reconstruct the powered inequality
   `J^d <= M0^a V` and every strictness direction.
4. Confirm the DP recurrence enforces `ell_{r+1}<=ell_r` rather than maximizing
   independent levels.
5. Compare the synthetic regression by exact cross multiplication.
6. Mutate a claimed numerator and confirm the checker rejects it.

## Counterexample boundary

No `Z-####` identifier is allocated. The rational target in the committed
regression is synthetic and is not a Robin transcendental enclosure.
## Purpose

Reconstruct and strengthen the vanished score-free Hall / native-dual research
reset as an add-only successor to frozen PR #499 at `99d3983b57f82941131caa8d9c36e4947f1179a0`.

**RH remains unproved.** This is an archival reconstruction of a proposed
score-free Hall repair, not an accepted proof and not a current complete
candidate.

## Reconciliation with the live frontier

The source packet originally reused the already-occupied `T/L/R/M/O-94020`
namespace. It has therefore been mechanically re-IDed as `T-98800` through
`L-98805`; the original ZIP and mapping are recorded in the namespace lock.

The exact score-edge refutation was already recorded by PR #501. This
reconstruction preserves a useful two-sort repair of PR #499, but it does
**not** supersede PR #521 or the later factor-67 source-faithfulness/no-go
frontiers. In particular, `L-98802` does not construct PR #521's live
endpoint/native common parent (`JNTLC`) or prove that the inherited quantizer
simultaneously transports the row bonus, source colours, and child capacities.
`L-98804` does not derive the asserted constant `60989` native-cost ledger for
that live object. These interfaces remain open; the inherited Mellin–Landau
conclusion is conditional on them. The exact replay below checks finite algebra
and type firewalls only.

## Decisive type repair

PR #499 correctly proved compact target Hall and nonnegative component-row Hall
bonuses, but incorrectly promoted every Hall edge to a complete positive packet
with its own exact declared score.  At `x=2` that edge score is strictly
negative.

This branch instead uses

```text
source sort: positive Hall residual, with target and declared score;
row sort:    target-free, score-free, nonnegative Hall bonus.
```

The row sort is never recursively copied and is evaluated only through the
final physical row and the exact native `Y_4` dual.

## Proposed conclusion-producing chain

```text
compact factor-67 target Hall
 -> positive residual source + score-free positive row bonus
 -> causal split of residual source only
 -> actual child target mass < 1/8
 -> positive endpoint integration
 -> omissions before one label-blind quantizer
 -> one current row + full reserved child capacities
 -> all q/4q columns, including q<K
 -> nonnegative native detail slack
 -> direct Y_4 price < 60989 per unit packet
 -> Lambda(X) <= 60989 + (1/8)Lambda(X/67+1)
 -> O(1) native deficit
 -> one-sided endpoint / prime-square / Mellin-Landau consumer
 -> RH candidate.
```

## No-RH-input boundary

The candidate does not assume RH/GRH, CPBD, a power-saving PNT error,
square-root Mertens cancellation, a generic large-sieve alignment estimate, or
`J_Lambda(X)-4sqrt(X)=O(log X)`.

## Exact replay

```bash
cd experiments/X-98800-score-free-hall-native-dual
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_SCORE_FREE_HALL_NATIVE_DUAL_CANDIDATE_ALGEBRA
```

The replay authenticates finite algebra, type firewalls, ownership mutations,
all-column constants, the native-slack cocycle, and dependency metadata.  It
does not rerun the inherited Hall, interval, quantizer, terminal, or
Mellin-Landau campaigns and explicitly records `rh_established=false`.

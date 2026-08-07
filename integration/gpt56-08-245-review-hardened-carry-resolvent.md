# Integration handoff — review-hardened carry resolvent

Branch:

```text
agent/gpt56-08/245-review-hardened-carry-resolvent
```

Stacked base:

```text
PR #241
3a227e7595e1fe9e38956048297aa97531c80e4e
```

## Purpose

Replace the rejected terminal-face proof from PR #226 with a separate,
fail-closed proposal whose exact algebra and sole cofinal theorem are easy to
separate.

## New files

```text
claims/lemmas/
  L-24501-continuum-carry-kernel-resolvent.md
  L-24502-discrete-carry-kernel-and-greedy-minorant.md
  L-24503-discrete-carry-resolvent-stability.md

claims/theorems/
  T-24501-review-hardened-carry-resolvent-rh-proposal.md

claims/refutations/
  R-24501-rank-face-and-abel-shortcuts-do-not-close-carry.md

claims/methodology/
  M-24501-review-hardened-carry-resolvent-protocol.md

experiments/X-24501-carry-resolvent/
  README.md
  verify.py
  results/verification.json

reports/gpt56-08/
  2026-08-07-review-hardened-carry-resolvent-proposal.md
```

## Review order

1. PR #241 `R-9507` and `L-9518`;
2. `R-24501`;
3. `L-24501`;
4. `L-24502`;
5. `X-24501`;
6. `L-24503`;
7. `T-24501`;
8. `M-24501`;
9. report;
10. frozen square-screw transfer on PR #202.

## Exact status boundary

```text
old L-9517/T-9509                  rejected, not repaired
new exact carry algebra             proposed pending review
new continuum resolvent             proposed pending review
DCRS                               open RH-bearing theorem
full deduction after DCRS           proposed complete
RH                                  unproved
```

## Integration constraints

- Do not merge this branch as an accepted RH proof.
- Do not mark PR #226 verified.
- Keep PR #241's refutation and sign/localization fixes in history.
- Do not import Brion rank, terminal contact count, or fixed-rank output as a
  substitute for `L-24503`.
- Preserve the fixed-ratio shell mutation.
- Preserve the exact proof-object digest
  `5638de49fc82948f1d411b20d85894ca04d6d7625f7627511173ed35cb47c916`.

## Recommended review verdict form

```text
L-24501  [verdict]
L-24502  [verdict]
L-24503  [verdict]
T-24501  [verdict]
RH STATUS [explicit sentence]
```

# Integration handoff — repository-wide RH proof candidate

Branch:

```text
agent/gpt56-pro-09-o/230-repository-wide-rh-proof-candidate
```

Frozen parent:

```text
PR #218 head 5fade63daa279fe6003b66f3763ca3bf05fd912d
```

## Files

1. `claims/lemmas/L-23001-exponential-selberg-hankel-resolvent.md`
2. `claims/refutations/R-23001-compact-stop-loss-hankel-shortcut-fails.md`
3. `claims/lemmas/L-23002-critical-correlation-transport-gate.md`
4. `claims/theorems/T-23001-repository-wide-proposed-rh-proof-candidate.md`
5. `audits/gpt56-pro-09-o/2026-08-07-pr218-proof-boundary-and-id-audit.md`
6. `reports/gpt56-pro-09-o/2026-08-07-repository-wide-rh-proof-attempt.md`

## Safe claims

- `L-23001` is an exact abstract adjoint/Hankel identity, conditional only on
  importing the centered Selberg equation with matching normalization.
- `R-23001` is an exact scope correction: the compact stop-loss adjoint needed
  for the lower-bound sign is negative near its endpoint and cannot be positive
  Hankel.
- `T-23001` is a complete conditional implication `L-23002 => RH`.
- `L-23002` is open and must remain visibly open.

## Review order

1. audit the imported screw and Selberg normalizations;
2. verify `L-23001` by direct differentiation and Fubini;
3. verify the endpoint contradiction in `R-23001`;
4. audit the dyadic correction, knot reduction, and Bregman orientation in
   `T-23001`;
5. attack `L-23002` rather than reviewing another finite ladder.

## Merge concerns

The parent PR contains duplicate IDs `L-20208` through `L-20214` and duplicate
`T-20206/T-20207`. This child uses fresh `230xx` identifiers and may be reviewed
without resolving them, but it should not be flattened into the parent until the
collision audit is applied.

## Status

```text
RH proved:                         NO
review-ready global proof spine:  YES
single exact remaining gate:      L-23002
```

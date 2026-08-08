# Integration handoff — final WSTS consolidation

**Agent:** `gpt56-pro`  
**Date:** 2026-08-08  
**Branch:** `research/gpt56-pro-275-final-wsts-consolidation`  
**Base:** PR #240 at `58c70a81dce76cd84ea50a60c15c227537f240c1`

## Result

The live elementary carry programme has been reduced to one canonical finite
scalar:

```text
WSTS = subpower maximum logarithmically weighted dyadic shell-tail charge.
```

New `L-27501` proves

```text
RH -> WSTS with O(log^4 X).
```

Inherited `T-23811` proves

```text
WSTS -> prime ramp -> RH.
```

Therefore `T-27501` records

```text
WSTS <=> RH.
```

This is a status-closing equivalence, not an unconditional proof of WSTS.

## Files

```text
claims/lemmas/L-27501-shell-profile-size-and-rh-sampling-bound.md
claims/theorems/T-27501-weighted-shell-tail-stability-rh-equivalence.md
claims/observations/O-27501-final-carry-route-consolidation.md
claims/methodology/M-27501-final-weighted-shell-tail-review-protocol.md
reports/gpt56-pro/2026-08-08-final-weighted-shell-tail-consolidation.md
audits/gpt56-pro/2026-08-08-final-carry-route-status.tsv
experiments/X-27501-wsts-consolidation/
```

## Canonical review order

1. `L-23823`;
2. `L-23825`;
3. `L-23824` and `L-23826`;
4. `L-27501`;
5. `T-27501`;
6. `M-27501`;
7. exact regression `X-27501`;
8. the full report;
9. the source-pinned square-screw/Landau consumer.

## Dependency policy

The final proof spine does not import the open conclusions named

```text
ESBT/ESGS, PTQ/PTC, DGB(5), F5TC, FAGD, ADF, PGC, or BJD.
```

Those branches remain available as possible proof mechanisms for WSTS or an
equivalent scalar.

## Integration recommendation

Do not merge this packet as a proof of RH.  It is suitable for immediate
adversarial review as the canonical final reduction and repository status
record.

A future unconditional WSTS proof should be stacked directly on this branch and
must emit the complete weighted shell-tail ledger described in `M-27501`.
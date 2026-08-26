# Hostile self-reconstruction of the quarter-power Boolean proposal

Date: 2026-08-26  
PR: #719  
Historical landing: `e56c9813`  
Live reconstruction target: `8eea03836b23154a0990a4a870aa5bb3ecb7510d` plus this correction sequence  
RH status: **unproved**

## Executive verdict

The proposal's support insight is correct, but its conclusion does not survive
end-to-end reconstruction.

```text
quarter-power balanced support              VERIFIED EMPTY
fixed-owner/core Type-I endpoint             VERIFIED SUBPOWER
arbitrary-cutoff Boolean identity            VERIFIED EXACT
cutoff-transfer algebra                      VERIFIED EXACT
coherent owner-product Type-I collapse       UNPROVEN / GAP
BCI102990                                    OPEN / RH-BEARING
historical T-103080 complete theorem          SUPERSEDED
RH                                            UNPROVED
```

## First broken arrow

The proof bounded the core Type-I lattice in each fixed owner fibre and then
used only same-occurrence pair multiplicity plus the number of dyadic owner
blocks to infer a bound for the coherent physical sum over distinct owner
products.

That inference is invalid. Same-occurrence multiplicity does not control
cross-product near collisions. The fixed-owner theorem and the coherent
physical restriction are different operator statements.

## Exact reason the shortcut cannot be repaired by wording

At the quarter-power cutoff the balanced term is zero. Therefore the complete
pair-indexed Type-I field is exactly the harmonic/BCI field modulo already
closed packets. Proving its subpower negative mass would prove the original
RH-bearing criterion; it is not inherited from the old Type-I estimate.

The quarter-power construction remains valuable because it converts the final
problem into a particularly sharp coordinate:

```text
QPTI103112:
  coherent physical restriction of block-dependent quarter-power Type-I
  lifts.
```

But `QPTI103112` is equivalent to `BCI102990`, not a proof of it.

## PR #756 comparison

PR #756 independently enforces the same source-order lesson. Its corrected
physical-squareclass adapter requires:

```text
retain P*c^2 and Q*d^2;
correlate distinct fibres before squaring;
use a genuine hard physical restriction for leverage;
keep varying-conductor signed recombination;
control the Wick residual;
isolate the principal member.
```

Those requirements identify exactly what the quarter-power shortcut omitted:
the cross-owner physical restriction. PR #756 supplies useful mechanism design
and exact finite/function-field models, but no theorem currently proves
`QPTI103112`, `BCI102990`, or the principal zeta-member estimate.

## Integration action

- retain `L-103111` as an exact support theorem;
- retain `L-103110` only at fixed-owner/orthogonal-fibre scope;
- treat historical `L-103070.6`, `L-103072.5--.7`, and `T-103080` as
  superseded;
- use `T-103110` as the live quarter-power frontier;
- use the disambiguation TSV before importing any `103070/103071/103080`
  identifier.

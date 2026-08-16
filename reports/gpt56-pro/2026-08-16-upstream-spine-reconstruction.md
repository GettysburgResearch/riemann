# Upstream-spine reconstruction after PR #494

This packet freezes PR #494's accepted one-shot closing implementation and
rebuilds the arithmetic/analytic source-to-endpoint spine.

## New architecture

```text
native finite Möbius datum
  -> exact anchored/bulk/defect split
  -> rank-one positive bulk source
  + directed Target-Lorenz anchored source
  -> block-diagonal whole-cell quantizer
  -> direct all-column and terminal feasibility
  -> native Y4 deficit <61000
  -> prime-square occupancy moat
  -> Mellin/Landau exclusion
  -> RH proposal.
```

## Principal repairs

- shared ancestry is not counted as confirmation;
- bulk Hall/profile monotonicity is removed;
- Target-Lorenz is restricted to the anchored sector;
- rows above 66 are handled by the explicit global frontier theorem;
- the signed quadrature defect is never called a source packet;
- all physical columns, including `q<K`, are derived;
- the prime-square and Mellin/Landau implication is written out one-way;
- no RH contour shift is used.

## Status

This is a full candidate proof packet under project terminology and remains
unproved pending hostile independent reconstruction.

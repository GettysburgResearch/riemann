# Reviewer B narrow adjudication of C statement shape

Verdict: `APPROVED_STATEMENT_SHAPE_REPAIR`.

The review scope was limited to these two revised conclusions:

```lean
theorem actualXiInputs_have_concrete_dependencies
    (inputs : ActualXiOrderThreeInputs) :
    SourceLockExact inputs.verified.sourceLock ∧
      CriticalMultiplicityResidual inputs.grouped.selectedReserve ∧
      Nonempty (ActualXiReserveAllocation inputs.grouped) ∧
      RegroupedActualXiC2Approximation inputs.grouped inputs.reserve
```

```lean
theorem buildLockedActualXiReserveAllocation
    {grouped : GroupedActualXiC2Expansion}
    (verified : PublishedVerifiedHeightTheorem)
    (inputs : ReserveTailInputs grouped) :
    SourceLockExact verified.sourceLock ∧
      Nonempty (ActualXiReserveAllocation grouped)
```

`ActualXiReserveAllocation grouped` is data in `Type`, so it cannot itself be
an operand of `And`. `Nonempty` is the proposition-level existence wrapper for
the already-carried or already-constructed data. The witnesses are respectively
`inputs.reserve` and `buildActualXiReserveAllocation inputs`.

The repair adds no hypothesis, introduces no axiom, and does not change the
actual-Xi order-three comparator statement or its PSD-only conclusion. The
data-producing API remains available separately.

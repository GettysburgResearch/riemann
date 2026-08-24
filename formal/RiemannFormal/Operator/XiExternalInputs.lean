import ChallengeDeps.XiPickOrderThreeConditional

namespace RiemannFormal.Operator

open ChallengeDeps.XiPickOrderThreeConditional

/-- The bibliographic/artifact lock is an exact data equality, independently
of the repository claim-file SHA. -/
theorem plattTrudgian_source_lock_exact :
    SourceLockExact plattTrudgianSourceLock := rfl

/-- The verified-height theorem carries its own exact external source lock. -/
theorem publishedVerifiedHeight_source_locked
    (h : PublishedVerifiedHeightTheorem) :
    SourceLockExact h.sourceLock :=
  h.sourceLockExact

/-- Exact multiplicity bookkeeping for the selected critical reserve: one
coefficient unit is consumed by the reserve and the remaining
`(m₀ - 1) R₀` stays in the grouped Xi expansion. -/
theorem criticalMultiplicityResidual_exact
    (reserve : SelectedCriticalReserve) :
    CriticalMultiplicityResidual reserve := by
  intro t
  ext <;>
    simp [CriticalMultiplicityResidual, criticalOrbitJet, criticalUnitJet,
      jetAdd, jetScale] <;>
    ring

/-- Every repaired headline input exposes the precise finite-height theorem,
grouped actual-Xi expansion, multiplicity residual, and one-use reserve ledger.
This theorem is used by QA to reject an inert proposition bundle. -/
theorem actualXiInputs_have_concrete_dependencies
    (inputs : ActualXiOrderThreeInputs) :
    SourceLockExact inputs.verified.sourceLock ∧
      CriticalMultiplicityResidual inputs.grouped.selectedReserve ∧
      ActualXiReserveAllocation inputs.grouped ∧
      RegroupedActualXiC2Approximation inputs.grouped inputs.reserve :=
  ⟨inputs.verified.sourceLockExact, inputs.residual, inputs.reserve,
    inputs.paidC2Approximation⟩

end RiemannFormal.Operator

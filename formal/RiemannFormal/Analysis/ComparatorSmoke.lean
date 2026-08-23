import Solution.MellinAPI

namespace RiemannFormal.Analysis

/-- Build-time witness that the owned Mathlib-only comparator solution elaborates inside the
pinned package graph. -/
theorem mellinAPIComparator_builds : Comparator.MellinAPI.ChallengeStatement :=
  Comparator.MellinAPI.fixedMellinConsumerSolution

#print axioms mellinAPIComparator_builds

end RiemannFormal.Analysis

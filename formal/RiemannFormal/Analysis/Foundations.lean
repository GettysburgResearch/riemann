import Mathlib.Analysis.MellinTransform
import RiemannFormal.Upstream.Zeta23Bridge

namespace RiemannFormal.Analysis

abbrev Detector := ℝ → ℝ

/-- A detector together with its stable scientific semantic identifier.
No analytic property is asserted by this structure. -/
structure FixedDetector where
  semanticId : String
  value : Detector

end RiemannFormal.Analysis

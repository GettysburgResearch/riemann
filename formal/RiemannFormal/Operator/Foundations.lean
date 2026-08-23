import Mathlib.Data.Matrix.Basic
import RiemannFormal.Statement.OpenCuts

namespace RiemannFormal.Operator

/-- Metadata for a finite packet; no positivity statement is asserted here. -/
structure FinitePacket where
  semanticId : String
  size : Nat

end RiemannFormal.Operator

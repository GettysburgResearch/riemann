import Mathlib.NumberTheory.ArithmeticFunction.Moebius
import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt
import RiemannFormal.Statement.OpenCuts

namespace RiemannFormal.Arithmetic

inductive SourceRole where
  | nativeSource
  | auxiliaryPositiveSource
  | signedObservation
  | childResponse
  | childCapacity
  deriving DecidableEq, Repr

/-- A typed arithmetic coefficient family. The role is kept explicit so that
historically false source promotions cannot be hidden by notation. -/
structure TypedSource where
  role : SourceRole
  coefficient : ℕ → ℝ

end RiemannFormal.Arithmetic

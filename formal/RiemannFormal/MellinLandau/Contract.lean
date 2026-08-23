import RiemannFormal.Analysis.Foundations
import RiemannFormal.Arithmetic.Foundations
import RiemannFormal.Statement.OpenCuts

namespace RiemannFormal.MellinLandau

/-- Metadata connecting an analytic fixed detector to the explicit open cut that a
producer must discharge. This structure proves no analytic implication. -/
structure ConsumerContract where
  detector : RiemannFormal.Analysis.FixedDetector
  openCut : RiemannFormal.OpenCut

/-- Arithmetic counterpart of the fixed-detector contract. -/
structure ArithmeticConsumerContract where
  detector : RiemannFormal.Arithmetic.FixedArithmeticDetector ℝ
  openCut : RiemannFormal.OpenCut

end RiemannFormal.MellinLandau

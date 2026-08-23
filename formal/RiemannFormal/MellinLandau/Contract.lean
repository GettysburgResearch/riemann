import RiemannFormal.Analysis.Foundations
import RiemannFormal.Statement.OpenCuts

namespace RiemannFormal.MellinLandau

/-- Metadata connecting a fixed detector to the explicit open cut that a
producer must discharge. This structure proves no analytic implication. -/
structure ConsumerContract where
  detector : RiemannFormal.Analysis.FixedDetector
  openCut : RiemannFormal.OpenCut

end RiemannFormal.MellinLandau

import RiemannFormal.Statement.ScientificStatus

namespace RiemannFormal

/-- Stable identifiers for the first formalization release's principal open cuts.
This is metadata, not an assertion that any cut holds. -/
inductive OpenCut where
  | rows23Native
  | fiveThreeNegativeMass
  | fixedDetectorNegativeMass
  | criticalVariation
  | crossCoreDispersion
  | halfDivisorNearCollision
  | physicalOccupancy
  | xiPickOrderFour
  deriving DecidableEq, Repr

def OpenCut.semanticId : OpenCut → String
  | .rows23Native => "OPEN.ARITH.ROWS23_NATIVE"
  | .fiveThreeNegativeMass => "OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS"
  | .fixedDetectorNegativeMass => "OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS"
  | .criticalVariation => "OPEN.ARITH.CV"
  | .crossCoreDispersion => "OPEN.ARITH.XD"
  | .halfDivisorNearCollision => "OPEN.ARITH.HCNC"
  | .physicalOccupancy => "OPEN.ARITH.BPOE"
  | .xiPickOrderFour => "OPEN.OPERATOR.XI.PICK_ORDER4_PLUS"

def OpenCut.description : OpenCut → String
  | .rows23Native => "Literal native fixed rows 2 and 3 satisfy the required one-sided estimate."
  | .fiveThreeNegativeMass => "The fixed 5:3 scalar has subpower logarithmic negative mass."
  | .fixedDetectorNegativeMass => "One fixed zero-safe native detector has subpower negative mass."
  | .criticalVariation => "Critical one-sided weighted variation is subpower."
  | .crossCoreDispersion => "Same-kernel signed cross-core dispersion is subpower."
  | .halfDivisorNearCollision => "The oriented half-divisor near-collision is subpower."
  | .physicalOccupancy => "Physical occupancy preserves the source/phase energy at subpower cost."
  | .xiPickOrderFour => "Actual-Xi Pick positivity holds at order four and above."

end RiemannFormal

import ChallengeDeps.FixedDetectorFiveThree
import RiemannFormal.Arithmetic.FixedRows

namespace Solution.FixedDetectorFiveThree

open ChallengeDeps.FixedDetectorFiveThree

theorem solution : Statement := by
  intro a b ha
  simpa [ChallengeDeps.FixedDetectorFiveThree.fiveThreeNumerator,
    ChallengeDeps.FixedDetectorFiveThree.row2Numerator,
    ChallengeDeps.FixedDetectorFiveThree.row3ScaledNumerator,
    RiemannFormal.Arithmetic.FixedRows.fiveThreeNumerator,
    RiemannFormal.Arithmetic.FixedRows.row2Numerator,
    RiemannFormal.Arithmetic.FixedRows.row3ScaledNumerator] using
    (RiemannFormal.Arithmetic.FixedRows.fiveThree_nonzero (a := a) (b := b) ha)

end Solution.FixedDetectorFiveThree

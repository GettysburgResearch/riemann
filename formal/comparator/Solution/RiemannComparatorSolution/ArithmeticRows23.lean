import RiemannComparatorChallengeDeps.ArithmeticRows23
import RiemannFormal.Arithmetic.FixedRows

namespace Solution.ArithmeticRows23

open ChallengeDeps.ArithmeticRows23

theorem solution : Statement := by
  intro a b ha
  simpa [ChallengeDeps.ArithmeticRows23.row2Numerator,
    ChallengeDeps.ArithmeticRows23.row3ScaledNumerator,
    RiemannFormal.Arithmetic.FixedRows.row2Numerator,
    RiemannFormal.Arithmetic.FixedRows.row3ScaledNumerator] using
    (RiemannFormal.Arithmetic.FixedRows.rows23_no_common_zero (a := a) (b := b) ha)

end Solution.ArithmeticRows23

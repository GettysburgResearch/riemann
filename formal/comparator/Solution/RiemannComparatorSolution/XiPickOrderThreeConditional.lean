import RiemannComparatorChallengeDeps.XiPickOrderThreeConditional
import RiemannFormal.Operator.XiOrderThree

open ChallengeDeps.XiPickOrderThreeConditional

/-- Sorry-free implementation of the exact shared challenge statement. -/
theorem XiPickOrderThreeConditional_psd : ChallengeStatement :=
  RiemannFormal.Operator.actualXiPickOrderThreeConditional

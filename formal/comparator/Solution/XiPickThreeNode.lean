import ChallengeDeps.XiPickThreeNode
import RiemannFormal.Operator.PickAlgebra

open ChallengeDeps.XiPickThreeNode

/-- Sorry-free solution of the trusted three-node determinant challenge. -/
theorem XiPickThreeNode_identity
    {x1 x2 x3 p1 p2 p3 : ℝ}
    (h12 : x1 + x2 ≠ 0) (h13 : x1 + x3 ≠ 0) (h23 : x2 + x3 ≠ 0)
    (ht12 : x1 ^ 2 ≠ x2 ^ 2) (ht13 : x1 ^ 2 ≠ x3 ^ 2)
    (ht23 : x2 ^ 2 ≠ x3 ^ 2)
    (hp1 : p1 ≠ 0) (hp2 : p2 ≠ 0) (hp3 : p3 ≠ 0) :
    pickDet3 x1 x2 x3 p1 p2 p3 =
      (p1 * p2 * p3 * delta3 (x1 ^ 2) (x2 ^ 2) (x3 ^ 2) ^ 2 /
        denominator x1 x2 x3) *
      secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
        (1 / p1) (1 / p2) (1 / p3) *
      secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
        (x1 ^ 2 * p1) (x2 ^ 2 * p2) (x3 ^ 2 * p3) := by
  simpa [ChallengeDeps.XiPickThreeNode.pickDet3,
    ChallengeDeps.XiPickThreeNode.det3,
    ChallengeDeps.XiPickThreeNode.pickEntry,
    ChallengeDeps.XiPickThreeNode.delta3,
    ChallengeDeps.XiPickThreeNode.secondDivDiff,
    ChallengeDeps.XiPickThreeNode.denominator,
    RiemannFormal.Operator.pickDet3,
    RiemannFormal.Operator.det3,
    RiemannFormal.Operator.pickEntry,
    RiemannFormal.Operator.delta3,
    RiemannFormal.Operator.secondDivDiff,
    RiemannFormal.Operator.pickDenominator3] using
      (RiemannFormal.Operator.three_node_pick_determinant_identity
        h12 h13 h23 ht12 ht13 ht23 hp1 hp2 hp3)

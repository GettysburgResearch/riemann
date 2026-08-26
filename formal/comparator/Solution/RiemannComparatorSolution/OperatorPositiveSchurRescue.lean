import RiemannComparatorChallengeDeps.OperatorPositiveSchurRescue
import RiemannFormal.Refutations.MatrixFirewalls

/-- Sorry-free solution of the positive-Schur-rescue firewall. -/
theorem OperatorPositiveSchurRescue_firewall
    {b z c : ℝ} (hb : b < 0) (hc : 0 < c) :
    b - z ^ 2 / c < 0 :=
  RiemannFormal.Refutations.positiveSchurCannotRescue hb hc

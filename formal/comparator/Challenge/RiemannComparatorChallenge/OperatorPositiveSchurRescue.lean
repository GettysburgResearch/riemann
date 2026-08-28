import RiemannComparatorChallengeDeps.OperatorPositiveSchurRescue

/-- Trusted challenge: a positive Schur correction cannot rescue an already
negative visible direction. -/
theorem OperatorPositiveSchurRescue_firewall
    {b z c : ℝ} (hb : b < 0) (hc : 0 < c) :
    b - z ^ 2 / c < 0 := by
  sorry

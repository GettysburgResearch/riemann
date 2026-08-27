import RiemannFormal.Operator.HeatQ4Finite

namespace RiemannFormal.Refutations

/-- Finite parity expectation used as a kernel-checkable Weyl/displacement
firewall. -/
def parityForm (x y : ℝ) : ℝ := x ^ 2 - y ^ 2

/-- Translation/displacement can change the sign of parity.  This is a finite
fixture only; it is not promoted to the full analytic uniform-center no-go. -/
theorem parityChangesUnderDisplacement :
    0 < parityForm 1 0 ∧ parityForm 1 2 < 0 := by
  norm_num [parityForm]

/-- A finite Q4 filter can have positive total coefficient energy while taking
a negative value on an exact packet. -/
theorem q4FiniteFilterSignFixture :
    (1 : ℝ) ^ 2 + (-2 : ℝ) ^ 2 + (1 : ℝ) ^ 2 = 6 ∧
      RiemannFormal.Operator.q4Filter2 0 1 0 = -2 := by
  norm_num [RiemannFormal.Operator.q4Filter2]

end RiemannFormal.Refutations

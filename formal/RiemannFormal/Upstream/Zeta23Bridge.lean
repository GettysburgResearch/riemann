import Zeta23.Statement
import RiemannFormal.Upstream.MathlibBridge
import RiemannFormal.Upstream.SourceLocks

namespace RiemannFormal.Upstream

/-- Importing Zeta23 does not change the project's RH proposition. -/
theorem zeta23_bridge_preserves_RH : RiemannFormal.RH ↔ RiemannHypothesis := Iff.rfl

end RiemannFormal.Upstream

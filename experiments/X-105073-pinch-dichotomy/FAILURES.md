# A1 FAILURES — refuted routes (each is a deliverable)

F-A1-1 (Direction 1 full closure: DEAD, with proof). Goal: push the self-consistency
ceiling below the (FAR-WIN)/form-(b) target 0.2122|c_B|^2, making T-105070 interface-free.
Optimization achieved: 5.8284|c_B|^2 -> C(eps) = (1+sqrt(1-eps/c_0'))^2 |c_B|^2 <= 4|c_B|^2
(conjugate-window halving + expand-the-square instead of triangle; A1.3). But C(eps) >=
|c_B|^2 > 0.2122|c_B|^2 for EVERY eps in (0, c_0'], and Theorem A1.6's theta-family ATTAINS
C(eps): no norm-inequality refinement can go lower. The 27.5x gap was 6.9x bookkeeping
slack and 4x irreducible structure. Route closed permanently at this altitude.

F-A1-2 (line-budget attack on the forced coherent component: DEAD, two ways).
(i) Structural: the strongest conceivable form of the cost inequality — coherent amplitude
a costs (2a^2/pi)log(1/h) against sharp-F1 budget (sqrt((3/2)A') + sqrt(2/pi)|c_B|)^2
log(1/h) — reduces to a <= |c_B| + sqrt(|c_B|^2 - (3pi/4)eps), IDENTICAL to the window
ceiling already known from A1.3. Zero new information. Worse: the extremal counter-model
(theta = -sqrt(1-eps/c_0')) saturates sharp-F1 with EQUALITY (machine-checked to 1e-31,
a1_verify.py), so no sharpening of F1's constant can help either — the anti-phase
overshoot configuration is exactly on the F1 boundary.
(ii) Technical (moot given (i), recorded for honesty): making the window-correlation ->
line-mass octave transfer rigorous hits a leakage term: extending <u_h, F>_{L2(WIN)} to
the full line costs ||FT[sqrt(x) psitil_h]||_{L2(R \ WIN)} * O(1) ~ O(sqrt(log(1/h)))
after normalization — NOT o(1). Fixable in principle through the P_w projector (F4), but
pointless: even granted for free, (i) kills the route.

F-A1-3 (second-generation pinch / bootstrap: TERMINATES, no contradiction for ANY eps).
After subtracting the forced coherent component alpha_h u_h, the re-run constraint is
|p_h + alpha_h|^2 + h||F_perp||^2 <= |c_B|^2 - (3pi/4)eps + o(1) — an UPPER bound on the
residual only; no floor is forced on F_perp, so iteration stops at depth 1, satisfiable
(F_perp = 0, alpha_h ~ -p_h). The bootstrap converges to the counter-model, not to a
contradiction — for ALL eps in (0, c_0'], not just a range. The eps = c_0' endpoint is
the psi = 0 model: the constraint set degenerates to the single point f = |alpha| = |c_B|
but remains nonempty. Task question answered: NO eps closes.

F-A1-4 (finite-h arctan corrections: NO GAIN). The exact pole window mass
p_h^2 = (2/pi)arctan(r_0/h)|c_B|^2 = |c_B|^2(1 - (2/pi)(h/r_0) + O((h/r_0)^3)) differs
from the sup-bound limit only by terms that vanish as h -> 0 at fixed r_0; every theorem
is a limsup statement, so the correction contributes o(1) and cannot move any constant.
(It DOES make A1.4(c)'s finite-h display exact, which is kept.)

F-A1-5 (boundary of the obstruction — what the counter-model does NOT rule out; honest
scope note, not a failure of a route actually run). Theorem A1.6's models satisfy the
LISTED facts: Q-budget, Plancherel, conjugate symmetry, the pole expansion with L-105072's
bounds, F1-F5, F3/F4 identities. They do NOT satisfy (and no one checked) e.g.: the full
P2.3 double-Dirichlet arithmetic structure of B_0, positivity/oscillation constraints on
Lambda* from mu/eta, cross-line rigidity (analyticity of Z_far in s linking different h),
or any zeta-side contour fact. A future closure MUST consume one of those — i.e. exactly
an interface of (FAR-WIN)/FW-beta type or a new arithmetic input. The obstruction theorem
is altitude-specific, and says the wall is real AT the norm altitude, not that [P2-FAR]
is unprovable.

F-A1-6 (script bug caught and fixed, recorded per discipline): first version of a1_opt.py
tested the feasibility constraint against B = p^2 - (3pi/4)eps instead of -(3pi/4)eps
(sign/offset slip after subtracting p^2); detected because the sampled sup exceeded the
predicted closed form by ~0.4p. Fixed; all five eps values now match the closed forms
(errors ~1e-6 = grid resolution; a1_opt_out.json).

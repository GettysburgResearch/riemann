# B2 lane — failure ledger (each entry is a refuted or abandoned route)

F1. REAL-CENTER JENSEN (the route L-105063 R-C1 recorded as stalled) — CONFIRMED
DEAD, with the mechanism isolated. Center c* on the real axis with the (L2)
endpoint floor |h'(c*)| >= (8/g^2)(1-W_sh): the pair factors give
|q_j(c*)| ~ y_j^2 vs ~ R^2 on the boundary, cost log(R/y_j) per pair, AND the
amplitude ratio contributes an independent 2 log(g/Lambda) (floor ~ 1/g^2 vs
cluster-scale max ~ M/Lambda^2). Two separate unbounded logs. No choice of real
center fixes both: any real point close enough to the cluster to have
|h'| ~ 1/y^2 (trough at x_j +- sqrt3 y_j) can be covered by another pair's
positive core in adversarial configs (core-covering: pair i with
|x_i - (x_j +- sqrt3 y_j)| < y_i, y_i ~ y_j, kills the trough floor).
Refuted 2026-08-23; replaced by the complex height center (B2.md §2).

F2. PER-y-SCALE WHITNEY TELESCOPING (the plan as tasked: dyadic scales of
y_min, Jensen per scale, telescope the logs) — UNNECESSARY for the pair
factors and INSUFFICIENT for the background. Executing the construction showed
that once the center sits at height H*Lambda, the per-pair Jensen cost is a
scale-free constant (5.813), at EVERY scale simultaneously — the dyadic ledger
collapses to a single disk (B2.md §4.1). The genuine multi-scale phenomenon
moved to the background field: the recursion that survives is in POSITION
space (window inflation until mass dominance), not in y-scale space.

F3. POLE-CENTERED JENSEN (center at z_{j_min}, immune to background
cancellation since g(z_j) = -m_j (2i y_j)^2 prod(...) is a pure product) —
DEAD: reintroduces per-pair factors |z_j - z_i| that are unbounded below
(near-coincident distinct pairs), i.e. the log returns through pair
separations instead of scales. No Cartan-type selection saves it: all m pairs
can be eps-coincident. Recorded as the complement of F1: pole centers kill the
amplitude problem but not the factor problem; height centers kill the factor
problem but not the amplitude problem — only the height center's amplitude
problem is guardable by a checkable hypothesis (DOM).

F4. CONE AT LOW HEIGHT (H = 4 first attempt): cone half-width 30 deg, budget
coefficient theta_bg = 0.0227 — fails against a uniform real-zero field: the
horizontal annulus (L, 28L) forced into S by (A1) is ~27x the core population
and partially anti-aligned; the (DOM) race lost by factor ~3.4 at every scale.
Fixed by H = 8 (annulus swallow wins by ~5.5x, B2.md §4.4) — but see F5.

F5. UNCONDITIONAL TERMINATION OF THE STOPPING RECURSION — NOT PROVED, and
believed FALSE in the abstract Hadamard class: a field whose real-zero density
grows fast enough outward (superpolynomially between consecutive octaves) can
defeat any fixed theta_bg forever. For genus-0-in-t^2 F of order <= 1 the
density is polynomially bounded on average, but a per-window proof needs a
density hypothesis. Hence the residual R-J (B2.md §5) instead of a theorem
"R-C1' is empty". The concrete blocked case: gap-scale clusters
(span ~ min(d_a, d_b)) in zero-dense neighborhoods, and shallow pairs of
weight << 1 swallowed at cost 5.813 each.

F6. 40-ITERATION SWALLOW CAP in disk_check.py is an implementation limit, not
a mathematical one; on the scanned configs the recursion terminated well
inside it (see disk_check_out.txt). Any config hitting the cap would be
reported as uncertified, not as a theorem violation.

F7. INTEGER-MULT TRANSCRIPTION of the mu = 3.4 equal-scale family: T_K != 0
was re-verified for the integer surrogates (1:3, 2:7) before use; the original
3.4-weighted profile is not an F-configuration (non-integer multiplicity), a
defect of the SOURCE example, recorded here rather than silently repaired.

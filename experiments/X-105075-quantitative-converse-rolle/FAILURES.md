# B1 FAILURES — refuted routes (each is a deliverable)

## F1. Rung-0 fixed-point closure: VACUOUS FOR EVERY ADMISSIBLE CONSTANT SET
Route: restructure master (T-105060(c)) as (1 - theta_0)(1 - kappa_0) <= tail,
theta_0 = A'_0 * C_omega/(2 c_0), and solve the fixed point.
Refutation (machine-verified, rate_check.py §2b): the deposited sharpness
certificates FORCE C_omega >= 3 (L-105064 §2 sharpness family, sup omega = 3)
and A'_0 >= 16/15 (L-105063 §3 extremal replay, extra/W = 16/15 at 40 dps);
c_0 <= 1 trivially. Hence theta_0 >= (16/15)(3/2)/1 = 8/5 > 1 ALWAYS.
Proved regime: theta_0 = 13.38 (A'=6, c0=Z23). Conjectured sharp A'=2: 4.46.
Closure needs A'_0 < 2c_0/3 = 0.4483 — unreachable by a factor >= 3.57 even at
the forced floor. Evasions tried: (a) start ladder at k=1 — rung-0 descent
still needs w_0, priced only by N_0^c (W4), self-reference unavoidable;
(b) price w_0 by rung-1 data — no deposited interface does this (W4's RHS is
rung-k's own off-line count). DEAD within the pointwise-compression method.

## F2. Master sum with A'_k = max(6, 2k): HARMONIC DIVERGENCE AT THE PUBLISHED RATE
Pinned rate (Conrey I, JNT 16 (1983) 49-74, Corollary): 1 - alpha_m = O(m^-2)
(printed final bound log F_m(1) <= m^-2; machine: m^2 log F_m(1) in [0.29, 0.53]
for 2 <= m <= 4000, increasing, ~0.524 at m = 1000). Then
sum_k 2k * (3/(2c)) * (1 - kappa_k)-majorant ~ (3C/c) log K DIVERGES (§2e).
Convergence threshold: rho > 2 in 1 - kappa_k <= C/k^rho (§2f). No published
rate beats m^-2 (searched 2026-08-23; Conrey's own F_m(1) construction is
intrinsically ~ (pi/6)/m^2 at R = 1, so his method cannot give rho > 2 without
a new mollifier family). Consequence: bound_K minimized at K=0; the ladder's
tail is USELESS with linearly growing caps. Route to revive: k-uniform
A'_k = O(k^(1-delta)) on the C-3 shallow ladder — open, and L-105063's depth-k
example (7 shallow pairs at w=0.65 forcing depth 4) shows the 2k growth is
real for the current proof, though not proved optimal.

## F3. Covering R-C1'/R-C2 by the rung-density theorem (L-105066 D3): FAILS
Hope: T-EMPTY fails only on a density-zero set of gaps; price the exceptions
by N_k(eta,T) << T^(1-eta/4) polylog. Refutation: residual clusters are made
of DEEP pairs (y_j < g/2). Typical gaps have g ~ 2pi/log T -> 0, so their deep
pairs have y_j -> 0: NEAR-REAL pairs, exactly the statistic D3 CANNOT count
(D3 requires y >= eta fixed; D5 localizes w_k AT y -> 0). The exceptional-gap
count is therefore itself the uncontrolled near-line pair count = [H3] of
T-105065. Circular; no o(1) proof possible from deposited interfaces.
Partial salvage only: clusters made entirely of y >= eta pairs need g > 2eta
and are o(N_0) by D3 — but on residual gaps NO per-gap extra bound exists to
multiply that count by (see F4), so even the rare-gap contribution is unpriced.

## F4. Bounding residual-gap extras globally by conservation: CIRCULAR
extra summed over ALL gaps <= N_{k+1}^r - N_k^r + 1 <= N_k^c - N_{k+1}^c +
A_k log T + B_k + 1 (Rolle + conservation). Feeding this back into descent (b)
yields N_k^c <= N_k^c: exactly vacuous. The count cap must be per-gap; the
defect D_res is irreducibly a hypothesis (carried in B1.md Thm Q2).

## F5. Using L-105067's 16W cluster cap to absorb R-C1: WORSENS CONSTANTS
A' = 16 on T-EMPTY clusters gives theta_0 = 3*16/(2*0.6725) = 35.7; the
residual R-C1' (T_K != 0) remains, and L-105067 Prop T-3 PROVES the 0-2-4
pointwise method cannot cross it. Import shrinks the residual set, never the
constant, and the constant is the binding blocker (F1).

## F6. Explicit all-m tail constant from Conrey: NOT AVAILABLE
The printed corollary is asymptotic (m_0 unspecified). Machine values (non-
interval mpmath.quad, dps 40) verify log F_m(1) < 0.53/m^2 for each tested m
in [2, 4000]; effectivizing Conrey's O-terms is outside deposited scope.
Sum w_k constants in B1.md carry this as the C_Conrey (= 1) transcription flag.

## F7. Beating the trivial bound with ANY constants consistent with deposits
Even discarding rung 0 entirely (illegitimate), the k=1 term alone is
(16/15)(3/(2*0.8137))(1-0.8137) = 0.3663 > 0.3275 (§2c). Nonvacuity of a
single term needs alpha_1 > 0.8301 — not in the literature. The method cannot
beat Z23's 0.3275 by ANY constant tuning; only distributional (average-omega /
near-line-repulsion [H3]) input changes this. Method-level, not constant-level.

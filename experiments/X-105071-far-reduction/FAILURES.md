# FAILURES — dead ends recorded (mandatory)
F-1. "Corner raw-mass smallness" (the R1 brief's implicit hope that Q_corner <= omega(delta)
log Y unconditionally, feeding form (a) via smooth-far decay): FALSIFIED BY THE NUMERICS
THEMSELVES — the corner field carries 71-77% of the raw mean square (far_num1: 0.707 at
Xc=2e5; lane P2: 0.77). No such lemma exists; any proof attempt was doomed. The corner field
is not small; it is spectrally displaced.
F-2. Trivial + PNT bounds on the corner field: the r~1 corner is, to leading order, a short
Mobius sum delta * sum_{d ~ sqrt y} mu(d)/sqrt(log): full PNT-strength cancellation
(M(x) << x e^{-c sqrt(log x)}) still leaves sqrt(y) e^{-c sqrt(log y)} >> y^{1/4} = the pinch
scale. The needed cancellation for even the corner's RAW boundedness is
sum_{d<=D} mu(d) d^{-2iu} partial sums of size D^{1/2+o(1)} at fixed u — RH-adjacent. Dead
as an unconditional route; only the WINDOW version matters and it needs the same input.
F-3. Montgomery-Vaughan mean value on the window: MV needs a t-average at least as long as
the log-span of the coefficients; the window has FIXED length 2 r_0 and the coefficient
log-span is unbounded (n up to e^{1/h}). The scale-average (x-average) that could replace it
IS the target quantity (F3/Plancherel) — circular. MV contributes nothing beyond diagonal
bookkeeping here. (It would re-enter if the window were widened to length ~ log(1/h)-many
spacings, but that destroys the pinch localization that produces the 1/h mass.)
F-4. Gevrey-mollifier + threaded ("wiggly") contour for the smooth far field: unconditionally
1/zeta << exp(C log T loglog T) on a contour threaded 1/log T away from zeros (RvM O(log T)
zeros per unit band, Borel-Caratheodory locally), and Gevrey-2 corner mollifiers give kernel
decay exp(-c sqrt|Im z|), which beats it. FAILS unconditionally because the deformation must
hold for all s in the window: pole z_p(rho) = a - rho and branch z_b(rho') = rho' - a collide
("far pinches") iff beta+beta' = 3/2 + 3h, gamma'-gamma = gamma_1 + 3 tau — cannot be excluded
without a two-zero anti-conspiracy hypothesis; the resulting (s-s')^{-1/2} singularities sit
at Re s' = (beta+beta'-3/2)/3, possibly > 0 i.e. inside Omega^+, with 1/|zeta'(rho)| factors
that have no unconditional lower bound. Salvaged as the CONDITIONAL Proposition G (FAR.md
4.4), not counted toward closure.
F-5. Self-consistency bootstrap (use the reductio's own J(h) <= A'/2h to bound the far window
mass): gives h int_WIN |D_half Ztil_far|^2 <= 5.83 |c_B|^2 — a true bound, but the triangle
inequality degenerates (the bound is derived FROM G*, so no contradiction can be extracted);
kept only as the scale-pinning F5.
F-6. Bookkeeping slip caught during F1's write-up: the naive triangle bound on
int_WIN |Ztil_far|^2 re-imports the pole's pi/h (the pole is INSIDE B_0); the log-budget form
only holds with the pole subtracted on the x-side before squaring. Fixed in FAR.md Sec 2
(F1's honest restatement); recorded because the first draft asserted the false form.
F-7. far_num3 checkpoint misalignment: x = 1e4, 3e4 checkpoints silently skipped (block size
5e4); only 1e5, 3e5 reported. Cosmetic, two points suffice for the local-exponent fit; noted.

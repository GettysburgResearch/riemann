# FAILURES / caveats — deformation stage (none fatal; weakest-justified variants noted)

F1 (convention deviation from P2.6's letter, justified). P2.6 L172-174 reads as if Z_loc =
the ENTIRE deformed |Im z| <= Z_0 piece and Z_far = |Im z| > Z_0 verbatim. DEFORM.md D2
instead pins Z_loc = the compact cut-hug H(s) only, assigning the four connecting pieces
(V_low, B_out, B_back, V_up) to Z_far. Justification: T-105070 SS2 calls Z_loc "the
cut-hugging local piece", and stage 2 must check amplitude hypotheses on a compact arc.
Consequence: M_far's content changes by a bounded-height-classical term (proved bounded on
the window part, DEFORM.md E3; on the ray part bounded in stated shape only — see F2); the sum B_0 = H_0 + Z_loc + Z_far and both interface statements are
unaffected. If a reviewer insists on P2.6's letter, move the connecting pieces into R_loc
instead — E3 gives exactly the bound needed; no mathematical content changes.

F2 (ray bounds deferred by stage design, with the risk named). On the ray part of Omega^+
(Re s > 1/4, unbounded), DEFORM.md verifies: no singularity collision for any Re s > 1/4
(z_p moves right, z_b + partner cuts move left in parallel, heights never coincide), and
analyticity of every piece; boundedness of Z_loc there (amplitude ~ 1/|z_b| -> 0). But the
QUANTITATIVE uniform bounds on the lengthening connecting horizontals (length ~ (3/2)Re s
against k(beta_z) ~ 1/|beta_z| decay; sketch in E3 gives a bounded, in fact decaying, shape)
are stated as shapes, not completed inequalities — deliberately left to stage 2 per the
stage instructions (do NOT verify hypotheses). Nothing in the deformation itself is at risk;
only M_loc/M_far numerics depend on it.

F3 (inherited, restated so stage 2 does not over-claim). For 0 < Re s <= 5/24 the CONTOUR
formula for Z_far is not available: on Gamma_far, Re(a-z) and Re(a+z) drop below 1, and
unverified zeros (|Im rho| > 60, poles and branch points at |Im z| > 51.4) make the far
integrand not even branch-well-defined without zero data (P2.8(b), the wall). There, Z_far
is defined ONLY by subtraction Z_far := B_0 - H_0 - Z_loc, with B_0's continuation supplied
by the reductio (P2.7 step 3). This is exactly the parent lane's stated architecture, not a
new gap — but it means the deformation identity is PROVED on Re s > 5/24 and extended by the
identity theorem, never by contour manipulation at small h. Z_loc itself (formula (Z)) is
unconditional and analytic on all of Omega^+; no failure touches the [P1-LOC] side.

F4 (small-print on branch matching, resolved but worth an independent recheck). The claim
that the series branch of zeta^{1/2}(a+z) (Re(a+z) > 1) continues to the b-factorized branch
on V_b minus the cut uses connectivity of the overlap region and positivity on the real ray
v > 1; and the auxiliary leftward cuts at partner branch points z'(rho_k) were checked
disjoint from all contours and from R_sweep (Re z' <= -9/16 < leftmost contour point
-3/8 at anchor; <= -1/4 - (3/2)h < -(3/2)h = leftmost point, gap exactly 1/4, for s in
Omega). The gap is 1/4 uniformly, fine — but the recheck is one line and cheap; flagged only
because a wrong cut layout would silently change omega's sign.

F5 (stage 2 — LITERAL derivative bound of SS2/[P1-LOC] FAILS at the pinch corner; amended
form proved, downstream repair subordinate). The interface reads "|R_loc| + |R_loc'| <= M_loc
on Omega^+". PRECISE OBSTRUCTION: R_loc contains a genuine half-power term,
  R_loc(s) = kappa (s-s_0)^{1/2} (1 + O(|s-s_0|)) + (analytic, bounded-derivative part),
  kappa = (sqrt3/2) A(0,s_0) [ 3k'(1/2)/k(1/2) + (3/2)gamma_Euler - (3/2)/z* ]
        = 0.0118261 + 0.0076410 i,  |kappa| = 0.014080 != 0
(the zeta''(rho_1) contributions from the s-variation of A(0,s) and the x-variation of
A(x,s) cancel exactly; closed form cross-checked against direct mpmath differentiation to
12 digits, hyp_num.py). Hence R_loc'(s) = (kappa/2)(s-s_0)^{-1/2} + O(1) -> infinity as
s -> s_0 inside Omega^+ (the corner Re s -> 0+, Im s -> gamma_1/3 is a limit point of
Omega^+ for every r_0). No choice of r_0 or region-shrinking evades this: it is a property
of the expansion at its own center. |R_loc| itself stays bounded (0.554 near, 5.71 global).
WHAT IS PROVED INSTEAD (HYPOTH.md H3): |R_loc| <= M_loc and
  |R_loc'(s)| <= M_loc (1 + |s-s_0|^{-1/2})  on Omega^+(r_0 = 1/2),  M_loc = 640;
literal form holds on truncations: |R_loc| + |R_loc'| <= 637.5 on {|s-s_0| >= 1/24}.
DOWNSTREAM REPAIR (P2.7 step (5), where M_loc is consumed via P2.4(c)): P2.4(c)'s proof
uses only |f(s+del)-f(s)| <= M del (del <= 1) and |f| <= M. Under the amended bound, along
the D_half ray |s+u-s_0| >= max(u, Re(s-s_0)) >= max(u, h), so on the window line Re s = h
the increment obeys |f(s+del)-f(s)| <= M int_0^del (1 + max(u,h)^{-1/2}) du
<= M (del + 2 del^{1/2}) AND <= M del (1 + h^{-1/2}); splitting the D_half del-integral at
del = h and using the second (floor) form on (0,h] (contribution O(M h^{1/2}(1+h^{-1/2}))
= O(M)) and the first form |f(s+del)-f(s)| <= M(del + 2 del^{1/2}) against the del^{-3/2}
weight on [h,1] (int_h^1 (del^{-1/2} + 2 del^{-1}) <= 2 log(1/h) + O(1)) gives
|D_half[R_loc](h+it)| <= C M_loc (1 + log(1/h)) instead of O(M_loc). [NOTE: the naive
increment bound M(del + 2 del^{1/2}) ALONE diverges against the del^{-3/2} weight; the
max(u,h) floor and the del = h split above are load-bearing.] In P2.7(6)
the error term becomes O(M |c_B| log^2(1/h)) instead of O(M |c_B| log(1/h)) — still o(1/h),
the main term (2/(3pi))|c_B|^2/h is untouched, and the limit h -> 0 gives the same c_0'.
CONSEQUENCE: [P1-LOC] should be restated with the amended derivative bound (or on a
truncated region + the log-repair); no constant downstream changes. The same amendment will
be needed of [P2-FAR] only if Z_far exhibits the analogous corner behavior — that burden is
unchanged and remains the wall. NOT FATAL, but the T-105070 SS2 text as written over-claims.

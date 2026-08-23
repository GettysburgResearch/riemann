# WELD — final assembly of the [P1-LOC-WELD] residue (T-105070 SS2 interface)

Stage files: DEFORM.md (deformation), HYPOTH.md (Theorem A hypotheses + M_loc), FAILURES.md
(caveats F1-F5), AUDIT.md (hostile review: PASS, 0 FATAL, 0 MAJOR, 5 MINOR — all five
applied in place, see the APPLIED block at the top of AUDIT.md), weld_num.py /
weld_num_out.txt (this stage's deformed-contour numerics, mpmath dps=30).

## W0. Setup

Target interface (T-105070 SS2, verbatim): there exist r_0 in (0,1], M_loc with
    Z_loc(s) = c_B (s - s_0)^{-1/2} + R_loc(s),   |R_loc| + |R_loc'| <= M_loc on Omega^+,
where Z_loc is the cut-hugging local piece of P2.6's contour split, s_0 = i gamma_1/3,
c_B = (3/2) k(1/2) / (sqrt3 |z*| |zeta'(rho_1)|) in modulus, |c_B| = 0.04782893516094,
k(beta) = 1/beta - (1-2^{-beta})/(beta^2 ln 2), k(1/2) = 0.309778, z* = 1/4 - i gamma_1/2,
gamma_1 = 14.134725141734693. Allowed inputs: (A1) zeros to height 60 verified on the line
and simple; (A2) zeta^{1/2} bounded on compact cut regions. Forbidden (and nowhere used):
RH, zero-free half-planes, density estimates, unverified zero data — audited (AUDIT A1-A5).

## W1. The deformation (DEFORM.md D0-D2; audit A1-A2 + new numerical arbiter)

From P2.5's vertical contour Re z = c = 1/16 (valid on the anchor band
A = {5/24 < Re s <= 1/4, |Im s - gamma_1/3| <= 1}), the segment |Im z - Im z_b| <= 2 is
deformed left across the branch point z_b(s) = 1/4 - (3/2)s into B_out ∪ H ∪ B_back, where
H is the Hankel hug of the leftward cut L(s) (length 2r = 1/4, cap radius delta -> 0).
Swept-region audit (D1, independently recomputed in AUDIT A1): the slit rectangle
[Re z_b - 1/2, 1/16] x [Im z_b - 2, Im z_b + 2] contains NO singularity of Psi other than
the wrapped cut — kernel k is entire (beta = 0 removable), z = 0 is outside the band,
z_p(rho_1) = z_b + eps stays strictly right (Re eps = 3 Re s > 0), z_p(rho_2) below,
z_p(bar rho_1) at height ~ +21, trivial poles at Re >= 2.75, partner branch points at
Re <= -9/16 with leftward cuts, and hypothetical off-line poles are excluded by pure
geometry (Re z_p >= (3/2)Re s - 1/4 > 1/16); off-line partner branch points would need
band ordinates |gamma| < 5.03, where the verified list is empty. No residue is swept.
Numerical arbiter (AUDIT A1): the deformation identity holds to 4.3e-28 at an anchor s,
and hug = collapsed formula (Z) to 1.9e-21; omega = +1 confirmed. Collapsing H (cap
O(delta^{1/2}) -> 0) gives the unconditional compact representation, analytic on all of
Omega^+ (DEFORM D2, eq. (Z)):
    Z_loc(s) = (3/(2pi)) int_0^{1/4} A(x,s) x^{-1/2} (x + 3(s-s_0))^{-1} dx,
    A(x,s) = k(1/2 - x) b(1-x) / ((z_b(s) - x) Z_1(3(s-s_0) + x)),
b(v) = ((v-1)zeta(v))^{1/2}, Z_1(w) = zeta(rho_1+w)/w; the kernel argument on the cut is
1/2 - x EXACTLY (s-independent), which is why the pinch carries k(1/2). Frozen amplitude:
    Z_loc(s) = (sqrt3/2) [k(1/2)/(z* zeta'(rho_1))] (s-s_0)^{-1/2} + R_loc(s),
i.e. SS2's c_B with omega = +1 pinned; |c_B| = 0.04782893516094 = CPINCH W4's value.
Split bookkeeping: Z_loc := the compact cut-hug only; connecting pieces go to Z_far
(convention F1, bounded by E3 on the window; ray part a stated shape, F2). The far
vertical |Im z| > 40 (all unverified-zero singularities, |Im z| >= 51.4) stays [P2-FAR].
Heights consumed by everything local: <= 17.33 << 60 at every window edge (AUDIT A2).

## W2. Theorem A hypotheses on the genuine amplitude (HYPOTH.md H1-H2; audit applied)

Dictionary: model eps_m <-> eps = 3(s-s_0), model r = 1/8 <-> hug 2r = 1/4, model amplitude
a(x,s) = -(3/2)A(x,s), kernel contract (P1 SS F) k(beta_z)/z. Verdicts (H4 table):
  1. r = 1/8 <= min(1/8, gamma_1/8): PASS.
  2. probe sector: Re eps = 3 Re s > 0 on Omega^+, 0 < |eps| <= r on N = {|s-s_0| <= 1/24}: PASS.
  3. I3 kernel: k entire, k(1/2) = 0.309778 != 0; z = 0 pole separated >= 6.30 from the
     cut+margins (formula/number reconciled per AUDIT MINOR-2): PASS.
  4. I1 b-factor: analytic nonvanishing on D(1,1/2) from (A1) + Euler product; principal
     branch valid (min Re((v-1)zeta) = 0.7928 > 0); sup|b| <= 1.0380: PASS.
  5. I2 zero-factor: exactly one zero (rho_1, simple) in D(rho_1,1/2) by the verified list;
     |zeta'(rho_1)| = 0.79316; inf|Z_1| >= 0.6193 (near disk |w| <= 5/8), >= 0.3209 (far
     rectangle W_c), Dirichlet tail for Re w >= 3/2 — no zero data beyond height 60: PASS.
  6. amplitude constants finite (Cauchy radii 1/8, 1/8, 1/96): |A| <= 0.0821 (N),
     M_a = 0.6569, A_1 = 0.5870, M_sx = 15.91, A_F = 1.0120: PASS.
  7. bounded-height inputs only: max zeta-argument height 17.33; unverified singularities
     >= 42.7 away from the local region (H2.6): PASS.
  8. I6 window radius: r_0 = 1/2 < 3.44: PASS.
  9. orientation/branch pinned omega = +1 (D0.b/D2; arbitered numerically, AUDIT A1): PASS.
 10. SS2 |R_loc| <= M_loc on Omega^+: |R_loc| <= 5.71 (near 0.554, far 5.70): PASS.
 11. SS2 |R_loc'| <= M_loc on Omega^+ LITERAL: FAIL — R_loc' = (kappa/2)(s-s_0)^{-1/2}+O(1),
     kappa = 0.0118261 + 0.0076410 i, |kappa| = 0.0140799 != 0, verified three independent
     ways (closed form vs direct derivatives 4e-16; vs 3-point fit of the genuine integral
     2e-6, AUDIT F5 block). Not curable by shrinking r_0: s_0 is a limit point of Omega^+.
 12. amended |R_loc'| <= M_loc(1 + |s-s_0|^{-1/2}): PASS (C_0 = 9.264, C_1 = 2.212 near;
     96 M_R^C = 631.8 far).
Audit applications: MINOR-1/-4 (DEFORM), MINOR-2 (HYPOTH), MINOR-3/-5 (FAILURES) — all
edited in place and logged at the top of AUDIT.md; none load-bearing.

## W3. Explicit M_loc (HYPOTH.md H3)

    M_loc := 640,   r_0 := 1/2,

covering max{M_R^N, M_R^F, C_0, C_1, 96 M_R^C} = max{0.554, 5.701, 9.264, 2.212, 631.8}.
Near bound |R_loc| <= E_1+E_2+E_3 = 0.5538 on N; far |R_loc| <= 5.701; derivative
|R_loc'| <= C_0 + C_1|s-s_0|^{-1/2} on N and <= 631.8 on F. On the truncation
{|s-s_0| >= 1/24}: |R_loc| + |R_loc'| <= 637.5 <= 640 (LITERAL form holds there).
Sharpness: 640 is a flat-Cauchy certificate, not a size estimate (true near constants O(1)).

## W4. The interface, in T-105070 SS2's exact form — and what is actually proved

SS2's exact form: "there exist r_0 in (0,1], M_loc with Z_loc(s) = c_B (s-s_0)^{-1/2}
+ R_loc(s), |R_loc| + |R_loc'| <= M_loc on Omega^+."
PROVED (unconditional, inputs (A1)+(A2) only), with r_0 = 1/2, M_loc = 640, omega = +1:
    Z_loc(s) = c_B (s-s_0)^{-1/2} + R_loc(s)  on Omega^+,  |c_B| = 0.04782893516094,  (i)
    |R_loc(s)| <= 5.71 <= M_loc               on Omega^+,                             (ii)
    |R_loc'(s)| <= M_loc (1 + |s-s_0|^{-1/2}) on Omega^+,                             (iii)
    |R_loc| + |R_loc'| <= 637.5 <= M_loc      on Omega^+ ∩ {|s-s_0| >= 1/24}.         (iv)
DISPROVED: the literal conjunction |R_loc| + |R_loc'| <= M_loc on ALL of Omega^+, for ANY
M_loc and ANY r_0: R_loc contains the genuine half-power kappa (s-s_0)^{1/2}(1+o(1)) with
|kappa| = 0.0140799 != 0 (triple-verified), so R_loc' blows up like |s-s_0|^{-1/2} at the
pinch corner. Downstream repair (FAILURES F5, audit-checked incl. the max(u,h)-floor +
del = h split): P2.4(c)/P2.7(6) consume (iii) at cost log^2(1/h) instead of log(1/h) —
still o(1/h); the main term (2/(3pi))|c_B|^2/h and the limit constant c_0' are unchanged.

## W5. This stage's numerical verification (weld_num.py, dps=30, VIA the deformed contour)

Z_loc evaluated as the genuine Hankel-hug contour integral (finite-eta edges + right cap,
eta = 1e-12, D0.b branch factorization; quad converged: maxdeg 5 vs 6 differ < 1e-22; NOT
the collapsed formula). Three rays arg(s-s_0) in {-pi/4, 0, pi/4}, |s-s_0| = 1e-2..1e-6:
    fitted coefficient c_hat = 0.00918468 + 0.04693874 i,
    worst |c_hat| vs |c_B| relative error = 9.7e-7   (target <= 1e-2),
    worst COMPLEX c_hat vs c_B relative error = 1.03e-6  (phase => omega = +1 re-confirmed).
Grid check: 24 points of Omega^+ (window + ray, incl. corners h = 0.02, |dt| = 1/2):
max |R_loc| = 0.0883; all 24 satisfy |R_loc| <= 640 AND the sharper 5.71 (24/24 PASS).
R_loc -> ~0.0968 along all three rays as s -> s_0, matching AUDIT's independent 0.0967.
Full log: weld_num_out.txt (runtime 109 s, no reduced point set needed).

## Verdict

All of the deformation, the amplitude hypotheses, |R_loc| <= M_loc, and c_B (modulus AND
phase) are closed unconditionally from bounded-height inputs. But the interface in SS2's
EXACT form includes |R_loc'| <= M_loc on all of Omega^+, and that clause is proven FALSE
for the genuine Z_loc — a sharper, amended interface is what closes.

[P1-LOC-WELD]: NOT CLOSED — residue restated: the literal SS2 bound |R_loc| + |R_loc'| <= M_loc fails at the pinch corner because R_loc' = (kappa/2)(s-s_0)^{-1/2} + O(1) with |kappa| = 0.0140799 != 0 (triple-verified), and the weld instead closes unconditionally under the amended interface r_0 = 1/2, M_loc = 640, |R_loc| <= 5.71, |R_loc'| <= M_loc(1+|s-s_0|^{-1/2}) (literal form holding on |s-s_0| >= 1/24 with 637.5), whose P2.7 consumption via the log^2(1/h) repair leaves the main term and every downstream constant unchanged.

# AUDIT — hostile stage-3 review of the [P1-LOC-WELD] (DEFORM.md + HYPOTH.md + FAILURES.md)

APPLIED (stage 4, 2026-08-23): no FATAL/MAJOR findings existed; all five MINOR fixes applied:
APPLIED: MINOR-1 — DEFORM.md D1.b partner-branch-point interval corrected to [-34.4, 48.6],
         "9 + 5ish" -> "9 + 5 = 14".
APPLIED: MINOR-2 — HYPOTH.md H2.3 separation line rewritten: displayed formula now matches
         the used number 6.3017 = gamma_1/2 - (3/2)(1/2 + 1/96) on the fattened Omega_C
         (unfattened value 6.3174 also stated).
APPLIED: MINOR-3 — FAILURES.md F1 "PROVABLY bounded" softened: proved for the window part
         (E3), stated-shape only for the ray part (F2).
APPLIED: MINOR-4 — DEFORM.md E2 kernel tail bound restated with |Im beta_z| >= |Im z| - 8.6;
         the conclusion <= 2/|Im z| for |Im z| >= 40 kept (verified 0.0345 <= 0.05).
APPLIED: MINOR-5 — FAILURES.md F5 repair derivation expanded: max(u,h) floor + del = h split
         made explicit, with the note that the naive increment bound alone diverges.
Replays: audit_num.py, audit_kappa.py (mpmath dps 30/40, independent grids/offsets).

## A1. Independent z-plane singularity inventory (from P2.5's formulas)

Recomputed from Psi = (3/2) k(beta_z) zeta^{1/2}(a+z) / (z zeta(a-z)), a = 3/4+(3/2)s,
beta_z = 1/4+(3/2)s+z. Complete source list: z=0 pole; k entire (the beta^2 ln2 denominator
zero at beta=0 is REMOVABLE — series k = ln2/2 - beta ln2^2/6 + ...; the points
beta = 2 pi i n/ln2 are zeros of the NUMERATOR 1-2^{-beta}, not poles — checklist items both
vacuous, DEFORM D0.b(i) correct); zeta^{1/2}(a+z) branch points at z_b (v=1), z'(rho)=rho-a
(all zeros), z=-2n-a=z_b-(2n+1) (trivial, on the single leftward cut at x>=3, correct);
1/zeta(a-z) poles at z_p(rho)=a-rho and z=a+2n (Re>=2.75, inert); a-z=1 is a ZERO of Psi
(D0.b(v), correct). Conjugate pinch z_p(bar rho_1): height (3/2)Im s + gamma_1 ~ +21, Re >
1/16, never crossed — accounted (D1 item 5). Mirror zeros 1-rho: for on-line zeros 1-rho =
bar rho, already counted as conjugates; off-line only above height 60, delegated to far field
by |Im z| >= 51.4 > 40 — nothing missing. Swept-region check at anchor: EVEN hypothetical
off-line zeros' poles are excluded by pure geometry, Re z_p = Re a - Re rho >= Re a - 1 =
(3/2)Re s - 1/4 > 1/16 strictly on Re s > 5/24 (stronger than D1's stated on-line argument);
off-line partner branch points are NOT Re-excluded but need band height gamma in [-5.03, 4.97]
where the verified list is empty. Inventory COMPLETE; no missed singularity.
NUMERICAL ARBITER (new): at anchor s = 0.23 + i(gamma_1/3 + 0.3), the deformation identity
int_S Psi = int_{B_out∪H∪B_back} Psi holds to |diff| = 4.3e-28 (|S| = 0.443), and
hug/(2 pi i) = collapsed formula (Z) to 1.9e-21 — no swept residue, orientation and branch
layout (omega = +1) CONFIRMED; this also discharges F4's sign recheck numerically at one s.
Also scanned: Re((v-1)zeta) >= 0.548 > 0 on the full dodge-box v-image [3/4,1.19]x[-2,2],
so the principal b-branch is single-valued on all of R_sweep (strengthens D1 item 9).
MINOR-1 (hits DEFORM.md D1.b: "gamma_rho in [-31.4, 48.6]: again 9 + 5ish points"): the
correct interval is [-34.4, 48.6] (= [-40+5.57, 40+8.57]); count is exactly 9+5 = 14.
Conclusion (all verified, Re-excluded left, cuts leftward) unchanged.

## A2. Height-60 exclusion at the window EDGES — verified

Top edge Im s = gamma_1/3 + r_0: local region |Im z| <= (3/2)(gamma_1/3+1) + 1/8 = 8.692
(r_0 = 1); amplitude zeta-arguments: Z_1 at rho_1 + w, |Im w| <= 3.2 => heights in
[10.93, 17.33]; b at 1-x, heights <= 1/8; deformation sweep needs list-completeness only for
|gamma| < 5.03 (empty). All << 60 at every edge. sep_F = gamma_1/2 - (3/2)(1/2 + 1/96)
= 6.30174 recomputed — the 1/96 Omega_C fattening IS included in the used number.
Ray Re s -> inf: Re w >= 3/2 handled by the 1/zeta Dirichlet tail (|1/Z_1| <= 1.51988|w|;
zeta(2)/zeta(4) = 1.519818 <= 1.51988 used — conservative). Strip inventory (Z_far
bookkeeping only) consumes on-line-ness to 48.6 <= 60 — within (A1). PASS.
MINOR-2 (hits HYPOTH.md H2.3: "(3/2)|Im s| >= (3/2)(gamma_1/3 - 1/2) = 6.3017"): the
displayed formula evaluates to 6.3174; the printed number 6.3017 is the 1/96-fattened
Omega_C value actually used downstream (hyp_num.py sep_F). Conservative direction; text slip.

## A3. Uniformity of the arc estimates — sound with a caveat already on record

The delta-cap estimate (E1) is pointwise in s, but is used only to DEFINE the collapse at
each fixed s; every interface bound is then derived directly from the collapsed compact
integral (Z), whose sups (H3) are uniform on N/F by construction. No uniformity gap in
[P1-LOC]. The four connecting pieces are h-uniformly bounded on the window (E3) but only
shape-bounded on the ray (F2); by the F1 convention they sit in Z_far, whose interface
[P2-FAR] is open anyway — no circularity, but:
MINOR-3 (hits FAILURES.md F1: "M_far's content changes by a PROVABLY bounded,
bounded-height-classical term (DEFORM.md E3)"): "provably bounded" is complete only for the
window part (h <= 1/4); the ray part is a stated shape (F2's own admission). Rephrase or
finish the ray inequality; no interface constant depends on it.
MINOR-4 (hits DEFORM.md E2: "|k(beta_z)| <= 1/|Im z| + (1+2^{-Re beta_z})/(ln2 |Im z|^2)"):
the honest bound has |Im beta_z| >= |Im z| - 8.6, not |Im z|. Worst case at |Im z| = 40:
1/31.4 + 1.65/(ln2 * 31.4^2) = 0.0345 <= 2/40 = 0.05, so the asserted "<= 2/|Im z| for
|Im z| >= 40" SURVIVES; intermediate step sloppy. Affects Z_far anchor tail only.

## A4. M_loc assembly — no double count, no omitted conjugate cross term

The conjugate zero bar rho_1 enters Z_loc only through the numeric values of Z_1 (at
w-distance 2 gamma_1 = 28.3, deep inside the Z_N/Z_c compacts — automatically included in
the grid infima); the conjugate WINDOW t ~ -gamma_1/3 is consumed in P2.7(6) at the G* level
via V* real, NOT by the interface — correctly no cross term in M_loc. Assembly recomputed
symbol-by-symbol: |T| <= 4, |T'| <= 16/3, int x^{1/2}|x+eps|^{-2} <= (8/3)|eps|^{-1/2},
(9/2pi)(8/3)/sqrt3 = 4 sqrt3/pi; E1+E2+E3 = 0.5538; M_R^F = 5.701; C_0 = 9.264; C_1 = 2.212;
13.06 = 4 sqrt(32/3) also covers the Re eps < 0 case (32/3 = 10.67 < 13.06); M_R^C = 6.581;
96 M_R^C = 631.8; truncated literal 637.5; M_loc = 640 covers all. Cauchy radii/regions
coherent (X_c margins reach |w| = 5/8 exactly; Omega_C keeps dist(., L_0) >= 1/32; A(0,s)
analytic on |s-s_0| <= 1/6 — Z_1's w=0 point removable). CORRECT.
MINOR-5 (hits FAILURES.md F5: "so |f(s+del)-f(s)| <= M(del + 2 del^{1/2}) and the near-part
of the D_half integral acquires a factor log(1/h)"): the displayed increment bound ALONE
gives a divergent del-integral (2 del^{1/2} * del^{-3/2} = 2/del); the log(1/h) needs the
max(u, Re(s-s_0)) floor stated in the same sentence, with the split at del = h
(int_0^h -> O(1), int_h^1 -> 2 log(1/h)). Conclusion O(M(1+log(1/h))) and the P2.7(6)
log^2 repair are CORRECT; derivation compressed to the point of being misleading.

## A5. Numeric spot-checks (audit_num.py; 20 digits, independent evaluation)

k(1/2)      = 0.30977762283130429755  (= closed form 2 - 4(1-1/sqrt2)/ln2 exactly)   MATCH
|z*|        = 7.0717829228629971335                                                   MATCH
|zeta'(rho_1)| = 0.79316043335650611601                                               MATCH
|c_B|       = 0.04782893516093999598  -> SS2's 0.04782893516094                       MATCH
gamma_2 - gamma_1 = 6.88731 (I6: 1/2 < 3.44 ✓). Independent offset regrids: K_N 0.33678
(<=0.33710+m), B_N 1.03670 (<=1.0380), min Re((v-1)zeta) 0.79281 (~0.7928), Z_N bdry
0.62050 (>= 0.6193 claimed), Z_c 0.32348 (>= 0.3209), rmax 2.03372 (~2.0338). ALL CONFIRM.

## F5 confirmation (the one FAIL is real, not an artifact)

kappa verified THREE independent ways: closed form vs direct A-derivatives agree to 3.9e-16;
vs a new third route — 3-point fit of the genuine Z_loc integral minus c_B(s-s_0)^{-1/2}
along ray arg = pi/6 at t = 1e-5..1e-9 — to 2.1e-6 (fit-truncation limited).
kappa = 0.011826112632815 + 0.007641034837415 i, |kappa| = 0.0140799 != 0. The literal
T-105070 SS2 bound |R_loc'| <= M_loc on Omega^+ is genuinely FALSE; the amended
|R_loc'| <= M_loc(1+|s-s_0|^{-1/2}) is what holds, and its P2.7 consumption (log^2(1/h),
still o(1/h), c_0' unchanged) is sound. Also sanity: |R_loc(s_0+1e-4)| = 0.0967 <= 0.554,
|R_loc(0.2 + i gamma_1/3)| = 0.0571 <= 5.71 — row-10 bounds consistent.

## Findings ledger

FATAL: none.  MAJOR: none new (F5 = the literal-interface over-claim is stage 2's own
declared finding; this audit CONFIRMS both the obstruction and the repair).
MINOR-1  DEFORM D1.b   partner-range typo [-31.4,48.6] -> [-34.4,48.6]; "9+5ish" -> 14.
MINOR-2  HYPOTH H2.3   formula/number mismatch 6.3017 (formula shows no 1/96; number used
                       is the fattened, conservative one).
MINOR-3  FAILURES F1   "PROVABLY bounded (E3)" overstated for the ray part (shapes only, F2).
MINOR-4  DEFORM E2     |Im beta_z| vs |Im z| slip; final <= 2/|Im z| verified true (0.0345<=0.05).
MINOR-5  FAILURES F5   repair derivation compressed; displayed increment bound alone
                       diverges — the max(u,h) floor + del=h split (present in-sentence) is
                       the actual proof. Conclusion correct.

VERDICT: PASS. The deformation is complete and numerically arbitered (4.3e-28), the
inventory has no missing singularity, heights > 60 never enter the local analysis at any
window edge, M_loc = 640's assembly is correct with no conjugate-term omission or double
count, all spot-checked constants match to 20 digits, and the amended interface (r_0 = 1/2,
|R_loc| <= 5.71, |R_loc'| <= M_loc(1+|s-s_0|^{-1/2}), literal form on |s-s_0| >= 1/24 with
637.5) stands. The five MINOR text repairs are recommended, none load-bearing.

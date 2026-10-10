# HYPOTH — Theorem A hypothesis verification on the genuine Z_loc amplitude + explicit M_loc
(stage 2 of [P1-LOC-WELD]; companion to DEFORM.md; numerics: hyp_num.py, mpmath dps=30)

Allowed inputs as in DEFORM.md: (A1) all zeta zeros with |Im| <= 60 on Re = 1/2, simple
(verified list gamma = 14.1347, 21.0220, 25.0109, ...); (A2) zeta^{1/2} bounded on compact cut
regions. No RH, no zero-free half-plane, no density estimates, no unverified zero data.

## H0. Object, dictionary, regions

Object (DEFORM.md D2, eq. (Z)): with s_0 = i gamma_1/3, eps := 3(s - s_0), z_b(s) = 1/4-(3/2)s,

    Z_loc(s) = (3/(2pi)) int_0^{1/4} A(x,s) x^{-1/2} (x+eps)^{-1} dx,
    A(x,s)   = k(1/2-x) b(1-x) / ( (z_b(s)-x) Z_1(eps+x) ),
    b(v) = ((v-1)zeta(v))^{1/2},  Z_1(w) = zeta(rho_1+w)/w,  Z_1(0) = zeta'(rho_1).

Dictionary to P1 Theorem A (P1_model_theorems.md, SS B-C): model eps_m = s-rho <-> eps = 3(s-s_0)
(3 > 0, so arg eps = arg(s-s_0): principal branches agree); model hug 2r <-> 1/4, i.e. r = 1/8;
model collapsed form F_loc = -(1/pi) int_0^{2r} a(x,s) x^{-1/2}(x+eps)^{-1} dx <-> (Z) with
a(x,s) = -(3/2) A(x,s); model kernel 2^{-z}/z <-> k(beta_z)/z (Transfer Contract F: "the model
theorems A,B,C1,C2 hold verbatim with kernel k(z) analytic on D(z_*,4r), k(z_*)!=0 ... only
c_p rescales, mechanism and exponents unchanged"). Theorem A's PROOF (P1 SS C, steps (1)-(4))
consumes exactly: the collapsed integral, Re eps >= 0, and the three amplitude constants
|a|_inf, M_a = sup|da/dx|, A_1 = sup|d a(0,s)/ds| on a neighborhood of the cut segment.

Regions (interface choice r_0 := 1/2; analyticity holds with clearances checked at r_0 = 1):
  Omega^+ := {0 < Re s, |Im s - gamma_1/3| <= 1/2} (window part Re s <= 1/4 plus ray),
  NEAR  N := {s in Omega^+ : |s - s_0| <= 1/24}  (<=> |eps| <= 1/8 = Theorem A's r),
  FAR   F := Omega^+ \ N.
  x-neighborhood X_c := {x in C : dist(x, [0,1/4]) <= 1/8}  (Cauchy radius 1/8 in x).
  Extended s-region for far-Cauchy: Omega_C := {s : dist(s, F) <= 1/96}  (Cauchy radius 1/96).
Both Cauchy radii, stated per the task: 1/8 (x-direction, N), 1/96 (s-direction, F); plus
s-radius 1/8 for A_1 (disk |s-s_0| <= 1/24 -> sup region |s-s_0| <= 1/6) and s-radius 1/24
for the mixed derivative M_sx (sup region |s-s_0| <= 1/12).

## H1. Theorem A's hypotheses, verbatim (P1_model_theorems.md)

(SS B, L31-35) "Fix gamma>0, rho=1/2+i gamma, z_*=(rho-1)/2, r in (0, min(1/8, gamma/8)].
Model inputs: b analytic on D(1,4r), b(1)=1 [= (v-1)^{1/2}zeta(v)^{1/2} loc]; Z analytic
nonvanishing on D(rho,4r), Z(rho)=:zp!=0 [zeta_m(v)=(v-rho)Z(v), SIMPLE zero = simplicity
input]. Amplitude on the cut: a(x,s) := ... x in [0,2r]."
(SS C, L46-47) "THEOREM A. For 0<|eps|<=r, |arg eps|<=pi/2 (probe sector): F_loc(s) =
c_p (s-rho)^{-1/2} (1 + E(s)), |E(s)| <= C_A |s-rho|^{1/2}."
(SS C, L59-69, the constants consumed) "M_a:=sup|da/dx|"; "|a|_inf"; "A_1:=sup|d a(0,s)/ds|";
"C_A = (2(2r)^{-1/2}|a|_inf + 2M_a(2r)^{1/2})/(pi |c_p|) + A_1/|c_p| r^{1/2}-term".
(SS F, L184-186) "(the transfer contract) kernel k(z) analytic on D(z_*,4r), k(z_*)!=0".
(SS F, I1) "zeta(v)^{1/2} = (v-1)^{-1/2} b(v), b analytic nonvanishing on D(1,1/2), b(1)=1."
(SS F, I2) "zeta(v) = (v-rho_1) Z(v), Z analytic nonvanishing on D(rho_1,1/2),
Z(rho_1)=zeta'(rho_1)=0.79316...!=0. Inputs: zero-free punctured disk ... + SIMPLICITY."
(SS F, I3) "k(z)=2^{-z}/z analytic nonvanishing near z_*: unconditional."
(SS F, I6) "window radius r0 < min(gamma_1, (gamma_2-gamma_1))/2."
(N1, L72-78) orientation: sign sigma in {+-1} "tied to the parent contour" — a CONTRACT item,
not a hypothesis to verify beyond pinning (done: DEFORM.md D0.b/D2, omega = +1).

## H2. Verification on the genuine amplitude, hypothesis by hypothesis

(H2.1) r-hypothesis: r = 1/8 <= min(1/8, gamma_1/8) = min(1/8, 1.7668). PASS (equality
allowed; hug length 2r = 1/4 is DEFORM's pinned value).

(H2.2) Probe sector: eps = 3(s-s_0), Re eps = 3 Re s > 0 on all of Omega^+, so
|arg eps| < pi/2 strictly; on N also 0 < |eps| <= 1/8 = r. PASS. (F is handled by direct
bounds in H3.2, not by Theorem A — Theorem A is a |eps| <= r statement by design.)

(H2.3) Kernel k(beta_z)/z — analyticity, poles/zeros, separation (P2.5 bookkeeping).
Poles/zeros of k: k is ENTIRE (DEFORM.md D0.b(i): the beta = 0 denominator zeros of both
terms cancel; k(beta) = (ln2)/2 - beta(ln2)^2/6 + ...). So the beta-map beta_z = 1/4+(3/2)s+z
composed with k is entire in (z,s); the ONLY singularity of k(beta_z)/z is the simple pole
z = 0. On the cut z = z_b(s)-x the kernel argument is beta = 1/2 - x EXACTLY (s-independent);
for x in X_c, beta ranges in the stadium around [1/4,1/2] of radius 1/8 (|beta| >= 1/8:
no removable-point evaluation needed). Nonvanishing at the pinch: k(1/2) = 0.309778 != 0
(only this value enters c_B; zeros of k elsewhere are irrelevant to analyticity).
Separation of the z = 0 pole from the cut: the pole sits at height 0; the cut+margin sits at
heights Im z in [Im z_b - 1/8, Im z_b + 1/8] with |Im z_b| = (3/2)|Im s| >=
gamma_1/2 - (3/2)(1/2 + 1/96) = 6.3017 on the 1/96-fattened Omega_C (the number actually
used downstream; the unfattened r_0 = 1/2 value is 6.3174, and at the stage-1 clearance
r_0 = 1 still >= 5.442). In amplitude
coordinates: |z_b(s) - x| >= (3/2)|Im s| - |Im x| >= 6.880 on N (|Im s - gamma_1/3| <= 1/24,
x-margin 1/8), >= 6.817 on |s-s_0| <= 1/12 (margin for M_sx), >= 6.302 on Omega_C (real x).
All O(1), uniform, from P2.5's "kernel pole at distance |z*| = 7.07" bookkeeping. PASS.

(H2.4) b-factor (hypothesis I1): b analytic nonvanishing on D(1, 1/2), b(1) = 1.
On D(1,1/2): Re v > 1/2. For Re v > 1: Euler product, zeta != 0, and v != 1 there except the
removable point (b(1) = 1, DEFORM D0.b(ii)). For 1/2 < Re v <= 1, |Im v| < 1/2: a zero of
zeta there has |Im| < 1/2 <= 60, hence by (A1) lies ON Re = 1/2 — excluded (Re v > 1/2
strictly); so (v-1)zeta(v) != 0 on all of D(1,1/2). PASS, from (A1) + Euler product only.
Explicit bounds (used region: v = 1-x, x in X_c, i.e. the stadium around [3/4,1] of radius
1/8, inside the rectangle [0.625,1.125] x [-1/8,1/8]): principal-branch validity:
min Re((v-1)zeta(v)) = 0.7928 > 0 on the rectangle (grid 121x121, mpmath), so
b = ((v-1)zeta(v))^{1/2} principal is the analytic branch with b(1) = 1;
  B_N := sup |b| <= 1.0380 (grid max 1.03670 + Lipschitz margin lip|b'| <= 0.2922 x h),
  B_r := sup_{[3/4,1]} |b| = 1.0000;  b'(1) = 0.288608 = gamma_Euler/2 (consistency check).
This is (A2)'s "zeta^{1/2} bounded on compact cut regions", instantiated. PASS.

(H2.5) Zero-factor (hypothesis I2): Z(v) := zeta(v)/(v - rho_1) analytic nonvanishing on
D(rho_1, 1/2), Z(rho_1) = zeta'(rho_1) != 0.
WHICH VERIFICATION IS USED, exactly: (i) simplicity of rho_1 (zeta'(rho_1) != 0,
|zeta'(rho_1)| = 0.7932) — from the verified-to-height-60 computation; (ii) the verified
list of ordinates: heights of D(rho_1,1/2) are [13.635, 14.635] <= 60, and the only zero
with ordinate in that interval is gamma_1 = 14.1347 (nearest others: 21.0220 above, none
below until the conjugates at -14.13); (iii) on-line-ness: any hypothetical off-line zero in
the disk would have |Im| <= 60, contradicting (A1). Hence zeta has exactly one zero (rho_1,
simple) in D(rho_1,1/2) and Z is analytic nonvanishing there. PASS.
Explicit bounds on the regions the amplitude actually visits (w = eps + x):
  disk |w| <= 5/8 (covers N and all Cauchy margins: |eps| <= 1/4 for |s-s_0| <= 1/12,
  plus |x| <= 3/8 on X_c, so |w| <= 5/8): heights of rho_1+w in [13.51, 14.76]: only rho_1; Z_1
  analytic nonvanishing on the closed disk, so |Z_1| attains its min on the boundary
  (minimum-modulus for the nonvanishing analytic Z_1):
     Z_N := inf_{|w| <= 5/8} |Z_1| >= 0.6193  (800-pt boundary grid, min 0.61962, minus
     Lipschitz margin sup|Z_1'| x step/2; interior sanity grid 0.6505);
  rectangle W_c := {-1/16 <= Re w <= 3/2, |Im w| <= 3.2} (covers F's compact part incl. the
  1/96-Cauchy margin: Re w = 3 Re s + x >= -1/32, |Im w| <= 3(1/2 + 1/96) = 1.531 <= 3.2):
  heights of rho_1+w in [10.93, 17.33] <= 60: only rho_1's ordinate is in range; off-line
  zeros excluded by (A1); w = 0 removable with Z_1(0) != 0. Nonvanishing on W_c. PASS.
     Z_c := inf_{W_c} |Z_1| >= 0.3209  (2000-pt boundary grid + margin; interior 0.3235).
  tail Re w >= 3/2: Re(rho_1 + w) >= 2, so |1/zeta(rho_1+w)| <= zeta(2)/zeta(4) = 1.51988
  (Dirichlet series of 1/zeta), giving |1/Z_1(w)| <= 1.51988 |w| — no zero data at all.

(H2.6) Heights > 60 cannot enter the compact local region — explicit geometry.
The local region (cut + amplitude margins) in the z-plane is K(s) + D(0,1/8), so
  |Im z| <= (3/2)|Im s| + 1/8 <= (3/2)(gamma_1/3 + 1) + 1/8 = 8.692   (even at r_0 = 1).
A zero rho contributes the pole z_p = a - rho (height (3/2)Im s - gamma_rho) and the partner
branch point z' = rho - a (height gamma_rho - (3/2)Im s). Either touches the region only if
  |gamma_rho| <= 8.692 + (3/2)|Im s| <= 8.692 + 8.567 = 17.26 << 60.
So every zero the local analysis can feel is in the verified range; conversely any
UNVERIFIED zero (|gamma| > 60) has its pole AND branch point at |Im z| >= 60 - 8.567 = 51.43,
at distance >= 51.43 - 8.692 = 42.74 from the local region: it cannot enter. In amplitude
coordinates the zeta-arguments visited are: rho_1 + w with heights in gamma_1 + [-3.2, 3.2]
= [10.93, 17.33] (Z_1-factor), v = 1 - x with heights <= 1/8 (b-factor); max height consumed
anywhere = 17.33, margin to the verified ceiling 60 is > 42. The "3|Im s|-window + |z*|
scale" in the task: the window contributes 3 r_0 <= 3 to Im w, the |z*| scale fixes the
region's center height at gamma_1/2 = 7.067 — both bounded, independent of any zero data. PASS.

(H2.7) Window-radius hypothesis (I6): r_0 = 1/2 < min(gamma_1, gamma_2-gamma_1)/2 =
min(14.13, 6.89)/2 = 3.44. PASS (with room to spare; DEFORM's analyticity r_0 = 1 also passes).

(H2.8) Orientation/branch: pinned in DEFORM.md D0.b (omega = +1: principal (s-s_0)^{-1/2},
b > 0 on v > 1, upward parent contour, counterclockwise hug); the model N1's clockwise
convention is the opposite parent orientation and flips only the sign — absorbed in c_B's
phase, |c_B| unchanged. Verified consistent with CPINCH W4 = 0.04782893516094. PASS
(FAILURES F4's one-line cut-layout recheck remains flagged, cheap, sign-only).

## H3. Explicit M_loc

### H3.1 Amplitude constants (all from H2's factor bounds; hyp_num.py)

Factorized bound |A(x,s)| <= |k(1/2-x)| |b(1-x)| / (|z_b(s)-x| |Z_1(eps+x)|) with
K_N := sup|k| on the beta-rectangle [1/8,5/8] x [-1/8,1/8] = 0.33710 (grid + Lip margin),
K_r := max_{[1/4,1/2]} k = k(1/4) = 0.32739; B_N, B_r, Z_N, Z_c as in H2.4-5. Then:
  A_N  := sup{|A| : x in X_c, |s-s_0| <= 1/24} <= K_N B_N/(6.880 Z_N)  = 0.08212
  A_NN := same with |s-s_0| <= 1/12            <= K_N B_N/(6.817 Z_N)  = 0.08287
  A_0N := sup_N |A(0,s)| <= k(1/2)/(7.0049 Z_N)                        = 0.07141
  S_1  := sup{|A(0,s)| : |s-s_0| <= 1/6} <= k(1/2)/(6.817 Z_N)         = 0.07337
Cauchy bounds (radii as declared in H0):
  M_a  := sup{|dA/dx| : x in [0,1/4], s in N} <= A_N/(1/8) = 8 A_N     = 0.65691
  A_1  := sup{|d A(0,s)/ds| : s in N} <= S_1/(1/8) = 8 S_1             = 0.58695
  M_sx := sup{|d^2A/ds dx|} <= A_NN/((1/8)(1/24)) = 192 A_NN           = 15.911
Far amplitude (real x in [0,1/4], s in Omega_C): compact part (Re w <= 3/2):
|A| <= K_r B_r/(6.302 Z_c) = 0.1619; tail (Re w >= 3/2, i.e. Re s >= 5/12): |A| <=
K_r B_r · 1.51988 · sup_{Re s >= 5/12} (3 Re s + 1.8125)/sqrt(((3/2)Re s - 1/4)^2 + 6.27^2)
= K_r B_r · 1.51988 · 2.0338 = 1.0120 (sup at Re s = 22.7; -> 2·1.52 K_r B_r as Re s -> inf).
  A_F := 1.0120.

### H3.2 |R_loc| on Omega^+ (r_0 = 1/2)

NEAR (s in N; Theorem A's proof steps applied verbatim to (Z)). Split A = A(0,s) + (A - A(0,s)):
  Z_loc = (3/2) A(0,s) eps^{-1/2} - (3/(2pi)) A(0,s) T(eps)
          + (3/(2pi)) int_0^{1/4} (A(x,s)-A(0,s)) x^{-1/2}(x+eps)^{-1} dx,
using int_0^{1/4} x^{-1/2}(x+eps)^{-1}dx = pi eps^{-1/2} - T(eps), T(eps) :=
int_{1/4}^inf x^{-1/2}(x+eps)^{-1}dx, |T| <= int_{1/4}^inf x^{-3/2} = 4 (|x+eps| >= x since
Re eps > 0, x >= 0; likewise |x+eps| >= |eps|, so |x+eps| >= max(x,|eps|) throughout).
With c_B (s-s_0)^{-1/2} = (3/2) A(0,s_0) eps^{-1/2} (DEFORM D2):
  R_loc = (sqrt3/2)[A(0,s)-A(0,s_0)](s-s_0)^{-1/2} - (3/(2pi))A(0,s)T(eps) + W_I,   (*)
  E_3 := |(sqrt3/2)(A(0,s)-A(0,s_0))(s-s_0)^{-1/2}| <= (sqrt3/2) A_1 |s-s_0|^{1/2}
         <= (sqrt3/2) A_1 (1/24)^{1/2}                                  = 0.10376
  E_2 := (3/(2pi))|A(0,s)||T| <= (6/pi) A_0N                            = 0.13637
  E_1 := |W_I| <= (3/(2pi)) M_a int_0^{1/4} x·x^{-1/2}·x^{-1} dx = (3/(2pi)) M_a = 0.31365
  => |R_loc| <= M_R^N := E_1 + E_2 + E_3                                = 0.5538 on N.
FAR (s in F): directly, |int_0^{1/4} x^{-1/2}(x+eps)^{-1}dx| <= int max(x,|eps|)^{-1}x^{-1/2}
= 4|eps|^{-1/2} <= 8 sqrt2 (|eps| >= 1/8), and |c_B||s-s_0|^{-1/2} <= 0.04783·sqrt(24):
  |R_loc| <= M_R^F := (3/(2pi)) A_F · 8 sqrt2 + 0.2343                  = 5.701 on F.
So |R_loc| <= max(M_R^N, M_R^F) = 5.71 on all of Omega^+.

### H3.3 |R_loc'| — where the literal interface fails, and what holds

NEAR: differentiate (*) term by term (d eps/ds = 3):
  |d/ds of first term| <= (sqrt3/2)[A_1 + A_1/2·(|s-s_0|/|s-s_0|)]... precisely
    <= (3 sqrt3/4) A_1 |s-s_0|^{-1/2}   (|A(0,s)-A(0,s_0)| <= A_1|s-s_0|, |A_s(0,s)| <= A_1);
  |d/ds of T-term| <= (3/(2pi))(A_1·4 + A_0N·3·(16/3)) (|T'(eps)| <= int_{1/4}^inf x^{-5/2}
    = 16/3);
  |W_I'| <= (3/(2pi)) M_sx · 1  +  (9/(2pi)) M_a int_0^{1/4} x^{1/2}|x+eps|^{-2} dx
    <= (3/(2pi)) M_sx + (9/(2pi)) M_a (8/3)|eps|^{-1/2}.
  => |R_loc'| <= C_0 + C_1 |s-s_0|^{-1/2} on N, with
     C_0 := (3/(2pi))(M_sx + 4 A_1 + 16 A_0N) = 9.264,
     C_1 := (3 sqrt3/4) A_1 + (4 sqrt3/pi) M_a = 2.212.
THE HALF-POWER IS REAL, NOT AN ARTIFACT: R_loc' = (kappa/2)(s-s_0)^{-1/2} + O(1) as s -> s_0
in Omega^+, with kappa = (sqrt3/2)[A_s(0,s_0) - 3 A_x(0,s_0)]
= (sqrt3/2) A(0,s_0) [ 3k'(1/2)/k(1/2) + (3/2)gamma_E - (3/2)/z* ]  (the zeta''(rho_1) terms
cancel exactly), numerically kappa = 0.0118261 + 0.0076410 i, |kappa| = 0.014080 != 0
(closed form and direct mpmath differentiation agree to 12 digits). Since s_0 is a limit
point of Omega^+ (corner Re s -> 0+, Im s -> gamma_1/3), the LITERAL SS2/[P1-LOC] bound
"|R_loc'| <= M_loc on Omega^+" is FALSE for the genuine Z_loc: see FAILURES.md F5 for the
precise obstruction and the (subordinate) P2.7 repair. What IS provable — and suffices:
  |R_loc'(s)| <= M_loc (1 + |s-s_0|^{-1/2})  on Omega^+.
FAR: R_loc is analytic on Omega_ext := {Re s > -1/6, |Im s - gamma_1/3| <= 1} minus the ray
L_0 = {Im s = gamma_1/3, Re s <= 0} (Z_loc's only s-singularities there are the pinch slit
Re s in [-1/12, 0] on Im s = gamma_1/3 and the principal cut of (s-s_0)^{-1/2}, both inside
L_0; Z_1-nonvanishing on W_c covers Re w >= -1/16). For s in F, dist(s, L_0) = |s-s_0| >=
1/24, so the Cauchy disk D(s, 1/96) lies in Omega_C with dist to L_0 >= 1/32; there
|x + eps| >= max over the two cases {Re eps >= 0: max(x,|eps|), |eps| >= 3/32;
Re eps < 0: dist(eps, [-1/4,0]) >= 3/32}, giving the integral bound <= 13.06 and
  sup_{Omega_C} |R_loc| <= M_R^C := (3/(2pi)) A_F · 13.06 + 0.04783·sqrt(32) = 6.581,
  |R_loc'| <= M_R^C/(1/96) = 96 M_R^C = 631.8   on F  (crude, finite, not sharp).

### H3.4 Assembled M_loc

    M_loc := 640   (covering max{M_R^N, M_R^F, C_0, C_1, 96 M_R^C} = 631.8, rounded up),

with the verified (amended) interface, on Omega^+ = Omega^+(r_0 = 1/2):

    Z_loc(s) = c_B (s-s_0)^{-1/2} + R_loc(s),  omega = +1 pinned,
    |R_loc(s)| <= 5.71 <= M_loc,
    |R_loc'(s)| <= M_loc (1 + |s-s_0|^{-1/2})       [literal bound FAILS at s_0: F5],
and on any truncation {|s-s_0| >= d}: |R_loc| + |R_loc'| <= 5.71 + max(C_0 + C_1 d^{-1/2},
631.8); at d = 1/24 this is 637.5 <= 640. Sharpness disclaimer: the dominant 96 M_R^C term
is a flat-radius Cauchy artifact; a graded radius ~ |s-s_0|/2 would give O(30) there, and
the true near-region constants are O(1) — M_loc = 640 is a certificate, not an estimate of size.

## H4. Verdict table

| # | Hypothesis (P1 Thm A / contract)         | Genuine instantiation                | Verdict |
|---|------------------------------------------|--------------------------------------|---------|
| 1 | r in (0, min(1/8, gamma/8)]              | r = 1/8, gamma_1/8 = 1.767           | PASS |
| 2 | probe sector 0<|eps|<=r, |arg eps|<=pi/2 | eps = 3(s-s_0), Re eps = 3Re s > 0   | PASS |
| 3 | I3: kernel analytic, k(pinch) != 0       | k ENTIRE; k(1/2)=0.30978; z=0 pole separated >= 6.88 | PASS |
| 4 | I1: b analytic nonvanishing D(1,1/2), b(1)=1 | (A1)+Euler; sup|b| <= 1.0380; branch: min Re((v-1)zeta) = 0.7928 > 0 | PASS |
| 5 | I2: Z analytic nonvanishing D(rho_1,1/2), simple | verified list, |zeta'(rho_1)| = 0.7932; inf|Z_1| >= 0.6193 (near), 0.3209 (far) | PASS |
| 6 | amplitude sups finite (|a|_inf, M_a, A_1)| 0.0821 / 0.6569 / 0.5870 (Cauchy, radii 1/8, 1/8) | PASS |
| 7 | only bounded-height zero data            | max height consumed 17.33 << 60; unverified singularities >= 42.7 away | PASS |
| 8 | I6: r_0 < min(gamma_1, gamma_2-gamma_1)/2| 1/2 < 3.44                           | PASS |
| 9 | orientation/branch pinned                | omega = +1 (DEFORM D0.b/D2; F4 recheck open, sign-only) | PASS |
| 10| SS2: |R_loc| <= M_loc on Omega^+         | 5.71 (near 0.554, far 5.70)          | PASS |
| 11| SS2: |R_loc'| <= M_loc on Omega^+ (literal) | R_loc' ~ (kappa/2)(s-s_0)^{-1/2}, |kappa| = 0.01408 != 0 | FAIL -> F5 |
| 12| amended: |R_loc'| <= M_loc(1+|s-s_0|^{-1/2}) | C_0 = 9.27, C_1 = 2.22 (near), 631.8 (far) | PASS |

M_loc = 640. All PASS verdicts consume only (A1) (zeros to height 60, on-line, simple:
items 4, 5, 7 and the F-region nonvanishing) and (A2) (compact sups: items 4, 5, 6) plus
elementary facts. No RH, no zero-free half-plane, no density input anywhere.

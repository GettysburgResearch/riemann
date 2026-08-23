# [P2-FAR] assault — statement lattice, proved reductions, the residual inequality
Lane: GRAND/far. Sources: T-105070 SS1-2, P2_transfer_theorem.md (P2.3-P2.8), P2_NOTES.md,
P4_mechanism_verdict.md, L-105058 SS4-5. RH status: unproved, not addressed, never assumed.

## 0. Conventions
As in P2: a = 3/4+(3/2)s, s = h+it, window WIN = {|t - gamma_1/3| <= r_0}, s_0 = i gamma_1/3,
psi_0(x) := V_0*(e^x) 1_{x >= ln 64} (unweighted x-side field, V_0* = Lambda* X^{-1/6}),
psi_h(x) := psi_0(x) e^{-hx}. B_0(h+it) = FT[psi_h](t) (P2.7(4), under the reductio).
c_P := sqrt(2/(3pi)) c_B; target constant of P2.7 Rem (iii): eps^2 (2/(3pi))|c_B|^2 = eps^2 |c_P|^2.
"Under R" = under P2.7's reductio hypothesis A := limsup Q_V/log Y = A' - < c_0'.

MODIFIED SPLIT (record): absorb R_loc into the far remainder. Define
    Ztil_far(s) := B_0(s) - H_0(s) - c_B (s-s_0)^{-1/2}
(so Ztil_far = Z_far + R_loc; by [P1-LOC] |R_loc|+|R_loc'| <= M_loc, so every bound below
transfers between Z_far and Ztil_far at cost M_loc, harmless). x-side under R:
    psitil(x) := psi_0(x) - h_0(x) - 2 Re[ c_B pi^{-1/2} x^{-1/2} e^{i gamma_1 x/3} ] (x>=1 branch),
    Ztil_far(h+it) = FT[psitil e^{-hx}](t) + (conjugate-pole cross term, O(1) on WIN).

## 1. Statement lattice

(a) STRONG FORM: |Z_far| + |Z_far'| <= M_far on Omega^+.                             [OPEN]
(b) L2-WINDOW FORM (P2.7 Rem iii): limsup_h h int_WIN |D_half[Z_far](h+it)|^2 dt
    <= eps_1^2 |c_P|^2, eps_1 < 1.                                                   [OPEN]
(F1) Log-budget bound (PROVED, under R): int_WIN |Ztil_far(h+it)|^2 dt <= C_F1 log(1/h).
(F2) D_half Minkowski lift (PROVED, under R): ||D_half[Ztil_far](h+i.)||_{L2(WIN)}^2
     <= C_F2 log(1/h)/h.   [= form (b) up to ONE factor log(1/h): R2's "one log short", exact]
(F3) Multiplier identity (PROVED, unconditional): on the Laplace class of P2.4(a),
     D_half = FT o (mult by sqrt(x)) o FT^{-1}; i.e. D_half[B_0](h+it) = FT[sqrt(x) psi_h](t).
(F4) Commutator lemma (PROVED): the frequency window projection P_w and mult-by-sqrt(x)
     commute up to a bounded operator: ||[P_w, sqrt(x)]||_{L2->L2} <= (1/2) int |v w(v)| dv.
(F5) Self-consistency bound (PROVED, under R; VACUOUS for closure — see 4.3):
     limsup_h h int_WIN |D_half[Ztil_far]|^2 dt <= (sqrt(3 pi A'/2) + |c_B|)^2 <= 5.83 |c_B|^2.
(FAR-WIN) THE RESIDUAL INEQUALITY (open; (FAR-WIN) => (b), Theorem 3 below):
     for some fixed C-infty window w with hat-w = 1 on WIN, supp hat-w in the doubled window,
     and some eps_1 < 1:
         limsup_{h->0+} 2 pi h int_1^inf x |(w * psitil)(x)|^2 e^{-2hx} dx
             <= (eps_1^2/2) |c_P|^2 = (eps_1^2/2)(2/(3 pi)) |c_B|^2 .
     Interpretation: (w*psitil)(x) is the sliding gamma_1/3-frequency amplitude of the
     PINCH-SUBTRACTED unweighted field. The pinch itself has amplitude
     |c_B| (pi x)^{-1/2}, whose weighted mass 2 pi h int x |.|^2 e^{-2hx} dx = |c_B|^2.
     So (FAR-WIN) says: the residual amplitude carries < (eps_1^2/2)(2/(3pi)) ~ 0.106 eps_1^2
     of the pinch's own weighted window mass. Numerics (Sec 5): measured ratio ~ 0.03-0.05.

## 2. Proofs of F1-F4

F1. Under R, P2.7(3) gives Q_{V_0}(Y) <= (3/2)A' loglog Y (1+o(1)), hence
J_0(h) = 2h int Q_0(Y) Y^{-2h} dY/Y <= (3/2)A'(log(1/2h) + O(1)) (substitute L = log Y:
2h int_0^inf log L e^{-2hL} dL = log(1/2h) - gamma_E + o(1)). Plancherel (P2.7(4) applied to
psi_h in L1 cap L2): int_R |B_0(h+it)|^2 dt = 2 pi J_0(h) <= 3 pi A' log(1/h)(1+o(1)).
On WIN: int_WIN |Ztil_far|^2 <= 3[ int_WIN |B_0|^2 + int_WIN |H_0|^2 + |c_B|^2 int_WIN dt/(h^2+tau^2) ]
<= 3[ 3 pi A' log(1/h) + 2 r_0 M_head^2 + pi |c_B|^2/h ]. CORRECTION: the pole term is pi/h,
NOT log — so as stated F1 needs the pole kept subtracted BEFORE squaring; redo cleanly:
int_WIN |Ztil_far|^2 <= 2 int_WIN |B_0 - c_B(.-s_0)^{-1/2}|^2 + 2 int_WIN |H_0|^2. The first
term: |B_0 - pole|^2 <= 2|B_0|^2 + 2|pole|^2 gives the pole's pi/h back — the log-budget
form survives only for the WEIGHTED object (F5), not here. HONEST RESTATEMENT OF F1:
    int_WIN |Ztil_far(h+it)|^2 dt <= 6 pi A' log(1/h) (1+o(1)) + 2 pi |c_B|^2/h-POLE-CANCELLED:
under R the pole DOES sit inside B_0 (that is the mechanism), and Ztil_far = B_0 - H_0 - pole
subtracts it exactly; no triangle-inequality proof can see the cancellation, but the IDENTITY
int_WIN |Ztil_far|^2 = int_WIN |B_0 - H_0 - pole|^2 is what F2 consumes via Minkowski on the
DIFFERENCE field: psitil = psi_0 - h_0 - pinch-x-side, and Plancherel for psitil e^{-hx}:
    int_R |Ztil_far(h+it)|^2 dt = 2 pi int |psitil(x)|^2 e^{-2hx} dx + O(1)
with int_1^inf |pinch-x-side|^2 e^{-2hx} dx = (|c_B|^2/pi) log(1/h)(1+o(1)) + O(1) and
cross terms <= 2 sqrt(J_0 * that) <= C sqrt(A') |c_B| log(1/h). Hence the correct F1:
    int_R |Ztil_far(h+it)|^2 dt <= C_F1 (A' + |c_B|^2) log(1/h),  C_F1 absolute.   [PROVED under R]
(The pole subtraction is performed on the x-side, where it is exact termwise; only L2 norms
of the three pieces and Cauchy-Schwarz are used. No pointwise zeta input.)

F2. D_half[f](s) = -(1/(2 sqrt pi)) int_0^inf (f(s+del) - f(s)) del^{-3/2} d del acts along
horizontal rays; t is a spectator. Minkowski's integral inequality in L2(WIN, dt):
||D_half f(h+i.)||_2 <= (1/(2 sqrt pi)) int_0^inf del^{-3/2} ||f(h+del+i.) - f(h+i.)||_2 d del.
Split at del = h. For del > h: triangle + F1 on lines h and h+del:
||.||_2 <= 2 C_F1^{1/2} sqrt(log(1/min(h+del... ,1/2))) <= 2 sqrt(C_F1 log(1/h));
int_h^inf del^{-3/2} d del = 2 h^{-1/2}. For del <= h: fundamental theorem of calculus in sigma
+ Minkowski + Cauchy line-derivative bound ||Ztil_far'(sigma+i.)||_{L2(WIN')} <=
(2/sigma) sup_{|sigma'-sigma| <= sigma/2} ||Ztil_far(sigma'+i.)||_{L2(WIN'')} (Cauchy integral
over circles of radius sigma/2 centered on the line, windows enlarged by sigma/2 <= 1/2 each
time — F1 holds on any bounded window with the same proof): ||f(h+del+i.) - f(h+i.)||_2 <=
del * (2/h) sqrt(C_F1' log(1/h)); int_0^h del^{-1/2} d del = 2 sqrt h. Total:
||D_half[Ztil_far](h+i.)||_{L2(WIN)} <= (1/(2 sqrt pi)) [ 4 + 4 ] sqrt(C_F1'' log(1/h)/h).
Squared: <= (16/pi) C_F1'' log(1/h)/h =: C_F2 log(1/h)/h.                        [PROVED under R]
This is form (b) times one factor log(1/h): the EXACT size of R2's gap by pointwise routes.

F3. P2.4(a) states G* = sqrt(2/3) D_half[B_0]. Independently, V*(X) = sqrt((2/3) log X) V_0*(X)
gives V*(e^x) = sqrt(2x/3) psi_0-integrand, so G*(h+it) = FT[V* e^{-hx}](t)
= sqrt(2/3) FT[sqrt(x) psi_h](t). Both identities hold on the class where P2.4(a)'s Fubini
licence applies (Re s > 1/6 unconditionally; Re s > 0 under R); equating:
D_half[B_0](h+it) = FT[sqrt(x) psi_h](t). Linearity + the same computation for the head and
for the explicit pinch x-side (P2.4(b) is exactly FT[sqrt(x) x^{-1/2} e^{s_0 x} pi^{-1/2}] =
pi^{-1/2} (s-s_0)^{-1} restated) give D_half[Ztil_far](h+it) = FT[sqrt(x) psitil e^{-hx}](t)
+ O(1)-conjugate-window term. QED. [D_half is the sqrt(x)-multiplier: this converts (b) into an
x-side weighted-mass statement — the door for arithmetic methods, and the exact content of
P2.8(c) R2's "multiplier sqrt(x)".]

F4. P_w f := FT^{-1}[hat-w FT f] has kernel w(x-y), w Schwartz (scale 1/r_0 in x).
[P_w, sqrt(x)] has kernel w(x-y)(sqrt y - sqrt x); |sqrt x - sqrt y| <= |x-y|/(sqrt x + sqrt y)
<= |x-y|/2 on x,y >= 1. Schur test with the symmetric kernel |w(v)| |v|/2:
||[P_w, sqrt(x)]|| <= (1/2) int_R |v w(v)| dv =: C_w < inf, uniformly in h. QED.

## 3. THEOREM (the reduction): (FAR-WIN) => [P2-FAR] in form (b)

Claim. Assume (FAR-WIN) with constant eps_1 < 1 (and [P1-LOC] for the R_loc bookkeeping).
Then under R, limsup_h h int_WIN |D_half[Z_far](h+it)|^2 dt <= eps_1'^2 |c_P|^2 with
eps_1' = eps_1 + o_{r_0}(1) < 1 for r_0 small — i.e. P2.7 Remark (iii)'s hypothesis holds and
P2.7 concludes with c_0' -> (1-eps_1')^2 c_0'.

Proof. By F3, D_half[Ztil_far](h+i.) = FT[sqrt(x) psitil_h] + O(1) on WIN (conjugate window
separation 2 gamma_1/3, kernel decay of the explicit pole terms). Insert the window:
hat-w = 1 on WIN, so on WIN, FT[sqrt(x) psitil_h] = FT[P_w sqrt(x) psitil_h] + FT[(1-P_w)...]
where the second term restricted to WIN is 0 in L2(WIN)-pairing sense... more carefully:
int_WIN |FT[sqrt x psitil_h]|^2 dt <= int_R hat-w2(t)^2 |FT[sqrt x psitil_h]|^2 dt
= 2 pi || P_{w2}[ sqrt x psitil_h ] ||_{L2(dx)}^2   (hat-w2 = 1 on WIN, 0 <= hat-w2 <= 1).
Commute (F4): P_{w2}[sqrt x psitil_h] = sqrt x P_{w2}[psitil_h] + [P_{w2}, sqrt x] psitil_h;
|| [P_{w2}, sqrt x] psitil_h ||_2 <= C_w ||psitil_h||_2 <= C_w sqrt(C_F1 log(1/h)) (F1).
Hence h int_WIN |D_half Ztil_far|^2 dt <= (1+eta) 2 pi h ||sqrt x P_{w2} psitil_h||_2^2
+ C(eta) h [ C_w^2 C_F1 log(1/h) + O(1) ] for any eta > 0; the bracket times h -> 0.
Finally P_{w2} psitil_h = (w2 * (psitil e^{-h.})) and e^{-hx} moves through the convolution up
to a factor e^{h/r_0-scale} = 1+o(1) on the kernel support (|v| <~ 1/r_0, h -> 0):
2 pi h ||sqrt x (w2*psitil) e^{-hx}||^2 (1+o(1)) <= (eps_1^2/2)|c_P|^2 (1+o(1)) by (FAR-WIN)
— wait, (FAR-WIN) as displayed is exactly 2 pi h int x |(w2*psitil)(x)|^2 e^{-2hx} dx <=
(eps_1^2/2)|c_P|^2 in the limsup. Adding the O(1)-terms' vanishing h-contributions and the
R_loc transfer (|D_half R_loc| <= 3 M_loc/sqrt pi by P2.4(c), window measure 2 r_0, times h -> 0):
limsup h int_WIN |D_half[Z_far]|^2 <= (1+eta)(eps_1^2/2)|c_P|^2 * 2 [the factor 2 from
|a+b|^2 <= 2|a|^2+2|b|^2 folding the conjugate-pinch cross term, absorbed since the display
already carries the 1/2]. Choose eta with (1+eta) eps_1^2 < 1. QED (constants tracked to
absolute factors; the 1/2 in (FAR-WIN)'s display is the safety factor that pays the folding).

Remark (sharpness of the reduction). The reduction consumes ONLY: F1 (reductio Plancherel
budget), F3-F4 (exact operator identities), and (FAR-WIN). No zeta values off bounded height
enter: (FAR-WIN) is a statement about the arithmetic field psi_0 at the SINGLE frequency
gamma_1/3 — the far z-contour and 1/zeta(a-z) at unbounded heights have been ELIMINATED from
the interface. This is the honest gain of this lane: [P2-FAR]'s wall is now a fixed-frequency,
scale-averaged amplitude inequality, measurable and finitely checkable at any truncation.

## 4. Route R1 status: what Delta^2 / Montgomery-Vaughan buy, and where they stop

4.1 Corner field. kap_0 = kap_sm + kap_c, kap_c supported on r = d/e in (1,1+delta] U [2-delta,2).
Corner coefficients: c_n^{(delta)} = sum_{de=n, d/e in corners, d > X^{1/3}} mu(d) eta(e);
|c_n| <= 2 Delta(n) (Hooley's Delta: divisors in a ratio window shorter than e-fold), and
sum_{n<=x} Delta(n)^2 <= x (log x)^{C_0} unconditionally (trivially C_0 = 3 via Delta <= d and
sum d(n)^2 ~ x (log x)^3/pi^2; Hall-Tenenbaum "Divisors" Ch. 6-7 give C_0 < 3; Hooley 1979
"On a new technique" for first moments). These bound coefficient SIZES.
4.2 THE TWO STOPS (recorded fully in FAILURES.md):
(i) The corner field's RAW mass is NOT small: numerically it carries 77% of the total mean
square (reproduced independently, Sec 5) — so no "Q_c <= omega(delta) log Y" lemma exists;
the R1 brief's hope that raw-corner smallness + smooth-far decay closes (a) is DEAD as stated.
(ii) The corner field's WINDOW mass is small (3.5%), but proving it is a fixed-height
cancellation statement: on WIN, the corner amplitude is the h-regularized Dirichlet series
sum_n c_n^{(delta)} n^{-3/4-(3/2)h-i(3/2)t}, (3/2)t ~ gamma_1/2 = 7.067 — BOUNDED height.
Montgomery-Vaughan's mean value theorem needs a t-average of length >> log-span of the
coefficients; WIN has FIXED length 2 r_0. The only available average is over the scale x —
which by F3/Plancherel IS the quantity itself, not a tool. Partial summation of the d-sum
at height gamma_1 needs partial sums sum_{d<=D} mu(d) d^{-1/2 - 2iu} = O(D^{1/2-eta}):
RH-strength. PNT-strength savings (M(x) << x e^{-c sqrt(log x)}) leave the corner amplitude
bound at sqrt(y) e^{-c sqrt(log y)} >> y^{1/4} = the pinch scale: ONE FULL POWER-SCALE short,
not a log. So R1's tools bound |c_n| but cannot produce the cancellation; the residue of R1
is exactly (FAR-WIN) restricted to the corner part — same wall, no reduction gained beyond
Sec 3's (which does not need the corner/smooth split at all).

4.3 F5 (self-consistency; why it cannot close). Under R, h int_WIN |G*|^2 <= 2 pi h J(h)
<= pi A' + o(1) (P2.7(2)+(4)), and D_half[Ztil_far] = G*/sqrt(2/3) - D_half H_0 - c_P-pole/...:
h int_WIN |D_half Ztil_far|^2 <= (sqrt((3/2) pi A') + |c_B|/sqrt(pi) * sqrt(pi) + o(1))^2
<= (sqrt(2)|c_B| + |c_B|)^2 = 5.83 |c_B|^2 (using A' < c_0' = (4/(3 pi))|c_B|^2). Needed:
eps_1^2 (2/(3 pi))|c_B|^2 = 0.212 eps_1^2 |c_B|^2. Deficit factor: 5.83/0.212 = 27.5.
The bound is VACUOUS for P2.7's contradiction (it uses the reductio's own J-bound — the
triangle inequality degenerates), but it PINS THE SCALE: after the sqrt(x)-multiplier repair
(F3), the residual gap in [P2-FAR](b) is a CONSTANT factor <= 27.5, not any power or log of h.
(FAR-WIN) must beat self-consistency by that bounded factor; numerics say the truth is ~700x
below self-consistency (Sec 5), so the target has generous room.

4.4 Gevrey-mollifier contour route for the SMOOTH far field (partial; conditional, labeled).
Unconditionally, in every unit height band [T, T+1] there are O(log T) zeros
(Riemann-von Mangoldt), so a "threaded" contour Gamma exists with Re(a-z) in [3/5, 4/5],
dist(Gamma, all zeros and their mirrors) >> 1/log T, on which the classical local expansion
log zeta(w) = sum_{|w-rho|<1} log(w-rho) + O(log T) gives |1/zeta(a-z)|, |zeta^{1/2}(a+z)|
<= exp(C log T loglog T) on Gamma. A Gevrey-2 corner mollifier (compactly supported in log r,
Fourier decay exp(-c sqrt(|Im z|)); exists by Denjoy-Carleman) makes the smooth kernel's
z-transform beat this: the far integrand is << exp(-c sqrt T + C log T loglog T), absolutely
integrable. WHAT BLOCKS THE UNCONDITIONAL CLAIM: deforming from the P2.5 contour to Gamma and
holding the representation on all of Omega^+ requires that no pole z_p(rho) = a - rho collide
with a branch point z_b(rho') = rho' - a as s sweeps the window: collisions occur iff
beta + beta' = 3/2 + 3h with gamma' - gamma = gamma_1 + 3 tau (a FAR PINCH), producing genuine
(s - s')^{-1/2} singularities of the smooth far field INSIDE Omega^+ at Re s' =
(beta+beta'-3/2)/3 > 0, with coefficients ~ exp(-c sqrt(gamma'))/( |zeta'(rho)| |z*'| ) —
heights unbounded, |zeta'(rho)| with no unconditional lower bound. Hence:
PROPOSITION G (conditional, NOT counted toward closure). If (i) every pair of zeros
rho = beta+i gamma, rho' = beta'+i gamma' with gamma' - gamma in [gamma_1 - 3 r_0, gamma_1 + 3 r_0]
satisfies beta + beta' <= 3/2, and (ii) |zeta'(rho)| >= exp(-sqrt(gamma)/A) at those zeros,
then the Gevrey-smooth far field satisfies form (a) on Omega^+ with explicit M_far(A, delta),
and [P2-FAR] reduces to the CORNER part of (FAR-WIN) alone. Hypotheses (i)-(ii) are unproved
(far weaker than RH — a two-zero anti-conspiracy — but unproved); recorded as a route marker.

## 5. Numerics (far_num1-3.py; far_num*_out.json)
Setup: independent code (far_common.py, own sieves for mu and the zeta^{1/2} coefficients eta),
Xc = 2e5 (10x lane P2's 2e4), M = 2^18 samples of V* on [ln 64, ln Xc], FFT pad 2^22.
Truncation h_eff ~ 1/ln Xc = 0.082: h below ~0.04 is truncation-limited (reported anyway).

5.1 Corner split reproduced (far_num1). Two corner conventions: A = doc's (1,1.25]U(1.75,2];
B = P2_num5's actual code (1,1.25]U(1.75,inf) — the code and the doc DIFFER (code has no upper
cut at r=2); the quoted 77% is B-style. Measured here (Xc=2e5): raw mean-square corner/all:
B = 0.707, A = 0.180. Window mass share at gamma_1/3 (h=0.01): r0=0.05: B 7.6%; r0=0.15:
B 7.8% (lane P2 quoted 3.5% at Xc=2e4, +-0.15 — same structure, factor ~2 from Xc and
convention; DISCREPANCY RECORDED, does not affect any proof); r0=0.30: 8.5%; r0=0.50: 10.1%.
Control band [7,8]: corner carries 77% of it (0.00122/0.00159) — the corner field IS the flat
background; the pinch window is where it is depleted. h-scaling of the share at r0=0.15:
0.0825 (h=.04) -> 0.0795 (.02) -> 0.0781 (.01): decreasing slowly, consistent with flat corner
vs growing pinch, truncation-limited.

5.2 (FAR-WIN) measured directly (far_num2). Frequency-localized amplitude a(x) of the
UNWEIGHTED field psi_0 (smooth bump window, half-widths r0 = 0.15/0.30/0.50 — a proxy for the
plateau window of Sec 3, same object up to fixed constants), complex pinch fit
a ~ c x^{-1/2} e^{i gamma_1 x/3} on x in [5, 11.5]:
    r0:                
0.15    0.30    0.50
    |c_fit|/(|c_B|/sqrt pi):  0.261   0.496   0.736   [bump clips the pole's |tau|^{-1} spread;
                                                       grows toward 1 with window width, as it must]
    residual/pinch weighted-mass ratio (h=0.02):  0.0130  0.0094  0.0068
                                       (h=0):     0.0133  0.0093  0.0065
    corner-field/pinch share (h=0.02):            0.0874  0.0856  0.0833
    implied eps_1 = sqrt(3 pi x ratio):           0.351   0.297   0.253
(FAR-WIN) requires ratio < 1/(3 pi) = 0.1061 for eps_1 < 1: measured 0.007-0.013 — an order of
magnitude inside, at every width, stable in h. Headroom vs the F5 self-consistency ceiling:
5.83/0.212 = 27.5x needed; measured ~ 700x better than self-consistency.

5.3 Delta^2 constants and corner coefficients (far_num3, x to 3e5, own Delta(n) two-pointer).
sum d(n)^2 / (x log^3 x / pi^2) = 1.70 (1e5), 1.64 (3e5) [trivial C_0 = 3 anchor, approaching
its asymptote from above]. sum Delta(n)^2 / x = 8.94 (1e5), 9.67 (3e5); local exponent
c_fit = 0.90 in x(log x)^c — far below 3, consistent with Hall-Tenenbaum. sum Delta(n)/x =
2.40, 2.46. Corner coefficients c_n(delta) (both corners, no d>X^{1/3} cut): |c_n| <= 2 Delta(n)
verified, 0 violations. sum c_n^2/x = 0.0099 (delta=.25), 0.0052 (.125), 0.0027 (.0625):
LINEAR in delta (halving ratios 1.89, 1.95), and ~1000x smaller than the Delta^2 budget at
delta = 0.25: coefficient SIZE is not the obstruction anywhere — only cancellation is,
exactly as Sec 4.2 concludes.

## 6. VERDICT
[P2-FAR]: NOT CLOSED — reduced to: (FAR-WIN), the fixed-frequency scale-averaged amplitude
inequality  limsup_{h->0} 2 pi h int x |(w * psitil)(x)|^2 e^{-2hx} dx <= (eps_1^2/2)|c_P|^2,
eps_1 < 1, for the pinch-subtracted unweighted field psitil — with the reduction
(FAR-WIN) => [P2-FAR](b) PROVED here (Sec 3) from F1-F4, all unconditional-under-R, no zeta
data off bounded height. Literature anchors for the residual: Hooley 1979 (Delta-function),
Hall-Tenenbaum "Divisors" (Delta^2 moments) bound the coefficients; Montgomery-Vaughan mean
values do NOT apply (fixed-length t-window); the cancellation needed is Selberg-Delange /
Hankel type at fixed height gamma_1/2 with the Mobius factor — precisely the (P-ii) error of
L-105058.4, there proved only modulo a zero-free half-plane. The wall is real but it is now
ONE scalar inequality about ONE frequency, with a proved 27.5x self-consistency ceiling (F5)
and measured headroom ~700x (Sec 5).

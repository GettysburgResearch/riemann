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
    Ztil_far(h+it) = FT[psitil e^{-hx}](t) + (conjugate-pole cross term + untruncated-pole
    tail, O(1) on any bounded window, in particular on WIN — but NOT integrable over the
    full line; see F1's G2 note).

## 1. Statement lattice

(a) STRONG FORM: |Z_far| + |Z_far'| <= M_far on Omega^+.                             [OPEN]
(b) L2-WINDOW FORM (P2.7 Rem iii): limsup_h h int_WIN |D_half[Z_far](h+it)|^2 dt
    <= eps_1^2 |c_P|^2, eps_1 < 1.                                                   [OPEN]
(F1) Log-budget bound (PROVED, under R; x-side form — review finding G2: the FULL-line
     integral of Ztil_far itself DIVERGES, since the subtracted untruncated half-pole has
     line density |c_B|^2 (h^2+tau^2)^{-1/2} ~ |c_B|^2/|tau|, non-integrable; the correct
     global object is the x-side one, and every windowed use is equivalent at O(1)):
         int_R |FT[psitil e^{-hx}](t)|^2 dt = 2 pi ||psitil_h||_{L2}^2
             <= C_F1 (A' + |c_B|^2) log(1/h),
     and on any bounded window W: ||Ztil_far(h+i.)||_{L2(W)} <= ||FT[psitil_h]||_{L2(W)} + O(1).
(F2) D_half Minkowski lift (PROVED, under R; consumes F1 in its windowed form only):
     ||D_half[Ztil_far](h+i.)||_{L2(WIN)}^2
     <= C_F2 log(1/h)/h.   [= form (b) up to ONE factor log(1/h): R2's "one log short", exact]
(F3) Multiplier identity (PROVED, unconditional): on the Laplace class of P2.4(a),
     D_half = FT o (mult by sqrt(x)) o FT^{-1}; i.e. D_half[B_0](h+it) = FT[sqrt(x) psi_h](t).
(F4) Commutator lemma (PROVED): the frequency window projection P_w and mult-by-sqrt(x)
     commute up to a bounded operator: ||[P_w, sqrt(x)]||_{L2->L2} <= (1/2) int |v w(v)| dv.
(F5) Self-consistency bound (PROVED, under R; VACUOUS for closure — see 4.3):
     limsup_h h int_WIN |D_half[Ztil_far]|^2 dt <= (sqrt(3 pi A'/2) + |c_B|)^2 <= 5.83 |c_B|^2.
(FAR-WIN) THE RESIDUAL INEQUALITY (open; (FAR-WIN) => (b), Theorem 3 below). Stated UNDER R
     (the reduction needs it only there; under R the convolution converges absolutely via the
     loglog Q-budget — unconditionally psi_0 may grow like e^{x/6} pointwise against a
     sub-exponential window tail, review finding G6). For some fixed C-infty window w with
     hat-w REAL, 0 <= hat-w <= 1, hat-w = 1 on WIN, supp hat-w in the doubled window
     (Theorem 3's proof uses THIS w as its projector, so these conditions are part of the
     hypothesis — G6), and some eps_1 < 1, with the Abel damping INSIDE the convolution
     (placement per review finding G1 — this is the form the proof consumes):
         limsup_{h->0+} 2 pi h int_R x_+ |(w * (psitil e^{-h.}))(x)|^2 dx
             <= (eps_1^2/2) |c_P|^2 = (eps_1^2/2)(2/(3 pi)) |c_B|^2 ,   x_+ := max(x, 1).
     Interpretation: (w * psitil_h)(x) is the sliding gamma_1/3-frequency amplitude of the
     PINCH-SUBTRACTED damped field. The pinch itself has amplitude
     |c_B| (pi x)^{-1/2}, whose weighted mass 2 pi h int x |.|^2 e^{-2hx} dx = |c_B|^2.
     So (FAR-WIN) says: the residual amplitude carries < (eps_1^2/2)(2/(3pi)) ~ 0.106 eps_1^2
     of the pinch's own weighted window mass. Numerics (Sec 5): measured ratio ~ 0.007-0.013
     (weight-outside placement on the truncated field; the placement difference is the
     D-term of Sec 3's Remark, o(1) under R and negligible at the measured truncation).

## 2. Proofs of F1-F4

F1 (x-side form; rewritten per review findings G2/G3/G4). Under R, P2.7(3) gives
Q_{V_0}(Y) <= (3/2)A' loglog Y (1+o(1)), hence by Abel summation
J_0(h) := ||psi_0 e^{-hx}||_{L2}^2 = 2h int Q_0(Y) Y^{-2h} dY/Y <= (3/2)A'(log(1/2h) + O(1))
(substitute L = log Y: 2h int_0^inf log L e^{-2hL} dL = log(1/2h) - gamma_E + o(1)).
The x-side pinch term: int_1^inf |2 Re[c_B pi^{-1/2} x^{-1/2} e^{i gamma_1 x/3}]|^2 e^{-2hx} dx
= (2|c_B|^2/pi) log(1/h)(1+o(1)) + O(1) (the mean of the square is 2|c_B|^2/(pi x); the
oscillating cross-frequency part is O(1) — constant corrected per G4, previously |c_B|^2/pi).
The head h_0 contributes O(1). Triangle inequality in L2(dx) on psitil_h = psi_h - h_{0,h}
- pinch_h, then Plancherel (psitil_h in L1 cap L2 under R, same licence as P2.7(4)):
    int_R |FT[psitil e^{-hx}](t)|^2 dt = 2 pi ||psitil_h||_{L2}^2
        <= C_F1 (A' + |c_B|^2) log(1/h),  C_F1 absolute.            [PROVED under R]
G2 NOTE (why the x-side form is the only correct global statement): the line integral
int_R |Ztil_far(h+it)|^2 dt is +INFINITY — Ztil_far subtracts the UNTRUNCATED half-pole
c_B(s-s_0)^{-1/2}, whose line density |c_B|^2 (h^2+tau^2)^{-1/2} ~ |c_B|^2/|tau| is not
integrable at tau -> +-inf. On any BOUNDED window W the two objects differ by O(1)
(the pole-transform tail + conjugate term, Sec 0), so every windowed use (F2, Theorem 3)
is unaffected: ||Ztil_far(h+i.)||_{L2(W)} <= ||FT[psitil_h]||_{L2(W)} + O(1).
G3 NOTE (correcting this file's own first-round "CORRECTION" narrative): the earlier claim
that the naive triangle bound "re-imports the pole's pi/h" was itself a miscomputation —
the subtracted term is the HALF-order pole, and |c_B (s-s_0)^{-1/2}|^2 integrated over WIN
is 2|c_B|^2 log(r_0/h), a benign log, NOT pi/h (pi/h is correct only for the full-order
pole after D_half, as used in F5 — that use stands). The first-draft triangle route was
essentially sound; the x-side form above is kept because it is the correct GLOBAL statement
(G2), not because of the pi/h phantom. FAILURES F-6 is annotated accordingly.
(Only L2 norms of the three pieces and Cauchy-Schwarz are used. No pointwise zeta input.)

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

F4 (G5-corrected: global multiplier). P_w f := FT^{-1}[hat-w FT f] has kernel w(x-y), w
Schwartz (scale 1/r_0 in x). Since P_w outputs live on ALL of R while sqrt(x) is undefined
for x < 0 and not (1/2)-Lipschitz on (0,1), define the GLOBAL multiplier
    m(x) := sqrt(max(x, 1))
— equal to sqrt(x) on [1, inf) = supp psitil, and globally (1/2)-Lipschitz on R:
|m(x) - m(y)| <= |x-y|/(m(x)+m(y)) <= |x-y|/2. [P_w, m] has kernel w(x-y)(m(y) - m(x));
Schur test with the symmetric kernel |w(v)||v|/2:
||[P_w, m]||_{L2(R)->L2(R)} <= (1/2) int_R |v w(v)| dv =: C_w < inf, uniformly in h (the
operator does not depend on h). QED. All Sec 3 uses go through m; the x < 1 region's
weight cost is handled there.

## 3. THEOREM (the reduction): (FAR-WIN) => [P2-FAR] in form (b)

Claim. Assume (FAR-WIN) with constant eps_1 < 1, for the window w it names (and [P1-LOC]
for the R_loc bookkeeping). Then under R,
limsup_h h int_WIN |D_half[Z_far](h+it)|^2 dt <= (eps_1^2/2) |c_P|^2 — i.e. P2.7 Remark
(iii)'s hypothesis holds with eps_1' = eps_1/sqrt(2) EXACTLY (review finding G7: r_0 is
fixed by w; every error term below vanishes as h -> 0 at fixed r_0, so no ill-defined
o_{r_0}(1) appears — the constant is exact, and stronger than the first draft claimed),
and P2.7 concludes with c_0' -> (1 - eps_1/sqrt(2))^2 c_0'.

Proof (rewritten per review findings G1/G5/G7/G8; the proof uses (FAR-WIN)'s OWN window w
as the projector — this is why w's conditions sit in the hypothesis).
Step 1 (F3 + window insertion). By F3 and Sec 0's bounded-window comparison,
D_half[Ztil_far](h+i.) = FT[sqrt(x) psitil_h] + O(1) on WIN (conjugate window separation
2 gamma_1/3; explicit pole terms). Since psitil_h is supported in [1, inf), sqrt(x) psitil_h
= m(x) psitil_h with m(x) = sqrt(max(x,1)) (F4's global multiplier — G5). With hat-w real,
0 <= hat-w <= 1, hat-w = 1 on WIN:
    int_WIN |FT[m psitil_h]|^2 dt <= int_R hat-w(t)^2 |FT[m psitil_h]|^2 dt
        = 2 pi || P_w[ m psitil_h ] ||_{L2(R)}^2 .
Step 2 (commute — F4 + F1). P_w[m psitil_h] = m P_w[psitil_h] + [P_w, m] psitil_h, and
|| [P_w, m] psitil_h ||_2 <= C_w ||psitil_h||_2 <= C_w sqrt(C_F1' log(1/h)) (F1, x-side).
For any eta > 0: h ||P_w[m psitil_h]||^2 <= (1+eta) h ||m P_w psitil_h||^2
+ C(eta) h C_w^2 C_F1' log(1/h), and the second term -> 0 as h -> 0.
Step 3 (consume (FAR-WIN) — no weight-migration step needed: G1). P_w psitil_h =
w * (psitil e^{-h.}) EXACTLY, which is (FAR-WIN)'s object with the damping inside the
convolution — the placement (FAR-WIN) now states. And |m(x)|^2 = max(x,1) = x_+, so
    2 pi h ||m P_w psitil_h||_{L2(R)}^2 = 2 pi h int_R x_+ |(w * (psitil e^{-h.}))(x)|^2 dx,
whose limsup is <= (eps_1^2/2)|c_P|^2 by (FAR-WIN) verbatim. (The old proof moved e^{-hx}
through the convolution via a false compact-support premise — w is Schwartz but NOT
compactly supported; see the Remark below for the two-regime argument relating the two
placements, kept for the numerics comparison. The official chain needs no such step.)
Step 4 (reassemble — G8 accounting, clean). D_half[Z_far] = D_half[Ztil_far] - D_half[R_loc],
and D_half[Ztil_far] = FT[m psitil_h] + (Step-1 additive terms) on WIN. Every non-main piece
VANISHES in windowed h-mass: |D_half R_loc| <= 3 M_loc/sqrt(pi) pointwise (P2.4(c) with
[P1-LOC]) gives h (2 r_0)(3 M_loc/sqrt(pi))^2 -> 0; the Step-1 O(1) terms (conjugate pole,
pole tail, head) give h * O(1) * 2 r_0 -> 0. Peter-Paul fold, once:
|main + vanishing|^2 <= (1+eta)|main|^2 + (1+1/eta)|vanishing|^2, and the second term's
h-mass -> 0 for every fixed eta. With Steps 1-3:
    limsup_h h int_WIN |D_half[Z_far]|^2 dt <= (1+eta)^2 (eps_1^2/2)|c_P|^2   for all eta > 0
        => limsup <= (eps_1^2/2)|c_P|^2 = eps_1'^2 |c_P|^2 with eps_1' = eps_1/sqrt(2).
No factor 2 is ever owed (G8 — the previous text paid the display's 1/2 into a fold that the
Peter-Paul weighting makes free; the conjugate-pinch cross term it worried about is already
inside the vanishing budget). The conclusion is therefore STRONGER than claimed: (FAR-WIN)
with eps_1 < 1 delivers P2.7 Rem (iii) with eps_1' = eps_1/sqrt(2) <= 0.708 < 1, and
c_0' -> (1 - eps_1/sqrt(2))^2 c_0'. QED.

Remark (placement of the damping; the G1 two-regime argument, kept for Sec 5's numerics).
The first draft stated (FAR-WIN) with the weight outside the convolution and moved e^{-hx}
inside via a false kernel-support premise (hat-w in C_c^infty with hat-w = 1 on an interval
forces w to be non-compactly supported — an analytic hat identically 1 on an interval would
be constant). Under R the two placements nevertheless differ by o(1) in the weighted mass:
with D(x) := (w * psitil)(x) e^{-hx} - (w * (psitil e^{-h.}))(x)
= int w(v) psitil(x-v) e^{-hx} (e^{hv} - 1) dv, split by v-regimes —
(i) v > 0: psitil(x-v) e^{-hx} e^{hv} = psitil_h(x-v) exactly, so the integrand is
w(v) psitil_h(x-v)(1 - e^{-hv}) with |1 - e^{-hv}| <= min(1, hv): kernel |w(v)| min(1,hv)
in L1 with mass O(h int |v w|), against the shifted weighted norm
h int (y+v)_+ |psitil_h(y)|^2 dy <= W_h + v h C_F1' log(1/h), W_h = O(1) under R (F5's
x-side bound) — total O(h log(1/h)) -> 0.
(ii) v < 0: |e^{hv} - 1| = 1 - e^{hv} <= min(1, h|v|); for |v| <= h^{-1/2} the kernel mass
is O(h^{1/2}) against e^{h|v|} <= e^{h^{1/2}} = O(1) times ||psitil_h||; for |v| > h^{-1/2}
use |e^{hv} - 1| <= 1, the under-R unit-block budget ||psitil||_{L2[T,T+1]}^2 <= C log(2+T)
(from Q_{V_0} <= (3/2)A' loglog Y plus the explicit pinch/head blocks), and w's Schwartz
decay: contribution O(h^N) for every N. Total: the placement difference is o(1) in the
h-weighted mass under R — so Sec 5's weight-outside measurements bear on the official
damped-inside (FAR-WIN) up to a vanishing correction. [Argument supplied by the hostile
review of this packet; recorded verbatim-in-substance.]

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

5.2 (FAR-WIN) measured directly (far_num2). CAVEATS (G9): far_num2's bump window is a
smooth proxy, not identically 1 on WIN (admitted; conservative in the fitted-pinch
denominator, which uses the CLIPPED fit |c_fit| < |c_B|/sqrt(pi) — overstating the ratio);
the weight sits outside the convolution (see Sec 3's Remark for the o(1) placement
equivalence under R); and the |c_n| <= 2 Delta(n) check of 5.3 runs at delta = 0.25 only.
Frequency-localized amplitude a(x) of the
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
inequality  limsup_{h->0} 2 pi h int x_+ |(w * (psitil e^{-h.}))(x)|^2 dx <= (eps_1^2/2)|c_P|^2,
eps_1 < 1, for the pinch-subtracted damped field (damping inside the convolution — Sec 1's
G1-corrected placement) — with the reduction (FAR-WIN) => [P2-FAR](b) PROVED here (Sec 3,
delivering eps_1' = eps_1/sqrt(2)) from F1-F4, all unconditional-under-R, no zeta data off
bounded height. Literature anchors for the residual: Hooley 1979 (Delta-function),
Hall-Tenenbaum "Divisors" (Delta^2 moments) bound the coefficients; Montgomery-Vaughan mean
values do NOT apply (fixed-length t-window); the cancellation needed is Selberg-Delange /
Hankel type at fixed height gamma_1/2 with the Mobius factor — precisely the (P-ii) error of
L-105058.4, there proved only modulo a zero-free half-plane. The wall is real but it is now
ONE scalar inequality about ONE frequency, with a proved 27.5x self-consistency ceiling (F5)
and measured headroom ~700x (Sec 5).

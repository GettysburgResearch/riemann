# Lane P1: Model Singularity-Transfer Theorem — PLAN
1. Read T-105059 (w-pinch program), L-105058.5 (mass lemma architecture), X-105059 NOTES (E1 half-derivative model comp).
2. Set model geometry: zeta_model(w) = (w-rho1)(w-rho1bar)G(w), G analytic nonvanishing on disk; pin contour picture.
3. (a) Pinch expansion: deform z-contour, identify pole z = w - rho1 of 1/zeta(w+z) hitting cut of zeta(w-z)^{1/2} from w-z=1; derive F(s) = c_pinch (s-rho1)^{-1/2}(1+O(|s-rho1|^kappa)) with explicit c_pinch.
4. Numeric check (a): implement model F, fit exponent -1/2 and constant to 3+ digits.
5. (b) Mellin lemma: multiplication by sqrt(log u) <-> Weyl half-derivative; derive exact Gamma constant; prove D^{1/2}(s-rho)^{-1/2} = (Gamma(1)/Gamma(1/2))... = full pole with constant.
6. Numeric check (b): verify constant Gamma(1)/Gamma(1/2) = 1/sqrt(pi) via direct Mellin integrals.
7. (c) L2 window bound: int |D^{1/2}F(-1/2+h+it)|^2 dt >= c/h, mimic L-105058.5 Schwarz architecture.
8. Numeric check (c): 1/h blow-up to 3 digits across h dyadic range.
9. Write transfer contract: exact genuine-zeta inputs consumed (radii, simplicity, nonvanishing).
10. Final: theorem statements + proofs in NOTES.md; final message leads with STATEMENTS PROVED.

## A. Geometry (derived, exact)
Normalizations. Prompt-norm s (pinch at s=rho, Re=1/2) vs L-105058.5-norm s'=s-1
(probe -1/2+h). w=(1+s)/2. Branch pt of zeta(w-z)^{1/2}: z_b(s)=w-1=(s-1)/2.
Pole of 1/zeta(w+z): z_p(s)=rho-w. Both -> z_*=(rho-1)/2 as s->rho. With
eps:=s-rho: z_b=z_*+eps/2, z_p=z_*-eps/2, so z_b-z_p=eps EXACTLY.
Probe side: the H2 machinery (L-105058.5(3)) probes from the CONVERGENT side:
Re s=1/2+h (s'=-1/2+h), i.e. Re eps=+h>0. [T-105059.6's "1/2-h" is the other
sign convention; the Mellin abscissa forces Re eps>0 — checked via |W_u|~u^{-1/2}.]
Cut of (w-z-1)^{-1/2} in z: v=w-z in (1/2,1] <=> z in [z_b, z_b+1/2): RIGHTWARD
horizontal ray from z_b. Since z_p-z_b=-eps with Re eps=h>0: the pole approaches
the branch point from the LEFT = the CUT-FREE side, at distance exactly |eps|;
it would meet the cut only for eps in (-infty,0], i.e. s on the leftward slit
rho+(-infty,0], which the probe line never touches. PINCH TYPE: endpoint pinch
(Landau): pole collides with the endpoint z_b of the (collapsed) cut integral;
no contour-trapping for Re eps>0, all branches principal. Key simplification:
at z=z_b+x on the cut, w+z-rho = 2w-1-rho+x = eps+x (exact, no factor).

## B. Model definition (lane P1 object)
Fix gamma>0, rho=1/2+i gamma, z_*=(rho-1)/2, r in (0, min(1/8, gamma/8)].
Model inputs: b analytic on D(1,4r), b(1)=1  [= (v-1)^{1/2}zeta(v)^{1/2} loc];
Z analytic nonvanishing on D(rho,4r), Z(rho)=:zp!=0  [zeta_m(v)=(v-rho)Z(v),
SIMPLE zero = simplicity input]. Amplitude on the cut:
  a(x,s) := 2^{-(z_b+x)}/(z_b+x) * b(1-x) / Z(rho+eps+x),  x in [0,2r].
Model F := open-Hankel integral (parent contour's local piece):
  F_loc(s) = (1/2pi i) int_H Psi dz,
  Psi = (2^{-z}/z) b(w-z)(w-z-1)^{-1/2} / ((w+z-rho) Z(w+z)),
H = Hankel arc: in below the cut from z_b+2r-i0, around z_b (left), out above
to z_b+2r+i0; principal branch of (w-z-1)^{-1/2}=(-(z-z_b))^{-1/2} (cut = the
rightward ray; positive on the leftward ray — matches zeta<0 on (1/2,1):
zeta^{1/2}=+-i|zeta|^{1/2} on the two sides, pure imaginary, opposite signs).
Pole z_p excluded (it lies left of z_b, H hugs the cut with clearance <|eps|).

## C. Theorem A (pinch expansion) — statement + proof
THEOREM A. For 0<|eps|<=r, |arg eps|<=pi/2 (probe sector):
  F_loc(s) = c_p (s-rho)^{-1/2} (1 + E(s)),  |E(s)| <= C_A |s-rho|^{1/2},
  c_p := -2^{-z_*}/(z_* Z(rho)),   (principal branch of (s-rho)^{-1/2}),
with C_A explicit in (r, sup|a|, sup|a'|) [below]. c_p != 0 always (w4 model:
|c_p| = 2^{1/4}/(|z_*||Z(rho)|)).
PROOF. (1) Collapse: on the two sides of the cut (-(z-z_b))^{-1/2} takes values
+-i x^{-1/2} (above/below; computed from principal arg -> -+pi). Traversing H
(below: x 2r->0-ish... orientation in: below from 2r to 0, around, out above 0 to 2r):
int_H = int_below + cap + int_above = [value -i on lower edge, +i upper] =>
  F_loc(s) = -(1/pi) int_0^{2r} a(x,s) x^{-1/2} (x+eps)^{-1} dx
(cap around z_b: length 2pi delta * delta^{-1/2} -> 0). Sign fixed by direction:
lower edge traversed toward z_b contributes -int_0^{2r}(-i x^{-1/2})a/(x+eps)dx...
NUMERIC ARBITER N1 verifies loop=collapse to machine precision (below).
(2) Split a(x,s)=a(0,s)+(a(x,s)-a(0,s)); |a(x,s)-a(0,s)|<=M_a x, M_a:=sup|da/dx|:
  |int_0^{2r}(a-a(0))x^{-1/2}(x+eps)^{-1}dx| <= M_a int_0^{2r}x^{1/2}x^{-1}dx
  = 2 M_a (2r)^{1/2}      (|x+eps|>=x for Re eps>=0).
(3) Tail: int_0^{2r} x^{-1/2}(x+eps)^{-1}dx = pi eps^{-1/2} - T(eps),
  |T| = |int_{2r}^inf x^{-1/2}(x+eps)^{-1}dx| <= 2(2r)^{-1/2}  (Re eps>=0),
using int_0^inf x^{-1/2}(x+eps)^{-1}dx = pi eps^{-1/2} (Beta; principal branch,
valid |arg eps|<pi). (4) a(0,s)-a(0,rho) = O(A_1|eps|), A_1:=sup|d a(0,s)/ds|.
Assemble: F_loc = -(1/pi)[a(0,rho)pi eps^{-1/2} + O(A_1|eps|^{1/2}pi... )
 + O(2(2r)^{-1/2}|a|_inf) + O(2M_a(2r)^{1/2})]
= c_p eps^{-1/2}[1 + O(|eps|^{1/2}(2(2r)^{-1/2}|a|_inf + 2M_a(2r)^{1/2}
 + pi A_1 r ... )/(pi|c_p|))]. So C_A = (2(2r)^{-1/2}|a|_inf + 2M_a(2r)^{1/2})/(pi |c_p|) + A_1/|c_p| r^{1/2}-term. QED (constants pinned in numeric block; kappa=1/2).

## N1 RESULTS (num_a.py + orientation check) — THEOREM A VERIFIED
Orientation fix: H must be traversed IN ABOVE the cut (from z_b+2r+i0), cap
leftward around z_b, OUT BELOW (to z_b+2r-i0) — i.e. clockwise around z_b —
for F_loop = -(1/pi) int a x^{-1/2}(x+eps)^{-1} dx = collapse. Verified:
|loop-col|/|col| = 8.2e-2, 2.9e-2, 9.3e-3, 2.9e-3 at delta=1e-3..1e-6 (rate
O(sqrt delta) = the cap term, as the proof predicts); reversed orientation
gives -F (rel diff ~2, diagnosed). [Sign is a convention tied to the parent
contour; c0' below uses |c_p|^2 only. CONTRACT ITEM for P2.]
Pinch asymptotics (nonconstant test amplitudes b=1+0.3(v-1), Z=zp(1+0.2(v-rho))):
F_col*eps^{1/2}/c_p - 1 -> 0 along 4 rays |arg eps|<=0.99*pi/2; at |eps|=1e-8
agreement 1.6e-4; (ratio-1)/sqrt(eps) stabilizes at -1.6347+0.0409i = the C_A
constant (kappa=1/2 exact). c_p = -0.196925+0.078556i, |c_p| = 0.2120155
= 2^{1/4}/(|z_*||zeta'(rho1)|) with |z_*|=7.0718, |zeta'(rho1)|=0.79316. PASS.

## D. Theorem B (the exact weight dictionary + half-derivative restoration)
LEMMA B1 (Mellin image of multiplication by sqrt(log u)) — EXACT, with Gamma
constant. Let f: [1,inf)->C measurable, sigma_a in R, and suppose
int_1^inf |f(u)| u^{-sigma} du/u < inf for every sigma > sigma_a. Let
F(s) = int_1^inf f(u) u^{-s} du/u (analytic, Re s > sigma_a). Then for
Re s > sigma_a the RIGHT-WEYL half-derivative
   (D^{1/2}F)(s) := -(1/Gamma(1/2)) int_0^inf x^{-1/2} F'(s+x) dx
converges absolutely and equals the Mellin transform of (log u)^{1/2} f(u):
   (D^{1/2}F)(s) = int_1^inf f(u) (log u)^{1/2} u^{-s} du/u.
So: multiplication by (log u)^{1/2} on the u-side IS the Weyl fractional
derivative of order 1/2 on the Mellin side, with constant 1/Gamma(1/2)=1/sqrt(pi)
— NOT the Riemann-Liouville D^{1/2} (which differentiates from a finite base
point and has extra boundary terms); the Weyl (right-sided, base +inf) form is
the exact operator. PROOF. Kernel identity: for L>0,
   int_0^inf x^{-1/2} L e^{-Lx} dx = Gamma(1/2) L^{1/2}   (Gamma integral).
Take L = log u: (log u)^{1/2} = (1/Gamma(1/2)) int_0^inf x^{-1/2}(log u)u^{-x}dx.
Multiply by f(u)u^{-s}/u, integrate; Fubini is licensed by the positive majorant
|f(u)|(log u)u^{-Re s - x} whose double integral is finite for Re s > sigma_a
(inner x-integral first). The inner u-integral is -F'(s+x). QED.
LEMMA B2 (restoration of the full pole) — EXACT constant. For s-a not in
(-inf,0]: D^{1/2}[(s-a)^{-1/2}] = (1/sqrt(pi)) (s-a)^{-1}. PROOF. F'= -(1/2)
(s-a)^{-3/2}; int_0^inf x^{-1/2}(x+c)^{-3/2}dx = B(1/2,1) c^{-1} = 2/c
(principal branch, |arg c|<pi, by rotation of the ray + Cauchy); multiply by
(1/2)/Gamma(1/2). QED. [Dual check, densities: u^a/sqrt(pi log u) has Mellin
(s-a)^{-1/2}; times sqrt(log u) -> Mellin (1/sqrt pi)(s-a)^{-1}. Same constant.]
THEOREM B (transfer of the pinch singularity). Let F be analytic on
Omega := {0<|s-rho|<=r_1, |arg(s-rho)|<=pi/2} cup {Re s>Re rho, |Im s-Im gam...|<=r_1}
extended to the right ray domain Omega_+ := {s+x : s in window, x>=0} with
   F'(s) = -(c_p/2)(s-rho)^{-3/2} + O(min(|s-rho|,r_1)^{-1/2}) on Omega_+ near rho,
   |F'(sigma+it)| <= C_far (1+sigma)^{-3/2} for sigma-Re rho >= r_1  (far decay).
Then for s in the probe window (Re(s-rho)=h>0, |s-rho|<=r_1/2):
   (D^{1/2}F)(s) = (c_p/sqrt(pi)) (s-rho)^{-1} + O(log(1/|s-rho|)) + O(C_far).
PROOF. Split int_0^inf = int_0^{r_1/2} + int_{r_1/2}^inf. Far: bounded by
C_far' via the decay. Near: insert F' = main + error; main gives the B2
beta-integral up to a tail int_{r_1/2}^inf x^{-1/2}|x+eps|^{-3/2}dx = O(r_1^{-1});
error contributes int_0^{r_1/2} x^{-1/2}|eps+x|^{-1/2}dx <= 2 + log(r_1/|eps|)
(split at |eps|; |eps+x|>=max(x-|eps|, Re... for Re eps>0 |eps+x|>=x). QED.
[Relative error vs the main term |eps|^{-1}: O(|eps| log(1/|eps|)) — subordinate.]

## N2 RESULTS (num_b.py) — THEOREM B VERIFIED
B2 exact: |G/pred - 1| = 0.0 at working precision (two complex points).
Composition on the model F (analytic F' cross-checked vs numeric diff, 6e-11):
G*eps/(c_p/sqrt(pi)) - 1 = -2.9e-2 (eps 1e-2), -3.7e-3 (1e-3), -4.4e-4 (1e-4),
3.2e-4 (|eps|=7e-5 complex) — scaling = eps*log(1/eps) as Theorem B predicts.
FULL POLE RESTORED with constant c_p/sqrt(pi). PASS.

## E. Theorem C (L2 window bound and the model limsup) — statements + proofs
Model field (u-side, explicit; s1 := rho-1, probe line Re s' = -1/2+h):
  lambda_m(u) := -(1/pi) int_0^{2r} a(x) x^{-1/2} u^{s1-x} dx  (a(x):=a(x,rho) frozen),
  W_u := sqrt(log N_u) * 2 Re lambda_m(u),  N_u := u^2 (so sqrt(log N_u)=sqrt(2 log u)).
Facts (exact): lambda_m(u) = u^{s1} Amp(log u), Amp(L) = -(1/pi)int a x^{-1/2}e^{-Lx}dx
= c_p (pi L)^{-1/2} (1+O(1/L))  [the density dictionary "F=(s-a)^{-1/2} <->
u^a/sqrt(pi log u)" is now a THEOREM with error term]. Mellin closed forms:
  Mellin[(log u)^{1/2} u^{s1-x}](s') = Gamma(3/2) (s'-s1+x)^{-3/2}, so
  F_W(s') = sqrt2 (G+G_c),  G(s') = -(Gamma(3/2)/pi) int_0^{2r} a(x)x^{-1/2}(x+eps')^{-3/2}dx,
  G_c same with conj(a), s1 -> conj(s1);  eps' = s'-s1. Leading term of G:
  (c_p/sqrt(pi)) eps'^{-1} (consistent with Thm B — independent closed-form check).
THEOREM C1 (window bound). For 0<h<=r0<=r/4, r0 below gamma/2:
  int_{|t-gamma|<=r0} |F_W(-1/2+h+it)|^2 dt >= (2|c_p|^2/pi)(2/h)arctan(r0/h)(1-delta),
  delta = delta(r0) + O(h/r0) -> 0 as r0 -> 0 then h -> 0.  PROOF: on the window
|sqrt2 G| >= sqrt2|c_p|/(sqrt(pi)|eps'|) (1 - C|eps'|^{1/2}...) by Thm A/B expansion;
|sqrt2 G_c| <= C_c (distance to conj window >= 2gamma - r0 >= gamma); expand the
square, cross terms O(1/|eps'|) integrate to O(log(1/h)) = o(1/h); the main term
integrates to |2 c_p^2/pi|(2/h)arctan(r0/h). QED.
THEOREM C2 (machinery form = the L-105058.5 analogue; MODEL INSTANCE). Suppose
  limsup_T Q_W(T)/log T =: A < inf,  Q_W(T) := int_1^T u W_u^2 du/u. Then
  A >= c0' := (4/pi)|c_p|^2 = 4*sqrt2 / (pi |z_*|^2 |Z(rho)|^2).
PROOF (verbatim L-105058.5 steps (2)-(5) with W for m). (2) For A'>A:
J(h) := int (u^{1/2}W)^2 u^{-2h} du/u = 2h int Q_W(T)T^{-2h}dT/T <= A'/(2h)+O(1).
(3) |W_u| <= C u^{-1/2}(log 2u)^{1/2} pointwise (model; explicit), so the Mellin
integral of W converges ABSOLUTELY on every line Re s' = -1/2+h, h>0; F_W is
analytic on Re s'>-1/2 and equals the closed form above (uniqueness from the
abs-convergence half-plane); Mellin-Plancherel for phi_h(x)=W(e^x)e^{(1/2-h)x}
in L^2(0,inf):  J(h) = (1/2pi) int_R |F_W(-1/2+h+it)|^2 dt.  (4) Lower bound by
the TWO windows t ~ +-gamma (W real => symmetric moduli): by C1,
J(h) >= (2/2pi)(2|c_p|^2/pi)(2/h)arctan(r0/h)(1-delta) = (2|c_p|^2/pi)(1/h)(1-delta').
(5) Combine: A'/2 >= (2/pi)|c_p|^2 (1-delta'); h->0 then r0->0: A' >= (4/pi)|c_p|^2. QED.
THEOREM C3 (saturation — direct evaluation, model consistency): for THIS W the
limit exists: Q_W(T)/log T -> (4/pi)|c_p|^2 exactly (u^{1/2}W_u =
2 sqrt2 sqrt(L)|Amp(L)| cos(gamma L + phi(L)), L=log u; |Amp| ~ |c_p|(pi L)^{-1/2};
int cos^2 -> 1/2). So the C2 bound is SHARP in the one-zero model, as it must be
(mass = sum over zeros; one zero-pair present). Genuine-zeta analogue of c0':
with Z(rho)=zeta'(rho_1): c0' = 16 sqrt2/(pi(1/4+gamma_1^2)|zeta'(rho_1)|^2) = 0.05723
(vs L-105058.5's c_0 = 0.0159; ratio 8 sqrt2/pi = 3.60 — the weight's gain).
Robustness remark (floor cells): sqrt(log N_u) = sqrt(2 log u) + O((log u)^{-1/2})
changes F_W by Mellin[(log u)^{-1/2} lambda-type] = O(log(1/|eps'|)) — subordinate
to the eps'^{-1} pole; C1/C2 survive with the same constant.

## N3 RESULTS (num_c.py mpmath + num_c2.py numpy) — THEOREM C VERIFIED
Closed-form identity: (4/pi)|c_p|^2 = 16 sqrt2/(pi(1/4+gamma_1^2)|zeta'(rho_1)|^2)
= 0.0572328 (both evaluations agree to 6 digits).
N3a density dictionary: Amp(L)sqrt(pi L)/c_p - 1 = -2.96e-2, -5.9e-3, -5.9e-4,
-5.9e-5 at L=20,1e2,1e3,1e4 — exactly O(1/L). PASS.
N3b limsup: (Q_W/log T)/c0' = 0.88227, 0.96240, 0.98864, 0.99664, 0.99903 at
log T = 50..12800 — converges to 1 (saturation, Thm C3), 3 digits. PASS.
N3d window 1/h law: I/pred = 0.90612, 0.98523, 0.99798, 0.99974 at h=1e-2..1e-5;
h*I -> 2|c_p|^2 = 0.08990 (measured 0.08988 at h=1e-5). PASS, 3+ digits.

## F. TRANSFER CONTRACT (genuine-zeta inputs the model proof consumed; for lane P2)
The model theorems A,B,C1,C2 hold verbatim with kernel k(z) analytic on
D(z_*,4r), k(z_*)!=0 (here k=2^{-z}/z; c_p = -k(z_*)b(1)/Z(rho); if w1's final
Perron kernel differs — dz/z^2, 1/ln2 factors — only c_p rescales, mechanism
and exponents unchanged). Inputs to supply for genuine zeta:
(I1) zeta(v)^{1/2} = (v-1)^{-1/2} b(v), b analytic nonvanishing on D(1,1/2),
     b(1)=1. UNCONDITIONAL (zero-free rectangle below gamma_1; zeta<0 on (0,1)).
(I2) zeta(v) = (v-rho_1) Z(v), Z analytic nonvanishing on D(rho_1,1/2),
     Z(rho_1)=zeta'(rho_1)=0.79316...!=0. Inputs: zero-free punctured disk
     (rigorous numerics, same as L-105058.5(4)) + SIMPLICITY (rigorous numerics).
     FALLBACK without simplicity: multiplicity m>=2 gives collapsed factor
     (x+eps)^{-m}: raw pinch eps^{1/2-m}, weighted eps^{-m}, window blowup
     h^{1-2m} >= h^{-1} — machinery still fires; constant then explicit in
     zeta^{(m)}(rho_1)/m!. Same fallback shape as L-105058.5.
(I3) k(z)=2^{-z}/z analytic nonvanishing near z_*=(rho_1-1)/2: unconditional.
(I4) [= w1, THE remaining glue, NOT proved here] the representation
     F_lambda,global(s) = sigma*F_loc(s) + F_reg(s), sigma in {+-1} fixed by the
     parent Perron contour orientation (Hankel arc convention: IN above the cut,
     around z_b, OUT below), F_reg analytic and bounded on the window
     {|s-rho_1|<=r_1, Re(s-rho_1)>0}, uniformly; identification of F_lambda as
     the Mellin transform of the actual tent field lambda_u = Lambda(X_u)/u with
     floor(U)-cell corrections subordinate; far-ray control |F'(sigma+it)| <<
     (1+sigma)^{-3/2} on the Weyl ray (mild: abs-convergence region).
(I5) [= w3] hypothesis side: J_W(h)<inf from the contradiction hypothesis
     (L-105058.5(2), pure real analysis) + |h_U(n)| <<_eps n^eps (unconditional)
     for the CS/absolute-convergence and Plancherel steps — verbatim transfer.
(I6) window radius r0 < min(gamma_1, (gamma_2-gamma_1))/2; other zeros' pinch
     points live at |t - gamma_k|, enter only F_reg — P2's domain must exclude them.
(I7) weight robustness: sqrt(log N_u) = sqrt(2 log u) + O((log u)^{-1/2}) —
     the correction's Mellin image is O(log(1/|eps|)): subordinate (proved, Thm C).
NO RH ANYWHERE. RH never claimed. The "zeta nonzero Re>1/2"-type statements are
derived en route inside the reductio (as in L-105058.5), never assumed.

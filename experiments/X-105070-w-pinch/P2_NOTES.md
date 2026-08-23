# LANE P2: continuation (w1) + hypothesis-side transfer (w3)
PLAN (10 lines):
1. Read T-105059 (tent reduction, W-pinch pin), L-105058.5/.4, E1 NOTES.
2. Pin the EXACT single-variable object: W_u, its Dirichlet-series form, diagonal N=N(u) issue (trap ii).
3. Decide formulation: u-side vs X-side vs octave-integrated; pick one matching T-105059.5 consumption.
4. w3 skeleton: negate limsup => J_W(h) <= A'/(2h); Abel/partial-integration for W-object; H2/PW boundary Plancherel.
5. w3 window step: Cauchy-Schwarz on gamma_1-window => boundary mass <= C*A'*(window length) = O(h log(1/h)).
6. w1: continuation of F(s) past the cut; bound far-cut, other zeros, z=0 pole uniformly in window (classical zeta only).
7. Interface to P1: cite model expansion (s-rho)^{-1/2} + half-derivative restoration => window mass >= c/h.
8. Numerics: J_W(h) vs Plancherel image at h=0.02, 0.01; window mass vs c/h prediction.
9. Iterate on any breakage (esp. trap ii); log failed attempts inline.
10. Final: transfer theorem modulo P1 interfaces, or precise repair + remainder.

## STEP 2-3: EXACT OBJECT PINNED + FORMULATION (trap ii RESOLVED, no repair needed at consumption level)
Convention (X-side). V(X) := Lambda(X) sqrt(log N_X) X^{-1/6} for X>=64, V:=0 for X<64.
FACT F1 (exact change of variables): with u := X^{1/3} CONTINUOUS in the pinned W_u
(U_X=floor(u) inside Lambda), u W_u^2 du/u = (1/3) V(X)^2 dX/X, hence
  limsup_T (1/log T) int_1^T u W_u^2 du/u  =  limsup_Y (1/log Y) int_1^Y V^2 dX/X.
So the pinned target == TARGET(V): limsup_Y (1/log Y) int_1^Y V^2 dX/X >= c_0'.
FACT F2 (consumption check, exact): Lambda^2 = V^2 X^{1/3}/log N_X identically; if io octaves L have
int_oct V^2 dX/X >= (c_0'-eps)ln2 (Cor-2 argument), then by T-105059.5
E(L) >= 2ln2 int_oct Lambda^2 dX/X >= 3ln2(c_0'-eps)(1+o(1)) 2^{L/3}/L io. VERIFIED symbolically.

Smoothing Lemma A0 (formulation bridge; to prove at deposit rigor): define
  Lambda*(X) := sum_n n^{-1/2} v(n X^{-2/3}) sum_{de=n, d>X^{1/3}} mu(d) eta(e),
  v(y) = (ln(2y)/ln2) 1_{(1/2,1]}(y),  V*(X) := Lambda*(X) sqrt((2/3)log X) X^{-1/6}.
Then int_64^inf (V - V*)^2 dX/X < infinity. Sources: (i) v-arg U_X -> X^{1/3} (Lipschitz away
from jump; error per X << log X in Lambda); (ii) jump n<=N_X vs n<=X^{2/3}: short-interval
divisor sum << sqrt(x) log x at x=X^{2/3} => Lambda-err << log X; (iii) sqrt(log N) vs
sqrt((2/3)log X): rel err O(X^{-1/3}); (iv) cube-integer boundary d=X^{1/3}: measure-summable.
Each gives V-err << X^{-1/6+eps} => L2(dX/X)-finite. COROLLARY: TARGET(V) <=> TARGET(V*)
(CS: |sqrt(int V^2) - sqrt(int V*^2)| <= O(1)); also Q_V <= A'logY => Q_{V*} <= A'logY + O(sqrt(logY)).

## STEP 3b: EXACT DOUBLE-DIRICHLET REPRESENTATION (the diagonal restriction admits one)
Fix d>e (else empty): X-support of the (d,e)-term = [(de)^{3/2}, min(d^3,(2de)^{3/2})).
Substitute X = (de t)^{3/2}:
  G*(s) := int_64^inf V*(X) X^{-s} dX/X
        = (3/2)sqrt(2/3)sqrt(3/2) sum_{d>e} mu(d)eta(e) (de)^{-3/4-(3/2)s}
          int_1^{min(2,d/e)} v(1/t) sqrt(log(de t)) t^{-1/4-(3/2)s} dt/t   [+O_64 head corr]
ABS CONV for Re s > 1/6 (matches X-side |V*| << X^{1/6+eps} threshold — consistency check).
[constants: (3/2) from dX/X=(3/2)dt/t; sqrt(2/3) from weight; sqrt(3/2) folded INTO sqrt(log(det))
 rewriting sqrt((2/3)logX)=sqrt((2/3)(3/2)log(det))=sqrt(log(det)). So prefactor = 3/2.]
Half-derivative rep (exact): sqrt(L) = -(1/(2sqrt(pi))) int_0^inf (e^{-dL}... ) i.e.
  sqrt(log m) = -(1/(2sqrt(pi))) int_0^inf (m^{-del} - 1) del^{-3/2} d del  (Gamma(-1/2)=-2sqrt(pi))
applied to m = de*t: factorizes under the del-integral. Ratio-kernel z-Perron on d/e then gives
  sum_{d>e} mu(d)eta(e)(de)^{-a} kap(beta; d/e) = (1/2pi i)int kap^(beta,z) zeta^{1/2}(a+z)/zeta(a-z) dz,
kap(beta;r) := int_1^{min(2,r)} v(1/t) t^{-1/4-beta} dt/t (0 for r<=1, const for r>=2; C^0 piecewise C^1).
PINCH GEOMETRY (calibration verified): with a = 3/4+(3/2)s+del: pole of 1/zeta(a-z) at z_p = a - rho;
branch of zeta^{1/2}(a+z) at z_b = 1-a; z_p - z_b = 2a - 1 - rho = 3(s - i gamma_1/3) + 2 del + 3h-part
at rho=rho_1, s = h+it near t = gamma_1/3. Pinch point z* = 1/4 - i gamma_1/2 (|z*|=7.075).
Raw singularity (s - i gamma_1/3)^{-1/2}; half-derivative (del-integral) => full pole. Window at
t = +-gamma_1/3 on lines Re s = h -> 0+. Other zeros: z_p(rho_j) at O(1) z-distance (t bounded in
window; gamma_2 - gamma_1 = 6.9 => separation ~ 2.3 in s, ~6.9 in z): NO density input needed.

## STEP 4: TRANSFER THEOREM (w3) — statement skeleton (proof to THEOREM.md)
Hyp (H-neg): A := limsup_Y (1/logY) int_1^Y V^2 dX/X < c_0'; fix A<A'<c_0'.
(1) Q_V(Y) <= A' logY (Y>=Y_0); same for V* + O(sqrt(logY)) [A0].
(2) J(h) := int (V*)^2 X^{-2h} dX/X = 2h int Q_{V*}(Y) Y^{-2h} dY/Y <= A'/(2h)+O(1) (h in (0,1/2);
    boundary term Q Y^{-2h} -> 0 BY (1), not by trivial bounds).
(3) CS: int |V*| X^{-sig} dX/X <= J(h')^{1/2} (int X^{2h'-2sig} dX/X)^{1/2} < inf for sig>h'>0;
    all sig>0 => G* analytic on Re s > 0 (abs-conv integral). Identity thm vs step-3b formula
    on Re s > 1/6 => the explicit object CONTINUES to Re s > 0 under (H-neg).
(4) PW/Plancherel: psi_h(x) := V*(e^x) e^{-hx} in L2(0,inf), Mellin abs conv ON line Re s=h
    (use h'=h/2), so hat(psi_h)(t) = G*(h+it) ptwise and J(h) = (1/2pi) int_R |G*(h+it)|^2 dt.
(5) Window Schwarz: int_{|t-gamma_1/3|<=r_0} |G*(h+it)|^2 dt <= 2pi J(h) <= pi A'/h + O(1).
(6) [P1 INTERFACE] window blow-up: int_{|t-gamma_1/3|<=r_0}|G*(h+it)|^2 dt >= (1-o(1)) pi |c_P|^2/h
    => A' >= |c_P|^2(1-o(1)) => c_0' := |c_P|^2 (per window; x2 using both +-gamma_1/3 as in .5(4)).

## FINAL STATUS (deliverable: THEOREM.md, 309 lines; num1-5.py replays)
PROVED: P2.1 (pinned W-target == X-side TARGET(V), exact; consumption into T-105059.5 verified
symbolically, 3ln2(c0'-eps)2^{L/3}/(L+1)); P2.2 (floor-smoothing L2-bridge; d-cutoff exact,
only weight+v-argument corrections, all L2(dX/X)-summable; numeric decay X^{-0.46});
P2.3 (EXACT double-Dirichlet rep of the diagonal object, abs conv Re s>1/6; verified 7e-17);
P2.4 (half-derivative operator identity G*=sqrt(2/3)D_half[B_0]; D_half[(s-a)^{-1/2}]=
(1/sqrt pi)(s-a)^{-1} exact; boundedness lemma 3M/sqrt(pi)); P2.5 (z-rep with kernel
k(beta)=1/beta-(1-2^{-beta})/(beta^2 ln2), pinch gap z_p-z_b=3(s-i gamma_1/3), pinch point
z*=1/4-i gamma_1/2, kernel factor k(1/2)=0.309778, O(1) separation of all other singularities);
P2.7 TRANSFER THEOREM modulo [P1-LOC]+[P2-FAR]: full L-105058.5-architecture reductio with
c_0' = (4/3pi)|c_B|^2, predicted 9.71e-4 with |c_B|=(3/2)k(1/2)/(sqrt3|z*||zeta'(rho_1)|)=0.04783.
NUMERICS: Plancherel ratio 1.000000 (h=0.02,0.01, pair-formula cross-check); window peak at
4.785~gamma_1/3+O(1/logXc); predicted pole mass 0.0153 vs measured 0.0146 (COEFFICIENT MATCH);
corner pairs (d/e near 1,2): 77% raw mean square, 3.5% window mass (far-field spectrally flat).
NOT CLOSED: [P2-FAR] (far z-field bound) — obstruction: 1/zeta(a-z) at Re~3/4, unbounded
heights, unconditionally uncontrollable pointwise/L1/L2 on any fixed strip line; dlVP-hugging
blocked by zeta^{1/2} branch points at unknown off-line zeros. Routes: (R1) corner/Delta-
statistics arithmetic route (Hooley-Tenenbaum Delta^2 moments + MV, eps_1-absorption; numerics
strongly favorable); (R2) reductio-L2 through D_half (one log short by naive pointwise route;
L2-multiplier refinement open). [P1-LOC] calibration delivered: coefficient shape + magnitude.

# DEFORM — the P2.5 -> Z_loc contour deformation (stage 1 of the [P1-LOC-WELD] residue)

Scope: write the explicit deformation producing Z_loc from P2.5's vertical contour, with full
singularity inventory and connecting-arc estimates. Hypothesis VERIFICATION (Theorem A's
amplitude bounds) is stage 2; nothing here is numeric beyond quoted certified constants.
Allowed inputs only: (A1) all zeta zeros with |Im| <= 60 lie on Re = 1/2 and are simple
(verified classical computation); (A2) zeta^{1/2} bounded on compact cut regions; plus
elementary facts (Euler product nonvanishing Re > 1; zeta ~ (v-1)^{-1}). NO RH, no zero-free
half-plane, no density estimates, no unverified zero data.

## D0. Restatement of the parent objects (verbatim refs)

P2.5 (P2_transfer_theorem.md L138-141): for Re s > 1/6 and any 0 < c < (3/2)Re s - 1/4,

    B_0(s) = H_0(s) + (1/2 pi i) int_{Re z = c} Psi(z, s) dz,
    Psi(z, s) := (3/2) k(beta_z) zeta^{1/2}(a+z) / ( z * zeta(a-z) ),

with (P2.5, L127-129) a := 3/4 + (3/2)s, beta_z := 1/4 + (3/2)s + z (the kernel argument),
k(beta) := 1/beta - (1-2^{-beta})/(beta^2 ln 2), and H_0 entire with H_0, H_0' bounded on
{Re s >= 0, |Im s| <= 20} (P2.5, L134-137). Orientation: upward Mellin-inversion line
(c - i inf -> c + i inf), P2.5 proof L159-162.

z-plane singularity inventory named by P2.5 (L144-157), for s near s_0 := i gamma_1/3:
  - kernel pole z = 0 (from the 1/z of hat kap_0(z) = (1/z) k(beta_z), P2.5 L161);
  - branch point of zeta^{1/2}(a+z) at z_b := 1 - a = 1/4 - (3/2)s;
  - poles of 1/zeta(a-z) at z_p(rho) := a - rho, each simple for verified simple rho;
  - THE PINCH IDENTITY (P2.5 L148): z_p(rho_1) - z_b = 2a - 1 - rho_1 = 3(s - s_0) =: eps,
    rho_1 = 1/2 + i gamma_1, gamma_1 = 14.134725141734693; pinch point
    z* := 1/4 - i gamma_1/2 = z_b(s_0) = z_p(rho_1)(s_0), |z*| = 7.0718;
  - kernel argument on the pinch: beta at z*, s_0 equals 1/2; k(1/2) = 0.309778 != 0.
Separations (P2.5 L154-157): z_p(rho_2) at distance > 6 from z*, z_p(bar rho_1) > 13,
z = 0 at |z*| = 7.07; all uniform for |Im s - gamma_1/3| <= r_0 <= 1.

P2.6 (L172-176): split the contour at |Im z| = Z_0 := 40; deform the |Im z| <= Z_0 piece
across the branch point as it crosses (Re z_b = 1/4 - (3/2)Re s > c once Re s < 1/6),
producing a cut-hugging loop; write B_0 = H_0 + Z_loc + Z_far. Domains: Omega(r_0) :=
{0 < Re s <= 1/4, |Im s - gamma_1/3| <= r_0}, Omega^+ := Omega ∪ {Re s > 1/4,
|Im s - gamma_1/3| <= r_0}. Target interface (T-105070 SS2, L86-88): r_0 in (0,1], M_loc with
Z_loc(s) = c_B (s - s_0)^{-1/2} + R_loc(s), |R_loc| + |R_loc'| <= M_loc on Omega^+,
c_B = (3/2) k(1/2) / (sqrt3 |z*| |zeta'(rho_1)|) in modulus = 0.04782893516094 (CPINCH W4).

## D0.b Branch specification (pinned once, used throughout)

(i) k is ENTIRE: 1 - 2^{-beta} = beta ln2 - beta^2 ln^2(2)/2 + beta^3 ln^3(2)/6 - ..., so
(1-2^{-beta})/(beta^2 ln 2) = 1/beta - (ln 2)/2 + beta (ln 2)^2/6 - ..., hence
k(beta) = (ln 2)/2 - beta (ln 2)^2/6 + ... : the apparent beta = 0 denominator zeros are
REMOVABLE; k has NO poles. The only kernel singularity of k(beta_z)/z is the simple pole
z = 0, residue k(1/4 + (3/2)s). ["zeros of the beta-map denominator": none survive.]
(ii) Cut of zeta^{1/2}(a+z): in the v = a + z plane take the classical cut
v in (-inf, 1]; in z this is the LEFTWARD horizontal ray L(s) := {z_b - x : x >= 0}
(height Im z_b = -(3/2) Im s ~ -gamma_1/2). This single cut absorbs the v = 1 branch point
AND all trivial-zero branch points v = -2n (they sit on the ray at x = 3 + 2(n-1) + h-shift,
i.e. x >= 3, far beyond the hug). Factor: zeta^{1/2}(a+z) = (z - z_b)^{-1/2} b(a+z),
b(v) := ((v-1) zeta(v))^{1/2}, principal branch of (z-z_b)^{-1/2} (positive for z - z_b > 0),
b > 0 on real v > 1; this matches the Dirichlet-series branch on Re(a+z) > 1 (both positive
on the real direction, continuation through the connected overlap). b is analytic and
nonvanishing on V_b := {0.2 < Re v < 1.3, |Im v| < 4}: (v-1)zeta(v) -> 1 at v = 1, and
zeta != 0 on V_b by (A1) (any zero there has |Im| <= 60 and Re != 1/2 for Re v > 1/2-part;
below-height-14 there are no zeros at all by the verified list; real v in (0,1): a real zero
would be an off-line zero of height 0 <= 60, excluded by (A1); Re v >= 1: Euler product for
Re v > 1, and Re v = 1, |Im v| < 4 excluded by (A1) likewise). b(1) = 1.
(iii) Other branch points of zeta^{1/2}(a+z) ("partner branch points"): z'(rho) := rho - a,
one per zero; verified ones sit at Re z' = Re rho - 3/4 - (3/2)Re s = -1/4 - (3/2)Re s
(on-line zeros), with auxiliary cuts chosen leftward horizontal from each z'. Unverified
zeros (|Im rho| > 60) give |Im z'| = |Im rho - (3/2)Im s| >= 60 - 8.6 > 51 — outside the
|Im z| <= 40 strip entirely.
(iv) Zero factor: Z_1(w) := zeta(rho_1 + w)/w, analytic, Z_1(0) = zeta'(rho_1) (simplicity
of rho_1 = (A1)); Z_1 != 0 on {Re w > 0, |Im w| <= 3 + 1/4} by (A1) (argument rho_1 + w has
Re > 1/2, height in [11.1, 17.4] <= 60).
(v) Note z = a - 1 = -z_b is a ZERO of Psi (pole of zeta(a-z)), not a singularity.

## D1. The homotopy

ANCHOR BAND A := {5/24 < Re s <= 1/4, |Im s - gamma_1/3| <= r_0}, r_0 := 1 (the maximal
SS2 value; all clearances below are checked at r_0 = 1). Fix c := 1/16. On A:
0 < c < (3/2)Re s - 1/4 (needs Re s > 5/24), so P2.5's representation holds with this c, and
on Re z = 1/16 both Re(a-z) = 11/16 + (3/2)Re s > 1 and Re(a+z) = 13/16 + (3/2)Re s > 1:
the integrand is series-defined, single-valued, absolutely integrable (|Psi| << |Im z|^{-2}).

Contours (all pieces oriented bottom-to-top along the parent direction). Parameters:
Z_0 = 40, hug length 2r := 1/4, dodge half-height Y_loc := 2, left excursion to
Re z = Re z_b - 2r. Write mu_b := Im z_b = -(3/2) Im s (in [-8.6, -5.6] on A ∪ Omega^+).

  Gamma_far  : Re z = 1/16, |Im z| >= Z_0 (two rays; unchanged).
  V_low(s)   : Re z = 1/16, Im z in [-Z_0, mu_b - Y_loc].
  B_out(s)   : horizontal from 1/16 + i(mu_b - Y_loc) left to (Re z_b - 2r) + i(mu_b - Y_loc),
               then vertical up to z_b - 2r (approaching the LOWER edge of the cut).
  H(s)       : Hankel hug: along the lower edge z = z_b - x - i0 with x: 2r -> 0, around z_b
               (circle radius delta -> 0, counterclockwise, passing right), back along the
               upper edge z = z_b - x + i0 with x: 0 -> 2r.
  B_back(s)  : vertical from z_b - 2r (upper side) up to (Re z_b - 2r) + i(mu_b + Y_loc),
               then horizontal right to 1/16 + i(mu_b + Y_loc).
  V_up(s)    : Re z = 1/16, Im z in [mu_b + Y_loc, Z_0].

CLAIM (deformation identity on A): with S := {Re z = 1/16, Im z in [mu_b - Y_loc, mu_b + Y_loc]},

    int_S Psi dz = int_{B_out ∪ H ∪ B_back} Psi dz.

Proof. The two paths cobound the slit rectangle R_sweep := [Re z_b - 2r, 1/16] x
[mu_b - Y_loc, mu_b + Y_loc] minus the slit {z_b - x : 0 <= x <= 2r}. Psi is analytic on
R_sweep minus the slit; the homotopy avoids the slit (the hug wraps it) and R_sweep contains
NO other singularity of Psi, by the audit below. Cauchy's theorem on the slit rectangle
(with the delta-cap; cap estimate below) gives the identity. QED.

SWEPT-REGION SINGULARITY AUDIT (at anchor, uniform over A; heights of R_sweep are within
[mu_b - 2, mu_b + 2] subset [-10.6, -3.6]; Re within [-3/8, 1/16]):
  (1) z = 0: height 0 not in [-10.6, -3.6]. OUT.
  (2) z_b and its cut, x in [0, 2r]: WRAPPED by H (not crossed); cut x > 2r: Re < Re z_b - 2r,
      left of R_sweep. OUT of the open sweep.
  (3) z_p(rho_1) = 1/4 + (3/2)s - i gamma_1: Re = 1/4 + (3/2)Re s >= 9/16 > 1/16. OUT (right).
  (4) z_p(rho_2): height (3/2)Im s - gamma_2 in [-15.4, -12.5]; below -10.6. OUT.
  (5) z_p(bar rho_1): height ~ +21.2. OUT. All other z_p(rho_k), heights listed in D1.b. OUT.
  (6) trivial-zero poles z = a + 2n: Re >= 2.75. OUT (right).
  (7) partner branch points z'(rho_k): Re = -1/4 - (3/2)Re s <= -9/16 < -3/8, and nearest
      height (z'(rho_1) ~ +7.07) outside the band anyway; their leftward cuts keep
      Re <= -9/16. OUT (left).
  (8) zeros of zeta(a - z) other than via (3)-(6): on R_sweep, Re(a-z) = 3/4 + (3/2)Re s
      - Re z > 3/4 + 5/16 - 1/16 = 1 (strict since Re s > 5/24): Euler product, no zeros. NONE.
  (9) branch ambiguity of zeta^{1/2}(a+z) inside R_sweep: v-image has Re v in [3/4, 1.19],
      |Im(v-1)| <= 2, inside V_b of D0.b(ii) minus the cut: single-valued, b-factorized. OK.
So: ZERO crossed poles, zero residues picked up; the only nonclassical object met is the
wrapped cut. The deformation identity holds for every s in A, and each piece-integral is
analytic in s on A (integrand jointly analytic, contours moving analytically with s,
uniform local majorants on compact pieces).

## D1.b Full inventory, strip |Im z| <= Z_0 = 40 (the local bookkeeping region), s in Omega^+

Poles of 1/zeta(a-z) from nontrivial verified zeros, z_p(rho) = a - rho, all at
Re z_p = 1/4 + (3/2)Re s (on-line zeros), heights (3/2)Im s - gamma_rho with
(3/2)Im s in [(3/2)(gamma_1/3 - r_0), (3/2)(gamma_1/3 + r_0)] = [5.57, 8.57] (r_0 = 1):
a height |.| <= 40 forces gamma_rho in [-34.4, 48.6], i.e. gamma_rho in
{14.13, 21.02, 25.01, 30.42, 32.94, 37.59, 40.92, 43.33, 48.01} (9 upper zeros) and
conjugates {-14.13, -21.02, -25.01, -30.42, -32.94} (5 lower, |gamma| <= 34.4):
14 simple poles, ALL with |Im rho| <= 60, hence verified on-line and simple ((A1)); all at
Re z_p > 1/4 > 1/16: strictly RIGHT of every contour piece, never crossed, never enclosed.
Only z_p(rho_1) approaches the contour: its distance to the hug endpoint z_b is exactly
|eps| = 3|s - s_0| (the pinch); for s in Omega^+, Re eps = 3 Re s > 0 keeps it off the cut
and off H. Nearest other pole to z*: z_p(rho_2), distance >= 6 (P2.5 L156).
Trivial-zero poles z = a + 2n, n >= 1: Re >= 2.75, height (3/2)Im s ~ +7.07: right of
everything, inert. Partner branch points z'(rho) = rho - a with |Im z'| <= 40: gamma_rho in
[-34.4, 48.6]: again 9 + 5 = 14 points, all verified, at Re z' = -1/4 - (3/2)Re s, LEFT of all
contours, auxiliary cuts leftward: inert. Kernel pole z = 0: left of Gamma at height 0,
never crossed: inert. UNVERIFIED zeros (|Im rho| > 60): their poles z_p AND branch points z'
have |Im z| >= 60 - 8.6 = 51.4 > 40: they live entirely in the Gamma_far region — DELEGATED
TO Z_far. This is the precise sense in which the local region consumes only bounded-height
classical inputs. COUNT: within the strip, 1 kernel pole + 1 pinch branch point/cut +
14 verified nontrivial-zero poles + ~14 partner branch points + countably many trivial-zero
poles (inert, Re >= 2.75) + trivial partner branch points absorbed on L(s) (x >= 3).
Contributions from the homotopy: cut integral (wrapped) = Z_loc; ALL residues: none crossed,
all zero.

## D1.c Connecting-arc and tail estimates (explicit)

(E1) Cap collapse. On the delta-circle around z_b: |(z-z_b)^{-1/2}| = delta^{-1/2}; the
amplitude factors are bounded by M_A(s) := sup_{|z-z_b|<=delta} (3/2)|k(beta_z) b(a+z)| /
(|z| |Z_1(a-z-rho_1)|) * |a - z - rho_1|^{-1} <= C_amp / (3h - delta) for delta < 3h/2
(|a - z - rho_1| = |eps + (z_b - z)| >= 3h - delta), C_amp := (3/2) sup|k b| / (inf|z| inf|Z_1|)
on the fixed compact neighborhood. Cap length 2 pi delta:
|cap| <= 2 pi delta * delta^{-1/2} * C_amp/(3h - delta) = O(delta^{1/2}/h) -> 0 (delta -> 0)
at every fixed s with h = Re s > 0. So the hug collapses to the two-edge cut integral.
(E2) Far tail (anchor band; rate 1/T). On Re z = 1/16, |Im z| >= T >= Z_0: with
sigma_+ := 13/16 + (3/2)Re s > 1, sigma_- := 11/16 + (3/2)Re s > 1 on A:
|zeta^{1/2}(a+z)| <= zeta(sigma_+)^{1/2}, |1/zeta(a-z)| <= zeta(sigma_-)/zeta(2 sigma_-),
|k(beta_z)| <= 1/|Im beta_z| + (1 + 2^{-Re beta_z})/(ln2 |Im beta_z|^2) with |Im beta_z| >=
|Im z| - 8.6 >= 31.4, hence <= 1/31.4 + 1.65/(ln2 * 31.4^2) = 0.0345 <= 2/|Im z| at |Im z| >= 40,
|1/z| <= 1/|Im z|. Hence |Psi| <= 3 zeta(sigma_+)^{1/2} (zeta(sigma_-)/zeta(2 sigma_-))
/ |Im z|^2 and int_{|Im z|>=T} |Psi| |dz| <= 6 zeta(sigma_+)^{1/2} zeta(sigma_-)
zeta(2 sigma_-)^{-1} / T. Decay rate O(1/T); at T = Z_0 = 40 this is the Z_far anchor bound.
(E3) Connecting pieces (window part, s in Omega closure, h <= 1/4). On V_low/V_up:
v = a + z has Re v = 13/16 + (3/2)h in [13/16, 19/16], |Im v| <= 48.6, and
dist(v, {zeros}) >= Re v - 1/2 >= 5/16 (all zeros at these heights are on Re = 1/2 by (A1));
same for w = a - z: Re w = 11/16 + (3/2)h, dist >= 3/16; both compact regions, zeta^{1/2}
bounded there by (A2), 1/zeta bounded by (A1)+compactness. With S_+ := sup|zeta^{1/2}(v)|,
S_- := sup|1/zeta(w)| over those compacts, |k(beta_z)/z| <= K_V := sup over the two segments
(|z| >= 1/16, |beta| bounded): |int_{V_low ∪ V_up} Psi dz| <= (3/2)(2 Z_0) K_V S_+ S_- / (2 pi)
-- explicit shape, finite, h-uniform. On B_out/B_back: lengths <= (1/16 - Re z_b + 2r) + Y_loc
<= 0.7 + 2 (window), v-image has Re v in [3/4, 1.19], |Im(v-1)| <= 2 (inside V_b, single
branch, b bounded), w-image has Re w >= 11/16 with dist(w, rho_1) >= 2r = 1/4 and all other
zeros at distance > 4: integrand bounded by the same compact-sup shape. All four connecting
pieces are analytic in s and bounded UNIFORMLY on Omega closure minus {Re s = 0}; on the ray
Re s > 1/4 the horizontals lengthen like (3/2)Re s but k(beta_z) ~ 1/beta decays along them
(|beta_z| ~ |z - z_b| there) and 1/|z| ~ 1/((3/2)Re s): the piece-integrals stay bounded,
with bound shape (log growth of int dt/(1/2+t)) * (1/max(dist, |Im z_b|)) -> 0. [Full
quantitative ray bounds = stage 2; no singularity is ever approached on the ray: z_p moves
right, z_b and the partner cuts move left in parallel at heights that never coincide.]

## D2. Result: Z_loc as a compact cut integral; the split, pinned

Collapsing H(s) (E1) and computing the edge values with D0.b's branches: on z = z_b - x,
beta_z = 1/4 + (3/2)s + z_b - x = 1/2 - x EXACTLY (s-independent; this is why the pinch
carries k(1/2) for every zero), a + z = 1 - x, a - z = rho_1 + eps + x with eps = 3(s - s_0);
(z - z_b)^{-1/2} = -i x^{-1/2} (upper edge), +i x^{-1/2} (lower edge). The bottom-to-top
parent orientation forces in-below/out-above (counterclockwise) and gives

    Z_loc(s) := (1/2 pi i) int_{H(s)} Psi dz
             = (3/(2 pi)) int_0^{1/4} A(x, s) x^{-1/2} (x + 3(s - s_0))^{-1} dx,        (Z)

    A(x, s) := k(1/2 - x) b(1 - x) / ( (z_b(s) - x) Z_1(3(s - s_0) + x) ),

k as in D0 (entire), b(v) = ((v-1) zeta(v))^{1/2} (D0.b(ii), b(1) = 1), Z_1(w) =
zeta(rho_1 + w)/w (D0.b(iv), Z_1(0) = zeta'(rho_1)), z_b(s) = 1/4 - (3/2)s. The arc is the
COMPACT segment K(s) = {z_b(s) - x : 0 <= x <= 1/4} (two edges); for s in Omega,
K(s) subset D(z*, 2) (|z_b - z*| = (3/2)|s - s_0| <= 1.55, plus length 1/4).
ANALYTICITY on Omega^+: the only s-singularity of (Z) is 3(s-s_0) in (-1/4, 0], i.e.
Re s <= 0 — excluded; z_b(s) - x != 0 (|Im| >= 5.57); Z_1(eps + x) != 0 (D0.b(iv), plus
Euler product for Re s large); b, k fixed. So Z_loc is UNCONDITIONALLY defined and analytic
on all of Omega^+ (both the window and the ray), bounded as Re s -> inf (A -> 0 like 1/|z_b|).
LEADING TERM (frozen amplitude x = 0, s = s_0, plus int_0^inf x^{-1/2}(x+eps)^{-1} dx =
pi eps^{-1/2}, principal branch, Re eps > 0):

    Z_loc(s) = (sqrt3/2) [k(1/2) / (z* zeta'(rho_1))] (s - s_0)^{-1/2} + R_loc(s),

i.e. SS2's c_B with omega = +1 PINNED by this deformation (branch conventions of D0.b:
principal (s-s_0)^{-1/2} on Re(s-s_0) > 0, b > 0 on v > 1, upward parent contour);
|c_B| = (3/2) k(1/2) / (sqrt3 |z*| |zeta'(rho_1)|) = 0.04782893516094 — exactly CPINCH W4's
certified value. Stage 2's task: Theorem A's amplitude-regularity hypotheses on A(x, s)
(analyticity in x on [0, 1/4] nbhd, sup|A|, sup|dA/dx|, sup|dA(0,s)/ds| on Omega^+), which
by (A1)/(A2) are compact-region checks; then R_loc-boundedness follows from P1 Thm A +
(E3)-type bounds.

THE SPLIT, PINNED. For s in the anchor band A (and, by the same convergence, all
Re s > 5/24 in the window):

    B_0 = H_0 + Z_loc + Z_far,   Z_far := (1/2 pi i) int_{Gamma_far ∪ V_low ∪ B_out ∪ B_back ∪ V_up} Psi dz,

split parameters: c = 1/16, Z_0 = 40 (heights |Im z| > 40 = far vertical), local region =
K(s) ⊂ D(z*, 2) (window) with dodge box [Re z_b - 1/4, 1/16] x [mu_b - 2, mu_b + 2],
r_0 = 1, hug length 2r = 1/4. CONVENTION (refines P2.6's one-line split; see FAILURES.md
F1): Z_loc = the compact cut-hug ONLY; the four connecting pieces are assigned to Z_far.
They are bounded on Omega^+ with bounded-height inputs only (E3), so [P2-FAR]'s burden is
unchanged: its sole unproved content remains the far vertical |Im z| > 40, where unverified
zeros' poles AND branch points live (D1.b) and where, for Re s <= 1/8, the contour formula
for Z_far is not even branch-well-defined (P2.8(b), the wall). On 0 < Re s <= 5/24, Z_far
is DEFINED BY SUBTRACTION Z_far := B_0 - H_0 - Z_loc (P2.7 step (3): B_0 continues to
Re s > 0 under the reductio; Z_loc is unconditional by (Z)); the two definitions agree on
Re s > 5/24 by the deformation identity + identity theorem. Nothing in Z_loc's expansion
depends on the reductio.

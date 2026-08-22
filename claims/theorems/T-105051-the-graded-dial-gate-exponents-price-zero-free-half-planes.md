# T-105051 — The graded dial: partial half-divisor field energy pays a zero-free half-plane

Claim ID: `T-105051`
Status: **PROVED CONDITIONAL QUANTITATIVE TRANSFER (forward + partial converse); GATE_theta OPEN for every theta < 2/3**
Created: 2026-08-22 (Lane A3)
Depends on: `L-100310`, `L-100311` (PR #685 `origin/research/gpt56-pro/100300-two-route-endgame` @ `4f69b7656f42dcb5ff250d13adc9f88e8d18f315` — DEPOSITED_UNREVIEWED, see `T-105050` §4.3); `L-102009`, `L-102010`, `T-102001` (PR #696 `origin/research/gpt56-sol/102000-parabolic-bessel-vaughan-correction` @ `f4016db548afceb31b150547cb6cd48b4cddb77d`); classical facts (EXTERNAL-CLASSICAL): zeta(1+it) != 0 (Hadamard–de la Vallée Poussin), zeta(sigma) < 0 on (1/2,1), and [converse only] "no zeros in Re s > sigma_0 implies M(x) << x^{sigma_0+eps}" (Littlewood's argument, Titchmarsh ch. 14).
Replay: `experiments/X-105051-dial/` (verify.py, results.json).
RH status: **not assumed; RH remains unproved**

## Objects (exactly those of PR #696)

U_X = floor(X^{1/3}); b_U(n) = mu(n) 1_{n>U}; eta multiplicative with
sum_k eta(p^k) z^k = (1-z)^{-1/2} (so eta*eta = 1, 0 <= eta <= 1); h_U = b_U * eta;
A_-(y) = 1 on (1,2), -sqrt2 on (2,4), 0 else;
H_{U,-}(Y) = sum_n h_U(n) n^{-1/2} A_-(Y/n)  (untruncated field), and the
TRUNCATED-field energy

    Ht_U(X) = int_U^{4X/U} | sum_{U<n<=X/U} h_U(n) n^{-1/2} A_-(Y/n) |^2 dY/Y,

versus the deposited untruncated H_U(X) = int_U^{4X/U} |H_{U,-}(Y)|^2 dY/Y
(L-102010.12). AUDIT FINDING (new): the literal T-102001.5 inequality
|B_U(X)| <= 3 H_U(X) with the UNTRUNCATED energy has an unjustified step — on the
annulus (X/U, 4X/U] the truncated field of the Hardy argument and the untruncated
field of L-102010.12 differ, with no pointwise domination. The rigorous chain is
|B_U(X)| <= 3 Ht_U(X) (proof in Step 0 below). Ht is therefore the corrected gate
object; every statement below uses it (and (II), (III) hold for both objects).
This makes the reviewers' recorded required fix ("Keep support truncation before
full-line Hardy", ARITH.VAUGHAN.HALF_DIVISOR row 43 @ 55fe0b6f; Reviewer B
VERDICT_DELTA line 24) precise; it is a STATEMENT-PRECISION REPAIR, not a
refutation of L-102010, whose Hardy relation is correct for the truncated field
— and not an observed failure: numerically |B| <= 3 min(H, Ht) at all samples.

For theta in (0,1) define the graded gate

    GATE_theta:  there are C, L_0 such that for all L >= L_0
                 int_{2^L}^{2^{L+1}} Ht_{U_X}(X) dX/X  <=  C 2^{theta L}.

GATE_{o(1)} (i.e. GATE_theta for every theta > 0) is the corrected reading of
HHFE102010.

## Statement

**(I) Forward dial.** For every theta in (0,1):

    GATE_theta  ==>  zeta(s) != 0  in  Re s > 1/2 + theta.

So f(theta) = theta: monotone, f(0+) = 0; as theta -> 0 this recovers
HHFE102010 => RH (T-102001.7) and strictly refines it at every positive level.
The conclusion is NEW mathematics (beyond zeta(s) != 0 on Re s >= 1) for every
theta < 1/2, since no zero-free half-plane Re s > sigma_0 with sigma_0 < 1 is known.

**(II) Trivial bound.** Unconditionally GATE holds at exponent 2/3 up to logs:
int_block H dX/X << 2^{(2/3)L} L^2. (So the dial's working range is theta in (0, 2/3).)

**(III) Converse dial (partial).** If zeta(s) != 0 in Re s > 1/2 + delta
(0 <= delta < 1/2), then GATE_theta holds for every theta > 1/3 + (2/3) delta.
So g(delta) = 1/3 + (2/3) delta; under RH the method yields exponent 1/3 + eps,
NOT o(1): the converse has a floor at 1/3 (see Scope/obstruction).

**(IV) Sandwich.** With Theta_gate = inf{theta : GATE_theta} and
Theta_zeta = sup Re(zeta zeros):

    Theta_zeta - 1/2  <=  Theta_gate  <=  min(2/3, 1/3 + (2/3)(Theta_zeta - 1/2)).

Dead band: proving Theta_gate < 1/3 is "harder than RH" for current technology
(RH itself is only known to force Theta_gate <= 1/3 via (III)); but ANY proved
gate exponent theta < 1/2 already pays an unproved zero-free half-plane.

## Proof of (I)

Step 0 (inherited exact identities, re-verified in lane A3 verify.py; Hardy step
repaired per the audit finding).
K_1 = A_- *_M A_+ with hat K_1(s) = (1-sqrt2 2^{-s})^2 (1-2^{-s})^2 (s+3/2)/(s^2(s-1/2)),
entire, supp K_1 in [1,16]; a_U*a_U*mu = h_U*h_U (L-102010.4);
B_U(X) := sum_n (a_U*a_U*mu)(n) n^{-1/2} K_1(X/n) = int_U^{X/U} H_{U,-}(Y) H_{U,+}(X/Y) dY/Y
(L-102010.7). Repaired Hardy reduction: truncate h_U at n <= X/U and write G_-, G_+
for the truncated fields; they agree with the untruncated fields on [U, X/U], so
B_U(X) = int_U^{X/U} G_-(Y) G_+(X/Y) dY/Y; G_- is supported in [U, 4X/U]; A_+ =
A_- - 2T A_- with (Tf)(u) = int_0^inf e^{-t/2} f(u+t) dt, and I - 2T (dilation-
invariant, Fourier multiplier (-3/2-i xi)/(1/2-i xi), sup-modulus 3) maps G_- to
G_+; Cauchy-Schwarz then Plancherel give
    |B_U(X)| <= ||G_-||_{L2([U,X/U],dY/Y)} ||G_+||_{L2(R+,dY/Y)}
             <= 3 ||G_-||^2_{L2([U,4X/U],dY/Y)} = 3 Ht_U(X).
W_1(X) = sum_n mu(n) n^{-1/2} K_1(X/n); Vaughan (L-100311): for U < X/16,
W_1 = T_U + B_U with |T_{U_X}(X)| <= (V_1/12) X^{-1/6}, so
C_T := int_2^inf |T_{U_X}| dX/X < infinity (L-100310.4, L-100311.6).

Step 1 (gate -> graded negative mass). All bounds pointwise in X at the frozen
value U = U_X (no Mellin transform of the moving-cut object is ever taken):
(W_1)_-(X) <= |T_{U_X}(X)| + 3 Ht_{U_X}(X) for X > 64. Summing GATE_theta over
blocks L_0 <= L <= log2 Y and absorbing finitely many small blocks:

    M_-(Y) := int_1^Y (W_1)_- dx/x  <=  C_2(theta) Y^theta,
    C_2(theta) = O(1) + 3C 2^theta/(2^theta - 1).

Step 2 (Lemma A: quantitative Mellin–Landau transfer — NEW, self-contained).
Let f: [1,inf) -> R be measurable with |f(x)| <= C_1 sqrt x, suppose
int_1^Y f_- dx/x <= C_2 Y^theta, and suppose F(s) = int_1^inf f x^{-s} dx/x
(Re s > 1/2) continues meromorphically to Re s > 0 and is analytic at every
real point of (0, inf). Then F is holomorphic on Re s > theta.
Proof: N(s) = Mellin of f_- is holomorphic on Re s > theta (partial integration
against M_- <= C_2 Y^theta). P(s) = Mellin of f_+ has finite abscissa
sigma_c <= 1/2 (explicit finite-abscissa step: f_+ <= C_1 sqrt x). On
Re s > max(sigma_c, theta) all integrals converge absolutely, F = P - N there,
and F is pole-free there by the identity theorem. If sigma_c > theta: F is
analytic at the real point sigma_c (hypothesis), N is analytic there, so
P = F + N extends analytically to a disc around sigma_c; the classical Landau
argument for nonnegative Mellin densities (Taylor at a = sigma_c + 1 with
(-1)^k P^{(k)}(a) >= 0, radius > 1 by the disc bump, Tonelli) forces convergence
of P strictly below sigma_c — contradiction. Hence sigma_c <= theta. QED.
(This subsumes the deposited specialized-Landau pattern L-99272; the
finite-abscissa and local-integrability requirements of its VERIFIED_WITH_FIXES
row are explicit here. Branch-safe: no fractional power of zeta appears —
the only analytic object is 1/zeta(s+1/2), the Mellin side of a genuine
Möbius sum; eta/zeta^{1/2} enters through arithmetic identities only.)

Step 3 (application and zero exclusion). f = W_1 qualifies:
F(s) = hat K_1(s)/zeta(s+1/2) for Re s > 1/2 (absolutely convergent unfolding),
meromorphic on C, and analytic at every real s > 0 because hat K_1 is entire and
zeta(sigma+1/2) != 0 for real sigma > 0 (zeta < 0 on (1/2,1) by the alternating
eta-series; pole at sigma = 1/2 makes 1/zeta analytic; zeta > 0 on (1, inf)).
Lemma A gives: hat K_1(s)/zeta(s+1/2) holomorphic on Re s > theta. A zero
rho = beta + i gamma with beta > 1/2 + theta would put a pole at s = rho - 1/2
unless hat K_1(rho - 1/2) = 0; the zeros of hat K_1 in Re s > 0 lie ONLY on
Re s = 1/2, i.e. beta = 1, excluded by zeta(1+it) != 0. QED (I).

## Proof of (II)

|h_U(n)| <= (1*eta)(n), sum_{n<=Y}(1*eta)(n) <= Y(1+log Y) (eta <= 1), so
|H_{U,-}(Y)| << sqrt Y log Y, H_U(X) << (X/U) log^2 X = X^{2/3} log^2 X. QED.

## Proof of (III)

Group h_U = b_U * eta by the eta-factor: H_{U,-}(Y) = sum_m eta(m) m^{-1/2}
beta_U(Y/m), beta_U(y) = sum_{d>U} mu(d) d^{-1/2} A_-(y/d) (zero for y <= U).
The classical input gives R(t) = M(t) - M(U) << t^{1/2+delta+eps} uniformly;
integrating by parts against t -> t^{-1/2}A_-(y/t) (total variation << y^{-1/2}
— three jumps plus smooth part) yields |beta_U(y)| << y^{delta+eps}. Then
|H_{U,-}(Y)| <= sum_{m<Y/U} eta(m) m^{-1/2}(Y/m)^{delta+eps}
<< Y^{delta+eps}(Y/U)^{1/2-delta-eps} = Y^{1/2+eps'} U^{delta-1/2},
H_U(X) << U^{2delta-1}(X/U) X^{eps} = X^{(1+2delta)/3+eps} at U = X^{1/3}. QED.

## Scope, honesty, obstruction

- Inherited links and their review state: L-102010/T-102001.5 is
  ARITH.VAUGHAN.HALF_DIVISOR = VERIFIED_WITH_FIXES (fix "keep support truncation
  before full-line Hardy" — incorporated verbatim in Step 0; Reviewer B cross-review
  AGREE, "Hardy norm 3 survive."); L-102009 VERIFIED; L-100310 rowed VERIFIED in
  `integration/implication-matrix/2026-08-20-node-aliases.tsv` (row IM-P07) @
  `origin/review/gpt56-pro/101100-conjunctive-bridges` — a research-integration
  artifact, NOT a review-wave ledger row (PR 685 has no row in the 2026-08-21
  arithmetic CLAIMS.tsv; see T-105050 §4.3); L-100311 is a PROVED EXACT
  deposit re-derived here; the specialized Landau pattern (L-99272,
  VERIFIED_WITH_FIXES) is replaced by the self-contained Lemma A. All identity-level
  inheritances re-verified by exact rational arithmetic and numerics (verify.py:
  eta*eta = 1 and a*a*mu = h*h = b*b*1 exactly to n = 400; Vaughan identity exact;
  W_1 = T_U + B_U to 3e-14 at X = 2000; field factorization of B_U to 2e-4;
  |B_U| <= 3H_U; Type-I scaled residual bounded by ~13.5 in magnitude
  (sign-oscillating below Y = 10^3, settling at 13.49 for Y >= 10^3);
  hat K_1 numeric Mellin matches the formula; hat K_1(1/2) = 0 to 5e-9).
- What is NEW: Lemma A; theorem (I) with f(theta) = theta; (II); (III) with
  g(delta) = 1/3 + 2delta/3; sandwich (IV); the dead-band/payoff analysis; the
  numerical exponent measurement of the gate energy (results.json).
- Obstruction (the converse floor): g(delta) does NOT tend to 0. Any converse proof
  that treats the eta-dilates of the Möbius A_--field by the triangle (or Minkowski)
  inequality floors at exponent 1/3, because ~X^{1/3} dilates each carry unit
  L^2(dY/Y) mass. Beating 1/3 under RH requires sign cancellation ACROSS dilates;
  in Plancherel form (L-103102.1) this is a fractional-mollifier mean value whose
  leading term contains a NEGATIVE moment of zeta on the critical line — not known
  to follow from RH alone (Gonek-type hypotheses needed). So "RH => HHFE102010" is
  NOT proved here and may be beyond current technology; the dial is honestly
  asymmetric: f(theta) = theta down, g(delta) = 1/3 + 2delta/3 up.
- Numerics on the true size of the gate (moderate X; results.json): dyadic block
  integrals measured for BOTH energies over L = 8..26 (X up to ~1.3e8, 8 log-uniform
  samples per block, exact step-field sweep): untruncated 0.38 -> 0.50, truncated
  0.36 -> 0.61 — essentially FLAT; least-squares exponents 0.021 (untruncated) and
  0.042 (truncated), versus the converse-proof floor 0.333 and trivial 0.667. Strong
  (non-certifying) evidence that HHFE102010 is TRUE and the 1/3 floor is a proof-
  method limit (the eta-dilate sign cancellation is empirically fully present).
- GATE_theta is OPEN for every theta < 2/3. Nothing here proves RH, and no
  unconditional zero-free improvement is claimed. The payoff table is:
  theta >= 1/2: conclusion classical-vacuous; theta in (1/3, 1/2): new zero-free
  half-plane, converse-consistent target; theta <= 1/3: harder than RH by (III)+(IV).

# T-105070 — The W-pinch closure: GATE_{o(1)} is false modulo two named interfaces; Theta_gate >= 1/3; Theta_gate = 1/3 under RH

Claim ID: `T-105070`
Status: **ASSEMBLY THEOREM. Tier A (chain outside the W-pinch lemma): PROVED, exact,
unconditional. Tier B (the W-pinch lemma itself): PROVED modulo two named interface
slots [P1-LOC-WELD] and [P2-FAR] — [P1-LOC-WELD] has its model theorem proved (lane P1)
and its coefficient computed and nonvanishing (lane P3, w4); [P2-FAR] is OPEN (the
honest wall). RH never assumed, never claimed; NO step of Tier A or Tier B uses RH or
any zero-free half-plane.**
STATUS UPDATE 2026-08-23 (same day, interface-assault wave): **[P1-LOC-WELD] is
DISCHARGED** by `L-105072` — with a FINDING: the literal derivative clause of §2's
statement is FALSE for the genuine Z_loc (half-power `kappa (s-s_0)^{1/2}`,
`|kappa| = 0.0140799 != 0`); the weld closes unconditionally under the amended bound
`|R_loc'| <= M_loc(1 + |s-s_0|^{-1/2})` (r_0 = 1/2, M_loc = 640), and the P2.7(6)
consumption survives at cost `log(1/h) -> log^2(1/h)`, still `o(1/h)`, with c_0' and
all downstream constants unchanged. **[P2-FAR] is REDUCED** by `L-105071` to the
single fixed-frequency amplitude inequality (FAR-WIN). NET STANDING: the theorem's
conclusion (i)-(iii) now rests on exactly ONE open statement — (FAR-WIN) — plus the
amended-interface reading of §2 recorded here. RH status unchanged: unproved, not
addressed.
Created: 2026-08-23. Agent: claude, lane P3.
Depends on: `T-105059` (.5 exact tent reduction, .6 program, .7 bootstrap audit),
`L-105058` (.1, .5), `T-105051` (I, III, Step 0), `L-105052`, `O-105054` @
`claude/riemann-proof-review-8nz34i`.
Inline components (this terminal assault): lane P1 (model pinch/transfer theorems
A, B, C1-C3 + numerics), lane P2 (THEOREM.md: P2.1-P2.8 — representation, D_half
operator identity, hypothesis-side transfer P2.7), lane P3 (CPINCH.md = w4 coefficient
theorem; BOOKKEEPING.md = measure lemma), lane P4 (falsification: VERDICT.json
"RESTORED" — the sqrt(log N) weight restores the full pole; blind constant
0.2489±0.0033 vs predicted 0.247167; c_0' candidate 0.000971).

## 0. Pinned statement of the W-pinch lemma (continuous-u, Definition of record)

For real `u >= 4`, `X := u^3`, `U := floor(u)`, `N := floor(X/U)`,
`Lambda(X) := sum_{N/2 < n <= N} h_U(n) n^{-1/2} ln(2n/N)/ln2` (T-105059.5),
`W_u := Lambda(u^3) sqrt(log N)/u` (W := 0 for u < 4); equivalently
`V(X) := Lambda(X) sqrt(log N_X) X^{-1/6}`.

    W-PINCH LEMMA:  limsup_T (1/log T) int_1^T u W_u^2 du/u >= c_0' > 0.

By lane P3 BOOKKEEPING Lemma 1 this is IDENTICAL to
`TARGET(V): limsup_Y (1/log Y) int_1^Y V^2 dX/X >= c_0'` (exact change of variables,
zero constants lost; cube corners and floors audited, numerically verified).

## 1. Main theorem (tiered)

**Theorem.** Assume the two interface statements of Section 2 ([P1-LOC-WELD] and
[P2-FAR]). Then, WITH NO OTHER HYPOTHESIS (in particular no RH anywhere):

(i) The W-pinch lemma holds with the explicit constant

    c_0' = (4/(3 pi)) |c_B|^2 = 0.000970890581...,
    |c_B| = (3/2) k(1/2) / (sqrt3 |z*| |zeta'(rho_1)|) = 0.0478289351609...,
    k(1/2) = 2 - 4(1 - 1/sqrt2)/ln2,  z* = 1/4 - i gamma_1/2

    [lane P2 Theorem P2.7 for the architecture; lane P3 CPINCH.md for the coefficient,
    computed to 20 digits, nonvanishing with rigorous rational enclosures].

(ii) `E(L) >= 3 ln2 (c_0' - eps) 2^{L/3}/(L+2)` for infinitely many L, for every
    eps > 0 [lane P3 BOOKKEEPING Lemma 2 + T-105059.5, the latter exact and
    unconditional; the denominator is (L+2), not (L+1) — the concrete (L+1)
    bound fails near octave tops (hostile-review finding F2, correction recorded
    in BOOKKEEPING.md); for large L the forms differ by 1 + O(1/L), absorbed
    into eps, so (iii) is unaffected].

(iii) `Theta_gate >= 1/3`: GATE_theta is FALSE for every theta < 1/3, and in particular
    **GATE_{o(1)} — HHFE102010 in the corrected Ht reading (T-105051 Step 0) — is
    FALSE unconditionally (given the Section 2 interfaces)** [quantifier check in
    Section 3].

(iv) With T-105051(III) (zeta nonzero on `Re > 1/2 + delta` => GATE_theta for
    theta > 1/3 + (2/3)delta; at delta = 0 this is RH => Theta_gate <= 1/3):
    **under RH, Theta_gate = 1/3 exactly.** RH is used HERE ONLY, for the upper
    half of the sandwich — the refutation (iii) never touches it.

**Tier A (proved now, unconditional, independent of the interfaces):** statements
0 (equivalence), (ii)-as-implication (bookkeeping), T-105059.5 (tent reduction,
exact), L-105058.1 (exact Plancherel), P2.1-P2.5 (formulation equivalence; smoothing
bridge with L2-summable floor corrections; exact double-Dirichlet representation;
the D_half half-derivative operator identity — T-105059.6's "designed escape" is now
an exact operator statement, P2.4(b): D_half turns `(s-a)^{-1/2}` into
`(1/sqrt pi)(s-a)^{-1}`; pinch geometry with `z_p - z_b = 3(s - s_0)` exact and all
other singularities O(1)-separated), P2.7's proof skeleton (the L-105058.5
architecture transferred verbatim: negation => J(h) bound => Cauchy-Schwarz
absolute-convergence licence => L1∩L2 Fourier-Plancherel => two-window Schwarz =>
contradiction), and the w4 coefficient theorem (CPINCH.md).

**Tier B (the two slots):** Section 2. If both land, the whole of (i)-(iii) is
UNCONDITIONAL and the W-pinch lemma is proved inline. If [P2-FAR] lands only in its
L2-window form with loss eps_1 < 1, everything survives with
`c_0' -> (1 - eps_1)^2 c_0'` (P2.7 Remark (iii)). Until then, the theorem is
CONDITIONAL on exactly the named residue(s) below — nothing else.

## 2. The interface slots (precisely delimited)

**[P1-LOC-WELD]** — status: MODEL PROVED + COEFFICIENT PROVED; weld residue small and
bounded-height-classical.
UPDATE 2026-08-23 (`L-105072`): **DISCHARGED, with the statement below AMENDED.** The
literal conjunction `|R_loc| + |R_loc'| <= M_loc` is DISPROVED for the genuine Z_loc
(R_loc carries the half-power `kappa (s-s_0)^{1/2}`, `|kappa| = 0.0140799`, so R_loc'
blows up like `|s-s_0|^{-1/2}` at the pinch corner — no r_0, M_loc evade it). What IS
proved, unconditionally from bounded-height inputs (max zero-height consumed 17.33):
the expansion with `omega = +1` pinned and c_B confirmed in modulus AND phase (1.03e-6,
genuine deformed-contour numerics); `|R_loc| <= 5.71`;
`|R_loc'| <= 640 (1 + |s-s_0|^{-1/2})` on Omega^+(r_0 = 1/2); and the consumption
repair: P2.4(c)/P2.7(6) accept the amended bound at cost `log^2(1/h)` in the error,
still `o(1/h)` — main term and c_0' unchanged. Read this slot's statement with the
amended derivative bound; so read, it is CLOSED.
Statement to weld (ORIGINAL WORDING, kept for the record — the derivative clause is
the amended one per the UPDATE above): there exist `r_0 in (0,1]`, `M_loc` with

    Z_loc(s) = c_B (s - s_0)^{-1/2} + R_loc(s),  |R_loc| + |R_loc'| <= M_loc on Omega^+,

`Z_loc` = the cut-hugging local piece of P2.6's contour split, `c_B` as in Section 1.
What exists: lane P1's Theorem A proves exactly this expansion (kappa = 1/2, explicit
C_A, numerically verified along 4 rays to 1.6e-4 at |eps| = 1e-8) for the model Hankel
integral with analytic amplitude; lane P2.5 supplies the genuine kernel `k(beta)/z`,
the exact pinch geometry, and the separation bookkeeping; lane P3's CPINCH.md derives
and evaluates `c_B` on the genuine data. The RESIDUE: writing the deformation that
produces `Z_loc` from P2.5's vertical contour and checking P1's amplitude-regularity
hypotheses on it (analyticity and derivative bounds for `k(beta_z)/z`, `b(a+z)`, and
the zero-factor on the cut neighborhood — all follow from bounded-height classical
inputs: verified zeros to height 60 on the line and simple, `zeta^{1/2}` bounded on
compact cut regions; NO zero-free half-plane, no density estimates). This is a
finite, compact-region verification.

**[P2-FAR]** — status: OPEN; THE wall. Statement: `|Z_far| + |Z_far'| <= M_far` on
`Omega^+` (or the weaker L2-window form, P2.7 Rem (iii)). Obstruction, honestly
(P2.8(b)): the far field evaluates `1/zeta` at unbounded heights inside the strip
with no unconditional pointwise/L1/L2 line bound; the half-divisor structure blocks
the classical zero-free-region detour. This is T-105059.6's half-singularity /
negative-moment wall relocated to the far field — the pinch itself is NOT obstructed.
Routes on record: (R1) arithmetic corner/smooth kernel split + Hooley–Tenenbaum
Delta-second-moments (numerics: the corner field carries 77% of raw mean square but
only 3.5% of window mass — spectrally flat at the pinch frequency, as [P2-FAR]
asserts); (R2) reductio-side L2-log inheritance through D_half (one log short by
pointwise routes; L2-based refinement open).
UPDATE 2026-08-23 (`L-105071`): the interface is REDUCED — (FAR-WIN), a single
fixed-frequency scale-averaged amplitude inequality for the pinch-subtracted
Abel-damped field, implies [P2-FAR] in form (b) with `eps_1' = eps_1/sqrt(2)`
(reduction theorem PROVED from four operator lemmas F1–F4,
unconditional-under-reductio; the packet's hostile review found and repaired three
invalid steps in the first proof — G1/G2/G5, see its FAILURES ledger — and confirmed
the repaired chain); `1/zeta` at unbounded heights is ELIMINATED from the interface. Both R1 and R2 terminate at (FAR-WIN); the
reductio's own budget caps the residual gap at a constant factor 27.5 (F5), and
independent numerics measure the ratio an order of magnitude inside the requirement
(implied eps_1 = 0.25–0.35). (FAR-WIN) itself remains OPEN — the wall is now one
scalar inequality about one frequency.

## 3. Bootstrap and quantifier audit (T-105059.7 RECHECKED)

Rechecked against the deposited texts this session:
(i) GATE => RH direction: T-105051(I) is stated for the corrected object Ht
(`|B_U| <= 3 Ht`, Step 0 verified present in T-105051), and gives
`GATE_theta => zeta != 0 in Re s > 1/2 + theta`; GATE_{o(1)} = all theta > 0 forces
RH. CONFIRMED as cited.
(ii) No circularity: the route here needs no reductio-through-RH at all — Tier A and
both interfaces are RH-free, so (iii) is a DIRECT refutation, strictly stronger than
T-105059.7's already-valid reductio form. CONFIRMED.
(iii) Quantifiers: GATE_theta is an ALL-large-L statement (`for all L >= L_0`,
T-105051); statement (ii) produces io L with `E(L) >= c 2^{L/3}/(L+2)`, and for any
theta < 1/3, C: `c 2^{L/3}/(L+2) > C 2^{theta L}` for all large L — so io violation
negates GATE_theta. CONFIRMED. (iv) The E_N-phase-conspiracy failure mode flagged by
lane P is moot in this route: the tent reduction T-105059.5 is exact, no remainder
extraction occurs. CONFIRMED.
(v) Lane P4 (falsification lane) verdict read mid-assembly: **RESTORED** — the
weighted field's window exponent beta_W = 0.008 ± 0.028 (full pole; unweighted
control 0.519 ± 0.027 = half pole), pinch constant blind-measured at 1.007 ± 0.013
of the predicted chain, two-zero test passes at both gamma_1 and gamma_2. The pinned
formulation stands; NO corrected-weight adaptation was needed.

## 4. Falsifiers

1. `c_B = 0`: excluded by CPINCH.md's rational enclosure (`k(1/2) in
   (0.3097773, 0.3097779)`, |c_B| >= 0.047828); a proof to the contrary breaks w4.
2. Any X with `Ht_U(X) < 2 ln2 Lambda(X)^2`: violates the EXACT T-105059.5 — a bug,
   not an interpretation.
3. Pole-restoration failure: window exponent of the weighted field drifting from 0
   (P4 measured 0.008 ± 0.028; a future scan finding beta_W >= 0.25 at larger T
   kills Tier B's mechanism).
4. `Z_far` window mass `>> 1/h` at the pinch frequency (would falsify [P2-FAR];
   current numerics show the far/corner field flat, 3.5% of window mass).
5. Measured window mass drifting from `pi |c_P|^2 / h_eff` (currently 0.0146
   measured vs 0.0153 predicted at h = 0.01, truncation-limited).
6. An error in the bookkeeping identity: any grid where the u-side and X-side/3
   integrals differ beyond quadrature error (currently 0.15% on independent grids).

## 5. Honest scope — what is and is not claimed

CLAIMED (conditional on Section 2's two slots, and on nothing else): GATE_{o(1)}
false; Theta_gate >= 1/3; under RH Theta_gate = 1/3. NOT CLAIMED: RH (in any
direction — the refutation of GATE_{o(1)} refutes a specific gate criterion, not
RH; the bootstrap direction GATE => RH makes the gate's falsity CONSISTENT with
either truth value of RH); GATE_theta for theta in [1/3, 1/2) — untouched, still
paying an unproved zero-free half-plane per level (T-105051 I, IV); any
unconditional bound on M(x) or m(u) beyond L-105058.5. CURRENT STANDING: because
[P2-FAR] is open, T-105070 is today a CONDITIONAL theorem with one open analytic
interface (plus one compact-region weld); the moment both are deposited, flip
Status to PROVED and the words "modulo two named interfaces" disappear.

## 6. Citation chain (complete)

T-105051 (I, II, III, IV, Step 0) — the dial, the corrected gate object Ht, the
converse; L-105058.1 (exact Plancherel), L-105058.5 (the H2/Paley–Wiener mass lemma:
the architecture P2.7 transfers verbatim; simplicity input and fallback constant),
L-105058.3/.4 (branch structure; Selberg–Delange EXTERNAL-CLASSICAL); O-105054.3
(kernel zero `hatA_-(1/2) = 0`); T-105059.2 (edge mechanism, `I_w = 2 pi(3 ln2 - 2)`),
T-105059.5 (Cauchy–Schwarz tent reduction, exact, unconditional), T-105059.6 (program
+ pinned lemma), T-105059.7 (bootstrap audit, rechecked here); lane P1 NOTES.md
(Theorems A, B1, B2, B, C1, C2, C3 + N1/N2 numerics); lane P2 THEOREM.md (P2.1-P2.8 +
num1-num5); lane P3 CPINCH.md (w4), BOOKKEEPING.md (measure lemma), cpinch.py,
bookkeep.py, bookkeep2.py; lane P4 VERDICT.json + stage1-5 (falsification pass,
RESTORED). Classical inputs beyond L-105058.5's class: NONE.

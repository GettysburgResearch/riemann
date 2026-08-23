# L-105071 — The far-field interface [P2-FAR] reduces to ONE fixed-frequency amplitude inequality (FAR-WIN): 1/zeta at unbounded heights is ELIMINATED from the interface

Claim ID: `L-105071`
Status: **REDUCTION PROVED (Theorem: (FAR-WIN) ⟹ [P2-FAR] form (b), via four proved
operator lemmas F1–F4, all unconditional-under-reductio, no zeta data off bounded
height) — (FAR-WIN) itself remains OPEN — RH NOT ADDRESSED**
Created: 2026-08-23
Agent: claude (external reviewer lane; far-field assault lane on T-105070's [P2-FAR];
routes R1 and R2 both executed, both terminating at the same single residual)
Depends on: `T-105070` (P2.7 Remark (iii) consumes the conclusion), `L-105072` (the
AMENDED [P1-LOC] interface — the literal form this lemma first cited for R_loc
bookkeeping was disproved by L-105072(d); the two uses are repaired in FAR.md §0/§3
via L-105072(e), with no quantitative change — cross-claim repair H2),
`L-105058` §5 (H²/Paley–Wiener architecture).
Replay: `experiments/X-105071-far-reduction/` (FAR.md = full write-up; R2_VERDICT.md;
FAILURES.md = 7 recorded dead ends; far_num1–3.py + JSON outputs, all re-run clean
from this directory).
RH status: **unproved, not addressed**

## 1. Statement

Setting of T-105070/P2.7 (unweighted x-side field `psi_0(x) = V_0*(e^x) 1_{x>=ln 64}`;
pinch `s_0 = i gamma_1/3`; `c_P = sqrt(2/(3pi)) c_B`; "under R" = under P2.7's reductio).
Define the pinch-subtracted field

    psitil(x) := psi_0(x) - h_0(x) - 2 Re[ c_B pi^{-1/2} x^{-1/2} e^{i gamma_1 x/3} ].

**(FAR-WIN)** (the residual inequality, OPEN; stated UNDER the reductio R — there the
convolution converges absolutely via the loglog Q-budget): for a fixed smooth window `w`
with `hat-w` REAL, `0 <= hat-w <= 1`, `hat-w = 1` on `|t - gamma_1/3| <= r_0`, support in
the doubled window (the reduction proof uses this `w` as its projector, so these
conditions are part of the hypothesis), some `eps_1 < 1`, and the Abel damping INSIDE
the convolution (`x_+ := max(x,1)`):

    limsup_{h->0+} 2 pi h int_R x_+ |(w * (psitil e^{-h.}))(x)|^2 dx
        <= (eps_1^2/2)(2/(3pi)) |c_B|^2 .

**Reduction Theorem (PROVED).** (FAR-WIN) with constant `eps_1 < 1` implies, under R,
[P2-FAR] in its L2-window form (b) with `eps_1' = eps_1/sqrt(2) <= 0.708 < 1` EXACTLY
(no `o_{r_0}` loss; the display's 1/2 is a genuine safety margin) — i.e. P2.7 Remark
(iii)'s hypothesis holds and T-105070's conclusion follows with
`c_0' -> (1 - eps_1/sqrt(2))^2 c_0'`.

Proved ingredients (FAR.md §§1–3):

- **F1** (log budget, under R; x-side form — the full-line integral of `Ztil_far`
  itself diverges, since the subtracted untruncated half-pole has line density
  `~ |c_B|^2/|tau|`; hostile-review finding G2):
  `int_R |FT[psitil e^{-hx}](t)|^2 dt = 2 pi ||psitil_h||^2 <= C_F1 (A' + |c_B|^2) log(1/h)`,
  and on any bounded window the two objects agree up to O(1).
- **F2** (Minkowski lift): pointwise routes give
  `||D_half[Ztil_far]||^2_{L2(WIN)} <= C_F2 log(1/h)/h` — R2's "one log short",
  exactly quantified.
- **F3** (multiplier identity, unconditional, exact): on the Laplace class of
  P2.4(a), `D_half = FT ∘ (mult by sqrt(x)) ∘ FT^{-1}` — the half-derivative IS
  the sqrt(x)-multiplier on the x-side.
- **F4** (commutator lemma): `||[P_w, sqrt(x)]||_{L2->L2} <= (1/2) int |v w(v)| dv`,
  uniformly in h.
- **F5** (self-consistency, vacuous for closure, scale-pinning): the reductio's own
  J-budget caps the far window mass at `5.83 |c_B|^2` — a factor 27.5 above the
  target: after the F3 repair the residual gap in [P2-FAR] is a CONSTANT factor,
  not a power or log of h.

The interface gain: the reduction consumes only F1 + F3 + F4 + (FAR-WIN). The far
z-contour and `1/zeta(a-z)` at unbounded heights no longer appear — [P2-FAR]'s wall
is now a fixed-frequency, scale-averaged amplitude statement about the arithmetic
field at the SINGLE frequency `gamma_1/3`, finitely checkable at any truncation.

## 2. Proof

Full proofs in `experiments/X-105071-far-reduction/FAR.md` §§2–3 (F1–F4 and the
reduction theorem). The packet's own hostile review found three invalid steps in the
first deposited proof — a false compact-support premise in the damping-migration step
(G1), the divergent full-line F1 display (G2), and the sqrt(x)-multiplier applied
outside its domain (G5) — all repaired in place (FAR.md §§1–3; the repairs use only
budgets already in the packet, and the reviewer's own reconstruction confirmed the
theorem's statement), together with a misdiagnosed entry in the failure ledger (G3:
the "pi/h re-import" was a phantom — the half-order pole's window mass is a benign
log). FAILURES.md F-6/F-8 record all of this. R2_VERDICT.md proves R2 is structurally
blocked as an independent closer: the negation hypothesis is frequency-blind; the
multiplier repair (F3/F4) is the correct FORM of the missing step, and its closing
content is exactly (FAR-WIN).

## 3. Verification (independent code, Xc = 2e5 = 10x lane P2's grid)

- Corner split reproduced: corner field carries 71–77% of RAW mean square but only
  7.6–10% of window mass (3 widths, 3 h) — spectrally displaced, not small. A
  corner-definition discrepancy between lane P2's doc and its code (upper cut at
  r = 2 present in doc, absent in code) is recorded; affects no proof.
- (FAR-WIN) measured directly: residual/pinch weighted-mass ratio 0.0065–0.0133
  across r_0 = 0.15/0.30/0.50, stable in h; requirement for `eps_1 < 1` is < 0.1061.
  Implied `eps_1 = 0.25–0.35` — an order of magnitude inside, ~700x below the F5
  self-consistency ceiling. (Caveats, G9: the numeric bump window is a proxy — not
  identically 1 on the window — and its denominator uses the clipped fitted pinch,
  both conservative; the weight sits outside the convolution, related to the official
  damped-inside placement by the o(1) equivalence of FAR.md §3's Remark.)
- Delta^2 budget: `sum Delta(n)^2/x = 9.67` (x = 3e5, local exponent 0.90);
  corner coefficients obey `|c_n| <= 2 Delta(n)` (0 violations), corner
  `sum c_n^2/x` LINEAR in the corner width delta and ~1000x below the Delta^2
  budget: coefficient SIZE is nowhere the obstruction — only cancellation.

## 4. Honest residual (why (FAR-WIN) is genuinely open)

- **R1's stop** (FAILURES F-2/F-3): the window amplitude is a fixed-height
  (`gamma_1/2`) Mobius cancellation statement — Selberg–Delange/Hankel type, the
  same (P-ii)-class error as L-105058.4, there proved only modulo a zero-free
  half-plane. Montgomery–Vaughan mean values do NOT apply: the window has fixed
  length `2 r_0` while the coefficient log-span is unbounded; the only available
  average (over scale x) IS the target quantity. PNT-strength cancellation leaves
  the corner amplitude one full power-scale above the pinch scale.
- **R2's stop** (R2_VERDICT.md): the reductio cannot say where the far field's
  `log(1/h)` line mass lives in frequency; F5's 27.5x self-referential ceiling is
  the best it gives.
- **Proposition G** (conditional, labeled, NOT counted): a Gevrey-2 mollifier +
  threaded contour closes the SMOOTH far field under a two-zero anti-conspiracy
  hypothesis (no pair of zeros with `gamma' - gamma ≈ gamma_1` and
  `beta + beta' > 3/2`, plus a weak `|zeta'(rho)|` floor) — far weaker than RH,
  still unproved (FAILURES F-4).

## 5. Falsifiers

A truncation at which the measured (FAR-WIN) ratio exceeds 0.1061 and grows (would
kill the interface empirically); an error in F3's operator identity (exact — one
Fubini licence, checkable); a frequency-localized configuration violating F4's
Schur bound; a proof that (FAR-WIN) implies a zero-free half-plane (would show the
reduction merely relocated the wall — the numerics say otherwise, but only a proof
settles it).

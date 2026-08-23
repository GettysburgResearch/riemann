# L-105072 — The local weld is PROVED: Z_loc's half-pole expansion with explicit constants, unconditional on bounded-height inputs — and T-105070's literal [P1-LOC-WELD] clause is FALSE, closed instead in amended form

Claim ID: `L-105072`
Status: **PROVED (deformation with zero crossed residues; all amplitude hypotheses;
|c_B| in modulus AND phase; |R_loc| <= 5.71; amended derivative bound with M_loc = 640;
downstream consumption repair) — the LITERAL T-105070 §2 clause `|R_loc| + |R_loc'|
<= M_loc on Omega^+` is DISPROVED (recorded finding against T-105070's interface
statement) — RH NOT ADDRESSED**
Created: 2026-08-23
Agent: claude (external reviewer lane; 4-stage weld pipeline deform → hypotheses →
adversarial audit → assembly, after a first single-lane attempt died on the output cap;
the pipeline's own audit stage returned PASS with 5 minor fixes, all applied)
Depends on: `T-105070` (P2.5/P2.6 contour objects; P2.4(c)/P2.7(5)-(6) consumption),
`L-105058` §5 architecture. Inputs: (A1) zeros verified on the line and simple to
height 60 (max height actually consumed: 17.33), (A2) compact-region zeta evaluations.
NO zero-free half-plane, no density estimates, no RH.
Replay: `experiments/X-105072-weld/` (WELD.md = assembly W0–W5 + verdict; DEFORM.md;
HYPOTH.md; AUDIT.md with APPLIED block; FAILURES.md F1–F5; weld_num.py + out — genuine
deformed-contour numerics, 109 s; audit_num.py, audit_kappa.py, hyp_num.py).
RH status: **unproved, not addressed**

## 1. Statement

Setting of T-105070 §2 ([P1-LOC-WELD]) and P2.5/P2.6: `s_0 = i gamma_1/3`,
`Omega^+` = the window `|Im s - gamma_1/3| <= r_0`, `Re s in (0, h_0]`;
`z_b(s) = 1/4 - (3/2)s`; `eps = 3(s - s_0)`.

**(a) The weld formula (PROVED).** With `b(v) = ((v-1)zeta(v))^{1/2}` (principal
branch, `b(1) = 1`), `Z_1(w) = zeta(rho_1 + w)/w` (`Z_1(0) = zeta'(rho_1)`):

    Z_loc(s) = (3/(2pi)) int_0^{1/4} A(x,s) x^{-1/2} (x + 3(s - s_0))^{-1} dx,
    A(x,s) = k(1/2 - x) b(1 - x) / ((z_b(s) - x) Z_1(3(s - s_0) + x)),

obtained from P2.5's vertical contour (anchor line Re z = 1/16, anchor band
`5/24 < Re s <= 1/4`) by an explicit homotopy crossing NO singularities (every
residue contribution is zero; connecting arcs -> 0 at rate 1/T; deformation identity
machine-arbitered to 4.3e-28, hug-vs-collapsed formula to 1.9e-21). Singularity
inventory on the swept strip `|Im z| <= 40` is complete (audit A1, independently
recomputed): the kernel k is ENTIRE (beta-denominator zeros removable), one z = 0
pole, 14 verified-zero poles (all heights <= 48.6 <= 60), partner branch points on
leftward cuts, trivial-zero poles inert at Re >= 2.75; every unverified-zero
singularity has |Im z| >= 51.4 vs local-region extent 8.69 — gap 42.7.

**(b) The expansion (PROVED), with branch phase pinned.**

    Z_loc(s) = c_B (s - s_0)^{-1/2} + R_loc(s)   on Omega^+ (r_0 = 1/2),
    c_B = (sqrt3/2) k(1/2) / (z* zeta'(rho_1)),  omega = +1 (principal branch),
    |c_B| = 0.04782893516094  — CPINCH's value, now confirmed in PHASE as well:
    genuine deformed-contour numerics fit c_hat = 0.00918468 + 0.04693874 i,
    complex agreement with c_B to 1.03e-6 (three rays, |s - s_0| down to 1e-6).

**(c) The bounds (PROVED):** `|R_loc| <= 5.71` on all of Omega^+ (grid maximum
observed 0.0883; ray limit 0.0968 = audit's independent 0.0967), and

    |R_loc'(s)| <= M_loc (1 + |s - s_0|^{-1/2}),   M_loc = 640,
    |R_loc| + |R_loc'| <= 637.5   on Omega^+ ∩ {|s - s_0| >= 1/24}.

**(d) The FINDING (DISPROVED clause).** T-105070 §2's literal
`|R_loc| + |R_loc'| <= M_loc on Omega^+` is FALSE for the genuine Z_loc, for EVERY
`r_0` and `M_loc`: R_loc contains the half-power `kappa (s - s_0)^{1/2}(1 + O(|s-s_0|))`,

    kappa = (sqrt3/2) A(0,s_0) [ 3k'(1/2)/k(1/2) + (3/2)gamma_E - (3/2)/z* ]
          = 0.0118261 + 0.0076410 i,   |kappa| = 0.0140799 != 0

(the zeta''(rho_1) contributions cancel exactly; closed form vs direct mpmath
differentiation: 3.9e-16), so `R_loc'` blows up like `|s - s_0|^{-1/2}` at the pinch
corner, a limit point of Omega^+.

**(e) The consumption repair (PROVED; FAILURES F5, audit-checked).** P2.4(c)'s proof
consumes only increments; under (c), along the D_half ray `|s + u - s_0| >= max(u, h)`,
and splitting the del-integral at `del = h` (the max(u,h) floor and the split are
LOAD-BEARING — the naive increment bound alone diverges):
`|D_half[R_loc](h+it)| <= C M_loc (1 + log(1/h))`. P2.7(6)'s error becomes
`O(M_loc |c_B| log^2(1/h))` — still `o(1/h)`; the main term `(2/(3pi))|c_B|^2/h`,
the limit `c_0'`, and every downstream constant are UNCHANGED.

**Consequence for T-105070:** the [P1-LOC-WELD] slot is DISCHARGED — its statement
must be read with the amended derivative bound (c), under which (a)-(e) close it
unconditionally from bounded-height inputs. T-105070's conditionality reduces to the
single remaining interface (FAR-WIN) (`L-105071`).

## 2. Proof

`experiments/X-105072-weld/`: DEFORM.md (contour, homotopy, inventory, arcs);
HYPOTH.md (all 12 Theorem-A hypothesis rows: 11 PASS, row 11 = the literal derivative
clause FAIL -> (d); M_loc assembly `max{0.554, 5.701, 9.264, 2.212, 631.8} -> 640`);
FAILURES.md F5 ((d)+(e) in full); AUDIT.md (adversarial stage: PASS, 5 minor fixes
applied — includes independent inventory recomputation, edge-geometry check at window
corners, and the F5 repair's del-split verification); WELD.md (assembly + verdict).

## 3. Verification

`weld_num.py` (mpmath dps 30): Z_loc evaluated VIA the deformed contour (finite-eta
Hankel hug, eta = 1e-12, quad maxdeg-invariance 1e-22) — NOT the collapsed formula;
coefficient fit on three rays: worst relative error 9.7e-7 vs |c_B| (target 1e-2);
24/24 grid points pass both M_loc = 640 and the sharper 5.71. `audit_kappa.py`:
closed-form kappa vs direct differentiation 3.9e-16 (re-run from this directory).
`audit_num.py`: deformation identity 4.3e-28; omega = +1 confirmed numerically.

## 4. Honest residual

- The weld itself has NONE on the stated region: (a)-(c) are unconditional.
- The FINDING (d) means T-105070 §2's interface as originally worded was
  unsatisfiable; the theorem survives because the consumption point tolerates (c)
  via (e) — this repair is part of the claim and was audit-checked, but it modifies
  a Tier-A error term (log -> log^2), so the deposit-level hostile review should
  re-derive it independently.
- Z_far's definition for `0 < Re s <= 5/24` remains by-subtraction under the
  reductio (DEFORM F3) — inherited from [P2-FAR]/(FAR-WIN), not new debt; the
  connecting pieces assigned to Z_far are bounded on the anchor band but their
  ray bounds for `Re s > 1/4` are shapes, not theorems (DEFORM F2) — irrelevant to
  Omega^+ consumption.

## 5. Falsifiers

A crossed singularity missed by both the enumeration and the 4.3e-28 arbiter
identity (would break (a)); a sign/branch error flipping omega (would contradict
the 1.03e-6 complex-phase agreement); an error in the kappa closed form (falsified
by any disagreement with direct differentiation); failure of the del = h split in
(e) (would reinstate a log(1/h) divergence — checkable against P2.4(c)'s proof line
by line).

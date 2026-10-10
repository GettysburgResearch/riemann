# L-105063 — The dipole count cap is PROVED on the separated/subcritical regimes: A′ = 6 on C-0∪C-1∪C-2, and 2k on the depth-k shallow ladder

Claim ID: `L-105063`
Status: **PROVED (Theorems C-0, C-1, C-2, C-3; C-2 new) ON THE STATED REGIMES — the all-gaps cap remains OPEN on two precisely-described residual regimes (§4) — RH NOT ADDRESSED**
Created: 2026-08-23
Agent: claude (external reviewer lane; count-cap pipeline CAP-A/CAP-B/CAP-C; the pipeline's assembly lane audited both case lemmas and refused an unusable sub-claim (LEMMA_B B-I(iii) — correct as stated but vacuous for the purpose, per the subsequent dedicated review); the dedicated three-lemma hostile review returned FIX_FIRST → all findings applied in the hardening commit, verdict thereafter DEPOSIT_SAFE)
Depends on: `L-105061` ([I-PF] + [THRESHOLD], proved), `L-105062` §1 (Hadamard product).
Replay: `experiments/X-105063-count-cap/` (FINAL_LEMMA.md = full proof; LEMMA_A.md, LEMMA_B.md = the two case lemmas; capA_/capB_/capC_ scripts + scans; 487 in-regime adversarial configs + 600 residual-regime scans, 0 violations).
RH status: **unproved, not addressed**

## 1. Statement

Setting of `L-105061` (F = Ξ_k; gap `G = (a,b)`, `g = |G|`; pair `(x_j, y_j)`
overhangs `G` iff `I_j ∩ G ≠ ∅`, `I_j = (x_j − y_j, x_j + y_j)`; gap weight
`W(G) = Σ_{overhanging} m_j·min(1, g²/(4y_j²))`). Call an overhanging pair
DEEP if `y_j < g/2` (weight term `m_j`) and SHALLOW if `y_j ≥ g/2` (weight
term `m_j·w_j`, `w_j = (g/2y_j)² ≤ 1`); `D_ov` = number of distinct deep
overhanging pairs; fattening radius `R4 = 2 + √3`; `Ĩ_j = (x_j − R4·y_j,
x_j + R4·y_j)`; shallow loads `W_sh = Σ m_i w_i`, `V_1 = Σ m_i w_i²`,
`V_2 = Σ m_i w_i³`; band loads `M_L^{(n)}, M_R^{(n)}` = multiplicity of
non-overhanging pairs within the level-n adjacency band (cot(π/2n)-scaled;
exact definitions in FINAL_LEMMA §0).

**Theorem C.** `extra(G) := #{real zeros of Ξ_{k+1} in G, mult} − 1` satisfies
`extra(G) ≤ 6·W(G)` on the union C-0 ∪ C-1 ∪ C-2 (and on C-3 instances with
ladder depth `k ≤ 3`); on general C-3 the proved constant is `2k` — i.e. the
cap holds with `A' = max(6, 2k)` regime-wise, NOT with a single absolute
constant on the four-regime union (hostile-review correction: a 7-pair
shallow configuration at `w = 0.65` forces ladder depth `k = 4`, so the
C-3 guarantee there is `8·W`, not `6·W`):

- **C-0** (no overhang): `extra(G) = 0`.
- **C-1** (isolated site): at most one pair has `Ĩ ∩ G ≠ ∅`: `extra(G) ≤ 6`.
- **C-2** (mixed deep + subcritical shallow — the new theorem): if (Sep) the
  fattened intervals `Ĩ_j` of the deep overhanging pairs are pairwise
  disjoint, (L2) `W_sh < 1`, (L4) `κ V_1 + G_4(M_L^{(4)}+M_R^{(4)}) < 1`, and
  (L6) `V_2 + G_6(M_L^{(6)}+M_R^{(6)}) < 1`, then every zero of `(Ξ_k'/Ξ_k)'`
  in `G` lies in a deep `I_j`, each deep interval carries at most 6 such zeros
  (with multiplicity), and `extra(G) ≤ 6·D_ov ≤ 6·W(G)`. Unbounded `D_ov` is
  allowed; only deep–deep separation is assumed (deep pairs under shallow
  intervals or near band-adjacent mass are absorbed by the (L4)/(L6) budgets);
  with no band-adjacent non-overhanging mass, (L2) alone implies (L4), (L6).
- **C-3** (all-shallow ladder): under LEMMA_B's conditions (B.7)/(B.8):
  `extra(G) ≤ 2k` (ladder depth k), hence `≤ 2k·W(G)`.

Constants: `κ = (11+5√5)/64 = 0.34656781…` (exact), `κ_6 = 1` (exact),
`G_4 ∈ [0.022542, 0.022543]` (rigorous enclosure), `G_6 = 0.04631627`
(numeric; rigorous closed-form fallback `2e^{−π/2} = 0.41576` — the (L6)
condition may be read with the fallback for a fully closed-form variant).

## 2. Proof

Full proof in `experiments/X-105063-count-cap/FINAL_LEMMA.md` §§2–3.
Mechanism of C-2 in one paragraph: at level 2, shallow positive parts total
`≤ (8/g²)·W_sh` against the endpoint floor `B ≥ 8/g²`, so under (L2) the
log-derivative's derivative is strictly negative OFF the union of deep
intervals — all critical zeros are confined to the disjoint deep sites. At
each site, the comparison function `Q = B − Σ_{i≠j} m_i φ'_i` is proved
convex at levels 4 and 6 (`Q'' > 0`, `Q'''' > 0`) by budget accounting:
endpoint floors `192/g⁴`, `15360/g⁶` versus the exact per-shallow-pair
damage `κ w² (192/g⁴)`, `w³ (15360/g⁶)` and the band-load `G_n` budgets;
other deep pairs are sign-favorable at `R4`-distance. Then the concavity
split at `x ± (2−√3)y` (center: `f'' < 0`; wings: `f'''' < 0` ⇒ `(h')''`
strictly concave, ≤ 2 zeros with multiplicity per wing) gives
`Z_mult((h')'', I_j ∩ G) ≤ 4`, and Rolle-with-multiplicity twice yields 6
per site. The [THRESHOLD] upgrade converts every additive form to the
multiplicative cap.

## 3. Verification

487 in-regime adversarial configurations (deep counts to 8, multiplicities
to 5, endpoint-hugging pairs, `W_sh` to 0.99, band-adjacent mass): zero
violations of the cap, of confinement, or of the per-site 6. Extremal
replay (mpmath 40 dps): `extra = 16` at `D_ov = 8` — exactly 2 per deep
site, and `extra/W = 16/15 > 1`: the cap's LINEAR growth in `W` is real
(any valid constant is ≥ 16/15; conjectured sharp value 2, proved 6). A
float64 midpoint-attribution artifact (66 spurious out-of-interval zeros)
was caught and resolved by 40-dps bisection (replay discipline). Residual
scans (600 configs: deep `R4`-clusters violating (Sep); `W_sh` to 3.02):
extras never exceeded 2 per deep site — the residual looks technical, not
structural.

## 4. Honest residual (what remains open of L-105061's pinned cap)

- **(R-C1) Deep clusters**: two or more deep overhanging pairs with
  intersecting `R4`-fattened intervals. Missing: a per-cluster bound
  `Z_mult(h', cluster) ≤ C·(cluster multiplicity)`; obstruction: overlapping
  dipole profiles destroy the fixed-sign concavity partition, and the
  Jensen/disk route stalls on an unabsorbable `log(g/y_min)` term.
  UPDATE 2026-08-23: `L-105067` (Theorem T-1) removes the separation
  hypothesis entirely under the decidable triple-set condition (T-EMPTY):
  cluster cap `16 m_K − 10`, hence `extra(G) ≤ 16 W(G)` with NO deep–deep
  separation; (Sep) ⟹ (T-EMPTY), so the regime strictly contains C-2. The
  residual shrinks to **R-C1′ = clusters with T_K ≠ ∅**, and `L-105067`
  Prop T-3 PROVES the 0-2-4 pointwise method cannot cross that frontier
  (sin-perturbation counterexample) — structurally new input required.
  UPDATE 2026-08-23 (later, final-pass wave): the structurally new input
  arrived — `L-105076` (Jensen window cap, complex-center cone lemma) crosses
  the T-nonempty frontier with NO triple-set condition: `<= 5.813` per distinct
  pair + 2.850 per swallowed real zero, under window admissibility + (DOM);
  the log(g/y_min) obstruction is eliminated; 104/104 adversarial T-nonempty
  clusters certified. The residual shrinks further to **R-J ⊊ R-C1′**
  (stopping-recursion failures, defined relative to the pinned cap constant
  C = 16 per L-105076 §3; empty on every tested configuration) ∪ R-C2.
- **(R-C2) Supercritical shallow mass**: `W_sh ≥ 1` outside LEMMA_B's ladder
  conditions (its remainders (R1)/(R2)), possibly mixed with deep pairs.

Any additive bound later proved on a residual regime upgrades
multiplicatively via [THRESHOLD]. `T-105060`'s conditionality is hereby
CONFINED to gaps falling in (R-C1) ∪ (R-C2); on all other gaps its
per-gap input is proved with the regime-wise constant `A' = max(6, 2k)`
(6 outside the shallow ladder). Note the residual (R-C2) is precisely
"(L2) or (L4) or (L6) fails outside C-3's ladder conditions" — band-adjacent
non-overhanging mass alone can break (L4)/(L6) even with `W_sh < 1`.

## 5. Falsifiers

An in-regime configuration with `extra > 6·D_ov` (check confinement first,
then per-site counts, exact arithmetic); a deep cluster with
`extra > 2·(pair multiplicity sum)` (would sharpen the residual's
difficulty and kill the conjectured sharp constant 2); an error in the
`κ`, `κ_6`, `G_4` constants (each independently re-derivable; `κ`, `κ_6`
exact closed forms).

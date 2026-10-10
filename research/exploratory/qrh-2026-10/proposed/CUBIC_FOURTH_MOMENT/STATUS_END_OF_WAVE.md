# Cubic fourth moment: status at the end of the wave

```text
Status: PROPOSED, CONDITIONAL, OPEN. Exploration-level status page; no new mathematics. Nothing
  here is reviewed by a human or integrated. No moment bound is proved. RH is not addressed.
Scope: the route of SKETCH.md (Theorem C4) after every same-day note in README.md. This page
  collects; it does not strengthen any statement or decide any open item.
Exact sources or dependencies: repo HEAD a814a313e6ec0aab2d15137efc08f646cc5a461a (working tree).
  SKETCH.md sha256 c610ba9d...bb0353 (unchanged since CUBIC_PROFILE_UNIFORMITY cited it);
  README.md e8a07dca...97ec4; LEMMAS_4BCD_GH.md 63890c82...c095; LF_THETA_THIRD.md
  ea4379ba...ad6c; A4_NO_OLDER_MOVING.md e3dac203...d84c. Reviews: ../../reviews/CUBIC_*.md,
  LEMMA18_1_REVIEW, LEMMA18_1_COMMON_SUPPORT, LEMMA18_1_CASE2_SEC188, LEMMA18_THETA_ROW_REVIEW,
  SEP30_L13_L45_REVIEW, SEP30_SEC4_REVIEW, and ../SEXTIC_FOURTH_MOMENT/README.md Sec. 4. Manuscript
  line numbers refer to pr908 31c706bb... paper.tex, sha256 42a5ee0f...deac6a3 (external,
  unreviewed; not re-read for this page; ranges are taken from the notes above).
What was actually run (nice -n 10, one process at a time):
  a4_checks.py 5/5 (4/4 controls); lf_theta_third_checks.py 14/14 (7/7), both outputs identical
  to the stored .out files; ../../reviews/cubic_hb_checks.py 27/27; lemmas_4bcd_gh_checks.py
  18/18 (12/12 controls, 62 s). No other script was rerun. No Lean, lake or comparator process.
Smallest remaining gap: (H-A) as listed in Sec. 2, above all Lemma 18.2 (centred-coefficient
  invariance) and the displayed Theta-row ledger F_1 + F_2 >= (5/6)v; see Sec. 4.
```

RH is unsolved. Labels: **PROVED HERE** = a written argument in this folder, not refereed;
**EXACT MODEL** = exact-arithmetic ledgers or LPs, which check the displayed inequalities, not the
analysis behind them; **IMPORTED** = taken from the external manuscript as stated.

## 1. The theorem as proposed (SKETCH.md Sec. 1.2, unchanged)

> **Theorem C4 (PROPOSED; CONDITIONAL on (H-A) and (H-B); OPEN).** For every `ε > 0` and `X ≥ 2`,
> `Σ_{q ∈ F'_3(X)} |L(1/2, χ_q)|⁴ ≪_ε X^{1+ε}`, where `F'_3` is the set of squarefree `q ≡ 1 (mod 9)`
> in `Z[ω]`, `q ≠ 1`, and `χ_q = (·/q)_3`. Sharp cutoff, no weights.

* **Single-window fallback (still stated, SKETCH l. 79 and risk item 13).** Assuming (H-A) only,
  without (H-B): `X^{53/51+ε}` (CUBIC_RELAXED_INDUCTION.md Sec. 3). CONDITIONAL.
* (H-A) plus the (2,1) forcing of Lemma 4.L instead of (H-B) gives `X^{1+ε}` with zero slack.
* The best unconditional bound found in the literature is `X^{4/3+ε}`. Theorem C4 would be new.
* Since PU, the loss in SKETCH Sec. 2.7 should read `(log X)⁴(log log X)⁴` (edit recommended, not applied).

## 2. What (H-A) now consists of

Review keys. n = 6: L18a = LEMMA18_1_REVIEW, L18b = LEMMA18_1_COMMON_SUPPORT, L18c =
LEMMA18_1_CASE2_SEC188, TR = LEMMA18_THETA_ROW_REVIEW (the latest n = 6 reading of 13953-14778),
L13 = SEP30_L13_L45_REVIEW, SEC4 = SEP30_SEC4_REVIEW. n = 3: CA = CUBIC_CENTRED_ATTACK, BR =
CUBIC_BOTH_RECTANGLES, AL = CUBIC_ALLOCATION_LOSS, PU = CUBIC_PROFILE_UNIFORMITY, HB =
CUBIC_HB_ATTACK. TL, RI, LC = the SKETCH §3 ledger scripts. All reviews are bounded agent
reviews; none is human or exact-SHA independent.

**2a. Still imported without an n = 3 re-derivation.** This list *is* (H-A). Marks: **IMPORTED AS
IS** (no n = 3 check beyond reading) or **EXACT MODEL ONLY** (the n = 3 ledger was checked exactly;
the estimate behind it is still imported).

| # | inherited statement | paper.tex lines | last n = 6 check | n = 3 mark | n = 3 evidence |
|---|---|---|---|---|---|
| H1 | mask erasure (old-eq:2.1a-b), with Lemma 4.10 `deleted-euler-factors` | 12602-12676; 1602-1646 | L18a §2.1; SEC4 §6 | IMPORTED AS IS | none |
| H2 | natural reflection to the padded core, profile `W♯`, rowwise suprema taken before centring | 12677-12830 | L18a §2.1 | IMPORTED AS IS | read structurally (CA §2.2, HB §2); cubic input is Lemma 4.K (R14) |
| H3 | Lemma 4.8 `hecke-strip-growth` (primitive functional equation, entireness) | 1415-1529 | SEC4 §4 | IMPORTED AS IS | used via Lemma 4.K and I2 |
| H4 | comparison and centring: `Σ\|S\|² ≤ 2Σ\|Δ\|² + 2Σ\|comp\|²`, same profiles, `Y_1 = Z^L` | 12940-13010 | L18a §2.3; L18c §1.1 | EXACT MODEL ONLY | min of the four lengths is exactly `L` under the caps at `L ≈ 0.42M` (BR [E1]; RI [N1]) |
| H5 | centred coefficient `D_𝐛`, retained formal difference, aggregate support box | 13012-13113 | L18b (as used); L18c §6 | IMPORTED AS IS | rectangle handling read (BR steps 0c-0d) |
| H6 | first transform, analytic part: row ball, whole-dyad localization, Poisson in `k`, Cauchy-Schwarz in `h` | 13114-13178, 13226-13268, 13331-13348 | L18a §2.4; L18b §2 | IMPORTED AS IS | rectangle handling read (BR steps 1-2, 6, 10) |
| H7 | first-transform common-support allocation, Möbius `s`, label counts (Rankin, divisor), target (2.5) | 13192-13208, 13300-13306, 13350-13409 | L18b §2 (24/24) | EXACT MODEL ONLY | AL 56/56, min slack exactly 0; label-count estimates not re-read |
| H8 | one-measure Fourier separation of kernels and inverse roots (Lemmas 4.5 `smooth-calculus`, 4.7 `kernel-seminorms`) | 13307-13335, 13899-13935; 1123-1413 | L13 §4 (33/33); SEC4 §3; uses read, not replayed | IMPORTED AS IS | whole-product kernels keep cancellation (BR float P2; empirical) |
| H9 | Gauss-row enlargement by positivity (zero slots) | 13411-13452 | L18a §2.5 | IMPORTED AS IS | none |
| H10 | second transform, analytic part: Poisson in `h`, diagonal count, `j ≠ 0` localization, extraction bijection | 13596-13697 | L18a §2.6; L18b §3 | IMPORTED AS IS | diagonal ledger (2.12) exact (TL [A5]); bijection exact (AL [A7]) |
| H11 | second-transform ledgers: (2.13), (2.14), exponent table, `𝔱`-allocation, volume `a_0 − b_2 + 2θ_N` | 13790-13933, 14392-14431 | L18b §3; TR §6 | EXACT MODEL ONLY | AL [S3]-[S8]; TL [A3]; θ-free per LF §2 |
| H12 | construction facts (a)-(c) behind A4: column-twist form, columns `u = D_2 a`, earlier primes coprime to later columns | 12990-13085, 13180-13290, 14317-14324 | L18b §3; TR (context) | IMPORTED AS IS | named as A4N's remaining gap |
| H13 | raw child normalization; "no clipping has occurred" | 13998-14090 | L18a §2.6; L18c §1.3 | IMPORTED AS IS | BR step 20 |
| H14 | non-Θ children: triangle split, per-rectangle clipping, induction call | 14119-14300 | L18a §2.6; L18c §1.3-1.4 | EXACT MODEL ONLY | costs `0·M`, at most `2θ_N` per edge (BR [E4]) |
| H15 | **Lemma 18.2** `centered-coefficient-invariant` | 13953-13996 | TR §2.1, §5 | EXACT MODEL ONLY | step-by-step n = 3 reading, verdict (a) (BR §2-3); rect_exact 12/12 |
| H16 | **Lemma 18.3** `centered-lattice-cancellation` | 14545-14680 | TR §2.2, §4 (19/19 exact, 14/14 float) | IMPORTED AS IS | float numerics only, 18/19 ([L2b] uninformative) (CA §3); Θ closed forms exact [L0] |
| H17 | Θ-row application (2.18), (2.18h): saving `r = (L − v)_+` survives the allocation | 14681-14740 | TR §6-7 | EXACT MODEL ONLY | LC [L4]; AL [S8]; CA [P2] |
| H18 | completion of the induction: loss envelope, no compounding in the exponent, choice order (2.1i) | 14779-14984 | L18c §2 | IMPORTED AS IS | reused with `k = 2` stages under (H-B) |
| H19 | **A8**: finite-order profile-uniformity clause | 12571-12578, 719-722; justified 14942-14973 | no independent line review on record (PU header) | IMPORTED AS IS | its use in the application is closed (PU (a)) |

Also used as standard (SKETCH I6, not (H-A)): lattice Poisson, powerful-ideal and ideal counts,
Rankin, divisor bounds, Mellin and Stirling. Lemma 4.9 and the amplifier are case 2 only (unused).

**2b. Re-derived at n = 3, so no longer in (H-A).** All are PROPOSED and unrefereed.

| # | manuscript object (lines) | n = 3 replacement | where |
|---|---|---|---|
| R1 | Lemma 13.2 `eq:gauss-local` (7055-7079) | Lemma 4.A | SKETCH §4 (proved) |
| R2 | Lemma 13.3 `full-correlation` (7081-7190) | Lemma 4.B | LEMMAS_4BCD_GH §3 |
| R3 | Lemma 13.4, child character (7196-7247) | Lemma 4.C | LEMMAS_4BCD_GH §1 |
| R4 | `𝔯`-rule, `ξ_𝔯`, bridge CRT and phases (13209-13276); Lemmas 4.3-4.4 | Lemma 4.D; `R ≡ 1` by cubic reciprocity (I1) | LEMMAS_4BCD_GH §2 |
| R5 | zero frequency "mod six" (13180-13191) | exponents `≡ 0 (mod 3)` force a powerful product | CUBIC_FOURTH_MOMENT_TRANSFER §3 item 2 |
| R6 | `B_c`, `B_d` and (2.6) (13379-13409) | Lemma 4.E | SKETCH §4 (proved) |
| R7 | Gauss-row zero `h = 0` (13572-13594) | Lemma 4.I | SKETCH §4 (sketched only) |
| R8 | second-transform local rules and table, `t_2`, `V`, `e_p` (13699-13800) | Lemma 4.G(a) | LEMMAS_4BCD_GH §5 |
| R9 | A4, "no existing moving character" (14349-14353) | proved given H12 | A4_NO_OLDER_MOVING §3 |
| R10 | Lemma 4.1 and the Θ-row forced residues and count (646-699; 14325-14390) | Lemma 4.H, Corollary 4.H (`f = v_1`) | LEMMAS_4BCD_GH §4; A4N |
| R11 | (2.15)-(2.16), `F_2` with `θ` | (LF) derived with `θ` generic | LF_THETA_THIRD §3 |
| R12 | `κ` from `F_1`, (2.17) | Lemma 4.F (`κ_1 = 5/6`), Lemma 4.G(b) (`κ_2 = 1`) | SKETCH §4; LEMMAS_4BCD_GH §5 |
| R13 | (2.19) with `5M/6`, `L = M/4` (14760-14770) | Lemma 4.J with `2M/3`, A-dependent `L` | SKETCH §4 (proved given H15-H17) |
| R14 | conductor bound and functional equation for rows (12686-12704) | Lemma 4.K | SKETCH §4 (sketched; **not reviewed**) |
| R15 | induction order, one centred stage (12903-12938, 14799-14804) | two-stage nested order | (H-B), a separate hypothesis |

## 3. Risk register, updated (SKETCH Sec. 5, items 1-13)

| # | step | status now | source |
|---|---|---|---|
| 1 | application (SKETCH Sec. 2) | PROVED HERE given Statement C; profile uniformity closed, verdict (a), given A8 (H19) | SKETCH §2; ../../reviews/CUBIC_PROFILE_UNIFORMITY.md |
| 2 | Lemmas 4.A, 4.E, 4.F | PROVED HERE; 4.E/4.F zero-slack points confirmed exactly; 4.F uses the manuscript's `F_1` (H11) | SKETCH §4; ../../reviews/CUBIC_ALLOCATION_LOSS.md |
| 3 | Lemmas 4.B, 4.C, 4.D | PROVED HERE (was "sketched"); a reciprocity factor restored; notation clash `𝔯` flagged | LEMMAS_4BCD_GH.md §1-3, §6 |
| 4 | Lemma 4.G (`κ_2 = 1`) | PROVED HERE given H11-H12: (LF) derived, A4 proved; `f = v_1`, not `2v_1` | LEMMAS_4BCD_GH.md §5; LF_THETA_THIRD.md; A4_NO_OLDER_MOVING.md |
| 5 | Lemma 4.H, count `Z^{(m'−f)/3}` | 4.H PROVED HERE (27 `S`-characters; ideals prime to `3a`); Corollary parts 1-4 proved given H12 | LEMMAS_4BCD_GH.md §4; A4_NO_OLDER_MOVING.md |
| 6 | Lemma 4.J (centred deficit) | PROVED HERE given H15-H17; its binding point `v = L` uses no lattice saving | SKETCH §4; ../../reviews/CUBIC_CENTRED_ATTACK.md |
| 7 | Lemma 4.K (row functional equation) | **sketched; not reviewed by any note**: still open | SKETCH §4 |
| 8 | (H-B) nested order | attacked twice, no break; needs `ξ ≤ μ*(δ)ρ/2` and profile closure through 3 reflections per width level | ../../reviews/CUBIC_HB_ATTACK.md; CUBIC_NESTED_REDTEAM.md |
| 9 | A5: Lemmas 18.2, 18.3 at `L ≈ 0.42M` | IMPORTED (H15-H17); survives attack (a); rectangle question closed (a); failure is all-or-nothing | ../../reviews/CUBIC_CENTRED_ATTACK.md; CUBIC_BOTH_RECTANGLES.md |
| 10 | A2, A4 allocations | IMPORTED, re-instantiated at n = 3: no loss, min slack exactly 0 (H7, H11) | ../../reviews/CUBIC_ALLOCATION_LOSS.md |
| 11 | A7: Lemmas 4.5, 4.7 | IMPORTED AS IS (H8); no n = 3 reading; invocation uniformity unchecked | ../../reviews/SEP30_L13_L45_REVIEW.md |
| 12 | Lemma 18.1 case 1 (sextic) as a whole | not checked by any human; four bounded agent readings, no wrong step | L18a, L18b, L18c, TR |
| 13 | single-window fallback `X^{53/51+ε}` | CONDITIONAL on (H-A) only; unchanged | CUBIC_RELAXED_INDUCTION.md §3 |

Tolerances (exact, two stages): a loss confined to the centred deficit is tolerated below
`(11 − 147δ)M/432` (CA, AL); a loss in an order-free ledger (H7, H11) is fatal for any `cM`, `c > 0`;
a loss in `F_1`/`F_2` is fatal once the coefficient of `v` drops below `3 − √5 ≈ 0.764` (AL §4).

## 4. Smallest statement whose failure breaks the route now

For `n = 3`, every centred input in the padded core (original or a reflected comparison) must satisfy,
uniformly over all common-support and `𝔱`-allocations and for `L ≤ min(A/2, A − M/2)`,

    A − 2M/3 − F_1 − F_2 − (L − v)_+  ≤  A − 2M/3 − (5/6)L + O(σ + δ + ξ).

The cubic arithmetic in it is now re-derived (2b). It can still fail in two inherited ways:

* **Qualitative (all-or-nothing):** Lemma 18.2 (H15) fails, i.e. some operation before the Θ/non-Θ
  row split or in the Θ branch acts on one rectangle only. A full Θ-row main term survives, a loss
  up to `M/3`, which is `144/11` times the tolerance. The sextic case 1 fails with it.
* **Quantitative (tightest):** at `v = L` there is no lattice saving, and `F_1 + F_2 ≥ (5/6)v` has
  zero slack at `(2,1)` primes and nonunit `i = 1, 2`. If the displayed ledgers (H7, H11) or the
  manuscript's `F_1` formula do not describe the analysis there, a whole-deficit loss of
  `(11 − 147δ)M/432` (`≈ 0.022M-0.025M`) breaks the two-stage route; `M/12` breaks every nested one.

## 5. What a human referee would need to read (in order)

Estimates: about 50 source lines per page; manuscript lines are TeX source lines.

| step | what | lines | ≈ pages |
|---|---|---|---|
| 1 | this page; SKETCH §1-3 (theorem, hypotheses, application, induction) | 180 + 372 | 10 |
| 2 | paper.tex conventions and Lemma 18.1 statement | 557-760, 12477-12601 | 7 |
| 3 | **decisive**: Lemma 18.2, Θ rows, Lemma 18.3, (2.15)-(2.19) | 13953-13996, 14312-14778 | 10 |
| 4 | reductions, reflection, comparison, both transforms, asking "does any step touch one rectangle, plain or scale only?" (BR §2 is a map) | 12602-13952 (skip 12831-12902, 13453-13570) | 24 |
| 5 | child normalization, non-Θ children, completion and order of choices (A8) | 13998-14310, 14779-14984 | 10 |
| 6 | helpers: Lemmas 4.5-4.8, 4.10 | 1123-1529, 1602-1646 | 9 |
| 7 | cubic lemmas: SKETCH §4, then LEMMAS_4BCD_GH, LF_THETA_THIRD, A4_NO_OLDER_MOVING; write out Lemma 4.K | 187 + 528 + 265 + 276 | 25 |
| 8 | (H-B): CUBIC_RELAXED_INDUCTION §4 and CUBIC_HB_ATTACK §1-4 | about 400 | 8 |
| 9 | application inputs: DDDS (arXiv 2410.03048v2) Secs. 1 and 3; PU §1-3 | about 300 + 200 | 10 |

Total: about 3,000 manuscript lines (≈ 60 pp), 2,400 repository lines (≈ 50 pp), plus DDDS. Steps 2-6 are
the same reading a referee of the sextic Lemma 18.1 case 1 would need; the cubic route adds 7-9.

## 6. Not done here

No manuscript line was re-read; no open item was decided; Lemma 4.K was not reviewed; the exact
models were not re-derived. The recommended SKETCH edits (A8 in the (H-A) table, the Sec. 2.7
loss, the Corollary 4.H third-bullet wording) are recorded in README.md and still not applied.

## Correction note (end of wave)

Table 2b counts 15 entries. Of these, R7 (Lemma 4.I) is only sketched, R14 (Lemma 4.K) is
sketched and unreviewed, and R15 is hypothesis (H-B), a replacement rather than a re-derivation.
So the honest count is 12 re-derived at n = 3 (PROPOSED), 2 sketched, and 1 replaced by (H-B).
The route is conditional on (H-A), (H-B), Lemma 4.K and the correctness of Lemma 18.1 case 1.

Update (end of wave): R7 (Lemma 4.I, corrected form) and R14 (Lemma 4.K) now have written
PROPOSED proofs ([LEMMA_4I.md](LEMMA_4I.md), [LEMMA_4K.md](LEMMA_4K.md)). The count becomes 14
re-derived at n = 3 (PROPOSED) and 1 replaced by (H-B).

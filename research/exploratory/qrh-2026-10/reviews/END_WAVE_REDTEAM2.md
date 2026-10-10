# End-of-wave red team 2: explicit PNT, Part-I-free route, formal packet, Addendum C

```text
Status: REVIEW (adversarial, bounded, one pass). Wording, provenance, consistency and a spot
  check of the EXPLICIT_PNT_7_8 derivations. No existing file was edited. Nothing here is a
  verdict on any mathematics beyond the spot checks listed, and nothing bears on RH or GRH.
Scope: everything changed in research/exploratory/qrh-2026-10 between e5731afb5 and HEAD
  0639cd715, including the 26 fixes of END_WAVE_REDTEAM.md applied in d99030d91.
Exact sources or dependencies: the files above at 0639cd715; the upstream challenge files at
  ref 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6 (read with git show); canonical/ and the 22
  research/integrated/**/CLAIMS.tsv files (collision grep).
What was actually run: reading; grep; sha256sum of the quoted scripts, results and challenge
  files (all match the quoted prefixes); git show of the four challenge .lean imports (each is
  `import Mathlib`); a short stdlib+sympy Python check of theta(4547), theta(12967),
  theta(118189) (= 4462.6872, 12840.3150, 117744.7057) and of the psi left-limit ratio at 227
  (0.002977). Lemma Z (Z1)-(Z3), the regime I-III constants, b, d, L* = 2d/b, the regime II/III
  junction at L = 189.155, and Corollaries 2-4 were re-derived by hand. No Lean, Lake, comparator
  or nanoda process was started, and no committed script was re-run.
Smallest remaining gap: the Siegel corollary is described three different ways (effective /
  explicit / existential, accepted / pending), and the Part-I-free route is summarised as
  "proves 7/8" in five places. Items 1, 5-8 first.
```

RH is unsolved. Severity: **blocking** = misstates what was checked; **should-fix** = misleading,
stale or inconsistent; **nit** = cosmetic. No blocking item was found.

## Issues

**1. Should-fix.** `reviews/LEAN_BUILD_ATTEMPT.md:177-180`
* Text: "therefore has two independent Lean proofs here: the Oct 1 route; the wave's three-line corollary".
* Problem: the Oct 1 route has a build, `#check` and `#print axioms` only. Its comparator run is
  still pending (same file, table row 6). The two proofs share Mathlib, the kernel and the trust
  base. "Independent" here means only that they share no `OAI.*` module.
* Replace with: "therefore has two Lean proofs here that share no OAI module: the Oct 1 route
  (built, axioms standard; comparator pending) and the wave's three-line corollary of the 7/8
  Dirichlet theorem (comparator accepted, below)."

**2. Should-fix.** `reviews/LEAN_BUILD_ATTEMPT.md:4-5, 11-12, 18-22` (header)
* Text: Status "comparator ACCEPTS the 7/8 zeta challenge, Addendum B"; Scope "Hecke: module built
  and `#print axioms` standard"; "What was actually run" ends at "comparator (Addendum B)".
* Problem: this is stale against Addendum C. The header omits the Hecke build, the 9242-job Siegel
  build, the nanoda build and three accepted comparator runs.
* Replace with: Status "... comparator ACCEPTS the zeta (Addendum B), Dirichlet, Hecke and
  wave-Siegel challenges (Addendum C); QRHWaveStrip, upstream SiegelZeros and nanoda pending".
  Append to "What was actually run": "Addendum C: Hecke build (7062 jobs), Oct 1 SiegelZeros build
  (9242 jobs), nanoda_lib build, comparator on DirichletSevenEighths, HeckeSevenEighths and
  SiegelFromSevenEighths."

**3. Should-fix.** `reviews/LEAN_BUILD_ATTEMPT.md:166-171` and `:187`
* Text: "After the regenerable `ir/*.setup.json` files were deleted ... built the missing 306 OAI
  modules ... plus their PNT+ dependencies"; "These are run sequentially with the same tools and settings".
* Problem: no start or end time is given for the Siegel build or the deletion. The commit times
  suggest that the build overlapped the Dirichlet comparator run: that run went from 17:20:31 to
  17:38:59, and the build was committed at 17:40:39. The build ran in the same Lake tree that
  comparator reads. Comparator assumption 2 already fails, but this would be a further,
  undisclosed deviation.
* Replace with: add the build's start and end UTC times. If it overlapped a comparator run, add a
  trust item: "the Oct 1 build wrote new oleans into the same tree while the Dirichlet comparator
  run was in progress; no existing olean's mtime changed (or: not checked)."

**4. Should-fix.** `SYNTHESIS.md:57-58`
* Text: "**Comparator accepts all three upstream 7/8 challenges (zeta, Dirichlet, Hecke family)** ... (LEAN_BUILD_ATTEMPT.md, Addenda A–B)".
* Problem: the Dirichlet and Hecke acceptances are in Addendum C.
* Replace with: "(LEAN_BUILD_ATTEMPT.md, Addendum B for zeta, Addendum C for Dirichlet and Hecke)".

**5. Should-fix.** `lean/README.md:85-87`; `SYNTHESIS.md:91-93`
* Text: lean/README "So this is an *effective* Landau–Siegel-type bound with constant `(log 3)/8 ≈ 0.137`. It is conditional only on accepting the imported 7/8 Dirichlet theorem"; SYNTHESIS "Comparator accepts it against the upstream Oct 1 challenge, and the constant is explicit".
* Problem:
  * Comparator checked the `∃ c` statement. Addendum C itself says that this "says nothing about
    whether `c` is effective".
  * The explicit constant lives in the helper `gap_of_real_zero`. That helper is kernel-checked in
    the build and replayed as a dependency, but it is not a comparator target, and neither
    `#check` nor `#print axioms` was run on it (`checks/CorollaryAxioms.lean`).
  * The packet's misreading 4 (`SEP30_7_8_FORMAL_PACKET/README.md:351-353`) frames the same fact
    the opposite way.
  * "Conditional only on" omits the Addendum B trust assumptions.
* Replace with (lean/README): "So, conditional on the 7/8 Dirichlet theorem (comparator-accepted
  under the Addendum B assumptions), the constant is explicit: `(log 3)/8 ≈ 0.137`. It is read off
  the helper `gap_of_real_zero`, which is kernel-checked but is not a comparator target. This is a
  consequence of a zero-free half-plane, not an unconditional effective Siegel bound."
  (SYNTHESIS): "Comparator accepts the `∃ c` statement against the upstream Oct 1 challenge; the
  helper `gap_of_real_zero` gives `c = (log 3)/8` explicitly (lean/README)."

**6. Should-fix.** `proposed/SEP30_7_8_FORMAL_PACKET/README.md:151, 188, 351-353, 360-362`
* Text: ":151 comparator **pending**"; ":188 ... `OAI.QRHWave.SiegelFromSevenEighths` | pending"; ":353 and that corollary has no comparator run yet"; ":361-362 The Hecke theorem was accepted after this draft was written."
* Problem: this is stale. The Siegel corollary was accepted (1082 s, `0639cd715`). The Hecke row was
  updated in place, but the Siegel rows were not.
* Replace with: ":151 built; axioms standard; comparator: Siegel corollary **accepted** since
  (1082 s); strip pending"; ":188 pending at drafting; **accepted** since (1082 s)"; ":353 ...
  existential. Comparator has since accepted it (1082 s). The explicit `c` is in the helper
  `gap_of_real_zero`, which is not a comparator target"; ":361-362 The Hecke theorem and the
  Siegel corollary were accepted after this draft was written; the Oct 1 route is still pending."

**7. Should-fix.** `SYNTHESIS.md:70-71`; `README.md:94`; `reviews/SEP30_VERIFICATION_MAP_V2.md:460-461`; `proposed/SEP30_7_8_FORMAL_PACKET/README.md:223-225`; `proposed/PART1_FREE_7_8/README.md:5-6`
* Text: "proves 7/8 from `β* ≤ 1` alone" (SYNTHESIS, packet); "proves 7/8 from `β* ≤ 1`"
  (README, map); "the 7/8 statement of the Sep 30 manuscript proved from beta_* <= 1 alone"
  (PART1_FREE_7_8 Status).
* Problem: these are summaries of a PROPOSED composition that has had only same-family agent
  review. The unhedged verb reads as an established proof. No file says "established".
* Replace "proves" / "proved" with "would prove (PROPOSED; bounded same-family review only)" in
  each place. For PART1_FREE_7_8 Status: "a proposed proof of the 7/8 statement from beta_* <= 1
  alone".

**8. Should-fix.** `reviews/SEP30_VERIFICATION_MAP_V2.md:459-463`
* Text: "It gives verdict (A): Part II as written, plus the extended endpoint count, proves 7/8 from `β* ≤ 1`. ... It adds new obligations: Remark 19.3 and two short proposed lemmas."
* Problem: Review 2 is not recorded. The verdict is "(A) with corrections": `λ ≤ 527/300`, Lemma
  17.6 stays, and Remark 19.3 is at most Rp. The proposed folder also now has three lemmas
  (P1F.0-P1F.2).
* Replace with: "It gives verdict (A), PROPOSED; a second same-family review gives '(A) with
  corrections' (PART1_FREE_ROUTE_REVIEW2.md: `λ ≤ 527/300`, Lemma 17.6 stays, Remark 19.3 at most
  Rp). New obligations: Remark 19.3 (as Lemma P1F.0, Rp) and P1F.1-P1F.2
  (proposed/PART1_FREE_7_8/)."

**9. Should-fix.** `reviews/PART1_FREE_ROUTE.md:251, 323`; `reviews/PART1_FREE_ROUTE_REVIEW2.md:253`
* Text: ":251 Stay (57): as in the substitution column of the v2 map: R 43, Rp 5, I 5, A 4. The four A nodes are Lemmas 4.2, 4.3, 4.4 and 17.1"; ":323 four of them A (Lemmas 4.2-4.4 and 17.1)"; REVIEW2 ":253 ... four of them A".
* Problem: map v2.1 (§10) predates both notes. Under v2.1 the 57 kept nodes are R 49, Rp 6, I 2,
  A 0, as `proposed/PART1_FREE_7_8/README.md:69-71` and SYNTHESIS:47 already say.
* Replace with: "Stay (57): v2.1 substitution column, R 49, Rp 6, I 2, A 0 (Lemmas 4.2-4.4 now R,
  17.1 Rp)". At :323, and as a dated note under REVIEW2:253: "keep their v2.1 statuses (6 Rp, 2 I)".

**10. Should-fix.** `EXPLICIT_PNT_7_8.md:347`
* Text: "Theorem 1 beyond `e^{190}` breaks only if CHJ Thm 1.2 failed at `log x ≥ 40` by more than a factor of 4 in `M`."
* Problem: "only" is too strong. Beyond `e^{190}`, Theorem 1 also rests on HSW Cor. 1.2 (Lemma Z),
  on Platt–Trudgian (the `x^{1/2}` part), on the identification of Mathlib's `riemannZeta` with
  ζ, and on H(7/8) itself.
* Replace with: "Among the imported constants, Theorem 1 beyond `e^{190}` is most exposed to CHJ
  Thm 1.2. It survives a fourfold error in `M`. It also rests on HSW Cor. 1.2, Platt–Trudgian and
  H(7/8) (with the trust assumptions of LEAN_BUILD_ATTEMPT)."

**11. Should-fix.** `README.md:92, 98`
* Text: ":92 **comparator accepts the upstream 7/8 zeta challenge** (Addendum B, with trust assumptions)"; ":98 ... the Oct 1 Siegel-zero challenge statement with `c = (log 3)/8`. Axioms standard".
* Problem: stale. The SYNTHESIS and AGENDA C1 already list the Dirichlet, Hecke and Siegel-corollary acceptances.
* Replace with: ":92 ... comparator accepts the upstream zeta (Addendum B), Dirichlet and Hecke
  challenges and the wave's Siegel corollary (Addendum C); strip, upstream Siegel and nanoda
  pending"; ":98 ... Axioms standard; comparator accepted the Siegel corollary (Addendum C); the
  strip's comparator run is pending".

**12. Should-fix.** `reviews/SEP30_LEAN_CORRESPONDENCE.md:44` (header)
* Text: "(zeta: comparator-accepted; Dirichlet: `#print axioms` only)".
* Problem: the body (:289) was updated and the header was not.
* Replace with: "(zeta and Dirichlet: comparator-accepted, LEAN_BUILD_ATTEMPT Addenda B-C)".

**13. Should-fix.** `CONDITIONAL_CONSEQUENCES.md:23`
* Text: "Statements that need the Hecke family or the Oct 5 claim are unchanged."
* Problem: stale. The Hecke challenge is now comparator-accepted, but its fidelity to the paper's
  family is a reading-level, single-pass check.
* Replace with: "Statements that need the Hecke family: comparator accepted the Lean Hecke
  theorem (Addendum C), but its match to the paper's family rests on HECKE_LEAN_FIDELITY.md
  (reading-level, one agent pass). Statements that need the Oct 5 claim are unchanged."

**14. Nit.** `lean/README.md:20-22`
* Text: "Comparator runs on comparator/*.json: see ../reviews/LEAN_BUILD_ATTEMPT.md, Addendum C (not run when this header was written)".
* Problem: lines 9-10 of the same header report the Siegel corollary as ACCEPTED.
* Replace with: "Comparator: SiegelFromSevenEighths.json accepted (1082 s); QRHWaveStrip.json pending (Addendum C)".

**15. Nit.** `SYNTHESIS.md:72-73, 77-80`
* Text: "with margin `≤ −7/96 − Δ`"; "makes four bookkeeping corrections (one loss bound; Lemma 17.6 stays; Remark 19.3 rated no better than Rp)".
* Problem: only three of the four corrections are listed (gate T2's line-range-only coverage is
  missing), the bound is not given, and the corrected margin carries `+(13/16)λ + 2ζ`.
* Replace with: "margin `≤ −7/96 − Δ` up to the `O(ε)` losses `(13/16)λ + 2ζ`"; "four corrections:
  `λ ≤ 527/300` in P1F.2; gate T2 checks line ranges only; Lemma 17.6 stays; Remark 19.3 at most Rp".

**16. Nit.** `EXPLICIT_PNT_7_8.md:198`
* Text: "Asymptotically the constant tends to `2·0.0025498 ≈ 0.0051`."
* Problem: `0.0025498` is the supremum over `L ≥ 190`, not the limit. The limit is `2/(128π)`.
* Replace with: "Asymptotically the constant tends to `2/(128π) ≈ 0.00497`; uniformly on `x ≥ e^{190}` it is at most `2·0.0025498 ≈ 0.0051`."

**17. Nit.** `EXPLICIT_PNT_7_8.md:122`
* Text: "the first 200 zeros give `Σ 2/(1/4+γ²) = 0.04207 < s_low`".
* Problem: a partial sum of positive terms is trivially below `s_low`. What is checked is that it lies below the (Z4) bound.
* Replace with: "`... = 0.04207`, below the (Z4) bound `0.046191`".

**18. Nit.** `EXPLICIT_PNT_7_8.md:46`
* Text: "`1.02·10^{26}`".
* Problem: Table R (:273) and the results file give `1.013·10^{26}`. The rounding is in the safe direction but at a different precision from the other entries.
* Replace with: "`1.013·10^{26}`".

**19. Nit.** `EXPLICIT_PNT_7_8.md:349`; `reviews/PART1_FREE_ROUTE.md:340`
* Text: "Addendum: independent sweep of the small-x ranges (coordinator, same day)"; "It independently re-derived the census".
* Problem: "independent" is used for same-family agent work (AGENTS.md; docs/REVIEWING.md).
* Replace with: "Addendum: separate float64 sweep of the small-x ranges"; "It re-derived the census from its own regex".

**20. Nit.** `ROBIN_GRADED.md:7, 30-31`
* Text: ":7 n_0 NOT made effective"; ":30-31 The ineffective `n_0` of Sec. 3 is made explicit in EXPLICIT_PNT_7_8.md".
* Problem: the explicit threshold comes from a different lemma (Lemma J via CHJ). Lemma K and
  `17A ≤ 0.79` are not used (EXPLICIT_PNT_7_8.md:333). The header at :7 now contradicts the note.
* Replace with: ":30-31 ... is made explicit, by a different route (Lemma J via Cully-Hugill–Johnston, not Lemma K), in ..."; ":7 ... n_0 not effective here; an explicit version is in EXPLICIT_PNT_7_8.md (PROPOSED)".

**21. Nit.** `reviews/LEMMA18_THETA_ROW_REVIEW.md:54`
* Text: "**Lemma 18.3 (lattice cancellation).** Its proof is correct as written."
* Problem: this is stronger than the note's own verdict ("no wrong step found in the lines read"; Status, :5).
* Replace with: "No wrong step was found in its proof."

**22. Nit.** `reviews/HECKE_LEAN_FIDELITY.md:191`
* Text: "The formal content is what comparator and `#print axioms` certify for that statement".
* Problem: when this was written (`995eb31fd`), the Hecke comparator run had not finished (`047538202`). "Certify" also overstates a machine check made under trust assumptions.
* Replace with: "... is what `#print axioms` and (since 047538202) comparator check for that statement ...".

**23. Nit.** `proposed/OCT5_11_12_PACKET/README.md:359`
* Text: "Comparator has accepted the zeta and Dirichlet challenges".
* Problem: :319-321 of the same file says zeta, Dirichlet and Hecke.
* Replace with: "Comparator has accepted the zeta, Dirichlet and Hecke challenges".

**24. Nit.** `AGENDA.md:205`
* Text: "That would give a paper-level 7/8 proof with no Part I and no 11/12 import."
* Problem: the 57 kept nodes still include 6 Rp and 2 I.
* Replace with: "... no 11/12 import, at the bounded-review level of its 57 kept nodes (6 Rp, 2 I)."

## Checked and fine

* **EXPLICIT_PNT_7_8, Theorem 1.**
  * Lemma Z (Z1)-(Z3) re-derived from HSW by partial summation; constants match.
  * Regime I (`T = √x/4`), II (`T = H_0`) and III (`T = 8πM x^{1/8}`) are admissible for CHJ.
  * `log(T/2π) = L/8 + log 4M`; `b = 0.169`, `d = 113.417`, `L* = 1342.2`, `b²/4d = 6.30·10⁻⁵`.
  * The regime-III bracket is positive from `L = 189.155` (where `T = H_0`).
  * H(7/8) is used only for `H_0 < |γ| ≤ T`. Below `e^{190}` the sum stops at `H_0`, consistent with the optimal `T ≈ 8πM x^{1/8}` reaching `H_0` at `L = 189.155`.
  * No sign or regime slip found.
* **Corollaries 2-4 and the Robin section.**
  * Corollaries 2-4 re-derived (partial-summation identity, `0.0026(1 + 8/(7 log X)) ≤ 0.002651`, `δ ≤ 0.2455`).
  * Lemma J steps 1-6 and Theorem R Cases A/B checked.
  * θ thresholds 4462.69, 12840.4, 117744.8 recomputed. The ψ ratio at the 227 left limit is 0.00298.
  * The sweep's endpoint checks suffice, because `C·g′(x) < 1` there.
* **Imported theorems.** Every one carries an arXiv id and version, and each is used inside its
  stated range: Büthe `x > 59/599/2657` with `4.92√(x/log x) ≤ T` up to `2.169·10^25`; CHJ
  `x ≥ e^{40}`; HSW `T ≥ e`.
* **C = 1.41.** Consistent with ROBIN_GRADED (`e^γ·0.789 ≤ 1.41`). Here it is reached via Lemma J
  with `c_U = 0.7579 ≤ 1.41e^{−γ} = 0.7917`, not via `17A` (see item 20).
* **Cross-file numbers.** These match their sources:
  * EXPLICIT constants and thresholds `0.0026`, `0.00266`, `0.006`, `227`, `967`, `2657`, `4462.69`, `10^{110}`;
  * run times 1094, 1108, 1096, 1082 s;
  * margin `−7/96`, `527/300`, gates 32/32, 10/10, 14/14, 43/43, 14/14, 19/19, 14/14;
  * map v2.1 counts 49/6/2/0 of 57, `67%` and `99%`;
  * 14/8/43 Lean nodes.
* **Hashes.** The script, results and challenge sha256 prefixes all match.
* **Imports.** All four challenge modules `import Mathlib` only, so Addendum C's
  statement-meaning remark for Dirichlet holds.
* **Formal packet.** `IMPORTED.QRH.SEP30.FORMAL_ZERO_FREE_7_8` is unique: no hit in canonical/
  or the 22 CLAIMS.tsv files, and no `IMPORTED.` ID exists there. Statement and plain-math
  reading match the Lean types, including the `[NeZero q]` / principal-pole hypothesis. The trust
  rows T1-T10 and `trust_assumptions` match Addendum B: cached Mathlib oleans, precompiled
  solution, best-effort landrun, single kernel, nanoda queued.
* **PART1_FREE folder.**
  * The README and REMARK_19_3 state "(A) with corrections", `λ ≤ 527/300`, Lemma 17.6 kept and
    P1F.0 at Rp, and ask for a review outside this model family.
  * The Lean `high_source_margin` slope hypothesis gives exactly `527/300` at `δ = 5/6`.
  * NC3/FC9 (`γ = 1/8`) are consistent.
* **HEIGHT_LEVELS §6.** Strip claims are limited to `#print axioms`; the comparator claim covers
  only the imported theorems.
* **Prior red-team fixes.** The fixes in d99030d91 are applied as described. Apart from items 12,
  13 and 23 (staleness introduced by later runs), they introduced no new error.
* **Label hygiene.**
  * Every new `.md` has the five-field header (HECKE_LEAN_FIDELITY's "Exact sources or dependencies (...)" field included).
  * Nothing under `research/integrated/` or `canonical/` changed.
  * No file claims RH or GRH progress.
  * No "certified" is attached to floating-point output.

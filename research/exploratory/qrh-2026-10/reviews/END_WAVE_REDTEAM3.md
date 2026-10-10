# End-of-wave red team 3 (scope 87678cceb..HEAD)

```text
Status: REVIEW (adversarial, bounded, one reader; same model family as the authors, so not an
  independent review). No mathematical claim. RH is unsolved and nothing here bears on it.
Scope: every file changed in research/exploratory/qrh-2026-10 between 87678cceb and HEAD
  (1e058cf92): SYNTHESIS §0, README headline and new rows, DETECTOR_DENSITY.md, reviews/CUBIC_*.md
  (BOTH_RECTANGLES, PROFILE_UNIFORMITY, ALLOCATION_LOSS, HB_ATTACK), proposed/CUBIC_FOURTH_MOMENT/
  (LEMMAS_4BCD_GH, LF_THETA_THIRD, A4_NO_OLDER_MOVING, STATUS_END_OF_WAVE, README notes),
  reviews/LEAN_BUILD_ATTEMPT.md Addendum C, lean/README.md, lean/comparator/*, AGENDA.md,
  proposed/SEP30_7_8_FORMAL_PACKET/README.md. proposed/PART1_FREE_7_8/ has no change in range.
Exact sources or dependencies: the files above at HEAD 1e058cf92; the 14 logs
  reviews/results/comparator_*.log; results/detector_density_stdout.txt; the stored .out files of
  a4_checks, lf_theta_third_checks, lemmas_4bcd_gh_checks, cubic_hb_checks; arXiv abstract page of
  2610.04045v1 (title, author and date only).
What was actually run: reading; grep; one sympy script (scratchpad) checking f(13/15), f(7/8),
  f(11/12), de Faveri's n = 6 exponent at 7/8, the sign of [dF] − f on each piece of
  (51/100, 1), and the /612 and /432 margins. No script of the wave was rerun. No Lean, lake or
  comparator process.
Smallest remaining gap: issues 1-3 below. Two of them are overclaims about the cubic route's
  verification state, in SYNTHESIS §0; the third is a wrong count in Addendum C.
```

Severity: **blocking** = misstates what was checked, in the favourable direction; **should-fix** =
inconsistent, stale or under-qualified; **nit** = cosmetic.

## Issues

1. **SYNTHESIS.md:186-187, blocking.**
   Text: "Every itemized risk except (H-A) and Lemma 18.1's own correctness has now had a bounded
   attack with no break found."
   Problem: STATUS_END_OF_WAVE.md:108 gives risk 7 (Lemma 4.K, the row functional equation) as
   "**sketched; not reviewed by any note**: still open". Lemma 4.K is not part of (H-A); it is in
   §2b as R14. Risk 13 is also "unchanged".
   Replacement: "Every itemized risk except (H-A), Lemma 18.1's own correctness and Lemma 4.K
   (sketched, not reviewed by any note; risk item 7) has had a bounded single-agent attack with no
   break found."

2. **SYNTHESIS.md:189-190, blocking.**
   Text: "19 inherited items (8 exact-model-only, 11 imported as is)".
   Problem: the table in STATUS_END_OF_WAVE.md:55-73 marks 6 items EXACT MODEL ONLY (H4, H7, H11,
   H14, H15, H17) and 13 items IMPORTED AS IS. The SYNTHESIS figures overstate the checked part.
   Replacement: "19 inherited items (6 exact-model-only, 13 imported as is)".

3. **reviews/LEAN_BUILD_ATTEMPT.md:230, blocking (count); also the commit message of 9ebd63449.**
   Text: "Nine challenges were run through comparator:".
   Problem: the sub-bullets list 3 + 1 + 1 + 2 = 7. The logs show 7 (challenge, solution) pairs
   and 6 distinct challenge modules: SiegelZeros is used twice. Each pair was run once without and
   once with nanoda, so there are 14 runs.
   Replacement: "Seven (challenge, solution) pairs, over six challenge modules, were run through
   comparator, 14 runs in all:".

4. **reviews/LEAN_BUILD_ATTEMPT.md:229-239, should-fix (layout).**
   Problem: the "Summary of Addendum C" block is inserted inside the table. As a result, the rows
   for `HeckeSevenEighthsNanoda.json` (238) and `QuasiRiemannHypothesisNanoda.json` (239) follow
   a bullet list and do not render as table rows.
   Fix: move lines 238-239 to directly after line 227, and put the summary after them. Also,
   line 238 reads "1222s"; it should read "1222 s".

5. **reviews/LEAN_BUILD_ATTEMPT.md:4-7 (Status) and 25-27 (What was actually run), should-fix
   (stale).**
   - Status text: "the zeta, Dirichlet and Hecke challenges are also accepted by the independent
     nanoda kernel".
   - Run field text: "comparator on the DirichletSevenEighths, HeckeSevenEighths,
     SiegelFromSevenEighths and QRHWaveStrip challenges".
   Problem: both fields leave out runs that the table and logs record:
   - SiegelZeros (900 s);
   - QRHWaveDirichletStrip (1130 s);
   - all seven nanoda runs.
   Replacement (Status): "all seven comparator (challenge, solution) pairs are also accepted with
   `enable_nanoda: true` by both the nanoda and the Lean kernel, Addendum C". In the run field,
   append "SiegelZeros and QRHWaveDirichletStrip, and all seven again with `enable_nanoda: true`
   (logs reviews/results/comparator_*_nanoda.log)".

6. **SYNTHESIS.md:62-63, should-fix.**
   Text: "the 7/8 closure's oleans predate every run".
   Problem: the olean check (LEAN_BUILD_ATTEMPT.md:207) was written before 87678cceb (18:36 UTC).
   The nanoda runs ran from 18:49 to 21:49 UTC, and an explicit-Siegel nanoda run is in progress
   at HEAD. The check does not cover those runs.
   Replacement: "the 7/8 closure's oleans predate every Lean-only run (check made before the
   nanoda runs; not repeated for them)". Alternatively, repeat the mtime check and record its
   time.

7. **README.md:109 and AGENDA.md:196, should-fix (inconsistent with Addendum C).**
   - README text: "the zeta, Dirichlet and Hecke challenges are also accepted by the independent
     **nanoda** kernel".
   - AGENDA text: "Done here for the zeta, Dirichlet and Hecke challenges".
   Problem: the logs show nanoda acceptance for all seven pairs.
   Replacement: "all seven comparator pairs (three upstream 7/8, two Siegel, two strips) are also
   accepted by the independent nanoda kernel (Addendum C)".

8. **README.md:26 (headline "Formal" bullet), should-fix.**
   Text: "the Oct 1 Siegel-zero statement with explicit `c = (log 3)/8`".
   Problem: the bullet sits under "accepted by comparator". What comparator accepted is the
   upstream `∃ c > 0` statement. The explicit constant comes from the helper `gap_of_real_zero`,
   which lean/README.md:91-92 says "is not itself a comparator target". Its Mathlib-only
   challenge (lean/comparator/QRHWaveSiegelExplicit.lean, commit 1e058cf92) has no log yet.
   Replacement: "the Oct 1 Siegel-zero challenge (`∃ c > 0`), comparator-accepted; the explicit
   `c = (log 3)/8` is read off the kernel-checked helper `gap_of_real_zero` (its own comparator
   run is in progress)". Keep README.md:116 consistent with this: "comparator accepted all three
   corollaries" covers the `∃ c` form only.

9. **SYNTHESIS.md:34, should-fix.**
   Text: "**The 7/8 half-plane is machine-checked.**"
   Problem: what was checked is a Lean statement under trust assumptions. SYNTHESIS.md:23-24
   and :68 say so; the headline drops it.
   Replacement: "**The Lean statement of the 7/8 half-plane is kernel-checked (two kernels, under
   the listed trust assumptions).**"

10. **SYNTHESIS.md:40-41, should-fix.**
    Text: "**Neither the formal proof nor, on paper, the 7/8 argument needs Part I or the 11/12
    theorem**".
    Problem: the paper-level half is a PROPOSED new composition, but it is asserted in bold as
    fact.
    Replacement: "**The formal proof does not use Part I or the 11/12 theorem; a PROPOSED
    paper-level route (two same-family reviews) also avoids them.**"

11. **SYNTHESIS.md:119-121, should-fix (qualifier silently dropped).**
    Problem: the pre-87678cceb text said "The paper-level status stays Rp, because it inherits
    Lemmas 17.1-17.2". The restructure deleted it, so "a full proof" now reads as unconditional.
    Replacement: append "The paper-level status stays Rp, because it inherits Lemmas 17.1-17.2."

12. **SYNTHESIS.md:176-177 and 180-182, should-fix (proved without label).**
    - Text 1: "Lemmas 4.B, 4.C, 4.D and 4.H are now proved in full".
    - Text 2: "A4 ... is proved at n = 3".
    Problem: the source files label these "proved here (PROPOSED)", from one agent and unreviewed.
    STATUS_END_OF_WAVE.md:90 and :105-106 give A4 as "proved given H12", where H12 is IMPORTED AS
    IS.
    Replacement 1: "now have written PROPOSED proofs (one agent, unreviewed), with precision
    fixes".
    Replacement 2: "A4 has a PROPOSED proof at n = 3, given the imported construction facts H12".
    The same applies to "closed" at :167 and :170: add "(bounded single-agent review)".

13. **STATUS_END_OF_WAVE.md:78-96, README.md:145 and SYNTHESIS.md:190, should-fix.**
    Text: "15 items re-derived at n = 3".
    Problem: table 2b counts three entries as re-derived that are not:
    - R7 (Lemma 4.I) is "sketched only";
    - R14 (Lemma 4.K) is "sketched; **not reviewed**";
    - R15 is "(H-B), a separate hypothesis", so it is a replacement, not a re-derivation.
    Replacement: "12 items re-derived at n = 3 (PROPOSED), 2 only sketched (Lemmas 4.I, 4.K), and
    1 replaced by hypothesis (H-B)".

14. **SYNTHESIS.md:186, STATUS_END_OF_WAVE.md:30 and cubic README notes, should-fix.**
    Text: "conditional on (H-A) and (H-B)".
    Problem: the route also rests on the sketched, unreviewed Lemma 4.K (risk 7) and on the
    correctness of the sextic Lemma 18.1 case 1 (risk 12).
    Replacement: "conditional on (H-A), (H-B), Lemma 4.K (sketched) and the correctness of the
    manuscript's Lemma 18.1 case 1".

15. **SYNTHESIS.md:184-185, README.md:144 and cubic README.md:229, nit.**
    Text: "requires choosing `ξ ≤ μ*ρ/2`".
    Problem: CUBIC_HB_ATTACK.md:277 decides "given `ξ ≤ μ*(δ)ρ/2` **and** `2ξ ≤ δ`".
    Replacement: "requires `ξ ≤ μ*(δ)ρ/2` and `2ξ ≤ δ`".

16. **SYNTHESIS.md:146-147 and README.md:115, should-fix (conditional comparison stated as fact).**
    - SYNTHESIS text: "In the sextic case this beats de Faveri's 2026 large-sieve density".
    - README text: "beating de Faveri's 2026 sextic large-sieve density (0.466)".
    Problem: DETECTOR_DENSITY.md:255-267 gives the caveats:
    - the inputs are unreviewed general lemma forms;
    - the family identification with [dF]'s `χ_a` is "PROPOSED and unchecked";
    - members are counted, not zeros;
    - the range is `T ≤ U^{1/100}` with an unspecified `T`-power.

    Replacement: "would lie below de Faveri's n = 6 bound (55/118 ≈ 0.466 at 7/8; arXiv:2610.04045v1,
    Cor 1.5) in the `U`-aspect, if the general forms of the manuscript's Lemmas 17.6/18.1 hold and
    the family identification (unchecked) is right".

17. **SYNTHESIS.md:77-78, nit.**
    Text: "Both comparator acceptances below".
    Problem: three items follow.
    Replacement: "All three comparator acceptances below".

18. **lean/README.md:23-26 and 115-118, nit (stale).**
    - The run field gives only the Lean-only times. Add the nanoda times: 1249 s, 1225 s, 1239 s.
    - "How to check" step 3 names only `QRHWaveStrip.lean` and "the two JSON files". It should
      list `QRHWaveStrip.lean`, `QRHWaveDirichletStrip.lean`, `QRHWaveSiegelExplicit.lean` and
      the JSON files in `comparator/`.

19. **proposed/SEP30_7_8_FORMAL_PACKET/README.md:333, nit.**
    Text: "kernel soundness (for the zeta statement this is now covered by two independent
    kernels".
    Problem: two kernels lower the single-kernel risk; they do not cover soundness. The coverage
    is also wider than zeta.
    Replacement: "kernel soundness (single-kernel risk now reduced: nanoda and Lean both accept
    every comparator pair; see T9)".

20. **results/detector_density_output.json:269 (scripts/detector_density.py:331), nit.**
    Problem: the key `certified_margin` holds the manuscript's stated margin 49/440640, stored as
    a float. Nothing here certifies it.
    Fix: rename the key to `paper_stated_margin`.

21. **lean/comparator/QRHWaveSiegelExplicit.lean:8, nit.**
    Text: "an explicit, existential-free Landau–Siegel-type bound".
    Fix: add "(a consequence of the imported 7/8 half-plane; not an unconditional effective
    Siegel bound)", matching lean/README.md:93.

## Checked and fine

- **Comparator logs.** Every acceptance claimed in Addendum C has a log with the stated
  wording:
  - each of the 7 nanoda logs contains both "nanoda kernel accepts the solution" and "Lean
    default kernel accepts the solution";
  - each of the 7 Lean-only logs contains the Lean line.

  All 14 quoted times match the logs (1108, 1096, 1082, 1104, 900, 1130, 1223, 999, 1249, 1225,
  1239, 1222, 1238 s, and 1094 s for the Addendum B zeta run). The runs are sequential with no
  overlap. Every `*Nanoda.json` has `enable_nanoda: true`, and its theorem names match its log.
- **nanoda is a separate type checker,** so "independent kernel" is used correctly. No
  same-family review is called independent: SYNTHESIS.md:121 and STATUS_END_OF_WAVE.md:47 say
  the opposite explicitly.
- **DETECTOR_DENSITY, exact arithmetic.**
  - `f(13/15) = 49/159` and `f(7/8) = 2/7`;
  - the pieces join at `σ = 11/12` (both give 1/6);
  - `R(δ) = 1 − 2αδ/(3α−δ)` gives `f` under `δ = 2σ − 1`, and the min-max over `(r, m, t)`
    re-derives with `t* = 10/7`;
  - inverse-only `23/80`, gap `1/560`, `A_eff = 8/7`;
  - de Faveri n = 6 at 7/8 is exactly `55/118 ≈ 0.4661`.
- **DETECTOR_DENSITY, comparison with [dF].** `[dF] − f` has no zero on any piece of
  (51/100, 1) except at σ = 1, so the claim at :68 holds on the whole interval, not only on the
  script's 399-point grid. (Nit: say so.)
- **DETECTOR_DENSITY, citation.** The arXiv:2610.04045v1 title, author and date match. Inside
  DETECTOR_DENSITY the citation is kept to its stated scope (`K ⊇ μ_n`, n = 6, caveats 1-5).
- **Margins.**
  - `μ* = (11−147δ)/612` and `c* = (11−147δ)/432` are used consistently (margin and (C)-only
    tolerance) across SKETCH, the cubic README, STATUS, CA, AL, BR and HB;
  - the δ = 1/100 values 953/61200 and 953/43200 check;
  - `144/11` checks.
- **The `f = 2v_1 → f = v_1` hazard** is stated the same way in LF_THETA_THIRD, LEMMAS_4BCD_GH,
  the cubic README, STATUS and SYNTHESIS.
- **Stored check outputs** match the claimed counts: 5/5 (4 controls), 14/14 (7), 18/18 (12),
  27/27, and DETECTOR 21/21 (5).
- **Labels.** Every new .md file has the five header fields. Nothing in range is under
  research/integrated/. No RH or GRH implication was found.

# End-of-wave red team: Lean check, map v2.1, status notes, sextic and cubic packets

```text
Status: REVIEW (adversarial, bounded, one pass). Wording, provenance, Lean statement fidelity and
  bookkeeping only. No file was edited, and nothing here is a verdict on any mathematics.
Scope: material added to research/exploratory/qrh-2026-10 between 6bb5fe1fd and HEAD
  e5731afb597b09b9202a29e3e797c077ec935989 (this wave's working branch):
  reviews/LEAN_BUILD_ATTEMPT.md (header, Addenda A-B); lean/ (README, three .lean files, checks/,
  comparator/); reviews/results/lean_*.log and comparator_*.log; SEP30_VERIFICATION_MAP_V2.md §10;
  status notes in INTAKE, CONDITIONAL_CONSEQUENCES, ROBIN_GRADED and OCT5_11_12_PACKET; SYNTHESIS §0;
  README (intro and table); HEIGHT_LEVELS §6; proposed/SEXTIC_FOURTH_MOMENT/*;
  proposed/CUBIC_FOURTH_MOMENT/README.md (end note); and the headers of SEP30_L42_44_REVIEW.md and
  CUBIC_CENTRED_ATTACK.md checked against their bodies.
Exact sources or dependencies: the files above at e5731afb5. The upstream challenge files are at
  ref 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, path
  standalone/2026-10-07-openai-quasi-riemann-import/upstream/lean/ComparatorChallenges/. Mathlib
  d13f23b7 sources were read in the build scratch copy, and the scratch logs of the Lean build
  were read but not run.
What was actually run: reading; grep; sha256sum of the challenge files and scripts; cmp of
  lean/*.lean against the built scratch copies; one Python script (stdlib only) that recomputes
  the map §3 counts and owned lines, with and without the §10 changes. No Lean, Lake or comparator
  process was started.
Smallest remaining gap: the comparator acceptance is cited, in places, for objects that
  comparator has not checked: the Dirichlet 7/8 theorem (that run was still in progress at
  17:31 UTC), the Hecke theorem and the three wave corollaries. Items 1-2 must be fixed first.
```

RH is unsolved. Nothing below bears on RH or GRH. Severity: **blocking** means the text
misstates what was checked; **should-fix** means the text is misleading, stale or incomplete;
**nit** means the problem is cosmetic.

## Issues

**1. Blocking.** `proposed/OCT5_11_12_PACKET/README.md:356-357` (and :318-319)
* Text: "Its 7/8 targets have since been built and accepted by comparator"; at :318, "Its 7/8
  targets were built and checked later the same day".
* Problem: comparator accepted only `QuasiRiemannHypothesis.json` (zeta).
  * The Dirichlet run (`DirichletSevenEighths.json`) was still exporting at the time of this review.
  * The Hecke challenge was never run.
* Replace with: "Its 7/8 targets have since been built, and `#print axioms` is standard for the
  zeta, Dirichlet and Hecke theorems. Comparator has accepted the zeta challenge only
  (../../reviews/LEAN_BUILD_ATTEMPT.md, Addendum B). None of this formalizes the 11/12 argument."

**2. Blocking.** `lean/README.md:5-6, 17-18, 19-20`
* Text, in three header fields:
  * Status: "Comparator results are in ../reviews/LEAN_BUILD_ATTEMPT.md, Addendum B."
  * What was actually run: "...; comparator (Addendum B)".
  * Smallest remaining gap: "(a kernel check under comparator's assumptions, not a human review)".
* Problem: comparator was run on none of the three files. `comparator/QRHWaveStrip.json` and
  `comparator/SiegelFromSevenEighths.json` have no log. `DirichletZeroStrip` and
  `SiegelFromSevenEighths` rest on the Dirichlet 7/8 theorem, which has `#print axioms` only.
* Replace with:
  * What was actually run: "lake build of the three modules; checks/CorollaryAxioms.lean
    (results/lean_corollary_axioms.log). Comparator has NOT been run on QRHWaveStrip.json or
    SiegelFromSevenEighths.json."
  * Smallest remaining gap: "ZetaZeroStrip rests on the zeta 7/8 theorem, which comparator
    accepted under the assumptions of Addendum B. DirichletZeroStrip and SiegelFromSevenEighths
    rest on the Dirichlet 7/8 theorem, which has `#print axioms` only. No part of the Lean
    development has had a human review."

**3. Should-fix.** `reviews/LEAN_BUILD_ATTEMPT.md:23` and `reviews/SEP30_LEAN_CORRESPONDENCE.md:43-44`
* Text: "the kernel check certifies the Lean statement against Lean + Mathlib + ..."; and "The
  formal check therefore certifies the 7/8 statement".
* Problem: this is a machine check under stated trust assumptions. "Certifies" overstates it.
* Replace "certifies" with "checks", in both places.

**4. Should-fix.** `reviews/LEAN_BUILD_ATTEMPT.md:11` and :128-130
* Text: "Hecke and SiegelZeros challenges were not attempted."; and "Comparator runs on the
  Dirichlet, Hecke and corollary challenges are recorded below as they complete."
* Problem:
  * The Hecke module was built and its axioms were printed (`results/lean_hecke_axioms.log`,
    `lean/checks/HeckeAxioms.lean`), but no addendum records that build. Even so, INTAKE.md:120-121,
    README.md:91 and SYNTHESIS.md:48-49 cite "Addenda A–B" for the Hecke result.
  * "Below" points into Sections 1-8, which are the frozen record of the original attempt.
* Replace with:
  * Scope: "Hecke: module built and `#print axioms` standard (Addendum C); no comparator run.
    The upstream SiegelZeros solution was not built. The wave's own Siegel corollary is in ../lean/."
  * At :129: "...will be recorded in a new Addendum C."
  * Then add an Addendum C with the Hecke build command, its log and the axiom output.

**5. Should-fix.** `SYNTHESIS.md:48-50`
* Text: "`#print axioms` on ..., on the Dirichlet version and on the Hecke-family version gives
  only [...]. The statements are about Mathlib's own `riemannZeta` and `DirichletCharacter.LFunction`."
* Problem: the Hecke statement is about `OAI.SevenEighths.HeckeFamily.{Character, LFunction}`.
  These are project definitions written into `ComparatorChallenges/HeckeSevenEighths.lean`
  (about 10 KB) itself. Nobody has checked that they match the paper's Hecke `L`-functions.
* Append: "The zeta and Dirichlet statements are about Mathlib's objects. The Hecke statement
  uses project-defined characters and L-functions whose fidelity to the paper is unchecked."

**6. Should-fix.** `reviews/LEAN_BUILD_ATTEMPT.md:101-114` (and :65-66)
* Text: "The patched third-party packages cannot change the meaning of the statement, because the
  statement mentions only Mathlib constants and Mathlib is unpatched."; and :66 "built on this
  machine from the pinned sources".
* Problem: the argument is sound for the zeta theorem, because comparator compared it against a
  Mathlib-only export. The trust list still omits three things:
  * (a) Mathlib was not rebuilt. Its `.olean` files came from cache.mathlib.org. "Git tree clean"
    checks the sources, not the oleans, and the exported definition of `riemannZeta` is whatever
    the cached olean contains.
  * (b) The mtime guard window (12:48-12:51) overlaps the unsandboxed lakefile `run_cmd`
    clone-and-patch step of `lake exe cache get` (12:43-12:51). The guard therefore does not
    cover configuration-time code.
  * (c) The argument does not extend to the Dirichlet theorem. `Statement.lean` elaborated its
    type in the environment that loads the patched packages, so an instance or notation change
    there would act on both sides alike.
* Add three trust bullets: "Mathlib oleans from the cache, not rebuilt from source"; "the mtime
  guard does not cover lakefile code run during cache get"; "the statement-meaning argument
  applies to the comparator-checked zeta theorem only". At :66, change the text to "built on this
  machine from the pinned sources (Mathlib from its binary cache)".

**7. Should-fix.** `CONDITIONAL_CONSEQUENCES.md:17-19` and `ROBIN_GRADED.md:25-27`
* Text: "The statements below that use only `H(7/8)` for ζ or for Dirichlet `L`-functions are
  therefore conditional on accepting that machine check".
* Problem: "That machine check" is the comparator acceptance, which covers ζ only. ROBIN_GRADED
  has no Dirichlet statements; the bullets are copied from CONDITIONAL_CONSEQUENCES.
* Replace with: "Statements that use only `H(7/8)` for ζ are conditional on accepting the
  comparator check. Those for Dirichlet `L`-functions are conditional on the `#print axioms`
  check only, since the comparator run is pending." In ROBIN_GRADED, keep the ζ sentence only.

**8. Should-fix.** `HEIGHT_LEVELS.md:132-138, 145`
* Text: "One statement now holds uniformly at all heights and is machine-checked. ... built on the
  imported 7/8 theorem, which comparator accepts"; and "the same holds for primitive Dirichlet
  `L`-functions".
* Problem:
  * "Holds" is unqualified.
  * "Which comparator accepts" reads as if it applied to the strip, which comparator has not checked.
  * The Dirichlet strip also needs `χ ≠ 1`, uses "nontrivial" in the `gammaFactor` sense, and
    rests on a theorem that comparator has not checked.
* Replace with: "One statement is now machine-checked uniformly in height, under the trust
  assumptions of LEAN_BUILD_ATTEMPT Addendum B. It is a Lean theorem about Mathlib's
  `riemannZeta`, derived from the imported 7/8 theorem; that theorem, not the strip, was accepted
  by comparator." The Dirichlet bullet becomes: "the same strip for primitive `χ ≠ 1`, off the
  poles of the Gamma factor (Lean; rests on the Dirichlet 7/8 theorem, `#print axioms` only)".

**9. Should-fix.** `SYNTHESIS.md:68-69`
* Text: "the Oct 1 Siegel-zero challenge statement holds with `c = (log 3)/8`, as a corollary of 7/8."
* Replace with: "the Oct 1 Siegel-zero challenge statement is derived in Lean, with
  `c = (log 3)/8`, from the imported 7/8 Dirichlet theorem (axioms standard; comparator not run
  on SiegelFromSevenEighths.json)."

**10. Should-fix.** `lean/DirichletZeroStrip.lean:6-8, 39-40` and `lean/README.md:41-46`
* Text: "'Nontrivial' means that the Archimedean factor `gammaFactor χ s` ... does not vanish";
  "a zero of the Archimedean factor, i.e. a trivial zero".
* Problem: the real Archimedean factor never vanishes. `gammaFactor χ s = 0` holds exactly at its
  poles, because Mathlib assigns `Gamma (-n)` the junk value 0 (`Gamma_neg_nat_eq_zero`,
  Gamma/Basic.lean:343-344). The Lean hypothesis is right. The English is misleading.
* Add: "In Lean, `gammaFactor χ s = 0` because Mathlib's `Gamma` is 0 at its poles. So the
  hypothesis says that `s` is not a pole of the Gamma factor, which for primitive `χ ≠ 1` is
  exactly the set of trivial zeros."

**11. Should-fix.** `lean/README.md:4-5`
* Text: "All three files compile ... with no errors or warnings".
* Problem: no build log of `OAI.QRHWave.*` is committed or present in the scratch logs. The only
  evidence that they compile is `results/lean_corollary_axioms.log`. Lake's output also always
  contains the 23 "has local changes" warnings.
* Fix: commit the build log. Otherwise write "compile (results/lean_corollary_axioms.log needs the
  built modules); the build log is not committed".

**12. Should-fix.** `reviews/SEP30_VERIFICATION_MAP_V2.md:47-53` (header), :62-64 (§0) and :369 (§6 item 7)
* Text: "four have arithmetic or numerical checks only (A): Lemma 17.1 ... and ... Lemmas 4.2, 4.3
  and 4.4"; and "LEAN_BUILD_ATTEMPT built 350 of 2,924 modules ... The comparator was not run,
  and `#print axioms` was not obtained."
* Problem: §10 states only that the *tables* record v2. The header's gap and §6.7 are claims about
  the present, and §10 has superseded them.
* Fix: add to the header's Status line "Addendum v2.1 (§10) supersedes the counts and the gap stated
  here". Add to §6.7: "(Superseded: the closure now builds; `#print axioms` is standard; comparator
  accepts the zeta challenge; see §10.)"

**13. Should-fix.** `README.md:101` and :50-51
* Text: "Of 65 load-bearing nodes: R 43, partial 5, I 5, A 7, U 5 ... Remaining A: Lemma 17.1,
  then 4.2–4.4"; and "Lemma 18.1 ... shows no error, but its common-support step is unverified".
* Problem: both contradict SYNTHESIS.md:38-46 (49 / 6 / 2) and the map, where Lemma 18.1 is R
  with every proof line read.
* Replace with:
  * Row: "v2 + addendum v2.1 (§10): as written R 49, partial 6, I 2, A 3, U 5. With the Oct 5
    substitution, R 49, partial 6, I 2 of 57 and 0 A/U; by lines 67% R and 99% R+partial.
    Bounded agent reviews only."
  * Headline 9: "Lemma 18.1 ...: every proof line read by three bounded reviews, no wrong step found."

**14. Should-fix.** `README.md` (the file table)
* Problem: there are no rows for `reviews/SEP30_L42_44_REVIEW.md`, `reviews/CUBIC_CENTRED_ATTACK.md`
  or `proposed/SEXTIC_FOURTH_MOMENT/`. The cubic row (:114) omits the attack result.
* Add rows:
  * "Lemmas 4.2-4.4: no wrong step found (bounded, one agent); 65/65 exact checks; imports cubic
    reciprocity".
  * "Centred-stage attack on the cubic route: survives at the level of the displayed steps;
    18/19 checks (one scale-limited FAIL); open: identical action on both rectangles".
  * "PROPOSED packet draft: Lemma 18.1 case 1 as a standalone sextic fourth moment".

**15. Should-fix.** `proposed/SEXTIC_FOURTH_MOMENT/README.md:283, 291, 366, 487` and :372
* Text: "4.2 is also status A"; "manuscript proofs unreviewed" (E3); "No review read the proofs of
  Lemmas 4.2, 4.3 or 4.4"; "First review of Lemmas 4.3 and 4.4 ..., which no bounded review has
  read"; and "No Lean formalisation of Lemma 18.1 exists in this repository."
* Problem:
  * Only the end note (:515-526) corrects the first four. An integrator reading §4.3, §6 or §10
    gets the stale status.
  * :372 contradicts SEP30_LEAN_CORRESPONDENCE.md:136 and :205. The imported Lean development (ref
    pr908) has an interface instance of Lemma 18.1 (code Fv). Its case 1 appears as
    `U^{max(1,2m)+ε}`; the normalization is unverified.
* Fix:
  * Append "[superseded: see Note after §10]" to each of the four lines.
  * Replace :372 with: "The imported Lean development contains a normalized, specialized instance
    of Lemma 18.1 (SEP30_LEAN_CORRESPONDENCE row 10, Fv). The general statement is not formalized,
    and no human reviewed any part."

**16. Should-fix.** `reviews/SEP30_VERIFICATION_MAP_V2.md:419`
* Text: "initialization transform replayed exactly at tiny scale".
* Problem: the end-to-end replay (MISC A4) is in double precision, with relative error ≤ 3.3e-15,
  and SEP30_MISC_REVIEW.md:34 and :192 label it EMPIRICAL. Only the symbols and the exponent
  identities are exact.
* Replace with: "initialization transform replayed at tiny scale (exact symbols; double-precision
  agreement ≤ 3.3e-15, EMPIRICAL)".

**17. Nit.** `lean/SiegelFromSevenEighths.lean:7`
* Text: "Primitivity and reality of `χ` are not used."
* Problem: non-principality is not used either (lean/README.md:67 says so).
* Replace with: "Primitivity, reality and non-principality of `χ` are not used."

**18. Nit.** `lean/SiegelFromSevenEighths.lean:15-17` and `lean/README.md:53-73`
* Problem: the file declares `OAI.SiegelZeros.WeightedTorusJets.*`. These are the same fully
  qualified names as the upstream `OAI/NumberTheory/SiegelZeros/Conclusions/Theorem.lean`. The
  challenge forces these names, but the two modules cannot be imported together, and
  "WeightedTorusJets" names a method that this proof does not use.
* Add one sentence saying this.

**19. Nit.** `reviews/SEP30_VERIFICATION_MAP_V2.md:418` and `proposed/SEXTIC_FOURTH_MOMENT/README.md:521`
* Text: "the inert prime 2".
* Problem: the review applies cubic reciprocity to `-2`, the primary associate
  (SEP30_L42_44_REVIEW.md, finding F4).
* Replace with: "the inert prime `-2`".

**20. Nit.** `SYNTHESIS.md:46` and :23
* Text: "(49 R, 6 partial, 2 inspected, 0 unreviewed)"; and "All are unreviewed."
* Replace with: "(of the 57 remaining nodes: 49 R, 6 partial, 2 inspected, 0 A/U)"; and "All are
  unreviewed by humans; the Lean statement of the Sep 30 zeta claim is machine-checked (§0)",
  as in README.md:14.

**21. Nit.** `reviews/LEAN_BUILD_ATTEMPT.md:38, 52`
* Problem: these lines cite scratch paths (`scripts/Axioms.lean`, `scripts/Statement.lean`). The
  committed copies are `lean/checks/Axioms.lean` and `lean/checks/Statement.lean`, with outputs in
  `results/lean_axioms.log` and `results/lean_statement.log`. Also, `results/lean_build_resume4_tail.log`
  is named "resume4", while the text speaks of three resumptions.
* Add the repo paths, and say which run "resume4" is.

**22. Nit.** `proposed/CUBIC_FOURTH_MOMENT/README.md:96-97`
* Text: "The one failure is a tiny-scale effect".
* Problem: CUBIC_CENTRED_ATTACK §3.3 says that numerics at this scale cannot exhibit the
  requirement. The check is uninformative, not explained away.
* Replace with: "The one failure, [L2b], is attributed (CUBIC_CENTRED_ATTACK §3.3) to `Z^ε` and
  divisor factors dominating at `Z ≤ 10⁸`. At this scale the check is uninformative; it is not
  a pass."

**23. Nit.** `AGENDA.md:123-125`
* Problem: item C1 does not record progress, unlike C2.
* Add: "*Done in part:* closure built; `#print axioms` standard (zeta, Dirichlet, Hecke);
  comparator accepts the zeta challenge; the other comparator runs are pending."

**24. Nit.** `reports/REPO_RECENT_WORK.md:37`
* Text: "The 7/8 closure (2,925 files) was **not built**."
* Problem: this is a historical entry for the lc2b3j branch, but it is now stale. Elsewhere the
  closure has 2,924 modules.
* Add: "(since built in this wave: reviews/LEAN_BUILD_ATTEMPT.md)".

**25. Nit.** `HEIGHT_LEVELS.md:146`
* Text: "`β < 1 − c/(log γ)^{2/3}(log log γ)^{1/3}`".
* Replace with: "`β < 1 − c/((log γ)^{2/3}(log log γ)^{1/3})`".

**26. Nit.** `proposed/SEXTIC_FOURTH_MOMENT/README.md:525-526`
* Text: "is being prepared as `reviews/LEMMA18_THETA_ROW_REVIEW.md`".
* Problem: that file does not exist. `reviews/theta_row_ledger.py` and
  `results/theta_row_ledger.json` are committed with no accompanying note.
* Replace with: "is planned (support script reviews/theta_row_ledger.py; no review written yet)".

## No issue found

* **Zeta strip statement.** `QRHWave.quasi_critical_strip` has binders identical to Mathlib's
  `RiemannHypothesis` (RiemannZeta.lean:185-186).
  * `riemannZeta` is Mathlib's root definition (results/lean_statement.log; there is no
    `Complex.riemannZeta`).
  * The README's account of the proof is correct, including the use of `ζ(0) = −1/2` to exclude
    `k = 0`.
* **Dirichlet strip.**
  * `gammaFactor_eq_zero_iff` matches Mathlib's definition (DirichletContinuation.lean:207-208;
    `Gammaℝ_eq_zero_iff`).
  * The trivial-zero lists are right: `0, −2, …` for even `χ`; `−1, −3, …` for odd `χ`.
  * Listing `s = 0` for even primitive `χ ≠ 1` agrees with `L(0, χ) = 0`.
  * The lower edge uses the functional equation for `χ⁻¹` and `conductor_inv`, and needs no
    root-number nonvanishing.
* **Siegel corollary.** Both statements are textually identical to the upstream challenge
  (SiegelZeros.lean, sha256 `bedaac02…`). Upstream `docs/003.md` maps the Oct 1 paper to that
  file, so "the Oct 1 challenge statement" is accurate.
* **Challenge hashes.** The following reproduce at 31c706bb: QuasiRiemannHypothesis.json
  `46ebb7ed…f320`, .lean `065f8c9a…12cc5`, DirichletSevenEighths.lean `8fb13ad9…`, tree
  `ef5d0c6c…`. The repo's `lean/*.lean` and `comparator/QRHWaveStrip.lean` are byte-identical to
  the scratch copies that were built.
* **Comparator log and stated trust.**
  * The log shows 1094 s (17:00:59 to 17:19:13), "Lean default kernel accepts" and
    `enable_nanoda: false`.
  * The following are all stated: precompiled solution (assumption 2 not met), best-effort
    landrun with no AF_UNIX wrapper, a single kernel, and 23 patched packages (11 + 12, matching
    the 23 "local changes" warnings).
* **Map v2.1 recount.** Recomputed from the §3 table with the seven §10 changes:
  * as written: R 49, Rp 6, I 2, A 3, U 5 (65 nodes);
  * with the substitution: R 49, Rp 6, I 2, A 0, U 0, plus L 8;
  * owned lines: R 7,469 (67.1%), Rp 3,526 (31.7%), I 139 (Def 5.6 63 + Prop 11.3 76), total 11,134.
  
  All match the file. The v2 base figures (6,930 / 2,770 / 399 / 1,035) also reproduce.
* **Verdicts cited in §10.** They match SEP30_L42_44_REVIEW (422 primes; 5,454 odd `c`;
  65/65) and the verdict table of SEP30_MISC_REVIEW.
* **Correspondence counts.** F 6 + Fv 8 + C 37 + B 8 + N 6 = 65, consistent with SYNTHESIS's
  14 / 8 / 43.
* **Script hashes.** These match their headers: sep30_l42_44_checks.py `edafdb80…`, a2/eis.py
  `87ca11d9…`, cubic_centred_attack.py `2cbc8718…` (equal at f6044af1d). The commits c8515d4ea
  and f6044af1d exist.
* **Review headers against their bodies.**
  * SEP30_L42_44_REVIEW: 65/65 with controls; cubic reciprocity imported; one agent.
  * CUBIC_CENTRED_ATTACK: 18/19, with the [L2b] FAIL disclosed; nothing floating is called certified.
* **Label hygiene.**
  * Every new .md file has the five-field header.
  * Nothing was added outside the folder, and nothing under `research/integrated/`.
  * The proposed claim ID `IMPORTED.QRH.SEP30.SEXTIC_FOURTH_MOMENT_CASE1` does not occur in
    `canonical/` or `research/integrated/`.
  * The added lines contain no AI model names and no claim about RH or GRH. Each new Lean file
    says "not RH" or "not GRH".
* **HEIGHT_LEVELS table.**
  * The Platt–Trudgian range is labelled as imported.
  * At every height above `3·10¹²`, the Vinogradov–Korobov region with its explicit constants
    is indeed weaker than 7/8.

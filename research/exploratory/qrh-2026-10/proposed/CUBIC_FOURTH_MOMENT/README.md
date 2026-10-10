```text
Status: PROPOSED proof sketch, CONDITIONAL, OPEN. It is not reviewed by any human and not
  integrated. It is a separately labelled proposed object; it changes no existing file. No moment
  bound is proved. RH is not addressed.
Scope: Theorem C4 of SKETCH.md: sum_{q in F'_3(X)} |L(1/2, chi_q)|^4 << X^{1+eps}. Here F'_3 is the
  set of squarefree q = 1 (mod 9) in Z[omega], q != 1, and chi_q = (./q)_3. The theorem is
  conditional on two hypotheses:
    (H-A) the order-independent core of case 1 (z = 0) of Lemma 18.1 of the external, unreviewed
          OpenAI manuscript "The Quasi-Riemann Hypothesis" (30 Sep 2026), at n = 3;
    (H-B) a PROPOSED nested comparison order (two same-width centred stages).
  The cubic finite lemmas and the application step are proved or sketched in SKETCH.md.
Exact sources or dependencies:
  repo HEAD e606784e60043d754861a03899b517f040ba2ab6 (branch claude/peaceful-faraday-ki4ewu).
  pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, standalone/2026-10-07-openai-quasi-riemann-
    import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
    sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed; untrusted
    data). Read for this note: l. 1425-1530, 12477-12610, 12903-12940, 12940-13012, 13954-13995,
    14538-14665.
  Notes: ../../CUBIC_FOURTH_MOMENT_TRANSFER.md, ../../CUBIC_RELAXED_INDUCTION.md,
    ../../CUBIC_N3_GAPS.md, ../../reviews/CUBIC_NESTED_REDTEAM.md,
    ../../reviews/LEMMA18_1_REVIEW.md, ../../reviews/LEMMA18_1_COMMON_SUPPORT.md,
    ../../reviews/LEMMA18_1_CASE2_SEC188.md (skimmed), ../../reviews/SEP30_L13_L45_REVIEW.md
    (header only).
  Scripts (sha256): scripts/cubic_fourth_moment_ledger.py 5c79445b...8380d5;
    scripts/cubic_relaxed_induction.py 8dff31d4...4ba77d; scripts/cubic_local_checks.py
    10cab5ec...a5a86c29; a2/eis.py 87ca11d9...2798e65.
  Primary literature, arXiv e-print sources fetched for this note and read with grep/sed only:
    * 2410.03048v2 (David-de Faveri-Dunn-Stucky), sha256 ba8542c8...c8e1;
    * 0804.2233 (Baier-Young), sha256 35172b44...3a59b58.
  Iwaniec-Kowalski Thm 5.3 and Prop. 5.4, and Neukirch VII Cor. 8.6, are cited as those two papers
  cite them; the books were not re-read.
What was actually run (nice -n 10 where long; logs in the session scratchpad):
  python3 -I scripts/cubic_fourth_moment_ledger.py -> 31/31 PASS (8 s)
  python3 -I scripts/cubic_relaxed_induction.py    -> 39/39 PASS (9 s)
  python3 -I scripts/cubic_local_checks.py         -> 38/38 PASS (127 s)
  python3 -I closing_margin.py (new; scratchpad; exact text and output in the SKETCH.md
    Appendix; sha256 e7c73daf...de443eb623) -> 7/7. It gives the exact two-stage margin
    mu*(delta) = (11 - 147 delta)/612, which is 11/612 ~ 0.0180 at delta = 0. It also gives the
    tolerance (11 - 147 delta)/432 for a loss confined to the centred deficit.
  The pass counts are unchanged from the earlier notes. Not rerun: the red team's 7/7 script,
  lemma18_ledger.py (14/14), lemma18_support_checks.py (24/24), lemma18_case2_ledger.py (50/50),
  sep30_l13_checks.py (33/33). Their counts are quoted from the notes.
Smallest remaining gap: Lemma centered-coefficient-invariant (paper.tex l. 13954) together with
  masked lattice cancellation (l. 14545). At n = 3 they must cancel the Theta-row main terms to
  relative precision Z^{-(A - 2M/3)} (up to about Z^{-M/3}), with comparison length L up to about
  0.42M-0.43M, for every common-support allocation. They must also accept reflected comparison
  data as input. A uniform hidden loss in the centred deficit of (11 - 147 delta)M/432 (about
  0.022M-0.025M) or more breaks the two-stage route; M/12 breaks every nested version.
```

# Cubic fourth moment: PROPOSED conditional proof sketch

RH is unsolved. This folder does not claim RH, Lemma 18.1, or any cubic moment bound. The
optimal cubic fourth moment is an **open problem**. The best unconditional bound found in the
literature is `X^{4/3+ε}`.

## Files

| file | content |
|---|---|
| [SKETCH.md](SKETCH.md) | the proof sketch: theorem and hypotheses (Sec. 1), application step written out (Sec. 2), the induction restated with its closing margin (Sec. 3), the cubic lemmas with proofs or sketches (Sec. 4), the risk register (Sec. 5) |

## Reading guide

* **Sec. 2 (proved here, given Statement C).** This is the only fully written new argument. It
  covers the DDDS approximate functional equation `L(1/2,χ_q) = A_1(q) + g̃_3(q)\overline{A_1(q)}`,
  the bound `|L| ≤ 2|A_1|` (the root number is a normalized cubic Gauss sum of modulus one), the
  dyadic split, the Mellin separation of `q` from the weight, the removal of the `S`-part, and the
  identification of the family with nonprincipal rows of Statement C via cubic reciprocity.
* **Sec. 3 (exponent bookkeeping).** It restates the induction with the earlier notes' check IDs.
  It adds the closed form for the two-stage margin.
* **Sec. 5 (risk register).** The single most likely failure point is the inherited centred
  stage (item 9), not any cubic-specific lemma.

## What this folder is not

* It is not a review of Lemma 18.1. Every inherited step is imported and was checked only by
  bounded agent reviews.
* It does not strengthen any statement in the notes it collects. Its theorem is exactly the
  CONDITIONAL statement of CUBIC_N3_GAPS.md Sec. 4. Three things are added: the explicit
  application step, the exact margin (which replaces the grid value), and the exact tolerance for
  a loss confined to the centred deficit. CUBIC_N3_GAPS quotes 0.0155M; that is the more
  conservative margin, demanded in every constraint at once.

## Note added after drafting (same day): the centred stage survived one attack

[../../reviews/CUBIC_CENTRED_ATTACK.md](../../reviews/CUBIC_CENTRED_ATTACK.md) attacked risk item 9
(the inherited centred stage) adversarially. Its verdict is **(a) survives at the level of the
displayed steps**:
* No loss of size `cM` was found in the centred-coefficient invariance or in the masked lattice
  cancellation, for `n = 3`, for reflected inputs, or for `L` up to the caps.
* Both lemmas are order-free. The lattice error is `O(Z^ε)`.
* The binding point `v = L` uses no lattice saving.
* The tightest constraint there is `κ = 5/6` (Lemmas 4.F/4.G), which was not re-reviewed.

Its script passes 18 of 19 checks. The one failure, [L2b], is attributed (CUBIC_CENTRED_ATTACK
§3.3) to `Z^ε` and divisor factors dominating at `Z ≤ 10⁸`. At this scale the check is
uninformative; it is not a pass.

Left open: whether every step of l. 13114-14310 acts identically on both rectangles. If one
does not, the loss can be as large as `M/3`, which would exceed the tolerance.

The route stays PROPOSED and CONDITIONAL on (H-A) and (H-B). No moment bound is proved.

## Note added later the same day: the "both rectangles" condition

[../../reviews/CUBIC_BOTH_RECTANGLES.md](../../reviews/CUBIC_BOTH_RECTANGLES.md) decides the
condition that the centred-stage attack left open. Its verdict is **(a) closed at the level of the
manuscript's displayed steps** (bounded, one agent).
* The two rectangles are the two terms of `D_b`: the original product `S(X1)S(X2)` and the
  comparison `S(Y1)S(Y2)`, with `X1X2 = Y1Y2`.
* Every step before the Θ/non-Θ row split, and every Θ-row step, acts identically on both.
* On non-Θ rows, l. 14119-14300 split them by the triangle inequality and clip each separately.
  No cancellation is used there, so this costs `0·M`, at most `2θ_N` per edge.
* For `n = 3`, Gauss sums, reciprocity and units act on whole columns, never on one rectangle.
  The quadratic twist `χ_p³` is specific to the sextic case.
* The stakes: a mismatch in the Θ branch would have cost `M/3`, which is `144/11` times the
  tolerance. The manuscript keeps clipping out of that branch (l. 14086, 14703-14705, 14786).

Runs: exact model 12/12. Float model 32/33 PASS, 23 uninformative, and 1 FAIL, a control that
went undetected at the smallest geometry (a scale limit, recorded as FAIL).

The route stays PROPOSED and CONDITIONAL on (H-A) and (H-B). The Fourier-measure lemmas remain
imported, and no human has checked any of this.

## Note added later the same day: risk item 1 (profile uniformity)

[../../reviews/CUBIC_PROFILE_UNIFORMITY.md](../../reviews/CUBIC_PROFILE_UNIFORMITY.md) closes risk
item 1 with **verdict (a)**, conditional on Lemma 18.1's profile-uniformity clause carrying over to
`n = 3` as part of (H-A). Bounded review by one agent.
* Statement C allows any smooth profile supported in a fixed compact interval of `(0, ∞)`,
  complex values included. Its constant depends on finitely many seminorms
  (l. 12571-12578, 719-722).
* Polynomial dependence on the seminorms is not stated in the manuscript. It follows from
  linearity (Lemma H there).
* The application feeds in only `W_w(y) = y^{−1/2−w} φ(y)`, with `p_j(W_w) ≍ (1+|Im w|)^j`. The
  Gamma weight integrates every polynomial, so the `X`-exponent stays `1+ε`.
* The 7/8 proof itself (Prop 19.2) applies Lemma 18.1 to complex witness profiles, so the same
  clause is load-bearing there too, in a stronger form.

Recommended edits to SKETCH.md, recorded here rather than applied:
* state the clause in Statement C, and list it as A8 under (H-A);
* correct the Sec. 2.7 losses to `(log X)⁴(log log X)⁴`.

Numerics: 26/27; one crude fit (E3) fails, and the failure is kept and explained.

## Note added later the same day: risk item 10 (allocation losses)

[../../reviews/CUBIC_ALLOCATION_LOSS.md](../../reviews/CUBIC_ALLOCATION_LOSS.md): **verdict (a)**,
no hidden loss of order `M` in the common-support allocations at `n = 3`. Bounded review by one
agent.
* Every allocation inequality of both transforms (A2, A4), redone at `n = 3` in exact arithmetic,
  has minimum slack exactly 0, and none is negative.
* Where the slack is 0:
  * the budget (2.6) at prime types (1,1) and (2,1);
  * `F_1 = 5c/6`;
  * `F_2 = b_2` at three types;
  * the crude Gauss-row count.
* A joint exact LP over both transforms gives worst centred-deficit slack 0, at `v = L`.
* The script passes 56/56, with 11 failing controls, all detected.

Correction to the risk register's tolerance:
* `c*(δ) = (11−147δ)/432` covers only a loss confined to the centred deficit.
* A loss in an order-free ledger would be fatal for any `c > 0`.
* A loss in `F_1/F_2` scales with `v`, and two stages would then need `κ ≥ 3 − √5 ≈ 0.764`.

# Level-2 audit F3-yang-constant

```text
Status: AUDIT (Level 2; adjudicated where flagged)
Scope: the specific issue named below, not the whole paper
Exact sources or dependencies: see 'Sources checked'
What was actually run: independent reading and recomputation by an auditor agent; independent two-sided adjudication where the auditor flagged an issue
Smallest remaining gap: see adjudication
```

**Target.** F3-yang-constant: Yang, arXiv 2301.03165 (v1/v2; JMAA 534 (2024) 128124), Littlewood-type zero-free constant 21.432 vs 21.233; downstream Bellotti arXiv 2306.10680 / JMAA 536 (2024) 128249, and Bellotti-Trudgian-Yang arXiv 2603.21490

**Auditor classification.** `suspected_gap`

**Final classification.** `suspected_gap`; public characterization allowed: **False**

**Summary.** The 21.432 vs 21.233 discrepancy comes from versions, not from an error. Yang arXiv v1 (Jan 2023) has 21.432 (M1=0.0466605). Yang v2 (Jan 2024, "updates in response to reviewer feedback") and the JMAA abstract have 21.233 (M1=0.0470978). Bellotti's only arXiv version (June 2023) cites 21.432 accurately for its date. It uses that value only to cover t <= exp(463388), and I recomputed the crossover at log t = 463537.3, so that step is valid. Bellotti's published abstract gives 53.989, not 54.004. That is consistent with her adopting 21.233: the (21.233, 53.989) crossover at log t = 482035.95 matches BTY's "exp(482036)". Because 21.233 < 21.432, the v2 region contains the v1 region, so no downstream constant (Bellotti in either version, BTY 2026, Fiori-Jaskari 2026) is weakened. The L2 audit did find a proof-coverage issue in Yang himself. The written argument does not cover v1's 21.432 for exp(208.43) < t < exp(268.95), because v1's t0 lies past the (1.4)/Littlewood crossover; v2 repaired this. In the current v2 text, 21.233 is not covered for exp(45.594) < t < exp(50.132): the claimed width beats both of the regions the paper invokes there, (1.3) and (1.4). The statement is not shown false. The window can be closed by BTY 2026 Lemma 1, a preprint. No cited downstream result relies on it. This was first raised here and needs independent reproduction.

**Witness / evidence.** Source facts: v1 (4.80) has M1 := 0.0466605 (1/M1 = 21.43140, giving 21.432), t0 = exp(268.95), t1 = exp(1059.1). v2 (4.80) has M1 := 0.0470978 (1/M1 = 21.23241, giving 21.233), t0 = exp(170.2), t1 = exp(967.6). Bellotti arXiv v1 line 34 cites "C1 = 21.432 for |t| >= 3", and §6 says "For t <= exp(463388) we use ... Yang". The Bellotti JMAA abstract (OpenAlex) gives 53.989. BTY eq. (3) uses 21.233 for t > exp(76.463).

Window witness for v2, checked rigorously with Arb (python-flint 0.9.0, 200 bits) at log t = 47. Claimed width loglog t/(21.233 log t) = 0.0038580528. Widths available from the paper: (1.3) 1/(5.558691 log t) = 0.0038276270; (1.4) Ford Thm 3 with HPY X = 0.618 = 0.0038475881. Both are strictly smaller. Using the paper's own formulas: (1.3) covers 21.233 only for log t <= 45.5944, and (1.4) covers it only for log t in [50.1325, 170.2635]. The proof's text says "If H <= t < t0, then Corollary 1.2 follows from (1.4)".

v1 witness at log t = 240 (Arb): claimed 21.432 width 0.0010655093 > (1.4) width 0.0010571932, while v1's main argument starts only at log t0 = 268.95.

The t0-1 step in v2: at log t = 170.2, (1.4) gives Z >= 0.04709721, slightly below M1 = 0.0470978 but above 1/21.233 = 0.04709650. The displayed inequality chain is reversed, but 21.233 still survives.

My transcription of (1.4) is confirmed: it reproduces Yang's own crossovers at 46.204 [(1.3)=(1.4)], 170.26 (v2), 208.43 (v1), 532141.05 (v2) and 511173.05 (v1).

**Sources checked.**
- arXiv:2301.03165v1 PDF (sha256 bd55cc8d...) and LaTeX e-print (sha256 c224faf1...)
- arXiv:2301.03165v2 PDF (sha256 ca09f14b...) and LaTeX e-print (sha256 0253a3f7...)
- arXiv API metadata for 2301.03165 (v2 comment: 'Updates in response to reviewer feedback'), 2306.10680 (single version, 2023-06-19), 2603.21490
- Crossref 10.1016/j.jmaa.2024.128124 (Yang, JMAA 534(2) 128124) and 10.1016/j.jmaa.2024.128249 (Bellotti, JMAA 536(2) 128249); Crossref updates filter: no errata/corrections for either
- OpenAlex abstracts of both JMAA versions (Yang: 21.233, exp(171)..exp(5.3e5); Bellotti: 53.989, 70.7, 4.438, 48.0718)
- arXiv:2306.10680v1 full text (sha256 e0703be3...), sections 1 and 6
- arXiv:2603.21490v1 (Bellotti-Trudgian-Yang) full text (sha256 4337b896...), intro and section 5 dependency statement
- arXiv:2212.06867 (Mossinghoff-Trudgian-Yang) full text, Theorems 1.3/1.4 and region (1.8), checking for other mid-range regions
- arXiv:2609.23222v2 (Fiori-Jaskari) full text: cites 21.233 in a survey; uses 53.989
- arXiv:2405.04869 grep (no use of the constants)
- Scripts (mpmath non-rigorous; python-flint Arb rigorous for the witness): /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/f3scripts/{yang_v2_check.py,yang_t0_check.py,yang_lowrange.py,yang_coverage.py,yang_intro_crossovers.py,yang_window_arb.py,yang_v2_lowbranch.py}

## Auditor report

# F3-yang-constant: L2 audit report

**Status:** L2 detailed technical audit. Bibliographic and version facts are verified. I re-derived the final step of Yang's zero-free-region constant and the coverage bookkeeping. New finding: a suspected gap in Yang, first raised here, not yet independently reproduced.
**Scope:** Yang arXiv 2301.03165 v1 and v2, published as JMAA 534(2) (2024) 128124. Bellotti arXiv 2306.10680 v1, published as JMAA 536(2) (2024) 128249. Bellotti-Trudgian-Yang (BTY) arXiv 2603.21490 v1. Also checked for downstream use: Fiori-Jaskari arXiv 2609.23222 v2 and MTY arXiv 2212.06867.

## 1. Which value appears where

| Source | Constant | Underlying data |
|---|---|---|
| Yang arXiv **v1** (2023-01-09) | **21.432** (abstract, Cor. 1.2 (1.6), final display) | M1 = 0.0466605, 1/M1 = 21.43140, rounded up to 21.432; t0 = exp(268.95), t1 = exp(1059.1), α = 0.141797; "largest known for exp(208.5) <= t <= exp(511173)" |
| Yang arXiv **v2** (2024-01-16, comment "Updates in response to reviewer feedback") | **21.233** | M1 = 0.0470978, 1/M1 = 21.23241, rounded up to 21.233; t0 = exp(170.2), t1 = exp(967.6), α = 0.13913; "largest known for exp(170.3) <= t <= exp(532141)" |
| Yang **JMAA 534 (2024) 128124** (abstract via OpenAlex; full text not accessed) | **21.233** | same abstract wording as v2 ("exp(171) <= t <= exp(5.3·10^5)"); Crossref lists no erratum |
| Bellotti arXiv 2306.10680 (only version, 2023-06-19) | cites **21.432** | [Yan23] = arXiv:2301.03165 (2023). Only Yang v1 existed then, so the citation is **accurate for its date** |
| Bellotti **JMAA 536 (2024) 128249** (abstract via OpenAlex; full text not accessed) | VK constant **53.989** (arXiv: 54.004) | consistent with switching to Yang's 21.233; see section 2 |
| BTY 2026 (arXiv 2603.21490v1) | cites **21.233** [Yang JMAA] and **53.989** [Bellotti JMAA] | uses Littlewood (3) only for t > exp(76.463) |
| Fiori-Jaskari 2026 (arXiv 2609.23222v2) | cites 21.233 (survey only); uses 53.989 | none |

## 2. How Bellotti uses Yang's constant, and whether anything changes

- **Where Yang enters Bellotti's proof.** Bellotti arXiv §6 (Proof of Theorem 1.2) says: "For t <= exp(463388) we use the best known explicit Littlewood zero-free region due to Yang". Above that she runs MTY's argument with T0 = exp(463388), M1 = 0.050007, E = 1.8008278, R = 468.
- **Requirement:** the Littlewood region with C1 = 21.432 must contain the VK region with C2 = 54.004 for t <= T0. That holds exactly when C2^3 (log x)^4 >= C1^3 x, where x = log t.
  - Recomputed crossover: x = **463537.30**, so T0 = exp(463388) is valid.
  - At small t the Littlewood region is narrower (lower crossover x ≈ 1.7, t ≈ 5.5). Below t = 14.13 there are no zeros at all, so nothing is missing there.
- **Effect of v2.** 21.233 < 21.432, so the v2 region contains the v1 region. Every use of 21.432 stays valid. Bellotti's arXiv constants are **not weakened**.
- **Published Bellotti (53.989).** The crossover for (21.233, 53.989) is x = **482035.95**. That matches BTY's sentence "(4) is sharper than (3) for t > exp(482036)". The published version therefore most likely used Yang's 21.233 with a larger T0. This is an inference: I did not read the published full text, so its T0 is unknown to me.
- **BTY 2026.** Their Theorem 1 uses Yang's (3) only for log t > 21.233/4.896 → **e^(4.3368) = 76.4629** (recomputed). Their Theorem 2 threshold is e^(19.62/4.8594) = 56.6865 (recomputed). Their Lemma 1 (3 <= t <= exp(76.47)) is proved by iteration from any classical region with c > 1/6 (Kadiri, MT or MTY) and does not depend on Yang.

**Conclusion on the stated discrepancy:** it is version drift. No value was mis-cited, and no downstream constant is affected.

## 3. L2 audit of Yang's constant: new findings

All formulas are transcribed from the LaTeX sources. My transcription of (1.4) reproduces Yang's own intro crossovers:
- (1.3) = (1.4) at log t = 46.204 (paper: 46.2/46.3);
- (1.4) = Cor. 1.2 at 170.26 (v2; paper 170.2/170.3) and 208.43 (v1; paper 208.4/208.5);
- (1.5) = Cor. 1.2 at 532141.05 (v2) and 511173.05 (v1).

### 3a. v2 / current: low-range window not covered by the argument (suspected gap)
- **The step.** The proof (v2 §4, before (4.79)) says: "If H <= t < t0, then Corollary 1.2 follows from (1.4)", with H = 5.45·10^8 and t0 = exp(170.2).
- **What the cited regions actually cover:**
  - (1.4) = Ford Thm 3 with HPY's 0.618 contains the 21.233 Littlewood region only for log t in **[50.1325, 170.2635]**.
  - MTY's classical region (1.3), 1/(5.558691 log t), covers it only for **log t <= 45.5944**.
- **The gap.** For **exp(45.594) < t < exp(50.132)**, neither cited region contains the claimed region.
- **Rigorous witness** (Arb, 200 bits) at log t = 47:

  | Region | Width at log t = 47 |
  |---|---|
  | claimed, loglog t/(21.233 log t) | 0.0038580528 |
  | (1.3) | 0.0038276270 |
  | (1.4) | 0.0038475881 |

  The claimed width is strictly larger than both at log t = 45.7, 46, 47, 48, 49, 50 and 50.1.
- **Can the main argument reach down there?** Not by the paper's own argument. Its t0 <= t < t1 branch needs η = (8 − E/L2)^(-1) with E = 30.95461, which is negative at loglog t ≈ 3.8.
- **No other region as of 2024 fills it.** MTY 2212.06867 offers only 5.558691 (for t >= 2), Ford (1.8) with X = 3 (weaker), and an intermediate region for t >= exp(1000).
- **The v2 intro is also off here.** It says (1.4) is "sharpest" for exp(46.3) <= t <= exp(170.2). Measured against the claimed Corollary 1.2 region, that is inaccurate on [46.3, 50.13].
- **Status:**
  - The theorem is **not shown false**: no zero is exhibited, and none is expected.
  - The written proof does not cover this finite range.
  - It is closable using BTY 2026 Lemma 1 (preprint): 1/(4.896 log t) contains the 21.233 region for log t <= 76.46.
- **Downstream impact: none found.**
  - Bellotti (either version) needs only the VK region inside this window, and (1.3)/(1.4) contain it with a factor of about 4.2 to spare.
  - BTY uses the 21.233 region only for log t > 76.46.
  - Fiori-Jaskari use 53.989.

### 3b. v1 (superseded): gap that v2 repaired
- **The step.** v1 takes t0 = exp(268.95) and still covers H <= t < t0 by (1.4) alone.
- **The problem.** (1.4) is narrower than the 21.432 Littlewood region for log t > 208.43. v1's own intro says Corollary 1.2 is the largest region from exp(208.5) up.
- **Witness** (Arb) at log t = 240: claimed width 0.0010655093 > (1.4) width 0.0010571932.
- **How the written argument fares:**
  - Read literally, v1's argument establishes only about 1/0.04597 ≈ 21.75 near t0.
  - v2 moved t0 to exp(170.2), right at the crossover, which fixes this.
- **Consequence for Bellotti's 21.432:** v2's argument does establish 21.432 for all t >= 3:
  - (1.3) covers up to log t = 47.26;
  - (1.4) covers [40.90, 208.43];
  - v2's main argument covers t >= exp(170.2) at 21.233.

  So the value Bellotti cited is fully supported by the published paper. Ironically, it is better supported than 21.233 itself.

### 3c. v1 and v2: "t0 − 1" step written in the wrong direction (presentation)
- **What the step needs.** Zeros with t' in [t0 − 1, t0) must satisfy 1 − β' >= w14(t') >= M1 loglog t'/log t'.
- **What is displayed:** "1 − β' <= w14(t0 − 1) < M1 loglog t0/log t0 < ...", i.e. the opposite direction.
- **In v2 this is harmless:**
  - At log t0 = 170.2, (1.4) gives Z >= **0.04709721**. That is slightly below M1 = 0.0470978 (ratio 0.99998743).
  - The needed step therefore fails only for M in (0.0470972, 0.0470978). Running the contradiction argument with that threshold gives M > 0.0470972 > 1/21.233 = **0.0470965**.
  - So 21.233 survives because of the rounding.
- **In v1 the same reversal hides the gap in 3b.**

### 3d. v2: typo in (4.93) and (4.107)
- **The issue.** The displayed C1 = A0(x0)/loglog t0 and the γ-term (γ/2)·loglog t0/log t0 in C5 do not match the printed numbers. The numbers match **t1**, which is valid because t >= t1 in that branch.
- **Values:**
  - C1(t1) = 0.0479575 <= 0.047958; literal t0 reading gives 0.06418.
  - C5 with t1 = 3.594128 <= 3.59415; literal t0 reading gives 3.600788.
- **Consequence:** read literally, the final ratio would be 0.0470159 < M1. This only affects reproducibility; the result stands.

### 3e. Arithmetic re-derived (mpmath, non-rigorous high precision)
Each value below agrees with the paper's printed bound.

**t >= t1 branch (v2):**

| Quantity | Recomputed | Printed bound |
|---|---|---|
| x* | 15.83268 | — |
| A0(x0) | 0.3296990 | <= 0.3297 |
| 1/(C1 M1) | 442.734 | >= 442.729 |
| C2 | 1.581752 | 1.58176 |
| C3 | 0.329888 | 0.32989 |
| C4 | 0.276487 | 0.27649 |
| C6 | 0.0001625 | 0.00017 |
| (4.122) ratio | 0.04709785 | > M1 |

**t0 <= t < t1 branch (v2):**

| Quantity | Recomputed | Printed bound |
|---|---|---|
| L2/loglog t bound | 1.004379 | 1.0044 |
| (4.124) | 0.0603807 | 0.06039 |
| 1/(0.06039·M1) | 351.588 | 351.588 |
| (4.129) | 0.525059 | 0.52506 |
| B2 | 0.611839 | 0.61184 |
| η range | [0.2857, 0.49997] | within [2/7, 1/2] |
| (4.134) | 0.0475042 | >= 0.0475 |

**Not re-derived:**
- Theorem 1.1 (the 1.546 constant) and the explicit k-th derivative test;
- Lemmas 4.1–4.8, c(R), C7–C11 and B3(t0);
- the published full texts of both JMAA articles;
- Yang's PhD thesis (19.62 and 51.34, cited by BTY).

## 4. Classification and recommended handling
- **Stated F3 question (21.432 vs 21.233 and Bellotti's citation):** version drift. Bellotti's citation was correct, and no constant in Bellotti, BTY or Fiori-Jaskari is affected. Taken alone, this would be no_issue_found_in_inspected_portion.
- **Overall classification: `suspected_gap`.** This comes from 3a: the current, published v2 proof does not cover the 21.233 region for exp(45.594) < t < exp(50.132).
  - The witness is a rigorous Arb comparison using the paper's own formulas.
  - Per methodology section 6(i) and (iv), it was first raised by this auditor. It must be independently reproduced before any public characterization, and should be kept in `audits/unresolved_findings.md` meanwhile.
  - It does not falsify the statement, and it can be closed with BTY 2026 Lemma 1, which is itself a preprint.
- **Items 3b–3d** are respectively a superseded-version gap repaired by the author in v2, and presentation-level issues.
- **Smallest statement whose failure would change this verdict:** for some log t in (45.594, 50.132), (1.3) or (1.4) is at least as wide as loglog t/(21.233 log t). The Arb checks above say no.

## 5. Reproducibility
- **Scripts:** /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/f3scripts/
  - yang_window_arb.py: Arb, rigorous witness;
  - yang_coverage.py, yang_lowrange.py, yang_t0_check.py, yang_intro_crossovers.py: coverage and crossovers;
  - yang_v2_check.py, yang_v2_lowbranch.py: constant re-derivation.
- **Versions:** mpmath at dps 30–40 (non-rigorous high precision); python-flint 0.9.0 (Arb).
- **Source hashes (sha256):**
  - arXiv PDFs: 2301.03165v1 bd55cc8d…, v2 ca09f14b…; 2306.10680 e0703be3…; 2603.21490 4337b896…; 2212.06867 127c32eb…; 2609.23222 77d12f38…
  - Yang LaTeX e-prints: v1 c224faf1…, v2 0253a3f7…



## Independent adjudication

**Rationale.** The 21.432 vs 21.233 discrepancy is version drift, not an error. Yang arXiv v1 (Jan 2023) states 21.432. Yang v2 (Jan 2024, "updates in response to reviewer feedback") and the JMAA abstract state 21.233. Bellotti's only arXiv version predates v2 and cites 21.432 correctly. She uses Yang only for t <= exp(463388); the crossover is at log t = 463537.30 (certified with Arb), so that step is valid. 21.233 < 21.432, so no downstream constant is weakened (Bellotti, BTY, Fiori-Jaskari).

I independently reproduced the auditor's secondary finding from freshly downloaded LaTeX (same hashes), using my own certified Arb code. In arXiv v2 the proof says "If H <= t < t0 then Corollary 1.2 follows from (1.4)", with t0 = exp(170.2). But for exp(45.594) < t < exp(50.132) the 21.233 region is strictly wider than both (1.3) and (1.4), and the paper's main argument is set up only for t >= exp(170.2). So the written proof does not cover that finite window. The step is invalid at that point, with a corrected computation.

The theorem is not refuted. It follows from Yang's own later work: his PhD thesis (UNSW 2025, CC BY), Theorem 1.2 with constant 19.62 for t >= 3, which handles small t through a new classical region (Lemma 2.1), and BTY 2026, Lemma 1. Neither is an erratum, and neither has been audited here. I could not read the published JMAA full text, which may differ from v2.

The finding is a gap in the proof, not an error in the result. Combined with the inaccessible published text, this keeps it at suspected_gap and rules out any public characterization as an error. I also raise a new, unverified point: Ford's Theorem 3 constants are calibrated to X = 3, so substituting X = 0.618 to get (1.4) requires recomputation. It does not remove the window.

# F3-yang-constant: adjudication report

**Status:** Adjudication of the Level-2 audit. I rebuilt the defence from primary sources and reran the auditor's witness with my own code.

**Scope:**
- Yang, arXiv 2301.03165 v1 and v2: LaTeX e-prints downloaded afresh. Hashes match the auditor's (v1 `c224faf1…`, v2 `0253a3f7…`).
- Yang JMAA 534 (2024) 128124 and Bellotti JMAA 536 (2024) 128249: abstracts via OpenAlex, metadata via Crossref. Both are open access under CC BY. The publisher full text could not be fetched in this environment, so it was **not inspected**.
- Bellotti, arXiv 2306.10680 (PDF hash `e0703be3…`).
- Bellotti–Trudgian–Yang (BTY), arXiv 2603.21490 (hash `4337b896…`).
- Mossinghoff–Trudgian–Yang (MTY), arXiv 2212.06867.
- Ford, arXiv 1910.08205 v1, v4 and v5.
- **Yang's PhD thesis** (UNSW 2025, doi 10.26190/unsworks/31825, CC BY 4.0, PDF sha256 `24e8781f…`). The original auditor did not read this.

**Arithmetic:**
- python-flint 0.9.0 (Arb, 256-bit) for every crossover and witness described as certified.
- mpmath 1.3.0 (non-rigorous high precision) for the Ford recomputation in section 5.

---

## 1. Verdict

| Question | Finding |
|---|---|
| Which value is in which version | **v1 (2023-01-09): 21.432** (M1 = 0.0466605; 1/M1 = 21.431403, rounded up). **v2 (2024-01-16) and JMAA abstract: 21.233** (M1 = 0.0470978; 1/M1 = 21.232414). This is version drift. Crossref lists no erratum for either JMAA paper. |
| Which value Bellotti uses | arXiv 2306.10680 (only version, June 2023) cites **21.432** from [Yan23] = arXiv:2301.03165. That was correct on its date. §6: "For t <= exp(463388) we use … Yang". |
| Is Bellotti's arXiv proof valid | Yes. Littlewood(21.432) contains the Vinogradov–Korobov (VK) region (54.004) up to log t = **463537.2958** (Arb), which exceeds 463388. |
| Published Bellotti (53.989) | Valid only with Yang's 21.233 (crossover **482035.9511**, matching BTY's "exp(482036)"), or with T0 <= exp(462980.51). Keeping 21.432 with 53.989 and T0 = exp(463388) would **fail**, since that crossover is 462980.51. The published version therefore almost certainly uses 21.233 or a different T0. This is an inference: the published text was not read. |
| Downstream constants | **None affected.** The v2 region contains the v1 region. BTY uses (3) = 21.233 only for t > exp(76.4629) (Arb). Fiori–Jaskari use 53.989. |
| Auditor's new finding (Yang v2 low-range window) | **Independently reproduced** at the level of the arXiv v2 text. It is a gap in the written proof over a finite range. The statement is not refuted, and the author's own later work implies it. |
| Final classification | **suspected_gap**: the proof-coverage gap is reproduced, but the result is not shown false and the published text is unread. |
| Public characterization as error | **Not allowed.** |

## 2. Strongest defence of Yang's Corollary 1.2 (21.233, |t| >= 3)

1. **Charitable reading of "follows from (1.4)" as "follows from (1.3) and (1.4)".** Both regions are displayed in the paper's introduction.
   - (1.3) is MTY's 1/(5.558691 log t). It contains the 21.233 region exactly when log t <= exp(21.233/5.558691) = **45.59436755**.
   - (1.4) contains it on [**50.13245727**, **170.2635232**].
   - Even read this way, **exp(45.594) < t < exp(50.132)** remains uncovered.
2. **Could the paper's own main argument reach down there?** No, not without a new run.
   - The t0 <= t < t1 branch uses η(t) = (8 − E/L2)^(-1) with E = 30.95461 and needs 2/7 <= η <= 1/2.
   - That forces roughly log t ∈ [174, 970] (with log log t ≈ L2).
   - At log t ≈ 47, 8 − E/L2 ≈ 0, so the branch is undefined there.
3. **Other regions available by January 2024.**
   - MTY offers only 5.558691 for t >= 2, Ford's (1.8) with X = 3 (weaker), and an intermediate region for t >= exp(1000).
   - Kadiri, Jang–Kwon and Mossinghoff–Trudgian all have constants above 5.5587.
   - Closing the window up to log t = 50.13 needs a classical constant <= 21.233/log 50.13 ≈ 5.424.
   - Closing it with (1.4) would need a better critical-line constant than X = 0.618. I found none in the 2024 literature.
4. **Ford's corrected Theorem 3** (arXiv v5, Feb 2025), rerun with X = 0.618 (section 5): it covers 21.233 only from log t ≈ 49.886. The window persists as roughly (45.594, 49.886).
5. **Author's later work closes the window, so the statement survives.**
   - **Yang's PhD thesis (2025):** Theorem 1.2 gives a 19.62 Littlewood region for t >= 3. It is proved as Lemma 2.1 (classical 1/(4.862 log t) for 2 <= t <= exp(56.6)) plus Lemma 3.1 (19.62 for t >= exp(56.5)), with no use of Ford's region (1.4). Since 19.62 < 21.233, this implies Corollary 1.2 for all t >= 3.
   - **BTY 2026 Lemma 1:** 1/(4.896 log t) for 3 <= t <= exp(76.47). It contains the 21.233 region for log t <= exp(21.233/4.896) = 76.4629. BTY (Yang is a co-author) apply (3) only above exp(76.463).
   - Neither source is an erratum, and neither mentions the gap. The thesis is examined but not journal-refereed. BTY is a preprint. I did not audit either.
6. **The published text may differ from v2.** It was not accessed. Against this possibility:
   - v2 was posted 5 days after JMAA's online date (2024-01-11);
   - v2 carries the comment "updates in response to reviewer feedback";
   - its abstract numbers are identical to the JMAA abstract (21.233; exp(171) <= t <= exp(5.3·10^5)).

   So v2 very likely equals the accepted text, but this is unverified.

## 3. Independent test of the auditor's witness

The formulas are copied from the v2 LaTeX. (1.4) is identical in v1 and v2:

```
(1.4)  width = (0.04962 − 0.0196/(J+1.15)) / (J + 0.685 + 0.155·log log t),
       J = (1/6)·log t + log log t + log 0.618
claimed width = log log t / (21.233·log t)
```

Certified Arb comparison (256-bit):

| log t | claimed (21.233) | (1.3) | (1.4) | Claimed wider than both? |
|---|---|---|---|---|
| 45.6 | 0.00394526944 | 0.00394514186 | 0.00392924996 | yes |
| 46 | 0.00391990462 | 0.00391083628 | 0.00390553337 | yes |
| 47 | 0.00385805275 | 0.00382762700 | 0.00384758811 | yes |
| 48 | 0.00379833378 | 0.00374788477 | 0.00379148764 | yes |
| 49 | 0.00374063505 | 0.00367139732 | 0.00373713979 | yes |
| 50.1 | 0.00367937512 | 0.00359078780 | 0.00367927914 | yes |
| 50.14 | 0.00367718947 | 0.00358792319 | 0.00367721174 | no ((1.4) covers) |

**Certified crossovers (Arb bisection):**

| Crossover | log t | Paper's own figure |
|---|---|---|
| (1.3) = (1.4) | 46.20443 | "46.2/46.3" |
| (1.4) = 21.233 (high) | 170.26352 | "170.2/170.3" |
| VK 55.241 = 21.233 | 532141.05 | "532141" |
| VK 55.241 = 21.432 | 511173.05 | v1's "511173" |

My transcription of (1.4) therefore matches the author's own numbers.

**v2 proof text (verbatim):** "If $H \le t < t_0$, then Corollary 1.2 follows from (1.4)", with t0 = exp(170.2).
- For (1.4) alone this inference fails on all of [log H ≈ 20.1, 50.132].
- With (1.3) added, it still fails on (45.594, 50.132).
- **The witness is confirmed.**

**v1 (superseded):**
- t0 = exp(268.95), but (1.4) covers 21.432 only up to log t = 208.42908.
- Z from (1.4) at log t0 = 268.95 is 0.0459693, below 1/21.432 = 0.0466592.
- So v1's written argument had an uncovered range (208.43, 268.95) and a failing t0 − 1 step. v2 repaired this by setting t0 = exp(170.2), right at the crossover.
- 21.432 at low t is fully covered: (1.3) up to 47.2562 and (1.4) from 40.8993. Bellotti's cited value is therefore supported by v2's argument together with (1.3) and (1.4).

**The t0 − 1 step in v2:**
- Z from (1.4) at log t = 170.2 is 0.04709720792 (Arb). That is below M1 = 0.0470978 but above 1/21.233 = 0.04709650073.
- Z from (1.4) is decreasing near t0, so the minimum over [t0 − 1, t0) is at t0.
- The displayed chain "1 − β' <= (1.4)(t0 − 1) < M1·loglog t0/log t0" has the wrong direction for what the step needs.
- Repaired reading: zeros there have Z >= 0.0470972. Running the contradiction with that threshold gives M >= 0.0470972 > 1/21.233.
- So 21.233 survives on rounding. This is presentation-level, and I agree with the auditor.

**Bellotti in the window:** (1.3) is 4.219 times wider than VK(54.004) at log t = 47. Bellotti never needs Yang's region at low t.

## 4. Assessment of the gap

- **Not an error in the result.** No zero is exhibited, the region is widely expected to be zero-free, and the author's later results imply the statement.
- **It is a real gap in the written argument of arXiv v2.** It is a precise invalid step, confirmed by certified computation from the paper's own formulas. It is confined to the finite range exp(45.594) < t < exp(50.132), about 6.3·10^19 to 5.9·10^21.
- **No downstream impact found.** BTY, Bellotti (both versions) and Fiori–Jaskari either use Yang's region only above exp(76.46), or need only the much narrower VK region there.
- **Wording in the introduction.** The v2 introduction says (1.4) is "sharpest" for exp(46.3) <= t <= exp(170.2) and that Corollary 1.2 is largest only from exp(170.3). If Corollary 1.2 holds, it would in fact be the largest known region on (45.594, 50.132). This is minor.

## 5. New observation by the adjudicator (unverified; keep in unresolved findings)

(1.4) is said to be "formed by substituting [HPY Thm 1.1] into [Ford Thm 3]". Ford's numerical constants depend on X, the critical-line constant in |ζ(1/2+it)| <= X t^(1/6) log t (X = 3 from Cheng–Graham; X = 0.618 from Hiary–Patel–Yang), through J(t). They are calibrated for X = 3:

- **Published logic (v1–v4).** Ford's closing "Maple" check, M <= 0.685 + 0.155 log log t, holds for X = 3 with a margin of only 5·10^-5 at T0 = 5.45·10^8. With X = 0.618 it fails by up to 0.12 (required constant about 0.806 instead of 0.685; mpmath grid).
- **Corrected logic (Ford arXiv v5, Feb 2025).** The comment says "Theorems 2 and 3 have different numerics". With X = 3 the maximum of (9.12) is 0.6744 < M0 = 0.675, and this reproduces Ford's Theorem 4 change from 8.463 to 8.464. With X = 0.618 the check needs M0 ≈ 0.788.
- **Effect of recomputing with v5 logic, X = 0.618, M0 = 0.789** (non-rigorous):
  - the region stays within −0.71% to +0.08% of printed (1.4);
  - it covers 21.233 on [49.886, 173.169];
  - the t0 − 1 step passes (Z = 0.04713 > M1).

  So the low window shrinks only to roughly (45.594, 49.886), and nothing else is lost.
- **Effect of a published-logic repair** (constant 0.806): it would open further gaps at log t ≈ (45.6, 63.4) and (153.7, 170.2). But Ford himself withdrew that logic.
- **Status:** this concerns how (1.4) is justified, not the reproduced window. Other X-dependent steps of Ford's proof were not rechecked. It needs independent reproduction before any use.

## 6. Other auditor items

| Item | Adjudicator view |
|---|---|
| (4.93) and (4.107) print t0 where the numbers need t1 | Not rechecked by me. Plausible and harmless, since t >= t1 in that branch. |
| Re-derived constants in the main branches (section 3e) | Not rechecked by me beyond 1/M1 and the crossovers. |

## 7. Classification and handling

- **Stated F3 question:** version drift. **no_issue_found_in_inspected_portion** for Bellotti, BTY and Fiori–Jaskari.
- **Overall: suspected_gap.**
  - The coverage gap in Yang arXiv v2 is now reproduced independently, from fresh sources and separate Arb code.
  - "Suspected" is kept because the published text was not inspected, and because the statement is implied by the author's later work, so this is a gap and not an error.
- **Public characterization as an error: not allowed.** The theorem is not shown false.

  Once the published text is checked, a neutral note would be supportable, for example: "the written proof in arXiv v2 does not cover exp(45.59) < t < exp(50.13); the statement follows from Yang's 2025 thesis (Thm 1.2) and BTY Lemma 1".
- **Record placement:** keep the window finding, and the section 5 Ford/X observation separately, in `audits/unresolved_findings.md`.
- **Smallest statement that would overturn the gap verdict:**
  - the published text covers (45.594, 50.132) by some other argument; or
  - a region available in 2024 contains loglog t/(21.233 log t) on that window.

## 8. Reproducibility

**Scripts** (all in `/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/adjf3_scripts/`):

| Script | What it does |
|---|---|
| `window.py` | Arb width table |
| `endpoints_arb.py` | Certified crossovers, Z at t0, 1/M1 |
| `extra.py` | 53.989 vs 21.432 crossover; window ratio; monotonicity of Z |
| `ford.py`, `ford_pub_check.py`, `ford_repair.py`, `ford_repair2.py` | Ford X-substitution recomputation (mpmath, non-rigorous) |

**Sources** (`/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/`):

| Source | Path or hash |
|---|---|
| Yang e-prints | `l2/adjf3_v1/` and `l2/adjf3_v2/` |
| Thesis text | `fulltext/url/yang_thesis_pdf/text.txt` |
| Ford v1 | sha256 `cf695a47…` |
| Ford v4 | sha256 `06d70624…` |
| Ford v5 | sha256 `df92c2e7…` |
| MTY | sha256 `127c32eb…` |


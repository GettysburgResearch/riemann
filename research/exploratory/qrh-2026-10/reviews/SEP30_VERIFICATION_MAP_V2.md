# Verification-status map v2 of the 30 Sep 2026 OpenAI 7/8 manuscript

```text
Status: EXPLORATORY (verification bookkeeping). This is not a review verdict on any lemma, not an
  integration record, and not a statement that the 7/8 theorem holds. It collates the verdicts of
  the bounded agent reviews written since v1, recounts the load-bearing graph, and ranks what is
  left. v1 (SEP30_VERIFICATION_MAP.md, sha256 657696c2a661...) is unchanged and remains the record
  of the earlier state.
Scope: the logical dependency graph of [OAI] Theorem 1.1 (zero-free half-plane Re s > 7/8 for
  finite-order Hecke L-functions over Q(sqrt(-3)) and all Dirichlet L-functions), at the level of
  the 65 load-bearing numbered results and the load-bearing prose blocks of v1. Two graphs: (a) the
  manuscript as written; (b) the "Oct 5 substitution" of PART1_SUBSTITUTION.md, in which [O5]
  thm:main replaces Thm 3.1 in the Part II bootstrap.
Exact sources or dependencies:
  [OAI] paper.tex at pr908 (31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6), standalone/2026-10-07-openai-
        quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/
        paper.tex, SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3
        (re-hashed: the git object and the scratch copy agree). External and unreviewed; untrusted data.
  [O5]  paper2.tex at the same ref, SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d.
  Review files read (branch claude/peaceful-faraday-ki4ewu at e606784e; sha256 prefixes), headers,
        verdict sections and status-consequence sections in each:
        reviews/SEP30_REFLECTION_DIFF.md 272fa8d692a6; SEP30_LOWSIDE_REVIEW.md 670cdaac5545;
        SEP30_INVMOMENT_REVIEW.md 6f9d08a44dbc; SEP30_EQC_CHECK.md 951109973e02;
        SEP30_L17_IDENTITIES.md 1a7b17955227; LEMMA18_1_REVIEW.md 840aa73ce90a;
        LEMMA18_1_COMMON_SUPPORT.md 0f2b54fc428e; LEMMA18_1_CASE2_SEC188.md 446e0604979e;
        SEP30_JUNCTION_CHECK.md fa8fd49800ed; SEP30_DETECTOR_QUANTIFIERS.md 1388e8985105;
        SEP30_L13_L45_REVIEW.md 0ef92082035a; SEP30_SEC4_REVIEW.md 16c7fa707e3e;
        PART1_SUBSTITUTION.md 3a8d4c286b26; CONTOUR_LEMMAS_BELOW_7_8.md 2230d06b482f;
        PR910_REPLAY.md 877ee965e12a; numerics/COEFF74_CHECK.md 1dba4cca97f4;
        also OCT5_REVIEW_SUMMARY.md a3d6d84bcdc5 and LEAN_BUILD_ATTEMPT.md 02a6fd6a98dc (headers).
  reviews/SEP30_MISC_REVIEW.md: not present at the time of writing; nothing from it is counted.
        Its check script sep30_misc_checks.py (untracked, in progress) targets Lemma 17.1's
        initialization transform, Lemma 15.1, Lemma 20.1, Prop 2.1 and Thm 1.1's final step.
What was actually run:
  - reviews/sep30_depgraph_v2.py (finished here from a partial script left by an interrupted
    agent; final SHA-256 633bbe2dfbb1907be87fb2bfceb8bb277c77b0052f66b73a466f91b638b1ec87), as
    `python3 -I sep30_depgraph_v2.py paper.tex out.json table.md` and with `python3 -I -O`.
    Both runs exit 0 and give byte-identical stdout (05ace36e...f6797), JSON (9aba2acd...47dc) and
    node table (9b33ee98...e7b7). The table in Sec. 3 is that generated file, pasted unchanged.
    The graph logic is v1's (sep30_depgraph.py, ac667abf...e459) plus one manual edge
    (Lemma 5.7 -> Def 5.6) and the substitution graph. Statuses and evidence strings are
    entered by hand from the review files; the script only counts, ranks and sums owned lines.
  - Reading: the header and verdict of every file listed above; for PART1_SUBSTITUTION,
    SEP30_DETECTOR_QUANTIFIERS, LEMMA18_1_CASE2_SEC188 Sec. 4 and 6, SEP30_L13_L45_REVIEW Sec. 4
    and 6, and SEP30_SEC4_REVIEW Sec. 0 and 7-9, the full verdict text. No manuscript proof was
    re-derived here, and no review was redone.
Smallest remaining gap: with the substitution, no load-bearing numbered node is unreviewed (U = 0),
  but four have arithmetic or numerical checks only (A): Lemma 17.1 (the marked inverse moment,
  a claimed new estimate) and the Gauss-sum/reciprocity helpers Lemmas 4.2, 4.3 and 4.4. The
  smallest statement whose failure would most likely move 7/8 is inside the marked inverse-moment
  engine: the Lemma 17.1 initialization transform (11606-12271; ledger PASS, no identity replay)
  together with Lemma 17.2's two Fourier separations and common-density moment bound (10538,
  11209, 11247; read, not replayed).
  Three of the R verdicts (Lemmas 4.1, 4.6, 13.1) come from SEP30_SEC4_REVIEW.md, whose committed
  text still carries output placeholders; see Sec. 2.3.
```

RH is unsolved. This file is about an external, unreviewed proof of a quasi-RH statement (`Re s > 7/8`), which says nothing about the critical line. "Reviewed" below always means a *bounded agent review* with the stated scope, by agents of a single model family. It never means certified, integrated, human-refereed or independently reviewed.

## 0. Summary

* **As written (65 load-bearing numbered nodes).** R 43, R-partial 5, I 5, A 7, U 5. In v1 the same nodes were R 11, I 8, A 10, U 36.
* **With the Oct 5 substitution (57 Sep 30 nodes + the imported [O5] thm:main).** R 43, R-partial 5, I 5, A 4, U 0. Eight Part I nodes have the status **L** ("leaves path via the Oct 5 substitution").
* **Line-weighted, with the substitution.** Of the 11,134 lines owned by the 57 numbered nodes (statements plus proofs), 62.2% sit in nodes with a whole-node bounded verdict of "no wrong step found", and 87.1% if partial verdicts are included.
* **No bounded review has reported a wrong step** in any load-bearing node. The non-fatal findings are in Sec. 7.
* **What this does not mean** is spelled out in Sec. 6. In short, these are bounded reviews by agents of one model family. They are not independent, not human, not an integration verdict, and not evidence about RH.

## 1. What changed since v1

1. **New reviews.** Twelve review notes and one numerics note have been written since v1. Together they cover the five v1 targets and most of v1's "Next after these" list:
   * reflection engine: SEP30_REFLECTION_DIFF;
   * low side: SEP30_LOWSIDE_REVIEW;
   * Section 17: SEP30_INVMOMENT_REVIEW, SEP30_EQC_CHECK and SEP30_L17_IDENTITIES;
   * Lemma 18.1: LEMMA18_1_COMMON_SUPPORT and LEMMA18_1_CASE2_SEC188;
   * junction: SEP30_JUNCTION_CHECK;
   * detector, Prop 16.1 and Prop 20.3: SEP30_DETECTOR_QUANTIFIERS;
   * Lemmas 13.2-13.4 and 4.5: SEP30_L13_L45_REVIEW;
   * Section 4 helpers: SEP30_SEC4_REVIEW;
   * Part I replacement and Lemmas 11.1, 19.1: PART1_SUBSTITUTION;
   * Sec. 7.2 factorization: numerics/COEFF74_CHECK.
2. **Correction to v1: Def 5.6 is directly load-bearing.** Lemma 5.7's statement is phrased in Def 5.6's terms, and Lemma 14.3 uses Lemma 5.7 (PART1_SUBSTITUTION §3.2). The v1 script missed this verbal edge. So 8 nodes, not 9, are used only through Thm 3.1, and 8 leave with the substitution.
3. **A finer code for partial reviews.** v1 counted three partial reviews as R (Lemmas 7.1, 15.1, 20.2). v2 keeps **R** for a whole-node verdict and adds **Rp** (R-partial). Rp means bounded-review verdicts that cover named parts of a node, while other named parts were only read or numerically checked. Lemma 20.2 stays R: it is a pure inequality, mechanically certified. Lemmas 7.1 and 15.1 move from R to Rp. No problem was found in either; the change only makes the bookkeeping explicit. For the four-code counts that were asked for, Rp is a sub-case of R and is shown separately.
4. **Lemma 18.1 is now covered line by line.** v1 recorded its verdict as "cannot tell". LEMMA18_1_CASE2_SEC188 §6 states that the three notes together read every proof line (12602-14984) and found no wrong step. That covers Lemmas 18.2 and 18.3, which lie inside the proof.
5. **Cor 14.1's conditional input is discharged.** LOWSIDE made Cor 14.1 conditional on Prop 5.1's branch-compatibility clause. SEP30_REFLECTION_DIFF R-e reviewed that clause (1843-1850, 2252-2262), with 143 numerical branch identities (error 9.6e-15). The two notes were written in parallel and neither cites the other.

## 2. Counts

### 2.1 Numbered nodes

| | R | Rp | I | A | U | L | total on path |
|---|---|---|---|---|---|---|---|
| v1 (as written) | 11 | – | 8 | 10 | 36 | – | 65 |
| v2, as written: direct | 43 | 5 | 5 | 4 | 0 | – | 57 |
| v2, as written: via Thm 3.1 only | 0 | 0 | 0 | 3 | 5 | – | 8 |
| **v2, as written: total** | **43** | **5** | **5** | **7** | **5** | – | **65** |
| **v2, with the Oct 5 substitution** | **43** | **5** | **5** | **4** | **0** | **8** | **57** + [O5] thm:main |

* **Reviewed or inspected (R + Rp + I).**
  * As written: 53 of 65. In v1 it was 19 of 65.
  * With the substitution: 53 of 57.
* **Without a bounded review (A + U).**
  * As written: 12 (7 A and 5 U). All 5 U are Part-I-only.
  * With the substitution: 4, all A: Lemmas 4.2, 4.3, 4.4 and 17.1.
* **The eight L nodes.** Thm 3.1 (A), Lemma 5.8 (U), Lemma 6.1 (U), Lemma 6.2 (U), Prop 6.3 (A), Lemma 9.1 (U), Prop 9.2 (U) and Prop 11.2 (A). Their proofs are not reviewed. They stop being load-bearing only under the substitution, which is a new composition (Sec. 6).
* **The imported node.** With the substitution, [O5] thm:main enters as an imported theorem. Bounded reviews R1, R2 and R3 read every proof line of its source and found no wrong step (OCT5_REVIEW_SUMMARY). It is counted separately, not as a Sep 30 node.

### 2.2 Owned lines (statement plus proof, numbered nodes only)

| | total | R | Rp | I | A | U |
|---|---:|---:|---:|---:|---:|---:|
| as written | 12,366 | 6,930 (56.0%) | 2,770 (22.4%) | 399 (3.2%) | 1,229 (9.9%) | 1,038 (8.4%) |
| with the substitution | 11,134 | 6,930 (62.2%) | 2,770 (24.9%) | 399 (3.6%) | 1,035 (9.3%) | 0 |

* **Two nodes dominate the totals.**
  * Lemma 18.1 owns 2,276 lines, and its whole proof is R.
  * Lemma 17.2 owns 1,856 lines and is Rp.
  * Lemma 17.1 owns 756 of the 1,035 A lines.
* **Prose is not in these totals.** The load-bearing prose that the graph reaches by `\ref` adds about 2,870 more lines with the substitution, in 39 subsection-level blocks. That count is coarse, since a block is a whole subsection. Its status is in Sec. 3a only for the blocks v1 tracked.

### 2.3 Sensitivity: the Section 4 review is not finalized

SEP30_SEC4_REVIEW.md gives written verdicts ("no wrong step found") for Lemmas 4.1, 4.6, 4.7, 4.8, 4.9, 4.10 and 13.1. Its committed text, however, still contains `RUNTIME_PLACEHOLDER`, `D3_TABLE_PLACEHOLDER`, `G_TABLE_PLACEHOLDER` and `OUTPUT_PLACEHOLDER`. The session scratchpad log `sec4/full.log` ends "ALL PASS, total 1252s", but that log is not committed.

* Lemmas 4.7-4.10 are also covered by SEP30_L13_L45_REVIEW, so they stay R either way.
* Lemmas 4.1, 4.6 and 13.1 depend on SEC4 alone. If SEC4 were withdrawn, the counts would be:
  * as written: R 40, Rp 5, I 5, A 7, U 8;
  * with the substitution: R 40, Rp 5, I 5, A 4, U 3;
  * R line share with the substitution: 61.0% instead of 62.2%.

## 3. Node table

**Status codes.**
* **R.** A bounded review with a written whole-node verdict ("no wrong step found", "no gap found" or "correct") at this exact source.
* **Rp.** Bounded-review verdicts on named parts. The remaining named parts were only read or numerically checked.
* **I.** Inspected or read, with no defect identified, but not line-checked.
* **A.** Arithmetic, symbolic or numerical checks only.
* **U.** No check found.
* **L.** Leaves the 7/8 critical path via the Oct 5 substitution: [O5] thm:main supplies `β* ≤ 11/12` through bridge B of PART1_SUBSTITUTION §2.3. The node's own status is in the "v2 as written" column.

**Columns.**
* **ndep.** The number of load-bearing numbered results that depend on the node transitively, in the graph as written and in the substitution graph.
* **Evidence.** It uses the abbreviations defined in the script:
  * DIFF = SEP30_REFLECTION_DIFF, LOW = SEP30_LOWSIDE_REVIEW and INV = SEP30_INVMOMENT_REVIEW;
  * EQC = SEP30_EQC_CHECK and L17 = SEP30_L17_IDENTITIES;
  * L18a, L18b and L18c = LEMMA18_1_REVIEW, _COMMON_SUPPORT and _CASE2_SEC188;
  * JUNC = SEP30_JUNCTION_CHECK, DET = SEP30_DETECTOR_QUANTIFIERS, L13 = SEP30_L13_L45_REVIEW and SEC4 = SEP30_SEC4_REVIEW;
  * SUB = PART1_SUBSTITUTION, CONT = CONTOUR_LEMMAS_BELOW_7_8 and P910 = PR910_REPLAY;
  * C74 = numerics/COEFF74_CHECK, and MAP1 = v1's evidence column, carried over.

Cor 1.2 and Remark 19.3 are not load-bearing, as in v1.

| Node | Title | TeX (statement; proof) | own lines | ndep (as written / O5) | v1 | v2 as written | v2 with O5 | Evidence |
|---|---|---|---:|---|---|---|---|---|
| Thm 1.1 | Main theorem (7/8) | 106-111; 16454-16463 (prose) | 16 | 0 / 0 | I | I | I | MAP1 (PR 908 audit §3.1, inspection). Final paragraph 16454-16463 not line-checked. |
| Prop 2.1 | Continuation from a common signal | 400-432; 434-502 | 102 | 18 / 16 | I | I | I | MAP1 (PR 908 §3.1). DET §6.1 uses its pretarget requirement only. Proof not line-checked. |
| Thm 3.1 | The $11/12$ half-plane | 532-537; 6783-6805 | 29 | 8 / - | A | A | **L** | MAP1 ledger only. Leaves with the substitution (SUB §3.1). |
| Lem 4.1 | Fixed numerators give ray characters | 646-674; 676-699 | 53 | 29 / 25 | U | R | R | SEC4 §1: no wrong step; A1-A4 exact (conductors, S-family). |
| Lem 4.2 | Prime Gauss identities | 766-775; 777-836 | 70 | 32 / 26 | A | A | A | MAP1 numerics (w5copg, PR 908). Proof unreviewed. |
| Lem 4.3 | Quadratic four-term formula | 841-869; 871-932 | 91 | 33 / 27 | A | A | A | MAP1 numerics K1/K2''. C74 uses the four-term Gamma (agrees 1.4e-14). Proof unreviewed. |
| Lem 4.4 | Sextic reciprocity and the fixed Gauss phase | 934-972; 974-1052 | 118 | 31 / 25 | A | A | A | MAP1 numerics K2',K3,K4; L13 A5; L18b B4. Proof unreviewed. |
| Lem 4.5 | Smooth calculus | 1123-1210; 1212-1286 | 163 | 40 / 35 | U | R | R | L13: no wrong step (line by line). |
| Lem 4.6 | Gaussian annular decomposition | 1288-1315; 1317-1340 | 52 | 25 / 21 | U | R | R | SEC4 §2: no wrong step; B1-B4. |
| Lem 4.7 | Finite seminorms for Fourier and Mellin kernels | 1347-1389; 1391-1413 | 66 | 11 / 11 | U | R | R | L13 (as used) + SEC4 §3: no wrong step. |
| Lem 4.8 | Hecke strip growth | 1425-1434; 1436-1529 | 104 | 24 / 21 | U | R | R | SEC4 §4: no wrong step (constant C ~ 0.69); L13 as used. |
| Lem 4.9 | Logarithmic control | 1531-1552; 1554-1600 | 69 | 23 / 20 | U | R | R | SEC4 §5 + L13: no wrong step (constants ineffective, harmless). |
| Lem 4.10 | Deleted Euler factors | 1602-1621; 1623-1646 | 44 | 17 / 15 | U | R | R | SEC4 §6 + L13: no wrong step. |
| Prop 5.1 | Completed cubic reflection | 1676-1881; 1883-2462 | 786 | 30 / 26 | U | R | R | DIFF: arithmetic core = R3-reviewed Oct 5 appendix proof; remainder R-a..R-g; PL/contour by reading. |
| Lem 5.2 | Fixed ray sectors for nonzero rows | 2470-2506; 2508-2532 | 62 | 25 / 14 | U | R | R | DIFF §4.2: no error. |
| Lem 5.3 | Common annular kernel profile | 2540-2566; 2568-2578 | 38 | 25 / 21 | U | R | R | DIFF §4.3: no error. |
| Lem 5.4 | Lattice kernel tails | 2618-2628; 2630-2636 | 18 | 24 / 20 | U | R | R | DIFF §4.3: no error. |
| Lem 5.5 | Quadratic reduction for completed indices | 2680-2729; 2731-2813 | 133 | 26 / 22 | U | R | R | DIFF §3.2 (new vs Oct 5), check Q: no error. |
| Def 5.6 | An unmarked reflected block | 2888-2950; no proof (definition) | 63 | 25 / 21 | U | I | I | Definition; read in DIFF scope. Direct via Lemma 5.7 (SUB §3.2). |
| Lem 5.7 | Unmarked reflected block | 2956-3001; 3003-3076 | 120 | 24 / 20 | U | R | R | DIFF §3.3, check U: no error. |
| Lem 5.8 | Unmarked completed-row moment | 3138-3168; 3170-3285 | 147 | 23 / - | U | U | **L** | Unreviewed. Leaves with the substitution. |
| Lem 6.1 | Planar additive large sieve | 3497-3514; 3516-3580 | 83 | 14 / - | U | U | **L** | Unreviewed. Leaves with the substitution. |
| Lem 6.2 | The balanced additive norm | 3587-3602; 3604-3666 | 79 | 11 / - | U | U | **L** | Unreviewed. Leaves with the substitution. |
| Prop 6.3 | Balanced low estimate | 3672-3682; 3684-3721 | 49 | 10 / - | A | A | **L** | MAP1 ledger only. Leaves with the substitution. |
| Lem 7.1 | The complete local identity | 4010-4067; 4073-4189 | 175 | 17 / 14 | R | Rp | Rp | MAP1 numerics L1-L5, CONT tables; DET region one; C74 (7.4)->(7.10) on 166,144 tuples (FLOAT). (7.5) analytic not checked. |
| Lem 8.1 | Buffered zero-free bins | 4281-4322; 4324-4368 | 87 | 17 / 11 | U | R | R | DET §1: no gap found. |
| Lem 8.2 | Pointwise dyadic estimates | 4385-4417; 4419-4498 | 113 | 14 / 8 | U | R | R | DET §2: no gap found. |
| Prop 8.3 | Two saturated witnesses | 4510-4547; 4549-4685 | 175 | 11 / 5 | U | R | R | DET §3: no gap found. |
| Lem 9.1 | Sextic large sieve | 4707-4725; 4727-5171 | 464 | 11 / - | U | U | **L** | Unreviewed. Leaves with the substitution. |
| Prop 9.2 | Sextic-sieve row envelope | 5181-5213; 5215-5446 | 265 | 10 / - | U | U | **L** | Unreviewed. Leaves with the substitution. |
| Def 10.1 | Data for an exact high representation | 5582-5650; no proof (definition) | 69 | 14 / 10 | R | R | R | CONT: no gap. |
| Lem 10.2 | External integrated and trace tails | 5672-5711; 5713-5728 | 56 | 14 / 8 | R | R | R | CONT: no gap. |
| Lem 10.3 | Contour transformation for a fixed bin | 5808-5834; 5836-5896 | 88 | 11 / 5 | R | R | R | CONT: no gap. |
| Lem 10.4 | A retained integral and its exponent | 6021-6115; 6117-6155 | 134 | 4 / 4 | R | R | R | CONT + P910: no gap. |
| Lem 10.5 | Extraction of the principal signal | 6174-6222; 6224-6301 | 127 | 3 / 3 | R | R | R | CONT: no gap. |
| Lem 10.6 | Outer row norms | 6342-6401; 6403-6463 | 121 | 2 / 2 | R | R | R | CONT: no gap. |
| Lem 11.1 | Late choice of height and external order | 6520-6558; 6560-6580 | 60 | 10 / 5 | U | R | R | SUB §4: no wrong step. |
| Prop 11.2 | Balanced high estimate | 6582-6592; 6594-6698 | 116 | 9 / - | A | A | **L** | MAP1 ledger only. Leaves with the substitution. |
| Prop 11.3 | Quadratic transfer | 6705-6713; 6715-6781 | 76 | 9 / 1 | I | I | I | MAP1 (PR 908 §2.4 read). |
| Lem 13.1 | Fixed-ray prime normalizer | 7006-7017; 7019-7040 | 34 | 2 / 2 | U | R | R | SEC4 §7: no wrong step; G0-G1 EMPIRICAL. |
| Lem 13.2 | Prime-power Fourier sums | 7055-7065; 7067-7079 | 24 | 8 / 8 | A | R | R | L13 §3: correct; D2 exact. |
| Lem 13.3 | Full correlation and common factors | 7081-7132; 7134-7190 | 109 | 13 / 13 | U | R | R | L13 §1: no wrong step (A, B exact); LOW brute force. |
| Lem 13.4 | Complete-common-support correlation | 7196-7210; 7212-7229 | 33 | 8 / 8 | U | R | R | L13 §2: no wrong step (C1 exact). |
| Cor 14.1 | Completed reflection with whole-index marks | 7361-7415; 7417-7441 | 80 | 13 / 13 | U | R | R | LOW: no wrong step, given Prop 5.1 branch compatibility (DIFF R-e). |
| Lem 14.2 | A quadratic--cubic norm bound | 7510-7540; 7542-7655 | 145 | 13 / 13 | U | R | R | LOW: no wrong step. |
| Lem 14.3 | Reflected energy | 7747-7804; 7806-7993 | 246 | 12 / 12 | A | R | R | LOW: no wrong step. |
| Lem 15.1 | The compensated completed-row norm | 8111-8122; 8124-8332 | 221 | 7 / 7 | R | Rp | Rp | PR 910 REVIEW §1.1 + P910 + LOW (exponents). Analytic transfer not re-proved. |
| Prop 15.2 | A quantitative additive Gram bound | 8340-8361; 8363-8557 | 217 | 7 / 7 | U | R | R | LOW: no wrong step. |
| Prop 15.3 | The compensated low estimate | 8564-8576; 8578-8649 | 85 | 6 / 6 | A | R | R | LOW: no wrong step; zero excess at d = 0. |
| Prop 16.1 | Dynamic local errors and conductor allocation | 8852-8905; 8907-9049 | 197 | 4 / 4 | I | R | R | DET §5: no gap; geometry-free. Ray presentation rests on Lemma 4.4. |
| Lem 16.2 | Absolute local tuple bounds | 9101-9131; 9133-9196 | 95 | 2 / 2 | R | R | R | CONT + P910. |
| Lem 17.1 | Marked inverse moment | 9250-9269; 11606-12341 | 756 | 6 / 6 | U | A | A | INV: statement diff + initialization ledger PASS. Initialization transform not replayed (L17). |
| Lem 17.2 | Canonical marked estimate | 9296-9340; 9789-11599 | 1856 | 7 / 7 | U | Rp | Rp | INV ledgers, EQC eq. (C), L17 identities 1-10. Fourier separations (10538, 11209, 11247) read only. |
| Lem 17.3 | Finite seminorm propagation | 9366-9441; 9443-9484 | 118 | 9 / 9 | U | R | R | L17 §1.2: correct. |
| Cor 17.4 | Indexed finite propagation | 9486-9531; 9533-9550 | 64 | 8 / 8 | U | R | R | L17 §1.2: correct. |
| Lem 17.5 | Masked primitive Poisson | 9722-9743; 9745-9781 | 59 | 8 / 8 | U | R | R | L17 §1.2: correct. |
| Lem 17.6 | Sixth-power amplification | 12362-12389; 12391-12469 | 107 | 5 / 5 | U | R | R | L17 §1.2: correct (given Lemma 4.5). |
| Lem 18.1 | Fourth moment with short prime factors | 12531-12579; 12580-14984 (prose) | 2276 | 7 / 7 | R | R | R | L18a + L18b + L18c: every proof line read, no wrong step. |
| Lem 18.2 | Common coefficient under complete extraction | 13953-13981; 13983-13996 | 43 | 7 / 7 | I | R | R | Inside L18 coverage (coefficient lemma; L18c §6). |
| Lem 18.3 | Masked rectangle cancellation | 14545-14596; 14598-14680 | 135 | 7 / 7 | I | R | R | Inside L18 coverage (Theta rows, lattice cancellation; L18c §6). |
| Lem 19.1 | Prime bound in a bin | 15015-15025; 15027-15062 | 47 | 4 / 4 | U | R | R | SUB §5: no wrong step; JUNC hypothesis instance. |
| Prop 19.2 | Row counts from the witnesses | 15185-15220; 15222-15446 | 261 | 4 / 4 | A | Rp | Rp | JUNC (84 exact gates) + L18c §4 interface. Qualitative row-dependent-test clause in prose only. |
| Lem 20.1 | A high exponent for one row bin | 15699-15757; 15759-15841 | 142 | 3 / 3 | I | I | I | CONT read; DET §5 consumption exact; P910; ledger. |
| Lem 20.2 | Compensated endpoint certificate | 15994-16004; 16006-16072 | 78 | 2 / 2 | R | R | R | Certified: PR 908, P910, JUNC E8-E9. |
| Prop 20.3 | Order of choices | 16196-16217; 16219-16453 | 257 | 1 / 1 | I | Rp | Rp | DET §6: order admissible. I2, I10, I12 rest on proofs outside its scope. |

### 3a. Load-bearing prose blocks

| Block | Lines | v1 | v2 | Evidence |
|---|---|---|---|---|
| Sec 7.1 exact Poisson series | 3734-3846 | U | A | C74 P1 (the Fourier claim in (7.1), 4,284 cases) and P2 (vanishing unless `(H,S)=1`), FLOAT. The analytic Poisson/Mellin identity (7.5), with its prefactor and interchanges, is not checked. |
| Sec 7.2 scalar Euler identity | 3847-4009 | A | A | C74 closes v1's "(7.4) → (7.10) factorization unchecked" at the finite level: 166,144 tuples, max deviation 7.1e-13 on nonzero tuples, FLOAT. Not covered: the r = 1 rows of three t > 0 families of table (7.16), and `k = v_p(s) = 3`. |
| eq:actual-residual-row-dyad | 3130 (Sec 5 prose) | (not tracked) | I | Read as invoked by LOW. SUB §3.2 shows it is directly load-bearing. |
| Sec 6.1 probe definitions (eq:general-probe, eq:low-separated) | 3349-3480 | (not tracked) | I | Read as inputs by LOW. Directly load-bearing (SUB §3.2). |
| `𝒳_u` consists of finite-order characters | 4222-4268, 4374-4376 | (not tracked) | R | SUB §1.4; DET §1 (rows 4229-4268). |
| Sec 10.1 principal data, (10.1)-(10.2) | 5500-5557 | R | R | CONT. |
| Sec 10.5 "Applying the row envelope" | 5905-6012 | (Part I) | **L** | SUB §3.1. |
| Sec 12 compensated probe + bootstrap | 6810-6917 | I/A | I; bootstrap sentence 6812-6814 → bridge B (R) under the substitution | Read by LOW and DET; ledger geometry identities. SUB §2.3 checks bridge B. |
| Sec 14 completed moment | 7995-8056 | (not tracked) | R | LOW (unmarked case only, as stated). |
| Sec 16.1 full holomorphic correction | 8667-8799 | I | I | DET read 8640-9060 line by line, for Prop 16.1; CONT checked the region obligations. |
| Sec 19.2 selection prose | 15095-15184 | A | Rp | JUNC: every quantitative hypothesis instance holds exactly. L18c §4: the Lemma 18.1 interface is consistent. Open: the qualitative clauses at 15134-15170, namely row-dependent witness profiles through Lemma 4.5, the R_z family condition, and the Theta-combination slot coefficients. |
| Sec 20.1 principal normalizer | 15548-15683 | R | R | CONT; SEC4 §7 re-derived the `A_T(Z)` asymptotic. |
| Sec 20.3 small and large rows | 15853-15919 | A | I | DET read it as an order-of-choices input and re-ran `m_small`, `z_inf` and the intermediate rows. |
| Sec 20.4 endpoint inequality | 15920-15993, 16073-16111 | A | Rp | JUNC: the Δ/4 comparison is correct, with slack ≥ (83/972)Δ, so w5copg's flag is resolved; the endpoint identities are exact (I17, I18, E11). DET §6.4(iii): the no-slot endpoint estimate itself was not re-derived. |
| Sec 20.5 frequency ranges | 16112-16188 | A | I | JUNC Q1-Q3 (supply margins 23/1443 and 2/185, mesh); DET re-ran `h+ζ < 5ℓ ⇔ ζ < 1/48`. |
| Thm 1.1 final paragraph | 16454-16463 | I | I | Counted inside node 1.1. |

## 4. Remaining U/A load-bearing nodes, ranked

### 4.1 Script score (v1 rubric, unchanged)

The score is (length + novelty + numerology slack) × sqrt(1 + ndep), computed in the substitution graph.

| Rank | Node | Status | L+N+S | ndep | owned lines | Score |
|---:|---|---|---|---:|---:|---:|
| 1= | Lemma 4.3 quadratic four-term formula | A | 1+2+1 | 27 | 91 | 21.2 |
| 1= | Lemma 17.1 marked inverse moment | A | 3+3+2 | 6 | 756 | 21.2 |
| 3 | Lemma 4.4 sextic reciprocity, fixed Gauss phase | A | 1+2+1 | 25 | 118 | 20.4 |
| 4 | Lemma 4.2 prime Gauss identities | A | 1+1+1 | 26 | 70 | 15.6 |

The residual nodes (Rp and I) in the substitution graph rank as follows:

| Node | Status | Score |
|---|---|---:|
| Lemma 17.2 | Rp | 22.6 |
| Lemma 15.1 | Rp | 19.8 |
| Lemma 7.1 | Rp | 19.4 |
| Def 5.6 | I | 18.8 |
| Prop 19.2 | Rp | 17.9 |
| Prop 2.1 | I | 16.5 |
| Lemma 20.1 | I | 10.0 |
| Prop 20.3 | Rp | 8.5 |
| Prop 11.3 | I | 4.2 |
| Thm 1.1 | I | 3.0 |

As v1 noted, this score over-rewards deep standard helpers.

### 4.2 Judgement ranking: what would most likely move 7/8 if it failed

1. **The marked inverse-moment engine: Lemma 17.1 (A), together with the open parts of Lemma 17.2 (Rp).**
   * *Why it ranks first.* It is a claimed new mean-value estimate. The marked case `z_0 > 0` used by Prop 19.2 rests entirely on the new recursion. INV §1 found that this recursion is not a normalized form of the R2-reviewed Oct 5 descent, so no Oct 5 verdict transfers to it.
   * *What is checked.*
     * Every ledger (INV, 120 checks, with tight constants).
     * Eq. (C) (EQC).
     * All 11 new arithmetic identities: 10 verified and 1 partial (L17).
     * Lemmas 17.3-17.6 (L17).
   * *What is not checked.*
     * The Lemma 17.1 initialization transform, 11606-12271: ledger PASS, but no identity replay.
     * The two Fourier separations and the common-density moment bound (10538, 11209, 11247): read only.
     * The extension of Lemma 17.1 to row-dependent test parameters, which is asserted only inside Lemma 17.6's proof (12466-12468, JUNC).
   * *Slack.* The supply margin is `8/39 − 7/37 = 23/1443`.
2. **Lemma 4.4, sextic reciprocity and the fixed Gauss phase (A; 25 dependents).**
   * *Where it is load-bearing.*
     * The bicharacter `R(n1,n2)` in Lemmas 13.3 and 13.4.
     * The conductor bound `Q_ψ ≪ q_u` in Lemma 8.1, which DET accepted without re-deriving.
     * The ray presentation in Prop 16.1 (8985-8998), which SEC4 flags as going beyond Lemma 4.1.
     * Lemma 5.2 and the CRT steps of Section 17.
   * *Checks.* Exact on large finite sets: 342,684 pairs (v1), 3,298 pairs (L18b B4), and the reciprocity factor inside 2,631,375 exact correlation values (L13 A1, A5).
   * *Gap.* The proof (974-1052) has not been read by any review. The content is standard reciprocity, adapted, and about 120 lines, so a review is cheap.
3. **Lemmas 4.2 and 4.3, prime Gauss identities and the quadratic four-term formula (A; 26-27 dependents).**
   * Both are exact on large finite tables, and C74 uses the four-term Γ, agreeing with direct sums to 1.4e-14.
   * Neither proof has been read. Both are standard and short (about 160 lines together).
4. **Lemma 7.1 with Sec. 7.1-7.2 (Rp, A, A).**
   * The analytic Poisson/Mellin identity (7.5) is unchecked.
   * The local identity is checked only in finitely many local cases, and not for `k = 3` or the `r = 1` rows of three `t > 0` families.
   * This is the high-side identity of the probe.
5. **Prop 19.2 (Rp) and the qualitative hypothesis transfer.**
   * JUNC's first unverified step is qualitative. Lemma 18.1's statement has no rowwise-test clause, and the prose supplies one through Lemma 4.5 at 15163-15167. Lemma 4.5 is now R, but its invocation uniformity was not checked (item 8 below).
   * Lemma 18.1 is invoked exactly on its boundary (`n1+n2+6κz = M`, `β* = (1+κ)/2`). This is permitted by the non-strict statement.
6. **Lemma 15.1 (Rp).** The low exponent `3/16` is attained with zero excess at `d = 0` (LOW). The row proof was re-derived by PR 910 and re-checked at exponent level, but its analytic transfer has not been re-proved in this wave.
7. **Prop 20.3 (Rp).** The order of choices is admissible (DET), but four independence claims are load-bearing:
   * I1 (the Lemma 18.1 mesh is independent of the slot count) is consistent per L18c §4;
   * I2 (moment-loss coefficients are K-free), I10 (moment losses are target-independent) and I12 (the mesh is independent of the arithmetic datum) rest on proofs outside DET's scope.
8. **Cross-cutting: invocation uniformity of Lemma 4.5 (R; 35 dependents).**
   * L13 reviewed the lemma itself. It left open whether each of its users applies it inside its hypotheses with the claimed uniformity (L13 "Smallest remaining gap" (i)).
   * The downstream reviews (L18c, L17, DIFF, JUNC) used it as a black box.
   * So the composition "Lemma 4.5 as stated ⇒ its 35 uses" has no single owner.
9. **Prop 2.1 (I; 16 dependents) and the I-only tail.**
   * Prop 2.1 has had only inspection plus Oct 5 analog reviews. It is a standard Mellin contradiction, with a Lean name pointer.
   * The other I nodes are low-risk: Lemma 20.1 (consumption checked exactly by DET), Def 5.6 (a definition), Prop 11.3 (standard base change) and Thm 1.1's 10-line final paragraph.

**In progress, not counted.** The check script of a pending SEP30_MISC_REVIEW.md targets items 1 (the Lemma 17.1 initialization transform, with an end-to-end replay), 6 and 9 (Lemma 15.1, Lemma 20.1, Prop 2.1 and the final contradiction of Thm 1.1). Its verdicts should be folded in by a v3 once that review is written.

**Outside the Sep 30 text: [O5] thm:main**, which the substitution imports. Its smallest failure point is `prop:R`, and the risk is correlated with Prop 5.1 (Sec. 5).

## 5. Remaining imported external theorems

With the substitution, **Blomer-Goldmakher-Louvel** (Lemma 9.1) and **Huxley / Baier-Bansal** (Lemma 6.1) leave the path. The following remain.

| Import | Load-bearing use | What was checked |
|---|---|---|
| **[O5] thm:main** (Oct 5 manuscript, 11/12) | bootstrap `β* ≤ 11/12` via bridge B (only under the substitution) | External and unreviewed manuscript. Agent reviews R1+R2+R3, the residual items and an end-to-end numerical test of eq:reflection read every proof line and found no wrong step (OCT5_REVIEW_SUMMARY). There is no independent or human review. Its weakest point is `prop:R`, which is the same reflection mechanism and theta data as [OAI] Prop 5.1 (SUB §3.3): correlated risk. |
| **Kubota-Patterson cubic theta; Dunn-Radziwiłł** unconditional cusp expansions (arXiv 2109.07463v3) | Prop 5.1 (and through it Cor 14.1 and Lemmas 5.2-5.7, 14.3, 17.2); also [O5] | Quoted correctly; expansions checked numerically to 5e-15 (R3); coefficient support and size checked from the DR transcription (DIFF check D). The "[DR, Lemma 5.3]" Bessel citation was not checked (DIFF §6). |
| **Goldmakher-Louvel** quadratic large sieve over Q(ω) (arXiv 1112.1642, Thm 1.1) | eq:quadratic-large-sieve → Lemma 5.5 → Lemmas 5.7, 14.2, 14.3; also [O5] | Read in full (OCT5_RESIDUAL_ITEMS). Its family hypotheses match in both texts (DIFF §3.1, LOW). Its estimates were not re-derived. |
| **Heath-Brown** cubic large sieve (Israel J. Math. 120 (2000), Thm 2) | Lemma 14.2 | The original was not re-read. Its statement was checked against DR's verbatim restatement (LOW). |
| **Thorner-Zaman** Chebotarev (ANT 13 (2019), Thm 1.1) | Lemma 13.1 (Sec. 20.1 normalizer), Lemma 18.1 (amplifier pool size), Sec. 10.1 | Used only at Hecke-Landau strength, i.e. the ray-class prime ideal theorem. The wording was not checked at source (SEC4 §7). |
| **Hecke functional equation**, normalized as Gao-Zhao eq. (1.1) | Lemma 4.8, hence 4.9, 8.1, 8.2 and Prop 16.1 | Not re-read at source. SEC4 D1 and D2 reproduce the functional equation numerically with the Lemma 4.1 conductors (mpmath, not certified). |
| **Class field theory** (Artin reciprocity; Milne CFT notes) | Lemma 4.1 | Standard. Consequences checked exactly on finite sets (SEC4 A1-A4). |
| **Cubic reciprocity** (as in DR eq. (1.4)); Hecke quadratic Gauss-sum reciprocity | Lemma 4.4; Sec. 17 CRT steps; [O5] | Exercised numerically only (EQC A3, L13 A5). |
| **Standard analysis and counting**: lattice Poisson summation, Mellin inversion, Phragmén-Lindelöf, Borel-Carathéodory with Hadamard three circles, Rankin's bound, the powerful-ideal count `O(Y^{1/2+ε})`, divisor bounds | throughout | Classical; not re-proved. |
| **Brought in by [O5] only** (under the substitution): Landau's prime ideal theorem, Hecke continuation, base change, `L(1, χ_{−3}) ≠ 0` | [O5] thm:main | Classical (OCT5_REVIEW_SUMMARY §2). |

## 6. How much has been reviewed, and what that does not mean

**The fraction.** With the Oct 5 substitution:
* 43 of the 57 load-bearing numbered nodes (75%) have had a whole-node bounded agent review with no wrong step found.
* 48 of 57 (84%) have it if partial verdicts are included.
* By owned lines, the shares are 62% (whole-node) and 87% (including partial).
* The imported [O5] thm:main has had bounded agent reviews of every proof line.

Without the substitution the shares are 43/65 (66%) and 48/65 (74%) of nodes, and 56% and 78% of owned lines. In v1, 11 of 65 nodes were R.

**What it does NOT mean.**

1. **Not independent.**
   * Every review was written by agents of one model family (Claude). All the reviews counted as new here were committed from one coordinating session and one branch.
   * They share conventions, a common symbol library (`a2/eis.py`), earlier notes and each other's framing. The later reviews explicitly build on the earlier ones.
   * The manuscripts were themselves produced by an AI system. Correlated blind spots, between reviewers and between reviewer and author, are possible and have not been measured.
2. **Not human.** No human expert has line-checked any node. Several reviews say that an expert check is needed. LEMMA18_1_CASE2_SEC188 §6 says so for Lemma 18.1: case 1 would be a new Lindelöf-on-average fourth moment for a sextic family.
3. **A single model family.** Two reviews by the same family are not two independent reviews. The counts above should be read as "one family's bounded pass", not as a consensus.
4. **Not an integration verdict.**
   * AGENTS.md requires one frozen source commit, an exact-SHA *independent* review, and readable mathematics resident under `research/integrated/`. None of these exists for [OAI].
   * The composition "[OAI] Part II + [O5] thm:main ⇒ [OAI] Thm 1.1" is new and needs its own independent review (SUB §6).
   * This map is bookkeeping. Changing a status requires a review, not an edit to the table.
5. **"No wrong step found" is not "proved".**
   * Each review has a scope, and inputs outside that scope were used as black boxes.
   * The mechanical checks verify displayed algebra and finite instances. Floating-point checks are not directed or certified, and a finite check is not a proof.
   * Analytic estimates (Fourier-measure `L¹` norms, tails, moment sizes) were read, not tested.
6. **The proof has no redundancy, and several points have zero slack.** Every load-bearing node is a single point of failure for Thm 1.1. Zero or near-zero slack occurs at four places:
   * the low exponent 3/16, at d = 0;
   * Lemma 18.1, invoked on its boundary;
   * the tight points Z1-Z4 inside Lemma 18.1;
   * the supply margin 23/1443.

   So a fixed-power loss anywhere in these chains would move or break 7/8. A high reviewed fraction does not lower this risk proportionally.
7. **Lean does not change this.** The import claims a formalization of the theorem, not of the numbered lemmas, and the formal route differs from the paper (v1 Sec. 5). LEAN_BUILD_ATTEMPT built 350 of 2,924 modules, with no errors, before its time budget ran out. The comparator was not run, and `#print axioms` was not obtained.
8. **Nothing here bears on RH.** The statement is a fixed half-plane `Re s > 7/8`.

## 7. Non-fatal findings collected from the reviews

None of these is a wrong step.

* **Lemma 18.1 at its boundary.** Prop 19.2 invokes Lemma 18.1 exactly at `n1+n2+6κz = M` and `β* = (1+κ)/2`. This is permitted, and a ν0 decrement would give a positive margin (JUNC).
* **The detector floor.** The floor 51/100 is a convention: any fixed `a0 = 1/2 + η` works (DET §4).
* **Lemma 4.8** is weaker than convexity but correct, with `C ≈ 0.69` (SEC4).
* **Lemma 4.9.** Its constants are astronomically large and ineffective, which is harmless for the fixed-(e, ε) asymptotics (SEC4).
* **Lemma 11.1.** The τ-independence of `A_η` is implicit; its one Part II use supplies it (SUB §4).
* **Prop 20.3.** The statement's pretarget list omits `z_inf`, `P0`, `b_round` and `eta_mesh`, although the proof fixes them pretarget (DET §7).
* **Lemma 5.5** is new mathematics relative to Oct 5 (DIFF §3.2).
* **Lemma 17.2's** proof is a different recursion from Oct 5's (INV).
* **Lemma 17.5** is not "[O5] lem:poisson verbatim" at the text level, which corrects an earlier note of ours (L17).
* **No-slack equalities.** `|d| ≤ 27·3^{k/6}|b|` holds with equality at `k ≡ 0 (mod 3)` (DIFF). Two parts of the 7/8 numerology also have zero slack: `C_II(7/8) = 3/16` (LOW) and the case-2 edge balance Z4 (L18c).
* **Imprecise prose in PR 910.** The sentence at PR 910 GEOMETRY_PERTURBATION.md:264 is imprecise (CONT).

## 8. Known misreadings to avoid

* **"U = 0, so the 7/8 proof is reviewed."** No. U = 0 holds only under the Oct 5 substitution. Four nodes are A, five are Rp and five are I. All reviews are bounded, single-family agent reviews.
* **"The eight Part I nodes are fine."** No. They are unreviewed. They leave the path only if [O5] thm:main is imported, and that composition is itself unreviewed by an independent party.
* **"v2 downgraded Lemmas 7.1 and 15.1."** The code changed from R to Rp because v2 separates partial reviews. No problem was found in either.
* **"Lemma 4.5 is reviewed, so every Fourier separation is checked."** The lemma is reviewed. Its 35 invocations, and the analytic separations in Lemmas 17.2 and 18.1 that use it, were read but not replayed.
* **"Oct 5 coverage transfers."** Only where a diff was done:
  * Prop 5.1's arithmetic core (DIFF) does transfer.
  * The Lemma 17.1 and 17.2 statements match Oct 5 at z = 0 (INV), but the proofs differ, so no proof verdict transfers.

## 9. Reproduction

```sh
cd research/exploratory/qrh-2026-10/reviews
P=standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints
git show pr908:$P/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex > /tmp/sep30.tex
python3 -I sep30_depgraph_v2.py /tmp/sep30.tex /tmp/map_v2.json /tmp/map_v2_table.md   # exit 0
```

The script prints the sha256 check, the counts of Sec. 2 (including the without-SEC4 variant), the owned-line shares, both rankings and the per-node ndep. It authenticates only text-level facts (hash, `\ref` edges, line ownership). Statuses and evidence strings are hand-entered from the files in the header.

## 10. Addendum v2.1 (later on 10 Oct 2026): two more reviews

The tables above are unchanged and record the v2 state. Two reviews written after v2 move
seven nodes:

| node | v2 | v2.1 | source |
|---|---|---|---|
| Lem 4.2 Prime Gauss identities | A | R | [SEP30_L42_44_REVIEW.md](SEP30_L42_44_REVIEW.md): no wrong step; exact checks at 422 primes |
| Lem 4.3 Quadratic four-term formula | A | R | same: no wrong step; the four-term formula is exact for all 5,454 odd `c` with `N(c) ≤ 2000`; one compressed step closed by an exhaustive finite check |
| Lem 4.4 Sextic reciprocity, fixed Gauss phase | A | R | same: no wrong step, given classical cubic reciprocity (imported; also applied to the inert prime 2; the cited source was not opened) |
| Lem 17.1 Marked inverse moment | A | Rp | [SEP30_MISC_REVIEW.md](SEP30_MISC_REVIEW.md): initialization transform replayed exactly at tiny scale; still conditional on Lemma 17.2 (Rp) |
| Lem 20.1 High exponent for one row bin | I | R | SEP30_MISC_REVIEW.md: correct as a reduction to named imported inputs |
| Prop 2.1 Continuation from a common signal | I | R | SEP30_MISC_REVIEW.md: complete proof read line by line |
| Thm 1.1 (final assembly only) | I | R | SEP30_MISC_REVIEW.md: the final contradiction read; correct |

Recount (same 65 nodes, same statuses otherwise):

| | R | Rp | I | A | U | L | total |
|---|---|---|---|---|---|---|---|
| v2.1, as written | 49 | 6 | 2 | 3 | 5 | – | 65 |
| **v2.1, with the Oct 5 substitution** | **49** | **6** | **2** | **0** | **0** | **8** | **57** + [O5] thm:main |

Owned lines with the substitution (11,134):
* R: 7,469 (67.1%);
* Rp: 3,526 (31.7%);
* I: 139 (1.2%; Def 5.6 and Prop 11.3);
* A and U: 0.

What this means:
* Under the substitution, every load-bearing numbered node now has at least a bounded review or
  an inspection.
* The open parts are:
  * the "read only" pieces of the six Rp nodes, the largest being Lemma 17.2's Fourier separations;
  * the two inspected nodes;
  * the imported external theorems of Section 5, now including classical cubic reciprocity as
    used in Lemma 4.4.
* As written, the 8 Part-I-only nodes (3 A, 5 U) remain unreviewed.

Separately, the import's Lean development of the 7/8 theorem now builds completely, and its
axioms are the three standard ones ([LEAN_BUILD_ATTEMPT.md](LEAN_BUILD_ATTEMPT.md), Addenda A–B).
That is a machine check of the Lean statement, not of this manuscript's text. A paper-to-Lean
correspondence is being prepared separately.

The counts are hand-entered from the review headers. They were not regenerated with
`sep30_depgraph_v2.py`, whose status table is the v2 one.

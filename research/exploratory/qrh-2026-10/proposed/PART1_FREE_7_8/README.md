# PROPOSED: a Part-I-free paper route to the Sep 30 7/8 theorem

```text
Status: PROPOSED object (exploration level). It is NOT an integrated packet and assigns no
  verdict. It collects a new composition of arguments: the 7/8 statement of the Sep 30
  manuscript proved from beta_* <= 1 alone, without Part I. Every review cited here is a bounded
  agent review, written within one model family. Before integration, the composition needs a
  review independent of this model family. It is not a claim about RH, which is unsolved.
Scope: the composition (Part II as written, plus literal edits E1-E6 and three short lemmas
  P1F.0-P1F.2) and its node set. The lemmas themselves are in REMARK_19_3.md. Out of scope: the
  proofs of the 57 Part II and shared nodes (statuses as in SEP30_VERIFICATION_MAP_V2.md,
  addendum v2.1), and Part I.
Exact sources or dependencies:
  [OAI]  Sep 30 paper.tex at ref 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, SHA-256
         42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3. External, unreviewed,
         read as untrusted data.
  [LEAN] upstream/lean at the same ref (read only).
  Notes: ../../reviews/PART1_FREE_ROUTE.md (the route), ../../reviews/PART1_FREE_ROUTE_REVIEW2.md
         (second review), ../../reviews/SEP30_LEAN_CORRESPONDENCE.md (paper-to-Lean map),
         ../../reviews/SEP30_VERIFICATION_MAP_V2.md (node statuses), REMARK_19_3.md (this folder).
What was actually run: for this folder, remark_19_3_checks.py (43/43 gates, 14/14 failing
  controls; see REMARK_19_3.md Sec. 7). The route's own checks (part1_free_checks.py, 32/32 plus
  the widened junction replay) and Review 2's checks (part1_free_review2_checks.py, 14/14) were
  run by those notes, not re-run here.
Smallest remaining gap: an independent review of the composition, and in particular of
  Lemma P1F.0 (Remark 19.3), whose paper-level status is no better than Rp. Then an exact-SHA
  review and a human integrator, as AGENTS.md requires for any integrated packet.
```

RH is unsolved. Nothing in this folder says otherwise. The 7/8 statement is a fixed zero-free half-plane `Re s > 7/8`, far from the critical line `Re s = 1/2`.

## 0. What this folder is and is not

* **It is a separately labelled proposed object**, as [AGENTS.md](../../../../../AGENTS.md) asks for new mathematics that extends existing work. It changes no accepted record. Nothing here is under `research/integrated/`.
* **It is a new composition of arguments.** Under AGENTS.md, a new composition needs its own review, even when each step is elementary. Editorial consolidation does not approve it.
* **It needs a review independent of this model family.** The route note, its second review and this folder were all written by agents of one model family on one branch. They are not independent of one another ([docs/REVIEWING.md](../../../../../docs/REVIEWING.md)).
* **It does not certify the manuscript.** The 57 nodes the route keeps carry their own statuses, and several are only Rp or I (Sec. 2).
* **The Lean theorem is a separate object.** The imported Lean development proves the 7/8 statement by an architecture with the same high-bin split ([SEP30_LEAN_CORRESPONDENCE.md](../../reviews/SEP30_LEAN_CORRESPONDENCE.md) §4). Its formal packet draft is [SEP30_7_8_FORMAL_PACKET](../SEP30_7_8_FORMAL_PACKET/README.md). This folder is about the paper's text, not the Lean proof.

## 1. The composition

The paper as written starts Part II from Thm 3.1, the 11/12 half-plane. That gives `Δ ≤ 1/24`, `κ ≤ 5/6` and the bin ceiling `δ ≤ 5/6` (6812-6830). The route replaces this input with `β* ≤ 1`, which the paper states at 386-387. Then `Δ ∈ (0, 1/8]`, `κ ∈ (3/4, 1]` and `δ ≤ κ ≤ 1`.

| Piece | Where | What it does |
|---|---|---|
| `β* ≤ 1` | paper 386-387 | replaces Thm 3.1 as the Part II input |
| Edits E1-E6 | [PART1_FREE_ROUTE.md](../../reviews/PART1_FREE_ROUTE.md) §2.3 | literal restatements: `Δ ≤ 1/8`, `κ ∈ (3/4, 1]`, the bin ceiling `δ ≤ κ`, the `κ = 1` clause of Lemma 18.1, and routing bins with `δ ≥ 5/6` to the high-bin count |
| Lemma P1F.0 | [REMARK_19_3.md](REMARK_19_3.md) §2-3 | Remark 19.3 written as a lemma: the no-slot amplified count `U^{e(r) − δr + ε}` for any bin with `1/50 < δ ≤ 1`, with no `δ ≤ α` |
| Lemma P1F.1 | REMARK_19_3.md §4 | high-bin row count `U^{1 − δ + ε}` for `5/6 ≤ δ ≤ 1`, from P1F.0 and Prop 8.3 at `t = 3/2` |
| Lemma P1F.2 | REMARK_19_3.md §5 | high-bin margin `E(d) − Δ ≤ −1/48 − δ/16 − Δ + (13/16)λ` for `d ≤ h`, plus `2ζ` beyond `h`, for `0 ≤ λ ≤ 527/300` (Review 2's correction) |
| Junction box widened | PART1_FREE_ROUTE.md §6, J1 | the junction script re-run with every `Δ` box widened from `(0, 1/24]` to `(0, 1/8]`. Only P2 (`κ ≤ 5/6`, the bound being replaced) fails |
| Final contradiction | PART1_FREE_ROUTE.md §3 | Prop 2.1 and Prop 20.3 with `ω = Δ/2`, for every `Δ ∈ (0, 1/8]`; equal slots, as in the paper |

**How the high bins close.** For a bin with `5/6 ≤ δ ≤ κ`:

1. P1F.1 gives the row exponent `R = 1 − δ + λ`, at every row size from `Z^{1/100}` to `Z^{13/16+ζ}`.
2. P1F.2 then gives a margin of at least `7/96 + Δ − (13/16)λ − 2ζ`. For the small `λ` and `ζ` of the route, that is larger than the balanced bins' `49/440640 + (51/64)Δ`.

The intermediate-row paragraph (16146-16165) is never applied to a high bin. It would fail there for `δ > 529/625`.

## 2. Node set

The starting point is the 65 load-bearing numbered nodes of SEP30_VERIFICATION_MAP.

**Leave (8).** These are the same eight nodes that leave under the Oct 5 substitution: Thm 3.1, Lemma 5.8, Lemma 6.1, Lemma 6.2, Prop 6.3, Lemma 9.1, Prop 9.2 and Prop 11.2. The imported theorems that only they use (BGL; Huxley/Baier-Bansal) leave with them. Def 5.6 stays, through Lemma 5.7.

**Stay (57).** Statuses are hand-copied from SEP30_VERIFICATION_MAP_V2 addendum v2.1, column "with the Oct 5 substitution":

| | R | Rp | I | A | U | total |
|---|---|---|---|---|---|---|
| kept nodes | 49 | 6 | 2 | 0 | 0 | 57 |

* The six Rp nodes are Lemmas 7.1, 15.1, 17.1 and 17.2, Prop 19.2 and Prop 20.3.
* The two I nodes are Def 5.6 and Prop 11.3.
* Under this route their ranges widen to `a, κ, δ ≤ 1` and `Δ ≤ 1/8`. PART1_FREE_ROUTE §1 checked that each one is stated for the wider range, and Review 2 re-checked the ten riskiest.

**Unlike the Oct 5 substitution, nothing is imported.** The route needs no 11/12 theorem at all, neither Part I nor [O5] thm:main.

**New obligations (proposed, this folder).**

1. **`β* ≤ 1`.** This is stated at 386-387 and is immediate from the definition. It is not a new node.
2. **Lemma P1F.0 (Remark 19.3).** The v2 map lists the remark as not load-bearing; in this route it is load-bearing.
   * Its derivation (15248-15294) uses no `δ ≤ α` and no `Δ ≤ 1/24`. The first use of `δ ≤ α` in the proof of Prop 19.2 is 15303, as Review 2 said (REMARK_19_3.md §3).
   * Its paper-level status is no better than Rp. It inherits Rp from Lemmas 17.1-17.2 through Lemma 17.6, and it sits inside Prop 19.2 (Rp).
3. **Lemma P1F.1.** A two-case inequality on top of P1F.0 and Prop 8.3 at `t = 3/2`.
4. **Lemma P1F.2.** Exact algebra on eq:common-high-exponent.
5. **The junction box widened to `Δ ≤ 1/8`.** Replayed by PART1_FREE_ROUTE J1.
6. **Edits E1-E6.** Literal; none changes a lemma statement.

**Formal counterparts.** Each of P1F.0-P1F.2 has a kernel-checked Lean declaration in the import closure of the Lean 7/8 theorem (REMARK_19_3.md §6). Matching instances are formally covered in Lean's own normalization. The Lean objects were not matched line by line with the paper's, so this is not a substitute for the paper-level review.

| Lemma | Lean declaration | Relation |
|---|---|---|
| P1F.0 | `HeckeDetectorNoSlotInverseCount.no_slot_inverse_count` | stronger range; raw moment as a hypothesis, discharged in the closure; different normalization |
| P1F.1 | `HeckeDetectorRowCount.high_bin_count`; `HeckeDetectorHighCount.high_count_from_raw_moments`; `ProbeFinalAssembly.CountParameters.high` | same two-case step; per fiber at `t = 3/2`; per bin for `δ > 5/6` |
| P1F.2 | `ProbeCentralExponent.high_source_margin`; `ProbeHighRowFamily.high_mixed_margin` | stronger in `δ, Δ, q`, covering `λ ≤ 527/300`; the route's instance has `λ ≤ 1/32` |

## 3. What a reviewer should check first

These are listed by how much would fail if they were wrong.

1. **Lemma P1F.0 against 15248-15294 and Lemma 17.6.** Especially S3 (row-dependent witness profiles through Lemma 4.5) and S6 (division by the spike). The v2 map lists S3's clause as open.
2. **Prop 8.3's saturated witness at `t = 3/2`.** The deficit `r ≥ 1 − O(ε)` must have an absolute constant. A fixed deficit of `1/8` already breaks the margin at `δ = 5/6` (Review 2 NC3; REMARK_19_3 FC9).
3. **That no high bin is sent to the intermediate-row paragraph** (16146-16165), and that edits E4-E5 route every `d ∈ [d_min, h + ζ]` of a high bin to P1F.1-P1F.2.
4. **The census of Part II uses of `Δ`, `κ`, `δ` upper bounds** (PART1_FREE_ROUTE §1; Review 2 §1). Gate T2 there checks coverage by line range only, so completeness rests on reading.

## 4. Files

| File | Role |
|---|---|
| [REMARK_19_3.md](REMARK_19_3.md) | Lemmas P1F.0-P1F.2: statements, proofs, Lean cross-reference |
| [remark_19_3_checks.py](remark_19_3_checks.py) | exact checks (sympy and fractions; `python3 -I`) |
| [remark_19_3_checks_output.json](remark_19_3_checks_output.json), [remark_19_3_checks_stdout.txt](remark_19_3_checks_stdout.txt) | output of the run reported in REMARK_19_3.md |

## 5. Known misreadings to avoid

1. **"The paper proves 7/8 without Part I."** No. As written, it cites Thm 3.1 (6812). This folder proposes literal edits plus three short lemmas that give a route that does not.
2. **"The Lean proof certifies this route."** No. The Lean proof has the same high-bin architecture and kernel-checks matching instances in its own normalization. The paper route's text still needs review.
3. **"The route is reviewed."** Only by bounded agent reviews within one model family. It needs a review independent of this model family, then an exact-SHA review and a human integrator.
4. **"This bears on RH."** No. It is about a fixed half-plane `Re s > 7/8`.

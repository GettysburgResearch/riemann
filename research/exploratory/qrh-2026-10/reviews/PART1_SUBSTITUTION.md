# Replacing Sep 30 Part I (Thm 3.1) by the Oct 5 11/12 theorem: interface check

```text
Status: REVIEW (bounded interface check), exploration level. This is not an integration verdict.
  It does not certify Oct 5 thm:main or any Sep 30 lemma. Verdict (a): at statement level, the
  substitution is valid. Eight claim-bearing Part I nodes then leave the 7/8 critical path. The
  ninth node, Def 5.6, does not leave: it is directly load-bearing through Lemma 5.7 (Sec. 3.2).
Scope: (i) every use in [OAI] of Thm 3.1, beta* <= 11/12, Delta <= 1/24, kappa <= 5/6 and the bin
  ceiling delta <= 5/6; (ii) the statement of [O5] thm:main (paper2 73-75) and the quantifiers of
  its deduction (660-771); (iii) bounded reviews of [OAI] Lemma 11.1 (6514-6580) and Lemma 19.1
  (15015-15062); (iv) the consequences for the node table of SEP30_VERIFICATION_MAP.md.
  Out of scope: the truth of [O5] thm:main (see OCT5_REVIEW_SUMMARY.md) and the proofs of the
  Sep 30 lemmas that Lemmas 11.1 and 19.1 cite.
Exact sources or dependencies:
  [OAI] Sep 30 paper.tex at pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
        standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
        The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
        SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (16,677 lines).
  [O5]  Oct 5 paper2.tex at the same ref, .../The-Quasi-Riemann-Hypothesis-October-5-2026/build/
        paper2.tex, SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d
        (3,988 lines). Both are external and unreviewed and were read as untrusted data.
  Review files read on branch claude/peaceful-faraday-ki4ewu at 8875b9aa783117c991736d7c1e3c86c500292e9a:
        reviews/SEP30_VERIFICATION_MAP.md (657696c2...b364), reviews/OCT5_REVIEW_SUMMARY.md
        (5c3ab27a...dc5), reviews/OCT5_RESIDUAL_ITEMS.md (794ae290...13fb),
        proposed/OCT5_11_12_PACKET/README.md (3e955c37...e88e87),
        reviews/SEP30_DETECTOR_QUANTIFIERS.md Sec. 6 (1388e898...b50) and
        reviews/SEP30_JUNCTION_CHECK.md Sec. 2 (fa8fd498...f56).
What was actually run:
  - reviews/part1_substitution_check.py (new; stdlib only; `python3 -I`; SHA-256
    471bb4865f87a8d6c1496337567093989cb084d4d57e7918bd0d65526900611b) on both TeX files: ALL CHECKS
    PASSED. It checks both hashes and lists every Part II \ref/\eqref that lands in the line spans of
    the nine "via 3.1" nodes or of three Part-I-only prose blocks. The only such citation is
    thm:eleven-twelfths at 6812. It also verifies the verbal edge Def 5.6 -> Lemma 5.7 -> Lemma 14.3,
    lists the Part II lines that carry 11/12, 1/24 or the 5/6 ceilings, and checks the [O5] statement
    and that [O5] does not cite the Sep 30 paper in any proof.
  - Line-by-line reading: [OAI] 48-62, 170-200, 362-560, 1531-1600, 2815-3140, 4201-4383, 4030-4060,
    5905-5925, 6493-6830, 7656-7830, 8564-8590, 12560-12592, 12822-12900, 14985-15112, 15468-15502,
    15948-15975, 16125-16170, 16236-16270, 16405-16463; [O5] 40-125, 184-420, 660-795.
  - Not run: no proof of [O5] was re-derived, no numerics, no Lean.
Smallest remaining gap: the junction has no gap beyond the definitional bridge B (Sec. 2.3), which is
  checked here. With the substitution, the bootstrap rests on [O5] thm:main, whose smallest failure
  point is prop:R. prop:R has only bounded agent reviews, and they are not independent. That replaces
  eight unreviewed Part I nodes. The composition itself is new, and AGENTS.md requires its own
  independent review.
```

RH is unsolved. Both manuscripts concern fixed zero-free half-planes (`Re s > 11/12` and `Re s > 7/8`). Neither says anything about the critical line. "Reviewed" here means a bounded agent review with the stated scope. It never means certified or integrated.

## 0. Summary

* **What Sep 30 Part II takes from Part I.** It takes the single inequality `β* ≤ 11/12`, where `β*` is the supremum in (1.1b), [OAI] 378-386. Nothing else from Thm 3.1, or from the eight Part-I-only lemmas behind it, is used: no estimate, no uniformity, no constant, and no data of the Part I probe.
* **What [O5] thm:main gives.** It gives zero-freeness in `Re s > 11/12` for *every* finite-order Hecke character of the same field, primitive or not, principal included.
* **The implication.** [O5] thm:main implies `β* ≤ 11/12` in two lines (bridge B, Sec. 2.3).
* **Verdict (a).** The substitution is valid. It removes Thm 3.1's proof, Lemmas 5.8, 6.1, 6.2, Prop 6.3, Lemma 9.1, Prop 9.2 and Prop 11.2 from the 7/8 path, together with about 140 lines of Part-I-only prose and two imports (BGL; Huxley/Baier–Bansal).
* **A correction to the verification map.** Def 5.6 is not "via 3.1". Lemma 5.7's statement is phrased in its terms, and Lemma 14.3 uses Lemma 5.7 directly.
* **Lemmas 11.1 and 19.1.** No wrong step was found in either. Lemma 11.1 is an elementary order-of-choices lemma. Lemma 19.1 is a standard smoothed prime-sum bound in a buffered zero-free rectangle. Neither depends on `β* ≤ 11/12`, so the substitution does not affect them.

## 1. What Sep 30 uses from Thm 3.1

### 1.1 The object

`β*` is defined once, at [OAI] 378-386:

> `β* = sup({1/2} ∪ {Re ρ : 1/2 ≤ Re ρ ≤ 1, L_F(ρ, η) = 0 for some primitive finite-order Hecke character η})`, with poles not included.

* **Field.** `F = Q(√−3)` throughout ([OAI] 50, 372).
* **Characters.** "A finite-order Hecke character η modulo 𝔣 is a character of the ray class group modulo 𝔣, extended by zero", with `L_F(s, η) = Σ η(𝔞) N𝔞^{−s}` ([OAI] 52-61). The text notes that the complex place admits no nontrivial finite-order character, so no angular (Größen-) component occurs.
* **Primitive only.** Imprimitive characters have the same zeros in `Re s > 0` (176-177, 373-376).
* **Principal character.** It is included (it is primitive of conductor 1). Its pole is excluded from the set.

Thm 3.1 (532-537) states zero-freeness in the open half-plane `Re s > 11/12` for every finite-order Hecke L-function over `F` and every Dirichlet L-function. Its proof (6783-6805) is a contradiction argument from `β* > 11/12`.

### 1.2 Every use

The only citation of Thm 3.1 outside Part I's own proof and the introduction (162, 253) is at 6812-6813: "Theorem 3.1 applies to every primitive character entering the supremum in (1.1b), and therefore gives `β* ≤ 11/12`." The script confirms this is the only Part II `\ref`/`\eqref` into any of the nine via-3.1 node spans.

Part II then uses that one inequality through these quantities.

| Consumed quantity | Lines | What it needs |
|---|---|---|
| `0 < Δ := β* − 7/8 ≤ 1/24` (eq:part-II-bootstrap) | 6816-6817, 15097-15099, 15498-15501 | `β* ≤ 11/12` |
| `κ := 2β* − 1 = 3/4 + 2Δ ≤ 5/6`, in particular `κ < 1` | 6819, 15100-15106 (κ < 1 puts Lemma 18.1 in its zero-free-hypothesis case), 15502, 15926 | `β* ≤ 11/12` |
| bin ceiling `a ≤ β*`, `δ = 2a−1 ≤ κ ≤ 5/6 = α` (eq:part-II-bin-ceiling) | 6821-6830, 15107, 15763, 16146 | `a ≤ β*` comes from the *definition* of β* (4370-4383); only `≤ 5/6` needs 11/12 |
| endpoint `δ = α = 5/6` included; Lemma 20.2 on `0 ≤ δ ≤ 5/6`, closed | 6829-6830, 15995-16003, 16165 | `β* ≤ 11/12` (closed: `β* = 11/12` is allowed) |
| compact `κ ∈ [3/4, 5/6]` for the Lemma 18.1 mesh; `δ ≤ 5/6 < 1` | 16241, 16269 | `β* ≤ 11/12` |
| `R_* + Δ/4 ≤ 139/96`; `m_high = 51Δ/64 < m_small` | 16141; ordering in SEP30_DETECTOR_QUANTIFIERS §6.2 | `Δ ≤ 1/24` |

The following involve `β*` but **not** Thm 3.1:
* `β* ≤ (1+κ)/2` in Lemma 18.1 holds with equality (12564-12566, 12581-12585, 15104-15106).
* The global bounds of Lemma 4.9 hold for `b ≥ β*` (1547-1597).
* The contours run on `Re s = β* + e` (Secs. 10, 20).

These come from the definition of `β*` and the contradiction hypothesis `β* > 7/8`.

### 1.3 What Part II does *not* take from Part I

* **No quantitative content.** Every bound for `L`, `1/L` and `L'/L` in Part II comes from Lemma 4.9 or from the buffered bins of Lemma 8.1. Lemma 4.9 uses Borel–Carathéodory and three circles on disks that are zero-free by the definition of `β*` or by the bin; Lemma 8.1 uses Lemma 4.9. Neither cites Thm 3.1. So Part II needs no height uniformity and no `1/L` bound from Part I.
* **No Part I data.** Part II re-instantiates the probe data "from Section 6" and says they "may differ from those used in Part I" (6846-6851).
* **No Part I estimate.** Part II's low side is Lemma 15.1 with Prop 15.2, not Lemma 5.8 or Prop 6.3. Its row count is Prop 19.2, not Prop 9.2. Its use of Lemma 5.7 is only "the algebraic frozen-base extraction" eq:unmarked-structural-block (7822-7829: "We do not apply the numerical unmarked estimate").
* **No Part I constant.** Part II has no `1/4800`, no `1021/25000` and no `C_I`.

### 1.4 Which characters the zero information is applied to

The bin ceiling is the only place where `β*` controls zeros of L-functions other than the target.

* For a row `u`, the family is `𝒳_u = {ν·χ_•(u)^{±1} : ν ∈ Θ}`, where `Θ = ⟨η, T̂⟩` is the group generated by the target and the fixed ray characters (4222-4245).
* [OAI] asserts at 4374-4376 that every primitive character inducing a member of `𝒳_u` is a finite-order Hecke character. The argument is sextic reciprocity: `n ↦ (u/n)_6` on primary `n` is a ray class character (4246-4253).
* The angular factor `α(p) = p/|p|` occurs on the Poisson side only inside the absolutely convergent correction product `ℋ_{η,u}` (`a_p`, `b_p` at 3863-3864; regions 4053-4058). It never occurs in an L-function whose zeros are used. The row L-functions in eq:probe-high (4040-4044) are `L^S(w, χ_•(u))` and `L^S(x, η·conj χ_•(u))`, both of finite order.
* So no Größencharacter zero information is needed. Every character whose zeros enter lies in the family over which `β*` is taken.

## 2. What [O5] thm:main gives, and the comparison

### 2.1 Statement and deduction

[O5] 73-75: "Every finite-order Hecke L-function over `K` has no zeros in the half-plane `Re s > 11/12`", with `K = Q(√−3)` (71).

The deduction (660-771) runs as follows.
* It fixes an *arbitrary* finite-order Hecke character `ν` of `K` and a finite set `S` that contains the primes above 2 and 3 and the conductor primes of `ν` (665-667).
* It proves `A_1(D) = Σ_{(n,S)=1} μ(n)ν(n)W(N n/D) ≪_{ν,S,W,ε} D^{11/12+ε}` (723).
* It then derives a contradiction at any zero `ϱ` with `Re ϱ > 11/12`, using `𝓜_W(s) = Ŵ(s)/L_K^S(s, ν)` (727-756).

The argument is per character and qualitative, and it uses no supremum over the family. The packet README (§2.1) records the remaining conventions:
* the principal character is covered, with the one-line repair N1 that excludes `s = 1`;
* imprimitive `ν` are covered, since `L_K^S` and `L_K` have the same zeros in `Re s > 0`.

[O5] cites the Sep 30 paper only at line 81, as motivation in the introduction, so the composition is not circular (script check).

### 2.2 Point-by-point comparison

| Dimension | Needed by [OAI] Part II | Given by [O5] thm:main | Covered? |
|---|---|---|---|
| Field | `F = Q(√−3)` | `K = Q(√−3)` | yes |
| Character class | primitive finite-order Hecke = primitive ray class characters ([OAI] 52-56) | every finite-order Hecke character. [O5] does not define the term; its proof treats `ν` as a function on a fixed ray class group (805-821), i.e. a ray class character | yes (superset) |
| Größencharacters with angular part | not in `β*`, and not needed (Sec. 1.4) | not claimed | not needed |
| Primitive vs imprimitive | primitive only | both | yes |
| Principal character (`ζ_F`) | included, pole excluded | included, pole excluded (N1) | yes |
| Twists `η`, `ν ∈ Θ`, `χ_•(u)^{±1}` | all finite-order (Sec. 1.4) | every finite-order `ν`, no restriction on conductor or on primes above 6 | yes |
| Exclusion sets `S` | internal; zeros in `Re s > 0` are unaffected by deleted factors (388-397) | internal; same remark (745-756) | irrelevant |
| L-function normalization | `Σ η(𝔞) N𝔞^{−s}`, zero-extended | `L_K(s, ν)` with `ν` zero-extended (215-217); Euler product at 745-750 | same |
| Region | `Re ρ ≤ 11/12` for zeros with `1/2 ≤ Re ρ ≤ 1`, i.e. `β* ≤ 11/12`; equality allowed | no zero in the open half-plane `Re s > 11/12` | exactly |
| Uniformity or quantitative content | none (Sec. 1.3) | none (constants depend on `ν, W`; R2 F3) | not needed |
| Height-uniform `1/L` bounds | none from Part I | none | not needed |

### 2.3 The bridge

**Bridge B.** Assume [O5] thm:main. Then `β* ≤ 11/12`, with `β*` as in [OAI] (1.1b).

*Proof.* Let `η` be a primitive finite-order Hecke character of `F = K`. It is a finite-order Hecke character in the sense of [O5], and the two L-functions coincide (the same Dirichlet series with the same zero extension). Let `ρ` be a zero of `L_F(s, η)` with `1/2 ≤ Re ρ ≤ 1`. If `η` is principal, then `ρ ≠ 1`, because `1` is a pole. By [O5] thm:main, `Re ρ ≤ 11/12`. So every element of the set in (1.1b) is at most `11/12`, and so is its supremum. ∎

* B is exactly the sentence at [OAI] 6812-6814, with [O5] thm:main in place of Thm 3.1.
* B needs no extra mathematical lemma. It needs only the definitional match in Sec. 2.2.
* The one point a reader must accept is that "finite-order Hecke character" means the same in both texts. [OAI] defines it as a ray class character. [O5] uses the standard term without a definition, and its proof is consistent with that meaning.

## 3. Effect on the 7/8 dependency graph

### 3.1 What leaves the critical path

With B in place of 6812-6813, nothing in Part II cites the following. Each item is used only inside Thm 3.1's proof chain. The script confirms that Part II has no `\ref` or `\eqref` into any of their line spans.

| Node or block | Lines | Status in the map | Imports that leave with it |
|---|---|---|---|
| Thm 3.1, proof | 532-537; 6783-6805 | A | — |
| Prop 11.2 balanced high estimate | 6582-6698 | A | — |
| Prop 6.3 balanced low estimate | 3672-3721 | A | — |
| Lemma 6.2 balanced additive norm | 3587-3666 | U | — |
| Lemma 6.1 planar additive large sieve | 3497-3580 | U | Huxley; Baier–Bansal |
| Lemma 5.8 unmarked completed-row moment | 3138-3285 | U | — |
| Prop 9.2 sextic-sieve row envelope | 5181-5446 | U | — |
| Lemma 9.1 sextic large sieve | 4707-5171 | U | Blomer–Goldmakher–Louvel |
| prose: Sec 6.2 intro; Sec 10.5 "Applying the row envelope"; Sec 11 margin table | 3486-3496; 5905-6012; 6493-6512 | (prose) | — |

In total this is about 1,230 lines of numbered-node text and about 140 lines of prose. The Part I ledger margins (`1021/25000`, `C_I(11/12) = 1/4`, `43/300`, `1/4800`) also stop being load-bearing.

### 3.2 What does not leave (correction to SEP30_VERIFICATION_MAP §1 and §4)

* **Def 5.6 (2888-2950) is directly load-bearing.**
  * Lemma 5.7's statement opens "For an unmarked reflected block" (2958). Its quantities (`H, A_0, N_0, B_0, S_0`, `𝒰_{v,ℓ_b,e_λ}(R)`, `ℐ_H`) are defined only in Def 5.6.
  * Lemma 14.3 uses Lemma 5.7's eq:unmarked-structural-block at 7823.
  * `sep30_depgraph.py` missed this verbal edge, so the map tagged Def 5.6 "via 3.1". It is a definition with no proof obligation of its own, but it cannot be dropped.
  * Nine nodes were tagged via 3.1; eight of them leave.
* **Part I material that Part II uses directly.** The following stay on the path whatever proves `β* ≤ 11/12`:
  * Lemma 11.1 (Sec. 4);
  * Lemma 7.1, Lemmas 8.1-8.3 and Lemmas 10.2-10.6;
  * Def 10.1 and Prop 11.3;
  * the prose norm inequality eq:actual-residual-row-dyad (3130; cited at 7689, 7803, 8048, 9888);
  * the Sec 6.1 definitions with eq:general-probe and eq:low-separated (3397, 3470; cited at 6886 and 8580);
  * the claim at 4374 that `𝒳_u` consists of finite-order characters.

  The last item also fed Thm 3.1's route, so the substitution neither creates nor removes that dependency.

### 3.3 What enters

* **[O5] thm:main as an imported statement.**
  * Its review record is R1 + R2 + R3 plus the residual items: every proof line was read by bounded agent reviews and no wrong step was found.
  * There is no independent exact-SHA review and no human review.
  * Its smallest failure point is prop:R (packet README §8).
* **Its imports.** Goldmakher–Louvel, Dunn–Radziwiłł, Patterson and Kubota are already on the 7/8 path through Prop 5.1 and Lemma 5.5. Landau's prime ideal theorem, Hecke continuation and the base-change and `L(1, χ_{−3})` facts are classical.
* **Correlated risk.** [O5] prop:R and [OAI] Prop 5.1 are the same reflection mechanism on the same imported theta data. A failure in that shared input (for example, the absent Kubota residue or the `χ_p³` conversion) would break both routes. The substitution removes unreviewed Part I text. It does not make the bootstrap independent of the reflection engine that Part II also uses.

### 3.4 Updated counts (relative to the map's §4 table only)

The map's table has 65 load-bearing numbered nodes, of which 46 are unreviewed (A + U). With the substitution:
* the eight nodes of Sec. 3.1 leave (3 A, 5 U);
* Def 5.6 moves from via-3.1 to direct.

That leaves 57 numbered Sep 30 nodes plus one imported theorem, with 38 unreviewed. Counting this file's bounded reviews of Lemmas 11.1 and 19.1 (U → R), 36 remain unreviewed.

These counts do not include reviews committed after the map. For example, SEP30_DETECTOR_QUANTIFIERS covers Lemmas 8.1-8.3, Prop 16.1 and Prop 20.3, and SEP30_L13_L45_REVIEW covers Lemmas 13.2-13.4 and 4.5. Those were not recounted here.

## 4. Review of Lemma 11.1 (late choice of height; 6514-6580)

**Statement, paraphrased.**
* Fix `σ_0` with `Δ_0 = β* − σ_0 > 0` and `C(s) = s + c`. Let `m > 0` and `0 < ω < Δ_0` be common to all targets.
* Assume the low bound `|J_η| ≪_η Z^{C(σ_0)+ω}`, and, for every `N`,
  `|J_η − f_η| ≪_{η,N} Z^{C(β*)−m}(1+T_1)^{A_η} + Z^{B_η}T_1^{−N}`.
  This must hold for `T_1 = Z^τ`, for every `0 < τ ≤ min{d_min/100, τ_{0,η}}` and all large `Z`, with `A_η, B_η` finite and independent of `N`.
* Then `τ` and `N` can be chosen after `η` so that `|J_η − f_η| ≪_η Z^{C(β*)−m/2}`.

**Check of the proof (6560-6580).**
* Take `τ_η ≤ min{d_min/100, τ_{0,η}, m/(4(A_η+1))}`. For `T_1 = Z^{τ_η} ≥ 1` we have `(1+T_1)^{A_η} ≤ 2^{A_η}Z^{A_η τ_η} ≤ 2^{A_η}Z^{m/4}`, so the first term is `O_η(Z^{C(β*)−3m/4})`. Correct.
* Next take `N` with `B_η − Nτ_η < C(β*) − m/2`. Such an `N` exists because `τ_η > 0`, and then `Z^{B_η}T_1^{−N} = Z^{B_η−Nτ_η} ≤ Z^{C(β*)−m/2}`. Correct.
* The functions `J_η` and `f_η` do not contain `T_1`, so the bound concerns fixed functions.
* `σ = m/2` and `ω` are fixed before the target, which is what Prop 2.1 (400-432) requires.

**Points to note. Neither is a gap.**
1. The proof needs `A_η` to be independent of `τ`; otherwise the choice `τ ≤ m/(4(A_η+1))` would be circular. The statement says only "independent of N". The subscript, and the clause about "finite profile orders for the target", imply that `A_η` is fixed before `τ`.
   * The Part II application states this explicitly (16382-16389, 16427-16431: increasing the order "changes only external seminorm constants ..., not `A_η`, `B_η`, or `τ_{0,η}`").
   * SEP30_DETECTOR_QUANTIFIERS §6.3 (I3, I4) reached the same reading.
   * `B_η` may depend on `τ` without harm, since `N` is chosen after `τ`.
2. The implied constant in the hypothesis may also depend on `τ`. This is harmless because `τ = τ_η` is fixed per target.

**Use in Part II (15468-15492, 16405-16453).**
* `τ_{0,η} = d_min ε_ht/(20(A_{ht,η}+1))` is defined after the internal orders and before `N`.
* `m` is common; `ω = Δ/2 < Δ = Δ_0`; the functions contain no `T_1`.
* All hypotheses are supplied as stated.

**Dependence on 11/12.** None. The lemma involves only `σ_0`, `β*` and generic exponents. It is in Part I's Section 11 but is not part of Thm 3.1's closure, and it stays on the 7/8 path under either route.

**Verdict.** No wrong step. It is an elementary order-of-quantifiers lemma, correct as stated, with the implicit `τ`-independence of `A_η` supplied by its one Part II application.

## 5. Review of Lemma 19.1 (prime bound in a bin; 15015-15062)

**Statement.** Under the hypotheses of Lemma 8.2, with the prime-annulus Mellin frequency inside its height allowance, the main-slot factor
`Q_i(u; z) = P_i^{−1/2} Σ_{p ∈ 1_T} conj χ_p(u) W_i(q_p/P_i)(q_p/P_i)^{z−1}`
satisfies `|Q_i| ≪_{𝒜,e,ε_1} U^{ε_1} P_i^{a−1/2+O(e)}`. The bound is uniform for `51/100 ≤ a ≤ 1`.

**Check of the proof.**
1. **Characters.** Expanding `1_{p ∈ 1_T} = |T|^{−1}Σ_θ θ(p)` gives prime sums of `p ↦ θ(p)·χ_p(u)^{−1}`. This is `ψ_{u,θ,−1} ∈ 𝒳_u`, since `θ ∈ T̂ ⊂ Θ` (definition at 4229-4233). Correct.
2. **No pole.** Retained rows exclude presentations that induce the principal character (4259-4268). So no `L(s, ψ)` has a pole at `s = 1`, and the prime sum has no main term. This is required for an exponent `a − 1/2 < 1/2`, and it holds.
3. **Contour.**
   * Write the von Mangoldt-weighted annulus as a Mellin integral against `−L'/L(s, ψ_orig)`, starting on `Re s = 2`.
   * On `|Im s| ≤ (3i+2)T_1`, the buffered bin of Lemma 8.1 makes the disks of radius `2 − a − 2e` about `2 + it` zero-free. Lemma 4.9 then gives `L'/L ≪_e log U` on the concentric radius `2 − a − 8e`, whose leftmost point is `a + 8e + it`.
   * The log-derivative of the deleted product is `≪ Σ_{p ∈ E_u} log q_p · q_p^{−0.51} ≪ log U`, because the radical of `E_u` has norm `O_S(q_u)` (4254), so `Σ_{p ∈ E_u} log q_p ≪ log U`.
   * Moving the central segment to `Re s = a + 8e` gives `P^{a+8e} log U` times a fixed `L¹` norm of the Mellin transform.
   * The horizontal joins have bounded length and lie in the controlled region. The tails beyond the truncation height decay like `T_1^{−N}` times `P^2`, by the late tail bounds 1154-1180. Choosing `N` after `τ` makes them negligible, which matches Lemma 8.2's permitted order of choices.
   * Correct.
4. **Twist.** The pure twist `(q_p/P)^{i Im z}` is absorbed into the L-argument rather than into the weight. So the weight's seminorms stay fixed and the cost is height allowance, which the hypothesis grants: Lemma 8.2 permits twist height `(3i+1)T_1` plus `T_1/2` of further frequencies, which is less than `(3i+2)T_1`. Correct.
5. **From Λ to primes.** Dividing by `log(P_i y)` preserves seminorms: `(y∂_y)^j (log(P_i y))^{−1} = (−1)^j j!/(log(P_i y))^{j+1}`, which is bounded for large `P_i`. Prime powers number `O(P_i^{1/2+o(1)})`, which gives `P_i^{o(1)}` after normalization; that is below the claimed bound since `a ≥ 51/100`. Correct.
6. **Normalization.** `P^{−1/2}·P^{a+8e}·U^{o(1)} = U^{ε_1}P^{a−1/2+O(e)}`. Uniformity in the row uses `Q_ψ ≪ U` and `(3+|t|)^2 ≪ U^{1/50}` (Lemma 8.1), and uniformity in `a` uses Lemma 4.9's constants, which are uniform on `[1/2, 1]`.

**Downstream use (15064-15081).** The cap `g_i ≤ δ/2` uses exactly `a − 1/2 = δ/2`. The bound becomes `≤ P_i^{δ/2+ϑ}` after `e` and `ε_1` are reduced; this is legitimate because `log U/log P_i = d/ℓ_i` is bounded on each fixed mesh. SEP30_JUNCTION_CHECK §2 checked the hypothesis instances (`a ∈ [51/100, 11/12]` in Part II).

**Dependence on 11/12.** None. The lemma is uniform for `a ∈ [51/100, 1]`; only its *application* has `a ≤ 11/12`.

**Verdict.** No wrong step. It is the standard bound for smoothed prime sums in a zero-free rectangle. It inherits Lemma 4.9, Lemma 8.1 and the tail bounds of Lemma 4.5. Those proofs are outside this scope; see SEP30_DETECTOR_QUANTIFIERS and SEP30_L13_L45_REVIEW.

## 6. Verdict

**(a) The substitution is valid.**

* Part II uses Thm 3.1 only through `β* ≤ 11/12` (Sec. 1). [O5] thm:main implies that inequality by the definitional bridge B (Sec. 2.3). No family, region or uniformity mismatch was found (Sec. 2.2). In particular:
  * no Größencharacter zeros are needed (Sec. 1.4);
  * the closed endpoint `β* = 11/12` is handled in Part II exactly as before;
  * no quantitative or uniform content of Thm 3.1 is used.
* **Nodes that leave the 7/8 critical path:**
  * Thm 3.1's proof (6783-6805);
  * Lemma 5.8, Lemma 6.1, Lemma 6.2, Prop 6.3, Lemma 9.1, Prop 9.2 and Prop 11.2;
  * three Part-I-only prose blocks (3486-3496, 5905-6012, 6493-6512);
  * the imports BGL and Huxley/Baier–Bansal.
* **Def 5.6 stays.** It is a definition, but it is directly load-bearing through Lemma 5.7 and then Lemma 14.3.
* **Conditions on using this verdict.**
  * The composed route "[OAI] Part II + [O5] thm:main ⇒ [OAI] Thm 1.1" is a new composition. Under AGENTS.md it needs its own independent review, and B together with Sec. 2.2 is the junction such a review must confirm.
  * The bootstrap's trust then rests on the [O5] review record, which is bounded and not independent; its weakest point is prop:R.
  * [O5] and [OAI] share their automorphic input (Sec. 3.3). The substitution shortens the unreviewed text. It does not diversify the risk.
* Nothing here bears on RH.

## 7. Known misreadings

1. **"The 7/8 theorem is now reduced to reviewed material."** No. Part II's 50-odd direct nodes are unchanged by the substitution, and most are unreviewed.
2. **"[O5] supplies more than `β* ≤ 11/12`, e.g. uniform bounds for `1/L`."** No. [O5] is qualitative (R2 F3), and Part II does not need more.
3. **"All nine via-3.1 nodes drop out."** No. Eight drop out. Def 5.6 is used directly.
4. **"`a ≤ β*` (the bin ceiling) comes from Part I."** No. It comes from the definition of `β*` (4370-4383). Only `δ ≤ 5/6` uses 11/12.
5. **"Lemmas 11.1 and 19.1 are Part I lemmas and leave with Thm 3.1."** No. Both are used directly by Part II, and neither depends on 11/12.

## 8. Reproduction

```sh
cd research/exploratory/qrh-2026-10/reviews
P=standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints
git show pr908:$P/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex > /tmp/sep30.tex
git show pr908:$P/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex  > /tmp/oct5.tex
python3 -I part1_substitution_check.py /tmp/sep30.tex /tmp/oct5.tex   # expect: ALL CHECKS PASSED
```

The script authenticates only text-level facts: hashes, citation locations and the presence of statements. It finds a verbal (non-`\ref`) dependency only through its explicit phrase checks. The completeness claim in Sec. 1.2 therefore rests on the reading listed in the header together with the grep for `β*`, `11/12`, `1/24`, `5/6`, `κ` and the bootstrap labels.

# Quasi-RH status and limits dossier (OpenAI 11/12 and 7/8 claims)

```text
Status:  Exploration-layer dossier. It summarises the Observatory's Level-2 section audits of the 11/12 paper
         and adds status, consistency, consequence and method-limit analysis. It is NOT a review approval, NOT an
         integrated packet, and does not certify any claim. RH remains unsolved. The quasi-RH statements below are
         unrefereed claims; "no error found" means only that within the inspected portions we found no error.
Scope:   (i) "The Quasi-Riemann Hypothesis" (OpenAI, 5 Oct 2026; 11/12), the audited object;
         (ii) its 199-page companion (OpenAI, 30 Sep 2026; 7/8), read for structure only, NOT audited;
         (iii) OpenAI's Lean comparator challenges for 7/8 and Siegel zeros, read statically, NOT built or replayed;
         (iv) follow-ups: Liu 2610.12234v2 and 2610.26835v2, Xu-Sang 2610.15291v2, Chang-Wang 2611.00924v1,
              Ji 2611.16665v2, and the input de Faveri 2610.04045v1. Each was read for its statements and
              dependencies only, not audited.
Exact sources or dependencies:
         github.com/openai/math @ 4eaee87548250b2682affda7d05d947c05554bae
           paper2.pdf  sha256 f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18
           paper2.tex  sha256 d9a8f15aa770cf88... (3988 lines; every line number "l.N" below refers to it)
           7/8 paper.tex sha256 42a5ee0febca59fd... (16677 lines; cited as "tex78 l.N")
           lean/docs/003.md sha256 41e52ed718260e6f...; ComparatorChallenges/{QuasiRiemannHypothesis,
           DirichletSevenEighths,HeckeSevenEighths,SiegelZeros}.{lean,json} (lean sha256 prefixes 065f8c9a,
           8fb13ad9, cb5e404f, bedaac02)
         arXiv PDFs (sha256): 2610.12234v2 5ed4bb38...; 2610.15291v2 e881519b...; 2610.26835v2 b3e6d41c...;
           2611.00924v1 6ce4ee86...; 2611.16665v2 dfe108d3...; 2610.04045v1 97720b3c...
         Our audits: ARCHITECTURE.md, audit_S3.md, audit_S4.md, audit_S5.md, audit_S6.md, audit_S7.md,
           audit_APPA.md, audit_APPB.md (this folder); ../lean_replay/README.md; ../claims_2026/SIEGEL/.
         There is no adversarial/ folder and no *_adjudication.md: no adversarial round has been run.
What was actually run: reading only, plus one sympy/numpy script of our own for the exponent algebra in Sec. 4
         (scratchpad dossier_checks/limits.py, run with python3 -I). No code from the OpenAI repository, or from
         any follow-up, was run. No Lean was built.
Smallest remaining gap: the 11/12 theorem rests on (a) the correctness of the imported facts: Patterson's
         coefficient formula and Kubota multiplier as transcribed in Dunn-Radziwill Sec. 5.1 and App. A, and
         Goldmakher-Louvel Thm 1.1; and (b) Prop. 6.2 plus Lemma 6.3 in the form used by Lemma 6.6 (l.1805-1855,
         l.1923-2187). We re-derived (b) and verified it numerically and in exact arithmetic. We did not re-prove (a).
         The 7/8 theorem is unaudited, and its Lean formalization has not been replayed.
```

Labels used below:
- **[P]** proved in paper2.
- **[P-]** stated in paper2 without proof.
- **[A]** checked in one of our section audits.
- **[O]** our own derivation in this dossier. Not reviewed; treat as a sketch.
- **[S]** secondary source: press or a citation inside another preprint. Not checked against the primary.
- **[F]** statement of a follow-up preprint, read but not audited.

---

## 1. Exact claims and their verification status

### 1.1 The claims

| # | Claim (exact) | Source | Proof status in source |
|---|---|---|---|
| Q1 | Every finite-order Hecke L-function over K = Q(√−3) has no zeros in Re s > 11/12. | paper2 Thm 1.1, l.73-75 | [P], conditional only on standard imports (Sec. 1.2) |
| Q2 | Every Dirichlet L-function, including ζ, has no zeros in Re s > 11/12. | paper2 Thm 1.1, l.74; base change l.759-770 | [P]: Q1 plus L_K(s, χ∘N) = L(s,χ)L(s,χχ₋₃) |
| Q3 | sup over 1≤q≤x, (a,q)=1 of \|π(x;q,a) − Li(x)/φ(q)\| ≪ x^{11/12} log x, with an absolute effective constant. | paper2 Cor 1.2, l.84-95 | [P-] ("standard explicit-formula argument") |
| Q4 | "Rules out Landau-Siegel zeros" (abstract l.47, l.141-143). | paper2 | [P-]. Q2 excludes real zeros in (11/12, 1). The classical region 1 − c₀/log(3q) is covered only when log(3q) > 12c₀; finitely many small moduli would need computation (audit_APPB §7). |
| Q5 | n(p) ≪ (log p)^A; deterministic Tonelli-Shanks and Miller test; h(D) ≫ √\|D\|/log log\|D\| effectively; Euler's 65 idoneal numbers complete. | paper2 l.97-125 | [P-]. Not load-bearing. |
| E1 | Same as Q1 and Q2 with 7/8 in place of 11/12. The boundary is excluded and a principal pole at s = 1 is allowed. | 7/8 paper Thm 1.1, tex78 l.106-111 | 199-page proof. **Not audited by us.** Lean formalization claimed (Sec. 1.3). |
| E2 | n(p) ≤ C(log p)^A, and deterministic square roots mod p. | tex78 Cor "nonresidues-square-roots", l.325ff | Stated as a consequence. Outside the Lean scope ("later applications are not included", docs/003.md). |
| L1 | There is an absolute c>0 such that every real zero β∈(0,1) of every primitive nonprincipal real L(s,χ), q≥3, satisfies (1−β) log q ≥ c. | OpenAI "Uniform exclusion of Landau-Siegel zeros", 1 Oct 2026; Lean `SiegelZeros` | Separate elementary proof (see ../claims_2026/SIEGEL). **Also a trivial corollary of E1 or Q2**: β ≤ 7/8 gives (1−β) log q ≥ (log 3)/8 = 0.1373 ([O], one line). |

The two OpenAI proofs are **different arguments**:
- **paper2 (11/12).** Mechanism: a sextic-twisted Möbius mean square (Prop. 3.1, l.679-689), proved by
  - Poisson duality to cubic-Gauss-sum coefficients (Sec. 4);
  - cube completion and cubic-theta reflection to a *quadratic* large sieve (Sec. 6);
  - a two-Poisson transfer (Sec. 7);
  - a finite induction (Sec. 5).
- **7/8 paper.** Mechanism: a family-wide rightmost-zero contradiction (tex78 Prop. "continuation from a common signal", l.399-432). Its ingredients are:
  - a zero detector;
  - a BGL-type sextic large sieve, used only in its Part I;
  - inverse and plain moment inductions;
  - prime compensation.

  Its own Part I proves a *different* 11/12 argument (tex78 l.525ff), with Mellin exponent C_I(s) = s − 2/3.

The Lean formalization covers the 7/8 paper, **not** paper2.

### 1.2 Our audit coverage of paper2 and its outcomes

Every line of paper2 from l.206 to l.3988 was inspected by at least one Level-2 section audit. From the introduction (l.52-205), the statement of Thm 1.1 and its scope were audited; the corollaries Q3 and Q5 were not.

| Region (paper2) | Audit | Outcome | What was verified beyond hand re-derivation |
|---|---|---|---|
| Outline l.206-659 | audit_APPB §2 | Consistent with the detailed proof. 6 presentation items (OUT-P1..P6). | Outline identities B1-B4 and scale algebra C1-C9 |
| Sec. 3, l.660-772 (Prop 3.1 ⇒ Thm 1.1) | audit_S3 | Correct as a conditional deduction. Presentation items F1-F4 (e.g. J=0 for D<7^{6/(1+ϑ)}). | χ_n(p⁶)=1_{p∤n} (24,076 cases); base-change Euler identity (41 characters); Mellin identities |
| Sec. 4, l.773-1253 (Lemma 4.1, Lemma 4.2, Lemma 4.4, Prop 4.5) | audit_S4 | No issue. U-S4-1 (IK04 numbering unchecked) is cosmetic. | End-to-end identity chain M_D → (eq:initial-column-output) with nontrivial ν, relative error ≤ 4e-15; negative controls fail |
| Sec. 5, l.1254-1631 (iteration) | audit_S5 | Induction well-founded; ⌈4/ϑ⌉ levels; constants uniform. P1: the b=1 self-reference is routed through Prop 5.4 and is not circular. | Cube inversion to 2e-16; LP over exponents; 14,355 exact random parameter samples |
| Sec. 6, l.1632-2216 (Prop 5.2) | audit_S6 | No issue. U1-U4 of the architecture map closed. | **Kubota multiplier sign settled**: θ(γw) = (c/a)₃θ(w) to 2e-13, while the conjugate is off by \|1−ω\|. Multiplier three-case formula exact in 80 configurations. Lemma 6.3 uniformity with N(k₀') ~ 1e47. |
| Sec. 7, l.2217-2685 (transfer) | audit_S7 | No issue. | Lemma 7.1, Lemma 7.2 and Lemma 7.3 identities end to end (≤ 1.4e-14); 498,816 range checks |
| App. A, l.2687-3480 | audit_APPA (independent code from S6) | No issue. | 515,936 cases, 0 failures; D1 settled independently; summed local identity with true per-tuple multipliers |
| App. B, l.3481-3988 | audit_APPB | No issue. All four uses meet their hypotheses. | Lemma B.1, B.2 and B.3 instances; derivative-order bookkeeping |

**Aggregate classification across all audits:**

| Classification | Count | Notes |
|---|---|---|
| verified_error | 0 | |
| suspected_gap | 0 | |
| missing_hypothesis | 0 | |
| unresolved_ambiguity | 0 load-bearing | U1-U4 closed by audit_S6 and audit_APPA. U-S4-1 concerns citation numbering only. |
| typo_or_presentation | ≈35, all harmless | See below. |

The presentation items are of three kinds:
- compressed proofs: the multiplier cases at l.3184-3196 and the GL index swap at l.1900-1912;
- unused or vacuous restrictions: ϑ ≤ 1/10 is never used;
- citation-precision points: DR (5.6) cited for κ; Pat77 Table III where DR App. A is meant; five uncited bibliography items.

**What the "no error" verdict rests on (imported, not re-proved by us):**
1. Patterson's coefficient formula, the cusp table and the automorphy of θ on Γ₂ with multiplier (c/a)₃, all as transcribed in Dunn-Radziwiłł §5.1 and App. A. We corroborated these numerically, by building θ from DR (5.6)-(5.8) and testing automorphy. That is not a proof.
2. Goldmakher-Louvel Thm 1.1. We checked the hypotheses of GL Def. 1 for the family x ↦ (x/k)₂κ_λ(x)^{e_k}.
3. Standard facts: Landau's prime ideal theorem, Hecke continuation, L(1,χ₋₃) > 0, Gauss-Jacobi, cubic reciprocity, DLMF 10.43.19, Stirling and Phragmén-Lindelöf.

**Load-bearing points** (ARCHITECTURE.md item 18):
- Prop. 6.2 + Lemma 6.3 as used in Lemma 6.6. The k₀-dependence must be exactly χ_{k₀}³ (a *quadratic* character), the factor N(k₀)² in the weight, and a unimodular scalar.
- The sign of the Kubota multiplier, which makes B_{p,1} = χ_p³ quadratic (l.3252-3253, l.408-411).

Both points were checked by hand, by exact integer arithmetic and by floating-point θ evaluation.

**Caveats on the audits themselves:**
- They were produced by AI agents in this Observatory's workflow. They are not human expert review.
- They do not test any implied constant at asymptotic scale.
- Numerical tests are finite and authenticate identities, not sizes.

### 1.3 OpenAI's Lean formalization: stated scope and what a replay requires

**Scope according to docs/003.md:**
- θ = 7/8 for ζ and for every Dirichlet L-function, uniformly over all moduli and characters, and the same for finite-order Hecke L-functions over Q(√−3).
- Principal poles are excluded.
- "The paper's later applications are not included."
- Separately: a uniform logarithmic real-zero gap (SiegelZeros), with no explicit c.

The doc links only the 7/8 paper and the Siegel-zero paper. Press reports agree that the 11/12 paper is not formalized [S: Quanta, 19 Oct 2026].

**Challenge statements (read statically):**

| Challenge | Statement | Solution module | Fidelity notes [O] |
|---|---|---|---|
| QuasiRiemannHypothesis | `riemannZeta s ≠ 0` for `7/8 < s.re` | `OAI.NumberTheory.DirichletL.Nonvanishing` | Uses Mathlib's `riemannZeta`. Its value at s=1 is a nonzero junk value, so s=1 does not trivialise the statement. Faithful. |
| DirichletSevenEighths | ∀ q (NeZero), ∀ χ : DirichletCharacter ℂ q, 7/8 < Re s, ¬(χ = 1 ∧ s = 1) ⇒ `LFunction χ s ≠ 0` | same | Uses Mathlib's `DirichletCharacter.LFunction`. Covers *imprimitive* χ, which is harmless (Euler factors are nonzero in Re s>0). Faithful. |
| HeckeSevenEighths | `LFunction χ s ≠ 0` for 7/8 < Re s, ¬(χ.residue = 1 ∧ s = 1) | `OAI.NumberTheory.DirichletL.Hecke.Nonvanishing` | **The challenge file defines its own objects.** `Character` is a MulChar on O/𝔪 that is trivial on units (= ray-class characters, since h_K = 1). `LFunction χ s := π^s Γ(s)⁻¹ Λ(s)/6`, where Λ is the completed Mellin transform of a weighted sum of products of shifted and rescaled Hurwitz even kernels. The shifts are (2a−b−Le)/(2L) and (b+Le)/(2L), the scales are L² and 3L², and e ∈ {0,1} accounts for parity, using N(x+yω) = ((2x−y)/2)² + 3(y/2)². Fidelity therefore requires a separate check that, for Re s > 1, this equals Σ_{𝔞≠0} η(𝔞)N𝔞^{−s} = (1/6)Σ_{z∈O∖0} χ(z)N(z)^{−s}. This check is plausible but **not done**. |
| SiegelZeros | ∃ c>0, ∀ q≥3, χ primitive, χ≠1, real-valued, ∀ β∈(0,1), L(β,χ)=0 ⇒ c ≤ (1−β) log q (two theorem names) | `OAI.NumberTheory.SiegelZeros.Main` | Faithful to L1. Note that it follows from DirichletSevenEighths with c = (log 3)/8, but OpenAI proves it in a separate development (≈70k lines; ../claims_2026/SIEGEL). |

Permitted axioms are `propext`, `Quot.sound` and `Classical.choice`, with `enable_nanoda: false`.

**Static facts recorded in ../lean_replay/README.md:**
- Toolchain v4.34.1; Mathlib d13f23b7...
- Import closure of 2,924 modules, ≈486,000 lines, plus PrimeNumberTheoremAnd and RellichKondrachov.
- A text scan found no `sorry`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe` or `opaque`. A text scan is not a proof check.

**What an independent replay requires.** It is blocked here: building runs third-party code and needs explicit permission.
1. Pin the toolchain and the manifest. Verify the patches applied by the lakefile from `lean/patches/`.
2. Run `lake build` on the three solution modules.
3. Run Lean FRO `comparator` with `lean4export`. Preferably also run an independent kernel such as nanoda, which the configs disable.
4. Run `#print axioms` on each challenge theorem.
5. Check statement fidelity by human review. This is easy for the zeta and Dirichlet statements, which use Mathlib definitions. For the Hecke statement, check the custom `LFunction`; ideally prove it equals the Dirichlet series on Re s > 1.
6. Record the hashes of every artifact.

**What a successful replay would establish.** It would establish the zeta and Dirichlet 7/8 statements (and so 11/12, a fortiori) relative to the Lean kernel and Mathlib's definitions, independently of the readability of either paper. It would not certify paper2's argument.

**Status: announced with a claimed formalization; formalization not independently replayed.**

### 1.4 Public expert reception (all [S], secondary)

- **Quanta, 19 Oct 2026 (K. Kakaes), "AI Proved the Quasi-Riemann Hypothesis. What Happens Now?"**
  - Mathematicians focus on the shorter 11/12 version, described as 49 pages, human-edited and not formally verified.
  - Experts "largely agree the result is correct".
  - Radziwiłł can sketch the argument in half a page; private write-ups of 7-13 pages circulate. He calls both papers poorly written.
  - Sarnak will not call it "a Theorem" until humans check all the details.
  - Sawin doubts that the methods reach 1/2. Bloom notes quasi-RH also seemed out of reach weeks earlier.
  - Dunn: the proof is "a synthesis of well-known ideas" and used metaplectic forms "nobody expected".
- **Scientific American, 8 Oct 2026.** Pasten: quasi-RH is "way more than enough for many applications"; on Siegel zeros, "it settles the question".
- **Wikipedia, "OpenAI bulk release of mathematical papers".**
  - Maynard: "putting together some ideas that were not terribly mainstream in an exceptionally clever way".
  - Sarnak repurposed a course to study the proof.
  - Concerns about the bulk release and its exposition.
- **Quanta updates (Oct-Nov 2026).**
  - Lichtman: "the most significant AI-for-math achievement so far, by quite a margin".
  - Granville on Siegel zeros: "It's all moot now".
  - Simpler Siegel-zero proofs (Green with OpenAI's model; Barreto).
  - Commelin cautions that some OpenAI Lean statements prove weaker results than the papers claim.
- **Withdrawals.** Three unrelated OpenAI papers were withdrawn on 7 Oct for a sign error (openai/math history.md). None concerns quasi-RH.

We found **no published report of an error** in either quasi-RH paper (searched 17 Nov 2026). Absence of a report is not verification.

### 1.5 Follow-ups: what they assume and what they re-prove ([F])

| Work | Claim | Assumes | Re-proves or new | Lean |
|---|---|---|---|---|
| Liu, arXiv:2610.12234v2 (12 Oct) | Re s > B_new = 0.874957019420… (root of 1188ξ³−2160ξ²+171ξ+190, B = (18ξ+7)/(18ξ+9)), for Hecke over Q(√−3), Dirichlet and ζ. Also proves "optimality within the explicitly specified exponent comparison system" (Thm 34.4). | All analytic inputs of the 7/8 paper (its Part I recalls them; locators to [Ope26a]). | Varies b, ℓ and κ. Extends the unweighted fourth moment from κ ≥ 3/4 to κ ≥ 13/18 (Part IV, §28). Exact-arithmetic endpoint certificates. | Claimed (Liu GitHub); not checked |
| Xu-Sang, arXiv:2610.15291v2 (15 Oct) | Re s > 8748867/10⁷ = 0.8748867 (Thm 1.1) | Explicitly assumes "the analytic inputs of [OAI26] … including the family-wide 7/8 zero-free half-plane". AI disclosure: "conditional on the correctness of the analytic inputs from [OAI26], whose proofs have not been independently verified here." | A relaxed direct estimate, and an amplified first moment of the reflected numerator (from the 7/8 paper's fourth moment) with a two-stage bootstrap 7/8 → κ=3/4 → B₀ → κ=29991/40000 → B₁. "No claim is made that the resulting exponent is optimal." | — |
| Liu, arXiv:2610.26835v2 (29 Oct) | Re s > B♭ = 0.874886647039964… (quartic 133488B⁴−376596B³+384534B²−167541B+26231 = 0) for finite-order Hecke L-functions over **every number field** (Thm 17.1). B♭ is the exact infimum of the refined comparison system (Thm 14.13). | Liu26a scalar results; Kazhdan-Patterson exceptional theta; GL and BGL sieves; the local calculations of [Ope26b] = OpenAI "Primitive roots for every admissible integer base" (4 Oct 2026, another unreviewed OpenAI preprint); Cureton-Thorner's descent strategy [S]. | Cyclotomic F ⊃ μ₁₂ analogues of the inverse and product moments (§10-12). Its Theorem 10.8 re-derives an 11/12 bound over F by the paper2 extraction. Remark 10.9 locates where the cancellation enters. | "In progress" |
| Chang-Wang, arXiv:2611.00924v1 (31 Oct) | Re s > B* − 1/160000 = 0.87446205769353…, where B* = 0.874468307… is attributed to Liu26c | "Conditional on the cited general-field theta, detector, prior-bound and Mellin input theorems" | An exhaustion-aware product moment | — |
| Newton (Zenodo, 16 Oct) [S, cited in Liu26b] | 0.87488664962, plus a barrier 0.8748866496166… in a fixed-κ system | 7/8 inputs | Parameter certificate | — |
| Cureton-Thorner (Axiom, "hexagon:2610.00200v2") [S, cited in Liu26b] | Re s > 31/32 for ζ_K and finite-order Hecke L over **every number field** K, via K(ζ₁₂) and abelian descent | Not read | Not read | [CTLean], claimed; not checked |
| Ji, arXiv:2611.16665v2 (15 Nov) | ζ_{Q(i)}(s) ≠ 0, hence ζ(s) ≠ 0, for Re s > 599/600 (Thm 1.1). Only this one Dedekind zeta. | The quartic Kubota series of angular weight 1 and its functional equation (David-Dunn-Hamieh-Lin, arXiv:2306.11875 Prop. 4.3), and **de Faveri's zero-density estimate** (arXiv:2610.04045 Cor. 1.5, unrefereed). Does not use OpenAI's results. | A quartic analogue over Z[i]: two Poisson steps, reflection, and a fourth-power-row main term. The exponent comes from H = X^{65/144}, Y = X^{1/288} and the de Faveri exponent E(σ) (Lemma 4.3). | — |
| de Faveri, arXiv:2610.04045v1 (2 Oct) (an input, not a follow-up) | Θ_n(A,B) ≪ (AB)^ε (A + B + A^{1−1/n}B^{2/n} + A^{2/n}B^{1−1/n}) for n-th-power-free n-th order Hecke families, n ≥ 3 (Thm 1.1). This is conjecturally optimal, with matching lower bounds for n = 3, 4 [DR under GRH; de Faveri-Dunn-Hoffstein unconditionally]. Also a zero-density estimate (Cor 1.5). | — | — | — |

**Reading of the follow-ups.**
- None of them reports an error in paper2 or in the 7/8 paper.
- Every improvement below 7/8 (Liu, Xu-Sang, Newton, Chang-Wang) **imports the 7/8 paper's analytic inputs**. Each is a reparametrisation or a local strengthening of one estimate. None is an independent verification.
- Liu 2610.26835 and Cureton-Thorner are the only ones that redo analytic work in a new setting (cyclotomic F ⊃ μ₁₂). Liu's version depends on another unreviewed OpenAI preprint.
- Ji's argument is the only *independent route*. It is quartic over Q(i) and gives a far weaker exponent, 599/600.

The Siegel-zero follow-ups (Banks 2610.15483, Kerr 2610.21099, Guo 2610.30476, Banks 2610.31402) concern L1. They are audited in ../claims_2026/SIEGEL. That audit found no error and did no Lean replay.

---

## 2. Consistency with known obstructions

### 2.1 Davenport-Heilbronn: where the Euler product is used

The Davenport-Heilbronn function (a combination of L(s,χ), L(s,χ̄) mod 5 with a functional equation) has zeros in Re s > 1. Hurwitz ζ(s,a) and Epstein zeta functions of class number > 1 also have zeros off the line. So no argument that uses only a functional equation, analytic continuation and Dirichlet-series shape can give a quasi-RH. paper2 uses multiplicativity at the following load-bearing points [A]:

1. **Coefficients of 1/L** (l.726-757). Σ μ(𝔫)ν(𝔫)N𝔫^{−s} = 1/L_K^S(s,ν) is the Euler product. The Littlewood principle detects zeros through the Möbius coefficients, which are multiplicative and supported on squarefree ideals.
2. **Row extraction** (l.695-705). χ_𝔫(p⁶) = 1_{𝔭∤𝔫} uses complete multiplicativity of the sextic symbol in its modulus. Then A_{p⁶} − A₁ = Σ_{𝔭|𝔫}μν W, a statement about multiples of 𝔭, which uses that μ vanishes off squarefree ideals and is multiplicative.
3. **The Möbius-to-Gauss conversion** (Lemma 4.1, l.823-857: (eq:gj) γ₂(n)³ = μ(n)α(n), l.842; (eq:convert2) μγ₋₁ = χ_n(−1)G⁻¹ ᾱ γ₂, l.850). The Möbius function equals, up to an angle and a ray-class phase, the cube of a cubic Gauss sum (Hasse; J(χ²,χ²) = −p). This holds prime by prime and extends to squarefree n only through CRT twisted multiplicativity, (eq:crt-a) a_ξ(ab) = a_ξ(a)a_ξ(b)χ_b(a)⁴ (l.851). The coefficients of 1/f for the Davenport-Heilbronn function f are not multiplicative and satisfy no such identity.
4. **Lemma 4.4 and Lemma 5.3** (l.962-992, l.1341-1467) use complete multiplicativity of Ψ_k and Möbius inversion over the cube index.

**Conclusion [O]:** there is no tension with Davenport-Heilbronn. The proof cannot be applied to non-Euler-product Dirichlet series.

### 2.2 The parity barrier

A bound Σ μ(𝔫)ν(𝔫)W(N𝔫/D) ≪ D^{Θ+ε} is parity-sensitive, so it cannot come from sieve axioms (Selberg's parity barrier). paper2 obtains it without a sieve. The parity information enters through two steps:
- the *algebraic identity* μ = ᾱγ₂³ (up to phases);
- the *automorphy* of Patterson's cubic theta function, whose coefficient formula (l.363-366) encodes arithmetic information from residues of Eisenstein series.

The only analytic inequality is the GL quadratic large sieve. This mirrors in reverse the way Heath-Brown and Patterson (1979) handled cubic Gauss sums at primes. Our reading is that the argument contains no step that a parity objection would forbid [O].

### 2.3 Large-sieve lower bounds (generic coefficients cannot work)

For generic coefficients, the sextic large sieve cannot have the "orthogonal" shape A + B:
- de Faveri's conjecturally sharp bound has the extra term A^{5/6}B^{1/3} for n = 6;
- Xu's companion manuscript (cited in Xu-Sang §1.1 [S]) claims a matching lower bound A^{5/6}B^{1/3} for squarefree sextic matrices with B^{16/11+δ} ≤ A ≤ B^{2−δ};
- DR Thm 1.4 (under GRH) and de Faveri-Dunn-Hoffstein (unconditionally) give lower bounds for n = 3, 4.

paper2 is consistent with all of this. Its only large sieve is *quadratic* (GL), applied after the theta reflection turns χ_p⁻¹χ_p⁻² into χ_p³ (l.408-411, l.1735-1742). The two features that avoid the (AB)^{2/3}-type terms are specific to its coefficients:
1. the angular factor ᾱ, which kills the constant terms (Patterson bias), so that T(s,Ψ) is entire (l.3344-3369);
2. the reflection to a quadratic family.

Liu (2610.26835, Remark 10.9) independently gives the same diagnosis: "For arbitrary coefficients the cubic large sieve retains (AB)^{2/3} … The present argument avoids that term only through items (2) and (3), which use the specific theta coefficients."

### 2.4 Ω-results, zero statistics and numerics

No known result conflicts with zero-freeness in Re s > 7/8. The relevant facts:
- **Ω-results.** ψ(x) − x = Ω±(x^{1/2} log log log x) (Littlewood); M(x) = Ω(x^{1/2}); L(1,χ) = Ω(1/log log q) (Chowla); n(p) = Ω(log p · log log log p) (Graham-Ringrose). All are compatible with the claimed O(x^{7/8+ε}), L(1,χ) ≫ 1/log log q and n(p) ≪ (log p)^{O(1)}. For L(1,χ) and h(−d) the consequence would be sharp up to constants.
- **Zero statistics.** Proportions of zeros on the line, pair correlation and low-lying zeros constrain only zeros near Re s = 1/2 or their spacing. They impose no lower bound on N(σ,T) for σ > 1/2.
- **Numerics.** Numerical RH for ζ (up to height ≈3·10¹²) and numerical GRH for small moduli are consistent.
- **Universality.** Voronin universality in 1/2 < σ < 1 approximates only non-vanishing targets, so it is consistent.

### 2.5 Consistency with GRH, and the strength of Prop. 3.1

For fixed u, 𝔫 ↦ (u/𝔫)₆ is the Artin symbol of K(u^{1/6})/K. So A_u(D) is a smoothed Möbius sum for a finite-order Hecke character of conductor ≪ N(u).
- Under GRH, |A_u(D)| ≪ D^{1/2+ε}N(u)^ε, and Prop. 3.1 follows [A, audit_S3 §4]. Prop. 3.1 is "GRH on average" for the sextic twist family at rows N(u) ≤ D^{1+ϑ}, i.e. at or just above the diagonal.
- Heuristically [O], Prop. 3.1 is of **density-hypothesis strength** for that family. If L(s, νχ_·(u₀)) has a zero with β ≥ σ that a detector can see at length D ≍ N(u₀), the (H/N u₀)^{1/6} rows u₀a⁶ all carry a sum of size D^{σ}. Then #{u₀ ~ U : such a zero} ≲ U^{2−2σ+ε}.
- This exceeds what generic large-sieve zero-density gives (de Faveri Cor. 1.5 has exponent 1−δ₆(σ), e.g. ≈0.73 at σ = 3/4 against 0.5 for DH). That is not a contradiction: paper2 uses the special Möbius/theta structure, not a generic sieve. But it shows that Prop. 3.1 is a very strong statement, so all the risk sits there [A, audit_S3 §7].

### 2.6 Scope boundaries

- **Finite order only.** The target ν must be a finite-order (ray-class) character, because Ψ = ν̄G is expanded in the characters of a fixed finite ray class group (l.809-821, l.1063-1064).
  - Not covered: Grössencharacters of infinite order (e.g. L-functions of CM elliptic curves over Q(√−3)), GL(2) and higher-degree L-functions, and non-abelian Artin L-functions (except as factors of ζ_L for L abelian over K).
- **Uniformity.** The half-plane is uniform in conductor and height; the constants are not. The proof is qualitative (derivative orders ≈ 4^{4/ϑ}, audit_S5 P4), so it gives **no explicit zero-free region** beyond the half-plane itself.

---

## 3. Consequences if correct

Write Θ ∈ {11/12 (paper2), 7/8 (7/8 paper)} for a half-plane free of zeros of all Dirichlet L-functions, and of all finite-order Hecke L-functions over K = Q(√−3). Every consequence below is classical conditional technology with GRH replaced by "no zeros in Re s > Θ". Status labels are given per item.

| Consequence | Precise form | Status |
|---|---|---|
| Zero density | N(σ,T,χ) = 0 for σ > Θ, for every χ; likewise every family count Σ_{q≤Q}Σ_χ N(σ,T,χ). Nothing new in 1/2 < σ ≤ Θ. DH for ζ was already known for σ ≥ 25/32 (Bourgain) [standard, not re-verified], so the theorem does not touch the open range. | [O], immediate |
| Primes (PNT error) | ψ(x) = x + O(x^Θ log²x) and π(x) = Li(x) + O(x^Θ log x). Equivalently (Möbius) M(x) ≪ x^{Θ+ε}. Quasi-RH(Θ) ⇔ ψ(x) − x ≪ x^{Θ+ε}. | [O], standard explicit formula |
| Primes in APs | ψ(x;q,a) = x/φ(q) + O(x^Θ log²(qx)), uniformly and effectively. Nontrivial for q ≤ x^{1−Θ−ε}: x^{1/8} for 7/8, x^{1/12} for 11/12. This compares with Siegel-Walfisz (q ≤ (log x)^A, ineffective) and GRH (q ≤ x^{1/2−ε}). It does not improve Bombieri-Vinogradov. paper2's Cor. 1.2 is the π-version with Θ = 11/12. | [P-] for 11/12; [O] |
| Lindelöf to the right of Θ | μ(σ) = 0 for σ > Θ, i.e. ζ(σ+it) ≪ t^ε. The proof is Borel-Carathéodory plus Hadamard three circles on log ζ, the argument of "RH ⇒ LH" (Titchmarsh §14.2) run from the line Θ. Also 1/ζ ≪ t^ε there, and the analogues for L(s,χ) in the q-aspect. With μ(1/2) ≤ 13/84 and convexity, μ(σ) ≤ (13/84)(Θ−σ)/(Θ−1/2) on [1/2, Θ]. | [O] |
| Short intervals | **No improvement in exponents.** Directly, h ≥ x^{Θ+ε}, which is far worse than Baker-Harman-Pintz x^{0.525}. With zero-density estimates N(σ,T) ≪ T^{A(1−σ)+ε}, the standard argument gives ψ(x+h)−ψ(x) = h(1+O(x^{−δ})) for h ≥ x^{1−1/A+ε}. The half-plane upgrades the o(h) error to a power saving, but A is still needed for σ ≤ Θ, and Guth-Maynard's 30/13 is attained below 7/8. | [O] |
| Linnik constant | Directly, p(q,a) ≪ q^{1/(1−Θ)+ε}: L = 8 for 7/8 and L = 12 for 11/12, worse than Xylouris's L = 5. Combined with a single-modulus density estimate Σ_{χ mod q} N(σ,T,χ) ≪ (qT)^{c(σ)(1−σ)+ε} for σ ≤ Θ (ε-losses are harmless because 1−σ ≥ 1−Θ), L ≤ max(2, sup_{σ≤Θ} c(σ)) + ε. With Montgomery's c = 3/(2−σ) this gives L ≤ 3/(2−Θ) + ε = **8/3 + ε** for 7/8 and 36/13 + ε for 11/12. Under DH in the q-aspect, L = 2 + ε (the GRH value). | [O], sketch; the Montgomery density theorem is used as remembered and not re-verified |
| Least quadratic nonresidue | n(p) ≪ (log p)^{1/(1−Θ)+ε}: exponent 8 for 7/8 and 12 for 11/12. This proves Vinogradov's n(p) ≪ p^ε. It follows from the explicit formula for Σ Λ(n)χ(n)w(n/y), using \|ρ\| ≥ 1−Θ and that zeros with \|γ\| ≤ 1 number ≪ log p. It gives deterministic polynomial-time square roots (Tonelli-Shanks) and the Miller primality test. | [P-] ("fixed power"), E2; exponent [O] |
| Siegel zeros and class numbers | No real zero in (Θ, 1). (1−β) log q ≥ (log 3)/8 for all q ≥ 3, so the Lean `SiegelZeros` statement is trivial from E1. Effective L(1,χ) ≫ 1/log log q (Littlewood) and h(−d) ≫ √d/log log d, effectively. Effective Siegel-Walfisz, as in the APs row. Euler's idoneal list is complete via Elsenhans-Klüners-Nicolae plus Grube (paper2 l.116-125). | [P-] / [O] |
| Chebotarev with power saving | ζ_L has no zeros in Re s > Θ when L/Q is abelian (a product of Dirichlet L) or L ⊇ K with L/K abelian (a product of Hecke L over K). By Deuring reduction (all its factors are factors of ζ_L), π_C(x, L/Q) = \|C\|/\|G\| Li(x) + O(x^Θ log(d_L x^{n_L})) for every Galois L/Q with LK/K abelian. Examples: ring class fields of orders in K; the Galois closures K(∛m) of pure cubic fields (S₃ over Q); and division fields K(E[n]) of CM elliptic curves with CM by Z[ω]. **Not covered:** e.g. S₃ fields whose quadratic resolvent is not Q(√−3), and general non-abelian extensions. Liu and Cureton-Thorner would cover all number fields, but those claims are conditional and unreviewed. | [O] |

**What is NOT implied:**
- RH and GRH: zeros with 1−Θ ≤ β ≤ Θ remain possible.
- The density hypothesis for σ ∈ (1/2, Θ].
- Lindelöf on the critical line (μ(1/2) = 0).
- Improved exponents for primes in short intervals or almost-all short intervals.
- Bombieri-Vinogradov or Elliott-Halberstam beyond level 1/2.
- GRH-strength APs (q up to x^{1/2}).
- Nonvanishing at s = 1/2, and pair-correlation or GUE statistics.
- Artin's primitive-root conjecture. Hooley's proof needs GRH-quality Chebotarev for non-abelian Kummer fields over a long range of k; OpenAI claims Artin separately, via another preprint.
- Anything for infinite-order Grössencharacters, GL(n≥2) L-functions, or Dedekind zeta functions of non-abelian fields (beyond the abelian-over-K class above).

---

## 4. The method's limit

### 4.1 Where 11/12 comes from (paper2), and why it is a hard floor for that architecture

**Extraction lemma (l.694-724).** Let H = D^h with h ≥ 1, and suppose the full-row mean square

  Σ_{0<N(u)≤H} |A_u(D)|² ≪ D^{1+ε} H,  where A_u(D) = Σ μ(𝔫)ν(𝔫)χ_𝔫(u)W(N𝔫/D) and χ_𝔫(u) = (u/𝔫)_n,

holds for an order-n residue-symbol family. Averaging over the ≍ H^{1/n}/log H rows u = p^n gives |A₁(D)|² ≪ D^{1+ε}H^{1−1/n} + D²H^{−2/n}, hence

  **β ≤ β(n,h) = 1/2 + h(n−1)/(2n)**,  so that at h = 1+ϑ, β(n,1+ϑ) = 1 − 1/(2n) + ϑ(n−1)/(2n).

This was checked symbolically (dossier_checks/limits.py; audit_S3 C4):

| n | β(n, 1) | Remark |
|---|---|---|
| 6 | 11/12 | paper2 |
| 4 | 7/8 | |
| 3 | 5/6 | |
| 2 | 3/4 | |

Liu (2610.26835, Lemma 10.10) states the general row form: Σ_{u ~ U, sixth-power-free} |M_u(U^r)|² ≪ U^{e(r)+ε} with e(r) = max{1, (1+5r)/6}.

**Why h ≥ 1 is forced [O, from the structure of Secs. 4-7].** Every step of paper2 except the GL large sieve is one of three things:
- an exact identity;
- a positivity enlargement;
- Cauchy-Schwarz.

For H < D the duality of Prop. 4.5 sends the rows to H_dual ≍ D²/H > Σ = XF. There the dual mean square's *diagonal* alone is ≍ H_dual. Fed back through (eq:weighted) (l.1235-1246), it returns Σ|A_u|² ≍ DH + D². That is the large-sieve barrier: the target DH is smaller than D².
- The positive gap H_dual ≤ ΣD^{−κ} (eq:positive-gap, l.1263) is exactly the condition H ≥ D^{1+2κ}.
- So with sextic rows, 11/12 is the floor of this architecture, as the paper itself says and audit_S3 confirms.
- A single twisted character with a zero at β forces only H^{1/6}D^{2β} ≪ DH, so the extraction is also tight on the signal side.

**Why order 6.** The duality turns μ·(u/𝔫)₆ into γ₋₁ (sextic Gauss sums). Only for this order does Gauss-Jacobi (eq:gj)/(eq:convert2) eliminate μ, leaving ᾱγ₂: a *cubic* Gauss sum, i.e. a Fourier coefficient of Patterson's cubic theta function, whose coefficients are explicitly known with no coprimality condition (l.363-366).
- For n = 2 the duality is self-dual: the dual coefficients are again Möbius-type, so there is no handle.
- For n = 3 the dual coefficient is μ·(cubic Gauss sum). It keeps μ, and Patterson-type biases (DR Thm 1.1) show that Gauss-sum averages without the angle twist need not cancel.

So the smaller n that would give a better floor are exactly the ones where the mechanism has no automorphic substitute [O].

### 4.2 Where 7/8 comes from (7/8 paper), and Liu's "optimality"

**The comparison system.** In the 7/8 architecture (as parametrised by Liu 2610.12234 (0.1), Xu-Sang §1.3, Liu 2610.26835 Intro and Chang-Wang (1.2)), all of them take:
- the direct estimate |J_η(Z)| ≪ Z^{l_x/2 + b/12 + ε};
- the principal Mellin term with C_b(s) = s − (4+b)/6;
- l_x = (1−b−ℓ)/2 and l_y = (1+b−ℓ)/2.

Matching the two gives

  **B(ℓ) = 11/12 − ℓ/4**,  where ℓ is the total exponent of the selected (amplifying) prime lengths.

The 7/8 paper takes ℓ = 1/6 (b = 1/8; tex78 l.6860, l.15511-15520), so B = 11/12 − 1/24 = 7/8. ℓ = 0 recovers the balanced 11/12 of tex78 Part I, where C_I(s) = s − 2/3.

**Structural floor [O].** Positivity of both averaging lengths forces ℓ < 1 − |b|. Hence B(ℓ) > 11/12 − 1/4 = **2/3**, however good the nonprincipal estimates are. Reaching 3/4 needs ℓ = 2/3; reaching 1/2 would need ℓ = 5/3, which is impossible in this system. To go below 2/3 the direct estimate itself (the low side: reflected energy plus the additive Gram bound) must change shape.

**What actually limits ℓ.** The nonprincipal Poisson rows must keep a target-independent power saving. Rows with a zero near β_* produce simultaneous large inverse and plain polynomials (the zero detector). Their number is bounded by:
- the inverse moment with prime factors (Liu 2610.26835 Thm 11.2: Σ_{N k≤CZ^m} |M_k(Z^r)Q_k|² ≪ Z^{m+ε} under r+2z < m and 2r+8z < 3m);
- the plain fourth moment, whose prime-amplification cost κ is licensed by the bootstrap β_* ≤ (1+κ)/2 (Xu-Sang App. A; Liu Part IV extends κ down to 13/18).

**Liu's optimality theorems, precisely ([F]):**
- **2610.12234 Thm 34.4.** Within the explicitly specified system, the infimum of attainable boundaries is B_new = 0.874957019… The system is: the supplied uniform upper bounds (the direct majorant with free total length, the stated inverse, plain and count estimates), all permitted detector cutoffs and contour choices, and κ ∈ [13/18, 1] with B ≤ (1+κ)/2.
  - The proof isolates a critical class (δ_c, x = 1/2) whose counting exponent is ≥ 2/3 for every cutoff. This forces three affine inequalities; a positive combination eliminates the lengths; and B ≤ (1+κ)/2 then forces B ≥ B_new.
  - Liu's own caveat: it "concerns the supplied uniform upper bounds and does not exclude improvements from stronger analytic estimates."
- **2610.26835 Thm 14.13.** With Xu-Sang's averaged numerator added, the infimum is B♭ = 0.874886647039964…, unattained by finite chains from above. Thm 15.4: the pointwise-numerator system has optimum B_new.
- **Later work.** Newton's 0.8748866496166… is a barrier for a fixed-κ-range system. Chang-Wang's 0.87446205… comes from a modified product moment.

**Interpretation [O].** "Optimality" means the optimum of a finite-dimensional, semi-algebraic program whose analytic inequalities are held fixed. It is not an upper bound on what the ideas can give. The tiny spread (0.8745-0.8750) shows that, with the current moment and count inputs, the bootstrap fixed point lies essentially at 7/8. The gains come from second-order effects.

**De Faveri's sharper sieve.** In the 7/8 paper the BGL sextic large sieve (K + D + (KD)^{2/3}, tex78 l.4707-4718) is used **only in Part I** (l.5181, 5305, 5327, 5921, 6621). We recomputed the Part I row envelope:
- with BGL, R(δ) = min{1, max(1−δ/2, 4/3−δ)}, which matches tex78 l.5195-5197 [O, limits.py];
- with de Faveri's Thm 1.1 for n = 6, the r = 1 branch drops to min{1, max(1−δ/2, 7/6−δ)}.

This would widen Part I's margins (the 11/12 stage) but **would not move 7/8 by direct substitution**. The Part II counts (tex78 Prop. "Row counts from the witnesses", l.15185) come from the inverse and plain moments, and Liu's critical class lives there.

### 4.3 Explicit conjectural inputs that would push the exponent down

Each statement is for every fixed finite-order ν, smooth compactly supported W, and ε > 0. The implications are [O] via the extraction or comparison formulas above.

- **(C1) Sub-diagonal sextic Möbius mean square (K = Q(√−3), order 6).** For 0 < h < 1:
  Σ_{0<N(u)≤D^h} |Σ_{(𝔫,S)=1} μ(𝔫)ν(𝔫)(u/𝔫)₆ W(N𝔫/D)|² ≪ D^{1+h+ε}.
  - It implies zero-freeness for Re s > 1/2 + 5h/12. Setting h = 9/10 gives 7/8, h = 3/5 gives 3/4, and h → 0 gives 1/2.
  - It is implied by GRH for the twists νχ_·(u).
  - It lies beyond the large-sieve barrier. Any positivity-plus-duality proof returns D², so it needs cancellation *between* the dual diagonal and off-diagonal terms. Nothing in paper2 provides that.
- **(C2) Full-row Möbius mean square of order n < 6.** Over a field containing μ_n:
  Σ_{0<N u≤D^{1+ϑ}} |Σ μν(u/𝔫)_n W|² ≪ D^{2+ϑ+ε}.
  - Implied exponents: 7/8 for n = 4 (e.g. over Q(i), Ji's setting), 5/6 for n = 3 (over K), 3/4 for n = 2 (any field, including square rows).
  - The required new input is a duality partner. For n = 4: an explicit quartic metaplectic theta or Kubota coefficient structure that removes μ, as (eq:convert2) does for n = 6, together with a quadratic or optimal reflected large sieve. Ji's zero-density substitute reaches only 599/600.
  - For n = 3: square-root cancellation for Möbius-weighted cubic Gauss sums with a suitable angular twist (a Patterson-type statement for μ·g̃).
  - For n = 2: an optimal Möbius large sieve over *all* rows including squares. It is self-dual, so no known mechanism applies.
  - To our knowledge, explicit Fourier coefficients of n-fold metaplectic theta functions are known only for n = 2 and 3 [standard; not re-verified]. This is the concrete obstruction for n ≥ 4.
- **(C3) Inputs for the 7/8-type comparison system** (Q(√−3), or cyclotomic F ⊃ μ₁₂ following Liu). Below the current ≈0.8745, at least one of the following is needed:
  - (a) a counting estimate for the critical simultaneous-large-value class (δ_c, x = 1/2) with exponent < 2/3. This means a stronger inverse moment with prime factors, beyond r + 2z < m, 2r + 8z < 3m, or a stronger plain fourth moment;
  - (b) the plain fourth moment at κ < 13/18, where the bootstrap needs κ = 2B − 1, so κ = 1/2 for B = 3/4;
  - (c) a direct (low) estimate that breaks B(ℓ) = 11/12 − ℓ/4. Without (c) the system cannot go below 2/3. Reaching 3/4 needs ℓ = 2/3 with the nonprincipal rows still saving a power.
- **(C4) Generic sieves cannot replace the special coefficients.** With de Faveri's (conjecturally sharp) Θ₆(A,B) ≍ A + B + A^{5/6}B^{1/3} + A^{1/3}B^{5/6} in place of the special-coefficient bound, the paper2 extraction gives only the trivial bound. Any further progress must keep using the angular theta coefficients (§2.3).
- **(C5) Toward 1/2.** Every input above that reaches 1/2 is of GRH strength for a family: (C1) with h → 0, or (C3)(b)-(c) in the limit. Nothing in either paper indicates a route; Sawin's skepticism [S] agrees.

---

## 5. Recommendations for researchers

1. **Status vocabulary.**
   - The 11/12 result: "unrefereed; Level-2 section-by-section audited by the Observatory (AI agents) with no error found; imported metaplectic and large-sieve inputs not re-proved".
   - The 7/8 result: "unrefereed, unaudited here; Lean formalization claimed, not replayed".
   - Do not call either a theorem in reviewed packets, and do not describe RH as advanced beyond quasi-RH.
2. **The fastest route to certainty is the Lean replay** (§1.3), done with explicit permission. Include comparator and an independent kernel. For HeckeSevenEighths, a proof that the custom `LFunction` equals the Dirichlet series on Re s > 1. A successful replay certifies the zeta and Dirichlet 7/8 statements, and hence 11/12, independently of either paper's exposition.
3. **Human verification targets for paper2.** In order of risk:
   - (i) DR's transcription of Patterson's Thm 8.1 and the Kubota multiplier (c/a)₃ against Patterson (1977) itself, not only DR;
   - (ii) GL Thm 1.1 for the family (x/k)₂κ_λ^{e_k} (Def. 1);
   - (iii) the multiplier case analysis l.3175-3196 and Lemma 6.3;
   - (iv) Lemma B.2 constants.

   Our numerics cover (i) and (iii) at small sizes only.
4. **Treat the sub-7/8 literature as conditional.** Liu, Xu-Sang, Newton and Chang-Wang all import the 7/8 inputs. Liu's all-fields result also imports another unreviewed OpenAI preprint. "Optimality" there is optimality of a fixed inequality system.
5. **Research directions.** These are well-posed and testable.
   - (a) Write the half-page human proof of 11/12 that Radziwiłł reports, and identify its minimal imports.
   - (b) Decide whether de Faveri's sieve or the DR/dFDH structure can enter Part II of the 7/8 argument, not just Part I.
   - (c) Attack (C2) for n = 4 over Q(i): an explicit-coefficient quartic substitute would give 7/8 by the *short* paper2 route.
   - (d) Quantify the density-hypothesis consequence of Prop. 3.1 for the sextic family (§2.5) as a separate, checkable theorem. A violation found numerically would falsify Prop. 3.1.
   - (e) Map the consequences table of §3 (Linnik 8/3 + ε, n(p) ≪ (log p)^{8+ε}, Lindelöf right of Θ) into precise lemmas with full proofs before citing them.
6. **Do not over-read the consequences.** The theorem does not improve short-interval exponents, Bombieri-Vinogradov, or the density hypothesis below Θ. The genuinely new consequences are uniform, effective error terms (APs to modulus x^{1−Θ}, Siegel-type effectivity, Lindelöf right of Θ, small nonresidues).
7. **Next pipeline step.** Run an adversarial round on this dossier and on the audits (an adversarial/ folder with *_adjudication.md). None exists yet.

---

## 6. Sources (secondary items are labelled)

- **OpenAI preprints** (openai/math @ 4eaee875): The Quasi-Riemann Hypothesis (5 Oct 2026, paper2); The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8 (30 Sep 2026); Uniform exclusion of Landau-Siegel zeros (1 Oct 2026); lean/docs/003.md; lean/ComparatorChallenges/{QuasiRiemannHypothesis, DirichletSevenEighths, HeckeSevenEighths, SiegelZeros}.{lean,json}.
- **arXiv:**
  - B. Liu 2610.12234v2 and 2610.26835v2;
  - Y. Xu, H. Sang 2610.15291v2;
  - X. Chang, H. Wang 2611.00924v1;
  - X. Ji 2611.16665v2;
  - A. de Faveri 2610.04045v1;
  - Dunn-Radziwiłł 2109.07463;
  - Goldmakher-Louvel 1112.1642;
  - Blomer-Goldmakher-Louvel 1112.1650.
- **[S] press:**
  - [Quanta, 19 Oct 2026](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/);
  - [Quanta updates](https://www.quantamagazine.org/update/169054/), [Quanta updates](https://www.quantamagazine.org/update/168664/);
  - [Scientific American, 8 Oct 2026](https://www.scientificamerican.com/article/the-most-exciting-claims-from-openais-heap-of-new-proofs/);
  - [Wikipedia: OpenAI bulk release of mathematical papers](https://en.wikipedia.org/wiki/OpenAI_bulk_release_of_mathematical_papers);
  - [Science, 13 Oct 2026](https://www.science.org/content/article/ai-edges-closer-solving-riemann-hypothesis-one-math-s-hardest-problems) (page not retrievable here: HTTP 403).
- **[S] cited only inside Liu 2610.26835:** Cureton-Thorner (Axiom) hexagon:2610.00200v2 and CTLean; Newton, Zenodo 10.5281/zenodo.23414581; Liu hexagon:2610.00655v1; OpenAI "Primitive roots for every admissible integer base" (4 Oct 2026).

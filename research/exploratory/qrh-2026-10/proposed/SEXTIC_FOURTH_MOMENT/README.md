# PROPOSED packet draft: Lemma 18.1 of the Sep 30 manuscript as a standalone sextic fourth-moment theorem

```text
Status: PROPOSED integration packet draft. This is NOT an integrated packet and assigns no verdict.
  The statement is an IMPORTED external claim: Lemma 18.1 (lem:plain, "Fourth moment with short
  prime factors") of the external, unreviewed manuscript "The Quasi-Riemann Hypothesis: A Zero-Free
  Half-Plane Re(s) > 7/8" (OpenAI, 30 Sep 2026). Three bounded agent reviews together read every
  proof line and found no wrong step. No independent exact-SHA review has been done, no human has
  reviewed any part, and no integrator has acted on it.
Scope: case 1 (z = 0) of Lemma 18.1, read as a standalone theorem: a Lindelof-strength mean square
  of products of two smoothed sextic character sums over all nonprincipal element rows of Z[omega].
  Section 2.4 records what the general statement and case 2 add. This draft does not extract an
  L-value fourth moment (Section 2.3 explains why), does not propose the 7/8 theorem, and does
  not bear on RH.
Exact sources or dependencies: paper.tex at ref pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
  SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (16,677 lines), read as
  untrusted data. Review files at commit c8515d4ea045e7b685f53feb6dd801bf0f529211 on branch
  claude/peaceful-faraday-ki4ewu (hashes in Section 1). Helper lemmas and imported theorems are
  in Section 4. Literature in Section 9 is from arXiv e-print sources fetched for this draft.
What was actually run: the manuscript was re-extracted and re-hashed; all review files and scripts
  were re-hashed; seven scripts were rerun (five in full, sep30_sec4_checks.py in quick mode,
  lemma18_moments.py on three small K), all passing; see CHECKS.md. Statement, definitions and section boundaries were re-read from the
  source for this draft; the remaining line ranges are taken from the reviews, which cite the
  same hash. No new mathematics was reviewed.
Smallest remaining gap: an independent exact-SHA review of the centred Theta-row stage
  (Lemmas 18.2-18.3 and (old-eq:2.18)-(2.19), paper.tex 13953-13996, 14312-14778), together with
  the two Gauss/reciprocity helpers Lemmas 4.3-4.4 (841-1070); these have since had one bounded
  review (../../reviews/SEP30_L42_44_REVIEW.md, no wrong step; see the note after Section 10). See
  Sections 8 and 10.
```

RH remains unsolved. This draft does not claim that it is proved or disproved, and it does not
claim the manuscript's 7/8 theorem. It concerns a moment estimate for one family of Hecke
characters. A fourth-moment bound, even an optimal one, says nothing about zeros on or off the
critical line by itself.

## 0. What this draft is and is not

* It is a **separately labelled proposed object**, as [AGENTS.md](../../../../../AGENTS.md) asks
  under "Before extending an integrated packet". It collects what an integrator and an independent
  reviewer would need: the frozen source, the exact statement, the helper lemmas and imported
  theorems, the dependency chain, the review record, scope boundaries and known misreadings.
* It is **not** under `research/integrated/` and it does not change the accepted record. None of
  the following integration requirements of [AGENTS.md](../../../../../AGENTS.md) is met yet:
  * one exact frozen source commit;
  * an exact-SHA independent review;
  * readable mathematics physically resident under `research/integrated/`;
  * a human integrator.
* The reviews in Section 6 are **bounded agent reviews**. AI agents of one model family wrote them
  on this branch. They are not independent of one another, and none is human.
  [docs/REVIEWING.md](../../../../../docs/REVIEWING.md) warns that "different chats using the same
  model can repeat the same mistake". They can be cited as preparation for review. They are not a
  substitute for it.
* No statement here is stronger than the manuscript's statement. The special case in Section 2.3
  is an instance of it. The L-value reading in Section 2.3 is labelled as *not* part of the
  proposed statement.
* The manuscript itself presents Lemma 18.1 as a technical input to its row count (12479-12480).
  It does not claim it as a new moment theorem and does not compare it with the moment
  literature. The view that case 1 would be new comes from this repository's review
  ([LEMMA18_1_REVIEW.md](../../reviews/LEMMA18_1_REVIEW.md) §1) and from Section 9 here.

Files in this draft:

| File | Content |
|---|---|
| README.md (this file) | source, statement, scope, native and imported inputs, dependency chain, review record, misreadings, smallest failure point, literature, next steps |
| [PROOF_OUTLINE.md](PROOF_OUTLINE.md) | condensed proof of case 1, each step tied to manuscript lines and to the review that read it |
| [CHECKS.md](CHECKS.md) | how to rerun each script, hashes, the results of this rerun, and what each script does and does not authenticate |

## 1. Frozen source

**The manuscript.** The upstream source is `openai/math` at commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a` (2026-10-06T21:58:50Z). It is imported unmodified at
PR 908.

| Object | Location | SHA-256 | Git blob | Size |
|---|---|---|---|---|
| Manuscript source (load-bearing) | `pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex` | `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3` | `268c4e3206d460c617d3d2129742a72b831b3def` | 766,316 bytes, 16,677 lines |
| Manuscript PDF (not compared with the TeX) | `.../September-30-2026/paper.pdf` | `8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7` | `8132b77eeb270a70b25df8d6609f008e83e65d91` | 1,588,969 bytes |
| Citation README | `.../September-30-2026/README.md` | `5a9c5ef1322c1e0051f58bee69ce422984eb523ba85d56529eae18f05771bd32` | `05daa0838d60781c338ac22a9b06e6990f970981` | 590 bytes |

* `pr908` resolves to `31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6`. The three hashes above were
  recomputed for this draft and agree with PR 908's `UPSTREAM_FILES.json`.
* The citation README gives the author as "OpenAI" and the date as 30 September 2026. Unlike the
  Oct 5 README, it says nothing about human assistance.
* The upstream licence is Apache-2.0 (PR 908 `upstream/LICENSE`, `THIRD_PARTY_NOTICES.md`). An
  integrator who makes text resident must keep the attribution and licence notices.
* Every line number in this draft refers to `paper.tex` at the hash above.

**Review record.** Paths are relative to `research/exploratory/qrh-2026-10/`. Every file was read
at commit `c8515d4ea045e7b685f53feb6dd801bf0f529211`. The branch moves while other agents commit,
so cite that commit or the hashes, not the branch.

| File | Role | SHA-256 | Git blob | Last changed in |
|---|---|---|---|---|
| `reviews/LEMMA18_1_REVIEW.md` (L18a) | structure of case 1, ledgers, numerics, literature | `840aa73ce90aee44b9a00d65c73285d00028635186934f1a26493d52c3c1758d` | `3a453ef0` | `70f81c5f0` |
| `reviews/LEMMA18_1_COMMON_SUPPORT.md` (L18b) | common-support allocations of both transforms | `0f2b54fc428e7dc32b7bad1b833f1077ba1408dda9c24e2d1b597592b0a7a805` | `f14d77fb` | `722629850` |
| `reviews/LEMMA18_1_CASE2_SEC188.md` (L18c) | case 2, Sec. 18.8, interface with Prop 19.2 | `446e0604979e08be8e9207ffae8a623d98f9403f15d9667e2ee79fab570ee441` | `d871bcac` | `cc91db048` |
| `reviews/SEP30_L13_L45_REVIEW.md` (L13) | Lemmas 13.2-13.4, 4.5; 4.7-4.10 as used | `0ef92082035a69391dfc921dd497193db075205fde54f69ab7be7bb8732d1129` | `08e3921a` | `8875b9aa7` |
| `reviews/SEP30_SEC4_REVIEW.md` (SEC4) | Lemmas 4.1, 4.6-4.10, 13.1 line by line | `d68f114baf8cff810019cbdb28ea25198fdd9fbbdbb50e92e815c5f62cd31355` | `2d54b53b` | `89149339d` |
| `reviews/SEP30_JUNCTION_CHECK.md` (JUNC) | quantitative hypotheses at the use in Prop 19.2 | `fa8fd49800ed9c714fe95b21d22aaf107900b04250171563151355b07abd1f56` | `e5faec6e` | `e2892847e` |
| `reviews/SEP30_VERIFICATION_MAP_V2.md` (MAP2) | status map; context only | `629ee5414738d44c1b411cb71f58aa30803378b45744c7f6fe68352ae807a4f9` | `4cd0a09e` | `89149339d` |

Script hashes are in [CHECKS.md](CHECKS.md) §1. The cubic spin-off
[../CUBIC_FOURTH_MOMENT/](../CUBIC_FOURTH_MOMENT/README.md) (README `176ce745…ac18f`, SKETCH
`c610ba9d…0353`, both at `c8515d4ea`) is cited for context only. It is conditional on case 1 of
this lemma, so it is downstream of this draft, not evidence for it.

## 2. Statement

### 2.1 Setting (manuscript lines 557-760, 6919-7004, 12477-12530)

* **Field.** `F = Q(√−3)`, `O = Z[ω]`, `λ = √−3 = 1 + 2ω`, and `q_a = N(a) = |a|²` (560-575).
  An element prime to `3` is **primary** if it is `≡ 1 (mod 3)`. Each ideal prime to `3` has a
  unique primary generator (580-582).
* **Fixed data.** A finite set `S` of prime ideals contains the primes above `6` and the defining
  moduli of all fixed characters. Primes outside `S` are **good**. Ideal sums run over good ideals,
  represented by primary generators. The fixed arithmetic datum `𝒜` (732-740) may enter the
  implied constants.
* **Sextic symbol, with zeros kept** (626-640). For a good prime `p` with `P = q_p`,
  `χ_p(a) ≡ a^{(P−1)/6} (mod p)` and `χ_p(a) = 0` if `p | a`. For good primary `c`,
  `χ_c(a) = ∏_{p|c} χ_p(a)^{v_p(c)}`. A power `χ_c(a)^j` is `0` whenever `(a, c) ≠ 1`, even if
  `6 | j`.
* **Plain polynomial** (old-eq:1.1, 705-708). At a base `Z > 1`, for a real log-length `n ≥ 0`
  and an annular test `W` (smooth, supported in a fixed compact subinterval of `(0, ∞)`, 719),

      S_ψ(n; W) = Z^{−n/2} Σ_l ψ(l) W(q_l / Z^n),

  where `l` runs over **all** good ideals, not only squarefree ones.
* **Rows and coefficients** (6952-6965, 12494-12508). The rows are elements `k ∈ O` with
  `0 < q_k ≪ Z^m`, with arbitrary units, `S`-parts and prime powers. The coefficients are

      ψ_k(n) = τ(n) χ_n(k),        M = m + q.

  Here `τ` is a twist fixed within the row sum. It is a product of fixed finite-ray characters
  and "displayed moving residue-symbol factors". The union `D_mov` of the prime supports of the
  moving factors has `q_{D_mov} ≤ Z^q`. An optional common puncture mask `1_{(n,𝔑)=1}`, with `𝔑`
  squarefree and `q_𝔑 ≤ Z^B` for bounded `B`, may be present (6966-6988).
* **Row family** (12522-12523). `ℛ_0` is the set of rows for which `ψ_k` induces a nonprincipal
  character.

### 2.2 The proposed statement: case 1 (Lemma 18.1, 12531-12579, case 1 at 12556-12557)

**Theorem (imported; proposed at this scope).** Fix the arithmetic datum `𝒜`, bounded ranges for
the real parameters `m, q, B, n_1, n_2`, and annular profiles `W_1, W_2`. For every `ε > 0`,

    Σ_{k ∈ ℛ_0, 0 < q_k ≪ Z^m}  | S_{ψ_k}(n_1; W_1) · S_{ψ_k}(n_2; W_2) |²   ≪   Z^{M + ε}.      (old-eq:2.1)

**Quantifiers and uniformity, as stated (12556-12557, 12567-12578).**

* There is **no restriction** on the bounded nonnegative lengths `n_1, n_2`, and **no lower
  bound** on the conductor of `ψ_k`.
* The implied constant depends on `𝒜`, `ε`, the bounded parameter ranges, finitely many smooth
  seminorms of `W_1, W_2`, and a fixed polynomial in the separated norm-twist heights (profiles
  of the form `W(y) y^{iω}`).
* The orders and the bound are uniform over all moving moduli, admissible masks and frozen outer
  labels in the stated ranges.

### 2.3 The special case that makes it a Lindelöf-strength fourth moment

Take `S = {(2), (λ)}`, `τ = 1` on good ideals (so `q = 0` and `M = m`), no mask, `W_1 = W_2 = W`,
`n_1 = n_2 = m/2`, and write `K = Z^m`. Then the theorem says

    Σ_{k ∈ ℛ_0, 0 < N(k) ≤ K}  | Σ_{l good} χ_l(k) W(N(l)/√K) |⁴   ≪_{W,ε}   K^{2+ε}.

**Why this is Lindelöf strength.** There are about `(2π/√3)K ≈ 3.63K` rows. Each inner sum is
trivially `O(√K)`, so the trivial bound is `K³`. The diagonal heuristic gives a mean of about
`(√K)² = K` for `|Σ|⁴`, hence a total of about `K²`. The claim matches that up to `K^ε`.

**What the special case already contains.**

* `n_2 = 0` gives a second moment of length-`√K` sums.
* `(n_1, n_2) = (m/4, 3m/4)` and lengths beyond the conductor (`n_i > m`) are included, the latter
  through reflection.
* The rows are elements, not squarefree moduli. They include units times `S`-parts, rows with
  sixth-power factors (`k = t c⁶`, about `(K/N(c))^{1/6}` per primitive character), and the thin
  quadratic-type (`k = t c³`) and cubic-type (`k = t c²`) subfamilies. Only rows whose character
  is principal are excluded.

**L-value reading (NOT part of the proposed statement; not in the manuscript; not reviewed).** By
an approximate functional equation, a dyadic split, Möbius removal of the redundant zeros, and the
conductor bound (old-eq:2.1c), one expects case 1 to give, for bounded `t`,

    Σ_{k ∈ ℛ_0, N(k) ≤ K} |L(1/2 + it, ψ_k^*)|⁴  ≪  K^{1+ε},

where `ψ_k^*` is the primitive character inducing `l ↦ χ_l(k)`. This deduction is not written out
anywhere for the sextic family. The analogous cubic application step is written out, conditionally,
in [../CUBIC_FOURTH_MOMENT/SKETCH.md](../CUBIC_FOURTH_MOMENT/SKETCH.md) §2. Until a sextic version
is written and reviewed, cite the character-sum form above, not this L-value form.

### 2.4 What the general statement adds

**Within case 1.**

* **Moving twists.** `τ` may carry moving residue-symbol factors of total radical `Z^q`; the bound
  is then `Z^{m+q+ε}`. This clause is what makes the induction closed: children of the transforms
  carry such twists.
* **Puncture masks.** A common mask of polynomial norm is allowed.
* **All bounded lengths.** There is no balance condition, so long and very unbalanced pairs are
  included.
* **Complex profiles.** Norm twists `y^{iω}` are allowed, with polynomial dependence on `ω`.
* **Uniformity.** The bound is uniform over moving moduli, masks and frozen labels.

**Case 2 (12558-12566): short prime factors.** Fix `3/4 ≤ κ ≤ 1` and a finite group `Θ` of
finite-order ray characters with conductor primes in `S`. `Θ` contains the fixed twists and the
characters that separate the fixed reciprocity phases, including `n ↦ χ_n(−1)` (12511-12520).
Multiply by a product `Q` of **prime slots**

    Q_{ψ_k,i} = Z^{−z_i/2} Σ_{p prime} ψ_k(p) ν_i(p) W_i(q_p / Z^{z_i})        (old-eq:1.2, 6933-6937)

with pairwise disjoint prime supports, coefficients `ν_i` that are fixed linear combinations of
members of `Θ`, and total length `z = Σ z_i > 0`. Restrict to the rows `ℛ_z` whose inducing
character is not in `Θ`, and put `A = n_1 + n_2 + z`. For every `ε > 0` there is a mesh `η > 0`
such that, if every `z_i ≤ η` and

    n_1 + n_2 + 6κz = A + (6κ − 1)z ≤ M,        (old-eq:3.9)

then `Σ_{k∈ℛ_z} |S(n_1)S(n_2)Q|² ≪ Z^{M+ε}`. If `κ < 1`, this requires the zero-free hypothesis
`β_* ≤ (1+κ)/2`, where `β_*` is the supremum of real parts of zeros of primitive finite-order
Hecke L-functions of `F` (old-eq:1.1b, 377-385). If `κ = 1`, no hypothesis is needed. The mesh
depends only on `ε` and the bounded ranges. It is uniform in `κ` and independent of the slot
count (12567-12578; L18c §4).

### 2.5 Outside the proposed statement

* **Case 2.** It is listed above for completeness. For `κ < 1` it is conditional. Its only use is
  Prop 19.2, inside the 7/8 argument. It is not proposed here.
* **The L-value form** of Section 2.3.
* **Theorem 1.1 (7/8)** and everything downstream of Lemma 18.1: Prop 19.2 (15185-15446), Sec. 20.
* **The cubic transfer** ([../CUBIC_FOURTH_MOMENT/](../CUBIC_FOURTH_MOMENT/README.md)). Its
  hypothesis (H-A) is the order-independent core of this case 1 at `n = 3`. It is not this
  statement.

## 3. Scope

| Dimension | Scope of the proposed statement |
|---|---|
| Finite / global | **global**: all `Z`, all rows in `ℛ_0` up to `Z^m`, all bounded lengths |
| Conditional / unconditional | case 1 is unconditional as written, given the helper lemmas and imported theorems of Section 4. It uses Lemma 4.8 (functional equation) but not Lemma 4.9 and no zero-free hypothesis |
| Uniformity | `ε`-loss; constants depend on `𝒜`, the ranges, finitely many seminorms and a fixed height polynomial; uniform in moving data. The induction depth `D = 2 + ⌈2M_max/σ⌉` grows as `ε → 0` |
| Effectivity | not claimed; the constants are not tracked |
| Family | sextic characters `l ↦ τ(l)χ_l(k)` of `Q(√−3)`, indexed by element rows `k`. Nothing for other fields or orders. The cubic family is a separate, conditional object |
| Relation to RH | none. It is a moment bound. Under GLH for this family case 1 is immediate (L18a §0); unconditionally it would be new (Section 9) |

## 4. Native versus imported

### 4.1 Native to Section 18 (proved there; every line read by L18a, L18b, L18c)

| Component | Lines | Read by |
|---|---|---|
| mask erasure (old-eq:2.1a), (2.1b) | 12602-12676 | L18a §2.1 |
| natural reflection; conductor bound (old-eq:2.1c); padded zero-slot core (2.1h) | 12677-12830 | L18a §2.1 |
| prime estimates (case 2 only) | 12831-12902 | L18c §1.1 |
| induction order, width floor | 12903-12938 | L18a §2.2; L18c §2 |
| comparison and centering, `L = M/4` | 12940-13010 | L18a §2.3; L18c §1.1 |
| centred coefficient `D_𝐛` and its support | 13012-13113 | L18b (as used); L18c §6 |
| first Poisson transform; zero frequency; common-support bridge; target (old-eq:2.5); ledger (2.6) | 13114-13410 | L18a §2.4; L18b §2 |
| Gauss-row enlargement (zero-slot); amplifier (case 2) | 13411-13594 | L18a §2.5; L18c §1.2 |
| second transform; diagonal (2.12); children (2.13)-(2.14); **Lemma 18.2** `centered-coefficient-invariant` (13953-13996); child normalisation and clipping | 13596-14310 | L18a §2.6; L18b §3; L18c §1.3-1.4 |
| Θ-rows: exceptional count; excess (2.15)-(2.17); **Lemma 18.3** `centered-lattice-cancellation` (14545-14680); (2.18), (2.19) | 14312-14778 | L18a §2.7; L18b §3; L18c §1.5 |
| completion of the finite induction; choice order (2.1i); physical remark | 14779-14983 | L18a §2.8; L18c §2 |

### 4.2 Helper lemmas of the manuscript outside Section 18

The table lists every lemma of the manuscript that Section 18 cites by label or equation
(checked by grep for this draft), with its review status.

| Lemma (label) | Lines | Where Section 18 uses it | Review status |
|---|---|---|---|
| 4.1 `fixed-numerator-ray` | 646-699 | conductor bound at `S` (12687-12700); finite ray choices on Θ-rows (14325-14340); 14961 | SEC4 §1: no wrong step |
| 4.3 `quadratic-four-term`, which defines the bicharacter `𝔯` (eq:reciprocity-four-class, 857) | 841-932 | through Lemma 4.4 | **not reviewed** when drafted (MAP2 status A); since then one bounded review, no wrong step (SEP30_L42_44_REVIEW) |
| 4.4 `fixed-gauss-phase`, with eq:row-fixed-ray-reduction (1054-1070) | 934-1052 | reciprocity phases in both transforms (13258-13268; 13686-13697), the supplementary character in `Θ` (12511-12520), Θ-row reduction (14325-14335) | **not reviewed** when drafted (MAP2 status A). Checked numerically on small pairs: L13 A5, L18b B4. Since then one bounded review, no wrong step, given classical cubic reciprocity (SEP30_L42_44_REVIEW) |
| 4.5 `smooth-calculus` | 1123-1286 | Fourier separation with one common measure (13320-13335, 13910-13935); rowwise suprema (12780-12786); heights (14834-14856) | L13 §4: no wrong step. Its invocations were read, not replayed (MAP2) |
| 4.7 `kernel-seminorms` | 1347-1413 | localisation tails (13156); radial kernels uniform in `R_sc` (14834-14842) | L13; SEC4 §3: no wrong step |
| 4.8 `hecke-strip-growth` | 1425-1529 | primitive functional equation and entireness for reflection (12700-12704) | SEC4 §4: no wrong step |
| 4.9 `logarithmic-control` | 1531-1600 | **case 2 only**: the slot bound (old-eq:3.5), 12844-12852 | SEC4 §5; L13: no wrong step (constants ineffective) |
| 4.10 `deleted-euler-factors` | 1602-1646 | mask mass (old-eq:2.1b), 12663-12667 | SEC4 §6: no wrong step |
| 13.2 `prime-power-fourier` (eq:gauss-local, 7063) | 7055-7079 | local Gauss values; the amplifier (case 2) | L13 §3 (exact D2): no wrong step |
| 13.3 `full-correlation` (eq:correlation-local, 7120) | 7081-7190 | second-transform expansion and local table (13606-13640, 13699-13751) | L13 §1: no wrong step |
| 13.4 `complete-support-correlation` | 7196-7247 | second-transform extraction (13686-13697) | L13 §2: no wrong step |

Lemma 4.2 (`prime-gauss-identities`, 766-836) and Lemma 13.1 are not cited in Section 18. Lemma
4.2 is also status A. [Superseded: see the note after Section 10.]

### 4.3 Imported external theorems (not re-proved in the manuscript)

| # | Imported theorem | Where it enters | How it was checked | Label |
|---|---|---|---|---|
| E1 | **Hecke**: functional equation and entireness of `L(s, ψ)` for primitive nonprincipal finite-order `ψ` of `F`; the manuscript cites Gao–Zhao, JNT 209 (2020), eq. (1.1) | Lemma 4.8, then reflection (12700) | SEC4 D2: the functional equation holds numerically with the conductors found in A2 | IMPORTED, classical |
| E2 | **Kummer theory and Artin reciprocity** for `F(a^{1/6})/F` (Milne, CFT notes, VIII (5.3), (5.5)) | Lemma 4.1 | SEC4 A1-A4 (conductors found and minimal moduli confirmed by exact collisions) | IMPORTED, classical |
| E3 | **Sextic reciprocity** with supplementary laws, and the quadratic Gauss-sum facts behind `G` and `𝔯` | Lemmas 4.3-4.4 | **numerically only** (L13 A5; L18b B4, 3298 pairs) [superseded: see the note after Section 10] | IMPORTED, classical; manuscript proofs unreviewed |
| E4 | **Lattice Poisson summation** on `O` with the self-dual measure `(2/√3)dx dy` (610-617) | both transforms (13226-13268; 13606-13620) | L18b D (end-to-end bridge, four configurations); L13 D1 (exact in `Z[ζ_L]`) | IMPORTED, classical |
| E5 | **Powerful-ideal count** `O(Y^{1/2+ε})` | first-transform zero frequency (13182-13190) | read (L18a §2.4) | classical |
| E6 | **Rankin's bound** and polynomial-size Euler products | label counts (13355-13366, 13824-13836) | read (L18b §2-3) | classical |
| E7 | **Divisor bounds** `τ_{N+2}(v)^C, C_N^{ω(v)} ≪ q_v^a`; the divisor-bounded convention | 742-760; 14911-14914 | read (L18c §2) | classical |
| E8 | **Ideal counting** in a disk, `πH/(3√3) + O(√H + 1)` | 617-622; the lattice cancellation of Lemma 18.3 | read | classical |
| E9 | **Mellin inversion, contour shifts and Stirling** for `Γ(s)/Γ(1−s)` | reflection profile `W^♯` (12709-12745) | read (L18a §2.1); SEC4 D0 | classical |
| E10 | **Prime ideal theorem in ray-class form** (Thorner–Zaman, ANT 13 (2019), Thm 1.1, used only at Hecke–Landau strength) | **case 2 only**: amplifier pool size (13462-13466) | read; wording not checked at source (SEC4 §7) | IMPORTED |
| E11 | **Borel–Carathéodory, Hadamard three circles, Phragmén–Lindelöf** | **case 2 only** through Lemma 4.9; Lemma 4.8 | SEC4 §4-5, E0-E1 | classical |
| E12 | **Elementary tools**: Möbius inversion, CRT, character orthogonality, Cauchy–Schwarz, Minkowski, Jensen (case 2 amplifier) | throughout | used as stated | classical |

The manuscript's large-sieve citations (Goldmakher–Louvel, Blomer–Goldmakher–Louvel, Heath-Brown;
lines 132-145) concern other sections. **None is cited in Section 18**; a grep of 12477-14984 finds
one citation, `[TZ, Thm 1.1]` at 13464. The manuscript relates its recursive moment arguments to
Heath-Brown's quadratic method (`[HBQuadratic, §2]`, line 141), as background only.

## 5. Dependency chain (paper.tex line ranges)

```text
Lemma 18.1, case 1 (statement 12531-12579; family 12477-12530)
 ├─ fixed-mask erasure (2.1a)-(2.1b), 12602-12676 ............... Lemma 4.10           [L18a]
 ├─ natural reflection, (2.1c)-(2.1h), 12677-12830 ............. Lemma 4.8 (E1), 4.1 (E2), 4.5 (sups)   [L18a]
 └─ finite induction on M in bands sigma/4 (12903-12938; completion 14779-14983)   [L18a, L18c]
     ├─ floor M <= rho: absolute counting ............................................ [L18a]
     ├─ comparison / centering, L = M/4 (12940-13010) ......... margins 5M/6 - A_comp >= M/6 - xi   [L18a; ledger]
     ├─ first Poisson transform (13114-13410)
     │   ├─ zero frequency: powerful products (E5) ...................................... [L18a]
     │   ├─ common-support bridge 13192-13349 ...... Lemma 4.4 (A), E4, Lemma 4.5/4.7 separation   [L18b; D]
     │   └─ target (2.5) + ledger (2.6) ............ zero slack at local types (1,1), (2,1)   [L18a; L18b A3]
     ├─ Gauss-row enlargement g = J_+ + sigma (13411-13460) ............................ [L18a]
     ├─ second transform (13596-14310)
     │   ├─ diagonal (2.12): excess A - M + 5sigma/3 ................. Lemma 13.3     [L18a; ledger]
     │   ├─ extraction 13686-13933 ................ Lemma 13.3, 13.4, E6              [L18b; E, F]
     │   ├─ Lemma 18.2 centered-coefficient-invariant (13953-13996) ........................ [L18b; L18c]
     │   └─ children: M' <= M - sigma (2.13), allowance M' + Delta_child (2.14) -> induction   [L18a]
     └─ Theta-rows (14312-14778) ◄── ZERO-SLACK CORE
         ├─ exceptional count Z^{(m'-f)/6} (14380) ....... Lemma 4.1, 4.4 (A), E8        [L18a; L18b]
         ├─ excess A - 5M/6 - F1 - F2 (2.15)-(2.17) .................................... [L18a; ledger]
         ├─ Lemma 18.3 centered-lattice-cancellation (14545-14680) ...... E8, Möbius  [L18a "standard"]
         └─ (2.18) and (2.19): max over v at v = L equals A - M <= delta ................. [L18a; L18b L4]
```

## 6. Review record (bounded agent reviews; not independent; not human)

All of these reviews were written by AI agents of one model family on this branch. They read the
same frozen source. They overlap in model and context, so they are not independent of one another
in the sense of [docs/REVIEWING.md](../../../../../docs/REVIEWING.md), and no human has read any
part. The verdict wording below is quoted or closely paraphrased.

| Review | paper.tex lines read | Method | Script, result (rerun for this draft) | Recorded verdict |
|---|---|---|---|---|
| [L18a](../../reviews/LEMMA18_1_REVIEW.md) | 12477-14973 with focus on case 1; first-transform bridge only in the coprime squarefree model | structural reconstruction; ledgers; numerics | `lemma18_ledger.py` 14/14; `lemma18_local.py` 283 checks; `lemma18_moments.py` (EMPIRICAL) | "Cannot tell. The proof is structurally plausible, and no concrete gap was found in what was checked." Gap: 13192-13349 and 13686-13933 |
| [L18b](../../reviews/LEMMA18_1_COMMON_SUPPORT.md) | 13192-13349, 13686-13933 line by line; 12477-14780 and 7042-7231 as used | line check of allocations; exact identities; end-to-end bridge | `lemma18_support_checks.py` 24/24 | "(a) Verified: no error found in the complete-common-support allocations". Lemma 18.1 as a whole "NOT certified by this note" |
| [L18c](../../reviews/LEMMA18_1_CASE2_SEC188.md) | case 2 (12831-14778, slot parts), Sec. 18.8 (14779-14984), interface (15095-15446) | line by line; exact ledgers with failing controls | `lemma18_case2_ledger.py` 50/50 (17 controls) | "no wrong step found in case 2 or in Sec. 18.8 ... every proof line of Lemma 18.1 (l. 12602-14984) has been read by at least one bounded review ... This is NOT a certification" |
| [L13](../../reviews/SEP30_L13_L45_REVIEW.md) | Lemmas 13.2-13.4 (7055-7247), 4.5 (1123-1286); 4.7-4.10 as used | line by line; exact checks in `Z[ω]`, `Z[ζ_L]` | `sep30_l13_checks.py` 33/33 | "no wrong step found" for 13.2, 13.3, 13.4, 4.5, 4.7, 4.9 |
| [SEC4](../../reviews/SEP30_SEC4_REVIEW.md) | Lemmas 4.1, 4.6-4.10, 13.1 (646-1646, 7004-7040) | line by line; exact and mpmath checks | `sep30_sec4_checks.py` ALL PASS (full run recorded; quick mode rerun here) | "no wrong step found" in all seven |
| [JUNC](../../reviews/SEP30_JUNCTION_CHECK.md) | the uses of Lemma 18.1 in Prop 19.2 (15095-15446) | exact rational gates | `sep30_junction_check.py` 84/84 (not rerun here) | every quantitative hypothesis instance holds; case 2 is invoked exactly on its boundary |

**Coverage.** L18a, L18b and L18c together read lines 12477-14984, which is the statement and
every proof line (L18c §6). Only L18b and L18c read the full common-support allocations; only L18c
read Sec. 18.8 line by line.

**Findings recorded by the reviews (none is a wrong step), plus one citation note from this draft.**

| ID | Lines | Finding | Source |
|---|---|---|---|
| S1 | 14380 | The exceptional-row count keeps `Z^{(m'−f)/6}`; the forced form gives `Z^{(m'−2f)/6}`, an unused `f/6` of slack at Z2 | L18b §3 |
| S2 | 12978 | The stated comparison margin `M/15` (case 2) is in fact `M/14` (exact suprema `16/21` and `13/14`) | L18c §1.1, K1 |
| S3 | 14762 | In case 2 the maximum in (2.19) is `−(6κ−1)z ≤ 0`; this slack is not used | L18c §1.5 |
| S4 | 15237 | Prop 19.2 invokes case 2 exactly on the boundary of (3.9) and of `β_* ≤ (1+κ)/2`; permitted by the non-strict statement | JUNC R1 |
| S5 | 1531-1600 | Lemma 4.9's constants are astronomically large and ineffective (`θ ≈ 0.9999`); harmless for fixed `ε` | SEC4 §5 |
| C1 | 13320-13335, 13910-13935 | Citation offset in a review, not a manuscript issue: L18b cites the two kernel separations as 13307-13319 and 13899-13904. Those lines hold the `s`-extension and the `F̃` display; the separation text is about 10 lines later. Found by grep for this draft | this draft |

**What no review did.**

* No review read the proofs of Lemmas 4.2, 4.3 or 4.4 (MAP2: status A). [Superseded: see the note after Section 10.]
* No review replayed an analytic estimate: Fourier-measure `L¹` norms, tails and the lattice
  cancellation were read, not computed.
* L18a called the proof of Lemma 18.3 "standard lattice Poisson plus Möbius" and found nothing
  wrong. No later note re-derived that proof line by line.
* Whether each displayed ledger describes the analysis was read, not formalised.
* No human reviewed any part. The imported Lean development contains a normalized, specialized
  instance of Lemma 18.1 (../../reviews/SEP30_LEAN_CORRESPONDENCE.md, code Fv). The general
  statement is not formalized.

## 7. Known misreadings

1. **"Lemma 18.1 proves RH, GRH or the 7/8 half-plane."** No. It is a moment bound. The 7/8
   theorem needs much more (Prop 19.2, Sec. 20, Lemma 17.1), most of it outside this draft.
2. **"It is a fourth moment of L-values."** Not as stated. It bounds the mean square of a
   *product of two smoothed character sums* (two "plain polynomials"), with arbitrary lengths. The
   L-value form needs an approximate functional equation and a Möbius treatment of redundant
   zeros. Neither is in the manuscript, and neither has been reviewed (Section 2.3).
3. **"Fourth moment with short prime factors" means case 1 has prime factors.** No. Case 1 is
   `z = 0`: no live slot. The short prime factors are case 2. Zero-length slots are absorbed into
   the constant (12568-12571).
4. **"The family is squarefree moduli, as in BGL, Gao–Zhao or DDDS."** No. The rows are all
   elements `k` with `0 < q_k ≪ Z^m`. `ℛ_0` removes only principal characters, with no lower
   bound on the conductor. So small-conductor characters are counted with multiplicity, and the
   quadratic-type and cubic-type rows are included. This is stronger than a squarefree-family
   statement by positivity, but not the same object.
5. **"The bound holds on the full row ball."** No. It holds on `ℛ_0`. On all rows, principal rows
   dominate once `A > 5M/6`; L18a §4 observed their share growing like `K^{1.1}` at `A = 2m`.
6. **"`5M/6` is the range of the theorem."** No. Case 1 has no length restriction. `A ≤ 5M/6` is
   the first stage within each band; the rest comes from centering and reflection.
7. **"This is a sextic large sieve."** No. It concerns coefficients that are themselves smooth
   character sums. The proof reflects every child by the functional equation, which general
   coefficients do not allow. Dunn–Radziwiłł's GRH-conditional sharpness of the `(MN)^{2/3}` term
   concerns general coefficients and does not contradict case 1 (L18a §1).
8. **"Case 2 is unconditional."** Only for `κ = 1`. For `κ < 1` it assumes `β_* ≤ (1+κ)/2`. In
   the 7/8 application `κ = 2β_* − 1`, so the hypothesis holds with equality (12581-12583).
9. **"Lemma 18.1 is used for 11/12."** No. Only the Sep 30 (7/8) argument uses it. The Oct 5
   (11/12) packet [../OCT5_11_12_PACKET/](../OCT5_11_12_PACKET/README.md) does not.
10. **"The numerics support the theorem."** They are consistent with case 1 up to `K = 3·10⁶`, but
    they are floating point at small `K` and cannot separate `K^ε` from a constant. They test
    nothing in the proof (CHECKS.md).
11. **"Three agent reviews mean it is reviewed."** No. They form one bounded, non-independent
    record. Integration needs an exact-SHA independent review.
12. **"There is room to spare."** No. The exponent bookkeeping has zero slack at several points
    (Section 8). A fixed-power loss at any of them breaks the stated range.

**Zero-slack points (case 1 unless marked).**

| Point | Lines | What is tight | Source |
|---|---|---|---|
| (2.6) | 13396-13408 | `𝔅_c + 𝔅_d ≤ c + d − 2p − R`; local slack is zero at types `(i,j) = (1,1), (2,1)` | L18b A3 |
| Z1: (2.19) at `v = L` | 14759-14768 | the centred deficit's maximum equals `A − M` exactly; absorbed only by `A − M ≤ δ` from reflection | L18a §2.7; L18b L4 |
| Z2 | 14504-14524 | `F_2 = 2b_2/3` at nonunit primes of multiplicity one (with unused `f/6`, S1) | L18a §2.7; L18b §3 |
| Z3 | 14470-14495 | `F_1 ≥ 2c/3` is attained when `J < 0` | L18a §2.7; L18b §3 |
| Z4 (case 2) | 13505-13513, 14183-14275 | amplifier gain equals greedy cost per edge; any excess `λσ` accumulates over `D − 2` edges | L18c §3 |

At Z1-Z3 an `O(σ)` loss is harmless because it is terminal. A loss proportional to `M` is not.

## 8. The smallest statement whose failure would invalidate case 1

**The centred Θ-row estimate (old-eq:2.18), lines 14700-14740, with its inputs Lemma 18.2
(13953-13996) and Lemma 18.3 (eq. old-eq:2.18f, 14545-14590).** For a centred input with
`A ∈ (5M/6, M + δ]`, on child rows whose inducing character lies in `Θ`, it asserts

    Σ_{𝔱,𝐉} |c_{𝔱,𝐉}(h')| · |P_{C,𝔱,𝐉}(h') P_{D,𝔱,𝐉}(h')|  ≪  Z^{a_0 − b_2 − r + 2θ_N + ε_1},
    r = (L − v)_+,  L = M/4,  v = c + w + min(c_2, d_2).

That is, the equal-product-scale difference of the two rectangles keeps one character, one mask
and one norm power on each side through both transforms (Lemma 18.2), so that the volume main
terms `c·T^{1+it}I_1I_2` cancel and leave `T·Z^{−r}` (Lemma 18.3).

* **Why it is the smallest.** It is the only mechanism that handles `A > 5M/6` on exceptional
  rows. Combined with (2.15)-(2.17) it gives (2.19), whose maximum is exactly `A − M` at `v = L`
  (Z1). A loss of `Z^{cM}` for any fixed `c > 0` in `r` would leave `A ∈ (M − cM, M]` unproved,
  and reflection cannot move a product out of that range.
* **Why it is plausible but load-bearing.** The cancellation is exact algebra plus standard
  lattice-point counting. But it must hold for every common-support allocation, every amplifier
  error and every `𝔱`-label, with formal (unclipped) scales. L18b checked the allocations; the
  proof of Lemma 18.3 has had only L18a's "standard" reading.
* **The cubic analogue** is the identified weakest point of the conditional cubic transfer
  ([../CUBIC_FOURTH_MOMENT/README.md](../CUBIC_FOURTH_MOMENT/README.md), "Smallest remaining gap").

**Next-smallest load-bearing statements.**

1. **Lemma 4.4** (four-class sextic reciprocity and the fixed Gauss phase, 934-1052), with the
   bicharacter of Lemma 4.3 (857). Every CRT phase in both transforms and the definition of `Θ`
   go through it. Its proof is unreviewed; it was checked on 3298 small pairs only.
2. **The one-measure Fourier separation** (13320-13335, 13910-13935). One Fourier measure, fixed
   before the live labels, must separate the kernel `Φ̂_1(R_sc x/(y_1y_2))` and the inverse roots
   with an `L¹` norm uniform in the sector. It rests on Lemmas 4.5 and 4.7 (reviewed), but its
   invocation was read, not replayed.
3. **The first-transform ledger (2.6)** at the local types `(1,1)` and `(2,1)`, where the slack is
   zero. It is exact and was checked for all `1 ≤ j ≤ i < 200`.

## 9. Comparison with the literature (primary sources)

The arXiv e-print sources below were fetched for this draft on 2026-10-10 and read with grep and
sed. Their SHA-256 hashes are those of the `arXiv.org/e-print/<id>` downloads; two of them agree
with the hashes recorded in the cubic spin-off. Journal versions were not compared.

| Work (primary source) | Family | What is proved | Relation to case 1 |
|---|---|---|---|
| Baier–Young, *Mean values with cubic characters*, J. Number Theory 130 (2010) 879-903; arXiv:0804.2233v4 (e-print `35172b44…a59b58`) | primitive **cubic Dirichlet** characters over `Q`; Hecke `L(s, ψ_m)` for rational squarefree `m` | first-moment asymptotic with power saving; cubic and sextic large sieve over `Q`; Theorem `secondmoment`: `Σ_{q≤Q} Σ*_{χ³=χ_0} \|L(1/2+it, χ)\|² ≪ Q^{6/5+ε}(1+\|t\|)^{6/5+ε}`, and `Σ*_{m≤M} \|L(1/2+it, ψ_m)\|² ≪ M^{3/2+ε}(1+\|t\|)^{4/3}` | different family; second moment only, and **not** of Lindelöf strength (`Q^{6/5}` against a family of size about `Q`); no fourth moment |
| Blomer–Goldmakher–Louvel, *L-functions with n-th-order twists*, IMRN 2014 no. 7, 1925-1955; arXiv:1112.1650v1 (e-print `a3a4c38a…f99bda`) | `n`-th order Hecke characters `χ_𝔞` of `K ⊇ μ_n`, `n ≥ 3`, over all ideals `𝔞` coprime to `S` | Theorem `thm3`: `Σ*_{N𝔞≤M} \|Σ*_{N𝔟≤N} λ_𝔟 χ_𝔞(𝔟)\|² ≪ (MN)^ε(M + N + (MN)^{2/3}) Σ\|λ_𝔟\|²` (squarefree, coprime to `S`); Corollary `kor2`: `Σ_{N𝔞≤N} \|L(1/2+it, χ_𝔞)\|² ≪ (N(1+\|t\|)^{d/2})^{1+ε}` | covers `n = 6`, `K = Q(ω)`. Gives a **Lindelöf-strength second moment**; the `n_2 = 0` part of case 1 is close to it. The large sieve at `M = N` gives only about `K^{4/3+ε}` for a fourth moment |
| David–de Faveri–Dunn–Stucky, *Non-vanishing for cubic Hecke L-functions*, arXiv:2410.03048v2 (e-print `ba8542c8…a1c8e1`) | **cubic** Hecke `χ_q` over `Q(ω)`, `q` squarefree, `q ≡ 1 (mod 9)` | mollified second moment asymptotic with power saving; positive proportion non-vanishing; a Lindelöf-on-average second moment of cubic Dirichlet series (Lemma `second_moment_lindelof_lemma`) | cubic, not sextic. States (source l. 494-501) that because the cubic large sieve is not perfectly orthogonal (Dunn–Radziwiłł, under GRH) "an optimal fourth moment bound is not available in the cubic case" |
| Gao–Zhao, *Moments and one level density of sextic Hecke L-functions of Q(ω)*, Funct. Approx. 70 (2024) 7-28; arXiv:2201.01885v2 (e-print `ac0ad023…887252`) | **sextic** Hecke `χ_c = (·/c)_6`, `c` squarefree, `c ≡ 1 (mod 36)` | Theorem `firstmoment`: `Σ* L(1/2, χ_c) W(N(c)/y) = A Ŵ(1) y + O(y^{6/7+ε})`; quotes `Σ* \|L(1/2, χ_c)\|² W ≪ y^{1+ε}` from BGL; one-level density and non-vanishing proportion `2/45` **under GRH** | same field and order. Up to second moments only; no fourth moment |
| Gao–Zhao, *Bounds for moments of cubic and quartic Dirichlet L-functions*, Indag. Math. 33 (2022) 1263-1296; arXiv:2104.09909v4 (e-print `9675bc1d…cd169d`) | primitive **cubic and quartic Dirichlet** characters over `Q` | Theorem `thmupperbound`: **under GRH**, `Σ_{q≤X} Σ* \|L(1/2, χ)\|^{2k} ≪_k X(log X)^{k²}` for all real `k ≥ 0`; sharp lower bounds for `k ≥ 1/2` (cubic unconditional, quartic under Lindelöf) | GRH-conditional, different families. At `k = 2` it is the analogue of case 1's L-value reading, with `log` instead of `K^ε`. No sextic Hecke analogue was located |
| Diaconu–Ion–Paşol–Popa, arXiv:2607.27131v1 (abstract only, via the arXiv API) | `r`-th order Hecke, `r ≥ 3`, global fields containing `μ_{2r}` | asymptotics for first and second twisted moments | second moments only; `μ_12 ⊄ Q(ω)`, so `r = 6` over `Q(ω)` is outside its hypothesis |

**Position.** In these sources no unconditional fourth-moment bound of Lindelöf strength appears
for any cubic, quartic or sextic family. The unconditional state of the art they record is a
Lindelöf-strength **second** moment (BGL, sextic and general `n`; DDDS, cubic Dirichlet series),
with a fourth-moment route capped near `K^{4/3}` by the non-orthogonal large sieve. GRH gives sharp
bounds for all moments in the cubic and quartic Dirichlet cases (Gao–Zhao). So case 1, if correct,
would be a new unconditional result for this sextic family. This search was not exhaustive. It
covered the works above and the earlier agent searches recorded in L18a §1 and
`CUBIC_FOURTH_MOMENT_TRANSFER.md` §7. An expert in the area should confirm the position.

## 10. Next-step boundary (what remains before any integration)

1. **Independent exact-SHA review** of the centred Θ-row stage (Section 8): Lemma 18.2
   (13953-13996), Lemma 18.3 with its proof (14545-14680), and (2.18)-(2.19) (14680-14778). Human
   scrutiny by an analytic number theorist is preferred.
2. **First review of Lemmas 4.3 and 4.4** (841-1070), which no bounded review has read. [Superseded: see the note after Section 10.]
3. **A replay of the one-measure separation** at the two bridges, or a written proof that the
   measure's `L¹` norm is uniform in the sector, citing Lemmas 4.5 and 4.7.
4. **Optional:** write out and review the sextic L-value deduction of Section 2.3 as a separate
   proposed object.
5. **Integrator decisions.**
   * Allocate a new claim ID. Suggested: `IMPORTED.QRH.SEP30.SEXTIC_FOURTH_MOMENT_CASE1`. No QRH
     or Hecke-moment ID appears in `canonical/` or `research/integrated/*/CLAIMS.tsv` at
     `c8515d4ea` (grep run for this draft).
   * Decide whether [PROOF_OUTLINE.md](PROOF_OUTLINE.md) suffices as the resident proof extract or
     whether lines 12477-14984 and the helper lemmas must be resident, with the Apache-2.0 notices.
   * Keep case 2, the L-value form and the 7/8 theorem as separate objects.

### Proposed claim row (for the integrator; no verdict assigned)

| Field | Proposed value |
|---|---|
| semantic_id | `IMPORTED.QRH.SEP30.SEXTIC_FOURTH_MOMENT_CASE1` (proposed; integrator allocates) |
| statement_short | For the sextic family `l ↦ τ(l)χ_l(k)` over `Q(√−3)`, the mean square over nonprincipal element rows `0 < N(k) ≪ Z^m` of a product of two smoothed character sums of arbitrary bounded log-lengths is `≪ Z^{m+q+ε}` (Lemma 18.1, case 1). |
| source | external manuscript; PR 908 `31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6`, path in §1, SHA-256 `42a5ee0f…deac6a3`, lines 12477-14984 |
| review evidence | L18a, L18b, L18c, L13, SEC4 at `c8515d4ea045e7b685f53feb6dd801bf0f529211` (bounded agent reviews) |
| quantifier_scope | global in `Z`; all bounded lengths; uniform in moving data; constants depend on `𝒜`, `ε`, ranges and finitely many seminorms |
| proof_kind | analytic induction using manuscript Lemmas 4.1, 4.3-4.5, 4.7, 4.8, 4.10, 13.2-13.4 and imported theorems E1-E9 |
| rh_relationship | none; a moment bound |
| required_fix | none recorded (findings S1-S5 are slack or remarks) |
| final_verdict | **not assigned**: awaits an independent exact-SHA review (Lemmas 4.3-4.4 have since had a first bounded agent review) |
| first_broken_arrow | none found by the agent reviews; the smallest failure point is the centred Θ-row estimate (§8) |

## Note added after drafting (same day)

Lemmas 4.2-4.4 (the Gauss and reciprocity helpers that this draft listed as never reviewed) have
since had one bounded agent review:
[../../reviews/SEP30_L42_44_REVIEW.md](../../reviews/SEP30_L42_44_REVIEW.md). It found no wrong
step, and `sep30_l42_44_checks.py` gave 65/65 PASS with every control failing as predicted.
* Lemma 4.4 imports classical cubic reciprocity and also applies it to the inert prime `−2` (the primary associate of 2). The
  cited source was not opened.
* This is still not an independent exact-SHA review in the sense of AGENTS.md.

A separate fresh-eyes review of the centred Θ-row stage (Section 8) has since been written:
[../../reviews/LEMMA18_THETA_ROW_REVIEW.md](../../reviews/LEMMA18_THETA_ROW_REVIEW.md). It is a
bounded review by one agent of the same model family as the earlier reviews.
* No wrong step was found in Lemmas 18.2-18.3 or (2.15)-(2.19).
* Its main finding is that the zero-slack point `v = L` does not use Lemma 18.3. There the centred
  saving `(L − v)_+` is zero, and the case closes through the uncentred ledger
  `F_1 + F_2 ≥ 2v/3`.
* The padding `A − M ≤ 2ξ < δ` is paid from `ε`, so the zero slack is harmless.
* Lemma 18.2 holds given its cited constructions; the imported one-measure Fourier separation was
  read as statements only.
* Runs: exact ledger 19/19; EMPIRICAL float64 Z[ω] lattice model 14/14, with its four controls
  failing as predicted.
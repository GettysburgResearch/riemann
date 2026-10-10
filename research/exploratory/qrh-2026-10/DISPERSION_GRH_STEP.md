# Where Dunn–Radziwiłł use GRH, and why their dispersion route is circular for the sextic family

```text
Status: PROPOSED analysis + SURVEY of one source. Tags: [LIT] stated or proved in DR24;
  [INF] our inference (not in DR24, not reviewed); [EMP] finite numerics (earlier notes);
  HEURISTIC where marked. No RH claim; nothing here proves or disproves any zero-free region.
Scope: (i) the GRH inputs of Dunn–Radziwiłł, "Bias in cubic Gauss sums: Patterson's conjecture";
  (ii) whether their dispersion mechanism can give the sub-diagonal second moment Mom(1, ρ),
  ρ < 1, of the Oct 5 sextic Möbius family (RUNG_STRENGTH.md), with or without GRH;
  (iii) the Oct 5 Step 3 Poisson dual written out at ρ < 1, and where it fails.
Exact sources or dependencies:
  DR24 = A. Dunn, M. Radziwiłł, Ann. of Math. 200 (2024); arXiv 2109.07463v3 (14 May 2024). Read
    from the arXiv TeX source (local untrusted copy, output.tex) as data. Numbering below is the
    printed numbering of v3, with TeX labels in brackets.
  Oct 5 = paper2.tex at pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
    The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex (external, unreviewed): §2 Steps 3–5,
    Lemma lem:arithmetic, Lemma lem:poisson, Prop. prop:poisson-reduction, Prop. prop:R,
    Prop. lem:reflection, Lemma lem:quadratic.
  PR 910 Prop. 7.2 (extraction law, imported); RUNG_STRENGTH.md §§2–4; FOURTH_MOMENT_A2.md §6;
  A2_LITERATURE.md §§0, 4, 5 (and its [EMP] dual-diagonal check a2/dual_diagonal_check.py).
What was actually run: python3 -I a2/dispersion_exponents.py (sympy, exact rationals, about 1 s):
  exponent bookkeeping for §§3–4; all asserts pass. Nothing else was computed. The DR source was
  read in §§1, 3, 6–11, 13 (Sections 4–5, Voronoi and Poisson, only where cited).
Smallest remaining gap: no unconditional, non-row-blind input is known that bounds the original
  off-diagonal Σ_{n1≠n2} μν(n1)μν(n2) W W Σ_{N u ≤ D^ρ} χ_{n1}(u) conj(χ_{n2}(u)) by D^{1+ρ+ε} for
  any ρ < 1. The DR mechanism reduces this to GRH for the same family, which is circular (§§2–3).
```

RH remains unproved. The Oct 5 manuscript is external and unreviewed. DR24 is a published,
GRH-conditional paper; we use only its structure, not its conclusions.

## 0. Verdict in brief

**Verdict (b): circular.** The averaging over `h` does not change this.

1. **Where GRH enters DR24.** [LIT] It enters in two ways. Both are pointwise, character-by-character
   statements about sums of primes or of `μ` against Hecke characters; DR24 uses no mollifier and
   no averaged Lindelöf.
   * *Throughout:* axiom (iv) of Definition 3.1 (square-root cancellation of the column sequence
     against **every** non-principal cubic Hecke character, uniformly in the conductor). It is
     verified for prime products by GRH (Lemmas 6.1–6.2). It is used for every non-cube dual
     frequency after Poisson summation in the row variable (Prop. 7.1, term `N₂`; Prop. 9.2, term
     `D₂`). The conductors run up to the full dual length `≈ B²/A`, which is as large as `X^{1/2}`.
   * *Principal / small conductor:* RH for the conductor-1 angular characters `(c/|c|)^{3ℓ}`. It
     controls a Möbius sum in the cube-removal variable (Prop. 8.1, Prop. 11.1) and the
     prime sums in Thm 1.3 for `3 | k`. DR24 say this use is avoidable.
2. **Dictionary.** DR's Gauss-weighted side corresponds to our dual `Σ_h |B_h|²`. DR's plain side,
   after Poisson summation in the row variable, corresponds to our original family `Σ_u |A_u|²`.
   Poisson in the row variable is an exact involution between these two sides (Oct 5
   (eq:convert1)/(eq:convert2)). So DR's GRH input becomes **quasi-GRH for the family members
   `L(s, ψ_u)`, `N u ≤ H`, themselves**. That alone already implies Mom(1, ρ) trivially.
   DR's *principal* dual frequencies (cubes), which produce the Patterson bias, correspond to the
   sixth-power rows `u = ε v⁶`. These rows are the extraction rows: their size is the conclusion.
3. **Averaged replacements stop at ρ = 1.**
   * A large sieve over the rows is row-blind, so it is capped at `ρ = 1` (RUNG_STRENGTH §3).
   * Zero-density counts with exponent `A`, combined with any zero-free half-plane `Re s > β*`,
     give a bootstrap whose fixed point is `1 − 1/(6A)`. For DH (`A = 2`) this is exactly
     **11/12**, and with `β* = 11/12` the output is 11/12 **identically in ρ** (§3).
   * A pointwise half-plane `β* = 11/12` reaches only relative precision `H·L^{−1/6}` on the dual
     side. Combined with DH it reaches `(H/L)^{1/6}`. The requirement is `H/L`.
4. **Correction to earlier notes.** A2_LITERATURE §0/§5, RUNG_STRENGTH §3, SYNTHESIS §2 and AGENDA
   call DR's dispersion estimate "the only analogous asymptotic". Its error terms are
   `B^{2+2η} + X^{1+ε}` (Prop. 9.2). In our dictionary these are `L^{2+2η} + 𝓗L`, and `𝓗L` is the
   dual diagonal itself. So even granting GRH, DR24's estimate does not reach relative precision
   `H/L`. It is not a precedent for the needed object, conditional or not.
5. **Unblocking lemma.** None non-circular is identified (§5). The smallest statement that would
   unblock the Oct 5 route at ρ < 1 is the off-diagonal bound (OD_ρ). It is equivalent to
   Mom(1, ρ) by the exact Poisson identity, so it is not a reduction. A candidate that is not
   visibly circular must act through the theta reflection, which is the only non-involutive step;
   it is stated as (Q_ρ), OPEN.

## 1. Where and why DR24 use GRH [LIT unless tagged]

### 1.1 The single structural hypothesis

**Definition 3.1** [seqdef], axiom (iv) [eq:can]. A sequence `α` is in the class `𝒞_η(A, w)` when:
* it is supported on squarefree `w`-rough `a ≡ 1 (3)` with `N a ≍ A`, and `|α_a| ≤ 1`;
* for all `t`, `ℓ`, `k`, `u`,

      Σ_{u | a} α_a (a/|a|)^ℓ N(a)^{it} (k/a)_3 ≪ (1+|ℓ|)^ε N(k)^ε (1+|t|)^ε (A/N u)^{1/2+η+ε},

  whenever `ℓ ≠ 0`, or `ℓ = 0` and `k` is not a cube.

The `N(k)^ε` makes this uniform in the conductor. The text right after the definition says:
"The Generalized Riemann Hypothesis is used to show that axiom (iv) holds for sequences of
interest to us."

**How GRH gives it: Lemmas 6.1–6.2** [le:primes, le:primes2]. The sequences are smoothed products
of `R ≤ log B/(K log log B)` primes.
* Newton–Girard reduces axiom (iv) to prime sums `Σ_ϖ (k/ϖ)_3^j (ϖ/|ϖ|)^{jℓ} N(ϖ)^{−j(v−it)}`.
* Only `j = 1` needs GRH; for `j ≥ 2` the sum converges absolutely on `Re v > 1/2`.
* Under GRH, `log L(s, (k/·)_3 ξ^ℓ) ≪ log²` on `Re s ≥ 1/2 + 1/log B` ([IK, Thm 5.19]).
  Here `ξ(a) = a/|a|` is the angular Größencharakter.
* So the L-functions are the **Hecke L-functions over Q(ω) of cubic characters `(k/·)_3` (conductor
  dividing `3k`), twisted by angular characters of every infinity type `ℓ`**, plus pure angular
  characters (conductor 1) when `k` is a cube.
* The loss `η > 100/K` comes from the `R`-fold product, not from any weakness in GRH.
* [INF] Under only a uniform zero-free half-plane `Re s > σ₀` with polylog control of `log L`, the
  same proof gives axiom (iv) with `η ≈ σ₀ − 1/2`. Props. 9.1, 9.2 and 10.1 assume `η ≤ 1/4`.

### 1.2 Where axiom (iv) is used: the non-principal dual frequencies

The mechanism is the same in both places. Expand `Σ_a V(N a/A)|Σ_b β_b g̃(b) conj((b/a)_3)|²`
and apply Poisson summation in `a` modulo `b₁b₂`. The cubic Gauss sums produced by Poisson cancel
the `g̃(b_i)`. What remains is plain `β` against dual cubic characters `(k/b)_3`, with dual length
`N(k) ≲ B²/A`.
* **Prop. 9.2** [prop:adj] (dispersion; Prop. 9.1 follows by sieving).
  * `𝒟` (9.13) splits into `𝒟₁` (9.37), with `dπ²γk` a cube, and `𝒟₂` (9.38).
  * `𝒟₁` is evaluated unconditionally by Poisson summation over cubes. It gives the main term
    `A^{2/3}|Σ_b β_b N(b)^{−1/6}|²`, the "Patterson bias".
  * `𝒟₂` collects the non-cube `k` with `N(k) ≪ 𝒵 = (ΔN(π)X)^ε(1 + B²N(π)Δ²/(N(d)A))`. It is
    bounded by applying axiom (iv) **pointwise in each `k`** to the `b₁`- and `b₂`-sums, then
    summing trivially. This gives (9.40): `𝒟₂ ≪ X^ε(AB^{2η} + B^{2+2η}N(π)Δ²)/N(πγ²)`.
* **Prop. 7.1** [prop:narrow] (narrow Type II/III). Same structure: `𝒩₁` (cubes) and `𝒩₂`
  (non-cubes). (7.20) gives `𝒩₂ ≪ X^ε B^{2η}(A + B²)`. The proof says: "𝒩₂ is small because the
  characters (d²ek/·)_3 … are both non-principal."
* **Prop. 10.1** [prop:broad] (Type II asymptotic, eq. (1.14)) is Cauchy–Schwarz plus Prop. 9.1.
  Section 13 feeds it prime-supported `β` via Lemmas 6.2–6.3.

**Small conductor or throughout?** Throughout. The dual frequencies are *all* non-cube `k` up to
the dual length, and DR24 do not split them into small and large `k`. In DR's applications
`A ≥ B`, so `N(k) ≲ B²/A ≤ B`. [INF, from the ranges in §13] The dual length is:
* `X^{O(ξ+ε)}` for narrow Type III (`N a ≍ X^{2/3}`, `N b ≍ X^{1/3}`);
* `≈ X^{1/2}` for narrow Type II (`A ≈ B ≈ X^{1/2}`);
* `B³/X ∈ [X^{3ξ}, X^{1/2−3ξ}]` for broad Type II.

DR24 (Sec. 1.4, after (1.14)) describe their dispersion estimate as GRH replacing "the usual
Siegel–Walfisz assumption". It is used on conductors far beyond the Siegel–Walfisz range.

**Why it is needed (operator-norm reason).** [LIT + INF] With `K = B²/A` dual rows, pointwise
axiom (iv) gives `A·K·B^{2η} = B^{2+2η}`. Heath-Brown's cubic large sieve on the dual instead
gives `A(K + B + (KB)^{2/3})`, and DR's Thm 1.4 shows that the `(KB)^{2/3}` term cannot be removed
for general coefficients. Run `a2/dispersion_exponents.py`, item (6), on the exponents:
* In the broad Type II range (`B ≤ X^{1/2−ξ}`), the large-sieve replacement would still beat the
  main-term scale `(AB)^{2/3}B`. [INF; not claimed in DR24]
* At `A ≈ B ≈ X^{1/2}` it would not. There GRH is what removes the `(KB)^{2/3}` loss.
* In Type III the dual has only `X^{O(ξ)}` frequencies, but the bound must beat the diagonal by a
  factor `1/log w`. There GRH acts like a Bombieri–Vinogradov input for cubic characters of
  conductor `≤ X^{O(ξ)}`. [INF]

### 1.3 The separate principal / small-conductor uses

* **Prop. 8.1 / Cor. 8.1** [prop:typeI] (Type I via the Voronoi formula, Prop. 5.3).
  * Statement: "we use the Riemann Hypothesis … in order to restrict the sum to squarefree numbers".
  * The Möbius inversion `(8.2)` creates `Σ_{c ~ C} μ(c)(c/|c|)^{3ℓ}N(c)^{1/2−s−3w}`. RH for
    `L(s, ξ^{3ℓ})` (conductor 1; `ζ_K` itself when `ℓ = 0`) bounds this in both the large-`C` and
    small-`C` ranges (displays [largeC], [errorvor]).
  * This is a **principal / near-principal** use: `μ` against a character of conductor 1.
  * It enters the dispersion estimate through the cross term `𝒞` ([b1intermed]).
  * Sec. 1.3 says it is avoidable, either through bilinear structure of `α_r` or through `r`-aspect
    subconvexity of `Σ_c g̃(cr)N(c)^{−s}`. "Since a more significant bottleneck appears elsewhere we
    have not endeavoured to make these results unconditional."
* **Prop. 11.1** [prop:avgtypeI]: GRH again, for the class `𝒞_η` and for the rough-number
  inversion.
* **Thm 1.3 for `3 | k`** and **Thm 1.2 with `f = e(3ℓx)`** amount directly to prime sums of
  angular characters. DR24 note that these "unambiguously require" a zero-free strip.
* **Thm 1.4** (the lower bound `𝓑(A,B) ≫ (AB)^{2/3}`) uses Prop. 8.1, hence GRH.
* Abstract: the dispersion estimate "relies on the Generalized Riemann Hypothesis, and is one of
  the fundamental reasons why our result is conditional."

### 1.4 What DR's dispersion estimate actually controls

DR24 state the consequence of (1.13) explicitly. If `β` has square-root cancellation against all
non-trivial cubic characters and `w > (AB)^ε`, the corrected mean square is

    ≪ (AB)^{o(1)} (AB + B² + (AB)^{2/3−ε}·B).

That is the optimal large-sieve scale `(A + B)B`, after subtracting the Patterson bias. Prop. 9.2
has the same shape, with errors `X^{1+ε}` (from `𝒟₁^⋄`, bounded trivially in (9.21)) and
`B^{2+2η}` (`𝒟₂`).

This is an asymptotic only because the bias `A^{2/3}B^{5/3}` exceeds both `AB` and `B²` when
`B^{1/2} < A < B²`. It is **not** an asymptotic at relative precision (columns/rows) below the
diagonal. In particular, DR24 never evaluate the `AB`-sized diagonal terms asymptotically. This
is the correction recorded in §0, item 4.

## 2. Dictionary: DR24 ↔ the Oct 5 sextic family

Notation: `L = D` columns, `H = D^ρ` original rows, `𝓗 ≍ D²/H = D^{2−ρ}` dual rows.

| | DR24 | Oct 5 family |
|---|---|---|
| Gauss-weighted side | `Σ_{a≍A} \|Σ_b β_b g̃(b) conj((b/a)_3)\|²` | dual `Σ_{N h ≤ 𝓗} \|B_h(D)\|²`, with `B_h = Σ* conj(α(n)) γ₂(n) ξ(n) χ_n(h) W` |
| row family | cubic `(·/a)_3` | sextic `χ_·(h) = conj((h/·)_3)·(h/·)_2` (an extra quadratic factor) |
| Poisson in the row variable | cubic Gauss sums cancel `g̃` | `γ₁γ₂ = μαG` (eq:gj): Gauss sums turn back into `μ` |
| plain side | `Σ_{k ≲ B²/A} \|Σ_b β_b (k/b)_3 N(b)^{−1/2}\|²` | original `Σ_{N u ≤ H} \|A_u(D)\|²`, with `A_u = Σ μ(n)ν(n)ψ_u(n) W` |
| principal dual frequencies | `k` a cube → Patterson bias | `u = ε v⁶` → `A_{εv⁶} ≈ A_ε(D)`: the extraction rows |
| GRH input | axiom (iv) for `β` = primes vs `(k/·)_3` | axiom (iv) for `μν` vs `ψ_u`, i.e. quasi-GRH for `L(s, ψ_u)`, `N u ≤ H` |
| column sequence | primes (external to the conclusion) | `μν` (its cancellation *is* the conclusion) |

The involution is in the source. Oct 5 Lemma lem:arithmetic: "(eq:convert2) converts the Möbius
coefficients to `a_ξ(n)` …, while (eq:convert1) converts them back". Step 5 then says: "We now
expand the square and apply Poisson summation in h as before; … The Gauss-sum coefficients become
Möbius coefficients."

The decisive difference is the last row of the table. DR assume GRH for *other* L-functions
(cubic Hecke characters against primes) to prove a statement about Gauss sums. Transplanted, the
same step assumes GRH for the very family whose principal member we want to bound.

## 3. Can the GRH step be replaced by averaging over the rows? (PROPOSED; exponents checked by script)

Write `M₂(ρ) = Σ_{N u ≤ D^ρ} |A_u(D)|² ≪ D^m`. PR 910 Prop. 7.2 (`k = 1`, linear in the moment
exponent) turns this into the boundary `σ(m, ρ) = (m − ρ/6)/2`. The target is `m = 1 + ρ`, which
gives `1/2 + 5ρ/12`.

**(a) Pointwise transplant: axiom (iv) at loss `η` for all non-principal rows.**
* This gives `m = 1 + ρ + 2η`, hence `σ = 1/2 + η + 5ρ/12`.
* With `η = β* − 1/2` from a family half-plane `Re s > β*`, this is `β* + 5ρ/12 > β*`. There is no
  gain for any `ρ > 0`.
* Even `β* = 11/12` would have to hold *uniformly* in `N u ≤ H`. The Oct 5 output is stated for a
  fixed `ν`; RUNG_STRENGTH §2 Remark says the conductor enters as `(N u)^{1/12}`.
* With `η = 5/12`, DR's own hypothesis `η ≤ 1/4` fails.
* On the dual side, the original off-diagonal is then `≲ H·D^{2β*}`. Scaled by `L/H`, this gives a
  dual off-diagonal of `L^{1+2β*} = L^{17/6}`, against the required `L^2`. Relative to
  `S_diag ≍ L³/H`, that is `H·L^{−1/6}`: worse than trivial once `ρ > 1/6`.

**(b) A large sieve over the rows `u` (or over `h`).**
* Over `u` it is row-blind: the single-row example gives `Δ ≥ L` (RUNG_STRENGTH §3a). So it yields
  `m = max(1 + ρ, 2)` and `σ = 1 − ρ/12 > 11/12` for `ρ < 1`.
* Over `h` it is the Oct 5 Step 4 route (§4). It keeps the dual diagonal, which is the same loss.

**(c) Zero-density counts for the family.** [standard zero-detection; HEURISTIC in constants]

Assume:
* (Z1) every `L(s, ψ_u)` with `N u ≤ H` is zero-free in `Re s > β*`, with polylog control of
  `log L`;
* (Z2) `Σ_{N u ≤ H} N_u(σ, D^ε) ≪ H^{A(1−σ)+ε}`, counted over **rows**, i.e. with the multiplicity
  `(H/N w)^{1/6}` of each member `ψ_w`.

Rows whose L-function has no zero right of `σ` have `|A_u| ≪ D^{σ+ε}`. Hence

    M₂(ρ) ≪ D^{1+ρ+ε} + max_{1/2 ≤ σ ≤ β*} D^{Aρ(1−σ) + 2σ + ε}.

For `ρ < 2/A` the maximum is attained at `σ = β*`, and

    σ_new = β* + ρ (A(1 − β*) − 1/6)/2,      fixed point  β* = 1 − 1/(6A).

* **DH (`A = 2`) gives exactly 11/12.** The script checks this on a grid `ρ ∈ (0, 1]`:
  * starting from `β* = 11/12`, the output is 11/12 for every `ρ`;
  * from `β* < 11/12` it is worse than the input;
  * from `β* > 11/12` it is never below 11/12.
* For `ρ ≥ 1`, DH gives `m = 1 + ρ`, i.e. the Oct 5 range.
* `A = 12/5` gives 67/72 and `A = 3` gives 17/18 (script item (4)).
* The multiplicity is unavoidable. The principal member alone contributes `H^{1/6}` rows, and
  `H^{1/6} ≤ H^{2(1−σ)}` is exactly `σ ≤ 11/12`. So a DH count over rows already *contains* the
  11/12 statement for `ζ_K`. This is the same leverage as the extraction, and the reason the
  fixed point appears.
* For comparison, Kintali's closed form `max(11/12, 7/6 − 1/(2A))` (SYNTHESIS §2.5) agrees at
  `A = 2` only. It is a different architecture.

**(d) Relative precision reached.**
* Under (Z1)+(Z2) with `A = 2`, the dual off-diagonal is controlled to `L²·D^{(2β*−1)(1−ρ)}`. That
  is relative precision `(H/L)^{2(1−β*)}` against `S_diag`, compared with the required `(H/L)^1`.
* At `β* = 11/12` this is `(H/L)^{1/6}`.
* It reaches `H/L` only at `β* = 1/2`.

**(e) The family `{ψ_h}` on the dual side.** Zeros of `L(s, ψ_h)` do not control `B_h`. Its
Dirichlet series is the twisted cubic-theta series `Σ γ₂(n) conj(α(n)) ξ(n) ψ_h(n) N(n)^{−s}`
(Patterson–Yoshimoto type). It has no Euler product, and no zero-detection argument applies to it.

Even *pointwise* Lindelöf for these series (`|B_h| ≪ D^{1/2+ε}` for all `h`) gives
`Σ_h |B_h|² ≍ 𝓗D`. That is the dual diagonal, i.e. `M₂ ≲ D²` and `σ = 1 − ρ/12`. [EMP]
`a2/dual_diagonal_check.py` (A2_LITERATURE §5) finds `M/Diag ∈ [0.97, 1.14]` for 1.8–43 rows per
column on the `γ₂` dual, so the dual mean square really is diagonal-sized (finite range only).

**Conclusion of §3.** On our dual side, the `h`-average is already the whole object. The average
that DR do *not* exploit is over their dual frequencies `k`, which on our side are the original
rows `u`. Averaging there means the original mean square (involution), a large sieve over `u`
(row-blind, ρ = 1), or zero density over rows (fixed point `1 − 1/(6A)`, i.e. 11/12 under DH).
None of these reaches below 11/12. **Circular, with zero gain.**

## 4. The sub-diagonal second moment and its Poisson dual at ρ < 1

**Exact dual** (Oct 5 Prop. prop:poisson-reduction; the algebra is valid for any `H`). Put
`𝓜_D = D^{−1}Σ_u Φ(N u/H)|A_u(D)|²`. Lemma lem:poisson with `χ = conj(χ_{z₁})χ_{z₂}`, followed by
(eq:convert2), (eq:recip) and (eq:quotient), gives

    𝓜_D = Z + Σ_ξ c_ξ 𝓢_ξ,   Z = (H/D) Φ̂(0) Σ*_g |W(N g/D)|² ∏_{p|g}(1 − 1/N p) ≍ H,

    𝓢_ξ = (H/D²) Σ*_{(b,f)=1} μ(f) N(b) Σ_{k≠0} Σ*_{(m₁m₂,b)=1} a_ξ(m₁) conj(a_ξ(m₂))
           · χ_{m₁}(k f⁴) conj(χ_{m₂}(k f⁴)) · W₀(N(bfm₁)/D) conj(W₀(N(bfm₂)/D))
           · Φ̂(H N(k) / (N(f)² N(m₁) N(m₂))),

where `a_ξ(n) = conj(α(n)) γ₂(n) ξ(n)` and `W₀(x) = x^{−1/2} conj(W(x))` ([eq:initial-column-output]).
The ranges are `N(b)N(f) ≲ D` and `0 < N(k) ≲ D²/(H N(b)²)`. The block `b = f = 1` is
`(H/D)·D^{−1}Σ_{N k ≲ 𝓗}|B_k(D)|²` with `𝓗 = D²/H`. So at `ρ < 1` the dual has
**rows `D^{2−ρ}` > columns `D`**.

**Where the dual diagonal goes.** [INF, exact algebra] The terms `m₁ = m₂` carry weight
`1_{(z,h)=1}·|W₀|²·Φ̂(…)`, which depends only on `z = v m` and not on how it splits. Summed over the
Möbius variable `v` (`f = ev`), they collapse by `Σ_{v|z} μ(v) = 1_{z=1}` to the negligible
`n₁ = n₂` Ramanujan-sum terms. So the exact identity contains **no** dual diagonal. It appears
only once `μ(f)` is replaced by `|μ(f)|`.

**Steps at `ρ < 1`, in order.**

| step | status at `ρ < 1` | cost |
|---|---|---|
| Poisson in `u` (lem:poisson) | exact | none |
| `μγ₋₁ ∝ conj(α)γ₂` (eq:convert2) | exact | none |
| positivity: `\|𝓢_{ξ;B,F}\|` bounded by the full dual mean square `𝓔` ((eq:weighted), smooth-weight lemma with row coefficient `μ(f)`) | **first loss**: drops the `μ(f)` cancellation that removes the dual diagonal | `𝓔 ≳ 𝓗 = D^{2−ρ}` against the needed `XF = D`: factor `D^{1−ρ} = L/H` |
| sufficient condition (eq:auxiliary-target) `𝓔 ≪ D^ε XF` | **false** at `ρ < 1`, unless each block's off-diagonal cancels its own diagonal; [EMP] the `γ₂` dual is diagonal-sized | — |
| theta reflection (lem:reflection) + quadratic large sieve (lem:quadratic) → Prop. R: `Σ_k \|T\|² ≪ 𝓗 + 𝓗²N(f)/X` | reflection *lengthens*: dual length `𝓗²/X > 𝓗 > X` | extra factor `𝓗/X = D^{1−ρ}` |
| cube removal (Step 5): cutoff `H_c = min(X^{1/3}, (X/𝓗)^{2/3})` | `< 1`: the short-cube range is empty, and the recursion's target `𝓔 ≲ X` lies below the diagonal `𝓗` | — |

Net result if Steps 4–5 are granted at no further cost:
`M₂ ≲ D^{max(1+ρ, 2, 3−ρ)} = D^{3−ρ}`, so the boundary is `3/2 − 7ρ/12`. With the positivity loss
alone (a perfect row-blind dual bound), `M₂ ≲ D²` and the boundary is `1 − ρ/12`. Both exceed 11/12
for `ρ < 1`, and both equal 11/12 at `ρ = 1`. So the pipeline optimum is `ρ = 1`, which is the Oct 5
claim. Script items (1)–(2):

| ρ | Oct 5 pipeline | positivity only | target `1/2 + 5ρ/12` |
|---|---|---|---|
| 1/2 | 29/24 | 23/24 | 17/24 |
| 3/4 | 17/16 | 15/16 | 13/16 |
| 9/10 | 39/40 | 37/40 | 7/8 |
| 1 | 11/12 | 11/12 | 11/12 |

**What `ρ < 1` needs instead.** Not a smaller dual mean square, but the cancellation that the
positivity step discards. Equivalently:

(OD_ρ) Σ_{n₁≠n₂} μν(n₁) conj(μν(n₂)) W W Σ_u Φ(N u/D^ρ) χ_{n₁}(u) conj(χ_{n₂}(u)) ≪ D^{1+ρ+ε},

which is the dual off-diagonal at relative precision `H/L`. The DR mechanism applied to (OD_ρ) is
§§2–3: circular.

## 5. Verdict and the smallest unblocking statement

**(b) circular.**
* The DR dispersion step needs pointwise (axiom (iv)) cancellation of the *plain* column sequence
  against every non-principal dual character, up to the dual length.
* For the sextic family the plain side is the family itself, so this is quasi-GRH for
  `L(s, ψ_u)`, `N u ≤ H`. That trivially implies Mom(1, ρ), and by Prop. R it implies member
  half-planes `1/2 + ρ/2`.
* The principal dual frequencies are the extraction rows.
* Every averaged substitute is row-blind or DH-type and stops at `ρ = 1`. Its bootstrap has fixed
  point `1 − 1/(6A)`, which is 11/12 under DH.
* (c) also applies, independently: DR24's estimate controls only the large-sieve scale
  `(A + B)B` (§1.4). It is not the needed relative-precision asymptotic even conditionally.

> **Coordinator note.** [Q_RHO_ANALYSIS.md](Q_RHO_ANALYSIS.md) shows that the theta reflection is
> also an involution, so "non-involutive" below is incorrect. It also shows that (Q_ρ) is
> equivalent to Mom(1, ρ) by Poisson in `h` (the manuscript's own lem:first-transfer).

**Smallest statement that would unblock the route.**
* (OD_ρ) for one fixed `ρ < 9/10` would beat 7/8. It is equivalent to Mom(1, ρ), so it is not a
  reduction.
* Within the DR paradigm, no smaller lemma exists: the only external input DR use becomes the
  conclusion.
* A candidate that is not visibly circular has to come from the non-involutive theta reflection.
  After Prop. lem:reflection the dual block becomes, up to the fixed finite sums and weights of
  that proposition,

      T_h ≈ Σ_m d(m) α(m) N(m)^{−1/2} χ_h(m)³ V♯(N(m) X / N(h)²),   N(m) ≲ M_h = N(h)²/X.

  **(Q_ρ) [OPEN; HEURISTIC formulation]:** with `𝓗 = D^{2−ρ}` and `X = D`,

      Σ*_{N h ≤ 𝓗} |T_h|² = Diag(𝓗) + (explicit secondary terms) + O(D^{1+ε}).

  * This is a mean square of **quadratic** twists of cubic-theta cusp coefficients, with rows
    `𝓗 < M ≍ 𝓗²/X` (row/column exponent `(2−ρ)/(3−2ρ) ∈ (ρ, 1)`).
  * It is required at relative precision `X/𝓗 = H/L` below its diagonal.
  * Its Poisson dual (in `h`) carries quadratic Gauss sums against `γ₂`-type coefficients, so it
    does not visibly return to `A_u`.
  * Whether (Q_ρ) is equivalent to (OD_ρ) by some other duality has not been checked.
  * No large sieve can prove it: it is sub-diagonal, and the quadratic large sieve gives
    `(𝓗 + M)`, i.e. a loss of `(𝓗/X)² = D^{2(1−ρ)}` against the needed `X`.

## 6. What this note does not show

* No zero-free region and no moment bound is proved. The exponent algebra in §§3–4 is
  bookkeeping on stated inputs.
* §3(c) uses a standard zero-detection step (Perron for `1/L` plus Borel–Carathéodory) that is not
  written out here.
* The range analysis of DR24 (§1.2, "operator-norm reason", and the claim that the cubic large sieve
  suffices in broad Type II) is our inference. DR24 do not state it.
* DR24 was read from the arXiv v3 TeX source. The published Annals version was not compared.
* The dictionary in §2 ignores ray-class phases `G`, `𝓡`, `ξ`, units and the masks at `S`. These
  are finite-order data (Oct 5 Lemma lem:arithmetic) and do not affect exponents.
* Suggested follow-up, not done because existing files were not to be edited:
  * propagate the §0 item 4 correction to A2_LITERATURE §§0, 5, RUNG_STRENGTH §3(b), SYNTHESIS §2
    and AGENDA;
  * cite the fixed-point law `1 − 1/(6A)` (§3c) from RUNG_STRENGTH §4.

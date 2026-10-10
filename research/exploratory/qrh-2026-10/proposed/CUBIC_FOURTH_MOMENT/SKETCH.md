# PROPOSED proof sketch: a Lindelöf-on-average fourth moment for cubic Hecke L-functions over Q(ω), conditional on the Lemma 18.1 scheme

```text
Status: PROPOSED proof sketch, CONDITIONAL, for expert scrutiny. The theorem is OPEN. Nothing here
  is proved unconditionally; no reviewed result is strengthened. RH is not addressed.
Scope: the bound sum_{q in F'_3(X)} |L(1/2, chi_q)|^4 << X^{1+eps} for the thin cubic family of
  David-de Faveri-Dunn-Stucky (squarefree q = 1 mod 9 in Z[omega]). It assumes the order-
  independent core of case 1 (z = 0) of Lemma 18.1 of the external, unreviewed OpenAI manuscript
  and a PROPOSED nested induction order. This note restates, in one place, the route assembled in
  CUBIC_FOURTH_MOMENT_TRANSFER.md, CUBIC_RELAXED_INDUCTION.md, reviews/CUBIC_NESTED_REDTEAM.md and
  CUBIC_N3_GAPS.md. It adds the application step written out (Sec. 2) and a closed form for the
  closing margin (Sec. 3.5). It does not re-review the inherited analytic core.
Exact sources or dependencies: see Sec. 7 and README.md in this folder.
What was actually run: see README.md (three ledger scripts rerun with unchanged pass counts; one
  new exact check of the closing margin, 7/7, text in the Appendix).
Smallest remaining gap: the inherited centred stage. Lemma centered-coefficient-invariant
  (paper.tex l. 13954) and lattice cancellation must remove the Theta-row main terms. For n = 3
  they must do so to relative precision Z^{-(A - 2M/3)}, up to about Z^{-M/3}, with comparison
  length L up to about 0.42M-0.43M. They must also do so when the input is itself a reflected
  comparison (nested order). The sextic proof needs only Z^{-M/6} with L = M/4. A uniform hidden
  loss of (11 - 147 delta)M/432 (about 0.022M-0.025M) in the centred deficit breaks the two-stage
  route; M/12 breaks every nested version.
```

RH is unsolved. This note does not prove or disprove RH, Lemma 18.1, or any moment bound. Every
statement below is labelled. "Proved here" means a complete argument is written in this note; it
has not been refereed. "Sketched" means the argument is given in outline. "Imported" means a
published or standard theorem, or a step of the external manuscript, used as stated.
"Unverified" means nobody has checked it beyond exponent ledgers.

## 0. Summary

* **Target (OPEN).** `Σ_{q ∈ F'_3(X)} |L(1/2, χ_q)|⁴ ≪_ε X^{1+ε}`. The family has `≍ X` members, so
  this is Lindelöf on average. GLH implies it trivially. The best unconditional bound found in the
  literature is `X^{4/3+ε}` (cubic large sieve; Sec. 1.4).
* **Route.** Prove a cubic analogue, Statement C, of case 1 of Lemma 18.1 by induction on the
  width. Then deduce the target by the approximate functional equation (Sec. 2). The application
  step is routine and is written out completely here. All the risk sits in Statement C.
* **What Statement C needs.**
  * (H-A) The order-independent analytic core of Lemma 18.1, case 1, holds verbatim at n = 3.
  * (H-B) A nested comparison order is admissible: a centred stage may call an earlier centred
    stage at the same width.
  * The cubic finite lemmas of Sec. 4. They are proved or sketched here, with exact finite checks.
* **Exponent bookkeeping.** With two centred stages the closing condition holds with uniform
  margin `μ*(δ) = (11 − 147δ)/612` (in units of `M`), where `δ` is the padded-core excess. That is
  `11/612 ≈ 0.0180` at `δ = 0`, at split `b_1 = 31/36`. This closed form reproduces the red team's
  grid values `0.01794` and `0.01555` (Sec. 3.5). A hidden loss confined to the centred deficit is
  tolerated up to `(11 − 147δ)/432`, which is `≈ 0.0255` at `δ = 0`.

## 1. Statement and hypotheses

### 1.1 Notation and family

* `F = Q(ω)`, `O = Z[ω]`, `d_F = −3`. `λ` is the prime above 3. `S = {(2), (λ)}`.
* For `q ≡ 1 (mod 3)`, `χ_q(α) = (α/q)_3`, the cubic residue symbol (DDDS eq. `chiqdef`).
* `F'_3 = {q ∈ O : q ≠ 1, q ≡ 1 (mod 9), q squarefree}` and `F'_3(X) = {q ∈ F'_3 : N q ≤ X}`
  (DDDS eqs. `F3def`, `F3primedef`). For `q ∈ F'_3`:
  * `χ_q(ω) = χ_q(λ) = 1` (DDDS Remark `supprem`, from the supplement `cubesupp`). So `χ_q`
    is trivial on units and defines a Hecke character of trivial infinity type on ideals.
  * `χ_q` is primitive with conductor `q O` (DDDS, the paragraph after `C3def`).
  * `|F'_3(X)| ∼ C_2 X` (DDDS, Sec. 1).

DDDS = David, de Faveri, Dunn, Stucky, "Non-vanishing for cubic Hecke L-functions", arXiv
2410.03048v2. Its e-print source was read with grep/sed (sha256 `ba8542c8…c8e1`). Equation and
lemma names are its LaTeX labels. The labels `chiqdef` to `supprem` are in its Sec. 1; the
others cited here are in Sec. 3 ("Preliminaries").

### 1.2 The theorem

> **Theorem C4 (PROPOSED; CONDITIONAL on (H-A), (H-B); OPEN).** For every `ε > 0` and `X ≥ 2`,
>
>     Σ_{q ∈ F'_3(X)} |L(1/2, χ_q)|⁴ ≪_ε X^{1+ε}.
>
> The sum has a sharp cutoff and no weights. The implied constant depends only on `ε`.

* **Variant** (sketched, same hypotheses): at `1/2 + it` the bound is
  `≪_ε X^{1+ε}(1+|t|)^{O(1)}`, by the same argument with DDDS Lemma `afe` in place of `afecenter`.
* **Supporting variants** (CONDITIONAL, from the earlier notes, not re-derived here):
  * (H-A) without (H-B), single window: `X^{53/51+ε}` (CUBIC_RELAXED_INDUCTION.md Sec. 3).
  * (H-A) plus the (2,1) forcing of Lemma 4.L instead of (H-B): `X^{1+ε}` with **zero** slack.

### 1.3 Hypotheses: imported versus new

**Imported, standard (published).**

| id | statement | source |
|---|---|---|
| I1 | cubic reciprocity `(a/b)_3 = (b/a)_3` for coprime `a, b ≡ 1 (mod 3)`; supplements for `ω, λ` | DDDS eqs. `cuberep`, `cubesupp` |
| I2 | functional equation of a primitive Hecke character `ψ` of `F` of trivial infinity type: `Λ(s,ψ) = (3 N𝔠_ψ)^{s/2}(2π)^{−s}Γ(s)L(s,ψ)` is entire for `𝔠_ψ ≠ O`, and `Λ(s,ψ) = W(ψ)N(𝔠_ψ)^{−1/2}Λ(1−s, ψ̄)`; the factor `W(ψ)N(𝔠_ψ)^{−1/2}` has modulus one (standard; for `χ_q` see I3) | DDDS Prop. `funceq`, which cites Neukirch, *Algebraic Number Theory*, VII Cor. 8.6 (not re-read here) |
| I3 | root number of `χ_q`, `q ∈ F'_3`: `W(χ_q)/N(q)^{1/2} = g̃_3(q) := N(q)^{−1/2} g_3(q)`, the normalized cubic Gauss sum, with `\|g̃_3(q)\| = 1` | DDDS Remark `rootnumber`; eqs. `generalgauss`, `normalized`, `sqrootcancel` |
| I4 | approximate functional equation and decay of its weight | Iwaniec-Kowalski, *Analytic Number Theory* (AMS Colloq. Publ. 53, 2004), Thm 5.3 and Prop. 5.4; specialised in DDDS Lemmas `afecenter`, `afe`, `decaylem` |
| I5 | Kummer theory with `μ_3 ⊂ F`; Artin reciprocity | as cited by the manuscript (Milne, CFT, VIII (5.3), (5.5)) |
| I6 | lattice Poisson summation; Rankin's bound; divisor bounds; counts of powerful ideals | standard |

**Imported from the external, unreviewed manuscript: hypothesis (H-A).** The source is pr908
`31c706bb…`, `paper.tex` sha256 `42a5ee0f…deac6a3` (re-hashed for this note), read as untrusted
data. (H-A) says that the following steps of case 1 (`z = 0`) of Lemma 18.1 hold verbatim at
`n = 3`, once the order-dependent inputs are replaced by those of Sec. 4:

| id | step | lines | agent review on record |
|---|---|---|---|
| A1 | mask erasure, reflection to the padded core, rowwise unit boxes | 12602-12830 | LEMMA18_1_REVIEW: no error |
| A2 | first Poisson transform with complete common support; Möbius label `s`; one Fourier measure for kernels and inverse roots | 13114-13409 | LEMMA18_1_COMMON_SUPPORT: no error, 24/24 |
| A3 | Gauss-row enlargement (zero-slot) | 13411-13594 | LEMMA18_1_REVIEW: no error |
| A4 | second transform: diagonal, complete extraction, `𝔱`-allocation, child normalization, coefficient lemma | 13596-14310 | all three Lemma 18.1 notes: no error |
| A5 | Lemma `centered-coefficient-invariant` and Lemma `centered-lattice-cancellation` | 13954-14000, 14545-14660 | REVIEW, COMMON_SUPPORT: no error |
| A6 | completion of the finite induction | 14779-14984 | LEMMA18_1_CASE2_SEC188: no error |
| A7 | helper Lemmas 4.5 `smooth-calculus` and 4.7 `kernel-seminorms` | 1123-1413 | SEP30_L13_L45_REVIEW: no wrong step found, 33/33 |

All of these are **bounded agent reviews**. No human expert has checked Lemma 18.1. Its case 1 would
itself be a new unconditional sextic fourth moment, beyond the conjecturally optimal sextic large
sieve (reviews/LEMMA18_1_REVIEW.md Sec. 1; reviews/CUBIC_NESTED_REDTEAM.md Sec. 4.2).

**New, hypothesis (H-B).** The nested comparison order of Sec. 3.3 is admissible. It is a
reordering, not a new estimate, and the red team found it well-founded. It is not in the
manuscript and has not been checked against the manuscript's bookkeeping line by line.

**New, supplied in this note (Sec. 4).** These are the cubic finite lemmas 4.A-4.K: Gauss sums at
prime powers, correlations, the `𝔯`-classification, the allowance `B_c` and its budget,
`κ_1 = 5/6`, the `F_2` table (`κ_2 = 1`), Kummer with `μ_3` and the exceptional count, the
Gauss-row zero, the centred deficit, and the row functional equation. They are proved or sketched
and are not hypotheses of Theorem C4. Their status is in the risk register (Sec. 5).

### 1.4 Literature position (primary sources)

* **Large sieve.** The cubic large sieve `(M + N + (MN)^{2/3})(MN)^ε` (Heath-Brown, as quoted in
  Baier-Young arXiv 0804.2233, eq. `HBcubic`) gives `X^{4/3+ε}` at `M = N = X`.
  de Faveri (arXiv 2610.04045) coincides with it for `n = 3`.
* **Non-orthogonality.** de Faveri-Dunn-Hoffstein (arXiv 2607.07911) prove, unconditionally, that
  the cubic large sieve is not perfectly orthogonal. The large-sieve route is therefore capped at
  `X^{4/3}`.
* **DDDS.** DDDS (2410.03048v2, Sec. 1, source l. 494-501), citing Dunn-Radziwiłł (under GRH),
  state: "the cubic large sieve is *not* perfectly orthogonal, so an optimal fourth moment bound
  is not available in the cubic case". They also
  note that the second moment over the full family behaves like the fourth moment over `F'_3`.
* **Baier-Young.** Baier-Young (0804.2233) treat cubic Dirichlet characters over Q, a different
  family, and prove no fourth moment.

No unconditional bound below `X^{4/3+ε}` was found (earlier notes' arXiv searches; not repeated
here). Theorem C4 would be new.

## 2. The application step (proved here, given Statement C)

Statement C is stated in Sec. 3.1. This section proves:

> **Proposition 2.1 (proved here, conditional only on Statement C at `q = 0`).** If Statement C
> holds for `m = 1`, `q = 0`, `τ = 1`, `n_1 = n_2 ∈ [0, 3/4]`, uniformly over the profiles
> `W_w` below with polynomial dependence on `|Im w|`, then Theorem C4 holds.

**2.1 Functional equation, root number, conductor.**

* For `q ∈ F'_3`, the character `χ_q` is primitive with conductor `q O`, of trivial infinity type
  (Sec. 1.1).
* By I2, `Λ(s, χ_q) = (3 N q)^{s/2}(2π)^{−s}Γ(s)L(s, χ_q)` is entire. The analytic conductor is
  `3 N q`, a degree-2 gamma factor over Q (`(2π)^{−s}Γ(s) = const · π^{−s}Γ(s/2)Γ((s+1)/2)` by
  duplication).
* `Λ(s, χ_q) = g̃_3(q) Λ(1−s, χ̄_q)` (I2, I3). The root number is the normalized cubic Gauss sum
  `g̃_3(q) = N(q)^{−1/2} Σ_{d mod q} χ_q(d) ě(d/q)`, with `ě(z) = e^{2πi(z + z̄)}`.

**2.2 Approximate functional equation.** Apply I4 (IK Thm 5.3) with `G ≡ 1`, balanced at
`√(3Nq)`, at `s = 1/2`. DDDS Lemma `afecenter`:

    L(1/2, χ_q) = A_1(q) + g̃_3(q) · \overline{A_1(q)},
    A_1(q) = Σ_{𝔫 ≠ 0} χ_q(𝔫) N𝔫^{−1/2} Φ_1(N𝔫 / √(3Nq)),
    Φ_1(y) = (2πi)^{−1} ∫_{(2)} (2π)^{−w} y^{−w} Γ(1/2+w)/Γ(1/2) dw/w,

with `y^k Φ_1^{(k)}(y) ≪_{k,A} (1+y)^{−A}` (DDDS eq. `Phi_bound`). The second sum is the
conjugate of the first because `Φ_1` is real on `(0, ∞)`.

**2.3 Why the root numbers cancel.** `|g̃_3(q)| = 1` for squarefree `q` (DDDS `sqrootcancel`).
Hence

    |L(1/2, χ_q)| ≤ 2 |A_1(q)|,   |L(1/2, χ_q)|⁴ ≤ 16 |A_1(q)|⁴.

So **no information about cubic Gauss sums is used**: the root number has modulus one and leaves
every `|·|²`. The same holds inside the induction. The manuscript reflects a plain factor only
inside `|S S|²` (l. 12785-12789), and conjugating the reflected factor turns `S_{ψ̄}(n; W̃)` back
into a `ψ`-sum with conjugated profile. So `ε(ψ_k)` never appears non-absolutely
(CUBIC_NESTED_REDTEAM Sec. 2, "Root numbers").

The Gauss sums do matter elsewhere. An *asymptotic* would need the cross terms `g̃_3(q)` and
`g̃_3(q)²`, which produce Patterson-type secondary terms. Inside the scheme, the Gauss-sum bias
reappears as the Θ-row excess `A − 2M/3` of Sec. 3.4 (CUBIC_NESTED_REDTEAM Sec. 4.2). The upper
bound avoids the former but not the latter.

**2.4 Dyadic decomposition and truncation.**

* Fix `φ ∈ C_c^∞([1/2, 2])` with `Σ_{j ∈ Z} φ(y/2^j) = 1` for `y > 0`.
* Split `A_1(q) = Σ_{j ≥ −1} A_1^{(j)}(q)`, inserting `φ(N𝔫/2^j)`.
* **Truncation.** For `2^j ≥ X^{1/2+ε}`, trivial bounds and `Φ_1(y) ≪ y^{−A}` give
  `|A_1^{(j)}(q)| ≪ 2^{j/2}(2^j/√(3X))^{−A}`. Summed over these `j` this is `O(X^{−10})`.
* That leaves `J ≪ log X` pieces with `N_j := 2^j ≤ X^{1/2+ε}`. By the power-mean inequality,
  `|A_1(q)|⁴ ≤ (J+1)³ Σ_j |A_1^{(j)}(q)|⁴ + O(X^{−10})`.
* Pieces with `N_j < 2` involve `O(1)` ideals. They are `O(1)` per `q`, hence `O(X)` in total, so
  below we take `N_j ≥ 2`, that is `n ≥ 0`.

**2.5 Separating `q` from the weight.**

* In each finite piece insert the Mellin integral for `Φ_1` and move it to `Re w = ε_0 := 1/log X`.
  No pole is crossed: `Γ(1/2+w)` has poles only at `Re w ≤ −1/2`. Then

      A_1^{(j)}(q) = (2πi)^{−1} ∫_{(ε_0)} (2π)^{−w} (Γ(1/2+w)/Γ(1/2)) (√(3Nq)/N_j)^{w} S_q(N_j; W_w) dw/w,
      S_q(N; W) := N^{−1/2} Σ_𝔫 χ_q(𝔫) W(N𝔫/N),   W_w(y) := y^{−1/2−w} φ(y).

* `|(√(3Nq)/N_j)^w| ≤ (3X)^{ε_0/2} ≪ 1`. The measure `|Γ(1/2+w)| |dw/w|` on `Re w = ε_0` has
  total mass `≪ log log X`, because `|w|^{−1} ≤ (ε_0 + |Im w|)^{−1}` and `Γ` decays
  exponentially.
* Hölder in `w` gives

      |A_1^{(j)}(q)|⁴ ≪ (log log X)³ ∫_{(ε_0)} |S_q(N_j; W_w)|⁴ dν(w),   dν = |Γ(1/2+w)||dw/w|.

* The seminorms of `W_w` grow like `(1 + |Im w|)^{O(1)}`, which `ν` absorbs.

**2.6 Removing the `S`-part.**

* Write `𝔫 = λ^a 2^b 𝔫'` with `𝔫'` prime to 6. Then `χ_q(𝔫) = χ_q(2)^b χ_q(𝔫')`, since
  `χ_q(λ) = 1`, and `|χ_q(2)^b| ≤ 1`. So

      S_q(N; W) = Σ_{a,b ≥ 0} χ_q(2)^b (3^a 4^b)^{−1/2} S^S_q(N/(3^a4^b); W),

  where `S^S` restricts to ideals prime to 6.
* Hölder with weights `ω_{ab} = (3^a 4^b)^{−1/2}`, `Σ ω_{ab} < 5`, gives
  `|S_q|⁴ ≤ 5³ Σ_{a,b} ω_{ab} |S^S_q(N/3^a4^b; W)|⁴`.
* Empty inner sums (`N/(3^a4^b) < 1/2`) vanish.

**2.7 Identification with Statement C.**

* **The rows match the family.** Take `Z := X`, so the row width is `m = 1`, with `q = 0` (no
  moving support) and `τ = 1`.
  * The row `k = q` has `ψ_q(𝔫) = (q/𝔫)_3`, the power-residue symbol of the ideal `𝔫`.
  * Every prime ideal `𝔭 ∤ 3` has a unique generator `π ≡ 1 (mod 3)`.
  * By I1, `(q/π)_3 = (π/q)_3 = χ_q(𝔭)`.
  * Hence `ψ_q = χ_q` on ideals prime to 6.
* **The family lies in `R_0`.** `χ_q` is nonprincipal, so `q ∈ R_0`. Positivity bounds the sum
  over `F'_3(X)` by the sum over all `k ∈ R_0` with `N k ≤ X`.
* **The sums are plain polynomials.** `S^S_q(N; W) = S_{ψ_q}(n; W)` with `X^n = N`, in the
  manuscript's normalisation `S_ψ(n; W) = Z^{−n/2} Σ_l ψ(l) W(q_l/Z^n)` (l. 12477-12531).
* **Statement C applies.** Apply it with `n_1 = n_2 = n ∈ [0, 1/2 + ε]` and `W_1 = W_2 = W_w`:

      Σ_{k ∈ R_0, Nk ≤ X} |S_{ψ_k}(n; W_w)|⁴ = Σ |S_{ψ_k}(n; W_w) S_{ψ_k}(n; W_w)|² ≪_ε X^{1+ε}(1+|w|)^{O(1)}.

* **Collecting.** The losses are `(log X)³` from 2.4, `(log log X)³` from 2.5 and `5³` from 2.6.
  This proves Theorem C4 from Statement C. ∎

Since `A = 2n ≤ 1 + 2ε`, the application uses only the padded-core range. The long lengths that
need reflection occur inside the induction, not here.

## 3. The induction, restated

All lengths are in units of `log Z`. Width `M = m + q`. Total `A = n_1 + n_2`. `θ = 1/3`.
Check IDs carry a script prefix:

* TL: `scripts/cubic_fourth_moment_ledger.py`, 31/31;
* RI: `scripts/cubic_relaxed_induction.py`, 39/39;
* LC: `scripts/cubic_local_checks.py`, 38/38;
* RT: the red team's `nested_redteam_check.py`, 7/7, text in reviews/CUBIC_NESTED_REDTEAM.md
  (not rerun);
* CM: the Appendix, 7/7.

TL, RI and LC were rerun for this note with unchanged counts.

### 3.1 The hypothesis with loss parameter

> **H(M; η).** For every admissible zero-slot datum of width `M` and every `ε > 0`:
>
>     Σ_{k ∈ R_0} |S_{ψ_k}(n_1; W_1) S_{ψ_k}(n_2; W_2)|² ≪_ε Z^{(1+η)M + ε}.
>
> The datum consists of cubic rows `k ∈ O` with `0 < Nk ≪ Z^m`, `ψ_k(n) = τ(n)(k/n)_3`
> zero-extended, the manuscript's moving support of norm `≤ Z^q`, masks, fixed `S`-ray twists
> `Θ` (Lemma 4.H), and smooth profiles. The lengths `n_1, n_2` are arbitrary and bounded.
>
> **Statement C** is `H(M; 0)` for all bounded `M`. The induction must carry general `q, τ` and
> masks, because children have them, even though the application uses `q = 0`.

### 3.2 Parameter order

1. `ε`.
2. `ρ, σ, δ`, small in terms of `ε`, with `δ ≪ min(ρ, σ)` and `δ < 11/147` (positive margin,
   Sec. 3.5).
3. The split `b_1` and the comparison lengths `L_j(A)`, fixed piecewise-affine functions.
4. `ξ ≤ min(ρ/30, μ*ρ/2, ε/(16(k+1)C_*D))` with `k = 2` centred stages and
   `D = 2 + ⌈2M_max/σ⌉` (manuscript l. 12903-12925, l. 14866-14889; red-team correction 4).

### 3.3 The well-founded order (PROPOSED: hypothesis H-B)

Bands of width `σ/4` in increasing `M`. Nodes are `(β, j)`, where `β` is the band and `j` the
stage:

| `j` | stage | totals covered (units of `M`) |
|---|---|---|
| 0 | `U`, uncentred | `A ≤ 2/3` |
| 1 | `C_1`, centred | `2/3 < A ≤ b_1` |
| 2 | `C_2`, centred | `b_1 < A ≤ 1 + δ` (padded core: also `n_i ≤ 1/2 + ξ`) |
| 3 | `R`, reflection closure | all other bounded lengths, reflected into the core |

| call | from | to | why it strictly decreases |
|---|---|---|---|
| child (second transform) | any `(β, j)` | width `≤ M − σ/2`, so band `≤ β − 2` | first coordinate (manuscript l. 14782-14790; width identity TL [A3]) |
| comparison | `C_j`, `j ≥ 1` | `(β, j')`, `j' < j`, same width | second coordinate. **New:** the manuscript allows only `j' = 0` (l. 14799-14804) |
| reflection closure | `(β, 3)` | `(β, ≤ 2)` | second coordinate |

The lexicographic order on `N × {0,1,2,3}` is well-founded, and a branch has at most
`(#bands)·4` nodes (RT [T6]: acyclic call graphs for 8/16/32 bands, `k = 1, 2, 3`).

The centred proof at `C_j` does not depend on the bound for its comparison, only on the choice of
`L`. The comparison enters only through `Σ_{R_0}|S|² ≤ 2Σ_{ball}|Δ_k|² + 2Σ_{R_0}|comp|²`
(l. 12987-13008; RT Sec. 1.3).

### 3.4 Each step's exponent inequality (excess over `(1+η)M`, at `η = 0`)

`T` denotes terminal `O(σ + δ + ξ)` losses. They go into `ε`, never into a multiple of `M`
(CUBIC_N3_GAPS Sec. 3.2 item 5, and LC [L3]: `T = 4σ/3 + (2/3)δ_fr,1 + δ_fr,2/3 + 2θ_N + ε_1 (+δ)`).

| step (manuscript lines) | excess | condition | checks |
|---|---|---|---|
| base `M ≤ ρ` (12925-12928) | `A − q ≤ ρ + δ` | terminal | — |
| reflection to the padded core (12602-12830) | none | Lemma 4.K | — |
| zero frequency, 1st transform (13180-13190) | `m − M ≤ 0` | exponents `≡ 0 (mod 3)` force a powerful product | transfer note Sec. 3, item 2 |
| first-transform ledger (13350-13409) | `(B_c + B_d − (c + d − 2p − R))/2 ≤ 0` | Lemma 4.E | TL [A4], [B8]; RI [R1]; LC [A3] (30000 configurations) |
| Gauss-row zero `h = 0` (13572-13594) | `2a_0/3 − 2s_0 − (a_0 − s_0) ≤ 0` | Lemma 4.I | TL [E1]; LC [G1] |
| diagonal `j = 0` (old-eq:2.12) | `(A − M) + 5σ/3 + δ_fr ≤ δ + T` | `A ≤ M + δ` | TL [A5]; RI [R4] |
| non-exceptional children (old-eq:2.13-2.14) | width `M' = M + J − g − g_2 + t_2 ≤ M − σ` | `g = J_+ + σ`, `g_2 ≥ t_2` | TL [A3]; RI [R2], [R2b] |
| Θ rows, uncentred (old-eq:2.15-2.16) | `A − 2M/3 − F_1 − F_2 ≤ A − 2M/3` | `≤ 0` in `U` | LC [L1] (sympy identity); TL [A1], [A2] |
| Θ rows, centred (2.18-2.19) | `A − 2M/3 − F_1 − F_2 − (L − v)_+ ≤ A − 2M/3 − (5/6)L + T` | Lemmas 4.F, 4.G, 4.J | LC [L4], [T3]; TL [B2], [C2] |
| comparison (12940-13010) | reflected total `A_comp = M − A + 2L + ξ` | must lie in a range proved earlier at width `M` | RI [N1]; RT [T1] |
| caps | all four plain lengths `≥ L`; reflected comparison stays in the core | `L ≤ A/2`, `L ≤ A − M/2` | LC Sec. 3.2 item 1 |

### 3.5 Closing condition and margin (exact)

Take `M = 1`. A centred input of total `A` in stage `C_j` closes if some `L` satisfies:

    (C)   (5/6) L ≥ A − 2/3 + μ
    (R)   1 − A + 2L ≤ b_{j−1} − μ          (b_0 = 2/3)
    caps  L ≤ A/2,   L ≤ A − 1/2 − μ.

**Eliminating `L`.** Take `L = L_j(A) := (6/5)(A − 2/3 + μ)`, the smallest admissible value.

* `C_1` is feasible iff `A ≤ 19/21 − 17μ/7`.
* `C_2` is feasible iff `A ≤ min((5b_1 + 3 − 17μ)/7, (8 − 12μ)/7, 3/2 − 11μ)`.
* The low end `A → 2/3^+` of `C_1` needs only `μ ≤ 5/66`. The low end `A = b_1` of `C_2` adds
  nothing, because there the lower bounds on `A` (`A ≥ 1/2 + μ`, `A ≥ 1 − b_1 + μ`) hold.
* Each feasible set is an interval: `lo(A)` is a maximum of affine maps and `hi(A)` a minimum. So
  checking the endpoints is exact.

**Optimising the split.** Requiring `C_2` to reach `1 + δ` and `C_1` to reach `b_1` gives

    μ*(δ) = (11 − 147δ)/612,    b_1 = (4 + 7δ + 17μ*)/5.

| `δ` | `μ*` | `b_1` | largest `L` used | red-team grid value |
|---|---|---|---|---|
| 0 | `11/612 ≈ 0.01797` | `31/36 ≈ 0.8611` | `≈ 0.422` | `0.01794` at `0.861` |
| 1/100 | `953/61200 ≈ 0.01557` | `3121/3600 ≈ 0.8669` | `≈ 0.431` | `0.01555` at `0.867` |
| 1/50 | `403/30600 ≈ 0.01317` | `≈ 0.8728` | `≈ 0.440` | — |

* **Checks.** CM checks this exactly. It also checks that `μ* + 10⁻⁶` fails for every split
  within `±0.005` of `b_1`, that the single window is empty at `A = 1` (`lo = 2/5 > hi = 1/3`), and
  that the stage ceilings at `μ = 0` are `19/21` and `158/147 > 1` (RI [N1]).
* **Tolerance to a hidden centred loss.** Suppose a uniform extra loss `cM` enters (C) only, with
  no margin demanded elsewhere. Two stages then close iff `c < c*(δ) = (11 − 147δ)/432`, at the same
  split. That is `11/432 ≈ 0.0255` at `δ = 0` and `≈ 0.0221` at `δ = 1/100` (CM). With enough
  stages the bound is `c < 1/12` (RT [T3], at `δ = 0`). The figure `0.0155M` quoted in CUBIC_N3_GAPS
  is the more conservative margin `μ*`, which is demanded in every constraint at once.

### 3.6 Loss bookkeeping (from the manuscript, adjusted)

* **Envelope.** `E_d = T_term + (d+1)(k+1)C_*(ξ + ε_0)`, where `d` is the number of remaining
  strict calls and `k + 1 = 3` same-width calls occur per level. Losses along a branch are a
  maximum of terminal terms plus this sum. They do not compound in the exponent (l. 14925-14938;
  RT Sec. 1.3).
* **Profiles.** The finite set of profile types must be closed under `k = 2` nested reflections
  before `C_ref` is fixed (l. 12790-12797; RT correction 4).

## 4. Cubic-specific lemmas

Notation: `p` is a good prime (outside `S`) and `P = q_p ≡ 1 (mod 3)`.
`χ_p(a) = (a/p)_3 ≡ a^{(P−1)/3} (mod p)`, zero-extended. `χ_c = Π χ_p^{v_p(c)}`.

**Fact 0** (proved). `χ_p` has exact order 3 on the cyclic group `(O/p)^×`, so `χ_p^e` is
principal iff `3 | e`. Also `χ_n(−1) = 1`, since `−1 = (−1)³`. Fact 0 is the only order input in
4.A-4.C (LC [S1]).

**Lemma 4.A (cubic `eq:gauss-local`; proved here).** Let
`G(p^a, k) = P^{−a/2} Σ_{x mod p^a} χ_p(x)^a e(kx/p^a)`, `a ≥ 1`. Then:

    |G(p^a,k)| = P^{(a−1)/2} 1_{v_p(k) = a−1}               if 3 ∤ a,
     G(p^a,k)  = P^{a/2} 1_{p^a | k} − P^{a/2−1} 1_{p^{a−1} | k}   if 3 | a.

*Proof.*

* `χ_p^a` factors through `(O/p)^×`. Write `x = x_0 + p y` with `x_0` a unit mod `p` and `y` mod
  `p^{a−1}`.
* The `y`-sum is `P^{a−1} 1_{p^{a−1} | k}`. Put `k = p^{a−1}k_0`.
* The remaining sum is `Σ_{x_0 ≠ 0} χ_p^a(x_0) e(k_0x_0/p)`.
  * If `3 ∤ a` the character is nonprincipal (Fact 0). The sum is a Gauss sum, of modulus `√P`
    when `p ∤ k_0` and `0` when `p | k_0`.
  * If `3 | a` it is the Ramanujan sum `P·1_{p | k_0} − 1`.
* Multiply by `P^{−a/2}P^{a−1}`. ∎

Exact checks: LC [G1] at `Np = 7` (`a ≤ 4`), `13` (`a ≤ 3`) and inert `25` (`a ≤ 2`); the control
[G1-CTRL] detects the sextic rule. In particular `G(u, 0) = 0` unless `u` is a cube.

**Lemma 4.B (cubic `lem:full-correlation`; sketched).** `F(u,v;j)` is the twisted congruence sum
of old-eq:2.11, with `C = (u,v)`, `u = Cn_1`, `v = Cn_2`. Then `F = 0` unless `C | j`. For
`j = Ck`:

    F = χ_{n_1}(k) χ̄_{n_2}(−k) Π_{p^c ∥ C} L_{p^c}.

The local factors are:

* for `p ∤ n_1n_2`: `L_{p^c} = P^{c−1}χ_p(n_1/n_2)^c · {P − 1 if p | k; −1 if p ∤ k and 3 ∤ c;
  P − 2 if p ∤ k and 3 | c}`;
* for `p` dividing one of `n_1, n_2`: `L_{p^c} = P^{c−1}(P−1)1_{3|c}1_{p∤k}`.

*Sketch.* This is the manuscript's proof (l. 7134-7190) with 6 → 3. The local field sum is
`Σ_{z ≠ 0,1} χ_p^c(z)`, which is `−1` or `P − 2` by Fact 0. The reciprocity factor
`χ_{n_2}(n_1)χ̄_{n_1}(n_2)` is 1 by I1. Exact checks: LC [C1], [F1] (44 brute-force tables,
including `(i, j_0) = (4,3), (5,3), (3,4), (3,5), (3,3)`), [S2] (3298 pairs), with controls.
**Corollary.** For `i > j_0`, `F(p^i, p^{j_0}; j)` vanishes unless `3 | j_0` and `j = p^{j_0}k`
with `p ∤ k`; then it equals `P^{j_0−1}(P−1)χ_p(k)^{i−j_0}`. The first unequal case is `j_0 = 3`.

**Lemma 4.C (cubic child character, `eq:correlation-child-character`; sketched).** For `u = Da`,
`v = Eb` with `(a,b) = 1` and `(ab, DE) = 1`:

    F(Da, Eb; j) = F(D,E;j) χ_a(j) χ̄_b(−j).

All reciprocity factors equal 1 at `n = 3` (l. 7196-7215). The sign is `χ_a(j)`, not its
conjugate. Exact checks: LC [E], six configurations over all `j` (up to `1.07·10⁷` frequencies);
the conjugated control is detected.

**Lemma 4.D (first-transform classification; sketched).** At a common prime with multiplicities
`(i, j) = (v_p(C), v_p(D))`, `χ_C χ̄_D = ξ_𝔯 1_{(k, 𝔠/𝔯) = 1}`. Here `𝔯` is the product of the
primes with `3 ∤ i − j`, and `ξ_𝔯 = Π_{p | 𝔯} χ_p^{(i−j) mod 3}` is primitive modulo `𝔯`.
*Sketch:* Fact 0, prime by prime. The CRT factorisation of the bridge Gauss sum (l. 13250-13262)
holds with trivial reciprocity phase. Exact checks: LC [A-B1], [A-B2], [A-B3]. The control
[A-B2-CTRL] shows that the sextic classification fails at `(4,1)`.

**Lemma 4.E (cubic allowance and budget old-eq:2.6; proved here).** Put
`B_c = ((3c − 4d − 2R)/6)_+` and `B_d = ((3d − 4c − 2R)/6)_+`. Then `B_c + B_d ≤ c + d − 2p − R`.

*Proof.*

* Both numerators cannot be positive: adding them gives `−c − d − 4R < 0`. Say `B_d = 0`.
* Write `c = Σ i`, `d = Σ j`, `p = Σ 1`, `R = Σ r` over common primes (in `log q_p` units), with
  `r = 1_{3 ∤ i−j}`.
* Per prime, budget minus numerator is `(i + j − 2 − r) − (3i − 4j − 2r)/6 = (3i + 10j − 12 − 4r)/6`.
  For `i, j ≥ 1`:
  * if `r = 0` it is `≥ 1/6`;
  * if `r = 1` and `i < j`, then `j ≥ 2` and it is `≥ 7/6`;
  * if `r = 1` and `i > j`, then `i ≥ j + 1` and it is `≥ (13j − 13)/6 ≥ 0`, with equality only
    at `(2,1)`.
* The budget itself is `i + j − 2 − r ≥ 0`. So `(Σ num)_+ ≤ Σ budget` in both cases. ∎

`B_c` occurs at l. 13377, 13422, 13645, 13869 and 14445. Except in (2.6) it always enters with
the favourable sign (LC Sec. 1.3). Exact checks: TL [B8] (`i, j < 200`); LC [A3] (30000 random
configurations, minimum slack 0). The control [A3-CTRL] shows the sextic allowance gives `19/24`.

**Lemma 4.F (`κ_1 = 5/6`; proved here, given the manuscript's `F_1`).** On the branch `J < 0`:

    F_1 = c/3 + 2D_0/3 + q̃/3 + B_c ≥ c/3 + 2d/3 + R/3 + B_c − (2/3)δ_fr,1 ≥ (5/6)c − (2/3)δ_fr,1.

*Proof.*

* If `3c ≥ 4d + 2R`, substitute `B_c`. The `d` and `R` terms cancel exactly.
* Otherwise `2d/3 + R/3 > c/2`.
* On `J ≥ 0`, `F_1 ≥ c` (LC [L2]). ∎

The bound is tight at `(2,1)` primes (TL [B2], [B7]: the miss is exactly `1/3` per prime against
`κ = 1`).

**Lemma 4.G (second-transform table, `κ_2 = 1`; derived from 4.A-4.C plus brute-force maxima).**
Write `F_2 = 2b_2 − (2/3)g_2 − p_2 + t_2 + V/3 + f/3`, in `log q_p` units per prime:

| local case | `F_2` | `b_2` | `F_2 − b_2` |
|---|---|---|---|
| equal `i`, `3 ∤ i`, unit | `4i/3` | `i` | `i/3` |
| equal `i`, `3 ∤ i`, nonunit | `4i/3 − 2/3 + (1/3)1_{i=1}` | `i` | `0` at `i = 1, 2` |
| equal `i`, `3 ∣ i` | `4i/3 − 1` | `i` | `i/3 − 1` (`0` at `i = 3`) |
| unequal `i > j_0`, `3 ∣ j_0` | `i + j_0/3 − 1` | `(i+j_0)/2` | `(3i − j_0 − 6)/6 ≥ 1/2` |

So `F_2 ≥ b_2 ≥ min(c_2, d_2)`. The nonunit `i = 1` entry uses the forced residue
`v_p(h') ≡ 1 (mod 3)` of Corollary 4.H, so `f = v_1`. Without it, `min F_2/b_2 = 2/3 = 2θ`, which
gives zero margin (LC [T3-CTRL]). Checks: LC [T1], [T2], [T3]; TL [C2], [C5].

**Lemma 4.H (Kummer / fixed-numerator ray with `μ_3`; sketched).** Fix `0 ≠ a ∈ O`.

* `F(a^{1/3})/F` is abelian, of exponent 3, and unramified outside `3a`. It is tamely ramified at
  good primes dividing `a`.
* `Frob_𝔭(a^{1/3})/a^{1/3} = (a/𝔭)_3`.
* `𝔄 ↦ (a/𝔄)_3` is a ray class character of conductor supported on `3a`, with exponent `≤ 1` at
  good primes.
* On primary ideals outside `S`, the numerators `u Π_{𝔭 ∈ S} π_𝔭^{v_𝔭}` give at most `3^{|S|+1}`
  characters. Units modulo cubes give 3 classes, since `−1` is a cube.

*Sketch.* Kummer theory (`μ_3 ⊂ F`), the discriminant `−27a²` of `X³ − a`, and Artin reciprocity
(I5). Exact checks: LC [K1] (the characters are periodic mod 18; the mod-6 control fails), [K2]
(exactly 27 characters), [K3].

**Corollary 4.H (exceptional rows; sketched).**

* A child row `h'` induces a member of `Θ` iff its total local exponent is `≡ 0 (mod 3)` at every
  good prime (Fact 0).
* So `(h') = 𝔥_0𝔳³` with `𝔥_0` fixed and cube-free, for each of finitely many `S`/unit data, and

      #{exceptional h' : q_{h'} ≪ Z^{m'}} ≪ Z^{(m'−f)/3+ε}.

* At a second-transform prime with no older moving character, the forced residue is
  `v_p(h') ≡ −e_p (mod 3)`. At nonunit equal-multiplicity primes `e_p = i + 1`, giving residues
  `1, 0, 2, 1, 0, 2` for `i = 1, …, 6`.

Checks: LC [K4] (all 908 good `h'` of norm `≤ 3000`; a finite consistency check, not a proof),
[K5], [K5-CTRL]. This count is the source of the threshold `2M/3` (TL [D6]).

**Lemma 4.I (Gauss-row zero; sketched).** By Lemma 4.A, the added row `h = 0` sees only cube
moduli `u`. Their contribution is `Z^{2a_0/3 − 2s_0}` (transfer note Sec. 3, item 3), which fits
the allowance `a_0 − s_0`. The manuscript's cruder count also fits, with equality at
`s_0 = a_0/3` (TL [E1]).

**Lemma 4.J (centred deficit at n = 3; proved here, given A5).** Assume the caps
`L ≤ min(A/2, A − M/2)` and an input in the padded core. Then, uniformly over every
common-support and `𝔱`-allocation,

    A − 2M/3 − F_1 − F_2 − (L − v)_+ ≤ A − 2M/3 − (5/6)L + T,     v = c + w + min(c_2, d_2).

*Proof.*

* **Lengths.** In the core, `n_i ≥ A − M/2 − ξ ≥ L − ξ`, and `A − L ≥ L`. So all four plain
  lengths are `≥ L − ξ`. The short-plain branch costs at most `M − A + 2L + O(ξ)`, the same as
  the comparison.
* **Saving.** By A5 the two rectangles share character, mask and norm power. Lattice cancellation
  (l. 14545-14660) then gives the relative saving `Z^{−r}` with `Z^r = min(U_i, V_i)`. After
  extraction this is `r = (L − v)_+`. That lemma uses only a fixed finite set of `S`-ray characters
  (Lemma 4.H), a squarefree mask of polynomial norm, and smooth annular profiles. It contains no
  order and no restriction `L ≤ M/4`.
* **Exponents.** In case 1, `w = w_o = ℓ = 0`, so `v = c + min(c_2, d_2)`. By Lemmas 4.F and 4.G,
  `F_1 + F_2 ≥ (5/6)c + min(c_2, d_2) − T ≥ (5/6)v − T`.
* **Maximising over `v`.** `max_v[−(5/6)v − (L − v)_+] = −(5/6)L`, attained at `v = L`: for
  `v ≤ L` the function `−L + v/6` is increasing, and for `v ≥ L` it is `−(5/6)v`. ∎

Checks: LC [L1], [L4].

**Lemma 4.K (reflection input: functional equation and conductor bound for rows; sketched).**

* By Lemma 4.H with `a = k`, `n ↦ (k/n)_3` on ideals prime to `3k` is a ray class character. It is
  tame at good primes, and its `S`-part lies in the fixed family. With the fixed twist `τ` and the
  moving support, the primitive inducing character `ψ*_k` has conductor norm `≪ Z^{m+q} = Z^M`
  (manuscript old-eq:2.1c).
* I2 then gives `Λ(s, ψ*_k) = W N^{−1/2} Λ(1−s, ψ̄*_k)`, with `|W N^{−1/2}| = 1` and gamma factor
  `(2π)^{−s}Γ(s)`. This is all that A1 uses (manuscript Lemma 4.8, l. 1425-1529).
* The zero-extended `ψ_k` differs from `ψ*_k` only at finitely many declared primes. A1's
  mask-erasure handles these.

**Lemma 4.L (optional (2,1) forcing; sketched; not needed under (H-B)).** At a first-transform
prime `p | 𝔯` with `i − j ≡ 1 (mod 3)`, the C-side child character carries `χ_p(u)^{1+i−j+v_p(j)}`.
So an exceptional C-norm child needs `v_p(h') ≡ 1 (mod 3)`, which raises `κ_1` to 1.

*Sketch.* The bridge character is `τ_C(a) = τ(a)χ_a(𝔢𝔯)ξ_𝔯(a)` (l. 13228-13271). Cubic
reciprocity has no phase. Second-transform primes, `𝔱`-labels and positivity never touch `p`
(l. 14317-14326, 13306-13308). Checks: RI [L1]-[L6b]. Some of these are in floating point and
labelled so.

## 5. Risk register

| # | step | status | evidence | most likely failure mode |
|---|---|---|---|---|
| 1 | Application (Sec. 2): AFE, root-number removal, dyadic split, Mellin separation, `S`-part, rows = family | **proved here** (given Statement C) | I1-I4, DDDS `afecenter` | uniformity of Statement C in complex profiles `W_w`; the manuscript's statement asserts polynomial seminorm dependence (l. 12573-12577) |
| 2 | Cubic finite lemmas 4.A, 4.E, 4.F | **proved here** | LC [G1], [A3]; TL [B8] | essentially none at the stated level |
| 3 | Lemmas 4.B, 4.C, 4.D (correlations, child character, `𝔯`) | **sketched** (6 → 3 in the manuscript's proofs) | LC [C1], [E], [F1], [A-B1..3], exact on small moduli | a prime-power case outside the tested tables; low risk |
| 4 | Lemma 4.G (`F_2` table, `κ_2 = 1`) | **sketched** (read off brute-force maxima plus the manuscript's `F_2` formula) | LC [T1]-[T3] | `F_2` formula inherited from the manuscript at `θ = 1/6`, re-instantiated at `θ = 1/3` (LC [L1] identity) |
| 5 | Lemma 4.H and its count `Z^{(m'−f)/3}` | **sketched** | LC [K1]-[K5] | uniformity of the forced residue over all `S`/unit data; low risk |
| 6 | Lemma 4.J (centred deficit) | **proved here, given A5** | LC [L4] | inherits risk 9 |
| 7 | Lemma 4.K (row functional equation, conductor `≤ Z^M`) | **sketched** | standard Kummer and Hecke theory | low risk |
| 8 | Nested order (H-B), Secs. 3.3-3.6 | **new; unverified against the manuscript's bookkeeping** | RT verdict (a) no break; RT [T1], [T6]; CM | the centred stage at width `M` may silently use a property of *original* inputs that a reflected comparison datum lacks (row-dependent dual scales, profile closure, clipping in `ξ`) |
| 9 | A5: centred-coefficient invariance and lattice cancellation, at `L ≈ 0.42M-0.43M` | **imported** (agent reviews only) | REVIEW, COMMON_SUPPORT | see below |
| 10 | A2, A4: common-support transforms and extraction | **imported** | COMMON_SUPPORT 24/24 | a loss `cM` hidden in an allocation, with `c ≥ c*(δ) ≈ 0.022-0.025` (two stages) |
| 11 | A7: Lemmas 4.5 and 4.7 | **imported** | SEP30_L13_L45_REVIEW | misapplied uniformity at some downstream invocation (that review's own open item (i)) |
| 12 | Lemma 18.1 case 1 (sextic) as a whole | **unverified** by any human | three bounded agent reviews | it would already be a new sextic fourth moment beating the conjecturally optimal sextic large sieve; its correctness is the prior question |
| 13 | Single-window fallback `X^{53/51+ε}` | **conditional on (H-A) only** | RI [S1]-[S4] | same as 9-12 |

**Single most likely failure point: item 9.** The step is Lemma `centered-coefficient-invariant`
together with masked lattice cancellation, at the cubic precision.

* **What it must do.** The comparison rectangle's Θ-row main terms must cancel the original's
  exactly: the same `ϑ ∈ Θ`, the same mask `𝔑_*`, and the same norm power `t` after both
  transforms and the full `𝔱`-allocation. They must cancel for every common-support allocation,
  for `L` up to `≈ 0.42M-0.43M` (`M/4` in the sextic proof), and for inputs that are themselves
  reflected comparisons.
* **Why it is the weakest point.**
  * These Θ-row main terms are the scheme's image of the Patterson polar term (CUBIC_NESTED_REDTEAM
    Sec. 4.2). The DDH lower bound shows that this term is genuine for uncentred Gauss-row norms.
  * An allocation-dependent mismatch would not be a small loss. It would leave a main term of
    relative size `Z^{A − 2M/3}`, up to `Z^{M/3}`.
  * This is the one place where the scheme claims to beat a proven obstruction to the
    general-coefficient method.

**Smallest statement whose failure invalidates the route.** For `n = 3`, every centred input in
the padded core must satisfy, uniformly over allocations,

    E − r ≤ A − 2M/3 − (5/6)L + O(σ + ξ)   for L ≤ min(A/2, A − M/2),

and the centred stage must accept reflected comparison data. A uniform extra loss in the centred
deficit of `c*(δ)·M = (11 − 147δ)M/432` (about `0.022M-0.025M`) or more breaks the two-stage route.
A loss of `M/12` breaks every nested version (RT [T3]).

## 6. What would move the status

* An expert line check of A5 and of the coefficient lemma (l. 13934-14310) at general `L`. This is
  the decisive item for both the sextic Lemma 18.1 and this route.
* A written restatement of the manuscript's l. 12903-12938 and l. 14779-14810 with the two-stage
  order and the parameter order of Sec. 3.2. Check it against every place where the manuscript
  uses "the uncentered assertion" (for example l. 12983-12985 and 14534-14536).
* A referee check of Lemmas 4.B-4.D, 4.G and 4.H beyond small moduli.
* A cheap falsification probe: an empirical fourth moment of `F'_3(X)` (the sextic analogue was
  flat to `K = 3·10⁶`; reviews/LEMMA18_1_REVIEW.md Sec. 4). Such numerics cannot confirm Theorem C4.
  A clear `X^{c}` growth with `c > 0` would contradict GLH, not the scheme, so it is a sanity check
  only.

## 7. Sources

* Manuscript: pr908 `31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6`, `standalone/2026-10-07-openai-quasi-
  riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/
  paper.tex`, sha256 `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`
  (re-hashed). Read for this note: l. 1425-1530, 12477-12610, 12903-12925, 12940-13012,
  13954-13995, 14538-14665. Other line numbers come from the notes below.
* Notes (repo HEAD `e606784e6`): CUBIC_FOURTH_MOMENT_TRANSFER.md, CUBIC_RELAXED_INDUCTION.md,
  CUBIC_N3_GAPS.md, reviews/CUBIC_NESTED_REDTEAM.md, reviews/LEMMA18_1_REVIEW.md,
  reviews/LEMMA18_1_COMMON_SUPPORT.md, reviews/LEMMA18_1_CASE2_SEC188.md (skimmed),
  reviews/SEP30_L13_L45_REVIEW.md (header).
* DDDS: arXiv 2410.03048v2 e-print (`revision_1.tex`), sha256 `ba8542c8…c8e1`, labels `chiqdef`,
  `C3def`, `F3def`, `F3primedef`, `supprem`, `cuberep`, `cubesupp`, `generalgauss`, `normalized`,
  `sqrootcancel`, `funceq`, `rootnumber`, `afecenter`, `afe`, `decaylem`, `Phi_bound`; the
  remark on the fourth moment is at source l. 494-501.
* Baier-Young: arXiv 0804.2233 e-print (`cubic_mean_values_2009-09-27.tex`), sha256
  `35172b44…3a59b58`. Prop. `prop:AFE` cites IK Thm 5.3. It treats cubic *Dirichlet* characters
  over Q and the Hecke `L(s, ψ_m)` of rational `m`; neither is this family.
* Iwaniec-Kowalski, *Analytic Number Theory*, Thm 5.3 and Prop. 5.4, cited as DDDS and
  Baier-Young cite them; the book was not re-read.
* de Faveri-Dunn-Hoffstein 2607.07911 and de Faveri 2610.04045, as recorded in
  CUBIC_NESTED_REDTEAM.md; not re-fetched.

## Appendix: `closing_margin.py` (exact text that was run; kept in the session scratchpad)

```python
"""Closed-form check of the two-stage closing condition for the cubic centred stage (M = 1).
Constraints for a centred input of total A in stage j (previous proved range b_{j-1}), margin mu:
  (C)  (5/6) L >= A - 2/3 + mu
  (R)  1 - A + 2L <= b_{j-1} - mu
  caps L <= A/2,  L <= A - 1/2 - mu
Claim: with b_0 = 2/3, a split b_1 and top 1 + delta, the best uniform margin is
  mu*(delta) = (11 - 147 delta)/612   at   b_1 = (4 + 7 delta + 17 mu*)/5,
so mu*(0) = 11/612 at b_1 = 31/36.  A loss c confined to (C) is tolerated iff c < (11 - 147 delta)/432.  EXACT (fractions); grids are exact on each stage by convexity
(lo(A) is a max of affine maps, hi(A) a min of affine maps), and the grid includes both endpoints."""
from fractions import Fraction as F

def window(A, bprev, mu):
    lo = max(F(0), F(6, 5) * (A - F(2, 3) + mu))
    hi = min((bprev - 1 + A - mu) / 2, A / 2, A - F(1, 2) - mu)
    return lo, hi

def covers(b1, top, mu, grid=400):
    for (a0, a1, bprev) in ((F(2, 3), b1, F(2, 3)), (b1, top, b1)):
        for t in range(0, grid + 1):
            A = a0 + (a1 - a0) * F(t, grid)
            if t == 0 and a0 == F(2, 3):
                A = a0 + F(1, 10 ** 9)          # open endpoint of C_1
            lo, hi = window(A, bprev, mu)
            if lo > hi:
                return False
    return True

ok = []
for delta in (F(0), F(1, 100), F(1, 50)):
    mu = (11 - 147 * delta) / 612
    b1 = (4 + 7 * delta + 17 * mu) / 5
    top = 1 + delta
    good = covers(b1, top, mu)
    eps = F(1, 10 ** 6)
    tighter = any(covers(b, top, mu + eps) for b in [b1 + F(k, 10 ** 4) for k in range(-50, 51)])
    lmax = window(top, b1, mu)[0]
    print("delta=%s  mu*=%s (%.6f)  b1=%s (%.5f)  covers=%s  mu*+1e-6 covers for some nearby b1=%s  L at top=%.4f"
          % (delta, mu, float(mu), b1, float(b1), good, tighter, float(lmax)))
    ok.append(good and not tighter)
# single window (no nesting): A = 1 needs (6/5)(1/3) <= (1 - 1/3)/2 - false
lo, hi = window(F(1), F(2, 3), F(0))
print("single window at A = 1: lo=%s hi=%s empty=%s" % (lo, hi, lo > hi))
ok.append(lo > hi)
# stage ceilings at mu = 0: s1 = 19/21, s2 = (5 s1 + 3)/7 = 158/147
s1 = F(19, 21); s2 = (5 * s1 + 3) / 7
print("s1 = %s, s2 = %s, s2 > 1: %s" % (s1, s2, s2 > 1))
ok.append(s2 == F(158, 147))
# loss c confined to (C) (a hidden centred loss), no margin elsewhere: two stages tolerate
#   c < c*(delta) = (11 - 147 delta)/432
def covers_closs(b1, top, c, grid=400):
    for (a0, a1, bprev) in ((F(2, 3), b1, F(2, 3)), (b1, top, b1)):
        for t in range(0, grid + 1):
            A = a0 + (a1 - a0) * F(t, grid)
            if t == 0 and a0 == F(2, 3):
                A = a0 + F(1, 10 ** 9)
            lo = max(F(0), F(6, 5) * (A - F(2, 3) + c))
            hi = min((bprev - 1 + A) / 2, A / 2, A - F(1, 2))
            if lo > hi:
                return False
    return True
for delta in (F(0), F(1, 100)):
    c = (11 - 147 * delta) / 432
    b1 = (4 + 7 * delta + 12 * c) / 5
    good = covers_closs(b1, 1 + delta, c)
    worse = any(covers_closs(b1 + F(k, 10 ** 4), 1 + delta, c + F(1, 10 ** 6)) for k in range(-50, 51))
    print("(C)-only loss, delta=%s: c*=%s (%.5f) at b1=%s covers=%s; c*+1e-6 covers nearby=%s"
          % (delta, c, float(c), b1, good, worse))
    ok.append(good and not worse)
print("SUMMARY %d/%d" % (sum(ok), len(ok)))
```

Output (`python3 -I closing_margin.py`, 4.6 s; script sha256 `e7c73daf…de443eb623`):

```
delta=0  mu*=11/612 (0.017974)  b1=31/36 (0.86111)  covers=True  mu*+1e-6 covers for some nearby b1=False  L at top=0.4216
delta=1/100  mu*=953/61200 (0.015572)  b1=3121/3600 (0.86694)  covers=True  mu*+1e-6 covers for some nearby b1=False  L at top=0.4307
delta=1/50  mu*=403/30600 (0.013170)  b1=1571/1800 (0.87278)  covers=True  mu*+1e-6 covers for some nearby b1=False  L at top=0.4398
single window at A = 1: lo=2/5 hi=1/3 empty=True
s1 = 19/21, s2 = 158/147, s2 > 1: True
(C)-only loss, delta=0: c*=11/432 (0.02546) at b1=31/36 covers=True; c*+1e-6 covers nearby=False
(C)-only loss, delta=1/100: c*=953/43200 (0.02206) at b1=3121/3600 covers=True; c*+1e-6 covers nearby=False
SUMMARY 7/7
```

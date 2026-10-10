# Conditional low-side hypotheses for the 7/8 architecture, priced in its own model

```text
Status: PROPOSED (exact formulations of four hypothesis classes and their derivation into the low
  estimate; elementary, not reviewed) + IMPORTED (the manuscript's lemmas; the dFDH statement,
  quoted verbatim) + model computation (EXACT_RATIONAL LP barriers with dual AND primal
  certificates; FLOATING_RECONNAISSANCE paper-count values, plus one closed form for H-diag).
  Every boundary below is CONDITIONAL on the unreviewed manuscript's other lemmas, on the lemma-range
  extrapolations of Sec. 7, and on the named hypothesis. No hypothesis here is proved. No RH claim.
Scope: the low (reflection) estimate of [OAI] Part II (Prop. 15.4 / TeX l. 8564-8649 and its inputs
  l. 3355-3480, 8085-8125, 8330-8360). The hypotheses replace only its Cauchy-Schwarz/Gram step.
  The high side, the row counts and the floor bin are left as in THRESHOLD_CALCULUS /
  bilinear_b2.py. Two detector floors: a0 = 51/100 (manuscript) and a0 -> 1/2+ (permitted by
  reviews/SEP30_DETECTOR_QUANTIFIERS.md Sec. 4; see Sec. 4.3 below).
Exact sources or dependencies:
  [OAI]  OpenAI, "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8" (30 Sep 2026),
         paper.tex at pr908 (31c706bb), SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3
         (scratchpad copy hash-checked). Untrusted external data; unreviewed. "l. N" = line N.
  [dFDH] A. de Faveri, A. Dunn, J. Hoffstein, "Non-orthogonality of the cubic and quartic large
         sieves via Rankin-Selberg", arXiv:2607.07911 (arXiv metadata: citation date 2026-07-08,
         online date 2026-07-13; the abstract page lists v1 and v2, and the e-print read is the current one); preprint, not refereed. Read from the arXiv e-print source
         (eprint SHA-256 5f60d984...4b3fcc, re-fetched today and byte-identical to the scratchpad copy;
         Revision_1.tex SHA-256 e46244c8...7773e8): eq. (1.3) Xi_3, (1.5) BGL bound, Thm 1.1, Thm 1.2,
         Conj. 1.3, eq. (1.9), proof of Thm 1.1 (Sec. 2).
  [BGL]  Blomer-Goldmakher-Louvel n-th order large sieve, Theorem 1.3 (as quoted by [dFDH]; not re-read).
  Repository: BILINEAR_B2.md, numerics/B2_NUMERICS.md, THRESHOLD_CALCULUS.md, FLOOR_BIN_BARRIER.md,
         RUNG_STRENGTH.md Sec. 2-3, reviews/SEP30_DETECTOR_QUANTIFIERS.md Sec. 4,
         reviews/CONTOUR_LEMMAS_BELOW_7_8.md; scripts/threshold_calculus.py, barrier_lp.py,
         bilinear_b2.py (imported unchanged).
What was actually run:
  scripts/conditional_b2.py (new; SHA-256 recorded in Sec. 9): 13 self-tests PASS (CS low side
    reproduces 7/8 and 11/12 and equals bilinear_b2.low_exact on 300 random rational geometries;
    the relaxed LP reproduces bilinear_b2.lp_barrier for uniform theta; the full LP reproduces
    167/192 and 13/15; endpoint formula = 401-point d-grid for every hypothesis); exact LPs for 8
    hypotheses x 2 floors (+ low side alone), each certified by a rational dual and an exact primal
    vertex; Nelder-Mead over (lx, ly, ell) in the paper-count model, fine-grid re-verification.
  A coarse grid scan of the paper-count high side H(geom) (1782 geometries x 2 floors; scratchpad).
  An exact crossing analysis of the slot-free high side (Sec. 4.2), checked against H_high at
    nde = 41, 241, 2001.
  An extra exact LP showing H-dFDH and CS coincide wherever H-dFDH could matter (Sec. 4.1).
  Machine: 4 shared cores under load 5-10; the model run took about XX min.
Smallest remaining gap: a proof of (H-diag), or of (H-lam) for some lam > 0: a SUB-DIAGONAL mean
  square, over the sextic moduli s ~ Y', of the twisted first moments sum_m b_m q_s^{-1/2}
  g_{chi_s}(s,-m) of the specific completed theta row. Such a bound can never be row-blind
  (Sec. 2.6), and it already contains a power saving for every individual twist. Below it sit
  the lemma-range obligations of Sec. 7: the contour lemmas are reviewed only down to
  139999/160000, and the target here is about 0.69.
```

**RH remains unproved. Nothing here proves or disproves it.** Everything concerns one external,
unreviewed proof architecture. Each "σ_H" is what that architecture *would* deliver under a
named, unproved hypothesis, inside a model of its stated lemma outputs.

## 0. Answer in brief

| hypothesis (Sec. 2) | what it asserts | row-blind? | sub-diagonal? | saving `ϑ(d)` over CS (Sec. 3) | LP barrier, `a0 = 51/100` | LP barrier, `a0 → 1/2⁺` | paper-count model `σ_H` |
|---|---|---|---|---|---|---|---|
| CS (manuscript) | — | — | — | 0 | 167/192 = 0.869792 | 13/15 = 0.866667 | 0.874974 (exact limit 0.874957, PR 910) |
| **(H-dFDH)** | conjectured sextic large sieve, extra terms included | yes | no | `½(2b−ly+d−max(0,b/6))₊` = **0** in every relevant geometry | 167/192 | 13/15 | **0.874974, identical to CS** |
| (H-biasA) | Gram of the Gauss-sum vector without the `P_a^{1/6}` bias | no | no (super-diagonal) | `b/12` | 926/1077 = 0.859796 | 6/7 = 0.857143 | 0.859796 |
| (H-LS) | sharp (bias-free) sextic sieve for the theta-row vector only | no | no (exactly at the wall) | `½ max(0, b/6, 2b−ly+d)` | 251/300 = 0.836667 † | 5/6 † | 0.836667 † |
| (H-λ), λ = 1/2 | twisted first moments at `Q^{1/2}Y'^{1/2}‖b‖²` | no | yes | `G/2 + (lx−d)/4` | 60/77 = 0.779221 | 7/9 = 0.777778 | 0.781933 |
| **(H-diag)** | twisted first moments at their diagonal `Y'‖b‖²` | no | yes (ρ = 23/40 at d = 0) | `G/2 + (lx−d)/2` (= 3/16 at the paper geometry) | 203/303 = 0.669967 | 2/3 | **(√33 − 3)/4 = 0.686141** (ℓ = 0), 0.6836–0.6861 |

`G = max(0, b/6, 2b − ly + d)` is the manuscript's Gram exponent. † marks a vertex at the
degenerate corner `lx = ℓ = 0`, `ly = 1` (X = 1, dual length 1). There the barrier is the
family floor `1 − h/6 = 5/6` of every sieve-level low bound (Sec. 6).

1. **(H-dFDH) buys nothing.** The conjectured norm's genuine extra term `A^{5/6}B^{1/3}`, at
   `A = Q` and `B = Y'`, is exactly the manuscript's Gram excess `Q·P_a^{1/6}`. The other extra
   term `A^{1/3}B^{5/6}` is smaller whenever `Y' ≤ Q`. A conjectured operator norm is row-blind,
   and both splittings then reproduce the manuscript's Cauchy–Schwarz output exactly (Sec. 3.1).
   The only change is that the Gram term `P_a²/Y'` disappears. That term is slack at every
   geometry the model can use (Sec. 4.1). So, conditional on [OAI]'s other lemmas and (H-dFDH),
   the boundary stays **σ_dFDH = 7/8**. Re-optimizing the geometry gives
   `(1507 − 2√921)/1653 ≈ 0.874957`, but that gain comes from PR 910's lemma-range extensions,
   not from (H-dFDH).
2. **The first gain needs coefficient-specific input.** Removing only the Gauss-sum bias (H-biasA,
   H-LS) saves `b/12`, i.e. 1/96 at the paper geometry. Re-optimized, this lowers the barrier to
   6/7–5/6 at best; it cannot pass the 5/6 family floor.
3. **(H-diag) is a sub-diagonal hypothesis. It moves the architecture to its Part I signal offset.**
   * The saving is `ϑ = (lx − d)/2 + G/2`, which is 3/16 at the paper geometry.
   * The low side alone drops to the exact barrier 2/3.
   * With the manuscript's row counts the binding constraint becomes the high side's witnessed
     bins. Without slots the model value is exactly `(√33 − 3)/4 ≈ 0.686141`, at
     `lx = ly = (3√33 − 13)/8 ≈ 0.52921`, ℓ = 0. This value is the same for both floors.
4. **Floor dependence.** Lowering the floor to `1/2⁺` changes every LP barrier by at most 1/300
   (Sec. 4.3). It does not move the paper-count values, because there the floor bin is not
   binding.

## 1. The exact objects (IMPORTED from [OAI]; transcription checked against the TeX)

Notation follows BILINEAR_B2 §1.1: `O = Z[ω]`, `q_a = |a|²`, `χ_c(a) = (a/c)_6` (zero on
nonunits), `g_ψ(c,k) = Σ_{d mod c} ψ(d) e(kd/c)` (l. 3359). Fix the manuscript's arithmetic data
`S, T, b_*, ξ, η` and slot system, the smooth tests `W_0, W_1 ≥ 0` and `Ω` (l. 3456), and a
geometry `(lx, ly, ℓ)` with `ℓ ≤ lx ≤ ly`.

For a rescaled subset `J` with depth `d = Σ_{i∈J} ℓ_i ∈ [0, ℓ]` and a tuple `p_J`, Prop. 15.4
(l. 8584–8589) has

    X' = Z^{lx−d}/r_J,   Y' = Z^{ly−d}/r_J,   Q = q_{b*}X'Y' ≍ Z^{M'},   M' = lx + ly − 2d,   P_a = Y'²/Q ≍ Z^b,

with `r_J ≍ 1`. For `σ ∈ T` and `v ∈ R` define:

* **Row vector** (from (l. 3470) and the marked row `B^J` of l. 8097):

      b_m = b_m^{J,σ,v} := Ω(q_m/Q) ξ(m) (q_m/Q)^{−iv} B^J_{m,σ}(Z),   m ∈ O∖{0};

* **Kernel** (from `A_{m,σ,v}`, l. 3461), over the moduli `s ∈ σ` (primary, prime to `S`, not
  necessarily squarefree):

      K(s, m) := q_s^{−1/2} g_{χ_s}(s, −m);

* **Weights:** `α_s := Y'^{−1} W_1(q_s/Y') χ_s(b_*) (τ ξ(s))^{−1} (q_s/Y')^{−1/2+iv}`, so that
  `A_{m,σ,v}(Y') = Σ_s α_s K(s, m)`;
* **Twisted first moments:** `𝓑_s := Σ_m b_m K(s, m)`. For squarefree `s`,
  `K(s,m) = γ_1(s) conj χ_s(−m)`, so `𝓑_s = γ_1(s) Σ_m b_m conj χ_s(−m)`;
* **Diagonal:** `D := Σ_{s∈σ} W_1(q_s/Y') Σ_m |b_m|² |K(s, m)|²`.

**Identity.** `Σ_m b_m A_{m,σ,v}(Y') = Σ_s α_s 𝓑_s`. This is exact: both sums are finite.

**Lemma 0 (PROPOSED, elementary).**
(a) `|Σ_s α_s 𝓑_s|² ≪ Y'^{−1} Σ_s W_1(q_s/Y') |𝓑_s|²`.
(b) `D ≪ Z^ε Y' ‖b‖²`, where `‖b‖² = Σ_m |b_m|² ≤ Σ_{q_m ≪ Q} |B^J_{m,σ}|²`.

*Proof.*
(a) Use Cauchy–Schwarz with weight `W_1`, and note
`|α_s|²/W_1(q_s/Y') ≪ Y'^{−2} W_1(q_s/Y')`.
(b) `|K(s,m)|²` is multiplicative in `s`, by CRT and `χ_{s_1s_2} = χ_{s_1}χ_{s_2}`. Trivially
`|K(s,m)|² ≤ q_s`.
* For a prime `p ∤ m`, `|K(p,m)|² = 1`; for `p | m` it is 0.
* For `k ≥ 2`, `χ_{p^k} = χ_p^k` is periodic mod `p`. Its Gauss sum mod `p^k` vanishes unless
  `p^{k−1} | m`. In that case `|K(p^k, m)|² ≤ q_p^{k−1}`, or `≤ q_p^k` when `χ_p^k` is
  principal (a Ramanujan sum).
* Write `s = s_1 s_2`, with `s_1` squarefree and `s_2` powerful, coprime. Then
  `Σ_{q_s ≍ Y'} |K(s,m)|² ≤ Σ_{s_2} |K(s_2,m)|² · #{s_1 : q_{s_1} ≍ Y'/q_{s_2}} ≪ Y' Σ_{s_2} |K(s_2,m)|²/q_{s_2} ≤ Y' · #{s_2}`.
* Here `s_2` runs over powerful ideals with `p^{k_p−1} | m` for every `p^{k_p} ∥ s_2`. So
  `s_2 | m·rad(m)`, and `#{s_2} ≤ d(m·rad(m)) ≪ Z^ε`. ∎

B2_NUMERICS measures exactly `L = Σ_s |𝓑_s|²` against `D` (squarefree `s`, `ν = 1`, unmarked row).
It finds `L/D ∈ [0.83, 1.34]` at every rung.

## 2. The hypotheses, stated exactly

All hypotheses are required **uniformly** in `J`, `p_J`, `σ ∈ T`, the fixed ray family
`ν_σθ`, and `v ∈ R`, with at most polynomial growth `(1 + |v|)^{J_0}` in `v`. The integral
`∫|Ŵ_0(iv)|(1+|v|)^{J_0/2} dv` then converges, exactly as in (l. 8612–8613). "≪" allows `Z^ε` for
every `ε > 0`.

### 2.1 (H-dFDH): the de Faveri–Dunn–Hoffstein sextic large sieve

**What [dFDH] actually state** (verbatim content, arXiv source).

* For `n ∈ {3, 4}`, `K = Q(ζ_n)`, they define (eq. (1.3), shown for `n = 3`)

      Ξ_3(A,B) := sup_{β≠0} ‖β‖₂^{−2} Σ_{a ∈ Z[ζ_3], a ≡ 1 (3), N(a) ≤ A} μ²(a) | Σ_{b ∈ Z[ζ_3], b ≡ 1 (3), N(b) ≤ B} μ²(b) β_b (a/b)_3 |²,

  and `Ξ_4` analogously, with `a, b ≡ 1 (mod λ³)`, `λ = 1+i` (eq. (1.4)).
* The best known upper bound is (1.5): `Ξ_n(A,B) ≪_ε (AB)^ε (A + B + (AB)^{2/3})`. This is
  [BGL, Thm 1.3], and [HB, Thm 2] for `n = 3`.
* **Theorem 1.1.** `Ξ_3(A,B) ≫_ε (AB)^{−ε}(A + B + (AB)^{2/3})` for all `A, B ≥ 1`.
* **Theorem 1.2.** `Ξ_4(A,B) ≫_ε (AB)^{−ε}(A + B + A^{3/4}B^{1/2} + A^{1/2}B^{3/4})`.
* **Conjecture 1.3** (quartic only). `Ξ_4(A,B) ≪_ε (AB)^ε(A + B + A^{3/4}B^{1/2} + A^{1/2}B^{3/4})`.
* **Eq. (1.9)** (Sec. 1.2, "The general case"), stated in prose ("we expect"), not as a
  numbered conjecture. For the family of Hecke characters of fixed order `n ≥ 3` over
  `K ⊃ Q(ζ_n)`, "the analogous operator norm (considered in [BGL, Theorem 1.3])" should satisfy

      Ξ_n(A,B) = (AB)^{o(1)} (A + B + A^{1−1/n} B^{2/n} + A^{2/n} B^{1−1/n})   as min(A,B) → ∞.

  They add that the lower bound "should be within reach of current tools for all `n ≥ 5`", and
  that any power saving on the `(AB)^{2/3+ε}` term of (1.5) for `n ≥ 4` "would be a substantial
  advance".

**(H-dFDH)** is the upper-bound half of (1.9) with `n = 6`, `K = Q(ζ_6) = Q(ω)`:

    Ξ_6(A,B) ≪_ε (AB)^ε (A + B + A^{5/6} B^{1/3} + A^{1/3} B^{5/6}).

The squarefree variables lie in a fixed primary class, as in [BGL]; [dFDH] do not write out the
`n = 6` normalization. The **genuine extra terms** are `A^{5/6}B^{1/3} + A^{1/3}B^{5/6}`. They
replace the BGL term `(AB)^{2/3}`, and are smaller than it unless `A ≍ B`.

**(H-dFDH\*)** is the transport to the manuscript's normalization (PROPOSED reduction, not
carried out). For all complex `(c_s)` supported on `s ∈ σ`, `q_s ≍ Y'`:

    Σ_{q_m ≪ Q, (m,6)=1} | Σ_s c_s K(s,m) |² ≪ Z^ε (Q + Y' + Q^{5/6}Y'^{1/3} + Q^{1/3}Y'^{5/6}) Σ_s |c_s|²,

together with the dual inequality, which has the same constant. Getting there from squarefree
`a, b` needs the usual splitting of non-squarefree rows and moduli. For example, the
sixth-power rows `m = k⁶e` cost `≤ Q^{1/6}Y' ≤ Q^{5/6}Y'^{1/3}` (since `Y' ≤ Q`). The conclusion
in Sec. 3.1 does not depend on these details.

### 2.2 (H-biasA): the Gauss-sum bias removed from the Gram norm

    Σ_{q_m ≪ Q} |A_{m,σ,v}(Y')|² ≪ (1+|v|)^{J_0} (Q/Y') (1 + P_a²/Y').

This is Prop. 15.2's bound (8354) without the `P_a^{1/6}` term. It is a statement about the
**specific Gauss-sum vector** `α`.

[dFDH]'s proof of Thm 1.1 uses exactly this kind of vector as the extremal vector:
`β_b = conj(g̃_3(b)) H(N b/B)`. Its sum over `b` has a polar term
`𝒫_B(a) ∝ conj(g̃_3(a)) N(a)^{−1/6} B^{5/6}` (their eq. `polar_term_cubic`, Sec. 2), which produces the `(AB)^{2/3}`.
The sextic analogue is the residue of the sextic Kubota series. It gives `A_m` a main term
`∝ Y'^{−1/6}ρ_6(m)`, with `ρ_6` the sextic theta coefficients. Its mean square is
`(Q/Y')P_a^{1/6}` times a mean of `|ρ_6|²`.

(H-biasA) is therefore **expected false** (HEURISTIC), unless that mean square vanishes.
B2_NUMERICS §4 sees a small excess: Gauss-sum specific, +2–4 % at `P_a ≥ 20`, with z up to 17.
It is priced only to isolate the bias.

### 2.3 (H-LS): a bias-free sextic sieve for the theta row

    Σ_{s∈σ} W_1(q_s/Y') |𝓑_s|² ≪ (1+|v|)^{J_0} (Q + Y') ‖b‖².

This is the perfectly orthogonal ("sharp") large-sieve level for the **specific** row vector
`b`. If the lower half of (1.9) holds for `n = 6` (proved by [dFDH] only for `n = 3, 4`), the
inequality fails for some vectors when `P_a > 1`. Those vectors are the transposed extremals
`b ∝ A_m`, i.e. the polar direction `ρ_6(m) N(m)^{−1/6}`. So (H-LS) says exactly this: **the
ξ-twisted theta row is not aligned with the sextic-theta polar direction**.

Heuristically this is plausible; nothing links the two objects. Numerically it holds with a wide
margin: `L ≈ D ≪ λ_max ‖b‖²` (B2_NUMERICS §3).

### 2.4 (H-λ), 0 < λ < 1: a partial sub-diagonal saving

    Σ_{s∈σ} W_1(q_s/Y') |𝓑_s|² ≪ (1+|v|)^{J_0} Q^{1−λ} Y'^{λ} ‖b‖².

This interpolates geometrically between (H-LS) (λ = 0) and (H-diag) (λ = 1).

### 2.5 (H-diag): twisted first moments at their diagonal

    Σ_{s∈σ} W_1(q_s/Y') |𝓑_s|² ≪ (1+|v|)^{J_0} D   (≪ Z^ε Y' ‖b‖² by Lemma 0(b)).

In words: on average over the `≍ Y'` sextic twists, the first moments of the completed, marked,
ξ-twisted theta row behave as if the `b_m` were random.

This is exactly what B2_NUMERICS measures, finitely: `L/D = 0.83–1.34` in two geometries,
`Z ≤ 5·10⁵`, unmarked row, `ν = 1`, squarefree `s`. Random-phase controls behave the same.

(H-diag) also implies a **member-level** statement. By positivity, every single twist satisfies
`|𝓑_s| ≪ Z^ε (Y' ‖b‖²)^{1/2}`. That is a power saving `(Q/Y')^{1/2} = Z^{(lx−d)/2}` over the
trivial bound `Q^{1/2}‖b‖`, for every `s ≍ Y'` at once. This is the analogue of RUNG_STRENGTH
§2, Observation 2.

Why no main term should occur: if `χ̄_s χ_c` is principal (`c = s` in the theta sum), the
nonprincipal twist `ξ` (mod `2λ`, coprime to `sc`) still kills the `m`-sum. So the diagonal size
is the natural conjecture.

### 2.6 Row-blind and sub-diagonal (in the sense of RUNG_STRENGTH §3)

A bound is **row-blind** if it holds for *every* coefficient vector of the given shape.
RUNG_STRENGTH §3(a) shows that a row-blind bound `Σ_rows |Σ_cols c·kernel|² ≤ Δ‖c‖²` always has
`Δ ≥` (column length). The proof takes `c` aligned with one row.

Here the `s`-route has **rows `s` (`≍ Y'`)** and **columns `m` (`≍ Q`)**, with `Y' < Q` because
`lx > d`. The ratio is `ρ = log Y'/log Q = (ly − d)/(M − 2d)`. That is 23/40 (`d = 0`) to
5/8 (`d = ℓ`) at the paper geometry, and 1/2 at the H-diag optimum of Sec. 4.2 (`P_a = 1`).

| hypothesis | object | claimed `Δ` | row-blind? | sub-diagonal (`Δ` below the column length `Q`)? |
|---|---|---|---|---|
| (H-dFDH) | operator norm of the sextic kernel | `Q + Y' + QP_a^{1/6} + Q^{1/3}Y'^{5/6}` | **yes**, by definition | no (≥ `Q`; super-diagonal in the `m`-route) |
| (H-biasA) | Gram of the Gauss-sum vector `α` | `Q(1 + P_a²/Y')` (in `‖α‖²` units) | **no**, if the lower half of (1.9) holds; and it concerns the extremal vector itself | no |
| (H-LS) | `𝓑_s` of the theta-row vector `b` | `Q + Y'` | **no**, same reason, but only along the thin polar direction | no: exactly at the row-blind wall `Δ = Q` |
| (H-λ), 0<λ<1 | same | `Q^{1−λ}Y'^λ` | **no**, for every λ > 0 (RUNG §3(a)) | **yes** |
| (H-diag) | same | `Y'` | **no** | **yes**, fully (diagonal with ρ < 1) |

So a published *row-blind* conjecture can only give ϑ ≤ 0 here (Sec. 3.1). Any saving needs
coefficient-specific input. Any saving beyond `b/12` needs a sub-diagonal statement of the kind
that RUNG_STRENGTH §4 shows contains member-level power savings.

## 3. The saving each hypothesis gives in the low estimate (PROPOSED derivation)

Fix `J`, the tuple, `σ` and `v`. Prop. 15.4's chain (l. 8612–8624) is
`|I_tuple| ≤ Q^{−1/2} ‖A‖ ‖b‖`. It gives the tuple exponent

    CS:  [−(ly − d) + G(d) + E_B(M', ℓ')]/2,    G(d) = max(0, b/6, 2b − ly + d),

where `‖b‖² ≤ Z^{E_B(M',ℓ')}` by Lemma 15.1, in the general form of THRESHOLD_CALCULUS §2. The
tuple count `Z^d` and coefficient `Z^{−3d/2}` (l. 8626–8631) add `−d/2`. The boundary is
`σ_low = 1 − lx/2 − h/6 + max_{d∈[0,ℓ]}[·]`. The bracket is convex in `d`, so the endpoints
`d ∈ {0, ℓ}` suffice.

Under (H-λ), the identity of Sec. 1 and Lemma 0(a) give instead

    |I_tuple| ≪ Q^{−1/2} · Y'^{−1/2} · (Q^{1−λ}Y'^λ)^{1/2} ‖b‖   ⇒   [−(ly − d) − λ(lx − d) + E_B(M',ℓ')]/2,

using `M' − (ly − d) = lx − d`. The saving over CS at depth `d` is therefore

    ϑ_λ(d) = G(d)/2 + λ (lx − d)/2.

### 3.1 (H-dFDH): ϑ = 0

There are two routes, and both give the same result.

1. **The `m`-route.** Apply (H-dFDH\*) to `A`. This gives
   `‖A‖² ≪ Y'^{−1}·Ξ_6(Q,Y') = (Q/Y')(1 + Y'/Q + P_a^{1/6} + Y'^{5/6}Q^{−2/3})`, because
   `Σ|α_s|² ≍ Y'^{−1}`.
   * `Q^{5/6}Y'^{1/3}/Q = P_a^{1/6}`: the genuine extra term **is** the manuscript's Gram excess.
   * `Y'^{5/6}Q^{−2/3} ≤ P_a^{1/6}` iff `Y' ≤ Q`.
   * So `G_dFDH = max(0, b/6)`.
2. **The `s`-route.** Apply (H-dFDH\*) to `b` and use Lemma 0(a). This gives the same
   `Y'^{−1}Ξ_6(Q, Y')‖b‖²`, which is identical to Cauchy–Schwarz with the `m`-route Gram bound.

Hence `ϑ_dFDH(d) = [G(d) − max(0, b/6)]/2 = ½ (2b − ly + d − max(0, b/6))₊`. This vanishes
whenever `11b/6 ≤ ly − d`. The manuscript imposes exactly that, with margin 1/12 (l. 8597).

The conjecture's `n = 3` case does not help the theta side either: the cubic large sieve used
in Lemma 14.4 is already optimal by [dFDH] Thm 1.1, a theorem.

### 3.2 Values at the manuscript geometry (17/48, 23/48, 1/6), where `E_B = M'` for all `d`

| hypothesis | `ϑ(0)` | `ϑ(ℓ)` | `σ_low` (exact) |
|---|---|---|---|
| CS, (H-dFDH) | 0 | 0 | 7/8 |
| (H-biasA), (H-LS) | 1/96 | 1/96 | 83/96 = 0.864583 |
| (H-λ) | `(1 + 17λ)/96` | `(1 + 9λ)/96` | `83/96 − 17λ/96` |
| (H-diag) | 18/96 = 3/16 | 10/96 | **11/16 = 0.6875** |

The saving is **not uniform in `d`**: it is largest on the unrescaled subset. So the uniform
B2(ϑ) model of BILINEAR_B2 §4 does not apply directly. The model below uses the exact `d`-dependence.

At the paper geometry the low side is no longer binding under (H-diag). The floor bin
(`7/8 − 7/1200`) and the witnessed bins (`H = 0.87477`) are. The geometry must move (Sec. 4).

## 4. Pricing in the manuscript's model

`σ_H = inf_geom max(σ_low^H, all high-side constraints)`, i.e. the minimum over geometries of
the binding constraint.

* **Exact LP layer (any row counts).** The high side is reduced to the floor bin, which is
  linear (FLOOR_BIN_BARRIER §1.2), plus the validity rows `ℓ ≤ lx ≤ ly`, `ℓ ≥ 0`. The LP uses
  every low-side piece (both `d` endpoints, all Gram and energy branches). It is therefore the
  exact infimum of `max(σ_low^H, floor)`, not a relaxation. Each value has a rational dual
  certificate, and also an exact primal vertex checked feasible against every row in Fractions.
* **Paper-count layer (FLOATING).** This is `bilinear_b2.H_high`: the Prop. 19.2 row counts,
  `κ = max(2β*−1, 3/4)`, the small-row condition and `σ ≤ 7/8`, with `tc.valid_geometry`
  (`ly ≥ lx`, `lx − ℓ > 0.01`, `ly − ℓ > 0.01`). Nelder–Mead is started from the grid-scan and
  LP points, and the result is re-verified on the fine grid (241 × 26 × 19).

### 4.1 Results

Paper-count model values (FLOATING, Nelder–Mead plus fine-grid re-verification). Taken from the
run log `scratchpad/conditional_b2.log`. The agent was cut off by an API rate limit before it
wrote `results/conditional_b2.json`. Cells marked "not run" were not reached; the coordinator
filled in this table from the log.

| hypothesis | `a0 = 51/100` | `a0 → 1/2⁺` (`1/2 + 1/2000`) | optimum geometry `(lx, ly, ℓ)` |
|---|---|---|---|
| CS (manuscript) | 0.874974 | 0.874974 | (0.358, 0.475, 0.167) |
| (H-dFDH) | 0.874974 | 0.874974 | same as CS |
| (H-biasA) | 0.859796 | not run | (0.290, 0.579, 0.131) |
| (H-LS) | 0.836667 † | not run | (0.02, 0.98, 0), degenerate corner |
| (H-λ), λ = 1/2 | 0.781933 | 0.781926 | (0.461, 0.461, 0.078) |
| (H-diag) | 0.683611 | 0.683772 | (0.500, 0.534, ≈ 0) |

The (H-diag) model values sit slightly *below* the slot-free closed form 0.686141. The optimizer
uses a tiny `ℓ ≈ 10⁻⁴` and `ly ≠ lx`, and the grid reads slightly low (§4.2). Treat 0.6836–0.6861
as the model range.

**(H-dFDH) equals CS everywhere it could matter (exact).** The two low sides differ only where
`11b/6 > ly − ℓ`. On that region an exact LP gives:
* `min max(σ_low^{dFDH}, floor) = 2297/2622 = 0.876049` at `a0 = 51/100`, above the CS value
  0.874974;
* `89/102 = 0.872549` at `a0 → 1/2`. There the paper-count high side is above 7/8: the κ-lock
  fails, with `σ = 0.886` at the LP vertex `(11/34, 1/2, 3/17)`. Nelder–Mead from that vertex
  returns to the standard optimum 0.874967.

So (H-dFDH) changes no model value.

### 4.2 (H-diag) in closed form (ℓ = 0)

With no slots every dyad has `R = 1 − 2δ/3`. The worst dyad is `d = h`, because the slope
`0.66 − δ/6` is positive. There `g(δ) = a(1 − ly) + h(5/6 − δ/6)` with `h = 1 − lx`, and `g`
increases in `δ`. The closure set `{g ≥ a}` is therefore an initial segment, and

    H = a* = 3h/(3ly + h)     (the bin whose g crosses a).

Checked against `H_high`: 0.747944 / 0.749639 / 0.749978 at nde = 41 / 241 / 2001, against
`a* = 3/4` at (1/2, 1/2, 0). The grid always reads slightly low.

Under (H-diag) the low side on the branch `M ≥ 1` is `1/3 + lx/6 + ly/2`. Minimizing
`max(1/3 + lx/6 + ly/2, 3(1−lx)/(3ly + 1 − lx))` gives `lx = ly = L` with
`(1+2L)² = 9(1−L)`, i.e. `4L² + 13L − 8 = 0`. Hence

    L = (3√33 − 13)/8 ≈ 0.529211,   σ = (1 + 2L)/3 = (√33 − 3)/4 ≈ 0.686141.

At this point the floor bin is `0.6371` (`a0 = 51/100`), so it does not bind, and the value is
the same for both floors. `P_a = 1` and `M = 2L ≈ 1.058 > 1`: the dual-length branch of
`E_B` is active. With slots allowed, the floating model gives 0.6836 (`a0 = 51/100`) and 0.6838 (`a0 → 1/2⁺`), consistent with the closed form up to grid and optimizer error.

### 4.3 Floor dependence (both floors, as requested)

The floor-lowered column rests on **reviews/SEP30_DETECTOR_QUANTIFIERS.md §4**, a bounded review,
not a certification. It finds that every floor-dependent inequality of [OAI] Sec. 8, of
Lemma 7.1 region one and of Prop. 16.1 holds verbatim for any fixed `a0 = 1/2 + η`, `η > 0`.
Without that finding only the `51/100` columns are justified by the manuscript as written.

| hypothesis | LP `51/100` | LP `1/2⁺` | difference |
|---|---|---|---|
| CS, (H-dFDH) | 167/192 | 13/15 | 1/320 |
| (H-biasA) | 926/1077 | 6/7 | 20/7539 |
| (H-LS) | 251/300 | 5/6 | 1/300 |
| (H-λ) λ = 1/4 / 1/2 / 3/4 | 1208/1461 / 60/77 / 952/1311 | 47/57 / 7/9 / 37/51 | 2.3e-3 / 1/693 / 6.7e-4 |
| (H-diag) | 203/303 | 2/3 | 1/303 |

In the paper-count model the floor never binds at the optima found (Sec. 4.1). For CS this was
already known (FLOOR_BIN_BARRIER §2.1).

## 5. The conditional statements

Each statement assumes all of [OAI]'s stated lemma outputs. Those lemmas are unreviewed, apart
from the bounded reviews listed in reviews/SEP30_VERIFICATION_MAP.md. Each statement also assumes
the lemma-range extrapolations of Sec. 7, whenever the geometry is not the manuscript's.

1. **(H-dFDH), a published conjecture (the upper half of [dFDH] (1.9), n = 6, transported as
   (H-dFDH\*)).** Conditional on the unreviewed manuscript's other lemmas and on (H-dFDH), ζ has
   no zeros in `Re s > σ_dFDH` with **σ_dFDH = 7/8**. That is no improvement: the conjecture's
   extra term is the manuscript's own Gram excess. With PR 910's re-optimized geometry the
   value is `(1507 − 2√921)/1653 ≈ 0.874957` with or without (H-dFDH). **There is no conditional
   boundary below 7/8 attributable to (H-dFDH).**
2. **(H-biasA) or (H-LS) (Gauss-sum bias only).** Conditional on the manuscript's other lemmas and
   on (H-LS), ζ has no zeros in `Re s > σ_LS` with **σ_LS ≈ 0.8367** (FLOATING,
   paper counts). The exact barrier for any row counts is `251/300` (`a0 = 51/100`), reached
   only at a degenerate corner. Under (H-biasA), which is expected false: **σ ≈ 0.8598**.
3. **(H-diag).** Conditional on the manuscript's other lemmas and on (H-diag), ζ has no zeros in
   `Re s > σ_diag` with **σ_diag = (√33 − 3)/4 ≈ 0.686141** (paper counts, slot-free geometry
   `lx = ly = (3√33 − 13)/8`, ℓ = 0, both floors; model 0.6836–0.6861). Whatever the row counts, the
   architecture cannot go below **203/303 ≈ 0.669967** at `a0 = 51/100`, or **2/3** at
   `a0 → 1/2⁺`. The latter needs reviews/SEP30_DETECTOR_QUANTIFIERS.md §4.
4. **(H-λ).** With `a0 → 1/2⁺` the barrier is `min((13 − 5λ)/(15 − 3λ), 5/6†)`.
   * For every λ, the point `lx = ly = 2/(5 − λ)`, `ℓ = (1 − λ)/(5 − λ)` makes the low side and
     the floor row both equal to `(13 − 5λ)/(15 − 3λ)` (checked symbolically). At that point
     `M + ℓ = 1` and `E_B = M`.
   * The LP certifies this value optimal at λ = 1/4, 1/2, 3/4 and 1 (47/57, 7/9, 37/51, 2/3).
     For other λ it is only an upper bound for the LP value.
   * It drops below the 5/6 family floor only for `λ > 1/5`. Paper counts at λ = 1/2:
   **σ ≈ 0.7819**.

## 6. Sanity checks against 167/192, 13/15 and the floor

* **Reproduction.** The full CS LP gives 167/192 and 13/15, the same as `barrier_lp.py`'s
  relaxation (it uses only `d = 0` and `G ≥ b/6`). So that relaxation was tight. The relaxed LP
  with a uniform shift reproduces `bilinear_b2.lp_barrier`: 322/375 = `13/15 − 4ϑ/5` at
  ϑ = 1/100 with `a0 = 1/2`, and 6371/7680 at ϑ = 1/20 with `a0 = 51/100`.
* **Uniform-ϑ equivalent.** Inverting `13/15 − 4ϑ/5` gives `ϑ_eff`: 1/4 for (H-diag), the
  THRESHOLD_CALCULUS §5 value whose barrier is the Part I signal offset 2/3; 1/9 for (H-λ = 1/2);
  1/24 for (H-LS); 1/84 for (H-biasA).
* **Floors.** Every hypothesis respects the floor-bin structure. The LP value is always attained
  with the floor row tight (`floor_tight = True` in the output).
* **5/6 family floor.** A sieve-level low bound has `E_B ≥ M'` and `θ_low ≥ lx/2`, hence
  `σ ≥ 1 − h/6 ≥ 5/6`. Only the sub-diagonal hypotheses go below 5/6. That is consistent with
  BRIDGE_MELLIN: the "floor is intrinsic" for CS/large-sieve bounds, not for the true size.
* **Consistency with the signal.** Under (H-diag) at the optimum, `|I| ≪ Z^ε`. The signal of a
  zero at `β*` is `Z^{C(β*)}` with `C(β*) = β* − 1 + lx/2 + h/6`, so a zero would need
  `β* ≤ 1 − lx/2 − h/6`. This is consistent with RH-true zeros on the line, since
  `C(1/2) = lx/2 + h/6 − 1/2 < 0` there.
* **Ordering.** For every hypothesis, the paper-count value is at least its LP barrier, which is
  at least the low-alone barrier. Low-alone barriers: CS 13/15, (H-dFDH) 13/15, (H-biasA) 38/45,
  (H-LS) 5/6, (H-λ) 97/120, 23/30, 43/60, (H-diag) 2/3.

## 7. Lemma-range obligations (inherited, and much larger here)

These extend THRESHOLD_CALCULUS §7 and BILINEAR_B2 §4. At `σ ≈ 0.69` and geometry
`(0.529, 0.529, 0)` they are:

1. **Contour lemmas.** Lemmas 10.3–10.6 are stated for `σ0 ∈ [7/8, 1)`.
   reviews/CONTOUR_LEMMAS_BELOW_7_8.md transfers them only to `139999/160000`, with modified
   domains `D2'`. Nothing is checked near 0.69.
2. **Euler region.** The Euler region (7.15) converges normally only for `Re x > 2/3 + η`. The
   (H-diag) barrier 2/3 sits exactly at this edge, and the model value is 0.019 above it.
3. **Lemma 18.1** is used at `κ = 3/4` when the true `2β* − 1` is about 0.37. This is
   conservative in direction, but outside the stated range.
4. **Lemma 15.1** assumes `M + ℓ = 1`. The optimum has `M ≈ 1.058`, so the closed form `E_B`
   with its dual-length branch is used. That is the LP supremum of (14.14), not the
   manuscript's proof.
5. **Prop. 19.2** assumes prime supply `> 7/37`. At `ℓ = 0` there are no slots, and the counts
   fall back to `R = 1 − 2δ/3`. The model is supply-capped.
6. **(H-diag)** itself must cover the marked rows `B^J`, every `ν_σθ`, non-squarefree `s` and all
   `v`. B2_NUMERICS tested only the unmarked `ν = 1` row with squarefree `s`.

## 8. What this note does not show

* No hypothesis is proved, and none is shown to be consistent with the manuscript beyond the
  bookkeeping above.
* (H-dFDH\*) is a stated, unperformed transport of (1.9). (1.9) itself is a prose expectation;
  [dFDH]'s numbered Conjecture 1.3 is quartic.
* The expected falsity of (H-biasA) is HEURISTIC. It rests on the sextic Kubota residue and
  [dFDH]'s cubic mechanism, not on a computation for `n = 6`.
* The paper-count values are FLOATING: grid suprema read low by up to about 3·10⁻³ on the coarse
  grid and 4·10⁻⁴ on the fine grid near a crossing (Sec. 4.2). Only the LP values and the
  closed form `(√33−3)/4` are exact, and the latter only within the slot-free family.
* Lowering the floor uses a bounded review's finding, not a certified one.

## 9. Files

| file | content |
|---|---|
| `scripts/conditional_b2.py` | hypotheses, exact low sides, exact LPs (dual + primal certificates), paper-count optimisation; imports threshold_calculus, barrier_lp, bilinear_b2 unchanged |
| `results/conditional_b2.json` | LP and model output |

Reproduce: `python3 scripts/conditional_b2.py --quick` (self-tests and LPs, about 3 s), or
`python3 scripts/conditional_b2.py --json results/conditional_b2.json` (adds the paper-count
model; tens of minutes on a loaded 4-core machine).

# O4: amplification instead of shortening, for the sextic Möbius family

```text
Status: PROPOSED (exploration, offense wave). Labels per claim below:
  PROVED-HERE: Lemma A1 (amplified extraction), Lemma A2 (amplifier-blind bounds have kappa >= 1),
    Lemma A4 (row orthogonality of the amplifier and the large-value reduction), the trivial
    break-even statements of designs (a3) and (d). Elementary; written out here; not reviewed.
  PROPOSED: Lemma A3 (the amplified Poisson dual is the Oct 5 dual family E(H, X, F) with f = l
    placed inside the square), the twist-exponent table (section 2.3), the design analysis (section 3).
  CONDITIONAL: kappa = 1 for the Oct 5 pipeline (rests on the Oct 5 imports lem:poisson,
    eq:convert2, eq:crt-a, Prop. canonical; external, unreviewed).
  EMPIRICAL: section 5 (floating point, finite).  OPEN: the hypotheses TM(eta, s) of section 4.
  RH is unsolved; no zero-free region is proved here; 11/12 and 7/8 are unreviewed external claims.
Scope: amplified mean squares sum_{N u <= H} |Amp_u|^2 |A_u(D)|^2 with row twists
  Amp_u = sum_{N l <= L} x_l chi_l(u) for the Oct 5 family A_u(D) = sum mu(n) chi_n(u) W(N n/D)
  over Z[omega]. Exponents in base D: H = D^h, L = D^lam. Question: can amplification move the
  extraction exponent below 11/12, conditional only on the Oct 5 imports?
Exact sources or dependencies: Oct 5 manuscript paper2.tex (scratchpad copy, 3988 lines; read
  lines 52-660, 875-1010, 1255-1345): Steps 2-5, lem:poisson, eq:energy, lem:remove-exclusions
  (uses eq:crt-a), prop:canonical, prop:R. Repository: RUNG_STRENGTH.md (leverage law, Prop. R'),
  LEVERAGE_FAMILIES.md (sections 1, 2.3), DISPERSION_GRH_STEP.md (section 4), Q_RHO_ANALYSIS.md
  (sections 2.1-2.3), moments/{common.py, eisenstein.py, sextic_kernel.c} (read and imported unchanged).
What was actually run (single thread each, shared 4-core machine):
  python3 -I amp_ledger.py                       (sympy exact; all asserts pass; < 2 s)
  python3 -I amp_moments.py results/amp_main.json --D 1000 2000 4000 8000 \
      --L 13 31 61 127 251 499 --Hfac 0.25 1 4    (D = 1000, 2000, 4000 completed in 32 s, 68 s,
      294 s; stopped during D = 8000 to respect the 20-minute rule)
  python3 -I amp_moments.py results/amp_D8000.json --D 8000 --L 31 127 499 --Hfac 0.25 1
  python3 -I make_tables.py > results/tables.md ;  python3 -I collision_rms.py > results/collision_rms.out
  python3 -I tm_twisted.py results/tm_theta01.json --D 1000 2000 4000 8000 16000 32000 --theta 0.1 --Lmax 211
  python3 -I tm_twisted.py results/tm_theta05.json --D 1000 2000 4000 8000 --theta 0.5 --Lmax 211
  Script sha256 prefixes: amp_moments.py 22fbf1503a14, tm_twisted.py 9a91dcae62d9,
  amp_ledger.py dda2d4e59f89, make_tables.py 89742e6e85ee, collision_rms.py 4d37970171d8
Smallest remaining gap: TM(eta, s) of section 4: a power saving N(r)^(-eta) in the row-twisted
  mean square T^off(r) = sum_{N u <= D L^s} chi_r(u) |A_u(D)|^2 (minus its explicit collision term),
  for twists of conductor N(r) <= L^2. Amplification beats 11/12 iff eta > 5s/12; the exponent is
  sigma = 11/12 + lam (5s/12 - eta) (section 4, exact). At s = 1 (enough rows for the
  Oct 5 toolbox) this needs eta > 5/12; at s < 1 it is a sub-diagonal statement (the rho = 1 wall).
```

## 0. Verdict

1. **The coordinator's count is correct (PROVED-HERE, Lemma A1 + ledger).** Suppose
   `M_amp ≪ D^ε H D L^{1+κ}` with `H = D L^{1+δ}`. Then the principal member satisfies

       |A_1(D)| ≪ D^{11/12 + λ(κ + 5δ/6 − 1/6)/2 + ε}   (plus the extraction-error floor D^{1 − h/6}).

   Amplification gains iff `κ + 5δ/6 < 1/6`. The break-even values are exact: `κ* = 1/6` at
   `δ = 0`, and `δ* = 1/5` at `κ = 0`.
2. **The coordinator's suspicion is correct, and in sharp form (CONDITIONAL on the Oct 5 imports).**
   Take a Möbius-compatible prime amplifier (`x_ℓ = 1` on primes).
   * After Poisson and absorption, the amplified dual row is exactly a combination
     `Σ_ℓ (unimodular)·χ_ℓ(k)·C(D; k, ℓ)` of the Oct 5 dual column sums at twist `f = ℓ`, i.e. the
     family `E(𝓗, X, F)` of eq:energy, but with `f` *inside* the square (Lemma A3).
   * Cauchy–Schwarz over `ℓ`, followed by the imported Prop. canonical, gives `M_amp ≪ D^ε H D L²`,
     valid for `H ≥ D^{1+κ'} L`. So **κ = 1**.
   * The ledger shows this pipeline is an *exact* break-even in rows: σ = `1/2 + 5h/12`, whatever
     `λ` is. Its whole loss is the forced row growth `h ≥ 1 + λ`, which gives σ = `11/12 + 5λ/12`.
     So the optimum is `λ = 0`. This makes LEVERAGE_FAMILIES §2.3 ("costs exactly what it gains")
     precise.
   * Expanding the square instead of using Cauchy–Schwarz locates the loss exactly. The `ℓ = ℓ'`
     terms are κ = 0 by Prop. canonical. The whole gap is in the row-twisted dual correlations
     `X(ℓ, ℓ')`, which need a saving `N(ℓℓ')^{−η}` with η > 5/12 (§2.1).
   * After Poisson in `k`, those cross terms are the original amplified off-diagonal. This is the
     Q_RHO involution again, so keeping them gives no reduction.
3. **No design examined reaches κ < 1/6 on the Oct 5 imports alone** (section 3). The structural
   reason is the twist-exponent table (§2.3, PROPOSED, exact arithmetic mod 6). For every
   Kummer-type amplifier character `χ_ℓ^e`, the CRT/reciprocity factor of the Poisson Gauss sum
   puts a twist of conductor `ℓ` (e ∈ {1, 5}) or `ℓℓ'` (e ∈ {2, 3, 4}) on the column variable that the
   theta reflection acts on. This factor does not depend on the amplifier coefficients, so Gauss-sum or
   theta-shaped coefficients cannot remove it.
4. **Best constructive output: a new, sharper smallest statement (OPEN), with exponents.**
   Amplification is governed by the row-twisted mean squares
   `T(r) = Σ_{N u ≤ H} χ_r(u)|A_u(D)|²`, with `N(r) ≤ L²` (§4).
   * With `H = D L^s`, a power saving `N(r)^{−η}` on the off-diagonal part gives
     **σ = 11/12 + λ(5s/6 − 2η)/2**, so amplification gains iff `η > 5s/12`.
   * At `s = 1` (no row deficit: the regime the Oct 5 toolbox can enter) this needs `η > 5/12`.
     That is close to square-root cancellation in the twist conductor (η = 1/2). GRH-random
     behaviour gives η up to `h/(4λ)`, which exceeds 5/12 at `s = 1` exactly when `λ < 3/2`.
   * At `s → 0` any `η > 0` suffices, giving σ = `11/12 − λη`. But then the amplified polynomial has
     `D^λ` more columns than rows, which is the ρ = 1 wall again.
   * Lemma A4 (PROVED-HERE) shows that the bounded part of `|A_u|²` is orthogonal to the amplifier,
     up to `O(H^{−A})`, when `L² ≤ H^{1−ε}`. Everything therefore sits in the large values, and the large-value
     mass already contains the conclusion through the principal rows (a fixed point, as in
     RUNG_STRENGTH §4).
5. **Numerics (EMPIRICAL, floating point, finite).** For the true sextic family the amplified moment
   is diagonal-sized:
   * `M_amp/Diag_b ∈ [0.972, 1.024]` over `D ≤ 8000`, `L ≤ 499` (up to 93 prime twists; `D = 8000` on a reduced grid), and
     `H/(DL) ∈ {1/4, 1, 4}`. This includes `H < DL`, where the amplified polynomial is sub-diagonal.
   * Empirical `|κ| ≤ 0.01`.
   * The principal-row enrichment grows like `L` (the number of primes), as the leverage count predicts.

So amplification is *true* (κ ≈ 0 empirically), but it is *unprovable with these tools*. Its exact price
is the twisted-moment statement TM(η, s).

## 1. Amplified extraction (PROVED-HERE)

Notation follows RUNG_STRENGTH §1: `ν = 1_{(n,6)=1}`, `W` a smooth bump on `[1, 2]`, and rows over
all nonzero `u ∈ Z[ω]`. Let `x_ℓ` be supported on prime ideals `ℓ ∤ 6` with `N ℓ ≤ L`, and put

    Amp_u = Σ_ℓ x_ℓ χ_ℓ(u),   M_amp(H) = Σ_{0 < N u ≤ H} |Amp_u|² |A_u(D)|².

Since `χ_ℓ(u) = ψ_u(ℓ)`, the amplifier is the Hecke value of the member `ψ_u` at `ℓ`. It is the exact
analogue of a GL(2) amplifier `Σ x_ℓ λ_f(ℓ)`.

**Lemma A1.** Let `Y = H^{1/6} ≥ 2`, and let `𝒫` be the primary primes `p ∤ 6` with `Y/2 < N p ≤ Y`. Then

    |A_1(D)|² ≤ 2 M_amp(H) / Σ_{p ∈ 𝒫} |Σ_{ℓ ≠ (p)} x_ℓ|²  +  2 max_{p ∈ 𝒫} |A_{p⁶}(D) − A_1(D)|²,

and `|A_{p⁶}(D) − A_1(D)| ≪_W D/Y`. For `x_ℓ = 1` on all such primes,

    |A_1(D)|² ≪ M_amp(H) · (log Y) / (Y · π_K(L)²) + D² H^{−1/3}.

*Proof.*
* The rows `p⁶`, `p ∈ 𝒫`, are distinct, have norm `≤ H`, and satisfy `χ_ℓ(p⁶) = χ_ℓ(p)⁶ = 1_{ℓ ≠ (p)}`.
  Hence `Amp_{p⁶} = Σ_{ℓ≠(p)} x_ℓ`.
* Since `χ_n(p⁶) = 1_{p ∤ n}`, we have `A_{p⁶} − A_1 = −Σ_{p | n} μ(n)ν(n)W(N n/D)`. This has
  `≪ D/N p` terms of size `≤ ‖W‖_∞`.
* By positivity, `M_amp ≥ Σ_{p∈𝒫} |Amp_{p⁶}|² |A_{p⁶}|²`. Also `|A_1|² ≤ 2|A_{p⁶}|² + 2|A_{p⁶} − A_1|²`.
  Multiply by `|Amp_{p⁶}|²`, sum over `p`, and divide by `Σ_p |Amp_{p⁶}|²`.
* For `x ≡ 1`, `|Amp_{p⁶}| ≥ π_K(L) − 1`, and `#𝒫 ≫ Y / log Y` (Landau). ∎

**Corollary (exponents; ledger items H0 and TM).** Write `M_amp ≪ D^{e+ε}`. Then
`σ = (e − h/6 − 2λ)/2`. For the record:
* No amplifier, with the imported Oct 5 mean square (`e = 1 + h`): σ = `1/2 + 5h/12 → 11/12`.
* Diagonal size times `L^κ`, at `h = 1 + (1+δ)λ`: σ = `11/12 + λ(κ + 5δ/6 − 1/6)/2`.
* The floor `1 − h/6` comes from the second term of Lemma A1. RUNG_STRENGTH Prop. R′ step 5 (the
  PR 910 dyadic induction, not re-derived here) is the expected way to remove it. It does not bind
  near σ = 11/12.

As in RUNG_STRENGTH Prop. R, the zero-free conclusion would need the bound for every smooth `W`.
Nothing here supplies that.

## 2. What the Oct 5 pipeline does with an amplifier

### 2.1 The amplified dual (Lemma A3, PROPOSED; exact algebra modulo the imported identities)

Take `x_ℓ = 1` on primes. Then `Amp_u A_u = Σ_m b_m χ_m(u)` with `b = x * (μνW_D)`.
* On squarefree `m`, `b_m = −μ(m) Σ_{ℓ | m, Nℓ ≤ L} W(N(m/ℓ)/D)`. This is **Möbius-compatible**
  (`μ(ℓ) = −1` is constant on primes).
* On `m = ℓ²k` it is the extra term `−μ(k)`. Its character is `χ_ℓ(u)² χ_k(u)`; this block is not
  treated here.

Run lem:poisson (modulus `m₁m₂`) and then the absorption eq:convert2 on the squarefree block. The
Gauss sum of `χ_{ℓn}` factors by CRT, and eq:crt-a (as used in lem:remove-exclusions) gives
`a_ξ(ℓn) = a_ξ(ℓ) a_ξ(n) χ_n(ℓ)⁴`. So the dual row is

    B^b_k = −Σ_{ℓ ≤ L} a_ξ(ℓ) χ_ℓ(k) · C(D; k, ℓ),    C(X; k, f) = Σ*_n a_ξ(n) χ_n(k) χ_n(f)⁴ W(N n/X),

where `C` is **exactly** the column sum of the manuscript's eq:energy with `f = ℓ`. The dual length is
`𝓗 = (DL)²/H`. The amplifier has turned into a *row combination of the dual family at the rows
`kℓ⁴`*, with unimodular coefficients that depend on `k` through `χ_ℓ(k)`.

**Consequence (CONDITIONAL; ledger "Design (a)").** Apply Cauchy–Schwarz in `ℓ`, then Prop. canonical
with `X = D` and `F ≍ L`. Its hypothesis `𝓗 ≤ XF·D^{−κ'}` means `H ≥ D^{1+κ'}L`. This gives

    Σ_k |B^b_k|² ≤ π(L) Σ_ℓ Σ_k |C(D;k,ℓ)|² ≪ D^ε L·(DL)²,
    M_amp ≪ D^ε (H·DL + (H/DL)·L³D²) = D^ε H D L².

So `κ = 1` and σ = `1/2 + 5h/12` with `h ≥ 1 + λ`, hence σ ≥ `11/12 + 5λ/12`.

*Where exactly the loss sits.* Expand the square in `ℓ`:
`Σ_k |B^b_k|² = Σ_ℓ Σ_k |C(D;k,ℓ)|² + Σ_{ℓ ≠ ℓ'} X(ℓ, ℓ')`, where

    X(ℓ, ℓ') = a_ξ(ℓ) conj(a_ξ(ℓ')) Σ_{N k ≤ 𝓗} χ_ℓ χ̄_{ℓ'}(k) C(D;k,ℓ) conj C(D;k,ℓ').

* The `ℓ = ℓ'` part is `≪ D^ε (DL)²` by Prop. canonical (CONDITIONAL). It contributes `H·DL`
  to `M_amp`, i.e. **κ = 0**.
* The whole loss is therefore in the cross-correlations `X(ℓ, ℓ')`. These are dual mean squares
  twisted on the row by `χ_ℓχ̄_{ℓ'}`, of conductor `N(ℓℓ') ≍ L²`. Their trivial (Cauchy–Schwarz) size is
  `(Σ_k|C_ℓ|² Σ_k|C_{ℓ'}|²)^{1/2} ≍ D²L`. κ < 1/6 needs an average saving `N(ℓℓ')^{−η}` with
  **η > 5/12** (the dual form of TM(η, 1) in §4).
* Poisson in `k` sends `X(ℓ, ℓ')` back to the original twisted moment `T(ℓℓ'^5)`. This is the Q_RHO
  involution, so the dual form is a rewriting, not a reduction.

The variant without the transfer recursion fares no better. It uses Prop. R plus the quadratic large
sieve for each `(k, ℓ)` and gives `M_amp ≪ HDL + D²L³ + D³L⁶/H`. Its best value on the ledger grid is
σ = 233/240 > 11/12 (`h = 5/4`, `λ = 1/10`).

### 2.2 Amplifier-blind final steps cost κ ≥ 1 (Lemma A2, PROVED-HERE)

For any arrays `C_ℓ(k)`,

    sup_{|c_ℓ(k)| = 1} Σ_k |Σ_ℓ c_ℓ(k) C_ℓ(k)|² = Σ_k (Σ_ℓ |C_ℓ(k)|)²,

because the phases can be aligned row by row. When the `|C_ℓ(k)|` are of comparable size in `ℓ`,
this is `≍ π(L)·Σ_k Σ_ℓ |C_ℓ(k)|²`, which is Cauchy–Schwarz with equality. Consider any final step
that bounds the amplified dual uniformly over unimodular coefficients `c_ℓ(k)`, i.e. that does not use
the fact that `c_ℓ(k) = a_ξ(ℓ)χ_ℓ(k)` is a *character of the row*. Such a step has κ ≥ 1 in the flat
case. This is the amplifier analogue of RUNG_STRENGTH §3(a).

A large sieve that *does* see `χ_ℓ(k)` treats `(ℓ, n)` jointly, i.e. the column `m = ℓn` of length
`DL` with weight `g(m)`. Its theta step then needs `g` to be smooth, which it is not (§3, design (a3)).

### 2.3 Twist-exponent table (PROPOSED; exact mod 6; ledger item 7)

Take an amplifier character `χ_ℓ(u)^e` and a column character `χ_n(u)`. The CRT factor of the Poisson
Gauss sum, combined with sextic reciprocity (up to ray-class factors), twists the dual `n`-sum by
`χ_n(ℓ)^{1+e}`. In the off-diagonal pairing it also twists it by the partner's `χ_n(ℓ')^{1−e}`.

| e | own twist on n | order | partner twist | order | conductor seen by the reflection |
|---|---|---|---|---|---|
| 1 | χ_n(ℓ)² | 3 | none | 1 | ℓ (the eq:energy `f`-twist) |
| 2 | χ_n(ℓ)³ | 2 | χ_n(ℓ')⁵ | 6 | ℓℓ' |
| 3 | χ_n(ℓ)⁴ | 3 | χ_n(ℓ')⁴ | 3 | ℓℓ' |
| 4 | χ_n(ℓ)⁵ | 6 | χ_n(ℓ')³ | 2 | ℓℓ' |
| 5 | none | 1 | χ_n(ℓ')² | 3 | ℓ' (same as e = 1 after regrouping) |

Both twists vanish only if `e ≡ −1` and `e ≡ 1 (mod 6)`, which is impossible. So **no Kummer row
twist is invisible to the theta reflection.** The twist comes from the moduli, not from the values
`x_ℓ`.

## 3. The six designs, with repairs

κ is quoted in the `H = DL` normalisation; σ is the resulting principal exponent.

| design | what happens | repairs tried | κ / σ | label |
|---|---|---|---|---|
| **(a) Möbius-compatible** (`x = 1` on primes) | absorption survives exactly (`b = μ·g`); the reflection sees `χ_n(ℓ)⁴` (§2.1) | (a1) C–S + Prop. canonical: κ = 1. (a2) Prop. R + joint QLS: σ_min = 233/240 on grid. (a3) keep `b = μ·s(N m)` with `s` smooth, so the reflection stays at conductor `N k`: then `Amp_u A_u` is just `A_u` with another weight, the principal gain disappears, σ = 11/12 exactly. (a4) cube amplifiers `ℓ = c³`, to ride on `c_θ(nb³) = |b|γ₂(n)·…`: by §2.3 (e = 3) the dual twists are `χ_n(c)⁴χ_n(c')⁴` (conductor `cc'`), not a cube index | κ = 1; σ = 11/12 + 5λ/12 | CONDITIONAL / PROPOSED |
| **(b) Gauss-sum / theta-shaped** (`x_ℓ ∝ γ_1(ℓ)` or `conj(a_ξ(ℓ))`) | the dual coefficient becomes a plain character `χ_ℓ(k)`, but the CRT twist is unchanged (§2.3); and the principal value `\|Σ x_ℓ\|²` loses its coherence (`L^{2β}`, β = 1/2 with no bias, 5/6 even with a hypothetical Patterson-type bias) | (b1) sextic Gauss sums; (b2) cubic Gauss sums `conj(γ₂)`; (b3) choose `x` so that the dual coefficient is 1: the twist persists | σ = 11/12 + 11λ/12 (β = 1/2), 11/12 + 7λ/12 (β = 5/6), using κ = 1 | PROPOSED + HEURISTIC (β) |
| **(c) dual-row amplifier** `\|Σ z_j χ_j(k)\|²` on `Σ_k \|B_k\|²` | Poisson in `k` (lem:first-transfer, exact; R2 PASS) maps `χ_j χ̄_{j'}(k)` to the row-shift correlations `Σ_y M(y j^a) conj M(y j'^b)` of the original family; the original principal rows `y = v⁶` receive no coherent weight | (c1) `j` prime; (c2) `j` a cube (quadratic `χ_j`); (c3) `j` with `j^a` a sixth power: then the twist is trivial and nothing is amplified | gain 0: σ = 11/12 | PROPOSED |
| **(d) resonance** (long, multiplicative `x`) | an upper-bound amplifier needs off-diagonal control. With the trivial bound `\|Amp_u\|² ≤ \|x\|₁²`, the ledger gives σ = `1/2 + 5h/12` *identically*: exact break-even. For `N(ℓℓ') > H` the twists lose row orthogonality (Lemma A4 fails), and Poisson in `u` gives nothing | (d1) Soundararajan-type `x_ℓ = f(ℓ)` on smooth `ℓ`; (d2) Bondarenko–Seip GCD-sum structure (positivity gives *lower* bounds only); (d3) resonator restricted to `N ℓ ≤ H^{1/2}`: it is then an ordinary amplifier | σ = 11/12 (break-even) | PROVED-HERE (break-even) + PROPOSED |
| **(e) several members at once** (Prop. R′) | `Amp = Σ_w Amp^{(w)}` with `x^{(w)}_ℓ = conj ψ_w(ℓ)`: the weights add, and each member gets `L²/J` relative weight against `L` typical. All members already share the exponent of Prop. R′, so nothing compounds | (e1) J members of bounded conductor; (e2) the six unit members `ψ_ε`; (e3) members `w` with `N w ≤ D^ω`: the conductor penalty `(N w)^{1/12}` of Prop. R′ makes this worse | no gain beyond the single-member case | PROPOSED |
| **(f) a final step that sees twists** | what is needed is a power saving in the row-twisted mean squares `T(r)` (§4). Through the Oct 5 dual, `T(r)` is a `χ̄_r(k)`-twisted dual correlation `Σ_k χ̄_r(k) C_{k,ℓ} conj C_{k,ℓ'}` with `N(r)` times more rows than the untwisted dual. Its trivial size is `N(r)D²`, against the needed `HD·N(r)^{−η}` | (f1) quadratic-twist moments `L(½, θ⊗χ_h)` with an extra `χ_ℓ(h)` twist: the twist is sextic in `h` and the effective degree exceeds 4, as in Q_RHO §3; (f2) Heath-Brown's QLS on products `(k, ℓ)`: rows-plus-columns shape, so κ ≥ 1 by Lemma A2; (f3) Lemma A4 (orthogonality plus large values): reduces everything to the large-value mass, which contains the conclusion | OPEN; needs η > 5s/12 | OPEN + PROVED-HERE (A4) |

### Lemma A4 (row orthogonality of the amplifier; PROVED-HERE, using only the standard lattice Poisson formula)

Let `x` be supported on prime ideals `ℓ ∤ 6`, `N ℓ ≤ L`, and let `Φ` be a smooth radial Schwartz
weight.
* For `ℓ ≠ ℓ'`, `χ_ℓ χ̄_{ℓ'}` is primitive of modulus `ℓℓ'`. lem:poisson (equivalently [IK04, Thm 4.5]
  plus the primitive Gauss-sum identity) gives
  `Σ_u χ_ℓχ̄_{ℓ'}(u) Φ(N u/H) ≪_A H (L²/H)^A`, since every dual frequency is nonzero and
  `Φ̂` decays.
* Hence, for `L² ≤ H^{1−ε}`, `Σ_u Φ(N u/H) |Amp_u|² = H Φ̂(0) Σ_ℓ |x_ℓ|²(1 − 1/Nℓ) + O_A(H^{−A}‖x‖₁²)`.
* For any `V > 0`, split `|A_u|² = min(|A_u|², V) + (|A_u|² − V)_+` and use positivity of `|Amp_u|²`:

      M_amp(H) ≤ V·(1 + o(1)) H Σ_ℓ |x_ℓ|² + ‖x‖₁² · Σ_{N u ≤ H} (|A_u|² − V)_+.

With Lemma A1 and `x ≡ 1`, this gives
`|A_1|² ≪ V H^{5/6}/π(L) + H^{−1/6}·LV(V) + D²H^{−1/3}`, where `LV(V) = Σ_u (|A_u|² − V)_+`.
But the principal rows alone give `LV(V) ≥ (1 + o(1)) H^{1/6} (|A_1|² − V)_+`. So the second term is
never smaller than the *trivial* bound `|A_1|² ≤ V + H^{−1/6}LV(V)`. **The bounded part of
`|A_u|²` is amplifier-orthogonal for free, and every obstruction to TM is carried by large values,
whose mass contains the conclusion** (the fixed point of RUNG_STRENGTH §4).

## 4. The smallest statement that would make amplification work (OPEN)

Write `T(r) = Σ_{0 < N u ≤ H} χ_r(u) |A_u(D)|²` for `r = ℓ ℓ'^5`, where `ℓ ≠ ℓ'` are prime ideals with
`N ℓ, N ℓ' ≤ L`. Then

    M_amp = Σ_ℓ |x_ℓ|² Σ_{(u,ℓ)=1} |A_u|² + Σ_{ℓ ≠ ℓ'} x_ℓ conj(x_ℓ') T(ℓ ℓ'^5).

`T(r)` has an explicit positive *collision term*
`H Φ̂(0) Σ μ(n)μ(n') W W [ℓ n = ℓ' n']`, of relative size `≲ 1/N ℓ'`. It belongs to the diagonal
`‖b‖²` of the amplified polynomial. Write `T^off(r)` for the remainder.

**TM(η, s).** For `H = D L^s` (`0 ≤ s ≤ 1`), every pair `ℓ ≠ ℓ'` with norms `≤ L` satisfies

    |T^off(ℓ ℓ'^5)| ≪ D^ε H D · N(ℓℓ')^{−η}.

**Consequence (PROVED-HERE given TM and the imported Oct 5 mean square at `h > 1`; ledger "TM route").**
`M_amp ≪ D^ε H D L^{1 + max(0, 1 − 2η)}`, and by Lemma A1

    σ = 11/12 + λ(5s/6 − 2η)/2    (0 ≤ η ≤ 1/2),

so amplification beats 11/12 **iff η > 5s/12**.

| s | rows `H` | break-even η* | what TM(η, s) is |
|---|---|---|---|
| 1 | `DL` (ρ_eff = 1) | **5/12** | the κ < 1/6 statement; the Oct 5 dual then has `𝓗 ≤ DL` rows, but needs a twisted dual moment with saving `N(r)^{5/12}` |
| 1/2 | `D L^{1/2}` | 5/24 | sub-diagonal by `L^{1/2}` |
| 0⁺ | `D^{1+θ}` | 0⁺ (any power saving) | σ = 11/12 − λη; sub-diagonal by `L` (the ρ = 1 wall in amplified form) |

Context:
* A GRH-random model gives `|T^off(r)| ≈ D√H`, i.e. η up to `h/(4λ)` (`N(r) = L²`, `H = D^h`). So TM
  is consistent with GRH for all η ≤ 1/2 once `L ≤ H^{1/2}`.
* At `s = 1` and η = 5/12 + ε, TM gives σ = `11/12 − ελ`. Reaching 7/8 would need `λ(η − 5/12) ≥ 1/24`.
* TM(η, 0⁺) with `L = D^λ` has the same conclusion as the sub-diagonal second moment Mom(1, ρ) with
  `5(1 − ρ)/12 = λη`. Neither is known to imply the other.

## 5. Numerics (EMPIRICAL; floating point, finite; ν = 1, W the moments/ bump)

### 5.1 Amplified moments at `H = c·DL` (`results/amp_main.{json,log}`)

`ratio_b = M_amp / (n_u Σ_m |b_m|² Π_{p|m}(1 − 1/Np))`, with `b = x * (μW)` (the exact diagonal of the
amplified polynomial). The control `randphase` uses `x_ℓ` = fixed random unimodular phases.

| D | H/(DL) | ratio_b for L = 13, 31, 61, 127, 251, 499 (prime) | randphase range | enrichment (prime) | max principal share |
|---|---|---|---|---|---|
| 1000 | 0.25 | 0.997, 0.972, 0.980, 0.993, 0.994, 0.997 (L = 13, 31, 61, 127, 251, 499) | 0.988-1.024 | 4, 9, 15, 29, 49, 200 | 1.1e-03 |
| 1000 | 1 | 0.986, 0.994, 0.997, 0.997, 0.997, 0.999 (L = 13, 31, 61, 127, 251, 499) | 0.994-1.002 | 4, 9, 15, 62, 108, 200 | 3.5e-04 |
| 1000 | 4 | 0.996, 0.998, 0.999, 1.000, 1.000, 1.000 (L = 13, 31, 61, 127, 251, 499) | 0.997-1.001 | 4, 18, 31, 62, 98, 182 | 1.0e-04 |
| 2000 | 0.25 | 1.006, 0.993, 0.999, 1.000, 1.000, 1.000 (L = 13, 31, 61, 127, 251, 499) | 0.997-1.006 | 4, 9, 15, 29, 101, 181 | 3.8e-04 |
| 2000 | 1 | 1.003, 1.000, 1.003, 1.000, 1.001, 1.000 (L = 13, 31, 61, 127, 251, 499) | 0.997-1.002 | 4, 9, 28, 58, 101, 165 | 1.1e-04 |
| 2000 | 4 | 1.003, 1.001, 1.001, 1.000, 1.000, 1.000 (L = 13, 31, 61, 127, 251, 499) | 0.999-1.003 | 4, 16, 28, 53, 93, 154 | 3.1e-05 |
| 4000 | 0.25 | 0.994, 0.999, 1.001, 0.996, 0.998, 0.997 (L = 13, 31, 61, 127, 251, 499) | 0.986-0.999 | 4, 9, 15, 38, 67, 119 | 4.7e-04 |
| 4000 | 1 | 0.997, 0.998, 1.000, 0.999, 0.999, 0.999 (L = 13, 31, 61, 127, 251, 499) | 0.996-1.000 | 4, 11, 19, 38, 64, 114 | 1.4e-04 |
| 4000 | 4 | 0.998, 0.998, 0.999, 0.999, 0.999, 1.000 (L = 13, 31, 61, 127, 251, 499) | 0.998-1.001 | 4, 11, 18, 37, 62, 110 | 3.8e-05 |
| 8000 | 0.25 | 0.996, 0.995, 0.998 (L = 31, 127, 499) | 1.000-1.002 | 9, 18, 60 | 9.6e-05 |
| 8000 | 1 | 0.999, 0.998, 1.000 (L = 31, 127, 499) | 1.000-1.001 | 5, 20, 64 | 2.5e-05 |

* The amplified moment is diagonal-sized at every `(D, L, H)` tested. This includes `H = DL/4`, where
  the amplified polynomial has 4 times more columns than rows. **Empirical κ:** the slope of `log ratio_b` against `log π(L)` lies in [−0.0009, +0.0036] in every `(D, H/DL)` cell (6 values of `L` for D ≤ 4000, 3 for D = 8000); all 120 ratio_b lie in [0.972, 1.024] (see `results/tables.md`).
* **Principal weight.** Let enrichment = (principal share of `M_amp`) / (principal share of `M_2`). It
  grows like the number of primes `π(L)`, e.g. `D = 1000`: 4.2, 9.2, 15.1 for 4, 9, 15 primes.
  * Where it is about 2× larger (larger `L`), the extra comes from `|A_{v⁶}|²` with small `v` exceeding
    `|A_1|²`, not from the amplifier.
  * The principal share of `M_amp` stays below `1.1·10⁻³`. At these sizes the leverage term
    `H^{1/6}L²|A_1|²` is far below the diagonal, as the count predicts.
* The control (random phases) has the same `ratio_b` and enrichment ≈ 0, as it should: random phases do
  not amplify.

### 5.2 Twisted moments at `H = D^{1+θ}` (`results/tm_theta0{1,5}.json`, `tm.log`)

`G[ℓ,ℓ'] = T(ℓℓ'^5)` for the 46 prime ideals of norm ≤ 211.

| D | theta | rows | M_amp/(pi(L) diag) | kappa_emp | lambda_max/diag | off rms | random scale | slope vs log N(ll') | principal share |
|---|---|---|---|---|---|---|---|---|---|
| 1000 | 0.1 | 7242 | 1.0047 | +0.0012 | 1.207 | 0.0141 | 0.0167 | +0.050 | 6.7e-03 |
| 2000 | 0.1 | 15528 | 1.0435 | +0.0111 | 1.149 | 0.0106 | 0.0115 | +0.009 | 3.0e-03 |
| 4000 | 0.1 | 33264 | 1.0473 | +0.0121 | 1.103 | 0.0076 | 0.0079 | -0.019 | 4.5e-03 |
| 8000 | 0.1 | 71292 | 1.0443 | +0.0113 | 1.083 | 0.0060 | 0.0054 | +0.028 | 1.5e-03 |
| 16000 | 0.1 | 152766 | 1.0543 | +0.0138 | 1.079 | 0.0055 | 0.0037 | +0.036 | 8.2e-04 |
| 32000 | 0.1 | 327438 | 1.0559 | +0.0142 | 1.077 | 0.0052 | 0.0025 | +0.046 | 5.9e-06 |
| 1000 | 0.5 | 114750 | 1.0454 | +0.0116 | 1.109 | 0.0061 | 0.0042 | +0.020 | 6.0e-04 |
| 2000 | 0.5 | 324510 | 1.0557 | +0.0142 | 1.089 | 0.0056 | 0.0025 | +0.001 | 1.4e-04 |
| 4000 | 0.5 | 917664 | 1.0570 | +0.0145 | 1.077 | 0.0051 | 0.0015 | +0.108 | 3.6e-04 |
| 8000 | 0.5 | 2595678 | 1.0562 | +0.0143 | 1.073 | 0.0047 | 0.0009 | +0.194 | 5.4e-05 |

* `M_amp/(π(L)·diag) − 1 ≈ 0.04–0.06`, constant in `D`. This is the collision part of `‖b‖²`, so the
  empirical κ at `H = D^{1.1}` is ≈ 0, even though `H < DL` here.
* `λ_max(G)/diag ≤ 1.21`, falling with `D`. No amplifier vector does better than about 1.2× the
  diagonal.
* Off-diagonal rms (normalised by `(G[ℓ,ℓ]G[ℓ',ℓ'])^{1/2}`):
  * At θ = 0.1 and `D ≤ 8000` it sits at the random-twist scale `(Σ|A_u|⁴)^{1/2}/Σ|A_u|²`
    (0.0141 → 0.0060).
  * It then levels off at 0.0047–0.0061 (θ = 0.1 with `D ≥ 16000`, and all θ = 0.5 rows), while the
    random scale keeps falling to 0.0009.
  * HEURISTIC explanation: the floor is the explicit collision term `ℓn = ℓ'n'` (size `≍ 1/N ℓ'` when
    `Nℓ/Nℓ'` is in `(1/2, 2)`; positive), which this script does not subtract. The continuous
    approximation `collision_rms.py` predicts rms 0.0063 for these 46 primes
    (`results/collision_rms.out`), against the observed 0.0047–0.0061.
  * The fitted slope against `log N(ℓℓ')` does **not** measure η. The collision term lives only on
    pairs with `Nℓ/Nℓ' ∈ (1/2, 2)`, which are more frequent among large norms. That support artefact
    gives the positive slopes at θ = 0.5 (+0.108 at `D = 4000`, +0.194 at `D = 8000`).
  * TM is therefore neither contradicted nor measured beyond this scale.

## 6. What this note does not show

* No zero-free region is proved, and no exponent below 11/12 is obtained unconditionally or on the
  Oct 5 imports.
* Lemma A3 treats only the squarefree, coprime main block of the Poisson identity. The blocks with
  common factors (the manuscript's Möbius `f`, `b` variables) and the `m = ℓ²k` terms were not written
  out.
* The twist table uses sextic reciprocity up to ray-class factors. That table was not checked numerically
  here; LEVERAGE_FAMILIES S4 and Q_RHO check C cover the identities it rests on.
* Designs (b)–(e) are exponent-level analyses, not proofs of impossibility. The claim is only that
  each fails on the Oct 5 imports with the stated exponent.
* The numerics stop at `D ≤ 32000`. The principal share is tiny there, so they cannot distinguish κ = 0
  from small positive κ in the leverage-relevant regime.

## Files

| file | content |
|---|---|
| `README.md` | this note |
| `amp_ledger.py`, `results/amp_ledger.out` | exact-rational exponent ledger (sympy), asserts for every formula in §§0–4 |
| `amp_moments.py`, `results/amp_main.{json,log}` | amplified moments `M_amp` for the true family, diagonal ratios, principal enrichment |
| `tm_twisted.py`, `results/tm_theta01.json`, `results/tm_theta05.json`, `results/tm.log` | twisted moment Gram matrix `G[ℓ,ℓ']`, empirical κ at `H = D^{1+θ}`, conductor slopes |
| `amp_D8000.json`, `amp_D8000.log` (in `results/`) | the `D = 8000` amplified run on a reduced grid |
| `make_tables.py`, `results/tables.md` | the tables of §5 |
| `collision_rms.py`, `results/collision_rms.out` | HEURISTIC size of the explicit collision term in `T(ℓℓ'^5)` |

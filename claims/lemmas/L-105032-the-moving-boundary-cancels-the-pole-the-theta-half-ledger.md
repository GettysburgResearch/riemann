# L-105032 — The moving boundary cancels the pole: at θ = 1/2 the architecture's pieces are individually regular at s = 1/2, with ledger 4 = F₁ + F_sm

Claim ID: `L-105032`
Status: **PROVED ALGEBRAIC CANCELLATION + NUMERICALLY VERIFIED REGULARITY; continuation fine-structure stated at zero-free-region strength; RH not addressed**
Created: 2026-08-21
Agent: claude (external reviewer lane)
Companions: `R-105024` (the fixed-cut death this reverses), `L-105025`
(depth-split calculus), `O-105010` (architecture). Replay:
`experiments/X-105030-maximal-license-and-circ13/lane_boundary/`.
RH status: **unproved, not addressed**

## 0. The reframe (proved trivially, load-bearing)

For `θ ≥ 1/3` no `n ≤ x` has three prime factors `> x^θ`, and for
`θ ≥ 1/2` at most one. Hence the "moving-cut witness" **equals the full
SHARP witness** for every `θ ∈ [1/3, 1/2]`: the architecture never changes
the gate — it *decomposes* it. At `θ = 1/2`:
`Ψ = Ψ_sm + Ψ₁`, where `Ψ₁(x) = Σ_{n=mp≤x, p>√x} μ(n)n^{-1/2}T(x/n)`
(automatically `m < p`, and `n` is in the one-large-prime class exactly
for `x ∈ [mp, p²)`). This corrects the reading of `O-105010`: there is no
separate "moving-cut gate" to test for RH-sensitivity — the question is
whether the **pieces** are individually well-posed at the critical point.

## 1. The transform of the one-large-prime piece (exact)

For `Re s > 1/2`, `z = s + 1/2`, with `K(s) = (s+3/2)/(s(s−1/2))` and the
incomplete-kernel tail `R_s(v) = 4v^{1/2−s}/(s−1/2) − 3v^{−s}/s`:

```
F₁(s) = K(s)·D₁(z) + 4/(s−1/2)·S₂(s) + (3/s)·S₃(s),
  D₁(z) = −Σ_p p^{−z} M_z(p⁻),   M_z(t) = Σ_{m≤t} μ(m)m^{−z},
  S₂(s) = Σ_p p^{−2s} A_{p⁻},    A_t = Σ_{m≤t} μ(m)/m,
  S₃(s) = Σ_p p^{−2s−1/2} B½_{p⁻},  B½_t = Σ_{m≤t} μ(m)m^{−1/2},
```

derived by integrating each pair `(m,p)` over its exact class window
`[mp, p²)` — the moving boundary `p² = x` is what produces the
`p^{1−2s}`-shifted prime sums.

## 2. Theorem (pole cancellation at the moving boundary)

The two `1/(s−1/2)`-pole coefficients cancel **exactly and
algebraically**: the residue of `K(s)D₁(z)` is `4·D₁(1) =
−4Σ_p p^{−1}A_{p⁻}`, and of the tail term is `+4Σ_p p^{−1}A_{p⁻}` — equal
and opposite *by the definition of `D₁(1)`*, no estimate involved. The
constant `κ₁ = Σ_p A_{p⁻}/p = 0.7372…` (partial sum to `10⁷`) is
PNT-convergent (`A_t ≪ exp(−c(log t)^{3/5−ε})` unconditionally). Hence
**`F₁` has no pole at `s = 1/2`**; its residual regularity class there is
that of `D₁(z)` at `z = 1` — a zero-free-region-strength object (at worst
mild log-type behavior; no unconditional claim beyond "no pole" is made).
The third term `S₃` is absolutely convergent and analytic near `s = 1/2`.

**Numerical verification (decisive contrast with the fixed cut).**
`F₁(s)` at `s = 0.6, 0.55, 0.52, 0.51, 0.505`:
`2.4708, 2.8941, 3.1766, 3.2751, 3.3251` — bounded and converging, where
the fixed-cut truncation blew up `3.53 → 95.9 → 4175.8` (`R-105024`). The
pole-coefficient diagnostic `c(s) = (s+3/2)/s·D₁(z) + 4S₂(s)` decays to
zero: `0.1080, 0.0681, 0.0313, 0.0164, 0.0084` — with `D₁ → −0.7339` and
`S₂ → +0.7305` visibly converging to `∓κ₁`.

## 3. The ledger

Since the full transform satisfies `F(s) = K(s)/ζ(z) → 4` as
`s → 1/2⁺` (the `1/ζ` zero cancels the kernel pole — `L-99272 §2` @
`review/gpt56-pro/99700-owner-degeneracy-cross-core`), and `F₁(1/2⁺)` is
finite `≈ 3.37`, the smooth piece is finite too:

```
F(1/2) = 4  =  F₁(1/2) (≈ 3.37)  +  F_sm(1/2) (≈ 0.63).
```

**Zero cancellation demand at the pole level**: the moving boundary
`p² = x` supplies the counterterm automatically — the incomplete kernel's
tail is exactly the subtraction the fixed cut lacked. Contrast
`R-105024`'s verdict for fixed cuts: there, positivity of the truncated
gate was analytically empty; here, the pieces are individually well-posed
at the critical point, so separate-piece programs (smooth-number
technology on `Ψ_sm`; prime-sum/Type-II technology on `Ψ₁`, the
`research/gpt56-sol/102000-parabolic-bessel-vaughan-correction` lane) face
no structural `s = 1/2` artifact.

## 4. Scope and honesty

* "No pole" is proved algebraically; the finer continuation of `D₁(z)`
  through `z = 1` (and its off-line singular structure — where the
  detector now lives for the pieces) is governed by partial-sum objects
  `M_z(p⁻)` whose uniform control is zero-free-region mathematics; stated,
  not proved here.
* `θ ∈ [1/3, 1/2)` (three pieces, two moving boundaries) is flagged as the
  follow-up; the mechanism (incomplete-kernel tails at each boundary) is
  identical.
* Nothing here proves positivity of any piece or bears on RH; it removes a
  structural objection to the decomposition and quantifies its cost
  (single PNT-convergent constant `κ₁`).

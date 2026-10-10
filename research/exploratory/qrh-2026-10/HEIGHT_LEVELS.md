# What happens as you go higher: four senses of "height" in the quasi-RH methods

```text
Status: PROPOSED synthesis + EMPIRICAL exact-symbol checks (Section 1.2) + pointers to imported or
  heuristic statements, each labelled. No RH claim.
Scope: the moment ladder (order k), the height T of zeros (PR 910's native-height route), the rank of
  the metaplectic reflection (GL(2) -> GL(3)), and the depth of the zero-free half-plane (sigma0 -> 1/2)
Exact sources or dependencies: RUNG_STRENGTH.md; FOURTH_MOMENT_A2.md; A2_LITERATURE.md;
  moments/README.md; falsification/PR910_HEIGHT_TEST.md (and falsification/NOISE_FLOOR.md when
  present); a2/check_twisted_mult.py, a2/check_nesting.py, a2/check_triple.py; PR 910 Prop. 7.2
  (imported); Brubaker-Bump-Friedberg WMDS conventions as summarised in A2_LITERATURE.md Section 1
What was actually run: python3 a2/check_triple.py 60 20000 (209 pairwise-coprime prime triples,
  max deviation 3.5e-14; control with one pair symbol dropped fails by >= 1.732)
Smallest remaining gap: none of the four directions supplies a mechanism below 11/12 (Oct 5) or
  below 13/15 (Sep 30); see Section 5
```

RH remains unproved. "Higher" below never means "closer to a proof". It means what changes, with
proofs where available, as one parameter is pushed up.

## 1. Higher moments (order k of the moment ladder)

### 1.1 The boundary does not see k (PROPOSED; elementary)

PR 910 Prop. 7.2 [imported] turns a diagonal-size `2k`-th moment over `D^h` rows into the boundary
`1/2 + 5h/(12k)`. This depends only on the row/column ratio `ρ = h/k`
([RUNG_STRENGTH.md](RUNG_STRENGTH.md), Observation 1).
* Going up in `k` at fixed rows *raises* the length `D^k` and makes the problem *more*
  sub-diagonal.
* Every rung below 11/12 needs `ρ < 1`, at every `k`.
* Numerically, `M_{2k}` matches its diagonal for `k = 1, 2, 3` over `ρ ∈ [0.35, 2]`, `D ≤ 64000`.
  The per-row statistics are complex-Gaussian, with `M_{2k}/M₂^k ≈ k!`
  ([moments/](moments/README.md)).

### 1.2 The dual objects change type as k grows (PROPOSED identification + EMPIRICAL check)

After Poisson in the row variable and Möbius absorption, the `2k`-th moment dual has columns
`r = d₁⋯d_k` with a balanced `k`-fold divisor weight and coefficient `conj(α(r)) γ₂(r)`. For pairwise
coprime primary primes, twisted multiplicativity gives

    γ₂(d₁⋯d_k) = ∏_i γ₂(d_i) · ∏_{i<j} conj((d_j/d_i)₃),

with a cubic symbol on *every pair*. This is checked:
* `k = 2`: 362 pairs (`a2/check_twisted_mult.py`).
* `k = 3`: 209 triples, max deviation `3.5·10⁻¹⁴`; dropping one pair symbol fails
  (`a2/check_triple.py`).

As a Weyl-group multiple Dirichlet series pattern (one node per factor, a pair symbol `(·/·)₃^{-1}`
per edge; orientation immaterial for primary elements, A2_LITERATURE §2), this is the
**complete graph `K_k`**. Its Cartan matrix is `C_k = 3I − J`, with
`det C_k = 3^{k−1}(3 − k)`.

| rung | moment | graph | type | known automorphic home |
|---|---|---|---|---|
| `k = 1` | 2nd (Oct 5, imported) | one node | `A₁` | cubic theta on the 3-fold cover of GL(2) (Patterson) |
| `k = 2` | 4th (PR 910 (3.5)) | edge | `A₂`, finite | cubic GL(3) Eisenstein Whittaker coefficients (BBF); GL(3) theta vanishes on the support (A2_LITERATURE §3) |
| `k = 3` | 6th | triangle | **affine `Ã₂`** (`det = 0`) | infinite Weyl group; natural boundaries expected (cf. the affine `D̃₄` fourth moment of quadratic L-functions in Diaconu–Goldfeld–Hoffstein theory) |
| `k ≥ 4` | 8th, … | `K_k` | **Lorentzian** (signature `(k−1, 1)`) | none known |

This identifies coefficient shape only, and the extra quadratic factor `(h/r)₂` lies outside every
cubic WMDS (A2_LITERATURE §2). The table still makes the ladder concrete: each rung up gives the
same boundary for the same `ρ`, while its dual object leaves finite type at `k = 3`.

## 2. Higher zeros (height T, PR 910's native-height route)

* PR 910 asks for a one-sided off-diagonal condition on the curve
  `σ₀(Y) = 1/2 + c loglog Y/log Y`, `Y ≈ 4T`.
* It holds up to `T = 10⁶` with margin 8 ([falsification/PR910_HEIGHT_TEST.md](falsification/PR910_HEIGHT_TEST.md)).
* As `T` grows, the mechanism changes:
  * the threatening events are large values of `ζ`, not zeros (EMPIRICAL);
  * the damping on the curve is only a power of `log Y`, while `ζ` has Ω-values of size
    `exp(√(log T/loglog T))`;
  * so failure is expected (HEURISTIC) once `log T ~ 10³–10⁴`, far beyond any computation.
* An RH-conditional Proposition A reduces this to a lower bound for the Möbius tail at large-value
  heights. See [falsification/NOISE_FLOOR.md](falsification/NOISE_FLOOR.md) once present.
* Lesson: in this route, finite-height evidence is silent exactly where the mechanism switches.

## 3. Higher rank (the reflection one level up)

* GL(2): the cubic theta has Gauss-sum coefficients (Patterson). That is what lets the Oct 5
  reflection act on `conj(α)γ₂`.
* GL(3): the cubic theta has a unique Whittaker model, but `τ(m,1) = 0` unless `m` is a cube
  (Proskurin, Bump–Hoffstein, as quoted by Friedberg–Ginzburg) [IMPORTED]. Its coefficients vanish
  on the coprime squarefree support of the fourth-moment dual. So the "next reflection" disappears.
* A2-shaped theta coefficients need covering degree `n ≥ 4`, e.g. the quartic theta on GL(3).
  Even its GL(2) coefficients are known only up to sign.

## 4. Deeper half-planes (σ₀ → 1/2)

| statement | members `L(s, ψ_u)` | principal (`ζ_K`) |
|---|---|---|
| Mom(1, ρ), `ρ > 1` (imported Oct 5 input) | trivial | `1/2 + 5ρ/12` → 11/12 |
| Mom(1, ρ), `ρ < 1` | `1/2 + ρ/2` (Prop. R, rigorous) | `1/2 + 5ρ/12` |
| Mom(1, ρ) for all `ρ > 0` | GRH (equivalence, RUNG_STRENGTH Corollary) | RH for `ζ_K` |

Going deeper is the same as going sub-diagonal. The first loss in the manuscript's own pipeline is
the positivity step, which discards the `μ(f)` cancellation of the dual diagonal
([DISPERSION_GRH_STEP.md](DISPERSION_GRH_STEP.md) §4).

## 5. Summary

| direction | what happens as it increases | proved / checked |
|---|---|---|
| moment order `k` | same boundary at the same `ρ`; the dual type goes `A₁ → A₂ → Ã₂ → Lorentzian` | Observation 1 (elementary); pair pattern checked for `k ≤ 3` |
| zero height `T` | large values of `ζ`, not zeros, become the threat | numerics to `10⁶`; Prop. A (RH-conditional) |
| reflection rank | the GL(3) cubic theta vanishes where needed | literature (IMPORTED) |
| depth `σ₀ → 1/2` | equivalent to sub-diagonal mean squares; endpoint ⇔ family GRH | Prop. R, Corollary (elementary) |

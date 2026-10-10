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

### 1.2 The dual coefficients change shape as k grows (PROPOSED analogy + EMPIRICAL check)

After Poisson in the row variable and Möbius absorption, the `2k`-th moment dual has columns
`r = d₁⋯d_k` with a balanced `k`-fold divisor weight and coefficient `conj(α(r)) γ₂(r)`. For pairwise
coprime primary primes, twisted multiplicativity gives

    γ₂(d₁⋯d_k) = ∏_i γ₂(d_i) · ∏_{i<j} conj((d_j/d_i)₃),

with a cubic symbol on *every pair*. This is checked:
* `k = 2`: 362 pairs (`a2/check_twisted_mult.py`).
* `k = 3`: 209 triples, max deviation `3.5·10⁻¹⁴`; dropping one pair symbol fails
  (`a2/check_triple.py`). This is implied by the `k = 2` rule `γ₂(ab) = γ₂(a)γ₂(b)conj((b/a)₃)` by
  induction, so it is a consistency check of `eis.py`, not new evidence.

As a Weyl-group multiple Dirichlet series pattern (one node per factor, a pair symbol `(·/·)₃^{-1}`
per edge; orientation immaterial for primary elements, A2_LITERATURE §2), this is the
**complete graph `K_k`**. Its Cartan matrix is `C_k = 3I − J`, with
`det C_k = 3^{k−1}(3 − k)`.

| rung | moment | graph | coprime-support coefficient shape | known automorphic home |
|---|---|---|---|---|
| `k = 1` | 2nd (Oct 5, imported) | one node | `A₁` | cubic theta on the 3-fold cover of GL(2) (Patterson) |
| `k = 2` | 4th (PR 910 FOURTH_MOMENT_REDUCTION.md (3.5); UPSTREAM (7.1) at k = 2) | edge | `A₂`, finite | cubic GL(3) Eisenstein Whittaker coefficients (BBF); GL(3) theta vanishes on the support (A2_LITERATURE §3) |
| `k = 3` | 6th | triangle | **affine `Ã₂`** (`det = 0`) | infinite Weyl group; natural boundaries expected (cf. the affine `D̃₄` fourth moment of quadratic L-functions in Diaconu–Goldfeld–Hoffstein theory) |
| `k ≥ 4` | 8th, … | `K_k` | **Lorentzian** (signature `(k−1, 1)`) | none known |

The pair pattern is forced by the one-variable twisted multiplicativity of `γ₂`. The type
assignment presumes one complex variable per factor (supplied by the balanced divisor weight) and
has been checked only on coprime squarefree support. It is a PROPOSED coefficient-shape analogy,
not an identification of the series. (The same complete-graph pattern appears for any split of `r`
into `k` coprime factors; whether the series is a WMDS of type `K_k` also depends on the
prime-power data at primes dividing several `d_i`, which was not checked.)

This compares coefficient shape only, and the extra quadratic factor `(h/r)₂` lies outside every
cubic WMDS (A2_LITERATURE §2). The table still makes the ladder concrete: each rung up gives the
same boundary for the same `ρ`, while, on this analogy, its dual coefficient shape leaves finite type
at `k = 3`.

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
  heights. That lower bound is still open ([falsification/NOISE_FLOOR.md](falsification/NOISE_FLOOR.md)).
  * Proposition A is correct under RH, which it uses in two places.
  * Under RH, `R_Y = −ζ·T_Y + O(t^{−1/2+ε})`. So the route survives iff
    `limsup |ζ·T_Y| ≤ 1/√8` on the region.
  * Without RH: any zero of `G_Y` on `[σ₀,1) × {T}` kills it.
  * Every resonance argument that is linear in `R_Y` gives exactly 0, so a proof must handle Möbius
    correlations quadratically (Chowla-type). That is why the gap remains open.
  * The heuristic onset of failure is `T ≈ 10^35–10^60`, or `10^300–10^500` if the observed
    suppression of the tail at large `|ζ|` persists.
* Lesson: in this route, finite-height evidence is silent exactly where the mechanism switches.

## 3. Higher rank (the reflection one level up)

* GL(2): the cubic theta has Gauss-sum coefficients (Patterson). That is what lets the Oct 5
  reflection act on `conj(α)γ₂`.
* GL(3): the cubic theta has a unique Whittaker model, but `τ(m,1) = 0` unless `m` is a cube
  (Proskurin, Bump–Hoffstein, as quoted by Friedberg–Ginzburg) [IMPORTED]. Its coefficients vanish
  on the coprime squarefree support of the fourth-moment dual. So the "next reflection" disappears.
* A2-shaped theta coefficients need covering degree `n ≥ 4`, e.g. the quartic theta on GL(3).
  Even its GL(2) prime coefficients are undetermined (non-unique Whittaker models); the open
  Eckhardt–Patterson conjecture would fix their square (LEVERAGE §3.3).

## 4. Deeper half-planes (σ₀ → 1/2)

| statement | members `L(s, ψ_u)` | principal (`ζ_K`) |
|---|---|---|
| Mom(1, ρ), `ρ > 1` (imported Oct 5 input) | `1/2 + 5ρ/12` (Prop. R′ (RUNG), PROPOSED via unreviewed PR 910 extraction; nontrivial for `ρ < 6/5`) | `1/2 + 5ρ/12` → 11/12 |
| Mom(1, ρ), `ρ < 1` | `1/2 + 5ρ/12` (Prop. R′ (RUNG)); `1/2 + ρ/2` (Prop. R (RUNG), elementary, unreviewed) | `1/2 + 5ρ/12` |
| Mom(1, ρ) for all `ρ > 0` | GRH (equivalence, RUNG_STRENGTH Corollary) | RH for `ζ_K` |

Going deeper *requires* going sub-diagonal: sub-diagonal mean squares imply half-planes. The
converse holds only at the GRH endpoint; a member half-plane `β* > 1/2` gives
`M₂ ≪ D^{1+ρ+2(β*−1/2)}`, not Mom(1, ρ) ([DISPERSION_GRH_STEP.md](DISPERSION_GRH_STEP.md) §3(a)).
The first loss in the manuscript's own pipeline is
the positivity step, which discards the `μ(f)` cancellation of the dual diagonal
([DISPERSION_GRH_STEP.md](DISPERSION_GRH_STEP.md) §4).

## 5. Summary

| direction | what happens as it increases | proved / checked |
|---|---|---|
| moment order `k` | same boundary at the same `ρ`; the dual coefficient shape on coprime support goes `A₁ → A₂ → Ã₂ → Lorentzian` (PROPOSED analogy) | Observation 1 (elementary); pair pattern checked for `k ≤ 3` (`k = 3` implied by `k = 2`) |
| zero height `T` | large values of `ζ`, not zeros, become the threat | numerics to `10⁶`; Prop. A (RH-conditional) |
| reflection rank | the GL(3) cubic theta vanishes where needed | literature (IMPORTED) |
| depth `σ₀ → 1/2` | implied by sub-diagonal mean squares (converse only at the endpoint); endpoint ⇔ family GRH | Prop. R (RUNG), Corollary (elementary, PROPOSED); Prop. R′ (RUNG) via unreviewed PR 910 |

## 6. A formal anchor, uniform in height (added at the end of the wave)

The four directions above are about mechanisms. One statement is now machine-checked uniformly in
height, under the trust assumptions of [reviews/LEAN_BUILD_ATTEMPT.md](reviews/LEAN_BUILD_ATTEMPT.md),
Addendum B. It is a Lean theorem about Mathlib's `riemannZeta`, derived in this wave from the
imported 7/8 theorem ([lean/](lean/README.md)). Comparator accepted that imported theorem; the
strip itself has `#print axioms` evidence only.

* Every nontrivial zero `ρ = β + iγ` of `ζ` has `1/8 ≤ β ≤ 7/8`, at every height `γ`.
* The same strip holds for primitive `χ ≠ 1`, off the poles of the Gamma factor. This version
  rests on the Dirichlet 7/8 theorem, which comparator also accepted (Addendum C).

How it sits against the other height facts:

| height range | what is known about β | status |
|---|---|---|
| `0 < γ ≤ 3·10¹²` | `β = 1/2` | IMPORTED computation (Platt–Trudgian 2021; not re-run here) |
| all `γ` | `1/8 ≤ β ≤ 7/8` | Lean theorem (this wave), on the imported 7/8 development |
| `γ → ∞` | classical zero-free regions `β < 1 − c/((log γ)^{2/3}(log log γ)^{1/3})` | IMPORTED; weaker than 7/8 at every height beyond the verified range |

So, at the level of zero-free regions, "going higher" now has a floor that does not erode: the
strip does not narrow towards `Re s = 1` as `γ` grows. That is all it says. In particular:
* Section 2's PR 910 route still breaks down heuristically at large heights, because the threat
  there is large values of `ζ`, which a zero-free strip does not control pointwise;
* the strip width `3/4` is far from RH's width `0`.

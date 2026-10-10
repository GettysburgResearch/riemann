# Explicit prime-number-theorem consequences of the half-plane Re s > 7/8

```text
Status: CONDITIONAL on H(7/8) (Lean-checked import, see below) + IMPORTED explicit results (Sec. 1)
  + PROPOSED derivations (Secs. 2-5, ours, unreviewed) + COMPARISON (Sec. 6) + EMPIRICAL sanity
  check (Sec. 7, floats). RH is unsolved; nothing here proves or disproves it.
Scope: explicit (all constants and thresholds stated) bounds for psi, theta, pi - li, primes in
  short intervals, and the Robin/Nicolas envelope of ROBIN_GRADED.md, for all x (or n) beyond
  stated thresholds. Finite verification ranges are imported, not extended.
Exact sources or dependencies:
  H(7/8): Lean theorem OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re, kernel-checked with axioms
    propext, Classical.choice, Quot.sound, under the trust assumptions recorded in
    reviews/LEAN_BUILD_ATTEMPT.md (Addenda A, B); the Lean development itself is unreviewed;
  Platt-Trudgian, RH true up to 3e12, arXiv:2004.09765v1 (Bull. LMS 53 (2021)), Thm 1 and Cor. 1;
  Buthe, partial-RH estimates, arXiv:1410.7015v4 (Math. Comp. 85 (2016)), Thm 2;
  Hasanalizade-Shen-Wong, N(T) bound, arXiv:2107.06506v1 (J. Number Theory 235 (2022)), Cor. 1.2;
  Cully-Hugill-Johnston, explicit Riemann-von Mangoldt formula, arXiv:2111.10001v5, Thm 1.2 + Table 4;
  Nicolas, primorials under RH, arXiv:1202.0729v2 (Acta Arith. 155 (2012)), eq. (1.3), Lemmas 2.1, 2.2;
  comparison only: Fiori-Kadiri-Swidinsky arXiv:2206.12557v2 Tables 3-4; Johnston-Yang
  arXiv:2204.01980v2 Thm 1.1, Thm 1.4, Table 1.
What was actually run: scripts/explicit_pnt_7_8.py (mpmath.iv interval arithmetic, outward rounding,
  128 bits; sympy symbolic identity checks; exact enumeration of psi, theta below 1501). About 17 s
  on one core. Optional --zeros flag: float sanity check against mpmath.zetazero (EMPIRICAL).
  Output: results/explicit_pnt_7_8.txt, results/explicit_pnt_7_8.json.
Smallest remaining gap: the result rests on the explicit truncation constant M of Cully-Hugill-
  Johnston (Thm 1.2; its text and Table 4 disagree, we use the larger Table 4 value; Thm 1 survives
  M -> 4M). For the Robin SIGN question (not the envelope) the truncated formula is too weak: its
  x^{-1/2} error swamps the RH-scale margin 0.78/(sqrt(x) log x). Nothing here is reviewed.
```

Notation. `L = log x`. `ψ, θ` are Chebyshev's functions, `R(x) = ψ(x) − x`, `S(x) = θ(x) − x`. Zeros `ρ = β + iγ` are the nontrivial zeros, with multiplicity. `H_0 = 3·10^12`. `M = 6.431`. `w(t) = t^{−2}(1/log t + 1/log² t)`. `J(x) = ∫_x^∞ R w` and `K(x) = ∫_x^∞ S w` (Nicolas's notation; ROBIN_GRADED calls `J` "`I`").

## 0. Results at a glance

All rows are CONDITIONAL on H(7/8) and the imports of Sec. 1, and PROPOSED (our derivation, unreviewed). Every constant comes from a quoted statement or from the interval computation in the script.

| # | Statement | Range |
|---|---|---|
| Thm 1 | `\|ψ(x) − x\| ≤ 0.0026 x^{7/8} log² x` | all `x ≥ 227` |
| Thm 1(a) | `\|ψ(x) − x\| ≤ x^{7/8}(log² x/(128π) + 0.17 log x − 113)` | `x ≥ e^{190}` |
| Thm 1(b) | best constant `A(L_0)` decreases to `1/(128π) = 0.0024868` (table in Sec. 3) | `x ≥ e^{L_0}` |
| Cor 2 | `\|θ(x) − x\| ≤ 0.0026 x^{7/8} log² x` | all `x ≥ 967` |
| Cor 3 | `\|π(x) − li(x)\| ≤ 0.00266 x^{7/8} log x` | all `x > 2657` |
| Cor 4 | `(x, x + 0.006 x^{7/8} log² x]` contains a prime | all `x ≥ 967` |
| Thm R | `σ(n)/n < n/φ(n) ≤ e^γ log log n + 1.41 (log n)^{−1/8}` | all `n ≥ e^{4462.69}` (≈ `10^{1938.1}`) |
| Thm R | same with `C = 0.1`, `0.01`, `10^{−6}`, `10^{−10}` | `log n ≥ 2.52·10^7`, `5.23·10^{10}`, `1.02·10^{26}`, `3.55·10^{114}` |

Three points to keep in view.
- **Where H(7/8) is actually used.** For `x ≤ e^{190}` (about `10^{82.5}`), Theorem 1 uses only zeros below `H_0`, so it is unconditional there. It is also weaker there than the best published unconditional bounds. H(7/8) starts to matter at `x ≈ e^{190}`. The conditional bound beats the best unconditional table (Fiori–Kadiri–Swidinsky) from `log x ≈ 253`, about `x ≈ 10^{110}`.
- **Why the leading constant is `1/(128π)`.** Zeros up to height `T` contribute about `(1/2π) log² T · x^{7/8}`. The optimal `T` is about `x^{1/8}`, which gives `(1/2π)(1/8)² = 1/(128π)`. Under RH the same count with `T ≈ x^{1/2}` gives Schoenfeld's `1/(8π)`.
- **ROBIN_GRADED's ineffective `n_0` is now explicit.** The constant `C` can be traded against `n_1`, and the trade-off is in Table R.

## 1. Imported statements (exact, with hypotheses)

**H(7/8) (Lean import).** `@OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re : ∀ {s : ℂ}, 7 / 8 < s.re → riemannZeta s ≠ 0`, about Mathlib's `riemannZeta`. This is the analytic continuation of ζ, so every nontrivial zero has `β ≤ 7/8`, and by the functional equation `β ≥ 1/8`. The kernel check is recorded in reviews/LEAN_BUILD_ATTEMPT.md, Addendum A. We use nothing else from the import.

**PT (Platt–Trudgian, arXiv:2004.09765v1, Theorem 1).** "The Riemann hypothesis is true up to height 3 000 175 332 800. That is, the lowest 12 363 153 437 138 non-trivial zeroes ρ have ℜρ = 1/2." The abstract states: "all zeroes β + iγ of the Riemann zeta-function with 0 < γ ≤ 3·10^12 have β = 1/2." We use `H_0 = 3·10^12`.

**Bü (Büthe, arXiv:1410.7015v4, Theorem 2).** "Let T > 0 such that the Riemann hypothesis holds for 0 < ℑ(ρ) ≤ T. Then, under the condition 4.92 √(x/log x) ≤ T, the following estimates hold:
- `|ψ(x) − x| ≤ (√x/8π) log(x)²` for `x > 59`;
- `|ϑ(x) − x| ≤ (√x/8π) log(x)²` for `x > 599`;
- `|π(x) − li(x)| ≤ (√x/8π) log(x)` for `x > 2657`."

With PT, the condition holds up to `x = 2.169·10^25`. The script checks `4.92·√(x/log x) ≤ 2.99997·10^12` there.
- This instantiation is PT Corollary 1.
- PT print `log² x` for the π-bound, which is weaker than Büthe's `log x`.
- Johnston–Yang (arXiv:2204.01980v2, Lemma 2.2) print `log x`, matching Büthe.
- We use Büthe's `log x`. With PT's printed form, Corollary 3 would need `x ≥ 1.64·10^6` instead of `x > 2657` (computed in the script).

**HSW (Hasanalizade–Shen–Wong, arXiv:2107.06506v1, Corollary 1.2).** "For any T ≥ e, we have |N(T) − (T/2π) log(T/2πe)| ≤ 0.1038 log T + 0.2573 log log T + 9.3675", where `N(T)` counts zeros with `0 < β < 1`, `0 < γ ≤ T`.
- Write `P(t) = (t/2π) log(t/2πe)` and `Q(t) = 0.1038 log t + 0.2573 log log t + 9.3675`.
- Their Table 1 lists the *published* Trudgian (2014) constants as `0.112, 0.278, 3.385`. Trudgian's arXiv:1208.5846v2 prints `0.111, 0.275, 2.450 + 7/8 + 0.2/T_0`. Because of that version difference we did not use Trudgian.

**CHJ (Cully-Hugill–Johnston, arXiv:2111.10001v5, Theorem 1.2).** "For any α ∈ (0, 1/2] there exist constants M and x_M such that for max{51, log x} < T < (x^α − 2)/2, ψ(x) = x − Σ_{|γ|≤T} x^ρ/ρ + O*(M x log x/T) for all x ≥ x_M." Here `O*(h)` means absolute value at most `h`.
- We use the Table 4 row `log x_M = 40, α = 1/2, M = 6.431`.
- **Version caveat.** The theorem's own text in v4 and v5 says "(40, 1/2, 5.03)". Table 4 and §6 give the larger values (6.431, and 0.6651 where the text says 0.5597). v2 had 2.091. We use the larger 6.431.
- Sec. 3 shows Theorem 1 still holds with `0.0026` if `M` is replaced by `4M`.

**Ni (Nicolas, arXiv:1202.0729v2).**
- (1.3): `Σ_ρ 1/(ρ(1−ρ)) = 2 + γ − log π − 2 log 2 = 0.0461914179…`. This value is unconditional: pair `ρ` with `1−ρ`, and the sum equals `2 Σ_ρ Re(1/ρ)`.
- Lemma 2.1 ("Proposition 1 of [6]"): for `x ≥ 121`, `K(x) − S(x)²/(x² log x) ≤ log f(x) ≤ K(x) + 1/(2(x−1))`, where `f(x) = e^γ log θ(x) ∏_{p≤x}(1 − 1/p)`. This is N2 of ROBIN_GRADED.
- Lemma 2.2: for `Re z < 1` and `x > 1`, `F_z(x) := ∫_x^∞ t^{z−2}(1/log t + 1/log² t) dt = x^{z−1}/((1−z) log x) + r_z(x)`, with `r_z(x) = −(z/(1−z))·[x^{z−1}/((1−z) log² x) + ∫_x^∞ 2t^{z−2}/((z−1) log³ t) dt]` (his (2.6)).
- We use Lemma 2.2 only as an identity. The script verifies it symbolically.

**Classical facts used.**
- (E) `∏_{p≤n} p < 4^n` (Erdős). So `θ(y) < y log 4` for `y ≥ 1`.
- (G) No zero has `0 < γ ≤ 14`.
- Bertrand's postulate.

Read but not used: Dudek, arXiv:1401.4233v1, Thm 2.1. It gives error `2x log² x/T` for half-odd-integer `x > e^{60}` and changes only lower-order terms here.

| Source | Version read | sha256 (PDF as fetched, first 16 hex) |
|---|---|---|
| Platt–Trudgian | arXiv:2004.09765v1 | `3362f66af9fa9373` |
| Büthe | arXiv:1410.7015v4 | `d87b9d33638d1734` |
| Hasanalizade–Shen–Wong | arXiv:2107.06506v1 | `3fc4c89f49249924` |
| Cully-Hugill–Johnston | arXiv:2111.10001v5 (v2 `288e298f…`, v4 `84e72c69…` compared) | `dc51b2ca4bf326dc` |
| Nicolas | arXiv:1202.0729v2 | `d5ff55f73a832714` |
| Fiori–Kadiri–Swidinsky | arXiv:2206.12557v2 | `405e5dcbca6067fa` |
| Johnston–Yang | arXiv:2204.01980v2 | `565993a6def48b23` |
| Dudek; Trudgian (not used) | arXiv:1401.4233v1; arXiv:1208.5846v2 | `3b3eecdf371619ed`; `274b3a0a14d79400` |

## 2. Zero sums (Lemma Z, PROPOSED; uses HSW, PT, Ni (1.3), G)

**Lemma Z.** Let `a = log(H_0/2π) = 26.8917563…`.
- (Z1) For `T ≥ 14`: `Σ_{0<γ≤T} 1/γ ≤ (1/4π) log²(T/2π) − 1/(2π) − (1/4π) log²(14/2π) + (1/2π) log(14/2π) + Q(T)/T + I_Q(14)`. Here `I_Q(14) ≤ 0.720888` bounds `∫_{14}^∞ Q/t²`. At `T = H_0` this is at most `Z_1 := 58.185931`.
- (Z2) For `T ≥ H_0`: `Σ_{H_0<γ≤T} 1/γ ≤ (1/4π)[log²(T/2π) − a²] + ε̄`, where `ε̄ := 2Q(H_0)/H_0 + ∫_{H_0}^∞ Q/t² ≤ 1.3252·10^{−11}`.
- (Z3) `s_high := Σ_{|γ|>H_0} 1/γ² ≤ (a+1)/(πH_0) + 2Q(H_0)/H_0² + 4∫_{H_0}^∞ Q/t³ ≤ 2.9595·10^{−12}`.
- (Z4) `s_low := Σ_{|γ|≤H_0} 1/|ρ|² ≤ 2 + γ − log 4π = 0.04619141793…`.

*Proof.*
- (Z1)–(Z3) are Stieltjes partial summation against `dN`. For example `Σ_{H_0<γ≤T} 1/γ = N(T)/T − N(H_0)/H_0 + ∫_{H_0}^T N/t²`. Insert `P − Q ≤ N ≤ P + Q` (HSW) and use the exact antiderivatives below.
- `∫ P(t)/t² dt = (1/4π) log²(t/2π) − (1/2π) log(t/2π)`.
- `P(t)/t = (1/2π)(log(t/2π) − 1)`.
- `∫_A^∞ log(t/c)/t² dt = (log(A/c) + 1)/A`.
- The `Q` integrals are bounded by elementary integration by parts. For example `∫_A^∞ log log t/t² ≤ (log log A + 1/log A)/A`.
- In (Z1), `N(t) = 0` for `t < 14` (G).
- (Z4): every zero with `|γ| ≤ H_0` has `β = 1/2` (PT), so `1/|ρ|² = 2 Re(1/ρ)`. Also `Re(1/ρ) = β/|ρ|² > 0` for every zero. Hence `s_low ≤ 2 Σ_ρ Re(1/ρ) = Σ_ρ 1/(ρ(1−ρ))` (Ni (1.3)). ∎

The script evaluates all four bounds in interval arithmetic. Two consistency checks:
- ROBIN_GRADED §5.3 used the heuristic tail `ε(T) ≈ 3.0·10^{−12}`; (Z3) is the rigorous version.
- EMPIRICAL: the first 200 zeros give `Σ 2/(1/4+γ²) = 0.04207 < s_low`.

## 3. Theorem 1: the ψ bound (CONDITIONAL, PROPOSED)

**Theorem 1.** Assume H(7/8). Then:
- `|ψ(x) − x| ≤ 0.0026 x^{7/8} log² x` for every real `x ≥ 227`;
- `|ψ(x) − x| ≤ x^{7/8}(log² x/(128π) + 0.17 log x − 113)` for `x ≥ e^{190}`.

For `227 ≤ x ≤ e^{190}` the proof does not use H(7/8).

*Proof, for `x ≥ e^{40}`.* Apply CHJ with an admissible `T`. The zeros with `|γ| ≤ min(T, H_0)` have `|x^ρ| = x^{1/2}` (PT). The zeros with `H_0 < |γ| ≤ T` have `|x^ρ| ≤ x^{7/8}` (H(7/8)). Every zero has `|ρ| ≥ |γ|`. With Lemma Z this gives, for `T ≤ H_0`,

    |ψ(x) − x| ≤ 2 Z_1(T) x^{1/2} + M x log x / T,                                   (3.1)

and for `T > H_0`,

    |ψ(x) − x| ≤ 2 Z_1 x^{1/2} + 2 x^{7/8} [ (1/4π)(log²(T/2π) − a²) + ε̄ ] + M x log x / T.   (3.2)

The choice of `T` depends on the range of `L = log x`, and so does `A_eff(L)`, the bound divided by `x^{7/8} L²`:

| Regime | Range of `L = log x` | `T` | `A_eff(L)` bound | sup (interval, cells of width 1/4) |
|---|---|---|---|---|
| I | `40 ≤ L ≤ 2 log(4H_0) = 60.2319` | `√x/4` (≤ `H_0`) | `2Z_1(T)e^{−3L/8}/L² + 4M e^{−3L/8}/L` | `2.06·10^{−7}` |
| II | `60.2319 ≤ L ≤ 190` | `H_0` | `2Z_1 e^{−3L/8}/L² + M e^{L/8}/(H_0 L)` | `2.328·10^{−4}` |
| III | `L ≥ 190` | `8πM x^{1/8}` | `1/(128π) + b/L − d/L² + 2Z_1 e^{−3L/8}/L²` | `0.0025497514` |

Admissibility of `T` (CHJ needs `max{51, L} < T < (x^{1/2} − 2)/2`):
- Regime I: holds since `x ≥ e^{40}`.
- Regime II: `T = H_0` is admissible once `L > 2 log(2H_0 + 2) ≈ 58.85`.
- Regime III: `T ≥ H_0` needs `L ≥ 8 log(H_0/(8πM)) = 189.155`.

In regime III, `log(T/2π) = L/8 + log 4M`. Expanding (3.2) gives

    |ψ(x) − x| ≤ x^{7/8} [ L²/(128π) + b L − d ] + 2 Z_1 x^{1/2},
    b = (log 4M + 1)/(8π) ≤ 0.1689997,   d = (a² − log² 4M)/(2π) − 2ε̄ ≥ 113.41712.

- On `L ≥ 190`, `2Z_1 x^{−3/8} ≤ 1.4·10^{−29}`. This gives Theorem 1(a).
- `b/L − d/L²` is largest at `L* = 2d/b ≈ 1342.2`, where it equals `b²/(4d) ≤ 6.296·10^{−5}`. So in regime III `A_eff ≤ 0.0024868 + 0.0000630 + 10^{−29} ≤ 0.0025498`.

*Proof, for `x < e^{40}`.*
- Bü+PT gives `|ψ(x) − x| ≤ √x log² x/(8π)` for `59 < x ≤ 2.169·10^25`. This is at most `0.0026 x^{7/8} log² x` once `x ≥ (8π·0.0026)^{−8/3} = 1443.55`.
- For `227 ≤ x < 1501` we computed `ψ(n)` exactly (interval sums of `log p`). On each `[n, n+1)` we checked `max(|ψ(n) − n|, |ψ(n) − n − 1|) ≤ 0.0026 n^{7/8} log² n`; the right side increases in `x`.
- The smallest starting point that works is `227`. ∎

**Tail constants (Theorem 1(b)).** `A(L_0) := sup_{L ≥ L_0}` of the regime-III bound:

| `L_0` | 190–1000 | 1500 | 2000 | 5000 | 10^4 | 10^5 | 10^6 | ∞ |
|---|---|---|---|---|---|---|---|---|
| `A(L_0) ≤` | 0.0025498 | 0.0025491 | 0.0025430 | 0.0025161 | 0.0025026 | 0.0024885 | 0.0024870 | `1/(128π)` = 0.0024868 |

**Sensitivity to the imported `M` (rigorous recomputation).** With `2M` the supremum over `x ≥ e^{40}` is at most `0.0025726`. With `4M` it is at most `0.0025993`. So Theorem 1 with `0.0026` survives a fourfold error in CHJ's constant. The leading `1/(128π)` does not depend on `M` at all.

## 4. Corollaries (CONDITIONAL, PROPOSED)

**Corollary 2 (θ).** `|θ(x) − x| ≤ 0.0026 x^{7/8} log² x` for all `x ≥ 967`.

*Proof.*
- (E) gives `0 ≤ ψ(x) − θ(x) = Σ_{k≥2} θ(x^{1/k}) ≤ log 4 (√x + x^{1/3} log x/log 2)`. There are at most `log x/log 2` nonzero terms, and the terms with `k ≥ 3` are each at most `θ(x^{1/3})`.
- For `x ≥ e^{40}` this adds at most `2.85·10^{−10} x^{7/8} log² x` to Theorem 1, so the total stays below `0.00254976 < 0.0026`.
- For `1443.55 ≤ x ≤ 2.169·10^25`, use Bü's θ-bound.
- For `967 ≤ x < 1501`, use exact enumeration (the script). ∎

**Corollary 3 (π − li).** `|π(x) − li(x)| ≤ 0.00266 x^{7/8} log x` for all `x > 2657`.

*Proof.*
- For `2657 < x ≤ X := 2.169·10^25`, Bü's `√x log x/(8π)` is below the claim once `x ≥ 1358.4`.
- For `x > X`, partial summation gives `π(x) − li(x) = π(X) − li(X) + (θ(x) − x)/log x − (θ(X) − X)/log X + ∫_X^x (θ(t) − t)/(t log² t) dt`.
- Use Bü at `X` and Corollary 2 inside, with `∫_X^x t^{−1/8} dt ≤ (8/7) x^{7/8}`. This gives the constant `0.0026 (1 + 8/(7 log X)) + √X log X/(4π X^{7/8} log X) ≤ 0.0026510`. ∎

**Corollary 4 (short intervals).** For every `x ≥ 967`, the interval `(x, x + 0.006 x^{7/8} log² x]` contains a prime.

*Proof.* Put `h = c x^{7/8} log² x`. Then `θ(x+h) − θ(x) ≥ h − 0.0026[(x+h)^{7/8} log²(x+h) + x^{7/8} log² x]`.
- Since `x^{−1/8} log² x ≤ 256/e²`, we have `h/x ≤ 34.65c`.
- So `(x+h)^{7/8} log²(x+h) ≤ (1+δ) x^{7/8} log² x`, where `δ ≤ (1 + 34.65c)^{7/8}(1 + log(1 + 34.65c)/log 967)² − 1 ≤ 0.2455` at `c = 0.006`.
- Then `0.0026(2 + δ) ≤ 0.00584 < 0.006`. ∎

Asymptotically the constant tends to `2·0.0025498 ≈ 0.0051`. For comparison, Cully-Hugill–Johnston (Thm 1.3, unconditional) give a prime between consecutive 140th powers, an interval of length about `140 x^{139/140}`. The first-order differencing refinement (`h ≍ x^{7/8} log x log log x`) was not carried out.

## 5. Robin and Nicolas, explicit (CONDITIONAL, PROPOSED)

ROBIN_GRADED Prop. R uses four inputs:
- N2 (Ni Lemma 2.1), which is already explicit;
- Lemma K, a bound on `J = ∫ R w`;
- a bound on `J_0 = ∫ (ψ − θ) w`;
- a pointwise bound on `S` for the second-order term `S²/(x² log x)`.

We make each one explicit. Lemma K is replaced by the sharper "K′" route that ROBIN_GRADED left as a sketch, now with explicit error terms.

**Lemma J (explicit K′).** Assume H(7/8). For `x ≥ e^{40}`:

    |J(x)| ≤ s_low · x^{−1/2}/log x · (1 + (1 + 4/log x)/log x)
           + s_high · x^{−1/8}/log x · (1 + (1 + 16/log x)/log x)
           + 8M x^{−1/2} (1 + 1/log x).

For `600 ≤ x ≤ X = 2.169·10^25`: `|J(x)| ≤ (1/4π) x^{−1/2}(log x + 3) + |J(X)|`.

*Proof.*
1. **Truncation.** For `t ≥ x ≥ e^{40}` apply CHJ with `T(t) = √t/4`. This is admissible, and `R(t) = −Σ_{|γ|≤T(t)} t^ρ/ρ + E(t)` with `|E(t)| ≤ 4M √t log t`.
2. **Error term.** `∫_x^∞ |E| w ≤ 4M ∫_x^∞ t^{−3/2}(1 + 1/log t) dt ≤ 8M x^{−1/2}(1 + 1/log x)`.
3. **Fubini.** The zero `ρ` enters for `t ≥ 16γ²`. So `∫_x^∞ Σ_{|γ|≤T(t)} (t^ρ/ρ) w = Σ_ρ F_ρ(y_ρ)/ρ` with `y_ρ = max(x, 16γ²)`.
   - This is justified by Tonelli: `Σ_ρ F_β(y_ρ)/|ρ| ≤ Σ_ρ 8(16γ²)^{−1/8}/|γ| < ∞` under H(7/8).
4. **Termwise bound.** Ni Lemma 2.2 and (2.6), with `∫_y^∞ t^{β−2}/log³ t ≤ y^{β−1}/((1−β) log³ y)`, give
   `|F_ρ(y)/ρ| ≤ y^{β−1}/(|ρ||1−ρ| log y) + y^{β−1}(1 + 2/((1−β) log y))/(|1−ρ|² log² y)`.
5. **Summing over zeros.**
   - Zeros with `|γ| ≤ H_0` have `β = 1/2` and `|1−ρ| = |ρ|`. They sum to the `s_low` line.
   - Zeros with `|γ| > H_0` have `1/8 ≤ β ≤ 7/8`, `|ρ|, |1−ρ| ≥ |γ|` and `y^{β−1} ≤ y^{−1/8}`. They sum to the `s_high` line.
   - All these functions decrease in `y`, and `y ≥ x`.
6. **Small x.** For `x ≤ X`, use Bü on `[x, X]`: `∫ (√t log² t/(8π)) w = (1/8π)∫ t^{−3/2}(log t + 1) ≤ (1/4π) x^{−1/2}(log x + 3)`. ∎

**Other inputs.**
- *Prime powers.* `0 ≤ J_0(x) ≤ log 4 [2x^{−1/2}(1/log x + 1/log² x) + (3/(2 log 2)) x^{−2/3}(1 + 1/log x)]`, by the bound on `ψ − θ` in Corollary 2.
- *Second-order term.* Use `|S(x)| ≤ √x log² x/(8π)` (Bü) for `599 < x ≤ X`. Beyond `X`, use `|S| ≤ (bound (3.1)/(3.2)) + (ψ − θ)`, evaluated on cells.
- *Nicolas side.* With `f_φ(N) = N/(φ(N) log log N)` and `x = p_k`, N2 gives `−J(x) − 1/(2(x−1)) ≤ log(f_φ(N_k)/e^γ) ≤ −J(x) + J_0(x) + S(x)²/(x² log x)`.

**Proposition N (explicit).** For every prime `p_k ≥ x_1` (Table R), `|log(f_φ(N_k)/e^γ)| ≤ c_U p_k^{−1/8}/log p_k`.

*Proof.* Multiply each bound above by `x^{1/8} log x`. Each resulting piece is monotone in `x`:
- `x^{−3/8} log x (log x + 3)` decreases for `log x > 4.2`;
- `x^{−7/8} log⁴ x` decreases for `log x > 32/7`;
- the `J_0` pieces decrease for `log x > 1`;
- `|J(X)| x^{1/8} log x` increases, so it is bounded by its value at `X`;
- beyond `X`, the cell maxima are taken up to `log x = 400`, and `L⁴e^{−L/8}` decreases after that.

So the supremum over `x ≥ x_1` is computed by finitely many interval evaluations (`robin_cU` in the script). ∎

**Theorem R (explicit Prop. R).** Assume H(7/8). For each row of Table R, every integer `n` with `log n ≥ L_1` satisfies

    σ(n)/n  <  n/φ(n)  ≤  e^γ log log n + C (log n)^{−1/8}.

*Proof.* Let `k = ω(n)`, `y = log N_k ≤ L = log n` and `c = C e^{−γ}`. Recall that `n/φ(n) ≤ N_k/φ(N_k) = e^γ log y · f_φ(N_k)/e^γ`.
- **Case A: `p_k ≥ x_1`.**
  - Let `u = c_U p_k^{−1/8}/log p_k`. Proposition N gives `n/φ(n) ≤ e^γ log y · e^u`.
  - Let `η` bound `θ(p)/p − 1` for `p ≥ x_1` (Bü, then Theorem 1). Then `y ≤ (1+η) p_k`, so `p_k^{−1/8} ≤ (1+η)^{1/8} y^{−1/8}` and `log y ≤ log p_k + log(1+η)`.
  - Hence `(e^u − 1) log y ≤ c_U e^{u_max}(1+η)^{1/8}(1 + log(1+η)/log x_1) y^{−1/8}`. The script checks that this is at most `c y^{−1/8}`.
  - So `n/φ(n) ≤ e^γ g(y)` with `g(y) = log y + c y^{−1/8}`. Since `g' > 0` for `y^{1/8} > c/8`, and `y ≤ L`, we get `g(y) ≤ g(L)`.
- **Case B: `p_k < x_1`.**
  - `N_j/φ(N_j)` increases in `j`, so `n/φ(n) ≤ N_{k_1}/φ(N_{k_1}) ≤ e^γ g(y_1)` by Case A, where `p_{k_1}` is the least prime `≥ x_1` and `y_1 = θ(p_{k_1})`.
  - This is at most `e^γ g(L)` once `L ≥ L_1 := y_1`.
  - `y_1` is computed exactly when `x_1 < 10^7`. Otherwise we use `y_1 ≤ x_1(1+η) + log(2x_1)` (Bertrand). ∎

**Table R** (interval-verified; all entries rounded in the safe direction; `c_U` is the upper-side constant, and the two-sided Nicolas constant came out equal in every row):

| `C` | `log x_1` | `x_1` | `c_U` | `log n_1 = L_1` | sharper than Robin's R2 for `n ≥ n_1`? |
|---|---|---|---|---|---|
| 1.41 | 8.42 | 4 537 | 0.7579 | 4462.69 ≥ θ(4547) | no |
| 1 | 9.47 | 12 965 | 0.5467 | 12 840.4 ≥ θ(12967) | no |
| 0.5 | 11.68 | 1.18·10^5 | 0.2777 | 117 744.8 ≥ θ(118189) | no |
| 0.1 | 17.04 | 2.51·10^7 | 0.05589 | 2.520·10^7 | yes |
| 0.01 | 24.68 | 5.23·10^{10} | 5.597·10^{−3} | 5.230·10^{10} | yes |
| 10^{−3} | 32.05 | 8.30·10^{13} | 5.602·10^{−4} | 8.302·10^{13} | yes |
| 10^{−4} | 39.23 | 1.09·10^{17} | 5.603·10^{−5} | 1.090·10^{17} | yes |
| 10^{−6} | 59.88 | 1.01·10^{26} | 5.606·10^{−7} | 1.013·10^{26} | yes |
| 10^{−8} | 200.76 | 1.55·10^{87} | 5.614·10^{−9} | 1.546·10^{87} | yes |
| 10^{−10} | 263.76 | 3.54·10^{114} | 5.568·10^{−11} | 3.545·10^{114} | yes |

How to read Table R.
- **`C = 1.41` (ROBIN_GRADED's constant) holds for all `n ≥ e^{4462.69}`.** The threshold is small because for `p_k ≤ 2.169·10^25` Büthe's RH-quality bounds control everything. H(7/8) enters only through zeros above `H_0`, whose total weight is `s_high ≈ 3·10^{−12}`. The dominant term in `c_U` at small `x_1` is the crude Chebyshev bound for `J_0`.
- **`C` can be made very small.** As `n_1 → ∞`, `C` can go down to `e^γ s_high (1+o(1)) ≈ 5.3·10^{−12}`. The jump between the `10^{−6}` and `10^{−8}` rows is a bookkeeping artifact. It comes from the second-order term `S²` in regime II (`T = H_0`), where `S/x^{1/2}` grows like `x^{1/2}/H_0`. A per-`x` choice of `T` would smooth it.
- **Comparison with R2** (Robin's unconditional `σ(n)/n < e^γ log log n + 0.6483/log log n`, which ROBIN_GRADED quotes secondhand via Lagarias). From `log n ≈ 2.5·10^7` the explicit conditional envelope is sharper. This replaces ROBIN_GRADED's calibration ("only once `log log n ≳ 35`"), which used only `C = 0.79`. Robin's inequality itself is known numerically far beyond these `n` (Morrill–Platt, not imported). So for the repository the new content starts only above that verified range.

**Corollary S1 (explicit pruning rule).** In the setting of Theorem R, suppose `log n ≥ y_1 e^{c y_1^{−1/8}}` (the column `log_n1_S1` in results JSON; for example 5886.50 for `C = 1.41`). If `σ(n) ≥ e^γ n log log n`, then:
- `p_{ω(n)} ≥ x_1`;
- `log(n/N_{ω(n)}) < c e^c (log n)^{7/8}`.

*Proof.*
- Case B would force `L < y_1 e^{c y_1^{−1/8}}`.
- In Case A, `log L ≤ log y + c y^{−1/8}`, so `L − y ≤ y(e^{c y^{−1/8}} − 1) ≤ c e^c L^{7/8}`. ∎

**What of ROBIN_GRADED is and is not made explicit here.**

| ROBIN_GRADED item | Status here |
|---|---|
| Prop. R (upper envelope), Prop. N (primorials), (S1) | explicit (Theorem R, Proposition N, Corollary S1) |
| Lemma K via Ingham's `ψ_1` formula (I1), constant `17A ≤ 0.79` | not used. Ingham's book was not re-verified. Lemma J replaces it, through CHJ |
| Remark K′ (sharper constant, "sketch") | made explicit in Lemma J, with explicit truncation error `8M x^{−1/2}` |
| I2 (Perron, pointwise `x^θ log² x`) | explicit: Theorem 1 |
| (S2) (small primes divide a violator) | not done (time); the same bookkeeping applies |
| Theorem V lower half (R3, N3: Ω-results when RH fails) | not explicit. The Ω-statements as quoted (Lagarias for Robin; Nicolas 1983 via Nicolas 2012) carry no constant or threshold. They come from a Landau-type oscillation argument, which is ineffective as stated |
| §5.3 (sign at colossally abundant numbers) | not done, and not reachable by this route. It needs the error in `J` to be `o(1/(√x log x))`. CHJ allows only `T < x^{1/2}/2`, so its truncation error is about `51 x^{−1/2}`, larger than the RH margin `0.78/(√x log x)`. The untruncated identity `J = −Σ_ρ F_ρ/ρ − J_1` with `0 < J_1 ≤ log(2π)/(x log x)` (quoted in Ni's proof of Lemma 2.5 from Nicolas 1983 (17)–(19)) would suffice. Its unconditional status was not checked at source |

## 6. Comparison with unconditional explicit bounds (COMPARISON)

Below, "ours" means the bound (3.1)/(3.2) with the best `T` from a candidate grid; each candidate is a rigorous bound. The other columns are transcribed table values: FKS Table 3 (`ε_θ = ε_ψ` after their rounding) and Johnston–Yang Theorem 1.1, `9.39 (log x)^{1.515} e^{−0.8274√log x}`.

| `log x` | ours, `\|ψ−x\|/x ≤` | FKS Table 3 | JY Thm 1.1 (closed form) |
|---|---|---|---|
| 100 | 2.1·10^{−10} (no H(7/8) used) | 2.0·10^{−12} | 2.6 |
| 200 | 2.8·10^{−10} | 1.77·10^{−12} | 0.24 |
| 250 | 2.3·10^{−12} | 1.72·10^{−12} | 0.084 |
| 260 | 7.6·10^{−13} | 1.72·10^{−12} | 0.069 |
| 300 | 8.3·10^{−15} | 1.69·10^{−12} | 0.032 |
| 500 | 4.3·10^{−25} | 1.63·10^{−12} | 1.1·10^{−3} |
| 1000 | 1.3·10^{−51} | 1.59·10^{−12} | 1.4·10^{−6} |
| 3000 | 3.1·10^{−159} | 5.0·10^{−15} | 3.6·10^{−14} |
| 10000 | 3.4·10^{−538} | 1.4·10^{−30} | 1.3·10^{−29} |

**Crossover.**
- **ψ.** For every integer `log x` from 253 to 300, our bound is below FKS's step value. Beyond 300 the gap only widens: ours decays like `x^{−1/8}`, theirs like `exp(−c√log x)`. So the H(7/8)-conditional ψ bound beats the best published unconditional one from about `x ≈ e^{253} ≈ 10^{110}`.
- **π − li.** Corollary 3's shape beats FKS Table 4 from `log x ≈ 259`.
- **Against JY's closed forms**, including the Vinogradov–Korobov one (Thm 1.4), the crossover is trivial (`log x = 41`), because those forms are weak at small `x`.

**Why there is a floor.** Unconditional tables stall near `1.6·10^{−12}` for `70 ≲ log x ≲ 2000`. Zeros above `H_0` may lie close to `Re s = 1` unconditionally, and their total weight is about `1/H_0`. H(7/8) removes that floor, which is the whole explicit gain. Below `log x ≈ 190` our bound is unconditional and weaker than FKS, which uses Büthe's smoothed method with the same `H_0`.

## 7. What was run

- **Main run.** `python3 -I scripts/explicit_pnt_7_8.py` (`nice -n 10`, one core, about 17 s; Python 3.13, mpmath 1.3.0, sympy 1.14.0).
  - All claimed constants come from `mpmath.iv` at 128 bits with outward rounding. Literature constants are entered as decimal strings and enclosed exactly. Only safe endpoints are compared.
  - Monotonicity facts (listed in the proofs) reduce "for all x" to finitely many evaluations. Elsewhere the script uses naive interval evaluation over whole cells, which is itself rigorous.
  - Exact enumeration of `ψ(n)` and `θ(n)` for `n ≤ 1500`.
  - sympy checks of the four integration identities used: Ni (2.2), (2.6), `∫_x^∞ w = 1/(x log x)`, and the antiderivative of `P/t²`.
- **Optional `--zeros`.** EMPIRICAL float check with `mpmath.zetazero` for the first 200 zeros: `Σ 2/(1/4+γ²) = 0.04207` (below `s_low`) and `Σ 1/γ = 1.352` (below the (Z1) bound 2.031).
- **Outputs.** `results/explicit_pnt_7_8.txt`, `results/explicit_pnt_7_8.json` (from the `--zeros` run, 45 s).
  sha256: script `f13f8787e0d7b3f7…`, txt `4daf86cae016b77d…`, json `8b67201826ba95c4…`.
- **Not done.**
  - Interval evaluation of `li` (so `π − li` below 2657 is not covered).
  - The `x^{7/8} log x log log x` short-interval refinement.
  - (S2).
  - Any independent re-derivation of the imported theorems.

## 8. Misreadings to avoid

- **Nothing here is about RH.** Every bound is a consequence of `β ≤ 7/8` plus finite verification. It does not approach the critical line.
- **Theorem R bounds the size of a Robin violation; it does not exclude one.** The sign question at the RH scale `(log n)^{−1/2}` is untouched (Sec. 5, last table row).
- **The thresholds are not new verification ranges.** For `x ≤ e^{190}` Theorem 1 is unconditional and weaker than published tables. The small `n_1` for `C = 1.41` reflects Büthe's imported finite range, not new information about zeros.
- **"Explicit" means explicit modulo the imports.** CHJ's Theorem 1.2 is load-bearing beyond `e^{190}` (Theorem 1) and beyond `2.169·10^25` (Lemma J). Its own constants changed between arXiv versions, and its text and Table 4 disagree.
- **Smallest statement whose failure would break the results.** Theorem 1 beyond `e^{190}` breaks only if CHJ Thm 1.2 failed at `log x ≥ 40` by more than a factor of 4 in `M`. Theorem R with `x_1 < 2.169·10^25` breaks if Büthe's Theorem 2 failed in that range.

## Addendum: independent sweep of the small-x ranges (coordinator, same day)

`scripts/explicit_pnt_sweep_check.py` is a separate float64 check (EMPIRICAL, not interval
arithmetic) of the step functions ψ and θ at every prime-power jump up to `2·10⁷`. At each jump it
checks both the left limit and the right value, against the claimed bound on the claimed range
(`results/explicit_pnt_sweep_check.txt`):

* ψ, `x ≥ 227`, `C = 0.0026`: the largest ratio is 0.00196 (the left limit at 347). OK.
* θ, `x ≥ 967`, `C = 0.0026`: the largest ratio is 0.002595 (the left limit at 1009). OK, but
  tight.

Just below the thresholds the bounds fail, as expected: the left limit at 227 has ratio 0.00298.
This is consistent with "227" and "967" being the smallest workable starting points.

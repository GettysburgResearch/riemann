# PR 910 native-height route: falsification test of the curve condition

```text
Status: FALSIFICATION TEST (EMPIRICAL / analytic) of a PROPOSED sufficient condition in PR 910
Scope: the one-sided off-diagonal condition O_Y(sigma;T) < 1/(12 Omega) of NATIVE_HEIGHT.md §6,
       required for every sigma in [sigma_0(Y), 1), with sigma_0(Y) = 1/2 + c loglogY/logY (c > 2),
       Y = ceil(4(T+2)), "for all large T". Verdict: NOT FALSIFIED in the tested range. The
       condition is heuristically expected to FAIL for every fixed c at astronomically large T.
       That expectation is a heuristic plus an RH-conditional reduction, not a proof. No RH claim.
Exact sources or dependencies: PR 910 head pr910 = 670a76c1a3a8f325c43c1755b1cfc24d313a3e3c,
       standalone/2026-10-10-quasi-riemann-height-descent/{NATIVE_HEIGHT.md,
       checks/check_native_height.py, results/check_native_height.json}; literature in §7.
What was actually run: replay of PR 910's exact checker (identical JSON); float64 numpy
       evaluation of G_Y, B_Y, R_Y, d_t R_Y and of E_Y by 8-point Gauss-Legendre quadrature;
       exact-integer sieve and Monte Carlo values of D_Y; mpmath (20-30 digit) spot checks.
       Scripts: scripts/pr910_height_scan.py; outputs: results/pr910_*.json.
Smallest remaining gap: a lower bound ("noise floor") for the Moebius tail
       sum_{n>Y} mu(n) n^{-s} at large values of zeta on the curve (§5.3). That bound plus
       Proposition A (RH) would give a conditional disproof. Nothing here is certified;
       ordinary floating point is reconnaissance.
```

## 0. Verdict (outcome (b), with a mechanism finding)

1. **Not falsified in the tested range.** On the PR's curve with `c = 2`, the statistic `12·Ω·E_Y(σ₀(Y);T)` never exceeded **0.121** in any run. That is at least 8× below the level 1 at which the condition could fail; in terms of `|R_Y|` the margin is about 3×. The maximum came from the targeted run at `T=735838.36`; the systematic scans to `T≈10⁵` never exceeded 0.0692. The curve for `c = 2` contains every curve with `c > 2`, so this covers all admissible `c`. The tested heights were:
   - every integer `Y ∈ [5684, 20000]`, three heights each, so `T ∈ [1418.75, 4998]`;
   - 1,199 sampled `Y` up to `4·10⁵`, so `T ≤ 99,899`;
   - targeted extreme-value heights up to `10⁶` (§4.4).

   Since `𝒪 = ℰ − 𝒟` with `𝒟 ≥ 0`, this shows, in ordinary floating point (not certified), that `𝒪 < 1/(12Ω)` at every point evaluated.
2. **The finite range cannot decide the question.** At these heights the curve lies at `σ₀ ∈ [0.85, 1.0]`, far from 1/2 (table in §3). The curve reaches `σ = 0.75` only at `Y ≈ 4·10¹¹`, and `σ = 0.6` only at `Y ≈ 10⁴⁰`. A positive run here is not evidence for the asymptotic condition.
3. **Mechanism (supports the P5 conjecture in a refined form).** Off the curve, at fixed `σ = 0.7` and `0.75`, the energy exceeds the PR threshold at large values of ζ, and not near small values or zeros:
   - `σ = 0.7`, `T = 30775.1`: `12Ω·ℰ = 23.08` (`|ζ| = 10.48`, `|R_Y| = 0.820`);
   - `σ = 0.75`, same `T`: `12Ω·ℰ = 4.95`, with `12Ω·𝒟 ≈ 0.21`;
   - at the 15 smallest-|ζ| candidates, the maximum is 0.995 at `σ = 0.7` and 0.244 at `σ = 0.75`.

   At large values, the data fit `|R_Y(σ+it)| ≈ κ·|ζ(σ+it)|·Y^{1/2−σ}` with `κ = O(1)`. At each run's top point `κ ≈ 0.8–1.1` across `σ ∈ {0.6, 0.7, 0.75, 0.9, 0.98}`, with 1.8 at `T=735838`; other large-value candidates go down to about 0.2. On the curve, `Y^{1/2−σ₀} = (log Y)^{−c}` is only polylogarithmic, while Ω-values of ζ grow like `exp(√(log T/log log T))`. Hence the heuristic expectation of eventual failure for every fixed `c` (§5). The heuristic onset is `log T ≈ 10³–10⁴`.
4. **Nothing in PR 910 is contradicted.** The PR states that the off-diagonal is *not* claimed small (lines 458–460, 489). The finding concerns the viability of the route, not a false claim.

## 1. Exact objects (quoted from `pr910:…/NATIVE_HEIGHT.md`, with line numbers)

* Lines 156–160: `G_Y(s)=Σ_{a≤Y} μ(a)a^{-s}`, `B_Y(s)=Σ_{b≤Y} b^{-s}`, `R_Y(s)=G_Y(s)B_Y(s)−1`.
* Lines 162–171 and 181: `R_Y(s)=Σ_{Y<n≤Y²} e_Y(n)n^{-s}`, with `e_Y(n)=Σ_{ab=n, a,b≤Y} μ(a) − 1_{n=1}`. Here `e_Y(n)=0` for `n≤Y`, and `e_Y(n)=−1−μ(n)` for `Y<n≤2Y`.
* Lines 272–277, (E): for `Y ≥ 2(|t|+1)`, `ζ(s)=B_Y(s)+Y^{1−s}/(s−1)+r_Y(s)` with `|r_Y|≤2Y^{−σ}`.
* Lines 321–341, (Z): at a zero `ρ=β+iT`, `|R_Y(ρ)+1| ≤ H_Y[Y^{2−2β}/|T|+2Y^{1−2β}]`. With `Y=⌈4(T+2)⌉` (line 335) this forces `|R_Y(ρ)|≥1/2` for large `T`.
* Lines 349–358: `Ω=2 log Y`, `h=Ω^{-1}`, and
  `ℰ_Y(σ;T)=∫_{T−h}^{T+h}(|R_Y(σ+it)|²+Ω^{−2}|∂_tR_Y(σ+it)|²)dt`.
* Lines 361–374: a Sobolev inequality, `|f(T)|² ≤ (3Ω/2)∫(|f|²+Ω^{−2}|f'|²)`, gives (P): a zero with `|R_Y(ρ)|≥1/2` forces `ℰ_Y(β;T) ≥ 1/(6Ω)`.
* Lines 416–435: `a_n=e_Y(n)n^{−σ}`, `δ_mn=log(n/m)`, `ℰ_Y=𝒟_Y+𝒪_Y`, where
  `𝒟_Y(σ)=2hΣ_n a_n²(1+(log n)²/Ω²)` and
  `𝒪_Y(σ;T)=4Σ_{Y<m<n≤Y²} a_m a_n (1+log m log n/Ω²) cos(Tδ_mn) sin(hδ_mn)/δ_mn`.
* Lines 452–456 (**the sufficient condition**): *"For all sufficiently large Y, the diagonal is at most 1/(12Ω). Hence, under the zero-detection size condition (Z), a sufficient one-sided estimate to exclude a zero at height T throughout a real-part interval is 𝒪_Y(σ;T)<1/(12Ω) for every σ in that interval, with the same Y and all endpoint hypotheses retained."*
* Lines 464–467: `δ_Y=c log log Y/log Y`, `σ₀(Y)=1/2+δ_Y`, `c>2`. Lines 476–484: `Ω𝒟_Y(σ) ≤ (512/(c log 2))(log Y)^{4−2c}/log log Y`, and the (Z) error is `O_c((log Y)^{1−2c})`, uniformly for `σ≥σ₀(Y)`.
* Line 489: *"We have therefore **not** proved a zero-free boundary of this shape."*

### 1.1 Logical form

Write `(H_T)` for the statement: with `Y=⌈4(T+2)⌉`, `𝒪_Y(σ;T)<1/(12Ω)` for every `σ∈[σ₀(Y),1)`.

PR 910 proves the implication `(H_T) ⇒ ζ(β+iT)≠0 for all β∈[σ₀(Y),1)` for every `T ≥ T_*(c)`. Here `T_*(c)` is large enough that `Ω𝒟_Y ≤ 1/12` and the right side of (Z) is at most 1/2. The proof uses `ℰ=𝒟+𝒪 < 1/(6Ω)`, which contradicts (P).

The "route" is therefore: `(H_T)` for all large `T` would give a zero-free region `β < 1/2 + c log log(4T+9)/log(4T+9)`. That is quasi-RH strength, far beyond Vinogradov–Korobov.

Two consequences used below:

* **Pointwise form.** `(H_T)` together with the Sobolev step gives `|R_Y(σ+iT)|² ≤ (3Ω/2)(𝒟+𝒪) < 1/8 + (3/2)Ω𝒟_Y`. So for large `T` the condition forces `|G_YB_Y−1| < 0.354+o(1)` at every point of the region `σ≥σ₀(Y(T))`. It is an `L^∞` mollification statement with a sharp-cutoff Möbius mollifier of length `Y≈4T`. All known mollifier theorems (Selberg, Levinson, Conrey) are `L²`/`L¹` statements.
* **The diagonal is harmless; its proved majorant is not effective.** Measured values are given in §4.2. The PR's explicit bound makes `Ω𝒟 ≤ 1/12` only at absurd sizes: for `c=2.01` it needs roughly `log log Y·(log Y)^{0.02} > 4400`. The reason is that the chain `|e_Y(n)|²≤d(n)²≤d_4(n)` replaces the true mean `E[e_Y(n)²] ≈ 0.417` by `L_Y³`. At `Y=8000` the PR majorant of `𝒟` exceeds the exact `𝒟` by a factor of about `3·10⁴` (§4.2). This is not a misstatement, since the PR says "sufficiently large".

## 2. PR 910's own checker (replayed)

`git show pr910:…/checks/check_native_height.py` was read in full. It is pure `Fraction`/Gaussian-rational arithmetic with no zeta evaluation (sha256 `16109d37…8bbbe8`). It was run with `python3 -I` from a scratch copy.

The output is **byte-identical as parsed JSON** to `results/check_native_height.json`: `PASS`, 29,785 explicit predicates, about 11 s. The checker authenticates finite coefficient identities only: the Newton step, `e_Y` support, the collar identity, and the mesh budget. It says nothing about `ℰ, 𝒟, 𝒪` at physical heights, as its own `not_run` field states.

## 3. Where the curve lies at computable heights (`c=2`, the most permissive admissible curve)

| Y | 5.7·10³ | 10⁴ | 4·10⁴ | 4·10⁵ | 4·10⁶ | 4·10⁸ | 10¹² | 10²⁰ | 10⁴⁰ | 10¹⁰⁰ |
|---|---|---|---|---|---|---|---|---|---|---|
| σ₀(Y), c=2 | 0.999 | 0.982 | 0.946 | 0.897 | 0.858 | 0.802 | 0.740 | 0.666 | 0.598 | 0.547 |
| σ₀(Y), c=2.5 | 1.12 | 1.10 | 1.06 | 0.996 | 0.948 | 0.877 | 0.800 | 0.708 | 0.623 | 0.559 |

* For `c=2`, the interval `[σ₀(Y),1)` is empty when `Y<5684`, i.e. `T<1418.75`. For `c=2.5` it is empty for `Y ≲ 3.3·10⁵`, i.e. `T ≲ 8·10⁴`.
* The low-lying zeros, and everything below `T≈1419`, are therefore outside the condition's domain.
* The Lehmer pair at `γ = 7005.0629, 7005.1006` sits at horizontal distance `≥0.45` from the curve.
* At σ₀, the (Z) right-hand side is at most 0.01 throughout the range, so the detector is "armed": any zero on or right of the curve would force `12Ω·ℰ ≥ 2`.

## 4. Numerics (float64 reconnaissance; spot-checked in mpmath)

Throughout, the reported statistic is **`ratio = 12·Ω·ℰ_Y(σ;T)`**. Since `12Ω𝒪 = ratio − 12Ω𝒟`, the condition can fail only where `ratio ≥ 1`.

### 4.1 Validation (`results/pr910_validate.json`, `pr910_mpcheck.json`)

* **Two computations of `R_Y`.** `G_YB_Y−1` and the direct sum `Σ e_Y(n)n^{−s}` (with `e_Y` from an exact integer sieve) agree to `≤2.8·10⁻¹⁴` at `Y∈{12,30,60}`.
* **Two computations of `ℰ`.** The 8-node Gauss–Legendre `ℰ_Y` equals `𝒟_Y+𝒪_Y` evaluated termwise from the PR formula (O). The relative difference is `≤3.2·10⁻¹³` in all 9 cases. This confirms the PR's exact formula (O), including the `1+log m log n/Ω²` weight and the `4·Σ_{m<n}` normalization.
* **The Euler remainder in (E).** `|ζ − B_Y − Y^{1−s}/(s−1)|` equals `0.25×(2Y^{−σ})` at every check point, i.e. about the half-endpoint term `Y^{−σ}/2`. So (E) holds with room.
* **mpmath recomputation.** An independent 20-digit mpmath recomputation of `G_Y`, `B_Y` and ζ was run at 6 key points (`pr910_mpcheck.json`, `pr910_mpcheck_1e6.json`). These include the on-curve maximum, `Y=2943362`, `T=735838.360004`, where mpmath gives `|R_Y|=0.0607066` and `|ζ|=7.5124`. At every point mpmath matches float64 `|R_Y|` to `≤2.4·10⁻¹⁰`.

### 4.2 The diagonal (`results/pr910_dtable.json`, `pr910_dmc.json`)

The exact sieve (`n≤Y²`, up to `Y=8000`) gives `mean e_Y(n)² over (Y,Y²] = 0.416–0.417` for all tested `Y`, and `max|e_Y| = 10–20`.

| Y | σ | 12Ω·𝒟 (exact sieve) | 12Ω·𝒟 (Monte Carlo, 4–6k samples) | PR majorant of 𝒟 |
|---|---|---|---|---|
| 8000 | 0.9887 (=σ₀) | 0.00628 | 0.0063 ± 0.0001 | 0.99 |
| 8000 | 0.75 | 0.808 | 0.803 ± 0.018 | 121 |
| 11286 | 0.9787 (=σ₀) | — | 0.0055 ± 0.0001 | — |
| 389029 | 0.8970 (=σ₀) | — | 0.0017 ± 0.0000 | — |
| 123109 | 0.70 | — | 0.820 ± 0.022 | — |
| 123109 | 0.75 | — | 0.213 ± 0.008 | — |

On the curve the diagonal uses under 1% of the budget.

### 4.3 Along the curve (`results/pr910_curve_c2.json`)

| block | points | T range | max ratio | median | 99% | 99.9% |
|---|---|---|---|---|---|---|
| every integer Y ∈ [5684, 20000], 3 T each | 42,951 | 1418.75–4998 | **0.0692** | 0.0011 | 0.0187 | 0.047 |
| 1,199 log-uniform Y ∈ (2·10⁴, 4·10⁵] | 1,199 | 5012–99,899 | 0.0275 | 0.00058 | 0.0117 | 0.0239 |

* **Where the maximum sits.** It is at `Y=11286`, `T=2819.5`, `σ₀=0.978684`. There `|ζ|=3.670`, `|R_Y|=0.0461`, `|G_Y|=0.265`, and `12Ω𝒟≈0.0055`.
* **The sampled row.** It is from `results/pr910_curve_c2_sampled_only.json`, a rerun of the same seeded sample alone. The combined run reports only its top 20, all of which have `T<3900`.
* **σ-dependence.** On 62 sub-sampled heights, an 8-point σ-grid on `[σ₀,0.999]` always put the maximum of `ℰ` at `σ=σ₀`; the largest grid ratio was 0.0117. So `σ=σ₀` is the binding end, as expected.

### 4.4 Targeted extreme values on the curve (`results/pr910_resonance_c2*.json`)

**Method.** Heights were selected by extremizing the small-prime Euler factor `Π_{p≤31}|1−p^{−σ₀−it}|^{−1}` on a 0.02-grid. At each selected height, `T` was scanned over ±0.5 with the true `Y(T)`.

* **`T∈[1400,10⁵]`, 25 large and 25 small candidates.**
  - Large values (`|ζ(σ₀+iT)|` up to 6.18): max ratio **0.0303**, at `T=97255.0`, `Y=389029`, `|ζ|=5.957`, `|R|=0.0304`.
  - Small values (`|ζ|` down to 0.254): max ratio 0.0070.
* **`T∈[10⁵,10⁶]`, 8 + 8 candidates** (`results/pr910_resonance_c2_1e6.json`; about 14 min).
  - Large values (`|ζ(σ₀+iT)|` up to 8.34): max ratio **0.1214**, the largest seen anywhere on the curve. It is at `T=735838.360004`, `Y=2943362`, `σ₀=0.862675`, with `|ζ|=7.51`, `|R_Y|=0.0607` and `|R|/|ζ|=0.0081`. The other 7 large candidates have ratios 0.0018–0.0164.
  - Small values (`|ζ|` down to 0.223): max ratio 0.0047.
  - A ±0.6 profile at step 0.05 around the maximum (`results/pr910_points_735838.json`) is smooth and single-peaked; its maximum is 0.1214.
* **Lehmer pair** `T=7005.0629/7005.0817/7005.1006`, on the curve (`σ₀=0.9543`): ratio 0.0090–0.0096.

Even on the curve, large values dominate. In the `T∈[1400,10⁵]` run, the median ratio is 0.0132 at the large-|ζ| candidates against 0.0013 at the small-|ζ| ones. The ratio `|R|/|ζ|` at large values is 0.004–0.005 (at `Y≈4·10⁵`) and 0.0125 (at `Y≈1.1·10⁴`). Compare `Y^{−δ}=(log Y)^{−2}`, which is 0.006 and 0.0115 respectively.

**What the ratio means for `|R_Y|`.** At the observed on-curve peaks, `ratio ≈ 33·|R_Y(σ₀+iT)|²`: 32.6, 32.8 and 32.9 at the three maxima. So the E-based failure level `ratio=1` corresponds to a local peak `|R_Y| ≈ 0.17`. That is tighter than the Sobolev-implied pointwise bound 0.354 of §1.1. The largest observed peak, `|R_Y|=0.061`, is about 2.8× below it.

### 4.5 Mechanism off the curve (`results/pr910_mechanism_hi.json`, `pr910_resonance_sigma0{6,7,75}.json`, `pr910_points.json`)

**Random heights.** 1,200 uniform `t∈[2·10⁴,10⁵]` were sampled, each with its own `Y(t)`. The fitted slope of `log|R_Y|` on `log|ζ|` is 0.28–0.35 at every σ (0.55, 0.6, 0.7, 0.8, σ₀). In the top-|ζ| bins, `median|R|/|ζ|` stops decreasing:

| σ | \|R\|/\|ζ\| by \|ζ\|-quantile bin (0–50%, 50–90%, 90–99%, 99–100%) |
|---|---|
| 0.7 | 0.085, 0.044, 0.032, 0.034 |
| 0.8 | 0.021, 0.012, 0.009, 0.010 |
| σ₀ | 0.0047, 0.0028, 0.0022, 0.0026 |

So `G_Y` tracks `1/ζ` only down to a floor. Beyond it, `|R_Y|` grows in proportion to `|ζ|`.

**Targeted heights**, `T∈[10⁴,6·10⁴]`, 15 large-|ζ| and 15 small-|ζ| candidates per σ:

| σ | large-\|ζ\| candidates: max / median ratio, # > 1 | small-\|ζ\| candidates: max / median ratio, # > 1 | 12Ω𝒟 at Y≈1.2·10⁵ | \|R\|/\|ζ\| at the top point vs Y^{1/2−σ} |
|---|---|---|---|---|
| 0.75 | 4.95 / 1.43, 10 of 15 | 0.244 / 0.065, 0 of 15 | ≈0.21 | 0.043 vs 0.053 |
| 0.70 | 23.08 / 5.83, 12 of 15 | 0.995 / 0.232, 0 of 15 | ≈0.82 | 0.078 vs 0.096 |
| 0.60 | 530 / 134, 15 of 15 | 50.5 / 3.6, 15 of 15 | 15.3 ± 0.6 (the diagonal alone exceeds the budget) | 0.262 vs 0.31 |

**The cleanest exhibit.** At `T=30775.1`, `Y=123109`, `σ=0.7`, `ζ` takes a large value (`|ζ|=10.477` in mpmath) and the polynomials give `|R_Y|=0.8202`. That point has:
* `12Ω·ℰ = 23.08`;
* `12Ω·𝒪 ≈ 23.08 − 0.82 ≈ 22.3`;
* a pointwise value `|R_Y|=0.82`, more than twice the 0.354 that `(H_T)` would force.

Compare the Lehmer pair at the same σ: `12Ω·ℰ ≈ 1.9`, with `|ζ|=0.23`.

None of these points lies on the PR curve. At these heights `σ₀≈0.92`, and `σ=0.7` is reached by the `c=2` curve only near `Y≈3·10¹⁵`. The exhibit shows that the detector cannot tell a large value from a zero: it is large values, not zeros, that push `ℰ` over `1/(6Ω)`.

## 5. Analysis: why the curve condition should eventually fail, and what is actually proved

### 5.1 Empirical law at large values

Across `σ∈[0.6,0.98]` and `Y∈[10⁴,4·10⁵]`, the measurements fit

`|R_Y(σ+it)| ≈ κ·|ζ(σ+it)|·Y^{1/2−σ}` at large values of ζ.

Here `κ` is an O(1) fluctuating factor, not a constant. It is `0.8–1.1` at each run's top-ratio point and `1.8` at the on-curve maximum `T=735838`. Among the other on-curve large-value candidates at `T∈[10⁵,10⁶]` it lies in `0.2–0.7`. The sizes of `|ζ|` and of the noise both matter.

**A model explanation (heuristic).** Factor `μ = μ_X * μ_rough`, splitting at the small primes `p≤X` that create a large value. Under RH write `T_Y:=Σ_{n>Y}μ(n)n^{−s}=1/ζ−G_Y`. Then

`ζT_Y ≈ ζ_rough·[ T^{rough}_Y + ∫ dW(v)·(1−ζ_X S_X(v)) ]`.

Here:
* `S_X(v)=Σ_{a≤e^v, a X-smooth}μ(a)a^{−s}`;
* `W(v)=Σ_{Ye^{−v}<m≤Y} μ_rough(m)m^{−s}` is the rough partial-sum increment near the cutoff.

For small `v`, `1−ζ_XS_X(v)≈1−ζ_X`. So the sharp cutoff at `Y` lets the full size of the Euler-product resonance `ζ_X` multiply boundary noise of size `Y^{−δ}`. This term is absent only if `G_Y` were cut off smoothly in the smooth part. That gives `|R_Y| ≈ |ζ|·Y^{−δ}·O(1)` once `|ζ_X|² ≫ 1/δ`, consistent with the measured slope rising toward 1 in the top bins.

### 5.2 Proposition A (rigorous modulo cited theorems; RH-conditional)

**Statement.** Assume RH. Fix `c>2`, and suppose `(H_T)` holds for all `T≥T₀`. Then there are `t_k→∞` with `Y_k=⌈4(t_k+2)⌉` such that

`|G_{Y_k}(σ₀(Y_k)+it_k)| ≤ exp(−(1+o(1))√(log t_k/log log t_k))`

and the same bound holds for the Möbius tail `|Σ_{n>Y_k}μ(n)n^{−σ₀−it_k}|`.

**Proof.**
1. **The condition gives a pointwise bound.** By §1.1 and the PR's bound `Ω𝒟_Y→0` (lines 476–480), `(H_T)` gives `|R_Y(σ₀+iT)|≤0.36` for large `T`. Hence `|G_Y| ≤ 1.36/|B_Y|`.
2. **Large values on the critical line.** Soundararajan's resonance theorem (unconditional) gives `t_k∈[T_k,2T_k]` with `|ζ(1/2+it_k)| ≥ exp((1+o(1))√(log T_k/log log T_k))`.
3. **Transfer to the curve.** Under RH, `|ξ(σ+it)|` is nondecreasing in `σ≥1/2`, because each Hadamard factor `|s−ρ|` with `Re ρ=1/2` is. Stirling then gives `∂_σ log|ζ| ≥ −½log(|s|/2π) − O(t^{−2})`. Hence `|ζ(σ₀+it)| ≥ |ζ(1/2+it)|·(t/2π)^{−δ/2}(1−o(1)) ≥ |ζ(1/2+it)|(log Y)^{−c/2}(1−o(1))`.
4. **From ζ to `B_Y`.** By (E), `|B_Y−ζ| ≤ Y^{1−σ}/|s−1|+2Y^{−σ} = O(t^{−1/2})`.
5. **Combine.** Steps 1–4 give the bound on `G_Y`. Under RH, `Σμ(n)n^{−s}` converges to `1/ζ(s)` for `σ>1/2` (Titchmarsh §14.25), so the bound passes to the tail. ∎

### 5.3 The missing step, and the heuristic onset

**The missing step.** A *noise-floor lemma* would close the argument: at infinitely many such `t_k`, the Möbius tail is at least `exp(−(1−ε)√(log t_k/log log t_k))`. With Proposition A, that gives a disproof of the curve condition under RH.

If RH fails with infinitely many zeros right of the curve, the condition fails anyway, by PR 910's own (P) for large `T`. The residual case has zeros only in `(1/2,σ₀)`. There the monotonicity in step 3 can fail, and one would need resonance lower bounds valid uniformly at `σ−1/2 = c log log T/log T`. Published uniform ranges, e.g. Bondarenko–Seip 2018, were *not* checked to reach that close.

**Why the lemma is expected.** The typical size of the tail is `≍ Y^{−δ}=(log Y)^{−c}`. That matches the measured `|R|/|ζ| ≈ (log Y)^{−2}` on the curve, §4.4. The lemma asks only that, at the resonance heights, the tail not be smaller than typical by a further factor `exp(−√log t)`. The resonance is a small-prime event; the tail is dominated by `n` near the cutoff `Y`. No mechanism correlating them is known.

**Proving it is out of reach here.** A resonance mean of `|R_Y|²` needs off-diagonal control for a Dirichlet polynomial of length `Y²≈16T²` twisted by a resonator. That is beyond current twisted-moment technology.

**Heuristic onset.** Failure needs `κ·max|ζ(σ₀+it)|·(log Y)^{−c} ≳ 0.17` (E-based; 0.354 pointwise):
* with the RH transfer above: `√(log T/log log T) ≳ (3c/2)log log T`, i.e. `log T ≈ (9c²/4)(log log T)³ ≈ 6·10³` for `c=2`;
* with Montgomery-scale values at `σ₀` directly (`log|ζ| ≈ (log T)^{1−σ₀}/((1−σ₀)log log T)`): `log T ≈ 5·10³`.

Either way the onset is `T ≈ 10^{2000}`–`10^{3000}`, hopelessly beyond computation. At `T ≤ 10⁶` the required `|ζ(σ₀+it)| ≳ 0.17(log Y)²/κ ≈ 13–39` (for `κ≈1`) cannot occur at `σ₀ ≥ 0.85`. The largest observed value is 8.3, at `T≈9.3·10⁵`. The largest effective `κ`, 1.8 at `T=735838`, leaves a factor of about 3.

**Where the detector could heuristically still work.** Large values only lose to the detector when `Y^{−δ} ≤ exp(−C√(log T/log log T))`, i.e. `δ ≳ (log T·log log T)^{−1/2}`. The PR's `c·log log T/log T` is closer to the line than that. At fixed `σ>1/2` the floor is a power `T^{1/2−σ}`, and the fixed-σ condition is heuristically **true** for large `T`. The off-curve failures in §4.5 (`σ=0.7, 0.75`, `T≈3·10⁴`) are therefore pre-asymptotic. They do not refute a fixed-σ route; they only show that "sufficiently large" exceeds `6·10⁴` there.

### 5.4 About the P5 conjecture

P5 conjectured that "`|R_Y|≥1/2` does not distinguish zeros from large values". That is confirmed in mechanism: §4.5 shows large values, not zeros, saturating `ℰ`.

P5's suggestion that the condition is plausibly violated in `[10³,10⁵]` is **not** borne out. The `(log Y)^{−c}` floor on the curve absorbs every large value that exists at `σ₀≥0.85`.

The condition is not equivalent to anything known to be false. It is a uniform (`L^∞`) sharp-cutoff mollification statement. Known results are `L²`, and at `θ=1` the mollifier length exceeds even the critical-line `4/7` range.

## 6. What this does and does not establish

* **Established, empirically, float64 with mpmath spot checks:** `𝒪_Y(σ;T) < 1/(12Ω)`, with margin ≥8× in `12Ωℰ` (≈3× in `|R_Y|`), at every evaluated point of the `c=2` curve, for `T≤10⁵` (sampled above `T=4998`, targeted up to `10⁶`). This is not interval arithmetic. Between grid points it is not a continuum statement.
* **Established, empirically:** the detector's energy at fixed `σ∈{0.7,0.75}` exceeds the PR threshold at large values of ζ by factors 5–23 near `T≈3·10⁴`, while it stays below it near small values and zeros.
* **Established, conditionally (Proposition A, RH):** the curve condition forces the Möbius tail to be super-polylogarithmically small at Soundararajan's resonance heights.
* **Not established:** that the curve condition fails. This is a heuristic expectation with onset near `log T~10³–10⁴`. No finite computation can test it; a proof needs the noise-floor lemma of §5.3.

## 7. Literature (cited for orientation; statements not re-verified here beyond what §5.2 uses)

* K. Soundararajan, *Extreme values of zeta and L-functions*, Math. Ann. 342 (2008). Resonance method; `max_{T≤t≤2T}|ζ(1/2+it)| ≥ exp((1+o(1))√(log T/log log T))`.
* A. Bondarenko, K. Seip, *Large greatest common divisor sums and extreme values of the Riemann zeta function*, Duke Math. J. 166 (2017); and *Extreme values of the Riemann zeta function and its argument*, Math. Ann. 372 (2018). The latter is uniform in σ near 1/2; its range was not checked against `σ₀`.
* H. L. Montgomery, *Extreme values of the Riemann zeta function*, Comment. Math. Helv. 52 (1977). RH Ω-results at fixed `σ∈(1/2,1)`.
* C. Aistleitner, *Lower bounds for the maximum of the Riemann zeta function along vertical lines*, Math. Ann. 365 (2016). Unconditional, fixed σ.
* J. Sondow, C. Dumitrescu, *A monotonicity property of Riemann's xi function and a reformulation of the Riemann hypothesis*, Period. Math. Hungar. 60 (2010). The `|ξ|` monotonicity; §5.2 uses only the one-line Hadamard-product argument.
* E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., §14.25. RH implies `Σμ(n)n^{−s}=1/ζ(s)` for `σ>1/2`.
* D. W. Farmer, S. M. Gonek, C. P. Hughes, *The maximum size of L-functions*, J. reine angew. Math. 609 (2007). Conjectural maximal order; not used quantitatively.

## 8. Reproduction (from `research/exploratory/qrh-2026-10/falsification/`)

**Script history.** `scripts/pr910_height_scan.py` (final sha256 `23cab96e…ad3e9e`) gained subcommands and options during the session: `points`, `dmc`, `mpcheck`, `--sigma`, `--skip-full`. The numerical core (`Native.eval`, `Native.energy`, the curve and resonance loops) was not changed.

**Reproducibility.** A rerun of `validate` and of a small `curve` run with the final script reproduces the earlier outputs to about `10⁻¹⁵` relative. They are not bit-identical, because BLAS summation order depends on the thread count (2 threads were used for `validate`/`dtable`, 1 thread elsewhere).

```sh
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
python3 -I scripts/pr910_height_scan.py validate            > results/pr910_validate.json
python3 -I scripts/pr910_height_scan.py dtable --ys 1000,2000,4000,6000,8000 > results/pr910_dtable.json
python3 -I scripts/pr910_height_scan.py curve --ylo 5000 --yhi 20000 --ymax 400008 --nsample 1200 > results/pr910_curve_c2.json   # ~8 min
python3 -I scripts/pr910_height_scan.py resonance --tlo 1400 --thi 100000 --P 31 --k 25 > results/pr910_resonance_c2.json        # ~4 min
python3 -I scripts/pr910_height_scan.py resonance --tlo 100000 --thi 1000000 --P 31 --k 8 > results/pr910_resonance_c2_1e6.json
python3 -I scripts/pr910_height_scan.py resonance --tlo 10000 --thi 60000 --P 31 --k 15 --sigma 0.7  > results/pr910_resonance_sigma07.json
python3 -I scripts/pr910_height_scan.py resonance --tlo 10000 --thi 60000 --P 31 --k 15 --sigma 0.75 > results/pr910_resonance_sigma075.json
python3 -I scripts/pr910_height_scan.py resonance --tlo 10000 --thi 60000 --P 31 --k 15 --sigma 0.6  > results/pr910_resonance_sigma06.json
python3 -I scripts/pr910_height_scan.py mechanism --tlo 20000 --thi 100000 --n 1200 --sigmas 0.55,0.6,0.7,0.8 > results/pr910_mechanism_hi.json
python3 -I scripts/pr910_height_scan.py points --ts 2819.5,7005.0628661749,7005.0817,7005.1005646726,30775.1,97255.000001 --sigmas 0.6,0.7 > results/pr910_points.json
python3 -I scripts/pr910_height_scan.py dmc --points '[[4000,0.75],[8000,0.9887],[8000,0.75],[8000,0.9],[11286,0.978684],[123109,0.92],[123109,0.7],[389029,0.897]]' --n 6000 > results/pr910_dmc.json
python3 -I scripts/pr910_height_scan.py mpcheck --dps 20 --points '[[11286,2819.5,0.9786839822973252],[28029,7005.0817,0.6],[123109,30775.1,0.7],[123109,30775.1,0.6],[389029,97255.000001,0.8970052500846171]]' > results/pr910_mpcheck.json
python3 -I scripts/pr910_height_scan.py dmc --points '[[123109,0.75],[57224,0.75],[220427,0.75]]' --n 4000 > results/pr910_dmc_075.json
python3 -I scripts/pr910_height_scan.py dmc --points '[[123109,0.6]]' --n 4000 > results/pr910_dmc_06.json
python3 -I scripts/pr910_height_scan.py curve --ylo 5000 --yhi 20000 --ymax 400008 --nsample 1200 --skip-full > results/pr910_curve_c2_sampled_only.json
python3 -I scripts/pr910_height_scan.py points --ts $(python3 -I -c "print(','.join('%.6f'%(735838.36+0.05*k) for k in range(-12,13)))") > results/pr910_points_735838.json
python3 -I scripts/pr910_height_scan.py mpcheck --dps 20 --points '[[2943362,735838.360004,0.862674506726492]]' > results/pr910_mpcheck_1e6.json   # ~2.5 min
```

The `σ=0.75` diagonal values quoted in §4.5 (`12Ω𝒟 = 0.213±0.008`, `0.308±0.008`, `0.146±0.004` at `Y=123109, 57224, 220427`) are in `results/pr910_dmc_075.json`.

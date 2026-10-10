# The Möbius-tail noise floor for the PR 910 curve condition

```text
Status: EXPLORATION. Proposition A of PR910_HEIGHT_TEST.md re-derived and CONFIRMED (RH).
        New, PROVED (elementary or standard under RH): a two-sided pointwise criterion (§3.2),
        a zero criterion that needs no RH (§3.3), a freezing lemma (§3.4), and a no-go
        result for linear resonance arguments (§3.5). The noise-floor lemma itself is
        NOT proved (OPEN). §4.3 is RH-conditional and partly HEURISTIC; §4.4 is a model
        theorem; §5 is EMPIRICAL (float64, not certified); §6 is HEURISTIC. No RH claim.
Scope: the sufficient condition (H_T) of PR 910 NATIVE_HEIGHT.md §6 on the curve
        sigma_0(Y) = 1/2 + c loglogY/logY, c > 2, Y = ceil(4(T+2)), for all large T.
        The question is whether (H_T) fails for arbitrarily large T, possibly under RH.
Exact sources or dependencies: pr910 = 670a76c1 (NATIVE_HEIGHT.md §§4-6: (E), (Z), (P), (O), §6.1
        diagonal bound); PR910_HEIGHT_TEST.md (§1.1, §5.2 Proposition A, §5.3);
        Soundararajan, Math. Ann. 342 (2008); Titchmarsh, 2nd ed., §§14.2, 14.25, 14.27;
        Montgomery-Vaughan, J. London Math. Soc. (2) 8 (1974) (mean-value theorem);
        Bondarenko-Seip arXiv:1704.06158 (abstract checked; see §2).
What was actually run: scripts/noise_floor_points.py, which imports Native etc. from the unmodified
        pr910_height_scan.py. It evaluates zeta by Euler-Maclaurin, checked against mpmath
        to <= 6e-12 relative, then tail = 1/zeta - G_Y at the 48 stored resonance points and
        at 600 random heights in [2e4, 1e5].
        scripts/noise_floor_onset.py: a random Euler product saddle-point model (heuristic onset).
        Outputs are in results/noise_floor_{validate,points,random,onset}.json.
Smallest remaining gap: Lemma NF(c) of §3.2, assuming RH:
        limsup_{t->oo} sup_{sigma in [sigma_0(Y(t)),1)} |zeta(s) * sum_{n>Y(t)} mu(n) n^{-s}| > 1/sqrt(8),
        for every c > 2. NZ(c) of §3.3 is sufficient for NF(c) and needs no RH: the Möbius partial
        sum G_{Y(T)} vanishes somewhere on [sigma_0, 1) x {T} for arbitrarily large T.
```

## 0. Results

| # | Statement | Hypothesis | Status |
|---|---|---|---|
| A | Proposition A of PR910_HEIGHT_TEST §5.2 | RH | **confirmed**, with exact quantifiers (§2) |
| 1 | `R_Y = −ζ·T_Y − (ζ−B_Y)·G_Y`, hence `R_Y = −ζT_Y + O_ε(t^{−1/2+ε})` on the region | RH | proved (§3.1) |
| 2 | (H_T) for all large T ⟹ `limsup sup|ζT_Y| ≤ 1/√8`; `limsup > 1/√8` ⟹ (H_T) fails for arbitrarily large T | RH (the R_Y-form needs no RH) | proved (§3.2) |
| 3 | A zero of `G_Y` (or `B_Y`) on `[σ₀(Y),1)×{T}`, `Y=Y(T)`, T large ⟹ (H_T) fails | none beyond PR 910's proved diagonal bound | proved (§3.3) |
| 4 | Freezing: on `[T, T+T^{1/2−2ε}]` the moving cutoff can be replaced by `Y(T)` at cost `O(T^{−ε/2})` | RH | proved (§3.4) |
| 5 | Every resonance first moment `∫ R_Y·P·W` with `P` a Dirichlet polynomial and `Ŵ` supported in `(−log Y, log Y)` vanishes identically | none | proved (§3.5) |
| 6 | Noise-floor lemma (doc §5.3) / NF(c) / NZ(c) | RH / RH / none | **OPEN**. The obstruction is identified in §4.1–4.2 |
| 7 | Explicit-formula mechanism: the tail is negatively correlated with `|ζ|` | RH + simple zeros, formal | heuristic + data (§4.3, §5) |
| 8 | Steinhaus model: given the small primes, the near-cutoff conditional variance is `≥ |1−P_X|²·Σ_{Y/2<b≤Y, X-rough} b^{−2σ}` | model | proved in the model (§4.4) |
| 9 | Onset of failure in a random Euler product model | model | HEURISTIC (§6) |

**Correction to PR910_HEIGHT_TEST §5.3.** That section says "No mechanism correlating them [resonance and tail] is known." This is too strong. Under RH (and simple zeros), the explicit formula writes the tail as a sum over zeros near `t` (§4.3). Large values of ζ come with a local gap between zeros, so a correlation is to be expected. The data show it: across random heights, `log|tail|` has slope ≈ −0.7 against `log|ζ|` (§5.2). This slope is *not* the slope −1 that pointwise mollification would need. At the targeted small-prime resonance points, the tail is not suppressed at all (§5.1). The heuristic expectation of eventual failure stands, but the onset depends on this slope (§6).

## 1. Notation

Throughout:
* `s=σ+it`, `t` large, `Y=Y(t)=⌈4(t+2)⌉`.
* `δ_Y = c log log Y/log Y`, `σ₀ = σ₀(Y) = 1/2+δ_Y`, `c>2`, `Ω=2log Y`, `L(t)=√(log t/log log t)`.
* `G_Y=Σ_{n≤Y}μ(n)n^{−s}`, `B_Y=Σ_{n≤Y}n^{−s}`, `R_Y=G_YB_Y−1`, `E_Y:=ζ−B_Y`.
* Under RH, `T_Y(s):=Σ_{n>Y}μ(n)n^{−s}`, which converges to `1/ζ(s)−G_Y(s)` for `σ>1/2` (Titchmarsh §14.25).
* The "region at height T" is `{σ+iT : σ∈[σ₀(Y(T)),1)}`.

Facts proved in PR 910 and used below:
* **(F1) Sobolev.** `|R_Y(σ+iT)|² ≤ (3Ω/2)·ℰ_Y(σ;T)` (NATIVE_HEIGHT §5).
* **(F2) Diagonal.** For `σ≥σ₀(Y)`, `Ω𝒟_Y(σ) ≤ ε_D(Y) := (512/(c log 2))(log Y)^{4−2c}/log log Y → 0` (§6.1, `c>2`).
* **(F3) Euler remainder (E).** `|E_Y − Y^{1−s}/(s−1)| ≤ 2Y^{−σ}` when `Y≥2(|t|+1)`. Hence on the region `|E_Y| ≤ Y^{1/2}/t + 2Y^{−1/2} ≤ 3t^{−1/2}`.

## 2. Proposition A re-derived

**Statement (as in PR910_HEIGHT_TEST §5.2).** Assume RH and fix `c>2`. Suppose `(H_T)` holds for every real `T≥T₀`. Then there are `t_k→∞` such that, with `Y_k=Y(t_k)` and `s_k=σ₀(Y_k)+it_k`,

`|G_{Y_k}(s_k)| ≤ exp(−(1+o(1))L(t_k))` and `|T_{Y_k}(s_k)| ≤ exp(−(1+o(1))L(t_k))`.

**Check, step by step.**

1. **The pointwise bound.** By (F1), `(H_T)` gives `|R_Y(σ₀+iT)|² < (3Ω/2)(𝒟+1/(12Ω)) ≤ 1/8 + (3/2)ε_D(Y)`, so `|R_Y| < 0.36` once `ε_D(Y) < 0.0030`. Only the endpoint `σ=σ₀` and only the heights `T=t_k` are used. So the hypothesis can be weakened to "(H_{t_k}) at σ₀ for large k". ✔
2. **Large values on the line.** Soundararajan, Math. Ann. 342 (2008), main theorem for ζ, unconditional: for large `T` some `t∈[T,2T]` has `|ζ(1/2+it)| ≥ exp((1+o(1))L(T))`. Since `log t~log T`, `L(T)=(1+o(1))L(t)`. ✔
   * Bondarenko–Seip (arXiv:1704.06158) improves this on `σ=1/2`. Its abstract states nothing uniform in σ, so it does not remove step 3's use of RH.
3. **Transfer to the curve (RH).** Under RH, `∂_σ log|ξ(σ+it)| = Σ_ρ (σ−1/2)/|s−ρ|² ≥ 0` for `σ≥1/2`. This is `Re ξ'/ξ = Σ_ρ Re (s−ρ)^{−1}`, using the standard cancellation of the Hadamard constant. With `Re ψ(z)=log|z|+O(|z|^{−2})` for `Re z ∈ [1/4,1/2]` and `∂_σ log|s(s−1)| = O(t^{−2})`, this gives `∂_σ log|ζ| ≥ −½log(|s|/2π) − O(t^{−2})`. Integrating over `[1/2,σ₀]` and using `|s|/2π < Y`:
   `|ζ(σ₀+it)| ≥ |ζ(1/2+it)|·(log Y)^{−c/2}(1+O(t^{−2}))`. ✔
4. **From ζ to `B_Y`.** By (F3), `|B_Y−ζ| ≤ 3t^{−1/2}`. ✔
5. **Combine.** `|B_Y(s_k)| ≥ exp((1+o(1))L)` because `(c/2)log log Y = o(L)`. Then `|G_Y| ≤ 1.36/|B_Y|`. Under RH, `T_Y = 1/ζ − G_Y`, and `|1/ζ(s_k)| ≤ exp(−(1+o(1))L)`. ✔

**Where RH enters:** step 3 (monotonicity of `|ξ|`) and step 5 (the tail exists and equals `1/ζ−G_Y`). Steps 1, 2 and 4 are unconditional.

**Verdict:** Proposition A is correct as stated. Its RH-free part is the implication "`(H_{t})` at σ₀ and `|ζ(σ₀+it)|` large ⟹ `|G_Y(σ₀+it)| ≤ 1.36/(|ζ|−3t^{−1/2})`".

## 3. Proved reductions

### 3.1 The product defect is ζ times the tail (RH)

**Lemma 3.1 (RH, standard).** For each fixed `ε>0`, uniformly for `σ≥σ₀(Y)` and `Y=Y(t)`: `G_Y(σ+it) ≪_ε t^ε`.

*Proof.* Set `M_t(u)=Σ_{n≤u}μ(n)n^{−it}`. Under RH, `1/ζ(w) ≪_ε |Im w|^ε` for `Re w ≥ 1/2+ε` (Titchmarsh §14.2). Perron's formula, with the contour moved to `Re w = 1/2+ε` exactly as in Titchmarsh §14.25 for `M(x)`, gives `M_t(u) ≪_ε u^{1/2+ε}(u+|t|)^ε`. Partial summation gives

`G_Y(σ+it) = M_t(Y)Y^{−σ} + σ∫_1^Y M_t(u)u^{−σ−1}du ≪ Y^{2ε}(1+ε^{−1})`.

Here `Y≍t`. ∎

**Lemma 3.2 (exact algebra, then RH).** Wherever `ζ(s)≠0` and `T_Y(s)` is defined,

`R_Y = (1/ζ − T_Y)(ζ − E_Y) − 1 = −ζ T_Y − E_Y G_Y`.

On the region, `|E_YG_Y| ≪_ε t^{−1/2+ε}` by (F3) and Lemma 3.1. So, under RH, **`R_Y(s) = −ζ(s)T_Y(s) + O_ε(t^{−1/2+ε})`** uniformly on the region. ∎

### 3.2 A two-sided criterion; the minimal target

**Theorem 3.3.**
* **(a) Unconditional, given (F1)–(F2).** Let `T` be large and `σ∈[σ₀(Y),1)`, `Y=Y(T)`. If `|R_Y(σ+iT)|² > 1/8+(3/2)ε_D(Y)`, then `(H_T)` fails.
  *Proof.* By (F1), `ℰ ≥ (2/(3Ω))|R_Y|² > 1/(12Ω)+ε_D/Ω ≥ 1/(12Ω)+𝒟_Y(σ)`. So `𝒪 = ℰ−𝒟 > 1/(12Ω)`. ∎
  Conversely, `(H_T)` forces `|R_Y| < (1/8+(3/2)ε_D)^{1/2}` on the whole region at height `T`.
* **(b) Under RH.** By Lemma 3.2:
  * `(H_T)` for all `T≥T₀` implies `limsup_{T→∞} sup_{σ∈[σ₀,1)} |ζT_Y(σ+iT)| ≤ 1/√8`;
  * if that limsup is `>1/√8`, then `(H_T)` fails for arbitrarily large `T`, so the route fails.

So the minimal "noise-floor" target is:

> **NF(c) (RH).** `limsup_{t→∞} sup_{σ∈[σ₀(Y(t)),1)} |ζ(σ+it)·Σ_{n>Y(t)} μ(n)n^{−σ−it}| > 1/√8`.

* NF(c′) implies NF(c) for `c′>c`. To kill the route for every `c>2`, NF(c) is needed for arbitrarily large `c`.
* The form in PR910_HEIGHT_TEST §5.3 is strictly stronger and sufficient: "tail `≥ exp(−(1−ε)L)` at the Proposition A heights" gives `|ζT_Y| ≥ exp((ε+o(1))L) → ∞`.
* NF asks for much less: one point per scale where `|ζ|·|tail|` exceeds 0.354. The point can be anywhere on the region, not just at the extreme-value heights.
* Without RH, the same target reads `limsup sup |G_YB_Y−1| > 1/√8`. By Theorem 3.3(a) this is unconditional.

### 3.3 A zero criterion that needs no RH

**Proposition 3.4.** Let `T` be large enough that `ε_D(Y) < 7/12`. If `G_Y(σ+iT)=0` or `B_Y(σ+iT)=0` for some `σ∈[σ₀(Y),1)`, `Y=Y(T)`, then `(H_T)` fails.

*Proof.* There `R_Y=−1`, and `1 > (1/8+(3/2)ε_D)^{1/2}`. Apply Theorem 3.3(a). ∎

> **NZ(c) (no RH).** For arbitrarily large `T`, the Möbius partial sum `G_{Y(T)}` has a zero `β′+iT` with `β′∈[σ₀(Y(T)),1)`.

* NZ(c) disproves the route unconditionally.
* Under RH, `G_Y = ζ^{−1}(1−ζT_Y)` on the region. So the zeros of `G_Y` there are exactly the solutions of `ζT_Y=1`, and NZ is the special case "value 1" of NF.
* NZ is phrased entirely in terms of zeros of Dirichlet polynomials of length `≈4T` at height `T`. That is a regime where neither Kronecker-type constructions nor mean-value theorems apply (§4.2). Kronecker needs heights far beyond the polynomial length, as in the known constructions of zeros of partial sums of ζ.
* Zeros of `B_Y` on the region are not expected, since `B_Y=ζ+O(t^{−1/2})`. They are listed only for completeness.

### 3.4 Freezing the cutoff (RH)

**Lemma 3.5.** Fix `0<ε<1/4`. Let `T` be large, `Y*=Y(T)`, `H=T^{1/2−2ε}`. For `t∈[T,T+H]` and `σ∈[σ₀(Y*),1)`:
* `σ ≥ σ₀(Y(t))`, since σ₀ decreases for `log Y>e`;
* `|R_{Y(t)}(σ+it) − R_{Y*}(σ+it)| ≪_ε T^{−3ε/2}`.

*Proof.*
1. `Y*≤Y(t)≤Y*+4H+1`. So `|G_{Y(t)}−G_{Y*}|` and `|B_{Y(t)}−B_{Y*}|` are both `≤(4H+1)Y*^{−1/2} ≪ T^{−2ε}`.
2. `|B_{Y(t)}| ≤ |ζ|+3t^{−1/2} ≪ T^{ε/2}`, by the Lindelöf bound under RH. `|G_{Y*}| ≪ T^{ε/2}` by Lemma 3.1.
3. Expand `GB − G*B* = (G−G*)B + G*(B−B*)`. ∎

**Corollary 3.6 (RH).** If `(H_t)` holds for all `t≥T₀`, then for every large `T`:
* `sup|R_{Y*}| ≤ 1/√8+o(1)` on `[σ₀(Y*),1)×[T,T+T^{1/2−2ε}]`;
* in particular, `G_{Y*}` has no zeros in that rectangle.

The moving cutoff is therefore **not** the obstruction. A fixed polynomial of length `Y*≈4T` must be controlled on a window of length `T^{1/2−2ε}`.

### 3.5 Linear resonance arguments cannot work

**Proposition 3.7.** Let `P(s)=Σ_{m≥1}p_mm^{−s}` be any finite Dirichlet polynomial, `σ` real, and `W∈L¹(ℝ)` with `Ŵ(ξ)=∫W(t)e^{−iξt}dt` supported in `[−log Y, log Y]`. Then

`∫R_Y(σ+it)P(σ+it)W(t)dt = Σ_{n>Y, m≥1} e_Y(n)p_m(nm)^{−σ}Ŵ(log nm) = 0`.

The support of `e_Y` lies in `(Y,Y²]` and `nm>Y`. ∎

* This covers every resonance weight `W=|Σ_{k≤N}r_kk^{−it}|²Φ(t/T)` with `N<Y/2` and `supp Φ̂⊂[−1,1]`.
* It covers `P ∈ {1, B_Y, B_Y^k, G_Y, …}`.
* So no first-moment (linear) resonance statistic can detect `R_Y`. Any proof of NF must be at least quadratic in Möbius, e.g. must evaluate `∫|R_Y|²W`.

## 4. The noise floor: what blocks a proof, and what is true in a model

### 4.1 The quadratic route

NF would follow from any weight `W≥0`, supported where Corollary 3.6 applies, with `∫|R_{Y*}|²W ≥ (1/8+η)∫W`.

With a resonator, `|R_{Y*}·Res|²` is a Dirichlet polynomial of length `≈16T²N`, averaged over a window of length `H≤T^{1/2}`. A window of length `H` cannot separate frequencies `log k` closer than `1/H`. Near `k≈K` that leaves about `K/H ≈ T^{3/2}N` integers per frequency cell. The window mean is therefore dominated by shifted-convolution sums

`Σ_{|k−k′| ≲ k/H} c_k c̄_{k′}`, with `c = e_Y ∗ r` (Dirichlet convolution),

which are binary correlations of Möbius-built coefficients with shifts up to `T^{3/2}N`.

### 4.2 The obstruction is structural: the tail lives where `n > t`

Even ignoring the moving cutoff, the tail block `n∈(Y,2Y]` with `Y≥2(t+1)` (the condition needed for (E)) is not resolved by any t-average up to height `Y/2`:
* Montgomery–Vaughan gives `∫_0^{T′}|Σa_nn^{−it}|²dt = Σ|a_n|²(T′+O(n))`.
* For `n>Y≥2T′`, the error allowance `O(n)` exceeds the main term `T′`, so the diagonal is not a lower bound. This is not a defect of the method: neighbouring frequencies `log n, log(n+1)` differ by `<1/T′`.

Equivalently, by partial summation,

`T_Y(s) = −M(Y)Y^{−s} + s∫_Y^∞ M(u)u^{−s−1}du`.

On `u≥Y`, the phase `u^{−it}` has local frequency `t/(2πu) ≤ 1/(8π)` cycles per unit `u`. So the tail is a low-frequency chirp transform of the Mertens function past the cutoff. A lower bound for it at prescribed (t-locked) frequencies is a statement about Möbius in short intervals against slowly varying phases.

The relevant quantitative input would be a two-point (log-averaged) Chowla estimate with:
* uniformity in dilations up to `N` and shifts up to `T^{1/2+o(1)}`;
* a power-of-log saving.

The saving must be power-of-log because the target diagonal is only `(log Y)^{1−2c}/log log Y` relative to trivial. Matomäki–Radziwiłł–Tao (averaged Chowla) and Tao (log-averaged two-point Chowla) give only qualitative `o(1)` savings, without this uniformity. GRH gives no binary Möbius correlations. **This is why the noise floor is out of reach, not merely unproved here.**

### 4.3 A correlation mechanism (RH + simple zeros; the convergence of the zero sum is formal)

Perron's formula for `G_Y` (`Y` a half-integer) gives `G_Y(s)=(2πi)^{−1}∫Y^w/(wζ(s+w))dw`. Moving the contour left across `w=0` and `w=ρ−s`, as in the explicit formula for `M(x)` (Titchmarsh §14.27), gives

`T_Y(s) = Σ_ρ Y^{ρ−s}/((s−ρ)ζ′(ρ)) + (trivial zeros)`, and so
`ζ(s)T_Y(s) = Y^{1/2−σ}·Σ_ρ Y^{i(γ−t)}·ℓ_ρ(s)`, where `ℓ_ρ(s)=ζ(s)/((s−ρ)ζ′(ρ))`.

Here `ℓ_ρ` is the Lagrange-type basis: `ℓ_ρ(ρ)=1` and `ℓ_ρ(ρ′)=0` for `ρ′≠ρ`.

* The noise `|T_Y|·Y^{δ}` is set by zeros within a few multiples of `δ_Y` of `t`, and by their `1/|ζ′(ρ)|`.
* A large value of `ζ(σ₀+it)` comes with a local gap in the zeros and with large `|ζ′|` at the zeros bordering the gap. Both shrink the tail.

So a mechanism correlating large `|ζ|` with small `|T_Y|` **does exist**. The open question is quantitative:
* pointwise mollification (the route) needs `|T_Y| ≲ 0.35/|ζ|`, i.e. log-log slope −1, at the largest values;
* the data give a bulk slope of ≈ −0.7 and no suppression at small-prime resonance points (§5).

### 4.4 Model theorem (Steinhaus random multiplicative model; rigorous in the model only)

**Setup.** Let `f` be a Steinhaus completely multiplicative function: the `f(p)` are i.i.d. uniform on the circle. It models `n^{−it}`; `μ(n)f(n)` models `μ(n)n^{−it}`. Put
* `P_X := ∏_{p≤X}(1−f(p)p^{−σ})`, the model of `1/ζ_X`;
* `𝒯_Y := Σ_{n>Y}μ(n)f(n)n^{−σ}`, an `L²` limit since `σ>1/2`;
* `𝔉_X := σ(f(p):p≤X)`.

**Proposition 4.1.** `E[|𝒯_Y|² | 𝔉_X] = Σ_{b X-rough} μ²(b)b^{−2σ}|S_b|²`, where `S_b := Σ_{a X-smooth, a>Y/b} μ(a)f(a)a^{−σ}`. In particular

`E[|𝒯_Y|² | 𝔉_X] ≥ |1−P_X|²·Σ_{Y/2<b≤Y, b X-rough} μ²(b)b^{−2σ}`.

*Proof.* Write `n=ab` with `a` X-smooth and `b` X-rough. Conditionally on `𝔉_X`, the `f(b)` for distinct squarefree rough `b` are orthonormal and independent of `𝔉_X`. For `b∈(Y/2,Y]`, `Y/b<2`, so `S_b = Σ_{a≥2}μ(a)f(a)a^{−σ} = P_X−1`. ∎

**Consequence in the model.**
* On a small-prime resonance (`|P_X|≤1/2`), the near-cutoff rough block alone has conditional variance `≫ Y^{−2δ}/log X` when `X≤Y^{1/2}` (sieve lower bound for rough numbers). With `X≈log T`, this floor is about `(log Y)^{−2c}/log log Y`.
* The mechanism is the `a=1` term: a sharp cutoff passes the rough numbers just below `Y` with weight `1`, not with the tiny weight `P_X`.
* This is the doc's §5.1 mechanism, made exact in the model.

**Not proved, even in the model:** anti-concentration jointly with "`|ζ_f|` large". The large value also involves the rough primes, which are shared with `𝒯_Y`. And the model ignores the `n>t` locking of §4.2, which is exactly what the deterministic problem lacks.

## 5. Numerics (EMPIRICAL; float64, Euler–Maclaurin ζ checked against mpmath to `≤6·10⁻¹²` relative; not certified)

### 5.1 The stored large/small-value points (`results/noise_floor_points.json`)

Notation: `Ymd := Y^{−δ}` with `δ=σ−1/2`, the polynomial size of the tail. "rms" is `√(6/π²)·Ymd/√(2δ)`.

| set | σ | \|ζ\| | \|G_Y\|·\|ζ\| | \|tail\|/\|1/ζ\| | \|tail\|/Ymd | near-cutoff share \|Σ_{Y/2<n≤Y}\|/\|G_Y\| | \|ζ·tail\| |
|---|---|---|---|---|---|---|---|
| curve, large (6 pts, T≤10⁵) | 0.897–0.920 | 5.6–6.0 | 0.97–1.03 | 0.02–0.03 | 0.58–0.84 | 0.02–0.04 | 0.022–0.030 |
| curve, large (6 pts, T≤10⁶) | 0.859–0.889 | 6.7–8.3 | 0.99–1.04 | 0.01–0.06 | 0.27–**1.79** | 0.02–0.03 | 0.010–**0.061** |
| curve, small \|ζ\| (12 pts) | 0.858–0.916 | 0.28–0.45 | 0.98–1.01 | 0.004–0.016 | **3.1–7.7** | ≤0.01 | 0.004–0.015 |
| σ=0.70, large (6 pts) | 0.70 | 9.4–10.7 | **0.30–1.82** | 0.57–0.82 | 0.62–0.89 | **0.37–1.61** | 0.56–0.82 |
| σ=0.75, large (6 pts) | 0.75 | 8.0–9.1 | 0.65–1.38 | 0.26–0.38 | 0.61–0.89 | 0.18–0.41 | 0.26–0.38 |
| σ=0.70, small (6 pts) | 0.70 | 0.25–0.61 | 0.90–1.10 | 0.11–0.20 | 2.8–5.2 | 0.03–0.11 | 0.10–0.18 |

* The identity of Lemma 3.2 is visible numerically. `|R_Y|` and `|ζ·tail|` agree to the size of `|E_YG_Y|`, which is `10⁻⁶–10⁻³`.
* **On the curve at `T≤10⁶`, the regime "tail ≈ −G_Y" is not reached.**
  * `G_Y` still equals `1/ζ` to within 1–6%: `|G_Y||ζ| ∈ [0.97,1.04]`.
  * The near-cutoff block is only 2–4% of `G_Y`.
  * The question in the task ("can `G_Y` be uniformly tiny where ζ is large?") only becomes live when `|ζ(σ₀+it)| ≳ 1/|tail| ≈ (log Y)^{c}`.
* **Off the curve (σ=0.7), that regime is reached.**
  * `|G_Y||ζ|` ranges over 0.30–1.82.
  * The near-cutoff block is comparable to `G_Y`.
  * The tail is not suppressed relative to `Y^{−δ}`.
  * At these points the head polynomial is visibly *not* tracking `1/ζ`. This is the noise floor in action, at heights where the curve is far away.
* **Large ζ, smaller tail.** At small `|ζ|` the tail is 3–8 × `Y^{−δ}`. At large `|ζ|` it is 0.3–1.8 × `Y^{−δ}`. This is the §4.3 correlation.

### 5.2 Random heights (`results/noise_floor_random.json`, 600 uniform `t∈[2·10⁴,10⁵]`, each with its own `Y(t)`)

| σ | median \|tail\|/Ymd by \|ζ\|-quantile bin (0–50%, 50–90%, 90–99%, 99–100%) | slope of log\|tail\| on log\|ζ\| | max \|ζ·tail\| |
|---|---|---|---|
| σ₀ (curve) | 0.77, 0.42, 0.31, 0.22 | −0.71 | 0.019 |
| 0.70 | 1.03, 0.52, 0.32, 0.22 | −0.71 | 0.40 |
| 0.60 | 1.49, 0.58, 0.33, 0.22 | −0.73 | **1.81** |

* The bulk slope ≈ −0.7 matches PR910_HEIGHT_TEST §4.5 (slope 0.28–0.35 for `log|R_Y|`, since `log|R|≈log|ζ|+log|tail|`).
* The top bin holds only 6 points per σ. Whether the slope steepens toward −1 or flattens at the extremes cannot be read off.
* PR910_HEIGHT_TEST's larger 1,200-point run saw flattening.
* The targeted resonance points (§5.1, σ=0.7, `|ζ|≈10.5`) have tail/Ymd = 0.62–0.89. That is larger than the random top bin (0.22 at `|ζ|≈6`). So **the tail is not a function of `|ζ|`**: small-prime-driven large values keep a near-typical tail.
* At σ=0.6, `|ζ·tail|` already exceeds 1 at random heights `≤10⁵`. By §3.3 (applied at fixed σ, off the curve), this means zeros of `G_Y` with real part near 0.6 at those heights. That is consistent with §5.3 of the earlier report: the fixed-σ failures are pre-asymptotic.

## 6. Heuristic onset in a random Euler product model (`results/noise_floor_onset.json`)

**Model** (HEURISTIC; nothing here is a statement about ζ):
* `log|ζ(σ₀+it)|` is modelled by `Σ_p −log|1−U_pp^{−σ₀}|`, with `U_p` uniform. Its cumulant generating function is exact: `K(λ)=Σ_p log ₂F₁(λ/2,λ/2;1;p^{−2σ₀})`.
* The tail is `A·Y^{−δ}·|ζ|^{−θ}`.
* Failure at a point needs `log|ζ| ≥ V* = (log(0.354/A) + c log log Y)/(1−θ)`.
* The Bahadur–Rao saddle point estimates `P(log|ζ|≥V*)`. There are `N_eff=T` trials in `[T,2T]`.
* The onset is the least `T` on the grid with `T·P ≥ 1`.

| c | A | θ | onset: first grid `log₁₀T` with `T·P≥1` (previous grid point) | σ₀ there | `V*` = required `log|ζ|` | `log₁₀P` |
|---|---|---|---|---|---|---|
| 2 | 1.0 | 0 | **40** (30: count `10^{−5.9}`) | 0.597 | 8.0 | −32.1 |
| 2 | 0.3 | 0 | **60** (40: `10^{−8.7}`) | 0.571 | 10.0 | −40.7 |
| 2 | 1.0 / 0.3 | 0.7 | **500** (300: `10^{−127}` / `10^{−235}`) | 0.512 | 43.5 / 47.5 | −392 / −480 |
| 3 | 1.0 / 0.3 | 0 | **150** (100: `10^{−34}` / `10^{−67}`) | 0.551 | 16.5 / 17.7 | −109 / −132 |
| 3 | 1.0 / 0.3 | 0.7 | **2000** (1000: `10^{−182}` / `10^{−333}`) | 0.505 | 80.9 / 84.9 | −1069 / −1190 |

**What the table says (heuristic only).**
* **θ=0 (no suppression).** This is the empirical law `|R_Y|≈κ|ζ|Y^{−δ}` of PR910_HEIGHT_TEST, and what §5.1 shows at small-prime resonance points. Failure would set in around `T≈10^{35}–10^{60}` for `c=2` and `T≈10^{100}–10^{150}` for `c=3`. The values of `|ζ(σ₀+it)|` needed are only `e^8–e^{18}`, and they come from moderate deviations of the Euler product (saddle `λ≈26–46`), not from Soundararajan-scale extremes. The `10^{2000}–10^{3000}` of PR910_HEIGHT_TEST §5.3 used the proven extreme-value scale and is a late, conservative bound.
* **θ=0.7 (the bulk slope of §5.2 persists to the extremes).** The onset moves to `T≈10^{300}–10^{500}` (`c=2`) and `10^{1000}–10^{2000}` (`c=3`).
* **θ=1 (exact tracking).** The criterion `|ζT_Y|>1/√8` could fail only through fluctuations of `A`, and the route might survive. So the onset, and even the expectation of failure, hinges on the open correlation question of §4.3.
* Every onset is far beyond computation. At `T≤10⁶`, the needed `|ζ(σ₀+it)|` (`≳ 0.354(log Y)^c/A`, about 25–80 for `A=1`) exceeds every value that occurs at `σ₀≥0.85`.

**Caveats.**
* `N_eff=T` is crude; a factor `log T` does not move any onset by a grid step.
* Bahadur–Rao is asymptotic. Rows where the saddle hit the search cap `λ=200` give only Chernoff-type upper bounds; none of them is an onset row.
* The Euler product model ignores the `n>t` locking of §4.2.

## 7. What is established, and the smallest remaining lemma

* **Proved (RH):**
  * Proposition A, as stated.
  * Lemma 3.2 (`R_Y=−ζT_Y+O(t^{−1/2+ε})`).
  * Theorem 3.3(b): the route's hypothesis implies `limsup|ζT_Y| ≤ 1/√8`, and a limsup above `1/√8` kills the route.
  * Lemma 3.5 (freezing).
* **Proved (no RH beyond PR 910's own diagonal bound):**
  * Theorem 3.3(a): the pointwise threshold `|R_Y| > (1/8+(3/2)ε_D)^{1/2}`.
  * Proposition 3.4: zeros of `G_Y` or `B_Y` on the region kill `(H_T)`.
  * Proposition 3.7: every band-limited linear resonance statistic of `R_Y` vanishes.
* **Proved in a model only:** Proposition 4.1, the near-cutoff conditional variance floor.
* **Not proved:**
  * the noise-floor lemma in any form (§5.3 form, NF, or NZ);
  * any average lower bound for the tail over a resonance set, or even over `[T,2T]` with the moving cutoff. §4.2 explains why: the tail sits at `n>2t`, where t-averages up to the current height do not resolve frequencies.
* **Smallest precise lemma that would finish the RH-conditional disproof:** NF(c) of §3.2, for every `c>2`. Each of the following implies it, from weakest technology to strongest:
  1. NZ(c) (§3.3; no RH needed);
  2. a resonance-weighted quadratic bound `∫|R_{Y*}|²W ≥ (1/8+η)∫W` on freezing windows (§4.1). This reduces to uniform two-point Möbius correlations with power-of-log savings (§4.2);
  3. the §5.3 form: tail `≥exp(−(1−ε)L)` at Soundararajan heights.

  None is within current technology, as far as this analysis can tell.

## 8. Reproduction (from `research/exploratory/qrh-2026-10/falsification/`)

```sh
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
python3 -I scripts/noise_floor_points.py validate > results/noise_floor_validate.json        # <1 s
python3 -I scripts/noise_floor_points.py points --k 6 > results/noise_floor_points.json      # ~15 s
python3 -I scripts/noise_floor_points.py random --n 600 --sigmas 0.6,0.7 > results/noise_floor_random.json   # ~70 s
python3 -I scripts/noise_floor_onset.py --cs 2,3 --As 0.3,1.0 --thetas 0,0.7 \
    --log10T 10,20,30,40,60,80,100,150,200,300,500,1000,2000 > results/noise_floor_onset.json  # ~3 min
```

`noise_floor_points.py` imports `Native`, `mobius_sieve`, `sigma0` and `Y_of_T` from `scripts/pr910_height_scan.py`, which is unchanged. The `points` subcommand reads the stored `results/pr910_resonance_*.json`.

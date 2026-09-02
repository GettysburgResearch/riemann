# The mollified compression: multiplicative weights on the Alpöge–Furman certificate

Claim identifiers `109300–109308`. Notation follows Alpöge–Furman (AF, arXiv:2608.13637v2) and
Bui–Heath-Brown (BHB, arXiv:1302.5018). `N = N(T,2T)` counts zeros with multiplicity in the
window, `s_1` the simple zeros on the critical line, `L = log(T/2π)`, `S_ρρ' := (φ²)^(γ_ρ−γ_ρ')/(φ²)^(0)`
the normalised Poisson–Gabor kernel (`sinc(L(γ−γ')/2)` for the flat window), `B(s) = Σ_{k≤y} μ(k)
P(log(y/k)/log y) k^{−s}` the BHB mollifier, `F := Bζ'`, `S_1 := Σ_ρ F(ρ)`, `S_2 := Σ_ρ F(ρ)F(1−ρ)`.

## 0. Where RH enters, and why the two-dimensional compression cannot be made unconditional

**L-109308.** BHB's proof (their Section 2, end) is the Cauchy–Schwarz inequality
`N^* ≥ |S_1|²/Σ_ρ|F(ρ)|²` together with the two evaluations `S_1 ∼ (19/24)TL²/2π` and
`S_2 ∼ (57/64)TL³/2π`, both unconditional (Lemmas 1–2 there). RH is used exactly once: to write
`Σ_ρ|F(ρ)|² = S_2`. Unconditionally one has only `S_2 ≤ Σ_ρ|F(ρ)|²` (an off-line pair `{ρ, ρ'=1−ρ̄}`
contributes `2Re(F(ρ)F(ρ')̄) ≤ |F(ρ)|²+|F(ρ')|²`), the wrong direction for Cauchy–Schwarz.

In AF's language, BHB's inequality is the statement that Weil's form restricted to `V = span{1, F}`
equals `P_1 + P_{≥2} + Q` with `P_{≥2} = (Σ_{mult} m_ρ)·e_1e_1^T` (multiple zeros load only the
constant direction, since `F` vanishes there) and, under RH, `Q = 0`; positivity of `P_1 =
[[s_1, S̄_1],[S_1, S_2]]` is exactly `s_1 S_2 ≥ |S_1|²`. Unconditionally `Q` is a sum of signature-`(1,1)`
blocks with `n_+(Q) ≤ p`; on a two-dimensional space this bound is vacuous as soon as `p ≥ 1`.
Hence AF's inertia mechanism cannot remove RH from the BHB argument as it stands: the index bound
bites only when the test space has dimension comparable to `N`. This is the reason for the
high-dimensional weighted family of Section 1. ∎

## 1. The weighted certificate (exact algebra)

Fix a window `φ` as in AF §2.2 and the **infinite** Gabor lattice `α_k = T + 2πk/L`, `k ∈ Z`, so that
Poisson–Gabor is exact: `Σ_k φ̂(z−α_k)φ̂(z'−α_k) = L(φ²)^(z−z')` for all complex `z, z'`. For a zero
`ρ = 1/2 + iγ` (`γ` complex) put `v_ρ := (φ̂(γ−α_k))_k ∈ ℓ²(Z)`; then `v_ρ·v_ρ = aL²` for every `ρ`,
`v_{1−ρ̄} = v̄_ρ`, and `v_ρ·v̄_ρ' = L(φ²)^(γ_ρ − γ̄_ρ')`.

Let `Z` be a finite set of nontrivial zeros closed under `ρ ↦ 1−ρ̄`, and let `h` be holomorphic on a
neighbourhood of the critical strip with `h(s̄) = h(s)̄` (real Dirichlet coefficients suffice) and
`h(ρ) = 1` at every zero `ρ ∈ Z` on the line of multiplicity `≥ 2`. Put `c_ρ := h(ρ)h(1−ρ)` and

```text
W_h := (aL²)^{-1} Σ_{ρ∈Z} m_ρ c_ρ v_ρ v_ρ^T      (a finite-rank operator on ℓ²(Z)).
```

`W_h` is the compression of Weil's form `W(f,g) = Σ_ρ m_ρ f(ρ) g(1−ρ̄)̄` to the family `f_k = h·φ̂(·−α_k)`,
using `h(1−ρ̄)̄ = h(1−ρ)` and `φ̂(γ̄−α)̄ = φ̂(γ−α)`; it is Hermitian because `Z` is symmetric and
`c_{1−ρ̄} = c̄_ρ`, `v_{1−ρ̄} = v̄_ρ`.

**Theorem 1 (T-109300).** With `s_1(Z)` the number of simple on-line zeros in `Z`,

```text
s_1(Z) ≥ 2 tr W_h − ‖W_h‖²_HS − 2 Σ_{ρ∈Z off-line} m_ρ (1 − c_ρ),
```

where `tr W_h = Σ_{ρ∈Z} m_ρ c_ρ`, `‖W_h‖²_HS = Σ_{ρ,ρ'∈Z} m_ρ m_ρ' c_ρ c̄_ρ' |S(γ_ρ − γ̄_ρ')|²`, and the
last sum is real (each pair contributes `2m Re(1−c_ρ)`).

*Proof.* Decompose `W_h = P_1 + P_{≥2} + Q` over the three kinds of zeros. An on-line zero has real
`v_ρ` and `c_ρ = h(ρ)h(ρ̄) = |h(ρ)|² ≥ 0`, so it contributes a PSD rank-one term; `P_1` (simple on-line)
is PSD of rank `≤ s_1(Z)` and `P_{≥2}` (multiple on-line, where `c_ρ = 1`) is PSD of rank `≤ #mult`.
An off-line pair contributes `m[c v v^T + c̄ v̄ v̄^T] = 2m Re(c v v^T)`, whose quadratic form is
`x ↦ 2m Re(c·α·β̄)` with `α = v^T x`, `β = v̄^T x`; this is the pull-back of the `2×2` Hermitian form
`[[0, c̄],[c, 0]]` (eigenvalues `±|c|`) under `x ↦ (α, β)`, so by AF Lemma 3.1 it has positive index
`≤ 1`. Subadditivity of the positive index gives `n_+(P_{≥2}+Q) ≤ #mult + p =: b`. Traces
(normalised by `aL²`, using `v_ρ·v_ρ = aL²` for all `ρ`): `tr P_1 = Σ_{simple on} |h(ρ)|² =: Σ_1`,
`tr P_{≥2} = N_mult := Σ_{mult on} m_ρ`, `tr Q = Σ_{off} m_ρ c_ρ` (real). AF Lemma 3.2 with
`(P, Q) = (P_1, P_{≥2}+Q)` gives

```text
s_1(Z) ≥ rank P_1 ≥ 2Σ_1 + 4(N_mult + Σ_off m c) − 4b − ‖W_h‖².
```

Since every multiple zero has `m ≥ 2` and every pair two zeros, `4b ≤ 2N_mult + 2N_off` with
`N_off := Σ_off m_ρ`. Substituting and regrouping `2(Σ_1 + N_mult + Σ_off m c) = 2 tr W_h` gives the
claim. The HS norm is `tr(W_h W_h^*) = Σ m m' c c̄' |v_ρ·v̄_ρ'|²/(aL²)²` and `v_ρ·v̄_ρ' = L(φ²)^(γ−γ̄')`. ∎

For `h ≡ 1` the defect vanishes and Theorem 1 is AF's chain (their eq. for Theorem A(i)), so the
theorem is a strict generalisation. The proof never uses the size of `h`: any polynomially bounded
`h` is admissible for the finite set `Z`. The passage from finite `Z` to the window `[T,2T]` with
truncated lattice is AF's tail estimate (their Proposition on `Ẽ`) with the weights inserted; with
polynomially bounded weights it needs a window whose Fourier transform decays faster than any
power (a Gevrey taper, as in AF Remark on Dirichlet averaging (§6.3)) and a smooth taper of the lattice in `k`. I have not
re-verified those two estimates with the weights; everything below that is called "exact" is
the finite-`Z` statement.

**Theorem 2 (T-109301, RH form).** Assume all zeros in `Z` lie on the critical line. Then for every
`h` as above,

```text
s_1(Z) ≥ 2 Σ_{ρ∈Z} m_ρ |h(ρ)|² − Σ_{ρ,ρ'∈Z} m_ρ m_ρ' |h(ρ)|² |h(ρ')|² S(γ_ρ−γ_ρ')² .
```

*Proof.* No off-line zeros; `c_ρ = |h(ρ)|²`, `γ` real. ∎

Two remarks. (i) The right side is a concave quadratic in the weights `w_ρ = |h(ρ)|²`; without the
constraint `w = 1` at multiple zeros its maximum over all weights is `1^T(S²)^{-1}1`, numerically
`0.79N` at height `10^4` (outputs/weighted_*.log), so the certificate class is far from exhausted
by uniform weights. The constraint is what makes the inequality a theorem, and `h = 1 + εBζ'`
satisfies it for free. (ii) The distinct-zero count follows in the same way: `2(s_1+s_2+p) ≥
3 tr W_h − 2Σ_1 + ... `; I do not pursue it.

## 2. Expansion in the weight parameter

**Proposition 3 (L-109302).** Let `h = 1 + εF` with `ε` real, `F = Bζ'`, and write `R_ρ := Re F(ρ)`,
`A_ρ := |F(ρ)|²`. Under RH (Theorem 2), with the bilinear form `⟨u,v⟩_S := Σ_{ρρ'} m m' u_ρ v_ρ' S²_ρρ'`,

```text
2 tr W_h − ‖W_h‖² = (2N − ⟨1,1⟩_S) + 4ε(Re S_1 − Λ_1) + 2ε²(S_2 − Λ_2 − 2Λ_2') − 4ε³Λ_3 − ε⁴Λ_4 ,
Λ_1 := ⟨R,1⟩_S,  Λ_2 := ⟨A,1⟩_S,  Λ_2' := ⟨R,R⟩_S,  Λ_3 := ⟨A,R⟩_S,  Λ_4 := ⟨A,A⟩_S .
```

Writing `X := Λ_1 − Re S_1 = Σ_ρ R_ρ D'_ρ` with `D'_ρ := Σ_{ρ'≠ρ} S²_ρρ'` (the local pair-correlation
density at `ρ`) and `Y := 2Λ_2 + 4Λ_2' − 2S_2`, the gain over the unweighted certificate is
`g(ε) = −4εX − ε²Y − 4ε³Λ_3 − ε⁴Λ_4`, so that, when the cubic and quartic terms are negligible at
the optimum `ε* = −2X/Y`,

```text
s_1 ≥ (2 − R(ψ) − o(1))N + 4X²/Y .
```

*Proof.* Expand `w_ρ w_ρ' = (1+2εR+ε²A)(1+2εR'+ε²A')` in `Σ mm' w w' S²` and `2Σ m w = 2N + 4εReS_1 +
2ε²S_2`; the unweighted part is AF's Theorem on `‖G̃‖²` with `⟨1,1⟩_S = (R(ψ)+o(1))N`. ∎

Mechanism. `X > 0` because the coherent part of the mollified derivative is positive
(`Re S_1 ∼ (19/24)LN`) and `D' > 0`; a negative `ε` lowers the weights of the simple zeros below
one while the multiple zeros stay at weight one, which is exactly BHB's device
(their `(1.2)`, AF §6(c)) transported to bandwidth one. The sign of `ε` is forced: for `ε > 0`
the certificate decreases. The anticorrelation of `|ζ'(ρ)|` with the local density lowers `X`
by about `18%` relative to the uncorrelated value `Re S_1 (R−1)` (numerics below); it does not
change the sign.

## 3. Numerical record (X-109303)

Zeros `n ∈ [n_0, 18816]` of Odlyzko's table with `ζ'(ρ)` from mpmath; local `L = log(γ̄/2π)` per
pair; band `|n−n'| ≤ 400`; edge-free inner window. BHB mollifier `P(x) = −θx² + (1+θ)x`,
`y = T^θ` at the window centre `T`. All zeros here are simple and on the line, so the RH form
(Theorem 2) is evaluated on the true configuration.

| window | `T` | `L` | AF unweighted `2−⟨1,1⟩_S/N` | best weighted, `θ=0.45` | `θ=0.35` | `θ=0.2` | `F=ζ'` | `|S_1|²/(S_2N)` (θ=.45) |
|---|---|---|---|---|---|---|---|---|
| 1000–18816 | 9799 | 7.35 | 0.6974 | **0.7450** (`ε·mean F = −0.100`) | 0.7389 | 0.7283 | 0.7146 | 0.7958 |
| 6000–18816 | 11906 | 7.55 | 0.6956 | **0.7428** (`−0.100`) | 0.7367 | 0.7263 | 0.7124 | 0.7916 |
| 12000–18816 | 14373 | 7.73 | 0.6945 | **0.7418** (`−0.100`) | 0.7356 | 0.7252 | 0.7111 | 0.7885 |

Decomposition (`θ = 0.45`; outputs/expansion_*.log):

| window | `Re S_1/(LN)` | `S_2/(L²N)` | `X/(LN)` | `Y/(L²N)` | `4X²/(YN)` | exact gain | cubic+quartic at optimum |
|---|---|---|---|---|---|---|---|
| 1000– | 0.842 | 0.892 | 0.2097 | 4.146 | 0.0424 | 0.0476 | −0.0068 |
| 6000– | 0.847 | 0.906 | 0.2102 | 4.190 | 0.0422 | 0.0472 | −0.0068 |
| 12000– | 0.846 | 0.909 | 0.2101 | 4.191 | 0.0421 | 0.0473 | −0.0067 |

The BHB limits are `19/24 = 0.792` and `57/64 = 0.891`; the finite-height first and second moments
are within `7%` and `2%` of them, and the two new ratios `X/(LN)`, `Y/(L²N)` are stable to three
digits across the windows. If they persist, the certificate's limit is `2/3 + 0.047 ≈ 0.714`
(flat window; the Montgomery–Taylor window adds its `0.006` to the base), above `19/27 = 0.7037`.
This is a projection, not a theorem: the asymptotics of `Λ_1, Λ_2, Λ_2'` and upper bounds for
`Λ_3, Λ_4` are the missing inputs. Note that `S_2/(L²N)` is already close to its limit, so
the first two rows are not a low-height artefact of the mollifier.

**The four functionals.** By Fourier inversion of `S² = ĝ/(aL)²` (`g = φ²⋆φ²`),
`⟨u,v⟩_S = (aL)^{-2} ∫ g(t) M_u(t) M_v(t)̄ dt` with `M_u(t) := Σ_ρ m_ρ u_ρ e^{itγ_ρ}`, `|t| ≤ L`, i.e.
`x = e^t ≤ T/2π`. So `Λ_1` is the cross-spectrum of the zero measure (Landau: spikes of mass
`(T/2π)Λ(n)` at `t = log n`) with the twisted first moment `Σ_ρ Bζ'(ρ) n^{iγ}`; `Λ_2` pairs the zero
measure with the twisted second moment `Σ_ρ |Bζ'(ρ)|² x^{iγ}`; `Λ_2'` is the mean square of the
twisted first moment over `x ≤ T`; `Λ_3, Λ_4` involve the twisted second moment in mean square.
The BHB machinery evaluates the untwisted moments; the twist `x^{iγ}` with `x` up to `T`
multiplies the effective mollifier length by `x`, far beyond the `T^{1/2−ε}` range of the
Gonek-lemma/large-sieve treatment. On the prime side the same objects are the second moments of
the Farey-supported measures `Σ_{k≤y}Σ_m (b(k)/k) a_ν(m) e(−m/k) δ_{2πm/k}` against the kernel `S²`,
whose off-diagonal (Farey neighbours at distance `≤ 1/L`, i.e. `|mk'−m'k| ≤ kk'/L`) is a bilinear
Farey sum. Either formulation is the named estimate to which the RH-conditional `≈ 0.71` reduces.
Bandwidth cannot be lowered to make the twists short: at bandwidth `λ` the uniform-weight optimum
is `1/μ_2(λ)` with `μ_2(λ) = 1/λ + λ/3` (AF Remark on `λ`), which is `0.632` at `λ = 3/4` and
below `2/3` for all `λ ≤ 0.79`.

## 4. The adjoined family gains nothing

**Proposition 5 (L-109304).** For the direct-sum family `{φ̂_k} ∪ {εFφ̂_k}` (test space `V_0 ⊕ F·V_0`),
the rank–trace certificate equals, under RH and at the AF scaling,

```text
(2 − R(ψ))N + 2ε²(S_2 − S_2^{pc}) − ε⁴ ⟨A,A⟩_S + O(ε⁶),   S_2^{pc} := Σ_{ρρ'} F(ρ)F(ρ')̄ S²_ρρ' ,
```

so the order-`ε²` gain is positive only if the mollified derivative is *anticorrelated* at
bandwidth one, `Σ_{ρ≠ρ'} F(ρ)F(ρ')̄ S² < 0`.

*Proof.* With `w_ρ = (v_ρ, εF(ρ)v_ρ)`, `tr = N + ε²S_2`, `‖·‖² = Σ mm'|1+ε²F F̄'|²S²`; the multiple
zeros load the first block only; AF's bookkeeping `tr P_1 + 2(#mult+p) ≤ N + ε²Σ_simple|F|²` and
the lemma give the display. ∎

Numerically (outputs/hybrid_*.log, `S_2^{pc}/S_2`): `1.14` for the BHB mollifier at `θ = 0.45`,
`1.11` at `θ = 0.35`, `1.07` at `θ = 0.2`, `1.03` for `ζ'` alone, `1.30` for `F = 1`
(Montgomery's `4/3`), and `0.92` only for the real alternating weight `Z'(γ)` (zero mean, gain
`0.002`). In the model `F = m + ξ` with a fluctuation form factor `κ ∈ [1/3, 1]`, the coefficient is
`N[(1−κ)σ² − m²/3]`, negative whenever `m²/(m²+σ²) > 2/3`, i.e. whenever BHB's ratio exceeds `2/3`.
Adjoining and multiplying are therefore not interchangeable: only the multiplicative family
moves the trace normalisation of the simple zeros relative to the multiple ones.

## 5. Ceiling for unconditional trace-moment certificates

**Proposition 6 (T-109305; proved modulo AF §6(e) and the Lean-certified ceiling).** Call
*unconditional trace-moment certificate* any lower bound for `s_1/N` that is a function of the
numbers `tr G̃_λ^k` of compressions of Weil's form to bandlimited families of bandwidth `λ ≤ 1`, in
the range `kλ < 2` where the prime side evaluates them without hypothesis (the Rudnick–Sarnak
range; AF §6(e)), together with the on/off partition. Every such certificate is `≤ 0.6819 < 19/27`.

*Proof.* At bandwidth `λ ≤ 2/3` the family has `d = λN(1+o(1))` elements (AF §2.3), so
`rank P_1 ≤ d` and the certificate is `≤ λ ≤ 2/3`. For `2/3 < λ ≤ 1` only `k ≤ 2` is available, and
a two-moment certificate at bandwidth `λ` is a bandwidth-one certificate in AF's sense (its data are
the first two trace moments against test functions of Fourier support in `[−λ,λ] ⊂ [−1,1]`), hence
`≤ p_0 ≤ 0.6818287 + 2.55·10^{-6}(|r'(1)|+∫|r''|)` by `Zeta23.PairCeiling.ceiling_law256`. ∎

The weighted certificate of Theorem 1 is outside this class: `h = 1 + εBζ'` is not bandlimited,
and its data are the `Λ_k`, not trace moments of an unweighted compression. This is why it can
exceed `0.6819` (numerically it does, under RH).

## 6. The unconditional obstruction (R-109306)

By Theorem 1 and Proposition 3, with `ε < 0`,

```text
s_1 ≥ (2 − R(ψ))N + 4|ε|(X − ½S_1^off) − ε²(Y − 2S_2^off) − 4ε³Λ_3 − ε⁴Λ_4 + o(N),
S_1^off := Σ_{off} m_ρ Re(F(ρ) + F(1−ρ)),   S_2^off := Σ_{off} m_ρ F(ρ)F(1−ρ) ,
```

where now `Λ_k` are the unconditional (complex-`γ`) functionals of Theorem 1 and everything except
`S_1^off, S_2^off` is a prime-side quantity. The defect is exactly the share of the mollified first
and second moments carried by off-line zeros. A shallow pair (depth `≪ 1/L`) has `c_ρ ≈ |h(ρ)|² ≈ 3/4`
at the optimum and costs `≈ 1/2` per zero, so the certificate beats `2/3` only if
`N_off ≲ 0.09N`, which is not known (AF give `N_off ≤ N/3`, Selberg's density gives `o(N)` only at
depth `≫ 1/L`). What would close it: `S_1^off ≤ (2−δ)X` and `S_2^off ≥ −CN L²` for some `δ, C > 0`,
i.e. a *mollified zero-density estimate*: the off-line zeros carry less than a fixed fraction of
`Σ_ρ Re Bζ'(ρ) D'_ρ`. No such statement is available from the HS norm alone (Cauchy–Schwarz gives
`Σ_off m|c_ρ| ≤ (‖W_h‖² N_off)^{1/2} ≈ 0.66N`, useless). This, and not the choice of certificate, is
the distance to an unconditional 70%: pair correlation beyond support one, or a zero-density
statement at depth `1/L` weighted by the mollified derivative.

## 7. Dirichlet L-functions

**Proposition 7 (T-109307).** Let `χ` be primitive mod `q`. Theorems 1–2 hold verbatim for `L(s,χ)`
with `h(s) = 1 + εB(s)L'(s,χ)`, `c_ρ = h(ρ)h̃(1−ρ)`, `h̃(s) := 1 + εB̄(s)L'(s,χ̄)` (conjugate coefficients),
and `tr W_h = N_χ + ε(Σ_ρ F(ρ) + Σ_ρ F̃(1−ρ)) + ε² Σ_ρ F(ρ)F̃(1−ρ)`.

*Proof.* The zero set of `L(s,χ)` is closed under `ρ ↦ 1−ρ̄` (functional equation and
`L(s̄,χ)̄ = L(s,χ̄)`); `h(1−ρ̄)̄ = h̃(1−ρ)`; on the line `c_ρ = |h(ρ)|²`; `F = BL'(·,χ)` vanishes at
multiple zeros. The rest is Theorem 1. ∎

Consequences. (i) For each fixed primitive `χ` in the `T`-aspect, AF's Theorem B gives `2/3` and
`0.6725`; the weighted certificate reduces `≥ 70%` under GRH to the same four functionals with
`Λ(n)χ(n)` in place of `Λ(n)` and BHB's moments for `L'(ρ,χ)` (the `q = 1` contour computation is
identical; the Gonek-lemma part carries `χ`), and unconditionally to the same off-line defect. The
`q`-aspect is no easier: the diagonal-dominance range is `X ≤ (qT)^{1}` and the ceiling of
Proposition 6 is unchanged. (ii) On average over primitive `χ` mod `q ≤ Q` AF's Remark on Dirichlet
averaging already gives `0.811` simple on the line and `0.905` distinct, unconditionally, because the
large sieve raises the bandwidth to `3/2`; under GRH the family average is `91%` simple
(Chandee–Lee–Liu–Radziwiłł 2014, pair correlation on `|α| < 2` by the asymptotic large sieve;
Özlük had `86%`), so AF's `0.811` is the unconditional counterpart of a conditional `0.91`. So "70%
for all Dirichlet `L`-functions" is already true on average and is, for each individual `χ`,
exactly the zeta problem again.

## 8. What is proved, what is reduced, what is refuted

- Proved exact: T-109300, T-109301, L-109302, L-109304, L-109308.
- Proved modulo two cited inputs (AF's Rudnick–Sarnak-range remark and the Lean ceiling): T-109305.
- Numerical record: X-109303 (RH numerics on the true zeros; three windows; stable ratios).
- Reduction: R-109306 lists exactly the non-computable quantities (`S_1^off, S_2^off`) and the
  missing asymptotics (`Λ_1, Λ_2, Λ_2'`; bounds for `Λ_3, Λ_4`).
- Not proved: any unconditional proportion above AF's `2/3` (or `0.6725`), for `ζ` or for any
  `L(s,χ)`; any RH-conditional proportion above `19/27`. The projected `≈ 0.71` under RH is a
  numerically supported conjecture with a precise analytic target.

## Sources

Alpöge–Furman, arXiv:2608.13637v2 (Lemmas 3.1–3.2, Prop. on `Ẽ`, Theorem on `‖G̃‖²`, §6(a)(c)(e),
`Zeta23.PairCeiling.ceiling_law256`, Remark on Dirichlet averaging); Bui–Heath-Brown, arXiv:1302.5018
(Lemmas 1–2, eq. (8), Section 2 end); Conrey–Ghosh–Gonek, PLMS 76 (1998); Montgomery, PSPM 24 (1973);
Rudnick–Sarnak, Duke 81 (1996); Gonek, Invent. Math. 75 (1984), and Contemp. Math. 143 (1993) for
Landau's formula; Chandee–Lee–Liu–Radziwiłł, Q. J. Math. 65 (2014).

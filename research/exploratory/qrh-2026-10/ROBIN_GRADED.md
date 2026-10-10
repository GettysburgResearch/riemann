# A Θ-graded Robin statement (conditional on QRH-IMPORT)

```text
Status: IMPORTED classical theorems (Sec. 1) + PROPOSED derivations (Secs. 2-3, ours, unreviewed)
  + CONDITIONAL on QRH-IMPORT (Sec. 4) + HEURISTIC (Sec. 5.3) + EMPIRICAL sanity numerics (Sec. 6).
  RH is unsolved; nothing here proves or disproves it.
Scope: asymptotic/cofinal. Bounds hold for n >= n_0(theta) with n_0 NOT made effective.
  The bounds limit the relative SIZE of a Robin or Nicolas violation. They exclude no violation.
Exact sources or dependencies: Robin, J. Math. Pures Appl. 63 (1984) 187-213 (via Lagarias
  arXiv:math/0008177v2, Nicolas-Sondow arXiv:1211.6944v4, Caveney-Nicolas-Sondow arXiv:1110.5078v2,
  Washington-Yang arXiv:2008.04787v1); Nicolas, J. Number Theory 17 (1983) 375-388 (via Nicolas,
  Acta Arith. 155 (2012) = arXiv:1202.0729v2); Ingham (1932) Thms 28 and 30; Davenport Ch. 12;
  QRH-IMPORT (INTAKE.md). The Robin and Nicolas originals were NOT accessed (Sec. 1.4).
What was actually run: scripts/robin_graded_numerics.py (double/long-double floats; CA self-test
  against OEIS A004490; CA numbers and primorials with largest prime <= 1e8; Ingham psi_1 formula
  spot check with 300 zero pairs). No directed or certified arithmetic.
Smallest remaining gap: Lemma K (Sec. 2) is the load-bearing new step. For the Robin programme the
  gap is an exponent: QRH bounds violations at scale (log n)^(-1/8), while Robin's sign lives at
  scale (log n)^(-1/2). That difference is the same 3/8 that appears elsewhere in this folder.
```

Notation. `f(n) = σ(n)/(n log log n)`, `f_φ(n) = n/(φ(n) log log n)`, `N_k = p_1⋯p_k` (primorial),
`ϑ(x) = Σ_{p≤x} log p`, `ψ` Chebyshev's function, `S(x) = ϑ(x) − x`, `R(x) = ψ(x) − x`.
`Θ = sup Re ρ` over nontrivial zeros. `H(θ)` means that `ζ(s) ≠ 0` for `Re s > θ`, so QRH-IMPORT implies `H(7/8)`; write `QRH_ζ := H(7/8)`, the only part used here.
`w(t) = t^{−2}(1/log t + 1/log² t)` and `K(x) = ∫_x^∞ S(t) w(t) dt` (Nicolas's notation).

## 0. Bottom line

1. **Upper envelope (PROPOSED).** Assume `H(θ)` with `1/2 < θ < 1`. Then for every `δ > 0`, every `n ≥ n_0(θ,δ)` satisfies
   `f(n) < f_φ(n) ≤ e^γ (1 + (C_θ+δ)(log n)^{θ−1}/log log n)`, where `C_θ = (3−θ)/(1−θ) · A` and `A = Σ_ρ 1/|ρ(ρ+1)| ≤ 0.04643`.
   - Under QRH-IMPORT: `C_{7/8} = 17A ≤ 0.79`. So `σ(n)/n ≤ e^γ log log n + 1.41 (log n)^{−1/8}` cofinally.
   - The constant is ineffective as stated.
2. **The exponent is sharp, giving a Θ-graded Robin criterion (PROPOSED assembly).** Define the Robin violation exponent `v_R = limsup log V(n)/log log n` over the `n` with `V(n) := f(n)/e^γ − 1 > 0`. Then:
   - `v_R = −∞` if RH holds (Robin);
   - `v_R = Θ − 1` if RH fails. The upper half is item 1. The lower half is Robin's Ω-theorem, with every exponent `β ∈ (1−Θ, 1/2)`.
   - Hence, for every `θ ∈ [1/2,1)`, `Θ ≤ θ ⟺ v_R ≤ θ − 1`. In particular **`QRH_ζ` (Θ ≤ 7/8) ⟺ for every ε > 0, `σ(n) < e^γ n log log n·(1 + (log n)^{−1/8+ε})` for all sufficiently large n.** QRH-IMPORT implies this inequality; the converse gives only `QRH_ζ`.
3. **Nicolas (primorials), PROPOSED.** Under `H(θ)`, `|log(f_φ(N_k)/e^γ)| ≤ (C_θ + o(1)) p_k^{θ−1}/log p_k`. Under QRH-IMPORT this is `(log N_k)^{−1/8}/log log N_k` up to the constant.
4. **Where Θ enters.** The leading Θ-dependence is the Mertens integral `K(x)`. Bounding it needs only the absolutely convergent explicit formula for `ψ_1 = ∫ψ` (no Perron truncation). The boundary term `S(x)/(x log x)` of the Mertens remainder cancels *exactly* against the `log log N` normalisation. That cancellation is why the scale is `x^{θ−1}/log x`, not `x^{θ−1} log x`. The pointwise Perron bound `ψ(x) − x ≪ x^θ log² x` is used only to make a second-order term `S(x)²/(x² log x)` lower order.
5. **Repository impact (Sec. 5).** The reviewed Robin packet is finite exact arithmetic: the barrier to 5582, the canonical reduction and the rational bounded-tail envelope. QRH-IMPORT changes none of its statements or constants, and shrinks no reviewed search region.
   - It does supply cofinal, ineffective constraints on hypothetical violators: `log(n/N_{ω(n)}) ≪ (log n)^{7/8}`, and every prime `q ≪ (log n)^{1/8}` divides `n` with `q^{a_q+1} ≫ (log n)^{1/8}`.
   - It cannot decide the sign at colossally abundant numbers. The QRH envelope sits at exponent `−1/8`; the RH margin at `−1/2`.

## 1. Imported classical statements (exact, with quantifiers)

**R1 (Robin 1984, Thm 1).** RH ⟺ `σ(n) < e^γ n log log n` for every integer `n > 5040`. [The repository already imports this; see `research/integrated/robin/finite-robin-foundations.md`.]

**R2 (Robin 1984, Thm 2; unconditional).** For all `n ≥ 3`, `σ(n) < e^γ n log log n + 0.6483 n/log log n`. Lagarias quotes the constant as `0.6482…` with `n ≥ 3`, from Robin's Thm 2. CNS (arXiv:1110.5078v2, eq. (2)) give the equivalent form `G(n) < e^γ + 0.6483/(log log n)²`.

**R3 (Robin 1984, §4, Prop. 1; as stated by Lagarias, arXiv:math/0008177v2, Prop. 3.2).** *If RH is false, then there exist constants `0 < β < 1/2` and `C > 0` such that `σ(n) ≥ e^γ n log log n + C n log log n/(log n)^β` for infinitely many `n`.*
- Lagarias's proof note: "β can be chosen to take any value `1 − b < β < 1/2`, where `b = Re(ρ)` for some zero ρ of ζ(s) with `Re(ρ) > 1/2`, and `C > 0` must be chosen sufficiently small, depending on ρ."
- Since Θ is a supremum, every `β ∈ (1−Θ, 1/2)` is admissible.
- In our notation: `V(n) ≥ (C e^{−γ})(log n)^{−β}` infinitely often.

**R3′ (secondary attribution).** Washington and Yang (arXiv:2008.04787v1, proof of Lemma 4.5) cite Robin p. 205 for the two-sided form over colossally abundant (CA) numbers M: if RH is false, `f(M) = e^γ(1 + Ω_±((log M)^{−β}))`.

**R4 (Ramanujan, RH-conditional; quoted in Nicolas–Sondow, arXiv:1211.6944v4, p. 3).** Under RH, `limsup_{n→∞}(σ(n)/n − e^γ log log n)√(log n) ≤ −e^γ(2√2 − 4 − γ + log 4π) = −1.393…`.
- Note that `2√2 − 4 − γ + log 4π = (2√2 − 2) − β_N`, with `β_N := Σ_ρ 1/(ρ(1−ρ)) = 2 + γ − log 4π = 0.04619…`.

**R5 (Robin's CA reduction; Nicolas–Sondow p. 4).** If `N′ < N″` are consecutive CA numbers, then `N′ < n < N″ ⟹ G(n) ≤ max(G(N′), G(N″))`, where `G(n) = f(n)`.

**N1 (Nicolas 1983).** RH ⟺ `N_k/φ(N_k) > e^γ log log N_k` for all `k ≥ 1`. If RH is false, both `>` and `<` hold for infinitely many `k`. [Nicolas 2012, Intro; CLMS arXiv:math/0604314v2 §2.1.]

**N2 (Nicolas 1983, Prop. 1 = Nicolas 2012, Lemma 2.1; unconditional).** Put `f(x) = e^γ log ϑ(x) ∏_{p≤x}(1 − 1/p)`, so that `f(p_k) = e^γ/f_φ(N_k)`. Then for every `x ≥ 121`:

    K(x) − S(x)²/(x² log x)  ≤  log f(x)  ≤  K(x) + 1/(2(x−1)).

**N3 (Nicolas 1983, Th. 3(c), as quoted in Nicolas 2012 (1.10)).** If RH fails, there exists `b`, `0 < b < 1/2`, such that `log f(x) = Ω_±(x^{−b})`.
- *Our reading (not checked against the 1983 text):* the Landau-oscillation proof gives every `b ∈ (1−Θ, 1/2)`, exactly as Lagarias records for R3.
- The upper limit `1/2` comes from the real singularity produced by prime squares (`ψ − ϑ ≈ √x`). The lower limit comes from the singularities `x^{ρ−1}`.

**N4 (Nicolas 2012, Thm 1.1; RH-conditional).** Under RH, with `c(n) = (n/φ(n) − e^γ log log n)√(log n)`:
- `limsup c(n) = e^γ(2+β_N) = 3.644…`;
- `c(N_k) ≥ c(2) = 2.2085…` for every `k`.

Each of these is equivalent to RH.

**I1 (Ingham 1932, Thm 28; absolutely convergent explicit formula).** For `x ≥ 1`,
`ψ_1(x) := ∫_0^x ψ = x²/2 − Σ_ρ x^{ρ+1}/(ρ(ρ+1)) − x log 2π + ζ′(−1)/ζ(−1) − Σ_{r≥1} x^{1−2r}/(2r(2r−1))`.
- *Spot check (EMPIRICAL, Sec. 6):* with 300 zero pairs the formula reproduces the exact `ψ_1(x)` at `x = 20.5, 50.5, 100.5` to `2·10⁻⁴`, `5·10⁻³` and `0.09`. Each difference is within the zero-tail bound.

**I2 (Ingham 1932, Thm 30; via Perron / the truncated explicit formula).** If ζ has no zeros with `Re s > θ`, then `ψ(x) − x = O(x^θ log² x)`.

**D (Davenport, Ch. 12; unconditional).** `Σ_ρ Re(1/ρ) = 1 + γ/2 − ½ log 4π = 0.0230957…`. Every nontrivial zero has `|Im ρ| > 14.13`.

### 1.4 Source trail

| Statement | Read in | sha256 (PDF as fetched) |
|---|---|---|
| R3 range of β, R2 | Lagarias, arXiv:math/0008177v2 §2–3 | `49cd7ad2…` |
| R2 (G-form), N1 | Caveney–Nicolas–Sondow, arXiv:1110.5078v2 | `2821d356…` |
| R4, R5, N1 | Nicolas–Sondow, arXiv:1211.6944v4 | `bc62cce6…` |
| N1–N4 | Nicolas, arXiv:1202.0729v2 (= Acta Arith. 155) | `d5ff55f7…` |
| R3′ | Washington–Yang, arXiv:2008.04787v1 | `59097fbe…` |
| Robin abstract (R1–R3 informal) | search-engine snippet of the J. Math. Pures Appl. abstract | — |
| finite range, context only | Morrill–Platt, arXiv:1809.10813v4, Thm 13 | `2214cba1…` |

Not accessed: Robin 1984 and Nicolas 1983 (originals), Ingham, Davenport, Rosser–Schoenfeld. **R3's β-range is second-hand (Lagarias) and N3's b-range is our reading.** These are the import risks.

## 2. Lemma K: the graded Mertens integral (PROPOSED)

**Lemma K.** Assume `H(θ)` with `1/2 < θ < 1`. Put `A = Σ_ρ 1/|ρ(ρ+1)|`. Then, as `x → ∞`,

    |K(x)| ≤ A (1 + 2/(1−θ)) · x^{θ−1}/log x · (1 + O_θ(1/log x)) + O(x^{−1/2}/log x).

*Proof.* Write `S = R − (ψ − ϑ)`. Then `K = I − J_0` with `I(x) = ∫_x^∞ R w` and `J_0(x) = ∫_x^∞ (ψ−ϑ) w`.

**The term `J_0`.** By Chebyshev, `0 ≤ ψ(t) − ϑ(t) ≤ ψ(√t) + ψ(t^{1/3}) log t/log 2 ≪ √t`. Hence `0 ≤ J_0(x) ≪ ∫_x^∞ t^{−3/2}/log t dt ≪ x^{−1/2}/log x`.

**The term `I`.** Let `R_1(t) = ∫_0^t R = ψ_1(t) − t²/2`. By I1 and `|t^{ρ+1}| ≤ t^{θ+1}`, for `t ≥ 1`:

    |R_1(t)| ≤ A t^{θ+1} + t log 2π + |ζ′(−1)/ζ(−1)| + log 2.

Hence `R_1(Y) w(Y) → 0`, and integration by parts gives `I(x) = −R_1(x) w(x) − ∫_x^∞ R_1(t) w′(t) dt`. Here `−w′(t) = t^{−3}(2/log t + 3/log² t + 2/log³ t) > 0`. Then

    |R_1(x) w(x)| ≤ A x^{θ−1}/log x · (1 + 1/log x) + O(1/(x log x)),
    ∫_x^∞ |R_1| |w′| ≤ (2A/log x)(1 + O(1/log x)) ∫_x^∞ t^{θ−2} dt + O(1/(x log x))
                    = (2A/(1−θ)) x^{θ−1}/log x · (1 + O(1/log x)) + O(1/(x log x)).

Add the two bounds. ∎

**Bound on A (unconditional).** `|ρ+1| > |ρ|`, so `A ≤ Σ 1/|ρ|²`.
- Average over the involution `ρ ↦ 1 − ρ̄`, which preserves `γ = Im ρ` and sends `β ↦ 1 − β`.
- The pair contributes at most `2/γ²` to `Σ 1/|ρ|²` and at least `1/(γ²+1)` to `Σ Re(1/ρ)`.
- With D this gives `Σ 1/|ρ|² ≤ 2(1 + 14.13^{−2}) · 0.0230957 ≤ 0.04643`.
- Under RH, `Σ 1/|ρ|² = β_N = 0.04619` exactly.

**Remark K′ (sharper constant, sketch).** Integrate the truncated explicit formula `R(t) = −Σ_{|γ|≤T} t^ρ/ρ + O(t log²(tT)/T)` against `w`, and let `T → ∞`. Use Nicolas's Lemma 2.2 (`F_z(x) = x^{z−1}/((1−z) log x) + r_z(x)`, with the second integration by parts (2.6) giving `|r_ρ/ρ| ≤ |1−ρ|^{−2} x^{β−1}/log² x · (1 + 2/((1−β)log x))`). This gives

    −I(x) = Σ_ρ x^{ρ−1}/(ρ(1−ρ) log x) + O_θ(x^{θ−1}/log² x),

so the leading constant improves from `(3−θ)A/(1−θ)` to `A′ = Σ 1/|ρ(1−ρ)| ≤ Σ 1/|ρ|² ≤ 0.04643`. Under RH this is Nicolas's `W(x)` term, `|W| ≤ β_N`. We have not written out the interchange of sum and integral, so the sharper constant is a **sketch**. Lemma K does not depend on it.

**Perron-free variant.** Lemma K uses only I1, which is absolutely convergent and needs no truncation. The pointwise Perron bound I2 enters only through the second-order term in N2. Without I2, differencing `ψ_1` gives the following, because ψ is monotone:
- `hψ(x) ≤ ψ_1(x+h) − ψ_1(x) = hx + h²/2 + R_1(x+h) − R_1(x)`;
- taking `h = x^{(1+θ)/2}` gives `R(x) ≪ x^{(1+θ)/2}`, so `S(x)²/(x² log x) ≪ x^{θ−1}/log x`.

That is the same exponent with a worse constant. So the **exponent** `θ − 1` in everything below follows from the absolutely convergent formula alone.

## 3. Consequences of `H(θ)` (PROPOSED)

### 3.1 Primorials (Nicolas side)

**Proposition N.** Assume `H(θ)` with `1/2 < θ < 1`, and let `x = p_k`. Then

    −(C_θ + o(1)) x^{θ−1}/log x ≤ log( N_k / (e^γ φ(N_k) log log N_k) ) ≤ (C_θ + o(1)) x^{θ−1}/log x,

with `C_θ = (3−θ)A/(1−θ)`, or the sketch constant `A′` from K′. Since `ϑ(p_k) = log N_k ~ p_k`, the scale equals `(log N_k)^{θ−1}/log log N_k · (1 + o(1))`.

*Proof.* By N2, `log(f_φ(N_k)/e^γ) = −log f(x)` lies in `[−K(x) − 1/(2(x−1)), −K(x) + S(x)²/(x² log x)]`. By I2, `S(x)² ≪ x^{2θ} log⁴ x`, so the correction is `O(x^{2θ−2} log³ x) = o(x^{θ−1}/log x)`. Apply Lemma K. ∎

*Reconstruction of N2.* N2 is imported, but we checked that it follows from three facts:
- Stieltjes integration gives `Σ_{p≤x} 1/p = log log x + B_1 + S(x)/(x log x) − K(x)`.
- Mertens fixes the constant: `Σ_{p≤x} −log(1−1/p) = log log x + γ + S(x)/(x log x) − K(x) − η(x)`, with `0 < η(x) = Σ_{p>x}(−log(1−1/p) − 1/p) ≤ 1/(2(x−1))`.
- `log log ϑ(x) − log log x = log(1 + log(1+u)/log x)`, with `u = S(x)/x`, lies in `[u/log x − u²/log x, u/log x]`.

The boundary term `S(x)/(x log x)` cancels exactly. Only `K(x)` survives at first order. Under RH, `−K = −I + J_0` gives Nicolas's `(2 + W(x))/(√x log x)`. In this form the whole `2` is `J_0 ≈ ∫_x^∞ √t w(t) dt ≈ 2/(√x log x)`, which comes from prime squares (`ψ − ϑ`). The zeros give `W`.

### 3.2 All integers (Robin side)

**Proposition R.** Assume `H(θ)` with `1/2 < θ < 1`. For every `δ > 0` there is an `n_0(θ, δ)` such that for all `n ≥ n_0`:

    f(n) < f_φ(n) ≤ e^γ ( 1 + (C_θ + δ) (log n)^{θ−1} / log log n ),

equivalently `σ(n)/n < n/φ(n) ≤ e^γ log log n + e^γ(C_θ+δ)(log n)^{θ−1}`.

*Proof.* Let `k = ω(n)`, `L = log n` and `y = log N_k = ϑ(p_k)`.
1. **Elementary reduction.** `σ(n)/n = ∏(1−p^{−a−1})/(1−p^{−1}) < n/φ(n)`. Since `p/(p−1)` decreases in `p`, `n/φ(n) ≤ N_k/φ(N_k)`. Also `N_k ≤ rad(n) ≤ n`, so `y ≤ L`. Hence for `k ≥ 2`: `f_φ(n) ≤ f_φ(N_k) · log y / log L`.
2. **Small k.** For `k < k_1`, `f_φ(n) ≤ max_{j<k_1} (N_j/φ(N_j))/log L < e^γ` once `L` is large.
3. **Large k.** By Proposition N, together with `p_k ≥ y(1 − o(1))`, for `k ≥ k_1(θ, δ)` we have `f_φ(N_k) ≤ e^γ(1 + c y^{θ−1}/log y)`, where `c = C_θ + δ`. Hence `f_φ(n) ≤ e^γ g(y)/log L` with `g(y) = log y + c y^{θ−1}`.
4. **Monotonicity.** `g′(y) = 1/y − c(1−θ) y^{θ−2} > 0` once `y^{1−θ} > c(1−θ)`. So for `y_0 ≤ y ≤ L` we get `g(y) ≤ g(L) = log L + c L^{θ−1}`.
5. **Remaining range.** For `y < y_0`, step 2 applies. ∎

**Specialisation (CONDITIONAL on QRH-IMPORT, θ = 7/8).** `C_{7/8} = 17A ≤ 0.789` and `e^γ C_{7/8} ≤ 1.406`. So, cofinally,

    σ(n)/n ≤ e^γ log log n + 1.41 (log n)^{−1/8},    f(n)/e^γ − 1 ≤ 0.79 (log n)^{−1/8}/log log n.

With the K′ sketch constant, the factor `0.79` becomes `0.0465`.

**Calibration (do not over-read).** `(log n)^{−1/8}` decays very slowly.
- With the Lemma K constant (`0.79`; proved here, unreviewed), the QRH envelope beats Robin's unconditional R2 (`f(n)/e^γ − 1 < 0.364/(log log n)²`) only once `log log n ≳ 35`, that is `log n ≳ 10^{15}`.
- `n_0` is not effective in any case.

### 3.3 The violation exponent equals Θ − 1

**Theorem V (PROPOSED assembly of Prop. R with R1–R3).** Let `V(n) = f(n)/e^γ − 1` and `v_R = limsup_{n→∞, V(n)>0} log V(n)/log log n`, with `v_R = −∞` if `V(n) > 0` only finitely often.
- If RH holds, `v_R = −∞` (R1).
- If RH fails, `v_R = Θ − 1 ∈ (−1/2, 0]`.

*Proof for RH false.*
- *Lower bound.* By R3, for each `β ∈ (1−Θ, 1/2)`, `V(n) ≥ c(log n)^{−β}` for infinitely many `n`. So `v_R ≥ −β` for all such `β`, and `v_R ≥ Θ − 1`.
- *Upper bound, Θ < 1.* `H(Θ)` holds, and Prop. R with `θ = Θ` gives `v_R ≤ Θ − 1`.
- *Upper bound, Θ = 1.* R2 gives `V(n) < 0.364/(log log n)²`, so `v_R ≤ 0`. ∎

**Corollary (Θ-graded Robin criterion).** For `θ ∈ [1/2, 1)`:

    Θ ≤ θ  ⟺  v_R ≤ θ − 1  ⟺  ∀ε>0 ∃n_ε ∀n ≥ n_ε:  σ(n) < e^γ n log log n · (1 + (log n)^{θ−1+ε}).

- At `θ = 1/2` this is a weak, cofinal shadow of Robin's sharp criterion R1.
- At `θ = 7/8` it is a **Robin-language equivalent of `QRH_ζ`** (the ζ-part of QRH-IMPORT). The `ε` and the ineffective `n_ε` are essential: unlike R1, this criterion has no finite threshold.

**Nicolas analogue.** Proposition N gives `limsup_k log|log(f_φ(N_k)/e^γ)| / log p_k ≤ Θ − 1`.
- With N3 (if the b-range reading holds), equality holds when RH fails, in both the `Nicolas-violation` direction and the opposite direction.
- Under RH, N4 gives `f_φ(N_k)/e^γ − 1 ≍ 1/(√p_k log p_k)` with positive sign. The exponent is `−1/2 = Θ − 1` in that case too, but there are no violations.

## 4. Statements conditional on QRH-IMPORT (used only through its ζ-part `QRH_ζ`: Θ ≤ 7/8)

These come from Sec. 3 at `θ = 7/8`. Every bound holds for `n ≥ n_0`, which is not effective.

| Object | Bound under QRH-IMPORT | Under RH (for comparison) |
|---|---|---|
| Robin violation size `V(n)` | `≤ 0.79 (log n)^{−1/8}/log log n` | no violation for `n > 5040` |
| Robin violation exponent `v_R` | `≤ −1/8` (⟺ `QRH_ζ`; implied by QRH-IMPORT) | `−∞` |
| Nicolas deviation at primorials | `\|log(f_φ(N_k)/e^γ)\| ≤ 0.79 p_k^{−1/8}/log p_k` | `f_φ(N_k)/e^γ − 1 = c(N_k)/(e^γ√(log N_k) log log N_k)`, `c(N_k) ∈ [c(2), e^γ(2+β_N))` for `k ≥ 120569` (N4) |
| CA numbers, largest prime x | zero term `≤ 0.79 x^{−1/8}/log x`; second-order term `O(x^{−1/4} log³ x)` | `≤ −(2√2−2−β_N)/(√x log x)` (R4) |
| non-squarefree mass of a violator, `log(n/N_{ω(n)})` | `≤ c (log n)^{7/8}` (S1) | — |
| small primes in a violator | every `q ≤ c (log n)^{1/8}` divides `n`, and `q^{a_q+1} ≥ c′ (log n)^{1/8} log log n` (S2) | — |

**(S1)–(S2), PROPOSED.** From the proof of Prop. R, a violator satisfies `log L − log y < c y^{θ−1}`, so `L − y ≤ c′ L^θ`. This is (S1). Writing `σ(n)/n = (n/φ(n)) ∏_{p|n}(1 − p^{−a_p−1})`, a violator needs `Σ_{p|n} p^{−a_p−1} ≲ c L^{θ−1}/log L`. A prime `q ∤ n` costs a factor `1 − 1/q` against the envelope. Together these give (S2).
- For comparison, unconditionally, Rosser–Schoenfeld's `n/φ(n) < e^γ log log n + 2.51/log log n` gives only `log(n/N_{ω(n)}) ≲ 1.41 log n/log log n` and `q^{a_q+1} ≳ (log log n)²`.
- CA numbers satisfy (S1) and (S2) with room to spare: `log(N/rad N) ≈ √(2 log N)` and `p^{a_p+1} ≈ p log N`. So (S1)–(S2) do not reduce the cofinal search class to anything finite.

## 5. What this means for the repository's Robin programme

### 5.1 Reviewed packet: unaffected

`research/integrated/robin/finite-robin-foundations.md` contains:
1. the exact barrier on `5041 ≤ n ≤ 5582`;
2. the canonical (Hardy–Ramanujan) transform `n ↦ H(n)` with `H(n) ≤ n`, `I(H(n)) ≥ I(n)`;
3. the nested-prefix encoding;
4. the exact powered bounded-tail envelope `I(P∏q_i^{b_i})^d ≤ (I_P I(R))^d M_0^a V`.

All four are finite exact (rational or directed) arithmetic, or purely structural. None uses an analytic input about zeros, so **QRH-IMPORT changes no statement, no constant and no search region** in the packet. The "larger certificate programme" (`10^54`, `10^100` traversals) sits far below any range where Sec. 3 says anything. The asymptotic bounds have ineffective thresholds, and at `log n ≈ 124–230` even the leading term is useless.

### 5.2 The open unbounded canonical tail: graded, not closed

- Sec. 3 says that **if** a canonical violator exists far out, its relative excess is at most `(log n)^{−1/8}/log log n` (times a constant). It is also near-squarefree in the sense of (S1)–(S2).
- **A relative-size bound does not exclude violations.** To exclude them one needs the sign of `log f` at the scale `(log n)^{−1/2}/log log n`, which is the RH margin (R4, N4). QRH-IMPORT gives the scale `(log n)^{−1/8}`.
- The exponent gap `7/8 − 1/2 = 3/8` (Θ − 1/2 ≤ 3/8 under QRH) is the same `3/8` recorded in [CONDITIONAL_CONSEQUENCES.md](CONDITIONAL_CONSEQUENCES.md) for every other RH-equivalent premise in the repository.
- **Canonical ≠ CA** (packet "Common misreadings"). R5 lets an analyst restrict to CA numbers. There, under QRH, the zero term `−I(x)` is `O(x^{−1/8}/log x)` and the second-order term `S²/(x² log x)` is `O(x^{−1/4} log³ x)`. Both dominate the structural RH margin `(2√2−2)/(√x log x)`, so QRH alone cannot decide the sign at any large CA number.
- (S1)–(S2) could become cofinal pruning rules for a future tail theorem, but only after the constants and `n_0` are made explicit. That requires explicit versions of I1 and I2 under `H(7/8)`, which have not been done.

### 5.3 A route by which QRH *would* enlarge a finite range (HEURISTIC, not carried out)

This route is not the repository's, but it is the one place where a half-plane hypothesis acts on finite ranges. Fix a height `T` to which RH has been verified (`T = 3·10^{12}`, Platt–Trudgian, as cited by Morrill–Platt). At a CA number with largest prime `x`, the leading expansion (Sec. 3.1 with R4) reads:

    log f(N) − γ ≈ Σ_ρ x^{ρ−1}/(ρ(1−ρ) log x) − (2√2−2)/(√x log x).

- Zeros below `T` contribute at most `β_N x^{−1/2}/log x`.
- Zeros above `T` contribute at most `ε(T) x^{Θ_T−1}/log x`, where `ε(T) = Σ_{|γ|>T} 1/|ρ(1−ρ)| ≈ (log(T/2π)+1)/(πT) ≈ 3.0·10^{−12}`.
- The sign stays negative while `ε(T) x^{Θ_T−1/2} < 2√2−2−β_N ≈ 0.78`:
  - `Θ_T ≤ 1` (no extra hypothesis): `x ≲ (0.78/ε(T))² ≈ 7·10^{22}`;
  - `Θ_T ≤ 7/8` (QRH-IMPORT): `x ≲ (0.78/ε(T))^{8/3} ≈ 3·10^{30}`.
- So QRH would raise the conversion "RH to height T ⟹ Robin for CA numbers with largest prime ≲ T^e" from `e = 2` to `e = 8/3`. In terms of `n`, that is roughly from `n ≲ 10^{10^{22.5}}` to `n ≲ 10^{10^{30}}`.
- The second-order term `u²/log x` stays controlled for `x ≲ T⁴` by truncating the explicit formula at height `T`.
- This is an order-of-magnitude sketch. It has no explicit error terms, and the termwise interchange is not justified at `β → 1`. **It is not a result.**
- For context only, Morrill–Platt (arXiv:1809.10813v4, Thm 13) report a direct interval-arithmetic CA computation giving Robin for `5040 < n ≤ 10^{10^{13.11485}}`. That result is not imported into the repository.

### 5.4 Suggested update (for maintainers; not applied)

The current text of `CONDITIONAL_CONSEQUENCES.md` §1.4 ("Robin: there is no Θ-graded statement …") could become:

> Robin: the reviewed packet is finite arithmetic and is unaffected. A Θ-graded statement exists (ROBIN_GRADED.md, PROPOSED). The Robin violation exponent equals `Θ − 1` when RH fails, so `Θ ≤ 7/8` ⟺ eventually `σ(n) < e^γ n log log n(1 + (log n)^{−1/8+ε})`. This bounds the size of violations, not their existence.

## 6. Numerics (EMPIRICAL; floating point, not directed)

`scripts/robin_graded_numerics.py` (`nice -n 10`, `--pmax 1e8`: 3.5 s; `--psi1`: about 2 min, mostly `mpmath.zetazero`). It does three things:
- **Self-test.** It enumerates CA numbers from the critical exponents `ε_{p,r} = log((1−p^{−r−1})/(1−p^{−r}))/log p`. The first 20 match OEIS A004490.
- **CA numbers.** At the first CA number `N` with largest prime `p`, it computes `Z_CA = (log f(N) − γ)√p log p`.
- **Primorials.** At `N_k` with `p_k = p`, it computes `Z_P = (log f_φ(N_k) − γ)√p log p`.

Asymptotic RH bands: `Z_P ∈ [2−β_N, 2+β_N] = [1.954, 2.046]` (N4) and `Z_CA ∈ [−0.875, −0.782]` (R4). The QRH envelope in the same units is `E = C p^{3/8}`.

|        p | log N_k | Z_P | Z_CA | E (C=0.0465, K′ sketch) | E (C=0.789, Lemma K) |
|---:|---:|---:|---:|---:|---:|
| 997 | 956 | 2.261 | −0.908 | 0.62 | 10.5 |
| 9 973 | 9 896 | 2.176 | −0.846 | 1.47 | 25.0 |
| 99 991 | 99 685 | 2.104 | −0.823 | 3.49 | 59.3 |
| 999 983 | 998 484 | 2.055 | −0.792 | 8.27 | 140.6 |
| 9 999 991 | 9 995 179 | 2.013 | −0.781 | 19.6 | 333.4 |
| 99 999 989 | 99 987 730 | 1.969 | −0.793 | 46.5 | 790.5 |

Reading:
- The observed deviations sit at the RH scale `1/(√p log p)` with the predicted constants. `Z_P` drifts into its band from above, a lower-order `O(1/log p)` effect. `Z_CA` wanders around the band edge by about 0.01.
- They lie a factor `≈ p^{3/8}` (about 10³ at `p = 10^8`) inside the QRH envelope.

Raw output: `results/robin_graded_numerics.txt` (sha256 `5e2e30f2…`). Script sha256: `ab7dfa3f…`.

This is consistent with the known verified range of Robin's inequality. It is a sanity check of the normalisations only. **It is not evidence for QRH-IMPORT or RH:** finite data cannot see `Θ`.

## 7. Misreadings to avoid

- Prop. R and Theorem V **do not** show that Robin violations are absent under QRH. They cap the size of violations; Robin's sign needs exponent `−1/2`.
- "`Θ ≤ 7/8` ⟺ `v_R ≤ −1/8`" is cofinal and ineffective. It is not a finite-check criterion like R1.
- The constant `0.79` comes from a crude integration by parts. `0.0465` is a sketch (K′). Neither has an effective threshold.
- R3's admissible range `β ∈ (1−Θ, 1/2)` is quoted from Lagarias's account of Robin. N3's range is our reading. If either were narrower, only the lower half of Theorem V (respectively, the Nicolas analogue) would weaken. Prop. R and Prop. N do not depend on R3 or N3.
- The cancellation of `S(x)/(x log x)` is specific to the `log log N` normalisation at primorials and CA numbers. The bare Mertens remainder `Σ_{p≤x} −log(1−1/p) − log log x − γ` is genuinely of size `x^{θ−1} log x` pointwise under `H(θ)`.

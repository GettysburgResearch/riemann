# Attack on the centred stage of the cubic fourth-moment route (risk item 9)

```text
Status: REVIEW (adversarial, bounded) of risk item 9 of proposed/CUBIC_FOURTH_MOMENT/SKETCH.md.
  Verdict (a): SURVIVES at the level of the displayed steps. No loss of size cM with c > 0 was
  found in the centred-coefficient invariance or in the masked lattice cancellation, for n = 3, for
  reflected inputs, or for L up to the caps. The route stays CONDITIONAL on the external, unreviewed
  Lemma 18.1 and on (H-B). No moment bound is proved. RH is not addressed.
Scope: case 1 (z = 0) of Lemma 18.1 of the OpenAI manuscript, transferred to n = 3. Only these
  steps were attacked: Lemma centered-coefficient-invariant (l. 13954), Lemma
  centered-lattice-cancellation (l. 14545), and their use in l. 14684-14770, together with the
  comparison construction (l. 12940-13008) and reflection (l. 12677-12828) that feed them. The
  kappa = 5/6 bounds (Lemmas 4.F, 4.G) and the nested order (H-B) were not re-reviewed.
Exact sources or dependencies:
  repo HEAD f6044af1de105feb3bb3bf88281c29c6e9b7328e (branch claude/peaceful-faraday-ki4ewu).
  pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6:standalone/2026-10-07-openai-quasi-riemann-
    import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
    sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed; read as
    untrusted data). Read: l. 12477-13200, 13200-13420, 13596-13700, 13900-14830.
  Read in full: proposed/CUBIC_FOURTH_MOMENT/{README,SKETCH}.md, CUBIC_N3_GAPS.md,
    CUBIC_RELAXED_INDUCTION.md, reviews/CUBIC_NESTED_REDTEAM.md.
  a2/eis.py imported read-only (sha256 87ca11d9...2798e65, unchanged).
  New: scripts/cubic_centred_attack.py, sha256 2cbc8718842f9769...c0b7c371587c90c. Another process
    committed it in f6044af1d without my action; the committed file equals the one that was run.
What was actually run:
  nice -n 10 python3 -I scripts/cubic_centred_attack.py -> 18/19 (48 s; log in the session
    scratchpad, centred/run2.log). The one FAIL is [L2b]. It is a scale limitation, explained in
    Sec. 3.3, not a counterexample. Run 1 had 15/18: two checks were mis-specified and one
    functional-equation cutoff was too short. Sec. 3.5 lists every change made between the runs.
  Arithmetic: [P] EXACT (fractions). [L], [C], [R] use an EXACT index set (primary elements of
    Z[omega], exact divisibility, exact cubic characters, checked against eis.sym_prime) with
    FLOATING smooth weights, Mellin inversions and sums. Nothing floating is called certified.
Smallest remaining gap: whether every operation between the centred input and the Theta-row child
  in l. 13114-14310 acts identically on the two rectangles. These operations are both transforms,
  the kernel separation, the Gauss-row enlargement, the extractions, the t-allocation and the
  absolute values. The manuscript asserts this in a three-sentence proof (l. 13983-13997). The
  question is order-free and L-free. The sextic proof needs exactly the same statement. The cubic
  route adds no new requirement to it.
```

RH is unsolved. Nothing here proves or disproves RH, Lemma 18.1 or any moment bound. "Survives"
means that I found no step whose failure produces a loss `cM` with `c > 0`. It does not mean the
step is proved.

## 0. Verdict

**(a) Survives.** The three attack directions give the following.

| direction | result | loss found |
|---|---|---|
| (a) `n = 3` | Both lemmas are order-free. Their only arithmetic input is that `Θ`-characters are residue-class functions on a fixed lattice. For `n = 3`, `Θ` consists of the 27 `S`-numerator characters, which are periodic mod 18 (CUBIC_N3_GAPS [K1-K2]). The closed forms `(2/n)_3`, `(ω/n)_3` are checked exactly here [L0]. | none |
| (b) reflected inputs | A reflected factor carries the original coefficients, conjugated, times a row scalar. Numerically that scalar is the normalized cubic Gauss sum [R1]. It is removed by `\|·\|` before any centring. The manuscript's own centred stage already takes reflected inputs (core reflection, l. 12810-12828). So a reflected comparison is not a new input class. | none (`O(ξ)` per nested level, terminal) |
| (c) `L ≈ 0.42M` | `L` enters only through (i) "all four plain lengths `≥ L`" (l. 12990, 14686), (ii) `A_comp` (l. 12955-12967), and (iii) `r = (L − v)_+` (l. 14694). The lattice error is absolute, `O(Z^{ε_1})`, so the relative precision is `Z^{-(L−v)}` whatever `L` is. The caps `L ≤ min(A/2, A − M/2)` keep (i) true. | none |

**The "twice the precision" framing needs correcting.** The sketch says the cubic route uses the
invariance "at twice the sextic precision". In the lattice lemma, precision is not a separate
resource. The lemma gives relative error `Z^{ε_1}/(smallest scale)` for every geometry. The cubic
demand `Z^{-(A−2M/3)}` (up to `Z^{-M/3}` at `v = 0`) is therefore met by taking a longer `L`, and
the caps allow it. More importantly, **the binding point `v = L` of the cubic closing condition
uses no lattice saving at all.** There `(L − v)_+ = 0`, and the deficit is controlled only by
`F_1 + F_2 ≥ (5/6)v` [P2]. The lattice step has positive slack `L − v − (A − 2/3 − 5v/6 + μ) > 0`
for every `v < L`. At `v = 0` and `A = M` that slack is `0.070M` (`δ = 0`) or `0.072M`
(`δ = 1/100`).

**Quantified tolerances** [P3-P5] (two stages, `M = 1`, exact):

| loss model | cubic tolerance | sextic, for scale |
|---|---|---|
| uniform loss `c_C` in the whole centred deficit (the sketch's model) | `c_C < 11/432 ≈ 0.0255` (`δ = 0`); `953/43200 ≈ 0.0221` (`δ = 0.01`) | `1/9 ≈ 0.111` |
| additive loss confined to the lattice saving, `r → (r − c_lat)_+` | `c_lat < 11/360 ≈ 0.0306`; `953/36000 ≈ 0.0265` | `1/6 ≈ 0.167` |
| lattice delivers only a fraction, `r → β r` | free for `β ≥ 5/6`; two stages fail below `β = 3 − √5 ≈ 0.764`; every nested version fails at `β ≤ 2/3` | — |

So the cubic route is about 4-5 times less tolerant than the sextic proof. Its weakest assumption,
though, is not the lattice step. A failure of invariance would not be a small loss `cM`. It would
be all-or-nothing: if one invariant datum differs between the two rectangles, a full main term
survives [C-CTRL]. The loss is then `A − 2M/3 − F_1 − F_2`, up to `M/3`, far above `0.025M`. The
displayed proof contains no mechanism for a partial mismatch of size between these two extremes.

## 1. The statement as the manuscript proves it (sextic), and what the cubic route needs

### 1.1 Inputs and the comparison (l. 12810-13008)

* **Padded core** (old-eq:2.1h, l. 12819). Reflect each plain factor of length `> M/2` once. The
  core is `n_i^* ≤ M/2 + ξ`, `A^* ≤ M + δ`.
* **Order of operations.** "Reflection and scale suprema are taken before centering"
  (l. 12825). Row-dependent dual scales `Y = C_k q_{d_0}/(X q_{h_0})` (old-eq:2.1d) are handled by
  coefficient mass and a rowwise supremum over `O(log² Z)` unit boxes (l. 12780-12784). The
  reflected factor is then conjugated inside `|·|`, which "replaces the conjugate character by the
  original character and conjugates its profile" (l. 12785-12789).
* **Comparison** (l. 12940-12996), sextic `L = M/4`. The comparison has lengths `L, A − L` and
  the same two profiles. Put `Y_1 = Z^L`, `Y_2 = X_1X_2/Y_1`, so `X_1X_2 = Y_1Y_2` exactly. Then
  `Δ_k = S(X_1)S(X_2) − S(Y_1)S(Y_2)`. The comparison is bounded separately, "on the original
  permissible rows" (l. 13005), after reflecting its longer factor. This gives
  `A_comp ≤ 3M/2 − A + ξ` (old-eq:3.11). In general the bound is `M − A + 2L + ξ`.

### 1.2 Lemma centered-coefficient-invariant (l. 13954-13997)

"For a centered input, the two transforms and the intervening Gauss-row enlargement … preserve"
the coefficient form eq:centered-coefficient-form (l. 13050-13063):

    (slot factors) · D_b(l_1,l_2) · τ_1(u) q_u^{it} 1_{(u,R)=1} 1_{s|u},   u = Π l_1 l_2,
    D_b(l_1,l_2) = Π_i W_i(q_{b_i} q_{l_i}/X_i) − Π_i W_i(q_{b_i} q_{l_i}/Y_i),   X_1X_2 = Y_1Y_2   (old-eq:2.18a).

On a child whose inducing character lies in `Θ`, with the live slot labels fixed, the plain
coefficient is

    ϑ(l_1) ϑ(l_2) 1_{(l_1 l_2, R_*)=1} q_{l_1 l_2}^{it} D_b(l_1, l_2),

with one `ϑ ∈ Θ`, one squarefree `R_*` of polynomial norm (common to both variables and both
rectangles), and one real `t`. The proof (l. 13983-13997) cites the following:

* the first-transform form;
* complete extraction with "the same ideals `b_i` … in the two terms of `D_b`" (l. 13203-13205);
* one Fourier measure "common … to both rectangles" (l. 13326-13331, 13913-13915);
* `𝔱`-extraction that "replaces both `X_i, Y_i` by `X_i/q_p, Y_i/q_p`" (l. 13924-13926);
* "Exceptional raw scales remain formal and are not clipped" (l. 14786);
* "No common clipped reduction is used for the signed difference" (l. 14179).

### 1.3 Lemma centered-lattice-cancellation (l. 14545-14660)

Put `𝓛_i(X,t) = Σ_l ϑ(l) 1_{(l,R_*)=1} q_l^{it} W_i(q_l/X)`. Then:

    𝓛_i(X,t) = c_{ϑ,R_*} X^{1+it} I_i(t) + O(Z^{ε_1}(1+|t|)^J)                      (old-eq:2.18d)
    T^{-1/2} |𝓛_1(U_1)𝓛_2(U_2) − 𝓛_1(V_1)𝓛_2(V_2)| ≪ Z^{ε_1}(1+|t|)^{2J} T^{1/2} Z^{-r}  (old-eq:2.18f)

The second line holds whenever `U_1U_2 = V_1V_2 = T` and all four scales are `≥ Z^r`. The proof
uses Poisson summation on a fixed lattice of residue classes and Möbius inversion of the mask. The
error is **absolute**; the main terms cancel identically.

### 1.4 Use (l. 14684-14770)

* "Initially all four plain lengths are at least `L`."
* Each extraction lowers a plain by at most the total extracted, so
  `r = (L − c − w − min(c_2, d_2))_+` (l. 14694).
* The `𝔱`-ledger (old-eq:2.18h) gives `Z^{a_0 − b_2 − r + 2θ_N}` (old-eq:2.18).
* Sextic: `A − 5M/6 − (2/3)v − (L − v)_+ ≤ A − M` at `L = M/4`, maximum at `v = L`
  (old-eq:2.19). This point is exactly tight: the `δ` of the padded core is absorbed there.

### 1.5 What the cubic route needs (SKETCH Sec. 3.5, Lemma 4.J)

* **Deficit.** `A − 2M/3 − F_1 − F_2 − (L − v)_+ ≤ A − 2M/3 − (5/6)L + T`, with
  `L = L_j(A) = (6/5)(A − 2M/3 + μ)`.
* **Ranges of `L`.**
  * `L(top) = 43/102 ≈ 0.4216M` (`δ = 0`) and `4393/10200 ≈ 0.4307M` (`δ = 1/100`) [P1].
  * At the bottom of `C_2` (`A = b_1 = 31/36`), `L ≈ 0.255M`.
  * In `C_1`, `L` runs from `≈ 0.02M` to `0.255M`.
* **Precision.** The lattice must deliver `Z^{-(A − 2M/3 − 5v/6 + μ)}` for `v < L`. That is at
  most `Z^{-(A−2M/3+μ)}`, about `Z^{-0.351M}`, at `v = 0`. The caps give `Z^{-L}`, which is
  `Z^{-0.4216M}` [P2].
* **Reflected inputs.** `C_2`'s comparison `(L, A − L)` is reflected to `(L, M − A + L)`, with total
  `A' = M − A + 2L`. It is then fed to `C_1`, which centres it with its own
  `L' = L_1(A') ≈ 0.233M` at `A = M`. The caps keep it in the core: `L ≤ A − M/2` gives
  `M − A + L ≤ M/2`.

## 2. Attack, step by step

### 2.1 (a) n = 3

The invariance proof uses three facts.

* Characters, masks and norm powers are multiplicative on the full product (l. 13072-13082). The
  zero-extension rule becomes "exponent `≡ 0 (mod 3)`".
* The two sides' inducing characters differ by a member of `Θ`. Their ratio is
  `χ_n(−1) ρ/ρ'`, and `χ_n(−1) = 1` for `n = 3`.
* An exceptional character "equals some `ϑ ∈ Θ`". For `n = 3`, `Θ` is the 27 `S`-numerator
  characters, plus fixed twists.

None of these is weaker at `n = 3`; the reciprocity phases are simply trivial.

The lattice lemma's proof uses only that "primary generators … with the fixed character weight
`ϑ` are a finite weighted collection of residue classes in a fixed lattice". For `Z[ω]` and
`S = {2, λ}`:

* the primary odd elements form 3 classes modulo `6O`, i.e. 27 classes modulo `18O`;
* the `Θ`-characters are constant on each of those 27 classes.

[L0] checks exactly the closed forms used: `(2/p)_3 = (p mod 2) ∈ F_4^×` and
`(ω/p)_3 = ω^{(Np−1)/3}`, for all 422 primary primes of norm `≤ 3000`. [L1] then confirms
old-eq:2.18d with these characters. The maximum absolute error is `≤ 29` for `X` up to
`1.6·10⁶`. It stays bounded by the number of divisors of the mask, `2^{ω(R_*)}`, with no
`X`-growth.

**Loss: 0.**

### 2.2 (b) inputs produced by a reflection

Concern: the dual side might carry Gauss-sum phases instead of the original coefficients.

* **What reflection produces.** The Hecke functional equation (l. 12700-12790) gives
  `T_ψ(X;W) = ε_k Σ_{d_0,h_0} (…) T_{ψ̄^0}(Y;W^♯)`. The dual coefficients are `ψ̄_k^0(n)`, and the
  only Gauss-type object is the row constant `ε_k`.
  * [R1] checks this numerically for two primitive cubic characters of conductor norm 2017 and 2053.
    The identity holds with `|ε_k| = 1` to `10⁻⁹`. It is independent of `X` and `W`: the spread
    over 3 scales and 2 profiles is `≤ 10⁻⁸`.
  * `ε_k` equals the normalized cubic Gauss sum of `k` (eis convention) to `10⁻⁹`.
  * `ε_k` differs between the two rows.
  * The control with `χ` in place of `χ̄` on the dual side fails.

  So the "dual-side Gauss phase" is a row scalar of modulus one. It is removed by `|·|²` before
  any Poisson step in the row variable.
* **Where the nested route uses a reflected datum.** Only inside `Σ_{R_0}|comp|²`, where
  `Σ|S|² ≤ 2Σ|Δ|² + 2Σ|comp|²` (l. 12987-13008). `Δ_k` itself contains two *unreflected*
  rectangles. No signed combination across a reflection occurs, so the invariance lemma is never
  asked to hold "through" a reflection.
* **Is the input class new? No.**
  * The manuscript's centred stage proves the padded core. Its inputs are already reflected
    factors: conjugated `W^♯` annuli, boxed row-dependent scales, natural zero extension
    (l. 12810-12828).
  * A reflected comparison `(L, M − A + L)` has the same form: one unreflected factor, one
    reflected factor, the same `ψ_k`, fixed box scales, total in an earlier stage's range, and
    inside the core by the caps.
  * What nesting adds:
    * profiles after up to three reflections (core, `C_2` comparison, `C_1` comparison), plus
      their box derivatives. This is a finite closure, fixed before `C_ref` (red-team
      correction 4);
    * `O(ξ)` length padding per reflection. This is terminal.
* **Numerics.** [L1], [L2a] and [L3] include a reflected-type profile `conj W^♯` and its boxing
  derivative `y∂_y conj W^♯`, with `W^♯` from a numerical inverse Mellin transform with
  `Γ(s)/Γ(1−s)`. They behave exactly like original profiles.

**Loss: none of order `M`.** The extra costs are `Z^{ε_1}` coefficient mass from `d_0, h_0`,
`(log Z)^{O(1)}` boxes and annuli, and `O(kξ)` lengths.

### 2.3 (c) L ≈ 0.42M

* I grepped every use of `L` in l. 12900-14990. They are l. 12944-12990 (construction and
  lengths), l. 14686-14694 (`r`) and l. 14760-14767 (old-eq:2.19). Line 14836 is an unrelated
  symbol. No other step depends on `L ≤ M/4`.
* The lattice hypothesis "all four scales `≥ Z^r`" holds with `r = (L − v)_+`. The original
  plains have `n_i ≥ A − M/2 − ξ ≥ L − ξ` (cap); the comparison has `A − L ≥ L` (cap).
* The comparison's long factor exceeds `M/2`. That is equally true in the sextic proof
  (`A − L > 7M/12`), and only non-`Θ` children and the diagonal see it. Those depend on the total
  `A`, not on `L`.
* [L3] sweeps `L = 0.25 … 0.48` at `A = M`, `Z = 10⁸`. Every centred difference obeys
  `rel ≤ 2^{ω} K Z^{-L}` with one `K`. The achieved precision grows with `L`: worst `r_obs`
  `0.077 → 0.355` as `L` goes `0.25 → 0.48`.

**Loss: 0.**

### 2.4 Where an `O(M)` failure would have to come from

[C-CTRL] breaks exactly one invariant datum between the two rectangles, at the cubic geometry
`L = 0.4216`, `Z = 10⁸`. Each break destroys the saving: the relative residual is `0.1-1.1`,
`r_obs ≤ 0.12 < 1/3`.

* mask differs by one prime;
* norm power `t` vs `t + 0.05`;
* profile swapped in one rectangle;
* product of scales off by `Z^{-0.02}`, i.e. a one-rectangle clipping.

So any of these, if it happened anywhere in l. 13114-14310, would leave a full `Θ`-row main term.
I checked each operation the invariance proof cites (Sec. 1.2) against the text. Each is stated to
act on the whole product, or on both rectangles with a common factor. I found none that acts on
one rectangle, one plain, or one scale only. The remaining risk is that this line-by-line claim
is wrong somewhere in lines I did not re-derive (l. 13420-13595 and 13700-13900 were not read
for this note).

## 3. Numerics (scripts/cubic_centred_attack.py)

### 3.1 Design

* **Index set.** Primary `z ≡ 1 (mod 3)` in `Z[ω]` with odd norm, one generator per ideal prime
  to 6: 2,206,433 elements of norm `≤ 7.3·10⁶`.
* **Characters.** `ϑ ∈ {1, (2/·)_3, (ω/·)_3}`, by the closed forms of [L0].
* **Masks.**
  * none;
  * "small": `π_7 π_13 (5)`, `2^ω = 8`;
  * "big": 7 primes, `q_{R_*} ≈ 1.8·10⁸`, `2^ω = 128`.
* **Norm powers.** `t ∈ {0, 2.5}`.
* **Profiles.** Annular on `[1/4, 4]`:
  * a real bump;
  * a complex `y^{0.7i}` bump;
  * a reflected-type piece `conj W^♯ · bump`, with `W^♯` the inverse Mellin transform of
    `MW(1−s)Γ(s)/Γ(1−s)` for a log-Gaussian `W`, quintic spline;
  * its boxing derivative.
* **Main term.** `(π/(6√3)) Π_{p|R_*}(1 − 1/Np) X^{1+it} ∫W(y)y^{it}dy` for principal `ϑ`, and 0
  otherwise.
* **Geometries** `(n_1, n_2; L)` at `Z ∈ {10⁶, 10⁸}`:
  * sextic `A = M`, `L = M/4`;
  * cubic `C_2` at `A = M` (`L = 0.4216`) and at `A = 1.01M` (`L = 0.4307`);
  * cubic `C_2` bottom, `A = b_1` with an unbalanced core input;
  * nested `C_1` applied to the reflected comparison `(0.4216, 0.4216)`, `L' = 0.2333`.

### 3.2 Results (run 2, 18/19)

| id | result |
|---|---|
| P1-P5 | exact ledger: `μ*`, `L(top)`, the zero lattice saving at the binding point, and the tolerance table of Sec. 0 |
| L0 | exact closed forms, 422 primes |
| L1 | `\|𝓛 − main\| ≤ 29` for every character, mask, profile and `t`, for `X ∈ [10, 1.6·10⁶]`; nonprincipal `ϑ` have no main term |
| L2a | all 180 centred differences satisfy `rel ≤ 2^{ω(R_*)}·K/min-scale` with `K = 40`; the observed maximum of `rel·min-scale/2^ω` is 9.8 |
| **L2b FAIL** | at `Z = 10⁸`, masks with `2^ω ≤ 8`: achieved precision `≥` required failed in some cases, e.g. cubic `C_2`, small mask, `0.252 < 0.333`; nested `C_1`, no mask, `0.153 < 0.176` |
| L3 | `L`-sweep, as in Sec. 2.3 |
| C-CTRL ×4 | all detected |
| R1, R1-CTRL | functional equation as in Sec. 2.2 |

Worst achieved precision `r_obs = −log_Z(rel)`, with masks none / small / big:

| geometry | `r_req` | `r_min-scale` | `Z = 10⁶` | `Z = 10⁸` |
|---|---|---|---|---|
| sextic, `L = M/4` | 0.167 | 0.250 | 0.195 / 0.076 / −0.038 | 0.180 / 0.077 / 0.022 |
| cubic `C_2`, `A = M` | 0.333 | 0.422 | 0.444 / 0.320 / 0.065 | 0.417 / 0.252 / 0.124 |
| cubic `C_2`, `A = 1.01M` | 0.343 | 0.431 | 0.265 / 0.189 / 0.049 | 0.507 / 0.269 / 0.143 |
| cubic `C_2` bottom | 0.194 | 0.255 | 0.202 / 0.035 / −0.073 | 0.248 / 0.105 / 0.016 |
| nested `C_1` on reflected comparison | 0.176 | 0.233 | 0.094 / 0.017 / −0.060 | 0.153 / 0.070 / 0.054 |

### 3.3 Reading of the FAIL, and what the numerics can and cannot tell

* The lemma's error has the shape `C · 2^{ω(R_*)} / (min scale)`, where `C` depends on profile
  seminorms. [L2a] and [L3] confirm that shape with one constant, uniformly in `L`, profile type
  (including reflected) and `t`.
* The precision requirement leaves the following room at `Z = 10⁸`:
  * `Z^{L − r_req}`, which is `Z^{0.088} ≈ 5` at `A = M`;
  * `Z^{0.057} ≈ 3` for nested `C_1`.

  That room is smaller than `C · 2^ω`: about 1-4 with no mask, 8-30 with the small mask, and
  `128 ≈ Z^{0.26}` with the big mask. So tiny-scale numerics **cannot exhibit** the cubic
  precision requirement. The same holds for the sextic one with masks.
* This is the `Z^{ε_1}` of old-eq:2.18f. Here `2^{ω(R_*)} ≤ exp(O(log Z/log log Z))`, which is
  `Z^{o(1)}` only very slowly. That is generic to divisor-bounded methods and is not a cubic loss.
* I did not fit a decay exponent from the two values of `Z`. That would infer an asymptotic from a
  two-point ladder.
* The numerics **do** show three things:
  * no `L`-dependent or reflection-dependent loss beyond the lemma's shape;
  * the main term cancels for reflected-type profiles;
  * any single broken invariant datum leaves the full main term.

### 3.4 What was not tested

* The full two-transform pipeline from an actual cubic row family down to a `Θ`-row child. It is
  far beyond tiny-scale cost, so the invariance lemma itself is tested only through its
  conclusion's shape and through the controls.
* Any Patterson-type secondary term at the Gauss-row level (the red team's heuristic). The
  scheme's `Θ`-row children have no Gauss coefficient (the invariance lemma, "without G"), so the
  lattice sums tested here are the objects the scheme actually cancels.

### 3.5 Changes between runs

* **Run 1 (15/18).** Three problems:
  * [R1] used a dual-sum cutoff of `200Y`, too short. `W^♯` has a `J_0`-type kernel and decays
    slowly: `|ε| = 0.9996`. Run 2 uses `1000Y`, `σ = 0.5` and a check against the Gauss sum.
  * [L2] combined the lemma's bound with the precision requirement for the 128-divisor mask.
  * [L3] compared `rel·min-scale` across geometries whose divisor norms fall differently.
* **Run 2.** [L2] was split into L2a (the lemma's bound, all masks) and L2b (the requirement at
  `Z = 10⁸`, masks with `2^ω ≤ 8`, asserted before seeing its outcome; it FAILED, Sec. 3.3). [L3]
  became an `L`-sweep. No PASS criterion was loosened after seeing a failure in the same check.
  The L2b failure is kept in the script and reported.

## 4. What remains (the precise statement)

The centred stage survives this attack in the following sense.

> Assume Lemma centered-coefficient-invariant holds as stated for the sextic proof, i.e. every
> operation of l. 13114-14310 acts identically on the two rectangles of a centred input.
>
> Then, for `n = 3`, for every centred input in the padded core (original or a reflected
> comparison), and for every `L ≤ min(A/2, A − M/2)`, the `Θ`-row children satisfy old-eq:2.18
> with `r = (L − c − w − min(c_2, d_2))_+`. The only losses are `O(θ_N + ξ) + ε_1` and the
> `Z^{ε_1}` divisor factor. There is no loss `cM` with `c > 0`, and no dependence on `n` or on
> `L ≤ M/4`.

Remaining items, most load-bearing first:

1. **The invariance hypothesis itself.** It is order-free and the same for the sextic proof. Its
   proof in the manuscript is a summary of l. 13114-14310. An expert line check of those lines,
   asking "does any step touch one rectangle, one plain or one scale only?", is the decisive
   item. A failure would be catastrophic (loss up to `M/3`), not marginal.
2. **The binding constraint is not item 9.** At `v = L` the lattice saving is zero and
   everything rests on `F_1 + F_2 ≥ (5/6)v` (Lemmas 4.F, 4.G; risk items 2, 4, 6). A loss there is
   the "whole-deficit" model, with tolerance `11/432 ≈ 0.0255M`. The risk register should name
   this as the quantitatively tightest point. Item 9 is the qualitatively riskiest.
3. **(H-B) bookkeeping.** This covers profile closure through 3 reflections plus box derivatives,
   and `ξ < μ*ρ/2` so that `A_comp` lands below `b_{j−1} − μ`. It is unchanged by this note.

**Smallest sub-question.** In l. 13114-14310, is there any operation applied to a centred
coefficient that is not common to the two rectangles? Candidates are a sectoring, clipping,
supremum, truncation, absolute value, or `Θ`/non-`Θ` split. The manuscript asserts there is none
(l. 12825-12828, 13105, 13326-13331, 13913-13926, 14179, 14786). If one exists on a positive
proportion of allocations, the cubic route (and the sextic case 1) fails outright. If none
exists, item 9 contributes no `cM` loss.

## 5. Corrections to the sketch's wording (no change to its conclusions)

* "Twice the sextic precision" should read: a longer comparison length, `L ≈ 0.42M` against
  `M/4`, permitted by the caps. The lattice lemma's relative precision is `Z^{-(L−v)}` for every
  `L`.
* "Most likely failure point: item 9" should be split. Item 9 is the most consequential if it
  fails, but it is all-or-nothing and order-free. The tightest *quantitative* point is the
  `κ = 5/6` bound at `v = L`, where the lattice step contributes nothing.
* The tolerance for a loss confined to the lattice saving is `11/360 ≈ 0.031M`, not `0.025M`. The
  value `11/432` applies to a loss in the whole deficit. A multiplicative shortfall in the lattice
  saving costs nothing down to `β = 5/6`.

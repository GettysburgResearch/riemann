# Lemma 4.K written out: functional equation and conductor bound for cubic rows over Q(ω)

```text
Status: PROPOSED proof, paper level, of Lemma 4.K of SKETCH.md Sec. 4 (risk item 7). Not reviewed.
  Verdict: proved, with one correction to the justification (not to the statement). The SKETCH
  derives the bound at S from "the S-part of the row lies in the fixed family". That does not
  control the lambda-exponent: the primary S-free part of a row is itself ramified at lambda
  (exponent 0 or 2, according to N mod 9). The bound is restored by a universal local bound:
  exponent <= 4 at lambda and <= 1 at every prime not above 3, for every character of order
  dividing 3. RH is not addressed.
  Theorem C4 remains OPEN and CONDITIONAL.
Scope: cubic Hecke characters of F = Q(omega): the Kummer row characters (k/.)_3, the family
  characters chi_c, and the row twists psi_k = tau (k/.)_3 of the cubic transfer of case 1 of
  Lemma 18.1. It gives the exact conductor (exact lambda-exponent), the functional equation, the
  passage from imprimitive to primitive characters, and N(f_k) N(R_0,k) <= C_* N(k) Z^q << Z^M.
  It says nothing about the analytic core (H-A), the nested order (H-B), or Statement C.
Exact sources or dependencies: SKETCH.md Secs. 1-5 (this folder); STATUS_END_OF_WAVE.md rows
  R14 and item 7. Manuscript pr908 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, paper.tex, sha256
  42a5ee0f...deac6a3 (re-hashed). Read: l. 100-160, 566-700 (Lemma 4.1), 1415-1530 (Lemma 4.8),
  12470-12835 (Sec. 18 setup, old-eq:2.1a-2.1h). IMPORTED, classical and not re-read here:
  Hecke's functional equation; Artin reciprocity and the conductor-discriminant formula; Kummer
  theory; Hilbert's formula for the different; cubic reciprocity (I1).
What was actually run: python3 -I lemma_4k_checks.py (imports ../../a2/eis.py read-only), 44 s,
  SUMMARY 10/10. It covers 713 characters (every squarefree k with N k <= 500, up to sign, times
  three units) and 12540 (modulus, character) pairs, plus four failing controls. Output is in
  lemma_4k_checks.out. sha256 (full values in Sec. 4): script 3fd08b5b..., output d0987173...,
  eis.py 87ca11d9....
Smallest remaining gap: (i) nobody has reviewed this note; (ii) the imported functional equation
  was not re-read from a primary source in this session; (iii) the shape of tau is assumed, not
  re-derived child by child. It is a fixed Theta character times finitely many moving cubic
  residue symbols with declared support of norm <= Z^q, and is read off the manuscript's sextic
  datum (l. 12494-12505). A moving factor of order not dividing 3 would void the bound C_* below.
```

RH is unsolved. This note proves no moment bound and does not touch Lemma 18.1 itself. The labels
are those of SKETCH.md. "Proved here" means written out here and not refereed. "Imported" means a
classical theorem used as stated.

## 0. Where Lemma 4.K is used

* **Application (SKETCH Sec. 2.1-2.3).** Each family character `χ_q`, `q ∈ F'_3`, is primitive
  with conductor `qO`. It has gamma factor `(2π)^{−s}Γ(s)` and a root number of modulus one, and
  this gives the AFE. The family conductor is part (b) below. The application uses `q = 0` only.
* **Reflection of long factors (A1, manuscript l. 12677-12830; SKETCH Sec. 3.4).** Each plain
  factor longer than `M/2` is reflected once into the padded core. Each comparison is reflected
  to total `M − A + 2L + ξ`. The reflection closure `R` of the nested order reflects again. Every
  reflection uses exactly three inputs:
  1. the primitive character `ψ*_k` inducing the natural row character;
  2. its functional equation, with `|ε_k| = 1` and the gamma quotient `Γ(s)/Γ(1−s)`;
  3. old-eq:2.1c, `C_k q_{𝔑_{0,k}} ≪ Z^M`, where `C_k = 3Q_k/(2π)²` and `𝔑_{0,k}` is the
     redundant natural radical.

  Lemma 4.K supplies 1-3 at `n = 3`. The rest of A1 (mask erasure old-eq:2.1a-b, Mellin profile
  `W♯`, annuli, `C_ref`) does not depend on the order and is imported as H2.

The sextic counterpart is manuscript Lemma 4.1 (`fixed-numerator-ray`, l. 646-699). It
deliberately asserts "no bound on its conductor exponents" at primes of `6a`. The bound at `S` is
then justified at old-eq:2.1c by "the unit and `S`-supported parts of a row ... range over a fixed
finite ray family". Part (c) below replaces that sentence by a local bound, in the cubic case.

## 1. Statement

**Notation.** `F = Q(ω)`, `O = Z[ω]`, `|d_F| = 3`, `h_F = 1`. `λ = 1 − ω`; the manuscript's
`λ = 1 + 2ω = ω(1 − ω)` is an associate. We have `λ² = −3ω`, `N λ = 3`, and `(2)` is inert with
`N(2) = 4`. An element is primary if it is `≡ 1 (mod 3)`. Every ideal prime to 3 has a unique
primary generator. `S` is the fixed finite set of primes: it contains `(2)` and `(λ)` and the
conductor primes of the fixed group `Θ`. `𝔣_Θ` is the lcm of the conductors of the members of
`Θ`.

* **Kummer row character.** For `0 ≠ k ∈ O`, set `η_k(𝔭) = (k/𝔭)_3`. This is the cube root of
  unity `≡ k^{(N𝔭−1)/3} (mod 𝔭)`, for `𝔭 ∤ 3k`. Extend `η_k` multiplicatively to ideals prime to
  `3k`. For `𝔫 = (n)` with `n` primary, `η_k(𝔫) = χ_n(k)`, the SKETCH's `(k/n)_3`.
* **Family character.** For `c` primary, `χ_c(α) = (α/c)_3 = Π_{π|c} (α/π)_3^{v_π(c)}`. This is
  a function of elements. Its ideal version is `χ̃_c(𝔫) = χ_c(n)`, `n` the primary generator of
  `𝔫`, for `(𝔫, 3c) = 1`.
* **Row twist (the SKETCH's H(M; η) datum).**
  * `ψ_k(𝔫) = τ(𝔫) η_k(𝔫)` on good ideals. It is zero-extended at `S`, at the primes of `k`, and
    at the declared moving radical `𝔡`, where `N(𝔡) ≤ Z^q`.
  * `τ = ϑ μ`, where `ϑ ∈ Θ` is fixed.
  * `μ` is a finite product of moving cubic residue symbols `𝔫 ↦ (a_i/𝔫)_3^{e_i}` or
    `𝔫 ↦ χ_{b_i}(n)^{e_i}`, with `a_i, b_i` supported on `S ∪ supp 𝔡`.
  * Rows satisfy `0 < N k ≪ Z^m`, and `M = m + q`.

> **Lemma 4.K (PROPOSED; proved here modulo the imported classical theorems of Sec. 2).**
>
> **(a) Kummer conductor.** `η_k` is a Hecke character of order dividing 3, of trivial infinity
> type. It is trivial iff `k ∈ F^{×3}`. Its conductor is exactly
>
>     𝔣(η_k) = λ^{f_λ(k)} · Π_{𝔭 ∤ 3, 3 ∤ v_𝔭(k)} 𝔭,
>
> where `f_λ(k)` is computed as follows. Put `j = v_λ(k)`.
>
> * If `3 ∤ j`, then `f_λ = 4`.
> * If `3 | j`, put `a = k/λ^j`, choose the sign `s = ±1` with `sa ≡ 1 (mod λ)`, and put
>   `t = v_λ(sa − 1)`. Then `f_λ = 3` if `t = 1`, `f_λ = 2` if `t = 2`, and `f_λ = 0` if `t ≥ 3`.
>
> In every case `f_λ ∈ {0, 2, 3, 4}`, and `N 𝔣(η_k) ≤ 81 · N(rad_{3∤}(k))`. The constant 81 is
> attained.
>
> **(b) Family conductor.** Let `c` be primary. Then `χ̃_c = η_c` (cubic reciprocity), so
> `𝔣(χ̃_c) = λ^{2·1[N c ≢ 1 (mod 9)]} · Π_{3 ∤ v_π(c)} π`. In particular, for `q ∈ F'_3`
> (`q ≡ 1 mod 9`, squarefree), `χ_q` is primitive with conductor `qO`, as DDDS state.
> Without the primary normalisation, `χ_c` is not a function of ideals when `N c ≢ 1 (mod 9)`,
> because `χ_c(ω) = ω^{(Nc−1)/3} ≠ 1`.
>
> **(c) Universal local bound.** Every character of order dividing 3 of `F_λ^×` has conductor
> exponent at most 4. Every such character of `F_𝔭^×`, `𝔭 ∤ 3`, has exponent at most 1.
>
> **(d) Row conductor bound (the cubic old-eq:2.1c).** Let `ψ*_k` be the primitive character
> inducing `ψ_k`. Let `𝔑_{0,k}` be the product of the primes `𝔭 ∈ S ∪ supp(k𝔡)` with
> `𝔭 ∤ 𝔣(ψ*_k)`; these are the redundant zeros. Then
>
>     N 𝔣(ψ*_k) · N 𝔑_{0,k} ≤ C_* · N(rad_good(k𝔡)) ≤ C_* · N(k) · Z^q ≪ Z^{m+q} = Z^M,
>     C_* = 81 · N(𝔣_Θ) · Π_{𝔭 ∈ S, 𝔭 ≠ λ} N𝔭 · Π_{𝔭 ∈ S} N𝔭,
>
> with `C_*` independent of `Z`, `k`, the moving labels and the masks.
>
> **(e) Functional equation (IMPORTED, specialised).** Let `ψ` be a primitive finite-order Hecke
> character of `F` of conductor `𝔣 ≠ O`. Put
>
>     Λ(s, ψ) = (3 N𝔣)^{s/2} Γ_C(s) L(s, ψ),   Γ_C(s) = 2(2π)^{−s} Γ(s).
>
> Then `Λ(s, ψ)` is entire, and `Λ(s, ψ) = W(ψ) Λ(1 − s, ψ̄)` with `|W(ψ)| = 1`. For `𝔣 = O` the
> only such `ψ` is trivial. So the rows `k ∈ R_0` (where `ψ*_k` is nonprincipal) are exactly
> those with `𝔣(ψ*_k) ≠ O`. For `ψ = χ_q`, `q ∈ F'_3`, `W = g̃_3(q)` (DDDS, imported I3).
>
> **(f) Imprimitive to primitive.** On all ideals, `ψ_k(𝔫) = ψ*_k(𝔫) · 1[(𝔫, 𝔑_{0,k} 𝔣(ψ*_k)) = 1]`.
> Moreover
>
>     L(s, ψ_k) = L(s, ψ*_k) Π_{𝔭 | 𝔑_{0,k}} (1 − ψ*_k(𝔭) N𝔭^{−s}),
>
> and the reflected sums are those of the manuscript's display after old-eq:2.1c, with scales
> old-eq:2.1d. The coefficient mass is `Π_{𝔭|𝔑_{0,k}}(1 − N𝔭^{−1/2})^{−2} ≪_ε Z^ε`.

What A1 uses is (d), (e) and (f), with `C_k = 3 N𝔣(ψ*_k)/(2π)²`. Statement (d) is the SKETCH's
claim with the constant made explicit.

## 2. Imported theorems (exact content)

* **[FE] Hecke's functional equation.** For a primitive Hecke character `ψ` of a number field
  `K` with conductor `𝔣`, the completed `Λ(s,ψ) = (|d_K| N𝔣)^{s/2} L_∞(s,ψ) L(s,ψ)` satisfies
  `Λ(s,ψ) = W(ψ)Λ(1−s,ψ̄)` with `|W(ψ)| = 1`. It is entire unless `ψ` is trivial.
  * At a complex place with trivial infinity component, `L_∞ = Γ_C(s)`.
  * Sources: Neukirch, *Algebraic Number Theory*, Ch. VII §8 (Thm 8.5, Cor. 8.6), as cited by
    DDDS Prop. `funceq`; Iwaniec-Kowalski, *Analytic Number Theory*, Thm 3.8; Gao-Zhao JNT 209
    (2020) eq. (1.1), as cited by the manuscript's Lemma 4.8. None was re-read here.
  * Only the displayed shape, `|W| = 1` and entireness are imported.
* **[TRIV] Trivial infinity type.** A finite-order character of `C^×` is trivial, since `C^×`
  is connected. So a finite-order Hecke character of `F` has trivial infinity type (manuscript
  l. 1437). Proved, one line.
* **[ART] Artin reciprocity.** For a finite abelian `L/F`, the Artin map identifies `Gal(L/F)`
  with a ray class group whose modulus is the conductor `𝔣(L/F)`. The local exponent at `𝔭` is
  the smallest `n` with `U_𝔭^{(n)} ⊂ N(L_𝔓^×)`, and for a cyclic `L` it equals the conductor of
  a faithful character. Source: Neukirch Ch. VI; Milne, CFT, VIII (5.3), (5.5) (cited by the
  manuscript).
* **[DIF] Different and conductor-discriminant.** Let `L/K` be a totally ramified cyclic local
  extension of prime degree `ℓ` with lower break `b`, so `i(σ) = v_L(σΠ − Π) = b + 1`. Then
  `v_L(𝔇) = (ℓ − 1)(b + 1)`, and for a faithful character `f(χ) = b + 1` (upper and lower breaks
  agree for prime degree). If `L/K` is tame, `b = 0` and `f = 1`. Source: Serre, *Local Fields*,
  IV §1-§2 and VI §2.
* **[I1] Cubic reciprocity and supplements** (SKETCH I1; DDDS `cuberep`, `cubesupp`):
  `(a/b)_3 = (b/a)_3` for coprime primary `a, b`, and `(ω/π)_3 = ω^{(Nπ−1)/3}`.

## 3. Proofs

### 3.1 (a) η_k is the Kummer character

* Let `β³ = k` and `L = F(β)`. Since `μ_3 ⊂ F`, `L/F` is cyclic of degree 1 or 3. The map
  `ι: σ ↦ σ(β)/β ∈ μ_3` is an injective homomorphism, independent of the choice of `β`.
* For `𝔭 ∤ 3k`, `X³ − k` has discriminant `−27k²`, a unit at `𝔭`. So `𝔭` is unramified.
  Frobenius acts on the residue field as `x ↦ x^{N𝔭}`, so `Frob_𝔭(β)/β ≡ β^{N𝔭−1} = k^{(N𝔭−1)/3}`.
  Since `𝔭 ∤ 3`, reduction is injective on `μ_3`. Hence `η_k(𝔭) = ι(Frob_𝔭)`.
* By [ART], `η_k = ι ∘ Art_{L/F}` is a ray class character with conductor `𝔣(L/F)`. It is trivial
  iff `L = F` iff `k ∈ F^{×3}`.

### 3.2 (a) Local exponents away from 3

Let `𝔭 ∤ 3` and `v = v_𝔭(k)`.

* **`3 | v`.** Write `k = π^v u` with `u` a `𝔭`-unit. Then `L_𝔓 = F_𝔭(u^{1/3})` and
  `disc(X³ − u)` is a unit, so the exponent is 0.
* **`3 ∤ v`.** `v_𝔓(β) = v/3 · e`, so `e = 3` and the extension is totally ramified. It is tame
  because `𝔭 ∤ 3`, so by [DIF] the exponent is 1.

### 3.3 (a) The exponent at λ (proved here)

Let `K = F_λ = Q_3(ω)`. Then `v = v_λ`, `v(3) = 2`, the residue field is `F_3`, and
`U^{(n)} = 1 + λ^n O_λ`. A unit is `≡ ±1 (mod λ)`, and `−1 = (−1)³`. So for `3 | j` we may
replace `k` by `a' = s·k/λ^j ≡ 1 (mod λ)` without changing `L`. Let `t = v(a' − 1)`.

**Cube classes do not change `t` when `t ≤ 3`.** For `y ∈ O_λ`,

    (1 + λy)³ = 1 + 3λy + 3λ²y² + λ³y³ ≡ 1 + λ³(y³ − y) ≡ 1   (mod λ⁴),

because `3 = −ω²λ² ≡ −λ² (mod λ³)` and `y³ ≡ y (mod λ)`. Also `ω³ = 1`. So the cubes of units
are exactly `±U^{(4)}`; this is checked exactly mod `81 = λ⁸`, unit up to sign, in [K-LOC]. The
classes in `U^{(1)}` mod cubes are therefore the classes mod `U^{(4)}`. In particular `t` does not
depend on the representative when `t ≤ 3`.

Let `γ = β − 1` with `β³ = a'`. Then `γ` is a root of `g(Y) = Y³ + 3Y² + 3Y − (a' − 1)`.

* **`3 ∤ j`.** `v_L(β) = j` with `v_L(λ) = 3`, so `L/K` is totally ramified. Choose
  `Π = β^x λ^y` with `jx + 3y = 1`, so `3 ∤ x`. For the generator `σ` (`σβ = ωβ`), `σΠ/Π = ω^x`.
  So `i(σ) = 1 + v_L(ω^x − 1) = 1 + 3 = 4`, `b = 3`, and `f = 4`.
* **`t = 1`.** The Newton polygon of `g` has vertices `(0,1)` and `(3,0)`; the middle
  coefficients `3, 3` have valuation 2, above the segment. So every root has `v(γ) = 1/3`,
  `L/K` is totally ramified, and `Π = γ` is a uniformiser. Then `σΠ − Π = (ω − 1)β`, so
  `i(σ) = 3`, `b = 2`, and `f = 3`.
* **`t = 2`.** The vertices are `(0,2)` and `(3,0)`, and the middle points `(1,2), (2,2)` lie
  above the segment. So `v(γ) = 2/3`, `v_L(γ) = 2`, and `Π = λ/γ` is a uniformiser. Now
  `σγ = (ω − 1) + ωγ`, so

      σΠ/Π − 1 = γ/σγ − 1 = (1 − ω)(1 + γ)/σγ,

  which has `v_L = 3 + 0 − 2 = 1`. So `i(σ) = 2`, `b = 1`, and `f = 2`.
* **`t ≥ 3`.** Write `a' = 1 + λ³x` and `Y = γ/λ`. Then

      Y³ − ω²λY² − ω²Y − x = 0,

  using `3/λ² = −ω²`. Mod `λ` this is `Y³ − Y − x̄`, which is separable over `F_3`. So `L/K` is
  unramified and `f = 0`.

These are the cases in (a). Sanity checks against known pure cubic discriminants:

| `k` | case | `f_λ` | `N𝔣` | `d = d_F · N𝔣` | known discriminant of the cubic field |
|---|---|---|---|---|---|
| `2` | `t = 2` (`−2 = 1 − 3`) | 2 | `36` | `−108` | `Q(2^{1/3})`: `−108` |
| `3` | `j = 2` | 4 | `81` | `−243` | `Q(3^{1/3})`: `−243` |
| `10 ≡ 1 (9)` | `t ≥ 3` | 0 | `100` | `−300` | `Q(10^{1/3})`: `−300` |

For `k = ω`, `L = Q(ζ_9)`, and `|d| = 3⁹ = 3³ · 27²`, which gives `f = 3`.

The bound `N𝔣(η_k) ≤ 81 · N rad_{3∤}(k)` is immediate. The constant 81 is attained at `3 ∤ v_λ(k)`
([K-BND]).

### 3.4 (b) Family characters

* Let `c` and `n` be primary and coprime, with `n` prime to 3. By [I1],
  `χ̃_c((n)) = (n/c)_3 = (c/n)_3 = η_c((n))`. So `𝔣(χ̃_c) = 𝔣(η_c)` by (a).
* Since `c` is primary, `j = 0` and `s = 1`, so `t = v(c − 1) ≥ 2`.
* Write `c = 1 + 3β`. Then `t ≥ 3 ⇔ λ | β ⇔ 3 | Tr β ⇔ N c ≡ 1 (mod 9)`, because
  `N c ≡ 1 + 3 Tr β (mod 9)` and `Tr β ≡ −(x + y) (mod 3)` for `β = x + yω`.
* `q ≡ 1 (mod 9)` gives `t ≥ 4`, so `𝔣(χ_q) = qO` for squarefree `q`.
* For primary `c`, `χ_c(ω) = ω^{(Nc−1)/3}` by [I1], and this is `≠ 1` iff `N c ≢ 1 (mod 9)`.
  ([K-REC], [K-FAM], [K-F3], [CTRL-UNIT].)

### 3.5 (c) Universal local bound

Let `χ` be a character of order dividing 3.

* **At `λ`.** `χ` is trivial on `K^{×3}`. By Sec. 3.3, `U^{(4)} = (U^{(2)})³ ⊂ K^{×3}`, because
  `x ↦ x³` maps `U^{(n)}` onto `U^{(n+2)}` for `n ≥ 2 > e/(p−1) = 1`. So `χ(U^{(4)}) = 1` and the
  exponent is `≤ 4`.
* **At `𝔭 ∤ 3`.** `U^{(1)}` is pro-`p` with `p ≠ 3`, so `U^{(1)} ⊂ K^{×3}` and the exponent is
  `≤ 1`. ([K-LOC] checks the first statement exactly mod `λ⁸`.)

### 3.6 (d) Row conductor bound

Write `ψ_k = ϑ · η` on good ideals, where `η = μ · η_k`.

* **`η` has order dividing 3.** Each factor `(a_i/·)_3` is a Kummer character (Sec. 3.1).
* **Each `χ_{b_i}(n)` is a Hecke character.** For `𝔫 = (n)` with `n` primary, the factor
  `𝔫 ↦ χ_{b_i}(n)^{e_i}` is the character `α ↦ χ_{b_i}(u_α α)` of `(O/3b_i)^×`. Here `u_α` is the
  unit with `u_α α ≡ 1 (mod 3)`, and the character is trivial on units. So it is a Hecke
  character of order `| 3` and modulus `λ² rad(b_i)`.
* **Ramification of `η`.** `η` is unramified at every good prime outside `supp(k𝔡)`.
* **The conductor.** `𝔣(ψ*_k) | lcm(𝔣_Θ, 𝔣(η))`, since `ψ*_k` is induced by `ϑη` restricted to
  good ideals. By (c):
  * at `λ`, the exponent of `𝔣(η)` is `≤ 4`;
  * at `𝔭 ∈ S ∖ {λ}`, it is `≤ 1`;
  * at a good `𝔭`, it is `≤ 1`, and it is 0 unless `𝔭 | k𝔡`.
* **Counting each prime once.**
  * A good `𝔭 | k𝔡` divides exactly one of `𝔣(ψ*_k)` and `𝔑_{0,k}`, once.
  * The `S`-part of `𝔣(ψ*_k)` has norm `≤ N𝔣_Θ · 81 · Π_{𝔭∈S∖λ} N𝔭`.
  * The `S`-part of `𝔑_{0,k}` has norm `≤ Π_{𝔭∈S} N𝔭`.

  Multiplying gives (d). `rad_good(k𝔡)` has norm `≤ N k · N𝔡 ≪ Z^m Z^q`.

**Correction to the SKETCH's justification.** SKETCH Lemma 4.K says "its `S`-part lies in the
fixed family" (as the manuscript does at old-eq:2.1c). That sentence controls `(ε λ^a 2^b/·)_3`:
27 characters, all with conductor dividing `2λ⁴`. It does not control the `λ`-exponent of
`ψ*_k`, because the primary good part `c` of the row is ramified at `λ` as well: its exponent is
2 iff `N c ≢ 1 (mod 9)`, by (b). For example, rows with trivial unit and `S`-part give:

| row | `N` | `f_λ` |
|---|---|---|
| `1 + 3ω` | 7 | 2 |
| `−2 + 3ω` | 19 | 0 |
| `1 + 9ω` | 73 | 0 |
| `−5 + 3ω` | 49 | 2 |

([CTRL-SPART].) The `λ`-components of the two parts can also cancel. For example, `(2/·)_3` has
`f_λ = 2`, but `2c` has `f_λ = 0` whenever `4 N c ≡ 1 (mod 9)`. The statement survives because
of (c), or, for the cubic case, because of (b) together with the bound `f_λ ≤ 4` on the fixed
family. The constant is `C_*`, not "the fixed
family's" constant. The same remark applies to the sextic old-eq:2.1c (SKETCHED, not checked:
there the local bounds are `≤ 4` at `λ` and `≤ 3` at `(2)`, from `U^{(4)} ⊂ K_λ^{×3}` and
`U^{(3)} ⊂ K_2^{×2}`). The manuscript's conclusion "a fixed factor" is right; the reason given is
incomplete.

### 3.7 (e), (f) Functional equation and imprimitive characters

* **Primitive character.** `ψ_k` agrees with a Hecke character on ideals prime to the finite
  modulus `𝔪_k = 𝔣_Θ λ⁴ Π_{S} 𝔭 · rad(k𝔡)`. With `h_F = 1` and trivial infinity type ([TRIV]),
  it is a character of `(O/𝔪_k)^× / O^×`. The set of moduli through which it factors is closed
  under gcd. Its least element is `𝔣(ψ*_k)`, and `ψ*_k` is defined on ideals prime to
  `𝔣(ψ*_k)` by its values on `(α)`, `α` prime to `𝔪_k`, through CRT. This is standard and was
  checked numerically in [K-COND]: periodic exactly at the multiples of `𝔣`.
* **Agreement off `𝔑_{0,k}`.** `ψ_k = ψ*_k` on ideals prime to `𝔪_k`, and `ψ_k = 0` elsewhere.
  So `ψ_k(𝔫) = ψ*_k(𝔫) · 1[(𝔫, 𝔑_{0,k}) = 1]`, since `ψ*_k(𝔫) = 0` already when `(𝔫, 𝔣) ≠ 1`.
  Comparing Euler products gives the displayed `L(s, ψ_k) = L(s, ψ*_k) Π(1 − ψ*_k(𝔭) N𝔭^{−s})`.
* **(e).** This is [FE] with `K = F`, `|d_F| = 3` and `L_∞ = Γ_C(s)`. It is degree 2 over `Q`,
  since `Γ_C(s) = π^{−s}Γ(s/2)Γ((s+1)/2)` up to a constant. The manuscript's
  `(3Q)^{s/2}(2π)^{−s}Γ(s)` differs only by the constant 2. For `𝔣 = O`: since `h_F = 1`, the
  ray class group mod `O` modulo units is trivial, so `ψ` is trivial.
* **Reflection.** Mellin inversion of `T_{ψ*_k}(X; W)` and the shift through
  `Λ(s,ψ*) = εΛ(1−s,ψ̄*)` give `ε_k T_{ψ̄*_k}(C_k/X; W♯)`, with
  `𝓜W♯(s) = 𝓜W(1−s) Γ(s)/Γ(1−s)` (manuscript l. 12704-12740).
* **The redundant factors.**
  * The deleted Euler factors `Π(1 − ψ*(𝔭)N𝔭^{−s})` expand as `Σ_{d_0|𝔑_0} μ(d_0)ψ*(d_0) N d_0^{−s}`.
  * Restoring the factors on the reflected side is the geometric series
    `Π(1 − ψ̄*(𝔭)N𝔭^{−(1−s)})^{−1} = Σ_{rad h_0 | 𝔑_0} ψ̄*(h_0) N h_0^{−(1−s)}`.
  * Together they give the manuscript's display with scales `Y = C_k N d_0/(X N h_0)`.
  * At central normalisation, the coefficient mass is `≤ Π_{𝔭|𝔑_0}(1 − N𝔭^{−1/2})^{−2}`. This is
    `≪_ε Z^ε`, because `N𝔑_0 ≤ C_* Z^M` has `≪ log Z / log log Z` prime factors (old-eq:2.1b).
  * With (d), `Y ≤ C_* Z^M / X`, which is the cubic old-eq:2.1c-2.1d. `C_*` is fixed, so
    `log C_ref / log Z ≤ ξ/2` for large `Z` (eq. `centered-reflection-length`).
* **Root numbers.** These enter only as `|ε_k| = 1` inside `|·|²` (SKETCH Sec. 2.3).

## 4. Finite checks (`lemma_4k_checks.py`; output `lemma_4k_checks.out`, 10/10)

sha256: `lemma_4k_checks.py` `3fd08b5b6df71fb079e8c0224c322f40bd85072ba32fc093fff06504912dcab8`;
`lemma_4k_checks.out` `d0987173dcadced423e3db60037605fc2fe11bb88107f940b50b9267f5922a1e`;
`../../a2/eis.py` (imported read-only) `87ca11d98bf3ee130a6dab613b5f7efe444058320b7c22b005327686f2798e65`.
Run: `python3 -I lemma_4k_checks.py`, 44 s on one core.

Characters are evaluated from the definition: `k^{(N𝔭−1)/3} mod 𝔭`, multiplicatively over the
factorisation of `(α)`. No reciprocity law or conductor formula is used to compute values.

| id | what | result |
|---|---|---|
| K-LOC | cubes of units mod `81 = λ⁸·unit` are exactly `±U^{(4)}` (exact, complete); index 27 | PASS |
| K-COND | 713 characters `η_k`: `k` ranges over every squarefree ideal with `1 < N ≤ 500` (237 ideals), times units `1, ω, ω²`, plus `ω, ω²`. For each, all `6·2^{ω_{3∤}(k)}` divisors `𝔪` of `λ⁵ rad_{3∤}(k)` were tested (12540 pairs). The set of `𝔪` with `η_k((α)) = 1` for all `α ≡ 1 (𝔪)` prime to `3k` is exactly the multiples of the predicted `𝔣(η_k)`. Hence the smallest modulus of periodicity is the predicted conductor. `λ`-exponent histogram: `{0: 56, 2: 121, 3: 356, 4: 180}` | PASS, 0 mismatches |
| K-BND | `max N𝔣/N rad_{3∤}(k) = 81` | PASS |
| K-REC | `(n/c)_3 = (c/n)_3` for 9426 primary pairs | PASS |
| K-FAM | 177 primary squarefree `c`, `3 ∤ c`: `χ_c(primary n)` has conductor `c λ^{0 or 2}`, with exponent 0 iff `Nc ≡ 1 (9)` (56 such `c`) | PASS |
| K-F3 | the 16 squarefree `q ≡ 1 (mod 9)` with `N q ≤ 500` have conductor `qO` | PASS |
| CTRL-NOLAMBDA | omitting the `λ`-part fails for 657/657 characters with `f_λ > 0` (explicit witness) | control detects |
| CTRL-CAP2 | capping the `λ`-exponent at 2 fails for 536/536 characters with `f_λ ∈ {3,4}` | control detects |
| CTRL-SPART | primary rows with trivial unit and `S`-part have `f_λ ∈ {0, 2}` (`1+3ω`: 2; `−2+3ω`: 0), so the `S`-part does not fix it | control detects |
| CTRL-UNIT | `χ_c(ω) ≠ 1` for all 121 primary `c` with `Nc ≢ 1 (9)` | control detects |

**Exact versus sampled.** "Not periodic" is exact: a witness `α ≡ 1 (𝔪)` with `η_k((α)) ≠ 1` is
exhibited. "Periodic" is sampled: every `α = 1 + 𝔪γ`, `γ` in a `7×7` box (`15×15` if fewer than
12 admissible), was tested. It is a finite consistency check of (a), not a proof. The proof is
Sec. 3. The checks are restricted to `N(k) ≤ 500` and to squarefree `k`; `v_λ(k) ∈ {2, 3}` is
covered by the proof, not the checks.

## 5. Verdict and updated risk-register line

**Verdict: proved (PROPOSED), with a correction of justification.** All four parts hold as the
SKETCH uses them: the row functional equation, `|W| = 1`, the gamma factor `(2π)^{−s}Γ(s)`, and
`N𝔣(ψ*_k) N𝔑_{0,k} ≪ Z^M`. The bound now rests on the universal local bound (c), not on "the
`S`-part lies in the fixed family". The exact `λ`-exponent is `f_λ ∈ {0, 2, 3, 4}`. The constant
is `C_* = 81 · N𝔣_Θ · Π_{S∖λ}N𝔭 · Π_S N𝔭`. Nothing downstream changes, because `C_*` is fixed
and goes into `C_ref`.

Replacement for SKETCH Sec. 5, item 7 (and STATUS_END_OF_WAVE item 7, R14):

| # | step | status | evidence | most likely failure mode |
|---|---|---|---|---|
| 7 | Lemma 4.K (row functional equation, conductor `≤ Z^M`) | **proved here (PROPOSED), not reviewed**, modulo imported classical theorems ([FE], [ART], [DIF], I1). Exact `λ`-exponent `{0,2,3,4}`; universal local bound replaces the "fixed family" justification | LEMMA_4K.md Secs. 3.1-3.7; `lemma_4k_checks.py` 10/10 (713 characters, `N ≤ 500`, 4 controls) | a child datum whose `τ` carries a moving factor of order not dividing 3, or a `Z`-dependent fixed character, would void `C_*`. Not re-derived child by child. Low risk |

## 6. Sources

* SKETCH.md (this folder), Secs. 1-5 (Lemma 4.K, I1-I5, A1, risk item 7); STATUS_END_OF_WAVE.md
  rows H2, H3, R14 and item 7.
* Manuscript pr908 `31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6`,
  `standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
  sha256 `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`. Lines read as listed
  in the header, as untrusted data.
* Imported, not re-read: Neukirch, *ANT*, VI and VII §8; Iwaniec-Kowalski, *Analytic Number
  Theory*, Thm 3.8; Gao-Zhao, JNT 209 (2020), eq. (1.1); Serre, *Local Fields*, IV and VI; Milne,
  *CFT*, VIII (5.3), (5.5); DDDS arXiv 2410.03048v2 (`funceq`, `rootnumber`, `cuberep`,
  `cubesupp`), as recorded in SKETCH.md.
* The pure cubic discriminants in Sec. 3.3 are the standard values (`−27m²` for `m ≢ ±1 (9)`,
  `−3m²` for `m ≡ ±1 (9)`, with `m` squarefree). They are used only as sanity checks.

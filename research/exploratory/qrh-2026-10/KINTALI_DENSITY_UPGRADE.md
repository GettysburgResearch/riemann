# Kintali's density input: what it needs exactly, and whether a better one is available

```text
Status: EXPLORATION / bounded literature check. Exact-rational bookkeeping (EXACT_RATIONAL);
  every improved constant below is CONDITIONAL on a Hecke-family density theorem that was NOT
  located in the literature; nothing here is reviewed.
Scope: the zero-density input of [K] Sec. 4.1 (display before (16)) and its effect through [K]
  Lemma 7 on the boundary of [K]'s architecture. Everything else in [K] is taken as written and
  stays unreviewed outside ./reviews/KINTALI_REVIEW.md and ./reviews/KINTALI_LEMMA3_REVIEW.md.
  No statement about RH.
Exact sources or dependencies:
  [K]     Kintali, "A Short Proof of the Quasi-Riemann Hypothesis" (7 Oct 2026), PDF sha256
          f7ddc46632e37466e85951ea67acbd3c2abc19c8259fac51be569b1f6bbbe8e5; pp. 11-16 (Lemma 5,
          (15), Lemma 6, density display, (16), Sec. 4.3 (22)-(23), Lemma 7) and pp. 2, 6-7, 16
          (claims 1 and 3, (9), Sec. 5.1).
  [Hinz]  J. Hinz, Acta Arith. 31 (1976) 167-193, pp. 167-169 (Satz A, Satz B; report of Huxley
          1971); scan aa3127.pdf sha256 5349862b73cc44197ced0a4edc913b79bf16195dcce5b6c766e3adaf2a54ed71.
  [HB79]  D. R. Heath-Brown, "The density of zeros of Dirichlet's L-functions", Can. J. Math. 31
          (1979) 231-240, doi:10.4153/CJM-1979-024-0; pp. 231-235 read (Theorems 1-3, Sec. 2,
          references); PDF sha256 12b21dd1d7c15f6b6cdee171ceb51ab784d987b87739b30adb218c6f6b7e8174.
          Huxley 1976 (J. London Math. Soc. (2) 13, 53-56) and Jutila 1977 (Acta Arith. 32, 55-62)
          are used ONLY as HB79 p. 231-232 states them; they were not read directly.
  [CS05]  M. D. Coleman, A. J. Swallow, Acta Arith. 120 (2005) 349-377; MIMS eprint 298 preprint
          BomVin.pdf sha256 78874ac6180892075bc61e416e8683a4d77ee6a583fe71cb750b33cac4a9a9d5;
          Sec. 4 (pp. 7-8, Lemma 7) and Sec. 7 (Theorems 9-11).
  [TZ16]  J. Thorner, A. Zaman, J. Number Theory 162 (2016), arXiv:1510.08086, Thm 1.1; PDF sha256
          94ddf7864fe74d266cef42816c9621516079321c48069d848527e7d0067b866d.
  [ref4]  Khale-O'Kuhn-Panidapu-Sun-Zhang, arXiv:2008.09677v3, Lemma 3.3 and its proof sketch.
  Abstract or listing only (not read in full): Chen-Gupta-Li arXiv:2507.08296 (v2, 27 Jul 2026);
          Corrigan-Zhao arXiv:2211.00260 (Bull. Aust. Math. Soc. 108 (2023)); Thorner-Zaman
          arXiv:1906.07717 (Adv. Math. 378 (2021)); Guth-Maynard arXiv:2405.20552;
          Cossaboom arXiv:2609.27715 (search listing only).
What was actually run: python3 -I scripts/kintali_density_upgrade.py (exact Fractions + sympy
  1.14.0; ~7 s; script sha256 75d17963e8d8ef630f43a39c729288260340c076fd23f9d349ac0c8a5c6c8eab).
  It computes sup_a [a + min(1, g(a))/2 - 1/3] for 12 density inputs, by the closed form
  sigma_1 + 1/6 and by a direct exact search with left limits plus a 20000-point rational grid,
  and asserts that the two agree and match the pinned values below. Literature: web search plus the
  PDFs and pages listed above.
Smallest remaining gap: a conductor-aspect zero-density estimate for the primitive finite-order
  Hecke characters of Q(sqrt(-3)), power-uniform in the conductor norm Q with any fixed T-power
  loss, with Q-exponent g(sigma) < 1 on some interval (sigma_D, 4/5] with sigma_D < 4/5. Example
  targets: a Hecke analogue of Huxley 1976 (giving 113/120) or of HB79 Thm 3 (giving 941/1002).
  None was located. Proving one would be new mathematics needing its own review.
```

RH is not touched. [K] claims a zero-free half-plane `Re s > 47/48` for Hecke L-functions over
`Q(√−3)` (external, unreviewed). Everything below is about the bookkeeping of that architecture.

## 0. Verdict

* **Best rigorously citable density input: Hinz 1976, Satz A (or Satz B).** It gives the boundary
  **29/30**. [K]'s 47/48 is 29/30 plus [K]'s margin 1/80. **I located no published density theorem
  for this Hecke family that improves 29/30.**
* The σ-dependence of [K]'s `h(σ) = min(3/(2−σ), 2/σ)` buys nothing. `h` peaks at `5/2` exactly at
  `σ = 4/5`, which is the one point that sets the boundary.
* The Dirichlet-character theorems that would help are not proven for Hecke characters. If their
  Hecke analogues held for `K = Q(√−3)` (CONDITIONAL; not located):
  * Huxley 1976 (`(Q²T²)^{(20/9)(1−σ)}`) would give **113/120 ≈ 0.94167**.
  * Heath-Brown 1979 Thm 3 (`(Q²T²)^{2(1−σ)}` for `σ ≥ 129/167`) would give
    **941/1002 ≈ 0.93912**.
  * Conductor-aspect DH on `(3/4, 1)` would give **11/12**. That is the architecture's cap, set by
    its low side and by `|H_η − 1| ≤ 1/2` on `Re s > 11/12`; no density input goes below it.
* **What blocks an upgrade.** Every Huxley/Jutila/Heath-Brown-type improvement located is either:
  * for Dirichlet characters only (`K = Q`), or
  * for Hecke characters in the angular/height aspect, with fixed or polylogarithmic conductor
    (Coleman, Coleman–Swallow), which [K] cannot use.

  The binding point is the left end of the needed σ-window (§1.3). Strong near-1 estimates help only
  if they reach down to about σ ≈ 0.77–0.80.

| density input (conductor exponent) | status for [K]'s family | `σ₁` | boundary `max(11/12, σ₁+1/6)` | with [K]'s 1/80 |
|---|---|---|---|---|
| [K] as written, `g = 5(1−σ)` | as cited | 4/5 | **29/30** | 47/48 |
| Hinz Satz A, `6(1−σ)/(2−σ)` | PUBLISHED, applies | 4/5 | **29/30** | 47/48 |
| Hinz Satz B, `4(1−σ)/σ`, `σ ≥ 3/4` | PUBLISHED, applies | 4/5 | **29/30** | 47/48 |
| Hinz A+B (σ-dependent) | PUBLISHED, applies | 4/5 | **29/30** | 47/48 |
| + Huxley 1976 analogue, `(40/9)(1−σ)` | Dirichlet only | 31/40 | 113/120 | 229/240 |
| + HB79 Thm 2(2) analogue, `10(1−σ)/(3−σ)` | Dirichlet only | 31/40 | 113/120 | 229/240 |
| + Jutila 1977 analogue (DH, `σ ≥ 7/9`) | Dirichlet only | 31/40 | 113/120 | 229/240 |
| + HB79 Thms 1, 3 analogues (DH, `σ ≥ 129/167`) | Dirichlet only | 129/167 | 941/1002 | 38141/40080 |
| Hinz + HB79 Thm 1 analogue only (DH, `σ ≥ 11/14`) | Dirichlet only | 11/14 | 20/21 | — |
| Hinz + Jutila analogue only (DH, `σ ≥ 7/9`) | Dirichlet only | 7/9 | 17/18 | — |
| Hinz + HB79 Thm 3 analogue only | Dirichlet only | 129/167 | 941/1002 | — |
| conductor-aspect DH on `(3/4, 1)` | HYPOTHETICAL | 3/4 | **11/12** (cap) | 223/240 |

(Script output, all exact. "+" rows include Hinz A+B. The 1/80 column only mirrors [K]'s
convention; §1.4 explains why the margin is not intrinsic.)

## 1. What density statement [K] needs, exactly

### 1.1 Where it enters

[K] Sec. 4.1: each nonunit row `u` with `U ≤ N u < 2U` gets a label `a`. The labels form a
**finite** set `51/100 + eℤ` inside `[51/100, β*]`. Every label `a > 51/100` comes with a zero of
an inducing character, with real part `≥ a` and height `≤ 2T` (Lemma 6). By Lemma 2:

* the primitive inducing character has conductor norm `O_{S,Θ}(U)`;
* at most 12 rows map to one character.

So `#B_a ≤ 12 · Σ N(a, 2T, ψ)` over primitive `ψ` with `N f ≤ C·2U`, and [K] (16) is
`#B_a ≪ U^{R(a)+δ}(3+T)^A`, `R(a) = min(1, ·)`. The `1` is the trivial row count `O(U)`.

### 1.2 The statement needed

Put `Q := C·2U` (a conductor **norm**). [K] needs, for each label `σ = a`:

```text
Σ_{N f ≤ Q} Σ*_{ψ mod f} N(σ, T, ψ)  ≪_{σ,ε}  Q^{g(σ)+ε} · T^{B}            (*)
```

* **Family.** Primitive finite-order Hecke characters of `K = Q(√−3)`, i.e. characters of the
  narrow (= wide) ray class groups mod `f`, over all integral `f` with `N f ≤ Q`. This is angular
  type zero: no Grössencharacter `λ^m`. Hinz sums over exactly this family. [K] actually needs
  much less: only the thin set of inducing characters of the rows, at most one ideal class of `u`
  per character, so about `U` characters out of about `U²`. The grand family is a convenience
  (§5).
* **Exponents.** Separate in `Q` and `T`. **Only the conductor exponent `g(σ)` matters.** Any fixed
  `T`-power `B` is absorbed, because [K] fixes the growth order `A` first and then takes
  `T = 3Z^τ` with `τ ≤ m0/(4(A+1))` (Lemma 7 proof, p. 16). Hence an "imperfect hybrid" bound,
  sharp in `Q` and lossy in `T`, is exactly the right kind of input. A result stated as
  `(Q²T^a)^{A(σ)(1−σ)}` contributes `g(σ) = 2A(σ)(1−σ)`, whatever `a` is.
* **Uniformity.**
  * In `Q ≥ 1` and `T ≥ 3`: needed.
  * In `σ`: not needed. For fixed buffer `e` only finitely many labels occur.
  * An `ε`-loss in the exponent is fine: (16) already carries `U^δ`.
  * Log-freeness is not needed.
* **σ-range.** Only `σ ∈ (b − 1/6, 1)` for the target `b` (§1.3).

### 1.3 The reduction: only one σ matters

At the worst dyad (`d = 1/2`), Lemma 7's saving is `E(1/2, a) = a − β* + min(1, g(a))/2 − 1/3`.
So the high side certifies every `b > b*(g)`, where

```text
b*(g) = sup_{a ∈ [51/100,1)} [ a + min(1, g(a))/2 − 1/3 ].
```

For every bound used here, `s + g(s)/2` is strictly decreasing on `[1/2, 1]` (checked by the
script, piece by piece). Validity ranges only begin as `σ` grows. So the sup is the left limit at

```text
σ₁(g) := sup{ σ : g(σ) ≥ 1 },     b*(g) = σ₁(g) + 1/6.
```

**`σ₁` is the point beyond which the grand-family zero count beats the trivial row count `U`.**
Consequences:

* **Below `b − 1/6`, no density input is needed at all**: the trivial count suffices there. A
  density bound valid only for `σ ≥ 4/5 − η` therefore suffices for every target
  `b ≥ 29/30 − η`, provided its Q-exponent satisfies `g(σ) < 2(b + 1/3 − σ)` on the window.
  Near `σ = b − 1/6` that means `g < 1`.
* For `b = 29/30` the window is `(4/5, 1)`. For `b = 11/12` it is `(3/4, 1)`, with requirement
  `g(σ) < 5/2 − 2σ`, i.e. conductor-aspect DH (`g = 4(1−σ)`) with equality exactly at `3/4`.
* In [K]'s normalization (`g = 2A(1−σ)`), the largest admissible `A(σ)` for target `b` is
  `(b + 1/3 − σ)/(1 − σ)`, from the script:

  | target b | σ = b−1/6 | σ = 4/5 | σ = 17/20 | σ = 9/10 | σ = 19/20 |
  |---|---|---|---|---|---|
  | 11/12 | 2.0000 (σ=3/4) | 2.2500 | 2.6667 | 3.5000 | 6.0000 |
  | 941/1002 | 2.1974 (σ=129/167) | 2.3623 | 2.8164 | 3.7246 | 6.4491 |
  | 113/120 | 2.2222 (σ=31/40) | 2.3750 | 2.8333 | 3.7500 | 6.5000 |
  | 29/30 | 2.5000 (σ=4/5) | 2.5000 | 3.0000 | 4.0000 | 7.0000 |

  The requirement relaxes quickly toward `σ = 1`. The binding constraint is always at the left end.
  So near-1 estimates (Huxley/Jutila/Heath-Brown DH ranges, log-free or Pintz-type bounds) help
  only to the extent their range reaches down to `b − 1/6`.
* For a constant `A`, `σ₁ = 1 − 1/(2A)` and `b* = 7/6 − 1/(2A)`. This agrees with
  THRESHOLD_CALCULUS.md §8.
* Why the σ-dependent `h` does not help: `σ₁ = 4/5` is exactly where `3/(2−σ) = 2/σ = 5/2`.
  Hinz Satz A alone and Satz B alone each reach `g = 1` at `σ = 4/5`.

### 1.4 Other constraints and [K]'s margin (bookkeeping observation, PROPOSED)

* The `d`-slope `R(a) + a − 21/25` stays positive for every input in the table: range
  `[0.16, 0.96]` from the script. If it were negative, the worst dyad would be `d = 0`, where
  `E(0,a) = a/2 − β* + 13/150 < 0` anyway.
* The other constraints on `b` are:
  * `C(b) − δ0 − (1/4 + ε) > 0` ([K] Sec. 3: `J ≪ Z^{1/4+ε}` for **every** `ε > 0`, p. 2 claim 1);
  * `r* > 11/12` for `|H_η| ≥ 1/2` ([K] (9): `|H_η − 1| ≤ 1/2` on `Re s > 11/12`).

  Both give 11/12.
* [K]'s choices `ε = 1/32`, large-row cutoff `501/1000`, `v = 4000`, `m0 = 1/1200` are fixed
  conveniences. Each appears adjustable:
  * `ε → 0`;
  * cutoff `1/2 + κ`, with `v > (9/4 + κ)/κ + 1`;
  * `m0 → 0`.

  If so, the same argument gives every `b > max(11/12, b*)`. With Hinz that is **every
  `b > 29/30`, not just 47/48**. This is a reading of [K]'s bookkeeping, not re-verified line by
  line. For targets below `91/96 ≈ 0.9479` (113/120, 941/1002), `ε = 1/32` must be shrunk:
  `ε < b − 11/12 − δ0`.

## 2. Literature survey (primary sources only)

### 2.1 Hecke characters, sum over conductors, power-uniform: what [K] can use

* **Hinz 1976, Satz A/B** (read, p. 168). Any number field `K` of degree `n`. The family is
  `Σ_{Nq ≤ Q} Σ*_{χ mod q}`, over primitive characters of the narrow ray class group, `Q ≥ 1`,
  `T ≥ 2`. Constants depend only on `K`.
  * Satz A: `{Q² T^{…}(log)^{3n}}^{3(1−σ)/(2−σ)}`.
  * Satz B (`3/4 ≤ σ ≤ 1`): `(Q²T^n)^{2(1−σ)/σ}`.

  Conductor exponents `6(1−σ)/(2−σ)` and `4(1−σ)/σ`, both `= 1` at `σ = 4/5`. **This is the input;
  `b* = 29/30`.** It is Montgomery's 1969/71 level transferred to number fields (Hinz p. 167).
* **Huxley 1971** ("The large sieve inequality for algebraic number fields III"), as reported by
  Hinz p. 169. Weighted sum with `N(q)/Φ(q)`: `≪ T(Q² + Q^{5/3}T^{n/3})^{3(1−σ)/(2−σ)}`. Same
  conductor exponent as Satz A, so `b* = 29/30`. Not read directly.
* **[ref4] Lemma 3.3.** `min(3/(2−σ), 2/σ)` with `(R²M^n)`. A proof sketch that reduces to Duke
  and points to Hinz/Coleman. Same conductor exponent: `b* = 29/30`.
* **Thorner–Zaman 2016, Thm 1.1** (read). **Single** modulus `q` (a congruence class group),
  log-free: `Σ_{χ mod q} N(σ,T,χ) ≪ (e^{O(n)} D_K² Q T^n)^{81(1−σ)}` (74 for
  `σ ≥ 1 − 10⁻³`). Not a sum over conductors. Numerically useless here: `A = 81/2` would give
  `b* > 1`. Weiss 1983 is of the same kind.
* **Thorner–Zaman 2021 GL(n) large sieve; Kowalski–Michel** (abstracts only). Log-free family
  bounds with large or unspecified constants. Not useful at `σ ≈ 4/5`.

### 2.2 Hecke characters with Huxley-type exponents: wrong aspect

* **Duke 1989, Thm 2.1** (statement read in the first review). Fixed modulus, sums over
  `λ^m` and height. Not conductor-uniform.
* **Coleman 1990/1992; Coleman–Swallow 2005** (read, pp. 7-8). For imaginary quadratic `K` they
  bound `N(σ, F, W)`, summed over `Nq ≤ F`, `|m| ≤ W`, primitive `χ`, `|γ| ≤ W`.
  * With `F = log^C W`, Lemma 7 gives `W^{2g(σ)(1−σ)}` with `g ≤ 12/5`, and DH (`g ≤ 2`) for
    `σ ≥ 5/6 + ε`. Coleman's earlier `f(σ) = 3/(3σ−1) + ε` for `σ ≥ 3/4` is also in the
    `W`-aspect.
  * The conductor is only **polylogarithmic** in the main parameter. [K] needs `Q ≈ Z^{1/2}`, so
    none of these applies. Their large sieve (Theorem 9: `Q²W² + Na`) is hybrid. The obstacle is
    the large-values and zero-detection bookkeeping, which they only carried out with `F = log^C W`.

### 2.3 Dirichlet characters (`K = Q`): exactly the needed shape, wrong field

From HB79 pp. 231-232 (scan read). All are for `Σ_{q≤Q} Σ*_{χ mod q} N(σ,T,χ) ≪ (Q²T^a)^{A(σ)(1−σ)+ε}`:

* Huxley 1976, J. LMS (2) 13: `a = 2`, `A = 20/9` on `[1/2, 1]`; `a = 2`, `A = 2` on
  `[11/14, 1]`.
* Jutila 1977, Acta Arith. 32: `a = 1`, `A = 2` on `[21/26, 1]`; `a = 2`, `A = 2` on `[7/9, 1]`.
* HB79 Thm 1: `a = 1`, `A = 2` on `[11/14, 1]`.
* HB79 Thm 2: `a = 6/5`, `A = 5/(3−σ)` or `20/9`.
* **HB79 Thm 3: `a = 2`, `A = 2` on `[129/167, 1]`**, uniformly in `Q`, `T`, `σ`.

Because [K] can afford any `T`-loss, the `a = 2` results are the strongest relevant ones. The best
combination is Huxley 20/9 below `129/167` and HB79 Thm 3 above: `σ₁ = 129/167`, `b* = 941/1002`.

* Jutila's `7/9` alone gives `17/18`. On top of Huxley it changes nothing, since
  `7/9 > 31/40`.
* HB79's methods (Huxley [3] zero detection, Huxley's Halász form, Jutila's (1.3)) use:
  * the Montgomery hybrid large sieve;
  * the convexity bound for `L(½+it, χ₁χ̄₂)`;
  * Jutila's k-th-power large-values estimate.

  Number-field versions of the first two exist in the hybrid conductor aspect (Huxley 1968–71,
  Hinz, Duke Thm 1.1(ii), Coleman–Swallow Thm 9). A conductor-aspect Hecke version of the whole
  Huxley/Jutila/Heath-Brown chain **was not located**. Its routineness is HEURISTIC.

### 2.4 Newer large-values work

* **Guth–Maynard** (arXiv:2405.20552; Annals 2026): ζ, `t`-aspect, `30/13`. It uses the
  `n^{it}` additive structure. No conductor-aspect or Hecke-family version was located.
* **Chen–Gupta–Li** (arXiv:2507.08296, abstract): `(qT)^{7(1−σ)/3+ε}` for a **single** modulus
  of Dirichlet characters. Not a sum over conductors. Even as a hypothetical `Q²T` analogue,
  `A = 7/3` gives only `20/21`, which is worse than Huxley's `a = 2` bound for [K]'s purposes.
* **Cossaboom** (arXiv:2609.27715, listing): GL(2), `t`-aspect, a single form.
* **Corrigan–Zhao** (abstract): Dirichlet families of fixed order or sparse moduli, over `Q`.
* None of these is a conductor-aspect Hecke density for `Q(√−3)`.

## 3. What each candidate would require (conditions, stated in full)

**113/120.** Assume the following (CONDITIONAL, not located):

* for primitive finite-order Hecke characters of `Q(√−3)` summed over `N f ≤ Q`,
  `≪_ε Q^{(40/9)(1−σ)+ε} T^{B}` holds for some fixed `B`;
* at each label `σ ∈ (31/40, 1)`, uniformly in `Q ≥ 1`, `T ≥ 3`;
* every unreviewed part of [K] holds, with the bookkeeping re-tuned as in §1.4 (`ε < 1/40 − δ0`).

Then [K]'s architecture gives `β* ≤ b` for every `b > 113/120`.

**941/1002.** As above, plus a conductor-aspect DH for that family on `[129/167, 1]`
(`≪ Q^{4(1−σ)+ε} T^{B}`). Here `ε < 45/2004 − δ0`.

**11/12.** Conductor-aspect DH on `(3/4, 1)`, or any `g` with `g(σ) < 5/2 − 2σ` there. This
is not known even for Dirichlet characters below `129/167`, as far as located. It cannot be
improved by density: the low side and (9) cap it.

## 4. Relation to the OpenAI Part I route

Kintali's grand-family count is wasteful by design. It bounds about `U` rows through a family of
about `U²` characters, so the density estimate must beat `Q^1` (§1.3). A **thin-family** count
`R(σ) < 5/2 − 2σ` on `(3/4, 1)` would also reach the 11/12 cap. Any reasonable density statement
for the sextic family `{ψ_u}` itself would do. [OAI] Part I Sec. 8–9 (saturated witnesses + sextic
large sieve; unreviewed) is a version of this, and it is what [K] replaced to shrink the trust
base. No published zero-density theorem for that sextic Hecke family was located; Corrigan–Zhao
is over `Q`. This is a direction, not a result.

## 5. Not done

* Huxley 1976 and Jutila 1977 were not read; their statements are as quoted by HB79.
* Hinz's and HB79's proofs were not checked.
* No attempt to prove any Hecke analogue.
* No search of MathSciNet/zbMATH (not available). The "not located" findings are limited to web
  search plus the bibliographies of Hinz, HB79, [ref4], Coleman–Swallow and Thorner–Zaman.
* The margin re-tuning in §1.4 is a reading of [K]'s bookkeeping, not a re-verification.
* Harman–Kumchev–Lewis-type Gaussian-prime density work (angular/height aspect) was not examined.

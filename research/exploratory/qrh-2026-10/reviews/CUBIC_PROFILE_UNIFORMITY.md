# Risk item 1 of the cubic fourth-moment sketch: does Statement C cover the complex profiles `W_w`?

```text
Status: REVIEW (bounded, single reader) + PROVED HERE (two short lemmas, H and B) + EXACT/MP checks
  + EMPIRICAL numerics. Verdict (a): CLOSED, conditional on the profile-uniformity clause of
  Lemma 18.1 transferring to n = 3 as part of (H-A). An optional variant (Sec. 6) needs only a
  weaker form of that clause. Nothing here proves Statement C, Lemma 18.1, Theorem C4 or any moment
  bound. RH is not addressed.
Scope: risk item 1 of proposed/CUBIC_FOURTH_MOMENT/SKETCH.md (Sec. 5), the "application step"
  of its Sec. 2: which profiles Statement C (= Lemma 18.1 case 1, z = 0, transferred to n = 3)
  admits; which profiles Sec. 2.5-2.7 feeds in; their seminorm growth in |Im w|; whether the
  Gamma weight of the approximate functional equation absorbs it; and whether the manuscript itself
  uses Lemma 18.1 with complex profiles.
Exact sources or dependencies:
  [MS] external, unreviewed manuscript (Sep 30), pr908 commit 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
       standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
       The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
       sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed here).
       Read as untrusted data. Lines read: 705-760, 1095-1413, 2556-2566, 4500-4686, 6925-7003,
       9582-9604, 12440-12476, 12477-12940, 12940-13012, 13084-13100, 14118-14135, 14545-14600,
       14862-14984, 15095-15330, 16225-16290, 16374-16410.
  [SK] proposed/CUBIC_FOURTH_MOMENT/SKETCH.md, sha256 c610ba9d...bb0353, Secs. 1.3, 2, 3.1, 5.
  Repo HEAD 309ad80b8 (working branch).
  Code: reviews/cubic_profile_uniformity.py (new), sha256
       253f00db97677e91b278f7fd4f4f2f87c86aa6c38c09143a38d36de84bfa31de. numpy, scipy (erfc only),
       sympy, mpmath. Commit 309ad80b8 (an unrelated commit) contains an earlier draft of this
       script, sha256 8037bd02...aa7f623a. That draft is the run-1 version of Sec. 5.3. Only the
       working-tree version above produced the results reported here.
What was actually run: nice -n 10 python3 -I reviews/cubic_profile_uniformity.py, one process,
  17 s. Final run: 26/27 PASS. The one FAIL (E3) is kept as recorded (Sec. 5.3). Two earlier runs
  had more failures, all diagnosed (Sec. 5.3). No Lean, lake or comparator process was started.
Smallest remaining gap: the finite-order profile-uniformity clause of Lemma 18.1 ([MS] l.
  12573-12578, together with the convention at l. 719-722). It must hold at n = 3. At n = 6 it is
  asserted in the statement and justified only by the order-of-choices paragraph (l. 14942-14973).
  No independent line review of that justification is on record. It is part of (H-A) but is not
  listed among A1-A7 in [SK] Sec. 1.3. The manuscript's own 7/8 proof needs a stronger form of the
  same clause (Sec. 4).
```

RH is unsolved. This note concerns one step of a conditional, proposed argument that rests on an
external, unreviewed manuscript. Labels used below:

* **PROVED HERE**: a complete argument is written in this note. It has not been refereed.
* **READ**: what the manuscript asserts, quoted or paraphrased with line numbers. It is not verified.
* **EXACT**: sympy or fractions identity checks.
* **MP**: mpmath high precision. This is not directed or certified arithmetic.
* **EMPIRICAL**: double-precision numerics on a finite range, with fitted exponents.

## 0. Answer in brief

1. **Profiles admitted (READ).** Statement C admits any smooth annular profile: support in a fixed
   compact subinterval of `(0, ∞)`. Nothing restricts profiles to real values, and the manuscript
   applies the lemma to complex ones. The constant depends on a profile only through its support
   window and an upper bound for finitely many homogeneous seminorms `p_j`. It also depends
   polynomially on "separated norm-twist heights". The statement does **not** literally say
   "polynomial in the seminorms". That follows from linearity (Lemma H, Sec. 1.3).
2. **Profiles fed in.** The only family is `W_w(y) = y^{−1/2−w} φ(y)` with `w = ε_0 + it` and
   `ε_0 = 1/log X`. The same profile goes in both slots. The `q`-dependence lies in a phase outside
   the absolute value. PROVED HERE: `p_j(W_w) ≍_j (1+|t|)^j`, and the exponent is exactly `j`. The
   separation norms satisfy `‖W_w‖_{J,sep} ≤ (1+|t|)^J ‖W_{ε_0}‖_{J,sep}`, again with exponent
   exactly `J`.
3. **Bookkeeping (PROVED HERE, exact constants).** Statement C gives at most
   `C X^{1+ε} (1+|t|)^{H}`, where `H = 4J*` and `J*` is the lemma's finite seminorm order. The
   weight `|Γ(1/2+w)| |dw/w|` integrates `(1+|t|)^H` to at most
   `√2 e^{1/3} 2^{H+2} [asinh(log X) + Γ(H+1)(2/π)^{H+1}]`, which is finite for every `H`. The true
   critical growth is `e^{c|t|}` with `c = π/2`. The `X`-exponent stays `1 + ε`.
4. **Manuscript's own use (READ).** Prop 19.2 (`prop:detector-counts`) applies Lemma 18.1, in
   both cases including case 1, to two copies of the witness polynomial. The witness profile is
   `W_2(y) y^{−σ−i(γ−ν)}`: complex, with height up to a power of `Z`. Its polynomial height
   dependence, of a degree fixed before `T_1 = Z^τ`, is load-bearing for the 7/8 proof. That use is
   stronger than what the cubic application needs.
5. **Verdict (a).** The register line is in Sec. 7.

## 1. What Statement C allows (READ, with one short lemma PROVED HERE)

### 1.1 The statement

Lemma 18.1 (`lem:plain`, l. 12531-12579) bounds
`Σ_{k ∈ R_z} |S_{ψ_k}(n_1; W_1) S_{ψ_k}(n_2; W_2) Q|² ≪ Z^{M+ε}`. Case 1 is `z = 0`, with no
restriction on the bounded lengths. The closing sentences read (l. 12571-12578):

> All real length parameters range over prescribed bounded sets. The mesh depends only on those
> sets and ε, uniformly for κ∈[3/4,1]. For each fixed Z-independent arithmetic datum 𝒜 and fixed
> slot count, the bound uses finitely many smooth seminorms and a fixed polynomial in the
> separated norm-twist heights. Their orders, and the bound itself, are uniform over all moving
> moduli, admissible masks, and frozen outer labels in the stated ranges.

The profiles enter through `S_ψ(n; W) = Z^{−n/2} Σ_l ψ(l) W(q_l/Z^n)` (l. 705-708). Their class
is fixed at l. 719-722:

> An annular test is a smooth function with support in a fixed compact subinterval of (0,∞).
> Families of annular or coupled profiles are used only with fixed logarithmic support and uniform
> bounds for every logarithmic derivative that is invoked.

The uniformity convention (l. 728-740) says that "finite seminorm orders, polynomial height
orders, implied constants, and lower thresholds may depend on 𝒜", and are uniform over moving
moduli and outer labels.

### 1.2 Seminorm definitions (l. 1102-1121)

For `w` on `(0,∞)^d` with logarithmic support in a fixed compact `Ω`, the manuscript sets
`w_log(u) = w(e^{u_1}, …, e^{u_d})` and defines

    p_j(w) = Σ_{|α| ≤ j} sup_u |∂^α w_log(u)|,
    ŵ(t) = ∫ w_log(u) e^{−i t·u} du,     ‖w‖_{J,sep} = ∫ |ŵ(t)| (1+|t|)^J dt,
    p_j(𝐰) = 1 + Σ_i p_j(w_i)   for a tuple (inhomogeneous).

Lemma 4.5 gives `‖w‖_{J,sep} ≪ p_{J+d+2}(w)`. Lemma 4.7 gives the twisted-Mellin cost: for
`W(y) y^{iω}`, an extra factor `(1+|ω|)^{h+j}` (l. 1385-1386). The manuscript stresses that the
single-profile `p_j` is homogeneous and the tuple seminorm is not (l. 2563-2564, 9586-9587).

### 1.3 What the constant may depend on

| property | Lemma 18.1, case 1, as stated | where |
|---|---|---|
| values | not restricted to real. The proof conjugates profiles (l. 12785-12789), reflects twisted profiles `W(y)y^{iω}` (l. 12719-12731), and its lattice lemma uses `q_l^{it} W_i(q_l/X)` (l. 14551-14556) | READ |
| support | a fixed compact subinterval of `(0,∞)`, the "profile window". It is fixed before the threshold (l. 14892-14895) | READ |
| smoothness | `C^∞` in `log y`. Only finitely many derivatives are invoked | l. 719-722, 14942-14950 |
| seminorms | homogeneous single-profile `p_j`, up to a finite order `J*` chosen backwards through the `D` stages | l. 12574-12575, 14942-14950, 14971 ("finite-order uniformity") |
| constant | depends on `𝒜`, `ε`, the length ranges, the windows, an upper bound for `p_{J*}(W_1), p_{J*}(W_2)`, and a fixed polynomial in separated norm-twist heights | l. 12574-12578, 728-740 |
| threshold `Z_0` | depends on the same data | l. 14946-14949 |

**Reading R (READ; the natural reading of l. 12574-12576 with l. 719-722).** There are `J*` and,
for each `K`, constants `C_K, Z_K` such that the following holds. For all `W_1, W_2` with
logarithmic support in `Ω` and `p_{J*}(W_i) ≤ K`, and for `Z ≥ Z_K`, the left side of (2.1) is at
most `C_K Z^{M+ε}`. Here `J*`, `C_K` and `Z_K` depend only on `𝒜`, `ε`, the length ranges and `Ω`.

**Lemma H (PROVED HERE).** Under reading R there are `C, Z_1` such that, for all nonzero
`W_1, W_2` with logarithmic support in `Ω` and all `Z ≥ 2`,

    Σ_{k ∈ R_0} |S_{ψ_k}(n_1; W_1) S_{ψ_k}(n_2; W_2)|² ≤ C p_{J*}(W_1)² p_{J*}(W_2)² Z^{M+ε}.

*Proof.*

* `S_ψ(n; cW) = c S_ψ(n; W)`, so the left side has bidegree `(2,2)` in `(W_1, W_2)` (check A6).
* Apply R with `K = 1` to `W_i / p_{J*}(W_i)`, and multiply back.
* For `2 ≤ Z < Z_1`, use the trivial bound
  `|S_ψ(n; W)| ≤ sup|W| · #{l : q_l ≤ 2Z^n} · Z^{−n/2} ≪ p_0(W) Z^{n/2}` and `≪ Z^m` rows. This
  gives `≪_{Z_1} p_0(W_1)² p_0(W_2)²`, and `p_0 ≤ p_{J*}`. ∎

The manuscript uses the same normalization itself: "write F_R = m_R F̃_R … If a polynomial … is
linear in this whole profile, then 𝒫(F_R) = m_R 𝒫(F̃_R)" (l. 9596-9601).

**Correction to the register wording.** Lines 12573-12577 assert *finite-order* seminorm
dependence and *polynomial* dependence on norm-twist heights. Polynomial dependence on the
seminorms, of exact bidegree `(2,2)`, is a consequence (Lemma H), not a literal assertion.

## 2. The profiles that Sec. 2 of the sketch feeds in

From [SK] Sec. 2.5-2.7:

* `A_1^{(j)}(q) = (2πi)^{−1} ∫_{(ε_0)} (2π)^{−w} (Γ(1/2+w)/Γ(1/2)) (√(3Nq)/N_j)^w S_q(N_j; W_w) dw/w`;
* `W_w(y) = y^{−1/2−w} φ(y)`, with `w = ε_0 + it` and `ε_0 = 1/log X`;
* `φ ∈ C_c^∞([1/2, 2])` with `Σ_j φ(y/2^j) = 1`.

The following points hold.

* **Only one family enters.** The `q`-dependent factor `(√(3Nq)/N_j)^w` multiplies the whole
  sum. Its modulus is `≤ (3X)^{ε_0/2} ≤ e`, and Hölder takes it out before `|S_q|⁴` is formed.
  Statement C therefore sees `W_1 = W_2 = W_w`, which depends on `t` and `ε_0` only, not on `q` or
  on the row.
* **The `S`-part does not change the profile.** [SK] Sec. 2.6 only shifts the length:
  `n = log_X (N_j / (3^a 4^b)) ∈ [0, 1/2 + ε]`. The values `n ∈ [−log 2/log X, 0)` occur only when
  `N_j/(3^a4^b) ∈ [1/2, 1)`. Such a sum contains at most the unit ideal and is `O(1)` trivially.
* **Log coordinates.** Put `g(u) = φ(e^u)`, supported in `Ω = [−log 2, log 2]`. Then
  `(W_w)_log(u) = e^{−(1/2+ε_0)u} g(u) · e^{−itu}`.
* **Two equivalent descriptions.**
  * (D1) A one-parameter profile family whose seminorms grow in `t`.
  * (D2) A fixed untwisted profile `W^{(0)}(y) = y^{−1/2−ε_0} φ(y)` times a pure norm twist
    `y^{−it}` of height `|t|`. This is exactly the form `W(y) y^{iω}` treated at l. 12719-12726, and
    the form of the manuscript's own witness profiles (Sec. 4).

### 2.1 Seminorms as functions of `|Im w|` (PROVED HERE)

Write `a = 1/2 + w`. Here `p_j(φ)` means `Σ_{k ≤ j} sup |g^{(k)}|`.

* **(S1) Upper bound.** By Leibniz (check A1),
  `∂^k[e^{−au} g] = e^{−au} Σ_i C(k,i)(−a)^i g^{(k−i)}`. On `Ω`, `|e^{−au}| ≤ 2^{1/2+ε_0}`, and
  `Σ_i C(k,i)|a|^i = (1+|a|)^k`. Since `1 + |a| ≤ 3/2 + ε_0 + |t| ≤ (5/2)(1+|t|)` for `ε_0 ≤ 1`
  (check A8),

      p_j(W_w) ≤ 2^{1/2+ε_0} (j+1) p_j(φ) (1+|a|)^j ≤ 2^{3/2} (j+1) (5/2)^j p_j(φ) (1+|t|)^j.

* **(S2) Lower bound.** At `u = 0` we have `g(0) = φ(1) = 1`. Every derivative `g^{(k)}(0)`,
  `k ≥ 1`, vanishes, because `g ≡ 1` to infinite order there for this `φ`. For a general partition
  these derivatives contribute only `O_j(|a|^{j−1})`. So `∂^j (W_w)_log (0) = (−a)^j`, and

      p_j(W_w) ≥ |a|^j ≥ ((1/2 + |t|)/√2)^j ≥ ((1+|t|)/(2√2))^j.

  Together with (S1), `p_j(W_w) ≍_j (1+|t|)^j`: **the growth exponent is exactly `j`**.
* **(S3) Separation norm.** `ŵ_w(τ) = ĝ_0(τ + t)`, where `g_0 = e^{−(1/2+ε_0)u} g`. With
  `1 + |s − t| ≤ (1+|s|)(1+|t|)`,

      ‖W_w‖_{J,sep} = ∫ |ĝ_0(s)| (1+|s−t|)^J ds ≤ (1+|t|)^J ‖W^{(0)}‖_{J,sep}.

  The exponent is exactly `J`. Lemma 4.5 used generically would give `p_{J+3}`, exponent `J+3`.
* **(S4) Mellin-tail norms.** The weighted derivative norms in eq:pointwise-mellin-tail satisfy
  `Σ_{j≤N} ∫ y^σ |D^j W_w| dy/y ≤ C_N (1+|t|)^N`, by the same Leibniz argument.
* **(S5) Reading D2.** `p_j(W^{(0)}) ≤ 2^{3/2}(j+1)(5/2)^j p_j(φ)`, uniformly for
  `ε_0 ∈ (0, 1]`. The twist height is `|t|`.

**Consequence (PROVED HERE, given Statement C with reading R).** By Lemma H and (S1), or by
reading D2 and the height clause,

    Σ_{k ∈ R_0, Nk ≤ X} |S_{ψ_k}(n; W_w)|⁴ ≤ C X^{1+ε} (1+|t|)^H,

with `H = 4J*` (D1) or `H = h*`, the fixed height order (D2). Both are finite and fixed by
`(𝒜, ε, ranges)`. The manuscript does not give their values.

## 3. The two checks

### 3.1 Support and smoothness (PROVED HERE)

| hypothesis | `W_w` | verdict |
|---|---|---|
| compact support in `(0,∞)`, fixed | `[1/2, 2]` for every `w` and `X` | met |
| smooth in `log y` | `C^∞`, since `φ ∈ C_c^∞` and `y^{−a}` is smooth on `(0,∞)` | met |
| real-valued? | not required (Sec. 1.3); `W_w` is complex | met |
| uniform in `X` | the only `X`-dependence is `ε_0 ∈ (0, 1]`, and (S1) is uniform there | met |
| bounded lengths | `n ∈ [0, 1/2 + ε]`; the negative sliver is trivial | met |
| rows | `Z = X`, `m = 1`, `q = 0`, `k ∈ R_0` with `Nk ≤ X` ([SK] 2.7) | met |

### 3.2 Growth against decay: exact bookkeeping (PROVED HERE; checks in brackets)

**Weight.** `dν(w) = |Γ(1/2+w)/Γ(1/2)| |(2π)^{−w}| |dw|/|w|` on `Re w = ε_0`.

* Stirling's formula with remainder `|μ(s)| ≤ 1/(6|s|)` for `Re s > 0` gives
  `|Γ(σ+it)| = √(2π) |s|^{σ−1/2} e^{−t arg s − σ + Re μ}`. Here `t arg s ≥ π|t|/2 − σ` and
  `|s| ≥ 1/2`. So, for `0 ≤ ε_0 ≤ 1/2` and all real `t`,

      |Γ(1/2+ε_0+it)| ≤ √(2π) e^{1/3} (1+|t|)^{ε_0} e^{−π|t|/2}      [M2: max ratio 0.717 on |t| ≤ 400].

**Integral.** Split at `|t| = 1`.

* Near part, `|t| ≤ 1`: `∫_{−1}^{1} dt/√(ε_0²+t²) = 2 asinh(1/ε_0)` [A3].
* Far part, `|t| ≥ 1`: `(1+t)^{H+1}/t ≤ 2^{H+1} t^H`, and
  `∫_0^∞ t^H e^{−πt/2} dt = Γ(H+1)(2/π)^{H+1}` [A2].

Together:

    I(H) := ∫ (1+|t|)^H dν ≤ √2 e^{1/3} 2^{H+2} [ asinh(1/ε_0) + Γ(H+1) (2/π)^{H+1} ]     [M4],

which is finite for every `H ≥ 0`. At `ε_0 = 1/log X` the first term is `log(2 log X) + o(1)`.

**Critical rate.** Growth `e^{c|t|}` is absorbed if and only if `c < π/2` [A5b]. So polynomial
growth of **any** degree is beaten, with infinite margin on the polynomial scale.

**Assembly.**

    Σ_q |L(1/2,χ_q)|⁴ ≤ 16 Σ_q |A_1(q)|⁴
      ≤ 16 (J+1)⁴ max_j Σ_q |A_1^{(j)}(q)|⁴ + O(X^{−9})                      (J+1 ≤ log X pieces)
    Σ_q |A_1^{(j)}(q)|⁴ ≤ e⁴ I(0)³ ∫ Σ_q |S_q(N_j; W_w)|⁴ dν(w)                (Hölder in w)
      ≤ e⁴ I(0)³ · 5⁴ · C X^{1+ε} · I(H)                                      ([SK] 2.6, Sec. 2.1)

Here `I(0) = 2 log log X + O(1)`. Numerically (MP, M3) `I(0) = 5.80` at `X = 10^8` and `13.15` at
`X = 10^256`, and `I(0) − 2 log log X` stays in `[−0.03, 0.39]`. The total is
`≪_ε X^{1+ε} (log X)⁴ (log log X)⁴`, so the exponent of `X` is `1 + ε` [A7].

**Cosmetic correction to [SK] 2.7.** The losses are `(log X)⁴`, not `(log X)³`; the extra factor
is the sum over the `J+1` dyadic pieces. Likewise `(log log X)⁴`, not `(log log X)³`, since
`I(H) ≍ log log X + C_H`. Both are `X^{o(1)}`.

**Controls (EXACT).**

* [A4] If the approximate functional equation weight were a sharp cutoff (Mellin kernel `1/w`, no
  Gamma factor), the `w`-integral would diverge already at `H = 0`.
* [A5] If the separating kernel decayed only like `(1+|t|)^{−B}`, it would absorb `(1+|t|)^H` only
  when `B > H + 1 = 4J* + 1`. This would matter for a partition of finite smoothness. It does not
  matter for the `C^∞` partition `φ`: E8 shows the Mellin envelope of `φ` decays faster than any
  fixed power, with local slopes `−2.5, −4.1, −6.7, −7.5, −10.5, −14.7` on `t ∈ [10, 800]`.

## 4. Does the manuscript itself use Lemma 18.1 with complex profiles? Yes (READ)

* **The detector makes complex profiles.** The witnesses of Prop 8.3 (`prop:detector-witness`,
  l. 4510-4686) have profiles
  `W_M(x) = W_1(x) V_≤(Dx/D_*) x^{−σ−i(γ−ν)}` and `W_S(y) = W_2(y) y^{−σ−i(γ−ν)}`
  (l. 4653-4656). Here `σ` is the real part of a zero and `|γ − ν| ≤ (3I+2)T_1`. "Their untwisted
  profiles form a uniformly smooth annular family" (l. 4540). This is structure D2, the same as
  `W_w`.
* **Prop 19.2 feeds them to Lemma 18.1.** Prop 19.2 (`prop:detector-counts`, l. 15185-15246)
  applies Lemma 18.1 to two copies of `S_m` (l. 15179-15180, 15242-15244). Case 1 is used
  explicitly: "at zero plain capacity use the zero-slot case of Lemma 18.1" (l. 15218-15219), and
  for `m ≥ 1/2` (l. 15312-15313).
  * Before applying it, the proof conjugates "both witness profiles and every selected slot
    profile" (l. 15137-15157).
  * The slot profiles carry the complex factor `(q_p/P_i)^{z_phys − 1}` (l. 15149).
  * The rowwise heights are then handled by Lemma 4.5's Sobolev step, at "a fixed power of
    `1+T_1`" (l. 15163-15168). The bound carries `(1+T_1)^{A_𝒜}` (l. 15201-15203, 15235-15239).
* **The degree must be fixed early.** `T_1 = Z^τ`, and τ is chosen *after* the fixed height
  order (l. 12471-12473, 16391-16407).
* **Lemma 18.1's own proof is written for twisted profiles.** Reflection of `W(y)y^{iω}` costs "a
  fixed polynomial in `1+|ω|`" (l. 12719-12731). The masked rectangle cancellation lemma uses
  `q_l^{it} W_i(q_l/X)` with `(1+|t|)^J` (l. 14551-14569).

So the clause is **load-bearing for the 7/8 proof**, and in a stronger form than the cubic
application needs:

* The manuscript needs a polynomial of a degree fixed before τ, at heights up to `Z^τ`.
* The cubic route needs only `∫(growth) dν < ∞`. Any polynomial degree suffices, and even
  exponential growth at a rate below `π/2`.

A failure of the clause would break Prop 19.2 as written before it touched this application.

## 5. Numerics (EMPIRICAL sanity check; script reviews/cubic_profile_uniformity.py)

### 5.1 Setup

The partition is `φ(y) = ρ(log₂ y) − ρ(log₂ y − 1)`, where `ρ` is the smooth step
`S(x) = 1/(1 + e^{1/x − 1/(1−x)})` shifted to `[−1, 0]`. Then `g(u) = S(1 − |u|/log 2)`, and
`Σ_j φ(y/2^j) = 1` to `4·10^{−16}` (E0). Throughout `ε_0 = 1/log 10^8 = 0.0543`.

Each `p_j(W_w)` was computed in two ways:

* the exact Leibniz formula (A1), with sympy-derived derivatives of `S`, on a 200001-point grid;
* filtered spectral differentiation (FFT on `2^15` points, modes below `10^{−15}·max` removed).

The two agree to `1.7·10^{−6}` relative (E1). The inputs `sup|g^{(k)}|` also agree with
`mpmath.diff` to `7.5·10^{−5}` (E1a).

| `t = Im w` | `p_0` | `p_1` | `p_2` | `p_3` | `p_4` |
|---|---|---|---|---|---|
| 0 | 1.058 | 4.325 | 30.44 | 472.5 | 1.397e4 |
| 10 | 1.058 | 11.64 | 140.5 | 1907 | 3.362e4 |
| 20 | 1.058 | 22.21 | 466.7 | 1.028e4 | 2.414e5 |
| 50 | 1.058 | 53.95 | 2718 | 1.380e5 | 7.075e6 |
| 100 | 1.058 | 106.8 | 1.070e4 | 1.074e6 | 1.081e8 |
| 200 | 1.058 | 212.6 | 4.255e4 | 8.517e6 | 1.706e9 |

### 5.2 Results

* **E2 (bracket).** For all 17 values of `t` in `[0, 200]`:
  * `p_j ≤ 2^{1/2+ε_0}(j+1) p_j(φ)(1+|a|)^j` (worst ratio 0.720);
  * `p_j ≥ (1/2)(1+t)^j` for `t ≥ 50` (worst `p_j/(1+t)^j` is 1.038).
* **E3b, E3c (exponent).** The local log-log slope on `[140, 200]` is
  `0.000, 1.000, 2.005, 3.008, 4.010` for `j = 0..4`. A quadratic-in-`1/t` extrapolation gives
  `−0.000, 1.000, 1.999, 3.000, 4.002`. On `t ≤ 50` only, the slopes run high
  (`p_4`: 4.26), because the `t`-independent constants `sup|g^{(k)}|` reach about `10^4`.
* **E7 (separation norms).** The fitted exponents are `0.000, 1.003, 2.025, 3.068` for
  `J = 0..3`. Every value obeys `‖W_w‖_{J,sep} ≤ (1+t)^J ‖W_{ε_0}‖_{J,sep}`.
* **E8.** The Mellin envelope of `φ` decays super-polynomially (Sec. 3.2).
* **E9 (variant B, Sec. 6).** Over `λ ∈ [−30, 8]`, `sup_λ p_j(V_λ)` is
  `1.051, 4.272, 29.77, 459.5, 1.355e4`. It lies below the bound `2^{1/2} p_j(φ) Σ_{k≤j}(5/2)^k`,
  and the supremum is the `λ → −∞` limit `y^{−1/2}φ`.

**Failing controls.**

* **E4.** The exponent hypothesis `j+1` is rejected for every `j`: `γ − (j+1)` is between
  `−0.89` and `−1.00`.
* **E5, E6 (polynomial-growth detector).** The detector compares the extrapolated exponents on
  `[20,60]` and `[60,200]`.
  * It accepts `W_w`: the windows give `0.00, 1.00, 2.04, 3.11, 4.23` and
    `0.00, 1.00, 2.00, 3.01, 4.03`.
  * It rejects the family `y^{−1/2−ε_0+t/10−it} φ`, whose growth is exponential: the windows give
    `2.6 … 6.9` and `11.5 … 15.5`.
  * Note that this control family grows at rate `(log 2)/10 < π/2`. It would still be integrable
    against `dν` (A5b). The detector tests polynomial growth, not integrability.
* **A4, A5.** The exact controls of Sec. 3.2.

### 5.3 Run history (all runs reported)

* **Run 1: 17/23.**
  * E1 failed. Unfiltered spectral differentiation amplifies round-off by `|k|^j`; at `j = 4` the
    error was 5% relative, and at `j = 5` worse. Diagnosis: a stand-alone comparison against
    `mpmath.diff`. Fix: the noise-floor filter.
  * Three criteria were ill-posed:
    * M3 required `I(0) − 2 log log X` constant to 0.05. The drift is the
      `O(ε_0 log(1/ε_0))` correction. M3 now tests boundedness and shrinking increments.
    * E3 (old) required `p_j/(1+t)^j` to vary by less than 12. The ratio is bounded but starts
      near `10^4` at `t = 0`. It was replaced by the bracket E2.
    * E8 used raw values of an oscillating `|Mφ|`. It now uses the envelope.
* **Run 2: 23/24.** E3 (linear-in-`1/t` extrapolation, tolerance 0.1) failed at `j = 4`
  (`γ = 4.112`).
* **Run 3 and the final run: 26/27.** E3 is kept unchanged and still FAILS. E3b and E3c were added
  *after* it failed, as is stated in the script. A5b was added in the final run.

These numerics show only that the explicit family has the computed growth. They are no evidence
for Statement C.

## 6. Variant B: a hardening that needs only bounded real profiles (PROVED HERE, given Statement C for one bounded family)

This variant avoids complex profiles, growth in `t`, Lemma H and the finite-order assumption. It
uses the manuscript's own device for row-dependent scales (eq:parameter-sobolev, l. 1143-1151:
"rowwise choices of scales in a polynomial range cost powers of log Z").

**Setup.**

* `Φ_1(x) = Γ(1/2, 2πx)/Γ(1/2) = erfc(√(2πx))`. Exchange `Γ(1/2+w) = ∫ e^{−s} s^{−1/2+w} ds`
  with the `w`-integral; then `(2πi)^{−1}∫ (s/(2πx))^w dw/w = 1_{s > 2πx}`. Check M1 confirms this
  to `2·10^{−32}`.
* Put `λ_q = log(N_j/√(3Nq))` and `V_λ(y) = y^{−1/2} φ(y) Φ_1(e^λ y)`. This is real and supported
  in `[1/2, 2]`.
* Then, exactly, `A_1^{(j)}(q) = S_q(N_j; V_{λ_q})`. No Mellin integral is used.

**Uniform seminorms.**

* With `D = x d/dx`, `D Φ_1(x) = −√(2x) e^{−2πx}`. Each `D^k erfc(√z)` is a polynomial in `√z`
  times `e^{−z}` and tends to 0 at both ends [A9]. So `d_k := sup_{x>0} |D^kΦ_1(x)| < ∞`.
* By Leibniz,

      p_j(V_λ) ≤ 2^{1/2} max(1, d_1, …, d_j) p_j(φ) Σ_{k ≤ j} (5/2)^k,

  uniformly in `λ ∈ R`. The same holds for `∂_λ V_λ(y) = y^{−1/2} φ(y) (DΦ_1)(e^λ y)` [E9].

**Sobolev step.** For `F ∈ C^1` and `I = [λ_0 − 1, λ_0 + 1]`, put `G = F²`. Averaging
`|G(λ_0)| ≤ |G(y)| + ∫_I |G'|` over `y ∈ I` and using `|G'|² ≤ 2|F|⁴ + 2|F'|⁴` gives

    |F(λ_0)|⁴ ≤ 9 ∫_I ( |F|⁴ + |F'|⁴ ) dλ.

Take `F(λ) = S_q(N_j; V_λ)`, so `F' = S_q(N_j; ∂_λ V_λ)`, and `λ_0 = λ_q`. Then
`λ_q ∈ Λ_j = [log N_j − ½ log 3X, log N_j − ½ log 3]`. Apply the `S`-part split of [SK] 2.6
inside the integral. Enlarge to `R_0` by positivity and use Tonelli:

    Σ_q |A_1^{(j)}(q)|⁴ ≤ 9 (½ log X + 3) · 2 · 5⁴ · sup_{λ} C_C(V_λ, ∂_λV_λ) · X^{1+ε}.

Here `C_C` is Statement C's constant for the family `{V_λ, ∂_λ V_λ : λ ∈ R}`. That family is
real-valued, has the fixed window `[1/2, 2]`, and has uniformly bounded logarithmic derivatives of
every order. This is exactly the family hypothesis of l. 719-722. The loss is one `log X`, in
place of `(log log X)⁴ I(H)`.

**What variant B still needs.** Uniformity of Statement C over one bounded family of real
profiles. Some uniformity is unavoidable: the approximate functional equation weight depends on `q`
through `Nq`, so any route meets a continuum of profiles. Variant B needs the weakest form.

## 7. Verdict and register update

**Verdict (a): closed.** Statement C, read as Lemma 18.1 case 1 *including* its uniformity clause
(l. 12571-12578, with l. 719-722), covers the application:

* `W_w` meets the support and smoothness hypotheses. Complex values are admitted, and the
  manuscript itself applies the lemma to the same structure `W(y) y^{−σ−iT}`.
* `p_j(W_w) ≍ (1+|Im w|)^j` exactly, and `‖W_w‖_{J,sep} ≤ (1+|Im w|)^J ‖W_{ε_0}‖_{J,sep}`.
* Statement C then gives `≤ C X^{1+ε} (1+|Im w|)^{4J*}` (Lemma H), or `(1+|Im w|)^{h*}` under the
  twist reading.
* `∫ (1+|t|)^H dν ≤ √2 e^{1/3} 2^{H+2} [asinh(log X) + Γ(H+1)(2/π)^{H+1}]` for every `H`. The
  critical rate is exponential (`π/2`), not polynomial.
* The final bound is `≪_ε X^{1+ε} (log X)⁴ (log log X)⁴`.

Variant B (Sec. 6) is an optional hardening. It needs only uniformity over one bounded family of
real profiles. It should be preferred if the finite-order clause is ever in doubt.

**Recommended edits to [SK].**

* State the uniformity clause inside Statement C (Sec. 3.1).
* Add to the (H-A) table: "A8: finite-order profile uniformity, l. 12571-12578, justified at
  l. 14942-14973; convention l. 719-722".
* Correct the loss count in Sec. 2.7 to `(log X)⁴ (log log X)⁴`.

**Risk-register line for item 1:**

| # | step | status | evidence | most likely failure mode |
|---|---|---|---|---|
| 1 | Application (Sec. 2): AFE, root-number removal, dyadic split, Mellin separation, `S`-part, rows = family | **proved here** (given Statement C); profile uniformity **closed** (reviews/CUBIC_PROFILE_UNIFORMITY.md, verdict (a)) | `p_j(W_w) ≍ (1+\|Im w\|)^j`; Statement C at most `(1+\|Im w\|)^{4J*}` by finite-order uniformity and bidegree-(2,2) homogeneity; `∫(1+\|t\|)^H dν < ∞` for every `H` (critical rate `e^{π\|t\|/2}`); variant B needs only a bounded real family; checks 26/27 (E3 fail documented) | the finite-order profile-uniformity clause of Lemma 18.1 (l. 12571-12578, justified only at l. 14942-14973) fails or does not transfer to n = 3; this would also break the manuscript's Prop 19.2, which needs a stronger form |

## 8. What was not done

* The justification of the finite-order clause (l. 14942-14973) was read, not reviewed.
* Nobody has checked that every internal step of Lemma 18.1 preserves finite seminorm order for
  complex profiles. That covers the reflection closure, the comparison rectangles, Θ-row
  cancellation and the coefficient lemma. Only the sites where the manuscript asserts it were
  read: l. 12719-12731, 12886-12901, 14551-14569 and 14942-14973.
* The Gamma-weight bound uses the standard Stirling remainder; it was checked in MP, not re-proved.
* Nothing here bears on items 2-13 of the register. In particular it does not bear on item 9 (A5,
  the centred stage), which remains the single most likely failure point of the route.

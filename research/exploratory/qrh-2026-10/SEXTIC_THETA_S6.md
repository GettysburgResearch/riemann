```text
Status: SURVEY [LIT] + inference [INF, HEURISTIC] + EMPIRICAL (FLOAT, double precision, not directed,
  not certified). No theorem is proved here. RH remains unproved; the 11/12 and 5/6 boundaries are
  claims or conditional models from LEVERAGE_FAMILIES.md, not results.
Scope: hypothesis (S6) of LEVERAGE_FAMILIES.md §5: some theta function on the 6-fold cover of GL(2)
  over K = Q(omega) has tau_6(p) = eta(p) gamma_{-+1}(p) at every prime p outside S (eta a Hecke
  character, gamma_{+-1} the normalized sextic Gauss sum, exact sign). Literature status of tau(p),
  tau(p^2), tau(p^3) for n = 6 (and n = 4); a residue (Patterson-bias) experiment at norm <= 3e5.
Exact sources or dependencies (primary sources, e-prints fetched 2026-10-10, sha256 of the download):
  [BH]   Broeker-Hoffstein, "Fourier coefficients of sextic theta series", Math. Comp. 85 (2016)
         1901-1927, arXiv:1312.0568 (e-print 4e05642b...3f1386). Read: Sec. 1, 2, 5 in full.
  [CFH]  Chinta-Friedberg-Hoffstein, "Double Dirichlet series and theta functions", Springer Proc.
         Math. 9 (2012) 149-170; chinta.ccny.cuny.edu/publ/patterson.pdf (7486de15...05fb5f3).
         Read: Sec. 1-2, 5, 6 (statements).
  [DDHL] David-Dunn-Hamieh-Lin, "Quartic Gauss sums over primes and metaplectic theta functions",
         arXiv:2306.11875, Jan 2026 revision (59f5e152...b0de96). Read: Sec. 1 and the theta section.
  [FGd]  Friedberg-Ginzburg, "Descent and theta functions for metaplectic groups", JEMS 20 (2018),
         arXiv:1403.3930 (a571d1e3...ac9ef5d). Read: intro, Sec. 7 (Theorem "maincfh").
  [P14]  Patterson, "The Fourier coefficients of metaplectic theta series on GL(2) over rational
         function fields", arXiv:1411.7594 (90a80fa5...bf90b). Read: Sec. 1, 2 (summary), 4.
  Known only through [BH], [CFH], [DDHL], [FGd]: Kazhdan-Patterson (Publ. IHES 59, 1984), Patterson
  (1977, 1984), Eckhardt-Patterson (PLMS 64, 1992), Suzuki (Crelle 340, 1983; Duke 90, 1997),
  Hoffstein (Invent. 107, 1992; CRM 1993), Bump-Hoffstein (LNM 1383, 1989), Wellhausen (Diss.
  Goettingen 1996), Deligne (Bourbaki 539). BBFH (PROMS 9, 2012): abstract level only, via
  A2_LITERATURE.md. No aggregator sites used.
  Code: a2/s6_gauss.c (sha256 d8266d88...0a6164), a2/s6_theta_bias.py (14d31c31...910fdc4; the run
  used d142611e...328bb2, which differs only in the docstring), a2/eis.py (87ca11d9...2798e65,
  imported, not modified). Identities S1-S3 of LEVERAGE_FAMILIES.md (gamma_1 = conj chi(4)
  gamma_3 gamma_2^2, gamma_2^3 = -alpha).
What was actually run: gcc -O2 a2/s6_gauss.c into the session scratchpad (not the repo), then
  nice -n 10 python3 a2/s6_theta_bias.py 300000 100 OUT.json BIN   (single process, 79 s)
  and the same at 100000 50 (12 s). OUT sha256 4ce62569...6b547745 (scratchpad; rerun to reproduce).
  25 991 prime elements with norm <= 3e5, 84 677 squarefree primary c; Gauss sums checked against
  eis.gamma (156 checks, max dev 1.4e-13). The two gamma_{+-1}^2 identities of Section 3 were
  checked with eis.gamma at all 47 primes of norm <= 200 (FLOAT, max dev 2.6e-15; inline command,
  not saved as a script).
Smallest remaining gap: the 216-component residue vector rho(pi, eta) (eta in K_S^*/K_S^{*6}O_S^*,
  S = {2, 3, inf}) of the sextic theta at split primes of norm <= ~100, to a few digits. With it,
  (S6) for EVERY theta in the space becomes a finite linear-algebra test. Only the V-sum of one
  representative set has been published ([BH] Conj. 5.7), and it is incompatible with (S6).
```

# (S6): the sextic theta coefficient at primes

## 0. Verdict

**(S6) is not known, not implied by anything proved, and is contradicted by the only published
numerical data on sextic prime coefficients.** The contradiction is conditional: it rests on
[BH]'s numerics and on one choice of theta function. The full theta space is not covered.

* **Literature [LIT].** For n = 6, Kazhdan–Patterson periodicity and the Hecke relations determine
  `τ(p⁴)` and `τ(p⁵) = 0`. They tie `τ(p)` to `τ(p³)` and leave both `τ(p)` and `τ(p²)` free.
  * The only conjecture in print about `τ(p)` is [BH] Conjecture 5.7. Its shape is:
    `τ(π)²` = (sixth root of unity, no pattern) × (normalized cubic Gauss sum) × (sporadic factor
    `3^l`, `l ∈ {−1, 0}`, times the square of an element of norm 7 or 13).
  * Everything else (CFH, the FG descent, the function-field proof) concerns `τ(p²)` or square
    indices.
* **Against (S6) [INF from BH Conj. 5.7 + exact identities].** For [BH]'s theta, (S6) fails twice:
  * *Modulus:* (S6) forces `|τ(π)/τ(1)|` to be constant. [BH] find `|τ(π)/τ(1)|²` ∈ {1, 7/3, …},
    depending on π.
  * *Infinity type:* (S6) forces `τ(π)² = η(π)²·γ_{±1}(π)²`. Since `γ_1² = −χ(−1)³χ̄(16)·α·γ_2`,
    the ratio `τ(π)²/(cubic Gauss sum)` would carry `η²α^{±1}`. That is a Hecke character of odd
    infinity type, whose values at split primes are not in `Q(ζ_6)`. [BH]'s ratio lies in a finite
    subset of `Q(ζ_6)`.
  * Read the other way, [BH]'s shape says `τ(π) = γ_{±1}(π) × (character of infinity type α^{∓1/2})
    × (unexplained sign)`. This is the same half-integral obstruction as S7 in LEVERAGE_FAMILIES
    (`α^{2/3}` there), and the sign is again the Möbius parity.
* **Experiment [EMP].** Residues of Gauss-sum Dirichlet series were computed by smoothed partial
  sums.
  * *Cubic control:* the method reproduces Patterson's theorem, `τ_3(π)/τ_3(1) = conj γ_2(π)`.
    Over 23 primes of norm ≤ 97, `|r| = 0.995 ± 0.016`, and every phase is within 0.07·π/3.
  * *Sextic:* `τ_6(π)/τ_6(1)` is **not resolved** at norm ≤ 3·10⁵. Two smoothings disagree by a
    median of 0.54 in `r`, against 0.037 in the cubic control. The experiment neither supports nor
    contradicts (S6).
* **Classification:** literature, *not known*; published numerics, *contradicted* for the one theta
  computed (conditional); this experiment, *undetermined at this scale*. Section 4 gives a heuristic
  for why the contradiction should extend to every theta in the space.

## 1. What is proved and conjectured: n = 6

Notation follows [BH] §1 and [CFH] §2. `τ_n(m)` is the m-th coefficient, normalized `τ(1) = 1`, and
`G_j(m,p)` is the normalized Gauss sum built from the j-th power of the n-th power residue symbol.

| object | statement | status | source |
|---|---|---|---|
| definition | `θ^{(n)} = Res_{s=1/2+1/(2n)} E^{(n)}`; `τ_n(m) = N(m)^{1/(2n)} Res A_m` | definition | Kubota; [BH] §1, §2.2 |
| periodicity | `τ_n(m p^n) = N(p)^{1/2} τ_n(m)` | **proved** | KP84 (via [BH], [CFH]) |
| Hecke relations | `τ_n(m p^j) = G_{j+1}(m,p) τ_n(m p^{n−2−j})` for `0 ≤ j ≤ n−2`, `(m,p) = 1`; `τ_n(m p^{n−1}) = 0` | **proved** | KP84, Hoffstein 1993; [CFH] (2.5); [BH] §1 |
| n = 6, `τ(p⁵)` | `= 0` | proved (Hecke) | [BH] §1 |
| n = 6, `τ(p⁴)` | `= conj G_1(1,p)` in the heuristic normalization. For [BH]'s representative set V and `Nπ ≡ 1 mod 4`, `τ(π⁴,V)/τ(1,V) = N(π)^{−1/2} conj g_6(1,π)` | proved (Lemma 5.1) | [BH] Lemma 5.1 |
| n = 6, `τ(p⁴)` at `Nπ ≡ 3 mod 4` | an extra factor `(−1,π)_6/√3` | **conjectured**, checked at `Nπ = 7, 19, 31` | [BH] Conj. 5.2 |
| n = 6, `τ(p)` vs `τ(p³)` | `τ(p) = G_2(1,p) τ(p³)`: one free class | proved relation; value **undetermined** | KP; [BH] §1; [DDHL] count `n/2 − 1 = 2` |
| n = 6, `τ(p²)` | `τ(mp²) = G_3(m,p) τ(mp²)`, a self-relation with a quadratic Gauss sum: one free class | proved relation; value **undetermined** | [BH] (1.3) |
| CFH conjecture | `Σ τ_6(m²)N(m)^{−u} = Σ conj τ_3(m)N(m)^{−u} · Σ G^{(3)}_1(1,d)N(d)^{−u}`. Gives `τ_6(p²) = 2G^{(3)}_1(1,p)` and a divisor-type formula at `m_1²m_2⁴` | **conjectured**. Proved over `F_q(T)` (n odd), and in [CFH] §5 only "almost" for general n | [CFH] Conj. 2.1, §6 |
| CFH, refined | `Nπ ≡ 7 (12)`: `τ(π²,V)/τ(1,V) = ζ_12^{h(π)}·2 g_3(1,ε²,π̄)/(√3 Nπ^{1/2})`, h odd, no pattern. `Nπ ≡ 1 (12)`: `ζ_6^{g(π)}·2 g_3/Nπ^{1/2}` or 0. Inert: `−2` or 0 | **conjectured from numerics** (`Nπ < 8000` and `< 1300`) | [BH] Conj. 5.4–5.6, Lemma 5.3 |
| descent version of CFH | an L² function on the 6-fold cover of SL₂ has square-index coefficients exactly of the CFH form, for products of primes in a positive-density set. Not proved to be the theta function | **proved** for the descent function | [FGd] Thm "maincfh" |
| **n = 6, `τ(p)`** | `(τ(π,V)/τ(1,V))² = ζ_6^{k(π)} g_3(1,ε²,π̄)/Nπ^{1/2} · 3^{l(π)} · c^{m(π)} c'^{n(π)}`, with `k + k(π̄) ≡ 0 (6)`, `l ∈ {−1,0}`, `c, c'` of norm 7 (`Nπ ≡ 1 mod 4`) or 13 (`≡ 3 mod 4`), `m, n ∈ {0, 2}` not both 2. No pattern in k, or in when c appears | **conjectured, purely numerical**: `Nπ < 900` (few digits) and Wellhausen `Nπ < 100` | [BH] Conj. 5.7 |
| `τ(p³)` | `= conj G_2(1,p)·τ(p)`, so it inherits [BH] 5.7 | follows from the Hecke relation | — |

For the representative-set dependence: the theta "function" is really a space. The residues
`ρ(r, η)` are indexed by `η ∈ K_S^*/(K_S^{*6} O_S^*)`, which has `6^{#S} = 216` classes for
`S = {2, 3, ∞}` ([BH] Lemma 2.2). A full representative set V gives one vector, and
`τ(r,V) = Σ_{η∈V} ρ(r,η)`. [BH] found their set V (Wellhausen's `V_2`; residues mod 12 in (5.1))
"gives the cleanest results". Other choices give different `τ(r,V)`.

## 2. n = 4, for comparison [LIT]

* **Suzuki 1983** (as quoted in [DDHL], with its sign correction):
  * biquadrate periodicity;
  * `ψ(m³ν) = 0`;
  * `ψ(m²ν) = conj g_4(ν,m) N(m)^{−3/4} ψ(ν)`, so `τ_4(a²) = conj g̃_4(a)/N(a)^{1/4}` for squarefree a;
  * vanishing unless a quadratic condition holds.
  * In [DDHL]'s words, these "say nothing about `ψ(π)`".
* **Patterson's conjecture**, refined by Eckhardt–Patterson 1992 (Conj. 2.11): `τ_4(π)² = 2 conj G_1(1,π)`
  up to normalization, i.e. `τ_4(π)` is a square root of a Gauss sum.
  * It is open over number fields; [DDHL] (2026 revision) say it "remains wide open".
  * It is proved on average (Bump–Hoffstein).
  * It is proved over `F_q(T)` (Hoffstein 1992; Patterson 2007).
* **Suzuki 1997** proves the Bump–Hoffstein argument relation `τ_1(p)G_1(1,p) = τ_3(p)` over function
  fields. It fixes the argument of `τ_4(p)` up to sign, not its modulus.
* **[FGd]** constructs descent functions consistent with both conjectures, but does not prove that
  they are the theta functions.

## 3. Why (S6) is incompatible with [BH]'s data

Write `r(π) = τ(π,V)/τ(1,V)`. Suppose (S6) held for this theta: `r(π) = κ·η(π)γ_{ε}(π)` with `ε = ±1`,
a constant κ, and a Hecke character `η = ξ·(z/|z|)^ℓ` (ξ of finite order).

1. **Modulus [INF].** `|r(π)| = |κ|` for all π ∉ S. [BH] 5.7 gives `|r(π)|² = 3^{l}·7^{m/2+n/2}`
   (or the norm-13 analogue).
   * Their lists (`Nπ ≡ 1 mod 4`, `Nπ < 900`): norm-7 factor present (and `l = −1`) at 73, 193, 241, 349,
     373, 421, 613, 661, 709, 757, 829, so `|r|² = 7/3`.
   * `l = 0` with no extra factor at 97, 229, 313, 457, 577, 877, so `|r|² = 1`.
   * Hence `|r|` is not constant. Contradiction.
2. **Infinity type [INF; uses exact identities S1–S3].** From `γ_1 = χ̄(4)γ_3γ_2²`, `γ_2³ = −α` and
   `γ_3² = χ(−1)³`:

       γ_1(π)² = −χ_π(−1)³ χ̄_π(16) · α(π) · γ_2(π),    γ_{−1}(π)² = −χ_π(−1)³ χ_π(16) · ᾱ(π) · γ_4(π).

   So (S6) gives `r(π)²/γ_{±2}(π) = −κ²χ(−1)³χ̄(±16)·η(π)²α(π)^{±1}`.
   * `η²α^{±1}` has infinity type `2ℓ ± 1 ≠ 0`. Its value at a split prime is
     `ξ²(π)·(π/|π|)^{2ℓ±1}`, which involves `√p ∉ Q(√−3)`. So it is not in `Q(ζ_6)`, and as π varies
     it equidistributes on the circle (Hecke).
   * [BH]'s `r(π)²/G^{(3)}(π̄)` lies in the finite set `{ζ_6^k 3^l c^m c'^n}` ⊂ `Q(ζ_6)`. Their cubic
     Gauss sum `g_3(1,ε²,π̄)/Nπ^{1/2}` equals `γ_{±2}(π)` up to a sixth root of unity fixed by
     conventions [INF: the additive-character and conjugation bookkeeping was not redone; any such
     change multiplies by a root of unity].
   * If the conventions instead pair `γ_2` with `γ_4`, the ratio picks up a cubic Gauss sum
     `γ_2² = γ_2/γ_4`, which equidistributes as well. Either way: contradiction.
3. **What [BH]'s shape does say.** `τ(π) = ±γ_ε(π)·√(unit-free algebraic)·(character of infinity
   type α^{−ε/2})`.
   * The Galois angle is right: `τ²` has the cubic angle ±1/3, so τ has angle ±1/6 mod 1/2, the
     sextic angle.
   * The infinity type is half-integral, and the square-root sign is unexplained ([BH]: "We have not
     found a pattern in the exponents k(π)").
   * This repeats ALT_PROBES §3(iv) for n = 4: the free sign of a square root of a Gauss sum is
     exactly the Möbius parity.
4. **Even (S6) at primes would not be enough [INF].** LEVERAGE_FAMILIES §5 step 2 needs
   `τ_6(n) = (Hecke)·γ_{−1}(n)` at squarefree composites, i.e. twisted multiplicativity. Non-unique
   Whittaker models remove it (Deligne; KP).
   * Every known or conjectured composite formula for n = 4, 6 has divisor-type sums. Patterson's n = 4
     conjecture gives `|τ_4(pq)|² ∈ {0, 4}`, against `|τ_4(p)|² = 2`.
   * The n = 6 square indices give, by [CFH] and [FGd]:
     `τ_6(p²q²) ∝ 2(G^{(3)}(p)G^{(3)}(q) + G^{(3)}(pq))`, and `τ_6(m_1²) = G^{(3)}(m_1)Σ_{m_1=d_1d_2}(d_2/d_1)_3`.
   * So the composite moduli are not 1.

**Caveats.**
* [BH] Conj. 5.7 is numerical. For `Nπ ≡ 1 mod 4` they rely "on very few digits".
* Their text contains at least one visible slip: "τ(π,V) = 0 for |π| = 37, 313, …" sits in the τ(π²)
  discussion, and 313 also appears in their nonzero τ(π) list.
* Wellhausen 1996 (the `Nπ < 100` data) was not seen.
* The contradiction covers one vector V of a 216-component space.

## 4. Does it extend to every theta in the space? (HEURISTIC)

(S6) asks for *some* vector `v ∈ C^{216}` with `Σ_η v_η ρ(π, η) = η(π)γ(π)`.

Suppose each class residue has the shape that [BH] observe for the V-sum:
`ρ(π,η) = a_η(π)·√(cubic Gauss sum)`, with `a_η(π)` in a fixed finite subset of `Q(ζ_6)`. Two facts
make this plausible:
* Patterson's function-field statement `ρ_0(r,ε,i) ∈ τ(εχ^i)·q^{−k}·Z[μ_n]` [P14 §4];
* the bounded-height pattern in [BH] 5.7.

Under that assumption:
* `Σ_η v_η a_η(π)` takes finitely many values;
* (S6) needs it to equal `ξ(π)·α(π)^{±1/2}·(const)` up to a unit, which takes infinitely many
  values;
* so no v works.

This is the precise sense in which the n = 6 escape route of LEVERAGE_FAMILIES §5 looks closed. The
assumption is an extrapolation and is unverified.

Over `F_q(T)`, theta coefficients are closed-form finite sums (Hoffstein 1992; Patterson 2007, 2014). There:
* Degree-one primes give "τ(εχ^i) times a Jacobi sum".
* Patterson [P14 §4] writes that for more complicated r "the values are irregular" and "a complete
  evaluation does not seem a reasonable expectation".

Function fields have no infinite-order unitary infinity types, so the obstruction in §3.2 has no
function-field test.

## 5. The experiment

**Design.**
* Over `Z[ω]`, use the conventions of `a2/eis.py`: primary `c ≡ 1 mod 3` (this is the representative
  set V′, one generator per ideal prime to 6) and `e(z) = exp(4πi Im z/√3)`.
* Compute `D_n(s,m) = Σ_c G_n(m,c) N(c)^{−s}` for n = 3 (control) and n = 6. Its Kubota pole is at
  `1/2 + 1/n` with residue `∝ τ_n(m,V′) N(m)^{−1/(2n)}` ([CFH] (2.4); [BH] §2.2).
* **Gauss sums at primes:** `a2/s6_gauss.c` computes them once per prime: an O(N p) discrete-log
  table and six additive-character bins give `G_1 … G_5`. Inert primes use `F_{q²}` arithmetic.
  Total 63 s up to norm 3·10⁵.
* **Composite c:** twisted multiplicativity, with exact symbols. For `m = π^j` (j = 1, 2, 4) the
  extra `π^{j+1}c′` terms are included.
* **Smoothing and fit:** the sums `Σ G_n(m,c) w(Nc/Y)` use three weights: `e^{−t}`, `e^{−t²}` and
  Riesz `(1−t)_+³`. Each is fitted to `A Y^{1/2+1/n} + B Y^{1/2−1/n} + C` over 40 values of Y, and
  `r(m) = (A_m/A_1) N(m)^{1/(2n)}`. The weight-to-weight spread is the noise diagnostic.

**Results** (norm ≤ 3·10⁵, 84 677 squarefree c, 23 prime indices of norm ≤ 97; FLOAT):

| quantity | cubic (n = 3), control | sextic (n = 6) |
|---|---|---|
| residue `A_1` (exp1 / exp2 / Riesz) | 0.1633 / 0.1625 / 0.1642 | 0.059 / 0.223 / 0.216 |
| `\|r(π)\|`, Riesz: mean ± sd, or range | 0.995 ± 0.016 (target 1) | 0.11 – 1.05 |
| phase of `r(π)/conj γ_2(π)` | within ±0.07·(π/3) of 1, all 23 primes | — |
| `\|r_exp2 − r_Riesz\|`, median (max) | 0.037 (0.079) | j = 1: 0.54 (1.33); j = 2: 0.82 (1.31) |
| relative fit residual, median | 0.004 | 0.05 |

**Readings.**
* *Cubic.* The cubic run reproduces Patterson's theorem for V′: `τ_3(π,V′)/τ_3(1,V′) = conj γ_2(π)`,
  with no extra root of unity, at about 2 % precision. This validates the pipeline: conventions,
  twisted multiplicativity, p-power terms and fitting.
* *Sextic, m = 1.* The residue is stable between the two long-range weights (0.223 vs 0.216, about 3 %).
  The short exp1 range fails.
* *Sextic, prime indices.* Not stable. The disagreement is of the same size as `|r|` itself, so
  nothing can be said about `|τ_6(π,V′)|` or its phase. The run neither supports nor contradicts (S6),
  or [BH]'s shape, for V′.
* The `X = 10⁵` run gave the same picture (cubic `|r|` 0.86–1.21, sextic inconsistent).
* *Why the sextic is harder.* Signal over noise scales like `X^{1/n}` relative to square-root
  cancellation: `X^{1/6}` against the cubic `X^{1/3}`. The m = π series also has a larger conductor.
  On a naive `X^{1/2}`-noise model, a 5 % determination of `τ_6(π)` needs roughly
  `(0.5/0.05)^6 ≈ 10⁶` times more length. That is why [BH] used the vector functional equation (3.1)
  with Gauss sums to norm 10⁸ on a cluster.
* Conjugate primes give conjugate `r`, by the symmetry `c ↦ c̄`. This is not independent evidence.

## 6. Precise next step

1. **Decisive and finite:** implement [BH] Algorithm 4.1, i.e. the Eckhardt–Patterson vector functional
   equation with the 216×216 matrix `T(r,s)`, for the individual residues `ρ(π,η)` at split π with
   `Nπ ≤ 100`.
   * Test the §4 assumption: does `ρ(π,η)²/γ_cubic(π)` lie in a finite set of `Q(ζ_6)` for every η?
   * Test (S6) directly: with about 250 primes, ask whether some `v` and some η from the finite list
     `ξ·(z/|z|)^ℓ` (ξ mod 12-ish, `|ℓ| ≤ 6`) satisfy `⟨v, ρ(π,·)⟩ = η(π)γ_{±1}(π)`. This is a
     least-squares rank test.
   * Budget: Gauss sums to norm about 10⁶–10⁷, which is cluster scale, not 15-minute scale.
2. **Cheaper partial check:** rerun this pipeline with [BH]'s representative set V and their
   conventions (additive character `e_v` on `K_S` only, their symbol conjugate to CFH's). Then
   reproduce `τ(1,V) ≈ 0.13585` and Lemma 5.1 (`|τ(π⁴,V)/τ(1,V)| = 1`) before trusting any sextic
   prime residue. At norm 3·10⁵ only `τ(1,V)` is reachable.
3. **Route consequence for LEVERAGE_FAMILIES §5.** Treat (S6) as *disfavoured*, not open-neutral. The
   one computed sextic theta has `τ(π)` equal to a sextic Gauss sum times a half-integral infinity
   type with an unpatterned sign. That is the n = 6 version of the Eckhardt–Patterson obstruction at
   n = 4. The 5/6 boundary of the cubic-row family is unsupported.

## Reproduction

```
cd research/exploratory/qrh-2026-10/a2
gcc -O2 -o $SCRATCH/s6_gauss s6_gauss.c -lm                         # build outside the repo
nice -n 10 python3 s6_theta_bias.py 300000 100 $SCRATCH/s6.json $SCRATCH/s6_gauss   # 79 s
```

Output: per prime index π and j ∈ {1, 2, 4}, the estimate `r` for each weight, the fit residuals,
`G_1 … G_5(π)`, `α(π)`, and the sextic symbols of −1, 2, 3, 4 at π. The cubic table above comes
from `n3_rows`, and the sextic table from `n6_rows`.

```text
Status: PROPOSED (Sections 1, 2.1-2.2 and Lemma A are elementary and proved here, not reviewed)
  + HEURISTIC (Section 3: the structural-pipeline model and its boundary formula; Section 5: a
  conjectural route) + EMPIRICAL (exact Jacobi-sum checks, floating Gauss-sum checks, integer counts).
  Nothing here proves a zero-free region. RH remains unproved.
Scope: whether a Kummer-type family with leverage c < 5/6 (more principal rows relative to its size)
  can carry the Oct 5 structural proof (Poisson in the row, Moebius absorption, theta reflection,
  row-blind large sieve) at rho = 1, which would give a boundary (1 + c)/2 < 11/12.
Exact sources or dependencies:
  [OAI5] OpenAI "Oct 5" manuscript, external and unreviewed: git object pr908 = 31c706bb...cbb6,
    standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
    The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex, sha256 d9a8f15a...8750d4d.
    Read: Sections 1-3 (lines 52-560), Lemma lem:arithmetic (823-862), Lemma lem:poisson (864-932),
    App. app:gauss-identities (2687-2872).
  [FG15] Friedberg-Ginzburg, "Metaplectic theta functions and global integrals", JNT 146 (2015)
    134-149, arXiv:1403.3929 (e-print gz sha256 ff08a2ff...712bd2712b). Read: Sections 2 and 5
    (uniqueness for GL(3) covers, quartic coefficients).
  [DDHL] David-Dunn-Hamieh-Lin, arXiv:2306.11875 (e-print gz sha256 59f5e152...b0de96). Read:
    Section 1 (lines 360-385) and the theta section (lines 1075-1145): Suzuki, Eckhardt-Patterson,
    count of undetermined coefficients, Deligne/Kazhdan-Patterson non-uniqueness on GL(2).
  [KP] Kazhdan-Patterson, Publ. IHES 59 (1984), Cor. I.3.6: cited second-hand through FG15.
  [IR] Ireland-Rosen, Ch. 8-9 (Gauss/Jacobi sums, Prop. 9.9.4); Weil, Trans. AMS 73 (1952)
    (Jacobi sums as Hecke characters); Hasse-Davenport. Classical, not re-read; the cases used
    are checked exactly below.
  Repository: reviews/OCT5_R3_THETA_REFLECTION.md (the exponent B_{p,j} = chi_p^{-j-2});
    RUNG_STRENGTH.md (leverage law, rho = 1 wall); ALT_PROBES.md (parity rule, theta census);
    A2_LITERATURE.md (cubic GL(3) theta vanishing; cubic large sieve sharp, [DR]).
  a2/eis.py (sha256 87ca11d9...2798e65), read and imported, not modified.
What was actually run (Python 3.13, single process, the machine is shared):
  python3 a2/leverage_gauss_checks.py 400 1500 OUT.json   (29 s)
    77 primary primes of Q(omega) (3 inert), 186 squarefree composites; 78 primes of Q(i) (4 inert).
  python3 a2/leverage_budget.py 1000000 OUT.json          (17 s)
  Outputs went to the session scratchpad (sha256 4180e892...c5d3 and bc0c4032...c8e6); rerun to
  reproduce. EXACT = integer arithmetic in Z[omega] or Z[i]; FLOAT = double precision, not directed.
Smallest remaining gap: within this architecture, c < 5/6 needs a GL(2) metaplectic theta (on an
  n-fold cover, n in {4, 6, 10}) whose Fourier coefficient at every prime is a Hecke character times
  ONE Gauss sum of order n, with the right sign. Those coefficients are not locally determined
  (non-unique Whittaker models). For n = 4 the Eckhardt-Patterson conjecture predicts a square
  root of a Gauss sum instead, which is incompatible. No such statement is known for n = 6 or 10.
```

# Leverage families: is c = 5/6 forced?

The 11/12 and 7/8 statements are claims of an external, unreviewed manuscript. "Imported" below
means taken from [OAI5] or from repository notes without independent proof.

## 0. Verdict

**On the HEURISTIC model of §3 and every automorphic input currently known, no examined family beats c = 5/6.**
No family examined has c < 5/6 together with all three ingredients: absorption, reflection and a
quadratic-type large sieve. The reasons, in order of strength:

1. **Leverage is the order of the row symbol** (Section 2, PROPOSED). For a one-variable Kummer
   family, c = 1 − 1/m, where m is the order of `u ↦ χ_n(u)`. The base field changes nothing.
   Product, quotient and norm families never beat the leverage of their longest Poisson variable,
   because each Poisson variable must have about D rows (Lemma A).
2. **Absorption fixes m by the angle of the theta coefficient** (Sections 1 and 3, the angle
   condition PROPOSED). With one Poisson average, μ is absorbed only if the theta coefficient at p
   has Galois angle `1/2 ∓ e/m`, and the sign comes out right.
   * The only GL(2) theta with explicit nonzero prime coefficients is Patterson's cubic theta
     (angle ±1/3). That forces m = 6.
3. **Higher-rank thetas pay a degree tax** (Section 3, HEURISTIC model). A GL(r) reflection needs
   `ρ ≥ max(1, 2 − 2/r)`, so the boundary is `σ = 1/2 + c·max(1/2, 1 − 1/r)`.
   * The explicit quartic GL(3) theta of [FG15] absorbs μ for quartic rows (c = 3/4), but r = 3
     gives σ = 1.
4. **m = 2 cannot absorb μ at all.** The quadratic Poisson Gauss sum is explicit, so μ would itself
   have to be an automorphic coefficient. That is the original problem (circular).

New structural point (Section 3.2, HEURISTIC beyond the cubic case): for a GL(2) theta reflection
after one Poisson average, **absorption and a quadratic post-reflection twist are the same
congruence**. Ingredients (A) and (LS) are therefore not independent. The binding constraint is the
existence of the theta function.

The only escape found inside this architecture (on the HEURISTIC model of §3) is a coefficient
theorem for n-fold covers of GL(2) with
n ∈ {6, 4, 10}, which would give 5/6, 7/8 and 9/10 respectively (Section 5). It is exactly the
range where Deligne and Kazhdan–Patterson show that Whittaker models are not unique.

## 1. The absorption identity, made precise

### 1.1 The prime case

Fix a primary prime `p ∤ 6` of `K = Q(ω)`, `q = N p`. Write `χ = χ_p = (·/p)_6`, `ρ = χ³`
(quadratic) and `ψ = χ²` (cubic). Then

    χ = ρ · ψ̄        (χ³·χ^{-2} = χ),   and   χρ = χ⁴ = ψ̄.

So the factorization "χ₆ = χ₂·χ₃^{-1}" is correct with `χ₃ := χ₆²`. Use the normalized Gauss sums
`γ_j(p) = q^{-1/2} Σ_x χ(x)^j e(x/p)` of [OAI5] (`γ_1` sextic, `γ_2` cubic, `γ_3` quadratic).

The absorption identity uses three standard facts.

* **Hasse–Davenport duplication** `g(χ)g(χρ) = χ̄(4) g(χ²) g(ρ)`, i.e. `g(χ) g(ψ̄) = χ̄(4) g(ψ) g(ρ)`.
  [OAI5] proves it as `χ(4)J(χ,χ) = J(χ,χ³)`, by counting `#{x : 4x(1−x) = y} = 1 + ρ(1−y)`.
  **EXACT check S2:** 77/77 primes, equality in `Z[ω]`.
* **Stickelberger for the cubic character.** `g(ψ)³ = q·J(ψ,ψ)` and `J(ψ,ψ) = −p` for primary `p`
  (`p ≡ 1 mod 3`). [OAI5] proves the second via `J ≡ −1 mod 3`. Hence `γ_2³ = −α`, with `α = p/|p|`.
  **EXACT check S1:** `J(ψ,ψ) = −p` for 77/77 primes, inert primes `−5, −11, −17` included.
* **Inversion.** `g(ψ)g(ψ̄) = ψ(−1)q = q`, so `γ_2γ_4 = 1`.

Combining them:

    γ_1 = χ̄(4) γ_3 γ_2²  =  χ̄(4) γ_3 · (γ_2³) · γ_4  =  −α χ̄(4) γ_3 conj(γ_2),

so

    μ(p) γ_1(p) = α(p) · G(p) · conj(γ_2(p)),        G(p) = χ̄_p(4) γ_3(p)  (ray class, Gauss's sign).

Conjugating and using `γ_1γ_{−1} = χ(−1)` gives eq:convert2:
`μ(p)γ_{−1}(p) = χ_p(−1) G(p)^{-1} conj(α(p)) γ_2(p)`.

In words: **μ times a sextic Gauss sum is a Hecke character (α) times a ray-class factor (G) times
a cubic Gauss sum.** The cubic Gauss sum is Patterson's theta coefficient (R3 item 3).

### 1.2 Where the sign comes from, and why it is intrinsic

The minus sign per prime is exactly the sign in `J(ψ,ψ) = −p`. Everything else in the chain carries
no sign:

* the duplication constant `χ̄(4)`;
* the quadratic Gauss sum `γ_3`, which Gauss's evaluation makes a ray-class function;
* the inversion `γ_2γ_4 = 1`.

In Weil's normalization the Jacobi sum `−J` is the Hecke character (here `p ↦ p`). So **each Jacobi
sum surviving in the reduction contributes one factor −1 per prime, i.e. one μ**.

The sign is not a convention. The function `p ↦ μ(p)γ_1(p)/(G(p)conj γ_2(p))` equals `α(p)`, a
Hecke character. The same function without μ equals `−α(p)`, which is not one. No Hecke character
equals −1 at all but finitely many primes:
* a finite-order Hecke character is 1 on the primes splitting completely in its class field, a set
  of positive density;
* a unitary Hecke character of infinite order has equidistributed values (Hecke).

At squarefree `n` the identity extends through twisted multiplicativity
`γ_j(ab) = γ_j(a)γ_j(b)χ_a(b)^jχ_b(a)^j`. The reciprocity factors go into `G` and `R`
(eq:recip, eq:quotient), and the signs multiply to `μ(n)`.

**FLOAT checks:**
* **S3:** `γ_2³ = μα` and `γ_1γ_2 = μαG` at 77 primes, deviation ≤ 4.7e-15.
* **S4:** eq:convert2 at 77 primes and **186 squarefree composites** with two or three prime
  factors and `N n ≤ 1500`, deviation ≤ 5.5e-15.
* **Control:** dropping μ makes every tested identity fail by exactly 2.

### 1.3 The general rule, with what is proved and what is heuristic

Let the row symbol be `χ^e`, of order `m`, so Poisson in the row produces `γ(χ^e)`. Suppose the
absorbing coefficient is `τ(p) = (Hecke)·γ(χ'^a)`, with `χ'` of order `n`.

* **Angle condition (necessary; PROPOSED, elementary).** First clear the normalizations, using
  `α(p)|p| = p`. The identity becomes one between unnormalized Gauss sums, an *algebraic* Hecke
  character (values in `K(ζ_N)`, such as `p ↦ p`) and an integral power of `q`. Every identity used
  here has this form.

  Now apply the automorphism `ζ_ℓ ↦ ζ_ℓ^c` of `K(ζ_N, ζ_ℓ)/K(ζ_N)`, where `ℓ` is the rational prime
  under `p`. Each `g(χ^b)` gets multiplied by `χ^{-b}(c)`, while the algebraic Hecke values and `q`
  are fixed. So `μ(p)g(χ^e) = Hecke · g(ρ)^s · g(χ'^a) · q^t` with `s ∈ {0, 1}` forces

      e/m − a/n ≡ s/2 (mod 1)        (angles of the Poisson sum and of τ differ by 0 or 1/2).

  Example: `g_1 = −(p/q) χ̄(4) g_3 g_4`, from §1.1, has `1/6 − 4/6 ≡ 1/2` with `s = 1`.

* **Sign (the Möbius parity).** Given the angle condition, the quotient `γ_P/τ` is `±(Hecke)×(1 or
  γ(ρ))`. The sign is −1, so μ is absorbed, exactly when the reduction leaves an odd number of
  Jacobi sums. This is the parity rule of [ALT_PROBES.md](ALT_PROBES.md) §2, rephrased.

| Poisson × coefficient | reduction | Jacobi sums | μ absorbed? | check |
|---|---|---|---|---|
| sextic `γ_1` vs cubic `conj γ_2` | `γ_1γ_2 = −αχ̄(4)γ_3` | one, `J(ψ,ψ) = −p` | **yes** (Oct 5) | S1–S4 |
| cubic `γ_2` vs cubic `γ_4 = conj γ_2` | `γ_2γ_4 = 1` | none | no | S7: `μγ_2/γ_2 = −1` |
| cubic `γ_2` vs cubic `γ_2` (other pairing) | `μγ_2/γ_4 = −γ_2²`, cube `= −α²` | — | no: infinity type would be `α^{2/3}` | S7 (dev 6e-15) |
| cubic `γ_2` vs **sextic** `γ_{−1}` | `μγ_2 = χ(−1)αGγ_{−1}` | one | yes, but needs a sextic-coefficient theta | S6 |
| cubic² (two Poisson averages) vs cubic `γ_4` | `μγ_2² = αγ_4` | one | **yes** (product family, §2.2) | S5 |
| quartic `γ(χ_4)` vs `conj γ(χ_4)` over `Q(i)` | `γ(χ)² = J(χ,χ)γ(ρ)/\|π\|`, `J = −χ(−1)π` | one | **yes** (needs a quartic-coefficient theta) | Q1–Q3 |
| quadratic `γ(ρ)` vs anything Hecke | `γ(ρ)` is explicit | none | no; μ is left alone | Q4 |

The quartic line is EXACT for 78/78 primes of `Q(i)`, inert `−3, −7, −11, −19` included:
`J(χ_π, χ_π) = −χ_π(−1)π` ([IR] Prop. 9.9.4). It is FLOAT for
`μ γ(χ) = χ(−1) α γ(ρ) conj γ(χ)`, with deviation ≤ 3.3e-15.

## 2. Leverage is the order of the row symbol

### 2.1 One-variable families (PROPOSED, elementary)

Let `F ⊇ μ_m`, and take rows `u ∈ O_F` in a ball if `F` is imaginary quadratic, or in a box with
`≍ H` lattice points if the unit group is infinite. The symbol `χ_n(u) = (u/n)_m` is principal in
`n` iff `u ∈ F^{×m}`, which gives `≍ H^{1/m}` principal rows; each of the finitely many classes
`ε F^{×m}` (ε a unit, `ε ∉ F^{×m}`) is a single nonprincipal member, so each member still has
`≍ H^{1/m}` rows. Hence

    c = 1 − 1/m,    and the leverage law (RUNG_STRENGTH §1–2) gives σ = 1/2 + cρ/2.

The base field enters only through which symbols and thetas exist. The same holds for:
* restricting rows to a sublattice (e.g. `u ∈ Z` inside `Z[ω]`, where `u = w⁶` or
  `−27w⁶ = ((1+2ω)w)⁶` are principal);
* restricting them to a multiplicative semigroup (smooth numbers, S-units).

In each case the principal count is the m-th root of the row count, up to constants. If rows are
`u = w^k`, the symbol in `w` has order `m/(m,k)`, and that order is what counts.

### 2.2 Several Poisson variables (Lemma A)

Take rows `(u_1, …, u_k)`, `N u_i ≤ H_i`, with character `∏ χ_n(u_i)^{e_i}`, all `e_i ≢ 0`.

**Lemma A (PROPOSED; the threshold is HEURISTIC).**
* *Threshold.* After Poisson in all `k` variables (moduli of norm `D²`), the dual rows number
  `∏ D²/H_i`. The rows term of any row-blind large sieve then needs `∏ H_i ≥ D^k`, the multivariable
  form of RUNG_STRENGTH §3(b). In particular the longest variable `u_j` has `H_j ≥ D`.
* *Counting.* With the other variables fixed, the principal condition fixes `u_j` modulo
  `m_j`-th powers, where `m_j = m/(m, e_j)`. Hence `P ≤ (∏_{i≠j} H_i) · H_j^{1/m_j} · D^ε`.
* *Conclusion.* `F/P ≥ H_j^{1−1/m_j} ≥ D^{1−1/m_j}`, so σ ≥ `1 − 1/(2m_j)` for the longest
  variable's symbol order. Several variables can only match a one-variable family, never beat it.

Concrete cases, with integer counts over `Z` used as a proxy for the lattice; only exponents are
compared:

| family | principal rows P | P vs family size F | absorption | σ at the structural threshold |
|---|---|---|---|---|
| single cubic `u ≤ H²` | `H^{2/3}` | `F^{1/3}` (c = 2/3) | no (§1.3) | — |
| product `u_1u_2`, cubic each | `H^{2/3+o(1)}`: 152 844 at `H = 10⁶`; `log P/log F` falls 0.455 → 0.432 → 1/3 | `F^{1/3}` (c = 2/3) | **yes**: `μγ_2² = αγ_4` (S5) | `F ≥ D²` gives σ ≥ **7/6** |
| quotient `u_1/u_2`, cubic or sextic | `≍ H`: `P/H` = 1.72 (cubic), 1.04 (sextic) at `H = 10⁶` | `F^{1/2}` (c = 1/2) | no: `μγγ̄ = μχ(−1)`, the Gauss sums cancel | σ ≥ **1** |
| `χ(u)χ²(w)`, sextic × cubic | `≈ H_u^{1/6} H_w^{1/3}` (by hand; dominated by `u` sixth powers, `w` cubes) | `F^{1/4}` at equal lengths (c = 3/4) | fully absorbed into GL(1): `μγ_1γ_2 = αG` | `log_D(F/P) = 5a/6 + 2b/3` with `a + b ≥ 2`, so σ ≥ **7/6** (5/4 at equal lengths) |
| norm family `u ∈ O_L`, `χ(N_{L/F}u)`, `[L:F] = d` | `count^{1/m}` | c = 1 − 1/m | Hasse–Davenport lifting gives `g^d`, e.g. `d = 2, m = 3` absorbs | count ≥ `D^d` gives σ ≥ `(1 + d(1−1/m))/2` ≥ 1 for d ≥ 2 |

The product and two-exponent families show that μ **can** be absorbed with lower-order symbols, by
pairing two Poisson Gauss sums. The price is a second Poisson variable of length ≥ D, which destroys
the leverage.

In the product family there is a second failure. Its post-reflection twist is cubic: `j = 2` in R3's
formula `B_{p,j} = χ_p^{−j−2}`, giving `χ²`. The cubic large sieve is not optimal for Gauss-sum
coefficients ([DR], A2_LITERATURE §4).

### 2.3 Twisted rows

Rows `(u, k)` with angular characters `α^k`, Größencharacters, Dirichlet characters to a composite
modulus, or `N(n)^{it}` add rows without adding principal copies. An additive parametrization of
characters has trivial kernel, so c increases.

Weighting rows by an amplifier `|Σ_ℓ x_ℓ χ_ℓ(u)|²` is equivalent to lengthening the column to `DL`.
It costs exactly what it gains. Only the multiplicative (Kummer) kernel `F^{×m}` produces leverage.

## 3. The structural boundary for one-variable families (HEURISTIC model)

### 3.1 Bookkeeping

Model the pipeline after [OAI5] Steps 3–4:

* Poisson in `u` (`H ≥ D`) gives a dual with `𝓗 = D²/H` rows and columns of norm `X ≍ D`. The
  target is `Σ_{h ≤ 𝓗} |B_h|² ≲ D²`, i.e. `E(𝓗, X) ≲ X` (eq:intro-dual-ms).
* Absorption turns the dual coefficients into theta coefficients.
* A GL(r) reflection of a twist of conductor `≍ N(h)` has dual length `N(h)^r/X`.
* An optimal large sieve gives `Σ_h |T_h|² ≲ 𝓗 + 𝓗^r/X`.

`≤ X` needs `𝓗 ≤ X` and `𝓗^r ≤ X²`, i.e.

    ρ ≥ max(1, 2 − 2/r),      σ(m, r) = 1/2 + (1 − 1/m)·max(1/2, 1 − 1/r).

For `(m, r) = (6, 2)` this is 11/12 and reproduces eq:intro-completed-ms
(`𝓗 + 𝓗²/X`). The model ignores the cube-removal iteration (R2 scope), which in [OAI5] also needs
`ρ ≥ 1`.

### 3.2 Absorption ⟺ quadratic post-reflection (GL(2), one Poisson average)

R3 verified the local exponent `B_{p,j} = χ_p^{−j−2}` exactly. Here `j` is the twist exponent on
`ᾱγ_2` and `2` is the Kubota multiplier, which has the same angle as the theta coefficient. Write
the Poisson character as `χ^e`; then the dual twist is `χ^{−e}`, and absorption needs (§1.3, in
units of 1/6)

    e − 2 ≡ 3 (mod 6)        and the post-reflection character is   χ^{e−2}.

The two conditions are the same congruence. **μ is absorbed iff the post-reflection family is
quadratic.**
* The cubic twist (angle sum 0) is the case "no μ". R3 records that `j = 4` gives Ramanujan sums
  and no character.
* For other n the statement relies on the expected analogue of R3's local computation: the
  multiplier and coefficient angles agree. This is HEURISTIC.
* Consequence: ingredient (LS) never fails separately for GL(2) thetas with one Poisson average.
  The only question is whether the theta exists.

### 3.3 Which thetas have explicit, nonzero prime coefficients

| cover | prime coefficient | source |
|---|---|---|
| n = 2, GL(2) (classical θ) | `τ(p) = 0` | classical |
| **n = 3, GL(2)** | **`τ(p)` = cubic Gauss sum** | Patterson; [DR] (5.7); R3 |
| n = 3, GL(3) | `τ(p,1) = 0`; support on cubes | Proskurin, Bump–Hoffstein, quoted in [FG15] §5 |
| **n = 4, GL(3)** (c odd) | **`τ(p,1) = \|p\|^{−1/2} ḡ_4(p)`**, `τ(p^{4k+1},1) = \|p\|^{k−1/2}ḡ(p)` | [FG15] §5; unique model by [KP] Cor. I.3.6 |
| n = 4, GL(2) | undetermined. Suzuki gives `τ(a²)`, biquadrate periodicity, vanishing at cubes, and a quadratic support condition, but "nothing about `ψ(π)`". The Eckhardt–Patterson conjecture: `τ(π)² N(π)^{1/4} ∝ ḡ_4(π)`, open, true on average (Bump–Hoffstein) | [DDHL] §1 and theta section |
| n ≥ 4, GL(2) | `n/2 − 1` (n even) or `(n−1)/2 − 1` (n odd) undetermined classes per prime; non-unique Whittaker models (Deligne, [KP]) | [DDHL] |
| n > 4, GL(3) | model not unique; coefficients unknown | [FG15] §5 |

### 3.4 The enumeration

With one Gauss sum of order n as coefficient (angle ±1/n), §1.3 forces the row order
`m(n) = denominator of 1/2 − 1/n`:
* `m = 2n` for n odd;
* `m = n/2` for `n ≡ 2 (mod 4)`;
* `m = n` for `n ≡ 0 (mod 4)`.

`a2/leverage_budget.py` (EXACT, fractions) gives:

| n | m(n) | c | σ at r = 2 | σ at r = n − 1 | coefficient known? |
|---|---|---|---|---|---|
| 3 | 6 | 5/6 | **11/12** | (same) | yes (Patterson) |
| 4 | 4 | 3/4 | 7/8 | 1 | GL(2): no (EP predicts a square root); GL(3): yes |
| 5 | 10 | 9/10 | 19/20 | 47/40 | no |
| 6 | 3 | 2/3 | **5/6** | 31/30 | no |
| 8 | 8 | 7/8 | 15/16 | 5/4 | no |
| 10 | 5 | 4/5 | **9/10** | 109/90 | no |
| 12 | 12 | 11/12 | 23/24 | 4/3 | no |

Every `(m, r)` with `m ≤ 12, r ≤ 6` and `σ(m, r) < 11/12` has either `m = 2` (any `r ≤ 5`) or
`m ∈ {3, 4, 5}` with `r ≤ 2`. Each case is excluded on known inputs:

* **m = 2.** The Poisson Gauss sum is explicit, so the absorption identity would read
  `μ(n)ξ(n) = (Hecke)·τ(n)`. Then `μ` times a ray-class character would be the automorphic
  coefficient, with a reflection. That is a functional equation for `1/L(s, ξ)`: the original
  problem. Circular.
* **r = 1.** The absorbing coefficient would be a Hecke character. The angle condition then forces
  `e/m ∈ {0, 1/2}`, i.e. m ≤ 2: circular again.
* **r = 2, m ∈ {3, 4, 5}.** This needs an n-fold GL(2) theta with n = 6, 4, 10 whose prime
  coefficient is (Hecke)×(one Gauss sum of order n). These coefficients are undetermined.
  * For n = 4 the Eckhardt–Patterson shape (angle `3/8 mod 1/2`) is incompatible. It would pair
    only with an octic row symbol (c = 7/8, σ ≥ 15/16), and the unknown sign of `τ_4(π)` is
    exactly the unknown Möbius parity (ALT_PROBES §3(iv)).

## 4. Classification of the requested families

Notation:
* (A) absorption: `μ·(Poisson Gauss sum) = Hecke × explicit × automorphic coefficient`;
* (R) a known reflection of the needed degree;
* (LS) an optimal large sieve for the post-reflection family;
* σ is the boundary if all three held at the structural threshold.

| family | m | c | σ if all held | (A) | (R) | (LS) | first failing ingredient | label |
|---|---|---|---|---|---|---|---|---|
| quadratic, rows in `Z` | 2 | 1/2 | 3/4 | **no**: `γ(ρ_n)` explicit; dual is the same Möbius family (Poisson is an involution) | none for `1/L` | Heath-Brown, but square rows give `H^{1/2}\|A_1\|²` | **A** (circular) | PROPOSED |
| quadratic, rows in `Z[i]` | 2 | 1/2 | 3/4 | **no**, same; the quartic theta does not help (Q4) | — | Onodera / Goldmakher–Louvel | **A** | PROPOSED |
| cubic over `Q(ω)` | 3 | 2/3 | 5/6 | **no** with the cubic theta (S7). `μγ_2 = χ(−1)αGγ_{−1}` needs a sextic-coefficient theta (S6) | 6-fold GL(2): automorphy known, coefficients unknown; 6-fold GL(5): σ = 31/30 | quadratic (by §3.2) if A held | **A** (no known object) | PROPOSED + HEURISTIC |
| quartic over `Q(i)` | 4 | 3/4 | 7/8 (r = 2) | formal identity **yes** (Q1–Q3), with `τ(p) ∝ conj γ_4(p)`. GL(2) quartic theta: undetermined; under EP the angle is wrong. GL(3) quartic theta: matches [FG15] | GL(3) degree tax: `ρ ≥ 4/3`, σ = **1** | presumably quadratic; untested | **R** (GL(3)) / **A** (GL(2)) | PROPOSED + HEURISTIC |
| quintic over `Q(ζ_5)` | 5 | 4/5 | 9/10 | needs a 10-fold GL(2) single-Gauss-sum coefficient | 10-fold GL(9): σ > 1 | — | **A** | HEURISTIC |
| **sextic over `Q(ω)` (Oct 5)** | 6 | 5/6 | **11/12** | **yes**: eq:convert2 (S4, incl. composites) | **yes**: cubic GL(2) theta, R3 | **yes**: quadratic, Goldmakher–Louvel (statement-level) | — | IMPORTED; parts reviewed (R1–R3) |
| order 12 over `Q(ζ_12)` | 12 | 11/12 | ≥ 23/24 | needs an order-12 coefficient (12-fold covers) | — | — | **c too large** | HEURISTIC |
| subsymbols over `Q(ζ_12)` (orders 2, 3, 4, 6) | — | — | — | reduce to the rows above (c depends only on m) | — | — | as above | PROPOSED |
| product `u_1u_2`, cubic | 3 + 3 | 2/3 per size | ≥ 7/6 at threshold | **yes**, S5 | GL(2) cubic theta | **no**: post-reflection cubic, `j = 2` | **threshold** (Lemma A) + **LS** | PROPOSED + HEURISTIC |
| quotient `u_1/u_2` | any | 1/2 per size | ≥ 1 at threshold | **no**: Gauss sums cancel | — | — | **A** + threshold | PROPOSED |
| sextic × cubic, `χ(u)χ²(w)` | 6, 3 | 3/4 per size | ≥ 7/6 | **yes**, into GL(1) | GL(1) | — | **threshold** | PROPOSED |
| norm family, `[L:F] = d ≥ 2` | m | 1 − 1/m | ≥ 1 | possible via `g^d` | GL(2) | — | **threshold** (`count ≥ D^d`) | PROPOSED |
| angular / Größen / Dirichlet-twisted rows | — | > c of base | > base | unchanged | — | — | **leverage** | PROPOSED |

## 5. The conjectural route, spelled out (HEURISTIC / OPEN)

The closest route to c < 5/6 is the cubic family with a sextic GL(2) theta. Every link except the
first is either proved here or an analogue of a reviewed Oct 5 step.

**(S6) Coefficient hypothesis, not in the literature known to us.** Some theta function on a 6-fold
cover of GL(2) over `Q(ω)` has, at every prime `p ∤ S`, Fourier coefficient
`τ_6(p) = η(p)·γ_{∓1}(p)`, with η a Hecke character. The relative sign must be exactly right at
every prime.
* The Hecke relation `τ(p) = G_2^{(6)}(1,p) τ(p³)` (CFH (2.5) via ALT_PROBES §3) makes this
  equivalent to a statement about `τ(p³)`.
* The Chinta–Friedberg–Hoffstein conjecture concerns only `τ(p²)`. [DDHL] counts two undetermined
  classes per prime for n = 6.

Lemma chain, assuming (S6):
1. **Poisson** in `u` for `A_u(D) = Σ μ(n)ν(n)(u/n)_3 W` with `H = D^{1+θ}`. This is
   [OAI5] Lemma lem:poisson with a cubic character; Gauss sums `γ_{2}` and `γ_{4}`.
2. **Absorption**: `μ(n)γ_2(n) = χ_n(−1)α(n)G(n)γ_{−1}(n)`. Proved at primes; numerically at
   composites (S6, dev 5.4e-15). Under (S6) it is a Hecke twist of `τ_6`.
3. **Reflection** of the sextic theta twisted by the cubic `χ_n(h)²`. The post-reflection twist is
   quadratic by the §3.2 congruence (`e − a ≡ 3`). HEURISTIC: needs the 6-fold analogue of R3's
   local computation and of [DR] §5.
4. **Quadratic large sieve** ([OAI5] lem:quadratic, Goldmakher–Louvel).
5. **Completion and removal** over `n b⁶`, the analogue of Step 5 and of the R2 iteration. This
   uses 6-fold periodicity and needs `ρ ≥ 1` as in [OAI5].

Conclusion: `Σ_{N u ≤ D^{1+θ}} |A_u|² ≲ D^{2+θ+ε}`; extraction from `H^{1/3}` cube rows gives
**σ = 5/6**. The analogous chains give **7/8** (m = 4: a 4-fold GL(2) theta with a single
quartic-Gauss-sum coefficient, against the EP shape) and **9/10** (m = 5: a 10-fold GL(2) theta).

**Smallest statement whose failure kills the route:** (S6) itself, including its sign. If
`τ_6(p) = ±η(p)γ(p)` with a sign that is not a Hecke character, absorption fails at those primes.

> **Follow-up on (S6)** ([SEXTIC_THETA_S6.md](SEXTIC_THETA_S6.md)).
> * (S6) is not known, and no proved result implies it.
> * Bröker–Hoffstein's numerical Conj. 5.7 (arXiv:1312.0568) for one sextic theta *contradicts*
>   (S6) for that theta. There `|τ(π)/τ(1)|²` varies, and their shape needs a half-integral
>   infinity type.
> * The theta space has 216 classes, so the general case is open. Settling it for every theta is a
>   finite rank computation at small primes, using Bröker–Hoffstein's algorithm, but it needs
>   cluster-scale Gauss sums.
> * A bias experiment at norm `≤ 3·10⁵` reproduced the cubic control (Patterson's theorem) but was
>   inconclusive for the sextic case.

## 6. Consequences

* Within the Oct 5 architecture, the leverage axis is closed for the families examined, with current
  knowledge. 11/12 is the best value among the families examined here (Kummer, products, quotients,
  norm forms, twisted rows), on the HEURISTIC model of §3.
* The two remaining axes are:
  * `ρ < 1`, i.e. sub-diagonal mean squares, which need a Möbius-specific on-average GRH
    (RUNG_STRENGTH §4);
  * a new coefficient theorem for n-fold covers of GL(2), n ∈ {4, 6, 10}, the non-unique Whittaker
    range.
* The obstruction matches the repository's family-transfer warning (OPEN_CUTS §5). The leverage is
  set by the Kummer kernel `F^{×m}`. The Möbius parity can be paid for only by a theta coefficient
  of matching angle, and the only explicit one in rank 2 has angle 1/3.

## 7. Not done

* No proof that a GL(r) reflection *must* cost `N(h)^r/X`. A degree-lowering identity for the
  quartic GL(3) theta (for example a Shimura-type correspondence for `τ(n,1)`) would reopen the
  m = 4 line; none is known to us. [FG15] relates the quartic GL(3) theta only to half-integral-weight
  forms through a Rankin–Selberg integral.
* The quartic post-reflection character was not computed.
* Brylinski–Deligne covers were not examined beyond the remark that rank-one thetas see only the
  effective order `n_α` (A2_LITERATURE §3 [INF]).
* [KP], Weil 1952 and Hasse–Davenport were not re-read. The specific identities used were checked
  exactly or numerically instead.
* [DR] was used through R3 and A2_LITERATURE only.

## Reproduction

```
cd research/exploratory/qrh-2026-10/a2
python3 leverage_gauss_checks.py 400 1500 /path/out_gauss.json   # ~30 s; S1-S7, Q1-Q4, controls
python3 leverage_budget.py 1000000 /path/out_budget.json         # ~17 s; tables of Sections 2.2, 3.4
```

| check | content | result |
|---|---|---|
| S1 (EXACT) | `J(χ²,χ²) = −p` | 77/77 |
| S2 (EXACT) | `χ(4)J(χ,χ) = J(χ,χ³)` | 77/77 |
| S3 | `γ_2³ = μα`; `γ_1γ_2 = μαG` | 4.7e-15; 2.9e-15 |
| S4 | eq:convert2, primes / composites | 2.0e-15 / 5.5e-15 |
| S5 | `μγ_2² = αγ_4`, primes / composites | 2.7e-15 / 6.8e-15 |
| S6 | `μγ_2 = χ(−1)αGγ_{−1}`, primes / composites | 2.0e-15 / 5.4e-15 |
| S7 | `(μγ_2/γ_4)³ = −α²`; `μγ_2/γ_2 = −1` | 6.0e-15; 5e-17 |
| Q1 (EXACT) | `J(χ_π,χ_π) = −χ_π(−1)π` over `Z[i]` | 78/78 |
| Q2, Q3 | `μγ(χ)² = χ(−1)αγ(ρ)`; `μγ(χ) = χ(−1)αγ(ρ) conj γ(χ)` | 3.3e-15; 2.2e-15 |
| controls | the same identities without μ | min deviation 2.000 (all three) |
| counts | product / quotient principal rows, `H = 10³…10⁶` | Section 2.2 table |

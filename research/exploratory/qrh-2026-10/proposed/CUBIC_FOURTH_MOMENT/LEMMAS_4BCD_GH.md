# PROPOSED proofs of the cubic Lemmas 4.C, 4.D, 4.B, 4.H (with Corollary 4.H) and 4.G of SKETCH Sec. 4

```text
Status:      PROPOSED (exploratory, unreviewed). Not integrated. RH is not addressed: these are finite
             arithmetic lemmas inside a CONDITIONAL fourth-moment scheme (SKETCH.md, Theorem C4,
             conditional on (H-A), (H-B)). Verdicts: 4.B, 4.C, 4.D proved here; 4.H proved here
             (with two precision fixes); Corollary 4.H proved here except the value of e_p, which
             is read off a definition in the manuscript's second transform (A4); 4.G proved here
             GIVEN the inherited ledger formula for F_2 (that formula itself stays OPEN / imported).
Scope:       finite / local statements about cubic residue symbols on Z[omega], at every prime
             power and every frequency; the Kummer statement is global but standard. Nothing here
             is evidence for Theorem C4 or for any global statement.
Exact sources or dependencies:
             SKETCH.md Sec. 4-5 (this directory); manuscript paper.tex at commit 31c706bb...,
             sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed
             here), read as untrusted data: l. 557-603 (conventions), 640-700
             (lem:fixed-numerator-ray), 1053-1075 (eq:row-fixed-ray-reduction), 7041-7230
             (lem:prime-power-fourier, lem:full-correlation, lem:complete-support-correlation),
             13114-13271 (first transform, xi_r, eq:first-poisson-bridge), 13699-13800
             (second-transform local table, t_2, V, e_p), 14325-14380 (forced residues,
             eq:exceptional-row-count). Imported standard facts: I1 (cubic reciprocity), I5
             (Kummer theory, Artin reciprocity, local conductors of tame characters).
             ../../CUBIC_N3_GAPS.md (LC) for the inherited F_2 ledger identity [L1].
What was actually run:
             python3 -I lemmas_4bcd_gh_checks.py  (output: lemmas_4bcd_gh_checks.out, same
             directory). Exact integer / Z[omega] arithmetic except [D3-F] (floating point,
             labelled). Imports ../../a2/eis.py read-only. No Lean, lake or comparator process.
Smallest remaining gap:
             (i) the F_2 ledger formula F_2 = 2b_2 - (2/3)g_2 - p_2 + t_2 + V/3 + f/3 at theta = 1/3
             (LC [L1], a symbolic identity on top of the manuscript's (old-eq:2.13) and
             child-normalization definitions, A4) is not re-derived here; (ii) the A4 claim that at
             a nonunit equal-multiplicity second-transform prime there is no older moving
             character and Theta is unramified there (l. 14347-14350) is imported.
```

Notation follows SKETCH Sec. 1.1 and Sec. 4 and the manuscript's Sec. `arithmetic`, with the
order changed from 6 to 3.

* `F = Q(ω)`, `O = Z[ω]`. The prime above 3 is `(λ)`; `λ = 1 − ω` and the manuscript's
  `√−3 = 1 + 2ω = ω(1 − ω)` are associates, and only the ideal matters below. `S` is a fixed
  finite set of primes containing `(2)` and `(λ)`. A prime or ideal is *good* if it is outside `S`.
* The six units `±1, ±ω, ±ω²` map bijectively onto `(O/3)^×`. Hence every ideal prime to 3 has a
  unique generator `≡ 1 (mod 3)`, called *primary*, and products and (exact) quotients of primary
  elements are primary.
* For a good primary prime `p`, `P = q_p ≡ 1 (mod 3)`, and `χ_p(x) = (x/p)_3` is the cube root of
  unity `≡ x^{(P−1)/3} (mod p)`, extended by `0` on `p | x`. For a good primary `u`,
  `χ_u = Π_p χ_p^{v_p(u)}` (zero-extended at every prime of `u`). The symbol depends only on the
  ideal `(u)`.
* `e(z) = exp(2πi Tr(z/√−3))`; it is trivial on `O` because `(√−3)` is the different of `O`.
* `F(u,v;j)` is old-eq:2.11: `F(u,v;j) = Σ_{x mod u, y mod v, vx − uy ≡ j (mod uv)} χ_u(x) χ̄_v(y)`.
* `𝓡(a,b) := χ_b(a) χ̄_a(b)` for coprime good primary `a, b` (the manuscript's reciprocity factor,
  l. 935-940 and l. 7140-7142).

Two inputs carry all the order dependence.

**Fact 0** (proved in SKETCH Sec. 4; reproved here in one line). `(O/p)^×` is cyclic of order
`P − 1` and `3 | P − 1`, so `x ↦ x^{(P−1)/3}` maps it onto the subgroup of order 3; thus `χ_p` has
exact order 3, `χ_p^e` is principal iff `3 | e`, and a nonprincipal `χ_p^e` is primitive modulo `p`
(a nonprincipal character modulo a prime ideal has conductor exactly `p`). Also `χ_u(−1) = 1`
because `−1 = (−1)³`.

**I1 (cubic reciprocity; imported, standard).** For coprime good primary `a, b`,
`χ_b(a) = χ_a(b)`, i.e. `𝓡(a,b) = 1`. (The classical statement is for elements `≡ ±1 (mod 3)`;
since `−1` is a cube and the symbol depends only on the ideal, the sign is irrelevant.) In the
manuscript the sextic `𝓡` is the nontrivial bicharacter `𝔯(a,b)` of eq:reciprocity-four-class;
at `n = 3` it is identically `1` on coprime primary pairs, which removes every reciprocity phase
below. Check [D4]: 3466 coprime pairs, `𝓡 = 1`; control [D4-CTRL6]: the sextic symbol is not
reciprocal on 1464 of the same pairs.

**Notation clash (flagged).** SKETCH Lemma 4.D uses `𝔯` for the *ideal* of first-transform primes
with `3 ∤ i − j` (the manuscript's `\mathfrak r` at l. 13207). The manuscript also uses `𝔯(a,b)`
for the sextic reciprocity *bicharacter*. Below, `𝔯` is always the ideal; the bicharacter is
written `𝓡` and equals `1`.

---

## 1. Lemma 4.C (cubic child character, `eq:correlation-child-character`)

**Statement (as SKETCH, with the hypotheses made explicit).** Let `D, E, a, b` be good primary
elements with `(a, b) = 1` and `(ab, DE) = 1`; `D` and `E` may share primes with any
multiplicities, and any of them may be `1`. Put `u = Da`, `v = Eb`. Then for every `j ∈ O`

    F(Da, Eb; j) = F(D, E; j) · χ_a(j) · χ̄_b(−j),

with all zero values retained. Since `χ_b(−1) = 1`, `χ̄_b(−j) = χ̄_b(j)`. The sign is `χ_a(j)`,
not its conjugate.

*Imprecision fixed.* SKETCH writes the hypotheses but not that `D, E, a, b` must be primary and
good; I1 needs both. No other change.

*Proof.* The modulus `uv = DE·a·b` has the three pairwise coprime factors `DE`, `a`, `b` (by
`(a,b) = 1` and `(ab, DE) = 1`). By CRT, `x mod Da` corresponds to `(x mod D, x mod a)`,
`y mod Eb` to `(y mod E, y mod b)`, and the congruence `vx − uy ≡ j (mod uv)` is equivalent to the
three congruences

1. mod `a`: `Eb·x ≡ j`, since `u = Da ≡ 0`. As `Eb` is a unit mod `a`, `x ≡ j(Eb)^{−1} (mod a)`.
2. mod `b`: `−Da·y ≡ j`, so `y ≡ −j(Da)^{−1} (mod b)`.
3. mod `DE`: `Eb·x − Da·y ≡ j`. Here `Ebx mod DE` depends only on `x mod D`, and `Day mod DE`
   only on `y mod E`.

The summand factors as `χ_u(x) χ̄_v(y) = [χ_D(x) χ̄_E(y)] · χ_a(x) · χ̄_b(y)`. By (1) and (2),

    χ_a(x) = χ_a(j) χ̄_a(Eb),        χ̄_b(y) = χ̄_b(−j) χ_b(Da).

These identities hold also when `χ_a(j) = 0` or `χ_b(j) = 0`: only the unit factors `Eb` (mod `a`)
and `Da` (mod `b`) were inverted. In (3) substitute `x' = bx mod D` and `y' = ay mod E`; these are
bijections because `b` is a unit mod `D` and `a` mod `E`. The congruence becomes
`Ex' − Dy' ≡ j (mod DE)`, and `χ_D(x) χ̄_E(y) = χ_D(x') χ̄_E(y') · χ̄_D(b) χ_E(a)`. Summing over
`(x', y')` gives `F(D, E; j)`. The collected unit factor is

    χ̄_a(Eb) χ_b(Da) χ̄_D(b) χ_E(a)
      = [χ_E(a) χ̄_a(E)] · [χ_b(D) χ̄_D(b)] · [χ_b(a) χ̄_a(b)]
      = 𝓡(a,E) · conj 𝓡(b,D) · 𝓡(a,b),

using multiplicativity of `χ_a, χ_b` in the argument. Every pair here is coprime, good and
primary, so each factor is `1` by I1. ∎

*n = 3 changes made explicit.* Only the last line: the manuscript keeps the three sextic
reciprocity factors; at `n = 3` they are `1`. The Möbius-extension paragraph after the
manuscript's proof (l. 7231-7249) transfers verbatim with
`F̃_{D,E}(a,b;j) := F(D,E;j) χ_a(j) χ̄_b(−j)`: the identity
`Σ_{(a,b)=1} c(a,b) F(Da,Eb;j) = Σ_{a,b} c(a,b) F̃_{D,E}(a,b;j) Σ_{t|a, t|b} μ(t)` holds because the
divisor sum is `1_{(a,b)=1}`; off the coprime locus `F̃` is still artificial (control [C1-CTRLh]
below shows the formula fails at `a = b`).

*Checks.* [C1]: 7 configurations (`D = E = p`, `D = E = p³`, `D, E` coprime, `D, E` partly
common, `D = E = 1`, `D = E = p²` with `a = p'²`, inert `(5)` in `b`), all `j mod uv`, exact.
Controls: [C1-CTRLc], [C1-CTRLc3] (conjugated sign `χ̄_a(j)`) and [C1-CTRLh] (hypothesis
`(a,b) = 1` violated) are all detected. The configurations were chosen with `F(D,E;·) ≢ 0`; an
earlier draft of this script used allocations with `c = 1` at a one-sided prime, for which
`F ≡ 0` and the control was vacuous (recorded so the vacuity is not repeated).

**Verdict 4.C: proved here (PROPOSED).**

---

## 2. Lemma 4.D (first-transform classification and the bridge phase)

SKETCH states only the classification. The proof of the bridge (l. 13250-13262) also needs the
CRT factorisation with its reciprocity phase, so the statement is split into D1 and D2.

**Lemma 4.D1 (classification).** Let `C, D` be good primary with the same radical `𝔠` (complete
common support, as in the manuscript l. 13191-13196), and put `i_p = v_p(C)`, `j_p = v_p(D)` for
`p | 𝔠`. Let `𝔯 = Π_{p | 𝔠, 3 ∤ i_p − j_p} p` and `ξ_𝔯 = Π_{p | 𝔯} χ_p^{i_p − j_p}`. Then, as
functions of `k ∈ O`,

    χ_C(k) χ̄_D(k) = ξ_𝔯(k) · 1_{(k, 𝔠/𝔯) = 1},

and `ξ_𝔯` is a primitive character modulo `𝔯`. Consequently
`1_{(k,𝔠/𝔯)=1} = Σ_{𝔢 | 𝔠/𝔯} μ(𝔢) 1_{𝔢 | k}`, which is the manuscript's `𝔢`-expansion, and
`R ≤ p`, `E ≤ p − R` hold as stated there (`R`, `E`, `p` the log-norms of `𝔯`, `𝔢`, `𝔠`).

*Imprecision fixed.* SKETCH writes `ξ_𝔯 = Π χ_p^{(i−j) mod 3}`; that is the same character
(`χ_p^3 = 1` on units). It omits that `C, D` must have complete common support (otherwise
non-common primes of `C` or `D` contribute a residual character, which the manuscript places in
`a, b`). It also says "multiplicities `(i, j) = (v_p(C), v_p(D))`"; that is correct here, while
Lemma 4.B uses `(i, j_0)` for different moduli.

*Proof.* Both sides are products over `p | 𝔠` of functions of `k mod p`. Fix `p`. If `p | k`, the
left factor `χ_p(k)^{i_p} χ̄_p(k)^{j_p}` is `0` (both exponents are `≥ 1`), and so is the right
factor (`ξ_𝔯(k) = 0` if `p | 𝔯`, and the mask vanishes if `p | 𝔠/𝔯`). If `p ∤ k`, the left factor
is `χ_p(k)^{i_p − j_p}`; by Fact 0 it is `1` when `3 | i_p − j_p` and is the nonprincipal
character `χ_p^{i_p − j_p}` otherwise. This is the right factor. For primitivity: `(O/𝔯)^×` is the
product of the `(O/p)^×`, `p | 𝔯`. A character of `(O/𝔯)^×` factors through `(O/(𝔯/p))^×` iff it
is trivial on the kernel of reduction, which is the `p`-component `(O/p)^×`. There it restricts to
`χ_p^{i_p − j_p}`, which is nonprincipal by Fact 0. So no proper divisor of `𝔯` is a modulus for
`ξ_𝔯`. ∎

*n = 3 change made explicit.* The sextic criterion is "net exponent nonzero modulo six". At `n = 6`
a prime with `i − j ≡ 3 (mod 6)` carries the quadratic character `χ_p³` and lies in `𝔯`. At `n = 3`
there is no quadratic twist: `χ_p³` is principal, and such a prime is in `𝔠/𝔯` (a pure puncture).
For example, at `(i, j) = (4, 1)` the sextic rule puts `p` in `𝔯`, while the cubic character is
principal (control [D1-CTRL6]).

**Lemma 4.D2 (bridge CRT factorisation, trivial reciprocity phase).** Let `a, b, r` be pairwise
coprime good primary elements, `ξ` a character modulo `r` (zero-extended), and `h ∈ O`. Put
`g(a,h) = Σ_{x mod a} χ_a(x) e(hx/a)` and `g_ξ(r,h) = Σ_{z mod r} ξ(z) e(hz/r)`. Then

    Σ_{k mod rab} χ_a(k) χ̄_b(k) ξ(k) e(hk/(rab))
       = χ_a(r) χ̄_b(r) ξ(ab) · g(a,h) · conj g(b,−h) · g_ξ(r,h).

For a further good primary `e` coprime to `rab`, the substitution `k = e k'` multiplies the
character factor by `χ_a(e) χ̄_b(e) ξ(e)`. Here `ξ(e)` is a frozen scalar, and the additive
normalisation of the substitution is order-free (l. 13240-13246). With `r` the primary generator of `𝔯`, `e` that of `𝔢` and `ξ = ξ_𝔯`, the total
phase is `χ_a(𝔢𝔯) ξ_𝔯(a) · conj(χ_b(𝔢𝔯) conj ξ_𝔯(b))`. That is `τ_C(a) conj τ_D(b)` divided by
`τ(a) conj τ(b)`, as in l. 13228-13231, and the factor `conj 𝓡(a,b)` of eq:first-poisson-bridge
equals `1`.

*Proof.* The map `(x, y, z) ↦ k = br·x + ar·y + ab·z` from `O/a × O/b × O/r` to `O/rab` is a
bijection (CRT: `br` is a unit mod `a`, and so on). Then `χ_a(k) = χ_a(br) χ_a(x)`,
`χ̄_b(k) = χ̄_b(ar) χ̄_b(y)`, `ξ(k) = ξ(ab) ξ(z)`, and
`e(hk/(rab)) = e(hx/a) e(hy/b) e(hz/r)` because `e` is additive. The sum factorises into the
three Gauss sums times `χ_a(br) χ̄_b(ar) ξ(ab)`, using
`Σ_y χ̄_b(y) e(hy/b) = conj Σ_y χ_b(y) e(−hy/b)`. Finally
`χ_a(br) χ̄_b(ar) = χ_a(r) χ̄_b(r) · χ_a(b) χ̄_b(a) = χ_a(r) χ̄_b(r) · conj 𝓡(a,b)`, and `𝓡(a,b) = 1`
by I1. The `e`-substitution is a bijection `k' mod rab ↔ k mod rab` restricted to `e | k`, and
`χ_a(ek') = χ_a(e) χ_a(k')`. ∎

*Remark.* D2 holds for arbitrary multiplicities in `a, b` (`χ_a` is a character modulo
`rad a` lifted to `a`). The normalisation `G(a,h) = q_a^{−1/2} g(a,h)` and the scalar
`H/(X q_𝔢 √q_𝔯)` of eq:first-poisson-bridge are order-free.

*Checks.* [D1]: one prime, all `i, j ≤ 7`, `Np ∈ {7, 13, 25}`. [D2]: `𝔠` a product of three primes
(norms 7, 13, 7), 216 exponent patterns, all `k mod 𝔠`, plus primitivity of `ξ_𝔯`. [D3]: termwise
CRT identity, exact, two triples. [D3-F]: full Gauss-sum identity in floating point (max error
`3·10⁻¹⁴`; labelled, not certified). Controls: [D1-CTRL6], [D4-CTRL6].

**Verdict 4.D (D1 and D2): proved here (PROPOSED).**

---

## 3. Lemma 4.B (cubic `lem:full-correlation`)

**Statement.** Let `u, v` be good primary and `j ∈ O`.

* (Fourier form) `F(u,v;j) = (q_u q_v)^{−1/2} Σ_{h mod uv} G(u,h) conj G(v,h) e(−jh/(uv))`.
* (Zero frequency) `F(u,v;0) = φ(u) 1_{u = v}`, where `φ(u) = #(O/u)^×`.
* (Common factors) Let `C` be the primary generator of `(u,v)`, `u = Cn_1`, `v = Cn_2`. Then
  `F(u,v;j) = 0` unless `C | j`. For `j = Ck`,

      F(Cn_1, Cn_2; Ck) = χ_{n_1}(k) χ̄_{n_2}(−k) Π_{p^c ∥ C} L_{p^c},

  where, with `P = q_p`:
  * if `p ∤ n_1 n_2`: `L_{p^c} = P^{c−1} χ_p(n_1/n_2)^c · {P − 1 if p | k; −1 if p ∤ k and 3 ∤ c;
    P − 2 if p ∤ k and 3 | c}`;
  * if `p` divides exactly one of `n_1, n_2`: `L_{p^c} = P^{c−1}(P − 1) 1_{3|c} 1_{p∤k}`.

  `L_C := Π L_{p^c}` equals the congruence sum
  `Σ_{x, y mod C, n_2 x − n_1 y ≡ k (mod C)} χ_C(x) χ̄_C(y)`, and `|L_C| ≤ q_C`.
* (Corollary) For `i > j_0 ≥ 1`, `F(p^i, p^{j_0}; j) = 0` unless `3 | j_0` and `j = p^{j_0}k` with
  `p ∤ k`; then it equals `P^{j_0−1}(P − 1) χ_p(k)^{i−j_0}`.

*Imprecisions fixed.* (a) SKETCH omits the factor `𝓡(n_1,n_2)` from the manuscript's statement.
That is correct only because `𝓡 = 1` (I1) on the coprime primary pair `(n_1, n_2)`. Here
`n_1 = u/C` and `n_2 = v/C` are primary because `u, v, C` are. (b) `χ_p(n_1/n_2)^c` means
`χ_p(n_1)^c χ̄_p(n_2)^c`; it is `1` when `3 | c`. (c) `k` is determined modulo `Cn_1n_2`, and every
right-hand factor has that period, so the formula is well posed. (d) The artificial extension of
`L_C` to non-coprime residual pairs (manuscript l. 7114-7122) transfers verbatim, with local value
`0` when `p | (n_1, n_2)`; it is used only after Möbius inversion and is not a congruence sum.

*Proof.* (Fourier form) Expand both Gauss sums. For `t ∈ O`, `h ↦ e(ht/(uv))` is a character of `O/uv`,
and it is trivial iff `t/(uv) ∈ O`, because `{z : Tr(zO/√−3) ⊂ Z} = O`. So
`Σ_{h mod uv} e(h(vx − uy − j)/(uv))` equals `q_u q_v` if `vx − uy ≡ j (mod uv)` and `0` otherwise.
This is order-free.

(Zero frequency) Nonzero summands have `x, y` units modulo `u, v`. Reducing `vx ≡ uy (mod uv)`
modulo `u` gives `u | vx`, so `u | v`; symmetrically `v | u`; primary generators then give `u = v`.
The congruence becomes `x ≡ y (mod u)`, and the sum is `Σ_{x unit} χ_u(x) χ̄_u(x) = φ(u)`. Zero
masks are used even when a local power `χ_p^{v_p(u)}` is principal.

(Common factors) If a summand is nonzero then `j = vx − uy ≡ 0 (mod C)`. For `j = Ck` the
congruence is equivalent to `n_2 x − n_1 y ≡ k (mod C n_1 n_2)`. Reduce it modulo `n_1` and `n_2`.
Since `(n_1, n_2) = 1`, `x ≡ k n_2^{−1} (mod n_1)` and `y ≡ −k n_1^{−1} (mod n_2)`, so

    χ_{n_1}(x) = χ_{n_1}(k) χ̄_{n_1}(n_2),     χ̄_{n_2}(y) = χ̄_{n_2}(−k) χ_{n_2}(n_1),

with zeros retained. The unit factor `χ̄_{n_1}(n_2) χ_{n_2}(n_1) = 𝓡(n_1,n_2) = 1` by I1. *(This is
the only change from the sextic proof in this step.)* The remaining part of the summand is
`χ_C(x) χ̄_C(y)`, which depends on `x, y mod C`. The lift count is order-free (manuscript
l. 7159-7170): at a prime `p` with `c = v_p(C)` and `p ∤ n_1 n_2` there is no extra lift; if
`d = v_p(n_1) > 0` (so `p ∤ n_2`), `y mod p^c` is free and determines `x mod p^{c+d}` uniquely.
By CRT the solutions correspond bijectively to the solutions of `n_2 x − n_1 y ≡ k (mod C)`, which
gives `L_C`, and `L_C = Π_p L_{p^c}` by CRT again.

*Local factor.* Fix `p^c ∥ C`, put `A = χ_p^c`, a character of `𝔽_p^× = (O/p)^×` extended by `0`.
By Fact 0, `A` is principal iff `3 | c`. At least one of `n_1, n_2` is a unit at `p`. For each
`y mod p^c` (if `p ∤ n_2`; symmetrically `x` otherwise) there is exactly one `x mod p^c`, and the
summand depends only on residues mod `p`. So `L_{p^c} = P^{c−1} Σ_{field} A(x) Ā(y)`, the field
sum running over solutions of `n_2 x − n_1 y = k` in `𝔽_p`.

* `p ∤ n_1 n_2`, `p | k`: `x = (n_1/n_2) y`, giving `A(n_1/n_2) Σ_{y ≠ 0} 1 = (P − 1) A(n_1/n_2)`.
* `p ∤ n_1 n_2 k`: put `y = (k/n_1) t`, `x = (k/n_2)(1 + t)`. The sum is
  `A(n_1/n_2) Σ_{t ≠ 0, −1} A((1+t)/t) = A(n_1/n_2) Σ_{z ∈ 𝔽_p^×, z ≠ 1} A(z)`, since
  `t ↦ z = 1 + 1/t` is a bijection from `𝔽_p^× ∖ {−1}` onto `𝔽_p^× ∖ {1}`. By orthogonality this is
  `−A(n_1/n_2)` if `A` is nonprincipal (`3 ∤ c`) and `(P − 2) A(n_1/n_2)` if `A` is principal
  (`3 | c`).
* `p | n_1`, `p ∤ n_2`: the field equation forces `x = k/n_2`. If `p | k` then `A(x) = 0`.
  Otherwise the sum is `A(k/n_2) Σ_{y ∈ 𝔽_p} Ā(y)`, which is `(P − 1)` if `A` is principal (and
  then `A(k/n_2) = 1`) and `0` otherwise. The case `p | n_2` is symmetric.

`A(n_1/n_2) = χ_p(n_1/n_2)^c`, which gives the stated `L_{p^c}`. The bound `|L_{p^c}| ≤ P^c`
follows from `P − 2 < P − 1 < P`, so `|L_C| ≤ q_C`.

(Corollary) Take `u = p^i`, `v = p^{j_0}`. Then `C = p^{j_0}`, `n_1 = p^{i−j_0}`, `n_2 = 1`, and
`χ_{n_1}(k) = χ_p(k)^{i−j_0}`. The one-sided local factor `P^{j_0−1}(P−1) 1_{3|j_0} 1_{p∤k}` gives
the claim. ∎

*n = 3 changes made explicit.* `6 → 3` in the principal/nonprincipal dichotomy (Fact 0), and
`𝓡(n_1, n_2) = 1`. There is no quadratic case: at `n = 6`, `c ≡ 3 (mod 6)` gives the
nonprincipal `χ_p³` and the value `−1`, while at `n = 3` it gives `P − 2` (control [B1-CTRL6]:
`u = v = p³`). The first unequal nonzero case is `j_0 = 3` (it is `j_0 = 6` in the manuscript).

*Checks.* [B1]: 14 configurations (prime powers up to `p⁴·p³`, mixed composites, conjugate primes
of norm 7, the inert prime 5), all `j mod uv` (2 248 034 frequencies), exact. [B2]: the
Corollary at `(2,1), (3,1), (4,3), (5,3), (3,2), (4,2)`. [B3]: zero frequency. Controls:
[B1-CTRL6], [B1-CTRL6b] (sextic rule), [B1-CTRLc] (conjugated residual symbol).

**Verdict 4.B: proved here (PROPOSED).** The Fourier form, the lift count and the zero-frequency
argument are order-free and copied. The local field sums and the reciprocity factor are re-done
at `n = 3` above.

---

## 4. Lemma 4.H (Kummer with `μ_3`, fixed numerators) and Corollary 4.H

**Lemma 4.H (statement, made precise).** Fix `0 ≠ a ∈ O`. Let `K = F(α)` with `α³ = a`.

1. `K/F` is abelian, and `σ ↦ σ(α)/α` is an injective homomorphism `Gal(K/F) → μ_3`.
2. `K/F` is unramified outside the primes dividing `3a`, and tamely ramified (ramification index
   `1` or `3`) at every prime `𝔭 | a` with `𝔭 ∤ 3`. (SKETCH says "good primes dividing `a`"; the
   statement also holds at `(2)`, which is in `S` but prime to 3.)
3. For every prime `𝔭 ∤ 3a`, `Frob_𝔭(α)/α = (a/𝔭)_3`, where `(a/𝔭)_3 ∈ μ_3` and
   `(a/𝔭)_3 ≡ a^{(q_𝔭 − 1)/3} (mod 𝔭)`. At a good `𝔭` this is `χ_p(a)`.
4. `𝔄 ↦ (a/𝔄)_3` (multiplicative over prime factors), on ideals coprime to `3a`, is a ray class
   character. Its conductor is supported on primes dividing `3a`, with exponent `≤ 1` at every
   prime dividing `a` and prime to 3. No bound is asserted at `(λ)`. Check [H1] finds period
   dividing `18 = 2·λ⁴·(unit)` for the 27 numerators below; that is a finite observation, not
   used.
5. Fix generators `π_𝔭`, `𝔭 ∈ S`. On primary ideals `A` outside `S`, the functions
   `A ↦ χ_A(u Π_{𝔭∈S} π_𝔭^{v_𝔭})`, with `u ∈ O^×` and `v_𝔭 ≥ 0`, depend only on the class of `u`
   in `O^×/(O^×)³ ≅ Z/3` (representatives `1, ω, ω²`; `−1 = (−1)³`) and on `v_𝔭 mod 3`. So there
   are at most `3^{|S|+1}` of them, all ray characters with conductor supported on `S`. For
   `S = {(2), (λ)}` there are exactly 27, pairwise distinct.

*Imprecision fixed.* SKETCH writes that the identification is a ray character "with exponent
`≤ 1` at good primes". It must be read *on ideals coprime to `3a`*: as the manuscript stresses
(l. 664-666), the prescribed zero of `χ_A(a)` when a good `A` meets `a` is not erased by the ray
character.

*Proof.* (1) `F ⊃ μ_3`, so the roots `α, ωα, ω²α` all lie in `K`, and `K/F` is Galois. For `σ` in
the Galois group, `σ(α)/α ∈ μ_3`. Since `σ` fixes `μ_3 ⊂ F`,
`στ(α)/α = σ(τ(α)/α) · σ(α)/α = (τ(α)/α)(σ(α)/α)`, a homomorphism. It is injective because `σ` is
determined by `σ(α)`.

(2) `disc(X³ − a) = −27a²`. `O[α] ⊂ O_K`, so the relative discriminant of `K/F` divides
`(27a²)`, and no prime outside `3a` ramifies. At a prime `𝔭 | a` with `𝔭 ∤ 3`, the ramification
index divides `[K:F] | 3`, which is prime to the residue characteristic. So the ramification is
tame.

(3) For `𝔭 ∤ 3a`, unramified, and `𝔓 | 𝔭` in `K`, arithmetic Frobenius satisfies
`Frob(x) ≡ x^{q_𝔭} (mod 𝔓)` on `O_K`. So `Frob(α)/α ≡ α^{q_𝔭 − 1} = a^{(q_𝔭−1)/3} (mod 𝔓)`;
`α` is a unit at `𝔓` because `𝔭 ∤ a`. Reduction mod `𝔓` is injective on `μ_3`: the differences
`1 − ω`, `1 − ω²` generate `(λ)` up to units, and `𝔭 ∤ 3`. Both sides are in `μ_3`, so they are
equal.

(4) By (3) and multiplicativity, `(a/𝔄)_3 = κ(Art_{K/F}(𝔄))` for `𝔄` coprime to `3a`, where
`κ: σ ↦ σ(α)/α`. Artin reciprocity (I5; Milne, CFT, VIII (5.3), (5.5), as cited by the
manuscript) makes `Art_{K/F}` factor through the ray class group modulo the conductor `𝔣(K/F)`.
That conductor is divisible only by ramified primes, hence supported on `3a` by (2). Local
conductor exponents of characters of a tamely ramified abelian extension are `≤ 1`. Directly:
by local class field theory the local character `κ_𝔭` on `O_𝔭^×` has order dividing 3. The
group `1 + 𝔭O_𝔭` is pro-`ℓ` with `ℓ` the residue characteristic, `ℓ ≠ 3`. Every element of it is
therefore a cube, and `κ_𝔭` kills it. So the exponent at `𝔭` is at most 1.

(5) For `A` primary outside `S`, `A` is coprime to every unit and every `π_𝔭`, so
`χ_A(u Π π_𝔭^{v_𝔭}) = χ_A(u) Π χ_A(π_𝔭)^{v_𝔭}` is a product of cube roots of unity. It depends on
`v_𝔭 mod 3` and, since `χ_A(w³) = 1` for a unit `w`, on `u mod (O^×)³`. `O^× = ⟨−ω⟩` is cyclic of
order 6, its cubes are `{±1}`, and the quotient has order 3. Apply (4) to each of the at most
`3^{|S|+1}` numerators. All are supported on `S`, since `S ⊃ {(2), (λ)}` contains the primes over
3 and the `π_𝔭`. *Distinctness for `S = {(2), (λ)}`.* If two numerators gave the same character,
their quotient `x = ω^s 2^t λ^r` would have `(x/𝔭)_3 = 1` at all but finitely many `𝔭`. Then
almost all primes split completely in `F(x^{1/3})`, and by Chebotarev `F(x^{1/3}) = F`, so `x` is a
cube. The valuations at `(2)` and `(λ)` force `3 | t` and `3 | r`, and `ω^s` is a cube only for
`3 | s`, because `F` contains no primitive 9th root of unity (`[Q(ζ_9):Q] = 6`). ∎

*n = 3 changes made explicit.* `μ_6 → μ_3` and `6 → 3` throughout. The unit group acts through
`O^×/(O^×)³` of order 3, not `O^×/(O^×)⁶ = O^×` of order 6. The count is `3^{|S|+1}`, not
`6^{|S|+1}`. The tameness/exponent-1 clause is new relative to the manuscript, which asserts no
conductor bound (l. 662-663). It is not needed for 4.H(5), only for Lemma 4.K.

*Checks.* [H1]: the 27 numerators `ω^s 2^t λ^r` give characters constant on classes mod 18 over
the 422 primary primes of norm `≤ 3000`; control [H1-CTRL6] (not periodic mod 6). [H2]: exactly 27
distinct. [H2b]: `χ_A(−1) = 1`. [H3]: `a = q` with `Nq = 7`: the character depends only on `A mod q`
and is nonconstant (exponent 1 at `q`). [H4]: `X³ − a` has a root mod `𝔭` iff `(a/𝔭)_3 = 1`
(261 pairs); control [H4-CTRL6]. All finite.

**Verdict 4.H: proved here (PROPOSED)**, with the two precision fixes above. It uses only the
standard imported inputs I5 and Chebotarev.

### Corollary 4.H (exceptional rows, forced residues, count)

**Statement (made precise).** Fix, for the current sum, a finite set `Q` of good primes and
residues `e_q ∈ Z/3` for `q ∈ Q`. These are the exponents at `q` of the frozen part of the row,
`v_q(G_c V_id)`, together with any frozen moving character at `q`. Put `e_q = 0` for good
`q ∉ Q`. For a nonzero row `h' ∈ O`, consider on primary `n` outside `S ∪ Q ∪ supp(h')`

    ψ_{h'}(n) = χ_n(h') · Π_{q∈Q} χ_q(n)^{e_q}.

1. (Forced residues) The primitive character inducing `ψ_{h'}` has conductor supported on `S`
   (a necessary condition for it to be a member of the fixed family `Θ`) iff
   `v_q(h') ≡ −e_q (mod 3)` for every good prime `q`.
2. (Cube form) Then `(h'_good) = 𝔥_0 𝔳³` with `𝔥_0 = Π_{q∈Q} q^{r_q}`, `r_q ∈ {0,1,2}`,
   `r_q ≡ −e_q (mod 3)`. `𝔥_0` is determined by the frozen data and is cube-free, and `𝔳` is an
   arbitrary good ideal.
3. (Count) Let `f` be `log_Z q_{𝔥_0}`. Then
   `#{exceptional h' : q_{h'} ≤ Z^{m'}} ≪_S (log Z)^{|S|} Z^{(m' − f)/3}`. In particular
   `≪ Z^{(m'−f)/3+ε}` whenever `f` is at least the radical length of the primes with `r_q ≠ 0`.
4. (Values of `e_p`) At a nonunit equal-multiplicity second-transform prime of multiplicity `i`
   (`3 ∤ i`), `v_p(G_c V_id) = i + 1`. If there is no older moving character at `p` (imported,
   A4), then `e_p = i + 1` and `r_p ≡ −(i+1)`, i.e. `1, 0, 2, 1, 0, 2` for `i = 1, …, 6`. At
   `i = 1`, `r_p = 1`, so `f ≥ v_1` (the radical length of these primes), as used in 4.G.

*Imprecisions fixed.* (a) SKETCH says "`𝔥_0` fixed". It is fixed only after the frozen moving
data (`Q`, `e_q`) and the `S`/unit data are fixed. The unit and the `S`-part of `h'` range over
`6 · O((log Z)^{|S|})` values, which is the `ε`. (b) SKETCH's "induces a member of `Θ`" is used
only through the necessary condition "conductor supported on `S`". That is all the upper bound
needs. (c) In 4, `e_p = i + 1` is not a Kummer fact: it comes from the definition
`e_p = v_p(v) mod n` with `v = G_c V_id` (manuscript l. 13760-13767, `6 → 3`). That definition
gives `v_p(G_c) = i` and `v_p(V_id) = 1` at a nonunit prime. The absence of an older moving
character at `p` is A4's claim (l. 14347-14350).

*Proof.* (1) Write `h' = ε h_S h_good` as in eq:row-fixed-ray-reduction. For primary `n` coprime
to `h'`, multiplicativity and I1 give, with zeros retained,

    χ_n(h') = χ_n(ε h_S) · Π_{q | h_good} χ_n(q)^{v_q(h')} = χ_n(ε h_S) · Π_{q | h_good} χ_q(n)^{v_q(h')}.

At `n = 3` the reciprocity factor `𝓡(n, h_good)` of the manuscript is `1`. By Lemma 4.H(5), the
first factor is a ray character with conductor supported on `S`. Hence
`ψ_{h'}(n) = θ(n) · Π_q χ_q(n)^{v_q(h') + e_q}`, with `θ` an `S`-ray character and the product
over the finitely many good `q` with `v_q(h') + e_q ≢ 0`. The product of `θ` and characters modulo
distinct good primes has, at each good `q`, conductor exponent `1` if `χ_q^{v_q(h')+e_q}` is
nonprincipal and `0` otherwise (CRT, as in the proof of 4.D1). By Fact 0 that is `1` iff
`3 ∤ v_q(h') + e_q`.

(2) is immediate from (1).

(3) Given `ε` (6 choices) and `h_S` with `q_{h_S} ≤ Z^{m'}` (`O((m' log Z)^{|S|})` choices), the
condition `q_{h'} ≤ Z^{m'}` forces `N𝔳³ ≤ Z^{m'}/(q_{𝔥_0} q_{h_S}) ≤ Z^{m'−f}`. The number of
ideals of norm `≤ T` is `O(T + 1)`, applied with `T = Z^{(m'−f)/3}`. If `T < 1`, only `𝔳 = (1)`
can occur, and only if `q_{𝔥_0} ≤ Z^{m'}`. This is the manuscript's bounded-scale boundary
convention.

(4) is the arithmetic `−(i+1) mod 3` for `i = 1, …, 6`, given the imported A4 input. ∎

*n = 3 changes made explicit.* The sextic forced residue at `i = 1` is `v_p(h') ≡ 4 (mod 6)`, the
form is `𝔥_0 𝔳⁶`, and the count is `Z^{(m'−2f)/6}` (weakened in the manuscript to `Z^{(m'−f)/6}`).
At `n = 3` the residue is `1 (mod 3)`, the form is `𝔥_0 𝔳³`, and the count is `Z^{(m'−f)/3}` with
`f = v_1`. This is the source of the threshold `2M/3`.

*Checks.* [H5]: 1074 rows `h'` of norm `≤ 300` (all units and `S`-parts) and `e ∈ {0,1,2}`. The
test "`ψ_{h'}` constant on classes mod 18" over primary primes of norm `≤ 1500` agrees exactly
with the forced-residue rule (162 exceptional cases). Control [H5-CTRL6]: the sextic rule
disagrees on 66 rows. A small illustration of the `𝔳³` count is printed; it is not a check.

**Verdict Corollary 4.H: proved here (PROPOSED) for parts 1-3. Part 4 is proved given the imported
A4 statement** that no older moving character sits at a nonunit equal-multiplicity
second-transform prime. That statement is not a Kummer fact and is not re-derived here.

---

## 5. Lemma 4.G (second-transform table, `κ_2 = 1`)

**Statement (made precise).** Let `D_2, E_2` be the second-transform moduli, with complete common
support. In `log_Z` units put:

* `c_2, d_2` for their log-norms and `b_2 = (c_2 + d_2)/2`;
* `G_c = (D_2, E_2)` and `g_2 = log_Z q_{G_c}`;
* `p_2` for the log-norm of the common radical;
* `t_2` (resp. `V`) for the radical length of the equal-multiplicity primes with `3 ∤ i` at which
  `j/G_c` is a unit (resp. a nonunit);
* `f = v_1` for the radical length of the nonunit primes with `i = 1`.

These are the manuscript's definitions (l. 13723-13740) with `6 → 3`. **Assume the ledger formula**

    F_2 = 2b_2 − (2/3)g_2 − p_2 + t_2 + V/3 + f/3                             (LF)

(LC [L1], derived from the manuscript's (old-eq:2.13) and its child normalization at `θ = 1/3`).
Then:

* (a) The partitioned scalar `1_part(h') F(D_2, E_2; G_c V_id h') / Z^{g_2 − t_2}` has modulus
  `≤ 1`. The absolute local table is: equal `3 ∤ i`, unit: `P^{i−1}`; equal `3 ∤ i`, nonunit:
  `P^{i−1}(P−1) ≤ P^i`; equal `3 | i`: `≤ P^{i−1}(P−1) ≤ P^i`; unequal `i > j_0`:
  `P^{j_0−1}(P−1) 1_{3|j_0} 1_{p ∤ k} ≤ P^{j_0}`. Every other unequal case is `0`.
* (b) `F_2` is a sum of per-prime contributions, given by the SKETCH table. Hence
  `F_2 − b_2 ≥ 0` at every prime, `F_2 ≥ b_2 ≥ min(c_2, d_2)`, and `κ_2 = 1`. Equality holds
  exactly at nonunit `i = 1, 2` and equal `i = 3`.

*Proof.* (a) Complete common support means every prime of `D_2E_2` is common. At `p` with
`(v_p(D_2), v_p(E_2)) = (i, j_0)`, Lemma 4.B gives the local factor of `F(D_2, E_2; j)`: the
residual `χ_{n_1}(k) χ̄_{n_2}(−k)` factorises over primes, with `χ_p(k)^{i−j_0}` or its conjugate
at unequal primes. So:

* equal `i`, `p ∤ k`: `|L| = P^{i−1}` if `3 ∤ i`, `P^{i−1}(P−2)` if `3 | i`;
* equal `i`, `p | k`: `P^{i−1}(P−1)`;
* unequal: the Corollary of 4.B.

At a unit prime `P^{i−1} = P^{g_2 − t_2}` locally (`g_2 = i`, `t_2 = 1`). At every other prime the
local value is `≤ P^{g_2}`. The residual symbols have modulus `≤ 1`. This proves (a) and the
manuscript's table with `6 → 3`. Check [G0] (brute force, `Np = 7, 13`) confirms the exact maxima.

(b) Every quantity in (LF) is a sum over second-transform primes, so `F_2` is additive. At one
prime, in `log q_p` units:

| local case | `c_2, d_2` | `g_2` | `p_2` | `t_2` | `V` | `f` | `F_2` by (LF) | `b_2` | `F_2 − b_2` |
|---|---|---|---|---|---|---|---|---|---|
| equal `i`, `3 ∤ i`, unit | `i, i` | `i` | 1 | 1 | 0 | 0 | `4i/3` | `i` | `i/3` |
| equal `i`, `3 ∤ i`, nonunit | `i, i` | `i` | 1 | 0 | 1 | `1_{i=1}` | `4i/3 − 2/3 + (1/3)1_{i=1}` | `i` | `0` at `i = 1, 2`; `(i−2)/3` for `i ≥ 4` |
| equal `i`, `3 ∣ i` | `i, i` | `i` | 1 | 0 | 0 | 0 | `4i/3 − 1` | `i` | `i/3 − 1 ≥ 0` |
| unequal `i > j_0`, `3 ∣ j_0` | `i, j_0` | `j_0` | 1 | 0 | 0 | 0 | `i + j_0/3 − 1` | `(i+j_0)/2` | `(3i − j_0 − 6)/6 ≥ 1/2` |

The last bound holds because `3 | j_0` and `i ≥ j_0 + 1` give `3i − j_0 − 6 ≥ 2j_0 − 3 ≥ 3`.
Unequal primes with `3 ∤ j_0` carry a zero correlation (a), so their allocations vanish and
contribute no row. The `f` entry at nonunit `i = 1` is the forced residue `r_p = 1` of Corollary
4.H(4); without it the entry is `2/3 < 1` (control [G1-CTRL], ratio `2/3 = 2θ`). Summing,
`F_2 ≥ b_2 = (c_2 + d_2)/2 ≥ min(c_2, d_2)`. ∎

*n = 3 changes made explicit.* The unit/nonunit split and `t_2, V` are defined at `3 ∤ i`, not
`6 ∤ i`. The unequal nonzero case needs `3 | j_0`. The coefficient `2/3` on `g_2` and `f/3`
replace the sextic `θ = 1/6` coefficients via (LF). The count exponent is `/3` (Corollary 4.H).

*Checks.* [G0] (absolute table, brute force); [G1], [G2] (table arithmetic, exact rationals,
`i ≤ 60`); [G1-CTRL].

**Verdict 4.G: proved here given (LF) and Corollary 4.H(4).** The local table and `κ_2 = 1` are
now derived rather than read off maxima. **OPEN:** (LF) itself, i.e. that the manuscript's
count × volume / allowance ledger (old-eq:2.13, child normalization `Δ_child`, allowance `a_0`)
re-instantiated at `θ = 1/3` gives exactly (LF). LC [L1] verifies this as a symbolic identity
*given* the manuscript's definitions. This note does not re-derive those definitions (A4).

---

## 6. Updated risk-register lines (SKETCH Sec. 5, items 3-5)

| # | step | status | evidence | most likely failure mode |
|---|---|---|---|---|
| 3 | Lemmas 4.B, 4.C, 4.D (correlations, child character, `𝔯` classification and bridge phase) | **proved here (PROPOSED)**, LEMMAS_4BCD_GH.md Secs. 1-3; uses only Fact 0 and I1 | `lemmas_4bcd_gh_checks.py` [B1]-[B3], [C1], [D1]-[D4] exact, with 8 failing controls detected | essentially none at the stated level. The residual risk is a misapplication downstream (e.g. using 4.C off the coprime locus without the Möbius insertion), not the lemmas themselves |
| 4 | Lemma 4.G (`F_2` table, `κ_2 = 1`) | **proved here given (LF)** (LEMMAS_4BCD_GH.md Sec. 5): absolute table from 4.B; per-prime `F_2` from (LF) and the A4 definitions of `t_2, V, f` with `6 → 3` | [G0] brute force; [G1], [G2] exact; [G1-CTRL]; LC [L1] for (LF) | (LF), the manuscript's ledger at `θ = 1/6` re-instantiated at `θ = 1/3`, is still inherited (A4); any error there changes the coefficients, not the local table |
| 5 | Lemma 4.H and its count `Z^{(m'−f)/3}` | **4.H proved here (PROPOSED)** (Kummer/Artin, with the precision fixes: ideals coprime to `3a`, exponent `≤ 1` at all primes `∤ 3` dividing `a`, exactly 27 `S`-characters). **Corollary 4.H parts 1-3 proved here; part 4 (`e_p = i + 1`) proved given A4's "no older moving character at a nonunit equal-multiplicity prime"** | [H1]-[H5] finite exact checks, controls [H1-CTRL6], [H4-CTRL6], [H5-CTRL6] | A4's claim about older moving characters at second-transform primes (l. 14347-14350), on which `f = v_1` rests |

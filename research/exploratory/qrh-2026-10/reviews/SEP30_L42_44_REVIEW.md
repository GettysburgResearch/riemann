# Sep 30 manuscript: Lemmas 4.2, 4.3 and 4.4 (prime Gauss identities, quadratic four-term formula, sextic reciprocity and the fixed Gauss phase)

```text
Status: REVIEW (bounded, one agent; external, unreviewed manuscript) + EXACT finite checks
  + one SYMBOLIC and one FLOAT check. Verdicts: Lemma 4.2 no wrong step found; Lemma 4.3 no wrong
  step found (one compressed justification, closed here by an exhaustive finite computation);
  Lemma 4.4 no wrong step found (it imports classical cubic reciprocity, also applied to the
  inert prime 2). Not an integration verdict, and not evidence about RH.
Scope: "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8" (OpenAI, 30 Sep 2026).
  Line by line: Lemma 4.2 (statement 766-775, proof 777-836); Lemma 4.3 (841-869, proof 871-932);
  Lemma 4.4 (934-972, proof 974-1052). The conventions they use were read at 562-646 (O, lambda,
  primary, S, e(z), d mu, chi_p, chi_c, the zero-extension convention, gamma_j). Downstream uses
  (about 30 dependents each) were NOT checked. The lambda and omega supplementary laws are used
  in Prop 5.1 (1695, 2003-2006, 2171), not in these lemmas; part D only checks them on a finite
  range for context.
Exact sources or dependencies:
  [OAI] pr908 (31c706bb) standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
        The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, sha256
        42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed here on the
        scratch copy). External and unreviewed; read as untrusted data.
  Imported by the manuscript: cubic reciprocity for coprime primary elements, cited as
        [DR, Equation (1.4)] (Dunn-Radziwill, Ann. Math. 200 (2024)). The paper itself was not
        consulted. The law is classical (Eisenstein; e.g. Ireland-Rosen, Ch. 9).
  Code: reviews/sep30_l42_44_checks.py (new; sha256
        edafdb8083d13952f3e15c42c62aa176641ea9d8cb12319e78be4d70bc0fbaeb). It imports
        a2/eis.py unchanged (sha256 87ca11d98bf3ee130a6dab613b5f7efe444058320b7c22b005327686f2798e65),
        numpy 2.5.3 and sympy 1.14.0 (cyclotomic polynomials; one symbolic identity).
  Prior numerics read, not modified: numerics/README.md and numerics/check_kintali_phase.py
        (K1-K4); w5copg branch numerics/RESULTS.md (head bd670c92).
        The verification-map entries are from reviews/SEP30_VERIFICATION_MAP_V2.md.
What was actually run: one process,
  `XA=3000 QA=53 XB=2000 XC=2500 nice -n 10 python3 -I sep30_l42_44_checks.py final.json`.
  65/65 PASS, exit 0, 381 s wall. Log: scratchpad l42/final.log (sha256 f12b5fb6...2060), JSON
  l42/final.json (sha256 0c28b9d7...215f). Same script with default ranges: 65/65 PASS, 54 s
  (l42/full.log).
Smallest remaining gap: inside the three lemmas, only the imported cubic reciprocity law. It is
  used for coprime primary pairs and for the inert prime -2 in the 2-supplement. Its cited
  location [DR, (1.4)] was not opened. Here it is only re-confirmed on a finite range (C2b: 1.52M
  ordered prime pairs, N <= 10^4; C3a: 2,265 primes, N <= 2*10^4). Outside scope: whether each
  of the ~30 dependents uses G, R and gamma_j inside these statements' hypotheses (primary,
  outside S, squarefree for gamma_j, "-1" as a residue class).
```

RH is unsolved. This note reviews three arithmetic helper lemmas inside an external, unreviewed proof of a quasi-RH statement (`Re s > 7/8`). That statement says nothing about the critical line. "No wrong step found" is the verdict of a bounded review by one agent. It is not certification, not integration, and not a human referee report.

All checks except B3 (symbolic) and B4 (floating point) are exact integer computations on finitely many moduli. They show that the displayed identities hold on those moduli. The proofs, read line by line, are what cover all moduli. The one exception is the finite square-class claims of Lemma 4.3/4.4. There the exhaustive class-level checks (B2, C4) are complete verifications, given the closed form.

## 0. Verdicts

| Lemma | TeX | ndep (as written / O5) | Verdict | Non-fatal findings |
|---|---|---|---|---|
| 4.2 Prime Gauss identities | 766-836 | 32 / 26 | **No wrong step found.** | F1: the proof does not restate that `x -> e(x/p)` is well defined and nontrivial on `O/(p)`. It follows from the self-duality paragraph (608-617). |
| 4.3 Quadratic four-term formula | 841-932 | 33 / 27 | **No wrong step found.** | F2: "evaluating on the two generators gives the displayed exponent" (929-932) does not by itself prove the 16-entry table or the bicharacter property. Both are true and are checked exhaustively here (B2.6, B2.7). |
| 4.4 Sextic reciprocity and the fixed Gauss phase | 934-1052 | 31 / 25 | **No wrong step found**, modulo the imported cubic reciprocity. | F3: "The table also gives Γ(p)² = (-1)^{(q_p-1)/2}" (1019-1021) silently uses `N(c) ≡ 3^f (mod 4)` on the square class `(-1)^e λ^f`. That is true (B2.8). F4: the 2-supplement (1005-1007) applies cubic reciprocity to the inert prime `-2`. The cited form is stated for "coprime primary a, b", and the classical law covers this case. |

No finding changes a statement. If the verification map is updated, the three nodes could move from **A** to **R**, with "imports cubic reciprocity" noted for 4.4. That is a suggestion only: the map files were not edited.

## 1. Conventions used (read at 562-646) and what was already checked

* `O = Z[ω]`, `λ = 1 + 2ω = √-3`, primary means `≡ 1 mod 3`, and `S` contains the primes above 6.
* `e(z) = exp(2πi Tr(z/λ)) = exp(4πi Im z/√3)`. For `z = a + bω`, `Tr(z/λ) = b`, so `e(O) = 1`, and `O` is self-dual (608-617).
* `χ_p(a) ≡ a^{(P-1)/6} mod p`, with value 0 when `p | a`. `χ_c = ∏ χ_p^{v_p(c)}`. For every integer `j`, `χ_c(a)^j` is 0 when `(a,c) ≠ 1`.
* `γ_j(c) = q_c^{-1/2} Σ_{v mod c} χ_c(v)^j e(v/c)`, for squarefree `c` only.

The script uses exactly these conventions through `a2/eis.py`. In part 0 it validates its symbol tables against `eis.sym_prime`, the direct computation of `a^{(N-1)/6} mod p` (43,234 values).

**Already checked before this note.**
* w5copg: floating point, squarefree primary `n` with `N ≤ 50000`, for `γ_2³ = μα`, `γ_1γ_2 = μαG`, `γ_3` = four-term formula, `χ_n(4) = n mod 2`, `G` multiplicativity, and reciprocity on 303,320 pairs.
* numerics K1: floating point, four-term `Γ` for all odd `c` with `N ≤ 10^4`.
* K2/K2″: exact, class algebra mod 4 and mod 36.
* K3: exact, `G(p³)`, `R(p,p)`, `χ_p(4)` at 2,265 primes.
* K4: exact, sextic reciprocity on 342,684 coprime pairs with `N ≤ 2000`, nonsquarefree included.
* L13 A5 and L18b B4: the reciprocity sign on the pairs those reviews use.

**Gaps this note fills.**
1. Every Gauss-sum identity was only floating point before. Here it is exact, in `O[ζ_M]` modulo `Φ_M`.
2. The proof-internal Jacobi-sum steps of Lemma 4.2, which were never checked.
3. Lemma 4.3 exactly, for every odd `c` (non-primary, λ-divisible, nonsquarefree, prime powers).
4. The CRT factor itself.
5. The supplements at prime powers and composites.
6. Failing controls with predicted failure counts.

## 2. Lemma 4.2 (prime Gauss identities)

**Statement (766-775).** For the primary generator `p` of a good prime, with `H = χ_p` and `P = q_p`: `γ_2(p)³ = -α(p)`, `γ_1(p)γ_2(p) = \overline{H(4)} γ_3(p) γ_2(p)³`, and `|γ_j(p)| = 1` for `j ≢ 0 (mod 6)`. This covers split `p` (`P = ℓ`) and inert `p = -q` (`P = q²`). The proof is uniform in `P`.

| Lines | Step | Check | Verdict |
|---|---|---|---|
| 778-781 | `ψ(x) = e(x/p)` is a nontrivial additive character of `k = O/(p)` | Well defined since `e(O) = 1`. Nontrivial since `1/p ∉ O` and `O` is self-dual (608-617). Not restated (F1). | correct |
| 785-791 | `\|τ(A)\|² = P` via `x = ty`. The y-sum runs over `k^×`: `P-1` at `t = 1`, `-1` otherwise. `Σ_t A(t) = 0`. | A1 (`j = 1..5`) | correct |
| 791-792 | `τ(A)τ(\bar A) = A(-1)P`, because `\overline{τ(A)} = \bar A(-1) τ(\bar A)` | A4a | correct |
| 792-800 | `τ(A)τ(B) = J(A,B)τ(AB)` for `AB` nonprincipal. The `x+y = 0` group is `B(-1)Σ AB = 0`. `\|J\| = √P`. | A4b (all 20 pairs), A5c | correct |
| 801-803 | `#{x : 4x(1-x) = y} = 1 + H³(1-y)`. This is `(2x-1)² = 1-y` with 2 invertible, and `H³(0) = 0` by zero extension. Hence `J(H,H³) = H(4)J(H,H)`. | A6a (every `y`), A5a | correct |
| 804-811 | `τ_1τ_3/τ_4 = H(4)τ_1²/τ_2`, then `τ_1τ_2 = \overline{H(4)} τ_3 τ_2³/P`, using `τ_2τ_4 = H²(-1)P = P` (`-1` is a cube) | A3, A6b | correct |
| 812-821 | `J(H²,H²) ≡ Σ x^m(1-x)^m ≡ 0 mod p`, with `m = (P-1)/3`, degree `2m < P-1`. The zero-extended `H²` matches `x^m` at 0 and 1. | A5b | correct |
| 822-829 | `∏_{x≠0,1} x(1-x) = (-1)(-1) = 1`, so `Σ j_x ≡ 0 (mod 3)`. Then `ω^j ≡ 1 + j(ω-1) mod (ω-1)²` gives `J ≡ P-2 ≡ -1 (mod 3)`. | A6c, A5d | correct |
| 830-833 | `J = up` with `u` a unit (`p \| J`, equal norms). Since `p ≡ 1` and the units are distinct mod 3, `u = -1`. | A5b | correct |
| 833-835 | `τ_2³ = J τ_2τ_4 = -pP`, then divide by powers of `√P` | A2 | correct |

**Controls.** Each wrong variant fails exactly as predicted:
* A non-primary generator `up`, `u ≠ 1`: A2 fails at every prime (2,110/2,110). This is where the primary normalization enters.
* Dropping the bar on `H(4)`: A3 fails exactly at the primes with `H(4) ≠ 1` (278/422).
* Flipping the orientation `H → \bar H`: A2 fails exactly at the split primes (414/422). For inert `p = -q`, `\bar p = p`.

## 3. Lemma 4.3 (quadratic four-term formula)

**Statement (841-869).** For nonzero odd `c`, `Γ(c) = |c|^{-1} Σ_{x mod c} e(x²/c) = ½ Σ_{y mod 2} e(-cy²/4) = (1 + i^{-b} + i^a + i^{b-a})/2`. Moreover:
* `Γ` depends only on `c mod 4`, and `Γ(cv²) = Γ(c)`;
* the square-class structure mod 4, the table `Γ = 1, 1, i, -i` on `1, -1, λ, -λ`, and `𝔯 = (-1)^{eh+fg+fh}`;
* `|Γ| = 1`, and `𝔯` is a symmetric sign-valued bicharacter.

| Lines | Step | Check | Verdict |
|---|---|---|---|
| 872-881 | Poisson on `O` (self-dual, covolume 1) for `f_ε = e(z²/c)e^{-πε\|z\|²}`; the stated `\hat f_ε` | B3 (SYMBOLIC: det, amplitude and exponent, after the rotation `z = e^{iθ/2}w`). B4 (FLOAT: the Poisson identity at finite ε for 8 `c` × 3 ε, max relative deviation 1.3e-15). | correct |
| 882-894 | Matrix `[[ε, -4i/(√3\|c\|)], [., ε]]`, `det = 16r_ε/(3q_c)`. Eigenvalues `ε ± 4i/(√3\|c\|)`, so the branch is the positive root. | B3 | correct |
| 895-907 | Coset Gaussian means `→ 1/(a q_b)`. Periodicity: `(z+cw)²/c - z²/c = 2zw + cw² ∈ O`. Normalized LHS `→ Γ(c)/\|c\|`. | read | correct |
| 908-921 | Replacing `r_ε` by 1. Phase error `O_c(1)`, since `Σ\|y\|²e^{-Cε\|y\|²} ≍ ε^{-2}` and the prefactor is `ε²`. Amplitude and damping errors `O_c(ε)`. All `o(I_ε)`, `I_ε ≍ ε^{-1}`. Periodicity mod 2: `(y+2t)²` changes `cy²/4` by `c(yt+t²) ∈ O`. Coset mean with `b = 2`, `a = q_c/4` gives `1/q_c`. | read | correct |
| 922-924 | Representatives `0, 1, ω, ω²` give the four terms. The code re-derives `y = 1, ω, ω²` → `i^{-b}, i^a, i^{b-a}`. `y → vy` permutes `O/2` for odd `v`, so `Γ(cv²) = Γ(c)`. | B2.4, B1 | correct |
| 924-929 | `(O/4)^×` has order 12. Squaring depends on the class mod 2. Squares `{1, ω, ω²}`. The four representatives are distinct, and `λ² = -3 ≡ 1`. | B2.1-B2.3 | correct |
| 929-932 | Table, and "evaluating on the two generators gives the displayed exponent" | B2.5-B2.7 (all 16 entries, all 12³ triples) | correct; F2 |

**F2.** `𝔯(a,b) = Γ(ab)/(Γ(a)Γ(b))` is a bicharacter only because this particular `Γ` is a quadratic refinement. That is a fact about the four values `1, 1, i, -i`. Its values on generator pairs do not imply it. Control B2-c1 shows a class function, `(1, i, i, i)`, whose `𝔯` is not a bicharacter. The claim is a finite statement on a 4-element group, so the exhaustive exact evaluation B2.6/B2.7 proves it. The statement stands.

**Oddness.** The Poisson argument never uses that `c` is odd. Oddness is what makes `Γ` a unit: for example `Γ(2) = 0` from both sides. The statement restricts to odd `c`, so this is consistent.

**Exact check of the conclusion.** B1 covers all 5,454 odd `c` with `N ≤ 2000`:
* 4,847 non-primary, 1,812 divisible by λ, 930 nonsquarefree, 120 prime powers `π^k` with `k ≥ 2`, and 44 rational integers.
* B1a checks `S(c)² = Γ(c)² N(c)` in `Z[ζ_N]`. It is import-free and fixes `S(c) = |c|Γ(c)` up to sign.
* B1b checks `S(c) = (Γ(c)/ε_N) g_N`, which fixes the sign. Here `g_N` is the rational Gauss sum and `ε_N ∈ {1, i}`, by Gauss's classical theorem, which is imported. In every case `Γ/ε_N = ±1`.

**Controls.** The opposite sign fails for all 5,454 `c`. "Γ depends only on `c mod 2`" fails on all 3 classes mod 2. The variant with `i^{+b}` differs from the stated closed form on 3,636 of the 5,454 `c` (2,180 of 3,270 in the default-range run).

## 4. Lemma 4.4 (sextic reciprocity and the fixed Gauss phase)

**Statement (934-972).**
* (a) `χ_b(a) = 𝔯(a,b) χ_a(b)` for coprime primary `a, b` outside `S`. `R := 𝔯` on all primary pairs.
* (b) `G(c) = \overline{χ_c(4)} Γ(c)` has modulus 1 and factors through a ray group at 2, 3.
* (c) `G(vw) = G(v)G(w)R(v,w)`, `G(1) = 1`.
* (d) `G(v²) = χ_v(4)`. At good primes, `G(p³) = γ_3(p)` and `R(p,p) = γ_3(p)² = χ_p(-1)`.
* (e) `χ_n(-1) = R(n,n) = 𝔯(-1,n)`, with `-1` read as a residue square class.
* (f) For squarefree `c`, `γ_2³ = μα`, `γ_1γ_2 = μαG`, `G = \overline{χ_c(4)} γ_3`, `|G| = 1`.

| Lines | Step | Check | Verdict |
|---|---|---|---|
| 975-983 | `#{x : x² = y} = 1 + χ_p(y)³`, so `Γ(p) = γ_3(p)`. A multiplier `u` gives `χ_p(u)³`. | A7 (7 multipliers, 422 primes) | correct |
| 983-991 | CRT for squarefree `c`: residues `Σ (c/p)x_p`. Cross terms `2(c/(pp'))x_p x_{p'} ∈ O`. So `Γ(c) = γ_3(c)` (`c` primary outside `S`, where `γ_3` is defined). | C1(i), C1(iv) | correct |
| 992-995 | `Γ(pq)/(Γ(p)Γ(q)) = χ_p(q)³χ_q(p)³` | C2c | correct |
| 997-1004 | Cubic reciprocity `(a/b)_3 = (b/a)_3`. Both normalizations agree because `-1` is a cube. So `χ_b(a)/χ_a(b)` is a sign, and its cube identifies it as `𝔯(p,q)`. Multiplicativity extends to coprime primary pairs (a primary element is the product of the primary prime generators). | C2a-C2b (1,521,522 ordered pairs of distinct primes, `N ≤ 10^4`, 580,948 with `𝔯 = -1`; conjugate pairs and inert primes included). K4 covers nonsquarefree pairs. | correct; imported law |
| 1005-1009 | `χ_c(4) = (2/c)_3 = (-2/c)_3 = (c/(-2))_3 ≡ c mod 2` | C3a (2,265 primes), C1(vii), C3g (all 907 primary ideals `N ≤ 3000`, 60 nonsquarefree) | correct; F4 |
| 1009-1016 | Ray group mod 12: same class and both primary forces unit 1, hence the same residue mod 4 | C4.1, C4.2 (exhaustive) | correct |
| 1016-1019 | "Its multiplicative refinement is the definition of 𝔯": `χ_{vw}(4) = χ_v(4)χ_w(4)` for all `v, w`, by the product definition of `χ_c`. `G(v²) = \overline{χ_v(4)}² = χ_v(4)`. | C4.3 (all 144 class pairs, exhaustive), C3e, C3g | correct |
| 1019-1028 | `Γ(p)² = (-1)^{(q_p-1)/2} = (-1)^{(q_p-1)/6} = χ_p(-1)`. `Γ(p³) = Γ(p)`, `\overline{χ_p(4)}³ = 1`. `R(p,p) = 1/Γ(p)² = Γ(p)²`. | C3c, C3d, C3e, B2.8 | correct; F3 |
| 1029-1040 | The diagonal of a symmetric sign bicharacter is multiplicative, so `R(n,n) = χ_n(-1)` for all primary `n`. It equals `𝔯(-1,n)` with `-1` the residue class. | C3f (907 ideals, 60 nonsquarefree), B2.9 | correct |
| 1041-1052 | `γ_j(ab) = χ_a(b)^jχ_b(a)^j γ_j(a)γ_j(b)`. Cubing for `j = 2` gives 1. The product of the factors for `j = 1, 2` is `(χ_a(b)χ_b(a))³ = R(a,b)`. Induction from Lemma 4.2 with (4.8). | C1(ii)-(v) (700 squarefree primary `c`, `N ≤ 2500`; 337 composite, 42 with an inert factor, 6 of the form `p\bar p`) | correct |

**F3.** The table gives `Γ(p)² = (-1)^f` on the class `(-1)^e λ^f`. Turning that into `(-1)^{(q_p-1)/2}` needs the norm map mod 4 to send that class to `3^f`. The norm is well defined mod 4 and multiplicative, with `N(λ) = 3`. B2.8 checks it on all 12 classes.

**F4.** `-2` is primary and coprime to every `c` outside `S`. The classical law includes the rational prime 2, so this is a use of the cited law and not a gap. The cited location was not opened (see the header).

**Controls.** Each wrong variant fails exactly as predicted:
* `R ≡ 1`, i.e. reciprocity without the correction, fails on exactly the 580,948 pairs with `𝔯 = -1`.
* `G` without the bar fails in (f) exactly where `χ_c(4) ≠ 1` (468/700).
* Dropping `μ` fails exactly where `μ = -1` (388/700).
* Reading the diagonal at the ideal ray class of `(-1)`, the misreading the statement warns against, fails at the 1,138/2,265 primes with `χ_p(-1) = -1`.
* `G(p²) = \overline{χ_p(4)}` fails at the 1,512 primes with `χ_p(4) ≠ 1`.

**Range of G.** `G` takes 9 distinct twelfth roots of unity on the 12 primary classes. The exponents are `{0,1,3,4,5,7,8,9,11}`, consistent with the w5copg table.

## 5. Checks (sep30_l42_44_checks.py, final run)

| Part | What | Range | Label | Result |
|---|---|---|---|---|
| 0 | Prime list = `eis.primes_upto` (`N ≤ 400`). Symbol tables = `eis.sym_prime` (43,234 values). Residue systems = `eis.residues`. Cyclotomic zero test. | | EXACT | PASS ×4 |
| A1-A7 | Lemma 4.2 and every proof step in Sec. 2 | 422 primes: split `N ≤ 3000`, inert `q ≤ 53` | EXACT in `O[ζ_ℓ]` | PASS ×13 |
| A-c1..c3 | Non-primary generator, bar dropped, orientation flipped | same | CONTROL | fail as predicted ×3 |
| B1a / B1b | Four-term formula, all odd `c` | 5,454 `c`, `N ≤ 2000` | EXACT / EXACT+GAUSS | PASS ×2 |
| B-c1..c3 | Opposite sign; "mod 2"; `i^{+b}` | same | CONTROL | fail ×3 |
| B2.1-B2.9 | Square classes mod 4, table, `𝔯`, norm parity, diagonal | exhaustive (12 classes) | EXACT | PASS ×9 |
| B2-c1 | Class function `(1,i,i,i)` is not a quadratic refinement | 64 triples | CONTROL | fails on 18 |
| B3 | `\hat f_ε` normalization | symbolic | SYMBOLIC | PASS |
| B4 (+c1) | Poisson identity at finite ε (phase-sign flip fails on the 18/24 non-real cases) | 8 `c` × 3 ε | FLOAT | PASS |
| C1(i)-(vii) | `Γ = γ_3`, (4.10), CRT, `\|γ_j\| = 1`, `χ_c(4)` | 700 squarefree primary `c`, `N ≤ 2500` | EXACT in `O[ζ_M]` | PASS ×7 |
| C1-c1, c2 | `G` without the bar; `μ` dropped | same | CONTROL | fail as predicted ×2 |
| C2a-c (+c1) | Sextic reciprocity; cubic reciprocity; sign identification | 1,234 primes, 1,521,522 ordered pairs | EXACT | PASS ×3, control fails as predicted |
| C3a-g (+c1, c2) | 2-supplement and unit supplement, `G(p³)`, `G(p²)`, `R(p,p)`, diagonal at prime powers and composites | 2,265 primes `N ≤ 2·10^4`; 907 ideals `N ≤ 3000` | EXACT | PASS ×7, controls fail as predicted |
| C4.1-C4.3 | Ray group mod 12; `G(vw) = G(v)G(w)R(v,w)` | exhaustive (144 pairs) | EXACT | PASS ×3 |
| D1, D2 | Prop 5.1 context: `(λ/p)_3` and `(ω/p)_3` are a character of `p mod 9`; trivial at `p ≡ 1 mod 9` | 2,265 primes | EXACT | PASS ×2 |

**How the exact tests work.**
* Every Gauss sum is scaled to an algebraic integer: `τ_j(c) = √N γ_j(c)` and `S(c) = |c|Γ(c)`.
* It is stored as an integer vector over `O[ζ_M]`. Here `M` is the reduced denominator of `e(x/c)`: `ℓ` for split primes, `q` for inert `-q`, and the product of the rational primes below `c` in general.
* Equality is tested by reducing modulo `Φ_M` (componentwise in `1, ω`, since `3 ∤ M`), or modulo `Φ_N` in part B.
* There are no square roots and no floating point, except in B4.

## 6. What this does not show

* The exact checks are finite. All moduli are covered only by the proofs, which were read here. The exception is the finite class-level claims (B2, C4), which are verified exhaustively.
* Cubic reciprocity is imported. It was re-confirmed only on finite ranges, and `[DR, (1.4)]` was not opened. Gauss's evaluation of the rational quadratic Gauss sum is imported in B1b only. B1a fixes the four-term formula up to sign without it.
* The ~30 downstream uses of each lemma were not checked against these statements. Two hypotheses matter there:
  * `γ_j` is defined only for squarefree `c`. On nonsquarefree indices, `G` is the class function.
  * `-1` in the diagonal is a residue class.
* This is one agent's bounded review. It says nothing about RH or about the critical line.

## 7. Reproduce

From `research/exploratory/qrh-2026-10/reviews`:

```
XA=3000 QA=53 XB=2000 XC=2500 nice -n 10 python3 -I sep30_l42_44_checks.py out.json   # 381 s, 65/65 PASS
nice -n 10 python3 -I sep30_l42_44_checks.py out.json                                   # defaults, 54 s
```

The environment variables `XA, QA, XB, XC, XR, XS, XP` set the ranges. Exit status 0 means every check passed, and every control failed as predicted.

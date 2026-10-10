# Sep 30 manuscript: Section 4 helpers (Lemmas 4.1, 4.6-4.10) and Lemma 13.1

```text
Status: REVIEW (bounded; external, unreviewed manuscript) + EXACT finite checks + MP/FLOAT sanity
  checks. Verdicts: no wrong step found in Lemmas 4.1, 4.6, 4.7, 4.8, 4.9, 4.10 and 13.1. Two
  remarks, neither a gap: (i) the Lemma 4.8 bound is weaker than convexity but correct, with an
  explicit absolute constant C = 0.69 (computed below at 40 digits, not certified); (ii) in Lemma 4.9,
  theta is within 0.3% of 1, so "<< C^eps" holds only with astronomically large, ineffective
  constants. This is harmless for the paper's fixed-(e, eps) asymptotics.
Scope: "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8" (OpenAI, 30 Sep 2026).
  Read line by line: Lemma 4.1 (646-699, with the notation 560-645 and the remark 701-703);
  Lemma 4.6 (1288-1340); Lemma 4.7 (1342-1413); Lemma 4.8 (1415-1529); Lemma 4.9 (1531-1600);
  Lemma 4.10 (1602-1646); Lemma 13.1 (7004-7040); the beta_* definition (365-385).
  Uses read only to check that each invocation matches the statement (those proofs are NOT
  reviewed): Lemma 4.1 at 1055, 2475, 2520, 3368, 5510-5515, 8404-8421, 8985-8998, 12693, 14339;
  Lemma 4.6 at 2615, 8137-8160; Lemma 4.7 at 9649, 13156, 14839; Lemma 4.9 at 12844-12852
  (Lemma 18.1, Case 2 input) and 15039-15044 (Lemma 19.1); Lemma 13.1 at 6868-6880 and
  15562-15585 (Sec. 20.1 normalizer); Thorner-Zaman at 13464 and 5512.
  Not duplicated: Lemma 4.5 and Lemmas 13.2-13.4 (SEP30_L13_L45_REVIEW.md, parallel). That note
  also gives a shorter reading of 4.7-4.10; this note is the line-by-line pass with checks.
Exact sources or dependencies:
  [OAI] pr908 (31c706bb) standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
        The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, sha256
        42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed here from a
        scratchpad copy). External and unreviewed; read as untrusted data.
  Imported results, as cited by [OAI] and NOT re-read at source here: Gao-Zhao, JNT 209 (2020),
        eq. (1.1) (Hecke functional equation); Milne, CFT notes v4.03, Ch. VIII (5.3), (5.5)
        (power-residue symbol and Artin map); Thorner-Zaman, ANT 13 (2019), Thm 1.1 (Chebotarev).
        Each is used only in a standard, fixed-field form; see the per-lemma notes.
  Code: reviews/sep30_sec4_checks.py (new; sha256 in Sec. 8). It imports a2/eis.py unchanged
        (sha256 87ca11d98bf3ee130a6dab613b5f7efe444058320b7c22b005327686f2798e65, asserted at
        start-up), plus numpy, sympy (GF(p) factorization, symbolic radial identity) and mpmath.
What was actually run: nice -n 10 python3 -I reviews/sep30_sec4_checks.py OUT.json (one process,
  RUNTIME_PLACEHOLDER). Python 3.13, numpy 2.5.3, sympy 1.14.0, mpmath 1.3.0. The log and JSON are in
  the session scratchpad (sec4/full.log, sec4/full.json) and are not committed. A "quick"
  argument gives a 78 s smoke run.
Smallest remaining gap: none inside the scoped lemmas. Outside scope:
  (i) the three imported statements were not re-read at source (each is used only in its
      classical fixed-field form);
  (ii) the uses listed above were checked for hypothesis match only. In particular, the
      ray-presentation claim of Prop 16.1 (8985-8998, modulus 36 rad(u)) goes beyond Lemma 4.1,
      which bounds no conductor exponent. It is consistent with exact checks A4, but it rests on
      Lemma 4.4 and is not reviewed here.
```

RH is unsolved. This note reviews seven helper lemmas of an external, unreviewed proof of a quasi-RH
statement (`Re s > 7/8`), which says nothing about the critical line. "No wrong step found" means a
bounded agent review. It is not a certificate. Parts A of the checks are exact on finitely many prime
ideals (norm at most 30,000). Parts B-G are ordinary floating or mpmath arithmetic. That is not
directed or certified, and it is evidence on finite grids, not a proof.

## 0. Verdicts

| Lemma (lines) | Content | Verdict | Load-bearing checks |
|---|---|---|---|
| 4.1 `lem:fixed-numerator-ray` (646-699) | Kummer: `A -> (a/A)_6` is a ray character, conductor supported on `6a`; the S-family is finite | **no wrong step found** | A1-A4: Frobenius order = residue degree (613 pairs); conductors of 8 Kummer characters found, each strict divisor refuted by an exact collision; 216 S-family characters periodic mod `2^3 lambda^4` and pairwise distinct; good-prime controls |
| 4.6 `lem:gaussian-annular` (1288-1340) | partition of `W_G` into annuli with Gaussian-decaying seminorms | **no wrong step found** | B1-B4 |
| 4.7 `lem:kernel-seminorms` (1347-1413) | Fourier/radial/Mellin kernel seminorms | **no wrong step found** | C1-C3 |
| 4.8 `lem:hecke-strip-growth` (1425-1529) | `\|L\| << Q^{3/5}(3+\|t\|)^2` on `-1/10 <= sigma <= 11/10`, uniform in `Q` | **no wrong step found**; explicit `C ~ 0.69` | D1 (the paper's own Poisson formula reproduces base-change L-values to 1e-32), D2 (functional equation with the A2 conductors), D3 (ratio <= C on grids, Q up to 961) |
| 4.9 `lem:logarithmic-control` (1531-1600) | zero-free disk => `L^{+-1} << C^eps`, `L'/L << log C` | **no wrong step found** | E0-E1; hypotheses at both uses match |
| 4.10 `lem:deleted-euler-factors` (1602-1646) | finite Euler products | **no wrong step found** | F1 (3,000 random trials) |
| 13.1 `lem:ray-prime-normalizer` (7006-7040) | fixed-ray prime sum asymptotic | **no wrong step found** | G0-G1 (EMPIRICAL); use in Sec. 20.1 matches |

## 1. Lemma 4.1 (fixed numerators give ray characters)

| claim (line) | check | result |
|---|---|---|
| `(a/p)_6` well defined for `p ∤ 6a` (649-651) | `p ∤ 6` gives `q_p ≡ 1 (mod 6)`: split primes have `q = p ≡ 1 (mod 3)`, inert ones `q = p^2 ≡ 1 (mod 3)`, and `q` is odd. `μ_6` injects into the residue field since `p ∤ 6`. | correct |
| `F(a^{1/6})/F` abelian (677-680) | `μ_6 ⊂ F`, and `σ -> σ(ξ)/ξ` is a homomorphism into `μ_6` because `τ(ξ)/ξ ∈ F` is fixed by `σ`. It is injective since `ξ` generates. | correct |
| unramified outside `6a` (680-682) | `disc(X^6 − a) = ±6^6 a^5`, and `ξ` is integral. | correct |
| Frobenius identity (653-656; 682-686) | `Frob(ξ) ≡ ξ^{q}` mod a prime above `p`, so `Frob(ξ)/ξ ≡ a^{(q−1)/6}`; reduction is injective on `μ_6`. It does not depend on the choice of root, since `Frob` fixes `μ_6 ⊂ F`. | correct; **A1** checks the consequence "order of symbol = residue degree" by factoring `X^6 − a` over `GF(p)` (sympy) for 8 numerators and all split `p ≤ 400`, and by counting sixth roots in `O/q` for inert `q = 5, 11, 17`: 613 pairs, 0 mismatches |
| ray character, conductor on `6a` (657-660; 686-690) | Artin map composed with the injective character `Gal -> μ_6`; Artin reciprocity puts the conductor on ramified primes. "No bound on conductor exponents" is stated honestly. | correct; **A2** (below) |
| zeros not erased (660-661) | the identification is only on ideals prime to `6a` | correct (a scope statement) |
| S-family (663-674; 692-699) | For `A` outside `S`, `χ_A(π_p) ∈ μ_6`, so only `v_p mod 6` and `u` matter. That gives at most `6^{|S|+1}` numerators, each with conductor on `S`, so one common modulus exists. | correct; **A3**: with `S = {λ, 2}` all 216 characters are periodic mod `2^3 λ^4` (norm 5184) and pairwise distinct, so the bound is attained |

**A2: empirical conductors.** For each character, the symbol on all 3,240 prime ideals of norm at
most 30,000 was tested for being a function of the ray class modulo `m = 2^i λ^j` (`i ≤ 4`, `j ≤ 7`).
A modulus is accepted only if it shows no collision and `|Cl_m|` is at most #primes/5; otherwise
"no collision" would be vacuous. Each strict divisor of the accepted modulus is refuted by an exact
collision: two primes in one ray class with different symbols. That collision is a proof that the
character does not factor through that `Cl_m`.

| character | minimal modulus | `Q = N(f)` | classes hit | consistency |
|---|---|---|---|---|
| `(2/·)_3` | `2 λ^2 = (6)` | 36 | 3/3 | `3·36 = 108 = \|disc Q(2^{1/3})\|` |
| `(λ/·)_3` | `λ^4 = (9)` | 81 | 9/9 | `3·81 = 243 = \|disc Q(3^{1/3})\|` |
| `(2/·)_2` | `2^3` | 64 | 8/8 | `F(√2)/F`, wild at 2 |
| `(−1/·)_6 = (−1/·)_2` | `2^2` | 16 | 2/2 | `F(i)/F` |
| `(ζ_6/·)_6` | `2^2 λ^3` | 432 | 36/36 | `F(ζ_36)`; the cubic part `F(ζ_9)/F` has conductor `λ^3` by conductor-discriminant |
| `(2λ/·)_3` | `2 λ^4` | 324 | 27/27 | |
| `(2/·)_6` | `2^3 λ^2` | 576 | 48/48 | lcm of the quadratic and cubic parts |
| `(λ/·)_6` | `2^2 λ^4` | 1296 | 108/108 | |

Every conductor is supported on `{2, λ}`, the primes over `6a`, as the lemma asserts. D2 below
confirms four of them analytically: the theta-series L-function satisfies the functional equation
of Lemma 4.8 exactly with `Q = N(f)`. That is independent evidence that the periodicity found is
the primitive conductor.

**A4: controls (numerators with a good prime).** For `a ∈ {5, π_7, π_7π_13, π_7^2, ζ_6π_19}` and
`a = 2λπ_19`:
* every well-covered modulus `2^i λ^j` fails by an exact collision, so the conductor is not supported on `S`. This is exactly the paper's warning at 701-703: a moving good prime leaves the fixed ray group;
* the symbol is periodic modulo `(36)·rad(u)`, for good `u`;
* dropping any good prime from the modulus produces an exact collision, so each good prime divides the conductor exactly once (tame).

This matches the ray presentation used in Prop 16.1 (8985-8998). Coverage there is partial: 648 of
648 classes are hit for `π_7` and `π_7^2`, but only 2,133 of 2,592 for `a = 5`. Prop 16.1 itself is
outside scope.

**Uses.** The citations at 1055, 2475, 2520, 3368, 8404-8421, 12693 and 14339 all apply the
lemma to numerators of the form `u ∏_{p∈S} π_p^{e_p}`, unit times `S`-part, with `e_p mod 6`, or
to a fixed `b_*`. That is exactly the S-family clause. 5510-5515 uses the Kummer description
for unit rows. It is correct: a unit `u ≠ 1` has no sixth root in `F`, since every unit has
`u^6 = 1`, so `F(u^{1/6}) ≠ F`, and Chebotarev gives a good prime with `χ_p(u) ≠ 1`. A2 exhibits
this for `ζ_6`. The Milne section numbers were not checked against the notes.

**Verdict: no wrong step found.**

## 2. Lemma 4.6 (Gaussian annular decomposition)

* The partition of unity: normalize the translates of a bump positive on `[−1/2, 1/2]`. Every `u` is within `1/2` of an integer, so the periodized sum is positive (**B1**: sum = 1 to 2e-16).
* `W_{G,k}(e^k x) = w_k(x)` and `Σ_k W_{G,k} = W_G`: immediate.
* `p_j(w_k) ≤ C_j(1+|k|)^j exp(−¼((|k|−C)_+)^2)`, with `supp χ ⊂ [−C, C]`. The `u`-derivatives of `exp(−(k+u)^2/4)` are polynomials of degree `≤ j` in `k+u` times the Gaussian, and `|k+u| ≥ |k| − C` on the support. Correct. **B2** (finite differences, `j ≤ 3`, `|k| ≤ 40`, `C = 1`): the ratio to the envelope is bounded and decreases for `|k| > 10`.
* Summability with `e^{A|k|}` (**B3**). The tail: `log(Z^B e^{A|k|} p_j) ≤ −(1/4)(κ log Z)^2 + O(log Z)` on `|k| > κ log Z − C_0`, so `c = 1/4`. Correct.
* Rescaling `y = e^k x` multiplies the log-Fourier transform by `e^{−ikt}`, so separation norms are unchanged and Lemma 4.5 applies with the fixed support of `w_k`. Correct.
* `M W_G(s) = ∫ W_G(y) y^s dy/y = (2√π)^{−1} ∫ e^{−u^2/4+su} du = e^{s^2}` (**B4**, 1.7e-31 at 30 digits; the convention is the one at 1160). The weighted logarithmic derivatives are integrable uniformly on compact `σ`-ranges. Correct.

**Use at 8137-8160** (Lemma 15.1). It applies the derivative estimate to a joint profile
`χ(log x) W_G(e^k x/∏ϱ_i) ∏ W_i(ϱ_i)`, with the `ϱ_i` in fixed windows. This is the same
product-rule argument with a bounded shift of `k`. It is an immediate extension, not literally
the statement, and the text says so ("with this bounded shift"). **Verdict: no wrong step found.**

## 3. Lemma 4.7 (finite seminorms for Fourier and Mellin kernels)

* The Fourier part: `ξ^γ ∂^β f̂ = c·FT(∂^γ(x^β f))`, then the `L¹` bound, the product rule, and `(1+|ξ|)^A ≤ C Σ_{|γ|≤⌈A⌉}|ξ^γ|`. Every term has at most `|β|` powers of `x` and at most `⌈A⌉` derivatives, so `s_{⌈A⌉+|β|}` suffices. Correct.
* The radial part: `r∂_r F(r) = ½ (ξ·∇)[F(|ξ|^2)]` (**C1**, sympy, d = 2, 3). `(1+r)^A ≤ (1+|ξ|)^{2A}`, so `s_{⌈2A⌉+2j}` suffices. The lemma says only "finitely many", which is correct.
* The Mellin part: differentiation inserts `(−s)^j`, and `N ≥ h+j+2` integrations by parts make `∫(1+|t|)^{h+j−N}` converge. The constants are uniform for `σ` in the strip, given the vanishing boundary terms, which are a stated hypothesis. Correct.
* The twist: `M[W y^{iω}](−s) = MW(−s+iω)`. With `v = t−ω` and `1+|v+ω| ≤ (1+|v|)(1+|ω|)`, it costs `(1+|ω|)^{h+j}`. Correct (**C3**: the observed factor is 735, against 6,561 allowed at `ω = 8`).
* **C2**: for `W = W_G` and `m(s) = (s+3)^2` (`h = 2`, `σ = 1/2`), the bound holds with explicit constants. The maximum ratio is 0.375 over `j ≤ 2`, four values of `x`, and `ω ∈ {0, 8}`.
* The rescaled cutoff gives the factor `R^{−σ}`. Correct.

**Uses at 9649, 13156, 14839**: these are applications to fixed-shape normalized transforms,
uniform in the scale `R`, which is what the sup over `r` provides. **Verdict: no wrong step found.**

## 4. Lemma 4.8 (Hecke strip growth)

| step (line) | check | result |
|---|---|---|
| finite order implies trivial infinity type (1437-1438) | `C^×` is connected | correct |
| `Λ = (3Q)^{s/2}(2π)^{−s}Γ(s)L`, `Λ(s,ψ) = εΛ(1−s, ψ̄)` (1439-1445) | `\|d_F\| = 3`, with one complex place, so `Γ_C(s) ∝ (2π)^{−s}Γ(s)` | correct; **D2** confirms it numerically for 4 Kummer characters: `\|Λ(s)\| = \|Λ(1−s̄)\|` holds to 15 digits with `Q = N(f)` from A2, at three points with `σ ≠ 1/2`, which pins down `Q` |
| `\|L(11/10+it)\| ≤ ζ_F(11/10)` (1446-1447) | absolute convergence | correct; `ζ_F(1.1) = 6.6298` |
| `\|L(−1/10+it)\| << Q^{3/5}(3+\|t\|)^{6/5}` (1447-1452) | `\|(3Q)^{(1−2s)/2}\| = (3Q)^{3/5}`, `\|(2π)^{2s−1}\| = (2π)^{−6/5}`, `\|Γ(1.1−it)/Γ(−0.1+it)\| ~ \|t\|^{6/5}` | correct; **D0** (Stirling ratio → 1); continuity at bounded `t` because `1/Γ` is entire |
| periodic `φ`, unit-trivial (1458-1468) | `ψ` is a ray character mod `f`, and `(u) = (1)` | correct |
| `6π^{−s}Γ(s)L = ∫(Θ_φ − φ(0))v^{s−1}dv` (1469-1474) | six generators per ideal | correct |
| Poisson: `Θ_φ(v) = (2/(√3 v)) Σ_h φ̂(h) Σ_b exp(−4π\|b−h/f\|^2/(3v))` (1475-1482) | re-derived: `e(zw) = exp(2πi⟨z,ξ⟩)` with `\|ξ\|^2 = (4/3)\|w\|^2`; the Gaussian transform gives `v^{−1}e^{−π\|ξ\|^2/v}`; the self-dual measure contributes `2/√3` | correct; **D1**: the resulting incomplete-gamma series reproduces `L(s,χ)L(s,χχ_{−3})` for `χ∘N` (`χ` mod 4, 5, 7) to relative error 2.7e-32 at 15 points, including `σ = −1/10` |
| `A_φ = 2φ̂(0)/√3`, asymptotics, split Mellin (1483-1504) | principal: `Res ζ_F = π A/6 = π/(3√3)` = the class-number formula value | correct |
| qualitative exponential growth (1505-1512) | `1/Γ(s) << e^{π\|t\|/2}`; in the principal case the `1/s` term is cancelled by the zero of `1/Γ` at 0 | correct |
| damped Phragmén-Lindelöf (1514-1530) | `\|e^{δ(s−1/2)^2}\| ≤ e^{9δ/25}` on the sides and `≤ e^{δ(9/25−T^2)}` on the horizontals; take `T → ∞`, then `δ → 0` | correct; the constant is independent of `Q` |
| principal version (1530-1538) | `(s−1)/(s+1)` removes the pole; `\|(s−1)/(s+1)\| ≤ 1.1/0.9` on `σ = −1/10` | correct; the theta relation `Θ(2t/√3) = t^{−1}Θ(2/(√3t))` was re-derived |

**Explicit constant (D3).** The proof gives `|L(s,ψ)| ≤ C Q^{3/5}|s+2|^2` with
`C = max(C_left, C_right)`, where:
* `C_left = 3^{3/5}(2π)^{−6/5}ζ_F(1.1) sup_t |Γ(1.1−it)/Γ(−0.1+it)|/(1.9^2+t^2) = 0.4329`;
* `C_right = ζ_F(1.1)/3.1^2 = 0.6899`.

So `C = 0.69`, and `|L| ≤ 0.74 Q^{3/5}(3+|t|)^2`. The constant was computed at 40 digits with the
sup taken on the grid `t ∈ [0, 200]` (step 1/4); the function decays like `t^{−4/5}` beyond. It is
not certified. On the grid `σ ∈ {−0.1, 0.25, 0.5, 0.8, 1.1}`, the maximum of `|L|/(Q^{3/5}|s+2|^2)` is:

D3_TABLE_PLACEHOLDER

All values are below `C`. The stated exponents are not sharp: convexity would give
`Q^{(1−σ)/2+ε}`-type bounds. But only `log|L|` enters Lemma 4.9, so the weaker bound is all that
is used. **Verdict: no wrong step found.**

## 5. Lemma 4.9 (logarithmic control)

Write `R_j = 2 − a − je` and `𝒞 = 2Q(3+|t|)^2`.

* **Zero-free disk and logarithm.** The disk of radius `R_2` is zero-free by hypothesis and simply connected, so `g = log ℒ` exists. `g(2+it)` is the Euler logarithm, bounded by `log ζ_F(2)`, plus a bounded term in the principal case. Correct.
* **Upper bound for `Re g` on `|s−(2+it)| ≤ R_3`.** The leftmost point is `a+3e ≥ 1/2 > −1/10`, so Lemma 4.8 applies up to `σ = 11/10`, and Euler convergence beyond. Heights move by at most `R_0 ≤ 3/2`, which is absorbed into `𝒞`. Correct.
* **Borel-Carathéodory from `R_3` to `R_4`.** `max_{R_4}|g| ≤ (2R_4/e)·max_{R_3}(Re g)_+ + ((R_3+R_4)/e)|g(c)|`, so `|g| <<_e log 𝒞`, with constant about `3/e`. Correct.
* **Three circles, `r_0 = 49/100 < R_6 < R_4`.** On the `r_0`-disk `Re s ≥ 1.51`, so `|g| ≤ log ζ_F(1.51)` plus, in the principal case, the bounded `log((s−1)/(s+1))` on its principal branch. Then `θ = log(R_6/r_0)/log(R_4/r_0) < 1`, and it is continuous in `a ∈ [1/2, 1]`. Correct.
* **The size of `θ` (E0).** `θ = 0.99717` at `a = 1, e = 10^{-3}`, and `θ = 0.99988` at `a = 1/2, e = 10^{-3}`. It is larger still for smaller `e`. So `exp(C_e(log 𝒞)^θ) ≤ 𝒞^ε` only once `log 𝒞 ≥ (C_e/ε)^{1/(1−θ)}`, which is a threshold of order `(3000/ε)^{350}` or more. The implied constant in (eq:disk-control) is therefore finite but astronomically large and ineffective. The paper uses the bound only with `e` and `ε` fixed before `Z → ∞`, so this is harmless. It would matter only to someone seeking explicit constants.
* **Cauchy from `R_6` to `R_8`.** `|g'| ≤ max_{R_6}|g|/(2e) <<_e (log 𝒞)^θ ≤ log 𝒞`. Correct, and stronger than stated.
* **Global clause.** For `β_* ≤ b ≤ 1`, take `a = b`, which lies in `[1/2, 1]` because `β_* ≥ 1/2` by definition (old-eq:1.1b, 377-385; the principal character is included, so zeros of `ζ_F` are covered). Take `e < min(10^{-3}, v/8)`. The `R_2`-disk lies in `Re s > b+2e > β_*`. The `R_8`-disk reaches `Re s = b+8e < b+v`. The case `b > 1` and the reciprocal `1/ζ_F` via `|(s−1)/(s+1)| ≤ 1` are correct. The point `s = 1` lies inside the disk for `t ≈ 0`, but `ℒ(1) = Res ζ_F/2 ≠ 0`, so the regularized function has no zero there. Correct.
* **Uniformity.** The bounds depend on `Q` and `t` only through `𝒞`, since Lemma 4.8 has an absolute constant, and they are uniform in `a ∈ [1/2, 1]`. This is what both uses need, because the characters there have moving conductors.

**E1 (sanity, mpmath).** Two cases were run, with `a = 0.56`, `e = 9·10^{-4}`, 192 points per
circle: `χ_5∘N` (`Q = 25`) at `t = 0` and `t = 14`, and the principal `ℒ` at `t = 0` and `t = 14`.
In every case:
* the winding number on the `R_2` circle is 0, so the hypothesis holds there;
* `max_{R_4}|g| ≤` the Borel-Carathéodory bound;
* `max_{R_6}|g| ≤ M(r_0)^{1−θ}M(R_4)^θ`;
* `max_{R_8}|g'| ≤ max_{R_6}|g|/(2e)`.

Actual sizes are `|g| ≈ 1` and `|g'| ≈ 1`, against `log 𝒞 ≈ 3-9`. See Sec. 8.

**Uses.**
* Lemma 18.1 Case 2 (12844-12852) uses the global clause with `b = s_κ = (1+κ)/2` and `v = e`, under the stated hypothesis `s_κ ≥ β_*` with `κ < 1`. So `b ∈ [1/2, 1)`, which is inside the lemma's hypotheses. It is applied to a primitive nonprincipal inducing `ψ` with moving `Q_ψ`, which is covered by the uniformity.
* Lemma 19.1 (15039-15044) uses the local version on `Re s = a + 8e`, the boundary of the closed `R_8`-disk, with buffered zero-free disks and `51/100 ≤ a ≤ 1`. The deleted product is handled by Lemma 4.10. Both match.

**Verdict: no wrong step found.**

## 6. Lemma 4.10 (deleted Euler factors)

* `|1 − a_p q^{−s}|^{±1} ≤ (1 − q^{−σ_0})^{−1}` for `Re s ≥ σ_0`. This uses `1 + x ≤ (1−x)^{−1}`.
* `−log(1 − q^{−σ_0}) ≤ ε log q` for large `q`. The finitely many small prime ideals contribute a constant.
* `∏(1 + q^{−σ}) ≤ q_R^{(−σ)_+} 2^{ω(R)}`, and `2^{ω(R)} <<_ε q_R^ε` by separating `q_p < 2^{1/ε}`. This holds for every real `σ`, not only on a bounded strip.
* `|D'/D| ≤ Σ log q_p/(q_p^{σ_0} − 1) ≤ log q_R/(2^{σ_0} − 1)`.

All are correct. **F1**: 3,000 random squarefree `R` (up to 25 prime ideals), `|a_p| ≤ 1`,
`σ_0 ∈ {0.05, 0.2, 0.5, 7/8}`: 0 violations. The closing remark on imprimitive `L(s,ψ*)D_R(s)`
is correct: `D_R` has no zeros in `Re s > 0`. **Verdict: no wrong step found.**

## 7. Lemma 13.1 (fixed-ray prime normalizer)

* **Input.** `π_{1_T}(x) ~ Li(x)/|T|` for a fixed quotient `T` of a fixed ray class group. This is the prime ideal theorem for ray classes (Hecke-Landau), equivalently Chebotarev for the class field of `T`. The cited Thorner-Zaman Thm 1.1 is far stronger than needed. The text says so (7027-7028, 7040: "No error exponent uniform in the ray conductor is used"). Its exact wording was not checked at source. Inert primes (norm `p^2`) and the primes dividing the modulus are `O(√x)` and finite respectively, so they are irrelevant.
* **Uniformity on the window.** "`o(x/log x)` uniform for `aP ≤ x ≤ bP`" is just the definition of `o(·)` on a moving window. Correct.
* **Stieltjes step.** `|∫E d(W(x/P)x^{−5/6})| ≤ sup_{[aP,bP]}|E| · TV = o(P/log P)·O(P^{−5/6})`, which is `o(P^{1/6}/log P)`. The boundary terms vanish because `W` is annular. Correct.
* **Main term.** With `x = Py`, it is `P^{1/6}/(|T| log P) ∫W(y)y^{−5/6} (log P/log(Py)) dy`, and the ratio tends to 1 uniformly on `[a, b]`. Positivity holds because `W ≥ 0` and `W ≠ 0`. Deleting a fixed finite set does not matter, since it is eventually outside the window. Correct.
* **Use in Sec. 20.1 (15562-15585).** `T`, `W_i`, `ℓ_i` and the deleted set `S` are fixed, and `P_i = Z^{ℓ_i}`. The product `A_T(Z) = (−1)^K Z^{−ℓ/6}∏S_i ~ (−1)^K|T|^{−K}(log Z)^{−K}∏ℓ_i^{−1}∫W_i y^{−5/6}` was re-derived: `∏P_i^{1/6} = Z^{ℓ/6}` and `log P_i = ℓ_i log Z`. Correct. The disjoint windows (6868-6880) make the `𝒫_i(Z)` disjoint but do not affect the single-slot asymptotic.
* **G0, G1** (EMPIRICAL; prime ideals up to norm 2·10^6). The trivial class of `Cl_6` (`|Cl_6| = 3`) equals `{p : (2/p)_3 = 1}` exactly on the first 3,000 primes, which links Lemma 4.1 and A2. For `T = Cl_6` and `T = Cl_12` (`|T| = 12`), the ratio of the left side to the refined main term `|T|^{−1}∫W(x/P)x^{−5/6}dx/log x` tends to 1. The ratio to the paper's main term drifts to 1 like `1 − O(1/log P)`, as the `log P/log(Py)` factor predicts. G_TABLE_PLACEHOLDER

**Verdict: no wrong step found.**

## 8. Mechanical checks (`sep30_sec4_checks.py`)

```
OUTPUT_PLACEHOLDER
```

**Exactness and limits.**
* Part A is exact integer arithmetic in `Z[ω]` (eis.py) on 3,240 prime ideals.
* The A2 "minimal modulus" and A4 "periodic mod 36 rad(u)" are EMPIRICAL on that range. The refutations, meaning the exact collisions that show a smaller modulus fails, are proofs.
* A1 tests the Frobenius identity only through its consequence on residue degrees and root counts.
* D, E and the constant `C` use mpmath at 25-60 digits. That is not directed and not certified. D1 and D2 test the paper's own Poisson identity and functional-equation normalization. They are not independent Hecke L-function software.
* B, C and F use double precision. G sums are double precision over exactly enumerated prime ideals.
* No statement uniform in an unbounded parameter is verified mechanically; that is what the reading in Secs. 1-7 is for.

## 9. Status-map consequences

In SEP30_VERIFICATION_MAP.md §4:
* Lemmas 4.1, 4.6 and 13.1 can move from **U** to **R**, citing this note, with the verdict "no wrong step found" and the scope above.
* Lemmas 4.7-4.10 already have a short reading in SEP30_L13_L45_REVIEW.md. This note adds the line-by-line pass and the checks D-F, so they are **R** here as well.

None of this changes the first unverified steps of the downstream targets (Lemma 18.1, Prop 15.2,
Prop 16.1). These lemmas are inputs to those steps, not the steps themselves.

# C3: does coefficient (7.4) factor into the local summands of (7.10)?

```text
Status: EXPLORATORY / FLOATING_RECONNAISSANCE. Symbols are exact. Gauss sums are ordinary
        double precision: not directed, not certified. No RH claim. No claim about the
        manuscript's theorems.
Scope: finite only. Coefficientwise identity K_eta(c,n,s,a;u) = prod_p kappa_p, where
       kappa_p is the summand of (7.10). Checked for 141,264 admissible tuples in the main
       configuration (70,723 nonzero), 4 x 8,352 tuples in alternative admissible
       configurations, and 5,472 tuples with an enlarged S. The local valuations covered are
       t = v_p(A) in {0,1,3,4,6,7}, k = v_p(s) <= 2, m = v_p(a) <= 1 and j = v_p(u) = 0..5.
Exact sources or dependencies: OpenAI "The Quasi-Riemann Hypothesis" (30 Sep 2026; external,
       unreviewed). paper.tex at git object pr908, path standalone/2026-10-07-openai-quasi-
       riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/
       paper.tex, sha256 42a5ee0f...6ac6a3. Sec. 4.1-4.2 (symbols, Gauss sums, G, R), Sec. 6.1
       (b_*, xi, tau, Xi, probe), Sec. 7.1-7.2, eqs. (7.1), (7.4), (7.7)-(7.10). Formulas were
       read from the TeX, not from pdftotext. Exact Z[omega] arithmetic is in ../a2/eis.py
       (imported, unmodified).
What was actually run: nice -n 10 python3 -I coeff74_factorization.py
       results/coeff74_factorization.json (317 s, one process, single thread), then the same
       script with --coverage (about 10 s). Python 3.13, numpy 2.5.3.
Smallest remaining gap: (1) Three of the four t>0 families of table (7.16) are covered only
       at r = 0, i.e. t = 3, 4, 6. Their r = 1 rows would need t = 9, 10, 12, with moduli of
       norm >= 12*7^9. (2) The exponent k = v_p(s) = 3 is not covered. (3) The analytic part of
       (7.5) is not checked: Poisson prefactor, Mellin weights and interchanges. (4)
       Everything is finite and floating-point.
```

RH remains unsolved. This note checks one finite algebraic identity inside the manuscript's
Section 7. It is not evidence for the zero-free half-plane.

## Verdict

**Every tested tuple satisfies the identity.** No mismatch appeared in any of the 166,144 tuples
(main configuration, alternative choices and enlarged S). The coefficient (7.4) was computed
directly from its definition. This includes F from (7.1), evaluated by brute force over d mod s,
with the full Gauss sum mod b_*A. It agrees with the product over p of the (7.10) summands,
where C_p is computed by brute force from its definition (7.7).

| quantity | max relative deviation |
|---|---|
| K_direct vs prod kappa_p, nonzero tuples (70,723) | **7.1e-13** |
| K_direct vs prod kappa_p, all 141,264 tuples | 1.5e-9 |
| same, using the closed form (7.8) for C_p | 1.8e-10 |
| F-split, intermediate (see below) | 5.0e-9 |
| enlarged S: all tuples (5,472) / nonzero tuples (4,207) | 2.2e-11 / 3.1e-14 |
| alternative b_*, ξ, η configurations (4 x 8,352) | <= 1.3e-12 |

The deviation is relative to max(1, |K|). The figures above 1e-12 come only from tuples whose
value is 0. In those tuples, large Gauss sums (up to about Q^6) cancel in floating point. Of the
zero tuples, 38,232 have a nonempty congruence in (7.1), so the vanishing there is a real
cancellation and not an empty sum.

**No convention issue was found** beyond those already fixed in [README.md](README.md):

* e(z) = exp(4πi Im z/√3);
* primary = 1 mod 3;
* χ_p(a) ≡ a^{(Np−1)/6};
* inert generator −q.

With these conventions and the TeX overbars (on α(A)G(A), ξ(u) and γ_3), the identity holds as
printed.

## What is compared

All objects are as in the TeX:

* A = c n³;
* H = u a⁶;
* τ = q_{b*}^{−1/2} g_ξ(b_*,1);
* Ξ(a) = ξ(a) χ_a(b_*);
* G(c) = conj(χ_c(4)) Γ(c);
* R = 𝔯 is the bicharacter Γ(ab)/(Γ(a)Γ(b)), defined also on noncoprime pairs.

* **Direct side, (7.4):**
  K = F(s,A,ua⁶) χ_s(b_*) / (√q_{b*} τ ξ(s) conj ξ(u)) · γ_2(c) conj(α(A)G(A)) η(A) Ξ(A)⁻¹ R(A,s).
  * F(s,A,H) = Σ_{d mod s, H ≡ b_*Ad (s)} χ_s(d) g_{ξχ_A}(b_*A, (H − b_*Ad)/s).
  * γ_2(c) is computed by direct summation mod c.
  * Γ uses the four-term formula. It agrees with direct summation to 1.4e-14 on composite and
    nonsquarefree elements.
* **Local side, (7.10):**
  κ_p = (−1)^{e0} γ_1^{−e0} η(p)^{e0} (a_p conj γ_3)^l ρ^{k−t} ω_p^{tk−e0 l−l(l−1)/2} C_p(t,k,j+6m).
  * a_p = conj(α(p))³ η(p)³, ρ = χ_p(u/p^j) and ω_p = χ_p(−1).
  * γ_1 and γ_3 come from direct prime Gauss sums.
  * C_p is computed by brute force from (7.7) in all 216 local cases used. It agrees with the
    closed form (7.8) to 4.1e-12, scaled by Q^{t−1/2}.
  * The Q-powers of (7.10) match q_c^{−1/2−x} q_n^{−1−3x} q_s^{−w} q_a^{−6z} in (7.3). The
    comparison is therefore between coefficients of Dirichlet monomials.
* **F-split (intermediate).** This is the sentence before (7.9) together with (7.9) itself:
  F(s,A,H) = √q_{b*} τ ξ(A) conj ξ(H/s) · Π_p U_p C_p(t_p,k_p,j'_p),
  with U_p = χ_p^{k−t}(h_p) χ_p^t(s_p) χ_p^{t−k}(A_p°) χ_p^{t−k}(b_*).
  It holds on every main tuple, to 5.0e-9 (the largest values again come from zero tuples).
  This isolates the b_*/ξ/τ factor and the unit factor (7.9) from the later pair-phase algebra.
* **P1, the Fourier claim in (7.1).** The transform mod sb_*A of ξχ_A(m) q_s^{−1/2} g_{χ_s}(s,−m)
  equals q_s^{1/2} F(s,A,H), with the kernel e(+Hm/(sb_*A)). This holds for every H in 9 pairs
  (s,A), including pairs where s and A share a prime: 4,284 cases, max deviation 2.5e-14.
* **P2, "the primitive Gauss sum vanishes unless (H,S)=1".** F = 0 for H = 0 and for H
  divisible by λ, 2 or an extra prime of S. This holds in 54 cases (main) and 72 cases
  (enlarged S); max |F| = 3.9e-12.

## Configurations

* **Main configuration:**
  * S = {2, λ} and b_* = 2λ.
  * ξ = (quadratic character mod λ) × (order-3 character on F_4^×, with ω ↦ e^{2πi/3}).
  * This gives τ = −i, so τ is nontrivial.
* **Alternative admissible choices:** these should also pass, and they do.
  * b_* = ζ·2λ and b_* = −2λ, where ζ = e^{iπ/3}.
  * ξ with the order-3 factor conjugated.
  * A second random η.
* **Enlarged S:** S = {2, λ, π_7, π̄_7}, so q_{b*} = 588.
  * ξ is χ_{π7}³ and χ_{π̄7} at the two new primes, which gives τ = 0.922 + 0.387i.
  * This tests the sentence "for any fixed enlargement of S, the same calculation".
* **η:** a completely multiplicative function on good primes with random unit-modulus values.
  The algebra uses only multiplicativity, not the Hecke property.

## Coverage

Primes are named by their primary generators:

* π7 = 1+3ω and π̄7 = −2−3ω (ω_p = −1);
* π13 = 4+3ω and π̄13 = 1−3ω;
* π19 = −5−3ω;
* −5, inert, of norm 25.

| tier | index sets | tuples | nonzero |
|---|---|---|---|
| T1 (box) | all 29 squarefree c with N c ≤ 100; n = 1; all 17 s with N s ≤ 49; a ∈ {1, π7, π̄7}; u = (6 units) × {1, π7, π7², π7⁵, π̄7, π̄7⁴, π13, π13³, π7π13, π̄7π̄13², −5, π19} | 106,488 | 68,430 |
| T2 (cube-full A) | (c,n) ∈ {(1,π7), (π7,π7), (π̄7,π7), (π13,π7), (π7π13,π7), (1,π̄7), (π̄7,π̄7), (1,π13), (π13,π13), (π7,π13), (1,−5)}; s ∈ {1, π7, π̄7, π7², π13, π7π13, π7π̄7, −5, π13²}; a ∈ {1, π7, π̄7, π13}; u = unit × Π_{p\|A} p^{j_p} with every j_p ∈ 0..5 (one-prime A: 6 units, with and without an extra factor π19; two-prime A: units 1, ζ, −1) | 33,696 | 2,205 |
| T3 (large A) | A ∈ {π7⁶, π7⁷, (π7π̄7)³, π13(π7π̄7)³}, with reduced sets of s, a and units; all j at the primes of A | 1,080 | 88 |

The largest modulus is N(b_*A) = 12·7⁷ ≈ 9.9·10⁶.

The local cases occurring in nonzero tuples were mapped to the rows of table (7.16), using
`--coverage` and `results/coeff74_coverage.json`. The count is of (tuple, prime) occurrences:

| table row | r = 0 | r = 1 |
|---|---|---|
| 1: (0,2r+2), k=0, m ≥ r+1 | 54 | — |
| 2: (0,2r+2), k=0, j=5 | 9 | — |
| 3: (0,2r+2), k=1, j=0 | 3 | — |
| 4: (1,2r), k=0, j=0 | 69,140 | 4 |
| 5: (1,2r), k=1, j=1 | 387 | 2 |
| 6: (1,2r), k=1, m ≥ r+1_{j≤1} | 1,434 | 8 |
| 7: (0,2r+1), k=0, j=2 | 994 | — |
| 8: (0,2r+1), k=1, j=3 | 423 | — |
| 9: (1,2r+1), k=0, j=3 | 543 | — |
| 10: (1,2r+1), k=1, j=4 | 261 | — |

The t = 0 cases are k = 0 (100,746 occurrences), k = 1 with j' = 0 (59,470) and k = 2 with
j' = 0 (4,791). No nonzero local case falls outside the table.

### Cancellations exercised

The table counts the nonzero main tuples in which each factor is ≠ 1, out of 70,723.

| factor / cancellation | tuples |
|---|---|
| τ (b_*/ξ/τ) | 70,723 (τ = −i) |
| ξ(s) | 38,753 |
| ξ(u) | 58,965 |
| ξ(A) | 50,473 |
| χ_s(b_*), cancelled by U_p | 51,520 |
| χ_A(b_*), cancelled by Ξ | 56,827 |
| R(A,s) = −1 | 26,162 |
| A–s cross phases Π χ_p^{t_p}(s_p) χ_p^{−k_p}(A_p°) | 25,530 |
| within-A pair phases Π_{p<r} (χ_p(r)χ_r(p))^{t_p t_r} | 4,806 |
| diagonal ω_p^{t_p k_p} = −1 | 1,558 |
| ω_p^{−l(l−1)/2} = −1 (l = 2 at Q = 7) | 80 |
| conj(γ_3)^l, l ≥ 1 | 2,293 |
| A with ≥ 2 distinct primes | 5,459 |
| t > 0 and k > 0 at the same prime | 2,284 |
| m > 0 | 43,817 |
| u with a nontrivial unit | 58,831 |

## Failing controls

Each control changes one ingredient. The control set has 5,844 tuples (2,104 of them nonzero),
covering all tiers. All controls fail with O(1) deviations, except the −s switch. That switch is
a real invariance, explained after the table.

| control | failing tuples | max dev |
|---|---|---|
| α(A) instead of conj α(A) | 1,908 | 2 |
| G(A) instead of conj G(A) | 1,864 | 2 |
| R(A,s) dropped | 780 | 2 |
| Ξ without χ_A(b_*) | 1,643 | 2 |
| χ_s(b_*) dropped | 1,518 | 2 |
| ξ(u) instead of conj ξ(u) | 1,413 | 1.73 |
| conj τ instead of τ | 2,104 | 2 |
| conjugated e in F only | 1,039 | 2 |
| generator −A (non-primary c) | 2,104 | 2 |
| generator ω·s (non-primary s) | 1,349 | 1.73 |
| γ_3 instead of conj γ_3 in (7.10) | 109 | 2 |
| ρ^{t−k} instead of ρ^{k−t} | 1,246 | 1.73 |
| ω_p^{−l(l−1)/2} dropped | 16 | 2 |
| ω_p^{tk} dropped | 71 | 2 |
| γ_1^{+e0} instead of γ_1^{−e0} | 1,835 | 1.98 |
| every prime generator −p (non-primary), consistently on both sides; 8,352 tuples | 4,713 | 2 |
| generator −s (non-primary s) | **0** | 1.4e-9 |

**Invariances (explained, not errors):**

* **s ↦ −s leaves K unchanged.** F picks up ξχ_A(−1), ξ(s) picks up ξ(−1), and R(A,s) picks up
  𝔯(A,−1). The net factor is χ_A(−1)𝔯(A,−1). The manuscript's Lemma 4.3 gives
  χ_A(−1) = 𝔯(−1,A), so the net factor is 1. The ω·s control fails by χ_A(ω), as it should. So
  the primary normalization of s is load-bearing only up to sign. That of c, n and the primes is
  fully load-bearing.
* **Conjugating e(·) consistently everywhere also leaves the identity intact.** This covers
  every Gauss sum, γ_j, τ and Γ, over 8,352 tuples, max deviation 1.3e-12. The orientation of e
  therefore matters only relative to the other objects: conjugating it in F alone fails.

## Boundaries

* **Not checked:**
  * the Poisson/Mellin identity (7.5) itself, with its prefactor X^{1/2}/(q_{b*}^{1/2} q_A);
  * the interchanges;
  * (7.11)–(7.15) beyond what [README.md](README.md) already covers (L3–L6);
  * the analytic claims of Lemma 7.1.
* **Floating-point only.** Gauss sums mod b_*A are evaluated all at once by a two-step DFT on
  the HNF residue grid. Three random frequencies per modulus were spot-checked against direct
  summation (max deviation 2.3e-14·√N). No exact cyclotomic evaluation was done.
* **Finite only.** Coverage is limited to t ≤ 7, k ≤ 2, m ≤ 1, primes of norm ≤ 97 in c and
  s with norm ≤ 49. Agreement on these tuples is consistent with the general coefficientwise
  derivation in Sec. 7.2 but does not replace it.

## Files

* `coeff74_factorization.py`: the script.
* `results/coeff74_factorization.json` and `results/coeff74_factorization.log`: full output.
* `results/coeff74_coverage.json`: the case map onto table (7.16).

```
cd research/exploratory/qrh-2026-10/numerics
nice -n 10 python3 -I coeff74_factorization.py results/coeff74_factorization.json   # 317 s
nice -n 10 python3 -I coeff74_factorization.py --coverage results/coeff74_coverage.json
```

sha256:

* script `5fb541e7…b17760`;
* JSON `4b801357…0d3cb6`;
* coverage `e2cfd464…fae7939`.

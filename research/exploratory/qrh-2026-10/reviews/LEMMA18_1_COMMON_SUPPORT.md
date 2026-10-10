# Lemma 18.1 (`lem:plain`): line check of the complete-common-support allocations

```text
Status: REVIEW (bounded; external, unreviewed manuscript) + EMPIRICAL finite checks.
  Verdict (a): no error found in the scoped lines. The imported inputs are listed in Section 5.
Scope: the complete-common-support allocations in the two finite Poisson transforms of the proof
  of Lemma 18.1 of "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8" (OpenAI,
  30 Sep 2026). First transform: paper.tex l. 13192-13349. Second-transform analogue:
  l. 13686-13933. Also read, as used: l. 12477-13191 (statement, reductions, centering,
  localization), 13409-13600 (Gauss-row enlargement), 13934-14310 (coefficient lemma, child
  normalization), 14312-14780 (Theta rows, lattice cancellation, (2.19)), 7042-7231 (finite
  correlations) and 1348-1388 (kernel-seminorms, statement only).
  Focus: case 1 (z = 0). Positive-slot steps (amplifier, greedy slot removal) were read only
  where the allocation passes through them.
Exact sources or dependencies:
  pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6; standalone/2026-10-07-openai-quasi-riemann-
    import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
    sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed here).
  First review: reviews/LEMMA18_1_REVIEW.md (its ledgers are reused, not repeated).
  Code: reviews/lemma18_support_checks.py (sha256 509a3dbb...2f2c7b); imports a2/eis.py
    unchanged (sha256 87ca11d9...798e65).
What was actually run (one process, nice -n 10, about 30 s):
  python3 -I lemma18_support_checks.py  -> 24/24 PASS (output in Section 4)
Smallest remaining gap: the scoped allocation is consistent. What remains is imported:
  (i) the L1 bound, uniform in the sector, for the Fourier coefficient measure that separates
      the kernels Phi_1^(R x/(y1 y2)) (y1 y2)^(-1/2) and Phi_2^ on fixed log boxes. Lemma
      kernel-seminorms (l. 1348) was read as a statement only; it is standard.
  (ii) the rest of Lemma 18.1 outside this scope: case 2, Sec. 18.8, Prop. 19.2.
  Lemma 18.1 as a whole is NOT certified by this note.
```

RH is unsolved. This note does not prove or disprove any zero-free region. The numerical checks
in Section 4 are floating-point evaluations of exact finite identities on small instances. They
are EMPIRICAL: they confirm the formulas used, not the asymptotic estimates.

## 1. What the first review left open

`LEMMA18_1_REVIEW.md` checked the exponent ledgers and the coprime squarefree model. It left one
step unchecked: the general allocation behind `(old-eq:2.5)`. That covers:

* the extraction of `C, D`;
* the masks `𝔢, 𝔯`;
* the artificial coprime extension with Möbius label `s`;
* the separation of the kernel and inverse roots.

It also left the second-transform analogue, with `D_2, E_2`, the partition `V_id`, and the
label `𝔱`. The numerology has zero slack at three points, so any extra fixed-power loss in these
steps would break the lemma.

## 2. First transform, l. 13192-13349

Notation: the two full index products are `n = Ca` and `n' = Db`. The common radical
`𝔠 = rad C = rad D` has log-norm `p`. At a common prime the multiplicities are `(i, j)`.

| step (lines) | what is done | exact? | loss (exponent of Z) | where accounted |
|---|---|---|---|---|
| decomposition (13192-13196) | `(n,n') ↔ (C,D,a,b)` with `rad C = rad D`, `(a,b)=1`, `(ab,CD)=1` | bijection (A1) | none | — |
| allocation (13197-13207) | at each common prime, fix its valuation in `l1, l2` (and slot). The residual is punctured at all of `𝔠` on that side. The same `𝔟_i` appear in both terms of `D_𝔟` | exact. Impossible allocations are zero terms | divisor-bounded count `∏(i+1)`: `Z^{ε1}` | count line 13321-13340 |
| row character (13209-13224) | `χ_C(k) χ̄_D(k) = ξ_𝔯(k) 1_{(k,𝔠/𝔯)=1}`, with `𝔯` the primes where `6 ∤ i−j`, and `ξ_𝔯` primitive | exact (B1, B2) | — | — |
| complementary mask (13214-13217) | `1_{(k,𝔠/𝔯)=1} = Σ_{𝔢 \| (k,𝔠/𝔯)} μ(𝔢)`, so `E ≤ p − R` | exact (A2; D negative control) | `2^{ω}`: `Z^{ε1}` | count |
| Poisson (13226-13268) | `k = 𝔢k'`, then Poisson modulo `𝔯ab`. Prefactor `H/(X q_𝔢 √q_𝔯)`, inverse roots `(q_a q_b)^{-1/2}`, normalized `G` (old-eq:2.4) | exact (D, four configurations) | exponent `m − A − R/2 − E` | ledger line 1 |
| CRT phase and reciprocity (13258-13268) | `χ_a(b𝔯) χ̄_b(a𝔯) ξ_𝔯(ab) · χ_a(𝔢) χ̄_b(𝔢)` → `τ_C(a) τ̄_D(b) R̄(a,b)`, times the frozen scalar `μ(𝔢) ξ_𝔯(𝔢)` | exact (B3, B4, D) | — | — |
| new moving support (13269-13276) | `χ_a(𝔢𝔯)`, `ξ_𝔯(a)` act on the whole residual. Their primes already puncture every residual factor | exact | `q̃ = q + R + E` | inside both norms |
| localization (13283-13299) | whole-dyad retention depends only on the sector, and the tail is bounded on the genuine coprime sum before any extension | upper bound | `K ≤ K_0 + δ_fr,1`, `δ_fr,1 < ξ` | `C_* ξ` |
| Möbius `s` (13300-13306) | `C_1` is extended to noncoprime residual pairs (full `G`, bicharacter `R`), then `Σ_{(a,b)=1} = Σ_{a,b} Σ_{s\|a,b} μ(s)` | exact (A4) | count `Z^{s_0}` | `+s_0` in the count; `−s_0` in each norm target |
| kernel separation (13307-13319) | `Φ̂_1(R_sc x/(y1y2))` and the inverse roots are functions of the row norm and the two **whole-product** norms on fixed log boxes. They are chosen before the live labels, so there is one Fourier measure for every live label and both rectangles. This gives one norm power `q_a^{it}` per column and no separate powers on `l1, l2` | exact Fourier expansion | `O(log Z)` dyads × measure L1 norm × height polynomial | imported (Section 5 (i)) |
| Cauchy-Schwarz in h (13317-13320) | applied only after separation, with `\|G_ξ\| ≤ 1`. `N_C` keeps `D_𝔟`, the mask, `s \| a`, `τ'_C` and one norm power | — | none | — |
| label count (13321-13340) | radical `Z^{p+ε}`; powers by Rankin `Z^{ε}`; allocations and `𝔢` divisor-bounded; `s` `Z^{s_0}` | upper bound | `p + s_0 + ε1` | ledger line 2 |

The ledger (l. 13384-13392) then closes exactly when (old-eq:2.6) `B_c + B_d ≤ c + d − 2p − R`
holds.

**Zero-slack primes.** Check A3 recomputes the local slack. It is zero exactly at the local types
`(i, j) = (1,1)` and `(2,1)`. At such primes the allocation spends only:

* the prime itself, counted in `p`;
* the divisor-bounded choices of exponent, allocation and `𝔢`.

None of these is a fixed power.

**The `s`-saving is realized downstream, with no loss.** The condition `s | u, v` puts every
prime of `s` into the second complete radical. Hence there are `Z^{p_2 − s_0 + ε}` radicals
(l. 13824-13832). The diagonal count is `Y_col/q_s` (l. 13628-13633). The added zero row needs
`s^6 | u` (l. 13574-13590). In each case `−s_0` appears exactly where `(old-eq:2.5)` allows it
(L1).

## 3. Second transform, l. 13686-13933

| step (lines) | what is done | exact? | loss | where accounted |
|---|---|---|---|---|
| localization (13652-13684) | done on the genuine full `(u,v,j)` sum before any extraction, with `\|F\| ≤ q_u q_v` | upper bound | `δ_fr,2 < ξ` | `C_*ξ` (eq:centered-child-edge-cost) |
| extraction (13686-13697) | `u = D_2 a`, `v = E_2 b`, complete common support. `F(D_2a, E_2b; j) = F(D_2,E_2;j) R(a,E_2) R̄(b,D_2) R(a,b) χ_a(j) χ̄_b(−j)` | exact (E: brute force from (old-eq:2.11)) | — | — |
| slot and plain sharing (13699-13734) | one-sided residual `χ_p(j)^i`; unequal `i > j_0` is zero unless `6 \| j_0` and the frequency is `p^{j_0}k`, `p ∤ k`, when it equals `P^{j_0−1}(P−1) χ_p(k)^{i−j_0}` | exact (F, including `(7,6)`) | — | — |
| local table (13742-13751) | `\|F(D_2,E_2; G_c V_id h')\| 1_part ≤ Z^{g_2 − t_2}` | bound (F: equality cases hit) | `g_2 − t_2` | exponent table |
| moving support (13761-13786) | `χ_n(G_c V_id)`: primes with `e_p ≠ 0` lie in the unit set (`t_2`) or the nonunit set (`V`); `e_p = 0` primes are already common punctures | exact | `q' = q̃ + w_o + t_2 + V` | (old-eq:2.13) |
| counts (13824-13836) | radicals `Z^{p_2 − s_0}`; powers by Rankin; partition `2^ω` | upper bound | `p_2 − s_0 + ε1` | exponent table |
| Möbius `𝔱` (13867-13897) | `F̃` on all residual pairs; full squarefree Möbius sum, inserted before factorwise estimates | exact (A4) | count `Z^{t_-}` | (eq:centered-divisor-boundary) |
| `𝔱`-allocation (13905-13923) | `1_{p \| ∏ n_i} = Σ_{J≠∅} (−1)^{\|J\|+1} ∏_{i∈J} 1_{p\|n_i}`; `n_i = p l_i` with no new coprimality; a slot selected twice gives zero; scales `X_i/q_p, Y_i/q_p` in both rectangles | exact (A5) | coefficient `Z^{−r̃_j/2}` per side | nets to `≤ 2θ_N` (L2, L3) |
| kernel separation (13899-13904) | `Φ̂_2(Z^{K+g} q_j/(q_u q_v))` depends on whole norms. `G_c V_id` is an outer phase. One measure for every label and both rectangles | exact Fourier expansion | as in the first transform | imported (Section 5 (i)) |

The exponent table (l. 13838-13861) and `(old-eq:2.14)` are consistent with these losses; the
first review checked them symbolically.

**The three tight points, rechecked against the allocation.**

* **(2.19) at `v = L`.** The saving `r = (L − c − w − min(c_2,d_2))_+` needs every formal post
  plain scale to have length at least `r − r̃_1`. That holds because the allocations extract
  the same `𝔟_i` from both rectangles and shorten no plain by more than its side's total
  extraction. The `𝔱` labels enter only through (old-eq:2.18h): `t_- − r̃_1 − r̃_2 − (r − r̃_1)_+ ≤ ω_2 − r` (L2, L3).
  The maximum is exactly `A − M` at `v = L` (L4). No allocation loss enters except `θ_N` and `ε1`.
* **`F_2 = 2b_2/3` at nonunit primes of multiplicity one.** These primes are in `D_2, E_2` with
  valuation 1 each. Their local data `(g_2, p_2, V, f) = (1, 1, 1, 2)` follow from the
  allocation. Check F confirms the local correlation values. There is unused slack here: the
  paper's own forced form `(h') = 𝔥_0 𝔳^6` with `q_{𝔥_0} ≥ Z^{2f}` gives the count
  `Z^{(m'−2f)/6}`, but (eq:exceptional-row-count) keeps `Z^{(m'−f)/6}`. The stronger count
  would leave `f/6` of slack at each such prime.
* **`F_1 ≥ 2c/3` when `J < 0`.** This uses only `q̃ ≥ R` and `B_c ≥ (3c − 5d − R)/6`, and the
  allocation supplies both exactly (`q̃ = q + R + E`). F_1 equals 2c/3 when `q = E = 0` and
  `3c ≥ 5D_0`.

Every other allocation cost is one of the following:

* a divisor-bounded or Rankin count;
* `O(log Z)` dyads;
* a `θ_N` or `δ_fr` correction inside `C_* ξ`;
* the `ε1` share.

All of these are `Z^{o(1)}` or `O(ξ)` per edge, and the induction depth is bounded. **No
fixed-power loss was found at any tight point.**

## 4. Mechanical checks (`lemma18_support_checks.py`)

```
PASS A1 complete-common-support decomposition is a bijection (3 primes, exps 0..7)   pairs=262144, round-trips=20000
PASS A2 R <= p and E <= p - R for every pair
PASS A3 (2.6) B_c+B_d <= c+d-2p-R, 20000 random multi-prime configurations   min slack=0; zero-slack local (i,j), i>=j: [(1, 1), (2, 1)]
PASS A4 sum_{s|a,s|b} mu(s) = 1_{(a,b)=1} (4 primes, exps 0..3)
PASS A5 t-allocation inclusion-exclusion identity (exhaustive)   23328 cases
PASS L1 s-label nets to zero in the first-transform ledger
PASS L2 (2.18h) identity
PASS L3 t-count bounded by the extraction coefficients (clipped-shell / exceptional sums)
PASS L4 (2.19) deficit maximised exactly at v = L with value A - M (zero slack)
PASS B1 chi_C conj chi_D = xi_r * 1_{(k, c/r)=1} (exact symbols, all k mod rad)
PASS B2 xi_r primitive mod r: Gauss sum = conj xi_r(h) tau(xi_r) for all h   max dev 7.8e-14
PASS B3 CRT factorization of the Gauss sum mod r a b (prime powers allowed)   7729 frequencies, max dev/sqrt(q_Q) 4.4e-15
PASS B4 chi_b(a) conj chi_a(b) = Gamma(ab)/(Gamma(a)Gamma(b)) (fixed mod-4 bicharacter)   3298 coprime primary pairs
PASS D bridge [(1,1)@7,(2,1)@7',(7,1)@13; a=p19^2, b=p31]   |dev|=1.1e-13 mass=1796.6
PASS D bridge [r=1: (1,1)@7,(7,1)@13; a=p19, b=p7'^2]      |dev|=1.6e-14 mass=1855.1
PASS D bridge [inert (3,1)@5, (2,8)@7; a=p7'^2, b=p13 p13'] |dev|=6.5e-13 mass=1736.6
PASS D bridge [(1,1)@13,(3,1)@7'; a=p19, b=p31 (R(a,b) = -1)] |dev|=7.8e-14 mass=2094.3
PASS E complete-support correlation (4 configurations with nonzero values, 1 forced-vanishing)  max dev 5.5e-14
PASS F single-prime correlation: vanishing, eq:correlation-local, unequal formula (p=7, i,j0<=7, (7,6))   1182 cases
PASS F absolute table |F(p^i,p^j0;j)| <= P^{g2-t2} locally (l. 13742-13751)   max(|F|-bound) = 9.09e-13
24/24 PASS
```

**Check D (end-to-end bridge).**

* **What it compares.** The left side is `Σ_{k∈O} Φ(k) χ_{Ca}(k) χ̄_{Db}(k)`, with a shifted
  Gaussian `Φ` so that the unit symmetry does not kill the sum. The right side is the paper's
  display: `Σ_𝔢 μ(𝔢) ξ_𝔯(𝔢) · H/(q_𝔢 √q_𝔯 √(q_a q_b)) · Σ_h G_ξ(𝔯,h) τ_C(a) τ̄_D(b) R̄(a,b) G(a,h) Ḡ(b,−h) · kernel`.
* **Configurations.** The common supports include multiplicities `(1,1)`, `(2,1)`, `(3,1)`,
  `(7,1)`, `(2,8)`, an inert prime and prime-power residuals.
* **Agreement.** The two sides agree to about `1e-13`. Only the kernel, the Fourier transform
  of the chosen `Φ`, differs from the paper's radial `Φ̂_1`. The Gauss-sum, label and phase part
  is exactly the paper's.
* **Negative controls.** Each of the following is detected as a mismatch:
  * dropping the `𝔢`-sum;
  * dropping `ξ_𝔯(𝔢)`;
  * dropping `R̄(a,b)`;
  * using `1/(q_a q_b)` in place of `1/√(q_a q_b)`.

  The test is therefore sensitive to the allocation data.

**Check F** works in `O/π^K ≅ Z/7^K`. It covers every `(i, j_0)` with `i, j_0 ≤ 7` and
`i + j_0 ≤ 13`, including the text's example `i = 7, j_0 = 6`, which gives
`P^5 (P−1) χ_p(k)`.

**Limits.** These are small-norm instances of exact finite identities, in floating point with
stated tolerances. They do not test the analytic bounds: the Fourier-measure norms, the
tail decay or the induction.

## 5. Verdict

**(a) Verified: no error found** in the complete-common-support allocations of l. 13192-13349
and l. 13686-13933. In detail:

* The pair decomposition, the valuation allocation with common punctures, and the `𝔢`/`𝔯`
  factorization of the row character are exact. So are the Poisson normalization, the CRT and
  reciprocity phases, the Möbius removal of coprimality (`s`, `𝔱`), and the `𝔱`
  factor-allocation.
* The kernels depend only on the whole-product norms. So one Fourier measure, fixed before the
  live labels, keeps `D_𝔟`, the common mask and a single norm power per column in both
  rectangles. This is what Lemma `centered-coefficient-invariant` and the lattice cancellation
  need.
* Every loss is either an exact term in the displayed ledgers or `Z^{o(1)}`/`O(ξ)`. That
  includes the three zero-slack points, one of which has spare slack `f/6`.

Remaining imported inputs (not re-proved here):

1. Lemma `kernel-seminorms` and Lemma `smooth-calculus`. These give the L1 norm of the
   separating Fourier measure on fixed log boxes and its polynomial height dependence, uniformly
   over sectors and `O(log Z)` dyads. They are standard Schwartz/Mellin facts; only their
   statements were read.
2. Sextic reciprocity in the four-class form `𝔯`. Check B4 confirms it on 3298 small pairs.
3. Rankin's bound and the polynomial-size Euler-product estimate for counting powers with a
   fixed radical. Lemma `deleted-euler-factors` for mask erasure.
4. Lemma `fixed-numerator-ray`, for the finite S-part of the rows.

**Scope caveat.** This settles only the step the first review could not verify. Lemma 18.1 as a
whole, and with it case 1 as a new unconditional sextic fourth moment, is still unreviewed
outside the scopes of the two notes. That includes the positive-slot amplifier and greedy
removal, the completion of Sec. 18.8, and the use in Prop. 19.2. It should not be relied on
without an expert check.

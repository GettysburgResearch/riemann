# Sep 30 reflection engine vs the reviewed Oct 5 version: statement diff and remainder review

```text
Status: REVIEW (bounded diff by an agent; external, unreviewed manuscripts; not an integration verdict)
Scope: Sep 30 paper.tex (7/8 claim), Section 5 lines 1648-3076: Prop 5.1 (prop:completed-reflection,
  statement 1676-1910, proof 1912-2462), Lemma 5.2 (2470-2532), Lemma 5.3 (2540-2578), prose
  2580-2616 (Minkowski step), Lemma 5.4 (2618-2636), eq:quadratic-large-sieve (2639-2671),
  Lemma 5.5 (2680-2813), Def 5.6 (2888-2950), Lemma 5.7 (2956-3076).
  Compared with Oct 5 paper2.tex (11/12 claim): eq:T (1287), eq:completed-twist (1304),
  prop:R (1317-1333), lem:reflection (1805-1845), lem:reflection-uniformity (1847-1857),
  lem:theta-bounds (1859-1878), lem:quadratic (1886-1913), lem:squarefree-completed (1923-2187),
  App. app:fixed-ray (2874-3479).
Exact sources or dependencies:
  pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6.
  Sep 30: standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
    The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
    sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (16677 lines).
  Oct 5: .../The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex,
    sha256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d (3988 lines).
  Prior review: reviews/OCT5_R3_THETA_REFLECTION.md and OCT5_REVIEW_SUMMARY.md (R3: no wrong step in
    paper2 1632-2214, 2874-3479). R3 script reviews/oct5_r3_theta_checks.py, sha256
    504d84f340b31fd5866c548530d713c25227183c73df21d7f3d0e78669c3b16e (read; imported, not modified).
  a2/eis.py sha256 87ca11d98bf3ee130a6dab613b5f7efe444058320b7c22b005327686f2798e65.
  Sep 30 results used but outside this scope (not reviewed here): Lemma 4.1 (fixed-numerator-ray),
    Lemma quadratic-four-term (841-933, containing eq:reciprocity-four-class) and
    lem:fixed-gauss-phase (934-),
    Lemma 4.5 (smooth-calculus, 1123) with eq:pointwise-mellin-tail, Lemma gaussian-annular (1288).
  External: Dunn-Radziwill arXiv:2109.07463v3 Sec. 5 and App. A (as audited in R3);
    Goldmakher-Louvel arXiv:1112.1642 Thm 1.1 (statement only, as in R3).
What was actually run:
  (1) A line-by-line reading of both texts in the scope above.
  (2) python3 -I reviews/sep30_reflection_checks.py OUT.json (new; sha256
      38c3cdf1e39489c33f3dfc680e47ffed5995eac8fec9bccd7433c8141f19fbfe), nice -n 10, 107 s, one
      process; Python 3.13.16, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, sympy 1.14.0.
  (3) A re-run of python3 -I reviews/oct5_r3_theta_checks.py OUT.json 22000 (unmodified, 38 s). Every
      R3 number in OCT5_R3_THETA_REFLECTION.md was reproduced (gauss, G, H, C, D 700/700, A, B, F, E).
  Both JSON outputs were written to the session scratchpad and are not committed; rerun to reproduce.
  Labels: EXACT = residue symbols as integer exponents; FLOAT = ordinary double precision (not
  directed, not certified); mpmath at 30 digits for the archimedean identities.
Smallest remaining gap: no discrepancy was found. Oct 5's *statements* do not imply Sep 30's
  Prop 5.1, Lemma 5.5 or Lemma 5.7 as stated; the arithmetic core of Prop 5.1 is the R3-reviewed
  Oct 5 appendix proof, and everything else was reviewed here. The first steps not independently
  verified are: (i) Lemma 5.7's separation step, which needs Lemma 4.5 (||w||_{J,sep} << p_{J+d+2}(w))
  and the Bochner/Minkowski inequality eq:reflection-common-minkowski (2580-2600); Lemma 4.5's proof
  was not read; (ii) Goldmakher-Louvel Thm 1.1 and its family hypotheses (statement level only, as in
  R3); (iii) the Phragmen-Lindelof and contour arguments (2350-2397), checked by reading only. The
  smallest load-bearing statement that Oct 5 does not cover is eq:completed-quadratic-norm (Lemma 5.5).
```

RH remains unsolved. This note compares two external, unreviewed manuscripts that claim zero-free
half-planes (`Re s > 7/8` for Sep 30, `Re s > 11/12` for Oct 5). It concerns only the shared
reflection engine (target 4 of [SEP30_VERIFICATION_MAP.md](SEP30_VERIFICATION_MAP.md)). A correct
reflection engine does not establish either paper's theorem.

## 0. Verdict

**Covered by the Oct 5 review plus the remainder reviewed here. No discrepancy was found.**

The coverage does **not** come from the Oct 5 *statements*. Read as stated, `prop:R`,
`lem:reflection` and `lem:quadratic` do not imply Sep 30 Prop 5.1, Lemma 5.5 or Lemma 5.7:

* `lem:reflection` (paper2 1805-1845) states only `|C| << 1`, a compact test class, and uniformity in a
  `k_0` family. Prop 5.1 states more: the explicit scalar, the sector dependence, branch compatibility,
  a Schwartz-type test class, and explicit seminorms.
* `lem:quadratic` (paper2 1886-1913) is Sep 30's imported sieve eq:quadratic-large-sieve (2644). It
  does **not** imply Lemma 5.5. Lemma 5.5 has a stronger row term (Section 3.2).
* `prop:R` (paper2 1317-1333) is an aggregate mean-square bound. It has no Lemma 5.7-type block
  statement and cannot be specialized to one.

The arithmetic core of Prop 5.1 is nevertheless identical, symbol for symbol after the dictionary in
Section 1, to the Oct 5 appendix *proof* (paper2 2874-3479). That proof is in R3's scope, where no
wrong step was found:

* the scalar `zeta` is Oct 5's `C` (paper2 3420);
* the local factors `B_p` and `omega_{p,j}` agree;
* the multiplier `kappa_F` is `kappa_0`, and the additive character `vartheta` is `psi`;
* the kernel bound eq:reflection-kernel is eq:ray-kernel (paper2 3460).

Everything else was reviewed here line by line (Section 4) and by new finite checks (Section 5):

* the general test class and Sep 30's own continuation argument;
* the dependence of `kappa_F` on `(h_0, r mod M^2)` only;
* branch compatibility;
* the cross-prime phase used by the marks of Sec. 14;
* the annular-Fourier and seminorm bounds;
* Lemmas 5.2-5.5 and 5.7.

| Sep 30 object | Implied by an Oct 5 statement? | Covered by R3-reviewed Oct 5 proof text? | Remainder reviewed here | Result |
|---|---|---|---|---|
| Prop 5.1 identity eq:reflection, `B_p` for j = 0..5, `d` support and size, `vartheta` | partly (`lem:reflection`, `lem:theta-bounds`; `|C| << 1` only) | yes, for compactly supported `V` (paper2 2906-3443) | test class (R-a); `phi` for a finite family (R-b); source formula at S-primes (R-c) | no error |
| Prop 5.1 (3): explicit `zeta`, `|zeta| <= 1/81`, `omega_{p,j}` | no | yes (paper2 3232-3275, 3420) | dictionary `tau^{+-}` vs `gamma_j` (check T) | no error |
| Prop 5.1 (3): `kappa_F`, `d`, `vartheta` fixed by `(h_0, r mod M^2)` | only for the `k_0` family (`lem:reflection-uniformity`) | yes, with "the active set" also fixed (paper2 3204) | R-d: the active set is not needed | no error |
| Prop 5.1 (3): branch compatibility for inactive `j_p = 0` primes | no | implicit (paper2 3270) | R-e, check E2E branch sums | no error |
| eq:reflection-cross-prime-phase (proof, 2265-2276) | no | no | R-f, check X | no error |
| Prop 5.1: entire continuation, polynomial strip growth | no | yes (paper2 3364-3408; R3 item 15, reading only) | R-a: Sep 30's own PL argument | no error (reading only) |
| eq:reflection-kernel | no (`C^J` form only) | yes, identical (paper2 3460) | — | no error |
| eq:reflection-annular-fourier, eq:reflection-test-seminorm, norm twist, Gaussian test | no | no | R-g, check H2 | no error |
| Lemma 5.2 (row sectors) | no | analog: paper2 eq:theta-row-twist (1975) | Section 4.2 | no error; uses Lemma 4.1 and the reciprocity lemma |
| Lemmas 5.3, 5.4 | no | no | Section 4.3 | no error; 5.3 uses Lemma 4.5 |
| eq:quadratic-large-sieve | **yes** (`lem:quadratic`, transposed) | GL hypotheses at statement level in both | — | statement match |
| Lemma 5.5 (completed-index quadratic norm) | **no** (Oct 5's route gives `(K+N)NB^2`, not `(K+NB)NB`) | no | Section 3.2, line by line; check Q | no error |
| Lemma 5.7 (unmarked reflected block) | **no** | no (analog: `(a^2, Y)` bookkeeping, paper2 2066-2091) | Section 3.3, line by line; check U | no error; uses Lemma 4.5 |

## 1. Dictionary of notation and normalizations

Both texts use `O = Z[omega]` with `lambda = 1 + 2 omega`. Primary means `== 1 (mod 3)`. Both write
`chi_p(x) = (x/p)_6` with every power zero-extended (`chi_p^0 = 1_{p ∤ x}`; Sep 30 636-640 and 1673-1674,
paper2 1724-1727). Both use `e(z) = exp(4 pi i Im z/sqrt3)` and `check-e(z) = exp(2 pi i (z + z-bar))`,
and both define `gamma_j(n)` by the same formula (Sep 30 642, paper2 310).

| Sep 30 | Oct 5 | Relation |
|---|---|---|
| `q_x` | `N(x)`, `NK(x)` | same |
| `mu in lambda^{-4} O`, `x = lambda^4 mu` | `ell`, `lambda^4 ell` | same |
| `k` in `mu = u lambda^k n b^3` | `m` | same |
| `V`: smooth, every `(x d_x)^j V` is `O(x^{+-C})` at `0` and `infty` | `V_*(y) = sqrt(y) W(y)`, `W in C_c^infty(I)` | Oct 5 class is contained in Sep 30 class |
| `V-hat(t) = int V x^t dx/x` | `V-hat_*(s)` | same |
| `(2 pi i)^{-1} int_(a) V-hat(s-1/2) X^{s-1/2} T(s,Psi) ds` = completed sum (1726-1733) | `T(X;Psi)` (eq:T, 1287) | equal when `V = V_*` |
| `T(s,Psi) = L_0(s,Psi) D(s,Psi)` | `script-T(s,Psi)` (3286) | same |
| `E` (prime support exactly `S`); mask `(nb, E) = 1` | `(nb, S) = 1` | equivalent |
| finite family `X`, `Psi_0 in X`, one `L` for all of `X` | one `Psi_0`; `L` (2928-2933) | see R-b |
| `phi(x) = chi_x(lambda)^2 Psi_0(x)` on primary `x` with `(x,E) = 1`, else `0`; `phi-hat(h)` | `phi`, `phi-hat(h_0)` (2907-2937) | same |
| `P`, `j_p in {0..5}`, `p ∤ L` | `P`, `j_p`, `p ∉ S` | same |
| active / inactive; `r = prod_{active} p` | `A`, `P \ A`; `r` | same |
| `c_F`, `a_F` (reduced `lambda^2 h_0/L = a_F/c_F`), `c = c_F r` | `c_0`, `c = c_0 r` | `c_F` is `c_0` |
| `M = lambda^12 L^4`; lift `h_p == 0 (mod M^2)` | same | same |
| `delta'`, `b`, `g`, `H`, `G = g H^{-1}` | `delta'`, `b_g`, `g`, `H`, `g_1` | same congruences (Sep 30 2092-2113 = paper2 3053-3064) |
| `L(t) = [[1,0],[t,1]]`; `Theta_0, Theta_1, Theta_2 = theta(L(t) w)` with `t = 0, omega^2, omega` (DR `F_1, F_19, F_10`) | `gamma_0, gamma_-, gamma_+` (DR `gamma_1, gamma_19, gamma_10`) | `Theta_1` is `-`, `Theta_2` is `+`; same rule for `u_0` (R3 check F) |
| `d_H`, `d_I` (coefficients of `theta-bar(H w)`) | `d_sigma`, `d_0` | same |
| `g~_3(n)` (1956), `d_I(lambda^{-3} n b^3) = 3^{5/2}\|b\| g~_3(n)` | `c_theta(nb^3) = 3^{5/2}\|b\| conj(chi_n(lambda)^2) gamma_2(n)` | equal for `(n,S) = 1` (1999); R3 check G |
| `kappa_F` | `kappa_0` | same three-case formula (2132-2185 = paper2 3175) |
| `D_F = lambda^3 c_F`, `delta'_F` | `D_0`, `delta'_0` | same |
| `vartheta(x) = e(-delta'_F r^{-1} x/D_F)` | `psi(lambda^4 ell)` | same |
| `sigma_p = lambda^2 c/p`, `epsilon_p = -((lambda^3 c/p) sigma_p)^{-1}` | same | same |
| `tau^+_{p,m}`, `tau^-_{p,m}` | `gamma_m(p)`, `chi_p(-1)^m gamma_m(p)` | check T, error 1e-15 |
| `omega_{p,j}` | `omega_{p,j}` | equal under the line above |
| `B_p` (1787-1796) | `B_{p,j_p}` (eq:theta-local-factors, 1735) | identical table |
| `zeta` (eq:reflection-row-phase, 1832) | `C` (paper2 3420) | identical formula |
| `K = (2 pi)^4/27`, `R(t) = prod_{+-} Gamma(1+t+-1/6)/Gamma(1-t+-1/6)` | the gamma quotient and scale in eq:theta-weight | same |
| `V^sharp` on any line `sigma >= 0` | `V_*^sharp` on `Re t = 0` | same function |
| `M_{A,B}(V) = sup_{-A<=eta<=1/4} int (1+\|u\|)^B \|V-hat(eta+iu)\| du` | the right side of eq:ray-kernel | same |
| row `m` (any nonzero element), twist `chi_{cn^3}(m)` | row `k = u_0 s v^2` with twist `g = f v^2`; `Psi_k = xi chi_n(k) chi_n(g)^4` | Section 4.2 |

## 2. Prop 5.1 against `lem:reflection` and the Oct 5 appendix

Each part of the Sep 30 statement is listed below. Sep 30 lines are given first.

1. **Completed indices and masks (1700-1739; proof 2044-2062).** `T(s,Psi) = L_0 D` is Oct 5's
   `script-T`, with `(n, E) = 1` equivalent to `(n, S) = 1`. Both put the character on the whole
   index `nb^3`, keep zero values, and allow `n` and `b` to share primes. The identity
   `phi(nb^3) prod_p chi_p(nb^3)^{j_p} = chi_n(lambda)^2 Psi(n) Psi(b)^3` on `(nb, E) = 1` uses
   `chi_b(lambda)^6 = 1` and the zero extension at `j_p = 0`. It is the identity used at paper2 1703-1704, and
   check K confirms it EXACTLY, including 367 cases with shared primes. A control that drops the
   zero extension at `j_p = 0` fails in 123 cases.
2. **Local cases j = 0..5 (1787-1796, 2020-2030, 2225-2250).** The table of `C_{p,j}`, `B_p` and
   `omega_{p,j}` is the same as paper2 eq:ray-fourier, eq:theta-local-factors and
   eq:ray-local-transform, under the `tau^{+-}`/`gamma_j` dictionary. The exponent `-j-2` (so
   `B_{p,1} = chi_p^3`) comes from the conjugate multiplier `chi_p(a)^{-2}`, as R3 established. Check T
   re-derives all six cases in Sep 30 notation (error 1.8e-14, 14 primes). Check E2E derives them
   inside the full Sep 30 construction.
3. **Twist classes.** Both texts use `Psi = Psi_0 prod_{p in P} chi_p^{j_p}` with `Psi_0` a ray
   character of `S`-supported conductor, zero-extended at `S`. Sep 30 needs one `L` for a finite
   family `X` (R-b). Lemma 5.2 reduces any nonzero row `m` to this form with `j_p = v_p(m) mod 6`.
   Oct 5 does the same reduction for `k = u_0 s v^2` with `j_p = v_p(k) + 4 v_p(g) mod 6`
   (eq:theta-row-twist). In both, every `j in {0..5}` can occur.
4. **Terms and counts (1776-1785; 2232-2236).** A term is indexed by `h_0 mod L` and the active set,
   with `c = c_F r`. This matches paper2 3008-3022. Oct 5 gives `O(2^{|P|})`; Sep 30 also gives
   `O(4^{|P|})` after splitting the Ramanujan factors, which is immediate.
5. **Coefficient functions (1797-1806; 1924-1990).** The support `{u lambda^k n b^3 : k >= -4}` and
   the bound `27 * 3^{k/6} |b|` match `lem:theta-bounds` (R3 item 16). The two `tau` magnitudes
   `3^{k/6+8/3}|b|` and `3^{k/6+3}|b|` are paper2's `3^{k'/2+2}` and `3^{k'/2+5/2}` with
   `m = 3k'-4` and `3k'-3`. Check D confirms, from the DR transcription:
   * no support violations among 15012 nonzero coefficients;
   * the attained values are exactly {8/3, 3} for `tau`, and `(k, |d|/|b|) = (-4, 9)` for `tau_1, tau_2`;
   * `max |d|/(27 * 3^{k/6}|b|) = 1` up to rounding (equality at `k == 0 mod 3`; no slack).
6. **Scalar `zeta` (1808-1842).** It equals paper2's `C` (3420) term by term. The bound
   `|zeta| <= 1/81` holds in both.
7. **Sector uniformity (1836-1842).** See R-d.
8. **Branch compatibility (1843-1850).** See R-e.
9. **Analytic part (1740-1773, 1852-1882).** The identity holds for every `a > 1` and for the
   Sep 30 test class (R-a). eq:reflection-kernel is eq:ray-kernel verbatim. The remaining bounds are
   covered in R-g.

## 3. Lemmas 5.5 and 5.7 against `lem:quadratic`, `lem:squarefree-completed` and `prop:R`

### 3.1 The imported sieve

* Sep 30 eq:quadratic-large-sieve (2644-2671) and paper2 `lem:quadratic` (eq:Q, 1890) are the same
  Goldmakher-Louvel bound, with rows and columns transposed (the bound is symmetric).
* The family verifications agree:
  * Sep 30's `e(a) = (q_a-1)/2 mod 2` is paper2's `e_k`;
  * Sep 30's "fixed primary square class modulo 4" is paper2's "classes modulo 24 O";
  * Sep 30's `epsilon_lambda` is paper2's `kappa_lambda`.
* Sep 30 names the reciprocity factor as eq:reciprocity-four-class. That lemma lies outside this
  scope. As in R3, GL's proof was not read.

### 3.2 Lemma 5.5 is new mathematics, not a restatement

Oct 5 never bounds `sum_k |sum_{n,b} beta(n,b) chi_k(nb)^3|^2` with `b` non-squarefree. Instead,
`lem:squarefree-completed` pulls `chi_{k_0}(b)^3` out of the inner sum and applies Cauchy-Schwarz in
`b` with weights `1/N(b)` (paper2 2138-2147). For `|beta| <= 1` that route gives
`(K+N) N B^2`. Lemma 5.5 claims `(K+NB) NB` (eq:completed-quadratic-norm, 2722), which is better by
a factor `B` in the row term. Lemma 5.7 uses this strength: its exponent `max(H, v+l_b) - l_b`
would become `max(H, v)` on the Oct 5 route. So Lemma 5.5 needs its own review. Line by line:

* **2731-2741, zero mask.** With `b = g t^2`, `c = (n, g)`, `n = cm`, `g = ch`, we have
  `nb = c^2 m h t^2`. Squares give `chi_k(.)^6 = 1_{coprime}`, so
  `chi_k(nb)^3 = chi_k(mh)^3 1_{(k, ct) = 1}`. This holds also when `t` shares primes with `n` or `g`.
  Check Q: EXACT, 3000/3000, including 415 collisions; dropping the mask fails 274 times.
* **2743-2749.** There are `O(T)` choices of `t`. Hilbert-space Cauchy costs a factor `T`. Correct.
* **2750-2762.** Expanding `1_{(k,c)=1} = sum_{r | (k,c)} mu(r)` and applying rowwise Cauchy costs
  `d(k) << (KNB)^eps`. Then `k = r k'` and `c = r c'`. Squarefreeness gives the row restriction
  `(k', r) = 1` and the column restriction `(c', r) = 1`. If `(r, t) > 1` the term is killed by
  `(k, t) = 1`. No joint `(k', c')` condition remains, since the full mask has already been expanded.
  Correct.
* **2764-2774.** `chi_k(mh)^3 = chi_r(mh)^3 chi_{k'}(mh)^3`, and `chi_r(mh)^3` is a column factor
  once `r` is fixed. The `S`-parts `m_S, h_S` take finitely many values. For each, `chi_{k'}(m_S h_S)^3`
  is a unit-modulus row factor, removed inside `|.|`. The column `j = m_g h_g` is squarefree and good
  with `q_j << NG/C^2`. GL then gives `(K/q_r + NG/C^2) sum_j |C_j|^2`. Correct.
* **2775-2794.** `j` has a divisor-bounded number of factorizations, and `c'` has `O(C/q_r)` values.
  The map `(c', m, h) -> (n, b)` is injective for fixed `r, t`. Cauchy over these choices gives the
  factor `C/q_r`, which proves eq:completed-quadratic-reduction. Correct.
* **2795-2813, counting.** `#D_r(t) << (C/q_r)(N/C)(G/C)`. With `q_r ~ r_0`, `O(r_0)` values of `r`
  and `O(T)` values of `t`, and `B ~ G T^2`, the total is
  `T^2 (NG/r_0)(K/r_0 + NG/C^2) = (NB/r_0)(K/r_0 + NG/C^2) <= NB(K + NB)`, using `G <= B` and
  `r_0, C >= 1`. The dyadic blocks are logarithmic in number. Correct.

Sanity limits: `B = 1` recovers GL. The diagonal term `K * #(n,b) ~ KNB` shows the row term cannot be
improved. Neither is a proof.

### 3.3 Lemma 5.7 against Oct 5's squarefree-row bookkeeping

Lemma 5.7 is a block-level energy bound with no Oct 5 counterpart statement. Its algebra corresponds
to paper2's `(a^2, Y)` updates (2066-2091), with:

* `S_0` the `a^2 / q` saving from active `j = 0` primes and small Ramanujan summands;
* `B_0` the `a^2/q` saving from `p | b` summands, and the factor `q^3` in `Y`;
* `N_0` the factor `q` in `Y` from `p | n` summands;
* `A_0` the factor `q^2` in `Y` from each active prime.

Line by line:

* **3003-3017.** For fixed `h_0` and fixed `R mod M_ref^2`, the class of `r = F_act R` is fixed.
  Prop 5.1 (3) then fixes `d` and `vartheta` (R-d). Every `p | R` has `j_p = 1` and is active.
  `prod_{p|R} B_p(lambda^4 mu) = chi_R(x_F)^3 chi_R(n b^3)^3 = chi_R(x_F)^3 chi_R(nb)^3`, with zeros
  kept. Check U: EXACT, 3000/3000; the sextic (conjugate-convention) control fails 1263 times.
  Correct.
* **3019-3029.** `delta = d alpha vartheta / (27 * 3^{k/6} |B_F b|)` satisfies `|delta| <= 1` by
  old-eq:4.3 for the representation `(n_0, b_0) = (N_F n, B_F b)`. Then
  `d alpha vartheta / sqrt(q_mu) = 27 delta 3^{-k/3} q_{N_F n}^{-1/2} q_{B_F b}^{-1}`. Checked by hand.
* **3030-3038.** A small Ramanujan summand or an active `j = 0` prime gives `q_p^{-1/2}`. A `p | n_0`
  summand gives `q_p^{1/2} q_p^{-1/2} = 1`. A `p | b_0` summand gives `q_p^{1/2} q_p^{-1} = q_p^{-1/2}`.
  These give `Z^{-nu_0} y_n^{-1/2} y_b^{-1}` with
  `nu_0 = v/2 + l_b + e_lambda/3 + (S_0 + B_0)/2`. Correct.
* **3039-3048.** `rho(R) = 81 zeta_R chi_R(x_F)^3` satisfies `|rho| <= 1`, and `27/81 = 1/3`.
  eq:unmarked-actual-annuli follows from multiplicativity of the norm. Correct.
* **3050-3053.** `Y = q_{c_F}^{-2} Z^{v + 3 l_b + e_lambda - T_0}`. Checked by expanding `T_0`.
  The bound `m_A(Y) << Z^{-(T_0 - v - 3l_b - e_lambda)_+/4}` holds. Correct.
* **3054-3063.** Lemma 5.3 applies in dimension 3 with exponents `(-2, 1, 3)` in `(y_R, y_n, y_b)`.
  Each Fourier mode gives unit-modulus row and column factors. The `(n, b)` box is kept as a fixed
  sharp restriction in `beta`, which Lemma 5.5 permits. The rows are enlarged only after separation.
  This is valid, given Lemma 4.5 (see gap (i)).
* **3065-3076, exponent.** With `K = Z^H`, `N = Z^v`, `B = Z^{l_b}`, Lemma 5.5 gives
  `max(H, v+l_b) + v + l_b`. Adding `-2 nu_0` and `-(.)_+/2` gives `E_0` exactly as displayed. The
  orders `p_5(W)` and `M_{A, ceil(4A)+7}(V)` are Lemma 5.3 with `d = 3` and `J = 0`. `J = 0` suffices
  because the separated bound is uniform in the Fourier height. Correct.

## 4. Remainder: Sep 30 content not covered by Oct 5, reviewed line by line

### 4.1 Prop 5.1

* **R-a. Test class, continuation and contour (1718-1724, 1740-1752, 2350-2397).**
  * Sep 30 allows any `V` whose Euler derivatives decay faster than any power at `0` and `infty`. Its
    Mellin transform is then entire and rapidly decreasing on vertical strips (the
    integration-by-parts identity used at 2447-2456). That is the only property of `V_*` that the
    Oct 5 proof uses after Mellin inversion (paper2 3405-3409).
  * `J(s)` (2280-2308) is the same object as paper2's `script-J`. The constant
    `(3^{5/2}/4)(27/(2pi)^2)^s` and the conversion `conj alpha(lambda^{-3}) = -i` were re-derived.
  * Sep 30 writes the reflected Mellin term (2335-2349) in a different but equivalent form. Check
    H2 confirms it with mpmath: relative error 2e-30 at two complex `s` with `Re s < 0`. The
    identity `(2pi)^{4s-2} 27^{-s} 3^{-5/2} = 3^{-4} K^{-t}` holds to 4e-34.
  * The growth argument (2365-2383) runs as follows:
    * `J` decays rapidly, by integration by parts in `log v`;
    * `1/(Gamma(s+1/3)Gamma(s+2/3)) << e^{pi|t|}`;
    * on `Re s < 0` the exponential parts cancel (`Gamma(4/3-s)Gamma(5/3-s)` against the direct
      factors);
    * on `Re s > 1` the bound comes from the direct series;
    * finally, Phragmen-Lindelof is applied with `e^{eps s^2}(B+s)^{-C}`.

    This is a standard argument and more explicit than paper2 3398-3404. It was checked by reading
    only.
  * The contour shift to `Re s = 1/2 - sigma < 0` and the termwise interchange on an absolutely
    convergent line are correct.
* **R-b. One `L` for a finite family (1678-1698, 2002-2011).** `(lambda/x)_3` is periodic mod 9
  (DR (1.5)). Each `Psi_0` is periodic modulo its conductor, and the zero mask modulo `E`. A common
  multiple of these finitely many moduli, with prime support `S` and divisible by 18, works. Correct.
  As a byproduct, check S needs `(lambda/b)_3` to be periodic mod 9 on primary `b`; this held over
  600 primes.
* **R-c. Source formula at S-primes (1950-2001).**
  * `g~_3(n)` has modulus 1 for every primary squarefree `n`, including the inert prime `-2`, where the
    cubic character of `F_4` is nontrivial. The twist identity uses `(t/n)_3^{-1}`.
  * The extension beyond `(n, 6) = 1` is used only for the size bound on `d`, which `lem:theta-bounds`
    already states for all `n`.
  * Equation 1999 is the `y = lambda v` substitution, and R3 check G confirms it.
  * Correct.
* **R-d. Dependence of `kappa_F`, `d`, `vartheta` on `(h_0, r mod M^2)` only (1836-1842, 2185-2200).**
  * Oct 5 says that `kappa_0` is fixed once `h_0`, the active set and `r mod M^2` are fixed
    (paper2 3204). Sep 30 drops "the active set".
  * The proof supports this. With lifts `h_p == 0 (mod M^2)`, `a == a_F r (mod M^2 c_F)`. So `a` modulo
    the needed prime powers of `L`, and `c mod 3`, depend only on `h_0` and `r mod M^2`. The
    congruences for `delta'` and `b` are then fixed.
  * Each of the three `kappa_F` formulas is a cubic symbol whose numerator and denominator are fixed
    modulo the moduli that determine it (supplementary laws mod 9, reciprocity at the primes of
    `c_F`). `delta'_F` and `r^{-1} mod D_F` are fixed because `D_F | M c_F` and `D_F | M^2`.
  * Check E2E confirms this numerically: `kappa_F` and `delta'_F` are constant over every family of
    active frequencies, 125820 terms in all.
* **R-e. Branch compatibility (1843-1850, 2252-2262).**
  * Adding an inactive `j_p = 0` prime changes neither `r` nor `a`. It therefore changes no data of
    the construction, and multiplies the scalar by `C_{p,0}(0) = 1 - q_p^{-1}`.
  * The statement correctly treats this as an identity *per branch*. The completed sum changes,
    because `Psi` gains the mask `1_{p ∤ n}`, and the extra active `j = 0` branch accounts for the
    difference.
  * Check E2E evaluates the full sum over all `h` (zero frequencies included) and compares it with the
    sum of branches with factors `(1 - 1/q)`: 143 identities, error 9.6e-15.
* **R-f. Cross-prime phase (2265-2276).**
  * `epsilon_p = -lambda^{-5} (c/p)^{-2}` follows from the definitions.
  * Substituting gives `chi_p(sigma_p)^{-2} omega_{p,j} = xi_{p,j} chi_p(c/p)^{2j+2}` in all six
    cases (for `j = 4`: `-2 == 2j+2 mod 6`; for `j = 0`: `4 - 2 = 2`).
  * Check X verifies the ratio is constant over all units `c/p`, for 14 primes and all `j`: spread
    1e-15. With exponent `2j-2` the spread is `sqrt 3`.
  * For `j = 1` the coupling is `chi_p^4 = conj(chi_p)^2`, a cubic character of the *other* active
    primes.
  * This is used by Cor 14.1 (marks), which is outside this scope and was not read.
* **R-g. Bounds for the transformed test (1852-1882, 2408-2461).**
  * `|R(sigma+iu)| << (1+|u|)^{4 sigma}` on `-1/4 <= sigma <= A`, with no numerator pole for
    `sigma > -5/6`. Check H2: the ratio is bounded (at most 3.7) for `sigma = -1/4, 0, 1, 3` and
    `u` up to `10^4`.
  * Shifting to the lines `-1/4, 0, A` and letting each `x d_x` contribute `(-t)^j` gives
    eq:reflection-kernel with `M_{A, ceil(4A)+j+2}`. This matches Oct 5.
  * Annular Fourier bound: `f_Y(v) = chi(e^v) V^sharp(Y e^v)`; `J+2` integrations by parts; Leibniz;
    and `m_A(Y e^v) ~ m_A(Y)` on a compact set of `v`. These give order `ceil(4A)+J+4`.
  * Seminorm bound: `B+2` Euler integrations by parts, with `|eta + iu| >= |u|` and
    `x^eta <= 1 + x^{-A} + x^{1/4}`.
  * Twist bound: `1 + |u| <= (1 + |u + u_0|)(1 + |u_0|)`.
  * Gaussian test: Mellin transform `e^{t^2}` (check H2: exact to 30 digits).
  * All correct.
* **R-h. Zero-entry adjustment (2122-2128).** Translating by `lambda^2 M^2 O` and adjusting `delta'`
  keeps every congruence and avoids zero entries in residue symbols. This is harmless; none occurred
  in check E2E.

### 4.2 Lemma 5.2 (row sectors, 2470-2532)

* For `(A, m_good) = 1`, eq:reflection-row-reduction is sextic reciprocity in the form of
  eq:row-fixed-ray-reduction (1055-1069). When they share a prime, both sides vanish, including for
  exponents divisible by 6.
* `chi_A(u m_S)` depends only on `u` and `v_l(m) mod 6`, and Lemma 4.1 makes `A -> chi_A(d)` a ray
  character supported on `S`.
* Fixing the ray class of `m_good` fixes `R(., m_good)`.
* The fixed family is therefore finite and one `(E, L)` serves all sectors. This matches Oct 5's
  eq:theta-row-twist together with "partitioning `k_0` into fixed ray classes" (paper2 1975-1993).
* Correct, given Lemma 4.1 and the reciprocity lemma (outside scope).

### 4.3 Lemmas 5.3 and 5.4

* **Lemma 5.3 (2540-2578).**
  * On the support of `W`, the monomial `h` lies between two positive constants.
  * Each `y_i d_{y_i}` acting on `V^sharp(Y h)` gives `a_i (x d_x V^sharp)(Y h)`, with no power of `Y`.
  * `p_j` is a sum of sup norms (Sep 30 1103-1106), so Leibniz gives eq:reflection-common-profile.
  * eq:reflection-common-measure is Lemma 4.5 applied with `j = J + d + 2`.
  * Correct, given Lemma 4.5.
* **Minkowski step (2580-2616).** This is the Bochner integral of a common density. Its finiteness is
  `||F~_Y||_{0,sep} < infty`.
* **Lemma 5.4 (2618-2636).** A shell contains `O(1 + 2^j U/a)` lattice points. Summing the geometric
  series with `A > 1` and using `U >= 1` gives the claim. Correct.

## 5. Finite checks (`reviews/sep30_reflection_checks.py`)

| Check | What | Result |
|---|---|---|
| S | `cub_sym`: cubic symbol by reciprocity and supplementary laws, no factorization, vs R3's Euler-criterion symbol | 1500/1500 EXACT |
| T | eq:reflection-local-fourier with `tau^-`; `tau^+ = gamma_m`, `tau^- = chi_p(-1)^m gamma_m`; `\|tau\| = 1`; local transform to `chi_p(sigma_p)^{-2} omega_{p,j} B_p`, j = 0..5; 12 split primes (N <= 43), inert 5, 11 | 5e-16; 1.0e-15; 1.3e-15; 1.8e-14 (FLOAT) |
| E2E | Sep 30 construction (2063-2245) with `L = 18`, `M = lambda^12 L^4`, lifts `h_p == 0 mod M^2`; 13 values of `h_0` including nonunits and `0`; all six (case, cusp) pairs; `P` = {N=7, N=13} for all 36 pairs `(j_1, j_2)`, and {7, 13, inert 5} for 6 triples. Checks: `kappa(G)` vs the Sep 30 formula; constancy of `kappa_F`, `delta'_F`; `sum_h prod C * conj kappa(G_h) * e(-delta' x/(D_F r)) = conj(kappa_F) vartheta(x) prod chi_p(sigma_p)^{-2} omega_{p,j} B_p(x)`; branch sums | `kappa`: 125820/125820 EXACT; constancy: yes; 728 active identities, max error 2.5e-14; 143 branch identities, 9.6e-15 (FLOAT) |
| E2E controls | conjugate multiplier / no `M^2` lift / sign of `epsilon_p` | fail in 52/52 / 28/52 (1344 non-constant terms) / 39/52 configurations; min error 0.63, max errors 3.2 and 2.0. The sign control can pass only when `chi_p(-1)^{j+2} = 1` |
| X | cross-prime phase: `chi_p(sigma_p)^{-2} omega_{p,j} / chi_p(c/p)^{2j+2}` constant; `epsilon_p = -lambda^{-5}(c/p)^{-2}` | spread 1.0e-15; 2592/2592 EXACT; control `2j-2`: spread 1.73 |
| K | whole-index mask with zero extensions | 1465/1465 EXACT (367 with shared `n, b` primes); no-zero-extension control fails 123 |
| Q | Lemma 5.5 zero mask | 3000/3000 EXACT (415 collisions); unmasked control fails 274 |
| U | Lemma 5.7 quadratic column factor | 3000/3000 EXACT; sextic control fails 1263 |
| D | supports and sizes from DR `tau`, `tau_1`, `tau_2` (R3 transcription), `N(nu) <= 6000` | 15012 nonzero; 0 support violations; ratio max `1 + 4e-15` (equality case) |
| H2 | Bessel form (Sep 30 2288-2292); reflected Mellin scalar (2335-2349); `3^{-4} K^{-t}`; Gaussian Mellin `e^{t^2}`; Stirling for `R` | 2e-31; 2e-30; 4e-34; 0; bounded |

**What the checks authenticate and what they do not.**

* Check E2E is an independent finite replay of the *arithmetic* of Prop 5.1: Fourier inversion,
  reduced fraction, `delta'`, `H`, multiplier, additive CRT and local Gauss sums. It does so for one
  `L` and small moving primes. The multiplier is computed directly as `(c_1/a_1)_3`, not from the
  formula under test.
* The automorphy of `theta` itself, the cusp labels and the DR coefficient formulas rest on R3 checks
  A, B, E, F and G. These were re-run unchanged and reproduced.
* No end-to-end numerical evaluation of both sides of eq:reflection was attempted (cost, as in R3
  Section 6).
* Finite checks are not proofs of the infinite statements, and FLOAT results are not certified.

## 6. Minor points (non-fatal)

1. Sep 30 1941-1946 cites DR Appendix A rows 1, 19, 10 for `Theta_0, Theta_1, Theta_2`. These labels
   agree with R3 checks B and F (`Theta_1` is DR's `gamma_19`).
2. Sep 30 2288 attributes the Bessel identity to "[DR, Lemma 5.3]". The identity is correct (check
   H2); the citation was not checked.
3. Lemma 5.5's general bound has a factor `T sum_t`, which is `T^2` blocks. Its final display absorbs
   this through `B ~ G T^2`. Correct, but easily misread as one factor `T`.
4. The bound `|d| <= 27 * 3^{k/6}|b|` has no slack at `k == 0 (mod 3)` (check D). Sep 30 uses it only
   as `|delta| <= 1`, which allows equality.

## 7. Not done

* Lemma 4.5 (smooth calculus), Lemma 4.1, Lemma quadratic-four-term (841-933), lem:fixed-gauss-phase and
  eq:pointwise-mellin-tail were not read.
* GL's proof was not read; DR/Patterson were audited only as in R3.
* Cor 14.1 and Section 14, which consume the cross-prime phase and the marks, are outside scope.
  So are Lemma 5.8, the Sec. 5 prose between 2814 and 2887, and every downstream use of Lemmas
  5.5 and 5.7.
* No asymptotic numerical test of Lemma 5.5 was run (a finite test cannot check an `eps`-loss bound).

## Reproduction

```
cd research/exploratory/qrh-2026-10/reviews
nice -n 10 python3 -I sep30_reflection_checks.py /path/to/sep30_out.json        # ~110 s, one process
nice -n 10 python3 -I oct5_r3_theta_checks.py /path/to/r3_out.json 22000        # ~40 s (R3, unchanged)
```

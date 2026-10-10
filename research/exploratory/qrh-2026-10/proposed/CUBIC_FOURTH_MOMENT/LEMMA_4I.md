# PROPOSED proof of the cubic Lemma 4.I (Gauss-row zero `h = 0`) of SKETCH Sec. 4

```text
Status:      PROPOSED (exploratory, unreviewed). Not integrated. RH is not addressed. Verdict:
             Lemma 4.I is PROVED HERE (PROPOSED) in a corrected, precise form (Sec. 1); four
             imprecisions of the SKETCH wording are flagged and fixed (F1-F4). This is a finite /
             local step inside a CONDITIONAL fourth-moment scheme (SKETCH.md, conditional on (H-A),
             (H-B), Lemma 4.K and Lemma 18.1 case 1); it is not evidence for that scheme.
Scope:       one added row (h = 0) of the final smooth row ball in the manuscript's second
             transform, transferred from n = 6 to n = 3; uniform in a_0, s, t, ell and the norm type
             (initial, amplified main term, extracted errors). Local / bookkeeping scope only.
Exact sources or dependencies:
             paper.tex at commit 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6 (path
             standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
             The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), sha256
             42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed here), read
             as untrusted data: l. 7041-7079 (old-eq:2.4, lem:prime-power-fourier, eq:gauss-local),
             13050-13070 (eq:centered-coefficient-form: s a fixed squarefree ideal), 13085-13101
             (H_N, theta_N), 13312-13319 (Moebius s, s_0), 13413-13425 (old-eq:2.7), 13572-13594
             (the sextic Gauss-row zero), 13596-13606 (B(u), Phi_2). In this folder: SKETCH.md Sec. 4
             (Fact 0, Lemma 4.A), STATUS_END_OF_WAVE.md (row R7). Imported: the manuscript's
             set-up (B(u) divisor-bounded with the assigned loss eps_1 <= eps_G, the support box,
             Phi_2 bounded, the 2 theta_N correction counted in the C_* xi stage allowance).
What was actually run:
             python3 -I lemma_4i_checks.py  (output lemma_4i_checks.out, same directory; 2.6 s, one
             core). Exact integer / Z[omega] arithmetic except [I4] (floating point, labelled).
             Imports ../../a2/eis.py read-only. Result: checks 6/6 PASS; failing controls detected
             4/4. sha256: lemma_4i_checks.py b5f35b6e...604f6b, lemma_4i_checks.out
             577eff36...e41f2, eis.py 87ca11d9...98e65. No Lean, lake or comparator process.
Smallest remaining gap:
             none inside Lemma 4.I beyond the imported set-up. The lemma closes R7 only; it does not
             touch Lemma 4.K (R14, unreviewed), (H-B) (R15), or the centred stage, which remain the
             load-bearing open items of SKETCH.md.
```

RH is unsolved. Nothing below proves or disproves RH, Lemma 18.1, or any moment bound.

Notation is that of SKETCH Sec. 1.1 and Sec. 4: `O = Z[ω]`, `p` a good prime with `P = q_p`,
`χ_p(x) = (x/p)_3`, zero-extended, `χ_u = Π_p χ_p^{v_p(u)}`, and

    G(u,k) = q_u^{−1/2} Σ_{x mod u} χ_u(x) e(kx/u),   G(1,k) = 1        (old-eq:2.4 with 6 → 3).

Moduli `u` are primary (`≡ 1 mod 3`) and prime to `S`.

## 1. Statement

**Lemma 4.I (cubic Gauss-row zero; proved here, PROPOSED).** Work in the final smooth row ball
of the second transform (manuscript l. 13572-13606, with `n = 3`). Take any of the three norm types,
at its column length `a_0` (`a_0 = A − c − w`). Let `B(u)` be the full allocated convolution
coefficient, including the fixed mask and the condition `s | u`, where `s` is a fixed squarefree
ideal (l. 13067) and `s_0 = log_Z q_s`. Assume:

* `B` is supported on primary `u` outside `S` with `q_u/Z^{a_0} ∈ exp([−H_N, H_N])`;
* `|B(u)| ≤ Z^{ε_1/2}` there (the assigned divisor-bounded loss);
* `|τ_1(u)| ≤ 1`, `t ∈ R`, and `ℓ ≥ 0`.

Put `Y_col = Z^{a_0 + θ_N}`. The added `h = 0` term of the ball norm is

    R_0 := Z^{−ℓ} Φ_2(0) | Z^{−a_0/2} Σ_u B(u) τ_1(u) q_u^{it} G(u,0) |².

(a) **Support.** `G(u,0) = 0` unless `u` is a cube ideal (`3 | v_p(u)` for every `p`). In that case
`u = v³` with `v` primary, and `G(u,0) = q_u^{1/2} Π_{p | u}(1 − 1/P)`. In particular
`0 < G(u,0) ≤ q_u^{1/2}`.

(b) **Refined bound.** `R_0 ≪ ‖Φ_2‖_∞ Z^{2a_0/3 − 2s_0 + 5θ_N/3 + ε_1}`. The implied constant
is absolute.

(c) **Crude bound (the manuscript's count).** `R_0 ≪ ‖Φ_2‖_∞ Z^{2a_0/3 + 5θ_N/3 + ε_1}`. If the
support is nonempty, then also `s_0 ≤ (a_0 + θ_N)/3`.

(d) **Fit.** If the support is empty then `R_0 = 0`. Otherwise both (b) and (c) give

    R_0 ≪ Z^{a_0 − s_0 + 2θ_N + ε_1},

with exponent slack `(a_0 + θ_N)/3 + s_0` in (b) and `(a_0 + θ_N)/3 − s_0` in (c). Both are
`≥ 0`. The slack in (c) is `0` exactly when `q_s³ = Y_col`. Since `q̃, w_o, w, B_c ≥ 0`, the
allowance of old-eq:2.7 satisfies `Λ_c ≥ a_0 − s_0 + ε_G`. So old-eq:2.7 bounds the added row,
with the same numerical `2θ_N` correction counted in the `C_*ξ` stage allowance as at `n = 6`.

### 1.1 Imprecisions in the SKETCH wording, and fixes

* **F1.** "Their contribution is `Z^{2a_0/3 − 2s_0}`." This is an upper bound, not a size. It
  omits `5θ_N/3`, the loss `ε_1` and the factor `Z^{−ℓ}Φ_2(0)`. Fixed in (b).
* **F2.** "fits the allowance `a_0 − s_0`". The precise target is
  `a_0 − s_0 + 2θ_N + ε_1 ≤ Λ_c + 2θ_N` (with `ε_1 ≤ ε_G`), and the slack is
  `(a_0 + θ_N)/3 + s_0`. This uses `a_0 ≥ −θ_N`, which holds because a nonempty shell has
  `Y_col ≥ 1` (l. 13573-13574). Fixed in (d).
* **F3.** "equality at `s_0 = a_0/3`". The equality point is `s_0 = (a_0 + θ_N)/3`. The bound
  `s_0 ≤ (a_0 + θ_N)/3` (from `q_s³ ≤ q_u`) needs `s` squarefree. Control [I2-CTRL] shows it fails
  for `s = p³`. The manuscript's sextic `q_s⁶ ≤ q_u` (l. 13578) relies on the same squarefreeness,
  stated at l. 13067. The refined bound (b) survives a non-squarefree `s` (Remark 2.1).
* **F4.** "By Lemma 4.A, `h = 0` sees only cube moduli." Lemma 4.A is prime-power local. Composite
  `u` also need the CRT factorisation (2.2) below. "Cube" means a cube ideal. With the primary
  normalisation it is the cube of a primary element, since `O` is a PID and the only unit
  `≡ 1 (mod 3)` is `1`.

## 2. Proof

**Step 1 (local value, Lemma 4.A at `k = 0`).** We have `v_p(0) = +∞ ≠ a − 1`. So for `a ≥ 1`:

    G(p^a, 0) = 0                                   if 3 ∤ a,
    G(p^a, 0) = P^{a/2} − P^{a/2−1} = P^{a/2}(1 − 1/P)   if 3 | a.        (2.1)

Directly: the sum `Σ_{x mod p^a} χ_p(x)^a` is `φ(p^a)` if `χ_p^a` is principal, and `0`
otherwise. By Fact 0, `χ_p^a` is principal iff `3 | a`.

**Step 2 (CRT).** Let `u_1, u_2` be coprime and prime to `3`. Then for every `k`

    G(u_1u_2, k) = χ_{u_1}(u_2) χ_{u_2}(u_1) G(u_1,k) G(u_2,k).                   (2.2)

*Proof.*

* Write `x = u_2x_1 + u_1x_2` with `x_i mod u_i`. This is a bijection onto `O/u_1u_2`.
* Since `χ_c = Π χ_p^{v_p(c)}`, we have `χ_{u_1u_2}(x) = χ_{u_1}(x)χ_{u_2}(x)`.
* Then `χ_{u_1}(x) = χ_{u_1}(u_2x_1) = χ_{u_1}(u_2)χ_{u_1}(x_1)`, and symmetrically for `u_2`.
* `e` is trivial on `O`, so `e(kx/(u_1u_2)) = e(kx_1/u_1)e(kx_2/u_2)`.
* Finally `q_{u_1u_2}^{−1/2} = q_{u_1}^{−1/2}q_{u_2}^{−1/2}`. ∎

The phase `χ_{u_1}(u_2)χ_{u_2}(u_1)` has modulus one by coprimality. (By cubic reciprocity it is `1`
for primary `u_i`, but only its modulus is used.) Iterating over `u = Π p^{a_p}`:

* `G(u,0)` is a unimodular constant times `Π_p G(p^{a_p},0)`.
* By (2.1) this vanishes unless every `3 | a_p`.
* When it does not vanish, `G(u,0) = q_u^{−1/2} Σ_{x mod u} χ_u(x) = q_u^{−1/2}φ(u)`, because `χ_u`
  is then the principal character mod `u`. This equals `q_u^{1/2}Π_{p|u}(1 − 1/P)`.
* Primary cube root: `(u) = 𝔳³`, and `𝔳 = (v)` with `v` primary. Then `u = εv³` with `ε` a unit and
  `v³ ≡ 1 (mod 3)`, so `ε ≡ 1 (mod 3)`, hence `ε = 1`.

This proves (a).

**Step 3 (pointwise).** On the support, `q_u ≤ Y_col`. So `|G(u,0)| ≤ q_u^{1/2} ≤ Y_col^{1/2}`.

**Step 4 (count).**

* Let `u = v³` with `s | u`. Since `s` is squarefree, every prime of `s` divides `v`, so `s | v`.
* Hence `#{u : u cube, s | u, q_u ≤ Y_col} ≤ #{𝔴 : N𝔴 ≤ Y_col^{1/3}/q_s}` (put `v = s𝔴`).
* There is an absolute constant `C_0` such that, for all `x > 0`, the number of ideals of `O` of norm
  `≤ x` is at most `C_0 x`:
  * it is `0` for `x < 1`;
  * for `x ≥ 1` it is `(1/6)#{(a,b) ≠ 0 : a² − ab + b² ≤ x} ≤ C_0x` (an ellipse of area `2πx/√3`).
* So the count is `≤ C_0 Y_col^{1/3} q_s^{−1}` (refined) and `≤ C_0 Y_col^{1/3}` (crude).
* If the support is nonempty, `s | v` gives `q_s ≤ q_v`. So `q_s³ ≤ q_u ≤ Y_col`, i.e.
  `s_0 ≤ (a_0 + θ_N)/3`.

**Step 5 (assemble).** By the triangle inequality, `|τ_1(u)q_u^{it}| ≤ 1` and `|B(u)| ≤ Z^{ε_1/2}`:

    |Σ_u B(u)τ_1(u)q_u^{it}G(u,0)| ≤ Z^{ε_1/2} · C_0 Y_col^{1/3} q_s^{−1} · Y_col^{1/2}.

Square this, multiply by `Z^{−a_0}`, and use `Z^{−ℓ}Φ_2(0) ≤ ‖Φ_2‖_∞`:

    R_0 ≤ C_0² ‖Φ_2‖_∞ Z^{ε_1} Z^{−a_0} Y_col^{5/3} q_s^{−2}
        = C_0² ‖Φ_2‖_∞ Z^{2a_0/3 + 5θ_N/3 − 2s_0 + ε_1}.

This is (b). Dropping `q_s^{−1}` gives (c).

**Step 6 (exponents).**

* Refined: `(a_0 − s_0 + 2θ_N) − (2a_0/3 − 2s_0 + 5θ_N/3) = (a_0 + θ_N)/3 + s_0`. This is `≥ 0`,
  since `a_0 ≥ −θ_N` and `s_0 ≥ 0`.
* Crude: `(a_0 − s_0 + 2θ_N) − (2a_0/3 + 5θ_N/3) = (a_0 + θ_N)/3 − s_0`. This is `≥ 0` by Step 4,
  and `= 0` iff `q_s³ = Y_col`.
* `Λ_c − ε_G = a_0 + q̃ + w_o + w + B_c − s_0 ≥ a_0 − s_0`.

This is (d). ∎

**Remark 2.1 (non-squarefree `s`).** Not needed, since `s` is squarefree. For general `s`, put
`s' = Π p^{⌈v_p(s)/3⌉}`. Then `s | v³` iff `s' | v`, and `q_{s'} ≥ q_s^{1/3}`. The count is
`≪ Y_col^{1/3}q_s^{−1/3}`, giving the exponent `2a_0/3 − 2s_0/3 + 5θ_N/3`. Its slack is
`(a_0 + θ_N − s_0)/3 ≥ 0`, because `q_s ≤ q_u ≤ Y_col`.

### 2.1 Changes from `n = 6` (manuscript l. 13572-13594), made explicit

| item | `n = 6` (manuscript) | `n = 3` (here) |
|---|---|---|
| vanishing rule (eq:gauss-local at `k = 0`) | `G(u,0) = 0` unless `u` is a sixth power | unless `u` is a cube (Lemma 4.A, Fact 0) |
| CRT phase | `R(p,u)^i χ_p(u)^{2i}`, modulus 1 | `χ_{u_1}(u_2)χ_{u_2}(u_1)`, modulus 1 (equal to 1 by I1) |
| support count | `O(Y_col^{1/6})` | `≤ C_0Y_col^{1/3}` crude; `≤ C_0Y_col^{1/3}/q_s` refined |
| `s`-bound (squarefree `s`) | `s_0 ≤ (a_0 + θ_N)/6` | `s_0 ≤ (a_0 + θ_N)/3` |
| exponent of `R_0` | `a_0/3 + 4θ_N/3 + ε_1` | `2a_0/3 + 5θ_N/3 + ε_1` (crude); `− 2s_0` refined |
| slack against `a_0 − s_0 + 2θ_N` | `≥ (a_0 + θ_N)/2 ≥ 0`, uses `a_0 ≥ −θ_N` | crude `(a_0 + θ_N)/3 − s_0 ≥ 0`, can be `0`; refined `(a_0 + θ_N)/3 + s_0` |
| numerical correction | `2θ_N` in `C_*ξ` | the same `2θ_N` (the crude route uses all of it, [I3-CTRL-theta]) |
| zero row and amplification | rows `hp⁶`; `0` never multiplied by a pool prime | rows `hp³`; `0·p³ = 0`, so `0` is still added only once, at the final ball |

At `n = 2`, only the refined count fits. The crude exponent there is `a_0 + 2θ_N > a_0 − s_0 + 2θ_N`
for `s_0 > 0` ([I3-CTRL-n2]). This is the transfer note's remark (CUBIC_FOURTH_MOMENT_TRANSFER.md
Sec. 3 item 3), confirmed.

## 3. Checks (`lemma_4i_checks.py`, output `lemma_4i_checks.out`)

| tag | what | arithmetic | result |
|---|---|---|---|
| [I0] | direct `x^{(Np−1)/3}` symbol agrees with (eis sextic symbol)² at `Np = 7, 7, 13, 19` | exact | PASS |
| [I1] | `q_u^{1/2}G(u,0) = Σ_x χ_u(x) = φ(u)·1[u cube ideal]`, brute force over all 131 moduli built from primes of norm 4 (inert 2, Fact-0 test only), 7, 7, 13, 13, 19, 25 (inert 5) with norm ≤ 2500, plus 6 larger ones (up to `2³·13³`): 10 cubes, 121 non-cubes | exact `Z[ω]` count vectors | PASS |
| [I1-CTRL] | sextic rule "`G(u,0) = 0` unless sixth power" at `n = 3` | exact | detected false (10 counterexamples, first `13³`) |
| [I1b] | `|G(u,0)|² = φ(u)²/q_u ≤ q_u` on cubes | exact integers | PASS |
| [I2] | for 6 squarefree `s` and `Y = Yv³`, `Yv ≤ 2·10⁴`: `q_s³ ≤ q_u` in all 19652 cube ideals with `s | u`; `max #{u}·q_s/Y^{1/3} = 0.70` | exact | PASS |
| [I2-CTRL] | `s = p³` non-squarefree: `q_s³ ≤ q_u` fails at `u = p³` | exact | detected |
| [I3] | exponent slacks of (b), (c) and the sextic l. 13584 inequality on 2600 rational grid points, `θ_N ∈ {0, 1/100, 1/10, 1/3}`; equality of (c) exactly at `s_0 = (a_0 + θ_N)/3` | exact `Fraction` | PASS |
| [I3-CTRL-n2] | crude count at `n = 2` exceeds the allowance (`a_0 = 1`, `s_0 = 1/4`) | exact | detected |
| [I3-CTRL-theta] | crude cubic route with correction `2θ_N − θ_N/100` fails at `s_0 = (a_0 + θ_N)/3` | exact | detected |
| [I4] | `sup_{|B| ≤ 1} Z^{−a_0}|Σ B G(u,0)|²` (`θ_N = 0`, `Z^{a_0} = Y`) against `Y^{2/3}/q_s²` and `Y/q_s`: max ratios 0.0214 and 0.0002 | floating point (labelled) | PASS (finite consistency, not a proof) |

Summary line of the run: `checks 6/6 PASS; failing controls detected 4/4`.

The checks are finite. [I1] verifies (a) on small moduli, [I2] the counting step, and [I3] the
exponent algebra. The proof in Sec. 2 does not depend on them.

## 4. Verdict and updated status line

**Verdict: proved (PROPOSED), in the corrected form of Sec. 1, with fixes F1-F4.** The SKETCH's
conclusion stands: the added row fits old-eq:2.7 with the `2θ_N` correction. The refined count has
positive slack `(a_0 + θ_N)/3 + s_0`. The manuscript-style crude count is exactly tight at
`q_s³ = Y_col`. This is unreviewed and not integrated.

Updated row for STATUS_END_OF_WAVE.md Table 2b (not applied there by this note):

    | R7 | Gauss-row zero `h = 0` (13572-13594) | Lemma 4.I (corrected statement, F1-F4) | LEMMA_4I.md (proved here, PROPOSED; checks 6/6, controls 4/4) |

With this row the end-of-wave count becomes 13 re-derived at `n = 3` (PROPOSED), 1 sketched and
unreviewed (R14, Lemma 4.K), and 1 replaced by (H-B) (R15). The route remains conditional on (H-A),
(H-B), Lemma 4.K and the correctness of Lemma 18.1 case 1. The SKETCH Sec. 4 entry for 4.I may be
relabelled "proved in LEMMA_4I.md (PROPOSED)". That edit is not made here.

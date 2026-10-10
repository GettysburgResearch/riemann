# Lemma 18.1 (`lem:plain`): line review of case 2 (positive slots), of Sec. 18.8, and of the interface with Prop. 19.2

```text
Status: REVIEW (bounded; external, unreviewed manuscript) + exact-rational ledger checks.
  Verdict: no wrong step found in case 2 or in Sec. 18.8. Taken with the two earlier notes, every
  proof line of Lemma 18.1 (l. 12602-14984) has been read by at least one bounded review, and no
  wrong step was found. This is NOT a certification. Lemma 18.1 still rests on black-boxed helper
  lemmas and imported theorems, listed in Section 6.
Scope: Lemma 18.1 of "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8" (OpenAI,
  30 Sep 2026). Read line by line:
  (a) case 2 (z > 0): prime estimates and floor (l. 12831-12938), positive-slot comparison
      (12945-13010), the sextic amplifier and its errors (13456-13594), the diagonal and width drop
      for the four norm types (13631-13661, 13790-13800), the positive-slot child: (3.14),
      clipping, F_act, greedy slot removal, (3.16) and the edge cost (14180-14305), and the Theta
      rows with slots (14312-14778);
  (b) Sec. 18.8, the completion of the finite induction (14779-14984);
  (c) the interface: the hypotheses of Lemma 18.1 as Prop. 19.2 invokes them (15095-15446).
  The rest of 12477-14984 was reread for context. Not reviewed: the proofs of Lemmas
  smooth-calculus (4.5; a parallel agent is reviewing it), kernel-seminorms (4.7) and
  logarithmic-control (4.9), which are used here as black boxes, and the row-count arithmetic of
  Prop. 19.2 (the junction; a parallel agent is checking it).
Exact sources or dependencies:
  pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6; standalone/2026-10-07-openai-quasi-riemann-
    import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
    sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed here).
    All line numbers refer to this file.
  Earlier notes: reviews/LEMMA18_1_REVIEW.md (case 1 structure, ledger 14/14, numerics) and
    reviews/LEMMA18_1_COMMON_SUPPORT.md (common-support allocations, 24/24). Both were read in
    full, with their scripts; neither script was modified.
  New code: reviews/lemma18_case2_ledger.py (sha256 7a7c0d2d...e960a3f9). It uses only Python's
    fractions module, sympy and numpy.
What was actually run (nice -n 10, one process at a time; logs in the session scratchpad):
  python3 -I lemma18_case2_ledger.py   -> 50/50 PASS, 17 of them failing controls detected (24 s)
  python3 -I lemma18_ledger.py         -> 14/14 (rerun unchanged, sha256 fc965201...7f65a3c, 6 s)
  python3 -I lemma18_support_checks.py -> 24/24 (rerun unchanged, sha256 509a3dbb...2f2c7b, 24 s)
Smallest remaining gap: what remains is imported. (i) Lemma 4.5 (smooth calculus): the Fourier
  separation and parameter-Sobolev steps that every transform and the Prop. 19.2 application go
  through. (ii) Lemma 4.9 (logarithmic control), which is the whole content of the pointwise slot
  bound (old-eq:3.5) that the greedy removal spends. (iii) Lemma 4.7 (kernel seminorms).
  (iv) Standard imported theorems (Section 6). The proof needs an exact balance per edge
  between the amplifier gain and the greedy cost (Section 3, point Z4). That balance holds, so
  any extra loss there of fixed size, or proportional to sigma, would break case 2.
```

RH is unsolved. This note does not prove or disprove any zero-free region, and it does not certify
Lemma 18.1 or the 7/8 claim. The mechanical checks verify displayed algebra only (affine identities,
local inequalities, finite Gauss data). They do not test analytic estimates or whether the ledgers
describe the analysis correctly.

## 0. What case 2 adds to case 1

Case 2 (paper.tex l. 12556-12566) bounds `Σ_{k ∈ R_z} |S(n1) S(n2) Q|² ≪ Z^{M+ε}`, where:

* `R_z` is the rows whose inducing character lies outside `Θ`;
* `Q` is a product of short prime polynomials ("slots") of lengths `z_i ≤ η`, with total
  length `z`;
* the lengths satisfy `A + (6κ−1)z ≤ M` (old-eq:3.9), with `A = n1 + n2 + z` and
  `κ ∈ [3/4, 1]`;
* when `κ < 1`, the zero-free hypothesis `β_* ≤ (1+κ)/2` is assumed.

The proof runs the same two-transform induction as case 1, with three additions:

1. **Pointwise slot bound (old-eq:3.5).** `|Q|² ≪ Z^{κz+ε}` on rows outside `Θ`. Under
   `β_* ≤ (1+κ)/2`, Lemma `logarithmic-control` gives each slot `P^{κ/2+e}`.
2. **Sextic amplifier.** Each first-transform Gauss norm is averaged over rows `h → h p⁶`, with
   `p` in a prime pool of size `Z^{σ/3}`. The main term gains `Z^{−σ/3}`. The errors extract
   `p¹`, `p⁶` or `p⁷`.
3. **Greedy slot removal.** A child that violates (3.9) loses whole slots to the pointwise bound
   until it satisfies (3.9) again. The cost is `κ d_z ≈ F_act/6`, and the amplifier gain pays
   for it.

Everything else is shared with case 1. That includes the centering, the `Θ`-row count, the
lattice cancellation and the common-support allocations, which the two earlier notes checked.

## 1. Case 2, line by line

### 1.1 Prime estimates, floor and comparison (l. 12831-13010)

| step (lines) | claim | re-derivation | check |
|---|---|---|---|
| (old-eq:3.4)-(3.5), 12833-12900 | `\|Q_ω\|² ≤ C Z^{κz+ε1}` on `R_z` | Shift the Mellin contour to `Re s = s_κ + e`, with `s_κ = (1+κ)/2 ≥ β_*`. `β_*` is defined over all primitive finite-order Hecke characters (l. 379), so it covers every child character. A slot character `ψϑ_ij` is nonprincipal because `ψ ∉ Θ`. Each slot is `P^{−1/2} P^{s_κ+e} = P^{κ/2+e}`. The displacement costs exactly `2ez` in the squared exponent. | the input is Lemma 4.9 (black box) |
| `κ = 1`, 12893 | no zero-free hypothesis is needed | absolute prime counting gives `\|Q_i\| ≤ P^{1/2}` | — |
| floor (old-eq:3.6), 12926-12938 | `z ≤ M/(6κ) ≤ 2M/9` and `κz ≤ M/6` | `A ≥ z` and (3.9) give `6κz ≤ M`. The extra terminal exponent at the floor is at most `ρ/6`. | K2 |
| `z < M/21`, `A − z > 2L`, 12947-12950 | needed for the comparison | `(6κ−1)z < M/6` with `6κ − 1 ≥ 7/2`, so `z < M/21`. Then `A − z > 33M/42 > M/2`. | K1 |
| (old-eq:3.11), 12956-12966 | `A_comp ≤ 3M/2 − A + 2z + ξ` | `b + (M − (A−z−b) + ξ) + z = M − A + 2b + 2z + ξ`, with `b ≤ L = M/4` | — |
| (eq:comparison-uncentered-margin) | `A_comp ≤ 23M/30 + ξ`; `A_comp + (6κ−1)z ≤ 14M/15 + ξ` | Exact suprema over `κ ∈ [3/4,1]`, `A ∈ (5M/6, M]` and `z ≤ (M−A)/(6κ−1)` are **16/21** and **13/14**. They are approached at `κ = 3/4`, `A ↓ 5M/6`. So the true margins are `M/14`, which beats the stated `M/15`. | K1 (control K2c: `κ = 1/2` loses the margin) |

The comparison product has the same rows, slots and width. It therefore calls the uncentered
positive-slot stage at the same width, which is proved first within the band. Its margin
`M/15 − ξ` is positive because `ξ < ρ/30`.

### 1.2 The sextic amplifier (l. 13456-13594)

| step (lines) | claim | re-derivation | check |
|---|---|---|---|
| pool, 13456-13474 | `\|P\| = Z^{ℓ*+o(1)}` with `ℓ* = σ/3`, and the pool is disjoint from every live slot window | Use the prime ideal theorem [TZ, Thm 1.1] (imported). The pool is disjoint once `Z^{ℓ*−η} > 2 max b_i`. The gap `ℓ* − η > σ/6` needs `η < σ/6`, which (old-eq:2.1i) supplies. Removing the `O(log Z)` primes dividing `h`, `s` or the frozen support leaves `\|P_h\| ≥ \|P\|/2`. | A2 (+ control) |
| CRT factor, 13476-13480 | `G(p^i u, h) = R(p,u)^i χ_p(u)^{2i} G(p^i,h) G(u,h)` | CRT gives `χ_{p^i}(u) χ_u(p^i)`. Reciprocity `χ_u(p) = R(p,u) χ_p(u)` then gives the formula. This matches support-check B3/B4. | — |
| invariance, 13480-13482 | `G(u, hp⁶) = G(u, h)` for `(p,u) = 1` | Substitute `x → x p^{−6}`, which gives a factor `conj χ_u(p)⁶ = 1` because the character has order 6. | G3; control G3c (`p⁵` fails) |
| local change, 13482-13485 | `h → hp⁶` changes only `i = 1, 6, 7` | From eq:gauss-local with `v_p(h) = 0` against `v_p(hp⁶) = 6`: the case `6 ∤ a` needs `v = a − 1`, giving `{1, 7}`; the case `6 \| a` needs `v ≥ a − 1`, giving `{6}`. | G1 exact for `a ≤ 36`; G2 brute force in `Z/7^a` (`a ≤ 8`) and `Z/13^a` |
| Jensen, 13495-13509 | `\|H(h)\|² ≪ \|P_h\|^{−1} Σ_p {\|H(hp⁶)\|² + Σ \|c_{p,i}\|² \|H_{p,i}\|²}` | `H(h) − H(hp⁶)` is a sum of boundedly many extracted terms, with `≤ 8` allocations of `p^i` between `l1` and `l2`. A slot cannot take `p`, because `p` lies outside every live window. Jensen's inequality then applies with a bounded constant. | — |
| main term, 13505-13513 | factor `Z^{−ℓ*}`; ball of length `K + J_+ + 2σ` | An output row `h' = hp⁶` has at most `(K+2σ)/(6ℓ* − o(1))` representations. Its norm is at most `Z^{K+6ℓ*} = Z^{K+2σ}`. | A1 |
| coefficients, 13515-13531 | `\|c\|²` equals `P^{−1}`, `(1−P^{−1})²`, `P^{−1}`; the row phase is `conj χ_p(h)` for `i = 1, 7` and absent for `i = 6` | Old/new normalized values are `(1, 0)`, `(0, P³(1−1/P))` and `(0, \|·\| = P³)`. The central factors are `P^{−1/2}`, `P^{−3}` and `P^{−7/2}`. | G1, G2 (phases checked for `h = 2, 3, 5`) |
| (old-eq:2.9)-(2.10), 13533-13567 | `(w, w_o) = (iℓ_p, e_iℓ_p)`; squared coefficient `= Z^{−w_o}`; `w ≤ 7σ/3` | For `i = 6`, `χ_p(u)^{12} = 1_{(u,p)=1}` is already the extraction puncture, so `e_6 = 0`. `ℓ_p ≤ ℓ*` gives `w ≤ 7ℓ* = 7σ/3`. | G1b, A3 |
| errors, 13537-13567 | frozen `p`; `ℓ = 0`; `g = J_+ + σ`; average with no prime-count factor | The bound is uniform in the frozen `p`, so the average over `p` costs nothing. The eligibility restriction is dropped only after positivity. | — |
| added row zero, 13569-13594 | `Z^{a0/3+4θ/3} ≤ Z^{a0−s0+2θ}` | `G(u,0) = 0` unless `u = v⁶`. Then `s \| u` forces `s⁶ \| u`, so `s0 ≤ (a0+θ)/6`. The difference of the two exponents is at least `(a0+θ)/2 ≥ 0`. | A4; control A4c (without `s⁶ \| u`) |

### 1.3 Diagonal and width drop for the four norm types (l. 13631-13661, 13790-13800)

The four norm types are the amplified main term and the errors at `i = 1, 6, 7`. For each:

* **(old-eq:2.12).** The identity holds for general `w, w_o, g, ℓ` (A6).
* **Diagonal inequality.** The bound `≤ A − M + (g − J_+ − ℓ) + δ_fr,1` uses
  `−D0 − w_o + J_+ ≤ δ_fr,1`. When `J ≥ 0` this equals `−c − 2w`; when `J < 0`, `D0 ≥ −δ_fr,1`.
* **Increments.** The increment `g − J_+ − ℓ` is `2σ − σ/3 = 5σ/3` for the amplified main term
  and `σ` for the errors (A7).
* **Case 2 needs nothing extra here.** (3.9) gives `A ≤ M`, so the diagonal is the terminal loss
  `5σ/3`.
* **Control A7c.** Without the `Z^{−ℓ*}` density gain, the amplified ball would cost `2σ`.
* **Width drop.** (old-eq:2.13) `M' = M + J − g − g2 + t2 ≤ M − σ` holds for all four types (A5,
  A8). The amplified type drops by `2σ`.

### 1.4 The positive-slot child (l. 14180-14305)

| step | claim | re-derivation | check |
|---|---|---|---|
| (old-eq:3.14) identity | `(A'−M') − (A−M) = g + w − d − c2 − (K0−K) − w_o + g2 − t2` | Substitute (2.13) and `a0 = A − c − w`. The `d2` side is the same with `c2 ↔ d2`. | C1 |
| (old-eq:3.14) bound | `≤ 6(w+ℓ) + δ_fr,1` | Use `g2 − t2 ≤ c2` and `J_+ ≤ (d + K0 − K) + δ_fr,1`, because `J ≤ d + (K0−K)`, `c ≥ 0` and `2w ≥ w_o`. Amplified main term: `g − d − (K0−K) ≤ 2σ + δ = 6ℓ* + δ`. Errors: `w − w_o + σ + δ ≤ 6w + δ`, using `σ ≤ 5w + w_o`. | C2: max of (lhs − rhs) is 0, attained |
| `σ ≤ 5w + w_o` | needs `ℓ_p ≥ σ/6` at `i = 1` | Equality holds at `ℓ_p = σ/6`. The pool actually has `ℓ_p ≥ ℓ* − log2/log Z`, so the true slack is about `σ`. This is not a tight point. | C3; control C3c (`ℓ_p = σ/7`) |
| (eq:centered-clipped-rectangle) | `A_clip = α + e − r̃ + π = α + e + π0 − r_clip`; `r_clip = r̃ − (π − π0) ≥ 0` | Use `Σ x_i + Σ_{I_j} z_i = α + e` and `(y)_+ = y + (−y)_+`. | C4 (exact, random) |
| (eq:centered-clipped-shell) | paired count and coefficients `≤ 2θ_N` | Use `r̃_j + ω_j ≥ t_−`, `\|e_j + ω_j\| ≤ θ` and `π_j ≤ θ`. | C5; control C5c |
| `F_act` chain, 14217-14240 | `F_act ≤ 6(w+ℓ) + δ_fr,1 + 2θ_N` | Uses `z' ≤ z` and `6κ − 1 ≥ 0`. The parent satisfies (3.9), `M'_act ≥ M'` and `r̃ ≥ 0`. Mask deletion only lowers the affine expression. | C6 (24 000 sides from raw data; max of (F − bound) is 0) |
| greedy, 14254-14275 | `d_z ≤ min{z_act, F/(6κ) + η}` and `κ d_z ≤ F/6 + κη` | The prefix stops at the first slot to reach `F/(6κ)`, so only one slot overshoots, by at most `η`. Removing length `d` lowers `A + (6κ−1)z` by exactly `6κd`. | C7 (simulated on exact slot lists); C9 symbolic |
| (old-eq:3.16) | `κ d_z ≤ Δ_child + δ_fr,1/6 + θ/3 + η` | `F/6 ≤ w + ℓ + δ/6 + θ/3` and `Δ_child = b2 − p2 + w + B_c + ℓ ≥ w + ℓ` (uses `κ ≤ 1`) | C7 |
| edge cost (eq:centered-child-edge-cost) | `δ_fr,2 + δ_fr,1/6 + η + 7θ/3` | `(M'_act − M') + (3.16 excess) + 2θ` (clipped shell). Cauchy-Schwarz takes the geometric mean of the two sides, so `η` is not doubled. | C8, C10 |
| induction call | the remaining product satisfies (3.9) at width `M'_act ≤ M − σ + ξ` | The child is in an earlier positive-slot band, already completed (uncentered and centered). If every slot is removed, the completed unrestricted zero-slot case applies. The child's slots keep their coefficient class, and its rows stay outside `Θ`. | — |

The child slot polynomial that (3.5) receives is the full prime polynomial, for four reasons:

* the `𝔱`-allocation either freezes a slot whole or leaves it unchanged;
* the masks are erased first by (old-eq:2.1a) and (eq:prime-mask-erasure);
* the surviving slot carries only the child's whole-product character, its original `ν_i` and one
  norm power, which acts as a pure twist of polynomial height in (3.5);
* no prime label is frozen.

So (3.5) applies as stated.

### 1.5 Theta rows with slots (l. 14312-14778)

* **Live slots on `Θ`-rows.** They are bounded by volume, `O_N(∏ P_i)`. That volume is the `e_j`
  factor in (eq:centered-raw-normalization), and `|e_j| ≤ θ_N`, so no fixed power is lost.
* **Amplifier errors.**
  * `w` enters the centered saving through `v = c + w + min(c2, d2)` and `F_1 ≥ 2(c+w)/3 − 3σ`
    consistently.
  * At `J < 0` the actual `F_1` gives only `2c/3 + w/3`. Together with `−5(g − J_+)/6 + ℓ`, this
    costs at most `29σ/18 < 22σ/9 < 3σ`.
  * That cost is terminal (K3, Z1b).
* **(old-eq:2.19).** In case 2 the maximum over `v` is `A − M = −(6κ−1)z ≤ 0`. The proof does not
  use this extra slack, which goes to zero with `z` (Z1).

## 2. Sec. 18.8, line by line (l. 14779-14984)

| claim (lines) | re-derivation | check |
|---|---|---|
| strict drop, 14782-14806 | `M' ≤ M − σ` by (2.13). The frequency, support and clipping corrections are at most `C_*ξ < σ/4` by (2.1i), so the drop is at least `3σ/4 > σ/2`. A child therefore falls at least two bands (of length `σ/4`) lower. | S2 |
| depth `D = 2 + ⌈2M_max/σ⌉` | Widths stay `≥ 0` and drop by `≥ σ/2`, so the number of strict calls is `≤ 2M_max/σ ≤ D − 2`. The worst chain attains `D − 2`. | S3 |
| no same-band cycle | A comparison calls the uncentered stage at the same width, which comes earlier in the band order. Each norm has one amplification, and errors are not amplified again. (3.16) is used once per natural child. Reflection to the padded core happens at the same width as preprocessing. | read |
| (old-eq:2.1j) | Since `0 ≤ 7/2 ≤ 6κ − 1 ≤ 5`, `\|Δ(A + (6κ−1)z − M)\| ≤ \|ΔM\| + \|ΔA\| + 5\|Δz\|`. | S1 (control `κ = 11/10`) |
| `C_*` independent of `N` | Every slot-subset error is aggregated into one `θ_N` (eq:centered-aggregate-support). The ledgers are affine in a fixed list of 19 aggregate lengths with numerical Lipschitz constants. The greedy overshoot is one `η`, not `Nη`. | read; C8 |
| analytic separations | The radial kernels go through Lemma 4.7, uniformly in `R_sc`. The height orders go through Lemma 4.5; they raise seminorm orders, not exponents of `Z`. | black boxes |
| (old-eq:2.1i) and `T_term` | `T_term = ρ + δ + ρ/6 + 3σ + 5σ/3` dominates each terminal loss: the zero-slot floor `ρ + δ`, the positive floor `+ρ/6`, the diagonal `δ + 5σ/3`, and the exceptional `3σ`, or `δ + 3σ` in the centered core. The constraints `ξ < δ/2, ρ/30, σ/(4C_*), ε/(16C_*D)` and `η < σ/6, ε/(16C_*D)` are jointly satisfiable in that order, and `η` does not depend on `N`. | S2 for `ε ∈ {1/10, 1/100, 1/1000}` |
| envelopes `E_d = T_term + (d+1)C_*(η+ξ+ε0)` | The recursion is `E_d = E_{d−1} + C_*(η+ξ+ε0)`. Terminal losses enter as a maximum, once per branch. The edge cost `≤ (35/24)ξ + η ≤ C_*(ξ+η)`, using `θ_N < ξ/8` and `δ_fr < ξ`. The largest path error is `≤ T_term + C_*D(η+ξ+ε0) < ε/4 + 3ε/16 < ε`. | S2 (for example, `E_{D−2} = 0.337ε` at `ε = 1/1000`); controls S2c1-c3 |
| masks stay polynomial, 14952-14963 | Each stage adds a bounded total length of frozen primes, over at most `D` stages. On `Θ`-rows they merge into one `𝔑_*`. | read |
| physical remark, 14975-14984 | With `q = 0` and sixth-power-free `u`, a prime outside `S` with valuation 1 to 5 makes the character ramified there, so it is outside `Θ`. | read; used in Section 4 |

**Why the loss bookkeeping closes.** Every per-edge cost is `O(ξ + η + ε0)`. Every `O(σ)` or
`O(ρ, δ)` loss is terminal, and there is one terminal loss per branch. The three controls show
what would happen otherwise:

* a per-edge loss of `σ/6` would reach `(D−2)σ/6 ≈ M_max/3` (S2c1);
* summing the terminal losses along a branch would give `(D−1)T_term ≈ 35` at `ε = 1/100` (S2c2);
* `ξ = σ/C_*` would remove the strict drop (S2c3).

## 3. Zero-slack points

The earlier notes identified three zero-slack points, all at the Theta-row stage. Case 2
introduces a fourth, of a different kind.

| point | where | what case 2 / Sec. 18.8 add there | check |
|---|---|---|---|
| Z1: (2.19) at `v = L` | 14759-14768 | No fixed loss. The amplifier costs only the terminal `O(σ)` inside `3σ`. In case 2 there is extra slack `(6κ−1)z`, which the proof does not use. | Z1, Z1b; control Z1c |
| Z2: `F_2 = 2b2/3` at nonunit multiplicity-one primes | 14504-14524 | A slot frozen at such a prime is counted in `c2` through `Q_plain`, `∏_F q_p`, so the local data are the same. The paper keeps `f`, not `2f`, which leaves `f/6` unused. | Z2; control Z2c |
| Z3: `F_1 = 2c/3` at `J < 0` | 14470-14495 | Amplifier errors add `+w_o ≥ 0` and the main term adds `+ℓ ≥ 0`. The `w/3` shortfall is terminal (Section 1.5). | Z3, K3 |
| **Z4 (case 2, per edge): amplifier gain = greedy cost** | 13505-13513, 14183-14275 | In the amplified main term `F_act ≤ g − J_+ = 2σ = 6ℓ*`, and the greedy cost is `F_act/6 = ℓ*`, which equals the amplifier gain `ℓ` in `Δ_child`. The balance is exact. Equality holds at `c = d = 0`, `K ≤ K0`, `c2 = d2 = g2 = p2 = V`, `t2 = 0`, `z' = z` and `A + (6κ−1)z = M`. What remains is `O(θ_N + δ_fr + η)` per edge. | Z4; C2 and C6 attain 0; controls Z4c1-c3 |

**Z4 has stricter zero slack than Z1-Z3.**

* At Z1-Z3 any loss of size `O(σ)` is harmless, because it is terminal.
* At Z4 any per-edge excess of size `λσ` accumulates over `D − 2 ≈ 2M_max/σ` edges to
  `2λM_max`, a fixed power.
* The balance is structural. The `6` in the affine coefficient `6κ` of (3.9) equals the `6` in
  the amplifier `h → hp⁶`: the ball grows by `6ℓ*` and the gain is `ℓ*`.
* The three mutations show the balance is load-bearing. With coefficient `5κ` (Z4c2), with no
  amplifier (Z4c1), or with half the density gain (Z4c3), each edge would lose a fixed multiple
  of `σ`, and that loss would accumulate.
* In the paper, the only per-edge losses at Z4 are bounded constants and powers of `log Z`:
  Jensen's constant, `|P_h| ≥ |P|/2`, the bounded representation count, and the `Z^{o(1)}`
  prime density. These fall in the `ε0` shares.

## 4. Interface: hypotheses of Lemma 18.1 versus their use in Prop. 19.2 (l. 15095-15446)

| hypothesis of Lemma 18.1 | how Prop. 19.2 meets it | status |
|---|---|---|
| `κ ∈ [3/4, 1]`; `β_* ≤ (1+κ)/2` when `κ < 1` | `κ = 2β_* − 1 = 3/4 + 2Δ ∈ (3/4, 5/6]` (l. 15097-15106), so the hypothesis holds with equality. (3.4) uses `s_κ + e` with `e > 0`, so equality is enough. | consistent |
| rows `k ∈ O`, `0 < q_k ≪ Z^m`; `ψ_k(n) = τ(n) χ_n(k)` with `τ` fixed and `M = m + q` | Rows are the physical `u` with `q_u ≍ U`, base `Z := U`, `m = 1`. After conjugating the whole product, `τ = conj ν` is a fixed-ray character with no moving radical, so `q = 0` and `M = 1` (l. 15152-15163, 15243-15245). The bin is a subset of the rows, and positivity extends it. | consistent |
| case 2 rows `R_z`: inducing character outside `Θ` | The rows are sixth-power-free with `q_u` large. They ramify at a prime outside `S`, which puts them outside `Θ = ⟨η, T̂⟩`, whose conductors lie in `S` (l. 3334-3340, 15168-15170, 14975-14984). | consistent |
| case 1 rows `R_0`: nonprincipal; lengths unrestricted | Used for `m ≥ 1/2` and at zero plain capacity. Physical rows are nonprincipal for the same reason as above. | consistent |
| slots `Z^{−z_i/2} Σ_p ψ(p) ν_i(p) W_i(q_p/Z^{z_i})`, `ν_i ∈ span Θ` fixed, disjoint supports, primes outside `S` (old-eq:1.2) | The coefficient is `ν(p) 1_T(p) = \|T\|^{−1} Σ_θ (νθ)(p)` with `ν ∈ Θ` and `T̂ ⊂ Θ` (l. 15137-15160). The profile is `W_i(y) y^{z_phys − 1}`. Windows are disjoint and exclude `S` (l. 6873-6880). | consistent |
| (3.9): `n1 + n2 + 6κz ≤ M` | Two copies of `S_m` give `2m + 6κz ≤ 1`, so the capacity is `z_P(m) = (1−2m)/(6κ)` (l. 15173-15181). | consistent |
| `z_i ≤ η`, with `η` depending only on `ε` and the bounded ranges, uniform in `κ` and independent of the slot count `N` | The Prop chooses "the capacity decrements and slot mesh using only `ε, Δ` and the bounded real ranges" (l. 15197). Lemma 18.1's `η` (old-eq:2.1i) does not depend on `N`. That independence is what lets the prime supply `8/39 > 7/37` be built from many short slots. The slot lengths must be fixed after `η`, which the order of choices allows. | consistent |
| bounded real length ranges; finite seminorm and height orders | Rowwise witness parameters go through Lemma 4.5 (Sobolev) before the lemma is applied (l. 15163-15168). | consistent; Lemma 4.5 is black-boxed |

No hypothesis is used beyond what Lemma 18.1 states. Not checked here: the count arithmetic
`1 − 2δm − 2qz` and the junction with the witness spikes (parallel agent).

## 5. Mechanical checks (`lemma18_case2_ledger.py`)

The output below is shortened. The full log has 50 lines: 33 checks and 17 failing controls,
each control detected.

```
PASS G1  eq:gauss-local: h -> h p^6 changes only valuations 1,6,7; |c|^2 = P^-1,(1-1/P)^2,P^-1
PASS G2  explicit Gauss sums in Z/7^a (a<=8), Z/13^a (a<=5); phases conj chi(h) at 1,7   max rel dev 4.3e-15
PASS G3  G(u, h p^6) = G(u, h)                    (control: p^5 detected)
PASS A1-A8 amplifier ledger, (2.12) for 4 norm types (increments sigma, 5sigma/3), (2.13) drop
PASS C1-C2 (3.14) identity both sides; inequality, max(lhs-rhs) = 0 attained
PASS C3  w - w_o + sigma <= 6w needs l_p >= sigma/6 (actual pool: slack ~ sigma)
PASS C4-C5 clipped identities; paired shell <= 2 theta_N
PASS C6  F_act <= 6(w+l)+delta_fr1+2theta_N, 24000 sides, max(F-bound) = 0
PASS C7-C10 greedy prefix, (3.16), edge cost (eq:centered-child-edge-cost)
PASS Z1-Z4 zero-slack points (Z4: amplifier gain = greedy cost exactly)
PASS K1  sup A_comp = 16/21 < 23/30; sup A_comp+(6k-1)z = 13/14 < 14/15
PASS K2-K3 (3.6); F_1 >= 2(c+w)/3 - 3sigma with actual g, l
PASS S1-S3 (2.1j); (2.1i) choices, T_term, E_{D-2} < eps; depth <= D-2
50/50 PASS (17 of them failing controls detected)
```

**Arithmetic used.**

* Exact rationals (`fractions.Fraction`) throughout, with sympy for the identities.
* Floating point only in G2 and G3, which evaluate explicit sextic Gauss sums with tolerance
  `1e-9`.

**Sampling.** Random parameter tuples satisfy all stated side conditions. A tenth to a seventh
of them are forced into the tight configuration, so that the bounds are attained.

## 6. Verdict for Lemma 18.1 as a whole

**No wrong step was found, and every proof line has now been read.** The three bounded reviews
together cover l. 12602-14984:

| part | lines | note | result |
|---|---|---|---|
| reductions, reflection, induction order, comparison | 12602-13010 | REVIEW; this note (positive-slot parts) | no error; 14/14 + K1-K2 |
| centered coefficient; first transform, coprime model and ledgers | 13012-13191, 13350-13410 | REVIEW, COMMON_SUPPORT | no error |
| common-support allocations, both transforms | 13192-13349, 13686-13933 | COMMON_SUPPORT | no error; 24/24 |
| Gauss-row enlargement (zero-slot and amplifier) | 13411-13594 | REVIEW (zero-slot); this note (amplifier) | no error; G1-G3, A1-A4 |
| second transform: diagonal, children, coefficient lemma, clipping | 13596-14310 | all three | no error; A5-A8, C1-C10 |
| Theta rows, lattice cancellation, (2.19) | 14312-14778 | REVIEW, COMMON_SUPPORT; this note (slots) | no error; Z1-Z3 |
| completion of the induction | 14779-14984 | REVIEW (summary); this note (line by line) | no error; S1-S3 |

**What remains unreviewed.** The following inputs are imported. None was re-proved by the three
notes.

1. **Black-boxed helper lemmas.**
   * Lemma 4.5, `smooth-calculus` (l. 1123). It covers logarithmic Fourier separation with
     common measures, the parameter-Sobolev bound and the late Fourier tail. A parallel agent is
     reviewing it.
   * Lemma 4.7, `kernel-seminorms` (l. 1347). It gives radial kernel decay uniform in `R_sc`,
     used for the localization tails and the separation.
   * Lemma 4.9, `logarithmic-control` (l. 1531). It gives `L'/L ≪ log` on `Re s ≥ β_* + v`. In
     case 2 this is the whole content of (old-eq:3.5), the bound the greedy removal spends.
2. **Other paper lemmas used as stated.** These were read as statements only, or checked only
   numerically on small cases.
   * Lemma 4.8, `hecke-strip-growth`: the functional equation and entireness used for
     reflection.
   * Lemma 4.10, `deleted-euler-factors`: the mask masses.
   * Lemma 4.1, `fixed-numerator-ray`.
   * Lemma 4.4: sextic reciprocity and the fixed Gauss phase. Support check B4 confirms it on
     3298 pairs.
   * The finite correlations of Sec. 13: `prime-power-fourier` (eq:gauss-local; G1/G2 here),
     `full-correlation` and `complete-support-correlation` (support checks E, F).
3. **Imported standard theorems.**
   * The prime ideal theorem in ray-class form [TZ, Thm 1.1], for the pool size.
   * Lattice Poisson summation.
   * Rankin's bound and polynomial-size Euler products.
   * The `O(Y^{1/2+ε})` count of powerful ideals.
   * Divisor bounds `τ_{N+2}(v)^C, C_N^{ω(v)} ≪ q_v^a`.
4. **Not tested by any of the three notes.**
   * The analytic estimates themselves: Fourier-measure `L¹` norms, tails, and the actual size
     of the prime density.
   * Whether each displayed ledger describes the analysis. This was read, not formalized.
   * The downstream junction in Prop. 19.2 (parallel agent).

**Assessment.**

* At the level of three bounded reviews, Lemma 18.1 is consistent. Every displayed identity and
  inequality that could be mechanized holds, 88 checks in all (14 + 24 + 50).
* The tight points close exactly as the paper claims: Z1-Z3 at the Theta stage and Z4 per edge
  in case 2.
* This is still not an independent expert certification. Case 1 alone would be a new
  unconditional Lindelöf-on-average fourth moment for a sextic family (Section 1 of
  `LEMMA18_1_REVIEW.md`).
* Before Prop. 19.2 and the 7/8 claim rely on Lemma 18.1, an expert should check the black boxes
  in items 1-2, above all Lemma 4.5, through which every Fourier separation passes.

## 7. Files

* `reviews/lemma18_case2_ledger.py`: the checks in Section 5 (new).
* `reviews/LEMMA18_1_REVIEW.md` and `reviews/LEMMA18_1_COMMON_SUPPORT.md`, with
  `lemma18_ledger.py` and `lemma18_support_checks.py`: the earlier notes and their scripts
  (unchanged; rerun: 14/14 and 24/24).

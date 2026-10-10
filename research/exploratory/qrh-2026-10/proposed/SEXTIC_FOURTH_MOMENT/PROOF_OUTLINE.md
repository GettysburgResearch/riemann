# Proof outline: Lemma 18.1, case 1 (condensation of the Sep 30 manuscript)

```text
Status: PROPOSED proof outline, an editorial condensation of an IMPORTED external proof. It adds no
  mathematics and strengthens nothing. Each step cites paper.tex lines and the bounded agent
  review that read it. Simplifications are marked [S1]-[S7] and listed at the end.
Scope: the proof of case 1 (z = 0) of Lemma 18.1 (paper.tex 12531-12579), lines 12602-14983.
  Case-2-only steps are named, not condensed.
Exact sources or dependencies: paper.tex at pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
  SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3; reviews L18a, L18b,
  L18c, L13 and SEC4 at c8515d4ea045e7b685f53feb6dd801bf0f529211 (README.md §1, §6)
What was actually run: nothing beyond README.md and CHECKS.md. Section headings and key displays
  were re-read from the source for this outline. The step contents follow the reviews.
Smallest remaining gap: the centred Theta-row estimate, Step 7 (README.md §8)
```

RH remains unsolved. This outline is a reading aid for an independent reviewer. It is not a
substitute for the manuscript, and it is not itself reviewed. Where it and `paper.tex` differ, the
manuscript governs. Review labels: **L18a** = `LEMMA18_1_REVIEW.md`, **L18b** =
`LEMMA18_1_COMMON_SUPPORT.md`, **L18c** = `LEMMA18_1_CASE2_SEC188.md`, **L13** =
`SEP30_L13_L45_REVIEW.md`, **SEC4** = `SEP30_SEC4_REVIEW.md`, all in `../../reviews/`. Check IDs
(A3, D, L4, ...) refer to the scripts in [CHECKS.md](CHECKS.md).

## 0. Notation (README §2.1; lines 557-760, 6919-7004, 12477-12530)

* Rows `k ∈ O` with `0 < q_k ≪ Z^m`; coefficients `ψ_k(n) = τ(n)χ_n(k)`; moving radical `≤ Z^q`;
  `M = m + q`.
* Plain sums `S(n_i) = Z^{−n_i/2} Σ_l ψ_k(l) W_i(q_l/Z^{n_i})`; `A = n_1 + n_2` (case 1).
* `X_i = Z^{n_i}`, `H = Z^m`, `X = Z^A`.
* "Natural" character: its zeros are exactly its conductor primes, its redundant row and moving
  primes, and `S` (12604-12609).
* `ξ, η, ε_0` are per-stage losses; `ρ` (width floor), `σ` (width step) and `δ` (padding) are
  terminal losses; `C_*` is a numerical Lipschitz constant; `θ_N` is an aggregate support error
  (14865-14890).

## Step 1. Fixed masks (12602-12676; L18a §2.1)

* Delete each extra puncture by Möbius inversion (old-eq:2.1a): `S_{k,𝔑}(X) = Σ_{d|𝔑} μ(d)ψ⁰_k(d)
  q_d^{−1/2} T_k(X/q_d)`.
* The divisor mass is `Σ_{d|𝔑} q_d^{−1/2} ≪ Z^{ε_1}` (old-eq:2.1b, via Lemma 4.10).
* Minkowski reduces the lemma to the *natural* assertion at the same width with an arbitrarily
  small loss. The inducing character is unchanged and lengths do not increase.

## Step 2. Reflection and the padded core (12677-12830; L18a §2.1)

* **Conductor bound** (old-eq:2.1c): `C_k q_{𝔑_{0,k}} ≪ Z^M`, where `C_k = 3Q_k/(2π)²`. Each good
  prime is tame and is counted once, in the conductor or in the redundant radical. The `S`-part
  ranges over a fixed finite ray family (Lemma 4.1).
* **Functional equation** (Lemma 4.8): the normalized sum at `X` equals the root number (modulus
  one) times the conjugate sum at `C_k/X`, with profile `𝓜W^♯(s) = 𝓜W(1−s)Γ(s)/Γ(1−s)`. The
  redundant Euler factors are deleted before reflection and restored as a geometric series of
  mass `Z^{ε_1}` (old-eq:2.1d).
* After annular truncation, a reflected length satisfies `n_ref ≤ M − n + ξ`
  (eq:centered-reflection-length, 12803).
* For `z = 0`, reflect each factor longer than `M/2` once. This gives the **padded zero-slot core**
  (old-eq:2.1h): `n_i^* ≤ M/2 + ξ`, `A^* ≤ M + δ`.
* Row-dependent reflected scales are handled by a rowwise supremum over `O((log Z)²)` unit boxes
  (Lemma 4.5).

So case 1 reduces to the padded core. [S1] This outline omits the exact rules for clipping
subunit scales (12772-12796).

## Step 3. Induction order and the floor (12903-12938; L18a §2.2, L18c §2)

* Induct on the width `M` in bands of length `σ/4`, in increasing order. All zero-slot bands come
  before all positive-slot bands.
* Within a zero-slot band: first prove `A ≤ 5M/6` (uncentred), then the rest of the padded core
  (centred), then all lengths by reflection.
* **Floor** `M ≤ ρ`: there are `O(Z^m)` rows and each squared product is `O(Z^{A+ε_1})`, so the
  exponent above `M` is at most `A − q ≤ ρ + δ`.
* The depth is `D = 2 + ⌈2M_max/σ⌉`.

## Step 4. Comparison and centering (12940-13010; L18a §2.3; ledger checks)

* Put `L = M/4` (old-eq:2.2). Assume `A > 5M/6`.
* **One factor shorter than `L`.** Reflect the other factor. The new total length is
  `≤ 3M/2 − A + ξ ≤ 2M/3 + ξ`, which the uncentred stage already covers.
* **Both factors at least `L`.** Let `(Y_1, Y_2) = (Z^L, X_1X_2/Z^L)`, so `Y_1Y_2 = X_1X_2`.
  * The comparison product `S(Y_1)S(Y_2)` is bounded separately after reflecting its long factor.
    This gives `A_comp ≤ 3M/2 − A + ξ` (old-eq:3.11), a margin of at least `M/6 − ξ` below
    `5M/6`, so the comparison falls in the uncentred stage at the same width.
  * The difference `Δ_k` = original − comparison is written as one coefficient `D_𝐛(l_1, l_2)`
    (old-eq:2.18a, 13012-13030).
  * Its squared norm is nonnegative, so it is extended by positivity to the full smooth row ball.
    No Poisson step is ever applied to an indicator of exceptional rows (13005-13010).

## Step 5. First Poisson transform (13114-13410; L18a §2.4, L18b §2)

* **Localisation** (13126-13170). Use whole dyads chosen from the sector only, with tails bounded
  absolutely through Lemma 4.7. The loss is `δ_fr,1 < ξ`.
* **Zero frequency** (13171-13190). A nonzero character mean needs every exponent `≡ 0 (mod 6)`,
  so the product of the two full index products is powerful. There are `O(X^{1+ε})` powerful
  products, so the zero frequency contributes `O(Z^{m+ε_1})`.
* **Nonzero frequencies with complete common support** (13192-13349). Write the two full index
  products as `Ca`, `Db`, with `rad C = rad D`, `(a,b) = 1` and `(ab, CD) = 1`.
  * Fix allocations of each common prime power.
  * Split the row character as `χ_Cχ̄_D = ξ_𝔯 · 1_{(k,𝔠/𝔯)=1}`, with `ξ_𝔯` primitive.
  * Möbius-expand the mask with `𝔢`, then apply Poisson modulo `𝔯ab` (lattice Poisson, E4).
  * Collect the CRT and reciprocity phases into `τ_C(a)τ̄_D(b)R̄(a,b)` (Lemma 4.4).
  * Extend to noncoprime residual pairs with the Möbius label `s`.
  * Separate the kernel `Φ̂_1(R_sc x/(y_1y_2))` and the inverse roots by **one** Fourier measure on
    whole-product norms, fixed before the live labels (Lemmas 4.5, 4.7).
  * Apply Cauchy–Schwarz in `h`.
  * Every step is exact or `Z^{o(1)}`/`O(ξ)` (L18b table §2; checks A1-A5, B1-B4, D).
* **Target and ledger.** It suffices to prove (old-eq:2.5)

      𝒩_C ≪ Z^{A − c + q̃ + 𝔅_c − s_0 + ε_G},   𝔅_c = max{0, (3c − 5d − R)/6},   q̃ = q + R + E.

  The exponent ledger closes iff (old-eq:2.6) `𝔅_c + 𝔅_d ≤ c + d − 2p − R`. This is proved prime by
  prime (13396-13408; ledger; L18b A3). The local slack is zero at the types `(1,1)` and `(2,1)`.

## Step 6. Gauss-row enlargement and second transform (13411-14310; L18a §2.5-2.6, L18b §3)

* **Enlargement** (13411-13456). In case 1, `w = w_o = ℓ = 0` and `g = J_+ + σ` (old-eq:2.8). By
  positivity the `h`-ball is enlarged to length `K + g`, with no amplification. The amplifier
  `h → hp⁶` (13456-13594) belongs to case 2 only.
* **Second Poisson in `h`** (13596-13649). Lemma 13.3 gives the exact expansion with `F(u,v;j)`.
* **Diagonal `j = 0`** (old-eq:2.12). `F(u,u;0) = φ(u)`, and the excess over the allowance is
  `≤ A − M + 5σ/3 + δ_fr,1`. This is a terminal loss **only because `A ≤ M + δ`** after
  reflection.
* **Off-diagonal: complete common-support extraction** (13686-13933).
  * Lemma 13.4 gives `F(D_2a, E_2b; j) = F(D_2,E_2;j) R(a,E_2) R̄(b,D_2) R(a,b) χ_a(j) χ̄_b(−j)`.
  * The local table gives `|F| ≤ Z^{g_2 − t_2}` (L13; L18b E, F).
  * The Möbius label `𝔱` and the inclusion–exclusion allocation keep the scales consistent in
    both rectangles (A5).
  * The same one-measure separation is used as in Step 5.
* **Children** (old-eq:2.13)-(2.14). Each separated side is again a product of two plain sums of
  one natural character, with
  * row width `m' = 2a_0 − K − g − g_2 − V`;
  * total width `M' = M + J − g − g_2 + t_2 ≤ M − σ`;
  * allowance `M' + Δ_child`, where `Δ_child ≥ w + ℓ`.

  Lemma 18.2 (`centered-coefficient-invariant`, 13953-13996) says each child side keeps one
  character, one mask and one norm power in **both** rectangles.
* **Non-exceptional children** (inducing character outside `Θ`; in case 1, nonprincipal) are
  bounded by the induction hypothesis at the smaller width `M'`. After triangle inequality, each
  rectangle is reflected into its padded core. [S2] The child normalisation, clipping and edge
  cost (14000-14310) are condensed to "loss `O(ξ)` per edge".

## Step 7. Exceptional (Θ) rows: the zero-slack core (14312-14778; L18a §2.7, L18b §3)

* **Count** (eq:exceptional-row-count, 14380). Exceptional induction forces one residue class mod
  6 for `v_p(h')` at every good prime (Lemmas 4.1, 4.4). So `(h') = 𝔥_0𝔳⁶` with `𝔥_0` fixed, and
  there are `≪ Z^{(m'−f)/6+ε_1}` such rows. (The paper keeps `f` where `2f` is available: S1.)
* **Uncentred excess** (old-eq:2.15)-(2.17). Bounding these rows by volume leaves the excess
  `A − 5M/6 − F_1 − F_2`, with `F_1 ≥ 2(c+w)/3 − 3σ − 5δ_fr,1/6` and `F_2 ≥ 2b_2/3`. **This is
  the origin of the `5M/6` threshold**: sixth-power rows are sparse (about `Z^{M/6}`), but each can
  be as large as the volume `Z^A`.
* **Centred case.**
  * Lemma 18.2 makes both rectangles share `ϑ ∈ Θ`, the mask `𝔑_*` and the norm power `q^{it}`.
  * Lemma 18.3 (`centered-lattice-cancellation`, 14545-14590) then gives
    `𝓛_i(X,t) = c X^{1+it} I_i(t) + O(Z^{ε_1}(1+|t|)^J)`. Its main terms depend only on
    `T = U_1U_2 = V_1V_2`, so they cancel in `D_𝐛`, leaving `T^{1/2}Z^{−r}` (old-eq:2.18f).
  * Aggregated over allocations, this gives (old-eq:2.18), with `r = (L − v)_+` and
    `v = c + w + min(c_2, d_2)`.
* **Deficit** (old-eq:2.19). `A − 5M/6 − 2v/3 − (L − v)_+ ≤ (A − M)_+ ≤ δ`. The maximum is
  attained exactly at `v = L` (L4). So the centred exceptional terms cost only the terminal
  `δ + 3σ`.

[S3] The clipped-shell and divisor-boundary bookkeeping (eq:centered-divisor-boundary,
eq:centered-raw-normalization, old-eq:2.18h; 14040-14180, 14700-14740) is condensed to "the
`𝔱`-labels net to at most `2θ_N`" (L18b L2, L3).

## Step 8. Completion of the finite induction (14779-14983; L18a §2.8, L18c §2)

* **Strict drop.** Every strict call goes to a child with `M' ≤ M − σ`. The frequency, support
  and clipping corrections cost at most `C_*ξ < σ/4`, so the width drops by at least `σ/2` and
  the child leaves its band. There are at most `D − 2` strict calls on a branch.
* **Loss accounting** (old-eq:2.1i). Choose `ρ, σ, δ` so that
  `T_term = ρ + δ + ρ/6 + 3σ + 5σ/3 < ε/4`. Then choose `ξ, η, ε_0 < ε/(16C_*D)`, with
  `ξ < min(δ/2, ρ/30, σ/(4C_*))`.
* **Envelopes.** `𝓔_d = T_term + (d+1)C_*(η + ξ + ε_0)`. Terminal losses enter once per branch, as
  a maximum. Cauchy–Schwarz averages the errors of the two children. So the largest path error is
  `< ε` (L18c S2).
* **Uniformity** (14834-14862). The analytic separations raise only seminorm and height orders,
  not exponents of `Z` (Lemmas 4.5, 4.7). Label counts are used once.
* **Physical remark** (14975-14983). For `q = 0` and sixth-power-free rows, every exceptional row
  is supported on `S`. This is used in Prop 19.2, not in case 1.

[S4] The quantifier order for a fixed slot count (14891-14950) concerns case 2 and is omitted.

## Where the saving comes from (L18a, "Where the saving comes from")

* The two transforms compose to the identity up to the positive enlargement `g`. They extract no
  cancellation by themselves. In the coprime squarefree model the recursion reads
  `Σ(M) ≲ Z^m + Z^{A+g} + Z^g Σ_child(M−g) + (Θ rows)`.
* The recursion closes because every child is again a product of two plain sums of one Hecke
  character, with conductor `≤ Z^{M'}`. So it can be **reflected** to total length `≤ M' + δ`, and
  the diagonal `Z^{A+g}` costs only the one-time `g ≈ σ`. For general coefficients this step is
  unavailable, and the large sieve's `(MN)^{2/3}` term appears instead.
* The genuine power savings are arithmetic: the powerful zero frequency, the sparsity of
  sixth-power exceptional rows (`5M/6`), and the centred lattice cancellation `Z^{−r}` with `r`
  up to `L = M/4`.

## Simplifications in this outline

| ID | What was simplified |
|---|---|
| S1 | clipping of subunit scales in reflection (12772-12796) |
| S2 | child normalisation, clipping and edge cost (14000-14310) |
| S3 | `𝔱`-label and divisor-boundary bookkeeping in the Θ-row stage |
| S4 | case-2 quantifier order and slot-count independence (14891-14950) |
| S5 | the localisation tail argument (13126-13170) is stated, not reproduced |
| S6 | the exact separating-measure construction (13320-13335, 13910-13935) is stated as "one measure fixed before the live labels" |
| S7 | all case-2 content: prime estimates (3.4)-(3.6), the amplifier, (3.14)-(3.16), greedy slot removal and Z4 (L18c §1, §3) |

None of these is a strengthening. Each omitted part was read by the review cited for its lines.

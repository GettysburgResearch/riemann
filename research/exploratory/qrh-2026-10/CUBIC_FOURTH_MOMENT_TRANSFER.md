# Transferring the Lemma 18.1 scheme to the cubic fourth moment

```text
Status: EXPLORATION (exponent bookkeeping only). PROPOSED repair step, not proved. HEURISTIC
  consequences labelled as such. No moment bound is proved here.
Scope: abstract scheme of case 1 (z = 0) of Lemma 18.1 (lem:plain) of the external, unreviewed
  OpenAI manuscript "The Quasi-Riemann Hypothesis" (30 Sep 2026). Transferred to order n = 3
  (cubic Hecke characters over Q(omega)) and calibrated on n = 2 (quadratic). Every displayed
  exponent ledger of the proof is redone with theta = 1/n and the order-dependent residues.
  The parts of the proof the earlier review did not verify (common-support bookkeeping,
  l. 13192-13349 and 13686-13933; Lemmas smooth-calculus and kernel-seminorms) are assumed
  correct, not checked.
Exact sources or dependencies:
  pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, file standalone/2026-10-07-openai-quasi-
    riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/
    paper.tex (sha256 42a5ee0f...deac6a3, re-hashed here). Read as untrusted data: statement
    l. 12477-12601, proof l. 12602-14777 (Sec. 18.1-18.7), finite Fourier lemmas l. 7042-7241,
    arithmetic conventions l. 557-700. Line numbers below refer to this file.
  reviews/LEMMA18_1_REVIEW.md and reviews/lemma18_ledger.py (14/14 PASS).
  Literature: arXiv abstract pages and arXiv API listings only (Sec. 7). Heath-Brown 1995 is
    a journal paper, cited from memory and not re-read.
What was actually run:
  python3 -I scripts/cubic_fourth_moment_ledger.py -> 31/31 PASS (sympy identities plus exact
    Fraction tables and grids, a few seconds, one process). Output is in
    results/cubic_fourth_moment_ledger_output.txt.
  Two arXiv API queries (cubic and moment; fourth moment and quadratic), plus id lookups.
Smallest remaining gap: the transfer is only plausible with one step the paper does not contain.
  The exceptional-row count of the C-norm children must use the forced residue
  v_p(h') = 1 (mod 3) at every first-transform conductor prime p | r whose multiplicities satisfy
  v_p(C) - v_p(D) = 1 (mod 3), and that saving must survive the complete common-support
  extraction and the t-allocation. Even then the cubic numerology has exactly zero slack at the
  balanced point A = M. Any loss of order M hidden in the unverified bookkeeping therefore
  breaks it.
```

RH is unsolved. This note does not prove or disprove anything about RH, about Lemma 18.1, or
about cubic moments. "Closes" below means only that the affine exponent ledgers balance.

## 0. Summary

* **Mechanical transfer (b: fails).** Replace 6 by 3 everywhere and re-optimise the
  first-transform allowance `B_c` within the paper's own ledger. The coefficient in the
  analogue of (old-eq:2.17) is then `κ = 5/6`, where `κ = 1` is needed. The centred stage
  (old-eq:2.19) fails for `A ∈ (19M/21, M+δ]`. At the balanced fourth moment `A = M` the
  deficit is `M/18`. The failure sits at first-transform common primes of multiplicities
  `(v_p(C), v_p(D)) = (2,1)`, which miss by exactly `(1/3) log q_p` each.
* **Repaired transfer (c: unclear, leaning plausible).** That step can be repaired by a PROPOSED
  forcing argument (Sec. 4). Its algebraic core is checked here, but it is not in the paper. With
  it, `κ = 1` and every ledger closes, with **zero slack** at `A = M` and comparison length
  `L = M/3`. The sextic proof has balanced slack `+M/12` there.
* **Order 3 is critical.** With `κ ≤ 1` the window for the comparison length at `A = M` is
  nonempty iff `1/n ≤ 1/3`.
* **Quadratic calibration (negative).** The scheme does **not** reproduce the known quadratic
  result. It is short by `M/4` at `A = M` and at best supports `K^{7/6+ε}`. Heath-Brown's large
  sieve gives `K^{1+ε}`, and Shen-Stucky give an unconditional asymptotic.

## 1. The abstract scheme and what each step uses

Notation as in the paper: rows `k ∈ O = Z[ω]` with `N k ≪ Z^m`, and `ψ_k(n) = τ(n) χ_n(k)`,
where `χ_n(k) = (k/n)_6` is zero-extended. `M = m + q`, `A = n_1 + n_2`, and `θ = 1/n`.

| step (lines) | what it does | hypothesis on the family used | where the order enters |
|---|---|---|---|
| masks, reflection (12602-12830) | erase fixed masks; reflect every plain factor longer than `M/2` | primitive Hecke functional equation (`Γ(s)/Γ(1-s)`, `\|ε_k\|=1`); conductor bound `C_k q_R ≪ Z^M`, needing **tameness at good primes** and a finite ray family at `S` | none (tameness holds for any n prime to the residue characteristic) |
| induction order (12903-12938) | width `M` in bands; first uncentred `A ≤ (1-θ)M`, then centred, then reflected | none | threshold `(1-θ)M` |
| comparison (12940-13010) | for `A > (1-θ)M`, subtract the rectangle `(L, A-L)`; reflect its long side: `A_comp = M - A + 2L` | functional equation again | needs `A_comp ≤ (1-θ)M` |
| 1st Poisson, zero freq. (13180-13190) | row mean nonzero only if all exponents are `≡ 0 (mod n)`, so the product is powerful: `Z^{m+ε}` | **orthogonality of n-th power symbols** in the row | same count `X^{1+ε}` for every n ≥ 2 |
| 1st Poisson, nonzero (13192-13409) | Gauss sums `G(a,h)`, reciprocity, Cauchy-Schwarz, target `N_C ≪ Z^{A-c+q̃+B_c-s_0}`; ledger needs `B_c + B_d ≤ c + d - 2p - R` | **reciprocity law** (bicharacter `R`), **prime-power Gauss sums** (`eq:gauss-local`, 6 → n) | `R` = common primes with `n ∤ v_p(C) - v_p(D)`; `B_c` |
| Gauss-row enlargement (13411-13594) | positivity: h-ball `K → K+g`, `g = J_+ + σ`; the row `h = 0` is added | `G(u,0) = 0` unless u is an **n-th power** | `Y^{1/n}` n-th powers (Sec. 3, [E]) |
| 2nd Poisson (13596-13951) | diagonal `j = 0` (needs `A ≤ M + δ`); complete common support; children of width `M' ≤ M - σ` | full correlation lemma (6 → n); **children are again products of two plain sums of an order-n Hecke character** | local table `n ∣ i` cases |
| Θ-rows (14312-14777) | rows whose child character lies in the fixed group Θ: `(h') = h_0 v^n`, counted `Z^{θ(m'-f)}`, bounded by volume; centred **lattice cancellation** saves `Z^{-r}`, `r = (L - v)_+` | Kummer theory (`μ_n ⊂ F`), **n-th power sparsity**, smooth lattice counting | `θ`, forced residues mod n |
| completion (14779-14973) | strict width decrease, terminal losses taken as a max | none | none |

The variable `z` (prime slots) is `0` throughout. Case 1 never uses the `p⁶` amplifier, the
`κ`-zero-free hypothesis, or (old-eq:3.6).

**Where `z = 0` matters.** With no slots, the padded core is `n_i ≤ M/2 + ξ`, `A ≤ M + δ`
(old-eq:2.1h). The diagonal (old-eq:2.12) is harmless only because `A ≤ M + δ`, which reflection
provides. `w = w_o = ℓ = 0` and `g = J_+ + σ`.

## 2. The cubic target

Rows `k ∈ Z[ω]`, `0 < N k ≪ Z^m`. `ψ_k(n) = τ(n)(k/n)_3` with all the paper's
zero-extension, mask and moving-support conventions, and every 6 replaced by 3. `R_0` is the set
of rows with nonprincipal inducing character.

> **PROPOSED Statement C (OPEN).** For every ε > 0 and bounded `n_1, n_2 ≥ 0`,
> `Σ_{k ∈ R_0} |S_{ψ_k}(n_1;W_1) S_{ψ_k}(n_2;W_2)|² ≪ Z^{M+ε}`.
> By positivity and Mellin inversion (as in the review, Sec. 0), the case `q = 0`, `n_1 = n_2 = m/2`
> would give `Σ_{c sf, c ≡ 1 (9), N c ≤ X} |L(1/2+it, χ_c)|⁴ ≪_{ε} X^{1+ε}(1+|t|)^{O(1)}`, with
> `χ_c = (·/c)_3`. By cubic reciprocity `(k/n)_3 = (n/k)_3` for primary `n, k`, so the rows are exactly the
> family of David-de Faveri-Dunn-Stucky. Cubic *Dirichlet* characters over Q are a different,
> thinner family and are not addressed.

Principal rows are `k = ±v³`. They number `Z^{m/3}`, each of volume `Z^A`. On the full row ball
they fit `Z^M` exactly when `A ≤ (1-θ)M = 2M/3`. This is the cubic analogue of `5M/6`, and it
is the origin of the threshold ([D6]).

## 3. Step-by-step transfer (exact exponents; script sections in brackets)

All lengths are in units of `log Z`.

1. **Identities** [A1-A6]. With exceptional count `Z^{θ(m'-f)}`, the exceptional excess is
   exactly `A - (1-θ)M - F_1(θ) - F_2(θ)`, where

       F_1(θ) = θc + (1-θ)(d + (K_0-K)) + 2θw + θq̃ + w_o + B_c - (1-θ)g + ℓ
       F_2(θ) = 2b_2 - (1-θ)g_2 - p_2 + t_2 + θV + θf

   At `θ = 1/6` these are the paper's (old-eq:2.16). The first-transform ledger, the diagonal
   excess (2.12) and the width identity (2.13) do not involve θ. On the branch `J ≥ 0`,
   `F_1 = c + 2w + θ(q̃ + w_o) + B_c` for every θ.
2. **Zero frequency.** Unchanged: `Z^{m+ε}`, because the product is still powerful.
3. **Gauss-row zero** [E]. Cubes give `Z^{2a_0/3 - 2s_0}`, which fits the allowance
   `a_0 - s_0`. Even the paper's cruder count fits, with equality at `s_0 = a_0/3`. For n = 2 only
   the refined count fits.
4. **Diagonal and width decrease.** Unchanged.
5. **Second-transform local table** [C]. For n = 3:

   | case | `F_2` | `b_2` |
   |---|---|---|
   | equal `i`, `3 ∤ i`, unit | `4i/3` | `i` |
   | equal `i`, `3 ∤ i`, nonunit | `4i/3 - 2/3 + f/3` | `i` |
   | equal `i`, `3 ∣ i` | `4i/3 - 1` | `i` |
   | unequal `i > j_0`, `3 ∣ j_0` | `i + j_0/3 - 1` | `(i+j_0)/2` |

   At a nonunit prime of multiplicity 1, `v_p(G_cV_id) = 2`, so exceptional induction forces
   `v_p(h') ≡ -2 ≡ 1 (mod 3)`. That gives `f = 1`, the exact analogue of the paper's `≡ 4 (mod 6)`
   (l. 14354-14357). With it, `F_2 ≥ b_2`, so `κ_2 = 1`, tight at nonunit `i = 1, 2` and equal
   `i = 3` [C2, C5]. Without it, `κ_2 = 2/3` [C3]. Note that `θf = 1/3` is numerically the same
   saving the paper uses for n = 6.
6. **First-transform allowance** [B]. On the branch `J < 0` (worst case `E = q = 0`), each common
   prime with `(i,j) = (v_p(C), v_p(D))` contributes `θi + (1-θ)j + θr + β_C` to `F_1`, where
   `r = 1_{n ∤ i-j}`. The budget is `β_C + β_D ≤ i + j - 2 - r` (old-eq:2.6).

   Optimising over **all** allowances gives:

   | order | `κ_1` without forcing | binding prime |
   |---|---|---|
   | n = 6 | `2/3` | `(2,1)` — this is the paper's `B_c = ((3c-5d-R)/6)_+` [B1, B5] |
   | n = 3 | **`5/6`** | `(2,1)` — closed form `B_c = ((3c-4d-2R)/6)_+` [B2, B8] |
   | n = 2 | `1` | — [B4] |

   For n = 3 at `(2,1)`: the budget is `2 + 1 - 2 - 1 = 0`, while `F_1 = 2/3 + 2/3 + 1/3 = 5/3 < 2 = c`.
   The miss is exactly `1/3` per prime [B7].

## 4. The PROPOSED repair: forcing at first-transform conductor primes

At `p | r` the C-side character is `τ_C(a) = τ(a) χ_a(𝔢𝔯) ξ_𝔯(a)` (l. 13228-13231).

* `ξ_𝔯 = Π_p χ_p^{i_p-j_p}`, because the row character is `χ_{Ca}(k) \overline{χ_{Db}(k)}`.
* CRT supplies `χ_a(𝔯) ξ_𝔯(a)` (l. 13260-13271); I re-derived this.
* Cubic reciprocity turns `χ_a(p)` into `χ_p(a)`.

So every C-norm child carries `χ_p(n)^{1+i-j}` at `p`. Its columns are punctured at `p`, and `τ`
has no older moving factor at a column prime (l. 14317-14326). An exceptional child row must
therefore have

    v_p(h') ≡ -(1 + i - j)  (mod 3).

For `i - j ≡ 1` the residue is 1. So `h_0` contains `p` and the count gains `θ log q_p`.

* The paper alludes to such conditions ("Additional conditions at old moving primes can only
  reduce the count", l. 14385-14386) but never uses them.
* The D side has exponent `1 - (i-j)`, which is `≡ 0` at `(2,1)`. That is harmless: there `F_1^D` has
  surplus.

With this forcing, `κ_1 ≥ 1` for every `(i,j)` with `i, j < 200` [B3, B6]. Remaining zero-budget
configurations are `(1,1)`, `(2,1)`, `(3,1)` and their transposes. In the explicit path with all
common primes of type `(2,1)` and `c = M/3` [F2], the exceptional excess is `M/18` without the
forcing and exactly `0` with it.

What would have to be proved:

* the child character's local exponent at `p | r` is exactly `1 + i - j` after the second
  transform, the complete extraction and the full Möbius `t`-allocation;
* the forced residue also covers rows admitted after positivity;
* it is compatible with the fixed-ray phases at `S`.

## 5. The comparison window: the key exponent comparison [D, G]

Constraints at the zero-slot core, in units of `M`:

* Comparison: `A_comp = M - A + 2L ≤ (1-θ)M`, so `L ≤ (A - θM)/2`.
* Centred: `max_v [A - (1-θ)M - κv - (L-v)_+] = A - (1-θ)M - min(κ,1)L ≤ (A-M)_+`.

| family | threshold | `κ` | `L` window at `A = M` | balanced slack at `A = M` | window empty for | self-consistent loss `η` |
|---|---|---|---|---|---|---|
| sextic (paper) | `5M/6` | 2/3 | `[1/4, 5/12]` | **+1/12** (at `L = 3/8`) | never | 0 |
| cubic, mechanical | `2M/3` | 5/6 | `[2/5, 1/3]`, empty | **-2/51** | `A > 19M/21` | **2/51** |
| cubic + forcing (Sec. 4) | `2M/3` | 1 | `{1/3}` | **0** | never (`A ≤ M`) | 0 |
| quadratic | `M/2` | 1 | `[1/2, 1/4]`, empty | **-1/6** | `A > M/2` | **1/6** |

* **Deficit with the best `L`.** At `A = M` it is `M/18` for the mechanical cubic transfer and
  `M/4` for the quadratic one.
* **The criterion.** With `κ ≤ 1` the window is nonempty iff `θ ≤ (1-θ)/2`, that is `n ≥ 3` [D5].
  So cubic is exactly critical. At `v = 0` (no common support) the deficit is
  `A - (1-θ)M - L` whatever `κ` is, so `κ > 1` cannot help.
* **Why the paper's own zero slack is not structural.** The paper fixes `L = M/4`, the lower end
  of its window, and so has zero slack at (old-eq:2.19). The sextic scheme has `M/12` to spare at
  `A = M`. The cubic scheme has none for any `L`.
* **Generic path** [F1]. With no common support, `A = M` and `L = M/3`, the exceptional
  contribution is count `Z^{M/3}` times volume `Z^{M}` times saving `Z^{-M/3}`. That is exactly
  `Z^M` (+`2σ/3` terminal).
* **HEURISTIC.** If everything else in the scheme is right, the mechanical cubic transfer with a
  relaxed target `Z^{(1+η)M}` balances at `η = 2/51`. That would give
  `Σ|L(1/2,χ_c)|⁴ ≪ X^{53/51+ε}` without the forcing step, still below the large-sieve `X^{4/3+ε}`.
  This is a statement about the exponent model only. The relaxed induction was not written out.

**Zero-slack points of the repaired cubic scheme:**

* `A = M` with `L = M/3`, where `A_comp = 2M/3` exactly. The uncentred stage must then be run on
  `A ≤ 2M/3 + C_*ξ` with a terminal loss, and `L` must depend on `A`, for example
  `L = (A - M/3)/2`.
* First-transform primes `(1,1)`, `(2,1)` (needs Sec. 4) and `(3,1)`.
* Second-transform nonunit `i = 1` (needs `f`), nonunit `i = 2`, and equal `i = 3`.

The sextic proof is tight only at its own chosen `L` and at `(2,1)` / nonunit `i = 1`.

## 6. Quadratic calibration

For n = 2 the Lindelöf-on-average fourth moment is known:

* Heath-Brown's quadratic large sieve (Acta Arith. 72 (1995) 235-275, recalled, not re-read)
  gives `Σ_{|d|≤X} |L(1/2+it, χ_d)|⁴ ≪ (X(1+|t|))^{1+ε}`.
* Shen, arXiv 1907.01107: asymptotic under GRH, unconditional lower bound.
* Shen-Stucky, arXiv 2402.01497: unconditional asymptotic with four main terms.
* X. Li, arXiv 2208.07343: unconditional second moment of quadratic twists of modular
  L-functions.

The scheme's `κ` is fine for n = 2 (`κ_1 = κ_2 = 1`). Its numerology still fails, because squares
are too dense. The full-ball threshold is `A ≤ M/2`. The comparison then allows only `L ≤ M/4`,
while the centred stage needs `L ≥ M/2`. The best the model supports is `K^{7/6+ε}`.

So the scheme does **not** reproduce the known quadratic result. Its strength and the large
sieve's are complementary:

* The quadratic large sieve is already sharp (`M + N`).
* The cubic large sieve has the `(MN)^{2/3}` term, which Dunn-Radziwiłł (arXiv 2109.07463) show is
  sharp under GRH for general coefficients.
* The scheme beats the latter only through reflection of plain children and the sparsity of
  n-th powers.

The calibration therefore neither confirms nor refutes the cubic transfer. It shows that the
scheme's success is a numerological coincidence of order `n ≥ 3`, with n = 3 on the boundary.

## 7. Literature check (primary sources, abstract level)

An arXiv API search (`abs:cubic AND abs:moment AND abs:L-functions`, 44 hits, read to 2609.*)
and the id lookups found **no unconditional fourth moment of Lindelöf strength for cubic Dirichlet
or cubic Hecke L-functions**.

* Gao-Zhao (2104.09909): upper bounds for all `k` under GRH; cubic lower bounds unconditional
  for `k ≥ 1/2`.
* David-de Faveri-Dunn-Stucky (2410.03048): mollified second moment and a Lindelöf-on-average
  second moment of cubic Dirichlet series, unconditional.
* Blomer-Goldmakher-Louvel (1112.1650): n-th order large sieve and second moment.
* Baier-Young (0804.2233): first moment and the order-3/6 large sieve.
* Diaconu-Ion-Paşol-Popa (2607.27131): first and second twisted moments for `r ≥ 3`, fields
  containing `μ_{2r}`. `Q(ω)` contains `μ_6`, so `r = 3` is in scope for second moments only.
* Unconditionally, the best fourth-moment bound obtainable from these tools is `X^{4/3+ε}`: the
  Heath-Brown cubic large sieve at `M = N = X`, or Weyl-type subconvexity times the second
  moment. This is the reviewer's estimate and was not re-derived from a source.

Statement C at `q = 0` would therefore be new.

## 8. Verdict

**(b) for the mechanical transfer; (c) overall.**

* **(b).** Replace 6 by 3 everywhere, with an optimally redesigned allowance `B_c`. The scheme
  then fails at the centred exceptional stage (analogue of old-eq:2.17/2.19):
  * the binding constraint is the first-transform common primes of multiplicity `(2,1)`;
  * they give `κ = 5/6` instead of 1, a shortfall of `(1/3) log q_p` per prime;
  * the comparison window is empty for `A > 19M/21`, with deficit `M/18` at `A = M`.
* **(c).** One PROPOSED forcing step (Sec. 4) makes every displayed ledger close. It sits
  naturally in the paper's framework, and its character algebra was re-derived here. But it is
  not part of Lemma 18.1's proof, so the cubic result would **not** be "conditional only on
  Lemma 18.1's proof being correct". Moreover the repaired scheme has **zero slack** at the
  balanced point `A = M`, where the sextic has `M/12`.

**Smallest sub-question.** In the cubic version of Sec. 18.6-18.7, does the exceptional count
for the C-norm children carry the saving `(1/3)Σ log q_p`? The sum is over first-transform
conductor primes with `v_p(C) - v_p(D) ≡ 1 (mod 3)`, so the question is whether the forced residue
`v_p(h') ≡ 1` survives complete extraction, the `t`-allocation and positivity uniformly. Two
things must also hold at `A = M`, `L = M/3`:

* the unverified common-support bookkeeping of the paper (l. 13192-13349, 13686-13933) loses
  nothing beyond `O(ξ + σ)`;
* every such loss is terminal.

**Steps needing re-proof for Statement C:**

1. Cubic Gauss and correlation lemmas (6 → 3). Routine.
2. Kummer and fixed-numerator lemma with `μ_3`, and the cubic reciprocity bicharacter. Routine.
3. The allowance `B_c` by the local table of [B6]. Checked as ledger.
4. Forcing at r-primes (Sec. 4). **New.**
5. Nonunit `i = 1` forcing `≡ 1 (mod 3)`. Analogue of l. 14354.
6. An A-dependent comparison length `L ∈ [A - 2M/3, (A - M/3)/2]` and an uncentred stage on
   `A ≤ 2M/3 + C_*ξ` with terminal loss.
7. All of Lemma 18.1's unverified bookkeeping, now with no margin.

## 9. Files

* `scripts/cubic_fourth_moment_ledger.py`: sections [A]-[G], 31 checks, EXACT_RATIONAL plus sympy.
* `results/cubic_fourth_moment_ledger_output.txt`: its output.

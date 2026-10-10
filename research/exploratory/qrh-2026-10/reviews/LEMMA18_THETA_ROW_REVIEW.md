# Fresh-eyes review: the centred Θ-row stage of Lemma 18.1 (Lemmas 18.2-18.3 and (2.15)-(2.19))

```text
Status: REVIEW (bounded, one reader; external and unreviewed manuscript) + EMPIRICAL model numerics.
  Verdict: no wrong step found in the lines read. This is not "verified" and not an independent
  exact-SHA review in the AGENTS.md sense: the reader is an AI agent of the same model family as
  the earlier bounded reviews, and no human has checked it.
Scope: paper.tex lines 13953-13996 (Lemma 18.2 `centered-coefficient-invariant` and its proof) and
  14312-14778 (Theta rows: exceptional-row count, (old-eq:2.15)-(2.17), Lemma 18.3
  `centered-lattice-cancellation` with its proof at 14598-14680, its application and
  (old-eq:2.18)-(2.19)). Read for context: 12477-13952 (statement, reductions, reflection,
  centring, both Poisson transforms, Gauss-row enlargement, second transform), 13996-14311
  (child normalisation and clipping), 14779-14984 (completion of the induction).
Exact sources or dependencies:
  pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, file standalone/2026-10-07-openai-quasi-
    riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
    sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-extracted and
    re-hashed for this review; 16,677 lines; read as untrusted TeX, not as a PDF).
  Manuscript helpers used as black boxes (statements only): lem:fixed-numerator-ray (647),
    eq:row-fixed-ray-reduction (1064), lem:smooth-calculus (1123), lem:kernel-seminorms (1348),
    lem:deleted-euler-factors (1602), lem:full-correlation (7081),
    lem:complete-support-correlation (7197), Lemmas 4.3-4.4 (reciprocity; see
    SEP30_L42_44_REVIEW.md).
  Repository context, read after forming a first view: proposed/SEXTIC_FOURTH_MOMENT/README.md
    Sections 8 and 10 and PROOF_OUTLINE.md; LEMMA18_1_REVIEW.md Sections 2.6-2.7;
    LEMMA18_1_COMMON_SUPPORT.md; LEMMA18_1_CASE2_SEC188.md Sections 1.3-1.5 and 3.
    Working-branch head when written: e5731afb5.
What was actually run (one process at a time, nice -n 10, one thread):
  python3 -I theta_row_ledger.py results/theta_row_ledger.json   -> 19/19 PASS (exact rational and
    symbolic; about 20 s)
  python3 -I theta_row_lattice.py results/theta_row_lattice.json 1.2e7 -> 14/14 PASS (EMPIRICAL,
    ordinary float64, 3,627,565 lattice points, 22 s)
  The lattice script's pass criteria were recalibrated after its first run (Section 9.4).
Smallest remaining gap:
  (1) The tight point is not Lemma 18.3. At v = L the centred saving r is zero. The case is closed
      by the uncentred count-and-volume ledger F_1 + F_2 >= 2v/3, which has no slack in its main
      exponent there (an explicit admissible configuration attains it; Section 7). Lemma 18.3's
      saving has a factor 1/3 of spare room for v < L.
  (2) Lemma 18.2 depends on the one-measure Fourier separation of the kernels and inverse roots
      (13320-13335, 13910-13935), i.e. on lem:smooth-calculus and lem:kernel-seminorms. These
      were read here as statements only.
  (3) No human analytic number theorist has checked this stage.
```

RH remains unsolved. This note does not claim that RH, the manuscript's 7/8 theorem or Lemma 18.1 is
proved or disproved. It reviews one stage of one lemma of an external manuscript. The numerics in
Section 9 are EMPIRICAL: ordinary floating point over a finite range. They are not certified, and
no asymptotic statement is inferred from them.

## 1. Verdict in brief

* **No wrong step found in the lines read.** Every displayed identity and inequality in the target
  lines was rederived by hand. Each exponent identity was also checked in exact arithmetic.
* **Lemma 18.3 (lattice cancellation).** No wrong step was found in its proof. It is lattice Poisson on
  a fixed finite union of residue classes, with the mask inserted by Möbius inversion, and the
  remaining steps are elementary algebra. The main-term coefficient really is independent of `X`
  and `t`, and the two rectangle main terms really cancel. The error is `2^{ω(𝔑_*)}` times a
  polynomial in the height, which is `Z^{o(1)}`.
* **Lemma 18.2 (common coefficient).** The claim holds given the constructions it cites. Every
  factor that is Fourier-separated is a function of a row, of frozen outer norms, or of a *whole*
  column norm. None is a function of a single plain variable or of a rectangle. So each side keeps
  one character, one mask and one norm power, common to both rectangles. This rests on the
  imported one-measure separation (gap (2) above).
* **(2.15)-(2.19).** The identity (2.15)-(2.16) is exact, and the bounds (2.17) hold. The maximum
  in (2.19) is exactly `A − M`, attained only at `v = L`. This was confirmed symbolically and on
  60,000 random exact configurations built from raw per-prime data.
* **New observation (Section 7).** At `v = L` the saving `r = (L − v)_+` is zero, so Lemma 18.3 is
  not used at the tight point. The stage closes if and only if the saving is at least
  `(2/3)(L − v)_+` (ledger check Z4). Lemma 18.3 supplies `(L − v)_+`.
  * The zero slack lives in the uncentred Θ-row ledger at `v = L`. There, the three "tight points"
    named by the earlier reviews are one and the same configuration.
  * The lattice lemma could lose up to a third of its saving without harm. It could not lose a
    fixed additive power near `v = L`.
* **Hidden losses.** Every loss at this stage is one of the following, and none is a fixed power of
  `Z` (inventory in Section 7.3):
  * `Z^{o(1)}` (divisor, Rankin, allocation or mask counts);
  * `(log Z)^{O(1)}` (dyads);
  * a polynomial in the separated heights, absorbed by the Fourier measure;
  * a fixed multiple of one of the small parameters `σ, δ, ξ, η, ε_0`.

  The zero slack in the main exponent is therefore harmless: the claim is `Z^{M+ε}`, and every
  small parameter is chosen after `ε`.

## 2. Precise restatements

### 2.1 Lemma 18.2 (`centered-coefficient-invariant`, 13953-13981; proof 13983-13996)

*Setting.* The input is centred: the product of two plain sums minus the comparison rectangle
with the same product of scales, `X_1X_2 = Y_1Y_2` (12991-13010). The coefficient form
(eq:centered-coefficient-form, 13063) is

```text
(prod_{i live} nu_i(p_i) W_i^slot(q_{p_i}/P_i)) · D_b(l_1,l_2) · tau_1(u) q_u^{it} 1_{(u,R)=1} 1_{s|u},
u = Π l_1 l_2,
D_b(l_1,l_2) = prod_i W_i(q_{b_i} q_{l_i}/X_i) − prod_i W_i(q_{b_i} q_{l_i}/Y_i).
```

*Claim.* Through the first transform, the Gauss-row enlargement (amplifier) and the second
transform with full Möbius `𝔱`-allocation, the following are preserved:

1. Each Gauss polynomial and each amplifier error keeps this form times `G(u,h)`, up to bounded
   frozen scalars and row scalars of modulus at most 1.
2. Each separated child side keeps it without `G` and without `s | u`. Each surviving slot keeps
   the child's whole-product character and its original `ν_i`.
3. Within one side, the two plain variables and both rectangles share one character, one
   puncture mask and one norm power `q^{it}`. The two sides of one squared norm may differ in
   norm power, and their inducing characters differ by a member of `Θ`.
4. On a row whose inducing character lies in `Θ`, once the live slot labels are fixed, the plain
   coefficient is `ϑ(l_1)ϑ(l_2) 1_{(l_1l_2,𝔑_*)=1} q_{l_1l_2}^{it} D_b(l_1,l_2)`, with:
   * one `ϑ ∈ Θ`;
   * one squarefree `𝔑_*` of polynomial norm, which may depend on the frozen row but is common to
     both variables and both rectangles;
   * one real `t`.

*Quantifiers.* The claims hold for every common-support allocation, every amplifier error, every
retained dyad, every fixed tuple of Fourier parameters, and every `𝔱`, `𝐉`.

### 2.2 Lemma 18.3 (`centered-lattice-cancellation`, 14545-14596; proof 14598-14680)

*Hypotheses.*
* `ϑ` ranges over a fixed finite set of finite-order ray characters with conductor in `S`.
* `𝔑_*` is squarefree with `q_{𝔑_*} ≤ Z^{B_*}`, where `B_*` is fixed.
* `W_1, W_2` are smooth on fixed annuli.
* The sums run over good ideals through their primary generators (global convention, 598-600).

*Claims.* With `L_i(X,t) = Σ_l ϑ(l) 1_{(l,𝔑_*)=1} q_l^{it} W_i(q_l/X)`:

* (2.18d): `L_i = c_{ϑ,𝔑_*} X^{1+it} I_i(t) + O(Z^{ε_1}(1+|t|)^J)`. Here `c` is independent of
  `X` and `t`, and `I_i(t)` is a fixed constant times `∫ W_i(y) y^{it} dy`.
* (2.18e): `|L_i| ≪ X`.
* Both bounds are uniform in `X > 0`, in the mask and in the finite character set.
* (2.18f): put `U_i = X_i/q_{b_i}`, `V_i = Y_i/q_{b_i}` and `T = U_1U_2 = V_1V_2`. If all four
  scales are at least `Z^r` with `r ≥ 0`, then

  ```text
  T^{−1/2} |Σ ϑϑ 1 q^{it} D_b| ≪ Z^{ε_1} (1+|t|)^{2J} T^{1/2} Z^{−r}.
  ```

  Without a lower length the same expression is `O(T^{1/2})`.

*What is uniform in what.*
* Constants depend on `Θ`, `B_*`, finitely many seminorms of `W_i` and `ε_1`.
* They do not depend on `X`, `t` (beyond the stated polynomial), the mask or the row.
* The ray conductor enters only through the fixed Poisson modulus, which is bounded because `Θ` is
  fixed.

## 3. Step-by-step verdict

| # | step (lines) | what I did | verdict |
|---|---|---|---|
| 1 | L18.3 unmasked Poisson (14599-14627) | Rederived the scaling `f_{X,t}(z) = X^{it} f_t(z/√X)` and the transform `X^{1+it} f̂_t(√X ξ)`. Integration by parts on the annulus gives `(1+|t|)^{J_0}(1+|ξ|)^{−J_0}`. The nonzero frequencies give `X^{1−J_0/2}` for `J_0 > 2`. For `X < 1` both sides are `O(1)`. The zero frequency `c_ϑ X^{1+it} I(t)` uses the self-dual measure. | no wrong step |
| 2 | primary generators as residue classes (14599-14603) | Ideals prime to 6 correspond to `z ≡ 1 (mod 3)` with odd norm. A ray character with `S`-conductor is a function of `z` modulo a fixed modulus. | no wrong step (checked in the model, M0) |
| 3 | mask by Möbius (14628-14650) | Rederived `L = Σ_{d∣𝔑_*} μ(d)ϑ(d)q_d^{it} L^0(X/q_d)`. The `q_d^{it}` cancels `(X/q_d)^{it}`, so `c_{ϑ,𝔑_*} = c_ϑ Π_{p∣𝔑_*}(1 − ϑ(p)/q_p)` is independent of `X` and `t`. The error is at most `2^{ω(𝔑_*)}` copies of the unmasked error, and `2^{ω} = Z^{o(1)}` for polynomial norm. | no wrong step (E1, E2) |
| 4 | (2.18e) (14652-14655) | Empty below a fixed scale; otherwise `O(X)` points. Uniform in `t` and the mask. | no wrong step |
| 5 | (2.18f) (14657-14680) | The double sum factorises exactly, because the mask, the character and `q^{it}` are completely multiplicative on good ideals. Both product main terms equal `c² T^{1+it} I_1 I_2`. The cross terms are `≪ Z^{ε}(1+|t|)^{J} max(U,V) ≤ Z^{ε}(1+|t|)^J T Z^{−r}`, and the error-times-error term uses `T Z^{−r} ≥ Z^r ≥ 1`. | no wrong step (E7 checks the factorisation) |
| 6 | L18.2 statement and proof (13953-13996) | Traced each separated factor in 13114-13950. The kernels `Φ̂_1`, `Φ̂_2`, the inverse roots, the localisation `ω_λ`, the sector boxes and the partition scalar are functions of the row, the outer norms or the *whole* column norm. The allocations (`C, D, 𝔢, 𝔯`, amplifier `p^i`, `D_2, E_2`, `𝔱`) divide `X_i` and `Y_i` by the same `q`. | no wrong step; rests on the imported one-measure separation |
| 7 | exceptional count (14312-14391) | Membership in `Θ` (conductor in `S`) forces `v_p(h')` into one class mod 6 at each good prime: tame Kummer ramification, through the reciprocity factorisation at 14326-14333. Hence `(h') = 𝔥_0𝔳^6`. At a nonunit prime of multiplicity one, `v_p(G_cV_id) = 2` and there is no older moving factor (the radicals are disjoint, 14318-14326), so `v_p(h') ≡ 4`. This gives `q_{𝔥_0} ≥ Z^{2f}`. The paper uses only `f`. | no wrong step; the Kummer step is standard and was not recomputed |
| 8 | raw volume (14392-14425) | `|P_j| ≪ N_post^{−1/2} T'_j Π P_i = Z^{(α_j − r̃_j)/2 + e_j}` from eq:centered-raw-normalization. Adding the `𝔱`-dyad count gives `a_0 − b_2 + 2θ_N`. | no wrong step |
| 9 | (2.15)-(2.16) (14431-14468) | Symbolic identity, including the intermediate form at 14462. | exact (S1, S2) |
| 10 | (2.17) (14470-14525) | `F_1`: the `J ≥ 0` simplification is exact (S3); the `J < 0` bound uses `q̃ ≥ R` and the 1-Lipschitz positive part; the `g`/`ℓ` increments cost `≤ 22σ/9 + 5δ_fr,1/6 < 3σ + …`. `F_2`: recomputed from the definitions of `b_2, g_2, p_2, t_2, V, f` for all admissible local types with `i, j_0 ≤ 120`; minimum slack 0, only at the nonunit type `(1,1)`. | exact (S3, P1, P2, E3) |
| 11 | application of L18.3 (14681-14735) | Every plain loses at most `c + w + c_2` (respectively `d_2`); the comparison has `Y_1 = Z^L`; the same `𝔟` is used in both rectangles; the side with `min(c_2,d_2)` gets the saving; `a_{1,i} ≤ r̃_1`. Formal scales are not clipped. | no wrong step |
| 12 | (2.18), (2.18h) (14710-14735) | `t_- − r̃_1 − r̃_2 − (r − r̃_1)_+ = (t_- − r̃_2) − max(r, r̃_1) ≤ ω_2 − r`; adding `e_1 + e_2` gives `≤ 2θ_N − r`. | exact (S4) |
| 13 | live slots on Θ-rows (14736-14745) | Volume `O_N(Π P_i)` is the `e_j` factor; the measure is fixed before the labels. | no wrong step |
| 14 | (2.19) (14752-14778) | `max_v [A − 5M/6 − 2v/3 − (L − v)_+] = A − M`, attained only at `v = L`. Positive slots: `A ≤ M − (6κ−1)z`. Zero-slot core: `A − M ≤ 2ξ < δ`. | exact (Z1); end-to-end check E1 |

## 4. Lemma 18.3: points worth recording

* **The error is better than stated, except near the mask's divisors.**
  * With a smooth profile and no mask, the unmasked lattice error is `O(X^{1−J_0/2})` for every
    `J_0`, i.e. smaller than any power.
  * With a mask, the error comes from divisors `d ∣ 𝔑_*` with `q_d` comparable to `X`. Each
    contributes `O((1+|t|)^{J})`.
  * So the true error is about `#{d ∣ 𝔑_* : q_d ≍ X}`, which is at most `2^{ω(𝔑_*)}`. The model
    shows exactly this (E5, Section 9.3).
* **The mask must be handled by Möbius, not as a congruence.** If `𝔑_*` (polynomial norm) were
  made part of the Poisson modulus, the nonzero frequencies would cost a power of `q_{𝔑_*}`. The
  paper does use Möbius (14628), which costs only `2^{ω}`.
* **Uniformity in the conductor.** The Poisson modulus is the lcm of the fixed `S`-conductors of
  `Θ` and the primary modulus 3, times 2. Its dual-lattice spacing is fixed, so the constant
  depends only on `Θ`. Nothing here is uniform in a growing conductor, and nothing needs to be.
* **No angular twist arises.** Finite-order Hecke characters of `Q(ω)` have trivial infinity
  type. Every separated factor in the transforms is radial: a function of `q_h`, `q_u`, `q_v` or
  frozen norms. An angular character `(z/|z|)^{6k}` would kill the main term and give an error
  that depends on `k` (E6). It plays no role in the lemma.
* **Main-term coefficient.** `|c_{ϑ,𝔑_*}| ≤ c_ϑ Π_{p∣𝔑_*}(1 + 1/q_p) ≪ log log Z`. The text's
  bound `Z^{ε_1}` (14651) is true but weak. This is harmless.
* **Same `t` in both plain factors is essential.** Suppose the two plain variables carried
  different norm powers `t_1 ≠ t_2`. Then the main terms would differ by
  `(X_1/V_1)^{i(t_1 − t_2)}` and would not cancel. The model confirms a non-cancelling term of
  volume size (control C2). Lemma 18.2 excludes this, because the only norm power is on the whole
  product `u = Π l_1 l_2`.

## 5. Lemma 18.2: is "centred" preserved with one norm power per side?

I traced every operation between the centred input and the Θ-row children.

| operation (lines) | acts on | effect on `(D_b, character, mask, t)` |
|---|---|---|
| comparison subtraction, central factor `1/√(X_1X_2)` (12991-13010) | constant, since `X_1X_2 = Y_1Y_2` | defines `D_b` with `b = (1,1)` |
| first Poisson in `k`; kernel `Φ̂_1(H q_h/(q_𝔢 q_𝔯 q_a q_b))`; inverse roots `(q_aq_b)^{−1/2}` (13252-13276) | row `h` and whole columns `a`, `b` | separated into `q_h^{iτ_0} q_a^{iτ_1} q_b^{iτ_2}`: one power per whole column |
| common support `C, D` and Möbius `s` (13209-13230, 13305-13318) | exact valuations at common primes, allocated once for the whole coefficient | the same `𝔟` divides `X_i` and `Y_i`; the primes become common punctures; `s ∣ u` stays as a condition on the whole column |
| CRT phases `χ_a(𝔢𝔯) ξ_𝔯(a)`, `R̄(a,b)` (13259-13276) | whole columns | characters on the whole product, which factor over `l_1, l_2` and slots |
| Gauss-row enlargement and amplifier `h → hp^6` (13411-13594) | row; `p^i` taken from the plains | the extracted `p^i` gives the same `𝔟` update in both rectangles; `R(p,u)^i χ_p(u)^{2i}` is a character on the whole `u` |
| second Poisson in `h`; kernel `Φ̂_2(Z^{K+g} q_j/(q_u q_v))`; inverse roots (13606-13631, 13910-13935) | row `j` and whole columns `u`, `v` | one power per whole column, added to `t` |
| complete support `D_2, E_2`; `F(D_2a,E_2b;j) = F(D_2,E_2;j) R(a,E_2) R̄(b,D_2) R(a,b) χ_a(j) χ̄_b(−j)` (13686-13697) | frozen and row scalars; characters on whole `a`, `b` | `R(a,b)` is split into `ρ(a)ρ'(b)` by finite Fourier on the fixed ray group |
| `𝔱`-Möbius and factor allocation (13867-13933) | `n_i = p l_i`, `l_i` unrestricted | a row scalar times `q_p^{it}`; the same `X_i/q_p`, `Y_i/q_p` in both rectangles |

**Conclusion.** No operation introduces a function of a single plain norm or a rectangle-dependent
factor. The inverse roots and kernels are smooth functions of whole-column norms. The fixed
log-box cutoffs are chosen on the common product annulus, which is the same box for both
rectangles because `X_1X_2 = Y_1Y_2` and the same `𝔟` is used. So the Fourier expansion is exact
on the support, and it gives exactly one `q^{iτ}` per whole column.

On an exceptional row, the zero-extended product character agrees with its primitive inducing
character `ϑ ∈ Θ` away from its zeros. Those zeros are coprimality conditions:
* zero extensions `χ_n(k) = 0` for `(n,k) ≠ 1`;
* six-divisible powers, which give `1_{(n,p)=1}`;
* fixed masks.

They combine into one `𝔑_*` that does not depend on the rectangle. The phrase "equals some
`ϑ ∈ Θ` on units" (13990-13991) should be read as "away from its zeros". This is the only
wording I would change.

**What this relies on and I did not re-prove.** The separation needs, on fixed log boxes:
* a Fourier measure with finite `L¹` norm and finite moments of the required order;
* uniformity over the sector and over `R_sc > 0`.

That is the content of lem:smooth-calculus and lem:kernel-seminorms, used here as statements.
The earlier common-support review treats the same item as imported.

## 6. The exceptional count and the ledger (2.15)-(2.19)

* **Count.** `#{h' : exceptional, q_{h'} ≪ Z^{m'_act}} ≪ Z^{(m'_act − f)/6 + ε_1}`.
  * The real count is `≪ Z^{(m'_act − 2f)/6}`, because `q_{𝔥_0} ≥ Z^{2f}`. The weaker form leaves
    `f/6` unused, as the common-support review also noted.
  * The finite choices at `S`, at the units and in the fixed-ray sectors give an `O(1)` factor.
  * Rows added after the partition scalar is bounded by one are included, so the count is an
    upper bound for the sum over the original rows.
* **(2.15)-(2.16)** hold as a symbolic identity in the 19 aggregate lengths (S1). The intermediate
  form at 14462-14466 is also exact (S2).
* **(2.17).**
  * The bound on `F_1` holds for all three norm types: zero-slot, amplified main term and the
    errors at valuations 1, 6 and 7.
  * The bound on `F_2` holds at every admissible local type (P1). Its only zero-slack type is a
    nonunit prime with equal multiplicity one.
  * Both were rechecked on 60,000 random exact configurations generated from per-prime data
    (E3).
* **End-to-end check (E1, E2).** For each random configuration I computed the exceptional excess
  directly from the definitions of `m', M', Δ_child, a_0, b_2, r`, without the paper's `F_1` and
  `F_2`. In every case the centred excess was at most `(A − M) + 3σ + 5δ_fr,1/6`, and the
  uncentred excess at most `(A − 5M/6) + 3σ + 5δ_fr,1/6`.

## 7. Zero slack, and whether hidden losses can break it

### 7.1 Where the slack really is zero

* The maximum of (2.19) is `A − M`, attained only at `v = L = M/4` (Z1).
* At `v = L` the saving `r = (L − v)_+` is **zero**. So the tight point is the *uncentred* bound
  `A − 5M/6 − (F_1 + F_2)` with `F_1 + F_2 ≥ 2v/3 = M/6`.
* An explicit admissible configuration attains it exactly, up to `5σ/6` from `g − J_+ = σ`
  (ledger witnesses Z2 and Z3):
  * zero slots;
  * one first-transform common prime of type `(i,j) = (2,1)`, with `R = p` and `B_c = 0`;
  * `q = E = 0` and `K = K_0`;
  * second-transform nonunit primes of multiplicity one, with `c_2 = d_2 = g_2 = p_2 = V` and
    `f = 2c_2`;
  * `c + c_2 = L`.

  This one configuration hits all three "tight points" of the earlier reviews at once:
  * `F_1 = 2c/3` at `J < 0`;
  * `F_2 = 2b_2/3` at a nonunit prime of multiplicity one;
  * `v = L` in (2.19).
* **How much centred saving is needed (Z4).** With a saving `θ(L − v)_+`, the maximum over `v` is
  `A − M` if and only if `θ ≥ 2/3`. Lemma 18.3 gives `θ = 1`.
  * So the lattice lemma can lose up to a third of its saving.
  * It cannot lose a fixed additive power. A saving `(L − v − λ)_+` raises the maximum to
    `A − M + 2λ/3` (control C3 in the ledger), because near `v = L` the needed saving
    `(2/3)(L − v)` is itself close to zero.

### 7.2 Why zero slack in the main exponent is not a defect

The lemma claims `Z^{M+ε}` for every fixed `ε > 0`. Section 18.8 chooses the parameters in this
order:
* `ρ, σ, δ` first, with `T_term = ρ + δ + ρ/6 + 3σ + 5σ/3 < ε/4`;
* then `ξ, η, ε_0 < ε/(16 C_* D)`, with `ξ < δ/2`.

At this stage the exceptional rows cost at most `(A − M)_+ + 3σ`, plus
`5δ_fr,1/6 + δ_fr,2/6 + 2θ_N` (inside `C_*ξ`) and the `ε_1` shares.

* In the zero-slot padded core `(A − M)_+ ≤ 2ξ < δ`, so the terminal loss `δ + 3σ` is inside
  `T_term`.
* With positive slots, `A − M ≤ −(6κ−1)z ≤ 0`.
* The terminal loss is taken once per branch, as a maximum, not a sum.

So `δ > 0` is not spare room. It is the price of the padding, paid from `ε`. The spare room is
`ε − T_term − C_*D(η + ξ + ε_0) > ε − ε/4 − 3ε/16 > 0`, and it is positive by construction.

### 7.3 Inventory of every loss at the stage

| loss | size | can it break the stage? |
|---|---|---|
| mask divisors in L18.3, `2^{ω(𝔑_*)}` | `Z^{O(1/log log Z)}` since `q_{𝔑_*} ≤ Z^{B_*}` | no: `Z^{o(1)}`, in an `ε_0` share |
| `c_{ϑ,𝔑_*}` size | `≪ log log Z` | no |
| separated heights `(1+|t|)^{2J}` | integrated against a Fourier measure with rapid decay | no, given the imported seminorm lemmas; it raises seminorm orders, not the exponent of `Z` |
| exceptional count `ε_1`; finite `S`, unit and sector choices | `Z^{ε_1}`, `O(1)` | no |
| `𝔱`-allocations `C_N^{ω(𝔱)}` | `≪ q_𝔱^a` for any fixed `a > 0`, with `q_𝔱` of polynomial size | no |
| `𝔱`-dyads, retained frequency dyads | `O(log Z)` each | no |
| `e_j`, `ω_j`, `θ_N` (slot ratios) | `≤ 2θ_N = 2H_N/log Z` | no: `O(ξ)` after the threshold `log Z ≥ C H_N/ξ` |
| `δ_fr,1`, `δ_fr,2` | `< ξ` | no: in `C_*ξ` |
| `g − J_+`, `ℓ`, `w/3` in `F_1` | `≤ 22σ/9 < 3σ` | no: terminal |
| padded core `A − M` | `≤ 2ξ < δ` | no: terminal |

**Bottom line.** I found no fixed positive power of `Z` among the losses. A failure would need:
* a fixed-power loss in the count; or
* a fixed additive loss in `r` near `v = L`; or
* a gap in `F_1 + F_2 ≥ 2v/3`.

None of these was found.

## 8. Errors and gaps found

**No wrong step found in lines 13953-13996 or 14312-14778.** The remarks below are wording or
dependency points. None changes a statement.

1. **13990-13991, "equals some `ϑ ∈ Θ` on units".** This should read "agrees with its primitive
   inducing character `ϑ ∈ Θ` on ideals coprime to its zeros". Editorial only.
2. **Lemma 18.3 statement (14548-14560).** It does not say that `l` runs over good ideals through
   primary generators. The global convention at 598-600 supplies this. Editorial only.
3. **Overloaded `J`.** The letter `J` is used three ways:
   * the height exponent in Lemma 18.3;
   * `J = d − c + (K_0 − K) − 2w + w_o` in (old-eq:2.8);
   * the bold `𝐉` for allocations.

   The meanings never mix in an argument. Notational only.
4. **14651.** "`c` is `Z^{ε_1}`-bounded" is true but weak (`≪ log log Z`).
5. **Dependency, not an error (13320-13335, 13910-13935).** The single Fourier measure, common to
   the live labels and both rectangles, is what makes Lemma 18.2 true. Its `L¹` and moment bounds,
   uniform in the sector, come from lem:smooth-calculus and lem:kernel-seminorms. These were not
   re-proved here (gap (2) in the header).
6. **Dependency, not an error (12512-12520, 13945-13948).** The statement that the two sides'
   inducing characters differ by a member of `Θ` uses the hypothesis that `Θ` contains every
   character used to separate the fixed reciprocity phases, and `n ↦ χ_n(−1)`. This depends on
   the fixed bicharacter table of Lemmas 4.3-4.4, which were reviewed separately and not
   re-checked here.

**Smallest repair.** None is needed for correctness. A one-line change at 13990 would remove the
only ambiguous phrase.

## 9. EMPIRICAL model of Lemma 18.3 (`theta_row_lattice.py`)

### 9.1 Model

* **Points.** The manuscript's conventions (568-600): `O = Z[ω]`, `S = {(2), (1−ω)}`, primary
  generators `z = a + bω` with `a ≡ 1`, `b ≡ 0 (mod 3)` and odd norm. All 3,627,565 such `z` with
  `q_z ≤ 1.2·10^7` were enumerated.
* **Characters `ϑ`.** All have conductor in `S`:
  * principal;
  * cubic (`z mod 2 ∈ F_4^*`);
  * sextic (the cubic character times the quadratic character read off `z³ mod 4`).

  Multiplicativity was checked on 4,000 random pairs (M0).
* **Masks.** Products of the first `k` prime ideals outside `S` (norms 7, 7, 13, 13, 19, 19, 25,
  31, …).
* **Profiles.** `C^∞` bumps on `[1,3]` and `[1/2,2]`.
* **Centred input.** `X_1 = X_2 = √T` and `(V_1, V_2) = (T^a, T^{1−a})` with `a ∈ {1/4, 0.4}`,
  modelling the comparison `Y_1 = Z^L`. The norm power is `t = 3.7`.
* **Statistic.** `ρ = |S_c|·min/T`. Lemma 18.3 predicts that `ρ` stays bounded up to the mask's
  divisor factor. The uncentred `|L_1L_2|/T` should match the volume main term.

### 9.2 Results

* **E1.** The Möbius identity of the proof holds to relative deviation `8·10^{−14}`.
* **E2.**
  * One coefficient `c_{𝔑_*}` serves for all `X` and `t`: `|L/main − 1|` at `X = 3·10^6` is
    `7·10^{−7}`, `3·10^{−6}` and `1·10^{−3}` for `t = 0`, `3.7` and `20`.
  * The absolute error is at most 3.4, 4.7 and 33 respectively. It grows with `t`, as the
    `(1+|t|)^J` factor allows, and stays below `2^{ω} = 64`.
* **E3.** Principal `ϑ`:
  * the computed main terms cancel to `< 10^{−15}·T`;
  * `ρ ≤ 0.17` with no mask, and `ρ ≤ 0.48` with the 6-prime mask;
  * the uncentred `|L_1L_2|/T` is 0.0471 (no mask) and 0.0149 (mask), within 0.1% of the
    predicted volume term at `T = 10^9`;
  * at `T = 10^9` the centred `|S_c|/T` lies between `10^{−6}` and `3·10^{−4}`.
* **E3b.** For the sextic character (conductor 4) there is no main term. Once `T ≥ 10^7`, the
  uncentred term is below `1.3·10^{−5}·T` and the centred term below `2.1·10^{−5}·T`.
* **E7.** The direct double sum over `(l_1, l_2)` with `D_b` equals the product form.

### 9.3 Controls that must fail, and divisor loss

**Controls** (`a = 0.4`, mask of 6 primes; `ρ_centred = 0.48` at `T = 10^9`). Columns: measured
`|S|/T`, the value predicted from the non-cancelling main terms, and `ρ` for
`T = 10^6, 10^7, 10^8, 10^9`.

| control | measured `|S|/T` at `10^9` | predicted | `ρ` by `T` |
|---|---|---|---|
| C1 product mismatch `V_2 → 1.05 V_2` | 0.00292 | 0.00284 | 0.54, 1.72, 4.82, 11.6 |
| C2 different norm powers `t_1 = 3.7`, `t_2 = 0` | 0.0298 | 0.0298 | 6.1, 4.7, 19.2, 118.8 |
| C3 different masks in the two rectangles | 0.0127 | 0.0127 | 3.1, 7.9, 20.0, 50.6 |
| C4 sharp cutoff `1_[1,2)`, no mask | 0.00021 | — | 0.06, 0.24, 0.49, 0.85 (smooth: 0.058, 0.028, 0.016, 0.004) |

* In C1-C3, `|S|/T` does not decay and matches the predicted non-cancelling term. So `ρ` grows in
  proportion to the minimum scale, as it must once a hypothesis of Lemma 18.2 is broken.
* C4 shows that the `O(1)` lattice error needs smooth profiles. The manuscript keeps all plain
  profiles smooth, and the exceptional branch does not clip.

**Divisor-type loss (E5).** Setup: `T = 10^9`, minimum scale 1000, mask with `ω = 0, …, 16`
primes.
* `ρ` rises from 0.007 to 0.88 at `ω = 11`, then falls as the mask shrinks the main terms.
* `ρ/max(1, #{d ∣ 𝔑_* : q_d ∈ [min/30, 3·min]})` stays between 0.0018 and 0.074.
* `ρ` stays far below `2^{ω}`.

So the model's error follows the number of mask divisors near the smallest scale, as Section 4
predicts.

### 9.4 Honesty notes on the numerics

* **Recalibrated criteria.** The first run of `theta_row_lattice.py` used badly calibrated pass
  criteria:
  * a relative main-term test at `t = 20`, where `|I(20)|` is tiny;
  * a fixed threshold of 0.02 for `|uncentred|/T`;
  * a "grows tenfold" test, when the minimum scale grows only 5.6-fold.

  Five checks "failed" for those reasons, not because of the mathematics. The final criteria
  compare the measurements with the predicted main terms, and they were chosen after seeing the
  first run. The raw tables are in `results/theta_row_lattice.json`.
* **Limits.** Ordinary float64. Scales up to `10^7`, so the minimum scale is at most about 4,000.
  Masks have at most 16 primes. Lemma 18.3 is tested in isolation, with no transforms, no slots
  and no `𝔱`-allocation. This is not evidence for the asymptotic claim. It only shows that the
  model behaves as the lemma predicts and that the controls fail as predicted.

## 10. What was and was not checked

**Checked (read line by line, rederived, and run where stated):**
* the statement and proof of Lemma 18.2 against the constructions it cites (13114-13950, read);
* the proof of Lemma 18.3, every step;
* the exceptional count;
* the raw-volume step;
* (2.15)-(2.19), with exact symbolic and rational checks;
* the application of Lemma 18.3, including the choice of the first side, the `𝔱`-dyad
  inequality and the unclipped formal scales;
* the inventory of losses against the parameter order of Section 18.8.

**Not checked:**
* **Imported or helper lemmas, read as statements only:**
  * the `L¹` and moment bounds of the separating Fourier measure (lem:smooth-calculus,
    lem:kernel-seminorms);
  * the reciprocity and fixed bicharacter table (Lemmas 4.3-4.4);
  * the correlation identities (lem:full-correlation, lem:complete-support-correlation);
  * lem:fixed-numerator-ray.
* **Mathematics not recomputed:**
  * the Kummer-theory step "`ϑ ∈ Θ` forces one class of `v_p(h')` mod 6", which was reasoned
    but not computed;
  * the local Gauss values of the amplifier, where only the valuation set `{1,6,7}` was rederived.
* **Other parts of the proof:**
  * the first-transform, enlargement and second-transform text, which was read for coefficient
    preservation but not replayed (`LEMMA18_1_COMMON_SUPPORT.md` replays it);
  * case 2 beyond its Θ-row ledger;
  * the downstream use in Prop. 19.2.
* **Independence:** no independent human check was made.

## 11. Files

| file | content |
|---|---|
| `LEMMA18_THETA_ROW_REVIEW.md` | this note |
| `theta_row_ledger.py` | exact checks S1-S5, P1-P2, E1-E3, Z1-Z4 and controls C1-C4 (19/19 PASS) |
| `theta_row_lattice.py` | EMPIRICAL Z[ω] model of Lemma 18.3: M0-M1, E1-E7, controls C1-C4 (14/14 PASS) |
| `results/theta_row_ledger.json`, `results/theta_row_ledger_stdout.txt` | ledger output |
| `results/theta_row_lattice.json`, `results/theta_row_lattice_stdout.txt` | model output and raw tables |

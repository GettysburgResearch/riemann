# The bootstrap barrier at B ≈ 0.87496: where κ ≥ 3/4 is used, the stage-3 map, and what actually binds

Sources: main paper `dl/qrh_main.txt` (line refs below), companion `dl/qrh_1112.txt`, Liu `dl/liu_2610.12234.txt`.
Numerics: `notes/stage3_closed.py` (closed-form row-count exponent, reproduces Liu's B_new = 0.8749570 and his
critical class δ_c = (49−√921)/48 = 0.38858, R* = 2/3 exactly).

## 1. Where κ ≥ 3/4 is used in Lemma 18.1 (fourth moment with short prime factors), and in Lemma 17.1

Statement (main 9368–9417): for 3/4 ≤ κ ≤ 1, Σ_{k∈R_z} |S(n1)S(n2)Q|² ≪ Z^{M+ε} provided
  n1 + n2 + 6κz = A + (6κ−1)z ≤ M            (18.3)
and, for κ < 1, β* ≤ (1+κ)/2. The paper keeps κ = 2β*−1 "dynamic" (9405–9408) so the hypothesis holds by equality.

Every place κ enters the proof (grep over 9330–10986):
* (18.11)–(18.12), lines 9572–9617: the ONLY analytic use of the zero-free hypothesis. L'/L(s_κ+e+it, ψ) ≪ log(Q(3+|t|)²) on
  ℜs = s_κ := (1+κ)/2 (Lemma 4.9 global part), Mellin inversion of each prime slot with contour at ℜs = s_κ + e gives the
  *pointwise* bound |Q_ω|² ≤ C Z^{κz+ε₁}·(seminorm)(1+|ω|)^h on rows outside Θ. Nothing here needs κ ≥ 3/4; it needs
  β* ≤ s_κ, i.e. κ ≥ 2β*−1. For κ = 1 it is unconditional (prime counting).
* (18.13), line 9643: z ≤ M/(6κ) ≤ 2M/9 and κz ≤ M/6. Only κz ≤ M/6 is used (terminal width-floor loss ρ/6); it follows
  from (18.3) for every κ > 0. The "2M/9" is cosmetic.
* Line 9652 (reflection/comparison step, Sec. 18.2): "(6κ−1)z ≤ M−A < M/6 and 6κ−1 ≥ 7/2, hence z < M/21 < M/20", feeding
  (18.15)–(18.16): A_comp ≤ 3M/2 − A + 2z + ξ ≤ 23M/30 + ξ and A_comp + (6κ−1)z ≤ 14M/15 + ξ, "margin ≥ M/15". THIS IS THE
  ONLY STEP THAT USES κ ≥ 3/4 NUMERICALLY. For general κ the same lines give z < M/(6(6κ−1)); the two comparison targets
  (A_comp ≤ 5M/6, A_comp + (6κ−1)z ≤ M) hold with positive margin iff 2z < M/6, i.e. iff 6κ−1 > 2, i.e. κ > 1/2. The margin
  is M(1/6 − 1/(3(6κ−1))), which is ≥ M/15 at κ = 3/4 and → 0 as κ ↓ 1/2. (At κ = 1/2 the comparison lengths collide.)
* (18.38)–(18.39), lines 10499–10541 (the heart of the capacity): a removed slot of length d lowers the affine expression
  A + (6κ−1)z by 6κ d and costs κ d in the squared exponent (pointwise bound (18.12)); the ledger (18.38) says a Poisson
  transform raises the excess F_act by at most 6(w+ℓ) + δ_fr,1 + 2θ_N while the child width envelope is Δ_child ≥ w + ℓ (18.33).
  Hence greedy removal costs F_act/6 + κη ≤ Δ_child + … . The ratio (cost per unit excess) = κ/(6κ) = 1/6 is κ-INDEPENDENT:
  the coefficient 6κ in (18.3) is exactly forced by [pointwise cost κ per unit length] × [ledger rate 6 per unit of width gain].
  So the "modified capacity" 2m + c(κ)z ≤ 1 has c(κ) = 6κ for ALL κ — the lemma as written is already the κ-optimal form of
  this proof; c cannot be lowered below 6κ without improving either the pointwise prime bound (i.e. κ itself) or the
  transform ledger constant 6 in (18.38).
* (18.51), line 10877: |ΔM| + |ΔA| + 5|Δz| "because 0 ≤ 6κ−1 ≤ 5": needs only κ ≥ 1/6.
* Uniformity statements (9401, 9617, 10923, 10940, 11853): the mesh/losses are uniform on the compact range [3/4,1]; the
  proof gives the same uniformity on any compact [κ₀,1] with κ₀ > 1/2.
* Exceptional (Θ-induced) rows, Sec. 18.7 (10570–10700): the count Z^{(m−f)/6} (rows h′ = h₀v⁶, sextic reciprocity) and the
  threshold A ≤ 5M/6 are κ-free; the prime product is bounded by volume there, not by (18.12).

CONCLUSION (Lemma 18.1): the proof extends verbatim to κ ∈ [κ₀, 1] for any κ₀ > 1/2, with the SAME capacity
n1 + n2 + 6κz ≤ M and hypothesis β* ≤ (1+κ)/2, margins shrinking like (1/6 − 1/(3(6κ−1))). No better c(κ) than 6κ is
available from this argument. In a stage with β* ≤ B₁ known one may take κ = 2B₁ − 1 (Liu's observation, which also kills the
Δ/4 loss of (19.6)).

Lemma 17.1 (marked inverse moment, 6951–6963): hypotheses r + 2z ≤ m − c₁ and 2r + 8z ≤ 3m − c₂. NO κ, NO zero-free input
anywhere (proof = completed row energy of Sec. 14 + two masked Poisson transforms, Sec. 17.5–17.6). The inverse capacity
z_M(r) = (1−r)/2 (19.2) is therefore untouched by any bootstrap. Sec. 17.7, Lemma 17.6: Σ_{u≍U, 6th-power-free}|M_u(U^r)|² ≪
U^{e(r)+ε}, e(r) = max{1, (1+5r)/6}; the slope α = 5/6 comes from the injectivity of (u,a) ↦ ua⁶ with P = (H/U)^{1/6} amplifier
primes and the sharp family mean square Σ_{qu≤H}|M_u(D)|² ≪ H (H ≥ D^{1+c}). It is unconditional; a zero-free region cannot
improve it (a pointwise bound U^{κr} per row gives row-count exponent 1 + (κ−δ)r ≥ 1, useless).

Where Part II uses β* ≤ 11/12: only (12.2) δ = 2a−1 ≤ κ ≤ 5/6 = α, needed (i) so that the long-witness count 1−α+(α−δ)r is
increasing in r and r ≤ t gives L(t) (11211, 19.4), (ii) for the compact κ-range [3/4,5/6] in the mesh (11853), (iii) for δ ≤ 5/6
in (20.11), (11803), (11876). With β* ≤ 7/8 known all three hold with 5/6 replaced by 3/4; the 11/12 input is then redundant.

## 2. Stage-3 analysis: the iteration map

Known: β* ≤ B₁. Assume β* > σ₀ (Prop. 2.1 with C(s) = s + c). Liu's general-geometry bookkeeping (his (0.1), (18.5), (22.5)):
balanced scales lx + ly = 1 − ℓ, b = ly − lx, h = (1+b+3ℓ)/2, direct bound Z^{lx/2+b/12}, principal exponent C(s) = s + lx/3 − 5/6 + ℓ/6,
hence the comparison boundary is σ₀ = B(ℓ) = 11/12 − ℓ/4 (+ (8b+3ℓ−3)₊/12 + (5ℓ−1)₊/8). The nonprincipal exponent of a row class
(δ, x) at d = h is
  E = −1/4 + b/6 + 5ℓ/4 + (1/2+ℓ)δ + ℓxδ − h(1−R*(δ,x;κ)),   δ = 2a−1 ∈ (1/50, 2B₁−1],  x = q/δ ∈ [0,1/2],
and the contradiction needs E ≤ 0 for every class (plus floor bin a = 51/100 with R = 1: −C₀ > (1/2+3ℓ/2)/50, C₀ = −1/4+b/6+5ℓ/4;
intermediate rows E_B(1/2) < 0 with R = 76/75 − 2δ/3; small rows ly/2 − 13h/75 − 1/50 > 0; 5ℓ − h > 0; ℓ/h > 7/37).
The count exponent (Prop. 19.2 / Liu §23), with c_κ = 1/(6κ):
  F_I(r) = r + 2x·(1−r)/2,  F_S(r) = 2m + 2x·c_κ(1−2m),  m = t − r,  R_short(t) = 1 − δ·min_r max(F_I,F_S),
  R_long(t) = 1 − δ + (α−δ)(t−1),  R*(δ,x;κ) = min_{t∈[1,3/2]} max(R_short, R_long).
The stage-3 input B₁ enters ONLY through κ = 2B₁−1 in F_S and through the bin ceiling δ ≤ 2B₁−1. Define
  Φ(B₁) := min over (ℓ, b) of B(ℓ,b) subject to sup_{δ≤2B₁−1, x} E ≤ 0 and the side constraints, with κ = 2B₁ − 1.

Numerical results (stage3_closed.py):
  Φ(7/8) = 0.87495698 (= Liu's B_new; critical class δ = 0.388, x = 1/2, R* = 2/3, b ≈ 0.122, ℓ ≈ 0.16684)
  Φ(0.87495698) = 0.87495692;  fixed point B_∞ = 0.8749569 = B_new − 6·10⁻⁸ (Liu's "≈ 4.5·10⁻⁸").
  The iteration converges in one step: dΦ/dκ ≈ 8·10⁻⁴, so Φ(B) − B_new ≈ 1.7·10⁻³·(B − 7/8).
  (a) Lemma 18.1 used unchanged all the way down to κ = 1/2 (i.e. a hypothetical β* ≤ 3/4 input): B = 0.874708 (κ=0.6: 0.874840).
  (b) "Modified capacity": none exists beyond c(κ) = 6κ (Sec. 1), so (b) = (a). Even the extreme cP = 2 (capacity 2m + 2κz ≤ 1,
      far beyond anything the proof gives) only yields 0.873485.
Role of the other inputs at the critical class (t* = 1.124, r* = 0.716, m* = 0.409, z_M = 0.142, z_P = 0.041, both savings = 0.858):
  * α = 5/6: R_long(t) caps t; α → 0.80 / 0.75 / 0.70 gives 0.874792 / 0.874510 / 0.874175.
  * inverse capacity (1−r)/2 → 0.6(1−r) / 0.75(1−r): 0.873990 / 0.873287 (then the critical class moves to x ≈ 0, δ ≈ 0.29).
  * detector range t ≤ 3/2: inactive (t* = 1.12); t_max = 2 changes nothing.
  * floor a > 51/100: inactive at B_new, but it is the NEXT barrier: with the counts of all classes improved by any amount the
    optimum saturates at B = 0.872356 (ℓ = 0.17724, b = 0.0788) exactly where −C₀ = (1/2+3ℓ/2)/50 (floor rows counted with R = 1).
    Floor → 0 then gives 0.870039 (ℓ = 0.18651, b = 0.1007), where C₀ = 0 and the intermediate-row bound R = 76/75 − 2δ/3 at
    d = 1/2 saturate simultaneously; the direct estimate alone allows ℓ ≤ 1/5, i.e. B ≥ 13/15 = 0.8667.
  * 11/12 input: irrelevant once 7/8 is known (δ ≤ 3/4 < α).

## 3. Companion 11/12 paper (recursive mean square)

Its structure (lines 215–240): Σ_{N(u)≤H}|A_u(D)|² ≪ D^{1+ε}H for H = D^{1+ϑ} (Prop. 3.1, proved by a large-sieve style
recursion through cubic-theta dual sums, Sec. 4–6, with NO zero-free hypothesis), then sixth-power amplification
A_{p⁶}(D) = A_1(D) + O(D/Y), Y = H^{1/6}: |A_1|² ≪ D^{1+ε}H^{5/6} + D²H^{−1/3} ⇒ A_1(D) ≪ D^{11/12+5ϑ/12}.
Natural limit: 11/12 = (1 + α)/2 with α = 5/6 — the same amplification slope as Lemma 17.6 (e(r) = (1+5r)/6). It is rigid
because the family mean square is sharp at H = D (diagonal), and amplification can only trade family size against the
1/6-power of amplifier primes. Iterating it with a 7/8 input does nothing: no exponent in the recursion depends on β*; the
only β*-sensitive object would be a pointwise bound A_u(D) ≪ D^{β*+ε}, which never beats the trivial/diagonal term. To go
below 11/12 one needs the zero-detector + moment + probe mechanism of Part II (which itself consumes Lemma 17.6's α in L(t)).

## 4. Output

(i) Binding obstruction. In the zero class a = (1+δ_c)/2 ≈ 0.694 (δ_c = (49−√921)/48) with maximal prime amplitude x = 1/2,
the row-count exponent furnished by balancing Lemma 17.1 (capacity z ≤ (1−r)/2, no κ) against Lemma 17.6 (slope α = 5/6) and
Lemma 18.1 (capacity z ≤ (1−2m)/(6κ)) is R* = 2/3, and at R = 2/3 the b-derivative of E vanishes (∂_bE = R/2 − 1/3, the 1/6
being the direct bound's b/12 Cauchy term and the 1/2 being ∂h/∂b). The inequality
   1 + δ_c − (1+δ_c)M/2 + δ_c ℓ ≤ B     (Liu (25.2), the E ≤ 0 condition at this class)
together with the direct-estimate constraints B ≥ 5/6 + M/12 − ℓ/6 and B ≥ 1/3 + 7M/12 + ℓ/3 forces B ≥ (7+18δ_c)/(9+18δ_c) = B_new.
κ enters only via the plain capacity in F_S, whose weight at the crossing is tiny (dB/dκ ≈ 8·10⁻⁴), so no bootstrap on κ can
move B_new by more than ~10⁻⁷ per stage and ~2.5·10⁻⁴ in total even with κ → 1/2.

(ii) Candidate modified lemma that WOULD unlock a third stage. Not Lemma 18.1 with a new capacity (c(κ) = 6κ is already
optimal for its proof). What would help is a larger INVERSE capacity:
   Lemma 17.1′: Σ_{qu≪Z^m}|M_u(Z^r)Q_u|² ≪ Z^{m+ε} whenever r + z/c_I ≤ m − c₁ (and the second constraint relaxed accordingly),
   with c_I > 1/2. Predicted bounds (κ = 3/4, same geometry system): c_I = 0.6 → B ≈ 0.87399; c_I = 3/4 → 0.87329.
Or an amplification with slope α < 5/6 in Lemma 17.6 (α = 0.75 → 0.87451). Either way the next walls are the floor bin
(0.87236) and C₀ ≤ 0 / intermediate rows (0.87004); the direct cubic-theta bound caps everything at ℓ = 1/5, B = 13/15.

(iii) Genuine new idea. The known half-plane cannot be fed back into the moment lemmas (17.1, 17.6 are unconditional; 18.1
already uses it optimally through κ), and the detector t ≤ 3/2 slack is unused. The obstruction is a COUNT of family members
u (qu ≍ U) whose twisted L(s, νχ_·(u)) has a zero at Re s ≈ 0.69: the moments give U^{2/3} and we need U^{2/3−η}. This is a
zero-density problem for the sextic family at σ ≈ 0.69, and the paper attacks it with pure 2nd/4th moments only. The classical
way to beat moment counts at a spike of size V = U^{δr/2} with δ ≈ 0.39 is a Halász–Montgomery large-values inequality
(#{u : |M_r(u)| ≥ V} ≪ (G V^{−2} + G U^{?} V^{−6}) …) built from the sextic large sieve of Sec. 9 plus the duality/ Poisson
machinery of Sec. 17 — i.e. a "large values" version of Lemma 17.1 rather than a mean value, which gains exactly when the
spike exponent δr/2 is large relative to r (here δr ≈ 0.28). A second, cheaper idea: exploit that the critical class has
x = 1/2, i.e. the physical prime sums are at their maximal size P^{δ/2}; a zero at a ≈ 0.69 forces prime sums over the row
character to be large on MANY scales simultaneously (explicit formula), so the selected-prime gain 2qz could be replaced by a
gain over a longer, multi-scale prime product, which is equivalent to raising the inverse capacity c_I in (ii).

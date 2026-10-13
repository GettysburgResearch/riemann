# W. Crack hunter: nine mechanisms against 0.874957, with exponent bookkeeping

```text
Status: EXPLORATORY (hand bookkeeping + quick runs of scripts/exponent_model.py variants; script exp/W/w_checks.py)
Scope: the Part II exponent system (20.4)/(18.4) and the direct bound (Liu Prop 22.2); every number below is a model
       number in that system, not a theorem
Sources: qrh_main.txt lines 375-470 (Prop 2.1), 2684-2830 ((6.1)-(6.2)), 3417-3620 (Lemma 8.1, Prop 8.3),
       6957-7010 (Lemma 17.1), 9249-9300 (Lemma 17.6), 11137-11215 (Prop 19.2), 11480-11700 (Sec 20); notes A, B,
       I, J, N, O, Q, S0, V
What was run: exp/W/w_checks.py (delta cap, primes-only counts, class-resolved row savings); runtime 90 s
Smallest remaining gap: none of the nine mechanisms moves the modelled boundary; the one with content is Section 9
```

Conventions. Balanced scales lx = (1−b−ℓ)/2, ly = (1+b−ℓ)/2, h = (1+b+3ℓ)/2; B_low = 11/12 − ℓ/4 + b(θ−1/12) +
(8b+3ℓ−3)₊/12 + (5ℓ−1)₊/8; at frequency d = h and class δ = 2a−1, amplitude ratio x,
E(h; δ, x) = C0 + δ(1/2+ℓ) + xδℓ − h(1−R(δ,x)) with C0 = −1/4 + 5ℓ/4 + b/6 (relative to C(7/8)); the proof needs
max E ≤ 0. Paper/Liu optimum B = 0.874957 at (b,ℓ) = (0.123, 0.1668), active class (δ,x) = (0.389, 1/2), R* = 2/3.
Three facts used repeatedly: (F1) floor identity: at δ → 0, R = 1, E ≤ 0 is ℓ ≤ lx/2 + b/12 ⇔ B ≥ 2/3 + b/6 + ℓ;
(F2) with R = 1−δ at every class, ∂_δ E = 1/2 + ℓ(1+x) − h = ℓ(x−1/2) − b/2 ≤ 0, so density-hypothesis counts push
the binding class to δ → 0; (F3) the two reflectable coefficient classes are θ, θ̄ (note I §0): μ = θ³ ↦ θ under
Poisson (reflectable), plain 1 ↦ μθ (not), so a plain or prime-supported factor enters only as a mark, cost 2z.

## Ranking (gain in B; "0" means the exponent system is provably unchanged)

| rank | mechanism | modelled B | stopped by |
|---|---|---|---|
| 1 | §9 class-resolved cross-row mean value (zero rows, not floor rows) | 13/15 if f ≥ 0.05 on all classes ≤ 5/6; 0.8747 if only δ ≤ 0.4; **0.874956 if only δ ≤ 0.2** | needs cancellation among rows *with zeros* at their bin contour: a ratios-type mean value over a zero-defined set |
| 2 | §4 explicit-formula / primes-only detector | 1.0896 (sextic sieve); 0.8739 only with a defect-free sieve | (UP)^{2/3} of Lemma 9.1 for prime-supported vectors (Patterson prime bias, note V slope 0.74) + zero interference |
| 3 | §6 swap the Poisson variable (dual of s instead of m) | not closed; direct side loses P_a^{1/3} (J §6) | no cubic-theta reflection for the sextic s-variable |
| 4 | §7 cubic companions (ζ_F(3z) instead of ζ_F(6z)) | formally 3/4 − ℓ/4 | companions ua^6 are rows of the family; sextic row character forced by γ₁γ₂ = μ·α·G |
| 5 | §2 pair / group of targets = row weight P(u) = Σ c_n χ̄_u(n) | 0 (exact) | extraction identity: signal × c₁, rows × ‖P‖; P = 1_S scales both by density |
| 6 | §5 positivity / second moment of the ratio | 0 (circular) | Σ|1+ξF|² − U − Σ|F|² needs Σ|F|² to O(U^{1/2}) = ratios conjecture |
| 7 | §3 δ ≤ 3/4 cap from the proven half-plane | 0.874956 for every d_max ∈ [0.4, 5/6] | binding class 0.389 < any cap; κ use already at fixed point (note B) |
| 8 | §1 test functions W0, W1, Gaussian | 0 (exact) | no term of (20.4) depends on the weight class; entire Mellin transforms do not vanish on lines |
| 9 | §8 Z-average weakening of Prop 2.1 | 0 | Plancherel in log Z orthogonalises heights, not rows; heights already ≤ Z^τ |

## 1. Test function (mechanism (1))

(a) Replace W0, W1 ∈ C_c^∞ and Φ(t) = e^{t²} in (6.1) by weights whose Mellin transforms are small on the lines
Re s = a + 16e of the worst class, or by Beurling–Selberg majorants/minorants of the dyadic cutoffs.

(b) Bookkeeping. The five terms of (20.4) are: a − 7/8 (contour Re s = a+16e, forced by the zero class, Lemma 8.1);
h(17/50 − 1/6) (Re z = z0 against the ζ_F(6z) pole; cancels at d = h); −a·ly (the Z^{s+z−1}X^{·}Y^{·} outside power
at the contour); −(1−a)ℓ − (δ/2−q)ℓ (slot amplitudes, Prop 16.1); d(R + δ/2 − 17/50) (count × numerator
U^{δ/2} on Re w = 1−a−6e × U^{−z0}). None contains a seminorm of W0, W1 or Φ: the weights enter only as
"finitely many smooth seminorms" in the implied constants (Lemma 17.1 statement) and as the (1+T1)^A height factors
with T1 = Z^τ, τ ≤ dmin/100. The signal C(s) = s − 5/6 + lx/3 + ℓ/6 takes the weights at the double residue
(w,z) = (1, 1/6) — a nonzero constant.

(c) Stopping inequality: the row bound is ∫_{Re s = a+16e}|Ŵ(s)|·|integrand| |ds|; Ŵ is entire of exponential
type, so it cannot vanish on a vertical line, and any zero set of Ŵ is discrete, measure zero on the line.
A majorant/minorant changes the row bound by O(1) and the signal by O(1). A weight with slower decay in Im only
enlarges the height window T1 (more zeros, same exponents).

(d) Verdict: exactly 0. The weight class is invisible to every exponent.

## 2. Two targets at once (mechanism (2))

(a) Three versions. (i) Product probe I_η·I_η′: signal Z^{C(β*)+C(β*′)}, direct Z^{2L_low}, cross terms
Z^{C(β*)}·Z^{C(β*′)−σ}. (ii) Family {ηχ_n²}: twist the primal m-sum by Σ_n c_n χ_n(m). Poisson in m sends
χ_s(m)χ_n(m) to χ̄_H(s)χ̄_H(n)·g(χ_n)χ_n(s)²·(phase) with row range U ↦ U·q_n; at the principal row u = a^6 the
factor χ̄_u(n) = 1 and the s-sum acquires χ_n(s)², i.e. the n-th term is the probe for the target ηχ_n². So the
"family" version is identical to inserting the row weight P(u) = Σ_n c_n g̃(χ_n) χ̄_u(n) with signal Σ_n c_n
g̃_n/L(s, ηχ_n²). (iii) Conjugate pair (η, η̄): real part of (ii) with n ∈ {1, conj}.

(b) Bookkeeping. (i): B solves 2C(B) = 2L_low, the same B; if β*′ < β* the signal is smaller. (ii): the direct bound
is Σ_m ξ(m)P̃(m)A_mB_m ≤ ‖A‖·‖P̃B‖ ≤ ‖A‖‖B‖·max|P̃| = Z^{lx/2+b/12}·‖c‖₁ (or ‖c‖₂ with a fourth moment of B,
not available). The row side: Σ_u ξ(u)P(u)F_u with F_u = q_u^{−z}L(w,χ_u)/L(x,ηχ_u)H_u, bounded on floor rows by
U·max|P F|. The mean of P over rows is c₁ (orthogonality of the χ̄_n(u) = χ̄_u(n)·phase), and c₁ is exactly the
coefficient of 1/L(s,η) in the signal. Extraction identity: for P ≥ 0 with mean c₁ on the rows,
    signal ∝ c₁·Z^{C(β*)},   floor rows ≤ Σ_floor P(u)|F_u| ≈ c₁·U·U^{ε}·Z^{(…)},
so the ratio is unchanged for every P. The only P that lowers the row side relative to the signal is one that is
anticorrelated with the phases of F_u on floor rows, i.e. P ≈ F̄, which is §5. (Checked against the thinning
weight P = Π_{p≤N}(1/6)Σ_j χ_p(u)^j = 1_{u sextic residue mod all p ≤ N}, ‖c‖₁ = 1: rows thinned by 6^{−π(N)},
signal multiplied by c₁ = 6^{−π(N)}, and for N → ∞ with Z the signal falls below Z^{C(β*)−σ}: the contradiction
in Prop 2.1 is about holomorphy, but its hypotheses (2.4)-(2.5) are about size.)

(c) Stopping identity: mean(P) = c₁ = signal coefficient. The group version is a change of constants (|G| fixed);
the product version doubles both sides. Note S0 §4's extraction tax is the same statement for the identity rows.

(d) Verdict: 0, exactly; and it identifies that *any* row weight expressible through the family's characters is
a target-family average and pays the extraction tax.

## 3. The proven half-plane inside the zero bins (mechanism (3))

(a) Under the contradiction hypothesis β* ∈ (σ0, 7/8], so every twist's zero class satisfies a ≤ 7/8, δ ≤ 3/4; drop
the bins δ ∈ (3/4, 5/6] from the max in (20.4), and from the endpoint certificate (Lemma 20.2) and from the long
witness L(t) = 1−α+(α−δ)t.

(b) Bookkeeping (exp/W/w_checks.py, Hmod_cap): max_{δ ≤ d_max, x} E with the paper's R*: B = 0.874956 for
d_max = 5/6, 3/4, 0.70, 0.60, 0.50, 0.40 (b re-optimised 0.121–0.126, ℓ = 0.1668 throughout). The maximiser
(0.389, 1/2) lies below every cap; E is decreasing in δ above it (the capacity term h(1−R*) grows faster than
δ(1/2+ℓ+xℓ)), so the removed bins are slack by ≥ 0.005 in E. Other uses of δ ≤ 3/4: (i) κ = 2β*−1 in Lemma 18.1's
capacity 2m+6κz ≤ 1 — note B: fixed point B_new − 6·10⁻⁸; (ii) the pointwise slot bound |Q_i| ≤ P_i^{q_i} with
q ≤ δ/2 ≤ 3/8 — enters only through x ≤ 1/2, already saturated; (iii) the exceptional-row saving r′/4 in §18.5
(note O §3.5) — binds only in the hybrid construction, not in Prop 19.2; (iv) Lemma 8.1's reflected bound
U^{a−1/2}: per class, unchanged. The detector floor a0 = 51/100 and the ceiling are not coupled: moving the
ceiling does not move the balance t* = 1 + δP_x/(2J), which depends on δ and α only.

(c) Stopping fact: R*(δ,x) and E(h;δ,x) are local in δ; a cap is a constraint on a slack region.

(d) Verdict: 0 (−6·10⁻⁸ through κ, already taken).

## 4. Explicit-formula / primes-only detector (mechanism (4))

(a) Replace M_r S_m by prime sums. Explicit formula with a dyadic weight φ at scale N = U^z:
Σ_p ψ_u(p) log p · p^{−s} φ(p/N) = −Σ_{ρ′} φ̃(ρ′−s)N^{ρ′−s} + (trivial zeros). Normalised by N^{1/2}, the extreme
zero ρ (Lemma 8.1 bin) gives a term N^{σ−1/2} = U^{zδ/2}, so a prime witness P_z has the same amplitude per unit
length as the inverse witness: |P_z|² ≫ U^{δz} (compare |M_r|² ≫ U^{δr}, |S_m|⁴ ≫ U^{2δm}).

(b) Bookkeeping. Two independent losses.
(α) Interference: all other zeros in the window have Re ρ′ < a+2e (Lemma 8.1), and ≍ log U of them lie within
height 1 of γ; they contribute ≤ U^{z(δ/2+2e)}·log U·(Σ_{ρ′}|φ̃(ρ′−s)| ≪ log U), i.e. U^{2ez}log²U times the
main term, with undetermined phases N^{iγ′}. The truncated inverse of Prop 8.3 has no such term (it uses L(ρ) = 0
and a global bound to the left; no zero-free region is needed on the left). A positive-definite kernel cannot repair
this: for complex ρ′−1/2 the Weil-type positivity h ↦ |Σ c_n n^{it}|² fails off the line
(Σ c_n n^{s}·Σ c_m m^{−s} is not a square modulus). So the witness is only ≫ U^{δz−2ez} on a subset of scales, and
the adversary picks the scale.
(β) Capacity (F3): a prime-supported coefficient has primal class 1, dual class μθ, not reflectable; it enters
Lemma 17.1 only as a mark (cost 2z) or Lemma 9.1 directly. The sextic sieve gives Σ_u|P_z^k|² ≪ (U + U^{kz} +
U^{2(1+kz)/3})·U^ε, i.e. Lindelöf-quality iff kz ≤ 1/2 (the (UP)^{2/3} term), so a 2k-th moment buys the count
#B ≪ U^{1−kδz} ≤ U^{1−δ/2}: R_prime(δ) = 1 − δ/2. Removing the inverse polynomial (r = 0) gives exactly the task's
z ≤ 1/2, i.e. the same R = 1 − δ/2.
Model (Hmod_R): R = 1−δ/2 at all classes: **B = 1.0896** (the primes-only detector does not even reproduce 7/8;
compare R* = 2/3 against 1−δ_c/2 = 0.806 at the binding class). With the (UP)^{2/3} term removed for
prime-supported vectors (kz ≤ 1): R = 1−δ, **B = 0.8739** (then floor bin and intermediate rows bind; the dial
table's 0.8724 is the same regime with the intermediate coupling relaxed).
Where Lemma 17.1's r + 2z ≤ 1 stops the multi-scale version with the inverse polynomial kept: the prime product
is a mark of length z, so z ≤ (1−r)/2 = 0.14 at r* = 0.72, below the supply ℓ/h = 0.205; the dial c_M = 1
(r + z ≤ 1) is worth 0.874052 and then the supply binds (note A §3).

(c) Stopping inequalities: (i) the (AB)^{2/3} term for prime-supported coefficients — DFDH's extremal sequence is
g̃(n) on squarefree n, and note V's primes-only series has slope 0.74 = 5/6 − 1/log X, so the Patterson prime bias
is of full strength and the term is sharp up to logs for primes too; (ii) the interference term (α).

(d) Verdict: negative (1.09); 0.8739 only with a provably false sieve; the Möbius polynomial is essential precisely
because μ = θ³ is the reflectable class.

## 5. Sign structure / positivity (mechanism (5))

(a) Σ_u ξ(u)F_u = ½(Σ_u|1+ξ(u)F_u|² − U − Σ_u|F_u|²), and the cubic variant with |1 + ξF|² replaced by
|1 + ξF + ξ̄F̄|-type sums.

(b) Bookkeeping. The identity is exact; the two positive sums are each ≍ U (F_u ≍ U^{ε} on floor rows), and the
target is U^{1/2+δ0/2}. Hence both Σ|1+ξF|² and Σ|F|² need asymptotics with error O(U^{1/2}); the second is the
second moment of the ratio L(w,χ_u)/L(x,ηχ_u) at Re x = a < 1, where 1/L has no convergent Dirichlet series, over
the zero-defined floor set. The one-sided use (Σ|1+ξF|² ≥ 0 and its ξ ↦ −ξ twin) gives |Re Σ ξF| ≤ (U + Σ|F|²)/2,
which is 2|Re ξF| ≤ 1 + |F|², i.e. the triangle inequality with a worse constant. Is the second moment of the ratio
easier than the first? Expand |L(w)/L(x)|² = L(w)L̄(w̄)/(L(x)L̄(x̄)): the denominator is the product over the pair
(ηχ_u, η̄χ̄_u), both in the family; its mollified version is Σ_u |M_r(u)|²|L(w)|² with M_r the Möbius polynomial
of the *conjugate pair*, i.e. a hybrid moment Σ|M_r S_m|²-type object (note O: covered region r ≤ 0.17 against
needed 0.84) with the same resolution cost Z^{η} as note N §2. No.
Where would a saving live? exp/W/w_checks.py (Hmod_f): a saving U^{−f} applied to all classes δ ≤ d1 gives
B = 0.874956 for d1 ≤ 0.2 and any f ≤ 1/2; 0.874718 for d1 = 0.4; 13/15 = 0.866667 for d1 = 5/6 and f ≥ 0.05
(then B_low's reflected penalty (5ℓ−1)₊/8 pins ℓ = 1/5). **Cancellation on floor rows alone is worth nothing at the
current counts; the saving has to cover the rows with zeros of class up to ≥ 0.4** (consistent with F2: only with
ideal counts does the floor become binding, note N §6).

(c) Stopping statement: a signed sum over a zero-defined set needs an arithmetic weight vanishing on rows whose
twist has a zero right of the contour; no Dirichlet polynomial vanishes at zeros of L, and a majorant of the bin
indicator (the detector |M_rS_m|²U^{−δ(r+m)} ≥ 1 on the bin) is useless for a signed sum.

(d) Verdict: 0 (circular), and mis-targeted: the binding rows are zero rows.

## 6. Swap the Poisson variable (new)

(a) Poisson-dualise the additive variable s (scale Y) instead of m (scale X), so that the rows are the dual of s.

(b) Bookkeeping. Row scale h′ = 1 − ly + ℓ = h − b: fewer rows, worth b(R + δ/2 − z0) ≈ 0.123·0.53 = 0.065 in E at
the critical class if the rest of (20.4) were unchanged. Direct side: Cauchy–Schwarz over s, then the sextic sieve
in s for Σ_s|Σ_m B_mξ(m)χ̄_s(m)|²: (Q²/Y′)·max(1, P_a^{1/3}) (note J §6, first bullet), i.e. the Gram exponent
θ = 1/12 becomes 1/6 (+b/12 in B_low) and the lx/2 becomes ly/2 (+b/2): total +7b/12 ≈ 0.072 on the direct side
against −0.065·(1/(1+slope)) on the row side; net ≈ 0.

(c) Stopping fact: the Möbius pairing (A) and Patterson's reflection (B) live in the c-variable (cubic theta, 3-fold
cover); the s-variable carries the 6-fold Kubota Eisenstein coefficient γ₁(s)χ̄_s(m), which has a functional
equation but no cuspidal theta and no quadratic reflection twist (C). The rows would couple to the direct side
sextically, and note F's general fact applies: a direct sharp n-th order sieve yields σ0 = 1.

(d) Verdict: not closed in 40 minutes, but every known ingredient points to ≥ 11/12; not a candidate.

## 7. Cubic companions: changing the 5/6 (new)

(a) The signal shift 5/6 is the residue of ζ_F(6z) at z = 1/6, the count U^{1/6} of companions u·a^6 of the
principal row. If the companions were cubes, C(s) = s − 2/3 + lx/3 + ℓ/6 and B = L_low + 2/3 − lx/3 − ℓ/6 =
**3/4 − ℓ/4** with the same direct bound.

(b)–(c) The companions are sixth powers because χ_{ua^6} = χ_u for the sextic row character, and the row character
is sextic because the m-sum carries χ_s(m) with s the sextic Gauss-sum variable, which is what pairs with the cubic
γ₂(c) to produce μ(c) in (4.7). The companions are rows of the family (not an artefact of the weight): any sieve on
the dual frequency is a convolution on the primal m-sum of conductor ≍ U, which the direct side cannot absorb
(a twist of conductor U multiplies the row range by U, §2(a)(ii)). So 1/N with N = 6 is the order of the family,
and note F's quartic failure shows N = 4 has no quadratic-coupled reflection.

(d) Verdict: 0; but it isolates the one exponent (1/6 ↦ 1/3) whose change would be worth 1/6 in B.

## 8. Z-average in Prop 2.1 (new)

(a) Prop 2.1 only needs ∫_0^∞|f_η(Z)|Z^{−Re C(s)}dZ/Z < ∞ locally uniformly; so (2.5) may be weakened to a
dyadic L¹ (or L²) mean in Z: ∫_Z^{2Z}|J_η − f_η| dZ/Z ≪ Z^{C(β*)−σ}.

(b) Row contributions are ∫ Z^{t}G_u(t)dt on a fixed contour; by Plancherel in log Z, the Z-mean square of
Σ_u ∫Z^tG_u dt is ∫|Σ_u G_u(t)|²dt over the height window: it removes the triangle inequality in the height
integral only, and heights are ≤ T1 = Z^{τ}, τ ≤ dmin/100 (paid as (1+T1)^A already).

(d) Verdict: 0 (a correct weakening with O(Z^{τ}) value). Recorded because it is the only place where Prop 2.1's
hypotheses can be loosened at all.

## 9. Class-resolved cross-row mean value — the best candidate, carried furthest

(a) Construction. Keep the paper's per-bin contours (Re x = a + 16e for the bin of class a). On that contour every
row of the bin has |1/L(x,ηχ_u)| ≪ U^{ε} (Lemma 8.1), so the bin sum Σ_{u ∈ bin(a)} ξ(u)F_u is, like the floor sum
of note N §3, a main-term-free oscillating sum over U^{R(δ)} terms. The mechanism is a saving U^{−f} on each bin
sum relative to the triangle inequality, uniformly in the class.

(b) Bookkeeping (Hmod_f, Hfloor_f; reflected penalty kept, paper's counts):
    f on classes δ ≤ 0.05:  0.874956     f on δ ≤ 0.2: 0.874956     f on δ ≤ 0.4: 0.874718
    f ≥ 0.05 on δ ≤ 5/6:    13/15 = 0.866667 at (b,ℓ) = (0.205, 0.200), pinned by B_low's (5ℓ−1)₊/8;
    with that penalty removed the dial table's 0.8485 (f = 0.1) and 0.8095 (f = 0.25) apply.
So the value of cancellation is concentrated on the zero rows of class 0.39 ≤ δ ≤ 5/6, where the bins are of size
U^{R*} ≤ U^{2/3}, not on the floor. Note V's empirical U^{0.52±0.03} for the floor sum is encouraging but it was
measured on the floor; the relevant experiment has not been run.

(c) The inequality that stops it, exactly: the bin is zero-defined. To average, Σ_{bin(a)} = Σ_{class ≤ a} −
Σ_{class < a}, and Σ_{class ≤ a} at contour a contains no unbounded 1/L (all classes ≤ a are zero-free right of
a+6e) — so, unlike the floor, **no row with a zero right of the contour is ever included**: the obstruction of
note N §5(ii) ("Σ_all contains 1/L on rows with zeros") disappears for the cumulative sets {class ≤ a}. What
remains is that {class ≤ a} is still not arithmetic: a mean value over it needs an indicator, and the only
indicators available are detector weights, which majorise the complement, not the set. The required statement:
    (W)  Σ_{u ≍ U, class(u) ≤ a} ξ(u) q_u^{−z} L(w,χ_u)H_u / L(x,ηχ_u)  ≪  U^{R(2a−1)(1−f) + (2a−1)/2 + ε}
         on Re x = a + 16e, Re w = 1 − a − 6e, for every a ∈ [51/100, 11/12], some f > 0.
At a = 11/12 this is the full family (all rows are zero-free right of 11/12 + e by Part I), an honest ratios-type
mean value with no zero-defined restriction — but it is the a that does not matter (§3). At a = a_c = 0.694 it is
the statement that matters, and the set depends on zeros.

(d) Verdict: the only mechanism whose modelled value is large (13/15 inside all side constraints, 0.81–0.85 with the
reflected penalty also removed) and whose obstruction is not a sharp diagonal; it is Lindelöf-strength for the
family (note N) at every class except the top one.

## Summary (≤ 400 words)

Nine mechanisms were bookkept against the Part II exponent system. Six are exactly zero: the test function (no
term of (20.4) sees the weight class; an entire Mellin transform cannot vanish on a line), the δ ≤ 3/4 cap (the
binding class 0.389 lies below every cap; B = 0.874956 for d_max from 0.4 to 5/6), the pair/group of targets (any
row weight built from the family's characters is a target-family average and pays the extraction tax exactly:
signal × c₁ = mean of the weight), the positivity identity (needs the second moment of the ratio to O(U^{1/2}),
which is the ratios conjecture; the one-sided form is the triangle inequality), the Z-average weakening of Prop 2.1
(Plancherel over heights, not rows), and the cubic-companion normalisation (3/4 − ℓ/4 formally, but the sixth-power
companions are rows of the family, forced by the sextic Möbius pairing). The primes-only detector is negative
(B = 1.09): a prime coefficient is of class 1, not reflectable, so its capacity is kz ≤ 1/2 from the (UP)^{2/3} term
of the sextic sieve — sharp for primes too, since the Patterson prime bias has full strength (note V) — and the
explicit-formula witness suffers interference from the ≍ log U zeros within e of the extreme one; even a defect-free
sieve gives only 0.8739. The Poisson-variable swap trades b/3 on the rows for 7b/12 on the direct side and has no
cubic-theta reflection.

The single result with content is the location of the wall. A power saving U^{−f} over rows applied only to
classes δ ≤ 0.2 (the floor and the near-floor continuum) changes nothing (0.874956); applied up to δ ≤ 0.4 it is
worth 0.0002; applied to all classes it is worth 13/15 inside the full constraint system (then the reflected
majorant penalty (5ℓ−1)₊/8 pins ℓ = 1/5) and 0.81–0.85 without that penalty. So the binding object is the sum over
rows *with zeros* of class ≈ 0.39–0.83 at their own bin contours, where 1/L is bounded on every included row — the
statement (W) of §9. Its obstruction is weaker than note N's (no unbounded 1/L is ever included, because the
cumulative sets {class ≤ a} are zero-free right of the contour), but the sets are still zero-defined.

Best candidate: (W). What to do next, in order: (1) run note V's floor-row experiment on the *cumulative* sets
{class ≤ a} at Re x = a + e for a ∈ {0.6, 0.7, 0.8} with the row L-values (not polynomials), to see whether the
U^{0.52} persists for rows with zeros; (2) if it does, attempt (W) at the top class a = 11/12 only (an honest
family mean value, no zero restriction) as a sanity theorem; (3) in parallel, re-examine Liu's reflected penalty
(5ℓ−1)₊/8, which becomes the next wall at 13/15 the moment any class-uniform saving exists. If (1) fails for zero
rows, the architecture's wall is correctly described by note N and nothing in this list moves it.

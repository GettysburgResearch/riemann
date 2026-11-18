# CRIT23 Level-2 audit, part 1 of 2: steps S1–S5 in the principal source (Alpöge–Furman)

```text
Status: EXPLORATORY AUDIT (Level 2, part 1 of 2). No new mathematical claim. Nothing here says RH is proved,
        or closer to proved. The theorems audited are asymptotic lim inf lower bounds for proportions of zeros.
Scope: load-bearing steps S1-S5 of ARCHITECTURE.md (Section 5), read in the principal source
        Alpoge-Furman arXiv:2608.13637v2 (AF), with the Lamzouri arXiv:2609.02882v2 (LZ) counterparts
        compared step by step. S6-S10 (prime-side second moment, weight removal, window optimisation,
        counting bookkeeping, Knausgard layer) are part 2. The five task questions are answered in Section 1;
        the headline constants are recomputed here as well, because they are cheap to recompute.
Exact sources or dependencies: AF v2 PDF sha256 6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444
        and its LaTeX source (e-print tarball sha256 d6a2e5ca0b1d2cece6597ccdfc6cbb0f458739113f28ca4ce84ac307de6b682d,
        file paper-v5-draft18.tex); LZ v2 PDF sha256 305df7fcbbf96e61ccca2cbae13dcb2b7f9251b054d02dd0c78551982621046b
        and its LaTeX source (tarball sha256 70370356f7010c422c92b6e467e86e8e9fe5a40696a5990e61f05582d4b3cf59,
        file ZetaZerosV2.tex). Zero ordinates: Observatory EXP-0001 (Arb-certified, first 100,000 zeros).
What was actually run: line-by-line reading of AF Sections 1.1-1.2, 2, 3, 4, 6 (source and PDF) and LZ Section 2
        and the Thm 1.1 proof; hand re-derivation of every S1-S5 statement; five independent Python scripts
        (experiments/code/claims_2026/crit23_part1/, outputs *.out next to them), all non-rigorous floating point
        except the sympy exact identities. No author code, Lean, or repository content was run.
Smallest remaining gap: none inside S1-S5 that affects any stated result. One proof step of AF Prop 4.2 is
        invalid as written for a class of zeros (finding P1-F1); the Proposition remains true with a two-line
        repair (given in Section 2.5). The analytic second moment (S6) is not audited here.
```

## 1. Answers to the task questions

### 1.1 What takes the proportion from 5/12 to 2/3

The proof does not use Levinson–Conrey mollification, a zero-density estimate, derivatives of ζ, or pair-correlation information beyond Fourier support [−1, 1]. It is Montgomery's 1973 second-moment argument with the RH-dependent step removed. Montgomery's argument gave 2/3 simple zeros under RH; the Montgomery–Taylor window gave 0.6725.

* **The second moment.** The pair-correlation second moment Σ_{ρ,ρ′} K(γ_ρ − γ_ρ′)², with test-function support log X = log(T/2π), is unconditional on the prime side. This was known before AF (Aryan 2022; BGSTB24). Under RH the zero side is a sum of nonnegative terms. Without RH, off-line pairs make the individual terms complex and of either sign.
* **The new step (S3 + S4).** AF never read the zero side term by term. They read it as tr G̃² for one real symmetric d × d matrix G̃ = (aL²)⁻¹ Σ_ρ m_ρ v_ρ v_ρᵀ, which is the compression of Weil's form to d ≈ N modulated copies of the window. Note that G̃ is built with the bilinear vv^T, not vv^*. The matrix splits into three kinds of piece:
  * each simple on-line zero contributes a PSD rank-one piece;
  * each multiple on-line point contributes a PSD rank-one piece with trace m;
  * each off-line pair {ρ, 1 − ρ̄} contributes a block of signature (1,1) and trace exactly 2m (up to a truncation error). The exact trace is AF Lemma 2.1, the Poisson–Gabor identity, used at complex arguments.
* **The inequality.** One spectral inequality on the whole form replaces termwise positivity. This is AF Lemma 3.2, the rank–trace inequality r ≥ 2 tr P + 4 tr Q − 4b − ‖P + Q‖²_HS. Applied to P₁ (the simple on-line zeros) and Q′ = G̃ − P₁, it gives N₀ˢ ≥ 4 tr G̃ − 2N − ‖G̃‖²_HS = (2 − R(ψ))N. Its scalar shadows are m² ≥ 2m − 1 (Montgomery) and m² ≥ 3m − 2 (Conrey–Ghosh–Gonek).
* **The constants.** The inequality turns the second-moment constant R(ψ) into 2 − R(ψ) and (3 − R(ψ))/2. The flat window gives R = 4/3, hence 2/3 and 5/6; the MT window gives 0.6725… and 0.8362….

This audit confirms independently that both matrix ingredients are exact for the actual AF construction:
* the bilinear trace of every zero, on-line or off-line, is 1 per unit multiplicity to 1e−12 (Section 2.2(A));
* the off-line blocks have signature exactly (1,1) even at depth |β − ½| = 0.48 (Section 2.3).

The jump from 5/12 is therefore not an incremental gain over PRZZ. It comes from a different method, whose RH-conditional value had always been 2/3.

### 1.2 Which inputs are unconditional

| Step | Inputs | Unconditional? |
|---|---|---|
| S1 | Functional equation ξ(s) = ξ(1−s); Schwarz reflection; 0 ≤ β ≤ 1 (Euler product plus functional equation) | yes |
| S2 | Weil explicit formula for F ∈ C²_c with supp F ⊂ [−log X, log X] (classical, [IK04 §5.5]); Paley–Wiener / integration by parts; Poisson summation | yes |
| S3 | Sylvester's law of inertia (AF Lemma 3.1) | yes (pure algebra) |
| S4 | von Neumann trace inequality; spectral theorem | yes (pure algebra) |
| S5 | Riemann–von Mangoldt; N(t, t+1) ≪ log t [Tit86 Thm 9.2]; the bound (2.8) | yes |

AF's Prop 4.2 writes |Im γ_ρ| < 1/2, i.e. 0 < β < 1, and that is classically equivalent to ζ(1+it) ≠ 0, the weakest zero-free region. Only |Im γ_ρ| ≤ 1/2 is needed, because (2.8) gives e^{L|Im z|/2} ≤ X^{1/4} in either case. So AF's sentence "no … zero-free region is used" is accurate for S1–S5, even in this weakest sense.

RH, GLH, pair-correlation conjectures and zero-density hypotheses appear nowhere in S1–S5. The overall input list, including S6 and the Korobov–Vinogradov region used inside BGSTB24 on the LZ route, is in ARCHITECTURE.md §4 and is part 2's business.

### 1.3 Load-bearing steps

The ten steps of ARCHITECTURE.md §5 stand. This part audits S1–S5 in AF; part 2 audits S6–S10.

| # | Step | AF location |
|---|---|---|
| S1 | encoding and conjugation symmetry | §1.2, §2.2–2.3 |
| S2 | the second moment as a real-symmetric object: explicit formula (2.2) → (2.11), Lemma 2.1 | §2.1–2.3 |
| S3 | block and inertia structure | Prop 4.1, Lemma 3.1, §6 regrouping |
| S4 | rank–trace inequality | Lemma 3.2, §6 chain |
| S5 | trace normalisation, localisation and tail | §2.2 grid, Props 4.2–4.3, Cor 4.5 |

Within part 1, the smallest statement whose failure would sink the theorem is Lemma 3.2 together with the inertia count n₊(Q′) ≤ s₂ + p. Both are verified here: by hand, on the actual AF matrices, by 20,000 random instances of every intermediate inequality, and by an L-BFGS adversarial search.

### 1.4 Constants recomputed from the stated formulas

Script `constants_part1.py` (mpmath, 40 digits; sympy exact).

| Quantity | Stated | Recomputed |
|---|---|---|
| ∬_{[−½,½]²} \|u−v\| | 1/3 | 1/3 (sympy, exact) ⇒ R(ψ₀) = 4/3 |
| Thm A (i), (ii), flat window | 2/3, 5/6 | 2/3, 5/6 (exact) |
| R(ψ_MT) by quadrature vs C_MT = ½ + cot(1/√2)/√2 | equal | 1.3274992963205883542656202092 (difference 0 at 30 digits) |
| 2 − C_MT | 0.67250… | 0.6725007036794116457343798 |
| (3 − C_MT)/2 | 0.83625… (abstract: 0.8362) | 0.8362503518397058228671899 |
| AF Lean form c_MT = √2 tan(1/√2)/(1 + tan(1/√2)/√2) | 1/c_MT = C_MT | 1/c_MT − C_MT = 0 (40 digits) |
| MT stationarity G(u) = ψ + ∫\|u−v\|ψ | constant | 1.21960728200841437 at u = 0, 0.17, 0.33, 0.5 |
| AF App. B.4 Cauchy–Schwarz stage 2/R − 1 | 1/2, 0.5066 | 0.5, 0.506592135712141 |
| AF Rem. 6.1 H(λ) = 2 − 1/λ − λ/3 | maximum at λ = 1 | H′ = λ⁻² − 1/3 > 0 on (0,1]; H(1) = 2/3; R_λ(ψ₀) = 1/λ + λ/3 re-derived |
| AF §7.2(b) extremal configuration | tr = 1, HS² = 4/3, s₁ = 2/3, N_d = 5/6 | identical (sympy); both certificates are tight there |

### 1.5 Do the two proofs share an unverified lemma (within S1–S5)?

No. Step by step:

* **S1.** Each proof has its own one-line argument. Both are correct. LZ's text uses 1 − ρ̄: the bar is lost in pdftotext but present in the source, line 876.
* **S2.**
  * AF use Weil's explicit formula plus their own Lemma 2.1.
  * LZ use only the Fourier identity ΣK² = ∬|F|² in L²(−λ, λ); in LZ the explicit formula enters only inside the imported BGSTB24 Lemma 5, which belongs to S6.
  * They share no lemma. Both pieces of AF's S2 are verified here: the explicit formula is checked in AF's normalisation against the zeta zeros to 1e−13, and Lemma 2.1 is checked at complex arguments to 3e−14.
* **S3/S4.**
  * AF: von Neumann trace inequality plus Sylvester inertia.
  * LZ: Gram–Schmidt in a real structure, a nested flag U ⊂ V ⊂ W, and Bessel's inequality.
  * These are independent proofs of what is, on matched data, the same certificate. Section 2.4 shows that AF's G̃ and LZ's kernel matrix [K(z − s)] have identical trace and Hilbert–Schmidt norm, and the same spectrum up to truncation.
* **S5.** AF only. LZ needs no localisation, because their trace is exactly |Z_T| and BGSTB24 sums over exactly 0 < γ, γ′ ≤ T.

## 2. Step-by-step audit

Notation follows AF:
* γ_ρ := (ρ − ½)/i = γ + i(½ − β);
* L = l = log(T/2π) and X = T/2π;
* φ(u) = χ(L/2 + u) χ(L/2 − u) ψ(u/L)^{1/2};
* a = ‖φ‖₂²/L;
* α_k = T + 2πk/L, with 0 ≤ k < d = ⌊LT/2π⌋;
* v_ρ = (φ̂(γ_ρ − α_k))_k;
* I = [T, 2T) and I′ = [T − √T, 2T + √T).

The checks use the paper's exact construction:
* χ(t) = f(t)/(f(t) + f(1−t)) with f(t) = e^{−1/t}, a concrete admissible choice;
* both windows;
* φ̂ evaluated at complex arguments. Composite Gauss–Legendre quadrature agrees with mpmath to 6e−16. The FFT tables agree with quadrature to 4e−11 (complex arguments) and 5e−11 (real).

### 2.1 S1: encoding and conjugation symmetry

**Statement (AF §1.2, §2.3).**
* γ_ρ ∈ ℝ ⇔ β = ½.
* The functional equation pairs each off-line zero ρ with 1 − ρ̄. Then m_{1−ρ̄} = m_ρ, γ_{1−ρ̄} = conj(γ_ρ) and v_{1−ρ̄} = conj(v_ρ). Consequently G̃ and Ẽ are real symmetric.

**Verification.**
* Im γ_ρ = ½ − β, which gives the first claim.
* ξ(1 − s̄) = conj ξ(1 − s) = conj ξ(s), so ord_{1−ρ̄} ξ = ord_ρ ξ.
* γ_{1−ρ̄} = ((½ − β) + iγ)/i = γ − i(½ − β) = conj γ_ρ.
* For φ real and even, φ̂(z̄) = conj(φ̂(−z)) = conj(φ̂(z)). With α_k real this gives v_{1−ρ̄} = conj(v_ρ). The hypothesis that φ is real and even is used here: AF's φ is both.
* Re γ_{1−ρ̄} = Re γ_ρ, so a pair is always wholly inside or wholly outside I′, and the on/off partition is closed under pairing.
* The map ρ ↦ 1 − ρ sends γ_ρ to −γ_ρ. Together with the conjugation symmetry, the zero multiset is symmetric under z ↦ −z and z ↦ z̄. This is used in Section 2.2 for finding F3.

**Numerics** (`s1_s4_blocks_linalg.py`, 8 named and 120 random configurations):
* max |v_{1−ρ̄} − conj v_ρ| ≤ 7.7e−15;
* |Im v_ρ| on-line ≤ 1e−15;
* max |Im G̃| ≤ 3.6e−15;
* max |G̃ − G̃ᵀ| ≤ 9e−16.

**LZ counterpart.** Z_T = {i(ρ − ½)(log T)/2π : 0 < γ ≤ T}, i.e. z = −γ_ρ·(log T)/2π. Conjugation invariance comes from 1 − ρ̄ (LZ source line 876). This is verified.

**Verdict.** No issue.

### 2.2 S2: the second moment as a real-symmetric object

**Statement.**
* (2.2): Σ_ρ m_ρ F̂(γ_ρ) = ∫ F̂ ν_X for supp F ⊂ [−log X, log X], where ν_X = μ + Π_X + P_X, the pole terms are absorbed into Π_X, and the prime sum is P_X = −π⁻¹ Σ_{n≤X} Λ(n) n^{−1/2} cos(τ log n).
* (2.11): (G̃ + Ẽ)_{kk′} = (aL²)⁻¹ ∫ φ̂(τ − α_k) φ̂(τ − α_{k′}) ν_X(τ) dτ.
* Lemma 2.1: Σ_{k∈ℤ} φ̂(z − α_k) φ̂(z′ − α_k) = L·(φ²)^(z − z′) for all z, z′ ∈ ℂ, and in particular Σ_k φ̂(z − α_k)² = aL².
* Hence ‖G̃ + Ẽ‖²_HS = (aL²)⁻² ∬ K(τ,τ′)² ν ν′ (5.8) is the prime-side object. Its zero-side reading (full lattice) is (a²L²)⁻¹ Σ m m′ (φ²)^(γ_ρ − γ_ρ′)², Montgomery's sum.

**Verification by hand.**

*Pole absorption.*
* X^{½+iτ}/(½ + iτ) = ∫_{−∞}^{log X} e^{(½+iτ)u} du.
* So ∫ F̂(τ) X^{½+iτ}/(½ + iτ) dτ = 2π ∫_{−∞}^{log X} e^{u/2} F(u) du = 2π F̂(i/2), using supp F ⊂ [−log X, log X].
* Taking (1/π)·Re, and using the evenness of ν_X (see the evenisation point below), gives ∫ F̂ Π_X = F̂(i/2) + F̂(−i/2).

*Prime term.* ∫ F̂(τ) cos(τ log n) dτ = π(F(log n) + F(−log n)). The prime sum in (2.2) is therefore the two-sided one.

*μ normalisation.* μ(τ) = (2π)⁻¹ [Re (Γ′/Γ)(¼ + iτ/2) − log π] matches the standard −g(0) log π + (2π)⁻¹ ∫ h Re Γ′/Γ form.

*Evenisation (F3).* AF state (2.1) for even F, but apply (2.2) and (2.11) to the non-even F = (φe^{iα_k·}) ∗ (φe^{iα_{k′}·}).
* This is legitimate. The zero multiset is symmetric under γ_ρ ↦ −γ_ρ, and μ, Π_X, P_X are all even, so both sides of (2.2) depend only on the even part of F.
* By contrast, the literal (2.1), with one-sided prime sum −2 Σ Λ(n) n^{−1/2} F(log n), is wrong for non-even F.
* The regularity hypothesis is met with room: F is C⁴ (convolution of two C² functions), so |F̂(γ_ρ)| ≪ X^{1/2} |γ|⁻⁴ and the zero sum converges absolutely.

*Lemma 2.1 proof.*
* The function Υ(s) = φ̂(z − s) φ̂(z′ − s) is the Fourier transform of a continuous function supported in [−L, L] that vanishes at ±L (a convolution of two continuous functions supported on [−L/2, L/2]).
* Υ = O(|s|⁻⁴). Poisson summation at step h = 2π/L samples Υ̂ at mL. So only m = 0 survives, and the boundary terms m = ±1 vanish because H(±L) = 0. This is the critical-density point.
* The m = 0 term is h⁻¹ Υ̂(0) = L (φ²)^(z − z′).
* Justification: the periodisation is continuous and has a single nonzero Fourier coefficient, so it is constant.
* The proof contains two harmless sign slips (P1-F3, below).

**Numerics** (`s2_gabor_explicit_formula.py`).

**(A) Lemma 2.1 for the actual taper.** Both windows, L = 5 and 7, 16 random pairs with |Im| up to 0.486.
* |lhs − rhs| ≤ 2.9e−14 for |rhs| between 2 and 69.
* The bilinear trace Σ_k φ̂(z − α_k)²/aL² equals 1.000000000000 for every complex z.
* The sesquilinear Σ_k |φ̂(z − α_k)|²/aL² equals L∫φ² e^{2u Im z}/(aL²), which reaches 3.0 at |Im z| = 0.49, matching the prediction to 6 digits.

This makes concrete why the construction must be bilinear: the "trace m per zero" normalisation holds only for vv^T.

**(B) Explicit formula (2.2) in AF's normalisation against the zeta zeros.** X = 50, L = log 50. All zeros in range are simple and on the line (EXP-0001).

| Test function F̂(τ) = φ̂(τ−α)φ̂(τ−α′) | zero side Σ_ρ F̂(γ_ρ) | ∫ F̂ ν_X | difference | literal (2.1) |
|---|---|---|---|---|
| flat, α = α′ = 0 (even) | 0.000221458069 | 0.000221458069 | 6e−15 | agrees (6e−15) |
| flat, α = α′ = 30 (non-even) | 7.783928887618 | 7.783928887618 | 8e−15 | off by 3.92i |
| flat, α = 30, α′ = 31.7 | 3.133558913302 | 3.133558913302 | 3e−15 | off by 1.63i |
| flat, **AF entry (G̃+Ẽ)_{10,11} at T = 2πX = 314.16** | 0.401855646028 ·aL² | 0.401855646028 ·aL² | 1.4e−13 | off by 1.92i |
| flat, AF diagonal entry k = k′ = 20 | 1.268651296892 ·aL² | identical | 1.4e−14 | off by 2.87i |
| MT, the same five cases | — | — | ≤ 1.3e−13 | off by 1.4i–3.7i for non-even F |

The pieces are also checked separately:
* ∫ F̂ Π_X equals F̂(i/2) + F̂(−i/2) to 10 digits; for example 20.3120416321 for the even flat case.
* ∫ F̂ P_X equals −Σ Λ(n) n^{−1/2} (F(log n) + F(−log n)) to 10 digits.

**Verdict.**
* S2 is correct.
* F3 (ARCHITECTURE.md) is confirmed with an explicit numerical witness. As written, (2.1) is valid only for even F. The form (2.2) that AF actually use is valid for every F in the family, so the theorem is unaffected. The classification stays typo_or_presentation.
* P1-F3, below, records the Lemma 2.1 sign slips.

### 2.3 S3: block and inertia structure

**Statement.**

AF Prop 4.1: P := (aL²)⁻¹ Σ_on m vvᵀ ⪰ 0, rank P ≤ N₀*(I′), tr P ≤ N₀(I′), and n₊(Q) ≤ #off/2.

AF §6:
* P₁ := (aL²)⁻¹ Σ_{on₁} vvᵀ satisfies rank P₁ ≤ s₁ and tr P₁ ≤ s₁.
* Q′ := G̃ − P₁ is the pull-back of ⊕_{on≥2} m|x|² ⊕_{pairs} [[0, m],[m, 0]], so n₊(Q′) ≤ s₂ + p.
* s₁ + 2s₂ + 2p ≤ N(I′).

**Verification by hand.**

*On-line pieces.* For on-line zeros v ∈ ℝ^d, so m vvᵀ ⪰ 0 has rank 1. tr P₁ ≤ s₁ follows from Lemma 2.1 at z = z′ real: the terms are nonnegative, so truncating to 0 ≤ k < d only lowers the sum.

*Off-line pairs.*
* Write v = a + ib. Then vvᵀ + v̄v̄ᵀ = 2(aaᵀ − bbᵀ), and xᵀ(aaᵀ − bbᵀ)x = (aᵀx)² − (bᵀx)². So the block is the pull-back of diag(1, −1).
* AF omit the factor 2/(aL²) here (P1-F4, cosmetic: inertia is unchanged by positive scaling).
* As a Hermitian form on ℂ^d, x*(vvᵀ + v̄v̄ᵀ)x = ȳ₂y₁ + ȳ₁y₂ with y₁ = vᵀx and y₂ = v̄ᵀx. This is the pull-back of [[0,1],[1,0]], which confirms the §6 form.

*Lemma 3.1.* If A*Q₀A is positive definite on U, then A is injective on U and Q₀ is positive definite on AU, so dim U ≤ n₊(Q₀). This is correct over ℂ.

*Counting.* Each multiple on-line point has m ≥ 2, and each pair carries 2m ≥ 2. Hence s₁ + 2s₂ + 2p ≤ N(I′), and distinct zeros number s₁ + s₂ + 2p.

**Numerics** (`s1_s4_blocks_linalg.py`, Part A). The actual G̃ is built on a grid of d = 200, L = 6, from 8 named configurations and 120 random ones. These include multiplicities 2–3, pairs at depth up to 0.49, and tight clusters with spacing ≲ 1/L.
* min eig P ≥ −2.7e−15.
* rank P ≤ #on distinct: equal for separated points, and smaller only when on-line points nearly coincide, where the numerical rank drops.
* n₊(Q) = p and n₊(Q′) = s₂ + p in every named case. The bounds are attained, never exceeded.
* tr P₁ = s₁ to 1e−8 for points away from the grid edges.
* Every off-line pair block has signature exactly (1,1) and trace/(2m) = 1.00000000.
* (‖a‖² − ‖b‖²)/aL² = 1.00000000 and ⟨a,b⟩/aL² ≤ 2e−12. These are AF's version of LZ (2.11): ‖g‖² − ‖h‖² = 1 with g ⊥ h.
* Eigenvalues spread widely, e.g. [−2.32, 6.32] for a double pair at depth 0.478. This is why termwise positivity fails and why only the positive index is used.

**LZ counterpart.** LZ (2.8), (2.11), (2.13) and the flag U ⊂ V ⊂ W were checked against the source:
* g_z = (f_z + f_{z̄})/2 and h_z = (f_z − f_{z̄})/(2i);
* ∫ f_z·conj(f_{z̄}) = 1 gives ‖g‖² − ‖h‖² = 1, and also Re⟨g,h⟩ = 0. With the J-real structure (2.14)–(2.15), this gives ⟨g,h⟩ = 0.

These were verified.

**Verdict.** No issue apart from the cosmetic P1-F4.

### 2.4 S4: the rank–trace inequality and the §6 chain

**Statement (AF Lemma 3.2).** Let P, Q be Hermitian with P ⪰ 0, rank P ≤ r and n₊(Q) ≤ b. Then r ≥ 2 tr P + 4 tr Q − 4b − ‖P+Q‖²_HS, with equality for P = Π₁ and Q = 2Π₂.

**The §6 chain.** It is applied with (P₁, Q′), r = s₁ and b = s₂ + p:
* (i) s₁ ≥ 4 tr G̃ − 2N(I′) − ‖G̃‖²_HS;
* (ii) 2(s₁ + s₂ + p) ≥ 4 tr G̃ − ‖G̃‖²_HS − N(I′).

**Verification by hand.** Every step of the proof was re-derived:
* Write Q = Q₊ − Q₋ with Q₊Q₋ = 0, tr(PQ₊) ≥ 0 and tr(Q₊Q₋) = 0.
* By von Neumann, tr(PQ₋) ≤ Σ pᵢnᵢ with both lists sorted decreasingly. Hence ‖P‖² − 2tr(PQ₋) + ‖Q₋‖² ≥ Σ(pᵢ − nᵢ)².
* Since pᵢ = 0 for i > r, this is ≥ Σ_{i≤r}(2pᵢ − 2nᵢ − 1) + Σ_{i>r} nᵢ² ≥ 2 tr P − r − 4 tr Q₋.
* ‖Q₊‖² ≥ 4 tr Q₊ − 4 n₊(Q).
* Adding these gives the lemma.

*Chain (i).* Insert tr Q′ = tr G̃ − tr P₁ and tr P₁ + 2(s₂ + p) ≤ s₁ + 2s₂ + 2p ≤ N(I′).

*Chain (ii).* Add 2 tr P₁ ≤ 2s₁, then subtract s₁ + 2s₂ + 2p ≤ N(I′).

Both chains were checked symbol by symbol against AF lines 553–567.

**Numerics.**

*Proof steps* (`s1_s4_blocks_linalg.py` Part B). 20,000 random Hermitian instances, d ≤ 8. The minimum of LHS − RHS was:

| Step | Minimum |
|---|---|
| von Neumann | 0 |
| step 1 | −5.8e−11 (rounding) |
| step 2 | 0 |
| step 3 | −6.8e−13 (rounding) |
| final | +1.2e−6 |

*Adversarial search.* 400 L-BFGS starts minimising the slack over P = XXᵀ and Q = YYᵀ − ZZᵀ, which has n₊ ≤ b. Minimum found: −7.1e−15, i.e. 0 up to rounding; equality is attainable.

*Equality and extremal cases.* The equality case is exact in sympy (r − RHS = 0). AF §7.2(b)'s extremal configuration gives exactly 2/3 and 5/6.

*Lemma 3.1.* 3,000 random complex instances, including rank-deficient A: no violation.

*Actual AF matrices* (Part A). Lemma 3.2 slack and both chain slacks are nonnegative in all 128 configurations; the minimum Lemma 3.2 slack is 0.84. These configurations are synthetic and are not meant to be near the extremal second moment.

*Same certificate as LZ.* Put η²(u) := Lφ(Lu)²/‖φ‖². Then LZ's K(z − s) for z = −γ_ρ L/2π equals the full-lattice AF Gram entry L(φ²)^(γ_ρ − γ_ρ′)/(aL²). On every named configuration:
* tr G̃ = tr[K] to 8 digits, and ‖G̃‖²_HS = Σ K² to 1e−6 absolute.
* The nonzero spectra agree to ≤ 1.2e−10 in all 8 named cases, clusters included.
* The K-matrix is complex symmetric, but its eigenvalues are real to 6e−16, as they must be, since it shares its nonzero spectrum with the real symmetric G̃.

So AF (1.2) and LZ (2.4) give the same certificate 2N − ΣK² on matched data, and likewise (ii) and LZ (2.5). This confirms ARCHITECTURE.md's description "same operator; different coordinates".

**Verdict.** No issue. S4, the core new inequality, is correct.

### 2.5 S5: trace normalisation, localisation, tail

**Statement.**
* §2.2: d = ⌊LT/2π⌋, α₀, …, α_{d−1} ∈ [T, 2T), and "d = N(T,2T) + O(L)".
* Prop 4.2: tr G̃ = N(I′) + O_χ(T^{1/2}L²).
* Prop 4.3: ‖Ẽ‖₁ ≪ T^{−1/2}.
* Cor 4.5: tr P + 2n₊(Q) ≤ N(I) + O(√T log T).
* §6 uses only tr G̃ = N + o(N), ‖Ẽ‖_HS = o(1), and N(I′) − N(I) ≪ √T log T.

**Verification of what is used.** All of it holds. Implied constants depend only on χ and ψ, uniformly in T:
* C_χ = ‖(φ²)″‖₁ is bounded uniformly in L. Numerically ‖φ″‖₁ ≈ 8.000 (flat) and 7.64 → 7.45 (MT) for L = 4 → 6.
* There is no interchange-of-limits issue. Lemma 2.1 is an exact identity for each L, and every sum in (2.11) and (5.8) is finite in k or absolutely convergent in ρ.

**Real zeta zeros** (`s5_trace_tail.py` (D)). These are all simple and on the line in range.

| T | L | d | N(I) | N(I′) | tr G̃ (flat) | tr G̃ − N(I) | tr G̃ − N(I′) |
|---|---|---|---|---|---|---|---|
| 2000 | 5.763 | 1834 | 1957 | 2044 | 1956.3628 | −0.64 | −87.64 |
| 6000 | 6.862 | 6552 | 6921 | 7100 | 6920.7579 | −0.24 | −179.24 |
| 20000 | 8.066 | 25673 | 26904 | 27282 | 26902.8213 | −1.18 | −379.18 |

The MT window agrees to 0.02.

*Prop 4.3, real zeros.* Σ over zeros with √T ≤ dist(γ, I) ≤ 390 is 3.0e−9 (T = 2000) and 5.3e−12 (T = 6000). On-line zeros carry no e^{L/2} factor, so this is far below the X^{1/2}/T shape. Prop 4.3's own proof is correct: it uses dist(Re γ, I) ≥ √T for all excluded zeros, including γ < 0, and N(t, t+1) ≪ log t.

**Two slips in the proof of Prop 4.2 (P1-F1) and one in §2.2 (P1-F2).**

*Slip (a): the inequality |Re γ_ρ − α_k| ≥ D_ρ.* AF line 327 asserts, for k ∉ [0,d), that α_k ∉ [T, 2T) and hence |Re γ_ρ − α_k| ≥ D_ρ := dist(Re γ_ρ, {T, 2T}). The tail estimate built on this is then summed "over zeros in I′".
* For zeros with Re γ_ρ ∈ I′ \ I the inequality is false. Grid points α_k with k < 0 or k ≥ d lie right next to such zeros.
* For those zeros the "tail" Σ_{k∉[0,d)} φ̂(γ_ρ − α_k)² is essentially the whole sum aL², not ≪ X^{1/2}L D_ρ⁻³.

*Witness for (a)* (`s5_trace_tail.py` (C)). Take a real point γ = T − √T/2, so D_ρ = √T/2.

| T | tail/aL² | displayed bound shape X^{1/2} L D_ρ⁻³/(aL²) | ratio |
|---|---|---|---|
| 2000 | 0.9999997 | 3.5e−4 | 2.9e3 |
| 10⁴ | 0.9999999998 | 5.2e−5 | 1.9e4 |

Asymptotically the ratio is ≍ TL → ∞ (aL² against X^{1/2}L·8T^{−3/2}), so no implied constant rescues the displayed inequality.

The real-zero table above shows the effect in aggregate. Zeros in I′ \ I contribute ≈ 0 each (total 0.70, 0.17, 0.15 for 87, 179, 378 such zeros). The proof claims they contribute ≈ 1 each up to a small tail. Consequently tr G̃ tracks N(I), not N(I′).

*Slip (b): the grid point α_d.* The claim "k ∉ [0,d) ⇒ α_k ∉ [T,2T)" also fails for k = d whenever LT/2π ∉ ℤ. Then α_d = T + h⌊T/h⌋ ∈ [2T − h, 2T).

*Witness for (b)* (`s5_trace_tail.py` (B)): α_d = 1998.889, 3999.533, 19999.455 and 59999.698 for T = 10³, 2·10³, 10⁴ and 3·10⁴. This affects only the O(1) zeros with D_ρ < h, which the D_ρ < 1 case already covers. AF's own Prop 5.2 treats k = d, d+1 separately.

*Repair* (corrected computation). Write head_ρ := Σ_{0≤k<d} φ̂(γ_ρ − α_k)². Then
 tr G̃ − N(I) = −Σ_{ρ∈I} m tail_ρ/aL² − Σ_{ρ∈I′\I} m(1 − head_ρ/aL²) + Σ_{ρ∈I′\I} m head_ρ/aL²
 (the first sum uses AF's valid bound for Re γ ∈ I).
* For ρ ∈ I′ \ I, all α_k (0 ≤ k < d) lie on one side at distance ≥ D_ρ = dist(Re γ_ρ, I). Hence |head_ρ| ≪ X^{1/2} min(L², L D_ρ⁻³).
* Summing over zeros with N(t,t+1) ≪ log t gives |tr G̃ − N(I)| ≪ X^{1/2} L.
* Therefore tr G̃ = N(I′) − N(I′ \ I) + O(X^{1/2}L) = N(I′) + O(√T log T).

So the Proposition holds as stated, with a better error than claimed, and §6 is unaffected. The numbers in (D) agree: tr G̃ − N(I) = O(1).

*Corroboration of F7.* The sharper D_ρ < 1 tail scales like e^{L|y|}L². This is (E), with y the depth of the zero: tail/(e^{Ly}L²) ≤ 0.85 for L = 4, …, 10 and y ∈ {0, 0.25, 0.49}. It decreases in L for y > 0, and for y = 0 it tends to a constant (about (1 + a)/2, half the lattice sum plus half of φ̂(0)²). So the O(L) boundary zeros contribute ≪ X^{1/2}L, not X^{1/2}L³ as the display gives. This confirms ARCHITECTURE.md F7 (harmless).

*The value of d (P1-F2).* AF line 217 states d = N(T,2T) + O(L), and §7.2 line 589 states d = N(T,2T) + O(1).
* In fact d = (T/2π)L + O(1), while AF's own formula gives N(T,2T) = (T/2π)(L + 2 log 2 − 1) + O(log T). So d − N(T,2T) = −(2 log 2 − 1)T/2π + O(L), which is ≍ T and not O(L).

*Witness for d* (`s5_trace_tail.py` (A), N counted from the Arb table):

| T | d | N(T,2T) | d − N | −(2log2−1)T/2π | (d − N)/L |
|---|---|---|---|---|---|
| 10³ | 806 | 868 | −62 | −61.5 | −12.2 |
| 10⁴ | 11733 | 12349 | −616 | −614.8 | −83.6 |
| 3·10⁴ | 40446 | 42290 | −1844 | −1844.4 | −217.7 |

The correct statement, d = N(1 + O(1/L)) (which is AF §1.2's "d ∼ N"), is all that is ever used. d enters only as the ambient dimension. The grid density L/2π is below the zero density at heights in (T, 2T]. This is harmless, because the trace normalisation comes from Lemma 2.1, which is exact for any z, and not from counting grid points.

**Verdict.**
* The statements used from S5 are correct.
* P1-F1 is a verified local error in a proof step, with a two-line repair and no effect on any stated result.
* P1-F2 is a presentation error with an explicit witness and no effect.

## 3. Findings (part 1)

Findings carry new IDs (P1-…). Re-verified ARCHITECTURE.md findings keep their IDs.

| ID | Class | Location | Finding | Witness | Effect |
|---|---|---|---|---|---|
| P1-F1 | verified_error (local proof step; statement survives) | AF Prop 4.2 proof (source line 327; PDF p.6) | The bound \|Re γ_ρ − α_k\| ≥ D_ρ (k ∉ [0,d)) and the resulting tail bound are applied to all zeros with Re γ_ρ ∈ I′. They are false for Re γ_ρ ∈ I′ \ I, and also for k = d when LT/2π ∉ ℤ. | γ = T − √T/2: tail/aL² = 0.9999999998 vs bound shape 5.2e−5 (T = 10⁴), ratio ≍ TL; real zeros: tr G̃ − N(I′) = −87.6 / −179.2 / −379.2, i.e. ≈ −N(I′∖I); α_d ∈ [2T−h, 2T) for T = 10³ … 3·10⁴ | None. Repair in §2.5 gives tr G̃ = N(I) + O(X^{1/2}L) = N(I′) + O(√T log T), which is within the stated O(T^{1/2}L²); §6 needs only tr G̃ = N + o(N). |
| P1-F2 | typo_or_presentation (witness) | AF §2.2 (line 217), §7.2 (line 589) | "d = N(T,2T) + O(L)" / "+ O(1)" is false; d − N(T,2T) = −(2 log 2 − 1)T/2π + O(L). | T = 10⁴: d − N = −616, (d − N)/L = −83.6 | None (d is only the dimension; d ∼ N is true and is what is used). |
| P1-F3 | typo_or_presentation | AF Lemma 2.1 proof (line 246) | With φ_z(u) := φ(u)e^{izu}, one has Υ(s) = Ĥ(s), not Ĥ(−s); the Poisson phase sign is inconsistent with Υ̂(−2πm/h). | algebra; the identity itself checked to 2.9e−14 at complex z, z′ | None (only m = 0 survives; φ̂ and φ² are even). |
| P1-F4 | typo_or_presentation | AF Prop 4.1 proof (line 316) | "2m(aaᵀ − bbᵀ) is the pull-back of m·diag(1,−1)": the factor 2/(aL²) is dropped. | algebra | None (inertia is scale-invariant). |
| F3 (re-verified) | typo_or_presentation (now with numerical witness) | AF (2.1) vs (2.2)/(2.11) | (2.1) is stated for even F and is wrong for non-even F; the form (2.2), which is the one used, is right for all F in the family. | zeta zeros, X = 50: (2.2) matches to ≤ 1.4e−13 for non-even F, including AF entries (G̃+Ẽ)_{kk′}; literal (2.1) is off by 1.4i–3.9i | None. |
| F7 (re-verified) | typo_or_presentation | AF Prop 4.2 proof | The display gives √X·L³ for the D_ρ < 1 zeros, not the stated √X·L²; the sharp per-zero tail is ≍ e^{L\|y\|}L², so the true contribution is ≪ √X·L. | (E): tail/(e^{Ly}L²) ≤ 0.85 and bounded in L | None. |
| P1-N1 | no_issue_found (hypothesis check) | AF Prop 4.2, "\|Im γ_ρ\| < 1/2" | The strict inequality (0 < β < 1) is classically equivalent to ζ(1+it) ≠ 0, but only ≤ 1/2 is needed. S1–S5 use no zero-free region in any sense. | (2.8) bound with e^{L/4} either way | — |
| P1-N2 | no_issue_found_in_inspected_portion | AF §1.2, §2.1–2.3, Lemma 2.1, §3 (Lemmas 3.1, 3.2), Props 4.1, 4.3, Cor 4.5, §6 chain; LZ §2 (Prop 2.1 proof (2.8)–(2.25)) and Thm 1.1 proof (Z_T) | No error found beyond the items above. | Section 2 | — |

The findings in ARCHITECTURE.md that lie outside S1–S5 (F1, F2, F4, F5, F6) were not re-examined here.

## 4. AF versus LZ, step by step (S1–S5)

| Step | AF (principal) | LZ | Shared lemma? | Status here |
|---|---|---|---|---|
| S1 | γ_ρ = (ρ−½)/i; v_{1−ρ̄} = v̄_ρ (φ real and even) | z = i(ρ−½)(log T)/2π; Z_T conjugation-invariant via 1−ρ̄ | no (both one line, classical) | verified, numerics 1e−15 |
| S2 | Weil explicit formula (2.2) → (2.11); Poisson–Gabor Lemma 2.1 (exact for complex z) | Fourier identity K(z−s) = ⟨f_z, f_{s̄}⟩; ΣK² = ∬\|F\|² (2.12) | no | verified; (2.2) vs zeros to 1e−13; Lemma 2.1 to 3e−14 |
| S3 | P ⪰ 0 rank-one pieces; pair blocks 2m(aaᵀ−bbᵀ), signature (1,1); Lemma 3.1 | f_z = g_z + ih_z, ‖g‖² − ‖h‖² = 1, g ⊥ h; flag U ⊂ V ⊂ W | no (Sylvester vs real Gram–Schmidt) | verified on actual G̃ |
| S4 | Lemma 3.2 via von Neumann | Bessel plus range bounds (2.18)–(2.21), scalar steps (2.22)–(2.24) | no (independent proofs of the same certificate) | verified; same certificate on matched data |
| S5 | grid, Props 4.2–4.3 (C² taper needed, Rem 4.4) | not needed (exact trace \|Z_T\|; localisation inside BGSTB24, i.e. S6) | — | statement verified; proof slips P1-F1/F2, repaired |

## 5. Reproduction

All scripts are in `research/exploratory/riemann-observatory/experiments/code/claims_2026/crit23_part1/`. Run each from that directory with `python3 -I <script>`. Outputs sit beside the scripts as `<script>.out`. Environment: Python 3, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, sympy 1.14.0. The zeros come from `experiments/results/zeros/zeta_zeros_1_100000_arb.tsv.gz` (EXP-0001).

| Script | Checks | Runtime (4 vCPU, loaded) |
|---|---|---|
| `af_testfn.py` | library: AF's χ, ψ, φ, φ̂(complex z) by quadrature; FFT tables `HatTable` | — |
| `constants_part1.py` | §1.4 constants | < 1 min |
| `s1_s4_blocks_linalg.py` | S1, S3, S4 on actual G̃; LZ spectral comparison; Lemma 3.1/3.2 random and adversarial tests | ~10 min |
| `s2_gabor_explicit_formula.py` | Lemma 2.1 at complex arguments; explicit formula (2.2)/(2.11) vs zeta zeros | ~12 min |
| `s5_trace_tail.py` | d vs N(T,2T); α_d; Prop 4.2 witness; tr G̃ on real zeros; edge tails; Prop 4.3 | ~1 min |

SHA-256 of the committed-state files (after the final runs):

```text
472d8ec873dc9d464b1bf1b468d35304d66fb188542203e8f66b03030455f626  af_testfn.py
7f81c1bdd3c75a3a23d4004461aac62e7008c0a9e6cf96700b12f98f4c665f4c  constants_part1.py
82a66045e47a0740f9dc03d93d07a19e027120a114e932a4b2bbfcb8b3c1afa1  s1_s4_blocks_linalg.py
0d5ddcf60d9389fdcaa6e6d0bf22ede1d15c74203a1dde97a6cbf68ea7a1b8b9  s2_gabor_explicit_formula.py
4cc47e9576c9cd2143f37b14204dd7d13d644e13630793ba9453ddc27391ea59  s5_trace_tail.py
312ba69d5334edb0172988da8597213312757bd85c85eb8869e64b0a04a3349c  constants_part1.out
748cdf87fd56eea1cd5215e8db0c1533631cee28c38e36bc6fbd58839a705176  s1_s4_blocks_linalg.out
98ec024a286a6a5389026a045ab862b58e6706ccfaa7914972384ca52c05a58e  s2_gabor_explicit_formula.out
4ccab677ebd2be10fd548b6dc8fb678e2408481f04952e092467896d163bd7a9  s5_trace_tail.out
```

One script change was made during the audit. The first version of the LZ spectral comparison in `s1_s4_blocks_linalg.py` paired the K-matrix spectrum with the top-n eigenvalues of G̃, which drops G̃'s negative eigenvalues. That was a bug in this audit's script, not in either paper. The script now takes the n eigenvalues of largest modulus, and the mismatch fell from O(1) to ≤ 1.2e−10.

The scripts are non-rigorous: floating point, with quadrature and FFT accuracy validated against mpmath and direct quadrature as stated. The zero ordinates are Arb-certified. The sympy identities are exact.

## 6. Not done in part 1, handed to part 2

* S6: AF §5 (Props 5.2–5.5, Thm 5.7), the prime-side second moment, including its error terms; and the statement and hypotheses of BGSTB24 Lemma 5 as LZ use it.
* S7–S10: LZ weight removal, window optimisation (constants already recomputed above), counting bookkeeping including the dyadic summation for the cumulative form, and Knausgård's layer.
* No Lean development was built or replayed.
* No claim is made about the zeros not covered by the certificate. The results are lim inf lower bounds and are insensitive to o(N) off-line zeros (AF §1.4).

# Sep 30 manuscript: Lemma 17.1 initialization replay, and bounded reviews of Lemma 15.1, Lemma 20.1, Prop 2.1 and the final contradiction

```text
Status: REVIEW (bounded; external, unreviewed manuscript). Five targets from SEP30_VERIFICATION_MAP.md §4
  that were only inspected (I) or partially reviewed. Verdicts in §1. No error was found in any target.
  The Lemma 17.1 initialization transform is VERIFIED at the identity level by an end-to-end tiny-scale
  replay. Lemma 17.1 itself stays CONDITIONAL on Lemma 17.2, whose proof is unreviewed. Prop 2.1 is
  CORRECT (complete proof read line by line). The others are correct as reductions to named imported
  inputs. This is not a verdict on Theorem 1.1.
Scope: paper.tex (Sep 30). Lemma 17.1 proof 11600-12341 (overlap reduction, residual polynomial, one
  masked Poisson transform, Moebius extension, common extraction, child polynomials, fibres, margins,
  energy); Lemma 15.1 8111-8332 (+ the Lemma 14.3 statement 7747-7790 for E_ref, 7696-7725 for
  A_0,S_0,N_0,B_0); Lemma 20.1 15684-15850 (+ Lemma 10.4 hypotheses 6030-6115); Prop 2.1 380-502; the
  final contradiction 106-111, 6806-6830, 15640-15683, 16380-16463, and Lemma 11.1 6520-6580 as used there.
Exact sources or dependencies:
  [OAI] pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, standalone/2026-10-07-openai-quasi-riemann-import/
        upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
        SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed from git;
        equal to the scratch copy).
  Reused read-only (imported, not modified): reviews/sep30_eqc_check.py (exact sextic symbol tables, direct
        Gauss sums, G/r/ray class functions, lattice); reviews/sep30_l17_identities.py (a0 = conj(alpha) gamma_2,
        the ray-character expansion of G, mark helpers). Their own checks are SEP30_EQC_CHECK.md and
        SEP30_L17_IDENTITIES.md.
  Imported and NOT checked here: Lemma 17.2 (canonical marked estimate); the uniform Fourier-moment bound
        eq:inverse-fourier-moment and Lemma 4.5 calculus behind both log-Fourier separations; Lemma 14.3 (its
        E_ref formula is used as stated); Prop 16.1 eq. (5.13e); Lemmas 8.1, 8.2, 19.1; Prop 20.3; Prop 15.3;
        the principal-residue interface (Lemma 10.5); Thm 3.1; Prop 11.3.
What was actually run: reviews/sep30_misc_checks.py (new, 897 lines, SHA-256
  f4ddc4ab9e38872b21367a6947115f8dc9f7b2ab6834bac3ebdca3bb1bafe041).
  * Full: `nice -n 10 python3 -I sep30_misc_checks.py --out <scratch>/misc/full.json` passes 48/48 checks
    in 63 s. Log SHA-256 cfa785c5...1f62f1c57705, JSON bf45e3e8...b1bafe041 (scratch only).
  * Quick (`--quick`): 48/48 in 9 s.
  Residue symbols, norms, valuations, counts and booleans are exact integer arithmetic. Exponent identities
  are exact (sympy, Fraction). Gauss sums, bumps, kernels and lattice sums are double precision: EMPIRICAL,
  not certified. Tolerance 1e-9 (pointwise absolute; replay relative). Part B uses scipy HiGHS linear
  programs in floating point (EMPIRICAL); the exact identities behind them are in the sympy check B1.
  * Development history:
    - My first end-to-end configuration was vacuous: only one column carried a nonzero two-list mark,
      so only principal terms survived and six controls could not break. The non-vacuity check caught
      this, and the configurations were redesigned.
    - The redesigned run disagreed at relative error 1e-2. A per-term comparison against the formal,
      unextracted Moebius sum located the cause: my child coefficient carried nu_0(n) twice (once in the
      coefficient and once in the ray factor). The bug was mine, not the paper's. After the fix the
      agreement is 3e-15.
    - The non-vacuity threshold was first "share > 1e-4". The full run has one configuration at a share of
      1.0e-4 (j = 1, shifted Gaussian). The criterion is now "share > 1e-5 and > 1e8 x replay error".
Smallest remaining gap: inside Lemma 17.1, the two log-Fourier separations (the (1+|I_0|)-coordinate
  overlap profile, 11690-11717, and the 6-coordinate initialization profile eq:initial-joint-profile,
  11990-12005). They rest on eq:inverse-fourier-moment and were read, not replayed. Every identity
  around them is replayed with the profile evaluated at the actual coordinates. The load-bearing input of
  Lemma 17.1 is Lemma 17.2 (1,810-line proof, unreviewed). For Theorem 1.1 the final step is a correct
  assembly, so the open load-bearing input there remains Prop 20.3 and its high-side inputs.
```

RH remains unsolved. This note checks one transform and four short blocks of an external manuscript that claims a zero-free half-plane Re s > 7/8 for Hecke L-functions over Q(√−3). Correct identities and correct logical reductions do not establish the 7/8 theorem: each verdict below is conditional on the inputs it names.

## 1. Verdicts

| Node (map §4) | Lines | Old status | Verdict | Evidence |
|---|---|---|---|---|
| **Lemma 17.1**: initialization transform (reduction of 17.1 to 17.2) | 11600-12341 | U | **VERIFIED (identity level)**. The overlap reduction, the residual form, the masked Poisson transform, the Moebius extension, the common extraction, the outer weight, the child polynomials and the fibre are all replayed exactly at tiny scale; the margins and energy ledger hold. **Lemma 17.1 itself is CONDITIONAL on Lemma 17.2** and on the Fourier-moment calculus. | A1-A6 (§2); hand (§2.4) |
| **Lemma 15.1**: compensated completed-row norm | 8111-8332 | R (partial) | **CORRECT at the exponent level**, with Lemma 14.3's E_ref used as stated. Every displayed identity is exact. Over all admissible data, the maximum of E_ref − M′ is 0 (at ε = 0). The analytic transfer (Gaussian annuli, separation, row sectors) was read only. | B (§3) |
| **Lemma 20.1**: high exponent for one row bin | 15699-15841 | I | **CORRECT as a reduction** to Lemma 10.4 (bin contour accounting) with g = qℓ. The per-row bound inputs (buffered L-value, eq. (5.13e), amplitude sets) are imported. | C (§4) |
| **Prop 2.1**: continuation from a common signal | 400-502 | I | **CORRECT**: the complete proof was checked line by line. | D (§5) |
| **Thm 1.1**: final contradiction | 106-111; 6806-6830; 15640-15683; 16454-16463 | I | **CORRECT as a logical assembly.** It is conditional on Prop 20.3 (high), eq:part-II-normalized-low (Prop 15.3), the principal interface, the H_η contraction, Thm 3.1 (for Δ ≤ 1/24) and Prop 11.3. Lemma 11.1, used in this step, was also checked. | D (§6) |

Suggested map updates: Lemma 17.1 goes from U to "A + R(init)", with the note "init transform replayed; conditional on 17.2". Lemma 20.1 and Prop 2.1 go from I to R. Lemma 15.1 stays R, now with an LP certificate of its branch analysis. The Thm 1.1 assembly goes from I to R (the assembly only).

## 2. Lemma 17.1: the initialization transform

### 2.1 What the proof does (11606-12341)

1. **Overlap reduction (11606-11667).** In M_u(Z^r;W)Q_u, let j = (n, P) be the product of the slot primes that divide n. Split n = jn_0 and P = jP_0, and put c = n_0P_0. Then μ(n_0) = μ(c)μ(P_0) and ψ_u(n)ψ_u(P) = ψ_u(j)²ψ_u(c). The normalization satisfies Z^{-(r+z)/2} = Z^{-G}Z^{-D'/2} with D' = r+z−2G. The result is eq:initial-overlap-polynomial. The Z^{-G} cancels the ≪ Z^G count of assigned tuples in a triangle inequality taken before squaring.
2. **Separation and residual (11668-11745).** One log-Fourier separation of W(y_jy_c/∏y_i) leaves the residual R_0(u) of eq:initial-residual-polynomial, with conj χ_c(u) after conjugating the sign ε_χ = 1.
3. **One masked Poisson transform (11746-11860).** Expand the square with C = (c_1, c_2) and c_a = Cz_a. Apply Lemma 17.5 with mask R = C. Restore the principal pair by G(1) = 1. Keep the outer mask 𝓑_init. This gives eq:initial-formal-component.
4. **Formal extension and extraction (11861-11905).** Use 1_{(z_1,z_2)=1} = Σ_{s|(z_1,z_2)} μ(s) and z_a = sn_a, then eq:initial-common-extraction. The s-part squares to 1_{(s,h')=1}. Substitute t = C/d', k = d'h', f = d's and ρ_{t,j}.
5. **Separation, Cauchy and ledger (11906-12341).** These cover the 6-coordinate profile, the weighted Cauchy inequality with fibre D_init(f)C_init(t), the normalized quotient measure, the puncture bound, the margins, the energy and the parameter order.

### 2.2 Replay (script part A)

| Check | Claim (lines) | Result |
|---|---|---|
| A1 | eq:initial-overlap-polynomial (11650-11667). M_u Q_u is computed directly (all squarefree n from the 44 split and inert primes with N ≤ 199; three disjoint slot lists, so overlaps occur). It is compared with Σ over the 8 assigned subsets and all assigned tuples of U_{u,j}. Run on 16 rows (some divisible by slot or column primes), ν ∈ {nu6, chi4} and ε_χ = ±1, with 16,264 nonzero inner terms. | **PASS**, max rel err 1.2e-13. Five controls break, at rel err 13-45: ψ_u(j) in place of ψ_u(j)², μ(P_0) dropped, (c,j) = 1 dropped, W argument y_jy_c∏y_i in place of the ratio, μ(j) dropped |
| A1 | y_c lies in a fixed compact window (11669) | observed [0.526, 9.55] ⊂ (2.4^{-3}, 2.4^4): PASS |
| A2 | eq:initial-common-extraction, including zeros | PASS (2e-15). Three controls break: χ_n(s)⁴ dropped; conj χ_n(d's)⁴; k = h' without d' |
| A2 | \|A_*(s) conj χ_s(d')χ_s(h')\|² = 1_{(s,h')=1} when d'\|C and (s,C) = 1 (11876) | PASS, 0 failures |
| A2 | ρ_{t,j}(n)χ_n(k)χ_n(f)⁴ reproduces exactly the exclusions at C, s, j and the numerator zeros at d', h' (11893-11899) | PASS, 0 mismatches; the control "puncture without t" mismatches |
| A2 | μ(z_1)μ(z_2)γ(conj χ_{z_1}χ_{z_2}; z_1z_2) = a_0(z_1) conj a_0(z_2) G([z_2][z_1]^{-1}), with Gauss sums summed directly | PASS (2e-15) |
| A3 | eq:initial-root-kernel; κ_c = m−2D'+P_1; W_0 argument x_Cx_sx_a; F_c = N_c + V_c; κ_c + P_1 + 2F_c = m; both margin identities (12207-12212); normalization; κ split and its 3η | 10/10 exact. Formal margins are ≥ c_1 and ≥ c_2 − 4η under the premises (20,000 exact instances) |
| **A4** | **End-to-end replay.** LHS = Σ_u Φ(q_u/K)\|R_0(u)\|²/X by direct lattice summation. **RHS_A** = principal + Lemma 17.5 on raw coprime column pairs. **RHS_B** = principal zero frequency + the child form of eq:initial-separated-identity, with the joint profile evaluated at the actual coordinates. RHS_B uses μ(d')μ(s)Ĝ(ϑ), the s-mask, priority-split marks (assigned coefficients outer, surviving subcollection in the child), Q^init with k = d'h', f = d's and ρ_{t,j}, and formal norms q_s²q_{n_1}q_{n_2} in the root and kernel. Three configurations × radial and shifted Gaussian: (i) j = 13a, ν_0 = nu6, υ = 1.3, one surviving list; (ii) j = 37a·61b, ν_0 = chi4, υ = −0.7, two lists; (iii) j = 1, no slots, ν_0 = quad. X = 300, primes of norm ≤ 79, 3,336-4,636 child terms per run. | **PASS**: RHS_A max rel err 2.4e-15 and RHS_B max rel err 3.3e-15. The nonzero-frequency share is 1e-4 to 1e-2 of the LHS, so the off-diagonal is visible. All 9 controls break in at least one run: μ(s) dropped (up to 4.2), f without s, k without d', ρ without t, ρ without j, ϑ swapped, the (s,h') mask dropped, assigned slot coefficients dropped, and lcm instead of formal norm in the kernel (up to 0.69) |
| A5 | eq:initial-fibre: (C,d',s,h') → (t,k,f) has fibres of size ≤ d(f) before slots; f is squarefree; the stated reconstruction is the inverse (Z-model, 111,825 images) | PASS; max fibre 9 = d(f), so the divisor loss is needed |
| A6 | Ratio ≤ Z^τ implies log_Z q_{d'h'} ≤ M_init = 2D'−m−2P_1+6η+τ (the complement of 𝓑_init lies in the raw tail; 11760-11776) | 0 violations in 200,000 random actual exponents; the control with 5η is violated |

Expected-insensitive controls (configuration-specific, not failures):
* ρ without j does not break in configurations (ii) and (iii). In (ii) no supported column contains a prime of j together with both marks; in (iii) j = 1.
* "Assigned dropped" does not break in (iii), which has no slots.

### 2.3 What A4 establishes, and what it does not

A4 is an exact identity check of steps 3-4 and of the arithmetic content of step 5, for each fixed Fourier mode. W_0 = ω(y)y^{iυ} is complex and the marks have complex coefficients.

It does **not** replay the two Fourier inversions themselves:
* the (1+|I_0|)-dimensional overlap profile 𝔥_ov,j;
* the 6-coordinate profile eq:initial-joint-profile.

Nor does it replay their uniform moment bounds. Both are Fourier inversion of a compact profile whose larger cutoffs equal one on the retained supports. A1 checks the support claim for y_c, and A3 checks the root, kernel and W_0 exponents that make the profile Z-free. The bound eq:inverse-fourier-moment is imported, as it was for Lemma 17.2.

### 2.4 Hand checks of the remaining steps

* **Weighted Cauchy (eq:initial-weighted-count).** For each fixed t, Σ_ω|V||Q_1||Q_2| ≤ C(t) Σ_{k,f} D(f)|Q_1||Q_2|. Cauchy in (k,f) and then in t gives Z^{P_1+2η}∏_a(∫H_{a,t}dν)^{1/2} with dν = Z^{-P_1-2η}ΣC(t)δ_t. Correct.
* **Hypotheses of Lemma 17.2 for each child.**
  - The coefficient is ᾱγ_2ν_* with ν_* = ν_0 conj ϑ, a fixed ray character with modulus in S.
  - The puncture is rad(tj), which is fixed once t is frozen by the measure.
  - The mark is an original subcollection of cap z_0 = z − G.
  - The weight is D_init(f) = d(f)^{1+2K_slot}, a function of f alone.
  - f = d's is squarefree, and the row ball is 1_{0<q_k≤Z^{M_init}}.
  - The invariants: the puncture bound log_Z q_r ≤ P_1+G+3η, and the margins ≥ c_1−9η−τ and ≥ c_2−22η−3τ, both ≥ 3c̄/4 > c_* = c̄/2. These were already PASS in SEP30_INVMOMENT_REVIEW (C19-C25, D13-D15, E22-E26); A3 re-derives the identities behind them.
* **Energy.** Z^{κ_c+3η}·Z^{P_1+2η}·‖ν‖·Z^{2F_init+ε_c}, with κ_c + P_1 + 2F_c = m and F_init − F_c = δ_init ≤ 3η, gives m + 11η + π + ε_c, as displayed. Correct.
* **Principal pieces.** The diagonal is Σ_c\|coef\|²Z^{-D'}·#{q_u ≪ Z^m} ≪ Z^{m+ε}. The restored principal nonzero frequencies are ≪ d(C)Z^ε by the Lemma 17.5 bound A Σ_{h≠0}\|FΦ(Aq_h)\| ≪ 1. Both are correct.
* **Notation hazard (not an error).** At 11752 the column cofactors are named z_1, z_2 ("c_i = Cz_i"), while z_i also denotes the slot lengths in the same proof (z = Σz_i, z_0 = z − G). The script uses the cofactor meaning in A2/A4 and the slot meaning in A1/A3.

## 3. Lemma 15.1 (script part B)

* **B1 (exact, sympy).** Each displayed identity holds:
  - M′ + ℓ′ − 1 = −3d (from M = 5/6 and ℓ = 1/6 at 6862-6866);
  - the expression for T_d − (H − 3d);
  - old-eq:5.3;
  - the branch-2 energy M′ + z_a − saving ≤ M′ + (1+3ℓ′−2M′−2Δ_H+θ_N)/4 using z_a ≤ ℓ′;
  - 1 + 3ℓ′ − 2M′ = d − 1/6.
* **B2 (linear programs).** E_ref is taken from Lemma 14.3 (old-eq:4.4-4.7) with N_* = 1 + ℓ′ + θ_N. The constraints are those used in the proof:
  - O ≥ −ε and H ≤ M′ − O + ε;
  - 2A_0 ≤ O + ε and 0 ≤ N_0 ≤ A_0;
  - 0 ≤ z_a ≤ ℓ′ and S_0, B_0 ≥ 0;
  - v, ℓ_b, e_λ ≥ −ε, retention y ≤ T_d + ε, and |θ_N| ≤ ε.

  E_ref − M′ is maximized over 12 branches (the choice of u, the choice of the max, and the sign of (T_d − y)_+) for d ∈ [0, 1/6]. The maximum is **0 at ε = 0** and 10.2ε at ε = 10⁻³. This is the lemma's Z^{M′+ε} with an O(ε) loss of modest constant.

  Each of three controls makes the maximum positive: dropping z_a ≤ ℓ′, dropping 2A_0 ≤ O, or using M = 1 instead of 5/6. So each structural inequality in the proof is load-bearing.
* **Read, not verified.**
  - The structural claim 2A_0 ≤ O + ε_Z (8234-8240). Here f = 1 and ρ = 1, so the active non-slot primes outside k_res (7708) are row primes of exponent ≥ 2. The claim is plausible from the definitions.
  - The Gaussian annular decomposition and its tail (8150-8180).
  - The common-density Minkowski step, and the use of Lemma 5.2 row sectors.

## 4. Lemma 20.1 (script part C)

* The proof checks the central hypothesis eq:stage-central-bound of Lemma 10.4 with g = qℓ. The per-row bound is U^{δ/2+O(e)}·Z^{ℓ(17/50−1/2)+qℓ}, where Σℓ_ig_i = qℓ with g_i = 0 on error slots; multiplying by #𝒞 ≪ U^{R+ε} gives exactly U^{R+δ/2}Z^{ℓ(z_0−1/2)+g}. The identity is checked; the inputs are not:
  - the buffered bound L^S·𝓗 ≪ U^{δ/2+O(e)} (Lemmas 8.1/8.2);
  - |Q_i| ≤ P_i^{g_i+ϑ} (definition of the amplitude sets);
  - the joint error-slot bound eq. (5.13e) (Prop 16.1).
* The checks below are exact (sympy):
  - line 1 = line 2 of eq:common-high-exponent, with C_0 = −1/48, a = (1+δ)/2, h = 13/16, ℓ = 1/6 and l_y = 23/48;
  - line 1 = eq:stage-high-exponent at σ_0 = 7/8 and g = qℓ;
  - −(1−a)ℓ − (δ/2−q)ℓ = −ℓ/2 + qℓ.

  Two controls fail as they should: g = dq/6 (the misreading the text itself warns against) and C_0 = −1/24.
* eq:floor-bound gives E(h) = −7/1200 at R = 1 and q = δ_0/2, and the slope 67/100 is positive. E is increasing in q (coefficient 1/6), so q = δ/2 is the worst case.

## 5. Prop 2.1 (script part D; complete hand check)

Every step is correct:
1. ε_* = min(Δ_0−ω, σ) > 0. Because C has slope one, C(σ_0)+ω = C(β_*)−(Δ_0−ω), so both contracts give Z^{C(β_*)−ε_*}; and β_*−ε_* > σ_0. D checks this on 20,000 exact instances. The control with slope 1/2 fails, so slope ≥ 1 is used.
2. For Z ≤ 1, shift to Re s = B:
   - H is bounded, since |H−1| ≤ 1/2;
   - 1/L^S is bounded on Re s ≥ 2;
   - |e^{(s−5/6)²}| = e^{(σ−5/6)²−t²}.

   The horizontal integrals vanish, so f ≪ Z^{B+c}.
3. F(s) converges on Re s > β_*−ε_*, using the decay at ∞ and B > Re s at 0.
4. g(u) = e^{−(2+c)u}f(e^u) is the inverse Fourier transform of the integrable, continuous A(2+it), and g is in L¹. Fourier inversion gives F(2+it) = A(2+it) everywhere, and the identity theorem extends this to Re s > 1.
5. |H| ≥ 1/2 on Re s > σ_0 ⊃ {Re s > β_*−ε_*}, so e^{−(s−5/6)²}F/H continues 1/L^S holomorphically there. Because ε_* is independent of η and β_* is a supremum, some target has a zero with Re ρ > β_*−ε_*. The deleted Euler factors are nonzero at ρ, so 1/L^S has a pole there: contradiction.

No gap was found. The proposition is a statement about the hypothetical family-wide quantities; it does not by itself prove any zero-free region.

## 6. The final contradiction of Theorem 1.1

The assembly at 16454-16463 applies Prop 2.1 with σ_0 = 7/8, C = C_II = s − 11/16 (so C(7/8) = 3/16), J = J_II = I_modified/(c_S A_T) and f = f_II (15657). The hypotheses map as follows:

* **Common form of f_II.** f_II has the form of eq:common-residue with the same H_η, S and Gaussian.
* **Contraction.** eq:shared-principal-nonvanishing gives the contraction on Re s > 7/8. P_0 is chosen before the target (CONTOUR review: R).
* **Low contract.** eq:part-II-normalized-low gives Z^{C(7/8)+ε} for every ε. Take ω = Δ/2: ω ∈ (0, Δ), and it is independent of η. D checks this for all Δ ∈ (0, 1/24] on a grid.
* **High contract.** Prop 20.3 gives Z^{C(β_*)−m/2}, with m fixed before the target. This passes through Lemma 11.1, whose proof (τ ≤ m/(4(A+1)), then N) was checked; D checks it on 2,000 exact instances.

  The principal-interface remainders need (1+h)e < m_w = 23/960 and e < m_z = 13/9600. Both hold for e < 10⁻³, and the margin m_z − e is 17/48000 at e = 10⁻³. The control e = 1/500 violates m_z, so the cap e < 10⁻³ is load-bearing and thin.
* **Bootstrap.** Δ ≤ 1/24 comes from Thm 3.1 (β_* ≤ 11/12), and κ = 3/4+2Δ ≤ 5/6.
* **Transfer.** Prop 11.3 extends the result from primitive Hecke characters to all Hecke and Dirichlet L-functions.

The logic is correct. Its truth rests entirely on Prop 20.3, Prop 15.3, the principal interface, Thm 3.1 and Prop 11.3. Of these, Prop 20.3 and its high-side inputs (Prop 19.2, Lemmas 17.1/17.2/18.1, and the Δ/4 comparison flagged as thin by w5copg) are not reviewed.

## 7. Known misreadings to avoid

* "Lemma 17.1 verified" is wrong. The *initialization transform* is replayed; the lemma is conditional on Lemma 17.2.
* A4 is a finite exact identity at X = 300 with Gaussian rows. It certifies nothing asymptotic, and its floating-point agreement is EMPIRICAL.
* The Prop 2.1 and Thm 1.1 verdicts are about logical structure only. They do not upgrade any analytic input.
* In Lemma 20.1, qℓ = q/6 is a base-Z exponent, not dq/6. The control confirms the identity fails with the latter.

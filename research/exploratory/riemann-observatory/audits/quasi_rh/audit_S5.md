# Level-2 audit of Section 5: the iteration of the dual mean-square estimate

```text
Status: Level-2 audit of one section, done independently. It is not a review of the whole paper and does not certify the paper.
Scope: paper2.tex l.1254-1631 (Section 5: Prop. 5.1, the completed sums (eq:T), Prop. 5.2 as stated,
       Lemma 5.3, Prop. 5.4 as stated, the proof of Prop. 5.1, and the proof of Prop. 3.1 in Sec. 5.6).
       Interfaces read so that the recursion could be checked:
         - Def. (eq:energy) and Lemma 4.4 (l.938-992);
         - Prop. 4.5 (l.1000-1252);
         - Lemma 6.6 and the proof of Prop. 5.2 (l.1923-1935, l.2189-2214);
         - Lemmas 7.1-7.3 and the proof of Prop. 5.4 (l.2217-2683);
         - outline Step 5 (l.425-658).
Exact sources: github.com/openai/math @ 4eaee87548250b2682affda7d05d947c05554bae,
       preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf
       (sha256 f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18, re-hashed here).
       LaTeX source tex1112/paper2.tex (sha256 d9a8f15a...8750d4d, 3988 lines) is authoritative for formulas.
       The PDF text of Section 5 (sec_s5_iteration.txt, and p2.txt l.1351-1360 for Sec. 5.6) was compared with the tex and matches.
       DR = Dunn-Radziwill, arXiv:2109.07463 (cached text), was consulted for DR (8.2).
What was actually run (our own code, python3 -I; nothing from the OpenAI repository was run):
       experiments/code/quasi_rh/s5_cube_inversion_checks.py   (sha256 059ed456...71f8) -> .out
       experiments/code/quasi_rh/s5_recursion_bookkeeping.py   (sha256 46cff4bd...84dd6) -> .out
       experiments/code/quasi_rh/s5_energy_sanity.py           (sha256 88fa39e4...b9f2) -> .out  [exploration only]
       The Lean formalization of the 7/8 companion was NOT replayed.
Smallest remaining gap: none inside Section 5. Section 5 is a complete conditional argument:
       Prop. 5.2 (Sec. 6) + Prop. 5.4 (Sec. 7), as stated  =>  Prop. 5.1  =>  (with Prop. 4.5) Prop. 3.1.
       All analytic risk sits in Prop. 5.2 and Prop. 5.4, which this audit checks only at the interface.
```

## 0. Verdict

Section 5 is **correct as a conditional argument**. Grant Proposition 5.2 (the completed mean square, proved in Sec. 6) and Proposition 5.4 (the transfer, proved in Sec. 7) exactly as stated at l.1317-1332 and l.1487-1508. Then:

- **Lemma 5.3 (cube inversion).** The Möbius identity and both bounds are correct. We re-derived the identity by hand and verified it numerically to machine precision, including non-squarefree cube indices and composite h (§2.3). Negative controls fail, as they should.
- **The induction in Prop. 5.1 is well-founded.** There is no circular use at the same scale:
  - Every child mean square that the transfer produces has row parameter H' < H(H/Σ)² ≤ D^{-2κ}H.
  - The gap H'/Σ' ≤ H/Σ is inherited exactly; it is not eroded by constants.
  - The only "self-referential" term is the cube index b = 1, which occurs in Lemma 5.3 when X < H. It is routed through the transfer and not through the induction hypothesis, so it is harmless (finding S5-P1).
- **The number of induction levels is ⌈C₀/κ⌉ = ⌈4/ϑ⌉, independent of D.** In the application the actual recursion depth is at most ⌊(1−ϑ)/(2ϑ)⌋+1, which is 5 for ϑ = 1/10.
- **ε-losses, derivative orders and implied constants stay uniform.**
  - Each level splits ε into three parts (ε/3 three times).
  - Each level multiplies the constants by quantities that depend only on (I, ν, S, κ, C₀, ε, j).
  - The derivative order grows as J_{j+1} = max(J*, 4J_j+12). This is finite but astronomically large (≈4^{40} at ϑ = 1/10). That is harmless for the qualitative Theorem 1.1 (S5-P4).
- **Every parameter range is consistent at each hand-off:**
  - Prop 3.1 → Prop 4.5 → Prop 5.1 → {Lemma 5.3 → Prop 5.2 → Lemma 6.6; Prop 5.4 → children}.
  - The restriction ϑ ≤ 1/10 is never used (S5-P2, confirming the architecture note P2).

We found no verified error, no suspected gap and no missing hypothesis. Four presentation points are recorded (§4), all harmless.

## 1. Notation and the logical skeleton

N = N_{K/Q}, O = Z[ω], λ = 1+2ω, "primary" means ≡ 1 (mod 3). S ⊇ {(2),(λ)}, and ξ ranges over the characters of the fixed ray class group (a finite set determined by ν and S, l.809-821, l.955-956). In the energy

E(H,X,F;ξ,W) = (XF)^{-1} Σ*_{F≤N f<2F} Σ_{0<N k≤H} |Σ*_n a_ξ(n) χ_n(k) χ_n(f)⁴ W(N n/X)|²   (eq:energy, l.938-952),

the rows k are elements of O, the columns n and the twists f are squarefree primary and prime to S, and Σ := XF.

```
Prop 3.1  <=  Prop 4.5 (Sec. 4)  +  Prop 5.1 [kappa = theta/2, C0 = 2]       (Sec. 5.6, l.1613-1629)
Prop 5.1  <=  induction on j (H <= D^{j kappa}):                                (Sec. 5.5, l.1516-1609)
              level j+1  <=  Lemma 5.3 (eps/3)  +  Prop 5.4 at L = L_b (eps/3)  +  level j (eps/3) on I' = [u/16,4v]
Lemma 5.3 <=  (eq:cube-inverse) [exact identity]  +  Prop 5.2 (short part)  +  Cauchy-Schwarz/counting (long part)
Prop 5.2  <=  Lemma 6.6 (Sec. 6)        Prop 5.4 <= Lemmas 7.1-7.3 (Sec. 7)
```

## 2. Claim-by-claim verification

### S5.1 Proposition 5.1 (l.1261-1277): the statement
- **Restated:** fix κ > 0 and C₀ ≥ 1. Assume H, X, F ≥ 1, Σ = XF ≤ D^{C₀} and H ≤ ΣD^{-κ}. Then for every ε there is J = J(κ, C₀, ε) such that E(H,X,F;ξ,W) ≪_{I,ν,S,κ,C₀,ε} ‖W‖²_{C^J(I)} D^ε Σ, for every compact I ⊂ (0,∞) and every W ∈ C_c^∞(I).
- **Checked:**
  - The hypotheses imply the ranges that Lemma 5.3 needs: X ≤ Σ (since F ≥ 1), F ≤ Σ (since X ≥ 1), and H ≤ Σ ≤ D^{C₀}.
  - D ≥ 1 is forced (1 ≤ Σ ≤ D^{C₀}).
  - J is independent of I. This is essential, because the induction is applied on enlarged intervals (l.1530-1531).
- **Heuristic size:**
  - For F = 1 the bound reads Σ_{N k≤H}|Σ_n|² ≪ D^ε X² with H ≤ XD^{-κ}. This is the "optimal large sieve" shape (H+X)X in the regime H < X.
  - The exploratory computation (§3, R-sanity) shows E/X ≈ (orthogonal diagonal)/X at X ≤ 4000. This is not probative.
- **Verdict:** a well-posed statement.

### S5.2 The completed sums (eq:T), (eq:completed-twist) (l.1282-1308)
- **Restated:**
  - T(X;Ψ) = Σ*_n Σ_{b≡1(3),(b,S)=1} conj(α(n)) γ₂(n) Ψ(n) conj(α(b))³ Ψ(b)³ / (√(N n) N b) · V_*(N n N b³/X), with V_*(y) = √y W(y).
  - Ψ_k(n) = ξ(n) χ_n(k) χ_n(f)⁴, with zero extension at S.
- **Checked:**
  - V_*(y)/√(N n) = N(b)^{3/2} X^{-1/2} W(·). Hence the b = 1 part is X^{-1/2} Σ*_n a_ξ(n) χ_n(k) χ_n(f)⁴ W(N n/X), as claimed at l.1298-1299.
  - Ψ_k is completely multiplicative on ideals: χ_n(k) is the multiplicative sextic Jacobi symbol in n, and ξ is a ray class character. It vanishes off (n,S) = 1.
  - Every ideal prime to 3 has exactly one generator ≡ 1 (mod 3), because the six units represent (O/3O)^×, which has order 6. So "b ≡ 1 (3)" is an ideal sum.
- **Verdict:** correct.

### S5.3 Lemma 5.3 (l.1341-1466): cube inversion
**(a) The identity (eq:cube-inverse) (l.1361-1373).**
- Substitute (eq:T) at scale X/N(h)³. Then (X/N h³)^{-1/2} = X^{-1/2} N(h)^{3/2}.
- So the h-term carries μ(h) conj(α(h))³ Ψ(h)³ N(h)^{1/2} X^{-1/2}.
- With b = hc, multiplicativity gives conj(α(h)c)³ = conj(α(b))³, Ψ(h)³Ψ(c)³ = Ψ(b)³ and N(h)^{1/2}N(c)^{1/2} = N(b)^{1/2}.
- Hence the coefficient of (n,b) is [Σ_{h|b} μ(h)] times the T-coefficient, and the identity follows. All sums are finite (support of W), so the interchanges are harmless.
- **Numerically verified** (C1), |LHS−RHS| ≤ 2.2·10⁻¹⁶ with |LHS| ~ 0.06-0.27, in two runs:
  - genuine coefficients a(n) = conj(α(n)) γ₂(n) at X = 3000;
  - random unimodular n-coefficients at X = 1.3·10⁵. This run includes the non-squarefree cube indices π₇², π₇'² (N = 49), the composite h = π₇π₇', a row k = ω²·π₁₉·λ meeting S, f = π₁₃'π₁₉', and ξ ∈ {1, cubic character mod 2}.
- **Negative controls must fail, and do:**
  - N(h)^{-1/2} in place of N(h)^{-1}: error 0.27;
  - α(h)³ in place of conj(α(h))³ on the h-side only: error 0.025.
- Remark: replacing the cube weight consistently on both sides preserves the identity, since it is formal in any completely multiplicative cube weight. The specific factor conj(α(b))³ in (eq:T) is fixed by the theta coefficients (Lemma 6.1, Sec. 6), not by Section 5.
- **Imported:**
  - "[IK04 (1.18)]" is Möbius inversion, Σ_{d|n} μ(d) = δ_{n,1}.
  - "[DR (8.2)]" was checked against arXiv:2109.07463, text l.2738-2748. It is the same device: g̃(ur) summed against Σ_{e=cd} μ(c), with the weight |e| = N(e)^{1/2} on the cube index. That weight matches the N(b)^{1/2} produced here by V_* (DR Remark 8.3: periodicity of theta coefficients on cubes).
  - Used consistently.

**(b) Short part (eq:short-cube-bound) (l.1376-1406).**
- Normalization: E = F^{-1} Σ_f Σ_k |X^{-1/2}·(column sum)|², so E_short carries 1/F. Correct.
- Weighted Cauchy-Schwarz with weights 1/N(h) uses |μ conj(α)³ Ψ³| ≤ 1.
- **Prop. 5.2 is applicable for each h:**
  - X/N(h)³ ≥ X/H_c³ ≥ 1, since H_c³ ≤ X;
  - N(f) < 2F ≤ D^{C₀+1}, hence "range C₀+1";
  - its constant is uniform in X, f and h.
- **Summation:**
  - Σ_{N h≤H_c} N(h)^{-1} (H + 2H²F N(h)³/X) ≪ H log + H²F H_c³/X, using Σ_{N h≤H_c} N(h)² ≍ H_c³.
  - H_c³ ≤ X²/H² gives H²F H_c³/X ≤ XF = Σ, and H ≤ Σ by hypothesis.
  - The two logarithms and D^{ε/4} give D^{ε/2}. Correct.
- If H_c < 1 the short sum is empty. Correct.

**(c) Long part (l.1408-1466).**
- **Expansion:**
  - Expanding T gives the coefficient μ(h)√(N(hc)) conj(α(hc))³ Ψ_k(hc)³ / √X. This was checked as in (a).
  - Grouping by b = hc gives β₀(b,f) = conj(α(b))³ ξ(b)³ 1_{(b,f)=1} Σ_{h|b, N h>H_c} μ(h), with normalization 1/(N(b)√L_b) = N(b)^{1/2}/√X.
  - Also Ψ_k(b)³ = ξ(b)³ χ_b(k)³ χ_b(f)^{12} = ξ(b)³ χ_b(k)³ 1_{(b,f)=1}.
  - **Numerically verified:**
    - C2: P_long computed from its definition equals the b-form for H_c ∈ {1, 7, 10, 13, 30}, with difference ≤ 1.1·10⁻¹⁶.
    - C3: the identity Ψ_k(b)³ = ξ(b)³χ_b(k)³1_{(b,f)=1} holds for all 17 b in range, including prime powers, with error ≤ 3.7·10⁻¹⁵.
    - |β₀| ≤ τ_div(b) held in every case.
- **Estimates:**
  - Cauchy-Schwarz with weights τ(b)/N(b) gives E_long ≤ (Στ/N) Σ_b τ(b)/N(b) · E(H, L_b, F). The b-term is exactly E(H,L_b,F): (1/F)Σ_fΣ_k|L_b^{-1/2}Σ_n|² = (L_bF)^{-1}Σ_fΣ_k|Σ_n|².
  - Σ_{N b≤R} τ(b)/N(b) ≤ (Σ_{N c≤R} 1/N c)² ≪ log²(2R). Correct.
  - Terms with 1/v ≤ L_b ≤ 1 have O_I(1) columns, so E(H,L_b,F) ≪_I (H/L_b)‖W‖²_∞ ≤ vΣ‖W‖²_∞, using H ≤ Σ. Correct.
  - Then E ≤ 2E_short + 2E_long, and the logarithms are absorbed using X ≤ D^{C₀}. Correct.
- "Empty when H² ≤ X": then H_c = X^{1/3}, so N(b) > H_c forces L_b < 1. Correct.
- If the supremum is nonempty, then N(b)³ ∈ (X²/H², X) forces H² > X and H_c³ = X²/H². Correct.
- **Verdict:** Lemma 5.3 is correct, with J = J(ε, C₀) independent of I.

### S5.4 Proposition 5.2 (l.1317-1332): interface only
- **Restated:** Σ_{0<N k≪H} |T(X;k,f)|² ≪ D^ε ‖W‖²_{C^J} (H + H²N(f)/X) for 1 ≤ H, X, N(f) ≤ D^{C₀}.
- Proved in Sec. 6; outside our scope.
- **Interface checked (proof l.2189-2214):**
  - k = u₀sv² gives T(X;u₀sv²,f) = T(X;u₀s,fv²) pointwise, since χ_n(v)² = χ_n(v)⁸ and χ_b(v)⁶ = χ_b(v)^{24}, zeros included. Numerically verified (C4): 60 000 (row, prime) cases, including v divisible by 2 or λ, and three full T-sums. 0 failures.
  - Lemma 6.6 is applied with row bound H/N(v)² ≥ 1 and N(g) ≤ H N(f), which needs range 2C₀. In Lemma 5.3's use this is 2(C₀+1). Consistent.
  - The v-sum gives ζ_K(2). Correct.
- **Verdict:** consistent with its use in Lemma 5.3.

### S5.5 Proposition 5.4 (l.1470-1508): interface only
- **Restated:**
  - For 1 ≤ H, L, F, Σ ≤ D^{C₀} with max{H, LF} ≤ Σ: A(W) ≪ D^ε Σ ‖W‖²_{C^{4m+12}(I)} (1 + sup E(H',X',F';ξ',U)/Σ').
  - The supremum runs over H', X', F' ≥ 1 with H' ≤ HL/(ΣF), H'/Σ' ≤ H/Σ and Σ' ≤ L, over ξ' in the fixed group, and over U ∈ C_c^∞([u/16, 4v]) with ‖U‖_{C^m} ≤ 1.
- **Checked:**
  - E(H,L,F) ≤ A(W), because Φ ≥ 0 and Φ ≥ 1 on [0,1]. The k = 0 term of A is nonnegative.
  - A suitable Φ exists: square a real radial Schwartz ψ with compactly supported Fourier transform and ψ(0) ≠ 0, then rescale.
- **Interface with Lemma 7.3 (l.2496-2670), which is what makes the supremum well-defined.** For the children (H', X'/N(j), F'N(j)), j | r, the paper shows the following, and we re-derived each step:
  - H' = HL/(ΣFR²) ≥ F' ≥ 1, since F' ≤ N(f') ≤ N(k') and f' | k';
  - X'/N(j) ≥ ΣF N(r)²/(H R N(j)) ≥ FΣ/H ≥ 1 (eq:child-column-lower-bound);
  - F'N(j) ≥ 1;
  - Σ'' = Σ' = L/R ≤ L;
  - H'/Σ' = H/(ΣFR) ≤ H/Σ;
  - H' ≤ HL/(ΣF).
- The characters ξ' come from expanding ξ₁(z)G(z⁻¹) on the **same** fixed ray class group, so the family does not grow along the recursion.
- **Derivative bookkeeping:** Lemma 7.3 gives C^{2m+4}, and Lemma 7.1 with j = 2m+4 gives C^{2j+4} = C^{4m+12}. Consistent.
- **Verdict:** the statement used by Prop. 5.1 matches what Sec. 7 claims to prove. The validity of Sec. 7 itself is outside our scope.

### S5.6 Proof of Proposition 5.1 (l.1516-1609): well-foundedness, termination, uniformity
**Induction claim P(j).** The statement of Prop. 5.1 holds with the extra restriction H ≤ D^{jκ}, with J = J(j, κ, C₀, ε) independent of I.

**Base case j = 0 (l.1532-1547).**
- H ≥ 1 and H ≤ 1 force H = 1; the rows are the 6 units.
- The columns number #{n : N n ∈ [uX, vX]} ≪_I X for X ≥ 1. The twists f number O(F).
- So E ≪_I HX‖W‖²_∞ ≤ Σ‖W‖²_∞, since H ≤ 1 ≤ F. Correct (J = 0 would suffice).

**Inductive step (l.1549-1604).** Re-derived line by line:
1. **Lemma 5.3 at ε/3.** Its hypotheses hold by S5.1.
2. **Nonempty supremum.** Then H² > X and H_c³ = X²/H². Each b has 1 < L_b ≤ X, so L_bF ≤ Σ and H ≤ Σ. Prop. 5.4 therefore applies at L = L_b with the same target Σ = XF, the same C₀, derivative order m = J(j, κ, C₀, ε/3) and ε/3.
3. **Children (l.1565-1577).**
   - H' ≤ HL_b/(ΣF) = H/(N(b)³F²) < H·H²/(X²F²) = H(H/Σ)² ≤ D^{-2κ}H ≤ D^{(j−1)κ} ≤ D^{jκ}.
   - H'/Σ' ≤ H/Σ ≤ D^{-κ}.
   - Σ' ≤ L_b ≤ X ≤ Σ ≤ D^{C₀}.
   - With H', X', F' ≥ 1, every child satisfies the hypotheses of Prop. 5.1 and the restriction of level j. **Correct.**
4. **Applying P(j) at ε/3 on I' = [u/16, 4v].** This gives E(child)/Σ' ≪ D^{ε/3}‖U‖²_{C^m(I')} ≤ D^{ε/3}.
   - The bound is uniform over the whole supremum: over all (H', X', F'), over ξ' in a finite set, and over U.
   - The constant depends on I' and hence only on I.
5. **Prop. 5.4 constant.** Its constant does not depend on L, H, F or Σ (l.1506-1508), so E(H,L_b,F) ≪ D^{2ε/3}Σ‖W‖²_{C^{4m+12}} uniformly in b.
6. **Lemma 5.3 again.** Substituting back into Lemma 5.3 gives D^ε Σ ‖W‖²_{C^J} with J = max(J_{5.3}(ε/3,C₀), 4m+12). This J depends only on (j, κ, C₀, ε).

**Termination (l.1606-1609).** j = ⌈C₀/κ⌉ covers every admissible H, because H ≤ Σ ≤ D^{C₀} ≤ D^{jκ}. The number of levels does not depend on D.

**Is there circularity?**
- **The cube index b = 1** lies in the supremum of Lemma 5.3 exactly when H_c < 1, that is, when X < H. Then E(H, L_1, F) = E(H,X,F) is the quantity being proved, and Lemma 5.3 alone is vacuous.
- The proof of Prop. 5.1 never feeds this term back into the induction hypothesis at the same H. It sends it through Prop. 5.4 at L = X. The children then satisfy H' ≤ H/F² < H(H/Σ)², which holds precisely because X < H.
- The R2 random test (§3) includes 6 979 such b = 1 samples, with all inequalities satisfied. **Not circular.**
- **Prop. 5.4 itself:** Lemmas 7.1-7.3 use only the supremum S_m at strictly smaller row ranges, never the estimate at the parent scale.

**Uniformity of ε and the constants.**
- Level j+1 at ε uses levels down to 0 at ε/3^{j+1}, which is finitely many.
- Writing K_j(I, ε) for the implied constant, K_{j+1}(I,ε) ≤ C_{5.3}(I,ε/3)·[1 + C_{5.4}(I, m_j, ε/3)(1 + K_j(I', ε/3))].
- K_j is finite for j ≤ ⌈C₀/κ⌉ and independent of D.
- All sums over children are taken as a **supremum** after the dyadic and character sums have been absorbed into D^{δ} inside Lemma 7.3. Logarithmic losses therefore do not compound with the branching. Even if they did, (log D)^{O(1/κ)} ≪ D^ε.

**Verdict:** the induction is well-founded, terminates, and is uniform.

### S5.7 Proof of Proposition 3.1 (Sec. 5.6, l.1613-1629)
- **Scales:**
  - From (eq:initial-scales): H_dual ≤ CD²/(HB²) = CD^{1−ϑ}/B², Σ = D/B, and H_dual/Σ = CD^{−ϑ}/B ≤ CD^{−ϑ}.
  - For D ≥ C^{2/ϑ} with C = C_{I,Φ} (l.1188), H_dual ≤ ΣD^{−ϑ/2}, so κ = ϑ/2 works.
  - Σ ≤ D ≤ D² justifies C₀ = 2; C₀ = 1 would also do.
- **The exclusion shifts (X,F) → (X/N d, F N d) of Lemma 4.4 inside Prop. 4.5.** They keep B, Σ and H_dual, so the gap is inherited.
- **Edge cases:**
  - X < 1: a nonempty column sum needs X ≥ 1/(2b₀), giving E ≪_I (H/X)‖W‖² ≪_I H‖W‖² ≪ Σ‖W‖².
  - H < 1: the sum is empty.
  - D < C^{2/ϑ}: bounded by trivial counting, with a constant depending on I and ϑ.
- **Quantifiers:**
  - The derivative order is J(ϑ/2, 2, ε), which depends only on (ϑ, ε), as (eq:auxiliary-target) requires. The constant may depend on C, i.e. on I, which is permitted.
  - E is monotone in its row bound, so (eq:auxiliary-target) for every 0 < H ≤ CD²/(HB²) follows.
- **ϑ ≤ 1/10 is never used.** Any ϑ ∈ (0,1) works here, and Sec. 3 only needs ϑ → 0 (S5-P2).
- **Verdict:** correct.

### S5.8 Consistency with the outline (l.425-658)
- The outline's cutoff H_c = min{X^{1/3}, (X/H)^{2/3}} equals (eq:cube-cutoff).
- At the basic scales H_c ≍ D^{2ϑ/3}.
- The schematic contraction H' < H(H/X)² ≪ D^{−2ϑ}H is the F = 1 case of l.1568-1572.
- No discrepancy.

## 3. Numerical and bookkeeping checks (our own code)

| ID | Script | What | Result |
|---|---|---|---|
| C1 | s5_cube_inversion_checks.py | (eq:cube-inverse): genuine a(n) at X=3000 (850 columns), and random n-coefficients at X=1.3·10⁵ (36 699 columns, 15 h incl. composite, 17 b incl. two prime squares); ξ ∈ {1, cubic mod 2}; k meeting S | max err 2.2·10⁻¹⁶ |
| C1-ctl | same | negative controls: N(h)^{-1/2}; α(h)³ on h-side only | errors 0.27 and 0.025 (correctly FAIL) |
| C2 | same | long-part regrouping via β₀(b,f), H_c ∈ {1,7,10,13,30}; \|β₀\| ≤ τ_div | max err 1.1·10⁻¹⁶; bound holds |
| C3 | same | Ψ_k(b)³ = ξ(b)³χ_b(k)³1_{(b,f)=1}, incl. prime powers | max err 3.7·10⁻¹⁵ |
| C4 | same | Prop. 5.2 reduction k=u₀sv² → (u₀s, fv²), incl. 2\|v, λ\|v; and at the level of T | 0 failures / diff 0 |
| C5 | same | γ₂(ab)=γ₂(a)γ₂(b)χ_a(b)²χ_b(a)² (used to build composite Gauss sums) vs direct; \|γ₂(p)\|=1 | max err 7.6·10⁻¹⁵ |
| R1 | s5_recursion_bookkeeping.py | exponent LP (scipy HiGHS) over all parents/b/children: max[H'−(h−2κ)], max[(H'−Σ')−(h−σ)], max[H'−(Σ'−κ)], max[Σ'−C₀], min X'', min F'', min H' for κ ∈ {0.005,0.05,0.25}, C₀ ∈ {1,2,4} | all signs as required (zero up to 10⁻¹⁶ rounding) |
| R2 | same | exact inequalities with constants (log-space random test, D up to 10⁶⁰): the chain l.1568-1575 and Lemma 7.3's child bounds | 14 355 admissible samples (6 979 with b=1), 0 failures |
| R3 | same | initialization: gap ≥ ϑ ≥ κ; levels ⌈4/ϑ⌉; actual depth ⌊(1−ϑ)/(2ϑ)⌋+1 | ϑ=1/10: 40 levels, depth ≤ 5 |
| R4 | same | derivative orders J_{j+1}=max(J*,4J_j+12) | J_j ≤ 4^j(J*+4); J_40 ≈ 6·10²⁴ for J*=10 |
| X | s5_energy_sanity.py | EXPLORATION: E(H,X,1)/X for X ≤ 4000, H ∈ {X/8, X/2}, coefficients conj(α)γ₂, γ₂, μ | E/X ≈ diagonal/X (0.013-0.08); nothing anomalous; not probative |

These checks confirm the arithmetic identities and the scale and exponent bookkeeping. They do not test Prop. 5.2 or Prop. 5.4.

## 4. Findings

| ID | Location | Class | Finding |
|---|---|---|---|
| S5-N1 | l.1516-1609 | no_issue_found | Prop. 5.1 induction: well-founded (children H' < D^{-2κ}H, gap inherited exactly), ⌈C₀/κ⌉ levels independent of D, ε split as ε/3 per level, constants depend only on (I,ν,S,j,κ,C₀,ε), J independent of I. |
| S5-N2 | l.1341-1466 | no_issue_found | Lemma 5.3: identity (eq:cube-inverse) and long-part regrouping verified numerically; short-part range uses H_c³ ≤ min(X, X²/H²) exactly as needed; L_b ≤ 1 terms counted correctly. |
| S5-N3 | l.1611-1629 | no_issue_found | Completion of Prop. 3.1: κ=ϑ/2, C₀=2 valid for D ≥ C^{2/ϑ}; X<1, H<1, small-D cases handled; derivative order depends on (ϑ,ε) only. |
| S5-N4 | l.1317-1332 / l.2189-2214; l.1487-1508 / l.2496-2683 | no_issue_found (interface) | Prop. 5.2 and Prop. 5.4 are used exactly as stated; the stated child constraints are what Lemma 7.3 produces; ξ' stays in the fixed group. Their proofs (Secs. 6-7) are not audited here. |
| S5-P1 | l.1345-1351, l.1406, l.1554-1572 | typo_or_presentation | When X < H, the cube index b=1 (N(b)=1 > H_c) lies in the supremum of Lemma 5.3, so that supremum contains E(H,X,F) itself and Lemma 5.3 is vacuous there. The proof of Prop. 5.1 handles it correctly through Prop. 5.4 at L=X (children H' ≤ H/F² < H(H/Σ)²). The paper does not mention this case. A sentence would help readers checking for circularity. |
| S5-P2 | l.1001, l.1615 | typo_or_presentation | ϑ ≤ 1/10 is never used in Secs. 4-5 (nor in Sec. 3); any 0<ϑ<1 works. Confirms architecture note P2. |
| S5-P3 | l.1321 vs l.1386-1399, l.2203 | typo_or_presentation | Prop. 5.2 sums over "0<N(k) ≪ H" while every use and the proof take N(k) ≤ H; harmless notational looseness. |
| S5-P4 | l.1549-1609 | typo_or_presentation | The derivative order grows as J_{j+1} = max(J*, 4J_j+12) over ⌈C₀/κ⌉ = ⌈4/ϑ⌉ levels, so k(ϑ,ε) in Prop. 3.1 is ≈ 4^{4/ϑ} (≈10²⁴ at ϑ = 1/10). This is harmless, because Theorem 1.1 uses Prop. 3.1 only for one fixed W at a time and is qualitative. Two remarks: the induction steps by κ although the contraction is 2κ; and in the application the recursion depth is ≤ ⌊(1−ϑ)/(2ϑ)⌋+1. |

There is no verified_error, suspected_gap, missing_hypothesis or unresolved_ambiguity inside Section 5.

## 5. What would invalidate Section 5's conclusion

The smallest statements whose failure would break Prop. 5.1, and hence Prop. 3.1 and Theorem 1.1, lie outside this section:

1. **Prop. 5.2 as stated.** In particular, uniformity of its constant in f and X and in all rows k ∈ O, including k meeting S. If it held only for squarefree k or with a loss N(f)^δ, the short part (eq:short-cube-bound) would lose a power of D.
2. **Prop. 5.4's scale constraints (eq:transfer-scales).** Specifically H' ≤ HL/(ΣF) together with H'/Σ' ≤ H/Σ, and its D^ε-only loss with a constant independent of L, H, F, Σ.
   - If the first constraint failed, the contraction H' < H(H/Σ)² would be lost and the induction would not terminate.
   - If the loss were D^{c} for some fixed c > 0 per level, the ⌈4/ϑ⌉ levels would accumulate D^{c·⌈4/ϑ⌉} and destroy the exponent.

Within Section 5 itself, the load-bearing inequality is N(b)³ > H_c³ = X²/H² ⇒ HL_b/(ΣF) < H(H/Σ)² (l.1568-1572). It was checked by hand, by LP and by random exact tests.

# Level-2 audit of Section 7: proof of the transfer proposition (two Poisson summations)

```text
Status: Level-2 audit of one section, done independently. It is not a review of the whole paper and
        does not certify the paper. RH and the Quasi-RH remain unreviewed claims of the source.
Scope: paper2.tex l.2217-2685 (Section 7: definitions (eq:P), (eq:first-transfer-forms); Lemma 7.1
       [lem:first-transfer]; the set-up of Sec. 7.2 (eq:common-mobius-sum), (eq:common-poisson-output);
       Lemma 7.2 [lem:arithmetic-poisson]; Lemma 7.3 [lem:second-transfer]; proof of Prop. 5.4).
       Interfaces read so the section could be checked end to end:
         - Prop. 5.4 and the smoothed energy A(W) (eq:smoothed-energy), l.1468-1512;
         - Lemma 4.1 (eq:recip), (eq:g), (eq:convert1), (eq:convert2), (eq:crt-a), (eq:quotient), l.823-857;
         - Lemma 4.2 (eq:poisson), l.875-932; Def. (eq:energy) and Lemma 4.4, l.938-992;
         - Lemmas B.1, B.2, l.3491-3615;
         - the use of Prop. 5.4 in the proof of Prop. 5.1, l.1549-1604.
Exact sources: github.com/openai/math @ 4eaee87548250b2682affda7d05d947c05554bae,
       preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf
       (sha256 f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18, re-hashed here: matches).
       The LaTeX source tex1112/paper2.tex (sha256 d9a8f15a...8750d4d, 3988 lines) is authoritative for formulas.
       The PDF text of Section 7 (sec_s7_transfer.txt) was compared with the tex and matches, except
       that pdftotext drops overlines (conjugation bars and the hat on Phi). Always read conjugations from the tex.
       Follow-ups checked for remarks on this section: Liu arXiv:2610.26835 (its Sec. 10.3 carries out an
       analogous two-Poisson transfer over general fields) and Ji arXiv:2611.16665 (a different route).
       Neither reports a problem with Sec. 7 of the 11/12 paper.
What was actually run (our own code, python3 -I; nothing from the OpenAI repository was run):
       experiments/code/quasi_rh/s7_transfer_identities.py   (sha256 f798d39e...0098) -> .out (sha256 1e250c47...ca4e)
       experiments/code/quasi_rh/s7_range_and_kernel_checks.py (sha256 f632af3a...6cfb) -> .out (sha256 2a4a99b8...0719)
       (both import only our own s4_zw.py, sha256 f8d5c204...730d). The Lean formalization of the 7/8
       companion was NOT replayed.
Smallest remaining gap: none inside Section 7. Section 7 is a complete proof of Prop. 5.4, given
       Lemmas 4.1, 4.2, 4.4, B.1, B.2 (audited in audit_S4.md, with numerical verification). The statements whose
       failure would break Sec. 7 are the two paired Gauss identities and the preimage regrouping. All three
       were verified numerically end to end (T1-T4 below).
```

## 0. Verdict

**Section 7 is correct as written.** It proves Proposition 5.4 (l.1487-1508) exactly in the form that Proposition 5.1 uses (l.1557-1592).

Classification of findings:
- **verified_error:** none.
- **suspected_gap:** none.
- **missing_hypothesis:** none.
- **unresolved_ambiguity:** none that is load-bearing.
- **typo_or_presentation:** six harmless items, P-S7-1 to P-S7-6 (§6).
- **no_issue_found_in_inspected_portion:** two observations, O-S7-1 (a caveat for numerical testing) and O-S7-2 (the "empty supremum" convention is consistent).

What we did:
- Every exact identity in Sec. 7 was re-derived by hand. The following were then **verified numerically end to end** with our own Z[ω] code, to relative error ≤ 1.4·10⁻¹⁴:
  - the expanded form of A(W) − Z in Lemma 7.1;
  - the second Poisson identity (eq:arithmetic-poisson-identity) of Lemma 7.2, in seven configurations, including Y < 1;
  - the full regrouping Q_{ξ₁}(U) = 𝒵 + [(r,f',k') form] of Lemma 7.3.
- Each test has its own negative controls with deliberately wrong conventions, and every control fails.
- Every inequality was re-derived by hand and checked on about 4.7·10⁵ exact-rational random and boundary samples:
  - the domination of the y-range;
  - the supports;
  - the child scales, including (eq:child-column-lower-bound);
  - the rescaled kernel supports.
- The smooth-weight (kernel) bounds rest on an Euler-operator identity, which we checked symbolically.

What the section does, in one paragraph:
- **First Poisson summation.** Poisson in the row variable k converts the Gauss-sum coefficients a_ξ into Möbius coefficients. This uses the paired identity (eq:paired-first-gauss).
- **Positivity enlargement.** The dual variable y = hf² is enlarged by positivity to a full lattice range N(y) ≤ Y_{C,d} ≍ ΣLF/H. This is larger than the natural range by the factor Σ/(LF) ≥ 1.
- **Second Poisson summation.** Poisson in y converts the Möbius coefficients back into Gauss-sum coefficients. The output is a child dual mean square with row range H' = HL/(ΣFR²), target Σ' = L/R and H'/Σ' ≤ H/Σ.
- **Where the size comes from.** No cancellation is proved in Sec. 7. Every step is one of the following:
  - an exact identity;
  - a positivity enlargement;
  - Cauchy-Schwarz (Lemma B.2, Lemma 4.4);
  - counting.

  The enlargement factor Σ/(LF) is chosen so that the second zero frequency 𝒵 has size exactly ≍ Σ (up to log). It is also what makes the child row range drop to HL/(ΣF).
- No stationary phase is used anywhere. The only analytic inputs are three:
  - exact lattice Poisson summation (Lemma 4.2);
  - the compact support of Φ̂ (it fixes all frequency ranges);
  - Mellin separation of smooth kernels (Lemma B.2).

## 1. Notation and logical skeleton

Notation:
- N = N_{K/Q}, O = Z[ω], λ = 1+2ω, and "primary" means ≡ 1 (mod 3).
- χ_n(x) = (x/n)₆ with zero extension. a_ξ(n) = conj(α(n)) γ₂(n) ξ(n) (l.807).
- I = [u,v], I_* = [u/2, 2v], I' = [u/16, 4v].
- Φ ≥ 0 is radial Schwartz with Φ ≥ 1 on [0,1] and supp Φ̂ ⊂ [0, C_Φ] (l.1470-1474).
- The hypotheses of Prop. 5.4 are 1 ≤ H, L, F, Σ ≤ D^{C₀} and max{H, LF} ≤ Σ.

```
Prop 5.4  <=  Lemma 7.1 (j = 2m+4, eps/4)  +  Lemma 7.3 (eps/4)                         (l.2672-2683)
Lemma 7.1:  A(W) - Z  =  [Poisson in k, Lemma 4.2] + (eq:paired-first-gauss) + Moebius in t
            |A(W) - Z| <= Lemma B.2 with rows (C,t,d,f,h), hypothesis supplied by Q_{xi1}(U) via y = h f^2
Lemma 7.2:  M = Z + [Poisson in y, Lemma 4.2] + paired identity (convert1,2, quotient, recip) + Moebius in w
Lemma 7.3:  Q_{xi1}(U) = calZ + sum over (r,f',k') [preimage regrouping]
            |block| <= Lemma B.2 with rows (r,f',k'), hypothesis supplied by Lemma 4.4 + S_m
```

## 2. Claim-by-claim verification

### S7.0 Preamble (l.2217-2228) and the object A(W) (l.1476-1483)
- **Restated:**
  - A(W) = (LF)⁻¹ Σ*_{F≤N f<2F} Σ_{k∈O} Φ(N k/H) |Σ*_n a_ξ(n) χ_n(k) χ_n(f)⁴ W(N n/L)|².
  - E(H,L,F;ξ,W) ≤ A(W), because Φ ≥ 0 and Φ ≥ 1 on [0,1]. The sum over k includes k = 0.
- **Checked:**
  - The preamble's claim that "the enlargement by Σ/(LF) ≥ 1 makes the second Poisson summation return with row range at most HL/(ΣF)" is consistent with the scales. The second dual length is ≍ ℓ²/Y_{C,d} ≍ L²H/(ΣLF) = HL/(ΣF).
  - Without the enlargement (Y ≍ L²F²/H) it would be H/F² ≥ HL/(ΣF). The enlargement therefore shortens the child rows.
- **Verdict:** correct.

### S7.1 Definitions (l.2231-2261)
- **Restated:**
  - Scales: ℓ = L/(N C N t), w_{C,d} = H N(C)/(N(d)L²F), and Y_{C,d} = c_I ΣLF N(d)/(H N(C)²), with c_I ≥ max(1, 4C_Φv²).
  - Coefficient: p_y(n) = μ(n)ξ₁(n)1_{(n,t)=1} conj(χ_n(y)) χ_n(C)⁴ χ_n(d).
  - Sums: P_{C,d,t}(y;U) = Σ*_n p_y(n) U(N n/ℓ), and Q_{ξ₁}(U) = Σ_{C,t} Σ_{d|C} w_{C,d} Σ_{y∈O} Φ(N y/Y_{C,d}) |P_{C,d,t}(y;U)|².
  - Ranges: C, t squarefree, (Ct,S) = 1, (C,t) = 1, N(C)N(t) ≤ 2vL.
- **Checked:**
  - "Retain only ℓ ≥ 1/(2v)" (l.2242) is the same condition as N(C)N(t) ≤ 2vL in (eq:first-transfer-forms) (P-S7-4).
  - Q_{ξ₁}(U) ≥ 0, since Φ ≥ 0.
  - The outer sums are finite. Each y-sum converges absolutely: |P| is bounded by the finite number of n with N(n) ≤ 2vℓ, and Φ is Schwartz.
  - Y_{C,d} < 1 is allowed, because Lemma 4.2 is exact at every scale H > 0 (l.2260-2261). This is exercised in T2 (Y = 0.42) and in T3 (min Y_{C,d} = 0.015).
- **Verdict:** well-posed.

### S7.2 Lemma 7.1 (l.2263-2349): the first Poisson summation

**Statement.** Fix j ≥ 0 and ε₀ > 0. Suppose Q_{ξ₁}(U) ≤ M‖U‖²_{C^j(I_*)} for all U ∈ C_c^∞(I_*) and all ξ₁. Then A(W) ≪ D^{ε₀}(Σ + M)‖W‖²_{C^{2j+4}(I)}.

Each step of the proof, re-derived by hand:

1. **Common factor (l.2274-2278).**
   - Put C = (n₁,n₂) and n_i = Cu_i. Squarefreeness gives (u₁,u₂) = (u₁u₂, C) = 1.
   - Then χ_{n₁}(k) conj(χ_{n₂}(k)) = 1_{(k,C)=1} χ_{u₁}(k) conj(χ_{u₂}(k)).
   - The character χ_{u₁} conj(χ_{u₂}) is a product of nontrivial sextic characters at distinct primes, including inert primes, where O/p = F_{ℓ²}. It is therefore primitive modulo u₁u₂.
   - By (eq:crt-a), a_ξ(Cu_i) = a_ξ(C)a_ξ(u_i)χ_{u_i}(C)⁴ with |a_ξ(C)| = 1. Also χ_{n₁}(f)⁴ conj(χ_{n₂}(f)⁴) = 1_{(C,f)=1} χ_{u₁}(f)⁴ conj(χ_{u₂}(f)⁴). **Correct.**
2. **Poisson summation (l.2279).** Lemma 4.2 is applied with r = C, m = u₁u₂ and scale H. It yields (H γ/√(N u₁ N u₂)) Σ_{d|C} μ(d) χ(d)/N(d) Σ_h conj(χ(h)) Φ̂(H N h/(N d N u₁ N u₂)). **Correct.** Lemma 4.2's normalization was audited in S4 §4.
3. **Zero frequency (l.2280-2285).**
   - Only the principal character contributes at h = 0, so u₁ = u₂ = 1 and n₁ = n₂ = C.
   - Exactly, Z = (H Φ̂(0)/(LF)) Σ_f Σ_{C,(C,f)=1} |W(N C/L)|² ∏_{p|C}(1 − 1/N p) ≥ 0.
   - Bound: #f ≪ F (F ≥ 1) and #{C : N C ≤ vL} ≪ vL (zero if vL < 1), so Z ≪_{I,Φ} H‖W‖²_∞. **Correct.** The display at l.2282-2284 is an upper bound (P-S7-5).
4. **Paired identity (eq:paired-first-gauss) (l.2286-2292).** We re-derived it as follows.
   - By CRT, γ(χ_{u₁} conj χ_{u₂}) = χ_{u₁}(u₂) conj(χ_{u₂}(u₁)) γ₁(u₁)γ₋₁(u₂). By (eq:recip) this equals R(u₁,u₂)γ₁(u₁)γ₋₁(u₂).
   - By (eq:convert1), a(u₁)γ₁(u₁) = μ(u₁)G(u₁).
   - By (eq:g) and (eq:convert1), conj(a(u₂))γ₋₁(u₂) = μ(u₂)χ_{u₂}(−1) conj(G(u₂)).
   - Then (eq:quotient), with (a,b) = (u₂,u₁), gives χ_{u₂}(−1) conj(G(u₂)) G(u₁) R = G(u₁u₂⁻¹).
   - Hence a_ξ(u₁) conj(a_ξ(u₂)) γ = μ(u₁)μ(u₂)(ξG)(u₁u₂⁻¹). **Correct.** The citation omits (eq:recip) and (eq:g) (P-S7-1).
   - The identity was also verified numerically, inside T1 with nontrivial ξ, and earlier with ξ = 1 (architecture_checks/check_paired.py).
5. **Möbius in t (l.2293-2299).** Expand (ξG)(z) = Σ_{ξ₁} ℓ_{ξ₁} ξ₁(z). Insert 1_{(u₁,u₂)=1} = Σ_{t|(u₁,u₂)} μ(t) and put u_i = tx_i.
   - The extension to non-coprime pairs is harmless. The summand, as a formula in (u₁,u₂), is weighted by Σ_{t|(u₁,u₂)} μ(t), which vanishes there. Liu (arXiv:2610.26835, Sec. 10.3) makes the same remark ("artificial diagonal pairs ... cancel in the complete Möbius sum").
   - Factors at t:
     - μ(u₁)μ(u₂) = μ(x₁)μ(x₂);
     - ξ₁(u₁) conj(ξ₁(u₂)) = ξ₁(x₁) conj(ξ₁(x₂));
     - χ_{u_i}(C)⁴ → χ_{x_i}(C)⁴, using (C,t) = 1;
     - χ_{u_i}(f)⁴ gives 1_{(t,f)=1};
     - χ(d) gives |χ_t(d)|² = 1;
     - conj(χ(h)) gives 1_{(h,t)=1}.

     What remains is μ(d)μ(t) (the first from Lemma 4.2, the second from the inversion), (f,Ct) = 1, (h,t) = 1 and (x_i,t) = 1 from squarefreeness. **Correct.**
6. **Normalization (l.2300-2321).**
   - Put z_i = N(x_i)/ℓ = N(Ctx_i)/L. Then N(u₁)N(u₂) = L²z₁z₂/N(C)², so the argument of Φ̂ is H N(h) N(C)²/(L² N(d) z₁z₂).
   - The prefactor is (LF)⁻¹ H N(d)⁻¹ (N u₁ N u₂)^{-1/2} = w_{C,d}(z₁z₂)^{-1/2}.
   - The coefficient: conj(χ_x(hf²)) = conj(χ_x(h)) conj(χ_x(f))², and conj(χ)² = χ⁴ (zeros included). This reproduces p_{hf²}(x).
   - **Checked symbolically (T5) and numerically (T1).**
7. **Ranges (l.2306, l.2310, l.2326-2328).**
   - n_i = Ctx_i with N(n_i)/L ≤ v gives N(C)N(t) ≤ vL ≤ 2vL.
   - supp Φ̂ ⊂ [0,C_Φ] and z_i ≤ v give N(h) ≤ C_Φ v² L² N(d)/(H N(C)²).
   - The zeros: χ_{x}(C)⁴ supplies (x,C) = 1; 1_{(x,t)=1} and conj(χ_x(hf²)) supply (x,t) = (x,f) = (x,h) = 1. **Correct.**
8. **Kernel bound (l.2316-2325).** Put K_h(z₁,z₂) = (z₁z₂)^{-1/2} W(z₁) conj(W(z₂)) Φ̂(A/(z₁z₂)), with A = H N(h) N(C)²/(L²N(d)) > 0.
   - On the support we have A/(z₁z₂) ≤ C_Φ, z_i ∈ [u,v].
   - The Euler identity (x₁∂₁)^a(x₂∂₂)^b Φ̂(A/(x₁x₂)) = (−1)^{a+b}[(t∂_t)^{a+b}Φ̂](A/(x₁x₂)) holds; we checked it symbolically (R3).
   - So every derivative is bounded by sup_{[0,C_Φ]}|(t∂_t)^kΦ̂| times powers of u⁻¹, **uniformly in A**. Hence sup_{C,d,h}‖K_h‖_{C^{j₀}(I²)} ≪_{I,Φ,j₀} ‖W‖²_{C^{j₀}(I)}. **Correct.**
   - Smoothness of t ↦ Φ̂(t) down to t = 0: Φ̂(t) = g(√t) with g even and smooth, and t∂_t = (r/2)∂_r (P-S7-6).
9. **Positivity domination (l.2330-2339).**
   - For fixed (C,d,t), the pairs (f,h) with hf² = y number at most #{f : (f)² | (y)} ≤ τ(y) ≪ N(y)^δ. Here N(y) ≤ Y_{C,d} ≤ c_I D^{3C₀}.
   - The nonzero image satisfies N(y) < 4F²·C_Φv²L²N(d)/(HN(C)²) ≤ Y_{C,d}. This is equivalent to 4C_Φv² LF ≤ c_I Σ, which holds because c_I ≥ 4C_Φv² and LF ≤ Σ (T5 symbolic; R1, 20 000 exact samples).
   - Since Φ ≥ 1 on [0,1] and Φ ≥ 0, Σ_{rows} w_{C,d} |P(hf²;U)|² ≤ max τ(y) · Q_{ξ₁}(U) ≤ D^δ M‖U‖². **Correct.**
10. **Lemma B.2 (l.2340-2348).**
    - Set-up: rows r = (C,t,d,f,h), finitely many because N(h) is bounded; weights w_r = w_{C,d}; c_r = ℓ_{ξ₁}μ(d)μ(t)w_{C,d}, so |c_r| ≤ |ℓ_{ξ₁}|w_r.
    - Both families are S_{1,r} = S_{2,r} = P_{C,d,t}(hf²; ·), at the row-dependent points x = N(n)/ℓ, which B.2 allows.
    - Kernels: K_h, supported in I² with I = [u,v] ⊂ int I_* = (u/2, 2v).
    - B.2 (with m = j) gives |A(W) − Z| ≪ D^δ M sup‖K_h‖_{C^{2j+4}} ≪ D^δ M‖W‖²_{C^{2j+4}(I)}.
    - With Z ≪ H‖W‖²_∞ ≤ Σ‖W‖²_∞, the lemma follows. **Correct.**
    - The proof of Lemma B.2 was re-read: Mellin representation, uniform coefficient bound, Cauchy-Schwarz in r, and q = 2m+4 making ∫∫(1+|s|)^m(1+|t|)^m(1+|s|+|t|)^{-q} finite.
    - The hypothesis of B.2 must hold for complex test functions U_t = V x^{it}. Q is defined, and Lemma 7.3 proves its bound, for complex U (P-S7-6).

**Numerically verified (T1).** A(W) was computed directly as a lattice sum over k ∈ O, including k = 0. It equals Z + [displayed (C,t,d,f,h,x₁,x₂) expression] with relative error 2.1·10⁻¹⁶. Set-up:
- ξ: a nontrivial ray class character of conductor 5;
- 28 squarefree columns with N ≤ 100;
- four twists f of norm 7 and 13;
- H = 30, L = 50, and W random complex.

The negative controls give errors relative to |A − Z|:

| Control | Error relative to \|A − Z\| |
|---|---|
| μ(t) dropped | 79 |
| N(d) dropped from w_{C,d} | 17 |
| G(x₂/x₁) in place of G(x₁/x₂) | 2.1 |

**Verdict:** Lemma 7.1 is correct.

### S7.3 Sec. 7.2 set-up and Lemma 7.2 (l.2351-2494): the second Poisson summation

**Statement.** Take arbitrary ℓ, Y > 0 and U ∈ C_c^∞([a,b]). Then
𝓜 = Σ_y Φ(N y/Y)|P(y)|² = Z + Σ_{g,e,w,h,ξ'} (Yμ(e)μ(w)c_{ξ'}N(g))/(N(e)ℓ) Σ*_{n₁,n₂} a♯(n₁) conj(a♯(n₂)) 𝒦(N n₁/X', N n₂/X'),
where:
- X' = ℓ/N(gw);
- a♯(n) = a_{ξ'}(n) 1_{(n,tg/e)=1} χ_n(deh) χ_n(Cew)⁴;
- 𝒦(x₁,x₂) = U₀(x₁) conj(U₀(x₂)) Φ̂(Y N(h)N(g)²/(N(e)ℓ²x₁x₂));
- |Z| ≪ Yℓ‖U‖²_∞.

Each step of the proof, re-derived by hand:

1. **Common factor (l.2421-2426).**
   - Put g = (n₁,n₂) and n_i = gz_i. The factor χ_n(C)⁴ forces (n,C) = 1, and 1_{(n,t)=1} gives (n,t) = 1. So (g,Ct) = (z₁z₂, gCt) = 1, and (z₁,z₂) = 1.
   - Then conj(χ_{n₁}(y)) χ_{n₂}(y) = 1_{(y,g)=1} conj(χ_{z₁}(y)) χ_{z₂}(y).
   - Also μ(n₁)μ(n₂) = μ(z₁)μ(z₂), ξ₁(n₁) conj(ξ₁(n₂)) = ξ₁(z₁) conj(ξ₁(z₂)) since |ξ₁(g)| = 1, and the C⁴ and d factors reduce to z_i. **Correct.**
2. **Poisson summation.** Lemma 4.2 with χ = conj(χ_{z₁}) χ_{z₂}, exclusion g, divisor e | g and scale Y.
   - Zero frequency: z₁ = z₂ = 1 and h = 0. This gives Z = YΦ̂(0) Σ*_{(g,Ct)=1} |U(N g/ℓ)|² ∏(1 − 1/N p).
   - #{g : N g ≤ bℓ} ≪ bℓ, and there are none if bℓ < 1. So |Z| ≪_{I_*,Φ} Yℓ‖U‖²_∞. **Correct** (R4 tabulates the counting constant).
3. **Paired identity (l.2430-2435).** Re-derived as follows.
   - By CRT and (eq:recip), γ(conj χ_{z₁} χ_{z₂}) = R(z₁,z₂) γ₋₁(z₁) γ₁(z₂).
   - By (eq:convert2), μ(z₁)γ₋₁(z₁) = χ_{z₁}(−1) conj(G(z₁)) a(z₁).
   - By (eq:convert1), μ(z₂)γ₁(z₂) = G(z₂) conj(a(z₂)).
   - Then (eq:quotient), with (a,b) = (z₁,z₂), gives G(z₂z₁⁻¹).
   - Times ξ₁(z₁z₂⁻¹), this is ξ₁(z)G(z⁻¹) at z = z₁z₂⁻¹, that is, Σ_{ξ'}c_{ξ'}ξ'(z₁z₂⁻¹). **Correct.** The cited range "(eq:convert2)-(eq:quotient)" also needs (eq:convert1) and (eq:recip) (P-S7-1).
4. **Character bookkeeping (l.2437-2445).**
   - χ_z(dh) conj(χ_z(e)) χ_z(C)⁴ = χ_z(deh)χ_z(Ce)⁴, because conj(χ_z(e)) = χ_z(e)⁵ for (z,e) = 1, which holds since e | g.
   - U(N(gz₁)/ℓ) conj(U(N(gz₂)/ℓ))/√(N z₁ N z₂) = (N g/ℓ) U₀ conj(U₀).
   - **Correct.** The intermediate display l.2448-2459 matches our derivation term by term.
5. **Möbius in w (l.2461-2475).** Put z_i = wn_i with (w, gCt) = 1.
   - By (eq:crt-a), a(wn) = a(w)a(n)χ_n(w)⁴.
   - |a(w)χ_w(deh)χ_w(Ce)⁴|² = 1_{(w,h)=1}, since (w,dCe) = 1 is automatic.
   - χ_n(Cew)⁴ supplies (n,C) = (n,e) = (n,w) = 1, so the residual exclusion is (n, t·g/e) = 1.
   - The argument of Φ̂ becomes Y N(h)/(N(e)N(w)²N(n₁)N(n₂)), which matches 𝒦 at x_i = N(n_i)/X'.
   - No condition (n₁,n₂) = 1 remains. **Correct.**
6. **Ranges (l.2378-2385, l.2489-2493).**
   - N(gw) ≤ bℓ, and N(z₁z₂) ≤ b²ℓ²/N(g)², give N(h) ≤ C_Φb²ℓ²N(e)/(YN(g)²).
   - "tg/e and Cew are coprime and squarefree": every pairwise coprimality follows from (C,t) = 1, (g,Ct) = 1, e | g and (w, gCt) = 1.
   - The sum is finite. **Correct.**

**Numerically verified (T2).** 𝓜 was computed directly as a lattice sum over y ∈ O, including y = 0. It agrees with Z + RHS in seven configurations, all with ξ₁ nontrivial, with relative error ≤ 1.4·10⁻¹⁴:

| N(C) | N(d) | N(t) | ℓ | Y |
|---|---|---|---|---|
| 1 | 1 | 1 | 30 | 12 |
| 7 | 7 | 1 | 30 | 7.5 |
| 7 | 1 | 13 | 22 | 3.3 |
| 91 | 13 | 7 | 9 | 0.42 |
| 19 | 1 | 49 | 4 | 25 |
| 13 | 1 | 1 | 45 | 9 |
| 19 | 19 | 1 | 50 | 9 |

The rows cover a composite C, a composite t, and Y < 1.

The negative controls give errors relative to |𝓜 − Z|:

| Control | Error relative to \|𝓜 − Z\| |
|---|---|
| Restriction (h,w) = 1 dropped | 0.93 |
| χ_n(e)⁴ in place of χ_n(e)⁵ | 3.3·10⁻⁴ |

The genuine identity holds at about 10⁻¹⁴ on this scale. For why the e-exponent control is vacuous in one configuration, see O-S7-1.

**Verdict:** Lemma 7.2 is correct.

### S7.4 Lemma 7.3 (l.2496-2670): regrouping and the second transfer bound

**Statement.** For U ∈ C_c^∞(I_*), Q_{ξ₁}(U) ≪ D^{ε₀}Σ(1+S_m)‖U‖²_{C^{2m+4}(I_*)}. Here S_m is the supremum in (eq:transfer-summary), with tests in C_c^∞(I') and ‖·‖_{C^m(I')} ≤ 1.

Each step, re-derived by hand:

1. **Application of Lemma 7.2 (l.2509-2521).** Lemma 7.2 is applied with ℓ = L/(N C N t) and Y = Y_{C,d}, at the same (C,d,t,ξ₁), with b = 2v. Set r = tg/e, f' = Cew, k' = deh. Then a♯(n) = a_{ξ'}(n)1_{(n,r)=1}χ_n(k')χ_n(f')⁴, which is exactly the coefficient of E_{(r)}. **Correct.**
2. **Scale identities (l.2526-2532).** All three were checked symbolically in sympy (T5), substituting N(r) = N(t)N(g)/N(e), N(f') = N(C)N(e)N(w) and N(k') = N(d)N(e)N(h):
   - X'₀ = ℓ/(N g N w) = L/(N r N f');
   - w_{C,d} Y_{C,d} N(g)/(N(e)ℓ) = c_IΣN(r)/L²;
   - Y_{C,d}N(h)N(g)²/(N(e)ℓ²) = c_IΣF N(k')N(r)²/(HL).
3. **Support (l.2541-2548).**
   - U₀ is supported in [u/2, 2v] and N(n) ≥ 1, which gives N(r)N(f') ≤ 2vL.
   - supp Φ̂ and x_i ≤ 2v give N(k') ≤ (4C_Φv²/c_I)·HL/(ΣFN(r)²) ≤ HL/(ΣFN(r)²), using c_I ≥ 4C_Φv². **Correct.**
4. **Preimages and regrouping (l.2550-2583).**
   - **Our derivation.** Fix (r,f',k'). The constraints (C,t) = 1, d | C, e | g, (g,Ct) = 1, (w,gCth) = 1 and h = k'/(de) ∈ O∖{0} are equivalent to the following: t | r; f' = C⊔e⊔w; e | k'; (w,k') = 1; d | (C,k'); and g = e·(r/t).
     - For de | k' ⇔ d | k' and e | k': d | C and e are coprime.
     - For (w,h) = 1 ⇔ (w,k') = 1: (w,de) = 1 is automatic.
   - **Same summand on every preimage.**
     - The coefficient a♯ depends only on (r,f',k').
     - X'₀ depends only on N(r)N(f').
     - The Fourier parameter depends only on (r,k').
     - The weight c_IΣN(r)/L² depends only on r.
     - So the summand is constant on the preimages, apart from μ(e)μ(w).
   - **Support restrictions.** The restrictions N(C)N(t) ≤ 2vL (since N(C)N(t) ≤ N(r)N(f')), N(gw) ≤ bℓ, and the h-range in Lemma 7.2 discard only zero kernels. **Correct.**
   - **Per-prime count (l.2560-2568).** At p | f', the three choices contribute:
     - p | C: weight +1 each for p ∤ d and, if p | k', for p | d, giving 1 + 1_{p|k'};
     - p | e: −1_{p|k'};
     - p | w: −1_{p∤k'}.

     The sum is 1_{p|k'}. With the τ(r) choices of t, the total is τ(r)1_{f'|k'}. **Correct.** T4 checks this exhaustively on 206 208 abstract configurations.
   - No sign-dependent cancellation is discarded: the regrouping is done "before taking absolute values" (l.2570), as required.
5. **Dyadic blocks and child scales (l.2585-2621).** Put X' = L/(RF'), Σ' = L/R and H' = HL/(ΣFR²).
   - For a retained r, f' | k' gives F' ≤ N(f') ≤ N(k') ≤ HL/(ΣFN(r)²) ≤ H'. Hence H' ≥ F' ≥ 1.
   - (eq:child-column-lower-bound): for j | r, X'/N(j) ≥ ΣFN(r)²/(HRN(j)) ≥ ΣF/H ≥ 1, using N(j) ≤ N(r), N(r) ≥ R, F ≥ 1 and H ≤ Σ. Also F'N(j) ≥ 1.
   - 1 ≤ X'/X'₀ = N(r)N(f')/(RF') < 4.
   - H'/Σ' = H/(ΣFR) ≤ H/Σ, Σ' ≤ L, H' ≤ HL/(ΣF), and Σ' = X'F' ≥ 1.
   - Rescaled support: x ∈ [u/(2ρ), 2v/ρ] ⊂ [u/8, 2v] ⊂ int I' for ρ = X'/X'₀ ∈ [1,4).
   - All of this was checked on 41 709 admissible exact-rational samples, 0 failures (R2). One trial in ten was a boundary trial, with H = Σ, N(k') = N(f') and N(j) = N(r).
6. **Kernel bound (l.2603-2614).**
   - 𝒦_{r,f',k'}(x₁,x₂) = U₀(ρx₁) conj(U₀(ρx₂)) Φ̂(B/(ρ²x₁x₂)), with ρ ∈ [1,4) and B ≥ 0.
   - By the same Euler identity, sup‖𝒦‖_{C^{2m+4}([u/8,2v]²)} ≪_{I_*,m,Φ} ‖U₀‖²_{C^{2m+4}(I_*)} ≪ ‖U‖²_{C^{2m+4}(I_*)}, uniformly in (ρ, B). **Correct.**
7. **Exclusion removal (l.2623-2640).**
   - For a retained r and V ∈ C_c^∞(I'), enlarge by positivity to all f' in the dyadic block and all 0 < N(k') ≤ H'. This gives Σ'·E_{(r)}(H',X',F';ξ',V).
   - Lemma 4.4 bounds this by Σ'·τ(r) Σ_{j|r} E(H', X'/N(j), F'N(j); ξ', V).
   - Each triple lies in the supremum family, by step 5 and Σ'' = Σ'. So each E is ≤ Σ'S_m‖V‖²_{C^m(I')}, by homogeneity of E in V.
   - The total is ≤ τ(r)²(Σ')²S_m‖V‖² ≪ D^δ(Σ')²S_m‖V‖², since N(r) ≤ 2vL ≤ 2vD^{C₀}. **Correct.**
8. **Lemma B.2 per block (l.2642-2651).**
   - Set-up: rows (r,f',k'); weights w = N(r)τ(r); |c| ≤ |c_{ξ'}|(c_IΣ/L²)·w; common points N(n)/X'; I_*(B.2) = I' and I(B.2) = [u/8,2v].
   - Hypothesis: Σ_r N(r)τ(r)·D^δ(Σ')²S_m‖V‖² ≤ 2R·#{r}·D^{2δ}(Σ')²S_m‖V‖², and #{r} = O(R).
   - Hence |block| ≪ (c_IΣ/L²)·R²D^{2δ}(L/R)²S_m‖U‖²_{C^{2m+4}} = c_I D^{2δ} Σ S_m ‖U‖². The identity (ΣR/L²)R(L/R)² = Σ was checked in T5. **Correct.**
9. **Total zero frequency (l.2653-2665).**
   - w_{C,d}Y_{C,d}ℓ = c_IΣ/(N(C)²N(t)), checked in T5.
   - Σ_{d|C} gives τ(C). Σ_C τ(C)/N(C)² ≤ ζ_K(2)², and Σ_{N t≤2vL} 1/N(t) ≪ log(2vL).
   - So |𝒵| ≪ D^δΣ‖U‖²_∞. Only Y_{C,d} > 0 is used. **Correct.**
10. **Assembly (l.2666-2669).** There are O((log 2D)²) dyadic pairs (R, F'), with R, F' ≤ 2vL. The character set is fixed and finite. With δ = ε₀/4 the stated bound follows, with constants depending only on I_*, m, C₀, ε₀ and the fixed data. **Correct.**

**Numerically verified (T3).** Q_{ξ₁}(U) was computed directly over 73 pairs (C,t) and all d | C, with y-lattice sums. It equals 𝒵 + [(r,f',k') form with weight (c_IΣ/L²)N(r)τ(r), k' = f'm, m ∈ O∖{0}] with relative error 8.5·10⁻¹⁶. Set-up:
- L = 60, v = 1, c_I = 1, Σ = 150, F = 2, H = 100;
- ξ₁ nontrivial;
- min Y_{C,d} = 0.015.

The negative controls give errors relative to |Q − 𝒵|:

| Control | Error relative to \|Q − 𝒵\| |
|---|---|
| τ(r) replaced by 1 | 1.05·10⁻³ |
| Restriction f' \| k' dropped | 1.55 |

**Verdict:** Lemma 7.3 is correct.

### S7.5 Proof of Proposition 5.4 (l.2672-2683)
- Lemma 7.3 with ε₀ = ε/4 gives M := C·D^{ε/4}Σ(1+S_m) for the derivative order j = 2m+4, uniformly in ξ₁.
- Lemma 7.1 with ε₀ = ε/4 gives A(W) ≪ D^{ε/4}(Σ + D^{ε/4}Σ(1+S_m))‖W‖²_{C^{2(2m+4)+4}} ≪ D^{ε/2}Σ(1+S_m)‖W‖²_{C^{4m+12}(I)}.
- Every implied constant depends only on m, C₀, ε, I, ν, S and the ray class group, and **not** on H, L, F or Σ. This is what Prop. 5.1 needs uniformly in the cube index b (l.1587-1592).
- S_m < ∞ always: each child has E ≪ H'X'‖U‖²_∞ with H' ≤ HL/(ΣF) and X' ≤ Σ' ≤ L.
- **Verdict:** correct. This matches the S5 audit's interface check (audit_S5.md §S5.5).

## 3. Size of each term

| Term | Where | Exact or bound | Size |
|---|---|---|---|
| Z (first zero frequency) | l.2280-2285 | exact, ≥ 0 | ≪_I H‖W‖²_∞ ≤ Σ‖W‖²_∞ |
| A(W) − Z | l.2300-2346 | identity, then B.2 | ≪ D^{ε₀/2} M ‖W‖²_{C^{2j+4}} |
| multiplicity of y = hf² | l.2330 | divisor bound | ≤ τ(y) ≪ D^{δ} |
| natural y-range vs Y_{C,d} | l.2333 | ratio | 4C_Φv²LF/(c_IΣ) ≤ 1 |
| Z in Lemma 7.2 | l.2416 | counting | ≪ Yℓ‖U‖²_∞ |
| 𝒵 (second zero frequency) | l.2653-2662 | Σ_{C,t,d} w Y ℓ | ≪ Σ log(2vL)‖U‖²_∞ |
| outer weight after regrouping | l.2528-2529 | exact | c_IΣN(r)/L² ≤ 2c_IΣR/L² |
| child mean square per r | l.2629-2633 | Lemma 4.4 + S_m | ≤ τ(r)²(Σ')²S_m‖V‖² |
| dyadic block (R, F') | l.2645-2651 | B.2 | ≪ D^{2δ}(ΣR/L²)·R·(L/R)²S_m = D^{2δ}ΣS_m |
| number of blocks | l.2666 | dyadic | O((log 2D)²) |
| child scales | l.2587-2621 | exact | H' = HL/(ΣFR²), Σ' = L/R, H'/Σ' = H/(ΣFR) |

The only genuine size inputs are the two zero frequencies, which give the "1" in (1+S_m), and the recursive quantity S_m. Everything else is exact or a constant-loss Cauchy-Schwarz step.

## 4. Imported results used by Section 7

Section 7 imports **no external theorem directly**. Its inputs are internal:
- **Lemma 4.2** (lattice Poisson with exclusions). It rests on [IK04 Thm 4.5, (3.12)]. The normalization was re-derived and verified numerically in audit_S4.md §4. Here it is used three times, all of the identical shape: in k (Lemma 7.1), in y (Lemma 7.2), and implicitly in the principal case (Z, 𝒵). It is exact for every scale > 0, which covers Y_{C,d} < 1.
- **Lemma 4.1** ((eq:recip), (eq:g), (eq:convert1), (eq:convert2), (eq:crt-a), (eq:quotient)). Verified numerically in architecture_checks/check_lemma41.py, check_recip.py and check_paired.py, and here inside T1-T3 with G read off brute-force Gauss sums.
- **Lemma 4.4** (exclusion removal). The identity was verified numerically in s4_prop45_end_to_end.py. Here it needs F' ≥ 1, which holds.
- **Lemmas B.1 and B.2** (Mellin separation). The proofs were re-read (§S7.2 step 10). The hypotheses I ⊂ int I_* hold in both uses: [u,v] ⊂ (u/2, 2v) and [u/8, 2v] ⊂ (u/16, 4v).

The follow-up papers do not bear on the correctness of Sec. 7:
- Liu (arXiv:2610.26835 Sec. 10.3) performs a structurally parallel two-Poisson transfer, with y = hf²E, χ_u(C)⁴χ_u(d_k), the complete Möbius extension and enlargement before inverse row Poisson, in a more general setting. This is mild corroboration of the architecture, not an independent check of the constants.
- Ji (arXiv:2611.16665) uses a different method.

## 5. Numerical checks (our own code only)

`experiments/code/quasi_rh/s7_transfer_identities.py`: 20 tests, 0 failures, 57 s.

Set-up:
- Φ(t) = e^{−πt} and Φ̂(t) = (2/√3)e^{−4πt/3}; the closed form was verified by quadrature in s4_poisson_checks.py.
- All frequency sums are complete (truncated at Φ̂ < 10⁻¹⁶). The paper's compact-support ranges are therefore **not** exercised numerically; they are checked by hand and in R1/R2.
- S = {2,3,5}. ξ and ξ₁ are nontrivial characters of conductor 5. G is the class function on primary classes mod 4.

Results:
- **T1, Lemma 7.1:** A(W) = Z + displayed sum; relative error 2.1·10⁻¹⁶. Three negative controls fail at 2-79 (relative to |A − Z|).
- **T2, Lemma 7.2:** seven configurations, relative error ≤ 1.4·10⁻¹⁴. Two negative controls fail.
- **T3, Lemma 7.3:** Q = 𝒵 + (r,f',k') form; relative error 8.5·10⁻¹⁶. Two negative controls fail.
- **T4:** the per-prime preimage count Σ μ(e)μ(w) = τ(r)1_{f'|k'}; 206 208 abstract cases, 0 failures.
- **T5:** ten symbolic identities (sympy), covering the normalizations of Lemma 7.1, the scale identities of Lemma 7.3, the child scales, the closing identity and the y-range ratio.

`experiments/code/quasi_rh/s7_range_and_kernel_checks.py`: 498 816 checks, 0 failures.
- **R1:** domination of the y-range; 20 000 exact-rational samples.
- **R2:** supports, H' ≥ F' ≥ 1, (eq:child-column-lower-bound), F'N(j) ≥ 1, 1 ≤ ρ < 4, the child scale constraints and the rescaled support in int I'. 41 709 admissible samples; one trial in ten was a boundary trial.
- **R3:** the Euler-operator identity behind the uniform kernel bounds; symbolic, a+b ≤ 6.
- **R4:** counting constants. #{g : N g ≤ x}/x ≤ 1.0 for x ≤ 3000, and Σ_{N t≤x}1/N t ≈ 0.33 log 2x.

What these checks do **not** authenticate:
- They do not test Prop. 5.2 or Sec. 6.
- They do not test the induction of Prop. 5.1 beyond the interface.
- They do not test whether S_m is actually ≪ D^ε (that is the induction hypothesis).
- They do not test Lemma B.2 numerically.
- They are finite toy instances of exact identities, not a replay of any primitive computation of the source.

## 6. Findings

| ID | Location | Classification | Severity | Finding |
|---|---|---|---|---|
| N-S7-1 | l.2263-2349 | no_issue_found_in_inspected_portion | n/a | Lemma 7.1: expansion, Lemma 4.2 application, zero frequency, (eq:paired-first-gauss), Möbius in t, normalization w_{C,d}(z₁z₂)^{-1/2}, frequency range, kernel bounds, positivity domination N(hf²) ≤ Y_{C,d}, and the Lemma B.2 application were all re-derived. Verified end to end (T1, 2.1·10⁻¹⁶) and on 20 000 range samples (R1). |
| N-S7-2 | l.2351-2494 | no_issue_found_in_inspected_portion | n/a | Lemma 7.2: the second Poisson identity, including Z, the paired identity, χ_z(dh)conj(χ_z(e))χ_z(C)⁴ = χ_z(deh)χ_z(Ce)⁴, the w-insertion via (eq:crt-a), the residual exclusion (n, tg/e) = 1, and the ranges. Verified in seven configurations (T2, ≤ 1.4·10⁻¹⁴), including Y < 1. |
| N-S7-3 | l.2496-2670 | no_issue_found_in_inspected_portion | n/a | Lemma 7.3: the three scale identities, the supports, the preimage characterization, the regrouping Σμ(e)μ(w) = τ(r)1_{f'\|k'}, the child scales and (eq:child-column-lower-bound), the rescaled kernels, Lemma 4.4, the per-block bound (ΣR/L²)R(L/R)² = Σ, 𝒵, and the dyadic assembly. Verified (T3 8.5·10⁻¹⁶, T4, T5, R2). |
| N-S7-4 | l.2672-2683 | no_issue_found_in_inspected_portion | n/a | Prop. 5.4: ε-allocation ε/4 + ε/4, derivative order 2(2m+4)+4 = 4m+12, and constants independent of H, L, F, Σ, as Prop. 5.1 requires. |
| O-S7-1 | numerical tests | no_issue_found_in_inspected_portion | n/a | Testing caveat, not a defect. With a radial row weight, any pair (n₁,n₂) whose character χ_{n₁}conj(χ_{n₂}) is nontrivial on the units contributes exactly 0 to both sides of every Poisson identity (substitute h → ζ₆h); compare O-S4-1. Numerical tests are informative only on unit-trivial pairs. Example: χ_{p}(ζ₆) = ζ₆^{(Np−1)/6}, so the pairs (p₁₃, p₁₃'), (p₃₇, 1) and (p₁₉, p₇p₁₃) are unit-trivial. T2 case 7 was added so that such a pair meets a nontrivial e. The e-exponent negative control is vacuous in case 6 for this reason, and fails as it should in case 7. |
| O-S7-2 | l.1505, l.2505, l.2590 | no_issue_found_in_inspected_portion | n/a | "An empty supremum is zero" is consistent: any dyadic block with a retained r produces child triples (H', X'/N(j), F'N(j)) that satisfy all the constraints of the supremum family, so a nonzero block never meets an empty supremum. |
| P-S7-1 | l.2286-2287, l.2430-2431 | typo_or_presentation | cosmetic | Citations are incomplete. (eq:paired-first-gauss) is attributed to "CRT, (eq:convert1), (eq:quotient)", but the derivation also uses (eq:recip), to turn χ_{u₁}(u₂)conj(χ_{u₂}(u₁)) into R(u₁,u₂), and (eq:g) or conj(γ₁) = χ(−1)γ₋₁ for the γ₋₁(u₂) factor. Likewise, Lemma 7.2's "(eq:convert2)-(eq:quotient)" also uses (eq:convert1) and (eq:recip). Both identities hold, re-derived and verified numerically. |
| P-S7-2 | Sec. 7 passim | typo_or_presentation | cosmetic | Several symbols are overloaded: u (interval endpoint and the cofactors u₁, u₂); w (weight w_{C,d}, Möbius variable w, and the B.2 weights); ℓ (scale and coefficient ℓ_{ξ₁}); j (derivative order and divisor j \| r); b (endpoint of I_* = [a,b]); M (bound) next to 𝓜 (mean square). The meaning is always clear from context. |
| P-S7-3 | l.2241 | typo_or_presentation | cosmetic | c_I ≥ 1 is never used. Only c_I ≥ 4C_Φv² is used, at l.2333 and l.2548. |
| P-S7-4 | l.2242 vs l.2256 | typo_or_presentation | cosmetic | "Retain only ℓ ≥ 1/(2v)" repeats the range N(C)N(t) ≤ 2vL already in (eq:first-transfer-forms). |
| P-S7-5 | l.2282-2284 | typo_or_presentation | cosmetic | The displayed \|Z\| bound omits Φ̂(0)∏(1−1/Np) and the restriction (C,f) = 1. As written it is a valid upper bound. |
| P-S7-6 | l.2316-2325, l.2603-2614, l.3590 | typo_or_presentation | cosmetic | Two facts are used but not stated. (i) The uniform kernel bounds need t ↦ Φ̂(t) to be smooth on [0, C_Φ] with (t∂_t)^kΦ̂ bounded. This holds because Φ̂(t) = g(√t) with g smooth and even (t∂_t = (r/2)∂_r); see R3. (ii) Lemma B.2 needs the mean-square hypothesis for complex tests V(x)x^{it}. Q and S_m are defined, and bounded in Sec. 7, for complex test functions, and Sec. 4 already conjugates W, so the consistent reading is "all test functions complex-valued". |

## 7. What was not checked
- **Lemma 4.2's IK04 numbering.** We did not check it; see U-S4-1. The mathematics was re-derived.
- **The induction closing S_m ≪ D^ε.** That is Prop. 5.1 (audit_S5.md), and it depends on Prop. 5.2 and Sec. 6, which are outside this audit.
- **Lean.** The Lean formalization of the companion 7/8 theorem was not replayed. Whether it covers an analogue of this transfer was not examined.

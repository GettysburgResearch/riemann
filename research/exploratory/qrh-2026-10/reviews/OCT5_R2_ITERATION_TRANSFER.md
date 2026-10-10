# R2 review: the transfer recursion in the October 5 quasi-RH manuscript

```text
Status: REVIEW (bounded; external manuscript)
Scope: paper2.tex lines 1254-1629 (Section sec:descent: Prop prop:canonical 1261-1277,
  completed sums 1282-1309, statement of Prop prop:R 1317-1333 [black box], Lemma
  lem:cube-reduction 1341-1467, Prop prop:transfer 1469-1509, proof of prop:canonical
  1514-1609, Section sec:completion 1611-1629) and lines 2217-2683 (Section
  sec:transfer-proof: first Poisson 2230-2349, second Poisson 2351-2494, Lemma
  lem:second-transfer 2496-2670, proof of prop:transfer 2672-2683). For the 11/12
  bookkeeping we also read lines 679-722 (Prop thm:ms and the prime extraction). For
  comparison we read the outline, Step 5, at lines 426-658. Interfaces were read and
  checked only as used: Lemma lem:arithmetic statement 823-857 (not re-proved);
  lem:poisson 875-932; lem:remove-exclusions 962-993; prop:poisson-reduction
  1000-1252; App. app:weights 3481-3650 (lem:smooth-mean-square checked).
Exact sources or dependencies: pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6
  (`git rev-parse pr908`). paper2.tex is
  standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
  The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex at that ref, sha256
  d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d (3988 lines); the
  scratchpad copy was re-extracted and the hashes are identical. Prior work: branch
  origin/claude/openai-math-riemann-analysis-w5copg @ bd670c92d15f835021c6579ed273b213d71caff7,
  standalone/2026-10-07-openai-quasi-rh/README.md sections 2-3 and 8 (sha256 38bbf639...bf2e);
  pr910 = 670a76c1a3a8f325c43c1755b1cfc24d313a3e3c,
  standalone/2026-10-10-quasi-riemann-height-descent/FOURTH_MOMENT_REDUCTION.md section 1.1
  (sha256 8dc1b137...5e7f).
What was actually run: a line-by-line hand check of every displayed identity and inequality
  in scope (Sections 3-6 below). Script reviews/oct5_r2_iteration_check.py
  (sha256 e4017ed5c78c5d067c379e90122105b465e7015764099e19d877e50bb9da4bdd), written from
  scratch for this review, ran 53 checks: 53 pass, and the `python3 -O` output is identical.
  These cover: (A) exact sympy/Fraction replay of the 11/12 bookkeeping; (B) 17 monomial
  identities of the two Poisson steps; (C) an exact Farkas identity for the descent
  contraction and gap preservation, plus an exact-rational grid exploration of the
  recursion (22,960 start states); (D) an exhaustive check of the preimage sign sum
  (127 patterns); (E) an EMPIRICAL floating-point replay of both paired Gauss-sum identities
  on 161 coprime pairs of norm <= 43 per factor, built from the definitions (max error 2.1e-14);
  (F) the derivative-order, epsilon and interval recursions.
Smallest remaining gap: line 1389-1400, the application of Prop prop:R (statement at lines
  1317-1333) inside Lemma lem:cube-reduction. This review treats it as a black box by
  assignment. The next imported input is Lemma lem:arithmetic (lines 823-857), used at lines
  2287-2291 and 2430-2435. Its consequences were derived algebraically and replayed only
  empirically, for small norms. Within lines 1254-1629 and 2217-2683, no step was found to
  be wrong.
```

RH is unsolved. The manuscript claims a fixed zero-free half-plane, Re s > 11/12, for all Dirichlet L-functions. It is external and unreviewed, and nothing here bears on the critical line. This review checks only the part of the argument labelled R2. That part takes the completed mean square (Prop prop:R) and several arithmetic and smoothing lemmas as inputs, and derives the dual mean-square bound (Prop prop:canonical), hence Prop thm:ms and the exponent 11/12. A PASS here means that this deduction is correct. It does not mean that the theorem is proved.

## 1. Verdict in one paragraph

The transfer recursion is a correct deduction from its stated inputs. Every algebraic identity in the two Poisson applications was re-derived. These include the weights, the Fourier arguments, the regrouping of seven auxiliary indices into the new triple (r, f', k'), and the sign sum that forces f' | k'. Every scale inequality in the induction was also re-derived, and no error was found. The "enlarged row range" step is legitimate. It works by positivity, its cost is exactly absorbed by the target Σ, and it produces the advertised shorter dual range. The outline's "fixed ratio" becomes an inequality H'/Σ' ≤ H/Σ in the full proof, and that inequality is sufficient. Termination is genuine: the row parameter contracts by D^(-2κ) per level, so ⌈C0/κ⌉ = ⌈4/ϑ⌉ levels suffice. The ε losses, derivative orders and support intervals compound only over that bounded number of levels. One regime (row range H > column scale X) is handled correctly, but the text and the outline do not mention it (finding F1). The W-dependence of the final bound has derivative order at least 5·4^⌈4/ϑ⌉ − 4. This is harmless for the qualitative theorem, because W is fixed for each putative zero. It confirms PR 910's remark that the completed calculation proves no height-uniform closure.

**R2 verdict: PASS conditional on Prop prop:R, Lemma lem:arithmetic and Lemma lem:smooth-mean-square (the last was checked here). This is not a verdict on Theorem 1.1.**

## 2. Verdict table

| # | Step (paper2.tex lines) | What was checked | Result |
|---|---|---|---|
| 1 | Cube inversion, eq:cube-inverse (1361-1373) | Substituted eq:T. Since V_*(y) = √y W(y), the coefficient of the total cube index B is N(B)^(1/2) X^(-1/2) ᾱ(B)^3 Ψ_k(B)^3 Σ_{h\|B} μ(h). Complete multiplicativity of Ψ_k (sextic symbol in the denominator, ray character, zero extension at S) and of α on primary elements was checked | PASS |
| 2 | Short cube part (1376-1406) | Weighted Cauchy–Schwarz. Prop R is applied at X/N(h)^3 ≥ 1 with range C0+1. Σ_{N(h)≤H_c} N(h)^2 ≪ H_c^3, and H^2 F H_c^3/X ≤ Σ is exact at H_c^3 = X^2/H^2 (script C) | PASS, given Prop R |
| 3 | Long cube part (1408-1462) | Expansion b = hc. Normalization √N(hc)/√X = N(b)^(-1) L_b^(-1/2). Ψ_k(b)^3 = ξ(b)^3 χ_b(k)^3 1_{(b,f)=1}, \|β_0\| ≤ τ(b). Weighted Cauchy–Schwarz yields a sup. The divisor sum is ≤ log^2. The L_b ≤ 1 terms are bounded by counting, ≤ vH ≤ vΣ | PASS |
| 4 | Regime H > X, i.e. H_c < 1 (not discussed in text) | Here b = 1 lies in the supremum, β_0(b,f) = 1_{b=1}, and lem:cube-reduction is circular on its own. The proof of prop:canonical still closes, because line 1570-1571 holds for b = 1 with contraction F^(-2) (H > X and H ≤ Σ D^(-κ) force F > D^κ) | PASS. Expository gap F1 |
| 5 | Prop prop:transfer statement vs. proof (1487-1509, 2672-2683) | Order m → 2m+4 (second Poisson) → 4m+12 (first). Intervals I_* = [u/2,2v] and I' = [u/16,4v]. Scale conditions eq:transfer-scales match the outputs at 2615-2621 | PASS |
| 6 | First Poisson, lem:first-transfer (2235-2349) | gcd extraction. lem:poisson with exclusion C. The paired identity eq:paired-first-gauss was re-derived from CRT, eq:convert1, eq:convert2, eq:recip and eq:quotient, and replayed on 161 pairs (script E). Möbius in t. Weight w_{C,d} and kernel 𝒦_h (script B). Frequency range. Zero frequency ≪ H ≤ Σ. y = hf^2 has multiplicity ≤ τ(y). Y_{C,d} ≥ natural range iff c_I ≥ 4C_Φv^2 and LF ≤ Σ. lem:smooth-mean-square applies with row-dependent scale ℓ | PASS |
| 7 | Second Poisson identity, lem:arithmetic-poisson (2353-2494) | gcd g and exclusion e \| g. Second paired identity, re-derived and replayed (script E). χ_z(dh) χ̄_z(e) χ_z(C)^4 = χ_z(deh) χ_z(Ce)^4. U_0 normalization N(g)/ℓ. Möbius w with eq:crt-a. Coprimality bookkeeping 1_{(n,tg/e)=1}. Frequency range. Zero-frequency bound Yℓ. Coprimality and squarefreeness of tg/e and Cew | PASS |
| 8 | lem:second-transfer (2507-2670) | Three monomial identities at 2527-2531 (script B). Preimage parametrization and sign sum Σμ(e)μ(w) = τ(r) 1_{f'\|k'} (script D, exhaustive up to 6 primes). The kernel depends only on (r, f', k'). H' ≥ 1. eq:child-column-lower-bound. Rescaled support [u/8,2v]^2 ⊂ int I'^2. Exclusion removal keeps every child in the supremum. Block total (ΣR/L^2)·R·Σ'^2 = Σ. Zero frequency ≪ Σ log L | PASS |
| 9 | Proof of prop:canonical (1516-1609) | Induction on H ≤ D^(jκ), with base case H = 1. Hypotheses of lem:cube-reduction and prop:transfer verified at each use. Contraction h − 2κ − h' = s1 + s2 + 2 s3 (exact Farkas identity, script C). Gap preservation H'/Σ' ≤ H/Σ ≤ D^(-κ). Σ' ≤ L_b ≤ Σ ≤ D^C0. ε split into three thirds. J_{j+1} = max(4J_j+12, J_cube). Interval enlarged once per level. j = ⌈C0/κ⌉ | PASS |
| 10 | sec:completion (1611-1629) | κ = ϑ/2 and C0 = 2 are admissible once D ≥ C_{I,Φ}^(2/ϑ). The cases X < 1 (counting, using X ≥ 1/b_0 and H ≪ Σ), H < 1 (empty sum) and bounded D are covered | PASS |
| 11 | Prime extraction to 11/12 (693-722) | Exact: D^(2+ϑ)/Y + D^2/Y^2 with Y = D^((1+ϑ)/6) gives exponents 11/6 + 5ϑ/6 and 5/3 − ϑ/3. The first dominates by 1/6 + 7ϑ/6. A_1 ≪ D^(11/12+5ϑ/12+ε), and Y = H^(1/6) is optimal (script A) | PASS |
| 12 | Outline Step 5 vs. full proof (426-658) | Y = XL_b/H, H' = HL_b/X, E ≲ X + (X/L_b)E', and the X/L_b conversion were all checked (script B). The full proof generalizes the sketch with f, C, d, t, g, e, w | PASS. Expository note F2 |
| 13 | Prop prop:R (1317-1333) | Not verified (black box by assignment). Interface: it is used only at 1389-1400, with the hypotheses checked in row 2. Consistency note in Section 6.4 | NOT VERIFIED |
| 14 | Lemma lem:arithmetic (823-857) | Not re-proved. All consequences used in scope were derived from its displayed identities. Both paired identities, and eq:recip for G, were replayed empirically from the definitions | IMPORTED. Empirical replay PASS |
| 15 | lem:smooth-mean-square (3566-3615) | Mellin separation with a uniform coefficient bound. Cauchy–Schwarz in r. Integrability of (1+\|s\|)^m (1+\|t\|)^m (1+\|s\|+\|t\|)^(-2m-4) on R^2. The row-dependent scales x_{j,r,n} are allowed. Both applications have kernel support strictly inside the test interval | PASS |

## 3. The descent section, line by line

**Completed sums (1282-1309).** The b = 1 part of eq:T is X^(-1/2) Σ* ᾱ(n) γ_2(n) Ψ(n) W(N(n)/X), because V_*(N(n)/X)/√N(n) = X^(-1/2) W(N(n)/X). The twist Ψ_k(n) = ξ(n) χ_n(k) χ_n(f)^4 is completely multiplicative in the primary generator n. This follows from the multiplicative extension of the sextic symbol in its denominator and from closure of primary elements under products. The zero extension at S is consistent. The identification with the column sum of eq:energy is exact.

**Lemma lem:cube-reduction (1341-1467).** Write B = hb for the total cube index. Then Σ_h μ(h) ᾱ(h)^3 Ψ(h)^3 N(h)^(-1) T(X/N(h)^3) has B-coefficient ᾱ(B)^3 Ψ(B)^3 N(B)^(1/2) X^(-1/2) Σ_{h|B} μ(h). This is eq:cube-inverse; all sums are finite by the support of W.

* Short part. |μ ᾱ^3 Ψ^3| ≤ 1. After Prop R, the f-average over O(F) squarefree f gives (H + 2H^2 F N(h)^3/X). Then Σ_{N(h)≤H_c} N(h)^(-1)·N(h)^3 ≪ H_c^3, so E_short ≪ D^(ε/2)(H + H^2 F H_c^3/X) ≤ D^(ε/2)·2Σ. Here H ≤ Σ is a hypothesis, and H_c^3 ≤ X^2/H^2.
* Long part. With b = hc, the prefactor is μ(h) √N(b) X^(-1/2) = μ(h) N(b)^(-1) L_b^(-1/2). Then Ψ_k(b)^3 = ξ(b)^3 χ_b(k)^3 χ_b(f)^12, and χ_b(f)^12 = 1_{(b,f)=1}. Cauchy–Schwarz with weights τ(b)/N(b) gives (Σ τ/N)^2 · sup_b E(H, L_b, F). The bound Σ_{N(b)≤R} τ(b)/N(b) ≤ (Σ 1/N(c))^2 ≪ log^2 R holds. For 1/v ≤ L_b ≤ 1 there are O_I(1) columns, so E ≪ H/L_b ≤ vH ≤ vΣ.
* Emptiness. If H^2 ≤ X, then H_c = X^(1/3), and N(b) > H_c forces L_b < 1.

**Prop prop:transfer (1469-1509).** E ≤ 𝒜(W) because Φ ≥ 1 on [0,1] and Φ ≥ 0; the k = 0 term is a nonnegative addition. In the statement, Σ is an independent target and only max{H, LF} ≤ Σ is assumed. In the proof, H ≤ Σ is used for both zero-frequency terms and for eq:child-column-lower-bound. LF ≤ Σ is used for the enlargement.

**Proof of prop:canonical (1516-1609).**

* Base case (1532-1547). H ≥ 1 and H ≤ 1 force H = 1. There are O(F) choices of f, O(1) of k, and O_I(X) columns of modulus ≤ 1, so E ≪ HX‖W‖^2 ≤ Σ‖W‖^2.
* Step (1549-1604). If the supremum is nonempty, then H^2 > X and H_c^3 = X^2/H^2 (line 1554). Prop transfer applies at L = L_b ∈ (1, X]. Its hypotheses 1 ≤ H, L, F, Σ ≤ D^C0 and max(H, L_bF) ≤ Σ hold, since L_b F ≤ XF.
  * Lines 1566-1572: H' ≤ H L_b/(ΣF) = H/(N(b)^3 F^2) < H (H/Σ)^2 ≤ D^(-2κ) H ≤ D^((j-1)κ). In log coordinates this is the exact identity h − 2κ − h' = s1 + s2 + 2 s3. Here s1 is the transfer row bound, s2 = 3β − 2x + 2h > 0 is N(b) > H_c, and s3 = x + f − h − κ ≥ 0 is the canonical gap (script C).
  * The identity holds for b = 1 as well (finding F1).
  * Gap preservation: (σ' − κ) − h' = s4 + s3, where s4 encodes H'/Σ' ≤ H/Σ.
  * Σ' ≤ L_b ≤ Σ, since log_D Σ − log_D L_b = f + 3β ≥ 0.
  * All hypotheses of the level-j statement hold for every child, and the children carry ‖U‖_{C^m(I')} ≤ 1 with I' depending only on I.
* ε and J (1588-1602). The three losses ε/3 (cube reduction), ε/3 (transfer) and ε/3 (induction hypothesis) multiply to D^ε. J(j+1, ε) = max(4·J(j, ε/3) + 12, J_cube(ε/3)). Both are finite at each of the finitely many levels.
* Conclusion (1606-1608). H ≤ Σ ≤ D^C0 ≤ D^(jκ) for j = ⌈C0/κ⌉, uniformly in D ≥ 2.

**Section sec:completion (1611-1629).** By eq:initial-scales, H/Σ = C D^(-ϑ)/B ≤ D^(-ϑ/2) once D^(ϑ/2) ≥ C_{I,Φ}. Then Prop canonical with κ = ϑ/2 and C0 = 2 gives eq:auxiliary-target. The derivative order is J(κ, 2, ε), which is independent of I as Prop poisson-reduction requires. The cases X < 1, H < 1 and bounded D are covered as stated. The shifted scales (X/N(d), F·N(d)) produced inside Prop poisson-reduction keep XF = D/B and H, so they fall under the same case analysis.

## 4. The transfer proof, line by line

**First Poisson (2230-2349).** Put n_i = C u_i. Then χ_{n_1}(k) χ̄_{n_2}(k) = 1_{(k,C)=1} χ_{u_1} χ̄_{u_2}(k), and χ_{u_1} χ̄_{u_2} is primitive modulo u_1 u_2. The exponent-6 symbols at the primes of u_1 u_2 are nontrivial, because N(p) ≡ 1 (mod 6) for every prime p prime to 6. Also |a_ξ(C)|^2 = 1 and a_ξ(C u) = a_ξ(C) a_ξ(u) χ_u(C)^4.

* The lattice-Poisson formula of lem:poisson, including the factor 2/√3 and the self-duality of O under e(zw) (Gram matrix [[0,1],[1,-1]]), was re-derived. It gives the factor H γ(χ)/√N(u_1u_2) · μ(d) χ(d)/N(d).
* The Gauss sum of a product character factors under CRT as γ(χ_1 χ_2) = χ_1(m_2) χ_2(m_1) γ(χ_1) γ(χ_2). Combined with eq:convert1, eq:convert2 and eq:recip, this gives a_ξ(u_1) ā_ξ(u_2) γ = μ(u_1) μ(u_2) ξ(u_1) ξ̄(u_2) G(u_1) Ḡ(u_2) χ_{u_2}(−1) R(u_1,u_2). That equals eq:paired-first-gauss by eq:quotient. The pre-quotient form was replayed numerically (Section 7).
* After the Möbius sum in t, the u-dependent factor is μ(x) ξ_1(x) χ_x(C)^4 χ_x(d) χ̄_x(hf^2), using χ^4 = χ̄^2. This is p_{hf^2}(x). The weight is H/(LF N(d) N(t) √N(x_1x_2)) = w_{C,d} (z_1z_2)^(-1/2), and the Fourier argument is H N(h) N(C)^2/(L^2 N(d) z_1 z_2) (script B).
* Zero frequency: u_1 = u_2 = 1, giving ≪ (H/LF)·F·L = H.
* Enlargement: N(hf^2) ≤ 4C_Φ v^2 L^2 F^2 N(d)/(H N(C)^2) = Y_{C,d} · (4C_Φ v^2/c_I) · (LF/Σ) ≤ Y_{C,d}. Each y arises from ≤ τ(y) pairs (f, h), and τ(y) ≪ D^ε since Y_{C,d} ≤ D^O(1).
* lem:smooth-mean-square applies with rows (C, t, d, f, h), coefficients |ℓ_{ξ_1}| w_{C,d}, kernels supported in I^2 ⊂ int I_*^2, and the row-dependent scale ℓ.

**Second Poisson identity (2407-2494).** Put n_i = g z_i. The conditions (z_1, z_2) = (z_1z_2, gCt) = (g, Ct) = 1 hold. The second paired identity μ(z_1) μ(z_2) ξ_1(z_1) ξ̄_1(z_2) γ(χ̄_{z_1} χ_{z_2}) = Σ c_{ξ'} a_{ξ'}(z_1) ā_{ξ'}(z_2) follows from CRT, eq:convert1, eq:convert2, eq:recip and eq:quotient applied to G(z_2 z_1^(-1)). We re-derived it.

* Character bookkeeping: χ̄_z(e) = χ_z(e)^5 gives χ_z(dh) χ̄_z(e) χ_z(C)^4 = χ_z(deh) χ_z(Ce)^4.
* Normalization: U(N(gz_1)/ℓ) Ū(N(gz_2)/ℓ)/√N(z_1z_2) = (N(g)/ℓ) U_0 Ū_0.
* After the Möbius sum in w: |a_{ξ'}(w) χ_w(deh) χ_w(Ce)^4|^2 = 1_{(w,h)=1}, using (w, gCt) = 1. The exclusion becomes 1_{(n,tg/e)=1}.
* tg/e and Cew are coprime and squarefree under the stated conditions. The frequency range and the zero frequency Z ≪ Yℓ (ℓ ≥ 1/(2v)) are as stated.

**Lemma lem:second-transfer (2496-2670).**

* The three identities at 2527-2531 hold exactly (script B). The factors N(d) and N(C)^2 built into Y_{C,d} are exactly what make the new Fourier parameter depend only on (r, k').
* Preimages. For fixed (r, f', k'), the preimages are: t | r (τ(r) choices, all admissible), an ordered disjoint factorization f' = C e w, and d | (C, k'), subject to e | k' and (w, k') = 1. Then g = e r/t and h = k'/(de). All conditions (g, Ct) = (w, gCth) = 1 follow.
* Each prime of f' contributes 1 + 1_{p|k'} − 1_{p|k'} − 1_{p∤k'} = 1_{p|k'}. This was checked exhaustively for all patterns with up to 6 primes (script D).
* The range restrictions (N(gw) ≤ bℓ, the h-range, N(C)N(t) ≤ 2vL, ℓ ≥ 1/(2v)) are implied by nonvanishing of the common kernel. So regrouping before taking absolute values is legitimate.
* Dyadic blocks. The bound F' ≤ N(f') ≤ N(k') ≤ HL/(ΣF N(r)^2) gives H' ≥ 1. The ratio X'/N(j) ≥ ΣF N(r)^2/(H R N(j)) ≥ FΣ/H ≥ 1. The ratio X'/X'_0 lies in [1, 4), so the kernels are supported in [u/8, 2v]^2.
* Positivity enlargement to all f' ∈ [F', 2F') and 0 < N(k') ≤ H', followed by lem:remove-exclusions, produces children (H', X'/N(j), F'N(j)) with Σ' = L/R. Each child satisfies eq:transfer-scales: H'/Σ' = H/(ΣFR) ≤ H/Σ, Σ' ≤ L and H' ≤ HL/(ΣF).
* Block total: (ΣR/L^2)·R·(L/R)^2 = Σ. Zero frequency: w_{C,d} Y_{C,d} ℓ = c_I Σ/(N(C)^2 N(t)), summing to ≪ Σ log L.
* Proof of prop:transfer: j = 2m+4 in lem:first-transfer gives order 4m+12, with the two losses D^(ε/4) and D^(ε/4).

## 5. Answers to the referee checklist item (transfer recursion)

1. **Enlarged row range (Y = XL_b/H).** This step is legitimate. In the full proof, Y_{C,d} = c_I Σ L F N(d)/(H N(C)^2). It exceeds the natural range of y = hf^2 by the factor (c_I/4C_Φv^2)·Σ/(LF) ≥ 1 (line 2333; script B). Enlarging a sum of |P(y)|^2 with Φ ≥ 1 on [0,1] can only increase it.
   * The cost shows up only in the diagonal. The zero-frequency mass w Y ℓ = c_I Σ/(N(C)^2 N(t)) equals the target Σ up to a convergent sum, instead of LF. This is Heath-Brown's device (HB95 Lemma 9; GL Lemma 4.4).
   * The gain is that the second Poisson has dual range ≈ ℓ^2/Y ≈ HL/(ΣF), which is shorter than H.
2. **H'/X' fixed while both scales contract.** In the outline (F = 1, no common factors), H'/X' = H/X holds exactly (script B). In the full proof only H'/Σ' = H/(ΣFR) ≤ H/Σ holds. Σ' = L/R ≤ L_b, and H' ≤ H/(N(b)^3 F^2 R^2). The induction uses only three things: the ratio inequality, Σ' ≤ D^C0, and the contraction H' < H (H/Σ)^2 ≤ D^(-2κ) H. Contraction of Σ is never used.
3. **Suppressed common factors and dyadic ranges.** The first Poisson introduces C (gcd), d | C (row exclusion) and t (Möbius coprimality), and folds f into y = hf^2. The second introduces g (gcd), e | g and w, plus the new frequency h. These seven indices regroup into r = tg/e (a new exclusion, removed by lem:remove-exclusions), f' = Cew (the new auxiliary twist variable, which is why the family carries χ_n(f)^4) and k' = deh (the new row). The new coefficient a_{ξ'}(n) 1_{(n,r)=1} χ_n(k') χ_n(f')^4 has exactly the form of eq:energy, so the family is closed. All normalizations cancel exactly (Section 4). The dyadic loss is O(log^2 D) blocks times the fixed character set.
4. **Termination and uniformity.**
   * Number of levels: ⌈C0/κ⌉ = ⌈4/ϑ⌉ (40 at ϑ = 1/10, 4000 at ϑ = 1/1000). This is bounded because ϑ is fixed before D → ∞. The grid exploration at κ = 1/20 found maximum depth 13 ≤ ⌈C0/(2κ)⌉ = 20 ≤ 40.
   * Every reduction is a supremum over children, never a sum over the branching tree. Per level the loss is a constant times D^ε, with the ε split geometrically: depth i sees ε/3^i.
   * The derivative order satisfies J_j ≥ 5·4^j − 4, so at ϑ = 1/10 it is at least 5·4^40 − 4 ≈ 6.0·10^24. The support interval grows to [u/16^j, 4^j v].
   * Constants depend on (I, ν, S, ϑ, ε) through this finite chain. Everything is finite for fixed (ϑ, ε, I), so Prop thm:ms holds as stated with a finite k(ϑ, ε).

## 6. Findings

* **F1 (expository; no mathematical error).** Prop canonical assumes only H ≤ Σ D^(-κ), so H > X occurs whenever F > D^κ. From Prop poisson-reduction, this happens when F ≫ D^ϑ B. Then H_c < 1, the short part is empty, and β_0(b,f) = 1_{b=1}. So eq:cube-reduction is an inequality E ≤ (log)^4 E, and the supremum contains E(H, X, F) itself. The proof of prop:canonical still closes. Line 1570-1571 holds for b = 1, because 1 > H_c^3, and Prop transfer applies at L = X. The contraction then comes from F^(-2), with F^2 > D^(2κ), instead of N(b)^(-3). Neither the text nor the outline mentions this; the outline assumes H ≤ X (line 478). One sentence after line 1556 would remove the apparent circularity.
* **F2 (expository).** Outline lines 604-613 ("ratio stays fixed", "both scales decrease") describe the F = 1 sketch. The proof needs and uses only H'/Σ' ≤ H/Σ and the contraction of H.
* **F3 (uniformity remark; consistent with PR 910 §1.1).** The final W-dependence is ‖W‖_{C^k}^2 with k ≥ 5·4^⌈4/ϑ⌉ − 4. Theorem 1.1 only needs a fixed W(y) = y^(-ϱ) φ(y) for each putative zero ϱ, so this is harmless there. It does mean that the recursion as written gives no useful height-uniform bound: ‖W‖_{C^k} ≍ |Im ϱ|^k. This is exactly PR 910's caution that the two-Poisson canonical descent produces additional transformed profiles, and that no height-uniform closure of the whole family follows from the completed calculation alone. In paper2 those profiles are the Mellin-separated tests U with ‖U‖_{C^m(I')} ≤ 1, the new characters ξ' and the exclusion shifts. The induction absorbs them qualitatively, because its constant depends only on the support interval and a C^J norm.
* **F4 (cosmetic).** Line 1572 gives D^((j-1)κ), stronger than the D^(jκ) needed, so the induction could step by 2κ. Similarly, eq:transfer-scales discards the factor R^(-2) available in H' (line 2588).

### 6.4 Note on the black box Prop R (for the reflection reviewer)

The bound in eq:R has no "+X" term. At H ≪ (X/N(f))^(1/2) it asserts Σ_k |T(X;k,f)|^2 ≪ D^ε H. So the ᾱ-twisted completed cubic theta sums have size about X^ε on average, with no Patterson-type X^(5/6) main term. This is plausible: on the theta side, the angular Grössencharacter ᾱ removes the contribution of the constant term. It is, however, exactly the content that the theta reflection must deliver (the w5copg checklist, item 2). R2 uses Prop R only at line 1390 and only in the stated form. The cutoff H_c^3 = min(X, X^2/H^2) is calibrated to it, and a weaker Prop R (for example one with an extra X^(2/3) term) would change H_c and the contraction rate.

## 7. Script: what it checks and what it does not

`reviews/oct5_r2_iteration_check.py` prints a report and writes nothing. To run it: `python3 -I oct5_r2_iteration_check.py` from any directory. It takes about 10 s and needs sympy 1.14.

* **A** (14 checks, exact): the 11/12 bookkeeping, the outline form, optimality of Y, sixth-power row norms, the Poisson-reduction scales and block bound, and κ = ϑ/2.
* **B** (17 checks, exact sympy monomials): every weight, argument and scale identity of both Poisson steps, plus outline consistency.
* **C** (8 checks): an exact Farkas identity for the contraction, the gap and Σ' ≤ Σ, the short-cube identity, and the j_max table. The exact-rational grid exploration has κ = 1/20, C0 = 2, step 1/20 and 22,960 start states. It enumerates every admissible cube index β, every R and every split of Σ' into X'F'. The grid is an illustration only; the Farkas identity is the proof for all real states.
* **D** (2 checks, exhaustive): the preimage sign sum and the τ(r) factor.
* **E** (6 checks, EMPIRICAL, floating point, tolerance 1e-9): an independent implementation of sextic symbols over Z[ω]. It uses the residue fields F_p and F_{q^2}, Gauss sums over HNF residue systems, and e(x/m) = exp(2πi·d/N(m)) with x·m̄ = c + dω. On 22 primary primes (norms 7 to 121) it checks γ_2^3 = −α, ᾱγ_2γ_1 = −G, R = ±1, both paired identities in their pre-quotient form on 161 coprime pairs (including composite factors), and G(ab) = G(a)G(b)R(a,b). The maximum error is 2.1e-14. This checks conventions and the CRT step; it is not a proof of Lemma lem:arithmetic or of eq:quotient on the ray class group.
* **F** (6 checks): J_j = 5·4^j − 4, its value at j = 40, the ε and interval chains, the per-level ε split, and 2(2m+4) + 4 = 4m+12.

## 8. Misreadings to avoid

* This is not a verification of Theorem 1.1. R2 is a deduction from Prop prop:R, and Prop prop:R carries the automorphic content.
* "Ratio fixed" is an outline simplification. The proof uses an inequality.
* The finite grid exploration and the small-norm Gauss-sum replay are not proofs. The exact Farkas identity and the algebraic re-derivations are what support the PASS.
* No height uniformity is claimed or available from this recursion (F3).
* RH remains unsolved. 11/12 is a fixed half-plane, and even if accepted it gives no critical-line information.

# Q. A selected prime in the additive variable: s = p s' in the compensated probe

Status: exploratory, 35-minute attack. Verdict: **the construction fails on the Poisson side for a structural reason** (the principal signal is proportional to the same prime mean that controls the Gram-exceptional coherence), so θ cannot be lowered this way; the predicted boundary is unchanged at 0.874957. Details, the exact local computation, and the no-go identity are below.

Sources: paper (qrh_main.txt) Sec 4.2 (652-915: Lemma 4.2-4.4, CRT formula γ_j(ab) = χ_a(b)^jχ_b(a)^jγ_j(a)γ_j(b), (4.8)), Sec 6.1 (2684-2830: (6.1), (6.2), A_{m,σ,v}), Sec 7.1-7.2 (2990-3365: (7.1)-(7.13), Lemma 7.1 table (7.16), (7.17)), Lemma 10.5 (4747-4857: (10.17), (10.18)), Prop 2.1 (381-460), Sec 12 (5150-5233: (12.5)), Lemma 13.3 (5330-5479: (13.7)-(13.8)), Prop 15.2 (6293-6456), Prop 15.3 (6457-6525), Sec 16 (6526-6922: (16.1)-(16.4), (16.8), (16.12)-(16.13)). Notes J (§3, §6.1) and A (§3). Model: `scripts/prime_in_additive.py` (built on `scripts/exponent_model.py`).

Convention. The text extraction loses overlines. In (16.8) the identity "η(p)Q^x D = v^{-1}" with D = η(p)v^{-1}Q^{-x} requires the mark weight to be the conjugate of η(p) (otherwise one gets η(p)^2). I therefore write the mark weight as ψ(p), with ψ = η̄ in the paper's A-marks and ψ free below; nothing depends on this convention except the labels. At u = 1 (the only row that matters for the verdict) ρ = 1 and no orientation ambiguity exists.

## 1. The modified probe and its direct representation

### 1.1 Definition
Add to the slot system of (12.5) one further slot P_s(Z) = {p prime : p ∉ S, p ∈ 1_T, q_p/P ∈ supp W_s}, P = Z^{ℓ_s}, with disjoint window, and define the **s-marked term**

  I^{(s)}_η(X,Y,Z) := Σ_{p ∈ P_s(Z)} ψ(p) W_s(q_p/P) · I_η[1_{v_p(s)=1}](X, Y, Z),

where I_η[1_{v_p(s)=1}] is (6.1) with the indicator v_p(s) = 1 inserted in the s-sum (s = p s', (s', p) = 1, s' ≍ Y' := Y/P, s ∈ σ ⟺ s' ∈ σ because p ∈ 1_T). The other scales X, Y, Z and the row ball Q = q_{b*}XY are unchanged; P_a = Y²/Q = Z^b/q_{b*} as in Prop 15.3. (Two-weight version W_s(q_p/P)W_1(q_{s'}/Y') is the same with q_p^{-w} replaced by q_p^{-w_1}; the single-weight version with (s',p) = 1 is used below.) The compensated A-slots of (12.5) can be kept; they commute with this restriction (the s-restriction only changes the s-coefficient, the A-marks only change the completed index and Z).

Normalization: Σ_p ψ(p)W_s over ≍ P/log P primes of a probe whose s-sum is a 1/P-fraction of the full one, so I^{(s)} is of the same nominal size as I_η (no renormalization, up to 1/log P).

### 1.2 Gauss-sum factorisation (Sec 4.2, CRT)
For coprime primary p, s' outside S, representing d = s'x + py (x mod p, y mod s'):

  g_{χ_{ps'}}(ps', −m) = χ_p(s') χ_{s'}(p) g_{χ_p}(p, −m) g_{χ_{s'}}(s', −m),   g_{χ_p}(p, −m) = ω_p \bar χ_p(m) 1_{p∤m} G_1(p),  |G_1(p)| = q_p^{1/2}.

By sextic reciprocity (Lemma 4.4) χ_p(s')χ_{s'}(p) = R(p,s') χ_p(s')² = χ_p(s')² on 1_T: a **moving cubic cross-phase** between the slot prime and the residual additive variable (it is the Gauss-sum CRT phase, not part of the coefficient). The fixed factors split: χ_{ps'}(b*)/ξ(ps') = Ξ(p)Ξ(s'), Ξ = ξ·χ_•(b*) (fixed finite-order character, conductor in S).

Hence, in the paper's exact annular rewriting A_m = Y^{−3/2} Σ_s c(s) W_1(r_s) r_s^{−1+iν} g_{χ_s}(s,−m), the modified polynomial is the same object with the **coefficient vector** c(s) replaced by

  c^{(s)}(s) = 1_{s = ps', p∈P_s(Z)} · ψ(p)Ξ(p)W_s(q_p/P) · c_σ(s'),   ‖c^{(s)}‖_∞ = 1,  #supp ≍ Y/log P,

and, after factorising the Gauss sum,

  A^{(s)}_m = P^{−1} Σ_{p} a(p) ε_p \bar χ_p(m) 1_{p∤m} A^{[p]}_m,   a(p) = ψ(p)Ξ(p)W_s(q_p/P),  ε_p = ω_pγ_1(p),
  A^{[p]}_m = Y'^{−3/2} Σ_{s'} c_σ(s') χ_p(s')² W(…) g_{χ_{s'}}(s', −m)   (the cubic-twisted Gram vector at scale Y').

So: the factor \bar χ_p(m) 1_{p∤m} (= the conjugate sextic character of p on the row, with the mask p ∤ m) is carried by the p-Gauss sum; the Ξ-phase and ray class are carried by the coefficient; the cubic twist χ_p(s')² sits in the residual additive sum. Normalisation check: if the P vectors \bar χ_p(m)A^{[p]}_m were orthogonal, Σ_m|A^{(s)}_m|² ≈ P^{−2}·P·(Q/Y') = Q/Y, the unmarked diagonal.

### 1.3 The Gram form (Prop 15.2 redone for c^{(s)})
Nothing in the proof of Prop 15.2 before the coefficient enters (Poisson in m with modulus s_1s_2, Lemma 13.3 correlation F(Cn_1,Cn_2;Ck) = χ_{n_1}(k)χ_{n_2}(−k)R(n_1,n_2)L_C, kernel argument q_Cq_k/P_a, Möbius, reciprocity χ_m(k) = κ_{ζ,e}(m)R(k_good,m)Π_{p|k_good}χ_p(m)^{e_p}) uses the coefficient. Three pieces:

(i) k = 0 (diagonal): forces s_1 = s_2, gives φ(C) per s; with #supp c^{(s)} ≍ Y/log P this is ≪ Q/Y. Unchanged.

(ii) Equal-prime pairs p_1 = p_2 = p: then p | C, so (Lemma 13.3) C | k forces p | k and q_Cq_k ≥ P², while the kernel needs q_Cq_k ≲ P_a. For P > P_a^{1/2} (ℓ_s > b/2) there are **no nonzero frequencies**: the block is complete. For P ≤ P_a^{1/2} the exceptional count is (P_a/q_C)^{1/6}/P per dyad, total ≪ (Q/Y)P^{−1}(P_a/P)^{1/6}. (Factorised check: the twist χ_p(s')² on the columns makes every exceptional column sum a cubic character sum mod p, saving P^{1/2}q_C/Y' by Pólya–Vinogradov, and the mask 1_{p∤m} contributes the sub-ball m = pm' with incompleteness P_a/P. Both pictures agree.) Negligible for ℓ_s ≥ b/7.

(iii) Distinct primes p_1 ≠ p_2 (p_i ∤ C generically; the thin set p_1 | s'_2 behaves like (ii)). Exceptional k = a_1^6 e: the column character on n_1 = p_1 s'_1/C is 1_{(n_1,a_1)=1}·χ_{n_1}(e_C)·κ_{ζ,e}(n_1)R(k_good,n_1), multiplicative in n_1, and p_1 ∤ a_1 automatically (q_{a_1} ≤ P_a^{1/6} < P). So the two-column sum **factorises exactly**:

  Σ_{n_1} c^{(s)}(Cn_1)(…) = [ Σ_{p ∈ P_s} ψ(p) Ξ(p) χ_p(e_C) κ_{ζ,e}(p) θ(p) W_s(q_p/P) ] · [ Σ_{s'} c_σ(s')(…)W ],       (Q.1)

θ ∈ T̂ from the ray-class indicator (R-phases are 1 on 1_T). Replacing the paper's trivial two-column count (Y/q_C)² by |(Q.1)|² gives the exceptional term (Q/Y)P_a^{1/6}·M(ψ)², where

  M(ψ) := max_{e_S, θ, e_C} P^{−1}|Σ_{p∈P_s} ψ(p)Ξ(p)χ_p(e_S e_C)θ(p)W_s(q_p/P)|.           (Q.2)

Nonexceptional k: the complete-mean argument applies to the s'-column for each fixed (p_1,p_2); the period of the joint coefficient grows by at most P, so the third term of (15.4) becomes at worst (Q/Y)P_a²P/Y (κ = 1 below; κ = 0 if the (15.5) lattice Poisson is run in the s'-variable with the p-sum outside).

**Direct bound** (Cauchy–Schwarz in m with Lemma 15.1 unchanged, prefactor Q^{−1/2}, rescaled tuples f(d) = −d as in (15.8)):

  |I^{(s)}_η| ≪ Z^{lx/2+ε} · max{ 1, P_a^{1/12} M(ψ), (P_a/P)_+^{1/12}P^{−1/2}, (P_a²P^κ/Y)^{1/2} }.        (Q.3)

### 1.4 What makes M(ψ) small, and the hidden principal member
Each character in (Q.2) is ψ·(fixed finite-order character χ_{e_S,e_C,θ} := Ξχ_•(e_Se_C)θ). Under the family hypothesis (no zero of any finite-order Hecke L-function of F with real part > β*, with polynomial conductor uniformity, which the explicit formula gives with log losses) the prime sum is ≪ P^{β*+ε} whenever ψχ_{e_S,e_C,θ} is nonprincipal; unconditionally after Part II, β* ≤ 7/8 for the whole family. Then M(ψ) ≪ P^{β*−1+ε} and (Q.3) gives

  θ_eff = max{0, 1/12 − (1−β*)ℓ_s/b}  (plus the two side terms of (Q.3)).

**But the family {Ξχ_•(e_Se_C)θ} contains the principal character.** ξ was chosen as a residue character mod b* of order dividing 6, nonprincipal at each prime of S. At a tame p ∈ S the characters of (O/p)^× of order | 6 are exactly the powers of the sextic residue symbol (·/π_p)_6, and by reciprocity (π_p/n)_6 = (n/π_p)_6·(phase in T̂) on primary n; at the prime over 2 the order-3 character is the cubic symbol (−2/n)_3 (the paper uses this: χ_c(4) = (c/(−2))_3), and at λ the quadratic component is trivial on primary n. Hence ξ̄ = χ_•(e_S^{(0)})·θ_0 for some S-supported numerator e_S^{(0)} and θ_0 ∈ T̂, i.e. Ξ̄ ∈ K_S·T̂ where K_S = {χ_•(ζπ_S^e)} is the fixed Kummer family that the exceptional frequencies k = a_1^6 e range over. With e_C = 1 (C ≍ 1 dominates, as in J (J.2)) the member e = b*^{-1}e_S^{(0)}, θ = θ_0 of (Q.2) is

  M(ψ) ≥ P^{−1}|Σ_{p ∈ P_s} ψ(p) W_s(q_p/P)|  =: |mean_s ψ|.                                   (Q.4)

This is the precise form of J's "the probe coefficient is the top eigenvector": the exceptional phase ρ_{e_0} equals Ξ̄ on the ray class, so the coherence is the plain mean of the slot weight. Thus the gain requires ψ itself (restricted to 1_T) to be nonprincipal, e.g. ψ = η̄ when η does not factor through T (the paper chooses T independently of η, so this is the generic case; for the finitely many targets η ∈ K_S T̂ no weight on 1_T helps).

## 2. Poisson side

### 2.1 Where p enters
Poisson in m uses the full modulus s b* A = p s' b* A (Sec 7.1): nothing changes in (7.1)-(7.5) except that the s-sum carries 1_{v_p(s)=1}ψ(p)W_s(q_p/P). In the Euler factorisation of Lemma 7.1 the valuation k = v_p(s) is already a summation index of P_p ((7.10), table (7.16)); restricting to k = 1 replaces P_p by its k = 1 part, exactly as restricting p | A replaces P_p by P_p^* in Sec 16. **p does not enter the completed index A and does not become a mark of multiplicity 5 on cn³**: the conjugate character \bar χ_p(m) of the direct side is the m-Fourier dual of the local Gauss lift at k = 1, not a factor of χ_A(m). (J's caveat (a) is not an obstruction: on the Poisson side the row coefficient is χ_s(H(b*A)^{−1}) = Π_{p|s}χ_p(·), multiplicative in s with no cross phases; the CRT phase χ_p(s')² of 1.2 is undone by Poisson.)

### 2.2 The local factor at p, six cases j = v_p(u) mod 6
From (7.8) (k = 1 needs t = 0, or t > 0 with j' ≥ 1; k ≥ 2 only at t = 0) and the k = 1 rows of (7.16):

  P_p^{(k=1)} = 1_{j=0} W_loc + (1−R)^{−1} [ J_j^{(1)} − η(p)(Q−1)Q^{−x−w} V^{1_{j≤1}}/(1−V) ],   W_loc = ρQ^{−w},
  J^{(1)}_0 = W_loc R,  J^{(1)}_1 = η(p)Q^{−x−w},  J^{(1)}_2 = 0,  J^{(1)}_3 = −η(p)b_pρ^{−2}Q^{2−3x−w},  J^{(1)}_4 = −η(p)a_pρ^{−3}Q^{5/2−4x−w},  J^{(1)}_5 = 0.

Every term carries Q^{−w} (the Mellin weight of the prime in s). Leading behaviour: j = 0: χ_p(u)Q^{−w} − η(p)Q^{1−x−w−6z}; j = 1: η(p)Q^{−x−w}(1 − Q^{1−6z}/(1−V)); j ≥ 2: −η(p)Q^{1−x−w}(1 + O(Q^{1−2x})). The full s-marked local replacement, with the scalar quotient (1−V)^{−1}(1−W)^{−1}(1−D) of (7.13) extracted as in (16.2), is

  G_p^{(s)} = ψ(p) P_p^{(k=1)} (1−V)(1−W)/(1−D),                                                (Q.5)

holomorphic in both Euler regions (no 1−W, P_p or H_p denominator; only 1−R, 1−V, 1−D). So the analogue of (16.3)-(16.7) holds verbatim: H_{η,u,Z} = Σ_{tuples} Π_{A-slots}(q^{z−1}G_{p_i}) · Σ_{p∈P_s} W_s(q_p/P) G_p^{(s)} · Π_{unselected}H_p, with (10.4) and (16.5)-(16.6) unchanged (|G_p^{(s)}| ≪ Q^{−w_r}·Q^{O(1)}). **Definition 10.1 is satisfied.** At nonprincipal rows the main part of the s-slot is ψ(p)χ_p(u)Q^{−w}1_{p∤u} (the sextic-character prime factor, with exponent −w instead of z−1 and amplitude P^{1/2−w_r} = P^{a−1/2+6e} on the dynamic line), the errors are O(Q^{1−x_r−w_r−6z_r}) = O(Q^{−2}) off u and divisor-many ramified terms on u with the same conductor-deficit structure as Prop 16.1.

### 2.3 The principal row: exact identity and the obstruction
At u = 1 (j = 0, ρ = 1, W_loc = W = Q^{−w}, D = η(p)Q^{−x}):

  P_p^{(k=1)} = Q^{−w}(1−R)^{−1} [ 1 − η(p)(Q−1)Q^{−x}V/(1−V) ],

and at the double residue w = 1, z = 1/6 (V = Q^{−1}) the bracket equals (1−Q^{−1})(1−η(p)Q^{−x})/(1−Q^{−1}), so

  G_p^{(s)}(x, 1, 1/6) = ψ(p) q_p^{−1} (1 − q_p^{−1})² / (1 − R_p(x)),   R_p = a_p² q_p^{3−6x}.        (Q.6)

The factor (1−η(p)q_p^{−x}) of 1/L(x,η) is reproduced exactly by the k = 1 restriction and cancels against 1−D: **the principal multiplier of the s-slot is Σ_p ψ(p)W_s(q_p/P) q_p^{−1}(1+O(q_p^{−1})), the plain mean of ψ on the slot** — the same functional as (Q.4). With ψ = η̄ (J's proposal) this is ≪ P^{β*−1+ε}: the signal is destroyed by exactly the factor that was gained in (Q.4). The only coherent remainder is the second-order term −Σ_p W q_p^{−1−x} ≍ P^{−x}/log P from the (e_0,l,k) = (1,0,1) family (p | c and p | s), which multiplies the signal by P^{−β*} (and changes C(s) to (1−ℓ_s)s + c, still admissible in Prop 2.1 after Z ↦ Z^{1−ℓ_s}); so (10.18) holds with A_η(Z) ≍ P^{−β*}m_W/log P, but the comparison is worse than without the slot (model V1 below).

**No-go identity.** For any slot weight ψ (any bounded coefficient on s, in fact), with m := |mean_s ψ|:
  direct bound  ≍ Z^{lx/2}[1 + P_a^{1/6} m²]^{1/2},   principal signal ∝ Z^{C(β*)}·m.
Dividing, signal/direct ≤ Z^{C(β*)−lx/2}P_a^{−1/12} with equality iff m = 1 (the ray-class indicator). The Gram loss Z^{b/12} is therefore a floor for every choice of additive coefficient, not only for the probe's; the exceptional eigenvector of the Gram operator is the signal direction. The step that "must hold" for the idea to work — |Σ_{p∈1_T}ψ(p)W| ≪ P^{1−δ} together with |Σ_p ψ(p)W q_p^{−1}(1−η(p)q_p^{−s})| ≫ P^{−δ'} for some δ' < δ — is impossible, because the two sums differ only by the factor (1−η(p)q_p^{−s})(1+O(q_p^{−1})), which can only produce the P^{−β*}-suppressed term.

Compensation does not help: adding rescaled terms λ_p I_η(X/q_p, Y/q_p, Z) (signal Z^{C}q_p^{−1/3}λ_p, direct (X/q_p)^{1/2}P_a^{1/12}) can restore a coherent principal term only with ψ-independent λ_p, i.e. by adding back an unmarked probe at smaller scales, whose nonprincipal rows are the ones (12.5) already pays for; and a weight ψ(p_1,p_2) = χ_{p_1}(p_2) on two s-primes gives the same bilinear symbol sum on both sides.

Section 16's compensation is thus not the problem (it can be redone: (Q.5) is the holomorphic replacement, (Q.6) the principal identity); the problem is that the identity (Q.6) has no ψ-free term.

## 3. Bookkeeping (scripts/prime_in_additive.py)
Model: ℓ_A = A-slot length (counts, h, balanced scales use ℓ_A), ℓ_s free with ℓ_s ≤ ly/2; direct bound lx/2 + max{0, θ_eff b, (b−ℓ_s)/12 − ℓ_s/2, b − ly/2 + ℓ_s/2} + k/2, θ_eff = max(0, 1/12 − (1−β*)ℓ_s/b).
* V0 (naive J formula; signal assumed retained): (a) β* = 7/8: **B = 0.86398** at b = 0.169, ℓ_A = 0.155, ℓ_s = 0.112 (θ_eff = 0, floor active); (b) self-consistent β* = B: **B = 0.86395** at ℓ_s = 0.106. Scan: ℓ_s = 0.02/0.04/0.06/0.08 → 0.87289/0.87076/0.86855/0.86627. Optimal ℓ_s ≈ 2b/3 ≈ 0.11 (θ_eff = 0; the equal-prime and nonexceptional side terms are slack). This is the θ = 0 ceiling of note A, and it ignores the s-slot's effect on nonprincipal rows (amplitude P^{a−1/2} instead of the A-slot's P^{z_0−1/2}; not modelled).
* V1 (honest: signal × P^{−β*} from (Q.6) with ψ = η̄): B = [11/12 − ℓ_A/4 − b/12 + max(…) + k/2]/(1−ℓ_s); optimum **ℓ_s = 0, B = 0.874957**; ℓ_s = 0.02/0.04/0.06 → 0.8876/0.9010/0.9167. Monotonically worse.
Prime supply: an s-prime contributes a plain polynomial Σψ(p)χ_p(u)q_p^{−w} at the rows, usable in principle as a Lemma 18.1 slot, so the competition with Prop 19.2 is milder than J feared; irrelevant given §2.3.

## 4. Deliverables
(a) Modified probe: §1.1; direct representation §1.2 (coefficient c^{(s)}, factor \bar χ_p(m)1_{p∤m} from the p-Gauss sum, cubic cross-phase χ_p(s')²); direct bound (Q.3) with θ_eff = max(0, 1/12 − (1−β*)ℓ_s/b) under the family zero-free hypothesis and M(ψ) ≪ P^{β*−1}, which needs ψ nonprincipal on 1_T (Q.4).
(b) Poisson side: p stays in the s-variable (k = v_p(s) = 1 of Lemma 7.1), the completed index is untouched, the holomorphic replacement (Q.5) and the Euler identity (7.13) survive, Definition 10.1 and (10.17) hold. **Breaks at the principal row**: identity (Q.6), the double residue is ψ-mean × q_p^{−1}, so the signal carries the same factor M(ψ) as the Gram term; (10.18) holds only with A_η(Z) ≍ P^{−β*}.
(c) Predicted boundary: **0.874957, unchanged** (V1). The naive number 0.86395-0.86398 (V0) is the θ = 0 ceiling and is not attainable by this device.
(d) Minimal completing lemma (what would have to be true, and is false): "there is a bounded function ψ on the primes of 1_T with |Σ_{p≍P}ψ(p)W| ≪ P^{1−δ} and |Σ_{p≍P}ψ(p)W q_p^{−1}(1 − η(p)q_p^{−s})| ≫ P^{−δ'} on Re s = β*+e for some δ' < δ". By (Q.6)-(Q.4) both sides are the same mean up to the (1−η(p)q_p^{−s}) factor, so δ' ≥ min(δ, β*)... impossible with δ' < δ ≤ 1−β* < β*. The lemma that would help instead is a bilinear one: non-alignment of the completed row B_m with the Patterson-bias direction (J §6.2), outside this note's scope.

## 5. Summary (≤350 words)

Setting s = p s' (p ≍ Z^{ℓ_s} in 1_T, weight ψ(p)W_s(q_p/P), v_p(s) = 1) changes nothing in the structure of either representation. Direct side: the Gauss sum factorises by CRT, g(ps',−m) = χ_p(s')²·g(p,−m)g(s',−m) on 1_T, the p-Gauss sum carries \bar χ_p(m)1_{p∤m}, the coefficient vector of A_m becomes ψ(p)Ξ(p)c_σ(s'), and Prop 15.2's proof goes through with the trivial two-column count replaced by the factorised sum (Q.1): the exceptional term becomes (Q/Y)P_a^{1/6}M(ψ)², M(ψ) the largest normalised mean of ψ against the fixed family Ξχ_•(e_S)θ; equal-prime pairs are complete for ℓ_s > b/2; the nonexceptional term grows by at most P. Under the family zero-free hypothesis M(ψ) ≪ P^{β*−1} if ψ is nonprincipal on 1_T, giving θ_eff = max(0, 1/12 − (1−β*)ℓ_s/b) and, in the model, B = 0.86398 (β* = 7/8 input) / 0.86395 (self-consistent) at ℓ_s ≈ 0.11, the θ = 0 ceiling.

Poisson side: p stays in the s-variable; Lemma 7.1 already indexes k = v_p(s), so the restriction picks the k = 1 part of P_p, the completed index cn³ is untouched (no multiplicity-5 mark), the holomorphic replacement (Q.5) and the scalar quotient (7.13) survive, and Definition 10.1/(10.17) hold. The construction breaks at the principal row: at the double residue the k = 1 local factor is exactly ψ(p)q_p^{−1}(1−q_p^{−1})²/(1−R_p) — the (1−η(p)q_p^{−s}) of 1/L(s,η) is reproduced by the restriction and cancels against 1−D — so the signal is multiplied by the plain mean of ψ on the slot, the same functional that controls the Gram coherence, because ξ̄ is itself a product of Kummer symbols of the S-primes (sextic reciprocity) and so Ξ̄θ_0 belongs to the exceptional phase family. For any additive coefficient with mean m, direct ≍ Z^{lx/2}(1+P_a^{1/6}m²)^{1/2} and signal ∝ Z^{C(β*)}m, so Z^{b/12} is a floor; with ψ = η̄ the signal drops by P^{−β*} while the Gram term drops only by P^{−(1−β*)}, and the boundary rises (0.8876 at ℓ_s = 0.02). Predicted boundary: 0.874957, unchanged. The missing lemma is bilinear (non-alignment of the row vector with the Patterson-bias direction), not a better additive coefficient.

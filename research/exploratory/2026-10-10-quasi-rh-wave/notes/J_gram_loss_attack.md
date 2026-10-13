# J. The Gram loss P_a^{1/6} in Proposition 15.2 — mechanism, verdict, model

Sources: main paper Secs 6.1 (lines 2684-2830: definition (6.1), separation (6.2), A_{m,σ,v}), 13.3 (5330-5480: Lemma 13.2 prime-power Fourier sums, Lemma 13.3 full correlation F, (13.6)-(13.8)), 14.4 (5801-6096, Lemma 14.3 / (14.14)), 15.1-15.3 (6097-6525). Kintali §3.3 eq. (14) (kintali_qrh.txt 587-615). Model: `scripts/exponent_model.py`, scan `scripts/gram_theta_scan.py`.

## 1. The chain of inequalities producing the low bound (Prop 15.3, lines 6457-6525)

Separation (6.2), line ~2800: for each ray class σ,

  I_η = Q^{-1/2}(2π)^{-1} Σ_σ ∫ Ŵ_0(iv) Σ_{m≠0} Ω(q_m/Q) ξ(m)(q_m/Q)^{-iv} A_{m,σ,v}(Y) B_{m,σ}(Z) dv,   Q = q_{b*}XY,

with (line ~2790)

  A_{m,σ,v}(Y) = Y^{-1} Σ_{s∈σ} W_1(q_s/Y) χ_s(b*)/(τξ(s)) (q_s/Y)^{-1/2+iv} q_s^{-1/2} g_{χ_s}(s,−m),

i.e. A_m = Y^{-1} Σ_{s≍Y} c_σ(s) g̃(s,−m) with |g̃| = 1 (normalised sextic Gauss sum; Lemma 13.2 shows χ_p has order 6: "6 | a" is the principal case), and B_m = Σ_θ a_θ ∫ Z^t Φ(t) T(t+1/2, ν_σθχ•(m)) dt = the theta-type row of length Z twisted by the row character a ↦ χ_a(m) = (m/a)_6.

For the compensated probe (12.5), with a rescaled subset J of total slot length d, X' = X/q_{p_J}, Y' = Y/q_{p_J}, Q = q_{b*}X'Y' ≍ Z^{M'}, M' = M − 2d, P_a = Y'^2/Q = Y'/X'·q_{b*}^{-1} = q_{b*}^{-1} Z^{1/8} (line 6470: "P_a = Y'^2/Q = q_{b*}^{-1} Z^{1/8}"; in general P_a = Z^b).

Step 1 (Lemma 15.1, (15.2), lines 6134-6140): Σ_{q_m≪Q} |B^J_{m,σ}|^2 ≪ Z^{M'+((d−1/6)/4)_+ + ε} = Z^{M'+ε} ≍ Q. Proof = Lemma 14.3 (reflected energy (14.14)) applied to the marked completed row; the "(d−1/6)/4" branch is the (5ℓ−1)_+ penalty of the model. So ‖B‖^2 ≍ Q, i.e. |B_m| ≈ Z^ε on average (Lindelöf-on-average for the rows).

Step 2 (Prop 15.2, (15.4), line 6303):

  Σ_{q_m≪Q} |A_m|^2 ≪ (1+|ν|)^{J_Gr} (Q/Y') (1 + P_a^{1/6} + P_a^2/Y') Z^ε.

Step 3 (Prop 15.3, lines 6478-6490): the length inequality ly − d − 11b/6 ≥ 1/12 gives P_a^2/Y' ≪ P_a^{1/6}, hence (15.7) Σ|A_m|^2 ≪ (Q/Y')P_a^{1/6}Z^ε; Cauchy–Schwarz in m:

  |Σ_m A_m B_m| ≤ ‖A‖‖B‖ ≪ ((Q/Y')P_a^{1/6})^{1/2} Q^{1/2},

times the prefactor Q^{-1/2} of (6.2): Q^{-1/2}(Q/Y')^{1/2}P_a^{1/12}Z^{M'/2} = (X')^{1/2}P_a^{1/12}  (line 6486). Rescaled tuples cost f(d) = d − 3d/2 − d/2 = −d ≤ 0 (15.8), so the total is Z^{lx/2 + b/12 + ε}, (15.6). This is the general form lx/2 + θb with θ = 1/12 = (1/2)·(1/6).

So the whole Gram loss is the exponent 1/6 in the middle term of (15.4), halved by the square root of Cauchy–Schwarz.

## 2. Exact origin of P_a^{1/6}: the sixth-power ("exceptional") Poisson frequencies

Proof of Prop 15.2 (lines 6308-6456). Expand |A_m|^2, write s_1 = Cn_1, s_2 = Cn_2, (n_1,n_2) = 1, and Poisson in the row variable m. The product g(s_1,−m)conj g(s_2,−m) is periodic in m modulo L = Cn_1n_2, q_L = q_{s_1}q_{s_2}/q_C ≍ Y'^2/q_C, while the row ball has radius Q^{1/2}. The Poisson dual frequency j ∈ O (Lemma 13.3 forces C | j, j = Ck) enters the Fourier kernel at argument Q·q_j/q_L = q_C q_k/P_a (line 6321). Hence the row sum is *incomplete* exactly when P_a = Y'^2/Q > 1, and the nonzero frequencies with q_C q_k ≲ P_a survive.

By (13.7), F(Cn_1,Cn_2;Ck) = χ_{n_1}(k)χ_{n_2}(−k) R(n_1,n_2) L_C(n_1,n_2;k), |L_C| ≤ q_C. By sextic reciprocity χ_{n_i}(k) = χ_k(n_i)·(fixed phase), so the residual columns n_1, n_2 carry the sextic character χ_k of modulus rad(k), and the joint coefficient is periodic modulo r = lcm(l_fixed, rad C, rad k) (line 6354). Then:

* **Nonexceptional k** (some prime p ∤ C l_fixed with 6 ∤ v_p(k)): χ_p(m_1)^{e_p} is nonprincipal, the complete mean vanishes, and 4-dimensional lattice Poisson (15.5) gives the residual-column cancellation; after the dyadic sums these contribute (Q/Y')·P_a^2/Y' (lines 6372-6395).
* **Zero frequency** k = 0: forces n_1 = n_2 = 1 (Lemma 13.3), gives φ(C); summed over C ≍ Y' this is the diagonal Q/Y' (lines 6362-6365).
* **Exceptional k ≠ 0** (lines 6396-6412): "(k) = a_1^6 e, where e is sixth-power-free and supported on the primes of C and the fixed support", at most 6^{ω(C)+O(1)} ≪ q_C^ε choices of e, and for each the shell bound q_k ≤ C_sh K_R permits q_{a_1} ≤ (K_R/q_e)^{1/6}, giving O(K_R^{1/6} q_C^ε) frequencies with K_R = RP_a/C_0. For these the sextic symbol χ_k(·) = χ_e(·)·1_{(·,a_1)=1} is principal on the residual columns, and the paper uses "|L_C| ≤ q_C, and the trivial two-column point count": contribution ≪ R^{−B} Z^ε Y'^2 (RP_a)^{1/6} C_0^{−1/6} D_0^{−1} before the prefactor Q/Y'^3, i.e. **(Q/Y')·P_a^{1/6}** (line 6412: "This gives the term (Q/Y')P_a^{1/6}Z^ε").

In words: P_a^{1/6} = #{sixth powers a^6 in the dual box q_a^6 ≲ P_a}, and each sixth-power frequency contributes one full diagonal Q/Y', because for it the character in the residual (denominator) variables is principal and there is nothing to cancel. The exponent 1/6 is 1/(order of the residue symbol); with cubic symbols it would be 1/3, with quadratic 1/2. It is not a conductor-growth cost of the slot primes, not a lattice-count loss near the fractions, and not a crude Schur bound: it is a genuine additional "diagonal" of the Gram matrix.

Comparison with Kintali §3.3 eq. (14): his planar large sieve (Lemma 6.1 here) treats the Y^2 fractions d/s as generic separated points of spacing δ ≍ 1/Y and gives Σ|A_m|^2 ≪ (Q+Y^2)/Y = (Q/Y)(1+P_a); at b = 0 (P_a = 1) there is nothing to lose. For b > 0 the large sieve loses the full P_a; Prop 15.2 already exploits the Gauss-sum structure of the coefficients a_{s,d} = χ_s(d) (complete correlations F) to reduce P_a to P_a^{1/6}. The sixth-power frequencies are the part of the "uncertainty-principle" loss that the character structure cannot remove.

## 3. Verdict: intrinsic to Σ_m|A_m|^2 — Prop 15.2 is sharp (lower-bound configuration)

Model computation (cubic/sextic symbol, C = 1 i.e. coprime denominators, ignoring fixed-modulus phases). With Φ a Gaussian majorant of the row ball and ψ = conj χ_{n_1}χ_{n_2} (primitive mod n_1n_2), Poisson gives
  Σ_m Φ(m/Q) ψ(m) = (Q/q_L) g(ψ) Σ_k conj ψ(k) Φ̂(Q^{1/2}k/(L√−3)).
Using g(χ_aχ_b) = χ_a(b)χ_b(a)g(χ_a)g(χ_b), g(conj χ) = χ(−1)conj g(χ) and reciprocity χ_{n_1}(n_2) = χ_{n_2}(n_1)·(fixed phase), the Gauss-sum phases combine exactly:
  g(s_1) conj g(s_2) g(ψ) = q_C q_{n_1} q_{n_2} · conj χ_C(n_1)χ_C(n_2) · (fixed-modulus phase).
Hence, up to the Möbius correction for (n_1,n_2) = 1 (which only changes the constant by 1/ζ_K(2)-type factors) and the Ramanujan factor c_C(k),

  Σ_m Φ(m/Q)|A_m|^2 = (Q/Y'^3) Σ_C Σ_k Φ̂(q_C q_k/P_a) c_C(k) | Σ_{n≍Y'/q_C} c_σ(Cn) W(n) χ_k(n) conj χ_C(n) ρ(n) |^2 + (diagonal),      (J.1)

with ρ a fixed-modulus unimodular function. Every term with Φ̂ ≥ 0 and c_C(k) = φ(C) > 0 (C | k) is **nonnegative**. For k = a^6·C·e_0 (e_0 in the fixed family chosen so that χ_{e_0}ρ is principal on the ray class σ; the family of exceptional e spans the characters of the fixed ray group, and the ray-class indicator contains the principal component), the inner sum is Σ_{n∈σ, (n,aC)=1} |c| W(n) ≍ Y'/q_C with no cancellation. Summing a over q_a^6 ≲ P_a/q_C^2 and C over C ≍ 1:

  Σ_m Φ(m/Q)|A_m|^2 ≥ (Q/Y'^3) Σ_C φ(C) q_C^{−2} Y'^2 (P_a/q_C^2)^{1/6} ≍ (Q/Y')·P_a^{1/6}.       (J.2)

So (15.4) is attained: Σ_{q_m≪Q}|A_m|^2 ≍ (Q/Y')(1 + P_a^{1/6}) in the paper's range P_a ≤ Y'^{6/11}. The paper's own counting in this branch (K_R^{1/6}q_C^ε frequencies × trivial columns, C_0^{−1/6}) differs from (J.2) only by the C_0 ≍ 1 normalisation; it is tight at C_0 ≍ 1.

Sanity checks. (i) Quadratic analogue over Z: A_m = Y^{−3/2}Σ_{p≍Y} g(p,m), g(p,m) = (m/p)ε_p√p. Square rows m = b^2 have |A_m| ≍ 1 (no cancellation in Σ ε_p√p over p ≡ 1 mod 4), Q^{1/2} of them, contribution Q^{1/2} = (Q/Y)P_a^{1/2}; the dual computation (square frequencies k = a^2 ≤ P_a) gives the same. Both sides agree, confirming the mechanism "k-th power frequencies ↔ k-th power rows ↔ loss P_a^{1/k}". (ii) Cubic analogue: the m-side counterpart is the Patterson bias Σ_{s≍Y'} g̃(s)conj χ_s(m) ≈ Y'^{5/6}τ(m) with |τ(m)| ≈ q_m^{−1/6} on cube-free m (coefficients of the cubic theta function), which exceeds the random size Y'^{1/2} on every row with q_m ≤ Y'^2; summing |A^{bias}_m|^2 ≈ Y'^{−1/3}q_m^{−1/3} over the ball gives Q^{2/3}Y'^{−1/3} = (Q/Y')P_a^{1/3}, matching the cube-frequency count. So the excess mass is NOT concentrated on sparse structured rows (cube rows alone give only (Q/Y')^{1/3}); it is a uniform bias spread over generic rows of the ball — Cauchy–Schwarz weights or row sieves cannot remove it. (iii) The same phenomenon is the sharpness of the (KD)^{2/3} term in the cubic/sextic large sieve (Lemma 9.1, (9.1); Heath-Brown, Dunn–Radziwiłł): Gauss sums are the extremal coefficients. A = ĝ*c is literally that extremal vector.

Operator picture. The s-space Gram matrix G = ĝĝ* decomposes by frequency, G = Σ_k λ_k v_k v_k*, v_k(s) = χ_s(k)·(phases). Bulk eigenvalues ≈ Q/Y'^2 (trace Q/Y' over Y' dimensions). The sixth-power frequencies give v_{a^6e} ≈ χ_e·1, a fixed finite set of directions, each with eigenvalue ≈ (Q/Y'^2)P_a^{1/6}. The probe's coefficient c_σ (ray-class indicator × fixed phases) *is* a top eigenvector. Hence ‖A‖^2 = c*Gc = λ_top‖c‖^2 cannot be reduced by splitting A; and A = ĝ*c is itself an eigenvector of ĝ*ĝ in m-space, so no m-space projection isolates the loss either.

Conclusion for item 2: **(b) intrinsic.** Prop 15.2 is sharp up to Z^ε for the probe's coefficients; the only improvable piece of (15.4) is the third term P_a^2/Y' (trivial point count for N < 𝒬 in (15.5); a Pólya–Vinogradov/Weil bound on the complete two-column transform would reduce it to ≈ (Q/Y')P_a^{?}/Y'^{1/2}·…), but that term is inactive at the optimum (it is the constraint b ≤ ly/2, slack at θ = 0: b = 0.169 < ly/2 = 0.254).

Consequently any improvement of θ must come from the *bilinear* form Σ_m ξ(m)A_mB_m, i.e. from non-alignment of B with the Patterson-bias direction — not from a better Gram lemma.

## 4. What is provable about the lemma itself

Sharp statement (what can be written down): for fixed finite linear combinations c of ray coefficients and any ε > 0, uniformly in 1 ≤ P_a ≤ Y'^{1−ε},

  Σ_{q_m≪Q}|A_m|^2 = (Q/Y')·[ κ_0(c) + κ_1(c) P_a^{1/6} ] (1 + O(Z^{−δ})) ,

with κ_0 the diagonal constant and κ_1(c) = Σ_{C,e} φ(C)q_C^{−7/3}… |mean of cρχ_e on σ|^2 ≥ 0, with κ_1 = 0 iff c is orthogonal to all fixed-modulus sextic twists on its ray class — impossible for a ray-class indicator. There is no improved upper bound. (The nonexceptional term can be improved to (Q/Y')P_a^{3/2}/Y'^{1/2}-type by using square-root cancellation in the complete 4-dimensional transform instead of the sup bound q_C, but this is irrelevant at the current parameters.)

Hence: θ = 1/12 is forced for the architecture "Cauchy–Schwarz over the row ball × Gram bound × row energy".

## 5. Model numbers (scripts/gram_theta_scan.py)

| θ | B | b | ℓ | active |
|---|---|---|---|---|
| 1/12 | 0.874957 | 0.1232 | 0.1668 | low, class (δ,x)=(0.3885,1/2) |
| 1/18 | 0.871423 | 0.1599 | 0.1632 | low, class, floor |
| 1/24 | 0.869608 | 0.1880 | 0.1569 | low, floor |
| 1/36 | 0.867588 | 0.1813 | 0.1560 | low, floor |
| 0 | 0.863950 | 0.1693 | 0.1544 | low, floor |

Predicted boundary for the θ I believe provable *by improving the lemma*: 0.874957 (no change). The values θ < 1/12 are reachable only by the bilinear routes below; the most promising (slot prime in the additive variable, §6.1) would, if it works at full strength, give θ_eff = max(0, 1/12 − (1−β*)ℓ_s/b) where ℓ_s is the slot length moved into s; at (b,ℓ) ≈ (0.17,0.15) and 1−β* ≈ 0.13 one has (1−β*)ℓ/b ≈ 0.115 > 1/12, so θ_eff = 0 and B ≈ 0.864 is the ceiling of that idea — but it conflicts with the count side's use of the same primes (see §6.1), so a realistic estimate is a partial transfer ℓ_s ≈ ℓ/2: θ_eff ≈ 1/12 − 0.057 ≈ 0.026, B ≈ 0.8674.

## 6. Routes beyond the lemma (item 4(e))

Why the obvious alternatives fail:
* Cauchy–Schwarz in s instead of m, then the sextic large sieve (9.1) for Σ_s|Σ_m B_mξ(m)conj χ_s(m)|^2: gives (Q^2/Y')max(1,P_a^{1/3}), worse (the (KD)^{2/3} term is the same phenomenon in dual form).
* Weighted Cauchy–Schwarz / row sieves: the excess is a uniform bias on generic rows (§3(ii)); no weight w_m separates it.
* Changing the row-ball weight Ω so that Ω̂ vanishes at the sixth-power frequencies: impossible, the frequencies a^6eC/L sit at |ξ| ≈ Q^{−1/2}, the resolution limit of the ball, and the period L varies with (s_1,s_2).
* Completing the m-sum: Q = XY is forced by the Poisson duality with the theta row; b > 0 (incompleteness) is exactly what the count side needs.

6.1 **Slot prime in the additive variable (the creative proposal).** The exceptional term for a pair (s_1,s_2) is coherent only through the fixed-modulus phase ρ_e(n); it is killed if the s-coefficient oscillates against every fixed-modulus character. Put one selected prime p ≍ P = Z^{ℓ_s} into s: s = p s', with the compensated-probe weight η(p) (as the marked slots already carry η(p_i), line 6118). Then in (J.1) the inner sum factorises as [Σ_{p≍P} η(p)χ_e(p)ρ(p)W(p)]·[Σ_{s'}…], and η χ_e ρ is a nonprincipal finite-order Hecke character for every e. Under the contradiction hypothesis of Part II (no zero of any finite-order Hecke L-function in Re s > β*) the prime sum is ≪ P^{β*+ε}, so the exceptional term acquires P^{−2(1−β*)} = Z^{−2(1−β*)ℓ_s}, while the diagonal is unchanged (pairs with p_1 = p_2 share C ⊇ p and are complete once P ≥ P_a^{1/2}; by the factorisation g(ps',−m) = conj χ_p(m)g(p)g(s',−m)·R, the pairs with equal slot are the Gram form of the polynomial at scale Y/P with P_a' = P_a/P^2 ≤ 1). Net: (15.4) becomes (Q/Y')(1 + P_a^{1/6}Z^{−2(1−β*)ℓ_s}), i.e. θ_eff = max(0, 1/12 − (1−β*)ℓ_s/b). Caveats: (a) conj χ_p(m) transfers to the row as χ_{Ap^5}(m), i.e. a mark of multiplicity 5 on the theta index, outside the family cn^3 (c squarefree) on which the completed reflection (Sec. 5) and the Euler identities (Sec. 7, 16) are built — the Poisson/high side must be redone; (b) the same primes are used by Prop 19.2 for the nonprincipal counts; a prime in s is not available there, so the two sides compete for ℓ. (c) It uses the zero-free hypothesis for the whole family, i.e. an inductive/bootstrapping structure of the contradiction; the paper's hypothesis already quantifies over the family (β* is the extremal zero), so this is in principle available. This is the only route I found that attacks the loss at its root (the phase ρ_e) rather than at the Cauchy–Schwarz step.

6.2 Bias subtraction (not recommended): write A = A^{bias} + A^{rand} with A^{bias}_m = Y'^{−1/6}τ(m)·Ŵ(5/6) (residue of the twisted Kubota–Patterson series). Then Σ_m τ(m)ξ(m)B_m = Σ_A a_A Σ_{q_m≤Q} τ(m)χ_A(m)ξ(m) is a twisted sum of cubic-theta coefficients by a sextic character of conductor ≍ Z ≫ Q; the trivial estimates (triangle over A, Voronoi in m) give Y'^{−1/6}Q^{1/3}Z^{1/2}, larger than the no-loss target QY'^{−1/2} by Z^{(b+3ℓ)/6}; a saving needs the row coefficients a_A = γ_2(c)α(cn^3)νθ(A) to be orthogonal to the theta coefficients — plausible (the γ_2 are Gauss-sum phases) but it requires uniform Patterson asymptotics in the twist, which are not available with power savings. Record for completeness.

6.3 Two-variable large sieve over (s, m) jointly: the exceptional contribution is the low-frequency (mean-value) component of m ↦ conj χ_{s_1}(m)χ_{s_2}(m) on the ball; a joint sieve would need to separate pairs (s_1,s_2) by q_C ≥ P_a (complete) from q_C < P_a (incomplete) — the incomplete coprime pairs dominate in number (≈ Y'^2) and carry the loss; no gain unless the coefficient on them oscillates, which returns to 6.1.

## 7. Deliverables summary
(a) Mechanism: Prop 15.2 proof, lines 6396-6412 (exceptional frequencies (k) = a_1^6 e, count K_R^{1/6}, trivial two-column count, |L_C| ≤ q_C) → term (Q/Y')P_a^{1/6}; halved by Cauchy–Schwarz at line 6486 → P_a^{1/12} = Z^{b/12}.
(b) Verdict: intrinsic; lower bound (J.2) from k = a^6·C·e_0, C ≍ 1, all terms nonnegative; the Gram operator has a fixed finite number of eigenvalues (Q/Y'^2)P_a^{1/6} whose eigenvectors are the probe's own coefficient vectors.
(c) No improved upper bound exists for Σ|A_m|^2; sharp form in §4.
(d) Boundary at provable θ: 0.874957 (unchanged); θ = 1/24 ⇒ 0.869608; θ = 0 ⇒ 0.863950 (floor-active).
(e) Best idea: slot prime with η(p)-weight in the additive variable, §6.1, θ_eff = max(0, 1/12 − (1−β*)ℓ_s/b); needs the Poisson side rebuilt for marks of multiplicity 5 and competes with Prop 19.2 for the prime supply.

<!-- materialized from workflow result: quasi_rh / map -->
# Quasi-RH (11/12) — proof architecture (materialized)

## Load-bearing steps

1. STRATEGY (plain terms). (1) Littlewood principle, Sec. 3 l.726-757: if A_1(D)=sum_{(n,S)=1} mu(n) nu(n) W(Nn/D) << D^{beta+eps} for every smooth compactly supported W, then the Mellin transform hat-W(s)/L_K^S(s,nu) is holomorphic on Re s>beta. Choosing W(y)=y^{-rho} phi(y) with phi>=0 gives hat-W(rho)=int phi dy/y>0, so there is no zero rho there. This is needed only qualitatively for each nu, with no uniformity in the conductor. Dirichlet L-functions follow by base change. (2) Embed A_1 into A_u(D)=sum mu nu chi_n(u) W, with chi_n(u)=(u/n)_6. Since chi_n(p^6)=1_{p not dividing n}, A_{p^6}=A_1+O(D/Np). (3) Proposition 3.1 gives the mean square sum_{0<Nu<=H}|A_u|^2 << D^{1+eps}H with H=D^{1+theta} (square-root cancellation on average). Averaging over the J ~ Y/log Y rows u=p^6 with Y=H^{1/6} gives |A_1|^2 << D^{1+eps}H/J + D^2/Y^2 = D^{(11+5theta)/6+eps} + D^{(5-theta)/3} (l.711-716). Hence A_1 << D^{11/12+5theta/12+eps}; letting theta -> 0 gives 11/12. So 11/12 = (1+5/6)/2: the 1 is the variance D per row from square-root cancellation, and the 5/6 is the loss from using only H^{1/6} sixth-power rows out of H ~ D rows. (4) H cannot drop to D. Duality sends the rows u to dual rows k with N k <= H_dual ~ D^2/(H B^2), and the iteration needs the gap H_dual <= Sigma D^{-kappa}, where Sigma=XF=D/B (eq:positive-gap); at H=D the gap vanishes. Hence H=D^{1+theta} with kappa=theta/2 (l.1621). Within this extraction 11/12 is optimal, since D H / J >= D^{11/6} once H>=D. The 7/8 paper changes the extraction (sixth-power-free rows u=u_0 a^6, amplification).
2. STRATEGY (proof of the mean square). (a) Poisson summation in u (Lemma 4.2) together with Gauss-Jacobi (Lemma 4.1: mu(n) gamma_{-1}(n) = chi_n(-1) G(n)^{-1} conj(alpha(n)) gamma_2(n), equivalently mu = conj(alpha) gamma_2^3) turns the Moebius sums into the dual family E(H,X,F) of cubic-Gauss-sum sums a_xi(n)=conj(alpha(n)) gamma_2(n) xi(n), twisted by chi_n(k) chi_n(f)^4. The needed bound E << D^eps XF (Prop. 4.5) is an optimal large-sieve bound for sextic characters, valid only for these special coefficients. (b) Cube completion gives T(X;k,f), a twisted sum of Fourier coefficients of conj(theta), Kubota's cubic theta function. The twist becomes a sum of translates to cusps a/c with c=c_0 k_0 (fixed part). At p | k_0 the additive twist coefficient chi_p(h)^{-1} and the conjugated Kubota multiplier chi_p(a)^{-2} combine to chi_p^{-3}=chi_p^3, which is QUADRATIC (l.410, l.1743-1746, l.3252-3253). The dual length is ~N(k_0)^2/X. The quadratic large sieve (GL) then gives Prop. 5.2: sum_k |T|^2 << D^eps (H + H^2 N f/X). (c) Moebius inversion in the cube index (Lemma 5.3) splits at H_c^3=min(X, X^2/H^2). Short divisors are handled by Prop. 5.2; long divisors give E(H, L_b, F) with L_b=X/N(b)^3 against the SAME target Sigma. (d) The transfer (Prop. 5.4) applies Poisson in k (Gauss -> Moebius), enlarges the y-range by positivity to Y_{C,d} ~ Sigma L F/H, then applies Poisson in y (Moebius -> Gauss). The output is E(H',X',F') with H' <= H L/(Sigma F) and H'/Sigma' <= H/Sigma. Since N b > H_c, H' < H (H/Sigma)^2 <= D^{-2 kappa} H. Induction (Prop. 5.1) ends after ceil(C_0/kappa) steps at H<=1. Cancellation is genuinely proved only in Prop. 5.2; every other step is an exact identity, a positivity enlargement, or Cauchy-Schwarz. The angular factor conj(alpha), produced by the d/d(z-bar) derivative, kills every constant term so that T(s,Psi) is entire (l.3344-3369). It is essential: without it the Patterson-bias main terms of size X^{5/6} return (DR Thm 1.1), and DR Thm 1.4 shows that the cubic large sieve is sharp for g~(b) without the angle.
3. D1 [most load-bearing] App. A.2, Kubota multiplier at the twisted cusps, (eq:ray-multiplier) l.3149-3205, and the exponent step l.3252-3253. With kappa(g_1)=kappa_0 (a/r)_3, so that conj(kappa) contains chi_p(a)^{-2}, j=1 gives B_{p,1}=chi_p^3 (quadratic). With the conjugate multiplier, j=1 would give a sextic character, the quadratic large sieve would no longer apply, and Prop. 5.2 would lose its proof. Check: the chain theta coefficients conj(g(1,c)) (DR 5.7) + multiplier (c/a)_3 (DR 5.4) + use of conj(theta) is consistent. The case 3|c ((c_0 r/a)_3=(c_0/a)_3 (a/r)_3) and the j=4 principal factor (consistent with chi_n(f)^4 acting as a frequency shift) both support the sign. The cases v_lambda(c)=1 and (c,lambda)=1 are compressed into l.3184-3196 and are NOT independently verified (U1).
4. D2 Lemma 6.3, uniformity in k_0 (l.1847-1855; proof l.3438-3450; construction l.3039-3230). Lemma 6.6 needs the k_0-dependence of each transformed term to be exactly: the quadratic character chi_{k_0}(.)^3, the factor N(k_0)^2 in the weight argument, and a unimodular scalar. The data (d, psi, c_0, H, kappa_0, delta'_0 mod D_0) must be fixed by k_0 mod M^2, with M=lambda^{12} L^4. Still to check: the v_lambda(c)=1 factor (-u_0/(a-u_0 b_g))_3, and that delta' mod D_0 is fixed by a mod M c_0 and r mod M^2.
5. D3 Lemma 6.6, the analytic core (l.1923-2187). Points: (a) s=t k_0 with every prime of k_0 active and j_p=1 (l.1940-1947, l.2001-2007); (b) (a^2,Y) bookkeeping keeping a^2 Y <= (H_0^2/X) N(t)^2 N(g) (l.2064-2088); (c) j_p=4 re-indexing identity (l.2035-2062); (d) Mellin separation with row-dependent coefficients c_{b,k_0}(s) under a uniform majorant, via Lemma B.3 (l.2111-2147); (e) dyadic and geometric summations (l.2148-2172); (f) index set divisor-bounded in tg (l.2089-2093). We redid (b), (c) and (e) by hand and found them consistent: j_p odd costs q^2, j_p in {0,4} costs q, j_p=2 (which needs v_p(g)>=2) costs q^2; in every case the cost is at most N(p)^{v_p(g)}.
6. D4 Lemma 6.5 and its application at l.2128-2133: the quadratic large sieve over K. The GL hypotheses (Def. 1) vs. the paper's sketch at l.1903-1912: reciprocity C([a],[b]) on classes mod 24 O, primitivity of chi_{k1} chi_{k2} within a common class, and columns meeting S handled by fixing the S-part (U3). Unit-triviality of x -> (x/k)_2 kappa_lambda(x)^{e_k} verified numerically.
7. D5 Prop. 5.2 from Lemma 6.6 (l.2189-2214). Write k=u_0 s v^2. Since chi_n(v^2)=chi_n(v^8) (8=2 mod 6, zero extensions included), T(X;u_0 s v^2,f)=T(X;u_0 s,f v^2). Lemma 6.6 is then applied with row bound H/N(v)^2 and N(g)<=H N(f), and the v-sum gives zeta_K(2). Hand-checked.
8. D6 App. A.2, finite Fourier expansion, active primes and local transform (l.2906-3001, l.3207-3282). (eq:ray-fourier), (eq:ray-local-transform) with the constants omega_{p,j}, and the three shapes of B_{p,j} are NUMERICALLY VERIFIED (7704 cases, 0 failures). The additive CRT (eq:ray-additive-crt) was re-derived by hand: eps_p=-((lambda^3 c/p) sigma_p)^{-1}.
9. D7 Patterson coefficients and the identification T <-> Theta_k (l.362-366; Lemma 6.1 l.1686-1718). Conjugation conventions were checked against the rendered DR (5.7). The cube completion relies on DR (5.8) imposing no (n,b) coprimality; confirmed. phi_k(n b^3)=chi_n(lambda)^2 Psi_k(n) Psi_k(b)^3 uses chi_b(lambda)^6=1 and complete multiplicativity of Psi_k, including the zero extensions.
10. D8 App. A.2, archimedean part (l.3284-3436). Hand-checked: J(s)=(3^{5/2}/4)(27/(2pi)^2)^s Gamma(s+1/3)Gamma(s+2/3) T(s,Psi); i*conj(alpha(lambda^{-3}))=1; dz'/d(z-bar)=-1/(c^2 v^2) at z=0, giving the factor conj(alpha(c))^2 N(c)^{1-2s}; scalar -i/81 with |C|<=1/81; gamma quotient Gamma(7/6+t)Gamma(5/6+t)/(Gamma(7/6-t)Gamma(5/6-t)) at t=1/2-s, first pole at t=-5/6; decay min(x^{1/4},x^{-A}). T(s,Psi) is entire because the derivative kills all constant terms at all cusps (l.3360-3369). Contour-shift justification is sketched (U4).
11. D9 Prop. 4.5, the first duality (l.1024-1252). The paired identity (eq:initial-paired-gauss) is NUMERICALLY VERIFIED. Hand-checked: the bijection (g,e,v,h) <-> (b,f,k) (l.1141-1154), including e=(f,k) <=> (h,v)=1; normalization H N(g)/(D^2 N(e)); hat-Phi argument H N(k)/(N(f)^2 N(m1) N(m2)); final count (H B/D^2) B (XF)^2 = H with XF=D/B. This step creates the gap H_dual/Sigma << D^{-theta} (l.1617-1619).
12. D10 Lemma 5.3, cube inversion (l.1341-1467). Hand-checked: (eq:cube-inverse) (the coefficient of b contains sum_{h|b} mu(h)); the short part, where sum_{N h<=H_c} N(h)^{-1} N(h)^3 ~ H_c^3 needs H_c^3 <= X^2/H^2; the long-part identity Psi_k(b)^3 = xi(b)^3 chi_b(k)^3 1_{(b,f)=1}, with normalization 1/(N(b) sqrt(L_b)). Design point: the long part is bounded by E(H,L_b,F) against the OLD target Sigma=XF.
13. D11 Lemmas 7.1 and 7.3, the transfer (l.2230-2670). Hand-checked: w_{C,d} and the enlargement N(y)<=Y_{C,d}, which uses LF<=Sigma (l.2330-2333); the scale identities (l.2526-2531); the k'-support bound (l.2541-2548); the preimage regrouping sum mu(e)mu(w)=1_{f'|k'} via the per-prime count (1+1_{p|k'})-1_{p|k'}-1_{p not| k'} (l.2550-2568); the closing identity (Sigma R/L^2) R (L/R)^2 = Sigma; the zero frequency w_{C,d} Y_{C,d} ell = c_I Sigma/(N(C)^2 N(t)). (eq:paired-first-gauss) NUMERICALLY VERIFIED.
14. D12 Prop. 5.1 induction (l.1514-1609). Contraction: H' <= H/(N(b)^3 F^2) < H (H/Sigma)^2, using N(b)^3 > H_c^3 = X^2/H^2 when the supremum is nonempty. Children inherit the gap through H'/Sigma' <= H/Sigma. Derivative orders grow J -> 4m+12 per step and the test intervals grow [u,v] -> [u/16,4v] per step; both stay finite over ceil(C_0/kappa) steps. Uniformity in the test U requires the induction hypothesis to hold for every interval with J independent of I (l.1530-1531).
15. D13 Section 3 extraction (l.694-724). The rows p^6 are distinct with norm <= H, the difference count is O(D/Y), and the exponent arithmetic (2+theta)-(1+theta)/6=(11+5theta)/6 checks.
16. D14 Lemma 4.4, removing exclusions (l.962-992), reused in Prop. 4.5 (l.1211-1224) and Lemma 7.3 (l.2623-2640). The shift (X,F) -> (X/N(d), F N(d)) preserves Sigma. The needed lower bound X'/N(j) >= 1 is (eq:child-column-lower-bound).
17. D15 Lemma B.2, row-dependent kernels (l.3566-3615), used three times (Prop. 4.5, Lemma 7.1, Lemma 7.3). Costs C^{2m+4} derivatives per use and needs the kernel support inside the interior of the test interval. All three uses check: [a_0/4,b_0] inside int [a_0/8,2b_0]; I inside int I_*; [u/8,2v] inside int [u/16,4v].
18. SMALLEST STATEMENT WHOSE FAILURE INVALIDATES THE RESULT: Prop. 6.2 + Lemma 6.3, in the form used in Lemma 6.6. For squarefree k_0 coprime to S and P_fix, T(X;u_0 t k_0,g) is a divisor-bounded sum of dual sums in which k_0 enters only through: chi_{k_0}(lambda^4 l)^3; the weight argument N(l) X/(N(c_*)^2 N(k_0)^2); and a scalar of modulus <= 1. All other data are constant on classes of k_0 mod M^2. If this fails, then Prop. 5.2, Lemma 5.3, Prop. 5.1, Prop. 3.1 and Theorem 1.1 all fail.
19. DEPENDENCY GRAPH: Thm 1.1 <= Prop 3.1 [+ Landau, Hecke, base change]; Prop 3.1 <= Prop 4.5 + Prop 5.1; Prop 4.5 <= Lem 4.2, Lem 4.1, Lem 4.4, Lem B.2; Prop 5.1 <= Lem 5.3 + Prop 5.4 + induction; Lem 5.3 <= Prop 5.2; Prop 5.2 <= Lem 6.6; Lem 6.6 <= Prop 6.2, Lem 6.3, Lem 6.4, Lem 6.5, Lem 4.1(recip), Lem B.1, Lem B.3; Prop 6.2/Lem 6.3/Lem 6.4 <= App A.2 <= Lem 6.1 + DR Sec. 5.1 + Patterson Thm 8.1/Tables + cubic reciprocity; Lem 6.5 <= GL Thm 1.1; Prop 5.4 <= Lem 7.1 + Lem 7.3; Lem 7.1 <= Lem 4.2, Lem 4.1, Lem B.2; Lem 7.3 <= Lem 7.2, Lem 4.4, Lem B.2; Lem 7.2 <= Lem 4.2, Lem 4.1; Lem 4.4 <= Lem 4.1(crt-a); Lem 4.1 <= App A.1; Lem B.2 <= Lem B.1. There is no circularity: Prop 5.4 is relative to a supremum at strictly smaller row range, and Prop 5.1 closes it by finite induction.
20. SCALES (first step, B=F=1): columns N n ~ D; rows N u <= H=D^{1+theta}; extraction rows N p <= H^{1/6}; dual rows H_dual ~ D^2/(H B^2) = D^{1-theta}; X=D/(BF), Sigma=XF=D/B, H_dual/Sigma ~ D^{-theta}/B; H_c ~ D^{2theta/3}; L_b=X/N(b)^3 in (1, X/H_c^3]; theta dual length ~ N(c_*)^2 N(k_0)^2/X; transfer intermediate Y_{C,d}=c_I Sigma L F N(d)/(H N(C)^2); transfer output H'=H L/(Sigma F R^2), Sigma'=L/R; at most ceil(4/theta) recursion steps.
21. FINDINGS CLASSIFICATION: verified_error: none. suspected_gap: none with a witness. unresolved_ambiguity: U1 l.3175-3196, multiplier cases v_lambda(c)=1 and (c,lambda)=1 asserted, not displayed (for (c,lambda)=1 we reconstructed c_1=-delta', a_1=-b_g, giving kappa=(a/c)_3 as claimed, PROVIDED the asserted unit and supplement evaluation holds); U2 l.3102-3113, identification of gamma_+- with DR's gamma_19, gamma_10 and the phases in t_+- (only support and size are used downstream); U3 l.1900-1913, GL Def. 1 verified only in outline; U4 l.3395-3411, contour-shift justification sketched (standard). typo_or_presentation: P1, an auditor pitfall rather than a paper defect: pdftotext drops the overline in DR (5.7), which creates a false conjugation mismatch; check the rendered page. P2: the restriction theta<=1/10 is never used. P3: label names lem:reflection and thm:ms do not match their environments (Proposition). P4: Lemma 4.1's hypothesis line omits that (crt-a) needs a,b squarefree; this is supplied at l.854. P5: Corollary 1.2 and the arithmetic applications (l.97-125) are unproved in the paper and not load-bearing. no_issue_found_in_inspected_portion: the steps recorded as checked in D3(b,c,e), D5-D15.
22. NUMERICAL CHECKS (our own code, nothing from the OpenAI repository; scripts at /home/user/riemann/research/exploratory/riemann-observatory/audits/quasi_rh/architecture_checks/, run with python3 -I): zomega.py (Z[omega] arithmetic, sextic symbol via x^{(q-1)/6}, the paper's e(z), gamma_j); check_lemma41.py ((gj),(g),(convert1),(convert2) for 44 primary primes with N<=200, split and inert; (crt-a) and composite cases for 91 two-prime products) 0 failures; check_recip.py (R in {+-1}, a function of classes mod 4; R=Gq(ab)/(Gq(a)Gq(b)); closed form Gq(a+b omega)=(1+i^{-b}+i^a+i^{b-a})/2 equals gamma_3; G=conj(chi(4)) Gq is a class function mod 4; G(ab)=G(a)G(b)R; R(c,c)=chi_c(-1); quotient identity on 300 pairs) 0 failures; check_paired.py ((initial-paired-gauss) with nu=1 and (paired-first-gauss), Gauss sum of conj(chi_{z1}) chi_{z2} mod z1 z2 computed directly, 92 pairs; Lemma 4.2 finite Fourier identity) 0 failures; check_local.py ((ray-fourier) and (ray-local-transform): 14 primes including inert, j=0..5, random sigma_p, eps_p, all x mod p, 7704 cases) 0 failures; check_gl_family.py (unit-triviality of the GL family, 468 cases) 0 failures. These checks confirm only the finite arithmetic layer. They do not test the multiplier case analysis, the cusp data, or the Kubota automorphy itself. The Lean formalization of the companion 7/8 theorem was NOT replayed.

## Imported results

- E1 Landau prime ideal theorem [Lan03], [IK04 Thm 5.33]. Form used (l.706-708): #{p not in S: Y/2<N p<=Y} is about Y/log Y for the fixed field K. Standard; OK.
- E2 Hecke meromorphic continuation [Hec20], [IK04 Sec. 5.10]. Form used (l.752-757): the identity L_K^S(s,nu) M_W(s) = hat-W(s) continues to Re s>11/12. Standard; the pole of the trivial character at s=1 is harmless.
- E3 Base change L_K(s,chi o N)=L(s,chi)L(s,chi chi_{-3}) up to Euler factors nonzero in Re s>0 (uncited), with Dirichlet's L(1,chi_{-3})>0 [Dav00 Ch. 4, 6] (l.759-770). Standard.
- E4 Explicit formula [Dav00 Ch. 19-20]. Used only for Theorem 1.1 => Corollary 1.2 (l.82-95); no proof in the paper; not load-bearing.
- E5 Lattice Poisson summation [IK04 Thm 4.5] and the primitive Gauss sum evaluation [IK04 (3.12)], used in Lemma 4.2 (l.875-932). The additive character is e(z)=exp(4 pi i Im z/sqrt3)=exp(2 pi i Tr(z/sqrt(-3))), under which O is self-dual; covolume factor 2/sqrt3. Normalization re-derived by hand; the finite Fourier identity was verified numerically.
- E6 Gauss-Jacobi identity [IK04 (3.18)]; Hasse [Has50 pp. 443-445]; Heath-Brown [HB00 (2)]. Form used: J(A,B)=g(A)g(B)/g(AB); J(chi_p^2,chi_p^2)=-p; gamma_2(n)^3=mu(n)alpha(n), i.e. mu(n)=conj(alpha(n)) gamma_2(n)^3. Re-derived in App. A.1 (l.2692-2772). Consistent with DR (1.8)/(2.2), since gamma_2(n)=(lambda/n)_3 g~_DR(n). All of Lemma 4.1 verified numerically.
- E7 Cubic reciprocity (a/b)_3=(b/a)_3 for a,b=1 mod 3, and the supplementary laws for omega and lambda [DR (1.4)-(1.5)]. Used at l.2780, l.2931-2933 and l.3184-3196. The uses inside (eq:ray-multiplier) for the cases v_lambda(c)=1 and (c,lambda)=1 were NOT verified case by case.
- E8 Kubota's cubic theta function theta [Kub69], [Pat77 Sec. 2], with the multiplier as in DR (5.2)-(5.4). Form used (l.3089-3092, l.3150-3156): theta(g_1 w)=kappa(g_1) theta(w) for g_1 = I mod 3, with kappa(g_1)=(c_1/a_1)_3; theta is invariant under SL_2(Z) and under translations by Z+3O. Matches DR (5.4) as printed (chi(gamma)=(c/a)_3 on Gamma_1(3), trivial on SL_2(Z)). This sign convention is what makes B_{p,1}=chi_p^3 quadratic.
- E9 Patterson's coefficient formula [Pat77 Thm 8.1] as in DR (5.6)-(5.8). Form used (eq:intro-theta-coefficients) l.364-366: the coefficient of conj(theta) at lambda^{-3} n b^3 is 3^{5/2}|b| conj(chi_n(lambda)^2) gamma_2(n), for primary n,b with n squarefree and NO coprimality condition between n and b. CHECKED against the rendered DR p.17, which reads tau(+-lambda^{3n-3}cd^3)=conj(g(1,c))|d/c|3^{n/2+5/2}, with (5.8): c,d=1 mod 3, mu^2(c)=1, no coprimality. Since gamma_2(n)=(lambda/n)_3 g(1,n)/|n| and the conj(theta)-coefficient at l is conj(tau(-l))=conj(tau(l)) (tau is even), the paper's formula follows exactly. Pitfall: pdftotext drops the overline in DR (5.7).
- E10 Cusp expansions at gamma_+-=(1 0; omega^{+-1} 1) [Pat77 Table II, Table III, (8.8)-(8.9)]; DR (5.9)-(5.15) and App. A. Form used (l.3102-3142, Lemma 6.4): t_0=tau, t_-(l)=omega^2 tau_1(omega^2 l) e~(l), t_+(l)=omega tau_2(omega l) e~(l); support l=u lambda^m n b^3 with m>=-4; |d(l)|<=27*3^{m/6}|b|. Magnitudes checked against DR (5.7), (5.13) and (5.14). The identification with DR's gamma_10, gamma_19 and the phases was NOT verified; only the support and size bounds are used downstream.
- E11 Dunn-Radziwill level-aspect Voronoi method [DR Sec. 5, App. A, Cor. 5.1, Prop. 5.1-5.3, (8.2)] and Yoshimoto [Yos87]. Template for App. A.2. The paper extends it to (h_0,L)!=1 (l.3033-3036) and to several active primes at once; this extension is new work and must be audited as such.
- E12 DLMF 10.43.19. Form used (l.3321-3323): int_0^inf v^{2s} K_{1/3}(4 pi |l| v) dv = 2^{2s-1} Gamma(s+1/3) Gamma(s+2/3) (4 pi |l|)^{-2s-1}. Checked by hand (mu=2s+1).
- E13 Stirling [IK04 Sec. 5.A.4] and Phragmen-Lindelof [IK04 Thm 5.53]. Used for polynomial growth of T(s,Psi) in vertical strips, which justifies the contour shift (l.3395-3411). Standard; only finiteness for each fixed Psi is needed.
- E14 Goldmakher-Louvel [GL Thm 1.1, Cor. 1.2, Def. 1, Sec. 2] (arXiv:1112.1642v2). GL Thm 1.1 verbatim: for a quadratic Hecke family {chi_a} with respect to an ideal c, sum*_{Na<=M} |sum*_{Nb<=N} lambda_b chi_b(a)|^2 << (MN)^eps (M+N) sum* |lambda_b|^2, with sums over squarefree ideals coprime to c. Def. 1 requires: primitive Hecke characters of trivial infinite type; reciprocity chi_a(b)=chi_b(a)C([a],[b]); chi_a chi_b primitive mod ab when [a]=[b]. Used as Lemma 6.5 with the family x -> (x/k)_2 kappa_lambda(x)^{e_k}. The paper's verification (l.1903-1912) is a sketch. We verified numerically that the family is trivial on units, and that the quadratic reciprocity factor depends only on classes mod 4. Row/column transposition is harmless by reciprocity.
- E15 Heath-Brown's admissible-exponent method [HB95 Lemma 8-9, Sec. 8], [HB00 Lemma 9], [GL Thm 4.1, Lemma 4.4], [BGL Sec. 3.2]. Methodological model only (l.612-617, l.655-658); not used as a black box.
- E16 NOT USED: Heath-Brown's cubic large sieve [HB00 Thm 2] and the BGL n-th order large sieve [BGL Thm 1.3]. Mentioned only for contrast (l.412); the 11/12 proof imports no cubic or sextic large sieve. Context: DR Thm 1.4 (under GRH) shows the cubic large sieve is sharp, with extremal coefficients g~(b) WITHOUT the angle conj(alpha). The paper's coefficients carry conj(alpha(n)), which makes T(s,Psi) entire (l.3344-3369); this factor is therefore load-bearing.
- E17 [PY19 Sec. 10.1], [PY20], [KLMS20], [FLN10], [OpenAI26] (7/8 paper): terminology and side references only; not load-bearing. Follow-ups Liu arXiv:2610.26835v2 (extends the 7/8 argument; boundary 0.87489..., general number fields) and Ji arXiv:2611.16665v2 (different route via quartic Gauss sums over Q(i) plus zero density; boundary 599/600) do not identify any error in the 11/12 paper. Both are unrefereed.

## Numbered statements and dependencies

- **Theorem 1.1 [thm:main]** (line 73, theorem): \begin{theorem}\label{thm:main}
Every finite-order Hecke $L$-function over $K$ has no zeros in the half-plane $\Rea s>11/12$. Thus every Dirichlet $L$-function, including $\zeta(s)$, has no zeros for $\Rea s>11/12$.
\end{theorem} — depends on: Proposition 3.1 [thm:ms] via the Section 3 proof (l.694-771): rows u=p^6, (eq:prime-extract) l.711-716, (eq:mobius-saving) l.722-724, Mellin argument l.726-757, EXT: Landau prime ideal theorem [Lan03], [IK04, Thm 5.33] (l.706-708), EXT: Hecke meromorphic continuation [Hec20], [IK04, Sec. 5.10] (l.752-755), EXT: quadratic base change L_K(s,chi o N)=L(s,chi)L(s,chi chi_{-3}) up to Euler factors (uncited, l.761-766), EXT: Dirichlet's L(1,chi_{-3})>0 [Dav00, Ch. 4, 6] (l.768-770)
- **Corollary 1.2 [cor:primes-ap]** (line 84, corollary): \begin{corollary}\label{cor:primes-ap}
Let $\pi(x;q,a)$ count the primes $p\le x$ with $p\equiv a\pmod q$.
Write $\varphi$ for Euler's totient function.
For $x\ge2$,
\[
 \sup_{\substack{1\le q\le x\\(a,q)=1}}
 \biggl|\pi(x;q,a)-\frac1{\varphi(q)}
                  \int_2^x\frac{\dd t}{\log t}\biggr|
 \ll x^{11/12}\log x,
\]
where the implied constant is absolute and effective.
\end{corollary} — depends on: Theorem 1.1, EXT: standard explicit-formula argument [Dav00, Ch. 19-20] (no proof given in the paper; not load-bearing)
- **Proposition 3.1 [thm:ms]** (line 679, proposition): \begin{proposition}\label{thm:ms}
For every fixed $0<\vartheta\le1/10$ and $\varepsilon>0$, there exists an integer $k=k(\vartheta,\varepsilon)\ge1$
such that, for every compact interval $I\subset(0,\infty)$,
all smooth $W$ supported in $I$, and $D\ge2$,
\begin{equation}\label{eq:ms}
 \sum_{0<\NK(u)\le D^{1+\vartheta}}|A_u(D)|^2
       \ll_{\nu,S,I,\vartheta,\varepsilon}
       \Bigl(\max_{0\le j\le k}\|W^{(j)}\|_\infty\Bigr)^2
       D^{2+\vartheta+\varepsilon}.
\end{equation}
\end{proposition} — depends on: Proposition 4.5 [prop:poisson-reduction], Proposition 5.1 [prop:canonical] with kappa=vartheta/2, C_0=2 (Sec. 5.4, l.1613-1629), trivial counting for X<1, H<1 and bounded D (l.1622-1628)
- **Lemma 4.1 [lem:arithmetic]** (line 823, lemma): \begin{lemma}\label{lem:arithmetic}
On a fixed ray class group, there are a function $G$ with values in
$\{z\in\mathbb C:|z|=1\}$ and a symmetric $\{\pm1\}$-valued
bicharacter $\mathcal R$. This means that $\mathcal R(a,b)=\mathcal R(b,a)$ and $\mathcal R$ is
multiplicative in each argument separately:
\[
 \begin{aligned}
 \mathcal R(aa',b)&=\mathcal R(a,b)\mathcal R(a',b),\\
 \mathcal R(a,bb')&=\mathcal R(a,b)\mathcal R(a,b'),
 \end{aligned}
\]
for all classes $a,a',b,b'$ in the ray class group.
These functions have the following properties.
Let $a,b,n$ be primary elements prime to $S$, with $(a,b)=1$ and
$n$ squarefree. Then
\begin{align}
 \chi_b(a)&=\mathcal R(a,b)\chi_a(b),&
 G(ab)&=G(a)G(b)\mathcal R(a,b),                                      \label{eq:recip}\\
 \gamma_2(n)^3&=\mu(n)\alpha(n),&
 \gamma_1(n)\gamma_2(n)&=\mu(n)\alpha(n)G(n),                 \label{eq:gj}\\
 G(n)&=\overline{\chi_n(4)}\gamma_3(n),&
 \gamma_1(n)\gamma_{-1}(n)&=\chi_n(-1).                     \label{eq:g}
\end{align}
Consequently
\begin{align}
 \overline{\alpha(n)}\gamma_2(n)\gamma_1(n)&=\mu(n)G(n),\label{eq:convert1}\\
 \mu(n)\gamma_{-1}(n)
 &=\chi_n(-1)G(n)^{-1}\overline{\alpha(n)}\gamma_2(n),\label{eq:convert2}\\
 a_\xi(ab)&=a_\xi(a)a_\xi(b)\chi_b(a)^4,                     \label{eq:crt-a}\\
 \chi_a(-1)\overline{G(a)}G(b)\mathcal R(a,b)&=G(ba^{-1}).            \label{eq:quotient}
\end{align}
In \eqref{eq:crt-a}, $a,b$ are also squarefree.
The identity for $G(ab)$ in \eqref{eq:recip} extends to all classes of the fixed ray class
group; the quotient in \eqref{eq:quotient} is taken in that group.
\end{lemma} — depends on: App. A.1 proof (l.2691-2872): prime case of (eq:gj) l.2692-2772 including J(chi_p^2,chi_p^2)=-p; (eq:crt-a) l.2773-2782; (eq:recip) and G via quadratic Gauss sums l.2784-2851; (eq:quotient) l.2853-2862, EXT: Gauss-Jacobi identity [IK04, (3.18)], EXT: g(chi)g(bar chi)=chi(-1)N(p), EXT: cubic reciprocity (a/b)_3=(b/a)_3 for primary a,b; Hasse [Has50, pp. 443-445], [HB00, (2)], self-contained Poisson evaluation of the quadratic Gauss sum (l.2788-2813), CRT, NUMERICALLY VERIFIED by us: all identities, 44 primes of norm <=200 (split and inert), 91 two-prime composites, 300 quotient pairs; 0 failures
- **Lemma 4.2 [lem:poisson]** (line 875, lemma): \begin{lemma}\label{lem:poisson}
Let $\mathcal H>0$, let $\mathfrak r$ be a nonzero ideal, and let
$\Phi(\NK(k)/\mathcal H)$ be a smooth radial Schwartz weight
on the row lattice. Let $\chi$ be a primitive multiplicative character
of $(\OO/\mathfrak m)^\times$, viewed as a function on $\OO$ by
reduction modulo $\mathfrak m$ and extension by zero on nonunits.
Write 
\[
\gamma(\chi)=\NK(\mathfrak m)^{-1/2}
\sum_{x\bmod\mathfrak m}\chi(x)e(x/\mathfrak m)
\]
for its normalized Gauss sum.
Since $\chi$ is primitive, its modulus $\mathfrak m$ is determined by $\chi$ and is suppressed in the notation. Then
\begin{equation}\label{eq:poisson}
 \begin{aligned}
 &\sum_k\chi(k)\ind_{(k,\mathfrak r)=1}\Phi(\NK(k)/\mathcal{H})\\
 &\quad=\frac{\mathcal{H}\gamma(\chi)}{\sqrt{\NK(\mathfrak m)}}
   \sum_{d\mid\rad \mathfrak r}\frac{\mu(d)\chi(d)}{\NK(d)}
   \sum_h\overline{\chi(h)}
        \widehat\Phi\!\Bigl(\frac{\mathcal{H}\NK(h)}{\NK(d)\NK(\mathfrak m)}\Bigr).
 \end{aligned}
\end{equation}
Here $\widehat\Phi$ is defined by
\[
 \widehat\Phi(|w|^2)=\frac2{\sqrt3}\int_{\mathbb C}
       \Phi(|z|^2)e(-zw)\,dx\,dy,\qquad z=x+\mathrm i y.
\]
The measure is normalized so that $\OO$ has covolume one.
Here $k,h\in\OO$, and $h$ is the Fourier frequency. We have
\[
 \chi\text{ nonprincipal}\quad\Longrightarrow\quad
 \overline{\chi(0)}=0.
\]
For the principal primitive character ($\chi=\mathbf1$, $\mathfrak m=1$),
the zero-frequency contribution is
\[
 \mathcal H\widehat\Phi(0)
   \prod_{\mathfrak p\mid \mathfrak r}\Bigl(1-\frac1{\NK(\mathfrak p)}\Bigr).
\]
\end{lemma} — depends on: EXT: lattice Poisson summation [IK04, Thm 4.5], EXT: primitive Gauss sum evaluation [IK04, (3.12)], self-duality of O under e(zw)=exp(2 pi i Tr(zw/sqrt(-3))), covolume sqrt(3)/2 (hand-checked), NUMERICALLY VERIFIED by us: finite Fourier identity sum_x chi(x)e(xh/m)=sqrt(N m) gamma(chi) conj(chi(h)) for composite moduli
- **Definition 4.3 [eq:energy] (dual mean square)** (line 938, definition): \begin{definition}
The parameters $\mathcal H$, $X$, and $F$ are the norm scales of
$k$, $n$, and $f$, respectively. Here $k$ ranges over elements of
$\OO$, and a star restricts a sum to squarefree ideals prime to $S$,
represented by their primary generators. For a smooth compactly
supported weight $W$ on $(0,\infty)$, define the \emph{dual mean square} by
\begin{equation}\label{eq:energy}
 \begin{aligned}
 &\E(\mathcal{H},X,F;\xi,W)\\
 &\qquad=\frac1{XF}
 \sum_{\substack{F\le\NK(f)<2F\\(f,S)=1}}^*\sum_{0<\NK(k)\le \mathcal{H}}
 \Bigl|\sum_{(n,S)=1}^*a_\xi(n)\chi_n(k)\chi_n(f)^4
                  W(\NK(n)/X)\Bigr|^2.
 \end{aligned}
\end{equation}
\end{definition} — depends on: a_xi(n)=conj(alpha(n)) gamma_2(n) xi(n) (l.807); E_r = same with (n,r)=1 (l.958-960)
- **Lemma 4.4 [lem:remove-exclusions]** (line 962, lemma): \begin{lemma}\label{lem:remove-exclusions}
Let $r_0$ be the product of the primes dividing $\mathfrak r$ outside
$S$. For $\mathcal H,X>0$, $F\ge1$, and smooth compactly supported $W$,
\begin{equation}\label{eq:remove-exclusions}
 \E_{\mathfrak r}(\mathcal H,X,F;\xi,W)
 \le\tau_{\mathrm{div}}(r_0)
 \sum_{d\mid r_0}\E\!\Bigl(\mathcal H,\frac X{\NK(d)},F\NK(d);\xi,W\Bigr).
\end{equation}
\end{lemma} — depends on: Lemma 4.1 (eq:crt-a), Cauchy-Schwarz in d; injectivity of f -> df onto squarefree f' with F N(d) <= N(f') < 2F N(d) (proof l.971-992, hand-checked)
- **Proposition 4.5 [prop:poisson-reduction]** (line 1000, proposition): \begin{proposition}\label{prop:poisson-reduction}
Fix $0<\vartheta\le1/10$ and put $H=D^{1+\vartheta}$.
For each fixed $C\ge1$ and all real $B,F\ge1$, consider the ranges
\begin{equation}\label{eq:initial-scales}
 X=\frac D{BF},\qquad 0<\mathcal{H}\le\frac{CD^2}{HB^2},\qquad
 XF=\frac DB.
\end{equation}
Suppose that for every $\varepsilon>0$ there exists an integer
$J=J(\vartheta,\varepsilon)\ge1$ such that, for every compact interval
$I\subset(0,\infty)$ and every smooth $W$ supported in $I$,
\begin{equation}\label{eq:auxiliary-target}
 \E(\mathcal H,X,F;\xi,W)
 \ll_{\nu,S,I,C,\vartheta,\varepsilon}\|W\|_{C^J(I)}^2D^\varepsilon XF,
\end{equation}
where
\[
 \|W\|_{C^J(I)}=\max_{0\le j\le J}\sup_{x\in I}|W^{(j)}(x)|.
\]
For functions of several variables, the norm uses all partial derivatives
of total order at most $J$.
Then the original mean-square
estimate in Proposition~\ref{thm:ms} holds.
\end{proposition} — depends on: Lemma 4.2 (Poisson in the row u, exclusion g), Lemma 4.1 (eq:convert2), (eq:quotient), (eq:crt-a) -> (eq:initial-paired-gauss) l.1067-1070 [NUMERICALLY VERIFIED by us with nu trivial, 92 pairs], Lemma 4.4, Lemma B.2 (row-dependent kernel K_{b,f,k}, cost C^{2J+4}), existence of nonnegative radial Schwartz Phi>=1 on [0,1] with supp hat-Phi compact (l.1025-1027, l.1470-1474), hypothesis (eq:auxiliary-target) is supplied by Proposition 5.1
- **Proposition 5.1 [prop:canonical]** (line 1261, proposition): \begin{proposition}\label{prop:canonical}
Fix $\kappa>0$ and $C_0\ge1$. Suppose that
\begin{equation}\label{eq:positive-gap}
 \mathcal H,X,F\ge1,\qquad
 \Sigma=XF\le D^{C_0},\qquad
 \mathcal H\le\Sigma D^{-\kappa}.
\end{equation}
For every $\varepsilon>0$ there is an integer
$J=J(\kappa,C_0,\varepsilon)\ge1$ such that
\begin{equation}\label{eq:canonical-bound}
 \E(\mathcal H,X,F;\xi,W)
 \ll_{I,\nu,S,\kappa,C_0,\varepsilon}
 \|W\|_{C^J(I)}^2D^\varepsilon\Sigma
\end{equation}
for every compact interval $I\subset(0,\infty)$ and smooth $W$ supported
in $I$.
\end{proposition} — depends on: Lemma 5.3 [lem:cube-reduction], Proposition 5.4 [prop:transfer], induction on j with H <= D^{j kappa}; base case H<=1 by counting (proof l.1516-1609); contraction H' < H (H/Sigma)^2 <= D^{-2 kappa} H (l.1565-1577)
- **Proposition 5.2 [prop:R] (completed mean-square estimate)** (line 1317, proposition): \begin{proposition}\label{prop:R}
Fix $\varepsilon>0$, $C_0\ge1$, and a character $\xi$ of the fixed ray
class group. There is $J=J(\varepsilon,C_0)\ge1$ such that
\begin{equation}\label{eq:R}
 \sum_{0<\NK(k)\ll\mathcal H}|T(X;k,f)|^2
 \ll_{I,\xi,S,\varepsilon,C_0}
 D^\varepsilon\|W\|_{C^J(I)}^2
 \Bigl(\mathcal H+\frac{\mathcal H^2\NK(f)}{X}\Bigr)
\end{equation}
whenever
\[
 1\le\mathcal H,X,\NK(f)\le D^{C_0}.
\]
Here $f$ is squarefree and primary with $(f,S)=1$,
$W$ is smooth and supported in a compact interval $I\subset(0,\infty)$,
and $T$ is defined by \eqref{eq:completed-twist}.
\end{proposition} — depends on: Lemma 6.6 applied with k=u_0 s v^2, g=f v^2, row bound H/N(v)^2, exponent range 2C_0 (proof l.2189-2214; chi_n(v^2)=chi_n(v^8) since 8=2 mod 6), zeta_K(2)<infinity
- **Lemma 5.3 [lem:cube-reduction]** (line 1341, lemma): \begin{lemma}\label{lem:cube-reduction}
Fix $C_0\ge1$ and $\varepsilon>0$. Suppose
$1\le\mathcal H,X,F\le D^{C_0}$ and $\mathcal H\le\Sigma=XF$.
There is an integer $J=J(\varepsilon,C_0)\ge1$ such that
\begin{equation}\label{eq:cube-reduction}
 \E(\mathcal H,X,F;\xi,W)
 \ll_{I,\nu,S,C_0,\varepsilon}D^\varepsilon
 \biggl(\Sigma\|W\|_{C^J(I)}^2+
 \sup_{\substack{b\equiv1\ (3),\ (b,S)=1\\
                  \NK(b)>H_c,\ L_b>1}}
       \E(\mathcal H,L_b,F;\xi,W)\biggr)
\end{equation}
for every compact interval $I\subset(0,\infty)$ and
$W\in C_c^\infty(I)$. An empty supremum is zero; in particular it
is empty when $\mathcal H^2\le X$.
\end{lemma} — depends on: definition (eq:T) of the completed sum T(X;Psi) (l.1287-1293) and (eq:completed-twist) (l.1304-1308), Moebius inversion over the cube index (eq:cube-inverse) l.1361-1369 [IK04 (1.18)], [DR (8.2)], cutoff (eq:cube-cutoff) H_c^3=min(X, X^2/H^2) (l.1336-1339), Proposition 5.2 (short part, l.1391-1406), divisor-sum bound sum_{N(b)<=R} tau(b)/N(b) << log^2(2R) (l.1449-1455)
- **Proposition 5.4 [prop:transfer]** (line 1487, proposition): \begin{proposition}\label{prop:transfer}
Assume $1\le\mathcal H,L,F,\Sigma\le D^{C_0}$ and
$\max\{\mathcal H,LF\}\le\Sigma$, for fixed $C_0\ge1$.
For every integer $m\ge0$ and $\varepsilon>0$,
\begin{equation}\label{eq:transfer-summary}
 \mathcal A(W)\ll D^\varepsilon\Sigma\|W\|_{C^{4m+12}(I)}^2
 \Bigl(1+\sup\frac{\E(\mathcal H',X',F';\xi',U)}{\Sigma'}\Bigr)
\end{equation}
where the supremum is over the family \eqref{eq:energy}, with
$\Sigma'=X'F'$, $\mathcal H',X',F'\ge1$, and
\begin{equation}\label{eq:transfer-scales}
 \mathcal H'\le\frac{\mathcal HL}{\Sigma F},\qquad
 \frac{\mathcal H'}{\Sigma'}\le
 \frac{\mathcal H}{\Sigma},\qquad
 \Sigma'\le L.
\end{equation}
For $I=[u,v]$, the tests satisfy
$U\in C_c^\infty(I')$, $I'=[u/16,4v]$, and
$\|U\|_{C^m(I')}\le1$; an empty supremum is zero.
The estimate holds for every compact $I\subset(0,\infty)$ and
$W\in C_c^\infty(I)$, with implied constant depending on
$m,C_0,\varepsilon,I,\nu,S$ and the fixed ray class group.
\end{proposition} — depends on: Lemma 7.1 [lem:first-transfer] (with j=2m+4), Lemma 7.3 [lem:second-transfer] (proof of Prop. 5.4 at l.2672-2683), smoothed energy A(W) of (eq:smoothed-energy) l.1476-1483, with E <= A(W)
- **Lemma 6.1 [lem:theta-realization]** (line 1686, lemma): \begin{lemma}\label{lem:theta-realization}
With these definitions,
\begin{equation}\label{eq:T-theta}
 T(X;k,f)=\frac1{3^{5/2}\sqrt X}
 \sum_{\substack{n,b\in\OO\\n,b\equiv1\ (3)\\n\ {\rm squarefree}\\(nb,S)=1}}
 c_\theta(nb^3)\phi_k(nb^3)\overline{\alpha(nb^3)}
 W\!\Bigl(\frac{\NK(nb^3)}X\Bigr).
\end{equation}
Moreover,
\begin{equation}\label{eq:theta-twist-translates}
 \Theta_k(z,v)=\sum_{h\in\OO/(q)}\widehat\phi_k(h)
       \overline{\theta(z+\lambda^2h/q,v)}.
\end{equation}
\end{lemma} — depends on: EXT: Patterson's coefficient formula (eq:intro-theta-coefficients) l.364-366, c_theta(nb^3)=3^{5/2}|b| conj(chi_n(lambda)^2) gamma_2(n) [Pat77, Thm 8.1], [DR (5.6)-(5.8)] -- CHECKED by us against the rendered DR p.17: tau(+-lambda^{3n-3}cd^3)=conj(g(1,c))|d/c|3^{n/2+5/2}, no coprimality of c,d; consistent, definitions of theta (eq:cubic-theta-definition) l.1650-1655, phi_k and Theta_k (eq:twisted-theta-definition) l.1661-1678, finite Fourier inversion; phi_k(0)=0 cancels constant terms
- **Proposition 6.2 [lem:reflection] (twisted theta transformation)** (line 1805, proposition): \begin{proposition}\label{lem:reflection}
The quantity $T(X;\Psi)$ defined in \eqref{eq:T} is a sum of $O_{\Psi_0,S}(2^{|\mathcal P|})$ terms of the form
\begin{equation}\label{eq:reflection}
 C\sum_{0\ne\ell\in\lambda^{-4}\OO}
 \frac{d(\ell)\alpha(\ell)}{\sqrt{\NK(\ell)}}\,
 \psi(\lambda^4\ell)
 \prod_{p\in\mathcal A}B_{p,j_p}(\lambda^4\ell)
 V_*^\sharp\!\Bigl(\frac{\NK(\ell) X}{\NK(c)^2}\Bigr).
\end{equation}


Here $\mathcal A$ and $c$ are as above, and $|C|\ll_{\Psi_0,S}1$.
The triples $(d,\psi,c_0)$ belong to a fixed finite family depending
only on $\Psi_0,S$, where $d\in\{d_0,d_+,d_-\}$,
$c_0\in\OO\setminus\{0\}$, and $\psi$ is a unit-modulus additive
character on $\OO$.
\end{proposition} — depends on: App. A.2 proof l.2904-3479: finite Fourier expansion (eq:ray-fourier) l.2992-3001; reduced denominators c=c_0 r l.3003-3025; cusp choice H, g=g_1 H l.3027-3101; cusp coefficients (eq:cusp-fourier-coefficients) l.3104-3142; Kubota multiplier (eq:ray-multiplier) l.3149-3205; additive CRT (eq:ray-additive-crt) l.3207-3230; local transform (eq:ray-local-transform) l.3231-3282; archimedean part l.3284-3436, Lemma 6.1, local factors B_{p,j} (eq:theta-local-factors) l.1735-1742; weight V_*^sharp (eq:theta-weight) l.1752-1758, EXT: theta automorphic on Gamma_2=SL_2(Z)Gamma_1(3) with multiplier (c/a)_3 [Kub69], [Pat77 Sec. 2], [DR (5.2)-(5.4)], EXT: DR (5.7)-(5.8), (5.9)-(5.15), (5.13)-(5.14), App. A; [Pat77, Thm 8.1, Tables II-III], EXT: cubic reciprocity + supplements [DR (1.4)-(1.5)], EXT: DLMF 10.43.19; Stirling [IK04 Sec. 5.A.4]; Phragmen-Lindelof [IK04 Thm 5.53], NUMERICALLY VERIFIED by us: (eq:ray-fourier) and (eq:ray-local-transform), 7704 cases, 0 failures; multiplier case analysis NOT verified
- **Lemma 6.3 [lem:reflection-uniformity] (uniformity in the twist)** (line 1847, lemma): \begin{lemma}[Uniformity in the twist]\label{lem:reflection-uniformity}
For the family $\Psi_{k_0}$ above, the summands in
Proposition~\ref{lem:reflection} may be indexed by
$(h,\mathcal A_{\rm fix})$, with $h$ in a fixed finite set depending
only on $\Psi_0,S$. Zero scalar coefficients are permitted.
For each fixed index, the triple $(d,\psi,c_0)$ depends on $k_0$
only through its ray class modulo a fixed ideal supported on $S$
and depending only on $\Psi_0,S$.
\end{lemma} — depends on: App. A.2 l.3438-3450, construction in A.2 of M=lambda^{12}L^4, delta', kappa_0, psi, H (l.3039-3230): all fixed by h_0, the active set and r mod M^2, family Psi_{k_0} (l.1826-1844): every p | k_0 has j_p=1 and is active
- **Lemma 6.4 [lem:theta-bounds]** (line 1859, lemma): \begin{lemma}\label{lem:theta-bounds}
For each $d\in\{d_0,d_+,d_-\}$, the coefficient $d(\ell)$
vanishes unless $\ell$ can be written as
\begin{equation}\label{eq:theta-support}
 \ell=u\lambda^mnb^3,
\end{equation}
where $u\in\OO^\times$, $m\in\mathbb Z$ with $m\ge-4$, and
$n,b\in\OO$ are primary with $n$ squarefree.
\begin{equation}\label{eq:theta-coefficient-bound}
 |d(\ell)|=|d(u\lambda^mnb^3)|\le27\cdot 3^{m/6}|b|.
\end{equation}

For $A>0$, integers $j\ge0$, and $V_*$ supported in a fixed compact
interval $I\subset(0,\infty)$, there is $J=J(A,j)$ such that
\begin{equation}\label{eq:theta-weight-decay}
 |(x\partial_x)^jV_*^\sharp(x)|
 \ll_{A,j,I}\|V_*\|_{C^J(I)}\min(x^{1/4},x^{-A}),\qquad x>0.
\end{equation}
\end{lemma} — depends on: App. A.2 l.3120-3142 (support and coefficient size), App. A.2 l.3452-3472 (weight decay: gamma quotient, first pole at t=-5/6, contour shifts to Re t=-1/4 and Re t=A), EXT: DR (5.7), (5.13), (5.14); [Pat77, Table III] -- magnitudes CHECKED by us: m=3k-3 gives 3^{k/2+5/2}=27*3^{m/6} (sharp), m=3k-4 gives 3^{k/2+2}<=27*3^{m/6}, t_+- at m=-4 are <=9|b|<=27*3^{-2/3}|b|, EXT: Stirling
- **Lemma 6.5 [lem:quadratic] (quadratic large sieve)** (line 1886, lemma, imported): \begin{lemma}\label{lem:quadratic}
Let $\mathcal H,U\ge1$, and let $\beta(n)$ be complex coefficients
on squarefree primary $n$ with $\NK(n)\asymp U$.
For every $\varepsilon>0$,
\begin{equation}\label{eq:Q}
 \sum_{\substack{k\equiv1\ (3),\ (k,S)=1\\\NK(k)\le\mathcal H}}^*
 \Bigl|\sum_{\substack{n\equiv1\ (3),\ n\ {\rm squarefree}\\
                       \NK(n)\asymp U}}
       \beta(n)\chi_k(n)^3\Bigr|^2
 \ll_{S,\varepsilon}(\mathcal HU)^\varepsilon(\mathcal H+U)
       \sum_n|\beta(n)|^2.
\end{equation}
The star restricts $k$ to squarefree primary elements.
\end{lemma} — depends on: EXT: Goldmakher-Louvel [GL, Thm 1.1 and Cor. 1.2; Definition 1 and Sec. 2] (arXiv:1112.1642v2), family x -> (x/k)_2 kappa_lambda(x)^{e_k}, conductor k lambda^{e_k}; classes mod 24 fix supplements and reciprocity (sketch l.1903-1912) -- unit-triviality NUMERICALLY VERIFIED by us (468 cases)
- **Lemma 6.6 [lem:squarefree-completed]** (line 1923, lemma): \begin{lemma}\label{lem:squarefree-completed}
For every $\varepsilon>0$ and $C_0\ge1$ there is
$J=J(\varepsilon,C_0)\ge1$ such that
\begin{equation}\label{eq:squarefree-completed}
 \sum_{\substack{0<N(s)\le\mathcal H\\s\ {\rm squarefree}}}
 |T(X;u_0s,g)|^2
 \ll_{I,\xi,S,\varepsilon,C_0}D^\varepsilon\|W\|_{C^J(I)}^2
 \Bigl(\mathcal H+\frac{\mathcal H^2N(g)}X\Bigr)
\end{equation}
for $1\le\mathcal H,X,N(g)\le D^{C_0}$, $u_0\in\OO^\times$,
every compact interval $I\subset(0,\infty)$, and $W\in C_c^\infty(I)$.
The sum uses the chosen generators of squarefree ideals, including
those meeting $S$.
\end{lemma} — depends on: Proposition 6.2, Lemma 6.3, Lemma 6.4, Lemma 6.5, Lemma 4.1 (eq:recip) (sextic reciprocity, (eq:theta-row-twist) l.1973-1994), Lemma B.1 (eq:smooth-pointwise) (Mellin separation in N(n)/U, l.2111-2127), Lemma B.3 (eq:integral-mean-square), proof l.1937-2187: s=t k_0 l.1940-1947; (eq:auxiliary-conductor-bound) l.1966-1971; quadratic residual factor l.2001-2007; j_p=4 re-indexing l.2035-2062; (a^2,Y) bookkeeping l.2064-2088; (eq:prepared-mean-square) l.2138-2147; dyadic sums l.2157-2172
- **Lemma 7.1 [lem:first-transfer]** (line 2263, lemma): \begin{lemma}\label{lem:first-transfer}
Under the hypotheses of Proposition~\ref{prop:transfer}, fix an integer
$j\ge0$ and $\varepsilon_0>0$. If $M\ge0$ satisfies
$\mathcal Q_{\xi_1}(U)\le M\|U\|_{C^j(I_*)}^2$
for every $U\in C_c^\infty(I_*)$ and every $\xi_1$, then
\[
 \mathcal A(W)\ll D^{\varepsilon_0}(\Sigma+M)
                    \|W\|_{C^{2j+4}(I)}^2.
\]
\end{lemma} — depends on: Lemma 4.2 (Poisson in k, exclusion C), Lemma 4.1 (eq:convert1), (eq:quotient) -> (eq:paired-first-gauss) l.2288-2292 [NUMERICALLY VERIFIED by us, 92 pairs], Lemma B.2, definitions (eq:P) l.2244-2250 and (eq:first-transfer-forms) l.2253-2259 with enlarged range Y_{C,d}=c_I Sigma L F N(d)/(H N(C)^2) (l.2239)
- **Lemma 7.2 [lem:arithmetic-poisson] (second Poisson identity)** (line 2407, lemma): \begin{lemma}[Second Poisson identity]\label{lem:arithmetic-poisson}
With the notation and index ranges above,
\begin{equation}\label{eq:arithmetic-poisson-identity}
 \mathcal M=Z+
 \sum_{g,e,w,h,\xi'}\frac{Y\mu(e)\mu(w)c_{\xi'}N(g)}{N(e)\ell} \sum_{(n_1n_2,S)=1}^*a^\sharp(n_1)\overline{a^\sharp(n_2)}
       \mathscr K\!\Bigl(\frac{N(n_1)}{X'},\frac{N(n_2)}{X'}\Bigr).
\end{equation}
The zero-frequency term satisfies
\[
 |Z|\ll_{I_*,\Phi}Y\ell\|U\|_\infty^2.
\]
\end{lemma} — depends on: Lemma 4.2 (Poisson in y, exclusion g), Lemma 4.1 (eq:convert2)-(eq:quotient), (eq:crt-a), notation (eq:common-mobius-sum) l.2358-2364 and outputs (eq:common-poisson-output) l.2388-2396
- **Lemma 7.3 [lem:second-transfer]** (line 2496, lemma): \begin{lemma}\label{lem:second-transfer}
Return to $I=[u,v]$ and $I_*=[u/2,2v]$. For an integer $m\ge0$,
let $S_m$ be the supremum in \eqref{eq:transfer-summary}.
Then, for every $\varepsilon_0>0$,
\[
 \mathcal Q_{\xi_1}(U)\ll D^{\varepsilon_0}\Sigma(1+S_m)
       \|U\|_{C^{2m+4}(I_*)}^2
 \qquad(U\in C_c^\infty(I_*)).
\]
The test functions in $S_m$ are supported in $I'=[u/16,4v]$ and have $C^m(I')$ norm at most one; an empty supremum is zero.
\end{lemma} — depends on: Lemma 7.2, Lemma 4.4 (exclusion (n,r)=1 removed, (X',F')->(X'/N(j),F'N(j))), Lemma B.2 (row index (r,f',k')), S_m = supremum of E at smaller parameters (the recursion, closed in Prop. 5.1), scale identities l.2526-2531; preimage regrouping forcing f'|k' l.2550-2583; closing identity (Sigma R/L^2)R(L/R)^2=Sigma l.2646-2651 (all hand-checked)
- **Lemma B.1 [lem:smooth]** (line 3491, lemma): \begin{lemma}\label{lem:smooth}
Fix a box $\mathcal I=I_1\times\cdots\times I_d$, where each $I_j$ is a
compact interval in $(0,\infty)$. Every $\mathcal K\in C_c^\infty((0,\infty)^d)$
supported in $\mathcal I$ has a representation
\begin{equation}\label{eq:smooth-separation}
 \mathcal K(\mathbf x)=\int_{\mathbb R^d}b(\mathbf t)
       \prod_{j=1}^d x_j^{\mathrm i t_j}\dd\mathbf t,
 \qquad x_j>0.
\end{equation}
For $J\ge0$ and every even integer $q>J+d$, the coefficient satisfies
\[
 \int_{\mathbb R^d}|b(\mathbf t)|(1+|\mathbf t|)^J\dd\mathbf t
 \ll_{\mathcal I,J,q,d}\|\mathcal K\|_{C^q(\mathcal I)}.
\]
\end{lemma} — depends on: Fourier inversion in logarithmic coordinates; integration by parts (proof l.3506-3524); variant (eq:smooth-pointwise) and (eq:smooth-weight-bound) l.3526-3556 for K_R = prod W_j(x_j) F(R prod x_j^{a_j})
- **Lemma B.2 [lem:smooth-mean-square]** (line 3566, lemma): \begin{lemma}\label{lem:smooth-mean-square}
Consider two families of finite sums
\[
 S_{j,r}(U)=\sum_n a_{j,r}(n)U(x_{j,r,n}),\qquad
 j=1,2,\quad x_{j,r,n}>0,
\]
with a finite set of rows $r$ and nonnegative weights $w_r$.
Suppose that, for every $U\in C_c^\infty(I_*)$,
\[
 \sum_r w_r|S_{j,r}(U)|^2\le M_j\|U\|_{C^m(I_*)}^2,
 \qquad j=1,2.
\]
Then for any $|c_r|\le w_r$ and smooth kernels $\mathcal K_r$
supported in $I^2$,
\begin{equation}\label{eq:coupled-mean-square}
 \Bigl|\sum_r c_r\sum_{n_1,n_2}
 a_{1,r}(n_1)\overline{a_{2,r}(n_2)}
 \mathcal K_r(x_{1,r,n_1},x_{2,r,n_2})\Bigr|
 \ll_{I,I_*,m}\sqrt{M_1M_2}\,
       \sup_r\|\mathcal K_r\|_{C^{2m+4}(I^2)}.
\end{equation}
\end{lemma} — depends on: Lemma B.1 (d=2), Cauchy-Schwarz in r; ||V(x)x^{it}||_{C^m} << (1+|t|)^m; q=2m+4 (proof l.3588-3615)
- **Lemma B.3 [lem:recombine]** (line 3621, lemma): \begin{lemma}\label{lem:recombine}
Let $r,\iota$ range over finite sets, let $d\ge1$, and let $w_r\ge0$.
Suppose the measurable coefficients $c_{\iota,r}$ satisfy
\[
 |c_{\iota,r}(\mathbf t)|\le b_\iota(\mathbf t),\qquad
 M:=\sum_\iota\int_{\mathbb R^d}b_\iota(\mathbf t)\dd\mathbf t<\infty,
\]
where $b_\iota:\mathbb R^d\to[0,\infty)$.
For measurable $F_{\iota,\mathbf t}(r)$, whenever the right-hand
side is finite, one has
\begin{equation}\label{eq:integral-mean-square}
 \sum_r w_r\Bigl|\sum_\iota\int c_{\iota,r}(\mathbf t)
 F_{\iota,\mathbf t}(r)\dd\mathbf t\Bigr|^2
 \le M\sum_\iota\int b_\iota(\mathbf t)
       \sum_r w_r|F_{\iota,\mathbf t}(r)|^2\dd\mathbf t.
\end{equation}
The same assertion holds for finite sums with the integrals omitted.
\end{lemma} — depends on: weighted Cauchy-Schwarz (proof l.3639-3650)


_Mapper note:_ NOT WRITTEN: the harness refused the Write of /home/user/riemann/research/exploratory/riemann-observatory/audits/quasi_rh/ARCHITECTURE.md with the message 'Subagents should return findings as text, not write report files'. The full report content is in this StructuredOutput: the statements catalogue (verbatim LaTeX with dependencies), imported_results (E1-E17), and load_bearing_steps, which holds the strategy and 11/12 derivation, D1-D15, the smallest failure point, the dependency graph, the scales, the findings classification and the numerical checks. The reproducibility scripts were written to /home/user/riemann/research/exploratory/riemann-observatory/audits/quasi_rh/architecture_checks/ (zomega.py, check_lemma41.py, check_recip.py, check_paired.py, check_local.py, check_gl_family.py). Source bound: paper2.tex sha256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d; paper2.pdf sha256 f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18.

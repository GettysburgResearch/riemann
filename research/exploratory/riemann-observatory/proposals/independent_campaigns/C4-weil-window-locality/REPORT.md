<!-- materialized from workflow result: campaigns / inv:C4-weil-window-locality -->
# C4-weil-window-locality — investigator report (materialized from structured return)

## Investigator notes / header

/home/user/riemann/research/exploratory/riemann-observatory/proposals/independent_campaigns/C4-weil-window-locality/REPORT.md. I did NOT write this file. The session instructions forbid subagents to write report .md files, and the harness refused the same write for C1. The report content is this structured return, which tools/materialize_results.py renders to that path. Machine-generated tables: /home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/tables_C4.md (sha256 5a12131922c1f185256b3c94280acf806127ce3f0359246be447a97278111837). Hashes and versions: manifest_C4.json in the same directory.

HEADER BLOCK.
Status: EXPLORATORY. It contains 4 complete proofs: C4-C, C4-LAT, C4-B and C4-BL, the last conditional on an explicit hypothesis R. It also contains IMPORTED, NUMERICAL-NONRIGOROUS, HEURISTIC and CONJECTURE items and one REFUTED heuristic. It makes no claim about RH.
Scope: zeta only. Weil form on windows supp g in [-L,L] in the brief's normalisation. Detection statements about hypothetical off-line zeros hold either under the explicit single-defect hypothesis H1 or in the synthetic injection model (true zeros plus an injected quadruple).
Exact sources:
- Connes-Consani arXiv:2006.13771 (L1).
- Bombieri, Rend. Lincei 11 (2000) 183-233, BDIM PDF (L1: Sec. 1, 8, 10, 12).
- Zhu arXiv:2608.24827v2 (L1; unrefereed).
- Andrews-Connes-La Gatta arXiv:2611.13129 (L1; unrefereed).
- Suzuki arXiv:2206.03682, 2606.09096, 2610.32704 (L1 partial).
- Groskin arXiv:2607.02828 (abstract only).
- Kim et al. arXiv:2607.24830 (Sec. 3.7 only).
- Alpoge-Furman arXiv:2608.13637 (abstract only).
- Yoshida 1992: zbMATH 0817.11041 review only (L0+).
- Trudgian 2014 S(t) bound: zbMATH 1284.11119 review (L0+).
- The 100000 Arb-certified zeros; mpmath siegelz zeros near 1e6, 1e8, 1e10.
What was actually run, with runtimes:
- High-precision Arb window profile, L=0.1..1.2: 627 s.
- Zeros-side cross-checks: entrywise, and at the level of the 1e-17 eigenvalue.
- Detection-threshold scans, additive model: 15 heights from 27.7 to 7e4 plus 1e6, 1e8, 1e10; 8 values of delta; 70 + 698 + 40 s.
- Very-large-height growth scans, 1e12..1e50: 140 s.
- N-convergence runs: T=100 and 1000 at N x1.5, x2, x3; T=1e4 at N x1.5.
- Collision variant, T=100, 1000, 1e4.
- Flat and lattice model checks.
- Exact evaluation of the Theorem C4-B inequality (50 digits).
- Local-symbol diagnostic.
Smallest remaining gap:
- (i) No rigorous detection theorem in the interpolation regime: delta small, L ~ (1/2)log(T/2pi)+O(1).
- (ii) No proof, for zeta, of the local resolvent hypothesis R needed for blindness.
- (iii) The Nyquist-regime thresholds are not converged in basis size. They are upper bounds that still drop by about 0.03-0.08 per refinement.

## Claims

- **id:** C4-0 | **status:** IMPORTED (a-c); (d) NUMERICAL-NONRIGOROUS for the 'no feature' part | **statement:** Windows of known unconditional positivity, and the 2 pi e^{2L} = gamma_1 coincidence. Normalisation as in the brief: g in C_c^inf(-L,L), f = g*g~ supported in [-2L,2L]; only prime powers n < e^{2L} enter.
(a) Connes-Consani's support [2^{-1/2}, 2^{1/2}] refers to g, in the multiplicative variable. The autocorrelation g*g^* is supported in [1/2, 2]. In the log variable this is L = (1/2)log 2 = 0.346574 for g and |x| <= log 2 for g*g~: the largest window with no prime power. Their positivity needs ghat(i/2) = 0 (and ghat(0) = 0 in their Thm 1). Yoshida 1992 proved positivity for the same window (t = (log 2)/2, as reported by Bombieri).
(b) Bombieri 2000, Thm 12: if g is supported in an interval I with |I| < log 2, then W >= (log(1/|I|) - log log(1/|I|) - O(1))||g||^2.
(c) Zhu 2026, Thm 1.2 and Cor 6.3 (unrefereed): certified W >= 8.9e-18 ||g||^2 for L = 0.8.
(d) 2 pi e^{2L} = gamma_1 at L = (1/2)log(gamma_1/2pi) = 0.405408, strictly above the CC/Yoshida window, where 2 pi e^{2L} = 4 pi = 12.566 < gamma_1. The coincidence is real but is not a positivity threshold: positivity is certified beyond it (L = 0.8), and our profile lambda_min(L) shows no feature at 0.4054. | **evidence:** Read at L1:
- CC 2006.13771: introduction (displays (3)-(6), Thm 1, Cor 2) and App. B/C.
- Bombieri 2000, BDIM full text: Sec. 1 (Yoshida verified t = (log 2)/2) and Sec. 12, Thm 12.
- Zhu 2608.24827, Sec. 1.2.
- ACL 2611.13129, Sec. 8.7: 'For lambda^2 < 14.13/2pi ~ 2.25 the ordinate of the first zero exceeds gamma and no undersampling occurs: this is the regime of [CC archimedean]'. The coincidence is therefore already recorded there.
Profile values (C4-P): -ln lambda = 6.62 (L=0.3466), 8.61 (0.4), 8.85 (0.4054), 13.88 (0.5). The slope per 0.1 in L rises smoothly: 1.6, 2.5, 3.7, 5.3, 6.4, ... There is no kink at 0.405. | **prior_art:** Yoshida 1992 (zbMATH 0817.11041, L0+); Bombieri 2000 Thm 12; Connes-Consani 2020/21; Zhu 2026; ACL 2026 Sec. 8.7.
- **id:** C4-1 | **status:** IMPORTED | **statement:** Prior art on window profile, resolution height and negative-eigenvalue counts.
- Zhu 2026 defines lambda*(L) exactly as the brief does (even real f). His Prop 2.3: RH implies lambda*(L) > 0 for every L, via Beurling's sampling theorem and Littlewood's gap bound. My planned 'Theorem A' is therefore prior art.
- Zhu Table 3: certified upper bounds from 1.05e-6 (L=0.5) to 3.19e-283 (L=2.0). Empirical law: -ln lambda* ~ 2 pi^2 N(T*)/ln N(T*), with T* = 2 pi e^{2L} the 'resolution height', 'below which a function band-limited to [-L,L] has enough oscillation capacity to interpolate zeros'.
- Zhu Thm 1.3: RH implies lambda*(L) <= exp(-L e^L) for large L (canonical product at half saturation, T = 2 pi e^L). Zhu Thm 1.4: certificate barrier T1 = 2 pi e^{A_L}, A_L ~ 4 e^L.
- ACL 2026: the Weil form on [lambda^{-1}, lambda], L = log lambda. The scale 2 pi lambda^2 = 2 pi e^{2L} separates zeros that undersample window transforms from zeros that oversample them. There are lambda^2-1 even and lambda^2-2 odd minuscule eigenvalues. The ground-state Mellin zeros reproduce the zeta zeros up to t ~ 3000-3100 at lambda^2 = 250, where 2 pi lambda^2 = 1571 (about 2T*).
- Bombieri 2000, Thm 8: for finite truncations, the number of negative eigenvalues equals the number of non-real conjugate pairs. Thms 10/11: limit alternatives, including linear relations among x^{-rho}. Bombieri's footnote 11 reports fake-off-line-zero experiments with the first 320 zeros.
- Suzuki 2026 (2610.32704, Thm 1.1), under RH: the eigenvalues t_{a,n} of a self-adjoint extension on [-a,a] satisfy t_{a,n} >= gamma_n and decrease to gamma_n.
None of these works states which (T, delta) a window detects. My arXiv/zbMATH/web searches found no such statement. Searches used: 'Weil positivity', 'Weil quadratic form', 'Weil functional', 'Krein extension zeta zeros', 'explicit formula off the critical line support', 'Weil positivity window', two web searches. | **evidence:** Full texts fetched and grepped (paths in the observatory fulltext cache):
- Zhu Secs 1-2, 9, 13, 16 and Table 3.
- ACL Abstract, Sec. 1, Sec. 7.3, Sec. 8.7.
- Bombieri Secs 1, 8, 10, 11, 12.
- Suzuki 2610.32704 abstract and Thm 1.1; Suzuki 2206.03682 Thms 1.1-1.8.
Kim et al. 2607.24830, Sec. 3.7: a residual grows like e^{2a delta} for an injected off-line zero. This is a different functional, and it is not compared against a height-dependent background. | **prior_art:** Zhu 2026 (arXiv:2608.24827); Andrews-Connes-La Gatta 2026 (arXiv:2611.13129); Bombieri 2000; Suzuki 2022/2026; Connes-Consani 2021 (2106.01715) and CCM 2023 (2310.18423), both read only at abstract level here.
- **id:** C4-P | **status:** NUMERICAL-NONRIGOROUS (high precision; ball-arithmetic assembly, but the archimedean quadrature error is not enclosed) | **statement:** Window profile lambda_min(L) = inf W(g*g~)/||g||^2 over g in L^2(-L,L). These are Galerkin values in the orthonormal Legendre basis, best N, ground state in the even sector:
- L=0.1: 0.457115
- L=0.2: 0.0949470
- L=0.3: 7.57305e-3
- L=(log 2)/2: 1.32952e-3
- L=0.4: 1.81727e-4
- L=0.405408: 1.44034e-4
- L=0.5: 9.37661e-7
- L=0.6: 1.62065e-9
- L=0.7: 4.23548e-13
- L=0.8: 1.70156e-17
- L=0.9: 4.29796e-23
- L=1.0: 6.25697e-30
- L=1.1: 2.05682e-38
- L=1.2: 7.98216e-49
The odd sector is larger by factors of 3 to 6e3.
Each value is 11-27% below Zhu's certified upper bound. At L=0.8 the value lies inside Zhu's two-sided certified enclosure [8.9e-18, 2.27e-17].
The values are not converged in N for L >= 0.9. The last N step lowers the value by 5% (L=0.9), 6.5% (1.0), 22% (1.1) and a factor 8.5 (1.2). They are upper-bound-type approximations to the true infimum.
We did not compute L up to 3: double precision cannot resolve lambda_min beyond L ~ 0.6, and at L=3 the needed dimension is about 5e3 at about 1000 digits (Zhu's law). | **evidence:** Assembly of the arithmetic side:
- explicit formula T[f] = int 2cosh(y/2)f - sum Lambda(n)n^{-1/2}(f(log n)+f(-log n)) - (log 4pi + gamma)f(0) - int_0^inf [e^{-y/2}(f(y)+f(-y)) - 2e^{-y}f(0)]/(1-e^{-2y}) dy (Bombieri Sec. 12; Suzuki 2606.09096 Sec. 1);
- closed forms c1 = int_0^1 (u^{-1/2}-1)/(1-u^2)du = (log 2)/2 + pi/4 and int_0^{e^{-2L}} u^{-1/2}/(1-u^2)du = artanh(e^{-L}) + arctan(e^{-L}), both derived here; so Arch_jk = C0(L) delta_jk - int_0^{2L} K(y)[A_jk(y) + A_kj(y) - 2 delta_jk] dy, with K = e^{-y/2}/(1-e^{-2y}) and A_jk(y) = int phi_j(x)phi_k(x-y)dx computed by exact Gauss rules;
- pole term P_jk = a_j b_k + b_j a_k.
Precision and solver: python-flint 0.9.0 Arb at 200-560 bits. The S-node Gauss rule for the archimedean integral was checked at L=0.6 (S=120 vs 200 agree to 12 digits). Smallest eigenvalue of each parity block by inverse iteration plus a ball Rayleigh quotient (radii <= 1e-109).
Cross-checks:
- (1) Arithmetic vs zeros side (100000 Arb zeros plus smooth-tail estimate), double precision, N=24: max entry difference 1.4e-7, 3.0e-8, 2.4e-8, 3.8e-8 at L = 0.3, 0.6, 1.0, 1.5. Modulated basis at T=100, L=1 (3474 zeros plus tail): 2.4e-5.
- (2) At the level of the tiny eigenvalue (hp_spectral_check.json), zeros-side sum_{gamma<=3000} 2|h_v(gamma)|^2 for the arithmetic ground state v: at L=0.6, 1.60738e-9 vs lambda = 1.62065e-9; at L=0.8, 1.67958e-17 vs 1.70156e-17. The remainders 1.33e-11 and 2.20e-19 match the 1/gamma^2 tail estimate 4v(L)^2(log(3000/2pi)+1)/(2pi 3000) = 1.31e-11 and 2.17e-19, with v(L) = 9.28e-5 and 1.19e-8.
Outputs: lambda_profile_main.json (sha256 1dcdd50d1a44d8885df884bfdbf13a3c18993e551d9ab6e7afef2f9625c69b79; 627 s) and hp_spectral_check.json (1a99c939f35df9da1a3e0cdd4f0e98ccacf3b12fd86dfc13e87aeed90ac29b5b). | **prior_art:** Zhu 2026, Table 3 (certified upper bounds) and Sec. 10 (float64 traps). This is an independent replication with a different basis and both parities; it is not new.
- **id:** C4-C | **status:** THEOREM (complete proof; standard Schur-complement/Sylvester argument, not claimed new) | **statement:** Exact detection criterion.
Fix L. Split the multiset of zero ordinates gamma = (rho - 1/2)/i into a real part Gamma_R and a finite non-real part Q, closed under conjugation and negation, with multiplicities m_z.
Assume (S): P(g) := sum_{Gamma_R} m |h_g(gamma)|^2 >= a ||g||^2 on C_c^inf(-L,L) for some a > 0.
Let k_z be the P-Riesz representer of g -> h_g(z), z in Q, so that k_z = P^{-1} e_z with e_z(x) = e^{-i conj(z) x} 1_{[-L,L]}. Let G = (<k_w, k_z>_P), which is positive definite. Let M_{zw} = m_z [w = conj z].
Then:
(i) The negative index of W on C_c^inf(-L,L) equals the number of negative eigenvalues of G^{-1} + M. In particular lambda_min(L) < 0 iff G^{-1} + M is not positive semidefinite.
(ii) The negative index is at most the number of non-real conjugate pairs, counted with multiplicity.
(iii) Monotonicity: if P1 >= P2 then the negative index under P1 is <= that under P2. Detection is monotone in L.
(iv) The infimum over complex g equals the infimum over real g. | **evidence:** Proof.
- W(g) = P(g) + sum_z m_z h_g(z) conj(h_g(conj z)). This is a finite-rank Hermitian perturbation of P by the bounded functionals l_z(g) = h_g(z) = <g, e_z>_{L2} = P(g, P^{-1} e_z).
- Decompose g = g_perp + sum_z c_z k_z, with g_perp P-orthogonal to every k_z, so l(g_perp) = 0. Then W(g) = P(g_perp) + W(sum c_z k_z), and the two pieces are W-orthogonal.
- On span{k_z} the form is c* (G + G M G) c = c* G (G^{-1} + M) G c. Sylvester's law of inertia gives (i), since P > 0 on the complement.
- Density of C_c^inf in the completion H_P, together with continuity of W on H_P, transfers the index.
- (ii): Weyl's inequality with G^{-1} > 0. The eigenvalues of M are +-m_z on each conjugate pair.
- (iii): P1 >= P2 implies G1 <= G2, hence G1^{-1} >= G2^{-1}. Windows are nested.
- (iv): in a real basis the form is real-symmetric, because the zero set is invariant under gamma -> -gamma and gamma -> conj gamma.
(S) holds under RH by Zhu Prop 2.3. In the synthetic model it holds numerically. | **prior_art:** Bombieri 2000 Thm 8 (count of negative eigenvalues for finite truncations; equality for large truncations under finitely many off-line zeros). Alpoge-Furman 2026 use Sylvester's law with signature-(1,1) blocks for off-line pairs. The host repository's completed-square Schur matrix S (CURRENT_RESULTS Sec. 7) is the arithmetic-side analogue. C4-C is the zeros-side form with an explicit kernel matrix.
- **id:** C4-LAT | **status:** THEOREM (complete proof; model statement, checked numerically) | **statement:** Lattice/flat model: exact two-regime law.
Setup: Gamma_R = lambda0 + sZ, s > 0, with density Psi0/2pi where Psi0 = 2pi/s. One non-real pair {T0 - i delta, T0 + i delta} with T0 = lambda0 + s(k + 1/2) and delta > 0. One-sided form on complex g in L^2(-L,L):
  W_lat(g) = sum_{Gamma_R} |h_g|^2 + 2 Re[h_g(T0 - i delta) conj h_g(T0 + i delta)].
Result: inf W_lat < 0 iff (a) L > Psi0/2 = pi/s (Nyquist), or (b) sigma^2(delta,L) := sinh(2 delta L)/(2 delta) - L > Psi0/2 (growth).
With kappa = delta Psi0, condition (b) reads sinh u - u > kappa with u = 2 delta L. It beats the Nyquist window iff kappa > kappa_c = 2.17732, the root of sinh k = 2k.
The same criterion (b) holds for the 'flat' model P = Psi0 ||g||^2. | **evidence:** Proof.
(i) Case L <= pi/s. The Fourier transform of |h_g|^2 is supported in [-2L, 2L] and vanishes at +-2L. Poisson summation gives sum_{Gamma_R}|h_g|^2 = (1/s) int |h_g|^2 = Psi0 ||g||^2. Apply C4-C with
  G = Psi0^{-1} [[sinh(2 delta L)/delta, 2L], [2L, sinh(2 delta L)/delta]],  M = [[0,1],[1,0]].
These commute, and G^{-1} + M has the eigenvalue Psi0/(sinh(2 delta L)/delta - 2L) - 1. This is negative iff (b) holds.
(ii) Case L > pi/s. Let h(r) = (r - T0) sin(pi(r - lambda0)/s) k(r), with k(r) = [sin(eps(r - T0))/(eps(r - T0))]^4 and eps = (L - pi/s)/4. Then h is in PW_L and in L^2, and h vanishes on Gamma_R. Using sin(pi(k + 1/2) -+ ib) = (-1)^k cosh b,
  2 Re[h(T0 - i delta) conj h(T0 + i delta)] = -2 delta^2 cosh^2(pi delta/s) (sinh(eps delta)/(eps delta))^8 < 0.
If the mirror pair at -T0 is present, take a higher sinc power; its contribution is O(T0^{-2}) and can be made negligible.
Numerical check (check_flat_lattice.json, sha256 addf226e55dd95b12a16c2b00e34ed2e385368ccedeafe715626eb916c9ff55c):
- Flat model: the sign of lambda_min flips between 0.98 and 1.02 times L_flat for delta = 0.1, 0.3, 0.49.
- Lattice below Nyquist: lambda0 = 11.97763 = log(T/2pi) exactly (Poisson).
- Lattice above Nyquist: lambda0 collapses to 1.8e-7 at 1.1 L_N, and delta = 0.01 and 0.1 are detected there. At 1.01 L_N the N=64 basis cannot represent the bandwidth-0.01L null function. This finite-basis delay is a negative record. | **prior_art:** The Poisson/aliasing identity is classical. No statement of this two-regime detection law was found.
- **id:** C4-B | **status:** THEOREM (complete proof under the explicit single-defect hypothesis H1; implication statement) | **statement:** Growth detection.
Assumptions: 0 < delta < 1/2 and T >= 100. (H1): rho0 = 1/2 + delta + iT is a zero (multiplicity m >= 1), and every nontrivial zero outside {rho0, 1 - conj rho0, conj rho0, 1 - rho0} is on Re s = 1/2.
Notation:
- sigma^2 = sinh(2 delta L)/(2 delta) - L
- S*(t) = 0.112 log t + 0.278 log log t + 2.510
- A = 2 sinh(delta L), B = 2L sinh(delta L), Ac = 3 e^{delta L} sinh(delta L) + delta L
- eps = Ac^2/(2T^2) + 8A^2/T^2 + sigma^2/(2 sqrt T) + 4A^2/(pi T^{3/4}) + (2A^2/pi)(log T + 1)/T + (0.4/pi)(10A^2/(pi T^2) + 16 pi sigma^2/T^2) + 8AB S*(2T)/T + 32AB(S*(2T) + 0.112 + 0.278/log 2T)/T
Conclusion: if
  2 sigma^4 > sigma^2 [log(T/2pi) + 4 pi L S*(2T)] + eps,
then lambda_min(L) < 0. Some real g in C_c^inf(-L,L) has W(g*g~) < 0.
Hence the detection window satisfies L*(T,delta) <= L_B(T,delta) = (1/(2 delta))[log log T + log log log T + O_delta(1)]. This is O((1/delta) log log T), whereas the Nyquist window is (1/2)log(T/2pi). | **evidence:** Proof.
1. Test function. Take g0 = e^{-iTx} w(x) with w = sinh(delta x) on [-L,L], so h_{g0}(z) = what(z - T).
2. Quadruple terms. The +T pair gives what(-i delta) conj what(i delta) + c.c. = -2 sigma^4, since int sinh(delta x) e^{+-delta x} = +-sigma^2. With multiplicity m it gives -2m sigma^4. The -T pair is bounded by Ac^2/(2T^2), because |what(zeta)| <= Ac/|zeta| for |Im zeta| <= delta.
3. Real zeros. Their contribution is P <= int_0^inf F dN with F(t) = |what(t-T)|^2 + |what(t+T)|^2. Backlund's formula N = theta/pi + 1 + S and integration by parts give F(0) + (1/pi) int F theta' - int F' S.
4. Ingredients:
   - |what(s)| <= 2A/|s| and |what'(s)| <= 2B/|s| for real s (one integration by parts, using int_0^L (sinh + delta x cosh) = L sinh(delta L));
   - ||what||^2 = 2 pi sigma^2 and ||what'||^2 <= 2 pi L^2 sigma^2;
   - theta' <= 0 on (0, 2pi], and theta'(t) <= (1/2)log(t/2pi) + 0.4 t^{-2} for t >= 2pi (Stirling remainder, DLMF 5.11; numerically theta'(t) - (1/2)log(t/2pi) is in (-0.0094, 0) on [2, 1000]);
   - |S| <= S*(t) (Trudgian 2014, t >= e) and |S| <= 1 on (0, e).
   These give (1/pi) int F theta' <= sigma^2 log(T/2pi) + E2 + E3 + E4 and int |F'||S| <= S*(2T)(4 pi L sigma^2 + 8AB/T) + E5. The term 4 pi L sigma^2 comes from 2||what|| ||what'||.
5. Approximation. Mollified, dilated g_n in C_c^inf(-L,L) have bounded variation, so |h_{gn}| <= C/(1+|z|) uniformly. Dominated convergence on the absolutely convergent zero sum gives W(g_n) -> W(g0).
6. Real g. Use C4-C(iv).
Asymptotics: e^{2 delta L}/(4 delta) ~ (0.5 + 1.407 L) log T.
Evaluation: thmB_bound.py, 50-digit mpmath; thmB_table.json, sha256 3e6ee84ef06fa951f57833e9c0eb98730ec80a2be899da6712d33d1de580eb50. | **prior_art:** I found no prior statement. The idea that e^{delta x} growth reveals an off-line zero is folklore: Kim et al. 2026 (Sec. 3.7) use an e^{2a delta} residual growth for a different functional. Under H1 the theorem is 'possibly new' only.
- **id:** C4-B2 | **status:** THEOREM (exact evaluation of the explicit C4-B inequality; conditional on H1) | **statement:** Consequences of C4-B.
The guaranteed window L_B(T,delta) is below the Nyquist window L_N = (1/2)log(T/2pi) for all log10 T above the following:
- 6.09 (delta = 0.49)
- 6.59 (0.45)
- 7.37 (0.4)
- 9.77 (0.3)
- 14.77 (0.2)
- 31.05 (0.1)
- 67.1 (0.05)
- 413 (0.01)
Examples:
- At the verified height T = 3e12 (L_N = 13.45): L_B = 6.49 (delta = 0.49), 7.94 (0.4), 10.57 (0.3); for delta = 0.2, L_B = 15.82 > L_N.
- At T = 1e100 (L_N = 114.2): L_B = 8.26, 10.10, 13.44, 20.12, 40.16, 80.24 for delta = 0.49, 0.4, 0.3, 0.2, 0.1, 0.05.
- At T = 1e1000 (L_N = 1150.4): L_B = 10.73 (0.49) and 52.3 (0.1).
Any hypothetical zero lies above the verified height 3e12 (Platt-Trudgian). For delta >~ 0.22 its rigorous single-defect detection window is below the Nyquist window. | **evidence:** thmB_table.json (bisection on L of the margin, mpmath dps 50; crossover found by bisection in log10 T). The rigorous bound is weaker than the numerics; e.g. at T=1e10, delta=0.49: L_B ~ 6.0 vs measured L* = 3.30. The loss is the factor (1 + 1.41L) from the S(t) term. | **prior_art:** Platt-Trudgian 2021 for the verified height 3.0001753328e12. No prior detection-window table was found.
- **id:** C4-R | **status:** REFUTED (as stated, for every fixed delta > 0), with a corrected replacement (C4-LAT exact in the model, C4-B rigorous under H1, C4-D1..D3 numerical) | **statement:** Brief's heuristic, tested: 'a window L can detect an off-line zero at height T only when T <~ 2 pi e^{2L}, and is blind far above that, up to O(log 1/delta)'. This is false. For fixed delta, kappa = delta log(T/2pi) -> inf, and detection occurs at L ~ (1/(2 delta)) log log T, far below (1/2)log(T/2pi). Equivalently, a window L detects large-delta defects up to doubly exponential heights T ~ 2 pi exp((sinh(2 delta L) - 2 delta L)/delta) (flat model).
Corrected statement:
- 'Nyquist locality' holds only for near-line defects, kappa <~ kappa_c = 2.177, i.e. displacement delta <~ 0.35 local mean spacings 2pi/log(T/2pi).
- In that regime L* ~ L_N + small offset + small log(1/delta) term.
- For kappa > kappa_c, L* ~ L_flat solving sinh(2 delta L)/(2 delta) - L = Psi_eff/2, with Psi_eff ~ log(T/2pi) up to local prime-comb fluctuations. | **evidence:** - Rigorous under H1: C4-B and C4-B2.
- Exact in the lattice model: C4-LAT.
- Synthetic numerics (C4-D1, C4-D3):
  - T = 1e10, delta = 0.49: L* = 3.30 vs L_N = 10.59.
  - T = 1e50, delta = 0.49: L* = 4.883 vs L_N = 56.65.
  - Across the growth-regime cases (kappa > kappa_c) at T <= 7e4: L* - L_flat is in [-0.28, +0.11]. | **prior_art:** The Nyquist/resolution height itself is prior art (Zhu 2026 Sec. 9; ACL 2026 Sec. 8.7). The detection heuristic as posed is the brief's own; I did not find it in the literature.
- **id:** C4-BL | **status:** THEOREM (complete proof, conditional on the explicit hypothesis R) + HEURISTIC (when R should hold) | **statement:** Conditional blindness.
Setup as in C4-C. Q is a single quadruple at (T, delta), Psi0 = log(T/2pi), V = span{e_z : z in Q}, and P is the self-adjoint operator of the real-zero form.
Hypothesis R(T, L, eta): <P^{-1} v, v> <= (1 + eta) Psi0^{-1} ||v||^2 for all v in V.
Conclusion: if (1+eta)^{-1} G_flat^{-1} + M is positive semidefinite, then W >= 0 on window L. Here G_flat = Psi0^{-1} (<e_w, e_z>), a 4x4 matrix with ±T cross-entries O(e^{2 delta L}/T).
Up to O(e^{2 delta L}/T) this reads: blind if sigma^2(delta,L) <= Psi0/(2(1+eta)).
The extra hypothesis needed is R. It is a quantitative local Beurling-Landau sampling and resolvent bound at height T. It must also control leakage from the window's near-null space. | **evidence:** Proof. G = E* P^{-1} E <= (1+eta) Psi0^{-1} E* E = (1+eta) G_flat. Operator monotonicity of inversion gives G^{-1} >= (1+eta)^{-1} G_flat^{-1}. Then C4-C(i).
HEURISTIC (when R holds):
- (i) Sampling regime with margin, T >= (1+c) 2 pi e^{2L}. The near-null eigenvectors, with eigenvalues ~ lambda_min(L) ~ exp(-2 pi^2 N(T*)/ln N(T*)), live below T*. Their leakage to T, ~ exp(-c' L (T - T*)), must be << lambda_min(L).
- (ii) The local symbol Psi_L(T+s) = Re psi(1/4 + i(T+s)/2) - log pi - sum_{log n < 2L} 2 Lambda(n) n^{-1/2} cos((T+s) log n) must stay >~ Psi0/(1+eta) on |s| <~ few/L. This can fail where the prime comb aligns (sup = A_L ~ 4 e^L, Zhu Lemma 3.2).
Numerically, psi_eff_diag.json: Psi_eff/log(T/2pi) = 0.60-0.92 at T0 = 1e6, 1e8, 1e10. So eta is typically 0.1-0.7 at these heights, not ~0. At T = 1e20..1e50, |L* - L_flat| <= 0.08, so eta -> 0 as log T >> L. Galerkin values only give LOWER bounds for <P^{-1}v, v>, so they cannot verify R. | **prior_art:** Beurling-Landau sampling theory (Beurling; Landau 1967; Seip 2004). Zhu Prop 2.3 (global sampling under RH). No local resolvent version for zeta zeros was found.
- **id:** C4-D1 | **status:** NUMERICAL-NONRIGOROUS (double precision; Rayleigh-Ritz, so each finite-basis threshold is an upper bound for the model threshold) | **statement:** Detection thresholds L*(T0, delta) in the additive single-defect model: true zeros (exact arithmetic side) plus an injected quadruple at the midpoint T0 of two consecutive Arb zeros. Detection rule: lambda_min < -1e-8 in the basis {e^{-iT0x} phi_j}; N = 48/64/96 for L <= 2 / <= 3.5 / > 3.5.
Nyquist regime, kappa < kappa_c:
- L* - L_N is in [+0.02, +0.63] at T0 = 27.7..7e4.
- At delta = 0.01: L* = 1.008, 1.305, 1.711, 2.006, 2.552, 2.975, 3.423, 3.764, 4.081, 4.470, 4.985, 5.284 at T0 = 27.7, 51.4, 100, 200, 499, 1001, 2000, 5000, 1e4, 2e4, 5e4, 7e4.
- The corresponding L_N are 0.742 ... 4.659.
- Exception: T0 = 7e4, delta = 0.2 gives L* = 4.484 < L_N = 4.659.
Growth regime, kappa > kappa_c:
- L* - L_flat is in [-0.28, +0.11].
- Examples: T0 = 1000.6 gives L* = 2.478/2.315 vs L_flat = 2.452/2.308 for delta = 0.45/0.49. T0 = 2e4, delta = 0.4 gives L* = 2.767 vs L_N = 4.033. | **evidence:** Code: exp_detect.py with detect_lib.py and weil_core.py.
Outputs:
- detect_lowT.json: sha256 0768eb39e5f1288c8c0bbdda33384c41ff570312e0c8d3a5ed77722b7df9fb0e, 70 s.
- detect_midT.json: sha256 3a3342044e69e22150cdf0044a68b4d3f50f9073a611ef17e3ff857aed184519, 698 s.
The tables are T2 in tables_C4.md.
Grid step 0.1 in L, then 5 bisections (resolution 0.003).
The local floor lambda0(L) (unperturbed form at T0) collapses from O(0.3) to < 1e-6 within about 0.4 of L_N; e.g. T0 = 1000.6: 0.33 at 2.51, 2.6e-3 at 2.71, 3.5e-7 at 2.91.
Float64 noise floor: about 1e-10 (spurious -7e-11 values seen). | **prior_art:** Injection experiments with fake zeros: Bombieri 2000, fn. 11 (first 320 zeros, finite truncations; no height/window law reported). C1 campaign: Li and other criteria.
- **id:** C4-D2 | **status:** NUMERICAL-NONRIGOROUS | **statement:** Fine structure of the Nyquist regime and convergence in N.
Basis refinement lowers the Nyquist-regime thresholds monotonically. Offsets L* - L_N at delta = 0.01:
- T0 = 100: 0.327, 0.220, 0.186, 0.177 for N x1, x1.5, x2, x3.
- T0 = 1000: 0.440, 0.290, 0.233, 0.158.
- T0 = 1e4: 0.394, 0.272 (x1, x1.5).
At delta = 0.1: T0 = 100 gives 0.230 -> 0.108 (x3), and T0 = 1000 gives 0.327 -> 0.124 (x3).
Growth-regime thresholds are unchanged (e.g. 2.3153/2.3091/2.3091 at T0 = 1000, delta = 0.49).
The log(1/delta) dependence suggested in the brief exists but is weak. Fitting L* = a + b ln(1/delta) over delta <= 0.2 gives b = 0.015-0.06 at N x1 and b = 0.030 (T=100) and 0.015 (T=1000) at N x3. In each case b is about 2/(d ln(1/lambda0)/dL), consistent with detection when 2 delta^2 D(T) > 1, where D is the derivative-kernel of the window RKHS.
The N -> inf limit of the offset is NOT determined; it is <= 0.18 (T0 = 100) and <= 0.16 (T0 = 1000) and still decreasing. | **evidence:** Outputs:
- detect_convN15.json (a16707e9...7388)
- detect_convN_T100.json (c34270f1...b989)
- detect_convN_T100_s3.json (6e774310...0fc82)
- detect_convN_T1000_s2.json (df3bf971...2e48)
- detect_convN_T1000_s3.json (a1ff950d...f429)
analyze_nyquist.py gives the fits and the lambda0-collapse slopes, e.g. 39.8, 85.4, 36.5, 47.6 per unit L at T0 = 100, 200, 500, 1000. | **prior_art:** Landau-Widom plunge, as used by Zhu Sec. 9/12 and ACL Sec. 2.5, is the analogous mechanism for the profile. I found no prior detection-offset measurement.
- **id:** C4-D3 | **status:** NUMERICAL-NONRIGOROUS (asymptotic archimedean symbol, error O(log T/T); prime phases in 60-digit arithmetic) | **statement:** Growth regime at large heights. L* stays near L_flat while L_N grows like (1/2)log T.
T0 = 1e6, 1e8, 1e10, with zeros located by mpmath:
- delta = 0.49: L* = 2.839, 3.061, 3.302 (L_N = 5.99, 8.29, 10.59).
- delta = 0.2: L* = 4.611, 5.570, 6.259.
T0 = 1e12, 1e15, 1e20, 1e30, 1e50, at arbitrary decimal heights:
- delta = 0.49: L* = 3.586, 3.669, 3.997, 4.408, 4.883.
- L_flat = 3.545, 3.749, 4.016, 4.399, 4.890.
- L_N = 12.90, 16.35, 22.11, 33.62, 56.65.
|L* - L_flat| <= 0.30 (1e12), 0.26 (1e15), 0.06 (1e20), 0.08 (1e30), 0.04 (1e50).
The single Theorem-B test function e^{-iTx} sinh(delta x) is nearly optimal: L_sinh - L* is in [0.001, 0.06].
Deviations from L_flat are explained by the local window symbol. At L*: Psi_eff = 7.2-11.0 vs log(T/2pi) = 11.98 at 1e6; 14.1-15.2 vs 16.58 at 1e8; 18.9-19.9 vs 21.19 at 1e10. | **evidence:** Outputs:
- detect_highT.json: sha256 04d7ae79637fa4e2bc37bcfb1025a361906d9cb4cac5aad5b4d96000d78ce806, 40 s.
- detect_ultra.json: 6a15e0dbb452d0b531b82ed8d264ace5c6b4c2ec10a5567fec04a6e8025008af, 140 s.
- psi_eff_diag.json: b9e1ac4cec0e88ec192cdf2b08ca15222a03465e44c14e094e4d3a4b4e3ad8e9.
The asymptotic vs exact archimedean matrices differ by 1.8e-3 (T=1e4) and 3.1e-4 (T=5e4) in max-entry, and lambda_mod changes in the 3rd-4th digit. The approximation is used only for T0 > 1e5.
Neighbours at 1e6, 1e8 and 1e10 come from mpmath siegelz sign changes (non-rigorous). | **prior_art:** None found.
- **id:** C4-D4 | **status:** NUMERICAL-NONRIGOROUS | **statement:** Sensitivity to the local zero configuration (collision variant). If the quadruple replaces its two neighbouring zeros, so that the zero count is preserved, thresholds drop substantially:
- T0 = 100: L* = 1.433 (delta = 0.01) ... 1.089 (0.49), vs additive 1.711 ... 1.545, with L_N = 1.384.
- T0 = 1000: 2.597 ... 1.875.
- T0 = 1e4: 3.715, 3.656, 3.265, 2.837, 2.615, 2.427, 2.349, 2.287 for delta = 0.01..0.49 (L_N = 3.686).
The gap left by the displaced zeros acts as a locally undersampled region. Any locality or blindness statement must therefore include the local real-zero configuration around T, as hypothesis R does. A single height-only law cannot be exact. | **evidence:** detect_collision.json, sha256 bb0a0e60db9445a1e9390a5b1289ef613fbc9127dee0096dd55ee18ae95b7383, 44 s. | **prior_art:** C1 used the same collision model for Li coefficients.
- **id:** C4-H | **status:** HEURISTIC + CONJECTURE | **statement:** Two-regime law (HEURISTIC, supported by C4-LAT, C4-B and C4-D1..D4):
  L*(T, delta) ~ min{ L_N(T) + c(T) + b(T) ln(1/delta), L_loc(T, delta) },
where L_loc solves sinh(2 delta L)/(2 delta) - L = Psi_eff(T, L)/2 and Psi_eff ~ log(T/2pi) + (local prime-comb fluctuation, relative size ~ L/log T).
The governing parameter is kappa = delta log(T/2pi) = 2 pi delta/(mean spacing), with crossover kappa_c = 2.1773.
Mechanism in the Nyquist regime: detection iff 2 delta^2 D(T) >~ 1, where D(T) = sup_{h(T)=0} |h'(T)|^2/P(h). D explodes doubly exponentially once T is inside the undersampled band.
CONJECTURE: for the true infimum (N -> inf), 0 <= c(T) <= 0.1 and b(T) -> 0 slowly. In addition |L* - min(L_N, L_flat)|/L_N -> 0 as T -> inf for every fixed delta. This is the lattice limit, with the edge cost from growing zero density as the only correction. | **evidence:** Small-delta expansion (derived here): W = P + 2|C|^2 - 2|S|^2 with C ~ h(T) and S ~ -i delta h'(T). It predicts the measured relation b ~ 2/(d ln(1/lambda0)/dL) (C4-D2) and the delta^2 L^3 law (flat model, delta L << 1).
C4-LAT gives c = b = 0 exactly for a lattice. The finite-N trend (C4-D2) is towards smaller c and b. | **prior_art:** Zhu Sec. 9 (resolution height); ACL Sec. 8.7 (undersampling deficit lambda^2 at t = 2 pi lambda^2).
- **id:** C4-REL | **status:** HEURISTIC (bridge proposal; not a statement about integrated results) | **statement:** Relevance to the host repository's operator route (CURRENT_RESULTS Sec. 7; OPEN_CUTS Sec. 3):
(1) Any rigorous continuum LOWER certificate at window L must resolve lambda_min(L). That margin collapses doubly exponentially: 1.7e-17 at L = 0.8, 6e-30 at 1.0, 8e-49 at 1.2 (C4-P; Zhu). Positive Galerkin matrices approach from above and certify nothing, as the repository already says.
(2) 'Which windows control which heights' depends on delta. A window L is sensitive to large-delta defects at all heights up to doubly exponential T, so no window is height-local for them. For near-line defects (delta log(T/2pi) < 2.18) only windows with L >~ (1/2)log(T/2pi) + O(0.2) see height T. An 'unbounded prescribed family of full windows' meant to exclude near-line zeros up to height T must therefore reach L ~ (1/2)log(T/2pi). No height-locality shortcut was found.
(3) C4-C is the zeros-side counterpart of the repository's completed-square Schur matrix S_L. | **evidence:** Combines C4-P, C4-B, C4-B2, C4-D1, C4-D2 and C4-LAT. Any use in the repository requires its own review. | **prior_art:** Zhu 2026, Thm 1.4 (certificate barrier T1 = 2 pi e^{A_L}). Host repository CURRENT_RESULTS Sec. 7, read for context only.

## Failed attempts and negative results

- Plan to compute lambda_min(L) for L in [0.1, 3] in double precision: infeasible. lambda_min falls doubly exponentially (1.7e-17 at L=0.8, 8e-49 at 1.2). Double precision resolves nothing beyond L ~ 0.6. The profile was computed with Arb at 200-560 bits up to L=1.2 only; L=3 would need dimension ~5e3 at ~1e3 digits.
- BUG (fixed): the first float64 archimedean integral used one large Gauss-Legendre panel. Nodes near y=0 suffer cancellation, giving moment errors of 6e-11 and a spurious POSITIVE eigenvalue floor of ~1.4e-11 at L>=1. The opposite failure (spurious negatives) is documented by Zhu. Replaced by a composite panel rule; float64 is still unusable below ~1e-10 (spurious -7e-11 seen).
- Performance trap: multithreaded OpenBLAS made tiny matrix products ~30x slower while another process ran. All runs pinned to 1 BLAS thread.
- First very-large-height run crashed at T0=1e15: spherical_jn at |argument| ~ 1e16 for the -T0 mirror pair returned non-finite values, and eigvalsh failed. Fixed by dropping the mirror pair, whose terms are bounded by Ac^2/(2T0^2).
- My first flat-model derivation had a factor-2 error, mixing the real two-sided and complex one-sided normalisations. The correct criterion is sinh(2 delta L)/(2 delta) - L > Psi0/2. It was confirmed numerically (check_flat_lattice.json).
- Mistake caught: I first placed the lattice-model test function sin(pi(r-lambda0)/s)k(r) with its maximum at the injected midpoint, which gives a POSITIVE quadruple term. The correct construction needs the extra factor (r - T0).
- Assumed N-convergence of Nyquist-regime thresholds: wrong. Each refinement (N x1.5, x2, x3) lowers L* by 0.03-0.15; growth-regime thresholds are stable. Nyquist-regime numbers are upper bounds; the N -> inf offset is not determined.
- Theorem A (RH implies lambda_min(L) > 0, via Beurling sampling) was planned as new. It is Zhu 2026 Prop 2.3 (same proof), so it is reported as IMPORTED.
- No rigorous interpolation-regime detection theorem (small delta, L ~ L_N + C) was obtained. Zhu's canonical-product construction (his Thm 1.3) runs at half saturation, T = 2 pi e^L. Adapting it would at best give detection for L >= log(T/2pi), twice the Nyquist window. Not carried out.
- Rigorous Theorem C4-B pays a factor (1 + 1.41L) over the flat criterion, from bounding int F' S with Trudgian's S(t) bound. Integrating by parts once more with S_1(t) would cost an L^2 factor instead; not pursued.
- A single height-only locality law is impossible. The additive and collision injection models differ by up to 0.8 in L*, so locality statements must involve the local zero configuration (hypothesis R).
- Literature: Yoshida 1992 was not accessed in full (zbMATH review and Bombieri's account only). The Bombieri 2003 CPAM paper was not accessed.

## Code

- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality/weil_core.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality/hp_core.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality/exp_lambda_profile.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality/hp_spectral_check.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality/detect_lib.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality/exp_detect.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality/exp_detect_ultra.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality/psi_eff_diag.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality/check_flat_lattice.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality/thmB_bound.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality/summarize_detect.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality/analyze_nyquist.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality/make_tables.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/lambda_profile_main.json (sha256 1dcdd50d1a44d8885df884bfdbf13a3c18993e551d9ab6e7afef2f9625c69b79)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/hp_spectral_check.json (sha256 1a99c939f35df9da1a3e0cdd4f0e98ccacf3b12fd86dfc13e87aeed90ac29b5b)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/detect_lowT.json (sha256 0768eb39e5f1288c8c0bbdda33384c41ff570312e0c8d3a5ed77722b7df9fb0e)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/detect_midT.json (sha256 3a3342044e69e22150cdf0044a68b4d3f50f9073a611ef17e3ff857aed184519)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/detect_highT.json (sha256 04d7ae79637fa4e2bc37bcfb1025a361906d9cb4cac5aad5b4d96000d78ce806)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/detect_ultra.json (sha256 6a15e0dbb452d0b531b82ed8d264ace5c6b4c2ec10a5567fec04a6e8025008af)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/detect_convN15.json (sha256 a16707e953e04a5380381fa5a8ad2a50a314445a1250d9109feccf85eafb7388)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/detect_convN_T100.json (sha256 c34270f1af8fd95468dbbe78c5b270bfd695e9c50b9fbb86082f8540bbb4b989)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/detect_convN_T100_s3.json (sha256 6e7743109863209e3113a3b05625488e4dcc8de30a6b7f44fd73177396e0fc82)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/detect_convN_T1000_s2.json (sha256 df3bf97169f0830e5d2f9d2679a78e925622c9f613cf0b13b921694db32b2e48)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/detect_convN_T1000_s3.json (sha256 a1ff950dea31dbca647e16786b50ab7e78475bc6250622b16515f147a631f429)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/detect_collision.json (sha256 bb0a0e60db9445a1e9390a5b1289ef613fbc9127dee0096dd55ee18ae95b7383)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/check_flat_lattice.json (sha256 addf226e55dd95b12a16c2b00e34ed2e385368ccedeafe715626eb916c9ff55c)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/thmB_table.json (sha256 3e6ee84ef06fa951f57833e9c0eb98730ec80a2be899da6712d33d1de580eb50)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/psi_eff_diag.json (sha256 b9e1ac4cec0e88ec192cdf2b08ca15222a03465e44c14e094e4d3a4b4e3ad8e9)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/tables_C4.md (machine-generated; sha256 5a12131922c1f185256b3c94280acf806127ce3f0359246be447a97278111837)`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/manifest_C4.json (versions: python 3.13.18, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, python-flint 0.9.0; per-file sha256 and runtimes)`

## Open questions

- Interpolation-regime detection theorem: under H1 (and RH for the other zeros), prove detection for every delta > 0 once L >= (1/2)log(T/2pi) + C. This would need a full-saturation (Landau-Widom-type) construction, beyond Zhu's half-saturation canonical product. Is C absolute, and does it tend to 0?
- Prove hypothesis R (the local resolvent bound) for the zeta zeros in the sampling regime T >= (1+c) 2 pi e^{2L}, or find heights where it fails badly. Prime-comb alignment (sup = A_L ~ 4e^L) can push the local symbol Psi_L(T) far below log(T/2pi). Without R the 'blindness' half of locality is only heuristic.
- What are the N -> inf limits of the Nyquist-regime offset c(T) and the log(1/delta) slope b(T)? Current upper bounds: c <= 0.18 (T=100), <= 0.16 (T=1000), still decreasing. Do they vanish as T grows, as in the lattice model?
- Remove the single-defect hypothesis H1 in Theorem C4-B. A localised version needs no other off-line zeros within about (log T)^{C/delta} of T (sketch only). A version using the zero of maximal real part in a neighbourhood is open.
- Relation between detection near T* = 2 pi e^{2L} and ACL's observation that the window ground state reproduces zeta zeros up to about 2T*. Does a window 'reconstruct' heights it cannot 'detect' off-line defects at?
- Can the factor (1 + 1.41L) in Theorem C4-B be removed using integrated S_1(t) bounds or a smoother test window? That would bring the rigorous window to the flat prediction u*(kappa)/(2 delta).
- Bridge question for the repository's energy-Schur route (CURRENT_RESULTS Sec. 7, OPEN_CUTS Sec. 3): is there any family of windows sparser than L ~ (1/2)log(T/2pi) that controls near-line (kappa < 2.18) zeros at height T? The present evidence says no.

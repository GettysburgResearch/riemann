<!-- materialized from workflow result: campaigns / inv:C3-failure-anatomy -->
# C3-failure-anatomy — investigator report (materialized from structured return)

## Investigator notes / header

NOT WRITTEN. The harness refused the write of /home/user/riemann/research/exploratory/riemann-observatory/proposals/independent_campaigns/C3-failure-anatomy/REPORT.md ("Subagents should return findings as text, not write report files"). I respected the refusal and did not route around it. The full report is in the claims, failed_attempts and open_questions fields.

The hash manifest (data, not a report) is /home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C3-failure-anatomy/manifest_C3.json (sha256 a3a6c38064d0fac02a4cb7219ed2d0bca27f0285043072a3290470680d717e8e).

HEADER.

Status: EXPLORATORY dossier; no claim about RH. It contains:
- four elementary results with complete proofs, labelled THEOREM: C3-A1, C3-Q1, C3-M1, C3-CG1;
- one PROPOSITION-PROOF-SKETCH: C3-O1;
- NUMERICAL-RIGOROUS replays (Arb balls or exact integer arithmetic);
- IMPORTED literature statements;
- a methodological taxonomy (F1-F15) and a 20-item checklist. These are classifications, not theorems.

Scope: 14 dossiers.
- de Branges positivity and Conrey-Li 2000.
- X.-J. Li 2008.
- Atiyah 2018.
- Bender-Brody-Mueller 2017 with Bellissard's comment, the BBM reply and Liu 2026.
- Turan's partial-sum hypothesis (Spira, Montgomery, Platt-Trudgian).
- Mertens and Stieltjes.
- Polya, plus Turan's T(x).
- Cramer's model and Maier.
- The mollifier ceilings of Hardy-Littlewood, Selberg and Levinson-Conrey.
- Three arXiv claims from 2018-2026: Oliva 1807.06447 (proof, then disproof, then withdrawn); Queme 2004.00460 (author-flagged irrecoverable error); Micheas 2607.04338 (withdrawn).
- Corrections to published explicit constants: Turing->Lehman; Cheng-Graham Kusmin-Landau 1/pi vs 2/pi -> Hiary-Patel-Yang; Ford 2002 Theorem 4 8.463 -> 8.464; the gap in Feng 2012 and its repair by Pratt-Robles; Pearce-Crump 2026 7% -> 6.78%.
- The Davenport-Heilbronn countermodel.

Exact sources or dependencies: listed per claim. The certified zero files are zeros_1_50000.tsv (sha256 6a7eb7ab...cc88) and zeros_50001_100000.tsv (494b5c10...5e5a). Campaign C2's zeta_19 and Davenport-Heilbronn witnesses were replayed with separate code; their numbers were not reused.

What was actually run: three scripts under experiments/code/C3-failure-anatomy/.
- liouville_mertens_sieve.py: exact sieve to 1e9, 153 s.
- conrey_li_debranges.py: Arb, K=2000 (16 s) and K=20000 (590 s).
- witnesses.py: sympy, mpmath and Arb; 8 sections; 193 s.

Smallest remaining gap:
(i) arXiv:0807.0090 v5-v10 (2024-2025) were not audited.
(ii) de Branges' manuscripts after 2004 were not audited against Conrey-Li.
(iii) Several primary texts were seen only through zbMATH reviews or secondary papers (L0/L0+): Turan 1948, Montgomery 1983, Maier 1985, Odlyzko-te Riele 1985, Haselgrove 1958, Turing 1953, Lehman 1970, Cheng-Graham 2004, Stieltjes 1885.
(iv) C3-O1 cites Littlewood's Omega+ theorem for theta(x)-x without re-proving it.

## Claims

- **id:** C3-D1 | **status:** IMPORTED (Conrey-Li IMRN 2000 no.18, 929-940; Zbl 0966.11039; arXiv:math/9812166, read at L1) + NUMERICAL-RIGOROUS replay | **statement:** de Branges positivity and Conrey-Li.

Setup (Conrey-Li Thm 1, 'essentially due to de Branges'). Let E be entire with no real zeros, |E(conj z)|<|E(z)| for Im z>0, conj(E)(conj z)=eps*E(z-i) with |eps|=1, and |E(x+iy)| strictly increasing in y>0.
- If Re<F(z),F(z+i)>_{H(E)} >= 0 for every F in H(E) with F(z+i) in H(E), then all zeros of E lie on Im z=-1/2.
- Moreover Re{conj(E)'(w)E(w+i)/(2 pi i)} >= 0 at every zero w.

Thm 2. If Re<F,TF>_{F(W)} >= 0 for all F, where T maps K(w,.) to K(w+i,.), then W extends to Im z>-1/2 with Re{W(z)/W(z+i)} >= 0.

Take xi(s)=s(s-1)pi^{-s/2}Gamma(s/2)zeta(s) and E(z)=xi(1-iz). The hypotheses on E hold unconditionally, and the conclusion is RH.

Exact failure: the necessary consequences fail. Each quantity below must be >= 0 and is negative.
- At rho_34=1/2+111.0295355431696745i: -Re{xi'(rho)xi(1+rho)} = -5.389100507182945e-69.
- Re{xi(1+282i)/xi(2+282i)} = -0.000131957.
- Chi_4 analogues: -2.310349004993483e-45 at 1/2+67.63692086354607i, and -0.000422340607 at t=8714.2.

So conditions (3.1), (3.3), (3.7) and (3.8) are false. Sarnak gives a numerics-free proof for the F(W) condition, for all Dirichlet L-functions, via density of the values of log zeta.

Category: F4, a sufficient condition strictly stronger than RH and false. The implication theorems themselves are correct.

Salvage: the Hermite-Biehler and de Branges-space structure remains a valid tool; this positivity condition is dead. | **evidence:** conrey_li_debranges.py at 192 bits; output conrey_li_debranges.json, sha256 4806263042595d74df77d928bdbe4b7c06f035f1fc1369b2cce3fd7aa7cbf80f.

Arb balls:
- [-5.389100507182945181443852872e-69 +/- 3.1e-121]
- [-0.000131957293372083440713 +/- 6.8e-56]
- chi_4 zero Krawczyk-certified in a box of radius 4e-56: [-2.31034900499348345618594357e-45 +/- 5.5e-98]
- [-0.000422340606580232770283 +/- 9.6e-55]

All four agree with the Mathematica values Conrey-Li print. | **prior_art:** de Branges, Bull. AMS 15 (1986) 1-17; JFA 107 (1992); JFA 121 (1994). Conrey-Li 2000, including Sarnak's remark. Lagarias, Acta Arith. 120 (2005), arXiv:math/0601653, on de Branges-type structure. de Branges' post-2004 manuscripts are unrefereed and not audited.
- **id:** C3-D1-scan | **status:** NUMERICAL-RIGOROUS (counts); PROPOSITION-PROOF-SKETCH (mechanism) | **statement:** Frequency of failure of the de Branges necessary condition -Re{xi'(rho)xi(1+rho)} >= 0 over the first K zeros:
- K=2000: fails at 195 zeros (9.75%).
- K=20000: fails at 2724 zeros (13.62%).
- No sign was undetermined in either run.
- The first failures are at n = 34, 71, 106, 127, 144, 173, 184, 186, 196, 233, ...; 34 is the first, matching Conrey-Li's choice.

The Thm 2 quantity Re{xi(1+it)/xi(2+it)} is negative on the grid t in [1,1000] (step 1/4) exactly at t = 282, 527.25, 527.5, 527.75, 836.5, 898.75, 899. This is grid information only.

Mechanism (PROPOSITION-PROOF-SKETCH). On the line, xi'(rho) = -i Xi'(gamma), so -Re{xi'(rho)xi(1+rho)} = -Xi'(gamma) Im xi(3/2+i gamma). Since Xi' alternates in sign at consecutive simple zeros, the condition forces sign(Im xi(3/2+i gamma_n)) to alternate in lockstep. That phase-locking has no arithmetic reason to hold. | **evidence:** conrey_li_debranges.json, sha256 4806263042595d74df77d928bdbe4b7c06f035f1fc1369b2cce3fd7aa7cbf80f.
conrey_li_debranges_K20000.json, sha256 a8af1a3814bb8583c9ba5925700ae04f46392d545517d9c91a8189695dd1fbee.
Zeros from flint.acb.zeta_zeros; 192-bit Arb; runtimes 16 s and 590 s. | **prior_art:** Conrey-Li give single witnesses only. No count of failures was found in our searches. This is 'possibly new' only as a statistic, not as an idea.
- **id:** C3-D2 | **status:** IMPORTED (L0+: blog comments and arXiv version history) | **statement:** X.-J. Li, arXiv:0807.0090, the 2008 text (v1-v3).

Claim: v1 says all nontrivial zeros lie on Re s=1/2. v2-v3 say Bombieri's refinement of Weil positivity is proved via Fourier analysis on number fields.

Exact failing steps, from public expert comments:
(a) Tao, 2 July 2008: 'the decomposition claimed in equation (6.9) on page 20 ... is, in fact, impossible; it would endow the function h ... with an extremely strong dilation symmetry which it does not actually obey'. This was fixed in v2/v3, as Tao agreed on 4 July.
(b) Connes: in Theorem 7.3 (p.29, the trace formula), h is extended 'from ideles to adeles by 0 ... and then using Fourier transform (see page 31). This cannot work and ideles form a set of measure 0 inside adeles'. Tao: 'The first concrete error here arises in the equation after (7.13)': a change of variables on the idele class group, with u integrated over the adeles.
(c) Tao, revised 7 July: p.18 needs 'certain invertibility properties of E which fail if there is a zero off of the critical line'. Also, a decomposition needs a subspace that is 'merely dense' to be the whole space.
(d) v4, 6 July 2008: 'withdrawn by author, due to mistake on page 29'.

STATUS NUANCE: the same identifier carries v5-v10 (4 Oct 2024 to 12 Oct 2025), a new argument via traces of an integral operator giving Li-criterion positivity. These have no journal-ref and no published critique was located. They were NOT audited. 'Withdrawn' applies only to the 2008 text.

Categories: F8 (null support), F3 (circular invertibility), F7 (dense taken as closed).

Salvage: Li's criterion and the Weil/Connes target remain; the 2008 argument does not. | **evidence:** arXiv abs page and the API metadata of all ten versions.
Tao blog 'Structure and randomness in the prime numbers', comment page 1 (fetched; sha256 b566f1f66afd4a99228d6966bdfaf49227c7e4608efcb87164a5bba742217400), comments of 2 July 8:28pm, 4 July 8:15am and the 7 July revision.
Woit, Not Even Wrong ?p=707 (sha256 3777081dfea461a3f0c1a8d1c81dbf76bd2de1b405f3e8dcdbc185ff8f17a3f2), quoting Connes. | **prior_art:** Connes, Selecta Math. 5 (1999), the trace formula Li adapts. Li, J. Number Theory 65 (1997), Li's criterion.
- **id:** C3-D3 | **status:** IMPORTED (preprint text, L1) + THEOREM (C3-A1) + public non-refereed critiques | **statement:** Atiyah 2018, 'The Riemann Hypothesis' (5 pp. preprint).

Claim:
1. Assume a zero b of zeta off the line; set F(s)=T{1+zeta(s+b)}-1, with F(0)=0 (3.2).
2. 'Take f=g=F in 2.6', where 2.6 is T{[1+f][1+g]}=T{1+f+g} for power series without constant term. This gives F=2F (3.3), so F==0.
3. 'T is not the zero polynomial and so it is invertible', hence zeta==0, a contradiction.

Exact failure:
(i) By C3-A1, 2.6 read literally forces T to be constant near 1. Then F==0 holds for every function, the step 'T invertible => zeta==0' is invalid, and constancy contradicts 2.5 (monotone with limit Zhe ~ 137 on the critical line) given 'T is a polynomial on compact convex sets'.
(ii) Under Atiyah's own remark that '2.6 is just the linear approximation', 3.3 does not follow.
(iii) Proves too much: 3.1-3.3 use only zeta(b)=0 and analyticity, never Re b != 1/2. Applied verbatim to the certified zero rho_1 = 1/2+14.134725141734693790i, the argument would show zeta has no nontrivial zeros, which is false.

Publication status: the 'fine structure constant' companion paper was not found in zbMATH or Crossref; only 'Arithmetic physics - Abel lecture' (Zbl 1442.11090). Atiyah died in January 2019.

Categories: F9, F2, F1. Salvage: none. | **evidence:** Preprint copy at sites.math.rutgers.edu/~zeilberg/akherim/atiyah_RH.pdf (sha256 55c05e2f923cea333e1ece1b654253984026d0c80ed128f971701ba1e4465f08); Sec. 2-3 read in full.
The sympy check is in witnesses.json section 'atiyah'. | **prior_art:** Lipton-Regan, Godel's Lost Letter, 2018-09-26 (fetched; sha256 e80696795506c3ff39fe19b9e0bb1a51cf235abace1ca790fe0f4805467c26a1): applied on an open region the identity 'entails that T must be linear', and no special property of zeta is used. They also relay Motl's objection that swapping on-line zeros for an off-line pair is invisible. Further discussion on r/math and MathOverflow (removed).
- **id:** C3-A1 | **status:** THEOREM (complete proof; exact sympy cross-check to degree 13) | **statement:** THEOREM. Let h be analytic at 0 with h(u+v+uv) = h(u+v) as formal power series in s for all u, v in s*C[[s]]. This is Atiyah's property 2.6 with h(w) := T(1+w). Then h is constant.

Proof.
1. Put u=v=s, so h(2s+s^2)=h(2s).
2. With h(w)=sum c_k w^k and (2s+s^2)^k = sum_j C(k,j) 2^{k-j} s^{k+j}, the coefficient of s^m in the difference is sum_{m/2<=k<=m-1} c_k C(k,m-k) 2^{2k-m}.
3. Its top term (k=m-1) is (m-1) 2^{m-2} c_{m-1}; the other terms involve c_k with k<m-1.
4. Induction on m>=2 gives c_{m-1}=0 for every m. Hence h == c_0 = T(1) = 1. QED | **evidence:** witnesses.py section 'atiyah': sympy solves the coefficient equations c_1..c_13 = 0 exactly.
witnesses.json sha256 7abd8ec7adb1260d7c117e895ad6568e5a9429364a8189e6706703649ada3ad6. | **prior_art:** Lipton-Regan 2018 remark that T 'must be linear' (from 2.7). Ours is the sharper 'constant' statement from 2.6. Elementary; not claimed new mathematics.
- **id:** C3-D4 | **status:** IMPORTED (L1 for Bellissard and the BBM reply; L0+ for Liu and Mueller 1704.04705) + NUMERICAL-RIGOROUS check | **statement:** Bender-Brody-Mueller 2017. PRL 118, 130201; arXiv:1608.03679v4.

Claim: H = (1-e^{-ip})^{-1}(xp+px)(1-e^{-ip}) has formal eigenfunctions psi_z(x) = -zeta(z,x+1), and the boundary condition psi(0)=0 holds iff zeta(z)=0. 'IF the analysis ... can be made rigorous to show that H is manifestly self-adjoint, then ... RH'. The BBM reply quotes the PRL: 'We are not able to prove that the eigenvalues of H are real'. This is a CONDITIONAL/HEURISTIC programme, not a claimed proof.

Critique (Bellissard, arXiv:1704.02644):
1. On L^2(0,inf) with the Dirichlet condition, p has deficiency indices (1,0), so no self-adjoint extension exists.
2. psi_z is not in L^2 for Re z = 1/2.
3. Weighted spaces L^2(x^alpha dx) shift the dilation generator by i(alpha+1)/2, moving the line.

BBM reply (arXiv:1705.06767): points 1 and 2 are already in the paper; the relevant inner product is biorthogonal or pseudo-Hermitian.

K. Liu (arXiv:2607.19067, 2026, unrefereed, abstract only): the completion of C_c^inf in BBM's metric eta = sin^2(p/2) is unitarily equivalent to L^2(R+), with purely absolutely continuous dilation spectrum, and 'Delta psi_z = x^{-z}, so for Re z=1/2 they do not belong to the completed space'.

Exact gap: no Hilbert space has been exhibited in which (i) H, or a closed extension, is self-adjoint and (ii) the psi_z with zeta(z)=0 are eigenvectors. The formal eigen-equation holds for EVERY complex z, so all the RH content sits in the missing inner product.

Category: F7. Salvage: heuristic only (the Berry-Keating 2xp limit and the PT viewpoint). | **evidence:** Arb Hurwitz zeta, witnesses.json section 'bbm'. |zeta(rho_1,x+1)|*|rho_1-1|/sqrt(x) = 1.00332, 1.000025, 1.00000025, 1.0000000025, 1.000000000025 for x = 1e2, 1e4, 1e6, 1e8, 1e10 (DLMF 25.11.43). Hence int_0^X |psi|^2 ~ X^2/(2|rho_1-1|^2), and psi is not in L^2(0,inf). | **prior_art:** Berry-Keating 1999 (H=xp); Connes 1999; Hu-Kim arXiv:1810.11662 (generalisation); Mueller arXiv:1704.04705 (a rigorous construction of a version of the operator).
- **id:** C3-D5 | **status:** IMPORTED + NUMERICAL-RIGOROUS witness | **statement:** Turan's partial-sum hypothesis.

Claim (Turan 1948, Danske Vid. Selsk. Mat.-Fys. Medd. 24 no.17; Zbl 0031.30204): if for all sufficiently large N, zeta_N(s) = sum_{n<=N} n^{-s} has no zero in sigma>1, then RH holds.

Refutation:
- Spira, Math. Comp. 22 (1968) 163-173: zeros in sigma>1 for N = 19, 22-27, 29-50.
- Montgomery 1983 (Studies in Pure Math., Mem. P. Turan, 497-506; Zbl 0518.10046), as stated by Platt-Trudgian: psi_N := sup{sigma : zeta_N(sigma+it)=0} = 1 + (4/pi - 1 - o(1)) loglog N/log N, with 4/pi - 1 best possible. So zeros exist in sigma>1 for ALL large N.
- Platt-Trudgian, LMS JCM 19 (2016) 37-41: there are no zeros in sigma>1 exactly for 1<=N<=18 and N = 20, 21, 28; for every other N there are infinitely many.

Category: F4. Truncations do not inherit RH. | **evidence:** Independent replay of C2's witness with separate code (witnesses.py 'turan', 128-bit Arb). A Krawczyk-certified zero of zeta_19 lies in [1.0010955115364762904215 +/- 2.2e-23] + [600884.2034277757127423323526 +/- 2.9e-23]i, and Re > 1 is certified.

Platt-Trudgian arXiv:1507.01340 was read at L1 for statements (sha256 2247e451...). Montgomery and Turan are L0. | **prior_art:** van de Lune-te Riele computed zeros for several N; Monach's thesis covers N>=51; Gonek-Ledoan IMRN 2010.
- **id:** C3-D6 | **status:** IMPORTED (Odlyzko-te Riele: Zbl 0544.10047 author review; Pintz: Zbl 0623.10031; Ingham: Zbl 0063.02974; Kim-Nguyen arXiv:2502.21021 L1; Hurst arXiv:1610.08551 L1; Stieltjes: JFM 17.0375.02, L0) + NUMERICAL-RIGOROUS | **statement:** Mertens and Stieltjes.

Mertens 1897: |M(x)| < sqrt(x) for x>1. This is REFUTED by Odlyzko-te Riele 1985: limsup M(x)x^{-1/2} > 1.06 and liminf < -1.009, non-constructively. Effective bounds on the first counterexample: Pintz 1987, exp(3.21e64); Kotnik-te Riele 2006, exp(1.59e40); Saouter-te Riele 2014, exp(1.004e33); Kim-Nguyen 2025, about exp(1.96e19). Hurst 2018: bounds -1.837625 and 1.826054, with M computed for all x <= 1e16.

Stieltjes 1885 (C. R. 101, 153-154): announced M(x)x^{-1/2} bounded. This is NOT refuted. It is open and believed false: Ingham 1942 showed it forces linear dependence of the ordinates, and under linear independence M(x)x^{-1/2} is unbounded both ways. The task premise 'Stieltjes/Mertens refuted' holds only for Mertens' constant-1 form.

Categories: F5, F4. Salvage: M(x) = O(x^{1/2+eps}) (equivalent to RH), the weak Mertens conjecture, and the lattice-reduction method. | **evidence:** Exact sieve to 1e9 (liouville_mertens_1e9.json, sha256 e3d0abe4e4852647ddaa649c31bc700ece8a01f7768b9824600a7188e753a2c7):
- M(10^k), k=1..9: -1, 1, 2, -23, -48, 212, 1037, 1928, -222.
- max M = 10246 at x = 903,087,703; min M = -8565 at x = 456,877,618.
- max over 1e4<=x<=1e9 of |M(x)|/sqrt(x) = 0.46416, at x = 179,919,749 (M = -6226).
- Over [200, 1e9] the maximum is 8/sqrt(200) = 0.5657, at x = 200.
Self-test against sympy up to 2e5. | **prior_art:** Kotnik-van de Lune 2004 heuristic growth sqrt(logloglog x)/2. Saouter-te Riele 2014.
- **id:** C3-D7 | **status:** IMPORTED + NUMERICAL-RIGOROUS (exact integers; fixed-point certificate for T) | **statement:** Polya's conjecture and Turan's T(x).

Polya 1919 (Jahresber. DMV 28, 31-40): L(x) = sum_{n<=x} lambda(n) <= 0 for x >= 2. This implies RH and simple zeros (Ingham 1942).

Turan: positivity of T(x) = sum lambda(n)/n for large x would imply RH.

Both were refuted by Haselgrove 1958 (Mathematika 5, 141-145; Zbl 0085.27102), non-constructively via Ingham's inequalities with computed zeta(2 rho) and zeta'(rho).
- Lehman 1960: L(906180359) = +1.
- Tanaka 1980: the smallest counterexample is 906150257.
- Borwein-Ferguson-Mossinghoff 2008 (Math. Comp. 77; Zbl 1198.11090): the smallest n with T(n)<0 is 72,185,376,951,205; L(n)<0 for 1e9 <= n <= 2e14; L(n) > 0.061867 sqrt(n) infinitely often.

Categories: F5, F4. Salvage: the Ingham-Haselgrove oscillation method. | **evidence:** Exact sieve to 1e9:
- L(x) <= 0 for 2 <= x < 906,150,257, and L(906,150,257) = 1 (Tanaka confirmed).
- L(906,180,359) = 1 (Lehman confirmed).
- L(x) > 0 for exactly 305,426 integers x <= 1e9; the last is 906,488,079; max L = 829 at 906,316,571; L(1e9) = -25,216.
- T(x) >= 1.4205e-6 > 0 for all 1 <= x <= 1e9. The certificate is sum lambda(n) floor(2^56/n) - x >= 102,357,542,618 > 0. The minimum is about 1.42684e-6 near x = 456,877,629 (float), beside the minimum of M at 456,877,618.
Output sha256 e3d0abe4e4852647ddaa649c31bc700ece8a01f7768b9824600a7188e753a2c7; 153 s. | **prior_art:** Haselgrove 1958; Lehman 1960 (Zbl 0103.03204); Tanaka 1980 (Zbl 0446.10004); BFM 2008.
- **id:** C3-D8 | **status:** IMPORTED (Maier review L0+; BFT L1) + PROPOSITION-PROOF-SKETCH | **statement:** Cramer's model and Maier's theorem.

Cramer 1936 (Acta Arith. 2, 23-46): the events n in C are independent with probability 1/log n.

Model prediction (PROPOSITION-PROOF-SKETCH, by Chernoff and Borel-Cantelli): almost surely #C cap (x, x+(log x)^lambda] ~ (log x)^{lambda-1} for all large x, when lambda > 2.

Maier 1985 (Michigan Math. J. 32, 221-225; Zbl 0569.10023): for every lambda > 1, pi(x+(log x)^lambda) - pi(x) = (log x)^{lambda-1} + Omega_pm((log x)^{lambda-1}). The model's analogue fails for primes at every lambda > 1.

Cause (Banks-Ford-Tao, Invent. Math. 233 (2023), arXiv:1908.08613 Sec. 1.1-1.2): the model is equidistributed mod p while primes are biased; for example it predicts x/log^3 x triples n, n+1, n+2. Granville's corrected model gives a largest gap of at least 2e^{-gamma}(log x)^2 = 1.1229(log x)^2.

This is not an RH proof attempt. It is included because random-model and RMT heuristics are routinely cited as if they were evidence about individual zeros.

Category: F12. Salvage: refined models (Granville; BFT). | **evidence:** zbMATH review of Maier; Banks-Ford-Tao text (sha256 ce04b3c9...). Granville 1995 (Zbl 0833.01018): the PDF is image-only and was not read. No computation can test an Omega_pm statement, and none was run. | **prior_art:** Granville 1995; Pintz on flaws of Cramer's model (cited in BFT); Soundararajan's survey.
- **id:** C3-D9 | **status:** IMPORTED (Conrey: Zbl 0668.10044; Farmer: Zbl 0783.11031; Selberg: Zbl 68.0161.01; Hardy-Littlewood: JFM 48.0344.03; PRZZ arXiv:1802.10521 L1 for its Sec. 1; 2026 items at L0+) | **statement:** The ceilings of mollifier methods (Hardy-Littlewood, Selberg, Levinson-Conrey).

The chain of results:
- Hardy-Littlewood 1921: N_0(T) > KT, which is proportion 0.
- Selberg 1942: a positive proportion.
- Selberg's method alone gives more than 6.78% (Pearce-Crump 2609.15329v2; v1 said 7%).
- Levinson 1974: more than 1/3.
- Conrey 1989: theta = 4/7 - eps gives kappa > 0.4088.
- BCY 2011: 0.4105. Feng 2012: 0.4128, with a gap; see C3-D13.
- PRZZ 2020: more than 5/12.
- Farmer 1993: the 'Theta = infinity conjecture', that the mollified mean-square formulas hold for all fixed Theta.

Exact ceilings:
1. kappa(theta) < 1 for every proven length theta: theta < 4/7 for Conrey coefficients, < 17/33 for arbitrary coefficients (Bettin-Chandee-Radziwill).
2. Even Theta = infinity gives only N_0(T) >= (1-o(1))N(T), which allows o(N(T)) off-line zeros.
3. The method counts zeros of an auxiliary combination via Littlewood's lemma and convexity. It never excludes an individual zero.

Unrefereed 2026 results by other mechanisms: Alpoge-Furman 2608.13637 (Claude) and Lamzouri 2609.02882, at least 2/3 simple and critical; B. Wang 2609.24167 improves this by delta_0 = 6.67e-8, with the comment 'New method is need[ed]'. Even 100% is not RH.

Category: F13. The theory itself is valid. | **evidence:** zbMATH reviews and the PRZZ introduction; arXiv metadata of the 2026 items. | **prior_art:** Conrey 1989; Farmer 1993; Bettin-Chandee-Radziwill (Crelle); PRZZ Res. Math. Sci. 7 (2020).
- **id:** C3-D10 | **status:** IMPORTED (status and text, L1) + PROPOSITION-PROOF-SKETCH (C3-O1) + NUMERICAL-NONRIGOROUS illustration | **statement:** Oliva, arXiv:1807.06447.

Status:
- v1 (2018-07-14): a proof of RH via Nicolas' inequality.
- v2 (2018-09-03): a DISPROOF, using the same criterion.
- v3 (2018-09-05): 'Withdrawn for expected critical errors in both versions'.

v1 claim: if n is a large counterexample to N_n/phi(N_n) > e^gamma loglog N_n (N_n the primorial), then so is n+1. With Nicolas' dichotomy, this would give RH.

Failing step (C3-O1): step (3), (1-1/p) loglog N_{n+1} >= loglog N_n with p = p_{n+1}.
(a) The function h(L) = (1-1/p) log L - log(L - log p) is decreasing in L = log N_{n+1}, so substituting Dusart's LOWER bound makes (3) easier: (4) does not imply (3). The paper's 'Lemma 2.2' ('for fixed b, eventually increasing in x') is applied with b ~ x, but f' changes sign only at x ~ (1.05-1.12) b log b.
(b) To first order, h = [-(1+log p)E + (1/2)(log p)^2]/p^2 with E = theta(p) - p. So (3) is equivalent to E <~ (1/2) log p, and by Littlewood's Omega+ for theta(x) - x it fails infinitely often.
(c) Nevertheless h > 0 for all p <= 2e7, since theta(p) < p there: the lemma is 'numerically true' and false infinitely often.
(d) Given Nicolas' dichotomy, the propagation lemma is itself equivalent to RH.

Categories: F10, F6, F5, F3, F15. | **evidence:** witnesses.py 'oliva' (sha256 of witnesses.json 7abd8ec7...):
- min h = 1.2508e-10 at p = 17,991,383; all h > 0 for p <= 2e7; max theta(p) - p = -1.21 (float64).
- The first-order law has median relative error 3.3e-4 for p > 1000.
- 60-digit mpmath turning points of f' in 'Lemma 2.2', x/(b log b) = 1.120, 1.085, 1.066, 1.046 for b = 1e4, 1e6, 1e8, 1e12; f' < 0 at x = b.
v1 text sha256 16ee55e7... | **prior_art:** Nicolas 1983 (the criterion and its dichotomy); Littlewood 1914 (Omega+ for theta(x)-x); Dusart arXiv:1002.0442.
- **id:** C3-D11 | **status:** IMPORTED (text and status, L1) + THEOREM (C3-Q1) + NUMERICAL-NONRIGOROUS illustration | **statement:** Queme, arXiv:2004.00460.

Status: v2 (2020-05-15) has the comment 'This paper contains an irrecoverable error paragraph 6 page 4'. The v1 footnote invites readers to locate the error, which is exemplary.

Claim:
1. Let rho be a zero of maximal real part in Omega_T and f = zeta'/zeta; then f(rho+eps) ~ 1/eps.
2. f is analytic in D(rho + eps/2 + v, v), so f(rho+eps) = sum_k (-(v-eps/2))^k f^(k)(c_0)/k!.
3. As eps -> 0 this tends to sum_k (-1)^k v^k f^(k)(rho+v)/k!, 'which is finite': a contradiction.

The failure is C3-Q1, and it lies exactly in item 6 on page 4. Also proves too much: the same steps exclude the on-line zero rho_1, whose right-hand disc is zero-free.

Categories: F6, F2. | **evidence:** mpmath at 40 digits (witnesses.json 'queme'): |(-v)^k f^(k)(rho_1+v)/k!| -> 0.6667 = 1/v for k <= 26; eps*|f(rho_1+eps)| = 0.99595, 0.99996, 0.9999996 for eps = 1e-2, 1e-4, 1e-6. v1 sha256 938548dc... | **prior_art:** Standard complex analysis: Cauchy-Hadamard and Abel's theorem.
- **id:** C3-Q1 | **status:** THEOREM (complete proof) | **statement:** THEOREM. Suppose f is meromorphic, analytic on the open disc D(rho+v, v), and has a pole at rho. Then the series sum_k (-v)^k f^(k)(rho+v)/k! diverges.

Proof.
1. The radius of convergence of the Taylor series at rho+v is exactly v, since a singularity lies on the boundary.
2. If the series converged at rho, Abel's theorem along the radius would give lim_{r->1-} f(rho + v(1-r)) as its sum. But f(rho+delta) ~ m_rho/delta -> infinity. Contradiction. QED

Explicit model: for g(z) = 1/(z-rho), every term equals 1/v, while for eps > 0 the series at rho+eps sums to 1/eps. Hence the termwise eps -> 0 limit in Queme's step 6 is illegitimate. | **evidence:** The proof above. Numerical corroboration in witnesses.json 'queme' (non-rigorous). | **prior_art:** Textbook (Ahlfors). The observation is not new; it is the explicit mechanism behind the author's self-reported error.
- **id:** C3-D12 | **status:** IMPORTED (status; v1 Sec. 1 and Thm 1 read at L1) + THEOREM (C3-M1) | **statement:** Micheas, arXiv:2607.04338.

Status: v2 (2026-07-08) reads 'Mistakes in main approach. Withdrawn'.

v1 Theorem 1: for every sequence tau_n with
- (C1) strictly increasing and positive,
- (C2) tau_n -> infinity,
- (C3) sum tau_n^{-2} < infinity,
- (C4) |tau_n - t_n| <= b_n, where t_n are the true ordinates,
- (C5) b_n decreasing to 0,
the product xihat(s) = (1/2) prod (1 - s(1-s)/(1/4 + tau_n^2)) equals xi(s) on the strip (eq. 17), and RH follows.

This is false by C3-M1. Category: F11 with F2. Product formulas take the zeros as input and cannot locate them. Salvage: none.

The archive's other Hadamard-product item, Liu arXiv:2404.06306 (an unrefereed disproof), was NOT audited. | **evidence:** v1 text sha256 3b4a5a9f...; arXiv metadata for v1 and v2. | **prior_art:** Hadamard 1893; the general principle that the functional equation plus the product formula cannot locate zeros (cf. Davenport-Heilbronn).
- **id:** C3-M1 | **status:** THEOREM (complete proof) + NUMERICAL-RIGOROUS illustration | **statement:** THEOREM. Micheas' Theorem 1 (v1) is false, independently of RH.

Proof.
1. Take b_n = 1/n and tau_n = t_n - 1/(2n), with t_n nondecreasing.
2. (C1) holds since tau_{n+1} - tau_n >= 1/(2n) - 1/(2n+2) > 0. (C3) holds since tau_n >= t_n - 1/2 and sum t_n^{-2} < infinity.
3. Let s_0 = 1/2 + i t_1, a zero of xi. Then s_0(1-s_0) = 1/4 + t_1^2, and the n-th factor at s_0 is (tau_n^2 - t_1^2)/(1/4 + tau_n^2).
4. For n=1 the factor is (1/4 - t_1)/(1/4 + tau_1^2), which is nonzero.
5. For n>=2, tau_n >= t_2 - 1/4 = 20.77 > t_1, so the factor lies in (0,1).
6. sum |1 - factor_n| = sum (1/4 + t_1^2)/(1/4 + tau_n^2) < infinity, so the product converges absolutely to a NONZERO number.
7. Hence xihat(s_0) != 0 = xi(s_0), contradicting eq. (17). QED | **evidence:** Arb partial products at s_0 using certified t_n (witnesses.json 'micheas'): -0.0745866 (N=1), -0.0026322 (N=100), -0.0016309 (N=1e3), -0.0014508 (N=1e4), -0.0014185196361316 (N=1e5). | **prior_art:** None specific. Elementary.
- **id:** C3-D13 | **status:** IMPORTED (Trudgian 0903.1885 L1; HPY 2207.02366 L1; Ford 1910.08205 v1/v5 L1; PRZZ 1802.10521 L1 for its p.8 and Sec. 5; Pearce-Crump L0+) + THEOREM (C3-CG1) | **statement:** Errors in published explicit constants, and their corrections.

(a) Turing 1953 -> Lehman 1970. Trudgian, Math. Comp. 80 (2011): 'Turing's paper contains several errors, which are fortunately corrected by Lehman'. Lehman also corrected Titchmarsh's explicit Riemann-Siegel error term. The constant 168 pi in the Turing and Lehman triples 'seems to be a misprint'. Rumely's 1.1242 'is a result of a rounding error from his Lemma 2'.

(b) Cheng-Graham 2004 (RMJM 34; Zbl 1062.11056), Lemma 2: S <= 1/(pi theta) + 1. The sharp Kusmin-Landau constant is 2/pi (Landau: S <= cot(pi theta/2), attained). Reported by K. Ford and J. Arias de Reyna. HPY 2022 (arXiv:2207.02366): 'The incorrect constant 1/pi has impacted all published explicit subconvex bounds on |zeta(1/2+it)|'. Hiary 2016's 0.63 t^{1/6} log t becomes 0.77, and HPY recover 0.618 t^{1/6} log t for t >= 3. Explicit witness: C3-CG1.

(c) Ford 2002 zero-free regions (arXiv:1910.08205; v1 is the published text, v2-v5 are the author's corrections 2022-2025). Fixes: the proof of (1.6), taken from Cheng-Graham ('Lemma 3 is false'); the proof of Lemma 3.2; formula (7.3); the numerics (8.8) and (8.9); the argument after Lemma 9.2. Theorem 4 changes from 1/(8.463 log|t|) to 1/(8.464 log|t|). The numerics of Theorems 2-3 change; Theorems 1 and 5 (57.54) are unchanged.

(d) Feng 2012 (JNT 132): kappa > 0.4128 used theta_F = 1/2. PRZZ: 'a gap was found in Feng's argument which reduces the size to 3/7' (giving 0.4107); Pratt-Robles 2018's theta_F = 6/11 'thereby validat[es] Feng's claim'. Feng's statement on square-free terms was 'not substantiated' until PRZZ Sec. 5.1.

(e) Pearce-Crump arXiv:2609.15329 (unrefereed): v1 '7%' became v2 '6.78%', with the comment 'Corrected proportion'.

Category: F14. | **evidence:** Fetched texts: Trudgian sha256 e8d021a3...; HPY b4cc7b26...; Ford v5 df92c2e7..., v1 cf695a47...; PRZZ 147187ac... Ford's version comments come from the arXiv API. | **prior_art:** Kusmin 1927; Landau 1928; Lehman, Proc. LMS 20 (1970) 303-320 (Zbl 0203.35502); Patel arXiv:2009.00769; Pratt-Robles, Res. Number Theory 4 (2018).
- **id:** C3-CG1 | **status:** THEOREM (explicit counterexample, Arb-certified) | **statement:** THEOREM (certified computation). Cheng-Graham's Lemma 2, as stated by HPY, is false. The lemma says: if f' is monotone and continuous with theta <= f' <= 1-theta on [a,b), then |sum_{a<=n<b} e(f(n))| <= 1/(pi theta) + 1.

Counterexample:
- theta = 0.02, w = 0.05, f(x) = theta x + (1-2 theta) w log(1 + e^{(x-1000)/w}).
- Then f' = theta + (1-2 theta) sigmoid((x-1000)/w) is continuous and strictly increasing, with theta < f' < 1-theta.
- The sum runs over n in [975, 1025].

Result: |S| = 31.59808527367395444... It exceeds 1/(pi theta) + 1 = 16.9154943... and is below Landau's sharp bound cot(pi theta/2) = 31.8205159..., as it must be. | **evidence:** witnesses.py 'chengraham', 128-bit Arb; |S| ball radius 3e-34. witnesses.json sha256 7abd8ec7adb1260d7c117e895ad6568e5a9429364a8189e6706703649ada3ad6. | **prior_art:** Landau 1928 extremal examples. HPY 2022 and Ford already establish the error; we add only an explicit smooth instance.
- **id:** C3-D14 | **status:** NUMERICAL-RIGOROUS + IMPORTED (functional equation: Titchmarsh 10.25) | **statement:** The Davenport-Heilbronn countermodel (support for F1).

f(s) = sum a(n) n^{-s}, with a(n) of period 5 taking the values (1, kappa, -kappa, -1, 0), where kappa = (sqrt(10-2sqrt5) - 2)/(sqrt5 - 1) = 0.28407904384041229603.

It satisfies a Riemann-type functional equation (Titchmarsh Sec. 10.25) but has a zero off the line, Krawczyk-certified in [0.80851718245663738555 +/- 5.4e-28] + [85.69934848537759217193 +/- 2.1e-28]i, with Re - 1/2 >= 0.3085.

Any argument that uses only the functional equation, the Gamma factor and analytic continuation proves too much. | **evidence:** witnesses.py 'dh': Arb Hurwitz zeta, with the derivative via acb_series. This is an independent replay of C2's dh_zeros.json with separate code. | **prior_art:** Davenport-Heilbronn 1936; Titchmarsh; Spira and Balanzario-Sanchez-Ortiz on DH zeros.
- **id:** C3-TAX | **status:** HEURISTIC / methodological classification (not a theorem) | **statement:** FAILURE-MODE TAXONOMY. Each code lists its mechanism, the dossiers where it occurs, and a quick test.

F1 Uses only the functional equation or properties shared with a countermodel.
- Dossiers: D3, D14.
- Test: run the argument on Davenport-Heilbronn (certified zero 0.8085+85.6993i), Epstein zeta, or zeta_N.

F2 Hypothesis never used ('proves too much'); the contradiction does not depend on Re b != 1/2.
- Dossiers: D3, D11, D12.
- Test: apply to rho_1, to 1/(z-rho), or to a perturbed zero set.

F3 Circular: a hidden RH-equivalent invertibility, positivity or propagation.
- Dossiers: D2(c), D10(d).
- Test: does each claim survive one off-line pair?

F4 Over-strong sufficient condition that is false.
- Dossiers: D1, D5, D6, D7.
- Test: compare with Ingham-type obstructions.

F5 Finite-to-infinite extrapolation.
- Dossiers: D6, D7, D10(c).
- Test: compare the Skewes scale of the first failure with the computed range.

F6 Non-uniform limits: a limit/sum interchange at the boundary of convergence, or 'eventually' in a moving parameter.
- Dossiers: D10(a), D11.

F7 Domain, self-adjointness or normalisability gap.
- Dossiers: D2(c), D4.

F8 Support of measure zero (ideles in adeles).
- Dossier: D2(b).

F9 Undefined or inconsistent new object.
- Dossier: D3.
- Test: a formal power-series consistency check (C3-A1).

F10 Inequality direction or sign error in a criterion.
- Dossier: D10(a).
- Test: the monotonicity of the target in each substituted bound.

F11 Factorisation-only arguments (misapplied Hadamard/Weierstrass).
- Dossier: D12.
- Test: perturb the zero set.

F12 Heuristic model treated as a law.
- Dossier: D8.

F13 Density read as 'all zeros'.
- Dossier: D9.

F14 Explicit-constant bookkeeping errors.
- Dossier: D13.

F15 Revision instability: the same method gives opposite conclusions, or dozens of versions.
- Examples: D10; status-only examples arXiv:2209.01890v58 and 2112.05521v81. | **evidence:** Built from dossiers D1-D14. Each code is instantiated by at least one documented case with an explicit witness or a cited critique. | **prior_art:** Folklore checklists, for example Aaronson's 'Ten signs a claimed mathematical breakthrough is wrong', and Farmer arXiv:2008.07206 on criteria for RH-equivalences. No systematic RH-specific taxonomy with certified witnesses was located.
- **id:** C3-CHECKLIST | **status:** HEURISTIC / methodological (not a theorem) | **statement:** ONE-PAGE CHECKLIST FOR A PROPOSED RH PROOF (human or AI).
1. State the exact claim: RH, a cited equivalent with its normalisation, or a sufficient condition. If the last, is it strictly stronger than RH (F4)?
2. Countermodel test: does every step hold for Davenport-Heilbronn (zero 0.80851718+85.69934848i), Epstein zeta, or zeta_19 (a zero with Re = 1.0010955)? If so, the argument is invalid.
3. Mark where Re rho != 1/2 is used. Re-run the argument at rho_1 = 1/2+14.1347i and on 1/(z-rho).
4. List every invertibility, positivity, density or propagation lemma, and test each against one off-line pair (F3).
5. Write all quantifiers. 'Fixed b, eventually in x' is not 'b ~ x' (F6).
6. Name the theorem behind each limit/sum/integral interchange. Never evaluate at the boundary of a disc of convergence (F6).
7. Compute the monotonicity of the target in every substituted bound (F10).
8. Name the Hilbert space, measure, domain, closure and deficiency indices. Check that eigenvectors and test functions lie in it and that supports have positive measure (F7, F8).
9. Exhibit a model of every new object's axioms (F9).
10. If only the Hadamard product and the functional equation are used, the zeros are free parameters (F11).
11. Point to the step using the Euler product in a way Davenport-Heilbronn fails.
12. A proportion, even 1-o(1), is not RH (F13).
13. No finite computation proves an infinite statement. Estimate the Skewes scale of a possible first failure, recalling Mertens (|M|/sqrt x < 0.571 up to 1e16, yet false), Polya (true to 9e8) and Turan T (true to 7.2e13) (F5).
14. Re-derive imported explicit lemmas with sharp constants and test them on extremal examples, e.g. Kusmin-Landau cot(pi theta/2) (F14).
15. Label every number as a certified ball or floating point; high precision is not certification.
16. Random-model and RMT predictions are not evidence about individual zeros; check them against Omega theorems such as Maier (F12).
17. If a revision reverses the conclusion, the method is not discriminating (F15).
18. Does the argument apply to a family containing a member with known off-line zeros?
19. Search arXiv and zbMATH for published obstructions: Conrey-Li, Montgomery, Odlyzko-te Riele, Haselgrove, Maier, Farmer.
20. Pre-register the smallest statement whose failure kills the argument (cf. Queme's footnote). | **evidence:** Every item is backed by a dossier or a certified witness above. | **prior_art:** AGENTS.md 'Non-negotiable boundaries'; methodology.md Sec. 6-8.

## Failed attempts and negative results

- Report file NOT written. The harness refused the write of proposals/independent_campaigns/C3-failure-anatomy/REPORT.md ('Subagents should return findings as text'). The content is in this structured output; only data files (JSON) were written under experiments/results/C3-failure-anatomy.
- Bug, fixed: the first sieve self-test failed because the large-prime ambiguity band [0.01, 9] was wrong when sqrt(N) < e^9. It is now [0.01, log(sqrt N + 1) - 0.01]. The full run had 0 ambiguous decisions.
- Inadequate bound, replaced: the a-priori float64 error bound for Turan's T(x) (4.7e-6) exceeded min T (1.43e-6), so positivity up to 1e9 was not certified. It was replaced by an exact fixed-point certificate: sum lambda(n) floor(2^56/n) - x >= 102,357,542,618 > 0.
- Float64 artefact, removed: the first finite-difference check of Oliva's 'Lemma 2.2' gave a meaningless sign at b = 1e8, because the change in f was below one ulp. It was replaced by 60-digit mpmath differentiation and bisection for the turning point.
- Recollection error, caught: we initially recalled the first negative of Turan's T(n) as about 7.2e16. The zbMATH review of BFM 2008 gives 72,185,376,951,205 (about 7.2e13).
- Task premise, corrected: Li's arXiv:0807.0090 is 'withdrawn' only for the 2008 text (v4, 6 July 2008). v5-v10 (2024-2025) carry a new, unrefereed claimed proof under the same identifier, which was not audited.
- Task premise, corrected: Stieltjes' claim M(x) = O(sqrt x) is NOT refuted; it is open and believed false. Odlyzko-te Riele refute only Mertens' |M(x)| < sqrt x.
- Task premise, corrected: Bender-Brody-Mueller explicitly do not claim a proof. It is a conditional programme ('if ... can be made rigorous').
- Task premise, refined: Turan's partial-sum hypothesis was contradicted for specific N numerically by Spira (1968) before Montgomery's 1983 asymptotic theorem covering all large N.
- Sources unreachable or unreadable: the Odlyzko-te Riele PDF (TLS chain failure, then HTTP 503; TLS was not bypassed); Booker's Turing article in Notices AMS (bot wall); Granville 1995 (image-only PDF, no text layer). These were replaced by zbMATH reviews and secondary L1 sources (Trudgian 2011; Banks-Ford-Tao).
- Not done: audit of Dasheng Liu arXiv:2404.06306 (Hadamard-product disproof claim); audit of de Branges' post-2004 manuscripts; audit of Oliva v2 (the disproof version); any computation probing Maier's theorem (Omega statements cannot be tested finitely).

## Code

- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C3-failure-anatomy/liouville_mertens_sieve.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C3-failure-anatomy/conrey_li_debranges.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C3-failure-anatomy/witnesses.py`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C3-failure-anatomy/liouville_mertens_1e9.json`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C3-failure-anatomy/conrey_li_debranges.json`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C3-failure-anatomy/conrey_li_debranges_K20000.json`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C3-failure-anatomy/witnesses.json`
- `/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C3-failure-anatomy/manifest_C3.json`

## Open questions

- The de Branges necessary condition fails at 9.75% of the first 2000 zeros and 13.62% of the first 20000. Does this rate stabilise or keep growing with height? Can it be predicted from the joint distribution of arg xi(3/2+i gamma_n) and the parity of n?
- Is there any refereed analysis of the 2024-2025 versions (v5-v10) of arXiv:0807.0090, which claim Li-criterion positivity via traces on two orthogonal subspaces?
- Is there any Hilbert space in which the BBM formal eigenfunctions psi_z (Re z = 1/2) are normalisable eigenvectors of a self-adjoint realisation? Liu 2026 (unrefereed) excludes the natural sin^2(p/2) completion.
- Can the proves-too-much tests F1/F2/F11 be mechanised? For example, symbolically run a candidate argument on a parametrised family containing Davenport-Heilbronn-type members, or on perturbed zero sets.
- For Oliva's step (3): give an explicit (Skewes-type) upper bound for the first n at which (1-1/p_{n+1}) loglog N_{n+1} < loglog N_n, using theta(x)-x sign-change bounds.
- Do de Branges' post-2004 manuscripts depend on the positivity conditions refuted by Conrey-Li, or on different spaces? This was not audited.

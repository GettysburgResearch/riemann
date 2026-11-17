# PAPER-0028 — The maximum size of \(L\)-functions

| Field | Value |
|---|---|
| Authors | Farmer, David W.; Gonek, S. M.; Hughes, C. P. |
| Year / stratum | 2007 / S5 |
| Venue | J. Reine Angew. Math. 609, 215-236 (2007). |
| Identifiers | zbMATH [1234.11109](https://zbmath.org/?q=an:1234.11109) · DOI [10.1515/CRELLE.2007.064](https://doi.org/10.1515/CRELLE.2007.064) · arXiv [math/0506218](https://arxiv.org/abs/math/0506218) |
| MSC | 11M06, 11M50, 11M26 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/math/0506218 |
| Selection | score 4.5984, in-pool citations 46, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** What is the true maximal order of |zeta(1/2+it)| on [0,T] (the '1 or 2?' question: Littlewood's RH-conditional O(exp(C sqrt(log t/log log t))) vs Omega-results with C' >= 1), and likewise for S(t) and for central values L(1/2,F) over families by conductor? Answer: conjectural, via random-matrix models of the zero product, Granville-Soundararajan random model of the prime product, and moment conjectures.

**Historical motivation.** The '1 or 2?' problem: Littlewood's RH bound has exponent sqrt(log t/ log log t) in the exponent, Omega results (Montgomery 1/20, Soundararajan C'=1) differ by factor of 2 in the power of log in the exponent; Kotnik numerics suggested C'>2. Paper decides conjecturally for '1' (half-way between: max near the Omega side), paralleling Montgomery-Vaughan / Granville-Soundararajan on the 1-line.

### Main results

- **THM-PAPER-0028-1** (Conjecture A (1.3), conjecture, scope: asymptotic; Sec. 1, p.2). $\max_{t\in[0,T]}|\zeta(\tfrac12+it)|=\exp\Big((1+o(1))\sqrt{\tfrac12\log T\,\log\log T}\Big)$ as $T\to\infty$. *Conditional on:* heuristic models: Haar characteristic polynomial model for Z_X, random-prime model for P_X, independence of P_X and Z_X.
- **THM-PAPER-0028-2** (Conjecture B (1.4), conjecture, scope: asymptotic; Sec. 1 p.2; Sec. 4). $\limsup_{t\to\infty}\dfrac{S(t)}{\sqrt{\log t\,\log\log t}}=\dfrac{1}{\pi\sqrt2}$. *Conditional on:* Keating-Snaith RMT model for Im log zeta, independence heuristics.
- **THM-PAPER-0028-3** (Conjecture C (1.5), conjecture, scope: asymptotic; Sec. 1 p.2, Sec. 5). For a family $\mathcal F$ of L-functions with $\#\{F: c(F)<D\}\approx D$ and symmetry type unitary/symplectic/orthogonal, $\max_{F\in\mathcal F,\,c(F)\le D}|F(\tfrac12)|=\exp\big((1+o(1))\sqrt{B\log D\log\log D}\big)$, with $B=1/2$ (unitary), $B=1$ (symplectic, orthogonal); implied constant depends only on $\mathcal F$. Contains Conjecture A via the shift family $F_y(s)=L(s+iy)$. Examples (1.6), (1.7): real Dirichlet L(1/2,chi_d) and weight-k level-N cusp forms with kN<=D, both B=1.
- **THM-PAPER-0028-4** (Theorem 2.1, theorem (random matrix, unconditional), scope: asymptotic; Sec. 2.1, p.4-5). Fix $\delta>0$, $M=\exp(N^\beta)$ with $\delta<\beta<2-\delta$, $K_\varepsilon(N)=\exp\big(\sqrt{(1-\beta/2+\varepsilon)\sqrt{\log M\log N}}\big)$ [as printed: $\exp\big(\sqrt{1-\tfrac12\beta+\varepsilon}\,\sqrt{\log M\log N}\big)$ per (2.8)]. For independent Haar $U_1..U_M\in U(N)$, $P(\max_j\max_\theta|\Lambda_{U_j}(\theta)|\le K_\varepsilon(N))\to1$ for every $\varepsilon>0$ and for no $\varepsilon<0$.
- **THM-PAPER-0028-5** (Theorem 2.3, theorem (random matrix), scope: asymptotic; Sec. 2.1, p.5). Let $M=N^c e^{N\log X}$, $2<X<N$, $c>0$, $K_\varepsilon(N)=\exp\big((\tfrac1{\sqrt2}+\varepsilon)\sqrt{N\log N\log X}\big)$. For independent Haar $U_j\in U(N)$, $P(\max_{j\le M}|\Lambda_{U_j}(0)|\le K_\varepsilon)\to1$ for all $\varepsilon>0$ and for no $\varepsilon<0$ (sampled-points version of Thm 2.1).
- **THM-PAPER-0028-6** (Theorem 3.1, theorem (unconditional on moment-conjecture validity range), scope: asymptotic; Sec. 3, (3.7)). The conjectured 2k-th moment asymptotic (3.3) [Keating-Snaith leading term times arithmetic factor, uniform in k] cannot hold for $k\ge(2\sqrt2+\varepsilon)\sqrt{\log T/\log\log T}$, any fixed $\varepsilon>0$.
- **THM-PAPER-0028-7** (Theorem 3.2, theorem (conditional on moment formula (3.3) in a range of k), scope: conditional; Sec. 3, (3.8)-(3.10)). Let $m_T=\max_{[0,T]}|\zeta(1/2+it)|$. If (3.3) holds for $k=\log^\delta T$ with $\delta<1/2$ then $m_T\ll\exp(\log^{1-\delta}T)$. If (3.3) holds for $k=\sqrt{2\log T/\log\log T}$ then $m_T\ll\exp\big(\sqrt{\tfrac12\log T\log\log T}+O(\sqrt{\log T}\,\log\log\log T/\sqrt{\log\log T})\big)$; if it holds for $k=\sqrt{8\log T/\log\log T}$ then the matching lower bound $m_T\gg\exp(\cdots)$ holds. *Conditional on:* moment conjecture (3.3) (full CFKRS/Keating-Snaith) with k growing.
- **THM-PAPER-0028-8** (Theorem 4.1, theorem (random matrix), scope: asymptotic; Sec. 4, (4.2)-(4.3)). With $K_\varepsilon(N)=(\tfrac1{\sqrt2}+\varepsilon)\sqrt{N\log N}$, $M=N^ce^N$, independent Haar $U_j\in U(N)$: $P(\max_{j\le M}\mathrm{Im}\log\Lambda_{U_j}(0)\le K_\varepsilon(N))\to1$ for all $\varepsilon>0$, no $\varepsilon<0$.
- **THM-PAPER-0028-9** (Conjecture E (2.36), conjecture, scope: asymptotic; Sec. 2.3, p.7). For fixed $d>0$, $\frac1T\mathrm{meas}\{0<t<T:|\zeta(\tfrac12+it)|>\exp(d\sqrt{\log T\log\log T})\}=\exp(-2d^2\log T(1+o(1)))$.

### Key definitions

- m_T = max_{t in [0,T]} |zeta(1/2+it)|
- Z_X(s)=exp(-sum_rho U((s-rho)log X)), P_X(s)=exp(sum_{n<=X} Lambda(n)/(n^s log n))
- Lambda_U(theta)=det(I-U e^{-i theta}) on U(N)
- Family F with conductor c(F), unitary/symplectic/orthogonal symmetry type

### Principal lemmas

- **THM-PAPER-0028-L1** (Lemma A.1; Appendix A). For fixed $\delta>0$ and $\delta\le\lambda\le1-\delta$: $P(\max_\theta|\Lambda_U(\theta)|\ge\exp(N^\lambda))=\exp\Big(-\dfrac{N^{2\lambda}}{(1-\lambda)\log N}(1+o(1))\Big)$, $U$ Haar in $U(N)$. — *Role:* Tail of the sup of the characteristic polynomial; engine for Thms 2.1, 2.3 and Conj. D. Proof uses Bernstein's inequality $\max|\Lambda_U'|\le N\max|\Lambda_U|$ to pass from sup to discrete sampling.
- **THM-PAPER-0028-L2** (Lemma 2.2; Sec. 2.1, p.5-6). If $|\zeta(\tfrac12+it_0)|=m_T=\max_{[0,T]}|\zeta(\tfrac12+it)|$ then there is an absolute $A>0$ with $|\zeta(\tfrac12+it)|>\tfrac12m_T$ for $|t-t_0|<A/\log T$. — *Role:* Local regularity near the max (Cauchy estimate on a circle of radius c/log T plus functional equation); justifies discrete sampling and Lemma 3.3.
- **THM-PAPER-0028-L3** (Lemma 3.3; Sec. 3, (3.14)). For all $k>0$: $m_T^{2k}\ll 2^{2k}\log T\int_0^T|\zeta(\tfrac12+it)|^{2k}dt$, absolute implied constant. — *Role:* Converts moment asymptotics at large k into an upper bound for the maximum.
- **THM-PAPER-0028-L4** ((2.1) [imported, Gonek-Hughes-Keating]; Sec. 2, p.3). For $s=\sigma+it$, $0\le\sigma\le1$, $|t|\ge2$, $X>2$, $K\in\mathbb N$: $\zeta(s)=P_X(s)Z_X(s)\big(1+O(X^{2-\sigma+K}/(|t|\log X)^K)+O(X^{-\sigma}\log X)\big)$ with $P_X=\exp(\sum_{n\le X}\Lambda(n)/(n^s\log n))$, $Z_X=\exp(-\sum_\rho U((s-\rho)\log X))$. — *Role:* Rigorous hybrid Euler product/Hadamard product used to split prime and zero contributions; unconditional.
- **THM-PAPER-0028-L5** (Lemma 5.1; Sec. 5.1, p.13-14). Independent real mean-0 variance-1 $x_j$, bounded $a_j$ with $V_J^{-2}\sum_{j\le J}|a_j|^n\to0$ for all $n\ge3$, $V_J=\sum a_j^2$; then $\sum a_jx_j$ tends to Gaussian of variance $V_J$. — *Role:* Gaussian limit for the symplectic/orthogonal prime model, giving B=1 rather than 1/2.
- **THM-PAPER-0028-L6** (Conjecture D (2.14); Sec. 2.1, p.5). For $2<X<\log^AT$: $\max_{t\in[0,T]}|Z_X(\tfrac12+it)|=\exp((1+o(1))\sqrt{\tfrac12\log T\log\log T})$. — *Role:* Zero-product half of the model; combined with $P_X=O(\exp(C\sqrt{\log t/\log\log t}))$ for X=O(log T) gives Conj. A; X large (random-prime model) and intermediate X give consistency.

### Proof architecture

Heuristic, three-pronged. (i) Section 2: use unconditional GHK approximation zeta=P_X Z_X(1+small). Model Z_X by Lambda_U for U in U(N), N=floor(log T/(e^gamma log X)), taking M ~ exp(e^gamma N log X) independent matrices to match the T log T zeros; Theorem 2.1 (via Lemma A.1 tail) gives max ~ exp(sqrt(1/2 log T loglog T)) when X small (P_X negligible). For X large, Granville-Soundararajan Gaussian random-prime model for log P_X gives the same constant; intermediate X by convolving the two (Lemma 2.4 independence-type lemma). (ii) Section 3: assuming full moment conjecture (3.3) for k up to ~ sqrt(log T/loglog T), Lemma 3.3 + Lemma 2.2 give upper (Thm 3.2) and lower bounds, plus Theorem 3.1 limiting the validity range of (3.3). (iii) Section 4: same with Im log Lambda_U for S(t). Section 5: extension to families (B=1/2 vs 1 from variance of Gaussian), alternative arguments for/against. Rigorous inputs: GHK (2.1), HKO tail theorem [12], Bernstein inequality; everything else is model-based.

**Imported results.** Gonek-Hughes-Keating hybrid product, Duke Math J. 2007 (eq. 2.1); Hughes-Keating-O'Connell, Thm 3.5/3.6 on tails of log|Lambda_U(0)| and Im log (ref [12]); Keating-Snaith RMT moment conjecture; Conrey-Farmer-Keating-Rubinstein-Snaith integral moment conjecture [5]; Granville-Soundararajan extreme-value probabilistic model for primes; Soundararajan 2005 Omega-result C'>=1; Montgomery, Balasubramanian-Ramachandra; Littlewood RH-conditional bound (1.1)

**Techniques.** Haar-measure characteristic polynomial tails (Hughes-Keating-O'Connell); Bernstein inequality for trigonometric polynomials; Gonek-Hughes-Keating hybrid Euler-Hadamard product; Granville-Soundararajan random-prime Gaussian model; moment-to-maximum comparison via local regularity (Cauchy estimate); union-bound/extreme-value calibration (M independent samples)

## Context and interpretation

**Importance and obstacle overcome.** First unified, quantitatively precise conjecture for max|zeta| (constant 1/sqrt2 in exp(sqrt(c log T loglog T))) with three independent heuristic routes (zeros, primes, moments) agreeing; the obstacle was that naive maximum of |Lambda_U| (=2^N) violates known bounds, so a model with the correct number M of independent samples was needed. Also yields restrictions on validity range of moment conjectures (Thm 3.1) and extension to families with B=1/2 vs 1.

**Relation to prior work.** 

**Limitations and open questions.** All main statements are conjectures. Independence of P_X and Z_X, the number of effectively independent samples M and the identification T log T zeros <-> M matrices of size N are heuristic. Theorem 3.2 is conditional on the moment conjecture holding for growing k (the paper itself notes (3.3) must fail past k ~ sqrt(8 log T/loglog T)). Symplectic S(t)-analogue not covered ('our methods cannot be directly applied'). Section 5.3 lists arguments against the conjecture (e.g. possible moment-conjecture changes, non-random large values). Unconditionally, the best known are RH-conditional O(exp(C log t/loglog t)) in the true exponent, far from conjecture.

## Research potential

- **Hypotheses that might be weakened.** Independence of P_X and Z_X at X=exp(log^alpha T); the Gaussian tail of log P_X for deviations of size sqrt(log T loglog T) (Granville-Soundararajan, only known/proved in restricted ranges); validity of Keating-Snaith/CFKRS moments for k up to c sqrt(log T/loglog T) (Theorem 3.2 hypothesis).
- **Generalizations.** Conjecture C for further families (Rankin-Selberg, GL(n) shift family L(s+iy) gives unitary B=1/2); joint max of |zeta| and S(t); Conjecture E tail exponent -2d^2 log T vs unconditional upper bounds such as Soundararajan's measure estimate (exp(-V^2/loglog T)) — could check the exponent 2d^2 vs 1/(log log T) normalization; large-deviation analogue for derivative zeta'(rho).
- **Candidate connections.** Soundararajan 'Moments of zeta' (CAND-01201): his Theorem on meas(S(T,V)) is the RH-conditional rigorous counterpart to Conj. E and Thm 3.2; Goldston-Gonek (CAND-01222): rigorous RH bound |S(t)|<=(1/2+o(1)) log t/loglog t vs Conjecture B sqrt scale; CFKRS lower order terms (CAND-01239) as the source of (3.3) with arithmetic factor; Bondarenko-Seip resonance method and Najnudel/Arguin et al. for log-correlated maximum.
- **Reusable lemmas.** Lemma A.1 (tail of max_theta |Lambda_U|) and Theorems 2.1/2.3 are directly reusable calibrations for extreme-value predictions; Lemma 2.2 + Lemma 3.3 (maximum <= (log T) * moment, local regularity at scale 1/log T) is reusable for any L-function; Lemma 5.1 (Lyapunov-type CLT) for prime sums.
- **Possible experiments.** Numerically estimate max_{t<=T}|zeta(1/2+it)| for T up to 10^{12}-10^{15} (Odlyzko-style zero tables / Hiary) and fit exp(c sqrt(log T loglog T)) against the 1/sqrt2 prediction, accounting for lower-order loglog log T corrections (Theorem 3.2 error term); measure empirical tail of log|zeta| vs Conjecture E exponent -2d^2 log T at moderate d. Simulate M independent Haar matrices to test the finite-N correction to Thm 2.1.
- **Risks / barriers.** Conjecture is out of reach unconditionally (even Lindelof unproved); finite-T numerics converge extremely slowly (sqrt(log T loglog T) varies little over feasible T). Model independence of primes and zeros is unprovable with current technology; later work (e.g. Arguin-Ouimet-Radziwill on moments of Riemann zeta on short intervals; Harper) shows subtle log-correlated corrections to the max of local pieces, so quantitative constants must be re-verified.

## Audit notes (Level 1 reader)

Eq. (2.8) in the extracted text prints as sqrt(1 - beta/2 + eps) * sqrt(log M log N) (square root nested inconsistently by OCR); I record it as printed in (2.8). Theorem 3.2 first claim 'mT << exp(log^{1-delta} T)' is a weaker (Lindelof-type) bound and is stated for delta<1/2 only. Lemma 2.2's proof is a one-line Cauchy estimate (sketch-level). Appendix A proof was inspected only at its start (Bernstein step). Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01208`; harvest queries: kw_RH_any, msc_11M06, msc_11M26, msc_11M50, arxiv_random_matrix_zeta.
- Triage decision: include — Conjecture on true maximal size of zeta on the critical line.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

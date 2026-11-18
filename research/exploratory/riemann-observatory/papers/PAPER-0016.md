# PAPER-0016 — Explicit bounds on \(\zeta (s)\) in the critical strip and a zero-free region

| Field | Value |
|---|---|
| Authors | Yang, Andrew |
| Year / stratum | 2024 / S7 |
| Venue | J. Math. Anal. Appl. 534, No. 2, Article ID 128124, 53 p. (2024). |
| Identifiers | zbMATH [1543.11077](https://zbmath.org/?q=an:1543.11077) · DOI [10.1016/j.jmaa.2024.128124](https://doi.org/10.1016/j.jmaa.2024.128124) · arXiv [2301.03165](https://arxiv.org/abs/2301.03165) |
| MSC | 11M06, 11M26, 11Y35 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/2301.03165 |
| Selection | score 4.6104, in-pool citations 8, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Give an explicit k-th derivative test (van der Corput A^{k-2}B process) with constants uniform in k, use it to bound zeta explicitly on the lines sigma_k=1-k/(2^k-2) (k>=4), and deduce an explicit Littlewood zero-free region 1-sigma<<loglog t/log t.

**Historical motivation.** Titchmarsh Thm 5.13 gives zeta(sigma_k+it)<<t^{1/(2^k-2)}log t but with unspecified constants; Granville-Ramare gave explicit but weaker (log-power loss) tests. Littlewood's 1922 region was never made explicit until Yang's work. Applications also to explicit zeta'/zeta, 1/zeta near the 1-line (Mertens function) and S(t).

### Main results

- **THM-PAPER-0016-1** (Theorem 1.1, theorem, scope: global; Sec. 1 (1.2); proof Sec. 3). Let k\ge4 be an integer and \sigma_k:=1-\frac{k}{2^k-2}. Then |\zeta(\sigma_k+it)|\le 1.546\,t^{1/(2^k-2)}\log t for all t\ge3. (E.g. |\zeta(5/7+it)|\le1.546t^{1/14}\log t.)
- **THM-PAPER-0016-2** (Corollary 1.2, corollary, scope: global; Sec. 1.1 (1.6); proof Sec. 4 end, (4.135)). \zeta(\sigma+it)\ne0 for \sigma>1-\dfrac{\log\log|t|}{21.233\,\log|t|}, |t|\ge3. Widest known region for \exp(170.3)\le|t|\le\exp(532\,141) (paper's own range statement; abstract says exp(171) to exp(5.3e5)). *Conditional on:* RH verified to 3e12 (Platt-Trudgian), Ford-type zero-detector machinery (Lemma 4.7, Ford Lemma 4.6).
- **THM-PAPER-0016-3** (Lemma 2.5, lemma, scope: global; Sec. 2). Let a,N integers, N>0, f with k\ge4 continuous derivatives, f^{(k)} monotonic and 0<\lambda_k\le|f^{(k)}|\le h\lambda_k on (a,a+N]; K=2^{k-1}. Then S_f(a,N)\le A_k h^{2/K}N\lambda_k^{1/(2K-2)}+B_kN^{1-2/K}\lambda_k^{-1/(2K-2)}, with A_k,B_k given by explicit recursion (2.44)-(2.46).
- **THM-PAPER-0016-4** (Lemma 2.6, lemma, scope: global; Sec. 2 (A_{10}(4.7399,3)<=2.744, B_{10}<=1.020, eta_3=4.7399)). For k\ge10, integers a,N>0, f with f^{(k)} monotonic, \lambda_k\le|f^{(k)}|\le h\lambda_k with 1<h\le3: S_f(a,N)\le 2.762\,h^{2/K}N\lambda_k^{1/(2K-2)}+1.02\,N^{1-2/K}\lambda_k^{-1/(2K-2)}.
- **THM-PAPER-0016-5** (Lemma 4.8, lemma, scope: global; Sec. 4). Master inequality for a zero \beta+it, t\ge3\cdot10^{12}, 1-\beta\le\eta_k/2, with zero-free rectangle 1-\lambda<\Re s\le1, t-1\le\Im s\le Dt+1: explicit inequality with constants 0.17996, 0.20523, 1.546 (from Thm 1.1), c(R) from (4.58) (see paper).

### Key definitions

- sigma_k=1-k/(2^k-2)
- K=2^{k-1}, J=2^{j-1}, R=2^{r-1}
- theta_r=R/(rR-2R+2)
- S_f(a,N)=sum_{a<n<=a+N}e(f(n))
- Littlewood-type region sigma>1-loglog|t|/(C log|t|)

### Principal lemmas

- **THM-PAPER-0016-L1** (Lemma 2.1; Sec. 2). Explicit second-derivative test: if f'' monotonic with \lambda_2\le|f''|\le h\lambda_2 on [a,a+N], then S_f(a,N)\le \frac4{\sqrt\pi}Nh\lambda_2^{1/2}+... (printed: \tfrac{4}{\sqrt\pi}N\sqrt{h\lambda_2}+N... ) — *Role:* Base case; derived from explicit Kuzmin-Landau (2.2)-(2.3) with interval subdivision and trivial bound.
- **THM-PAPER-0016-L2** (Lemma 2.3 (Explicit A process); Sec. 2). For integers a,N and q>0: (S_f(a,N))^2\le (N-1+q)\big(\tfrac Nq+\tfrac2q\sum_{r=1}^{q-1}(1-\tfrac rq)S_{g_r}(a,N-r)\big), g_r(x)=f(x+r)-f(x). — *Role:* Weyl-van der Corput differencing with sharpened prefactor N-1+q (vs N+1+q in Cochrane-Graham / N+q in Patel-Trudgian).
- **THM-PAPER-0016-L3** (Lemma 2.4; Sec. 2). Explicit third-derivative test S_f(a,N)\le A_3(\eta_3,h)h^{1/2}N\lambda_3^{1/6}+B_3(\eta_3)N^{1/2}\lambda_3^{-1/6} for \lambda_3\le|f'''|\le h\lambda_3, f''' monotonic. — *Role:* Starting constants A_3,B_3 for the recursion.
- **THM-PAPER-0016-L4** (Lemma 3.2 (Simonic 2020, Cor. 2); Sec. 3). For 1/2\le\sigma\le1, t\ge t_0>0, h>1/(2\pi): |\zeta(s)-\sum_{n\le ht}n^{-s}|\le \frac{1}{(ht_0)^{\sigma}}\big(\tfrac h{...}\big)... (Euler-Maclaurin remainder). — *Role:* Imported; reduces zeta to a partial sum over n<=ht.
- **THM-PAPER-0016-L5** (Lemma 3.3; Sec. 3). For s=\sigma_k+it, r\ge2, R=2^{r-1}, 0<a<b\le ha: |\sum_{a<n\le b}n^{-s}|\le C_r(\eta_3,h)a^{k/(2K-2)-r/(2R-2)}t^{1/(2R-2)} (shape). — *Role:* Applies the r-th derivative test on dyadic-type pieces; X_1=h_0t^{\theta_k}, X_2=\lfloor h_0h_2t\rfloor, \theta_r=R/(rR-2R+2).
- **THM-PAPER-0016-L6** (Lemma 3.5; Sec. 3). For k\ge4, s=\sigma_k+it, t\ge t_0, h_0,\eta_3>0, h_2\in(0,e), h_3>1: |\sum_{X_1<n\le X_2}n^{-s}|\le\beta_k(t_0)t^{1/(2K-2)}\log t, \beta_k=\sum_{r=2}^{k-1}F_k(r,t). — *Role:* Assembles the three-range split ((0,X0] trivial; (X0,X1],(X1,X2] via Lemma 2.6) into Thm 1.1.
- **THM-PAPER-0016-L7** (Lemma 4.1; Sec. 4). For 0<a\le1/2, t_0\ge100, t\ge3t_0, 1/2\le\sigma\le1-t^{-1}, and |\zeta(\sigma+iy)|\le Xt^Y\log t for t_0\le|y|\le t: \frac12\int\frac{\log|\zeta(\sigma+it+iau)|}{\cosh^2u}du\le\log X+Y\log t+\log\log t. — *Role:* Replacement of Ford Lemma 3.4 with log-power Z=1 suited to Theorem 1.1.

### Proof architecture

Sec. 2: explicit Kuzmin-Landau -> Lemma 2.1 (k=2) -> explicit A process (Lemma 2.3) -> Lemma 2.4 (k=3) -> Lemma 2.5 inductive recursion for A_k,B_k uniform in k, with trivial-bound fallback for small N (e.g. N<=2336) to avoid ill-suited intervals; Lemma 2.6 for k>=10 numerics. Sec. 3: zeta(s)=sum_{n<=ht}n^{-s}+remainder (Simonic); partial sums over 0<n<=X2 split into (0,X0] trivial, (X0,X1],(X1,X2] via Lemma 2.6 with different k (choice theta_r); partial summation; optimise parameters to get constant 1.546 (Thm 1.1). Sec. 4: replace Ford-Richert bound by Thm 1.1 (on sigma_k lines) plus Phragmen-Lindelof (Lemma 3.1) in between; new Lemmas 4.1,4.4-4.6 for the integrals and zero counts (using S(t) bounds); Lemma 4.8 master inequality; extremal argument with M1=0.0470978 gives 1-beta<=loglog t/(21.233 log t) for t>=t_0; small t covered by RH verification and earlier ranges.

Dependency edges: CAND-02339 → Titchmarsh Thm 5.13 (makes explicit); CAND-02339 → CAND-02337 (uses MTY/Ford zero-detector framework; compared against); CAND-02341 → CAND-02339 (uses Yang's Littlewood region for t<=exp(463388))

**Imported results.** Titchmarsh Thm 5.13 (qualitative k-th derivative bound); Simonic 2020 Cor 2 (explicit Euler-Maclaurin remainder), Kadiri 2013, Cheng 2000; Cochrane-Graham 2004 Lemma 5 and Patel-Trudgian 2015 Lemma 2 (A process); Platt-Trudgian: RH to 3e12; Ford 2002 Lemma 4.6/7.1 framework; Mossinghoff-Trudgian-Yang; Hiary-Patel-Yang (HPY24) explicit AB process; Littlewood 1922 (qualitative)

**Techniques.** van der Corput A^{k-2}B process made explicit; explicit Kuzmin-Landau; Weyl differencing with trivial-bound avoidance of bad intervals; Euler-Maclaurin remainder (Simonic); Phragmen-Lindelof interpolation; Ford zero-detector with non-negative trig polynomial (as in MTY); extremal-zero argument

## Context and interpretation

**Importance and obstacle overcome.** First explicit A^{k-2}B test uniform in k with a log-power-saving form (1.8); first explicit Littlewood region (C=21.233 in v2; 21.432 in the first version as quoted by Bellotti). Obstacle: A_k,B_k blow up when the test is applied to short or badly controlled intervals; overcome by falling back on the trivial bound at each differencing step.

**Relation to prior work.** 

**Limitations and open questions.** Region beats others only for exp(170.3)<=t<=exp(532141); asymptotically weaker than Vinogradov-Korobov. Theorem 1.1 degenerates to |zeta(1+it)|<=1.546 log t for large k, weaker than known 1-line bounds. Sec. 5 suggests specialising to fixed k, replacing a uniform constant by a(k)->0 for t>=t_k, using Thm 1.1 + Phragmen-Lindelof to improve S(t) bounds (Lemma 4.5, 4.6) and Ford-Richert bound (4.8) for small t; suggests computer-assisted derivation.

## Research potential

- **Hypotheses that might be weakened.** Uniformity in k >=4 is the cost: specialising to k=4,5 (or t>=t_k) would reduce A_k,B_k; the choice h<=3 in Lemma 2.6 and eta_3=4.7399 are tunable parameters.
- **Generalizations.** Same A^{k-2}B machinery for Hurwitz zeta and Dirichlet L-functions (Khale-type), and for explicit zeta'/zeta, 1/zeta, M(x) bounds; explicit exponent pairs beyond A^{k-2}B(0,1).
- **Candidate connections.** Combine with Bellotti's improved Ford-Richert constants (CAND-02341) in a hybrid zero-free region; explicit S(t) bounds (HSW) via Thm 1.1 and Phragmen-Lindelof.
- **Reusable lemmas.** Lemma 2.3 (A process with N-1+q), Lemma 2.5/2.6 (explicit k-th derivative test), Lemma 4.1.
- **Possible experiments.** Recompute A_k,B_k recursion (2.44)-(2.46) numerically for k=4..40 with interval arithmetic and compare with 2.744/1.020 at k=10; optimise (h_0,h_2,h_3,eta_3) to see how much 1.546 can drop; check Corollary 1.2 range of optimality exp(170.3)..exp(532141).
- **Risks / barriers.** Final constant 21.233 sensitive to small-t; bottleneck at small k (per Sec. 5). Region is still sub-optimal asymptotically versus Korobov-Vinogradov, so cannot influence RH-type conclusions.

## Audit notes (Level 1 reader)

Version discrepancy: Bellotti (CAND-02341, Intro) cites Yang's constant C_1=21.432, while arXiv v2 reads 21.233; v1 not read. Intro gives range exp(170.3)<=t<=exp(532 141) while abstract says exp(171)..exp(5.3e5) (consistent after rounding). In the extracted text of Lemma 2.1 the second-derivative test is garbled; the displayed coefficients should be checked against the PDF. Lemma 3.2 and Lemma 3.3 statements were abbreviated/garbled by extraction so the record gives their shape only. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02339`; harvest queries: kw_zero_free, msc_11M06, msc_11M26, msc_11Y35, arxiv_zero_free.
- Triage decision: include — Explicit zeta bounds and zero-free region.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

# PAPER-0050 — Some explicit estimates for the error term in the prime number theorem

| Field | Value |
|---|---|
| Authors | Johnston, Daniel R.; Yang, Andrew |
| Year / stratum | 2023 / S6 |
| Venue | J. Math. Anal. Appl. 527, No. 2, Article ID 127460, 23 p. (2023). |
| Identifiers | zbMATH [1535.11128](https://zbmath.org/?q=an:1535.11128) · DOI [10.1016/j.jmaa.2023.127460](https://doi.org/10.1016/j.jmaa.2023.127460) · arXiv [2204.01980](https://arxiv.org/abs/2204.01980) |
| MSC | 11N05, 11M06, 11M26, 11Y35, 11N37 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/2204.01980 |
| Selection | score 4.5603, in-pool citations 14, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Improve explicit error terms for the prime counting functions, namely |psi(x)-x|, |theta(x)-x| and |pi(x)-li(x)| for x>=2, by refining the Platt-Trudgian method using an explicit zero-free region, explicit zero-density estimates near the 1-line, the explicit Riemann-von Mangoldt formula of Cully-Hugill-Johnston, and the Platt-Trudgian RH height 3e12.

**Historical motivation.** Explicit PNT error terms (Rosser-Schoenfeld, Dusart, Buthe, Platt-Trudgian) are needed in applications (e.g. Ramanujan's inequality, bounds on primes in intervals). Platt-Trudgian's Pintz-style argument was valid for x>=exp(1000); this paper widens the range and sharpens constants.

### Main results

- **THM-PAPER-0050-1** (Theorem 1.1, theorem, scope: asymptotic; Sec 1.2, Table 1). For all $x\ge2$: $|\psi(x)-x|\le9.39\,x(\log x)^{1.515}\exp(-0.8274\sqrt{\log x})$. More generally for each row (X,A,B,C,eps_0) of Table 1, $|\psi(x)-x|\le Ax(\log x)^B\exp(-C\sqrt{\log x})$ and $|\psi(x)-x|\le\epsilon_0x$ for all $\log x\ge X$ (e.g. X=3000: A=8.86, B=1.514, C=0.8288, eps_0=3.14e-14; X=1e10: A=45.17, B=1.501, C=1.0903).
- **THM-PAPER-0050-2** (Corollary 1.2, corollary, scope: asymptotic; Sec 1.2). For (X,A,B,C) from Table 1 and A_1=A+0.01: $|\theta(x)-x|\le A_1x(\log x)^B\exp(-C\sqrt{\log x})$ for $\log x\ge X$.
- **THM-PAPER-0050-3** (Corollary 1.3, corollary, scope: asymptotic; Sec 1.2). For all $x\ge2$: $|\pi(x)-\mathrm{li}(x)|\le9.59\,x(\log x)^{0.515}\exp(-0.8274\sqrt{\log x})$.
- **THM-PAPER-0050-4** (Theorem 1.4, theorem, scope: asymptotic; Sec 1.2 eq (1.7)-(1.9)). For x>=23 (Ford's Vinogradov-Korobov region): $|\psi(x)-x|\le0.026x(\log x)^{1.801}\exp(-0.1853\log^{3/5}x(\log\log x)^{-1/5})$; $|\theta(x)-x|\le0.027\cdots$; and (stated as |pi(x)-x|, evidently li(x) intended) $\le0.028x(\log x)^{0.801}\exp(\cdots)$. Asymptotically better than Thm 1.1 but worse for exp(59)<=x<=exp(2.8e10).
- **THM-PAPER-0050-5** (Theorem 1.5, theorem, scope: asymptotic; Sec 1.2). Ramanujan's inequality $\pi^2(x)<\frac{ex}{\log x}\pi(x/e)$ holds for all x>=exp(3361) (improving exp(3915) of Platt-Trudgian); conjecturally for x>=38,358,837,683.

### Principal lemmas

- **THM-PAPER-0050-L1** (Lemma 2.1; Sec 2). Imported: if zeta(beta+it)=0 with |t|<=H=3 000 175 332 800 and 0<beta<1 then beta=1/2 (Platt-Trudgian 2021 RH verification). — *Role:* Finite verification height; used for small zeros and in Buthe-type explicit bounds.
- **THM-PAPER-0050-L2** (Lemma 2.4; Sec 2). For max{50,log x}<T/1.8<(x^{1/35}-2)/4 and x>=exp(1000): $\frac{|\psi(x)-x|}{x}\le\sum_{|\Im\rho|\le T}\frac{x^{\Re\rho-1}}{|\Im\rho|}+\frac{4.3128}{T}\log^{0.6}x$ (from Cully-Hugill-Johnston explicit Riemann-von Mangoldt, Table 5, T* in [T/1.8,T]). — *Role:* Explicit truncated explicit formula with controlled error.
- **THM-PAPER-0050-L3** (Lemma 2.6; Sec 2, App B). Zero-density: N(sigma,T)<=C_1(sigma)T^{8(1-sigma)/3}log^{5-2sigma}T+C_2(sigma)log^2T for tabulated sigma (Table 3, Appendix B), recomputed from Kadiri-Lumley-Ng using Hiary-corrected |zeta(1/2+it)|<=0.77 t^{1/6} log t (t>=3) and the new RH height. — *Role:* Controls zeros with real part >sigma (the dominant contribution).
- **THM-PAPER-0050-L4** (Lemma 2.7, 2.8, 2.9, 2.10; Sec 2). Zero-free regions: classical beta<1-1/(R_0 log|t|), R_0=5.5666305 (Mossinghoff-Trudgian, |t|>=2); Ford-type improved region for |t|>=5.45e8; simplified region beta>=1-nu_2(t), nu_2=(1/(3.359 log|t|))(1-8.02 loglog|t|/log|t|) for |t|>=3; Vinogradov-Korobov nu_3=1/(c log^{2/3}|t|(loglog|t|)^{1/3}), c=57.54; nu=max(nu_1,nu_2,nu_3) with transitions exp(91.2), exp(54563). — *Role:* Zero-free regions used in bounding the sum over zeros with Re rho>sigma.
- **THM-PAPER-0050-L5** (Lemma 2.5; Sec 2). For T>=4 pi e: $\frac1{4\pi}\log^2\frac T{2\pi}-0.9321\le\sum_{0<\Im\rho\le T}\frac1{\Im\rho}\le\frac1{4\pi}\log^2\frac T{2\pi}$. — *Role:* Bounds the contribution of zeros with Re rho<=sigma.
- **THM-PAPER-0050-L6** (Lemma 2.2/2.3; Sec 2). Buthe-type bounds: |psi(x)-x|<sqrt(x)log^2 x/(8 pi) for 59<x<=2.169e25 (similarly theta, pi); |psi(x)-x|/x<=1.570e-12 for x>=exp(2000). — *Role:* Cover small x ranges (Sec 3.1).

### Proof architecture

Sec 3.1 covers x<=exp(2488) with Buthe-style explicit bounds (Lemma 2.2, 2.3) and Broadbent et al. tables. For X<=10000 (Sec 3.2): choose T=exp(2 sqrt(log x/R_0)); apply Lemma 2.4 (3.1); split zeros by Re rho<=sigma and >sigma (3.2), bound the first via Lemma 2.5 (s_1), the second via partial summation against dN(sigma,t) and the classical zero-free region (3.4)-(3.5), subdividing [t_0,T] into K geometric pieces t_k=exp((1+k/K)sqrt(log x/R_0)) and using zero-density Lemma 2.6 (s_2), plus error s_3=4.3128 log^{0.6}x/T; the three-term sum times F(x,sigma) is decreasing, giving A',B,C' with B=(5-2sigma)/2, C_k=(K+k)/K+K/(K+k)... minimized over k, sigma, K (C'<=C_0=(8sigma-2)/3-8(1-sigma)/(3K)). For X>=1e5 (Sec 3.3) use the K=1 argument with the wider zero-free region nu_2, requiring lower bound of T=min t x^{nu_2(t)} on t>=H (Appendix A Lemma A.1, A.2). Corollaries via standard partial summation (Sec 4); Thm 1.4 via Ford VK region (Sec 5). Imported: all inputs of Sec 2 (Platt-Trudgian height, Cully-Hugill-Johnston explicit RvM, KLN zero density, MT15/Ford zero-free regions, Hiary corrected bound 0.77 t^{1/6} log t).

Dependency edges: CAND-01818 → Platt-Trudgian 2021 (PT21b) (improves); CAND-01818 → Cully-Hugill-Johnston 2021 (uses); CAND-01818 → Kadiri-Lumley-Ng 2018 (uses_and_recomputes); CAND-01818 → Hiary 2016 (corrects_dependency_on)

**Imported results.** Platt-Trudgian 2021: RH up to H=3000175332800; Cully-Hugill-Johnston 2021: explicit Riemann-von Mangoldt error (CHJ21, Thm 1.2, Table 5); Kadiri-Lumley-Ng 2018: explicit zero-density, adapted with CHT21 Thm 2 and corrected Hiary bound; Mossinghoff-Trudgian 2015 zero-free region R_0=5.5666305; Ford 2002 explicit zero-free regions (Thm 3 and Thm 5); Buthe 2016 and Broadbent et al. 2021 small-x explicit bounds; Hiary 2016 bound for zeta on the critical line corrected to 0.77 t^{1/6} log t

**Techniques.** explicit formula for psi(x) truncated at height T; partial summation against zero counting function; explicit zero-density estimates (Ingham-type exponent 8(1-sigma)/3); explicit zero-free regions (classical, Ford, Vinogradov-Korobov); optimization over sigma, K (subdivision of heights); numerical verification for small x via Buthe and Broadbent et al.

## Context and interpretation

**Importance and obstacle overcome.** Gives an order-of-magnitude smaller eps_0 than PT21b (e.g. 3.14e-14 at log x=3000), valid for all x>=2 in the headline bound. Obstacle: combining zero-density bounds with zero-free regions requires subdividing heights (K pieces) rather than the single-piece K=1 of PT21b, and handling a discovered unreliable lemma (Hiary 2016, which uses an error in Cheng-Graham) by replacing with 0.77 t^{1/6} log t.

**Relation to prior work.** 

**Limitations and open questions.** Bounds are unconditional but depend on numerical constants and tables; for log x>=X not covered by tables must use Thm 1.4. The sqrt(log x) shape inherits from classical zero-free region; improved region in Thm 1.4 is worse for realistic x. Theorem 1.4 states |pi(x)-x| in (1.9), a typo for li(x).

## Research potential

- **Hypotheses that might be weakened.** The RH verification height H (3e12) enters Lemma 2.2/2.3 and the small-zero contributions; improving it or the zero-density constants C_1,C_2 directly improves A,eps_0. Section 6 lists potential improvements.
- **Generalizations.** Same method for primes in arithmetic progressions (explicit zero-free regions and zero density for Dirichlet L-functions); explicit Mertens-type sums; explicit error terms for Chebyshev theta-ratio inequalities.
- **Candidate connections.** Provides explicit PNT error that is a consistency check for any claimed zero-free-region or RH-equivalence argument (de la Vallee-Poussin versus Riemann hypothesis forms: |psi(x)-x|<sqrt(x)log^2 x/(8 pi) under RH for x>=73.2); relates to explicit zero-density near 1/2 (Simonic, CAND-01828) only via different regime.
- **Reusable lemmas.** Lemma 2.9 (simplified zero-free region nu_2, valid |t|>=3, proof Sec 2) and Lemma 2.4 are reusable; the K-subdivision optimization lemma (eqs 3.9-3.12) is reusable for any combination of zero-density and zero-free-region bounds.
- **Possible experiments.** Recompute Table 1 with an updated Lemma 2.6 table (new zero-density constants) and with a higher RH height; verify the K-subdivision optimization numerically in high precision; test |psi(x)-x| bounds against computed psi(x) for x up to 1e19+ (finite checks do not give global conclusions).
- **Risks / barriers.** Does not approach RH: the best unconditional error remains exp(-c sqrt(log x))-type or VK form; zero-density needs Hiary-corrected bound whose reliability was a source of error in earlier version.

## Audit notes (Level 1 reader)

Sec 1.4: authors disclose that an earlier version used an unreliable result of Hiary 2016 (which relied on an error in Cheng-Graham 2004) and replace it by |zeta(1/2+it)|<=0.77 t^{1/6} log t; Lemma 2.6 recomputed accordingly. Theorem 1.4 (1.9) writes |pi(x)-x| rather than |pi(x)-li(x)| (apparent typo). Lemma 2.9 claims validity for |t|>=3 with proof splitting at exp(91.2853); the intermediate range relies on Lemma 2.1 and 2.7 (consistent). Appendix and Sec 4-6 not read; numerical tables not independently reproduced.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01818`; harvest queries: kw_zero_free, msc_11M06, msc_11M26, msc_11N05, msc_11Y35, arxiv_zero_density, arxiv_zero_free.
- Triage decision: include — Current explicit PNT error bounds.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

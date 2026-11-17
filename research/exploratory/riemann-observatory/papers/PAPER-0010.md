# PAPER-0010 — Explicit zero-free regions for the Riemann zeta-function

| Field | Value |
|---|---|
| Authors | Mossinghoff, Michael J.; Trudgian, Timothy S.; Yang, Andrew |
| Year / stratum | 2024 / S7 |
| Venue | Res. Number Theory 10, No. 1, Paper No. 11, 27 p. (2024). |
| Identifiers | zbMATH [1553.11079](https://zbmath.org/?q=an:1553.11079) · DOI [10.1007/s40993-023-00498-y](https://doi.org/10.1007/s40993-023-00498-y) · arXiv [2212.06867](https://arxiv.org/abs/2212.06867) |
| MSC | 11M26, 42A05, 11Y35 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/2212.06867 |
| Selection | score 4.6133, in-pool citations 11, seed lists 3, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Make the classical (de la Vallee Poussin type) and Korobov-Vinogradov zero-free regions of zeta explicit with the best constants, using higher-degree non-negative trigonometric polynomials found by simulated annealing, optimised parameters, new intermediate regions, and the RH verification height 3e12.

**Historical motivation.** Korobov-Vinogradov (1958) region is the asymptotically largest known; explicit versions (Ford 2000/2002, Nielsen) gave 57.54 and 49.08/49.13; classical constant 5.573412 (Mossinghoff-Trudgian 2015). Motivation includes explicit PNT error terms and primes in short intervals (primes between cubes).

### Main results

- **THM-PAPER-0010-1** (Theorem 1.1, theorem, scope: global; Sec. 1, (1.5); proved Sec. 5). \zeta(\sigma+it)\neq 0 for all |t|\ge 3 and \sigma\ge 1-\dfrac{1}{55.241\,(\log|t|)^{2/3}(\log\log|t|)^{1/3}}. *Conditional on:* Explicit Richert-Ford bound (3.1) with A=76.2,B=4.45 (Ford), RH verified to height 3e12 (Platt-Trudgian), Patel sub-Weyl bound (3.3), Hasanalizade-Shen-Wong N(T) bound (3.8).
- **THM-PAPER-0010-2** (Theorem 1.2, theorem, scope: asymptotic; Sec. 1, (1.6); proved Sec. 7). For sufficiently large |t| (asymptotic, ineffective threshold), \zeta(\sigma+it)\ne0 for \sigma\ge 1-\dfrac{1}{48.1588(\log|t|)^{2/3}(\log\log|t|)^{1/3}}.
- **THM-PAPER-0010-3** (Theorem 1.3, theorem, scope: global; Sec. 1, (1.7); proved Sec. 9). \zeta(\sigma+it)\neq0 for |t|\ge2 and \sigma\ge 1-\dfrac{1}{5.558691\,\log|t|}. *Conditional on:* RH verified to 3e12, Kadiri's method with Jang-Kwon/Xylouris mollifier.
- **THM-PAPER-0010-4** (Theorem 1.4 (intermediate zero-free region), theorem, scope: global; Sec. 1; proved Sec. 6). For |t|\ge e^{1000}, \zeta(\sigma+it)\ne 0 whenever \sigma>1-\dfrac{0.05035}{h(t)}+\dfrac{0.0349}{h(t)^2}, where h(t)=\tfrac{27}{164}\log|t|+7.096. *Conditional on:* Patel bound |zeta(1/2+it)|<=307.098|t|^{27/164}.
- **THM-PAPER-0010-5** (Sec. 2 consequence, corollary, scope: asymptotic; Sec. 2). With Thm 1.1, a prime lies between n^3 and (n+1)^3 for all n\ge \exp(\exp(32.76)); with Thm 1.2 and Pintz, \pi(x)-\mathrm{li}(x)\ll x\exp\{-d(\log x)^{3/5}(\log\log x)^{-1/5}\}, d=(56/(2\cdot 3^4 c^3))^{1/5}\ge 0.2123 for c=48.1588.

### Key definitions

- Non-negative trigonometric polynomial P_K(x)=sum_{k<=K} b_k cos kx, b_k>=0, b_1>b_0, P_K>=0
- theta=theta(b_0,b_1) solving sin^2 theta=(b_1/b_0)(1-theta cot theta), 0<theta<pi/2
- smoothing f(u)=lambda e^{lambda u} w(lambda u), w=g*g
- Z(beta,t)=(1-beta)B^{2/3}(log t)^{2/3}(loglog t)^{1/3}
- L_1=log(Kt+1), L_2=loglog(Kt+1)

### Principal lemmas

- **THM-PAPER-0010-L1** (Lemma 4.1; Sec. 4). Zero detector (Ford Lemma 2.2): for s=1+it, -\Re\zeta'/\zeta(s)=\frac1{4\eta}\int \frac{\log|\zeta(s-\eta+2\eta iu/\pi)|-\log|\zeta(s+\eta+2\eta iu/\pi)|}{\cosh^2u}du+\frac{\pi}{2\eta}\sum_{|\Re(s-\rho)|\le\eta}\Re\cot\frac{\pi(\rho-s)}{2\eta}. — *Role:* Converts upper bounds on zeta on two vertical lines into a zero-detecting inequality.
- **THM-PAPER-0010-L2** (Lemma 4.2; Sec. 4 (4.8)). Mollified version (Ford 4.5+4.6) with smoothing f, Laplace transform F, |F_0(z)|\le D/|z|^2; bounds \Re\sum\Lambda(n)f(\log n)n^{-s}. — *Role:* Mollification; choice f(u)=\lambda e^{\lambda u}w(\lambda u), w=g*g from Heath-Brown Lemma 7.5.
- **THM-PAPER-0010-L3** (Lemma 4.4; Sec. 4). For K>1, b_j coefficients of a non-negative trigonometric polynomial of degree K: \int\frac{\sum_{j=1}^K b_j\log|\zeta(1+\eta+ijt_1+iut_2)|}{\cosh^2u}du\ge -2b_0\log\zeta(1+\eta). — *Role:* Generalises Ford Lemma 5.1 to degree K; the place where high-degree polynomials enter.
- **THM-PAPER-0010-L4** (Lemma 4.5/4.6; Sec. 4). For 0<\eta\le1/4, t\ge100: N(t,\eta)\le 1.3478\eta^{3/2}B\log t+0.479+\frac{\log A-\log\eta+\frac32\log\log t}{1.879}; and an explicit bound for \sum_{|1+it-\rho|\ge\eta}|1+it-\rho|^{-2} for t\ge10^4. — *Role:* Local zero-count and tail-of-zeros control; uses Ramare e^{\gamma(\sigma-1)}/(\sigma-1) bound and HSW N(T). Corrects a restriction (eta<=0.019) in Ford's Lemma 4.2 (fn 1, p.9).
- **THM-PAPER-0010-L5** (Lemma 4.7; Sec. 4). If \beta+it is a zero, t\ge10^4, 1-\beta\le\eta/2, no zeros in 1-\lambda<\Re s\le1, t-1\le\Im s\le Kt+1, then an explicit inequality in \lambda,1-\beta,\eta,A,B,b_0,b_1,b,R is satisfied (see paper for full display). — *Role:* Master inequality; contradiction with it gives the region once eta=E(L_2/(BL_1))^{2/3}.
- **THM-PAPER-0010-L6** (Sec. 3.3 (3.6),(3.7); Sec. 3.3, Sec. 8). Degree-40 polynomial P_{40} with b_0=1,b_1=1.74600190914994,\sum_{k\ge1}b_k=3.56453965437134 (Thm 1.1); degree-46 P_{46} with b_1=1.74708744081848, b=3.57440943022073 (Thm 1.2); nonnegativity justified in Sec. 8. — *Role:* Principal source of improvement over Ford (deg 4) and Nielsen (deg 5).

### Proof architecture

Follows Ford 2002 (Korobov-Vinogradov) with Kadiri-type classical argument for Thm 1.3. Zero-detector (Lemma 4.1) -> mollified inequality (4.2) -> bounds on log|zeta| on line inside strip via Richert-Ford |zeta|<=A|t|^{B(1-sigma)^{3/2}}log^{2/3}t (Lemma 4.3) and outside strip via non-negative trig polynomial (Lemma 4.4) -> zero-counting tail (4.5, 4.6) -> master inequality Lemma 4.7 with eta(t)=E(L2/(B L1))^{2/3}. Proof of Thm 1.1 is split by height: 3<=t<=3e12 by RH verification; 3e12<=t<e^{8928} by Thm 1.3; e^{8928}<=t<e^{52238} by Thm 1.4; t>=T0=e^{52238} by extremal argument: define M=inf Z(beta,t) over zeros, Z=(1-beta)B^{2/3}(log t)^{2/3}(loglog t)^{1/3}, assume M<M1=0.048976, build zero-free rectangle of width lambda=M/(B^{2/3}L1^{2/3}L2^{1/3}) using minimality, apply Lemma 4.7 to a near-extremal zero to get M>=M1, contradiction; B^{2/3}/M1<55.241. E=1.8821259 chosen to minimise constant for all t>=3 rather than asymptotically (Ford's E in (4.12) minimises asymptotic only).

Dependency edges: CAND-02337 → Ford 2002 (Korobov-Vinogradov explicit) (extends); CAND-02341 → CAND-02337 (improves A,B input and constants of); CAND-02339 → CAND-02337 (complementary (Littlewood region); cited as [MTY24])

**Imported results.** Ford 2002 (Math Proc/Proc LMS) Lemmas 2.2, 3.4, 4.2-4.6, 5.1, 7.1 and Thm 3; Richert/Ford explicit bound (3.1) with A=76.2,B=4.45; Ramare bound zeta(sigma)<=e^{gamma(sigma-1)}/(sigma-1) via Bastien-Rogalski; Patel: |zeta(1/2+it)|<=307.098|t|^{27/164}; Hasanalizade-Shen-Wong N(T) error 0.1038 log T+0.2573 loglog T+9.3675; Platt-Trudgian: RH verified to 3e12; Jang-Kwon/Xylouris mollifier for Thm 1.3, Kadiri 2005; Pintz for PNT error term

**Techniques.** Ford zero-detector and mollifier (Heath-Brown Lemma 7.5); non-negative trigonometric polynomials of degree 40 and 46 found by simulated annealing; extremal-zero minimality argument creating a zero-free rectangle; explicit zero-counting (Hasanalizade-Shen-Wong); Richert-Ford explicit bound on zeta near the 1-line; sub-Weyl bound of Patel for intermediate region; interval-splitting with numerical verification of RH

## Context and interpretation

**Importance and obstacle overcome.** Gives currently best unconditional explicit regions in several height ranges (per Intro: region of Thm 1.3 best for 3e12<|t|<=exp(64.1); (1.8) for exp(64.1)..exp(1000); Thm 1.4 for exp(1000)..exp(52238); Thm 1.1 beyond). Obstacle: sensitivity of constant to secondary error terms at moderate t, and to polynomial choice; overcome by degree 40/46 polynomials, optimising E for all t, and patching with intermediate regions.

**Relation to prior work.** 

**Limitations and open questions.** Region remains far from RH; asymptotic constant improvement stalls (Sec 1: improving 48.x needs better smoothing, better polynomial, or smaller Richert B). Thm 1.2 has ineffective 'sufficiently large' threshold. Bellotti (CAND-02341) subsequently improves A,B giving 54.004 and 48.0718. Sec. 10 lists future work.

## Research potential

- **Hypotheses that might be weakened.** Constants A=76.2,B=4.45 in (3.1) are the load-bearing input; any reduction of B (as in Bellotti: B=4.43795) propagates as B^{2/3}/M1. RH-verification height H=3e12 can be replaced by later heights to lower the classical constant.
- **Generalizations.** Authors note Khale's Dirichlet L-function analogues could use degree-40+ polynomials; same for Hecke/Dedekind zeta zero-free regions.
- **Candidate connections.** Pintz-type PNT error exponent d; primes between cubes (Dudek, Cully-Hugill); Mertens function and zero-density explicit versions.
- **Reusable lemmas.** Lemma 4.4 (degree-K non-negativity inequality), Lemma 4.5/4.6 (explicit local zero counts with Ramare bound), extremal-zero minimality scheme in Sec. 5.
- **Possible experiments.** Reproduce simulated-annealing search for P_K with K>46 and recompute theta, E optimisation; check nonnegativity of P_40,P_46 by interval arithmetic; recompute the crossover heights exp(8928), exp(52238).
- **Risks / barriers.** Method cannot reach the critical line; improvements are only in constants. Entire result is a statement about |t|>3e12 beyond known RH verification, so no bearing on RH itself.

## Audit notes (Level 1 reader)

none noticed in inspected portion (Sections 5 proof beyond the case split and Sections 6-10, computations in Sec. 8, were not read in detail; numerical constants not independently recomputed). Paper itself flags and corrects a hypothesis range in Ford's Lemma 4.2 (footnote 1, Sec. 4).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02337`; harvest queries: kw_zero_free, msc_11M26, msc_11Y35, arxiv_zero_free.
- Triage decision: include — Current best explicit Vinogradov-Korobov zero-free region.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

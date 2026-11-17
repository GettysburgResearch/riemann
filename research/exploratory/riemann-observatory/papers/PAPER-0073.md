# PAPER-0073 — Pair correlation estimates for the zeros of the zeta function via semidefinite programming

| Field | Value |
|---|---|
| Authors | Chirre, Andrés; Gonçalves, Felipe; de Laat, David |
| Year / stratum | 2020 / S6 |
| Venue | Adv. Math. 361, Article ID 106926, 22 p. (2020). |
| Identifiers | zbMATH [1472.11230](https://zbmath.org/?q=an:1472.11230) · DOI [10.1016/j.aim.2019.106926](https://doi.org/10.1016/j.aim.2019.106926) · arXiv [1810.08843](https://arxiv.org/abs/1810.08843) |
| MSC | 11M06, 11M26, 41A30 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1810.08843 |
| Selection | score 4.4885, in-pool citations 9, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Within Montgomery's pair correlation method (under RH or GRH), can optimising over the Cohn-Elkies-type class of functions (f even, f(0)=\hat f(0)=1, \hat f\ge0, f eventually non-positive) by semidefinite programming improve bounds on N^*(T)/N(T), proportion of simple/distinct zeros, and small gaps N(x,T)\gg N(T)?

**Historical motivation.** Montgomery 1973 gave N^*(T)<=(4/3+o(1))N(T) under RH; Montgomery-Taylor improved to 1.3275 (optimal for bandlimited \hat f supported in [-1,1]); Goldston-Gonek-Ozluk-Snyder 1.3262 under GRH; previous best pair-correlation bounds on simple zeros 67.27%, small gaps 0.6068 (Carneiro-Chandee-Littmann-Milinovich).

### Main results

- **THM-PAPER-0073-1** (Theorem 1, theorem (conditional, computer-assisted), scope: asymptotic; Sec.2, p.3). Assume RH: $N^*(T)\le(1.3208+o(1))N(T)$. Assume GRH for Dirichlet L-functions: $N^*(T)\le(1.3155+o(1))N(T)$, where $N^*(T)=\sum_{0<\gamma\le T}m_\rho$ counts zeros with multiplicity. *Conditional on:* RH, GRH.
- **THM-PAPER-0073-2** (Corollary 2, corollary, scope: asymptotic; Sec.2). Under RH, $N_s(T)\ge(0.6792+o(1))N(T)$; under GRH, $N_s(T)\ge(0.6845+o(1))N(T)$ (simple zeros), via $N_s\ge2N-N^*$. *Conditional on:* RH, GRH.
- **THM-PAPER-0073-3** (Corollary 3, corollary, scope: asymptotic; Sec.2). Under RH, $N_d(T)\ge(0.8477+o(1))N(T)$; under GRH, $N_d(T)\ge(0.8486+o(1))N(T)$ (distinct zeros), combining Theorem 1 with Bui-Heath-Brown $N_s\ge(19/27+o(1))N$ and inequality $2N_s\le N^*-5N+6N_d$. *Conditional on:* RH, GRH.
- **THM-PAPER-0073-4** (Theorem 4, theorem (conditional, computer-assisted), scope: asymptotic; Sec.2). Assuming RH and the simple-zeros-type hypothesis (2) ($N^*(T)\sim N(T)$): $N(0.6039,T)\gg N(T)$. Assuming GRH and (2): $N(0.5769,T)\gg N(T)$, where $N(x,T)=\#\{0<\gamma,\gamma'\le T:0<\gamma'-\gamma\le 2\pi x/\log T\}$. *Conditional on:* RH, GRH, (2).
- **THM-PAPER-0073-5** (Theorem 5, theorem (conditional), scope: asymptotic; Sec.2.1). Assuming GRH, for the Chandee-Lee-Liu-Radziwill averaged simple-zeros functional over primitive Dirichlet characters with $\Phi$, $M\Phi(ix)\ge0$: $N_{\Phi,s}(Q)\ge(0.9350+o(1))N_\Phi(Q)$. *Conditional on:* GRH.
- **THM-PAPER-0073-6** (Theorem 6 / Corollary 7, theorem (conditional), scope: asymptotic; Sec.2.2). Assuming RH, zeros of $\xi'(s)$ satisfy $N_1^*(T)\le(1.1175+o(1))N_1(T)$, hence $N_{1,s}\ge(0.8825+o(1))N_1$ and $N_{1,d}\ge(0.9412+o(1))N_1$. *Conditional on:* RH.

### Principal lemmas

- **THM-PAPER-0073-L1** (Lemma 8; Sec.3.1, p.7). For $f\in\mathcal A_{LP}$ and $Z(f)=r(f)+\frac2{r(f)}\int_0^{r(f)}f(x)x\,dx$: under RH $N^*(T)\le(Z(f)+o(1))N(T)$; under GRH (using $F(x,T)\ge\frac32-|x|-o(1)$ for $1\le|x|\le\frac32-\delta$ from Goldston-Gonek-Ozluk-Snyder) $N^*(T)\le(\tilde Z(f)+O(\delta)+o(1))N(T)$ with the extended functional $\tilde Z$. — *Role:* Reduces counting multiplicity to a convex optimisation: uses Montgomery F(x,T)=T^{-2|x|}\log T+|x|+o(1) for |x|\le1 (Goldston-Montgomery), non-negativity of F, and \hat g(x)\le0 for |x|\ge1.
- **THM-PAPER-0073-L2** (Lemma 9; Sec.3.1). For $f\in\mathcal A_{LP}$ and $\varepsilon>0$, assuming RH and (2): $N(P(f)+\varepsilon,T)\gg N(T)$ with $P(f)=\inf\{\lambda>0:p_f(\lambda)>0\}$, $p_f(\lambda)=-1+\frac\lambda{r(f)}+\frac{2r(f)}\lambda\int_0^{r(f)/\lambda}\hat f(x)x\,dx$; GRH analogue with $\tilde p_f$. — *Role:* Converts small-gap problem to finding f with p_f(lambda)>0 for smallest lambda.
- **THM-PAPER-0073-L3** (Lemma 10; Sec.3). GRH analogue for Dirichlet L-functions averaged over q in [Q,2Q] (Chandee-Lee-Liu-Radziwill framework): bound on proportion of simple zeros in terms of an LP-type functional. — *Role:* Yields Theorem 5.
- **THM-PAPER-0073-L4** (Lemma 11; Sec.3). RH bound for N_1^*(T) for zeros of xi'(s) in terms of a functional Z_1(f) based on F_1(x,T) (Farmer-Gonek-Lee Theorem 1.1). — *Role:* Yields Theorem 6.
- **THM-PAPER-0073-L5** (Sec.4.1 SDP formulation; Sec.4.1-4.1.1). Functions f(x)=-(s_1(x^2)+(x^2-R^2)s_2(x^2))e^{-\pi x^2} with SOS polynomials s_i and \hat f=(s_3(x^2)+x^2s_4(x^2))e^{-\pi x^2} (Laguerre basis L_k^{-1/2}) ; objective Z(f) linear in the Gram matrices, so for fixed R the inner problem is an SDP; outer one-dimensional search over R (Brent). d=40, sdpa-gmp, Julia/Nemo/Arb. — *Role:* Numerical optimisation plus rigorous verification: positive definiteness of Gram matrices checked in interval arithmetic with b>=(1+2d)B correction making the identity I(X1,...,X4)=0 exact; Z(f) upper-bounded by interval arithmetic with incomplete Gamma identity (16).

### Proof architecture

(1) Montgomery's F(x,T) and Fourier identity (8) turn sums over pairs of zeros into integrals of \hat g against F. (2) Using F>=0 (Mueller/Heath-Brown), the asymptotic F(x,T)=T^{-2|x|}logT+|x|+o(1) for |x|<=1 (unconditionally in T-structure but RH-conditional), and \hat g<=0 outside [-1,1], deduce Lemma 8/9 inequalities (GRH adds F>=3/2-|x| for 1<=|x|<3/2). (3) Optimise the resulting functionals over the Cohn-Elkies-type class A_LP (relaxation of band-limited class: instead of supp \hat f in [-1,1] only \hat f<=0... as written f eventually nonpositive and \hat f>=0). (4) Parametrise A_LP by SOS polynomials times Gaussian, giving SDP; solve with high precision; certify rigorously via interval arithmetic and spectral margin correction. Optimiser files and verification script are attached in the arXiv version (Z-40.txt, tildeZ-40.txt, L-40.txt, Z1-40.txt, P-40.txt, tildeP-40.txt).

Dependency edges: CAND-01861 → Montgomery 1973 pair correlation (extends/optimises); CAND-01861 → Cohn-Elkies 2003 linear programming bound (imports framework)

**Imported results.** Montgomery 1973: pair correlation F(x,T) asymptotics for |x|<1 (RH); Goldston-Montgomery refined uniform version (Lemma 8 of [29]); Mueller / Heath-Brown: F(x,T)>=0; Goldston-Gonek-Ozluk-Snyder: F(x,T)>=3/2-|x|-o(1) on 1<=|x|<=3/2-delta under GRH; Chandee-Lee-Liu-Radziwill: framework and asymptotic N_Phi(Q) for averages over primitive Dirichlet characters (Lemma 2.1 of [16]); Farmer-Gonek-Lee: F_1 for xi' zeros (Theorem 1.1); Bui-Heath-Brown: 19/27 simple zeros under RH (used in Cor 3); Cohn-Elkies 2003: linear programming bound framework

**Techniques.** Montgomery pair correlation function F(x,T); Cohn-Elkies linear programming bounds (sphere packing) transplanted to zeta zeros; sum-of-squares / semidefinite programming; Laguerre polynomial basis, Gaussian times polynomial ansatz; high-precision SDP (sdpa-gmp) with rigorous post-verification by Arb ball arithmetic; bilevel optimisation (Brent's method)

## Context and interpretation

**Importance and obstacle overcome.** Provides the best known pair-correlation-method constants (Thm 1: 1.3208; GRH 1.3155; small gaps 0.6039/0.5769) by relaxing the bandlimited class to the Cohn-Elkies class and making the optimisation convex via SDP. Obstacle: the larger class (not compactly supported \hat f) has no closed-form extremiser; certification of numerical SDP output is nontrivial and is handled with interval arithmetic and a PSD-margin trick.

**Relation to prior work.** Improves Montgomery, Montgomery-Taylor, Cheer-Goldston (67.27% simple zeros), Goldston-Gonek-Ozluk-Snyder (GRH), Carneiro-Chandee-Littmann-Milinovich (0.6068), Sono and Chandee-Lee-Liu-Radziwill (Dirichlet L-functions: 93.22% -> 93.50%), Farmer-Gonek-Lee (85.83% for xi'). Note Bui-Heath-Brown (19/27=70.37%) via a different method remains better for the proportion of simple zeros of zeta (stated in paper).

**Limitations and open questions.** Bounds are still far from the conjectured c=1 and gap constant 0; numerical optimum depends on d=40, no proof of optimality; rigorous certificate covers only the specific function found, not extremality; the method requires pair-correlation asymptotics available only for |x|<=1 (or 3/2 under GRH), so asymptotic improvement ceilings exist. Note paper observes instability of optimisers in R; Bui-Heath-Brown simple-zeros proportion not improved.

## Research potential

- **Hypotheses that might be weakened.** Theorem 4 uses hypothesis (2) N^*(T)~N(T) (all zeros simple asymptotically) -- can be replaced by a quantitative version with proportion lower bound combining Cor 2/Bui-Heath-Brown; Theorems 1, 4 need RH (or GRH for Dirichlet L-functions for the improved constants).
- **Generalizations.** Replace F(x,T) known range |x|<=1 by larger-range partial results (Conrey-Snaith / Rodgers ratios-conjecture-based) to extend ALP optimisation; apply to pair correlation of other L-function families (Rudnick-Sarnak n-level), to correlations used in the de Bruijn-Newman argument (CAND-01803) via small gap constant; use higher-correlation (triple) SDP analogues.
- **Candidate connections.** Cohn-Elkies/Viazovska sphere packing duality: extremal functions in dimension 1 have Fourier eigenfunction structure -- possible exact dual/extremal solutions; relation to Montgomery-Taylor extremal; combination with Carneiro-Chandee-Milinovich style Beurling-Selberg extremals; small-gap constant feeds Rodgers-Tao Lambda>=0 (needs only positive proportion of gaps below lambda*mean, lambda>0.77 known). The improved lambda=0.6039 (Thm 4) is a quantitative strengthening of the small-gap input used there.
- **Reusable lemmas.** Lemmas 8-9 (inequalities converting pair-correlation Fourier functionals into N^*(T) and N(x,T)); the certification procedure in Sec.4.1.1 (b>=(1+2d)B criterion) is reusable for other proof-producing SDP computations.
- **Possible experiments.** (a) Rerun the supplied scripts/matrices (Z-40.txt etc.) and verify with independent interval arithmetic; (b) increase degree d beyond 40 and check stability of constants (1.3208); (c) try dual SDP certificate / lower bound on achievable constant within A_LP to detect optimality; (d) incorporate the weight w(u)=4/(4+u^2) variants.
- **Risks / barriers.** Fundamental barrier: pair correlation method with |x|<=1 information cannot give N^*(T)<=(1+o(1))N(T) or N(x,T) for small x beyond a limiting value; each improvement is a small numerical gain. Method cannot reach 100% simple zeros; and statements remain conditional on RH/GRH.

## Audit notes (Level 1 reader)

Proof of Lemma 8 uses F(x,T) formula (9) 'uniformly for |x|<=1' written as T^{-2|x|}log T+|x|(1+o(1)); in the extracted text the parenthesisation is ambiguous (T^{-2|x|}\log T + |x| inside bracket with (1+o(1))), minor typesetting ambiguity. Abstract mentions 'other L-functions' and 'sums involving multiplicities'; the main theorems are all conditional on RH/GRH, and Theorem 4 additionally assumes (2). Otherwise none noticed in inspected portion; the computer-assisted verification was not re-run.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01861`; harvest queries: kw_pair_correlation, kw_zeta_zeros, msc_11M06, msc_11M26, arxiv_pair_corr, arxiv_zeta_zeros.
- Triage decision: include — Semidefinite programming improves pair-correlation consequences.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

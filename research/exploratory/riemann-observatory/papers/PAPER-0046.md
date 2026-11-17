# PAPER-0046 — Zeros of the Riemann zeta function on the critical line

| Field | Value |
|---|---|
| Authors | Feng, Shaoji |
| Year / stratum | 2012 / S5 |
| Venue | J. Number Theory 132, No. 4, 511-542 (2012). |
| Identifiers | zbMATH [1333.11086](https://zbmath.org/?q=an:1333.11086) · DOI [10.1016/j.jnt.2011.10.002](https://doi.org/10.1016/j.jnt.2011.10.002) · arXiv [1003.0059](https://arxiv.org/abs/1003.0059) |
| MSC | 11M26, 11M06 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/1003.0059 |
| Selection | score 4.563, in-pool citations 27, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Improve the Levinson-Conrey lower bound for kappa (proportion of zeros of zeta on the critical line) by using a new mollifier whose coefficients are mu(j) times Selberg-type correction sums over primes dividing j (designed to mollify zeta+zeta'/log T, i.e., a truncation of 1/(zeta + zeta'/L)), keeping Conrey's length y=T^{4/7-eps} for the main piece and length T^{1/2-eps} for the prime-sum pieces.

**Historical motivation.** Selberg 1942 (positive proportion), Levinson 1974 (0.3420), Levinson/Lou-Yao/Conrey improvements to 0.3658, then Conrey 1989 (0.4088) using Deshouillers-Iwaniec, then Bui-Conrey-Young's two-piece mollifier 0.4105; Feng's idea is to mollify zeta+zeta'/log T directly by truncating 1/(zeta+zeta'/L).

### Main results

- **THM-PAPER-0046-1** (Theorem 1, theorem (unconditional), scope: asymptotic; Sec 1 eq (1.10); proof Sec 5). $\kappa\ge0.4128$, where $\kappa=\liminf_{T\to\infty}N_0(T)/N(T)$ (at least 41.28% of zeros of zeta lie on the critical line; multiplicity counted).
- **THM-PAPER-0046-2** (Theorem 2, theorem (general bound formula), scope: asymptotic; Sec 5, eq (5.4)). Let $L=\log T$, $R>0$, $\theta<4/7$, $\theta_1<1/2$, $I\ge2$, $P_1(0)=0,P_1(1)=1$, $P_l(0)=0$ ($l\ge2$) real polynomials, $Q$ real with $Q(0)=1$, $Q'(x)=Q'(1-x)$. Then $\kappa\ge1-\frac1R\log\Big(\int_0^1Q(-\frac d{da})Q(-\frac d{db})\frac{F(\theta,\theta_1,b,a,t)-e^{-a-b}F(\theta,\theta_1,-a,-b,t)}{\theta_1(a+b)}\Big|_{a=b=-R}dt+\int_1^{\theta/\theta_1}Q(-\frac d{da})Q(-\frac d{db})\frac{F^*(\theta,\theta_1,b,a,t)-e^{-a-b}F^*(\theta,\theta_1,-a,-b,t)}{\theta_1(a+b)}\Big|_{a=b=-R}dt\Big)$, with $F,F^*$ given by (4.48),(4.49).
- **THM-PAPER-0046-3** (Mollifier (1.11)/(2.2)-(2.4), definition, scope: finite; Sec 1 (1.11), Sec 2 Lemma 1 (2.3)-(2.4)). $B(s)=\sum_{j\le y}a_jj^{-s-R/L}$, $y=T^\theta$; for $y_1<j\le y$, $a_j=\mu(j)P_1(\frac{\log y/j}{\log y})$; for $j\le y_1=T^{\theta_1}$, $a_j=\mu(j)\big[P_1(\frac{\log y/j}{\log y})+\sum_{p_1p_2|j}\frac{\log p_1\log p_2}{\log^2y_1}P_2(\frac{\log y_1/j}{\log y_1})+\sum_{p_1p_2p_3|j}\frac{\log p_1\log p_2\log p_3}{\log^3y_1}P_3(\cdot)+\dots+\sum_{p_1\cdots p_I|j}\frac{\prod\log p_i}{\log^Iy_1}P_I(\cdot)\big]$.
- **THM-PAPER-0046-4** (Corollary 1 ('theta=1 conjecture'), conditional corollary, scope: conditional; Sec 5, Corollary 1 (5.5)). If Lemma 2 (hence Theorem 2) were valid for every $\theta=\theta_1<1$ (the 'theta=1 conjecture'), then $\kappa\ge0.6107$ (with $\theta=\theta_1=1-\varepsilon$, $R=0.7721$, $I=3$). *Conditional on:* Lemma 2 valid for theta=theta_1<1.
- **THM-PAPER-0046-5** (Parameters of Thm 1 proof, numerics, scope: computational; Sec 5 after Theorem 2). $\theta=4/7-\varepsilon$, $\theta_1=1/2-\varepsilon$, $R=1.3025$, $I=3$, $P_1(x)=x+0.2950x(1-x)-2.2345x(1-x)^2+1.882x(1-x)^3$, $P_2(x)=0.0849x+1.9824x^2$, $P_3(x)=0.7516x$, $Q(x)=1-0.6684x-1.0798(x^2/2-x^3/3)-5.0447(x^3/3-x^4/2+x^5/5)$, then $\varepsilon\to0$ gives $0.4128$.

### Key definitions

- Mollifier B(s) with coefficients a_j of (2.3)-(2.4)
- Sigma(alpha,beta) (2.8), E_alpha(j) (2.12), F(j,w)=prod_{p|j}(1-p^{-w})
- kappa=liminf N_0(T)/N(T)

### Principal lemmas

- **THM-PAPER-0046-L1** (Lemma 1; Sec 2 (2.2)-(2.6)). Under the standard Levinson-Conrey reduction (1.1), Littlewood's lemma and $a_j\ll1,a_1=1$: $\kappa\ge1-\frac1R\log\Big(\frac1T\int_1^T|BV(\sigma_0+it)|^2dt\Big)+o(1)$, $\sigma_0=\frac12-\frac RL$, $V(s)=Q(-\frac1L\frac d{ds})\zeta(s)$, with the mollifier coefficients (2.3)-(2.4). — *Role:* Reduction to a mean-value integral
- **THM-PAPER-0046-L2** (Lemma 2 (due to Conrey); Sec 2). With $\Delta=T^{1-\delta}$, $0<\delta<1$, $g(\alpha,\beta,w)=\frac1{i\Delta\pi}\int_{(1/2)}e^{((s-s_0)/\Delta)^2}\zeta(s+\alpha)\zeta(1-s+\beta)B(s)B(1-s)ds$ and $\Sigma(\alpha,\beta)=\sum_{h,k\le y}\frac{a_ha_k}{h^{1+\alpha}k^{1+\beta}}(h,k)^{1+\alpha+\beta}$: $g(\alpha,\beta,w)=\frac{\Sigma(\beta,\alpha)-e^{-(\alpha+\beta)L}\Sigma(-\alpha,-\beta)}{\alpha+\beta}+o_\delta(1)$ uniformly, for $y\le T^{4/7-\varepsilon}$ and bounded $a_j\ll1$. — *Role:* Imported from Conrey 1989 (uses Deshouillers-Iwaniec Kloosterman sum bounds); reduces the whole mean-value problem to the arithmetic quadratic form Sigma(alpha,beta)
- **THM-PAPER-0046-L3** (Lemma 3 (Conrey); Sec 2 (2.13)-(2.14)). For real polynomial $P$ with $P(0)=0$: $S=\sum_{n\le y/j,(n,j)=1}\frac{\mu(n)}{n^{1+\alpha}}P(\frac{\log y/nj}{\log y})=\frac1{F(j,1+\alpha)}\big(\alpha P(\frac{\log y/j}{\log y})+\frac1{\log y}P'(\frac{\log y/j}{\log y})\big)+O\big(\frac{(\log\log y)^2F_1(j,1-2\delta)}{\log^2y}\big)+\dots$ uniformly for $j\le y$, $\alpha\ll1/\log y$. — *Role:* Evaluates the Mobius sums inside E_alpha(j) with the main polynomial P_1
- **THM-PAPER-0046-L4** (Lemmas 4-9; Sec 2). Mertens' theorem (L4), Levinson's Lemmas 5 and 6, and lemmas L7-L9 on sums over m, square-free j and prime tuples with weights f(log/log y). — *Role:* Technical tools for evaluating E_alpha(j) (Sec 3) and Sigma(alpha,beta) (Sec 4); not read in detail
- **THM-PAPER-0046-L5** ((1.12)-(1.14) (motivation); Sec 1). Selberg's minimization: $\sum_{m,n\le y}\frac{a_ma_n}{mn}(m,n)\ge1/\sum_{n\le y}\frac{\mu^2(n)}{\varphi(n)}=\frac{1+o(1)}{\log y}$ for $a_1=1$, equality at $a_n=\mu(n)\frac{nL(y/n;n)}{\varphi(n)L(y;1)}\approx\mu(n)\frac{\log y/n}{\log y}$. — *Role:* Explains the Levinson mollifier as minimization of a quadratic form and motivates adding prime-sum terms to mollify zeta+zeta'/log T through the expansion 1/(zeta+zeta'/L)=1/zeta - zeta'/(zeta^2 L)+...

### Proof architecture

Standard Levinson-Conrey framework: Littlewood lemma gives kappa>=1-(1/R)log(mean square of B V on sigma_0); Balasubramanian-Conrey-Heath-Brown reduces the mean square to g(alpha,beta,w) (2.7); Conrey's Lemma 2 reduces g to Sigma(alpha,beta) (valid for y<=T^{4/7-eps}); Sec 3 evaluates E_alpha(j)=sum_{j|h<=y} a_h h^{-1-alpha} using Lemma 3 for the main polynomial P_1 and Lemmas 5-9 for the prime-sum terms; Sec 4 evaluates Sigma(alpha,beta)=sum_j j^{1+alpha+beta}F(j,1+alpha+beta) E_alpha(j)E_beta(j) in terms of functions F,F^* (4.48)-(4.49) split into ranges j<=y_1 and y_1<j<=y; Sec 5 assembles Theorem 2 and inserts numerically optimized polynomials (I=3) to get 0.4128; Corollary 1 repeats with theta=1-eps.

Dependency edges: CAND-01232 → Conrey 1989 (Lemma 2, kappa>=0.4088) (imports Lemma 2 and the Sigma(alpha,beta) reduction); CAND-01232 → CAND-01215 (contemporaneous independent improvement; BCY comment on theta admissibility); CAND-01232 → Levinson 1974 (uses f=zeta + zeta'/log T framework)

**Imported results.** Conrey 1989 Lemma 2 (Sigma reduction for y=T^{4/7-eps}, requires only a_j<<1 and a_1=1); Balasubramanian-Conrey-Heath-Brown 1985; Levinson 1974/1975 lemmas (L5, L6); Conrey 1989 Lemma 3; Deshouillers-Iwaniec 1982/1984 (through Conrey); Mertens' theorem; Selberg's quadratic form result

**Techniques.** Levinson method with f=Q(-(1/L)d/ds)zeta; Littlewood lemma; Balasubramanian-Conrey-Heath-Brown mean value method; Conrey's mean value theorem for mollifiers of length T^{4/7-eps} (Deshouillers-Iwaniec Kloosterman sums); Selberg quadratic-form minimization heuristic; Dirichlet convolution expansion of 1/(zeta+zeta'/L); Mertens-type and Euler-Maclaurin evaluation of sums over square-free j with prime-tuple weights

## Context and interpretation

**Importance and obstacle overcome.** Claims 0.4128 > 0.4105 (BCY) > 0.4088 (Conrey). Obstacle: selecting extra mollifier terms that capture the zeta'-perturbation while remaining within the length range (theta_1<1/2) where the evaluation is rigorous; the prime-sum terms of 'length' y_1=T^{1/2-eps} avoid new off-diagonal analysis because Conrey's Lemma 2 handles arbitrary bounded coefficients a_j.

**Relation to prior work.** Same framework as Conrey 1989; same time as and independent of Bui-Conrey-Young (CAND-01215). BCY remark (arXiv v2) that Feng's formulas are correct, except they cannot verify his originally-claimed length theta=4/7-eps for the new mollifier; with theta_1=1/2-eps, which is admissible, Feng's mollifier would surely improve 0.4088. The v2 reading here uses theta_1=1/2-eps and gets 0.4128. Subsequent work (Pratt-Robles-Zaharescu-Zeindler 2020) reaches kappa>5/12=0.41666 using more pieces and kappa*>0.4056 etc.; Feng's number was the record until then.

**Limitations and open questions.** Gains tiny relative to the full RH. Method cannot reach 100% without theta infinity-like conjectures (Farmer) or R->0; Zhang/Feng small-gap results show a positive proportion of zeros of zeta + zeta'/L is near the line. Corollary 1 shows only 0.6107 even if theta=1 were allowed. Author suggests combining with BCY to improve both kappa and kappa^*. Numerical constant 0.4128 rests on evaluating the complicated functions F,F^* with the given polynomials; verification not independently provided.

## Research potential

- **Hypotheses that might be weakened.** Lemma 2 needs only a_j<<1,a_1=1, y<=T^{4/7-eps}; the prime-sum pieces are restricted to j<=y_1=T^{1/2-eps} only by the author's evaluation of E_alpha(j), not by Lemma 2, so extending theta_1 toward 4/7 (and I larger) is an explicit open optimization.
- **Generalizations.** Number of prime terms I (here I=3) can be increased; replace Q-polynomial family; combine with BCY's chi-twisted second piece; apply to simple zeros kappa* (Q linear) and to other families (Dirichlet L, GL(2)) where Levinson-Conrey works; apply to prime-gap conditional results as claimed in abstract.
- **Candidate connections.** Ties with the 'L-function families/generalized structures' programme: the Dirichlet-convolution identities (mu*Lambda)(j)=-mu(j) log j etc. generate a natural hierarchy for mollifying derivatives; link with Farmer's theta=infinity conjecture and with the Hejhal/Conrey-Snaith ratios-conjecture predictions of the optimal mollified moment.
- **Reusable lemmas.** Theorem 2 (explicit variational formula for kappa in terms of polynomials P_1,...,P_I,Q,R,theta,theta_1) is a reusable certificate-style statement; Lemma 3 and the Selberg quadratic form motivation are reusable heuristics.
- **Possible experiments.** Independently implement F and F^* (4.48),(4.49) and evaluate the integrals in (5.4) with the listed polynomials in rigorous interval arithmetic to confirm kappa>=0.4128; then optimize over I>=4, higher-degree P_l and over theta_1 up to 4/7, checking the robustness to BCY's caveat.
- **Risks / barriers.** If the admissibility range of theta_1 for the prime-sum pieces were smaller than 1/2 the claimed bound would change (BCY flagged only theta=4/7 for the new mollifier); the proof is long (30 pages of dense computation) with a single published refereed version; the numerics are unverifiable without recomputation. Even a correct 0.4128 is a local-statistical positive-proportion statement not bearing on RH.

## Audit notes (Level 1 reader)

Triage note says 'later superseded by 41%+ Bui-Conrey-Young numerics context'; in fact 0.4128 exceeds BCY's 0.4105, so Feng's is the stronger bound (BCY and Feng are independent, contemporaneous, Feng's later 0.4128 was the record until Pratt et al. 2020). Statement of Lemma 2 as printed lets the main mollifier use y=T^{theta}, theta=4/7-eps; coefficient a_j must satisfy a_j<<1 uniformly, and the prime-sum terms sum log p_1...log p_l/log^l y_1 over p_1...p_l|j are bounded (not verified in the text beyond the claim 'a_j<<1'). Abstract states 41.28% matching Thm 1; text near (2.1) says 'a_j<<1, a_1=1' - for j divisible by square factors the prime-sum terms are included in a_j in (2.4) yet the heuristic (1.16) only holds for squarefree j (the author says these contribute lower order but this is not detailed). Sections 3-4 (the core computation) not read in detail. Q condition 'Q'(x)=Q'(1-x)' as written is equivalent to Q(x)+Q(1-x)=const used in BCY. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01232`; harvest queries: kw_zeta_zeros, msc_11M06, msc_11M26, arxiv_critical_line, arxiv_zeta_zeros.
- Triage decision: include — Landmark improvement of critical-zero proportion (Feng's 41.28%).
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

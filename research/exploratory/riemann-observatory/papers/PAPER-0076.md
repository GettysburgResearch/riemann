# PAPER-0076 — Perturbed moments and a longer mollifier for critical zeros of \(\zeta \)

| Field | Value |
|---|---|
| Authors | Pratt, Kyle; Robles, Nicolas |
| Year / stratum | 2018 / S6 |
| Venue | Res. Number Theory 4, No. 1, Paper No. 9, 26 p. (2018). |
| Identifiers | zbMATH [1444.11170](https://zbmath.org/?q=an:1444.11170) · DOI [10.1007/s40993-018-0103-4](https://doi.org/10.1007/s40993-018-0103-4) · arXiv [1706.04593](https://arxiv.org/abs/1706.04593) |
| MSC | 11M06, 11M26, 11L05, 11L26, 11L07 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1706.04593 |
| Selection | score 4.4561, in-pool citations 8, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** For a Dirichlet polynomial A(s)=sum_{n<=N=T^theta} a_n n^{-s}, what is the asymptotic (with shifts alpha,beta<<1/L) of the twisted second moment I(alpha,beta)=int zeta(1/2+alpha+it) zeta(1/2+beta-it) |A(1/2+it)|^2 Phi(t/T) dt, how far can theta be pushed for structured coefficients (Feng mollifier mu^2(n)(mu*Lambda^{*k})(n)f(n), Conrey mollifier mu(n)f(n)), and what does this give for kappa, the liminf proportion of zeta zeros on the critical line (Levinson method)?

**Historical motivation.** Levinson 1/3; Conrey 2/5 (theta=4/7); Bui-Conrey-Young 41.05%; Feng's 41.28% claim was found to have a gap in the error terms. This paper repairs it for the Feng mollifier at length 6/11, validating theta=1/2, and obtains kappa>0.4149.

### Main results

- **THM-PAPER-0076-1** (Theorem 1.1, theorem, scope: asymptotic; Sec. 1.2, p. 3; proved Secs. 3-4). Let $L=\log T$, $\alpha,\beta\ll L^{-1}$, $A(s)=\sum_{n\le N}a_n n^{-s}$, $N=T^\theta$, $\Phi$ smooth supported in $[1,2]$ with $\Phi^{(j)}\ll_j L^j$. Then $I(\alpha,\beta)=\sum_{d,e\le N}\frac{a_d\overline{a_e}}{[d,e]}\frac{(d,e)^{\alpha+\beta}}{d^{\alpha}e^{\beta}}\int_{-\infty}^{\infty}\Big(\zeta(1+\alpha+\beta)+\zeta(1-\alpha-\beta)\big(\tfrac{2\pi de}{t(d,e)^2}\big)^{\alpha+\beta}\Big)\Phi(t/T)\,dt+O(E)$, with $E=T^{3/20}N^{33/20}+N^{1/2}T^{1/2+\epsilon}$ if $a_n\ll n^\epsilon$ (exponents as read from the garbled text layer); $E=T^\epsilon(N^{11/6}+N^{11/12}T^{1/2})$ if $a_n=\mu^2(n)(\mu*\Lambda^{*k})(n)f(n)$, $f\in\mathcal F$; $E=T^\epsilon(N^{7/4}+N^{7/8}T^{1/2})$ if $a_n=\mu(n)f(n)$, $f\in\mathcal F$. Here $\mathcal F=\{f(n)=P(\log(N/n)/\log N)\}$, $P$ a polynomial. The asymptotic is therefore nontrivial for $\theta<17/33$ (generic), $\theta<6/11$ (Feng), $\theta<4/7$ (Conrey).
- **THM-PAPER-0076-2** (Remark 1.1, remark, scope: asymptotic; Sec. 1.2, p. 3). As $\alpha,\beta\to0$ the main term of Thm 1.1 tends to $\sum_{d,e\le N}\frac{a_d a_e}{[d,e]}\int(\log\frac{t(d,e)^2}{2\pi de}+2C_0)\Phi(t/T)dt$, the Bettin-Chandee-Radziwill main term (via $\zeta(1+s)=1/s+C_0+O(s)$).
- **THM-PAPER-0076-3** (Theorem 1.2, theorem, scope: asymptotic; Sec. 1.3, pp. 3-4). Cross-moment with two Dirichlet polynomials $A=\sum_{n\le N}a_n n^{-s}$, $B=\sum_{k\le K}b_k k^{-s}$, $N=T^{\theta_1}$, $K=T^{\theta_2}$: $\Upsilon(\alpha,\beta)=\int\zeta(\tfrac12+\alpha+it)\zeta(\tfrac12+\beta-it)AB(\tfrac12+it)\Phi(t/T)dt$ equals $\sum_{n\le N,k\le K}\frac{a_nb_k(n,k)^{\alpha+\beta}}{[n,k]n^\alpha k^\beta}\int(\zeta(1+\alpha+\beta)+\zeta(1-\alpha-\beta)(\frac{2\pi nk}{t(n,k)^2})^{\alpha+\beta})\Phi(t/T)dt+O(E)$ with three explicit error terms (generic coefficients, Feng-type $a_n$ with $b_n\ll n^\epsilon$, Conrey-type $a_n=\mu f$ with $b_n\ll n^\epsilon$), listed on p. 4 of the source.
- **THM-PAPER-0076-4** (Remark 1.3, remark, scope: asymptotic; p. 4). Coupling the Conrey mollifier with a generic polynomial in Thm 1.2, the limiting exponent in the error becomes $4/7$.
- **THM-PAPER-0076-5** (Theorem 1.3, theorem, scope: asymptotic; p. 4). For $a_n,b_n\ll n^\epsilon$, $N\ge K$, the moment $J(\alpha,\beta)=\int\zeta(\tfrac12+\alpha+it)\zeta(\tfrac12+\beta-it)|A|^2|B|^2(\tfrac12+it)\Phi(t/T)dt$ has main term as in Thm 1.1 with $a_d:=\sum_{nk=d}a_nb_k$ and sums over $d,e\le NK$, with error $E=T^\epsilon(T^{1/2}N^{3/4}K+T^{1/2}NK^{1/2}+N^{7/4}K^{3/2})$.
- **THM-PAPER-0076-6** (Sec. 5 (result), computation, scope: global; Sec. 5, pp. 20-21). With two-piece mollifier $\psi=\psi_1+\psi_2$ ($\psi_1$ Conrey, $N_1=T^{\theta_1}$, $\theta_1=4/7-\epsilon$; $\psi_2$ Feng with $K=3$, $N_2=T^{\theta_2}$, $\theta_2=6/11-\epsilon$), $R=1.3025$ and the explicit polynomials $P_1,P_2,P_3,Q$ on p. 21, the Levinson/Littlewood-lemma inequality $\kappa\ge1-\frac1R\log\big(\frac1T\int_1^T|V\psi(\sigma_0+it)|^2dt\big)+o(1)$ yields unconditionally $\kappa\ge0.41491637$ (cf. Bui-Conrey-Young 0.4105, Feng 0.4107 corrected, Feng's contested 0.4128).

### Key definitions

- I(alpha,beta) twisted second moment (1.5)
- class F of mollifier shapes f(n)=P(log(N/n)/log N)
- Feng mollifier a_n=mu^2(n)(mu*Lambda^{*k})(n)f(n)
- kappa=liminf N_0(T)/N(T)
- V(s)=Q(-(1/L)d/ds)zeta(s)

### Principal lemmas

- **THM-PAPER-0076-L1** (Lemma 2.1 (Deshouillers-Iwaniec); Sec. 2.2, pp. 5-6). For $A,B,N,V\ge1$, $|c(a,n)|\le1$: $\sum_{v\le V,b\le B}\sum_{n\le N}\sum_{a\le A}c(a,n)e(\bar{\varrho}ab\bar n/v)$ (with coprimality conditions) $\ll(ABNV)^{1/2+\epsilon}\{(BV)^{1/2}+(A+N)^{1/4}[BV(N+\varrho A)(V+\varrho A^2)+\varrho A^2B^2N]^{1/4}\}$. — *Role:* Imported; bounds Type II / incomplete Kloosterman sums after separating variables for Feng and Conrey coefficients.
- **THM-PAPER-0076-L2** (Lemma 2.2 (Bettin-Chandee); Sec. 2.2, p. 6). $\sum_{a\sim A}\sum_{m\sim M,n\sim N,(m,n)=1}\nu_a\alpha_m\beta_n e(a\bar m/n)\ll\|\alpha\|\|\beta\|\|\nu\|(1+A/(MN))^{1/2}((AMN)^{7/20+\epsilon}(M+N)^{1/4}+(AMN)^{1/8+\epsilon}(AN+AM)^{3/8})$. — *Role:* Imported; gives the generic-coefficient exponent 17/33 (Bettin-Chandee-Radziwill).
- **THM-PAPER-0076-L3** (Approximate functional equation (2.3); Sec. 2.1, p. 4-5). With pole annihilator $G(s)=e^{s^2}p(s)$, $p(s)=((\alpha+\beta)^2-(2s)^2)/(\alpha+\beta)^2$: $\zeta(\tfrac12+\alpha+it)\zeta(\tfrac12+\beta-it)=\sum_{m_1,m_2}\frac{(m_1/m_2)^{-it}}{m_1^{1/2+\alpha}m_2^{1/2+\beta}}V_{\alpha,\beta}(m_1m_2,t)+X_{\alpha,\beta,t}\sum\frac{(m_1/m_2)^{-it}}{m_1^{1/2-\beta}m_2^{1/2-\alpha}}V_{-\beta,-\alpha}(m_1m_2,t)+O_A((1+|t|)^{-A})$. — *Role:* Starting point (adapted from Young and Bui-Conrey-Young); G vanishes at +-(alpha+beta)/2 to cancel poles as alpha+beta->0.
- **THM-PAPER-0076-L4** (Diagonal / off-diagonal analysis; Secs. 3.1-3.2, pp. 6-8). Split $m_1n_2=m_2n_1$ (diagonal, yields $\zeta(1+\alpha+\beta+2s)$ contour integral) from $m_1n_2-m_2n_1=\Delta\ne0$; truncate $|\Delta|\le D=MN_1T^{-1+\epsilon}$ by repeated integration by parts after a dyadic partition of unity; the off-diagonal supplies the second main term and an error expressed via sums of $e(a\bar n_1/n_2)$. — *Role:* Reduces the moment to exponential sums.
- **THM-PAPER-0076-L5** (Type I/II separation for mu^2(mu*Lambda^{*k}); Sec. 4, text lines ~1320-1345). For coprime $u,g$, $(\mu*\Lambda^{*j})(ug)=\sum_{s}\sum(\mu*\Lambda^{*s})(u)(\mu*\Lambda^{*(j-s)})(g)$ ($2^j$ terms); with $\mu^2(dn_1)=\mu^2(d)\mu^2(n_1)$ and the binomial theorem in $(\log n_1)^j$ one separates $d$ from $n_1$, enabling Type I/II treatment with incomplete Kloosterman sums. — *Role:* Key new input exploiting mollifier structure; gives 6/11 instead of 17/33.

### Proof architecture

(1) Approximate functional equation for zeta(1/2+alpha+it)zeta(1/2+beta-it) with pole annihilator G; (2) expand |A|^2, integrate in t: diagonal m1 n2=m2 n1 gives one main term via zeta(1+alpha+beta+2s); (3) off-diagonal m1 n2 - m2 n1 = Delta, truncated by integration by parts, gives the second main term zeta(1-alpha-beta)(...)^{alpha+beta} plus an error in sums of Kloosterman-fraction exponentials; (4) generic a_n: Bettin-Chandee trilinear bound (Lemma 2.2) as in BCR; Feng coefficients: separate variables via the coprime splitting of (mu*Lambda^{*j}), Type I/II decomposition, Deshouillers-Iwaniec (Lemma 2.1) giving 6/11; Conrey mu f gives 4/7; (5) Theorems 1.2, 1.3 follow similarly; (6) Sec. 5 inserts a two-piece mollifier into Levinson's method and optimizes numerically.

**Imported results.** Bettin-Chandee, Trilinear forms with Kloosterman fractions, arXiv 1502.00769; Bettin-Chandee-Radziwill, mean square of zeta times Dirichlet polynomials, J. reine angew. Math.; Deshouillers-Iwaniec exponential sum bounds (Invent. Math. 1982/83); Levinson's method / Littlewood's lemma (Titchmarsh Ch. 9-10; Conrey 1989); Main-term computations of Conrey, Bui-Conrey-Young, Feng (reused with new parameters)

**Techniques.** approximate functional equation with pole annihilator; diagonal vs off-diagonal analysis; Type I/Type II decomposition of mollifier coefficients; Deshouillers-Iwaniec bounds for sums of Kloosterman fractions; Bettin-Chandee trilinear Kloosterman bound; Levinson method / Littlewood lemma; numerical optimization of mollifier polynomials

## Context and interpretation

**Importance and obstacle overcome.** First rigorous long-mollifier asymptotic (theta=6/11>1/2) exploiting arithmetic shape of the Feng mollifier. Generic Kloosterman-fraction bounds stop at 17/33; structured coefficients allow Type I/II splitting where incomplete Kloosterman bounds apply.

**Relation to prior work.** Extends Bettin-Chandee-Radziwill (generic a_n, theta<17/33) by adding shifts alpha,beta (needed for Levinson) and structured-coefficient gains; completes Feng's program; superseded by Pratt-Robles-Zaharescu-Zeindler (5/12).

**Limitations and open questions.** Error exponents only 6/11 (Feng) and 4/7 (Conrey), far from theta=1 (Lindelof) and theta=infinity (RH by Bettin-Gonek). Footnote 2 says pushing the Feng length from 6/11 to (perhaps) 4/7 requires more effort (later done by Pratt-Robles-Zaharescu-Zeindler). The final kappa uses main-term formulas imported from earlier papers, not rederived.

## Research potential

- **Hypotheses that might be weakened.** The restriction to coefficients mu^2(mu*Lambda^{*k})f or mu f: the Type I/II splitting needs only approximate separability of a_{dn}; coefficients like mu*log-type or those from mollifying zeta^{(j)} could be treated similarly.
- **Generalizations.** Analogues for Dirichlet L-functions / Selberg class with Kloosterman fractions replaced by other exponential sums; shifted moments with other twist families.
- **Candidate connections.** Bettin-Gonek: theta=infinity Conrey-Levinson mollifier implies RH, so each increase in admissible theta is a quantitative step along the moments-to-RH direction; link with Farmer's theta=infinity conjecture and the ratios conjecture.
- **Reusable lemmas.** Lemmas 2.1 and 2.2 with the coprime splitting of (mu*Lambda^{*j})(ug) are reusable for bilinear forms with Kloosterman fractions; Theorem 1.1's main term is a black box.
- **Possible experiments.** Numerically evaluate I(alpha,beta) for T~1e6-1e8 with Feng coefficients at theta slightly above 6/11 to detect any extra off-diagonal main term; re-optimize kappa with stated polynomials to reproduce 0.41491637.
- **Risks / barriers.** Barrier is Weil/Kloosterman-type bounds; beyond 4/7 needs genuinely new bounds on sums of Kloosterman fractions. No route from this method to RH itself.

## Audit notes (Level 1 reader)

Theorem 1.3 as printed concludes for 'I(alpha,beta)' with d,e<=NK although the integral defined is J(alpha,beta) (notational slip, p. 4). Error-term formulas in Thm 1.1/1.2 were read from a garbled text layer; Feng and Conrey exponents check out (N=T^{6/11}: N^{11/6}=T, N^{11/12}T^{1/2}=T; N=T^{4/7}: N^{7/4}=T, N^{7/8}T^{1/2}=T). Final kappa in Sec. 5 depends on imported main-term computations not reproduced here. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01881`; harvest queries: msc_11M06, msc_11M26, arxiv_critical_line.
- Triage decision: include — Longer mollifier for critical zeros, directly improves proportion method.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

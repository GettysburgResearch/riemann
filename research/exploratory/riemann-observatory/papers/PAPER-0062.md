# PAPER-0062 — Gaps between zeros of the Riemann zeta-function

| Field | Value |
|---|---|
| Authors | Bui, H. M.; Milinovich, M. B. |
| Year / stratum | 2018 / S6 |
| Venue | Q. J. Math. 69, No. 2, 403-423 (2018). |
| Identifiers | zbMATH [1447.11094](https://zbmath.org/?q=an:1447.11094) · DOI [10.1093/qmath/hax047](https://doi.org/10.1093/qmath/hax047) · arXiv [1410.3635](https://arxiv.org/abs/1410.3635) |
| MSC | 11M26, 11M06 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1410.3635 |
| Selection | score 4.5252, in-pool citations 11, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Unconditionally, how large are gaps between consecutive zeros of zeta on the critical line (Lambda = limsup (t_{n+1}-t_n)/(2 pi/log t_n)) and between multiple zeros (Lambda*)? Method: Hall's Wirtinger-inequality method with an amplified product zeta(1/2+it) zeta(1/2+it+i kappa pi/L) M(1/2+it) and twisted fourth moments.

**Historical motivation.** Selberg 1946 (Lambda>1), Hall (2.63), Bredberg (2.76), Mueller's method conditional results; Montgomery's pair correlation conjecture predicts Lambda=lambda=infinity; Ben Arous-Bourgade GUE-based precise conjecture.

### Main results

- **THM-PAPER-0062-1** (Theorem 1.1, theorem, scope: asymptotic; Sec. 1.1, p.2; proof Sec. 2.2, 2.6). $\Lambda>3.18$, where $\Lambda=\limsup_{n\to\infty}\frac{t_{n+1}-t_n}{2\pi/\log t_n}$ over consecutive zeros on the critical line. Consequently, assuming RH, $\lambda>3.18$ for consecutive zeros $\gamma_n$.
- **THM-PAPER-0062-2** (Theorem 1.2, theorem, scope: asymptotic; Sec. 1.1, p.2; proof Sec. 2.3, 2.6). $\Lambda^\star>4.05$, where $\Lambda^\star=\limsup (t^\star_{n+1}-t^\star_n)/(2\pi/\log t_n^\star)$ over ordinates of multiple zeros on the critical line (set $\Lambda^\star=\infty$ if only finitely many multiple zeros).
- **THM-PAPER-0062-3** (Theorem 2.1 (Wirtinger-type), theorem, scope: finite; Sec. 2.1). For f,f' continuous complex-valued on [a,b]: (i) if $f(a)=f(b)=0$ then $\int_a^b|f|^2\le((b-a)/\pi)^2\int_a^b|f'|^2$; (ii) if $f(a)=f(b)$ and $\int_a^bf=0$ then $\int_a^b|f|^2\le((b-a)/2\pi)^2\int_a^b|f'|^2$.
- **THM-PAPER-0062-4** (Theorem 2.2, theorem, scope: asymptotic; Sec. 2.5, p.6). For $\vartheta<1/4$, $F(t,v,\kappa,M)=e^{ivtL}\zeta(\tfrac12+it)\zeta(\tfrac12+it+i\tfrac{\kappa\pi}{L})M(\tfrac12+it)$, $M(s)=\sum_{h\le y}d_r(h)P[h]h^{-s}$, $y=T^\vartheta$: $\int|F^{(j)}|^2w(t/T)dt=\frac{c_j(v,\kappa)A_{r+2}(\log y)^{r^2+4r}L^{4+2j}}{2(r^2-1)!((r-1)!)^4}\hat w(0)T+O(TL^{(r+2)^2+2j-1})$, j=0,1,2, with $c_j$ an explicit 9-fold integral over $[0,1]^9$.
- **THM-PAPER-0062-5** (Numerical certificate (Sec. 2.6), computation, scope: computational; Sec. 2.6). With $\vartheta=1/4,r=1,v=1.26,P(x)=1-5.8x+6.4x^2$: $h_1(1.26,3.18,M)>1.0002$; with $\vartheta=1/4,r=1,v=1.25,P(x)=1-5.2x+5.5x^2$: $h_2(1.25,4.05,M)>1.0048$, where $h_1=c_0/(\kappa^2c_1)$, $h_2=4c_1/(\kappa^2c_2)$. *Conditional on:* Theorem 2.2.

### Key definitions

- $L=\log(T/2\pi)$
- $\Lambda=\limsup(t_{n+1}-t_n)/(2\pi/\log t_n)$ for consecutive critical-line zeros; $\lambda$ same for all zeros $\gamma_n$
- $F(t,v,\kappa,M)=e^{ivtL}\zeta(1/2+it)\zeta(1/2+it+i\kappa\pi/L)M(1/2+it)$
- $h_1(v,\kappa,M)=\limsup\frac{L^2\int|F|^2}{\kappa^2\int|F'|^2}$, $h_2=\limsup\frac{4L^2\int|F'|^2}{\kappa^2\int|F''|^2}$

### Principal lemmas

- **THM-PAPER-0062-L1** (Sec. 2.2 criterion; Sec. 2.2). If $\Lambda\le\kappa$ then $\int_T^{2T}|F|^2\le(1+o(1))\frac{\kappa^2}{L^2}\int_T^{2T}|F'|^2$, so $h_1:=\limsup\frac{L^2}{\kappa^2}\frac{\int|F|^2}{\int|F'|^2}>1$ implies $\Lambda>\kappa$ (apply Wirtinger (i) between consecutive zeros of F; F mimics a real function via factor $e^{ivtL}$). — *Role:* Reduction of gap problem to mean-value ratios.
- **THM-PAPER-0062-L2** (Sec. 2.3 criterion; Sec. 2.3). For multiple zeros a,b of F one has $F'(a)=F'(b)=0$ and $\int_a^bF'=0$, so Wirtinger (ii) gives $\int|F'|^2\le((b-a)/2\pi)^2\int|F''|^2$; $h_2:=\limsup\frac{4L^2}{\kappa^2}\frac{\int|F'|^2}{\int|F''|^2}>1$ implies $\Lambda^\star>\kappa$. — *Role:* First use of Wirtinger (ii) for zeros of zeta.
- **THM-PAPER-0062-L3** (Lemma 3.1; Sec. 3, (5)). For $\vartheta<1/4$ and shifts $\alpha_j,\beta_j\ll L^{-1}$, $I_{\alpha,\beta}(M)=\int\zeta(\tfrac12+\alpha_1+it)\zeta(\tfrac12+\alpha_2+it)\zeta(\tfrac12+\beta_1-it)\zeta(\tfrac12+\beta_2-it)M(\tfrac12+\alpha_3+it)M(\tfrac12+\beta_3-it)w(t/T)dt=\frac{c(\alpha,\beta)A_{r+2}(\log y)^{r^2+4r}L^4}{2(r^2-1)!((r-1)!)^4}\hat w(0)T+O(TL^{(r+2)^2-1})$ uniformly, with c(alpha,beta) an explicit integral over [0,1]^9. — *Role:* Core shifted twisted fourth-moment asymptotic; derivatives in shifts (Cauchy integral formula on radius ~1/L) give the j=1,2 mean values.
- **THM-PAPER-0062-L4** (Theorem 5.1 (Bettin-Bui-Li-Radziwill); Sec. 5.1). Twisted fourth moment of zeta against Dirichlet polynomial of length $y=T^\vartheta$, $\vartheta<1/4$, with explicit six-term main term $Z_{\alpha_1,\alpha_2,\beta_1,\beta_2,h,k}$ and error $O_\epsilon(T^{1/2+2\vartheta+\epsilon}+T^{3/4+\vartheta+\epsilon})$. — *Role:* Imported input extending admissible length from 1/11 (Hughes-Young) to 1/4.
- **THM-PAPER-0062-L5** (Lemmas 4.1, 4.2; Sec. 4). Lemma 4.1: evaluation of sums over $d_r$-weighted divisor-type sums producing Mellin-Barnes integrals; Lemma 4.2: smooth-function identity used to convert sums over $h,k\le y$ into the 9-dimensional integral. — *Role:* Combinatorial/analytic evaluation of the off-diagonal main terms.

### Proof architecture

(1) Suppose Lambda<=kappa; zeros of F (amplified, phase-twisted product) in [T,2T] are separated by at most (1+o(1))kappa pi/L, so Wirtinger (i) summed over consecutive zeros gives int|F|^2 <= (1+o(1))(kappa^2/L^2) int|F'|^2. (2) Reduce to showing h_1>1 via shifted mean values. (3) Compute I_{alpha,beta}(M) with the twisted fourth moment theorem (Thm 5.1, theta<1/4), main term via contour integrals and Lemma 4.1/4.2 giving the 9-fold integral c(alpha,beta) (Lemma 3.1); apply differential operators Q((1/L)(d/dalpha1+d/dalpha2+d/dalpha3)) at alpha_2=i kappa pi/L, beta_2=-i kappa pi/L to get c_0,c_1,c_2 (Thm 2.2). (4) Choose theta=1/4, r=1 and optimise quadratic polynomial P and v numerically so h_1>1 at kappa=3.18 and h_2>1 at kappa=4.05. Multiple-zero case replaces Wirtinger (i) by (ii) applied to F'.

**Imported results.** Wirtinger inequalities (Hardy-Littlewood-Polya, Thms 257, 258); Twisted fourth moment of zeta with theta<1/4 (Bettin-Bui-Li-Radziwill, Thm 5.1); Riemann-von Mangoldt formula N(T)=TL/2pi - T/2pi+O(L); Conrey 2/5 proportion of critical simple zeros (for comparison)

**Techniques.** Wirtinger inequalities (Hall's method); mollifier-type amplifier M(s)=sum d_r(h)P[log(y/h)/log y] h^{-s}; twisted fourth moment of zeta (Bettin-Bui-Li-Radziwill); shifted-moment / ratios-conjecture style recipe turned rigorous; Cauchy integral formula to differentiate asymptotics in shifts; numerical optimisation of 9-dimensional integral over polynomial P

## Context and interpretation

**Importance and obstacle overcome.** Improves unconditional Hall-method bound (Bredberg Lambda>2.76; Hall 2.63) to 3.18, and under RH surpasses all Mueller-method results (previous best lambda>2.9 under RH, 3.072 under GRH). Obstacle: short admissible Dirichlet polynomial in twisted fourth moment (theta<1/11 Hughes-Young); overcome by BBLR theta<1/4 and a compact single-integral formulation of the main term.

**Relation to prior work.** Variation of Hall's method as in Bredberg; replaces his amplifier sum_{h<=y}1/h^s (y=T^theta, theta<1/11) with a general d_r-amplifier with polynomial P and theta<1/4 via Bettin-Bui-Li-Radziwill; supersedes Mueller-method results under RH (Bui-Milinovich-Ng 2.9? and Goldston-Gonek-Montgomery-type results).

**Limitations and open questions.** Bound 3.18 is limited by theta<1/4 (twisted fourth moment length) and numeric optimisation over low-degree P; conjecturally Lambda=infinity (GUE; Ben Arous-Bourgade conjecture limsup (gamma_{n+1}-gamma_n) sqrt(log gamma_n/32)=1). Lambda* result has no content unless multiple zeros exist. Upper-bound side (Goldston-Gonek RH limsup<=pi/loglog) untouched. Unconditional statement applies to critical-line zeros t_n only; for gamma_n requires RH.

**Ideas in remarks/appendices/abandoned paths.** Sec. 1.1: if N_s(T)>=(C+o(1))N(T) then Lambda*>=2/(1-C); with Conrey C=2/5 gives 10/3, and Bui-Heath-Brown simple-zero proportion gives Lambda*>=27/4 under RH. Remark in Sec. 2.2: the factor e^{ivtL} (instead of Hardy theta) is chosen purely to simplify computation. Sec. 2.4(IV): first use of Wirtinger (ii) for zeta zeros.

## Research potential

- **Hypotheses that might be weakened.** Any extension of the twisted fourth moment beyond theta=1/4 (conjecturally 1/2) feeds directly into Theorem 2.2 and improves 3.18 and 4.05; constants are limited only by Lemma 3.1's range and P's degree.
- **Generalizations.** Same scheme should give large gaps for Dirichlet L-functions and GL(2) L-functions where twisted fourth moments (or second moments of degree-2 products) are available; also the h_2 construction (Wirtinger ii) for zeros of derivatives or multiple zeros of other L-functions.
- **Candidate connections.** Gaps/spacing distribution feeds Polymath15 heat-flow zero dynamics (CAND-01890: large gaps correspond to low repulsion in dz/dt = 2 sum 1/(z_j-z_k)); also quantitative simple-zero proportion results (Bui-Heath-Brown) give Lambda*>=27/4 under RH.
- **Reusable lemmas.** Theorem 2.2 (explicit 9-fold integral c_j(v,kappa) for mean squares of amplified zeta^2 products and derivatives) is a reusable mean-value engine; Lemma 3.1 for shifted twisted fourth moment.
- **Possible experiments.** Re-evaluate c_0,c_1,c_2 by independent quadrature and optimise P with higher degree (degree 3-5) and r>1 to see how far 3.18 moves at theta=1/4; verify the claim h_1>1.0002 margin is robust to quadrature error (very thin margin).
- **Risks / barriers.** Wirtinger method intrinsically bounded by how well F can be made to look real; beyond ~3.2-3.5 may need fundamentally different amplifier or ratios-conjecture level information.

## Audit notes (Level 1 reader)

Numerical certificates use theta=1/4 while Theorem 2.2/Lemma 3.1 are stated for theta<1/4; the passage to theta=1/4 (or theta slightly smaller with continuity of h_j) is not spelled out in the inspected portion, and the margin h_1>1.0002 is thin. Sec. 3 refers to 'Theorem 2.3' though only Theorem 2.2 is stated (apparent typo). Abstract/Theorem 1.1 uses limsup over critical-line zeros t_n; transfer to gamma_n requires RH (stated). Otherwise none noticed in inspected portion; proofs in Sec. 4-5 were not read line by line.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01835`; harvest queries: kw_moments_zeta, kw_zeta_zeros, msc_11M06, msc_11M26, arxiv_critical_line, arxiv_zeta_zeros.
- Triage decision: include — Large gaps between zeros, current record.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

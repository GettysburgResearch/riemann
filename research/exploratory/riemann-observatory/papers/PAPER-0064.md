# PAPER-0064 — The \(\theta = \infty\) conjecture implies the Riemann hypothesis

| Field | Value |
|---|---|
| Authors | Bettin, Sandro; Gonek, Steven M. |
| Year / stratum | 2017 / S6 |
| Venue | Mathematika 63, No. 1, 29-33 (2017). |
| Identifiers | zbMATH [1370.11101](https://zbmath.org/?q=an:1370.11101) · DOI [10.1112/S0025579316000139](https://doi.org/10.1112/S0025579316000139) · arXiv [1604.02740](https://arxiv.org/abs/1604.02740) |
| MSC | 11M06, 11M26 |
| Families | C |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1604.02740 |
| Selection | score 4.5146, in-pool citations 4, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Does Farmer's theta=infinity conjecture (Levinson-type mollified second moment I_N(0,T) << T^{1+eps} for mollifiers of length N up to T^theta, theta arbitrarily large) force the Riemann hypothesis? Answer: yes, and a finite theta gives a quantitative zero-free half-plane.

**Historical motivation.** Levinson's method (1974) gives a proportion of critical zeros from upper bounds of I_N; Conrey extended theta from 1/2 to 4/7. Farmer conjectured I_{T^theta}(0,T) ~ (1+1/theta)T for all theta>0 and showed it gives kappa=1; Radziwill showed kappa=1 via Levinson needs arbitrarily long mollifiers. This note shows the conjecture is not just a 100%-on-the-line statement but implies RH.

### Main results

- **THM-PAPER-0064-1** (Theorem 1, theorem, scope: conditional; Introduction, Theorem 1; proof Section 2). Let $\theta>0$ and suppose that for every $\varepsilon>0$, $I_N(0,T)\ll_\varepsilon T^{1+\varepsilon}$ uniformly for $2\le N\le T^\theta$, where $I_N(T_1,T_2)=\int_{T_1}^{T_2}|M_N(\tfrac12+it)|^2|\zeta(\tfrac12+it)|^2dt$ and $M_N(s)=\sum_{n\le N}\frac{\mu(n)}{n^s}\big(1-\frac{\log n}{\log N}\big)$. Then $\zeta(s)$ has no zeros in $\Re s>\tfrac12+\tfrac1{2\theta}$. In particular, if this holds with $\theta$ arbitrarily large, RH is true. *Conditional on:* theta=infinity-type mollified second moment bound.
- **THM-PAPER-0064-2** (Theorem 2, theorem, scope: conditional; Introduction, Theorem 2). Let $\theta>0$ and suppose for every $\varepsilon>0$, $I_N(T,2T)\ll_\varepsilon T^{1+\varepsilon}$ for $2\le N\le T^\theta$. Then $\zeta(s)$ has no zeros in $\Re s>\tfrac12+\tfrac2\theta$; if true for arbitrarily large $\theta$, RH holds (nontrivial only for $\theta>4$). *Conditional on:* theta=infinity-type bound on [T,2T].
- **THM-PAPER-0064-3** (Remark after Thm 2, remark, scope: asymptotic; Introduction after Theorem 2 (formulas as printed, no proof given)). If $\zeta$ had a unique simple zero $\rho_0=\beta_0+i\gamma_0$, $\gamma_0>0$, $\beta_0>1/2$, then $I_N(T,2T)=c_1\frac{N^{2\beta_0-1}\log T}{T^3\log^2N}\big(1+\Re N^{2i\gamma_0}\frac{|\zeta'(\rho_0)|^2}{\zeta'(\rho_0)^2}+o(1)\big)+O(T^{1+\varepsilon}+N^{\beta_0-1/2+\varepsilon}/T)$, consistent with the bound only if $\theta<4$; and $I_N(0,T)=\frac{N^{2\beta_0-1}}{\log^2N}(C(N)+o(1))+O(T^{1+\varepsilon}+N^{\beta_0-1/2+\varepsilon}T^\varepsilon)$ with $C(N)$ bounded away from 0 (stated without proof), so $I_{T^\theta}(0,T)\ll T^{1+\varepsilon}$ implies $\beta_0\le\frac12+\frac1{2\theta}$. *Conditional on:* hypothetical zero configuration.

### Key definitions

- $I_N(T_1,T_2)$ mollified second moment of zeta with Levinson-type mollifier $M_N$
- $M_x(s)\log x=\sum_{n\le x}\mu(n)n^{-s}\log(x/n)$ (extension to real x>0, M_1:=0)
- $H_t(w)=\int_1^\infty M_x(\tfrac12+it)(\log x)x^{-w}dx=\frac1{(w-1)^2\zeta(w-\frac12+it)}$ for $\Re w>3/2$
- auxiliary $G_t(w)=\frac{(w-1)^2(w-\frac32+it)\zeta(w-\frac12+it)}{(w+1)^2(w-\frac12+it-\rho_0)(w+it+1)^4}$

### Principal lemmas

- **THM-PAPER-0064-L1** ((2.2); Section 2). $g_t(u)=\frac1{2\pi i}\int_{3-i\infty}^{3+i\infty}G_t(w)u^{-w}dw$ vanishes for $u>1$ and is $O(1)$ for $0\le u\le1$ (G_t holomorphic in $\Re w\ge0$ with $G_t(w)\ll(1+|w+it|)^{-5/2}$). — *Role:* Compactly supported kernel making the Mellin convolution J_t(x) depend only on M_y for y<=x
- **THM-PAPER-0064-L2** ((2.4)-(2.5); Section 2). $J_t(x)=\frac1{2\pi i}\int G_tH_tx^wdw$ satisfies $J_t(x)\ll\int_1^x|M_y(\tfrac12+it)|\log y\,dy$ and, by shifting to $\Re w=0$, $J_t(x)=O(1)+\frac{x^{\rho_0+\frac12-it}(\rho_0-1)}{(\frac32+\rho_0-it)^2(\rho_0+\frac32)^4}$ (residue at the pole w=rho_0+1/2-it of 1/zeta(w-1/2+it)). — *Role:* Isolates a single off-line zero rho_0 as a growing term x^{beta_0+1/2}/(1+|t|)^2 dominating the mollifier integral
- **THM-PAPER-0064-L3** (unnumbered chain; Section 2). Cauchy-Schwarz gives $\frac{x^{2\beta_0}}{(1+|t|)^4}+\frac1x\ll\int_1^x|M_y(\tfrac12+it)|^2\log^2y\,dy$; multiplying by $|\zeta(\frac12+it)|^2$ and integrating over [T_1,T_2] with $\int_{T_1}^{T_2}|\zeta(1/2+it)|^2dt\gg T_2\log(T_2+2)$ ($0\le T_1\le T_2/2$) gives $\frac{x^{2\beta_0}\log(T_1+2)}{|1+T_1|^3}+\frac{T_2\log(T_2+2)}{x}\ll\log^2x\int_1^xI_y(T_1,T_2)dy$. — *Role:* Converts pointwise lower bound into lower bound for the mollified second moment

### Proof architecture

Assume a zero rho_0=beta_0+i gamma_0 with beta_0>=1/2. Mellin transform of M_x(1/2+it)log x is 1/((w-1)^2 zeta(w-1/2+it)); multiply by G_t (which cancels the zeta factor and contains the pole at rho_0) so J_t(x) is both bounded by an L^1 average of |M_y| (via compactly supported kernel g_t) and, by contour shift, has main term x^{beta_0+1/2}/(1+|t|)^2. Cauchy-Schwarz in y, multiplication by |zeta(1/2+it)|^2 and integration in t over [0,T], with x=T^theta, gives T^{2 beta_0 theta} << T^{1+eps+theta}; letting T->infinity yields beta_0<=1/2+1/(2theta). Theorem 2 stated to follow in the same way with T_1=T,T_2=2T.

Dependency edges: CAND-01843 → Farmer 1993 Mathematika 40 (answers: theta=infinity conjecture is stronger than RH); CAND-01843 → Pintz 1982/83 (method imported); CAND-01843 → CAND-01856 (same authors' technique (Pintz-type isolation of one zero) reappears in Gonek-Graham-Lee)

**Imported results.** Levinson 1974 and Conrey 1989 (context: kappa>1/3, >2/5); Farmer 1993 (theta=infinity conjecture, implies kappa=1); Radziwill, Limitations to mollifying zeta (arXiv 1207.6583); Pintz 1982/83, Oscillatory properties of M(x); Gonek-Graham-Lee, A Generalized Lindelof Hypothesis (unpublished manuscript) for the [T,2T] uniform Omega-result; lower bound int_{T1}^{T2}|zeta(1/2+it)|^2 dt >> T2 log(T2+2)

**Techniques.** Mellin inversion and convolution; contour shift isolating a single zero; Cauchy-Schwarz; Pintz's method for Omega-results for M(x)=sum mu(n) (Acta Arith. 1982/83); lower mean value bound for zeta on the critical line

## Context and interpretation

**Importance and obstacle overcome.** Shows that the theta=infinity conjecture (a heuristically supported moment conjecture) is at least as hard as RH; any further extension of the Levinson-Conrey range (theta>1) already gives a quasi-RH zero-free half-plane Re s>1/2+1/(2theta). The obstacle was to extract a lower bound for mollified moments from a hypothetical single off-line zero, done by the cutoff kernel g_t whose Mellin transform cancels the poles of zeta.

**Relation to prior work.** 

**Limitations and open questions.** Theorem 1 is conditional on an upper bound for I_N for all N up to T^theta; nothing is proved unconditionally. Theorem 2 gives a weaker half-plane (1/2+2/theta) and is nontrivial only for theta>4; the authors say it is essentially best possible for [T,2T] but give the sharpness only as an unproved asymptotic remark. No known unconditional range beyond theta<4/7 (Conrey; later Bui-Conrey-Young 0.5 variants not in this paper).

## Research potential

- **Hypotheses that might be weakened.** Hypothesis I_N(0,T)<<T^{1+eps} uniformly for 2<=N<=T^theta: one could try replacing 'all N' by only N=T^theta (the proof uses x=T^theta only for the final step but integrates I_y over 1<=y<=x, so a dyadic/average-in-N hypothesis suffices: int_1^x I_y dy << x T^{1+eps}); also replacing T^{1+eps} by o(T^{1+1/theta... }) i.e. an asymptotic with explicit error term.
- **Generalizations.** Replace zeta by Dirichlet L-functions or Selberg-class elements (Mellin transform 1/((w-1)^2 L) and the same G_t trick) to get GRH-type consequences from conjectured mollified moments (relevant to Farmer-Gonek-Hughes-type long mollifier asymptotics); also other mollifier shapes (smooth weights).
- **Candidate connections.** Links to Radziwill's limitations of mollifying zeta, Farmer's pair-correlation consequence, Pintz's Omega-results for the Mertens function (the same Mellin-isolate-a-zero mechanism); connects to the generalized Lindelof hypothesis for primes equivalent to RH (Gonek-Graham-Lee).
- **Reusable lemmas.** The G_t/g_t construction (Section 2, (2.2)-(2.5)): compactly supported (in u) kernel with prescribed Mellin transform that cancels 1/zeta and retains a pole at a chosen zero; usable to prove any 'bounded average of M_y' hypothesis excludes zeros.
- **Possible experiments.** Numerically compute I_N(0,T) for T up to 10^6..10^7 and N=T^theta, theta=1,2,3, and compare with Farmer's (1+1/theta)T prediction; verify the smooth-cutoff kernel g_t numerically and the size of the residue term x^{1/2+1/2}/(1+|t|)^2 in the simulated hypothetical-zero model.
- **Risks / barriers.** The hypothesis is a strong conjecture (theta=infinity) not known to follow from anything; Radziwill's limitation shows that mollifiers beyond some length cannot be controlled by present technology; the [T,2T] version needs an Omega-result uniform in t which rests on an unpublished manuscript.

## Audit notes (Level 1 reader)

(1) Proof of Theorem 2 is not given: the text says it 'follows in the same way on taking T_1=T, T_2=2T', although the introduction says the [T,2T] problem 'is more subtle because one needs an Omega-result for M_N(t) that is uniform in t' and cites an unpublished manuscript (Gonek-Graham-Lee) plus Pintz; the extracted proof section only supplies the [0,T] argument where a factor (1+|t|)^{-4} appears with t up to T and the final power comparison would need x^{2 beta_0}/T^{4}-type loss, giving the weaker exponent 1/2+2/theta; the derivation of that exponent is not shown. (2) Intro sentence 'even an upper bound ... for some theta>1 and all N in the range 2<=N<=T^theta implies a zero-free region' is imprecise (it says 'for some theta>1' in the sentence while Theorem 1 holds for any theta>0 with a trivial/ weaker region for small theta). (3) Asymptotic formulas for I_N under a single hypothetical zero are stated without proof. Otherwise the argument for Theorem 1 (Mellin identities, Cauchy-Schwarz, final T^{2 beta_0 theta}<<T^{1+eps+theta}) checks out in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01843`; harvest queries: kw_RH_any, msc_11M06, msc_11M26, arxiv_rh_abs, arxiv_rh_ti.
- Triage decision: include — Short, striking implication theta=infinity conjecture implies RH.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

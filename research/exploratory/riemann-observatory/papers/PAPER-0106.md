# PAPER-0106 — Freezing transitions and extreme values: random matrix theory, \(\zeta(\frac12 +\mathrm{i}t)\) and disordered landscapes

| Field | Value |
|---|---|
| Authors | Fyodorov, Yan V.; Keating, Jonathan P. |
| Year / stratum | 2014 / S5 |
| Venue | Philos. Trans. R. Soc. Lond., Ser. A, Math. Phys. Eng. Sci. 372, No. 2007, Article ID 20120503, 32 p. (2014). |
| Identifiers | zbMATH [1330.82028](https://zbmath.org/?q=an:1330.82028) · DOI [10.1098/rsta.2012.0503](https://doi.org/10.1098/rsta.2012.0503) · arXiv [1211.6063](https://arxiv.org/abs/1211.6063) |
| MSC | 82B44, 60G70, 15B52, 11M50 |
| Families | B, F |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/1211.6063 |
| Selection | score 4.2908, in-pool citations 31, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Does the freezing transition of log-correlated random energy landscapes govern the extreme and high-value statistics of |p_N(theta)| for CUE matrices, and by analogy of |zeta(1/2+it)| over short stretches of the critical line? Predict the distribution of the maximum and the multifractal measure of high points.

**Historical motivation.** Resolve the Montgomery heuristic / FGH conjecture for max |zeta| by exhibiting the fine structure of extremes, tying RMT, zeta and disordered landscapes; explains why the log-correlations give c=3/2 rather than 1/2.

### Main results

- **THM-PAPER-0106-1** (Eq. (11)-(13), Sec. 2.1, prediction (non-rigorous), scope: asymptotic; Sec. 2.1). For $0<\beta<1$, $Z_N(\beta;2\pi)/Z_e$ with $Z_e=N^{1+\beta^2}\frac{G^2(1+\beta)}{G(1+2\beta)\Gamma(1-\beta^2)}$ has density $P(z)=\beta^{-2}z^{-1-1/\beta^2}e^{-z^{-1/\beta^2}}$; for $\beta>1$ the scaled moment $z=Z_N(\beta)(\ln N)^{3/2}/N^{2}$ is predicted to have tail $P(z)\propto z^{-1-1/\beta}\ln z$. *Conditional on:* freezing-transition scenario for log-correlated fields.
- **THM-PAPER-0106-2** (Eq. (17), conjecture, scope: asymptotic; Sec. 2.2). Freezing of the free energy: $-\mathbb E\,\mathcal F(\beta)\to\beta+1/\beta$ for $\beta\le1$ and $2$ for $\beta>1$, where $\mathcal F(\beta)=-\frac1{\beta\log N}\log Z_N(\beta,2\pi)$.
- **THM-PAPER-0106-3** (Eq. (18)-(19), conjecture, scope: asymptotic; Sec. 2.3). $-2\max_{\theta\in[0,L)}\log|p_N(\theta)|\sim a_{N_L}+b_{N_L}x$ with $a_{N_L}=-2\log N_L+c\log\log N_L+o(1)$, $c=3/2$, $b_{N_L}=1+O(1/\log N_L)$, $N_L=NL/2\pi$. For $L=2\pi$ the density of $x$ is $p(x)=2e^{x}K_0(2e^{x/2})$ ($K_\nu$ modified Bessel); the left tail satisfies $p(x)\approx -xe^{x}$ as $x\to-\infty$. (Later proved: Arguin-Belius-Harper, Paquette-Zeitouni, Chhaibi-Madaule-Najnudel for c=3/2 and the law; not part of this paper.) *Conditional on:* freezing scenario.
- **THM-PAPER-0106-4** (Eq. (21)-(24), conjecture, scope: asymptotic; Sec. 2.3(ii)). For mesoscopic arcs $1\ll N_L\ll N$: $x=u\sqrt{-2\ln L}+y$ with u standard Gaussian independent of y; $-g'$ gives density of y, $g_\beta(y)=e^y\frac1{2\pi i}\int e^{-sy}M(s)\Gamma(s-1)ds$ with $M(s)$ in terms of Barnes G (eq. 22); $\mathbb E y=\frac{27}{... }$ as given in (23): $\langle y\rangle=\frac72-2\gamma_E-\ln(2\pi)$, $\langle y^2\rangle_c=\frac{4\pi^2}{3}-\frac{27}{4}$.
- **THM-PAPER-0106-5** (Eq. (25)-(27), conjecture, scope: asymptotic; Sec. 2.4). High points: $\mu_N(x;L)=\frac1L\mathrm{meas}\{\theta:|p_N(\theta)|>N_L^x\}$. For L=2pi, 0<x<1, typical value $\mu_e(x)=N^{-x^2}\sqrt{\frac1{\pi\log N}}\frac{G^2(1+x)}{2xG(1+2x)\Gamma(1-x^2)}$ and $\xi=\mu/\mu_e$ has density $x^{-2}\xi^{-1-1/x^2}e^{-\xi^{-1/x^2}}$; mean $=\mu_e\Gamma(1-x^2)$.
- **THM-PAPER-0106-6** (Eq. (33)-(37), (40), conjecture (zeta), scope: asymptotic; Sec. 2.5). With $\zeta_{\max}(L;T)=\max_{T\le t\le T+L}|\zeta(1/2+it)|$, $0<L\le2\pi$: $-2\log\zeta_{\max}\sim-2\log(\tfrac L{2\pi}\log\tfrac T{2\pi})+c\log\log(\tfrac L{2\pi}\log\tfrac T{2\pi})+x$ with c=3/2 and x distributed as in the CUE case (eq. 19 for L=2pi approx., eq. 21 for L<<2pi); high-point measure scale multiplied by arithmetic factor $a(x)=\prod_p(1-1/p)^{x^2}\sum_{m\ge0}\big(\Gamma(x+m)/(m!\Gamma(x))\big)^2p^{-m}$; and freezing $-\langle\hat F_\zeta(\beta)\rangle=\beta+1/\beta$ ($\beta\le1$), $2$ ($\beta>1$). *Conditional on:* CUE/zeta moment conjectures (Keating-Snaith, CFKRS) at leading order, decoupling of arithmetic factor (a(1)=1).
- **THM-PAPER-0106-7** (Table 1, Sec. 2.6, numerical evidence, scope: computational; Sec. 2.6). Hiary's computations (about 10^7 zeros per height, T from 3.6e7 to 10^22) of the ratio of sample mean of $\zeta_{\max}(2\pi;T)$ to the model mean $e^{\gamma_E}N/(\log N)^c$, N=nearest integer to log T: ratios for c=3/2 are 1.0013, 0.9927, 0.9768, 0.9305 vs about 0.50-0.55 for c=1/2.

### Key definitions

- V_t^{zeta}(x)=-2 log|zeta(1/2+i(t+x))|, V_N^{U}(theta)=-2 log|p_N(theta)|
- Z_N(beta;L)=(1/2 pi)int_0^L |p_N(theta)|^{2 beta} dtheta (partition function)
- mu_N(x;L): relative length of high points {|p_N|>N_L^x}

### Principal lemmas

- **THM-PAPER-0106-L1** (Eq. (6) / Appendix A; Sec. 1, App. A). Heuristic: $\langle V_t(x_1)V_t(x_2)\rangle\approx-2\log|x_1-x_2|$ for $1/\log t\ll|x_1-x_2|\ll1$ and $2\log\log t$ for $|x_1-x_2|\ll1/\log t$. — *Role:* Establishes zeta as a log-correlated field (rigorous at variance level by Bourgade 2010, CAND-01234).
- **THM-PAPER-0106-L2** (Eq. (8); Sec. 1). $V^{(U)}_N(\theta)=\sum_{n\ge1}n^{-1/2}[e^{-in\theta}v_n^{(N)}+c.c.]$, $v_n=n^{-1/2}\mathrm{Tr}\,U_N^n$ tend to iid standard complex Gaussians (Diaconis-Shahshahani). — *Role:* Gaussian-field representation behind the free energy analogy.
- **THM-PAPER-0106-L3** (Eq. (93); Sec. 5). $\frac1T\int_0^T|\zeta(1/2+it)|^{2\lambda}dt\sim a(\lambda)\mathbb E|p_N(\theta)|^{2\lambda}$, $N=\log(T/2\pi)$. — *Role:* Moment conjecture that transfers CUE predictions to zeta.

### Proof architecture

Not a proof paper. Sec. 3 reviews freezing in the random energy model and the 1/f-noise (log-correlated) landscape via replica/duality arguments; Sec. 4 computes high moments of CUE characteristic polynomials (Fisher-Hartwig / Selberg-integral type asymptotics, moments of moments) and interprets them as a partition function whose analytic continuation reveals a duality beta -> 1/beta and freezing at beta=1; the max distribution is extracted from the frozen phase; Sec. 5 transfers to zeta through the moment conjecture. Numerics (Hiary) test c=3/2.

**Imported results.** Keating-Snaith moments of CUE characteristic polynomials; Selberg CLT for log|zeta|; CFKRS conjecture for shifted moments of zeta; Farmer-Gonek-Hughes conjecture on max of zeta; Diaconis-Shahshahani trace moments; Derrida-Spohn / Carpentier-Le Doussal freezing results

**Techniques.** Statistical mechanics of log-correlated fields (REM, freezing, replica trick); Barnes G-function and Fisher-Hartwig moment asymptotics for CUE; Duality beta<->1/beta; Mellin/contour integral representation of the max distribution; Fast zeta evaluation (Hiary amortized-complexity algorithm)

## Context and interpretation

**Importance and obstacle overcome.** Provided the first sharp prediction for the full law of max|zeta| over short intervals (c=3/2, Bessel-K0 type density) and for freezing of moments; later turned into theorems for CUE and partially for zeta (ABBRS). Obstacle: no proof; arithmetic influence on extremes handled only by the heuristic a(1)=1.

**Relation to prior work.** Builds on Farmer-Gonek-Hughes (max over long ranges with independent matrices) and Keating-Snaith; adds freezing/log-correlated viewpoint from Derrida-Spohn, Carpentier-Le Doussal and Fyodorov-Le Doussal-Rosso.

**Limitations and open questions.** All main statements are conjectural/heuristic; zeta extension depends on the arithmetic factor decoupling, and numerics converge very slowly (ratio deteriorates with c=3/2 at small N). Distribution p(x) test is only preliminary. Paper itself notes that extrapolation to ranges of length T is unjustified and that left tail |x|e^x could suggest larger values than Montgomery, which the authors consider unlikely.

## Research potential

- **Hypotheses that might be weakened.** The moment conjecture (eq. 93) is needed at leading order only; a proof of upper bound on E|zeta|^{2beta} over short intervals for beta<=1 would give rigorous partial freezing.
- **Generalizations.** Other L-functions in t-aspect; functions with Sato-Tate-type families; hybrid arithmetic factor corrections to a(x) for x near 1.
- **Candidate connections.** Bourgade 2010 (CAND-01234) supplies the proved log-correlation at variance scale; Selberg-class and Gaussian multiplicative chaos approaches; growth of zeta and Lindelof-type bounds, though freezing is consistent with RH-scale max exp(c log t/loglog t) being far from attained.
- **Reusable lemmas.** Moments-of-moments heuristics as test cases; the contour-integral formula (21)-(22) for the mesoscopic max law as a benchmark for numerics.
- **Possible experiments.** Compute zeta_max(2pi;T) at larger T with Hiary-type algorithm and compare to c=3/2 with log-log corrections; estimate high-point measure mu_T(x) against eq. (37) with a(x); test the L<<2pi mesoscopic formula with Gaussian factor.
- **Risks / barriers.** No rigorous bridge from random matrix extremes to arithmetic zeta; finite-height convergence is logarithmically slow; none of this bears on the location of zeros so no direct RH implication.

## Audit notes (Level 1 reader)

Eq. (23) text writes E{x^2 - <x>^2} for the variable y (notation slip); the mean formula in (23) printed reading 'E y = 27/... ' is a garbled extraction in text, correct value per source is 7/2-2 gamma_E - ln(2 pi). The remark in Sec. 2.4 that mean of mu stays finite as x->1 is stated without proof. Remainder not checked.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01371`; harvest queries: msc_11M50, arxiv_critical_line, arxiv_zeta_extreme.
- Triage decision: include — Freezing transition and extreme values conjecture for zeta.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

# PAPER-0052 — Mesoscopic fluctuations of the zeta zeros

| Field | Value |
|---|---|
| Authors | Bourgade, P. |
| Year / stratum | 2010 / S5 |
| Venue | Probab. Theory Relat. Fields 148, No. 3-4, 479-500 (2010). |
| Identifiers | zbMATH [1250.11080](https://zbmath.org/?q=an:1250.11080) · DOI [10.1007/s00440-009-0237-3](https://doi.org/10.1007/s00440-009-0237-3) · arXiv [0902.1757](https://arxiv.org/abs/0902.1757) |
| MSC | 11M06, 11M50, 60F05, 60B20, 15B52 |
| Families | B, F |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/0902.1757 |
| Selection | score 4.5594, in-pool citations 26, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** What is the joint Gaussian limit of log zeta at nearby points 1/2+eps_t+i f_t^(j)+i omega t when the separations are mesoscopic (between 1/log t and 1), and what does it imply for fluctuations of zero counts on short intervals (Coram-Diaconis question)?

**Historical motivation.** Extends Selberg CLT and Hughes-Nikeghbali-Yor dynamic CLT to the scale where values correlate; explains numerical correlation structure observed by Coram and Diaconis for zero counts, and extends n <-> log t to local scales.

### Main results

- **THM-PAPER-0052-1** (Theorem 1.1, theorem (unconditional), scope: asymptotic; Sec. 1.1, eq. (1.4)-(1.6)). Let $\omega$ be uniform on $(0,1)$, $\varepsilon_t\to0$, $\varepsilon_t\gg 1/\log t$, and $0\le f_t^{(1)}<\dots<f_t^{(\ell)}<c<\infty$ with $\log|f_t^{(j)}-f_t^{(i)}|/\log\varepsilon_t\to c_{i,j}\in[0,\infty]$ for all $i\ne j$. Then $(-\log\varepsilon_t)^{-1/2}\big(\log\zeta(\tfrac12+\varepsilon_t+if_t^{(j)}+i\omega t)\big)_{j\le\ell}$ converges in law to a centered complex Gaussian vector with $\mathrm{cov}(Y_i,Y_j)=1$ if $i=j$, $1\wedge c_{i,j}$ if $i\ne j$. If $\varepsilon_t\ll1/\log t$ the same holds with normalization $(\log\log t)^{-1/2}$ (and in the definition of $c_{i,j}$).
- **THM-PAPER-0052-2** (Corollary 1.2, corollary, scope: asymptotic; Sec. 1.1). Finite-dimensional distributions of $(\log\log t)^{-1/2}\log\zeta(\tfrac12+i\omega t+i(\log t)^{-\delta})$, $0\le\delta\le1$, converge to a centered Gaussian process with kernel $\gamma\wedge\delta$ ($\gamma\ne\delta$), $1$ ($\gamma=\delta$); realized as $X_\delta=B_\delta+D_{1-\delta}$, B Brownian motion, D totally disordered (independent coordinates, variance delta); no measurable version exists.
- **THM-PAPER-0052-3** (Corollary 1.3, corollary, scope: asymptotic; Sec. 1.2, eq. (1.9)). Let $K_t>\epsilon$ with $\log K_t/\log\log t\to\delta\in[0,1)$. Then the finite-dimensional distributions of $\tilde\Delta_t(\alpha,\beta)=\frac{1}{\pi\sqrt{(1-\delta)\log\log t}}\Delta(\omega t+\alpha/K_t,\omega t+\beta/K_t)$ ($\Delta$ = zero count minus smooth expectation) converge to a centered Gaussian process with covariance 1 if (alpha,beta)=(alpha',beta'); 1/2 if exactly one endpoint coincides (same side); -1/2 if beta=alpha'; 0 otherwise. Realized as $\tilde D_\beta-\tilde D_\alpha$, D~ independent N(0,1/2). Recovers Fujii's CLT for delta in [0,1].
- **THM-PAPER-0052-4** (Theorem 1.4, theorem (random matrix analogue), scope: asymptotic; Sec. 1.3). For $u_n$ Haar on $U(n)$, $\varepsilon_n\to0$, $\varepsilon_n\gg1/n$, $0\le\varphi_n^{(1)}<\dots<\varphi_n^{(\ell)}<2\pi-\delta$ with $\log|\varphi^{(j)}_n-\varphi^{(i)}_n|/\log\varepsilon_n\to c_{i,j}$: $(-\log\varepsilon_n)^{-1/2}(\log Z(u_n,e^{\varepsilon_n+i\varphi_n^{(k)}}))_k\to$ complex Gaussian with covariance (1.6); for $\varepsilon_n\ll1/n$ replace by $\log n$.
- **THM-PAPER-0052-5** (Proposition 3.1, proposition (CLT tool), scope: asymptotic; Sec. 3.2). If $a_{pt}\in\mathbb C$ with $\sup_p|a_{pt}|\to0$, $\sum_p|a_{pt}|^2\to\sigma^2$, and there is $m_t$ with $\log m_t/\log t\to0$ and $\sum_{p>m_t}|a_{pt}|^2(1+p/t)\to0$, then $\sum_p a_{pt}p^{-i\omega t}\to\sigma Y$ in law ($\omega$ uniform on (0,1), Y standard complex normal).

### Key definitions

- log zeta(sigma+it)=-int_sigma^infty (zeta'/zeta)(s+it) ds, limit from above at zeros
- Complex standard normal Y=(N1+iN2)/sqrt2
- Delta(t1,t2): zero count in (t1,t2] minus smooth expectation (t/2pi)log(t/2 pi e)
- Convention on log Z(X) for |X|=1 as L^2 limit

### Principal lemmas

- **THM-PAPER-0052-L1** (Lemma 2.2; Sec. 2.2). For $\varepsilon_n\gg1/n$, $\varepsilon_n\to0$, $0<\Delta_n\le2\pi-\delta$, $\log\Delta_n/\log\varepsilon_n\to c$: $\frac1{-\log\varepsilon_n}\sum_{j\le n}\frac{e^{ij\Delta_n}}{je^{2j\varepsilon_n}}\to c\wedge1$. — *Role:* Produces the covariance 1^c in the U(n) case via the Diaconis-Evans theorem.
- **THM-PAPER-0052-L2** (Lemma 2.3; Sec. 2.3). Analogue for $\varepsilon_n\ll1/n$: $\frac1{\log n}\sum_{j\le n}x_n^j/j\to c\wedge1$ with $-\log\Delta_n/\log n\to c$ (as used in proof; exact statement not fully read). — *Role:* Critical-line covariance, also used in Sec. 4 construction.
- **THM-PAPER-0052-L3** (Lemma 3.3 / 3.4; Sec. 3.3-3.4). Prime-sum analogues of Lemmas 2.2/2.3: $\frac{1}{-\log\varepsilon_t}\sum_{p\le t}p^{-1-2\varepsilon_t+i\Delta_t}\to c\wedge 1$ (and log log t version), proved through the prime number theorem. — *Role:* Covariance computation for the zeta side.
- **THM-PAPER-0052-L4** (Selberg approximation (quoted, Sec. 3.1); Sec. 3.1). $\frac1t\int_1^t|\log\zeta(\sigma+is)-\sum_{p\le x}p^{-\sigma-is}|^{2k}ds\le c_{k,a}$ for $1/2\le\sigma\le1$, $t^{a/k}\le x\le t^{1/k}$ (k=1 used). — *Role:* Reduces log zeta to a short Dirichlet polynomial; imported from Selberg.

### Proof architecture

Two parallel proofs. U(n): Cramer-Wald, expand log Z in traces, apply Diaconis-Evans CLT (Thm 2.1, imported) with coefficients a_nj, verify (2.1) via Lemma 2.2/2.3 and (2.2) with m_n = n/(-log eps_n). Zeta: Selberg's L^2 approximation of log zeta by sum over p<=t (hence normalized difference -> 0 in probability), Slutsky, Cramer-Wald, then Prop. 3.1 (Montgomery-Vaughan large sieve inequality + Petrov CLT + moment/mean-in-time comparison with independent uniforms using linear independence of log p, Lemma 3.2), then covariance from Lemma 3.3/3.4 via PNT. Sec. 4 shows the covariance matrix is PSD via a branching-process / Brownian-tree construction (Le Gall).

**Imported results.** Selberg CLT/L^2 approximation of log zeta (Selberg 1946; Tsang thesis; Joyner 1986); Diaconis-Evans 2001 Theorem 2.1 (Trans. AMS 353); Montgomery-Vaughan mean value theorem for Dirichlet polynomials; Petrov Thm 4.1 CLT for sums of independent variables; Titchmarsh Thm 9.3 (N(t) formula)

**Techniques.** Selberg's method of approximating log zeta by Dirichlet polynomials; Montgomery-Vaughan mean value theorem; Cramer-Wald device and Slutsky; Diaconis-Evans trace CLT for CUE; Prime number theorem for covariance asymptotics; Gaussian processes with non-measurable (white-noise-like) component

## Context and interpretation

**Importance and obstacle overcome.** Shows the n <-> log t analogy persists for mesoscopic separations, giving log-correlated structure (covariance ~ min(1,c)) proved unconditionally with no RH, using only L^2 Selberg approximation with Prop. 3.1 replacing moment methods. Obstacle: Selberg approximation holds only in mean square, so convergence is shown via L^2 reduction rather than almost-sure Euler product.

**Relation to prior work.** Generalizes Selberg (single point), Tsang/Joyner (off-axis, eps_t), Hughes-Nikeghbali-Yor (distant points, independent limits) and Fujii (zero-count CLT at one scale); analogue of Diaconis-Evans Thm 6.1 and Wieand for CUE counting.

**Limitations and open questions.** Only finite-dimensional convergence in t-average (not pointwise a.e. in t, not tightness); first-order (variance) scale only; real part and Im part (counting) are treated together but no large deviations. Case of general distinct c_{i,i+1} for counting gives a more complicated covariance, not worked out. No information on extremes or on zeros of an individual zeta. Remark says results hold for Selberg class (no proof given).

## Research potential

- **Hypotheses that might be weakened.** Boundedness f_t<c and existence of the limits c_{i,j}; Selberg-class claim is stated without proof, so it could be made rigorous (needs only L^2 approximation and PNT-type input).
- **Generalizations.** Multiplicative chaos limit / moments of the mesoscopic field (later Arguin-Belius-Bourgade-Radziwill-Soundararajan); functional CLT with tightness; extension to Dirichlet L-functions in the q-aspect.
- **Candidate connections.** Gives the log-correlated field input behind Fyodorov-Keating freezing predictions (CAND-01371): the covariance 1^c(...) is exactly the 'log-correlated' structure used there.
- **Reusable lemmas.** Prop. 3.1 (L^2-mean-value + CLT criterion for sums over primes) is reusable for any t-average CLT of prime sums; Lemmas 3.3/3.4.
- **Possible experiments.** Numerically test (1.9) covariance of zero-count fluctuations at height ~10^22 using Odlyzko data across delta in (0,1); test slow convergence through (log log t)^{-1/2} corrections.
- **Risks / barriers.** Variance-level results do not constrain tails or max; no link to location of zeros, so no direct RH implication.

## Audit notes (Level 1 reader)

Minor: Sec. 4 text says the covariance limit is '(4.1)' but (4.1) defines angles and covariance of interest is (1.6); in Cor 1.3 the case delta=1 (and eps_t=0 normalization) excluded. Nothing else noticed in inspected portion; proofs of Lemma 3.2-3.4 not fully checked.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01234`; harvest queries: msc_11M06, msc_11M50, arxiv_critical_line, arxiv_zeta_zeros.
- Triage decision: include — Multidimensional Selberg CLT; zeros/RMT correspondence at mesoscopic scale.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

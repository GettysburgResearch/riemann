# PAPER-0023 — On the distribution of spacings between zeros of the zeta function

| Field | Value |
|---|---|
| Authors | Odlyzko, A. M. |
| Year / stratum | 1987 / S4 |
| Venue | Math. Comput. 48, 273-308 (1987). |
| Identifiers | zbMATH [0615.10049](https://zbmath.org/?q=an:0615.10049) · DOI [10.2307/2007890](https://doi.org/10.2307/2007890) |
| MSC | 11M06 |
| Families | B |
| Work type | computation_report |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://web.physics.rutgers.edu/grad/682/papers/zeta.pdf |
| Selection | score 4.6026, in-pool citations 85, seed lists 3, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Numerically test the Montgomery pair-correlation conjecture and the GUE hypothesis (zeta zeros behave like eigenvalues of random Hermitian matrices) using rigorously error-bounded values of the first 10^5 zeros and of zeros number 10^12+1 to 10^12+10^5 (height about 2.7e11), and explain anomalies via primes. Correction to triage text: the data are NOT near height 10^20; zero number 10^12 is at height about 2.7e11.

**Historical motivation.** Montgomery (1973) pair correlation and Dyson's observation of GUE; Hilbert-Polya idea; Berry's quantum chaos analogy. Prior large computations (Brent, van de Lune et al.) only verified RH, did not produce accurate zero positions.

### Main results

- **THM-PAPER-0023-1** (Sec. 2 empirical finding (Figs 1-6, Tables 1-2), numerical experiment, scope: finite; Sec. 2, Figs 1-6, Tables 1-2, pp. 279-284). With normalized spacings $\delta_n=(\gamma_{n+1}-\gamma_n)\frac{\log(\gamma_n/2\pi)}{2\pi}$, the empirical pair correlation, density of $\delta_n$ and of $\delta_n+\delta_{n+1}$ for $N=0$ and $N=10^{12}$ (blocks $N<n\le N+10^5$) agree well with GUE predictions $1-(\sin\pi x/\pi x)^2$, $p(0,u)$, $p(1,u)$, and the agreement is markedly better at $N=10^{12}$ than at $N=0$. E.g. second moment of $\delta_n-1$: 0.161 (N=0), 0.176 (N=10^12), GUE 0.180.
- **THM-PAPER-0023-2** (Table 3 (Kolmogorov statistic), numerical experiment, scope: finite; Table 3, p. 287). Kolmogorov distances $D$ of $\delta_n$ from GUE for blocks of $10^5$ zeros: $D=0.0207$ (N=0, prob ~$10^{-37}$), 0.0081 (N=10^8), 0.0052 (10^11), 0.0058 (2e11), 0.0045 (10^12, prob 3.5e-2); for $\delta_n+\delta_{n+1}$ at $N=10^{12}$: $D=0.0091$, prob $1.3\cdot10^{-6}$. Convergence to GUE is slow, consistent with $S(t)$ being tiny (typical size $\sqrt{\log\log T}$).
- **THM-PAPER-0023-3** (Tables 4-5 (small spacings), numerical observation, scope: finite; Tables 4-5, pp. 288-290). For the high blocks (N=10^11, 2e11, 10^12) the counts of $\delta_n<0.05$ (16, 20, 18) and $\delta_n<0.1$ (107,123,124) exceed GUE expectations (13.68, 108.80) whereas low blocks show deficiency; minimal spacings found by Brent ($\delta=0.001235$ at n=41,820,581) and van de Lune et al. ($0.000310$ at n=1,048,449,114) have low GUE probability (Table 5, e.g. 0.048). Author flags that persistence at greater height would question GUE and even pair correlation. (Later work, not in this paper, attributes this to slow convergence with $1/\log^2$ corrections.)
- **THM-PAPER-0023-4** (Eq. (2.29) and Table 6 (long-range autocovariance), numerical observation/conjecture test, scope: finite; Sec. 2, pp. 291-293). Autocovariances $c_k=M^{-1}\sum(\delta_n-1)(\delta_{n+k}-1)$ match Dyson's conjectured GUE value $c_k\approx -1/(2\pi^2k^2)$ for small fixed $k$, but for large $k$ (e.g. $k\approx 950$-$1000$) show statistically significant structured sign patterns, far above the independent-noise level $\approx 5\cdot10^{-4}$.
- **THM-PAPER-0023-5** (Figs 13-15, Landau-type formula discussion, heuristic explanation supported by data, scope: finite; Sec. 2, pp. 294-296, eq. after (2.30)). Spectrum $f(x)=c|\sum_n(\delta_n-1)e^{2\pi i nx}|^2$ has sharp peaks near $x=2(\log N)/\log q$... for prime powers $q=p^m$; explained via Landau's formula (under RH, as $N\to\infty$) $\sum_{0<\gamma\le T}e^{i\gamma y}$ is large exactly for $y=\log p^m$ (value about $-\frac{T}{2\pi}\Lambda(p^m)p^{-m/2}$-type), and the zero-spacing perturbation expansion (2.30). This shows the long-range correlations are an arithmetic (prime) effect not captured by GUE.
- **THM-PAPER-0023-6** (Sec. 3 accuracy claim, rigorous error analysis (computer-assisted, under machine-model assumptions), scope: computational; Sec. 3, pp. 296-305). Zeros $\gamma_n$, $10^{12}<n\le10^{12}+101000$ were computed to within $\pm 10^{-8}$ via Riemann-Siegel with $m=206393$ terms, using Brown's floating-point model (b=2,t=47 sp, t=94 dp on Cray), with termwise error bound (3.9) $\le 2.14\cdot10^{-12}n^{-1/2}$ and total cosine-sum error bound (about $1.95\cdot10^{-9}$) plus RS remainder control; all those zeros verified to satisfy RH.
- **THM-PAPER-0023-7** (Sec. 2 discussion (2.25)-(2.27), remark on conflicting conjectures, scope: asymptotic; pp. 290-291). GUE predicts $\max_{\gamma_n\le T}(\gamma_{n+1}-\gamma_n)\sim 8^{-1/2}\pi\cdot$ (via $\log p(0,t)\sim -\pi^2t^2/8$) of order $(\log T)^{-1}\cdot(\log T)^{1/2}$-scale i.e. $\gg (\log T)^{-1/2}(\log\log T)^{-1/2}$ in normalized units, contradicting Montgomery's S(t)-based conjecture (2.27); data cannot decide.

### Key definitions

- Normalized spacing $\delta_n=(\gamma_{n+1}-\gamma_n)\log(\gamma_n/2\pi)/2\pi$
- GUE hypothesis: asymptotic distribution of $\delta_n$ equals GUE nearest neighbor law $p(0,u)$
- $p(k,u)$: GUE density of normalized $(k+1)$-th neighbor spacing
- Autocovariance $c_k(N,M)$ of $\delta_n$

### Principal lemmas

- **THM-PAPER-0023-L1** (Eq. (1.2) (Montgomery); Sec. 1, p. 274). Under RH, $F(\alpha,T)=(1+o(1))T^{-2\alpha}\log T+\alpha+o(1)$ uniformly for $0\le\alpha\le1$ where $F(\alpha,T)=2\pi(T\log T)^{-1}\sum_{0<\gamma,\gamma'\le T}T^{i\alpha(\gamma-\gamma')}/(1+(\gamma-\gamma')^2)$. — *Role:* Imported theorem motivating pair-correlation conjecture (1.3)-(1.4)
- **THM-PAPER-0023-L2** (Eq. (2.16) (Selberg); p. 279). $\int_0^T S(t)^{2k}dt\sim\frac{(2k)!}{k!(2\pi)^{2k}}T(\log\log T)^k$. — *Role:* Imported; explains why spacing statistics converge slowly (S(t) tiny).
- **THM-PAPER-0023-L3** (Eqs (6.4)-(6.5) (Mehta-des Cloizeaux); Sec. 6, p. 305). GUE k-th neighbor spacing density $p(k,t)$ is given by a determinant/prolate-eigenvalue expansion over eigenvalues $\lambda_j$ of the finite Fourier operator (6.2). — *Role:* Imported formulas used to compute GUE predictions (more accurate than the derivative formula (6.6)).
- **THM-PAPER-0023-L4** (Eq. (2.23)-(2.25) (Mehta-des Cloizeaux, Dyson); pp. 289-290). $p(0,t)=\frac{\pi^2}{3}t^2-\frac{2\pi^4}{45}t^4+\dots$ near $0$ (normalized), and $\log p(0,t)\sim-\pi^2t^2/8$ as $t\to\infty$. — *Role:* Imported; yields GUE probability for minimal spacing among M zeros (2.24) used in Table 5.
- **THM-PAPER-0023-L5** (Landau-type formula before (2.30); pp. 294-295). Under RH, for fixed $y>0$, $\sum_{0<\gamma\le T}e^{i\gamma y}$ is $-\frac{T}{2\pi}e^{-y/2}\Lambda$-weighted at $y=\log p^m$ (i.e. $\approx -\frac{T}{2\pi}e^{-y/2}\log p$) and $O(e^{-y/2}\log T)$ otherwise. — *Role:* Imported; basis for prime explanation of spectral peaks.

### Proof architecture

No theorems proved by the paper's own argument; it is a computational statistical study. Pipeline: (i) compute zeros via Riemann-Siegel with careful mixed single/double precision scheme and Brown-model error analysis (Sec. 3); (ii) form normalized spacings; (iii) compare to GUE densities computed via prolate-spheroidal eigenfunction methods (Sec. 6); (iv) tests: histograms, moments, q-q plots, Kolmogorov statistic with asymptotic law (2.21)-(2.22), extremal-value probabilities; (v) interpret long-range correlations through explicit formulas (Landau/Guinand-Weil) and Fourier spectrum of spacing sequence.

Dependency edges: CAND-00724 → Montgomery 1973 pair correlation (tests); CAND-00724 → CAND-00759 (announces/anticipates (Odlyzko-Schonhage algorithm cited as [61], not yet implemented))

**Imported results.** Montgomery 1973 pair correlation theorem (under RH), eq. (1.2); Selberg moments of S(t), eq. (2.16); Mehta-des Cloizeaux GUE spacing formulas (6.4)-(6.5); Landau 1911 formula on sums over zeros; Montgomery 1977 Omega-result for S(t) under RH, eq. (2.14)

**Techniques.** Riemann-Siegel formula with rigorous floating-point error analysis (Brown's model, Schryer tests); Turing's method for zero counting/verification; GUE spacing densities via prolate spheroidal functions (Mehta-des Cloizeaux); Kolmogorov statistic, q-q plots; Fourier spectrum of spacing sequence; explicit formulas (Landau, Guinand, Weil)

## Context and interpretation

**Importance and obstacle overcome.** First large-sample high-accuracy study of zeros at height ~10^11-10^12 that confirmed GUE statistics, founding the empirical random-matrix picture of zeta zeros. Obstacle: producing 10^5 zeros at height 2.7e11 with certified accuracy on 1980s hardware, and separating genuine arithmetic effects from slow convergence.

**Relation to prior work.** Tests Montgomery 1973 conjecture; extends Brent 1979 and van de Lune-te Riele-Winter 1986 verification work; uses Odlyzko-Schonhage algorithm [61] only as an announced future method (not yet implemented). Subsequent: Odlyzko 1989/1992 higher-height data (10^20-10^22), Bogomolny-Keating, Bogomolny et al. 2006 explaining the small-spacing excess by log-corrections.

**Limitations and open questions.** Statistical evidence only at heights up to ~2.7e11; explicitly leaves open whether the excess of small spacings persists (answered later by higher-height data and log-correction theory). GUE spacing values (p(k,u)) lack a rigorous error analysis; Dyson's c_k conjecture unproved; sp cosine accuracy assumed. Nothing here bears on RH itself beyond verifying the computed zeros are on the line.

## Research potential

- **Hypotheses that might be weakened.** The accuracy claim depends on assumed Cray cosine/log routine error bounds (Sec. 3, around (3.8)); redoing it with interval arithmetic would remove that assumption.
- **Generalizations.** Repeat spacing/autocovariance/Fourier-spectrum study for L-functions and for higher heights with Odlyzko-Schonhage; test Bogomolny-Keating log-corrected effective N prediction against Tables 4-5 data.
- **Candidate connections.** Prime peaks in the spectrum of spacings (Figs 13-15) are an empirical version of the Bogomolny-Keating periodic-orbit corrections and of the Landau explicit-formula sum; connects to CAND-00807 (Berry-Keating) and to exponential-sum/Landau lemma use in pair correlation.
- **Reusable lemmas.** Landau-type sum over zeros (p. 294-295) and the perturbation expansion (2.30) are reusable for quantitative prediction of spacing-spectrum peak heights.
- **Possible experiments.** Recompute Table 6 autocovariances and the Fig. 13 spectral peaks with modern zero tables (e.g. 10^13 zeros) and compare peak heights to $\Lambda(q)/\sqrt q$ predictions; reproduce Table 5 minimal-spacing probabilities with effective-N correction.
- **Risks / barriers.** Finite statistical data cannot bear on RH or global statements; slow $\log\log$ convergence makes extrapolation unreliable.

## Audit notes (Level 1 reader)

Triage summary says 'near height 10^20' with 'corrections'; the paper actually uses zeros 10^12+1..10^12+10^5 (height ~2.7e11), mismatch with triage text. Text is from an OCR of a scan; some symbols in Table 1/5 are garbled in the OCR (not in the paper). Landau-type formula and (2.25)/(2.26) displays were garbled by OCR so my LaTeX for them is reconstructed; verify against the printed page. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00724`; harvest queries: kw_RH_any, kw_moments_zeta, kw_pair_correlation, msc_11M06.
- Triage decision: include — Landmark numerical evidence for GUE spacing at large height.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

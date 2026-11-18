# PAPER-0092 — Maximum of the Riemann zeta function on a short interval of the critical line

| Field | Value |
|---|---|
| Authors | Arguin, Louis-Pierre; Belius, David; Bourgade, Paul; Radziwiłł, Maksym; Soundararajan, Kannan |
| Year / stratum | 2019 / S6 |
| Venue | Commun. Pure Appl. Math. 72, No. 3, 500-535 (2019). |
| Identifiers | zbMATH [1443.11161](https://zbmath.org/?q=an:1443.11161) · DOI [10.1002/cpa.21791](https://doi.org/10.1002/cpa.21791) · arXiv [1612.08575](https://arxiv.org/abs/1612.08575) |
| MSC | 11M06 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/1612.08575 |
| Selection | score 4.3237, in-pool citations 30, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Prove the leading order of the Fyodorov-Hiary-Keating conjecture: for t uniform in [T,2T], the maximum of log|zeta(1/2+iu)| over |t-u|<=1 is (1+o(1)) log log T with probability 1-o(1). Correction to triage: the theorem is unconditional (no RH); the triage note 'conditional on RH-free methods' is not accurate -- the conditional-on-RH result for Im log zeta is Najnudel's.

**Historical motivation.** Fyodorov-Hiary-Keating (replica method/numerics) conjecture (3) max_{|t-u|<=1}log|zeta| = log log T - (3/4)log_3T + X_T; Farmer-Gonek-Hughes vs Littlewood dispute on maximal order; analogy with CUE characteristic polynomials and log-correlated fields.

### Main results

- **THM-PAPER-0092-1** (Theorem 1.1, theorem, scope: asymptotic; Sec. 1.1). For any $\epsilon>0$, as $T\to\infty$: $\frac1T\,\mathrm{meas}\{T\le t\le2T:(1-\epsilon)\log\log T<\max_{|t-u|\le1}\log|\zeta(\tfrac12+iu)|<(1+\epsilon)\log\log T\}\to1$.
- **THM-PAPER-0092-2** (Proposition 2.1, proposition, scope: asymptotic; Sec. 2). For any $V=V(T)\to\infty$, $\mathbb P\big(\max_{|t-u|\le1}|\zeta(1/2+iu)|>V\log T\big)=O(1/V^2)=o(1)$ for t uniform in [T,2T]; hence $\mathbb P(\max\log|\zeta|<\log(V\log T))\to1$.
- **THM-PAPER-0092-3** (Proposition 3.1, proposition, scope: asymptotic; Sec. 3 (9)-(12)). For $\epsilon>0$ and $K=K(\epsilon)$ large, with t uniform in [T,2T]: $\mathbb P\big(\max_{|t-u|\le1}\log|\zeta(\tfrac12+iu)|>(1-2\epsilon)\log\log T\big)\ge\mathbb P\big(\max_{|t-u|\le1/4}\sum_{j=1}^{K-3}P_j(u)>(1-\epsilon)\log\log T\big)+o(1)$, where $P_j(u)=\Re\sum_{p\in J_j}p^{-\sigma_0-iu}$, $J_0=[2,e^{(\log T)^{1/K}}]$, $J_j=(e^{(\log T)^{j/K}},e^{(\log T)^{(j+1)/K}}]$, $\sigma_0=\frac12+\frac{(\log T)^{3/(2K)}}{\log T}$, $X=\exp((\log T)^{1-1/K})$.
- **THM-PAPER-0092-4** (Proposition 3.2, proposition, scope: asymptotic; Sec. 3; proved Sec. 5). For $K>3$ and $0<\lambda<1$: $\mathbb P\big(\max_{|t-u|\le1/4}\min_{1\le j\le K-3}P_j(u)>\frac\lambda K\log\log T\big)=1+o(1)$.

### Key definitions

- $\sigma_0=\frac12+\frac{(\log T)^{3/(2K)}}{\log T}$
- $X=\exp((\log T)^{1-1/K})$, prime ranges $J_j$, $P_j(u)=\Re\sum_{p\in J_j}p^{-\sigma_0-iu}$
- FHK conjecture: $\max_{|t-u|\le1}\log|\zeta(1/2+iu)|=\log\log T-\frac34\log_3T+X_T$
- Event $\mathcal T(k/\log T)=\{P_j(t+k/\log T)>\frac{1-\epsilon}K\log\log T\ \forall1\le j\le K-3\}$

### Principal lemmas

- **THM-PAPER-0092-L1** (Lemma 4.1; Sec. 4.1). For $\frac12\le\sigma\le\frac12+(\log T)^{-1/2-\epsilon}$ and $V\ge2$: $\mathbb P(\max_{|t-u|\le1}|\zeta(\tfrac12+iu)|>V)\ge\mathbb P(\max_{|t-u|\le1/4}|\zeta(\sigma+iu)|>2V)+o(1)$. — *Role:* Large values just right of the critical line propagate to the line (uses zeta=sum_{n<=T}n^{-s}+O(T^{-1/2}) and a Fourier/Poisson-kernel representation of n^{-(sigma-1/2)}).
- **THM-PAPER-0092-L2** (Lemma 4.2/4.3; Sec. 4.1-4.2). There is a Dirichlet polynomial mollifier M such that for most t, $\zeta(\sigma_0+it)M(\sigma_0+it)\approx1$; Lemma 4.3: $\mathbb P(\max_{|t-u|\le1}|M\zeta(\sigma_0+iu)-1|>\epsilon)=o(1)$ (via a Sobolev-type inequality (6) and Lemma 4.2). — *Role:* Mollification at sigma_0 > 1/2 (impossible on sigma=1/2) turning zeta into exp(-sum over primes).
- **THM-PAPER-0092-L3** (Lemma 4.4/4.5; Sec. 4.3). The chosen mollifier satisfies $M(\sigma_0+iu)\approx\prod_{p\le X}(1-p^{-\sigma_0-iu})$ for all $|u-t|\le1$ for most t, with X=exp((log T)^{1-1/K}). — *Role:* Reduces log|zeta| max to max of Re sum_{p<=X} p^{-sigma_0-iu}, completing Prop 3.1.
- **THM-PAPER-0092-L4** (Sobolev inequality (6); Sec. 2). $\max_{u\in[-1,1]}|f(u)|^2\le\frac{|f(1)|^2+|f(-1)|^2}2+\int_{-1}^1|f'(v)f(v)|dv$ for $f\in C^1$. — *Role:* Used for the short proof of the upper bound (with second moments of zeta and zeta') and in Lemma 4.3.
- **THM-PAPER-0092-L5** (Lemma 3.4; Sec. 3). Gaussian approximation (CLT-type moment estimate) for Dirichlet polynomials over primes with mean 0 and variance ~(1/2)sum 1/p^{2 sigma_0}. — *Role:* Gaussian behaviour/independence of P_j used in Sec. 5.
- **THM-PAPER-0092-L6** (Propositions 5.1, 5.3; Sec. 5). Joint large-deviation/Gaussian comparison for (P_j(t+tau))_{1<=j<=K-3} (and pairs at two shifts) in the range of values up to log log T. — *Role:* Input to the second-moment (Cauchy-Schwarz) argument on events T(k/log T).
- **THM-PAPER-0092-L7** (Proposition 5.4; Sec. 5, p.5 and Prop 5.4). Covariance structure of $P_m(t+\tau)$, $|\tau|\le1$: $\mathrm{cov}\sim\frac1{2K}\log\log T$ if $-\log|\tau-\tau'|\ge\frac{m+1}K\log\log T$ and $o(\log\log T)$ if $\le\frac mK\log\log T$ (eq. (5)). — *Role:* Log-correlated structure of the field (branching-random-walk structure).
- **THM-PAPER-0092-L8** (Proposition 5.5; Sec. 5). For all $0<x_j\le\log\log T$: $\mathbb P(\mathcal T(k/\log T)\cap\mathcal T(\ell/\log T))\sim\mathbb P(\mathcal T(k/\log T))\mathbb P(\mathcal T(\ell/\log T))$ when $|k-\ell|>(\log T)^{1-1/(2K)}$ (decorrelation of well-separated points), with comparable bounds otherwise. — *Role:* Second moment (Paley-Zygmund/Cauchy-Schwarz) input for existence of a point in the interval where all P_j are large.

### Proof architecture

Upper bound: Sobolev inequality + second moments of zeta and zeta' (Prop 2.1) give max<= log(V log T). Lower bound: (Prop 3.1, Sec. 4) transfer max of log|zeta| on [t-1,t+1] to max of Re sum_{p<=X} p^{-sigma_0-iu} on |t-u|<=1/4 by three steps -- shift to sigma_0 (Lemma 4.1), mollifier M with M zeta ~ 1 on the whole interval (Lemmas 4.2, 4.3), and M ~ Euler product truncated at X (Lemma 4.4/4.5). (Prop 3.2, Sec. 5) show via branching-random-walk techniques of Arguin-Belius-Harper that a.e. t admits u with all block sums P_j(u)>=(lambda/K) log log T, j=1..K-3, using the second moment bound over the log T discrete points t+k/log T, with Gaussian-moment comparison (large deviation regime) of joint laws and the covariance structure (5). Combining with K large and lambda->1 yields Theorem 1.1.

**Imported results.** Selberg's central limit theorem for log|zeta| (variance (1/2) log log T); zeta(sigma+it)=sum_{n<=T} n^{-sigma-it}+O(T^{-1/2}) (Titchmarsh Thm 4.11); Prime number theorem with error (Montgomery-Vaughan Thm 6.9); Mean value theorems for Dirichlet polynomials (Montgomery-Vaughan) and second moments of zeta,zeta'; Methods of Arguin-Belius-Harper on branching random walk maxima

**Techniques.** branching random walk / multiscale decomposition of Dirichlet polynomial over prime blocks; Sobolev inequality on short intervals; second moment (Cauchy-Schwarz) method for existence of exceptional point; mollification at sigma slightly right of 1/2; Gaussian comparison/large deviations for Dirichlet polynomials on primes; Selberg's central limit theorem method (Radziwill-Soundararajan [35])

## Context and interpretation

**Importance and obstacle overcome.** First rigorous theorem about maxima of zeta itself in the log-correlated-field framework (randomness only from the interval); proves FHK leading order, giving evidence that log|zeta| behaves as a log-correlated field with covariance (1/2)log min(1/h, log T). Obstacle: no mollifier exists on sigma=1/2 (zeros); circumvented by working at sigma_0 slightly to the right and showing propagation to the line.

**Relation to prior work.** Builds on Arguin-Belius-Harper (max of CUE and zeta model), Radziwill-Soundararajan's proof of Selberg's CLT (mollifier construction); parallel conditional work of Najnudel (RH); complements Bondarenko-Seip and Soundararajan resonator results on global maxima.

**Limitations and open questions.** Only the leading order (1+o(1))log log T of FHK's conjecture (3): max = log log T - (3/4) log_3 T + X_T; second-order term and the limiting law X_T are open (Arguin-Ouimet for a model, Paquette-Zeitouni for CUE). Im log zeta unconditionally open (Najnudel proved under RH). Result concerns random intervals of length 2, not the global maximum on [0,T] (still dispute Farmer-Gonek-Hughes vs Littlewood). The authors note scope to refine by letting K->infinity.

**Ideas in remarks/appendices/abandoned paths.** Remark 1.3: the covariance of log|zeta(1/2+it)| and log|zeta(1/2+i(t+h))| is (1/2)log min(1/h, log T), the same as log|P_N(z)| for CUE; sharp threshold -log|tau-tau'| vs (j/K) log log T gives a discrete multiscale tree structure. Remark at end of 1.3: parameter K may tend to infinity to improve the result. Remark in 1.1: independent proof by Najnudel under RH for max of Im log zeta.

## Research potential

- **Hypotheses that might be weakened.** The restriction to random intervals of length 1 and K fixed: letting K->infinity with T or intervals of growing length (|t-u|<=(log T)^a) would probe the second-order term -(3/4) log_3 T; the unconditional treatment of Im log zeta is flagged by authors as open.
- **Generalizations.** Same structure should give leading-order maxima for L(1/2+it,chi) and for L-functions in families where mollification at sigma_0 plus Selberg-type CLT is known (Dirichlet characters, GL(2)); also max of log zeta over intervals of length (log T)^{-a} interpolating to typical values.
- **Candidate connections.** Compare/complement Bondarenko-Seip (CAND-01786): resonance gives global exp(sqrt(log T log_3 T/log_2 T)) while this gives typical-interval log log T; both inform FHK vs Farmer-Gonek-Hughes. Links to Gaussian multiplicative chaos for zeta (Saksman-Webb) and random matrix characteristic polynomial maxima (Arguin-Belius-Bourgade); and to Polymath15 (CAND-01890) via size of |H_t/B_t|.
- **Reusable lemmas.** Lemma 4.1-4.3 (mollification at sigma_0 propagating to the critical line over a unit interval) and Prop 5.5 (decorrelation of well-separated points) are reusable for other statistics on short intervals; Sobolev inequality (6).
- **Possible experiments.** Numerically sample t in [T,2T] and compute max over |t-u|<=1 of log|zeta| for T up to 10^{20}-10^{30} (zeta evaluation by Riemann-Siegel) and compare with log log T - (3/4) log_3 T to test FHK second order and the proposed K-block decomposition (compute P_j variances empirically); test the covariance claim (5).
- **Risks / barriers.** Second-order asymptotics need tightness/precise barrier estimates for Dirichlet polynomials at scale (log T)^{1/K}->1; also controlling mollifier error uniformly (Lemma 4.3) becomes harder as K grows.

## Audit notes (Level 1 reader)

Triage description ('conditional on RH-free methods as stated') is inaccurate: Theorem 1.1 is unconditional. Introduction mentions Bondarenko-Seip with c<1/sqrt2 (older [7]); the improved c<1 version is CAND-01786 (later). Lemma/Prop numbering: Proposition 3.2 label appears twice in the extracted text (line near 417 and 488) -- extraction artifact. Details of Sec. 5 not verified line by line. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01957`; harvest queries: msc_11M06, arxiv_critical_line.
- Triage decision: include — Proves leading order of Fyodorov-Hiary-Keating maximum conjecture.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

# PAPER-0027 — A hybrid Euler-Hadamard product for the Riemann zeta function

| Field | Value |
|---|---|
| Authors | Gonek, S. M.; Hughes, C. P.; Keating, Jonathan P. |
| Year / stratum | 2007 / S5 |
| Venue | Duke Math. J. 136, No. 3, 507-549 (2007). |
| Identifiers | zbMATH [1171.11049](https://zbmath.org/?q=an:1171.11049) · DOI [10.1215/S0012-7094-07-13634-2](https://doi.org/10.1215/S0012-7094-07-13634-2) · arXiv [math/0511182](https://arxiv.org/abs/math/0511182) |
| MSC | 11M26, 11M06, 11M50 |
| Families | B, F |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/math/0511182 |
| Selection | score 4.5988, in-pool citations 47, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Construct a model of $\zeta(1/2+it)$ that contains both primes and zeros: a partial Euler product $P_X(s)$ times a partial Hadamard product $Z_X(s)$ over zeros, with $X$ a parameter mediating between them; model $Z_X$ by characteristic polynomials of random unitary matrices, and use it to heuristically derive the Keating-Snaith moment conjecture $I_k(T)\sim a(k)\frac{G^2(k+1)}{G(2k+1)}(\log T)^{k^2}$, separating the arithmetic factor $a(k)$ from the RMT factor.

**Historical motivation.** Keating-Snaith RMT model for moments contained no primes (arithmetic factor $a(k)$ inserted ad hoc); the Conrey-Gonek/Conrey-Ghosh conjectures determined $g(k)$ only for $k\le4$. A model with primes and zeros was sought to explain how arithmetic and RMT factors combine.

### Main results

- **THM-PAPER-0027-1** (Theorem 1, theorem (unconditional), scope: global; Sec 1, eq (5)-(7), p.3). Let $s=\sigma+it$, $\sigma\ge0$, $|t|\ge2$, $X\ge2$, $K\in\mathbb N$ fixed. Let $u\ge0$ be $C^\infty$ of mass 1 supported on $[e^{1-1/X},e]$, $U(z)=\int_0^\infty u(x)E_1(z\log x)dx$ with $E_1(z)=\int_z^\infty e^{-w}/w\,dw$. Then $\zeta(s)=P_X(s)Z_X(s)\big(1+O\big(\frac{X^{K+2}}{(|s|\log X)^K}\big)+O(X\log^{X}\cdot X^{-\sigma})\big)$ (printed as $O(X\log X)^{-\sigma}$ in the extracted text), where $P_X(s)=\exp\big(\sum_{n\le X}\Lambda(n)/(n^s\log n)\big)$ and $Z_X(s)=\exp\big(-\sum_{\rho_n}U((s-\rho_n)\log X)\big)$; implied constants depend on $u,K$ only. The second error can be removed by using $\tilde P_X$ with $v(e^{\log n/\log X})$, $v(t)=\int_t^\infty u$.
- **THM-PAPER-0027-2** (Conjecture 1 (Keating-Snaith), conjecture (imported), scope: asymptotic; Sec 1, p.2). For fixed $\Re k>-1/2$: $\frac1T\int_T^{2T}|\zeta(1/2+it)|^{2k}dt\sim a(k)\frac{G^2(k+1)}{G(2k+1)}(\log T)^{k^2}$, $a(k)=\prod_p(1-1/p)^{k^2}\sum_{m\ge0}\big(\frac{\Gamma(m+k)}{m!\Gamma(k)}\big)^2p^{-m}$. *Conditional on:* conjecture, unproved for $k>2$.
- **THM-PAPER-0027-3** (Conjecture 2 (Splitting Conjecture), conjecture, scope: asymptotic; Sec 1, p.4). For $X,T\to\infty$ with $X=O((\log T)^{2-\epsilon})$ and $k>-1/2$: $\frac1T\int_T^{2T}|\zeta(\tfrac12+it)|^{2k}dt\sim\frac1T\int_T^{2T}|P_X(\tfrac12+it)|^{2k}dt\times\frac1T\int_T^{2T}|Z_X(\tfrac12+it)|^{2k}dt$. *Conditional on:* unproved; true for k=1,2 by Corollary.
- **THM-PAPER-0027-4** (Theorem 2, theorem (unconditional), scope: asymptotic; Sec 1 / Sec 3, p.4). Let $1/2\le c<1$, $\epsilon>0$, $k\in\mathbb R$, $X,T\to\infty$ with $X=O((\log T)^{1/(1-c+\epsilon)})$. Then uniformly for $c\le\sigma\le1$: $\frac1T\int_T^{2T}|P_X(\sigma+it)|^{2k}dt=a(k,\sigma)F_X(k,\sigma)(1+O_k(1/\log X))$, where $a(k,\sigma)=\prod_p(1-p^{-2\sigma})^{k^2}\sum_{m\ge0}d_k(p^m)^2p^{-2m\sigma}$ and $F_X=\zeta(2\sigma)^{k^2}e^{-k^2E_1((2\sigma-1)\log X)}$ for $\sigma>1/2$, $F_X=(e^\gamma\log X)^{k^2}$ for $\sigma=1/2$ (as printed; $c=1/2$ allowed).
- **THM-PAPER-0027-5** (Conjecture 3, conjecture, scope: asymptotic; Sec 1 / Sec 4, p.4). For $X,T\to\infty$, $X=O((\log T)^{2-\epsilon})$, $k>-1/2$: $\frac1T\int_T^{2T}|Z_X(\tfrac12+it)|^{2k}dt\sim\frac{G^2(k+1)}{G(2k+1)}\Big(\frac{\log T}{e^\gamma\log X}\Big)^{k^2}$. Derived by replacing zeros with eigenangles of Haar $U(N)$, $N=\lfloor\log T\rfloor$. *Conditional on:* GUE/Haar model for zeros; Theorem 4.
- **THM-PAPER-0027-6** (Theorem 3 and Corollary, theorem (conditional on nothing stated; uses Hughes/Ingham-type mean values), scope: asymptotic; Sec 1, p.5; proof in Sec 5). For $\epsilon>0$, $X,T\to\infty$, $X=O((\log T)^{2-\epsilon})$, and $k=1,2$: $\frac1T\int_T^{2T}|\zeta(\tfrac12+it)P_X(\tfrac12+it)^{-1}|^{2k}dt\sim\frac{G^2(k+1)}{G(2k+1)}\big(\frac{\log T}{e^\gamma\log X}\big)^{k^2}$. Corollary: Conjectures 2 and 3 hold for $k=1,2$.
- **THM-PAPER-0027-7** (Theorem 4, theorem (random matrix, rigorous), scope: asymptotic; Sec 4, p.~20). For $\phi(\theta)$ as in (20) (the RMT analogue of $\exp(-\sum_n U(\cdot))$) and fixed $k>-1/2$, $X\ge2$: $\mathbb E_N\Big[\prod_{n=1}^N\phi(\theta_n)\Big]\sim\frac{G(k+1)^2}{G(2k+1)}\Big(\frac N{e^\gamma\log X}\Big)^{k^2}\big(1+O_k(1/\log X)\big)$ as $N\to\infty$.

### Key definitions

- $P_X(s)=\exp\sum_{n\le X}\Lambda(n)/(n^s\log n)$
- $Z_X(s)=\exp(-\sum_{\rho_n}U((s-\rho_n)\log X))$
- $U(z)=\int_0^\infty u(x)E_1(z\log x)dx$
- Splitting Conjecture

### Principal lemmas

- **THM-PAPER-0027-L1** (Lemma 2 (Bombieri-Hejhal); Sec 2, p.5). With $P_X^*(s)=\prod_{p\le X}(1-p^{-s})^{-1}\prod_{\sqrt X<p\le X}(1+\tfrac1{2p^{s}})^{-1}$... smoothed explicit formula yielding $P_X$-type approximations (printed as $P^*_X$). — *Role:* Imported smoothed explicit formula used to pass from zeros to primes.
- **THM-PAPER-0027-L2** (Lemma 3; Sec 3, p.~10). For real $k$, $1/2\le c<1$, $2\le X\ll(\log T)^{1/(1-c+\epsilon)}$: $\frac1T\int_T^{2T}|P_X^*(\sigma+it)|^{2k}dt=a(k,\sigma)\prod_{p\le X}(1-p^{-2\sigma})^{k^2}\ldots(1+O_k(X^{1/2-2\sigma}/\log X))$ uniformly in $c\le\sigma\le1$. — *Role:* Mean-value of Euler-product part; feeds Theorem 2.
- **THM-PAPER-0027-L3** (Lemma 1; Sec 2, p.~6). Properties of $u$ and $U(z)=\int u(x)E_1(z\log x)dx$ (e.g., $U(z)\approx-\gamma-\log z+O(|z|)$ for small $z$ and decay for large $z$). — *Role:* Controls how many zeros effectively contribute: $\exp(-U(i(t-\gamma_n)\log X))\approx i(t-\gamma_n)e^\gamma\log X$.
- **THM-PAPER-0027-L4** (Lemmas 7-8; Sec 5, p.~35-40). Arithmetic lemmas on sums over coprime $a,b$ and $\kappa(n)=\prod_{p|n}(1+1/p)$ used in the proof of Theorem 3 for k=1,2. — *Role:* Evaluation of mean values of $|\zeta P_X^{-1}|^{2k}$.

### Proof architecture

Sec 2: smoothed explicit formula (Bombieri-Hejhal) with weight $u$ gives Theorem 1, an unconditional hybrid factorization $\zeta=P_XZ_X(1+\text{err})$ with error small only in the intermediate regime ($X$ not too small vs $|s|$). Sec 3 proves Theorem 2 (moments of the Euler product part) rigorously. Sec 4 computes the Haar-average moment of the RMT analogue of $Z_X$ (Theorem 4) via Barnes G / Selberg-type integral. Heuristic bridge: Splitting Conjecture + Conjecture 3 give Keating-Snaith (all X-dependence cancels). Sec 5 proves Theorem 3 for k=1,2, hence verifies Splitting for these k.

**Imported results.** Bombieri-Hejhal smoothed explicit formula; Hardy-Littlewood and Ingham second and fourth moments; Keating-Snaith 2000 conjecture [13]; Conrey-Ghosh and Conrey-Gonek values g(3)=42, g(4)=24024; Montgomery-Odlyzko GUE hypothesis for zeros

**Techniques.** Smoothed Bombieri-Hejhal explicit formula; Exponential integral weight U; Moments of Dirichlet polynomials / Euler products; Haar averages over U(N) via Barnes G-function (Keating-Snaith); Splitting (independence) heuristic for Euler vs zero parts

## Context and interpretation

**Importance and obstacle overcome.** Provides an unconditional (no RH) exact-formula-derived hybrid representation of $\zeta$ and a principled heuristic for factorization of moments into an arithmetic factor times a RMT factor, with an intermediate parameter $X$ that cancels in the final answer. Obstacle: error terms in the hybrid formula limit $X$; the independence of the Euler and Hadamard parts is only conjectural (proved for k=1,2).

**Relation to prior work.** Builds on Keating-Snaith (RMT only), Conrey-Ghosh/Conrey-Gonek (number theoretic g(k)), Bombieri-Hejhal. Precursor to Conrey-Farmer-Keating-Rubinstein-Snaith recipe and ratios; later literature (Bui-Keating, Gonek-Hughes-Keating hybrid for other L-functions, Heap, Arguin et al. on moments and Euler-Hadamard) develops the model.

**Limitations and open questions.** Splitting conjecture unproven for $k\ge3$ and conjectured only for $X=O((\log T)^{2-\epsilon})$ (authors expect larger range); lower-order terms in the moments not captured (authors ask whether the model extends to them); Theorem 4's RMT model uses $N=\log T$ without lower-order corrections.

**Ideas in remarks/appendices/abandoned paths.** Closing remark that the model should reproduce Gonek's and Hughes-Keating-O'Connell results for moments of $\zeta'$ at zeros, and may capture lower-order terms (p.5); the observation that $N=\log T/(e^\gamma\log X)$ matches effective degree of the zero polynomial (p.4).

## Research potential

- **Hypotheses that might be weakened.** Range $X=O((\log T)^{2-\epsilon})$ in Conj. 2, 3 and Thm 3; and smoothness of $u$ support $[e^{1-1/X},e]$ in Theorem 1 (can be relaxed to $[1,e]$ per remark).
- **Generalizations.** Other L-functions ([14] cited); with RH, $P_X$ and $Z_X$ at $\sigma=1/2$ for negative moments $k>-1/2$; using Theorem 1 to bound $\max|\zeta|$ or low-lying zeros; extension to distribution of $\log|\zeta|$ (Gaussian CLT with variance $\tfrac12\log\log T$ splitting between $P_X$ and $Z_X$).
- **Candidate connections.** Splitting conjecture is a precise statement about decorrelation of primes up to $X$ from zeros within $1/\log X$; link with Arguin-Belius-Bourgade-Radziwill-Soundararajan max of zeta on short intervals and with Selberg CLT. Also with ratios-conjecture lower order terms (CAND-01202).
- **Reusable lemmas.** Theorem 1 (unconditional hybrid factorization) and Theorem 2 (moments of $P_X$ for real $k$ and $\sigma\ge1/2$).
- **Possible experiments.** Numerically test the Splitting Conjecture at $k=3$ using Odlyzko zeros near $10^{22}$ by computing $P_X$ and $Z_X$ separately for $X\sim(\log T)^{1.5}$, compare joint vs product of moments; check Theorem 1's error numerically as function of $X$.
- **Risks / barriers.** Splitting heuristic may fail beyond $(\log T)^{2}$ or at higher $k$ for reasons related to lower-order terms; the hybrid formula by itself yields no information about zeros off the line.

## Audit notes (Level 1 reader)

Extraction garbles the second error term in Theorem 1 (printed as 'O(X log X)^{-sigma}'); actual form should be checked against published Duke version. Lemma 2 in v1 is attributed to Bombieri-Hejhal but numbering of lemmas (Lemma 1 appears at line ~276 after Theorem 3). Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01207`; harvest queries: kw_weil_positivity, msc_11M06, msc_11M26, msc_11M50, arxiv_critical_line, arxiv_explicit_formula, arxiv_random_matrix_zeta.
- Triage decision: include — Hybrid model combining primes and RMT zeros, influential heuristic.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

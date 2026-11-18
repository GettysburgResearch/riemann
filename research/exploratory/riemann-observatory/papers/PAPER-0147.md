# PAPER-0147 — On the order of magnitude of the difference between consecutive prime numbers.

| Field | Value |
|---|---|
| Authors | Cramér, H. |
| Year / stratum | 1936 / S2 |
| Venue | Acta arith., Warszawa, 2, 23-46 (1936); Prace mat.-fiz. 45, 51-74 (1937). |
| Identifiers | zbMATH [62.1147.01](https://zbmath.org/?q=an:62.1147.01) · DOI [10.4064/aa-2-1-23-46](https://doi.org/10.4064/aa-2-1-23-46) |
| MSC |  |
| Families | A, F |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://matwbn.icm.edu.pl/ksiazki/aa/aa2/aa212.pdf |
| Selection | score 2.3429, in-pool citations 32, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** How large can the gap p_{n+1}-p_n be? A probabilistic model suggests p_{n+1}-p_n=O((log p_n)^2). The paper (i) gives a heuristic derivation of limsup (p_{n+1}-p_n)/(log p_n)^2 = 1 and (ii) proves, assuming RH, a frequency bound for exceptionally large gaps: Theorem II and Theorem III on sums over gaps.

**Historical motivation.** Hoheisel (1930) gave p_{n+1}-p_n=O(p^{1-delta}); Cramér (1919) gave O(sqrt p log p) under RH; Westzynthius (1931) showed gaps larger than log p are unbounded relative to log p; Piltz conjectured O(p^eps). Cramér proposes (log p)^2 and shows what RH can say about exceptional large gaps.

### Main results

- **THM-PAPER-0147-1** (Heuristic Theorem, Sect. I, p. 27, theorem about a random model (almost sure), transferred to primes only as a suggestion, scope: asymptotic; Sect. I, pp. 26-28, eqs. (6),(7)). In the urn model with independent draws, with probability $1$: $\limsup_{n\to\infty}\frac{P_{n+1}-P_n}{(\log P_n)^2}=1$. The argument: events $E_m=\{$black balls from all $U_{m+\nu}$, $1\le\nu\le c(\log m)^2\}$ have probability $\varepsilon_m$ with $A m^{-c}<\varepsilon_m<B m^{-c}$; Borel-Cantelli gives finitely many for $c>1$, and infinitely many for $c<1$ by using independent blocks $m_{r+1}=m_r+[c(\log m_r)^2]+1$.
- **THM-PAPER-0147-2** (Lemma 3, lemma, unconditional, scope: asymptotic; p. 31, Lemma 3, proof pp. 31-35). There are absolute constants $\lambda>0$, $\tau_0$ such that for $\tau>\tau_0$ and $\tau\log^2\tau\,e^{-\tau}<\sigma<1/\tau^2$, with $\Delta=\frac{\lambda\sigma\tau}{\tau+\log\sigma}$: $\pi(e^{\tau+\Delta})-\pi(e^{\tau-\Delta})>\frac{\sigma e^\tau}{\tau}\bigl(1-3\,\Re F(s)\bigr)$, where $s=\sigma+i\tau$ and $F(s)=\sum_{\gamma>0}e^{-(\gamma-i\beta)s}$ is the sum over zeros $\rho=\beta+i\gamma$ in the upper half plane.
- **THM-PAPER-0147-3** (Consequence of Lemma 3, p. 35-36, corollary (new proof of Hoheisel's theorem), scope: asymptotic; pp. 35-36 and footnote 5). For some $\delta>0$ and all large $x$ there is a prime in $(x,x+cx^{1-\delta}]$, hence $p_{n+1}-p_n=O(p_n^{1-\delta})$. Needs the unproved (detailed proof not given here) estimate (26) for $\sigma=e^{-\delta\tau}$; a footnote says Tchudakoff's 1936 zero-density claim lets $\delta$ be any number $<1/4$.
- **THM-PAPER-0147-4** (Theorem I, theorem, conditional on RH, scope: asymptotic; pp. 36-37, Theorem I (first proved in Cramér 1919, [4])). If RH holds, then $p_{n+1}-p_n=O(\sqrt{p_n}\,\log p_n)$. In fact for large $x$ there is a prime in $(x,x+5\lambda\sqrt x\log x]$. Proof: under RH $|F(s)|\le e^{-\tau/2}\sum_{\gamma>0}e^{-\gamma\sigma}$, and by $N(T)=\frac{T}{2\pi}(\log\frac T{2\pi}-1)+O(\log T)$ one gets $\sum_{\gamma>0}e^{-\gamma\sigma}\sim\frac1{2\pi\sigma}\log\frac1\sigma$. Choose $\sigma=\tau e^{-\tau/2}$, so $\Re F\to 1/(4\pi)<1/3$ and Lemma 3 applies. *Conditional on:* Riemann hypothesis.
- **THM-PAPER-0147-5** (Lemma 4, lemma, conditional on RH, scope: asymptotic; p. 37-39). Assume RH. Let $\sigma(\tau)\downarrow0$ with $0<\sigma<1$. Then there is an absolute $K$ such that for all $t>m$, $\int_t^{t+1}|F(\sigma(t)+i\tau)|^2d\tau<K e^{-t}\frac{\sigma(t)}{\sigma^2(t+1)}\log^2\frac1{\sigma(t+1)}$. For $\sigma=e^{-c\tau}$ with $1/2<c<1$ this is $<Kt^2e^{-(1-c)t}$, i.e. $\Re F$ is small on average. *Conditional on:* Riemann hypothesis.
- **THM-PAPER-0147-6** (Theorem II, theorem, conditional on RH, scope: asymptotic; p. 40, Theorem II; proof pp. 41-44). Assume RH. For $h(x)=x^\alpha\log^\beta x$ let $S_{\alpha,\beta}(x)=\sum_{p_n\le x,\ p_{n+1}-p_n>h(p_n)}(p_{n+1}-p_n)$ and $N_{\alpha,\beta}(x)=\#\{p_n\le x: p_{n+1}-p_n>h(p_n)\}$. Then (39a) $S_{\alpha,\beta}(x)=O\!\bigl(\frac{x\log^3x}{h\log h}\bigr)$ for $0\le\alpha<1/2,\beta\ge0$ and for $\alpha=1/2,0\le\beta\le1$; (39b) $S_{1/2,\beta}(x)=O(1)$ for $\beta>1$; (40a) $N_{\alpha,\beta}(x)=O\!\bigl(\frac{x\log^3x}{h^2\log h}\bigr)$ for $0\le\alpha<1/2,\beta\ge0$; (40b) $N_{1/2,\beta}(x)=O(\log^{3-2\beta}x)$ for $0\le\beta\le1$; (40c) $N_{1/2,\beta}(x)=O(1)$ for $\beta>1$. In particular, with $h=\log^3x$: $\sum_{p_n\le x,\ p_{n+1}-p_n>\log^3p_n}(p_{n+1}-p_n)=O(x/\log\log x)=o(x)$. *Conditional on:* Riemann hypothesis.
- **THM-PAPER-0147-7** (Theorem III, theorem; part b) second half conditional on RH, scope: asymptotic; p. 44-45, Theorem III, (54)-(57)). a) $\sum_n\frac{p_{n+1}-p_n}{p_n\log^\lambda p_n}$ diverges for $\lambda\le1$ and converges for $\lambda>1$. b) $\sum_n\frac{(p_{n+1}-p_n)^2}{p_n\log^\lambda p_n}$ diverges for $\lambda\le2$; and, if RH holds, converges for $\lambda>4$. Proof of convergence: split by $p_{n+1}-p_n\le\log^\beta p_n$ or $>$, with $2<\beta<3$ and Theorem II estimates (55)-(57), giving $\sum_{x<p_n\le2x}(p_{n+1}-p_n)^2<Kx\log^{2\beta-1}x$, hence $\sum_{p_n\le x}(p_{n+1}-p_n)^2=O(x\log^{3+\varepsilon}x)$. *Conditional on:* Riemann hypothesis (for convergence of (54) when lambda>4).

### Key definitions

- F(s)=\sum_{\gamma>0}e^{-(\gamma-i\beta)s}=\sum_{\gamma>0}e^{i\rho' s}-type zero sum (eq. (8)), G(s) prime-power sum (9), H=2\pi F+G (10)
- S_{\alpha,\beta}(x), N_{\alpha,\beta}(x) for exceptional gaps h(x)=x^\alpha\log^\beta x (eqs. (35)-(38))

### Principal lemmas

- **THM-PAPER-0147-L1** (Lemma 1; p. 28-29). $\Re H(s)=\pi+O(1/\tau)$ uniformly in $D=\{0<\sigma\le1,\tau>1\}$, where $H(s)=2\pi F(s)+G(s)$ and $G(s)=\sum_{n\ge2}\frac{\Lambda(n)}n\bigl(\frac1{s-i\log n}+\frac1{i\log n}\bigr)$. Unconditional. — *Role:* Relates the zero sum F to the prime sum G through an explicit formula from Cramer 1919/[3] (formula (13) p. 114 there), so that the prime sum is dominated by n near e^tau.
- **THM-PAPER-0147-L2** (Lemma 2; p. 30-31). For positive $a,b$ there is $C(a,b)$ with $\sum_{x<n\le x+h}\frac{\Lambda(n)}n<C\frac{h\log x}{x\log h}$ for $x>2,h>2,a\log x<h<bx$. Unconditional, by a Brun-Titchmarsh-type sieve bound for short intervals (via Brun and Hardy-Littlewood estimates cited as [1],[7]). — *Role:* Controls the contribution of tails S_2,S_3,S_4 in the proof of Lemma 3.
- **THM-PAPER-0147-L3** (Lemma 3; p. 31, proof pp. 31-35, split sums S_1..S_4, Poisson-type kernel sigma/(sigma^2+(tau-log n)^2)). As above: $\pi(e^{\tau+\Delta})-\pi(e^{\tau-\Delta})>\frac{\sigma e^\tau}{\tau}(1-3\Re F)$ for $\tau\log^2\tau\,e^{-\tau}<\sigma<\tau^{-2}$. — *Role:* Fundamental lemma: lower bound for primes in an interval of width approximately 2 Delta in log scale, in terms of the zero sum F. All of Theorems I, II and the Hoheisel proof follow from it.
- **THM-PAPER-0147-L4** (Lemma 4; p. 37-39, proof via $|f(\sigma+i\tau)|^2\le\sigma\int|\Phi(v,\tau)|^2e^{-v\sigma}dv$ and the Fejer-type kernel $g(x)=2-|x|$ and $N(T)$ estimate). Mean-square bound for F on vertical unit segments under RH, as above. — *Role:* Replaces a pointwise bound of Re F by an average bound; essential for Theorem II (exceptional gaps are rare).

### Proof architecture

Explicit formula expresses sum_{rho} e^{-(gamma-i beta)s} (F) through prime-power sums G with a Poisson/Lorentzian kernel sigma/(sigma^2+(tau-log n)^2) concentrated at n near e^tau (Lemma 1 and eq. (11)). Lemma 2 (short-interval sieve bound) estimates the tails, giving Lemma 3: a lower bound for primes in (e^{tau-Delta}, e^{tau+Delta}) provided Re F<1/3. Under RH |F| <= e^{-tau/2} sum e^{-gamma sigma} is small for sigma around tau e^{-tau/2}, giving Theorem I. For general sigma(tau), Lemma 4 gives mean-square smallness of F, so that exceptional tau (those where an interval of length Delta contains no primes) have small measure. Transfer to prime gaps: for a gap > h(p_n) the tau-interval (log p_n - Delta... ) lies inside (log p_n, log p_{n+1}), thus all such tau are exceptional. Summing counts over dyadic ranges gives Theorem II, and then Theorem III.

Dependency edges: CAND-00191 → CAND-00260 (cites as probabilistic background [6]); CAND-00191 → Cramér 1919 Math. Z. 4 (Theorem I reproved; explicit formula imported)

**Imported results.** Cramér 1919/[3] (Studien ueber die Nullstellen der Riemannschen Zetafunktion, Math. Z. 4 (1919) 104-130): explicit formula for 2piF(s); Asymptotic N(T)=T/(2pi)(log T/(2pi)-1)+O(log T) (Riemann-von Mangoldt); Brun-type sieve and Hardy-Littlewood bounds for pi(x+h)-pi(x) (refs [1],[7]); Tchudakoff's 1936 zero-density claim (footnote 3, unproved in this paper); Borel-Cantelli lemma (Cantelli [2])

**Techniques.** explicit formula of Cramér type linking zero sum to prime sum; Poisson/Lorentz kernel localization in log scale; mean-square estimate of Dirichlet series over zeros using N(T); dyadic decomposition and Abel summation; probabilistic heuristic with Borel-Cantelli

## Context and interpretation

**Importance and obstacle overcome.** First treatment of how RH constrains the frequency of exceptionally large prime gaps; it replaces pointwise control of Re F by averaged control, and Theorem II/Lemma 4 give e.g. that gaps exceeding log^3 p occur with total length o(x). It also contains the probabilistic model and the Cramér conjecture (4), now standard.

**Relation to prior work.** Extends Cramér 1919 (Theorem I there) and gives a new proof of Hoheisel via Lemma 3; the probabilistic part is the first appearance in print of the heuristic that max gap is about (log p)^2 (the same model is in the 1934 talk, CAND-00260).

**Limitations and open questions.** The Cramér conjecture $p_{n+1}-p_n=O((\log p_n)^2)$ remains unproved; the rigorous result (Theorem I) is still $O(\sqrt p\log p)$. Theorem II is a conditional density bound and not a pointwise bound. The footnote claims a proof of the Hoheisel estimate (26) but does not give it. Heuristics: this paper takes the pure independent model, which was later shown to be too crude for large gaps (Granville 1995, not verified here).

## Research potential

- **Hypotheses that might be weakened.** Lemma 4 and Theorem II use full RH through |F|<=e^{-tau/2}sum e^{-gamma sigma}; replace by a zero-density estimate (Montgomery) or by a hypothesis 'RH for a positive proportion / for zeros up to height T' to see which of (39)-(40) survive.
- **Generalizations.** Replace zeta by Dirichlet L-functions, to get gaps between primes in arithmetic progressions under GRH. Replace the sharp N(T) by the quantitative zero-density bound.
- **Candidate connections.** Compare Theorem II(40b) with Selberg's 1943 result and with Heath-Brown/Goldston for conditional bounds on exceptional gaps; Lemma 3 is an early form of the explicit-formula test-function approach (Kernel sigma/(sigma^2+x^2)) used in Goldston-Montgomery pair correlation. From memory, not verified here.
- **Reusable lemmas.** Lemma 3 as an unconditional lower-bound lemma in terms of Re F; Lemma 4 mean-square bound; Lemma 2 short-interval sieve bound.
- **Possible experiments.** For x up to about 1e12 tabulate S_{alpha,beta}(x) and N_{alpha,beta}(x) for h = log^3 x and h = sqrt(x) log x (beta in {0.5,1,1.5}) and compare with the bounds in (39)-(40) to see the actual constants; compute the actual Re F(sigma+i tau) from the first 1e6 zeros for tau in log scale and test the 1/3 threshold in Lemma 3.
- **Risks / barriers.** Square-root barrier: with only |F|<small one cannot go below sqrt(p) log p; getting log^2 requires RH plus pair-correlation-type input; not accessible by this method.

## Audit notes (Level 1 reader)

Mild: Lemma 3 has the stated range tau log^2 tau e^{-tau} < sigma < 1/tau^2, while in application sigma = tau e^{-tau/2} (fine). The bound (26) for sigma=e^{-delta tau} is asserted without proof (p. 35-36, footnote 5). Otherwise none noticed in inspected portion; unread parts: details of p. 43 and Lemma-type bounds for N_{alpha,beta} in (49)-(51).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00191`; harvest queries: citation_expansion.
- Triage decision: include — Cramer's probabilistic model and RH-conditional gap bound.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

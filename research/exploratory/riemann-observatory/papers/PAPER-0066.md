# PAPER-0066 — Beyond pair correlation

| Field | Value |
|---|---|
| Authors | Montgomery, H. L.; Soundararajan, K. |
| Year / stratum | 2002 / S5 |
| Venue | Halász, Gábor (ed.) et al., Paul Erdős and his mathematics I. Based on the conference, Budapest, Hungary, July 4--11, 1999. Berlin: Springer; Budapest: János Bolyai Mathematical Society (ISBN 3-540-42236-6/2-vol.-set; 963-8022-96-5). Bolyai Soc. Math. Stud. 11, 507-514 (2002). |
| Identifiers | zbMATH [1095.11043](https://zbmath.org/?q=an:1095.11043) · arXiv [math/0003234](https://arxiv.org/abs/math/0003234) |
| MSC | 11N05, 11M06 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arXiv:math/0003234 |
| Selection | score 4.5136, in-pool citations 19, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Short-interval prime statistics beyond pair correlation. The paper tests numerically, for $\psi(x+h)-\psi(x)-h$ with $h=10^5$ and $x\le X=10^{10}$, whether the second moment matches the Goldston-Montgomery pair-correlation prediction. It then refines the heuristic with the exact secondary main term, which comes from the Hardy-Littlewood singular series averaged over $k\le h$. Note: the triage text ('higher correlation of zeros') is inaccurate. The paper concerns primes in short intervals and the twin-prime singular series, and the zeros enter only through the Goldston-Montgomery equivalence under RH.

### Main results

- **THM-PAPER-0066-1** ((1) Goldston-Montgomery (imported), imported equivalence, background, scope: conditional; p.1, eq. (1)). Assuming RH, the Pair Correlation Conjecture is equivalent to $\int_1^X(\psi(x+h)-\psi(x)-h)^2dx\sim hX\log(X/h)$ uniformly for $X^{\epsilon}\le h\le X^{1-\epsilon}$ (quoted as ref. [3]; the paper's displayed range 'X^e <= h <= X^{1-e}' is partly garbled in the extract). The Cramer model would instead predict $\sim hX\log X$. *Conditional on:* RH.
- **THM-PAPER-0066-2** (Table 1 / numerics, computation, scope: computational; p.1-2, Table 1, Figure 1). For $0\le x\le X=10^{10}$ and $h=10^5$, the moments $\mu_k=\frac1X\int_0^X(\psi(x+h)-\psi(x)-h)^kdx$ were computed. They give $\mu_2=9.0663\times10^5$ (the Cramer prediction is $h\log X=23.02\times10^5$ and the PCC prediction $h\log(X/h)=11.51\times10^5$). The normalized moments $\tilde\mu_4\approx3.04$ and $\tilde\mu_6\approx15.53$ (Gaussian values 3 and 15) show the distribution is close to normal, with a slightly heavy sixth moment. The extremes are about $+5.30\sigma$ and $-5.17\sigma$. $\operatorname{meas}\{x\le10^{10}:|\psi(x+10^5)-\psi(x)-10^5|>3000\}=3080882$, fewer than expected for a Gaussian.
- **THM-PAPER-0066-3** (Theorem, theorem (unconditional), scope: asymptotic; p.4, Theorem; proof pp.4-5). Let $\mathfrak S(k)=\prod_{p\mid k}\bigl(1-\frac1{p-1}\bigr)\prod_{p\nmid k}\bigl(1-\frac1{(p-1)^2}\bigr)$ for even $k$ and $0$ for odd $k$ (written as $2C\prod_{p\mid k,p>2}\frac{p-1}{p-2}$ with $C=\prod_{p>2}(1-(p-1)^{-2})$ for even $k$). Then, for every $\epsilon>0$, $\sum_{k=1}^{h}(h-k)\mathfrak S(k)=\tfrac12h^2-\tfrac12h\log h+Ah+O(h^{1/2+\epsilon})$ with $A=(1-\gamma_0-\log 2)/2$ ($\gamma_0$ Euler's constant).
- **THM-PAPER-0066-4** ((2), conjecture / heuristic, scope: conditional; p.4, eq. (2) and following text). Given the Theorem and the Hardy-Littlewood conjecture with $E(X,k)\ll X^{1/2+\epsilon}$ uniformly in $1\le k\le X$ and cancellation in the error sum: $\int_0^X(\psi(x+h)-\psi(x)-h)^2dx=hX\log(X/h)+BhX+\text{smaller terms}$, with $B=\gamma_0-\log2\pi... $ in the extract. The extract gives $B=C_0-\log 2=\,$'2.41509' (garbled), and the printed value $2.41509$ cannot equal $\gamma_0-\log 2$ read literally. Treat the exact closed form of $B$ as unverified against the PDF image. The conjectured error is $\ll h^{1/2}X^{1/2+\epsilon}+h^{3/2+\epsilon}X^{1/2}$. *Conditional on:* quantitative Hardy-Littlewood prime-pair conjecture with E(X,k) << X^{1/2+eps}, cancellation in sum of (h-k)E(X,k).

### Principal lemmas

- **THM-PAPER-0066-L1** (Proof of Theorem: reduction; p.4). With $s(k)=\prod_{p\mid k,p>2}\frac{p-1}{p-2}$, $\sum_{k\le h}(h-k)\mathfrak S(k)=2\sum_{k\le h/2}(h/2-k)\,s(k)\cdot 2$ after the even-$k$ substitution, so it suffices to show $\sum_{k\le K}(K-k)s(k)=\frac{K^2}{2}\cdot\frac{?}{}$ ... (extract: $=\frac{K^2}{2}\cdot\frac{2}{\pi^2}$-type main term) $-\frac{K\log K}{2}+\frac K2(1-\gamma_0-\log 4)$ plus an error term. The exact constant in front of $K^2$ in the extract is garbled. — *Role:* reduces the Theorem to a Dirichlet series computation
- **THM-PAPER-0066-L2** (Dirichlet series identity; p.4-5). $S(s)=\sum_{k\ge1}s(k)k^{-s}=\zeta(s)T(s)$ with $T(s)=\prod_{p>2}\bigl(1+\frac{p-2}{(p-1)... }\bigr)$ (symbol-level garbled); $T(s)=\zeta(s+1)^{-1}(1-2^{-s-1})\,U(s)$ for $\Re s>-1/2$, where $U$ is an absolutely convergent Euler product with $U(0)=2/\pi^2\cdot$(the extract prints $2/\pi$, ambiguous) and $U'(0)=0$. — *Role:* Perron/Mellin representation of the Cesaro sum
- **THM-PAPER-0066-L3** (Contour shift; p.5). Writing $\sum_{k\le K}(K-k)s(k)=\frac1{2\pi i}\int_{(a)}S(s)\frac{K^{s+1}}{s(s+1)}ds$ ($a>1$) and shifting to $\Re s=b\in(-1/2,0)$ picks up a simple pole at $s=1$ (from $\zeta$) and a double pole at $s=0$ (using $\zeta(s+1)=1/s+\gamma_0+O(|s|)$, $\zeta(0)=-1/2$, $\zeta'(0)=-\frac12\log2\pi$). The remaining integral is $\ll_b K^{b+1}$, using the functional equation with Stirling and the mean-square estimate for $\zeta$ on $[\frac12+\eta,\ldots]$ (Titchmarsh Thm 7.2) with Cauchy-Schwarz. — *Role:* gives the $K\log K$ and linear secondary terms

### Proof architecture

The heuristic arithmetic in section 1 expands $\int(\psi(x+h)-\psi(x)-h)^2$ into a diagonal term $h\sum\Lambda(n)^2\sim hX\log X-hX$ (PNT with RH-strength remainder) plus an off-diagonal term $2\sum_{k\le h}(h-k)\sum_{n\le X}\Lambda(n)\Lambda(n+k)$. Replacing the inner sum by the Hardy-Littlewood prediction $\mathfrak S(k)X$ leaves the Cesaro sum of the singular series. The Theorem is then a rigorous Mellin-Perron computation of that sum. The numerical test is the only independent check on the conjectural step.

**Imported results.** Goldston-Montgomery 1987 equivalence of PCC and the variance asymptotics under RH; Hardy-Littlewood prime-pair conjecture (assumed for (2)); Titchmarsh Thm 7.2 mean-square of zeta; zeta functional equation and Stirling

**Techniques.** Hardy-Littlewood singular series; Perron/Mellin integral with contour shift; Euler product factorization of $\sum s(k)k^{-s}$; large-scale sieve computation of $\psi$ increments; moment comparison with Gaussian

## Context and interpretation

**Importance and obstacle overcome.** It exposes that the leading pair-correlation prediction $hX\log(X/h)$ is off by an $O(hX)$ term that matters at accessible ranges. The numerically observed second moment was lower than even the PCC leading term. The paper shows the discrepancy is accounted for by the lower-order singular-series contribution $Bh X$, with predicted $9.098\times10^5$ against observed $9.066\times10^5$. This is a cautionary example for inferring structure from leading terms only.

**Relation to prior work.** 

**Limitations and open questions.** The second-moment formula (2) is not proved. It depends on the quantitative Hardy-Littlewood conjecture, which is open, and on an assumed cancellation in $\sum(h-k)E(X,k)$. The numerics use one pair $(X,h)=(10^{10},10^5)$. The authors explicitly flag that $T(1)=U(0)=2/\pi^2$-type coincidences and $U'(0)=0$ look 'fortuitous' and say that 'something is going on that remains to be understood'. That is an open question about the structural origin of these identities.

## Research potential

- **Hypotheses that might be weakened.** The Hardy-Littlewood error bound $E(X,k)\ll X^{1/2+\epsilon}$ uniformly up to $k\le X$ could be weakened to an average-in-$k$ bound. Montgomery-Soundararajan's follow-up work on primes in short intervals carries out this kind of weakening.
- **Generalizations.** Redo the Cesaro-sum Theorem with other weights (smooth, Fejer) or for $\sum(h-k)\mathfrak S_{\mathcal A}(k)$ for other prime $k$-tuples patterns.
- **Candidate connections.** Link to Goldston-Montgomery and Bogomolny-Keating (lower-order terms in zero correlations). The $\log(X/h)$ versus $\log X$ gap parallels the structure of CFKRS shifted-moment main terms (CAND-01200).
- **Reusable lemmas.** The Theorem (Cesaro-averaged singular series with explicit linear term) is a clean, rigorous lemma for any short-interval variance computation. The Perron-shift template carries over directly.
- **Possible experiments.** Recompute $\mu_2$ for several $(X,h)$ (e.g. $h=10^3..10^6$, $X=10^{9}..10^{11}$) and test (2) including the $BhX$ term. Check the exponent in the unproved error $h^{1/2}X^{1/2+\epsilon}+h^{3/2+\epsilon}X^{1/2}$. Check numerically the identities $T(1)$, $U(0)$, $U'(0)=0$ to see whether they are exact.
- **Risks / barriers.** The claimed main-term constants must be checked against the PDF; extracted text lost glyphs. The Theorem alone says nothing about RH, and the numerics are a single finite sample.

## Audit notes (Level 1 reader)

Extraction is lossy: all 'c' glyphs are dropped, and several constants ($B$, $U(0)$, the $K^2$ coefficient, $C$) are unreadable or ambiguous, so the exact values in this record are unverified for those. For example, the printed $B=2.41509$ cannot be $\gamma_0-\log 2=-0.116$ read literally; the true value is likely $\gamma_0-\log 2\pi$-type or a different expression, so check against the PDF. Also p.3: the Theorem statement lists the error $O(h^{1/2+\epsilon})$ while the proof sketches the integral bound $K^{b+1}$ with $b\to1/2$, which is consistent. The Table 1 first row entry is 1.0000 for $\mu_0$, as expected. No other issue noticed.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01265`; harvest queries: kw_RH_any, kw_pair_correlation, kw_zeta_zeros, msc_11M06, msc_11N05.
- Triage decision: include — Higher correlations of zeros beyond pair correlation.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

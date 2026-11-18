# PAPER-0132 — Nonvanishing of quadratic Dirichlet \(L\)-functions at \(s=\frac{1}{2}\)

| Field | Value |
|---|---|
| Authors | Soundararajan, K. |
| Year / stratum | 2000 / S4 |
| Venue | Ann. Math. (2) 152, No. 2, 447-488 (2000). |
| Identifiers | zbMATH [0964.11034](https://zbmath.org/?q=an:0964.11034) · DOI [10.2307/2661390](https://doi.org/10.2307/2661390) · arXiv [math/9902163](https://arxiv.org/abs/math/9902163) |
| MSC | 11M20 |
| Families | A, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/math/9902163 |
| Selection | score 3.7486, in-pool citations 91, seed lists 0, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Show that a positive proportion (in fact at least 7/8) of quadratic Dirichlet L-functions $L(s,\chi_{8d})$ do not vanish at the central point $s=1/2$, by computing mollified first and second moments, handling an unexpected off-diagonal contribution in the second moment.

**Historical motivation.** Chowla's conjecture that $L(1/2,\chi)\ne0$; Jutila's $\gg X/\log X$ via first and second moments; GRH-conditional 15/16 (Ozluk-Snyder) from Katz-Sarnak; the earlier twist-family paper [19] could not evaluate an off-diagonal term for psi=1.

### Main results

- **THM-PAPER-0132-1** (Theorem 1, theorem, scope: asymptotic; Sec. 1, p.448). For at least 87.5% of odd square-free $d\ge0$, $L(\tfrac12,\chi_{8d})\ne0$: for all large $x$ and any fixed $\varepsilon>0$, $\sum_{\substack{d\le x\\L(1/2,\chi_{8d})\ne0}}\mu(2d)^2\ge(\tfrac78-\varepsilon)\sum_{d\le x}\mu(2d)^2$.
- **THM-PAPER-0132-2** (Corollary 1.4, corollary, scope: asymptotic; Sec. 1, p.454). There is a degree-3 polynomial Q with $\sum_{0\le d\le X}L(\tfrac12,\chi_{8d})^2=XQ(\log X)+O(X^{5/6+\varepsilon})$, sum over fundamental discriminants $8d$.
- **THM-PAPER-0132-3** (Theorem 2, theorem, scope: asymptotic; Sec. 1 p.454; Sec. 7). There is a degree-6 polynomial R with $\sum_{0\le d\le X}L(\tfrac12,\chi_{8d})^3=XR(\log X)+O(X^{11/12+\varepsilon})$, sum over fundamental discriminants $8d$ (sketch only, Sec. 7).
- **THM-PAPER-0132-4** (Proposition 1.1, proposition, scope: asymptotic; Sec. 1 p.451; proof Sec. 3). If $M(d)=\sum_{l\le M}\lambda(l)\sqrt l\,(\tfrac{8d}{l})$ with $\lambda(l)\ll l^{-1+\varepsilon}$, then for $j=1,2$: $S_R(|M(d)^jA_j(d)|;\Phi)\ll\big(\tfrac{X^\varepsilon}{Y}+\tfrac{M^{2}}{X^{1/2-\varepsilon}}\big)^{j}$-type bound (exact form per source p.451: $\ll (X^\varepsilon/Y + M^2/X^{1/2-\varepsilon})$ to power structure garbled in extraction).
- **THM-PAPER-0132-5** (Proposition 1.2, proposition, scope: asymptotic; Sec. 1 p.452; proof Sec. 4 (Polya-Vinogradov)). For odd $l=l_1l_2^2$, $l_1$ square-free: $2S_M(\tfrac{8d}{l}A_1(d);\Phi)=\frac{\hat\Phi(0)C}{\zeta(2)}\frac{\sqrt{l}}{... l_1 g(l)}\Big(\log\frac{X}{l_1}+C_2+\sum_{p|l}\frac{C_2(p)}{p}\log p\Big)+O\big(\ldots\big)$ (main term as in p.452; error uses $Y$, $X^{1/2-\varepsilon}$), with $C=\frac13\prod_{p\ge3}(1-\frac1{p(p+1)})$, $g(l)=\prod_{p|l}\frac{p+1}{p}(1-\frac1{p(p+1)})$. Exact formula only partially captured by text extraction.
- **THM-PAPER-0132-6** (Proposition 1.3, proposition, scope: asymptotic; Sec. 1 pp.453; proof Sec. 5 (Poisson summation)). Second mollified-moment asymptotic for $2S_M(\tfrac{8d}{l}A_2(d);\Phi)$ with main term $\frac{D\hat\Phi(0)}{36\zeta(2)}\frac{d(l_1)}{\sqrt{l_1}\sigma(l_1)h(l)}\big(\log^3\frac{X}{l_1}-\ldots\big)$ plus lower-order terms $O(l)$ with polynomials $Q_{j,k}$ of degree <=2, plus remainder $R(l)$, $|R(l)|\ll \ldots l^{1/2+\varepsilon}Y^{1+\varepsilon}/X^{1/2-\varepsilon}$ pointwise and $\sum_{L\le l<2L}|R(l)|\ll\ldots L^{1+\varepsilon}Y^{1+\varepsilon}/X^{1/2-\varepsilon}$ on average.
- **THM-PAPER-0132-7** (Sec. 6 optimal-mollifier remark, remark/result, scope: asymptotic; Sec. 1 pp.453-454; Sec. 6). With mollifier length $\sqrt X^{\theta}$ (i.e. $M=X^{\theta/2}$), the optimal mollifier yields proportion $\ge1-(\theta+1)^{-3}+o(1)$; Props 1.2-1.3 allow $\theta=1-\varepsilon$ giving 7/8. Arbitrary length ($\theta\to\infty$) would give almost all.

### Key definitions

- $\chi_{8d}=(\tfrac{8d}{\cdot})$
- $M(d)=\sum_{l\le M}\lambda(l)\sqrt l(\tfrac{8d}{l})$ mollifier of length M
- $S(f_d;F)=\frac1X\sum_{d\ odd}\mu^2(d)f_dF(d/X)$
- $\omega_j(\xi)=\frac1{2\pi i}\int_{(c)}\big(\frac{\Gamma(1/2+s/4)}{\Gamma(1/4)}\big)^j\xi^{-s}\frac{ds}{s}$

### Principal lemmas

- **THM-PAPER-0132-L1** (Lemma 2.2; Sec. 2). For odd positive square-free d and $j\ge1$: $L(\tfrac12,\chi_{8d})^j=2A_j(d)$ with $A_j(d)=\sum_{n\ge1}\frac{(8d/n)d_j(n)}{\sqrt n^{\,j}}\omega_j\big(\frac{n\pi}{8d}\big)$-type smoothed sum (def. (1.6)). — *Role:* Approximate functional equation for L and L^2 (the real character gives root number 1).
- **THM-PAPER-0132-L2** (Lemma 2.4; Sec. 2.3 (imported from Heath-Brown [9])). Heath-Brown large sieve for real characters: $\sum_{\chi\in S(Q)}|\sum_{n\le N}a_n\chi(n)|^2\ll_\varepsilon(QN)^\varepsilon(Q+N)\sum_{n_1n_2=\square}|a_{n_1}a_{n_2}|$, S(Q)= real primitive characters of conductor <=Q. — *Role:* Bounds non-principal character sums in the off-diagonal terms.
- **THM-PAPER-0132-L3** (Lemma 2.5; Sec. 2.3 (imported from Heath-Brown [9], Thm 2)). For $\sigma\ge1/2$: $\sum_{\chi\in S(Q)}|L(\sigma+it,\chi)|^4\ll Q^{1+\varepsilon}(1+|t|)^{1+\varepsilon}$ and the square-moment analog with $(1+|t|)^{1/2+\varepsilon}$. — *Role:* Controls the tail terms/remainders.
- **THM-PAPER-0132-L4** (Lemma 2.6; Sec. 2.4). For F nonnegative smooth supported in (1,2) and odd n: $S_M(\tfrac dn;F)=\frac{1}{2n}\frac Xn... \sum_{\alpha\le Y,(\alpha,2n)=1}\frac{\mu(\alpha)}{\alpha^2}\sum_k(-1)^kG_k(n)\tilde F\big(\frac{kX}{2\alpha^2n}\big)$ (Poisson summation with Gauss sums $G_k(n)$). — *Role:* Converts the character sum over d to a dual sum in which the k=square terms give the off-diagonal contribution.
- **THM-PAPER-0132-L5** (Lemma 4.1; Sec. 4). Polya-Vinogradov-based bound for $S_M(\tfrac{8d}{ln};\Phi_n)$ when $ln\ne\square$. — *Role:* Shows only $ln=\square$ terms contribute to the first moment (Prop 1.2).
- **THM-PAPER-0132-L6** (Lemmas 5.1-5.5; Sec. 5). Analysis of Dirichlet series of Gauss-sum weights and estimation of the k=square off-diagonal terms (Sec. 5.3). — *Role:* Evaluate the nondiagonal contribution: the most delicate part of the argument.

### Proof architecture

1) Approximate functional equations (Lemma 2.2) express L(1/2)^j via sums with d_j(n). 2) Remove the square-free condition on d with $\mu^2(d)=M_Y(d)+R_Y(d)$ (Y a parameter), the tail R_Y handled by Proposition 1.1 through Heath-Brown's large sieve (Lemmas 2.4-2.5). 3) First mollified moment: Polya-Vinogradov reduces to diagonal ln=square (Prop 1.2). 4) Second mollified moment: Poisson summation in d (Lemma 2.6) isolates k=0 (diagonal) and a nonzero k=square off-diagonal term that cannot be ignored; evaluated in Sec. 5.3 giving the polynomial-in-log main term with lower-order terms (Prop 1.3). 5) Choose optimal mollifier lambda(l) ~ mu(l)/l * log^2(M/l)/log^2 M * (log(X^{3/2}...M^2 l)/log M)-shaped (Sec. 6) with M=X^{1/2-eps}, evaluate (6.4) and the second-moment sum, and conclude ratio via Cauchy-Schwarz: (sum of first mollified moment)^2/(second mollified moment) >= (7/8-eps) * count. 6) Corollary 1.4 from Prop 1.3 with l=1; Theorem 2 by sketch.

Dependency edges: Lemma 2.2 → Props 1.2, 1.3 (input); Lemma 2.6 (Poisson) → Prop 1.3 (input); Props 1.1-1.3 → Theorem 1 (input); Prop 1.3 (l=1) → Corollary 1.4 (specialization)

**Imported results.** Heath-Brown, large sieve for real characters, Quart. J. Math. 1995 (Cor. 2, Thm 2); Polya-Vinogradov inequality; Jutila's first/second moment asymptotics (for comparison); Katz-Sarnak symmetry heuristics (motivation only)

**Techniques.** mollifier method (Bohr-Landau, Selberg); approximate functional equation; Poisson summation with Gauss sums; Polya-Vinogradov; Heath-Brown large sieve for quadratic characters; off-diagonal analysis via Dirichlet series; optimization of mollifier coefficients

## Context and interpretation

**Importance and obstacle overcome.** First unconditional positive proportion (7/8) of central nonvanishing for the quadratic family, matching the symplectic-symmetry expectation structure; obstacle was the unexpected off-diagonal contribution in the mollified second moment, evaluated here via Poisson summation (Sec. 5.3).

**Relation to prior work.** Improves Jutila (X/log X); compares with Iwaniec-Sarnak (1/3 for characters mod q), Balasubramanian-Murty; proportion matches Kowalski-Michel (rank J_0(q), 7/8) and Conrey-Ghosh-Gonek conditional $1-(\theta+1)^{-3}$ for simple zeros.

**Limitations and open questions.** Mollifier length limited to $X^{1/2-\varepsilon}$, giving 7/8; no mollifier beyond that, so almost-all nonvanishing is open. Fourth moment asymptotic not obtained. Author remarks a result like Cor. 1.4 with remainder $X^{1-1/1500+\varepsilon}$ by Guo (preprint). Nonvanishing for individual d (Chowla) remains open; the result gives positive proportion only, not individual or RH-type statement.

## Research potential

- **Hypotheses that might be weakened.** Restriction to discriminants divisible by 8; stated as extendable to any arithmetic progression of fundamental discriminants and to other points sigma+it (author remark).
- **Generalizations.** Longer mollifiers (theta>1) would raise proportion to $1-(\theta+1)^{-3}$; this requires beating the X^{1/2} barrier in off-diagonal terms, analogously to Conrey-Ghosh-Gonek (simple zeros, GRH).
- **Candidate connections.** 1-(theta+1)^{-3} appears in Kowalski-Michel and CGG; the paper suggests but does not explain a link to simple zeros of zeta (Sec. 1).
- **Reusable lemmas.** Lemma 2.6 (Poisson summation for $\mu^2$-twisted quadratic sums), Props 1.1 (tail of squarefree sieve) and 1.3 (off-diagonal evaluation).
- **Possible experiments.** Numerically compute the mollified first and second moments for fundamental discriminants up to ~10^7 with the paper's optimal lambda(l), to check the predicted main terms and the size of the off-diagonal contribution; compare with 1-(theta+1)^{-3} for theta<1.
- **Risks / barriers.** Extending mollifier beyond X^{1/2} would hit the Poisson/large-sieve error barrier in Props 1.1-1.3; positive-proportion result says nothing about a specific zero or RH.

## Audit notes (Level 1 reader)

Extraction garbled the exact forms of Props 1.1, 1.2, and 1.3 (display math lost); the statements recorded for those three are partial and flagged accordingly; not rechecked against the Annals version. Abstract numeric claims in Theorem 1 and Corollary 1.4/Theorem 2 are exact as in text. No inconsistencies noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01099`; harvest queries: msc_11M20, citation_expansion.
- Triage decision: include — Landmark nonvanishing at central point of quadratic L-functions.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

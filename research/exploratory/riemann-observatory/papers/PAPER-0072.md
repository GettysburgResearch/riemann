# PAPER-0072 — An upper bound for discrete moments of the derivative of the Riemann zeta-function

| Field | Value |
|---|---|
| Authors | Kirila, Scott |
| Year / stratum | 2020 / S6 |
| Venue | Mathematika 66, No. 2, 475-497 (2020). |
| Identifiers | zbMATH [1442.11123](https://zbmath.org/?q=an:1442.11123) · DOI [10.1112/mtk.12008](https://doi.org/10.1112/mtk.12008) · arXiv [1804.08826](https://arxiv.org/abs/1804.08826) |
| MSC | 11M06, 11M26 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1804.08826 |
| Selection | score 4.4885, in-pool citations 9, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Assuming RH, what is the correct order of magnitude upper bound for the discrete moments J_k(T)=\frac1{N(T)}\sum_{0<\gamma\le T}|\zeta'(\rho)|^{2k} for all real k>0? (Conjecture of Gonek and Hejhal: J_k(T) \asymp (\log T)^{k(k+2)}.)

**Historical motivation.** Gonek (1984) conditionally showed J_1(T) ~ (1/12)(log T)^3; Gonek and Hejhal independently conjectured J_k(T) \asymp (\log T)^{k(k+2)}; Hughes-Keating-O'Connell predicted J_k ~ C_k (log T)^{k(k+2)} with explicit C_k (Barnes G, Euler product). Milinovich proved upper bound with epsilon loss; Harper's method removes epsilon for continuous moments, motivating the adaptation.

### Main results

- **THM-PAPER-0072-1** (Theorem 1.1, theorem, scope: asymptotic; Sec.1, p.2). Assume RH. For every real $k>0$: $J_k(T)\ll_k(\log T)^{k(k+2)}$ as $T\to\infty$, where $J_k(T)=\frac1{N(T)}\sum_{0<\operatorname{Im}\rho\le T}|\zeta'(\rho)|^{2k}$. Implied constant grows like $e^{e^{Ak}}$. *Conditional on:* RH.
- **THM-PAPER-0072-2** (Proposition 4.1, proposition, scope: asymptotic; Sec.4). Assume RH, $k>0$. $\frac1{N(T,2T)}\sum_{T<\gamma\le2T}|\zeta'(\rho)|^{2k}\ll_k(\log T)^{k(k+2)}$ (dyadic version; Thm 1.1 follows by summing over dyadic ranges using $N(2^{-i}T,2^{1-i}T]\asymp2^{1-i}N(T)$). *Conditional on:* RH.
- **THM-PAPER-0072-3** (Theorem 1.2, theorem, scope: asymptotic; Sec.1, p.2-3; proved in last section). Assume RH, $k>0$, $|\alpha|\le(\log T)^{-1}$ complex. Then $\frac1{N(T)}\sum_{0<\operatorname{Im}\rho\le T}|\zeta(\rho+\alpha)|^{2k}\ll_k(\log T)^{k^2}$. Improves Milinovich's Theorem 1.2 (which had an $\varepsilon$ loss). *Conditional on:* RH.
- **THM-PAPER-0072-4** (Corollary 1.3, corollary, scope: asymptotic; Sec.1, p.3). Assume RH, $k\ge1/2$, $\nu\in\mathbb N$. Then $\frac1{N(T)}\sum_{0<\gamma\le T}|\zeta^{(\nu)}(\rho)|^{2k}\ll_{k,\nu}(\log T)^{k(k+2\nu)}$ (Cauchy integral formula on circle radius $(\log T)^{-1}$, Holder, then Thm 1.2). *Conditional on:* RH.

### Principal lemmas

- **THM-PAPER-0072-L1** (Proposition 3.1; Sec.3). Assume RH, $T$ large, $2\le x\le T^2$, $\sigma_x=\tfrac12+\tfrac1{\log x}$. For a zero $\rho=\tfrac12+i\gamma$ with $T<\gamma\le2T$: $\log|\zeta'(\rho)|\le\operatorname{Re}\sum_{n\le x}\frac{\Lambda_L(n)\log(x/n)}{n^{\sigma_x+i\gamma}\log n\log x}+\log\log T+\frac{\log T}{\log x}+O(1)$, with $\Lambda_L(n)=\Lambda(n)$ for $n=p,p^2$, $n\le L$ and 0 otherwise. — *Role:* Harper/Soundararajan-type upper bound for log|zeta'(rho)| by a short Dirichlet polynomial over primes and prime squares; first ingredient of the method.
- **THM-PAPER-0072-L2** (Lemma 5.1; Sec.5). Assume RH. For integers $a>b$: $\sum_{T<\gamma\le2T}(a/b)^{i\gamma}=-\frac{T\Lambda(a/b)}{2\pi\sqrt{a/b}}+O(\sqrt{ab}(\log T)^2)$ (Gonek's uniform Landau formula). — *Role:* Discrete analogue of continuous orthogonality $\int e^{irt}dt$; computes moments of prime Dirichlet polynomials over zeros.
- **THM-PAPER-0072-L3** (Lemma 5.2; Sec.5). For $k>0$ and good $\gamma$: $\exp(2k\sum_iG_{i,j}(\gamma))\ll\prod_i(\sum_{n\le e^2k\beta_i^{-3/4}}(kG_{i,j}(\gamma))^n/n!)^2$ (Taylor truncation of exponential). — *Role:* Replaces exponentials of the Dirichlet polynomial by short polynomials so the Landau formula applies (Harper's Euler-product-free technique).
- **THM-PAPER-0072-L4** (Lemma 5.3; Sec.5). Assume RH. For tuples $\ell_i\le2e^2k\beta_i^{-3/4}$: $\sum_\gamma\prod_iG_{i,j}^{\ell_i}(\gamma)\le N(T,2T)\,\mathbb E[\prod_iG_{i,j}(X)^{\ell_i}]+O(T^{e/25}(\log T)^2)$ with $X$ a random model (independent random variables $X_p$ on the unit circle). — *Role:* Transfers zero-sum of products of Dirichlet-polynomial powers to a probabilistic model.
- **THM-PAPER-0072-L5** (Lemma 5.4/5.5; Sec.5). $\sum_{\gamma}\exp(2k\sum_{i\le I}G_{i,I}(\gamma))\ll N(T,2T)\mathbb E[\exp(2k\sum_i G_{i,I}(X_p))]+e^{2k}T^{e/5}(\log T)^2$, and an inductive step over $j$ with factor $e^{-\beta_{j+1}^{-1/2}\log(1/\beta_{j+1})/21}$ for $\gamma\in S(j)$ (the set where $G_{i,j'}$ small for $j'<j$). — *Role:* Handles zeros where the Dirichlet polynomial is atypically large via Markov/Chebyshev on higher moments.

### Proof architecture

Direct adaptation of Harper's (2013) proof that I_k(T) << T(log T)^{k^2} on RH to the discrete setting. (1) Prop 3.1: RH-conditional upper bound for log|zeta'(rho)| via Soundararajan/Harper truncation, using the identity for -Re zeta'/zeta and Landau-Gonek explicit formula; the extra log log T from the derivative. (2) Prop 4.1 reduces J_k to dyadic zero ranges. Split primes into scales T^{beta_{i-1}}<n<=T^{beta_i}, define Dirichlet polynomials G_{i,j}(t). (3) Partition zeros into 'good' sets S(j) according to which first scale the polynomial becomes large; on S(j) use Taylor truncation (Lemma 5.2) and then compute moments using Gonek's Landau formula (Lemmas 5.1, 5.3) comparing with a random model; induct on j (Lemmas 5.4-5.5). (4) Evaluate the model expectation (Gaussian-type) giving (log T)^{k(k+2)}. (5) Sec.8: Thm 1.2 for shifted moments by same method; Cor 1.3 via Cauchy's formula.

Dependency edges: CAND-01860 → Harper 2013 (Sharp conditional bounds for moments of zeta) (adapts method); CAND-01860 → Milinovich 2010 (Upper bounds for the moments of zeta'(rho)) (sharpens)

**Imported results.** Soundararajan 2009 / Harper 2013 method (Harper: continuous moments of zeta on RH, Q.J.Math? Harper 2013 Sharp conditional bounds for moments of the Riemann zeta function); Gonek 1984 uniform Landau formula (ref [10]); Riemann-von Mangoldt formula N(T)=T/2pi log(T/2pi e)+O(log T); Milinovich 2010 shifted-moment setup; Milinovich-Ng lower bound J_k >> (log T)^{k(k+2)} for natural k; Radziwill-Soundararajan unconditional lower bounds (cited for extension to real k)

**Techniques.** Harper's method (Soundararajan resolution with Euler-product-free moment bounds); Gonek's uniform version of Landau's formula for sums over zeros; Taylor truncation of exponentials of Dirichlet polynomials; dyadic decomposition and induction on prime scales; random model for Dirichlet polynomials (independent unitary random variables); Cauchy integral formula for higher derivatives

## Context and interpretation

**Importance and obstacle overcome.** Removes the epsilon in Milinovich's bound, confirming the Gonek-Hejhal conjecture's upper half for all real k>0 on RH and its full form for natural k (with the Milinovich-Ng lower bound). Obstacle: discrete sums over zeros do not enjoy continuous orthogonality; this is overcome by Gonek's Landau formula in place of orthogonality and the need to handle log|zeta'(rho)| rather than log|zeta|.

**Relation to prior work.** Sharpens Milinovich 2010 (bound with (log T)^epsilon); in same spirit as Harper 2013. Matches the conjectures of Gonek, Hejhal and Hughes-Keating-O'Connell in order of magnitude. Related via Mertens function: J_{-1}(T)<<T plus RH implies M(x)<<x^{1/2}(log x)^{3/2} (Gonek, Ng).

**Limitations and open questions.** Only upper bounds; implied constant grows like exp(exp(Ak)) versus conjectured exp(-k^2 log k)-type; no lower bound for non-integer k in the paper (said to follow from Milinovich-Ng + Radziwill-Soundararajan); negative k (relevant for simple zeros and Mertens) not covered; no asymptotic formula for any k other than the known k=1 (Gonek) conditional. Open: J_{-1}(T)<<T, and the full asymptotic with C_k.

## Research potential

- **Hypotheses that might be weakened.** RH is needed for Prop 3.1 (zeros on the line) and Landau-Gonek formula; one could try versions assuming only a zero-density hypothesis or LH. Cor 1.3 requires k>=1/2 due to Holder step; extending to k<1/2 requires different argument.
- **Generalizations.** Discrete moments at zeros for other L-functions (Dirichlet, automorphic of degree 2) via Harper's method; negative moments J_{-k} (under RH+simplicity) toward Gonek-Hejhal for k<0 relevant to Mertens function bounds M(x)<<x^{1/2}(log x)^{3/2}; mixed moments of zeta^(nu) at zeros (Cor 1.3 gives upper bounds for all nu).
- **Candidate connections.** Mertens function and Ng/Gonek conditional results (J_{-1}<<T => M(x)<<sqrt x (log x)^{3/2}); simple zeros proportion via N*(T)>=J_k^2/J_{2k} (Cauchy-Schwarz, though growth too fast); Hughes-Keating-O'Connell random matrix model of zeta' at zeros; Bui-Gonek-Milinovich hybrid Euler-Hadamard model.
- **Reusable lemmas.** Prop 3.1 (RH-conditional upper bound for log|zeta'(rho)| via short Dirichlet polynomial, usable for any shifted/derivative discrete moment); Lemma 5.1 (Landau-Gonek formula with explicit error) ; Lemma 5.3 (comparison with random model for zero sums).
- **Possible experiments.** Numerically compute J_k(T) from Odlyzko zero tables for k=1/2,1,2,3 and compare with C_k(log T)^{k(k+2)} to test growth of constants; test the T^{e/25} error term in Lemma 5.3 versus numerics; test Cor 1.3 constants for nu=1,2.
- **Risks / barriers.** Method inherently one-sided (upper bounds); extension to negative moments requires simplicity of zeros and lower-bound control on |zeta'(rho)|, which is out of reach (equivalent to strong conjectures); implied constants doubly exponential in k.

## Audit notes (Level 1 reader)

none noticed in inspected portion (the text itself notes in a footnote that Conrey-Ghosh-Gonek's GLH-based 19/27 simple-zero result had a gap, corrected by assuming GRH; the statement of Prop 5.2's exponent '3/4' and the definition of beta_i were read from garbled extraction and not independently verified).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01860`; harvest queries: kw_RH_any, msc_11M06, msc_11M26, arxiv_critical_line, arxiv_rh_abs.
- Triage decision: include — Sharp RH-conditional discrete moments of zeta' at zeros.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

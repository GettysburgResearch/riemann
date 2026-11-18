# PAPER-0075 — Zeros of Jensen polynomials and asymptotics for the Riemann xi function

| Field | Value |
|---|---|
| Authors | O'Sullivan, Cormac |
| Year / stratum | 2021 / S6 |
| Venue | Res. Math. Sci. 8, No. 3, Paper No. 46, 27 p. (2021). |
| Identifiers | zbMATH [1479.11146](https://zbmath.org/?q=an:1479.11146) · DOI [10.1007/s40687-020-00240-5](https://doi.org/10.1007/s40687-020-00240-5) · arXiv [2007.13582](https://arxiv.org/abs/2007.13582) |
| MSC | 11M26, 11M06, 41A60 |
| Families | C, F |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/2007.13582 |
| Selection | score 4.4561, in-pool citations 8, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Is there a Jensen-type criterion for RH using Hermite polynomials (P^{d,n}(X)=sum binom(d,j) gamma(n+j) H_{d-j}(X)) that is easier to verify than hyperbolicity of J^{d,n}, and what are precise asymptotics for the Taylor coefficients gamma(n) of xi at 1/2?

**Historical motivation.** After GORZ 2019 revived the Jensen criterion, O'Sullivan sought a variant of the criterion with better properties (using Hermite polynomials), and a rigorous complete asymptotic expansion for the xi Taylor coefficients, following a suggestion of Romik on the Lambert W function.

### Main results

- **THM-PAPER-0075-1** (Theorem 1.1, theorem, scope: global; Sec 1, from Cor 3.2-3.3). RH is true iff $J^{d,n}(X)=\sum_{j=0}^d\binom dj\gamma(n+j)X^j$ is hyperbolic for all $d\ge1,n\ge0$, where $\gamma(m)=\frac{m!}{(2m)!}\xi^{(2m)}(1/2)$, the Taylor coefficients of $\Theta(z)=\xi(1/2+\sqrt z)$.
- **THM-PAPER-0075-2** (Theorem 1.2, theorem, scope: global; Sec 1, Thm 3.5 with Omega = Hermite generating function). RH is true iff $P^{d,n}(X)=\sum_{j=0}^{d}\binom dj\gamma(n+j)H_{d-j}(X)$ is hyperbolic for all $d\ge1,n\ge0$ (a special case of a general theorem where $H$ is replaced by Jensen polynomials of any Laguerre-Polya function).
- **THM-PAPER-0075-3** (Theorem 1.3, theorem, scope: asymptotic; Sec 1, proved in Sec 8). For all sufficiently large $d$, $P^{d,n}(X)$ is hyperbolic whenever $n/\log^2 n\ge d^{3/4}/2$.
- **THM-PAPER-0075-4** (Theorem 1.4, theorem, scope: asymptotic; Sec 1, eq (1.8), proof Sec 7). With $w=W(2n/\pi)$ (Lambert W), as $n\to\infty$: $\gamma(n)=4\pi^2e^{7w/4}\sqrt{\frac{w}{w+1}}\big(\frac{e^{w}}{16ne^{2/w}}\big)^{n}\big(1+\sum_{k=1}^{K-1}c_k(w)n^{-k}+O(\log^K(n)/n^K)\big)$ with $c_1(w)=-\frac{w^4+58w^3+29w^2-24w-16}{192(w+1)^3}$ (the displayed form uses the extraction of (1.8)).
- **THM-PAPER-0075-5** (Theorem 1.5, theorem, scope: asymptotic; Sec 1, (1.9), Sec 7). With $w=W(2n/\pi)$: $\xi^{(2n)}(1/2)=4\pi^2 e^{7w/4}\sqrt{\frac{2w}{w+1}}\,(\frac{w}{2e^{1/w}})^{2n}\,(1+\sum_{k<K}\mu_k(w)n^{-k}+O(\log^K n/n^K))$, a reformulation of GORZ Thm 9 with the Lambert function in place of $L$ with $n=L(\pi e^L+3/4)$.
- **THM-PAPER-0075-6** (Theorem 1.6, theorem, scope: asymptotic; Sec 1, Sec 5-6). For the Turan expansion $\Xi(z)=\sum(-1)^nb_{2n}H_{2n}(z)$, $b_{2n}=4\pi^2\frac{e^{7w/4-w^2/16}}{(2n)!}\sqrt{\frac{2w}{w+1}}\big(\frac{w}{4e^{1/w}}\big)^{2n}(1+\sum\tau_k(w)n^{-k}+O(\log^{3K}n/n^K))$, extending Romik's asymptotics.
- **THM-PAPER-0075-7** (Theorem 3.5 / 3.6, theorem, scope: global; Sec 3). 3.5: for Phi real entire of genus 1 with coefficients c_j and Omega in the Laguerre-Polya class, Phi is hyperbolic iff $\sum_j\binom dj c_j g^*_{d-j}(\Omega;x)$ is hyperbolic for all d. 3.6 gives a further criterion in terms of $\sum_j (c_j/j!)\Omega^{(j)}(z)$ for Phi, Omega both in LP.
- **THM-PAPER-0075-8** (Corollary 3.8, corollary, scope: finite; Sec 3, (1.5)-(1.6)). If $J^{d,n}$ is hyperbolic then $P^{d,n}$ is hyperbolic, so all known J-results transfer to P; the converse fails: $P^{2,n}$ hyperbolic iff $\gamma(n+1)^2+2\gamma(n)^2\ge\gamma(n)\gamma(n+2)$, strictly weaker than Turan.

### Principal lemmas

- **THM-PAPER-0075-L1** (Theorem 8.1 (Turan 1959, Thm III); Sec 8). If $G=\sum_{j\le d}c_jH_j$ is real and $\sum_{j=0}^{d-2}2^jj!\,c_j^2<2^d(d-1)!\,c_d^2$ then all zeros of G are real and simple. — *Role:* imported tool that gives Thm 1.3
- **THM-PAPER-0075-L2** (Theorem 4.1 / Theorem 5.2; Sec 4-5). Complete asymptotic expansion for $I_\alpha(f;n)=\int_1^\infty(\log t)^ne^{-\alpha t}f(t)\,dt$ with $u=W(n/\alpha)$, with explicit error terms. — *Role:* general Laplace-method engine for Thms 1.4-1.6
- **THM-PAPER-0075-L3** (Lemma 4.3 (neglecting the tails) / Lemma 4.5 (central approximation); Sec 4). Tails of the integral beyond $|x|\le\delta=n^{-2/5}$ are negligible and the central part is approximated by a Gaussian-type integral with controlled corrections. — *Role:* error control in the Laplace method
- **THM-PAPER-0075-L4** (Corollaries 3.2, 3.3; Sec 3). $\Theta^{(n)}$ is hyperbolic iff $J^{d,n}$ is hyperbolic for all $d\ge1$; and if $\Theta^{(n)}$ is hyperbolic then so is $\Theta^{(m)}$ for $m>n$ (Polya/Laguerre). — *Role:* link between derivative RH_n and shifts

### Proof architecture

Section 3 shows the abstract criterion: Phi hyperbolic iff the 'Omega-twisted' Jensen polynomials are hyperbolic, for Omega in the Laguerre-Polya class (Hermite generating function e^{2Xt-t^2} is such an Omega). Sections 4-7 prove all-order Laplace asymptotics of gamma(n) in terms of the Lambert function by writing xi^(2n)(1/2) as an integral against (log t)^n of a theta sum. Section 8 combines the asymptotics with Turan's inequality for Hermite expansions to prove Thm 1.3.

**Imported results.** Polya 1927 and Jensen 1913 (Jensen polynomial criterion); Griffin-Ono-Rolen-Zagier 2019 (asymptotics of xi derivatives, Hermite limit); Turan 1959 Thm III (zeros of Hermite sums); Csordas-Norfolk-Varga 1986 (Turan inequalities for xi coefficients); Romik (Hermite expansion of Xi); Chasse 2013 (hyperbolicity for d<=2*10^17)

**Techniques.** Laguerre-Polya class and Jensen-type criteria; Laplace's method with Lambert W; Turan's criterion for Hermite expansions; asymptotic expansion of Turan coefficients b_{2n} of Xi in Hermite polynomials

## Context and interpretation

**Importance and obstacle overcome.** Provides a relaxed (weaker-at-each-point yet globally equivalent) hyperbolicity criterion and the sharpest known closed asymptotics (with all-order, effective error terms) of gamma(n) and xi^(2n)(1/2), usable for any effective Jensen work. It overcomes the missing exact expression by using Lambert W.

**Relation to prior work.** Builds on GORZ 2019 and Griffin et al. (CAND-01931), whose authors mention this paper (remark 4) as complementary. Uses Romik's Hermite expansions and Turan's 1959 result. Wagner (CAND-01962) is cited for L-function generalization.

**Limitations and open questions.** Theorem 1.3 is asymptotic in d with only n/log^2 n >= d^{3/4}/2 and is weaker than a full proof, since RH requires all (d,n) and the region n small relative to d is not covered. Whether P^{d,n} is hyperbolic for all (d,n) is equivalent to RH, so it is not obviously easier. The paper notes P^{d,n} is weaker than J^{d,n} at fixed (d,n), so hyperbolicity is easier to attain but the criterion is equivalent in the limit of all (d,n).

## Research potential

- **Hypotheses that might be weakened.** Theorem 3.5 allows any Omega in the Laguerre-Polya class, so a family of relaxed criteria exists. One can choose Omega adaptively (e.g. Gaussian/Laguerre kernels) to improve the Turan-type bound in Thm 1.3.
- **Generalizations.** Extend Theorem 1.3 to Dirichlet and modular L-functions by combining with Wagner's formulas (CAND-01962), obtaining effective hyperbolicity thresholds beyond the exponent 3/4. Replace d^{3/4} with the best exponent given Theorem 1.4 and compare with the e^{cd} bound of CAND-01931.
- **Candidate connections.** The criterion Theorem 3.5 is a heat-flow/Laguerre-Polya operator statement, so it ties into the full-source operators and heat programme, and via derivative descent (Corollary 3.3) to the xi geometry programme.
- **Reusable lemmas.** Theorem 4.1/5.2 (general (log t)^n Laplace expansion) and explicit c_1(w).
- **Possible experiments.** Compute P^{d,n} for moderate d (up to 50) and n in the transition region using high-precision gamma(n) and Sturm-sequence root counting, to find the actual hyperbolicity frontier of n versus d and compare with J^{d,n} and the bound n >= d^{3/4} log^2 n.
- **Risks / barriers.** Hyperbolicity for all large n is true independently of RH, so this criterion's content is only in the small-n region, which is as hard as RH.

## Audit notes (Level 1 reader)

Paper's (1.8) numerator extracted as 'w^4+58w^3+29w^2-24w-16' and the display of Thm 1.4 was lossily extracted, so exact exponent/constant forms should be checked in the PDF. The statement of Thm 1.3 uses 'for all d sufficiently large', which is ineffective on d. Nothing inconsistent noticed in the inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01869`; harvest queries: kw_RH_any, kw_laguerre_polya_xi, msc_11M06, msc_11M26, arxiv_jensen_poly, arxiv_rh_abs.
- Triage decision: include — Jensen polynomial criterion reformulated, asymptotics of xi.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

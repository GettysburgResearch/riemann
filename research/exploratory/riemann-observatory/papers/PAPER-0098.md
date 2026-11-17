# PAPER-0098 — The Jensen-Pólya program for various \(L\)-functions

| Field | Value |
|---|---|
| Authors | Wagner, Ian |
| Year / stratum | 2020 / S6 |
| Venue | Forum Math. 32, No. 2, 525-539 (2020). |
| Identifiers | zbMATH [1452.11104](https://zbmath.org/?q=an:1452.11104) · DOI [10.1515/forum-2019-0104](https://doi.org/10.1515/forum-2019-0104) · arXiv [1905.11269](https://arxiv.org/abs/1905.11269) |
| MSC | 11M26 |
| Families | C, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/1905.11269 |
| Selection | score 4.312, in-pool citations 5, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Do the Griffin-Ono-Rolen-Zagier (GORZ) results, namely hyperbolicity of Jensen polynomials J^{d,n} for all sufficiently large n at fixed d, extend from the Riemann Xi-function to other completed L-functions (Dirichlet, modular, Dedekind)? This gives evidence for GRH, not a proof.

**Historical motivation.** After GORZ (PNAS 2019) proved the asymptotic hyperbolicity of Jensen polynomials for xi and conjectured/suggested extensions, Wagner asked whether the Hermite phenomenon is specific to zeta or holds for other L-functions, given the Polya/Jensen criterion and the GUE heuristics.

### Main results

- **THM-PAPER-0098-1** (Definition 1.1, definition, scope: asymptotic; Sec 1, eq (1.4)). A real sequence $a:\mathbb N\to\mathbb R$ is Hermite-Jensen if there are positive sequences $A(n)$, $\delta(n)$ with $\delta(n)\to0$ such that $\log\frac{a(n+j)}{a(n)}=A(n)j-\delta(n)^2j^2+o(\delta(n)^d)$ as $n\to\infty$ for some $d\ge1$ and all $0\le j\le d$.
- **THM-PAPER-0098-2** (Definition 1.2, definition, scope: asymptotic; Def 1.2, (1.5)-(1.7)). A Dirichlet series $L(s)=\sum a(n)n^{-s}$ is good if (1) its completion is $\Lambda(s)=N^{s/2}\int_0^\infty[f(t)-f(\infty)]t^{s}\,dt/t$ with $f(t)=\alpha(0)+\sum_{n\ge n_0}\alpha(n)e^{-\pi nt}$; (2) $f(1/(Nt))=\epsilon N^{1/2}\ t^k f(t)$ with $\epsilon=\pm1$, giving $\Lambda(s)=\epsilon\Lambda(k-s)$, $k\in\mathbb Q$; (3) the coefficients of $\Lambda$ are real. Xi(z) is $\Lambda(k/2-iz)$ (times $-z^2-k^2/4$ if a pole at $s=k$).
- **THM-PAPER-0098-3** (Theorem 1.3, theorem, scope: asymptotic; Sec 1, proved in Sec 2-3). If $L(s)$ is a good Dirichlet series, then for each fixed $d\ge1$ the Jensen polynomial $J_\gamma^{d,n}(X)$ (with $\gamma(n)$ the Taylor coefficients of $\Xi_1(x)=\Xi(i\sqrt x)$, or $\Xi(i\sqrt x)/\sqrt x$ in the odd case $\epsilon=-1$) is hyperbolic for all but finitely many $n$.
- **THM-PAPER-0098-4** (Theorem 2.1, theorem, scope: asymptotic; Sec 2, Thm 2.1 (as extracted)). The integral $F(n)=\int_{1/\sqrt N}^\infty (f(t)-f(\infty))N^{k/4}t^{k/2-1}(1+(-1)^n\epsilon)(\log N+2\log t)^n\,dt$ has a full asymptotic expansion $\sim \pi N^{k/4}(1+(-1)^n\epsilon)\,L^{n+1}\,(\cdots)\,(1+b_1/n+b_2/n^2+\cdots)$ where $L=L(n)$ is the unique positive root of an equation of Lambert type $n=L(\ldots)$ and $b_k\in\mathbb Q(L)$. This is the arbitrary-precision formula for $\Lambda^{(n)}(k/2)$.
- **THM-PAPER-0098-5** (Corollary 1.4, corollary, scope: asymptotic; Sec 4, Thm 4.1). Dirichlet L-functions of real primitive self-dual characters are good, so Thm 1.3 applies. Thm 4.1 gives an explicit expansion of $\Lambda^{(n)}(\chi,1/2)$.
- **THM-PAPER-0098-6** (Corollary 1.5, corollary, scope: asymptotic; Sec 4, Thm 4.2). For a newform $f\in S_{2k}^{new}(\Gamma_0(N))$, the modular L-function is good (Thm 4.2 gives the expansion of $\Lambda^{(n)}(f,k/2)$).
- **THM-PAPER-0098-7** (Corollary 1.6, corollary, scope: asymptotic; Sec 4, Thm 4.3). The Dedekind zeta function of a number field K is good (Thm 4.3 gives an expansion involving $2^{r_1+r_2+n+1}R(K)h_K/w_K$ and sums over ideal-class contributions $F_i(n)$).

### Principal lemmas

- **THM-PAPER-0098-L1** (Thm 2.1 / Sec 3 (asymptotic comparison); Sec 3). The expansion of $\Lambda^{(n)}$ is stable under shifts $n\mapsto n\pm j$ with relative error $O(n^{-2+\epsilon})$; this yields the quadratic-log-concavity structure of Def 1.1 and then convergence of renormalized $J^{d,n}$ to Hermite polynomials. — *Role:* core input to Thm 1.3, reproduces the GORZ pipeline in the L-function setting

### Proof architecture

Write Lambda by an integral over f split at 1/sqrt(N) via the functional equation, so derivatives at the center become integrals of (log N + 2 log t)^n against f(t)-f(infinity). Apply Laplace's method (saddle point at the Lambert-type root L(n)) to get all-order asymptotics for Lambda^(n)(k/2). Show gamma(n) is Hermite-Jensen, i.e. log gamma(n+j)/gamma(n) = A(n) j - delta(n)^2 j^2 + o(delta^d). Then the GORZ theorem [GORZ, Thm 3/Sec 5], imported, says that a Hermite-Jensen sequence has renormalized Jensen polynomials converging to H_d, whose roots are real and simple. Hence J^{d,n} is hyperbolic for n >= n0(d). Corollaries come from checking Def 1.2 for each family and computing explicit constants.

**Imported results.** Griffin-Ono-Rolen-Zagier, Jensen polynomials for the Riemann zeta function and other sequences, PNAS 2019 (Hermite-Jensen convergence criterion); Polya 1927 (equivalence of RH with hyperbolicity of all Jensen polynomials); Hermite polynomials have real simple zeros

**Techniques.** Laplace/saddle point method with Lambert-W type implicit root; Mellin/theta-function integral representation of completed L-functions; Hermite-polynomial limit of Jensen polynomials (GORZ); functional equation splitting of the integral at 1/sqrt(N)

## Context and interpretation

**Importance and obstacle overcome.** It shows the GUE-in-derivative-aspect/Hermite phenomenon is universal for the (real) Selberg-class-type completed L-functions that have a theta-integral representation. The main obstacle was producing arbitrary-precision Laplace asymptotics when the Gamma factor and conductor vary.

**Relation to prior work.** Direct extension of GORZ 2019. It was later cited by O'Sullivan (CAND-01869) and by Griffin et al. (CAND-01931) as the L-function generalization. Predecessors on Jensen polynomials: Polya 1927, Csordas-Norfolk-Varga 1986, Dimitrov-Lucas 2011.

**Limitations and open questions.** The result is purely asymptotic and ineffective: n0(d) is not bounded, so it does not touch GRH. 'Good' requires real coefficients and a theta-type representation with only exponentials e^{-pi n t}, which covers only self-dual or real cases. The remark that this 'offers evidence for GRH' has no theorem behind it, since hyperbolicity for large n holds regardless of the location of zeros of Lambda. No effective bound on n0(d), no treatment of low shifts.

## Research potential

- **Hypotheses that might be weakened.** Condition (3) (real coefficients) and the single-exponential f(t) form; this should be relaxable to general degree and non-self-dual L via the Selberg class and multiple Gamma factors. Check whether the order-of-growth relation between log gamma and n needs only order 1 growth.
- **Generalizations.** Use Wagner's Thm 2.1 together with the effective Turan-type method of Griffin et al. (CAND-01931) to get effective n0(d) for Dirichlet and modular families, and uniform in the conductor N or the weight k. Test the uniformity in N, since L=L(n,N).
- **Candidate connections.** Compare with the O'Sullivan Hermite-combination criterion (CAND-01869) for L-functions; the Laplace-method bounds are the same type as the asymptotics for Xi derivatives used in the xi-geometry and derivative descent programmes.
- **Reusable lemmas.** The general asymptotic formula for F(n) (Thm 2.1) and the explicit b_1 coefficient.
- **Possible experiments.** Numerically compute gamma(n) for a few quadratic characters and an elliptic-curve L-function via mpmath, and compare with Thm 4.1/4.2 expansions to see the true n0(d). Also check Turan and degree-3 Jensen hyperbolicity for all small n, which is the real RH-relevant region.
- **Risks / barriers.** Large-n hyperbolicity is true under RH failure as well, so it carries no information about the zeros. Any RH-relevant content needs an effective bound reaching the low-n region.

## Audit notes (Level 1 reader)

Text extraction is garbled in the proof sections, so some formulas (L(n) equation, b_k) were read only partially. In the Remark after Theorem 1.3, the claim of 'evidence for GRH' is heuristic, not a theorem. In Def 1.2 the splitting constant (epsilon N^{1/2}) and the interplay of k, N were read from lossy extraction and should be verified in the PDF. Section 3 gives error O(n^{-2+epsilon}), and I did not verify that this suffices for the o(delta^d) condition for every d.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01962`; harvest queries: kw_GRH, kw_RH_any, kw_laguerre_polya_xi, msc_11M26, arxiv_grh, arxiv_jensen_poly, arxiv_rh_abs.
- Triage decision: include — Extends Jensen-Polya program to other L-functions.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

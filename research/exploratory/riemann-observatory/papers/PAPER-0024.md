# PAPER-0024 — Jensen polynomials for the Riemann zeta function and other sequences

| Field | Value |
|---|---|
| Authors | Griffin, Michael; Ono, Ken; Rolen, Larry; Zagier, Don |
| Year / stratum | 2019 / S6 |
| Venue | Proc. Natl. Acad. Sci. USA 116, No. 23, 11103-11110 (2019). |
| Identifiers | zbMATH [1431.11105](https://zbmath.org/?q=an:1431.11105) · DOI [10.1073/pnas.1902572116](https://doi.org/10.1073/pnas.1902572116) · arXiv [1902.07321](https://arxiv.org/abs/1902.07321) |
| MSC | 11M06, 11M26, 11F03 |
| Families | C, F |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1902.07321 |
| Selection | score 4.6019, in-pool citations 24, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Polya (1927): RH iff all Jensen polynomials J_gamma^{d,n} of the Taylor coefficients gamma(n) of Xi at its centre are hyperbolic (real-rooted). Prove hyperbolicity for as many (d,n) as possible via a general Hermite-model theorem for Jensen polynomials of sequences with suitable growth.

**Historical motivation.** Polya reduced RH to real-rootedness of the Jensen polynomials of Xi; only d<=3 was known for all shifts. Random-matrix (GUE) heuristics predict Hermite behaviour in the derivative aspect; the authors prove it.

### Main results

- **THM-PAPER-0024-1** (Theorem 1, theorem, scope: asymptotic; Section 1; proof Section 5.1). For every $d\ge1$, the Jensen polynomial $J_\gamma^{d,n}(X)=\sum_{j=0}^d\binom dj\gamma(n+j)X^j$ is hyperbolic for all sufficiently large $n$ (n >= n_0(d)), where $-1+4z^2\Lambda(\tfrac12+z)=\sum_{n\ge0}\frac{\gamma(n)}{n!}z^{2n}$ and $\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$.
- **THM-PAPER-0024-2** (Theorem 2, theorem, scope: finite; Section 1; Section 5.2). If $1\le d\le8$ then $J_\gamma^{d,n}(X)$ is hyperbolic for every $n\ge0$ (effective proof of Theorem 1 for small d). *Conditional on:* computations for small n (Section 5.2, not inspected).
- **THM-PAPER-0024-3** (Theorem 3, theorem, scope: asymptotic; Section 1 (Thm 3, Corollary); Section 2). Let $\alpha(n),A(n),\delta(n)>0$ with $\delta(n)\to0$ and, for some integer $d\ge1$ and all $0\le j\le d$, $\log\frac{\alpha(n+j)}{\alpha(n)}=A(n)j-\delta(n)^2j^2+o(\delta(n)^d)$ as $n\to\infty$. Then $\lim_{n\to\infty}\frac{\delta(n)^{-d}}{\alpha(n)}J_\alpha^{d,n}\Big(\frac{\delta(n)X-1}{\exp(A(n))}\Big)=H_d(X)$ uniformly on compact subsets of $\mathbb R$, where $H_d$ are Hermite polynomials with $\sum H_d(X)t^d/d!=e^{-t^2+Xt}$ (orthogonal for $e^{-X^2/4}$). Corollary: $J_\alpha^{d,n}$ is hyperbolic for all but finitely many $n$ (Hermite roots are simple, real-rootedness is stable).
- **THM-PAPER-0024-4** (Theorem 6, theorem, scope: asymptotic; Section 2). General form: if $\frac{\alpha(n+j)}{\alpha(n)}E(n)^{-j}=\sum_{i=0}^dC_i(n)\delta(n)^ij^i+o(\delta(n)^d)$ with $C_i(n)\to c_i$, then the same limit holds with $\exp(A(n))\to E(n)$ and $H_d\to H_{F,d}$, where $F(t)=\sum c_it^i$, $\sum H_{F,m}(X)t^m/m!=F(-t)e^{Xt}$, i.e. $H_{F,m}(X)=m!\sum_{k=0}^m(-1)^{m-k}c_{m-k}X^k/k!$.
- **THM-PAPER-0024-5** (Theorem 4 (Chen-Jia-Wang conjecture), theorem, scope: asymptotic; Section 1). For every $d\ge1$ there is $N(d)$ with $J_p^{d,n}(X)$ hyperbolic for all $n\ge N(d)$, $p(n)$ the partition function. (Conjectured minimal N(d) tabulated d<=32: 1,25,94,206,381,610,908,1269,...,35627; Larson-Wagner effective bound $N(d)\le(3d)^{24d}(50d)^{3d^2}$.)
- **THM-PAPER-0024-6** (Theorem 5, theorem, scope: asymptotic; Section 1; proof Section 3). For any weakly holomorphic modular form f on SL_2(Z) (possibly fractional weight/multiplier, real Fourier coefficients, pole of positive order m at infinity), for fixed $d\ge1$ the Jensen polynomials $J_{a_f}^{d,n}(X)$ are hyperbolic for all sufficiently large n.
- **THM-PAPER-0024-7** (Theorem 7, theorem, scope: asymptotic; Section 4, Theorem 7, eq. (11)-(14) (formulas as extracted; exact displayed constants should be checked against the PDF)). With $F(n)=\int_1^\infty(\log t)^nt^{-3/4}\theta_0(t)dt$, $\theta_0(t)=\sum_{k\ge1}e^{-\pi k^2t}$, one has $\Lambda^{(n)}(\tfrac12)=-\frac{F(n)}{2^{n+2}}\,n!\,/\ldots$ as in (11) (zero for odd n), $\gamma(n)=\frac{n!}{(2n)!}\big(8^n\cdot 2^{?}\ldots\big)=\frac{n!}{(2n)!}\cdot\frac{32\,2^{2n}F(2n-2)-F(2n)}{2^{2n-1}}$-type identity (13), and $F(n)\sim\sqrt{2\pi}\,\frac{L^{n+1}}{\sqrt{(1+L)n-\tfrac34L^2}}\,e^{L/4-n/L+3/4}\big(1+\frac{b_1}{n}+\frac{b_2}{n^2}+\cdots\big)$ as $n\to\infty$, where $L=L(n)\approx\log\frac n{\log n}$ is the unique positive root of $n=L(\pi e^L+\tfrac34)$ and $b_k\in\mathbb Q(L)$ ($b_1=\frac{2L^4+9L^3+...}{...}$ as printed). Consequently $\hat\gamma(n)=\frac{n!}{(2n)!}6^{-2n}2^{2n}\hat F(2n-2)=\gamma(n)(1+O(n^{-2+\varepsilon}))$.

### Key definitions

- Jensen polynomial $J_\alpha^{d,n}(X)=\sum_{j}\binom dj\alpha(n+j)X^j$
- hyperbolic polynomial: all zeros real
- Hermite polynomials in the non-standard normalization $H_d$ orthogonal for $e^{-X^2/4}$: $H_2=X^2-2$, $H_3=X^3-6X$, $H_6=X^6-30X^4+180X^2-120$
- $\gamma(n)$: Taylor coefficients of $4z^2\Lambda(1/2+z)-1$ in $z^2$ scaled by n!
- $F(n)$, $L(n)$ (saddle point)

### Principal lemmas

- **THM-PAPER-0024-L1** (Proof of Thm 6/3; Section 2). The bracket $\sum_{i}C_i(n)\delta^{k-d+i}\sum_{j=k}^d(-1)^{j-k}\binom{d-k}{j-k}j^i\to(-1)^{d-k}(d-k)!c_{d-k}$ because the inner sum is the $(d-k)$-th finite difference of $j^i$ (zero for $i<d-k$, equal to $(d-k)!$ for $i=d-k$). — *Role:* Core of the Hermite limit theorem
- **THM-PAPER-0024-L2** ((9)-(10); Section 3). For weakly holomorphic f, $a_f(n)=A_fn^{(k-1)/2}I_{k-1}(4\pi\sqrt{mn})+O(n^Ce^{2\pi\sqrt{mn}})$ (Rademacher/Poincare series); log of ratio $a_f(n+j)/a_f(n)$ has asymptotic expansion with $A(n)=2\pi\sqrt{m/n}+O(1/n)$, $\delta(n)=(\pi/2)^{1/2}m^{1/4}n^{-3/4}+O(n^{-5/4})$. — *Role:* Verifies hypotheses of Theorem 3 for modular coefficients
- **THM-PAPER-0024-L3** (Proof of Thm 7; Section 4). Saddle point at $t=a=e^L$ solving $n=\pi a+\tfrac34\log a$ for $f(t)=(\log t)^nt^{-3/4}e^{-\pi t}$; expansion $f((1+\lambda)a)/f(a)=e^{-C\lambda^2/2}(1+A_3\lambda^3+A_4\lambda^4+\cdots)$, $C=(\varepsilon+\varepsilon^2)n-\tfrac34$, $\varepsilon=1/\log a$; ratio $f/\theta_0=1+O(n^{-K})$ near a. — *Role:* Gives all-orders asymptotics for the central derivatives of Lambda
- **THM-PAPER-0024-L4** ((15)-(18); Section 5.1). With $\hat n=2n-2$, $L=L(\hat n)$, $K=(L^{-1}+L^{-2})\hat n-3/4$, Stirling plus Thm 7 yields (16); expanding $\log R(j;n)=\sum g_m(n)j^m$ one gets $g_m(n)=O((n-1)^{1-m})$ and the choices $\delta(n)=\sqrt{1/\hat n-2/(L^2K)}$-type and $A(n)=\log\frac{nL^2}{4\hat n^2}+\ldots$ (18) satisfy (15) with $g_i(n)=o(\delta^i)$ for $i\ge3$. — *Role:* Verification of the hypothesis of Theorem 3 for gamma(n), every d

### Proof architecture

Section 2: purely formal proof that, if log(alpha(n+j)/alpha(n)) is quadratic in j to order o(delta^d), the rescaled Jensen polynomial converges coefficientwise to Hermite H_d (Theorem 3 as special case F=e^{-t^2} of Theorem 6); Hermite roots simple so hyperbolicity persists for large n. Section 3: applies Thm 3 to coefficients of weakly holomorphic modular forms using Rademacher-type Bessel asymptotics (gives Theorem 5, hence CJW conjecture Thm 4 via f=1/eta). Section 4: writes gamma(n) via F(2n-2),F(2n), derives all-order asymptotic of F by saddle point (Thm 7). Section 5.1: Stirling + Thm 7 give (16), compute g_1,g_2, define A(n),delta(n) and check Thm 3's hypothesis for every d; Section 5.2: effective version for d<=8 (Thm 2). Section 6: numerics showing convergence of J_gamma^{3,n},J_gamma^{6,n} to Hermite.

Dependency edges: CAND-01793 → Polya 1927 (tests the RH-equivalent criterion in derivative aspect); CAND-01793 → Csordas-Norfolk-Varga 1986 (extends d<=3 to d<=8 and every d for large n); CAND-01793 → Chen-Jia-Wang (proves their conjecture)

**Imported results.** Polya 1927 (RH iff hyperbolicity of all J_gamma^{d,n}); Csordas-Varga 1990; Csordas-Norfolk-Varga 1986, Dimitrov-Lucas 2010 (d<=3); Coffey 2009 and Pustyl'nikov 2001 (earlier asymptotics of Xi^{(2n)}(1/2)); Chasse 2011 Thm 1.8 (J_gamma^{d,0} hyperbolic for d<=2*10^17); Rademacher-Poincare series asymptotics for modular coefficients; Larson-Wagner effective bound for partition Jensen polynomials; Riemann's theta integral representation of Lambda

**Techniques.** Hermite-polynomial limit of Jensen polynomials; finite differences; saddle point method to all orders; Rademacher/Hardy-Ramanujan asymptotics for Fourier coefficients; Stirling expansion; Hermite's criterion for effective hyperbolicity

## Context and interpretation

**Importance and obstacle overcome.** Proves a large partial case of the Polya/Jensen criterion: for each fixed d, all but finitely many shifts n are hyperbolic, plus all n for d<=8, and identifies the GUE/Hermite limit rigorously. The obstacle was an all-orders asymptotic (Thm 7) of gamma(n) precise enough that log gamma(n+j)/gamma(n) is quadratic up to o(delta^d) for every d, and the realization that this single condition forces Hermite behaviour.

**Relation to prior work.** 

**Limitations and open questions.** Result is for fixed d and n>=n_0(d) with ineffective (Thm 1) threshold; RH needs all d at n=0 (equivalently all d and large n would give hyperbolicity of derivatives only if one could pass from large n down to n=0, which requires effectiveness uniform in d). Hermite model at shift n is insensitive to the location of finitely many zeros. No new test for d>8 at small n.

## Research potential

- **Hypotheses that might be weakened.** Theorem 3 hypothesis (quadratic-log expansion to o(delta^d)): the same machinery with delta(n) depending on d and n jointly (uniform in d<=D(n)) would give an effective version; the most valuable target is a threshold n_0(d) polynomial in d, which for d~n would approach RH via Chasse-type n=0 checks.
- **Generalizations.** Hermite model for Jensen polynomials of Taylor coefficients at other centres (Xi(1/2+z) around z=iT, i.e. Jensen polynomials 'at height T', Griffin-Ono-Rolen-Zagier-style follow-ups) and for Dirichlet L-functions / modular L-functions Lambda(s,f); also Theorem 6 with non-Gaussian F (different c_i) for other sequence families.
- **Candidate connections.** De Bruijn-Newman constant Lambda>=0 (Rodgers-Tao) and the heat-flow picture: Jensen polynomials relate to the heat flow of Xi; hyperbolicity of J^{d,n} for large n is a statement about derivative-aspect zeros, linking to the 'full-source operators and heat' programme and to Turan inequalities (Dimitrov-Lucas); Hermite polynomial limit is also the GUE derivative-aspect prediction (Katz-Sarnak, Montgomery-Odlyzko).
- **Reusable lemmas.** Theorem 6 (formal Hermite-limit lemma via finite differences) is fully reusable for any positive sequence with an asymptotic expansion; Theorem 7's saddle-point expansion for F(n)=int_1^inf (log t)^n t^{-3/4} theta_0(t)dt gives explicit gamma(n) asymptotics usable for effective Turan inequalities of all orders.
- **Possible experiments.** Compute the actual minimal n_0(d) for d up to ~30 for gamma(n) (analogue of the table N(d) for partitions, which grows ~10 d^2 log d) with high-precision interval arithmetic and compare with Hermite prediction; check at which n the degree-d renormalized polynomial's roots leave the Hermite roots' neighbourhood; test the Hermite model for shifted Xi(1/2+iT+z).
- **Risks / barriers.** Theorem 1 is ineffective in n_0(d) and does not reach n=0; Hermite stability argument gives no information on RH itself. Non-uniform in d, so no route to RH without an effectiveness-in-d breakthrough.

## Audit notes (Level 1 reader)

Several displayed formulas in Theorem 7 and (13), (18) are scrambled in the text extraction (e.g. b_1 numerator, the exact constants in (11), (13)); statements above for those are marked 'as printed/as extracted' and should be re-checked against the PDF before use. Footnote 1: Chasse's d<=2*10^17 refers to J_gamma^{d,0}. Section 5.2 (effective d<=8 proof) was not inspected. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01793`; harvest queries: kw_RH_any, kw_laguerre_polya_xi, msc_11M06, msc_11M26, arxiv_jensen_poly, arxiv_random_matrix_zeta, arxiv_rh_abs.
- Triage decision: include — Jensen polynomial hyperbolicity for Polya criterion; asymptotic evidence.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

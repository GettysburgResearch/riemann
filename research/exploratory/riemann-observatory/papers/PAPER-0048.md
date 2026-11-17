# PAPER-0048 — Zero-free regions for Dirichlet \(L\)-functions and the least prime in an arithmetic progression

| Field | Value |
|---|---|
| Authors | Heath-Brown, D. R. |
| Year / stratum | 1992 / S4 |
| Venue | Proc. Lond. Math. Soc., III. Ser. 64, No. 2, 265-338 (1992). |
| Identifiers | zbMATH [0739.11033](https://zbmath.org/?q=an:0739.11033) · DOI [10.1112/plms/s3-64.2.265](https://doi.org/10.1112/plms/s3-64.2.265) |
| MSC | 11N13, 11M26 |
| Families | A, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://typeset.io/pdf/zero-free-regions-for-dirichlet-l-functions-and-the-least-4qczj8tg0n.pdf |
| Selection | score 4.5622, in-pool citations 39, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** How wide can one make zero-free regions (near s=1, |t|<=1) for the family of Dirichlet L-functions modulo q, allowing for an exceptional (Siegel/Landau) zero, and how far can this improve Linnik's constant L in P(a,q) << q^L? Combines Burgess character-sum bounds, an improved partial-fraction inequality, an optimized positive-definite test-function (calculus of variations) argument, and a new zero-density estimate.

**Historical motivation.** Linnik's 1944 theorem P(a,q)<<q^L with many successive numerical reductions of L (Table 1: 10000 Pan 1957 down to 13.5 Chen-Liu 1989); GRH gives 2+eps. Improving the zero-free region constants (Gronwall/Landau/Titchmarsh c_1, Schoenfeld 0.10367, Graham 0.2069) and Deuring-Heilbronn exponents.

### Main results

- **THM-PAPER-0048-1** (Theorem 1, theorem, scope: asymptotic; Sec. 1, p.4). For q sufficiently large, $\prod_{\chi \bmod q}L(s,\chi)$ has at most one zero in $\sigma\ge 1-\frac{0.348}{\log q},\ |t|\le 1$; such a zero is real, simple, and belongs to a non-principal real character.
- **THM-PAPER-0048-2** (Theorem 2, theorem, scope: asymptotic; Sec. 1, p.4). For q large, $\prod_\chi L(s,\chi)$ has at most 2 zeros (with multiplicity) in $\sigma\ge1-\frac{0.696}{\log q},|t|\le1$; moreover there is a character $\chi_1$ such that $L(s,\chi)\ne0$ for $\sigma\ge 1-\frac{0.702}{\log q},|t|\le1$ for all $\chi\ne\chi_1,\bar\chi_1$.
- **THM-PAPER-0048-3** (Theorem 3, theorem, scope: asymptotic; Sec. 1, p.4). For q large there are $\chi_1,\chi_2$ such that $L(s,\chi)\ne0$ for $\sigma\ge1-\frac{0.857}{\log q},|t|\le1$ for all $\chi\notin\{\chi_1,\bar\chi_1,\chi_2,\bar\chi_2\}$. (Author notes 0.857 is $6/7+o(1)$.)
- **THM-PAPER-0048-4** (Theorem 4 (Deuring-Heilbronn repulsion), theorem, scope: asymptotic; Sec. 1, p.4-5). Let $\varepsilon>0$, $\chi$ real non-principal mod q with $L(1-\lambda/\log q,\chi)=0$, $\lambda\le0.348$. For q large, $\prod_\chi L(s,\chi)$ has only the zero $s=1-\lambda/\log q$ in $\sigma\ge1-\min\{(\tfrac{12}{11}-\varepsilon)\log\lambda^{-1},\tfrac13\log\log\log q\}/\log q$ (with $|t|\le 1$ as in the preceding theorems; the exact range of $t$ was not re-verified in the extracted text).
- **THM-PAPER-0048-5** (Theorem 5 (zero density), theorem, scope: asymptotic; Sec. 1, p.5; proved Sec. 11-13). Let $N(\lambda)$ be the number of L-functions mod q with a zero in $\sigma\ge1-\lambda/\log q,|t|\le1$. For $\varepsilon>0$, q large, $\lambda\le\frac13\log\log\log q$: $N(\lambda)\le(1+\varepsilon)\frac{67}{6\lambda}\big(e^{73\lambda/30}-e^{16\lambda/15}\big)$.
- **THM-PAPER-0048-6** (Theorem 6 (Linnik constant), theorem, scope: global; Sec. 1, p.5; proof Sec. 15). $P(a,q)\ll q^{5.5}$ for $(a,q)=1$, with effectively computable implied constant (improving 13.5 of Chen-Liu).

### Key definitions

- L=log q
- exceptional zero $\rho_1=1-\lambda_1/\log q$ of real character $\chi_1$
- $\lambda_0,\lambda_2,\lambda_3$: scaled distances of next zeros
- N(lambda): number of L-functions mod q with a zero in sigma>=1-lambda/log q, |t|<=1
- P(a,q): least prime in progression a mod q

### Principal lemmas

- **THM-PAPER-0048-L1** (Lemma 2.1-2.4; Sec. 2). Burgess bounds $\sum_{N<n\le N+H}\chi(n)\ll q^{(k+1)/(4k^2)+\varepsilon}H^{1-1/k}$ (k=2,3, or any k if q cube-free), extended to non-cube-free moduli via Lemma 2.3 (factor v = cube-full part) and Lemma 2.4 (dependence on order of chi). — *Role:* Imports Burgess into zero-free region analysis; yields the smaller constant phi in Lemma 2.5 / 3.1.
- **THM-PAPER-0048-L2** (Lemma 3.1; Sec. 3). For non-principal chi mod q and phi as in Lemma 2.5, $-\Re\frac{L'}{L}(s,\chi)\le-\sum_{|1+it-\rho|\le\delta}\Re\frac1{s-\rho}+(\frac{\phi}{2}+\varepsilon)\log q$ uniformly for $1+\frac1{L\log L}\le\sigma\le1+\frac{\log L}{L}$, $|t|\le L=\log q$, q large. — *Role:* Replaces the 1/2 L term in the standard inequality (3.2) (and Stechkin's 0.2764) by phi/2 with phi=1/6 or 1/8 via Burgess; discarding only nearby zeros.
- **THM-PAPER-0048-L3** (Lemma 6.1; Sec. 6). For q large there is an integer $L'\le\frac{3}{10}...$ (extracted text garbled: some $\mathcal L\le \frac{4}{5}$-type bound on an auxiliary height parameter) such that no $L(s,\chi)$, $\chi$ mod q, vanishes in $1-\frac{\log\log\mathcal L}{3\mathcal L}\le\sigma\le1,\ \mathcal L<|t|\le10\mathcal L$. — *Role:* Pigeonhole via Jutila's density bound $\sum_\chi N(\sigma,T,\chi)\ll_\varepsilon (qT)^{(2+\varepsilon)(1-\sigma)}$ to clear a window of heights; imports Jutila.
- **THM-PAPER-0048-L4** (Lemmas 6.2-6.4; Sec. 6). Positivity inequalities for test function f (conditions 1,2) with F its transform: e.g. Lemma 6.2: $F(-\lambda_1)-F(0)-F(\lambda_2-\lambda_1)+f(0)(\psi+\varepsilon)\ge0$; Lemma 6.3 (chi_1, rho_1 real): $2F(-\lambda_0)-2F(\lambda_1-\lambda_0)-F(0)+f(0)(\tfrac14+\varepsilon)\ge0$. — *Role:* Generalized Stechkin/Landau-type positivity ($1+\chi(n)$ times $1+\Re\chi(n)n^{-i\gamma'}$) arguments that bound distance between zeros; the constants theorems 1-4 come from optimizing f.
- **THM-PAPER-0048-L5** (Lemmas 7.1-7.4; Sec. 7). Explicit optimal choice of f (calculus of variations) in several parameter regimes theta in (0,pi/2), =0 limit, hyperbolic, and (pi/2,pi). — *Role:* Makes the optimization of the test function explicit; reduces constants to numerical computation.
- **THM-PAPER-0048-L6** (Lemma 8.2; Sec. 8). For chi_1, rho_1, rho_0 real: $\lambda_0\ge2.427\ldots$ (Pintz obtains 4+o(1) by a different method). — *Role:* Quantitative Deuring-Heilbronn repulsion between the exceptional zero and next real zero.
- **THM-PAPER-0048-L7** (Lemma 10.3; Sec. 10). If q sufficiently large then $\lambda_3\ge\frac67-\varepsilon$. — *Role:* Source of the 6/7 behind Theorem 3's 0.857.
- **THM-PAPER-0048-L8** (Lemma 15.1; Sec. 15). For $\lambda_1\ge0.384$ a bound for $K-2\sum_{\chi\ne\chi_0}\sum_{\rho}|F((1-\rho)L)|$ in terms of zero-density counts $N_0(\Lambda_r)$ and constants C(.), used with L=5.5, K=0.3. — *Role:* Final numerical verification step in the Linnik-constant argument: the exponent 5.5 appears as the parameter L of the argument.

### Proof architecture

Standard Linnik three-principle framework (single exceptional zero; Deuring-Heilbronn repulsion; log-free zero density). Sections: 2 Burgess bounds with extension to non-cube-free moduli; 3 improved inequality for -Re L'/L using Burgess to reduce the 1/2 log q constant to phi/2; 4-5 zero-free regions via derivatives of L'/L and Dirichlet-polynomial/smoothing approximations; 6 positivity inequalities with a test function, producing constraints on lambda_0, lambda_1, lambda_2, lambda_3 (positions of first few zeros); 7 optimization of the test function; 8-10 numerical solution in the real/complex cases yielding Theorems 1-4 (constants 0.348, 0.696, 0.702, 0.857); 11-13 new zero-density estimate (Theorem 5) combining Burgess-improved bounds with the earlier Graham estimate form; 14-15 application to Linnik: if exceptional zero small (lambda<=lambda(eps)) imports Heath-Brown [14] giving q^{3+eps}; otherwise the new zero-free/density information gives q^{5.5} by a weighted sum over zeros with explicit tables. Imported: Burgess, Jutila's density theorem, Heath-Brown [14] effective result for small lambda, Chen/Graham density forms, Gronwall-Landau-Titchmarsh.

Dependency edges: Burgess bounds (Lemma 2.1-2.4) → Lemma 3.1 (phi/2 constant) (input); Lemma 3.1 → Theorems 1-4 (input); Theorems 1-4 and Theorem 5 → Theorem 6 (input); Jutila density → Lemma 6.1 (imported)

**Imported results.** Burgess (1957, 1962) character sum bounds; Jutila 1977 log-free-type zero density $(qT)^{(2+\varepsilon)(1-\sigma)}$ for $4/5\le\sigma\le1$; Heath-Brown 1990 (effective) P(a,q)<<q^{3+eps} when exceptional zero lambda<=lambda(eps); Graham zero-density and Deuring-Heilbronn with c_2<3/2; Pintz (real zeros of single real L-function: c_1=4+o(1))

**Techniques.** Burgess character sum bounds; Turan/Stechkin/Landau positivity (3+4cos+cos2 type) with general test functions; Partial-fraction (Hadamard) formula for L'/L; Deuring-Heilbronn zero repulsion; zero-density estimates, Jutila pigeonholing; calculus of variations for optimal test function; computer-assisted numerical optimization (tables 8-13)

## Context and interpretation

**Importance and obstacle overcome.** Best known Linnik exponent (5.5) for decades, until later work (Xylouris 5 in 2011, via different zero-density/Deuring-Heilbronn improvements). Key obstacle: previous authors could not bring Burgess's subconvex-type bounds into the zero-free region argument; here done via modifying the constant 1/2 L in the L'/L inequality (Lemma 3.1) and optimizing the test function.

**Relation to prior work.** Improves Chen-Liu 13.5, Graham 20/36, Jutila, Chen; zero-free constants improve Schoenfeld 0.10367 / Graham 0.2069 / 0.2769; Theorem 5 improves Chen's N(lambda) bound; Iwaniec/Hooley partial conditional bounds mentioned.

**Limitations and open questions.** Result is unconditional and effective but far from GRH exponent 2+eps; author states numerics are not rigorously error-analyzed (rounding/truncation). Cube-free moduli could be improved (Burgess) but is not done. Pintz's c_1=4 suggests the constants in Theorems 1-3 are improvable. Zero-free regions are only width O(1/log q) near s=1, |t|<=1 (not RH-strength).

## Research potential

- **Hypotheses that might be weakened.** The 'sufficiently large q' threshold is not made explicit; making it explicit with rigorous interval arithmetic would give a certified version. Restricting to cube-free q would allow all k in Burgess (Lemma 2.1).
- **Generalizations.** Replace Burgess by subconvexity (Weyl-type) bounds for Dirichlet L-functions to improve phi in Lemma 3.1; apply the same test-function/positivity machinery to automorphic L-functions or to Linnik-type problems for GL_2.
- **Candidate connections.** Quantitative zero repulsion near s=1 feeds Siegel-zero/class number lower bounds; relation to Pintz's alternative c_1=4 and later Xylouris improvements.
- **Reusable lemmas.** Lemma 3.1 (shortened -Re L'/L inequality), Lemma 6.1 (Jutila pigeonhole window), Lemmas 6.2-6.4 + 7.x (positivity inequalities with optimal test function).
- **Possible experiments.** Rerun the Sec. 7-10 optimization (the LP/variational problems giving 0.348, 0.696, 0.857) in rigorous interval arithmetic to authenticate the constants; vary the Burgess constant phi in {1/2,1/6,1/8,1/12} to see sensitivity of Theorem 1's 0.348.
- **Risks / barriers.** Siegel zero cannot be excluded; any improvement is bounded by the unconditional exceptional-zero obstruction. Heavy numerical computations unverified.

## Audit notes (Level 1 reader)

Sec. 1 (p.6): author explicitly says numerical computations are not reproduced and no rigorous rounding/truncation analysis was done, so constants 0.348, 0.696, 0.857, 5.5 rest on unauthenticated floating-point optimization. Lemma 6.1 statement was garbled in extracted text, so its exact bound on the auxiliary parameter was not captured. The text also notes Theorem 6 relies on [14] for small-lambda case.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00740`; harvest queries: kw_weil_positivity, kw_zero_density, msc_11M26.
- Triage decision: include — Zero-free regions for Dirichlet L, Siegel zero, Linnik constant.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

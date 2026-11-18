# PAPER-0022 — Autocorrelation of ratios of \(L\)-functions

| Field | Value |
|---|---|
| Authors | Conrey, Brian; Farmer, David W.; Zirnbauer, Martin R. |
| Year / stratum | 2008 / S5 |
| Venue | Commun. Number Theory Phys. 2, No. 3, 593-636 (2008). |
| Identifiers | zbMATH [1178.11056](https://zbmath.org/?q=an:1178.11056) · DOI [10.4310/CNTP.2008.v2.n3.a4](https://doi.org/10.4310/CNTP.2008.v2.n3.a4) · arXiv [0711.0718](https://arxiv.org/abs/0711.0718) |
| MSC | 11M06, 11M26, 11M50 |
| Families | B, E |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/0711.0718 |
| Selection | score 4.6055, in-pool citations 66, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Formulate, via a refined 'recipe' for all main terms (harmonic detector, approximate functional equations, diagonal retention), conjectures for averages over families of ratios of products of L-functions with shifts (unitary: zeta/t-family; symplectic: $L(s,\chi_d)$; orthogonal: families of Hecke/tau twists), compare with theorems for ratios of characteristic polynomials over $U(N)$, $USp(2N)$, $SO(2N)$, $SO(2N+1)$, and derive applications (moments of $\zeta'/\zeta$, Keating-Snaith ratio moments, sums over zeros $\zeta(\rho+a)/\zeta(\rho+c)$).

**Historical motivation.** Farmer's ratio conjecture (1.1), originally from long-mollifier work, implied Montgomery pair correlation, Levinson, and Hejhal/Rudnick-Sarnak triple correlation; the matching RMT identity was found by Nonnenmacher-Zirnbauer (1999) so a general conjecture for ratios over all classical groups and families was formulated.

### Main results

- **THM-PAPER-0022-1** (Theorem 4.1 (quoted from [7],[20]), theorem (RMT, imported), scope: finite; Sec 4, eq (4.4)-(4.6), p.~9). If $N\ge\max\{Q-K,R-L\}$ and $\Re\gamma_q,\Re\delta_r>0$: $\int_{U(N)}\frac{\prod_{k=1}^K\Lambda_A(e^{-\alpha_k})\prod_{\ell=K+1}^{K+L}\Lambda_{A^*}(e^{\alpha_\ell})}{\prod_{q=1}^Q\Lambda_A(e^{-\gamma_q})\prod_{r=1}^R\Lambda_{A^*}(e^{-\delta_r})}dA=\sum_{\sigma\in\Xi_{K,L}}e^{N\sum_{k=1}^K(\alpha_{\sigma(k)}-\alpha_k)}y_U(\alpha_{\sigma(1)},\dots,\alpha_{\sigma(K)};-\alpha_{\sigma(K+1)},\dots,-\alpha_{\sigma(K+L)};\gamma;\delta)$, with $y_U(\alpha;\beta;\gamma;\delta)=\frac{\prod_{k,\ell}z(\alpha_k+\beta_\ell)\prod_{q,r}z(\gamma_q+\delta_r)}{\prod_{k,r}z(\alpha_k+\delta_r)\prod_{\ell,q}z(\beta_\ell+\gamma_q)}$, $z(x)=1/(1-e^{-x})$, $\Xi_{K,L}$ the set of $\binom{K+L}K$ permutations preserving the order within the first K and the last L.
- **THM-PAPER-0022-2** (Theorems 4.2, 4.3, 4.4 (quoted), theorem (RMT, imported), scope: finite; Sec 4, p.~9-11). Symplectic $USp(2N)$ (needs $2N\ge Q-K-1$), odd orthogonal $SO(2N+1)$ ($2N\ge Q-K+1$) and even orthogonal $SO(2N)$ ($2N\ge Q-K$) analogues of Theorem 4.1, each a sum over $\epsilon\in\{\pm1\}^K$ with sign factors $\mathrm{sgn}(\epsilon)$ and reflected shifts $\epsilon_k\alpha_k$ (with $\Re\gamma_q>0$).
- **THM-PAPER-0022-3** (Conjecture 5.1, conjecture (ratios conjecture, zeta), scope: conditional; Sec 5.1, eq (5.15), p.14). If $\Re\gamma_q,\Re\delta_r>0$ and $\Re\alpha_j>-\frac1{2(K+L)}$: $\int_0^T\frac{\prod_{k=1}^K\zeta(s+\alpha_k)\prod_{\ell=K+1}^{K+L}\zeta(1-s-\alpha_\ell)}{\prod_q\zeta(s+\gamma_q)\prod_r\zeta(1-s+\delta_r)}dt=\int_0^T\sum_{\sigma\in\Xi_{K,L}}\prod_{k=1}^K\frac{\chi(s+\alpha_k)}{\chi(s-\alpha_{\sigma(k)})}Y_UA_\zeta(\alpha_{\sigma(1)},\dots;-\alpha_{\sigma(K+1)},\dots;\gamma;\delta)\,dt+O(T^{1/2+\epsilon})$, with $Y_U=\frac{\prod\zeta(1+\alpha_k+\beta_\ell)\prod\zeta(1+\gamma_q+\delta_r)}{\prod\zeta(1+\alpha_k+\delta_r)\prod\zeta(1+\beta_\ell+\gamma_q)}$ and $A_\zeta$ the Euler product (5.14) absolutely convergent near 0 (with Corollary 6.2: closed form of $A_\zeta$ as $\prod_p\int_0^1\ldots d\theta$ via Lemma 6.1). *Conditional on:* unproved ratios conjecture.
- **THM-PAPER-0022-4** (Conjectures 5.2, 5.3, 5.4, conjecture, scope: conditional; Sec 5.2-5.3, p.~17-20 (lines ~899, 1070, 1094)). Ratios conjectures for the symplectic family $L(1/2+\alpha,\chi_d)$, and the orthogonal families (even/odd, e.g. twists by weight-k Hecke forms), with sums over $\epsilon\in\{\pm1\}^K$ of $\prod_k (\text{conductor ratio})^{-\ldots}$, $Y$-factor and arithmetic factor $A$, error $O(X^{1/2+\epsilon})$, for $\Re\alpha_k,\Re\gamma_q>0$. *Conditional on:* unproved.
- **THM-PAPER-0022-5** (Lemma 6.1 / Corollary 6.2, lemma/identity (proved), scope: finite; Sec 6.1, eq (6.2)). For $e(\theta)=e^{2\pi i\theta}$: $\sum_{\sum a_k+\sum c_q=\sum b_\ell+\sum d_r}\prod\ldots p^{-\ldots}\mu(p^{c_q})\mu(p^{d_r})=\int_0^1\frac{\prod_q(1-e(\theta)p^{-1/2-\gamma_q})\prod_r(1-e(-\theta)p^{-1/2-\delta_r})}{\prod_k(1-e(\theta)p^{-1/2-\alpha_k})^{-1}\ldots}d\theta$ (as printed, schematic), yielding the local factor of $A_\zeta$ as an integral over the circle.
- **THM-PAPER-0022-6** (Lemmas 6.7, 6.8, lemma, scope: finite; Sec 6.4, p.~25-30 (lines ~1368, 1483)). Lemma 6.7: if $F(z;w)$ is regular near $0$, symmetric in the first $K$ and in the last $L$ variables, $f$ has a simple pole of residue 1 at 0 and is otherwise analytic in $|s|\le1$, and $H=F\prod_{k,\ell}f(z_k-w_\ell)$, then the permutation sum $\sum_{\sigma\in\Xi_{K,L}}H(\alpha_{\sigma(1)},\dots)$ equals a multiple contour integral (rewriting the combinatorial sum as a K+L fold contour integral, Section 6.4). Lemma 6.8 is the all-$K$ symmetric version.
- **THM-PAPER-0022-7** (Conjecture 7.1, conjecture (consequence), scope: conditional; Sec 7.1, eq (7.12)-(7.13), p.~38). Assuming the ratios conjecture: $\frac1T\int_0^T\Big(\frac{\zeta'}{\zeta}(1/2+r+it)\Big)^2dt=\Big(\frac{\zeta'}{\zeta}\Big)'(1+2r)+\Big(\frac T{2\pi}\Big)^{-2r}A_\zeta(-r,-r,r,r)\frac{\zeta(1-2r)\zeta(1+2r)}{1-2r}+c(r)+O(T^{-1/2+\epsilon})$ (scaled form as printed with $\frac Tte$ factor), $c(r)$ uniformly bounded for $|r|<1/4-\epsilon$ and given by an explicit prime sum (7.13).
- **THM-PAPER-0022-8** (Conjecture 7.2, conjecture (consequence), scope: conditional; Sec 7.4, eq near line 1882-1900, p.~39). For $a,c$ with nonnegative real part and $|a|,|c|\gg(\log T)^{-1}$: $\frac1T\sum_{\gamma<T}\frac{\zeta(\rho+a)}{\zeta(\rho+c)}=\frac1T\int_0^T\Big[\frac1{2\pi}\log\frac t{2\pi}+\frac{\zeta'}\zeta(1+a)-\frac{\zeta'}\zeta(1+c)-\sum_p\frac{\log p}{p^{2+a+c}}\ldots-\Big(\frac t{2\pi}\Big)^{-a}\frac{\zeta(1-a)\zeta(1+c)}{\zeta(1+c-a)}\prod_p\ldots\Big]dt$ (printed with an explicit Euler product; extraction partial).

### Key definitions

- $\Xi_{K,L}$: subset of permutations $\sigma$ of $\{1..K+L\}$ with $\sigma(1)<\dots<\sigma(K)$, $\sigma(K+1)<\dots<\sigma(K+L)$
- $z(x)=1/(1-e^{-x})$
- $Y_U$, $A_\zeta$
- characteristic polynomial $\Lambda_A(s)=\det(I-sA^*)$

### Principal lemmas

- **THM-PAPER-0022-L1** (Recipe Sec 5 steps (5.7)-(5.14); Sec 5.1, p.12-14). Approximate functional equation for each numerator zeta; multiply out the $2^{K+L}$ terms; retain terms with equal numbers of $\chi(s)$ and $\chi(1-s)$; Mobius expansion for denominators ($\Re$ shifts positive); keep diagonal; express resulting arithmetic sum as Euler product $G_\zeta=Y_UA_\zeta$. — *Role:* Derivation of Conjecture 5.1.
- **THM-PAPER-0022-L2** (Orthogonality / harmonic detector (3.6); Sec 3.1, eq (3.6)). $\lim_{T\to\infty}\frac1T\int_0^T(m/n)^{it}dt=1$ if $m=n$, $0$ otherwise (analogues for $\chi_d$ and Hecke twists in Sec 3). — *Role:* Selecting diagonal terms in the recipe.
- **THM-PAPER-0022-L3** (Theorem 4.1-4.4 (RMT); Sec 4). Exact finite-$N$ ratios theorems for $U(N)$, $USp(2N)$, $SO(2N)$, $SO(2N+1)$ (proved in companion papers CFZ [7] via supersymmetry and Conrey-Forrester-Snaith/ Bump-Gamburd [20]). — *Role:* Template and consistency check for the L-function conjectures with $N\leftrightarrow \log(T/2\pi)$ or $\log(|d|/\pi)$ conductor substitution.

### Proof architecture

Mostly heuristic. Sec 2-3: groups and families; Sec 4: RMT ratio theorems (quoted); Sec 5: recipe generalizing CFKRS (harmonic detector -> diagonal -> Euler product factoring) giving conjectures 5.1-5.4 with error $O(X^{1/2+\epsilon})$ or $O(T^{1/2+\epsilon})$; Sec 6: refinements (closed form of the arithmetic factor via integrals over the circle (Lemma 6.1, Cor 6.2), tests for $p=11$ (Lemma 6.5, Cor 6.6), conversion of the $\binom{K+L}K$-term combinatorial sum into multiple contour integral via Lemmas 6.7-6.8); Sec 7: applications (mean square of $\zeta'/\zeta$ near the critical line, Keating-Snaith conjecture about $\zeta(1/2+it)^K/\zeta(1/2-it)^K$, discrete sums over zeros, autocorrelation).

**Imported results.** Ratios theorems for $U(N),USp(2N),SO(N)$ [7] and [20] (Conrey-Farmer-Zirnbauer RMT; Bump-Gamburd-type proofs); Farmer's conjecture (1.1) [13]; Goldston-Montgomery equivalence of pair correlation and second moment of primes [18]; Keating-Snaith conjecture (7.14); Hughes-Keating-O'Connell

**Techniques.** CFKRS recipe for ratios; Permutation sums over $\Xi_{K,L}$; Euler product factoring of arithmetic factor; Contour integral representation of combinatorial sums; Supersymmetry (companion) for RMT ratios

## Context and interpretation

**Importance and obstacle overcome.** Provides the general ratios conjecture (the source of subsequent ratios-conjecture literature: one-level density lower-order terms, Conrey-Snaith correlations, Sarnak-Zaharescu/Miller type studies) and a closed form for the arithmetic factor. Key obstacle: guaranteeing consistency of the formula under functional equation symmetries and parameter exchanges; solved by the permutation structure $\Xi_{K,L}$ and unified RMT comparison.

**Relation to prior work.** Extends the CFKRS recipe for moments (no denominators) to ratios; companion to Conrey-Farmer-Zirnbauer 'Howe pairs, supersymmetry, and ratios of random characteristic polynomials' (RMT proof); used in Conrey-Snaith applications (CAND-01202) and n-level correlation (CAND-01253).

**Limitations and open questions.** All L-function results are conjectural; the error exponent 1/2+eps is heuristic; the restriction $\Re\alpha_j>-1/(2(K+L))$ and positivity of denominator shifts' real parts are heuristic domain assumptions; non-equal-length families and non-self-dual L-functions not treated in this version; mollified moments etc. deferred to applications paper.

**Ideas in remarks/appendices/abandoned paths.** Sec 6 (Lemma 6.5/Corollary 6.6) explicit test at the prime $p=11$ for the family of twists of the weight 12? modular form (actually $\Delta$): shows how local arithmetic factor is computed in a specific orthogonal family (not read in detail); Sec 7 exhibits ratios conjecture derivations of Keating-Snaith ratio moment (7.14).

## Research potential

- **Hypotheses that might be weakened.** The positivity $\Re\gamma_q,\Re\delta_r>0$ used for absolute convergence of the Mobius series (extend by analytic continuation as in Remark of CAND-01202 Rem 2.2); the shift lower bound $-1/(2(K+L))$.
- **Generalizations.** Number field and function field families where the ratios conjecture is provable (Andrade-Keating); more than one-parameter families; non-unitary groups (Sp, SO even/odd refinements, Conjectures 5.2-5.4) and 'other symmetry' families such as $GL(3)$.
- **Candidate connections.** Conjecture 7.1 ($\zeta'/\zeta$ mean square) relates to Goldston-Montgomery on primes in short intervals and to the pair correlation; Conjecture 7.2 gives discrete averages that bear on simple zeros/Mertens-type questions.
- **Reusable lemmas.** Lemma 6.1 (circle-integral formula for the Euler factor) and Lemmas 6.7-6.8 (permutation sum to contour integral) are reusable in any proof or heuristic that needs to evaluate sums over $\Xi_{K,L}$.
- **Possible experiments.** Numerically test Conjecture 7.1 for $r$ in $(0,0.25)$ and Conjecture 7.2 using Odlyzko tables; test Conj 5.1 for $(K,L,Q,R)=(1,1,1,1)$ with $T\sim10^{6}$ numerically compared with Farmer (1.1).
- **Risks / barriers.** No rigorous route to Conj 5.1 for ratios beyond short mollifiers; off-diagonal terms are ignored in the recipe; RMT agreement is evidence not proof.

## Audit notes (Level 1 reader)

Extraction shows an odd '(4.4)' denominator index 'r+1' (r=1) in Theorem 4.1 as an OCR artifact (denominator should be $\prod_{r=1}^R\ldots$); text extraction of Conjecture 7.1 is missing a factor in the second term (displayed as $T/2\pi$ rather than exact power). Otherwise none noticed in inspected portion. Proofs of Thms 4.1-4.4 not read in this paper (they are quoted).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01203`; harvest queries: kw_RH_any, kw_moments_zeta, msc_11M06, msc_11M26, msc_11M50.
- Triage decision: include — Companion to the ratios conjectures; autocorrelation of ratios is a central heuristic tool.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

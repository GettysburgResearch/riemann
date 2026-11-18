# PAPER-0061 — Correlations of eigenvalues and Riemann zeros

| Field | Value |
|---|---|
| Authors | Conrey, John Brian; Snaith, Nina Claire |
| Year / stratum | 2008 / S5 |
| Venue | Commun. Number Theory Phys. 2, No. 3, 477-536 (2008). |
| Identifiers | zbMATH [1169.11035](https://zbmath.org/?q=an:1169.11035) · DOI [10.4310/CNTP.2008.v2.n3.a1](https://doi.org/10.4310/CNTP.2008.v2.n3.a1) · arXiv [0803.2795](https://arxiv.org/abs/0803.2795) |
| MSC | 11M26, 11M50 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/0803.2795 |
| Selection | score 4.5291, in-pool citations 21, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Assuming RH and the ratios conjecture, give an explicit formula for all lower-order terms of the n-point correlation function of Riemann zeta zeros; carry out the same method for eigenvalues of $U(N)$ obtaining a new (non-determinantal) formula for n-correlation, and show that in the scaling limit the two formulas coincide and yield the determinantal form for all test functions (without support restrictions).

**Historical motivation.** Montgomery-Dyson pair correlation (1972), Odlyzko numerics, Rudnick-Sarnak n-correlation with restricted test function support, and Bogomolny-Keating arithmetic lower-order terms (found by Hardy-Littlewood prime pair analysis); the aim is a systematic derivation of all lower-order terms for n-correlation without Hardy-Littlewood analysis.

### Main results

- **THM-PAPER-0061-1** (Theorem 1 (Gaudin; known), theorem (imported), scope: finite; Sec 3, p.5). For continuous $f:[0,2\pi]^n\to\mathbb C$: $\int_{U(N)}\sum^*_{1\le j_1,\dots,j_n\le N}f(\theta_{j_1},\dots,\theta_{j_n})dX_N=\frac1{(2\pi)^n}\int_{[0,2\pi]^n}f(\theta_1,\dots,\theta_n)\det_{n\times n}S_N(\theta_k-\theta_j)d\theta_1\cdots d\theta_n$, $S_N(\theta)=\frac{\sin(N\theta/2)}{\sin(\theta/2)}$, sum over distinct indices.
- **THM-PAPER-0061-2** (Theorem 2 (Ratios Theorem [7,8]), theorem (RMT, imported), scope: finite; Sec 3.1, p.6). For $\Re\gamma>0,\Re\delta>0$ ($\gamma\in C,\delta\in D$), $|C|\le|A|+N$, $|D|\le|B|+N$: $R(A,B;C,D)=\sum_{S\subset A,T\subset B,|S|=|T|}e^{-N(\sum_{\hat\alpha\in S}\hat\alpha+\sum_{\hat\beta\in T}\hat\beta)}Z(S+T^-,T+S^-;C,D)$, where $A=S+S^-$, $B=T+T^-$ and $Z$ is the ratio of $z$-products (eq. (20)).
- **THM-PAPER-0061-3** (Theorem 3, theorem (proved here), scope: finite; Sec 3.2, p.6-7). If $\Re\alpha_j>0$, $\Re\beta_j>0$ for $\alpha_j\in A,\beta_j\in B$, then $J(A;B)=J^*(A;B)$, where $J(A;B)=\int_{U(N)}\prod_{\alpha\in A}\big(-e^{-\alpha}\tfrac{\Lambda_X'}{\Lambda_X}(e^{-\alpha})\big)\prod_{\beta\in B}\big(-e^{-\beta}\tfrac{\Lambda_{X^*}'}{\Lambda_{X^*}}(e^{-\beta})\big)dX$ and $J^*$ is an explicit sum over set partitions with factors $e^{-N(\ldots)}Z(S,T)Z(S^-,T^-)\times$ (sums over partitions of the remaining shifts as in Lemma 1).
- **THM-PAPER-0061-4** (Theorem 4, theorem (RMT, proved here), scope: finite; Sec 3.4, p.15-16). Let $C_\mp$ be vertical paths $-\delta+\pi i\to-\delta-\pi i$ and $\delta-\pi i\to\delta+\pi i$ and $f$ a $2\pi$-periodic holomorphic function of $n$ variables. Then $\int_{U(N)}\sum_{j_1,\dots,j_n=1}^Nf(\theta_{j_1},\dots,\theta_{j_n})dX$ is expressed as a sum over $K+L+M=\{1..n\}$ of $N^{|M|}$ times $n$-fold contour integrals of $J(-iz_K;iz_L)f(z)$ over $C_\pm$ (all indices, not distinct).
- **THM-PAPER-0061-5** (Theorem 5, theorem (RMT, proved here), scope: finite; Sec 3.5, eq (86), p.17-18). With $J^*$ as in Theorem 3: $\int_{U(N)}\sum^*_{1\le j_1,\dots,j_n\le N}f(\theta_{j_1},\dots,\theta_{j_n})dX_N=\frac1{(2\pi)^n}\int_{[0,2\pi]^n}\sum_{K+L+M=\{1,\dots,n\}}N^{|M|}J^*(-i\theta_K;i\theta_L)f(\theta_1,\dots,\theta_n)d\theta_1\cdots d\theta_n$ (distinct indices, integration along the imaginary axis; the integrand has no poles on the path). Moving contours onto the imaginary axis gives principal value terms that cancel exactly with extra terms in Theorem 4. Proven via the more general Theorem 6 (parameter $0\le R\le n$, by induction).
- **THM-PAPER-0061-6** (Conjecture 1 (Ratios Conjecture [6]), conjecture (imported), scope: conditional; Sec 4.1, eq (100)-(102), p.21-22). With $Z_\zeta(A,B)=\prod_{\alpha\in A,\beta\in B}\zeta(1+\alpha+\beta)$, $Z_\zeta(A,B;C,D)=\frac{Z_\zeta(A,B)Z_\zeta(C,D)}{Z_\zeta(A,D)Z_\zeta(B,C)}$, and $A_\zeta=\prod_pZ_p\int_0^1A_{p,\theta}d\theta$: the integral over an interval $I$ of ratios of shifted zeta functions equals $\int_I\big[\text{sum over swaps }(t/2\pi)^{\ldots}Z_\zeta A_\zeta\big]dt+O(|I|^{1/2+\epsilon})$ (same structure as CAND-01203 Conj 5.1), valid in the standard shift ranges. *Conditional on:* unproved ratios conjecture.
- **THM-PAPER-0061-7** (Theorem 7, theorem (conditional), scope: conditional; Sec 4.2, p.23-25). Assuming the ratios conjecture, if $\Re\alpha_i,\Re\beta_j>0$ then $J_{\zeta,I}(A;B;U)=J^*_{\zeta,I}(A;B;U)+O(|I|^{1/2+\epsilon})$ where $J_{\zeta,I}=\int_I\prod_{\alpha\in A}\frac{\zeta'}{\zeta}(\tfrac12+it+\alpha)\prod_{\beta\in B}\frac{\zeta'}\zeta(\tfrac12-it+\beta)\prod_{\mu\in U}\big(-\tfrac{\chi'}\chi(\tfrac12+it+\mu)\big)dt$ and $J^*_{\zeta,I}=\int_IJ^*_{\zeta,t}dt$ with $J^*_{\zeta,t}$ the analogue of $J^*$ with $N\to\log(t/2\pi)$-type factors and arithmetic factors.
- **THM-PAPER-0061-8** (Theorem 9 and Corollary 2, theorem (conditional), scope: conditional; Sec 4.5, eq (163), (166), p.33-34). Assume RH and Ratios Conjecture 1. For $f$ holomorphic: $\sum_{0<\gamma_1\ne\cdots\ne\gamma_n\le T}f(\gamma_1,\dots,\gamma_n)=\frac1{(2\pi)^n}\int_{[-T,T]^n}\frac1T\int_{I^*}\sum_{K+L+M=\{1..n\}}J^*_{\zeta,t}(-iz_K;iz_L;iz_M)\,dt\,f(z_1,\dots,z_n)dz_1\cdots dz_n+O(T^{1/2+\epsilon})$ with the integrand having no poles on the path; Corollary 2 (translation invariance of $f$) rewrites this as $\frac1{(2\pi)^n}\int_0^T\int\ldots J^*_{\zeta,t}(-iz_K+it;iz_L-it;iz_M-it)f(z)\,dz\,dt$. In the scaling limit, arithmetic terms vanish and the leading term is the determinantal $\det S(z_j-z_k)$ form for arbitrary $f$ (stated in the text, Sec 1, with proof sketched via the RMT formula). *Conditional on:* RH, Ratios Conjecture.

### Key definitions

- $J(A;B)$ (eq (21)) and $J^*(A;B)$ (eq (22))
- $Z(A,B)=\prod z(\alpha+\beta)$, $z(x)=1/(1-e^{-x})$
- $J^*_{\zeta,t}$
- $n$-correlation sum over distinct ordinates $\gamma_1\ne\cdots\ne\gamma_n$

### Principal lemmas

- **THM-PAPER-0061-L1** (Lemma 1; Sec 3.2, p.8). For differentiable $H$ of $w\in W$: $\prod_{w\in W}\frac d{dw}e^H=e^H\sum_{W=W_1+\cdots+W_r}H(W_1)\cdots H(W_r)$ (Faa di Bruno formulation by set partitions). — *Role:* Converts derivatives of the ratios theorem into the logarithmic derivative averages $J(A;B)$.
- **THM-PAPER-0061-L2** (Lemma 2; Sec 3.3, p.10-15). Suppose $\alpha^*\in A,\beta^*\in B$, $A'=A-\{\alpha^*\}$, $B'=B-\{\beta^*\}$. Then $J^*(A;B)$ has at most a simple pole at $\alpha^*+\beta^*=0$ with explicit residue $\propto J^*(A';B')$ (residue identity). — *Role:* Key for moving contour integrals to the imaginary axis (no poles on path; principal value terms cancel).
- **THM-PAPER-0061-L3** (Lemma 3 and Lemma 4; Sec 4.3, p.26-31). Zeta analogues of Lemmas 1 and 2 (residue identity for $J^*_{\zeta}$) used in Sec 4.3 to prove Theorem 8 (contour version) and Theorem 9. — *Role:* Transfers the RMT residue structure to the ratios conjecture setting.
- **THM-PAPER-0061-L4** (Theorem 6; Sec 3.5, eq (89), p.18). With $0\le R\le n$, $(2\pi i)^n\int_{U(N)}\sum^{n,R}f(\theta_{j_1},\dots,\theta_{j_n})dX=\sum_{K+L+M=\{1..n\}}(-1)^{|(L+M)\cap\{1..R\}|}N^{|M|}I^{n,R}_{f;K,L,M}$, where indices $1..R$ run over distinct-sum and the remaining $n-R$ over all indices; proved by induction on $n$ and $R$ (move $z_R$ integral to the imaginary axis, residues at $z_R=z_t$). — *Role:* Induction engine interpolating between Theorem 4 (R=0) and Theorem 5 (R=n).
- **THM-PAPER-0061-L5** (Theorem 8; Sec 4.4, p.31-33). Contour-shifted version of the ratios-conjecture $n$-correlation formula over $C_\pm$ analogous to Thm 4 (with vertical segments of height $T$ contributing only $O(T^\epsilon)$). — *Role:* Intermediate step to Theorem 9.

### Proof architecture

RMT part: start from Ratios Theorem 2 for $U(N)$ (finite N, exact); differentiate to get $J(A;B)=J^*(A;B)$ (Theorem 3, using Lemma 1 on derivatives of exponentials); use contour integral representation of sums $\sum_j f(\theta_j)$ via residues of $\Lambda'/\Lambda$ to get Theorem 4 (all indices, shifted paths); then induct on number R of distinct-index variables (Theorem 6) moving contours to the imaginary axis; Lemma 2 shows $J^*$ has only the simple poles $\alpha+\beta=0$ whose principal-value pieces cancel with the diagonal terms, yielding Theorem 5 (distinct indices, imaginary axis, no poles). Zeta part: Conjecture 1 plus Corollary 1 (inclusion of $\chi'/\chi$ factors) gives Theorem 7; analogs of Lemma 3/4 and Theorem 8 give Theorem 9: $n$-correlation for Riemann zeros including all lower-order terms with error $O(T^{1/2+\epsilon})$. In the scaling limit Theorem 5 matches Theorem 9 and yields determinantal form with no support restrictions on $f$. Sec 5 writes out pair, triple (also in [10]), and quadruple correlations explicitly for RMT and zeta.

**Imported results.** Gaudin's lemma/determinantal n-correlation for $U(N)$ (Thm 1); Ratios Theorem for $U(N)$ [Conrey-Farmer-Zirnbauer, Conrey-Forrester-Snaith] (Thm 2); Ratios Conjecture [CFZ, Conj. 1]; Bogomolny-Keating lower-order pair correlation terms; Rudnick-Sarnak limiting n-correlation (restricted support)

**Techniques.** Ratios theorem for characteristic polynomials (exact, finite N); Logarithmic derivative generating functions (Faa di Bruno via set partitions); Contour integration and residue identity for removing diagonal terms; Induction on number of distinct indices; Scaling limit comparison with Gaudin determinant

## Context and interpretation

**Importance and obstacle overcome.** Gives general closed formula for n-level correlation of zeta zeros (conditional on RH+ratios) with complete lower-order structure, and shows determinantal limit directly for arbitrary test function, circumventing the support restriction obstacle of Rudnick-Sarnak/Rubinstein/Gao and the combinatorial difficulty (matching sums over partitions with determinant expansion) by a residue-cancellation argument.

**Relation to prior work.** Extends Conrey-Snaith triple correlation [10] and CAND-01202 pair correlation (Thm 4.1 there) to all n; uses Ratios Conjecture of CFZ (CAND-01203); alternate to Bogomolny-Keating Hardy-Littlewood approach and Rudnick-Sarnak.

**Limitations and open questions.** Entirely conditional on RH plus the ratios conjecture (for zeta); test function $f$ must be holomorphic (periodic for RMT); formulas for n>=4 get unwieldy; nearest-neighbour spacing lower order terms flagged as anticipated application, not done.

**Ideas in remarks/appendices/abandoned paths.** Intro remark that the method may resolve the combinatorial obstacle in Gao's n-level density for quadratic Dirichlet L-functions with support in $[-2,2]$ (p.2); the new non-determinantal formula for RMT n-correlation (Theorem 5) as a tool for matching arithmetic and RMT structure.

## Research potential

- **Hypotheses that might be weakened.** Holomorphy of the test function $f$ in Theorems 4,5,9 (extension to smooth or compactly supported $f$ would require control of contour shifting); RH assumption (the sum over zeros could be treated with complex ordinates).
- **Generalizations.** Other L-function families (symplectic/orthogonal, with ratios conjectures from CAND-01203 Conj 5.2-5.4) to obtain lower-order n-level density formulas; discrete spacing distribution (nearest-neighbor) from the n-correlation hierarchy, as suggested by the authors.
- **Candidate connections.** Relation to Bogomolny-Keating lower order terms (check agreement numerically for pair and triple); to Hejhal triple correlation; to Montgomery's pair correlation function conjecture $F(\alpha)$ for $\alpha>1$ (via ratios).
- **Reusable lemmas.** Lemma 2 and Lemma 4 (residue identity: $J^*$ has only simple poles at $\alpha+\beta=0$) and Theorem 6 (induction scheme interpolating all/distinct indices).
- **Possible experiments.** Evaluate the quadruple correlation formula of Sec 5.6 and compare against empirical 4-point correlation of Odlyzko's zeros near $10^{22}$; check that $J^*(-i\theta_K;i\theta_L)$ reproduces the sine-kernel determinant numerically for N=4..8 (Theorem 5 vs Theorem 1).
- **Risks / barriers.** The ratios conjecture is unproven even for zeta so the formula is not unconditional information; the Riemann Hypothesis assumed throughout so cannot be used to decide RH-type questions.

## Audit notes (Level 1 reader)

none noticed in inspected portion (the extraction truncates formulas in Theorems 3, 4, 7, so statements for those are descriptive; inspected only a portion of Sec 3.5 and 4.4 proofs).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01253`; harvest queries: kw_RH_any, kw_zeta_zeros, msc_11M26, msc_11M50, arxiv_random_matrix_zeta, arxiv_zeta_zeros.
- Triage decision: include — All lower-order terms in n-correlation via ratios conjecture.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

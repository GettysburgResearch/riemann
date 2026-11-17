# PAPER-0123 — A survey of the Selberg class of \(L\)-functions. II.

| Field | Value |
|---|---|
| Authors | Perelli, Alberto |
| Year / stratum | 2004 / S5 |
| Venue | Riv. Mat. Univ. Parma (7) 3*, 83-118 (2004). |
| Identifiers | zbMATH [1166.11345](https://zbmath.org/?q=an:1166.11345) |
| MSC | 11M06, 11-02 |
| Families | E |
| Work type | survey |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://www.rivmat.unipr.it/fulltext/2004-3s/pdf/04.pdf |
| Selection | score 4.0246, in-pool citations 44, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Survey (part II of Perelli's survey of the Selberg class S). It covers three topics. (5) Analytic properties of linear and non-linear twists F(s,a)=sum a_F(n) n^{-s} e(-n^{1/d} a) of extended-Selberg-class functions, obtained via Fox hypergeometric functions. (6) Classification of functions of degree 1<=d<2, the degree conjectures, and measure-theoretic results on invariants. (7) Independence results: algebraic, statistical and functional independence, the distinct-zeros problem, and pair correlation. Main questions: is S exactly the GL(n) automorphic L-functions, and do L-functions that are not Euler-product-related stay independent, including at the level of zeros.

**Historical motivation.** Selberg (1989, 'Old and new conjectures and results about a class of Dirichlet series') proposed the class S as a model of all L-functions. Kaczorowski-Perelli's twist method (1999 onward) is a way to prove structure theorems from the axioms alone. The independence theory goes back to Selberg's 1940s moment work and Bombieri-Hejhal (1995) on zeros of linear combinations of L-functions.

### Main results

- **THM-PAPER-0123-1** (Theorem 5.2 ([26],[29] = Kaczorowski-Perelli), theorem (cited), scope: global; Sec. 5, p. 87). Let $F\in\widetilde{\mathcal S}^\#_1$ (extended Selberg class, degree 1) and $\alpha>0$. Then the linear twist $F(s,\alpha)=\sum a_F(n)n^{-s}e(-n\alpha)$ is entire if $a_F(n_\alpha)=0$ (with $n_\alpha=q_F\alpha$, and $a_F(n_\alpha):=0$ if $n_\alpha\notin\mathbb N$). If $a_F(n_\alpha)\neq0$ it has at most simple poles at $s_k=1-\frac{k+i\theta_F}{1}$... i.e. $s_k=1-k-i\theta_F$, $k=0,1,\dots$, with residue at $s_0$ equal to $c(F)\,a_F(n_\alpha)/n_\alpha^{i\theta_F}$, $c(F)\neq0$.
- **THM-PAPER-0123-2** (Theorem 5.4 ([29]), theorem (cited), scope: global; Sec. 5, p. 89 (the survey's own transcription of $n_\alpha$ and $s_k$ is partly garbled in the text layer, so exact constants should be checked against [29])). For $d>0$, $F\in\widetilde{\mathcal S}$ of degree $d_F=d$ and $\alpha>0$, the non-linear twist $F_d(s,\alpha)=\sum a_F(n)n^{-s}e(-n^{1/d}\alpha)$ is entire if $a_F(n_\alpha)=0$, where $n_\alpha=q_F d^{-d}\alpha^d$; otherwise it has at most simple poles at $s_k=\frac{d+1}{2d}-\frac{k}{d}-i\frac{\theta_F}{d}$, $k=0,1,\dots$, with $c_0(F,\alpha)\neq0$ at $s_0$.
- **THM-PAPER-0123-3** (Theorem 5.3 ([28]), theorem (cited), scope: global; Sec. 5, p. 88, eq. (5.4)). For $1<d<2$, $F\in\widetilde{\mathcal S}^d$, $\alpha>0$, $J\ge1$: there are $c_0\neq0$ and polynomials $P_j(s)$ ($P_0=c_0$) such that for $\sigma^*>\sigma_a(F)$, $F(s,\alpha)=q_F^{ks}\sum_{j<J}\alpha^{k(d_Fs-d_F/2+i\theta_F+j)}P_j(s)D_F(s^*+jk,\alpha)+G_J(s,\alpha)$ with $G_J$ holomorphic for $\sigma^*>\sigma_a(F)-kJ$, $k=1/(d_F-1)$ (overconvergence).
- **THM-PAPER-0123-4** (Theorem 6.2 ([26]) and Theorem 6.3 ([26]), theorem (cited), scope: global; Sec. 6, pp. 93-94). (6.2) If $F\in\widetilde{\mathcal S}^\#_1$ then $q_F\in\mathbb N$, $a_F(n)n^{i\theta_F}$ is periodic mod $q_F$, $\eta_F\in\{-1,0\}$, and F is uniquely a sum over characters $\chi$ of $P_\chi(s+i\theta)L(s+i\theta,\chi^*)$ with Dirichlet polynomials $P_\chi$ of degree-0 type; $\dim_{\mathbb R}V^\#_1(q,\xi,\omega^*)$ is finite (explicit formula). (6.3) If $F\in\mathcal S_1$ (Selberg class) and $q_F=1$ then $F=\zeta$; if $q_F\ge2$ then $F(s)=L(s+i\theta_F,\chi)$ for a primitive character $\chi$ mod $q_F$ with $\chi(-1)=-(\eta_F+1)\cdot$(sign as stated).
- **THM-PAPER-0123-5** (Theorem 6.4 ([28]), theorem (cited), scope: global; Sec. 6, p. 96). $\widetilde{\mathcal S}^\#_d=\emptyset$ for $1<d<5/3$; moreover for $1<d<2$ no $F\in\widetilde{\mathcal S}^\#_d$ has a pole at $s=1$. Hence $\mathcal S_d=\emptyset$ for $0<d<1$ (Conrey-Ghosh, cited elsewhere), $\mathcal S_1\ni$ only zeta/Dirichlet, and no new degrees in $(1,5/3)$.
- **THM-PAPER-0123-6** (Theorem 6.5 ([31]) 0-1 law, theorem (cited), scope: global; Sec. 6, p. 97). Let $I$ be a continuous, additive, real-valued invariant of the (extended) Selberg class. Then either $I(\mathcal S)$ has Lebesgue measure 0 or $I(\mathcal S)-I(\mathcal S)=\mathbb R$. Same for the extended class.
- **THM-PAPER-0123-7** (Theorem 6.6 ([14], unpublished, proof given in survey), theorem (conditional), scope: conditional; Sec. 6, pp. 98-99). Assume every $F\in\mathcal S^\#_d$ with $d\in\mathbb N$ has a $\gamma$-factor with all $\lambda_j=\tfrac12$. Then the exceptional set $E=\{d>0: d\notin\mathbb N,\ \widetilde{\mathcal S}_d\ne\emptyset\}$ satisfies $E\cap\mathbb Q=\emptyset$ and $m(E)=0$. *Conditional on:* integer-degree functions have all lambda_j=1/2 in a gamma-factor.
- **THM-PAPER-0123-8** (Theorems 7.2, 7.3, 7.4, 7.7 ([50],[3],[5]), theorem (cited), scope: conditional; Sec. 7, pp. 101-106). Under Hypothesis S ($\sum_{p\le x}a_i(p)\overline{a_j(p)}/p=\delta_{ij}n_j\log\log x+c_{ij}+O(1/\log x)$) and Hypothesis D (density estimate $N_j(\sigma,T)\ll T^{1-a(\sigma-1/2)}\log T$ uniformly for $\sigma\ge1/2$): the vector $(\log F_j(1/2+it)/\sqrt{\pi n_j\log\log t})_j$ has weak limit the standard Gaussian on $\mathbb C^N$ (Thm 7.2, Selberg/Bombieri-Hejhal), also in short intervals of length $\ge\log T/\log\log T$ type scale (7.3). Thm 7.4: for $F_j$ with a common functional equation, GRH and Hypothesis H0, all but $o(T\log T)$ zeros up to T of a linear combination $\sum c_jF_j$ are simple and on the critical line. Thm 7.7: distinct $F,G\in\mathcal S$ with $d_F=d_G$ satisfying S and D have $\Delta(T;F,G)\gg T\log T$ (non-effective constant). *Conditional on:* Hypothesis S, Hypothesis D, GRH and H0 for Thm 7.4.
- **THM-PAPER-0123-9** (Theorems 7.5, 7.6, 7.8, 7.10, theorem (cited), scope: global; Sec. 7, pp. 105-112). 7.5 ([38]): for distinct $F,G\in\mathcal S$, $\Delta(T;F,G)=\Omega(T)$ (unconditional). 7.6 ([52] Srinivas): distinct $F,G\in\mathcal S$ with $d_F=d_G$: for large T there is a zero $\rho$ of F with $m_F(\rho)>m_G(\rho)$ and $|T-\rho|\ll\log\log T$, hence $\Delta\gg T/\log\log T$. 7.8 ([25]): if $\log F_1,\dots,\log F_N$ are $\mathbb Q$-linearly independent and $H$ a nonconstant polynomial-type function in the class $\mathcal H$, then $h(s)=H(\log F_j)$ has infinitely many singularities in $\sigma>1/2$ (key Lemma 7.1: infinitely many N-tuples of zeros whose multiplicity vectors form a basis of $\mathbb R^N$). 7.10 ([39]): the pair correlation conjecture PC implies the simple-zeros and distinct-zeros conjectures 7.1, 7.2; if the PC asymptotic holds for some $\alpha_0>0$ then unique factorization follows.

### Key definitions

- Selberg class S: axioms (i) Dirichlet series absolutely convergent for sigma>1, (ii) (s-1)^m F(s) entire of finite order, (iii) functional equation \Phi(s)=\omega\overline{\Phi(1-\bar s)}, \Phi=Q^s\prod\Gamma(\lambda_js+\mu_j)F, Q>0, \lambda_j>0, \Re\mu_j\ge0, |\omega|=1, (iv) a_F(n)\ll n^\varepsilon, (v) Euler product \log F=\sum b_F(n)n^{-s}, b_F(n)=0 unless n=p^m, b_F(n)\ll n^\vartheta, \vartheta<1/2
- extended Selberg class \widetilde{S}: axioms (i)-(iii) only, F not identically 0
- degree d_F=2\sum\lambda_j
- linear twist F(s,\alpha)=\sum a_F(n)n^{-s}e(-n\alpha)
- non-linear twist F_d(s,\alpha)=\sum a_F(n)n^{-s}e(-n^{1/d}\alpha)
- S^#: functions in extended class with a_F(1)... (non-Euler-product models), \widetilde{S}^\#_d
- critical value n_\alpha=q_F\alpha, conductor q_F=(2\pi)^{d}Q^2\prod\lambda_j^{2\lambda_j}
- Hypotheses S and D (Sec. 7)
- Delta(T;F,G): number of zeros of F or G (counted with multiplicity) up to T that are not common zeros, symmetric difference

### Principal lemmas

- **THM-PAPER-0123-L1** (Lemma 6.1 ([28]); Sec. 6, p. 96). For $1<d<2$ and $F\in\widetilde{\mathcal S}^d$, the Rankin-Selberg-type series $F\otimes\bar F(s)=\sum|a_F(n)|^2n^{-2s}$-type (6.2) is holomorphic for $\sigma>\sigma_a(F)-k$ except for a simple pole at $s=1$. — *Role:* Used in Thm 6.4 to remove the Ramanujan axiom (iv) from the argument.
- **THM-PAPER-0123-L2** (Lemma 7.1 ([25]); Sec. 7, p. 108). If $\log F_1,\dots,\log F_N$ are linearly independent over $\mathbb Q$ there are infinitely many N-tuples of zeros $(\rho_1,\dots,\rho_N)$ in $\sigma>1/2$ with multiplicity vectors $m(\rho_j)$ forming a basis of $\mathbb R^N$. — *Role:* Engine of the functional independence Thm 7.8.
- **THM-PAPER-0123-L3** (Theorem 5.1 ([26],[29]); Sec. 5, p. 87). For $d_F=1$ the Fox hypergeometric function $H_K(-iy,s)$ is holomorphic for $y\ne\beta$ and $H_K(-i\beta,s)$ has at most simple poles at $s_k=1-k-i\theta_F$, nonvanishing residue at $s_0$ (here $\beta=\prod\lambda_j^{-2\lambda_j}$). — *Role:* Computes the polar structure of the linear twist from the functional equation via the Mellin-Barnes representation (5.2).
- **THM-PAPER-0123-L4** (Eq. (5.2); Sec. 5, p. 85). $F_N(s,\alpha)=R_N(s,\alpha)+\omega Q^{1-2s}\sum a_F^-(n)\,H_K(Q^2n\zeta_N,s)$, from shifting the contour in $F_N(s,\alpha)=\frac1{2\pi i}\int F(s+w)\Gamma(w)\zeta_N^{-w}dw$, $\zeta_N=\frac1N-2\pi i\alpha$, then using the functional equation. — *Role:* Starting identity for all twist results; N→∞ afterwards.

### Proof architecture

Survey, with proofs mostly sketched. Section 5: regularize the twist with $e^{-n/N}$, write it as a Mellin-Barnes integral, shift the contour, apply the functional equation to get (5.2), analyse the Fox hypergeometric kernels $H_K$ (Braaksma theory, main parameter $\mu=2\sum\lambda_j-1=d_F-1$) and let $N\to\infty$. Section 6 (d=1): poles of $F(s,\alpha)$ at $\alpha=m/q_F$ plus $\alpha$-periodicity give $q_F\in\mathbb N$ and periodicity of $a_F(n)n^{i\theta}$, so $F$ is a combination of Dirichlet L-functions; then the functional equation pins down characters. Section 6 (1<d<5/3): overconvergence formula (5.4) is turned by a Fourier transform into $S_1(x)=x^{-k/2}S_2(x)+O(\cdot)$ with $S_1$ concentrated at integers; a weighted L^2 comparison with weight e(x) yields a contradiction. Thm 6.6: Molteni's n-th-root criterion plus additivity of degree and a sum-set (Steinhaus) lemma. Section 7: Bombieri-Hejhal/Selberg moment method for Gaussian statistical independence, domination of one Euler product on short intervals for zero statements, Mellin-transform and multiplicity-basis arguments for functional independence, Landau's formula for pair correlation. Imports: Braaksma on Fox functions, Selberg/Bombieri-Hejhal central limit machinery, Landau formula, Rudnick-Sarnak.

Dependency edges: CAND-01611 → CAND-01607 (part II depends on notation, definitions and results of part I (Sections 1-4)); CAND-01611 → CAND-01608 (overlapping survey of Selberg-class structure theory (Kaczorowski, Cetraro lectures))

**Imported results.** Braaksma, asymptotics of Fox hypergeometric functions; Selberg 1946/1992, Bombieri-Hejhal 1995 central limit and independence theorems; Conrey-Ghosh: no functions of degree 0<d<1 in S; Kaczorowski-Perelli [25],[26],[28],[29],[30],[31] twist and structure papers; Molteni [33] on roots in S; Srinivas [52] Thm 7.6; Murty-Perelli [39],[40] pair correlation; Landau's formula; Rudnick-Sarnak (n-level correlation, automorphic)

**Techniques.** linear and non-linear twists; Fox hypergeometric functions / Mellin-Barnes integrals (Braaksma); overconvergence of twists and exponential-sum L^2 arguments; Selberg central limit theorem and statistical independence; short-interval domination of Euler products; Landau's formula and pair correlation of zeros of distinct L-functions; Steinhaus sum-set argument (measure of exceptional degree set)

## Context and interpretation

**Importance and obstacle overcome.** Sets out the program of structure theory for S: that the axioms force degrees to be integers (degree conjecture) and the class to be automorphic. RH enters only as a hypothesis (GRH in Thm 7.4, H0), and the survey stresses that off-line zeros occur for linear combinations of Euler products with a common functional equation, so the Euler product is essential to any GRH for general L-functions. The main obstacle, non-integer degrees, is overcome only for d<5/3 via twist overconvergence.

**Relation to prior work.** Continues part I (Sections 1-4, [42], Milan J. Math. 2005) which sets notation: invariants degree, conductor, shift, root number, Conjectures 3.2 (UF), 3.3 (SOC), 4.1-4.2. Relies on Kaczorowski-Perelli papers, Bombieri-Hejhal, Conrey-Ghosh, Molteni, Srinivas, Murty-Perelli (pair correlation, [39],[40]).

**Limitations and open questions.** Open problems stated: 5.1 (is sigma_a(F)=1 for all F in extended class of positive degree), 5.2 (heuristic reason for the simple pole of the non-linear twist), 5.3 (vanishing/non-vanishing of residues at s_k, k>=1), 6.1-6.5 (content of extended-class degree d for non-integer d; finiteness of dimension of V^# for non-integer d; analogue of Thm 6.1 with absolutely convergent Dirichlet series; weakening the hypothesis in Thm 6.6), 7.1 (replace Omega(T) and T/log log T by cT), 7.2 (strongly distinct zeros), 7.3 (quantitative Thm 7.8), 7.4, 7.5 (PC implies SOC), 7.6 (N-level correlation). Conjectures: 6.1 main (S = GL(n) automorphic L-functions), 6.2 converse, 6.3 degree, 6.4 strong degree, 6.5-6.6 twist/twisted conductor, 6.7 0-1 law, 7.1-7.4 (simple zeros, distinct zeros, PC, WPC). The classification stops at d<5/3, which is the limit of the method; Kaczorowski observed the same range follows from the (epsilon,1/2+epsilon) exponent pair conjecture.

## Research potential

- **Hypotheses that might be weakened.** Hypothesis S (quantitative SOC with error O(1/log x)) and Hypothesis D (density exponent a) in Thms 7.2-7.7; the assumption that integer-degree gamma factors have lambda_j=1/2 in Thm 6.6; use of the exponent-pair conjecture to push 5/3 in Thm 6.4.
- **Generalizations.** Extend Thm 7.8 (functional independence of singularities of H(log F_j)) to a quantitative Omega(T) count (Problem 7.3); extend Thm 7.7 to F,G of different degree; effective constant in 7.7 (noted possible in [4]).
- **Candidate connections.** Linear combinations of Euler products with common functional equation are the standard source of off-line zeros (Davenport-Heilbronn type), a boundary case for any RH-for-Selberg-class conjecture; Thm 7.4 gives the extent to which GRH + independence control them. The twist-pole criterion (a_F(n_alpha) detected via poles at alpha=m/q) is a possible tool for testing candidate functions against the axioms.
- **Reusable lemmas.** Eq. (5.2) and Thm 5.1/5.2 as a template for deriving arithmetic constraints on a candidate L-function from its functional equation; Lemma 6.1 (Rankin-Selberg without Ramanujan) and Thm 7.1 (F^a=G^b implies F=H^b, G=H^a, Molteni).
- **Possible experiments.** Numerically test the residue structure of Problem 5.3 for degree-2 cusp-form twists (e.g. a Maass/holomorphic form of small level at alpha=n_alpha with explicit s_1 residue). Test Hypothesis S/D error terms numerically for pairs of degree-2 L-functions to see how far Thm 7.7's T log T constant is realized.
- **Risks / barriers.** Survey only: proofs are in cited papers [26],[28],[29],[25],[5]. Everything in Sec. 7 requires S/D, which are not known beyond degree <=2 in general; no unconditional progress on GRH is claimed. Several 'Theorems' are unpublished or conditional (Thm 6.6).

## Audit notes (Level 1 reader)

Text layer from pdftotext has glyph substitution (e.g. '4' for '=', 'D' for '>', 'E' for '<', 'G' for '<='), so exact constants in Thms 5.2, 5.4 and 6.3 could not be verified symbolically; the transcription in main_results of those constants is reconstructed and flagged. The Contents on p. 83 lists only three sections for Part II, matching the statement 'part II contains Sections 5,6,7' (Sections 8-12 listed in the overall outline appear in later parts not covered here). Theorem 5.5 is stated for the extended class but the survey notes it is proved in [29] only for F=zeta (Lemma 4.1 of [29]) with a remark that the argument is general. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01611`; harvest queries: kw_selberg_class, msc_11M06.
- Triage decision: include — Second part of the Selberg class survey.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

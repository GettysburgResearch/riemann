# PAPER-0099 — Weil positivity and trace formula the Archimedean place

| Field | Value |
|---|---|
| Authors | Connes, Alain; Consani, Caterina |
| Year / stratum | 2021 / S6 |
| Venue | Sel. Math., New Ser. 27, No. 4, Paper No. 77, 70 p. (2021). |
| Identifiers | zbMATH [1480.46084](https://zbmath.org/?q=an:1480.46084) · DOI [10.1007/s00029-021-00689-4](https://doi.org/10.1007/s00029-021-00689-4) · arXiv [2006.13771](https://arxiv.org/abs/2006.13771) |
| MSC | 46L85, 11M55 |
| Families | C, D |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/2006.13771 |
| Selection | score 4.312, in-pool citations 5, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Is there an operator-theoretic (Hilbert space, semi-local trace formula) conceptual reason for the positivity of the archimedean Weil functional $W_\infty=-W_{\mathbb R}$ on test functions supported in $(1/2,2)$, via the trace of the scaling action compressed to Sonin's space $S(1,1)$?

**Historical motivation.** Weil's criterion; Connes 1999 semi-local trace formula; Berry-Keating Hamiltonian (reconciled in CAND-02189); failure of X.-J. Li's attempt (non-innerness of local ratios). Geometric program of the Scaling Site needs principal values it cannot yet handle, so this paper connects operator and geometric approaches via Schwartz kernels.

### Main results

- **THM-PAPER-0099-1** (Theorem 1 (eq. 4), theorem, scope: local; Introduction, Theorem 1 (eq. 4); proof via Theorem 6.11 and Remark 6.12). Let $g\in C_c^\infty(\mathbb R_+^*)$ have support in $[2^{-1/2},2^{1/2}]$ and Fourier transform vanishing at $\pm\frac i2$ (stated in the intro as 'at $\frac i2$ and $0$'). Then $W_\infty(g*g^*)\ge \mathrm{Tr}(\vartheta(g)\,S\,\vartheta(g)^*)\ge0$, where $S$ is the orthogonal projection of $L^2(\mathbb R)_{ev}$ onto Sonin's space $S(1,1)$ (even functions vanishing, with their Fourier transform, on $[-1,1]$) and $\vartheta$ is the scaling action.
- **THM-PAPER-0099-2** (Theorem 6.11 (eq. 141), theorem, scope: local; Sect. 6, Theorem 6.11, Remark 6.12). For $g\in C_c^\infty(\mathbb R_+^*)$ with support in $[2^{-1/2},2^{1/2}]$ and $\hat g(\frac i2)=0$ (the Fourier transform vanishing at $-\frac i2$ in the text), $W_\infty(g*g^*)\ge\mathrm{Tr}(\vartheta(g)S\vartheta(g)^*)-c\,|\hat g(0)|^2$ with $c=\frac{4\gamma}{\log 2}$ (here $\gamma$ is the constant of Lemma 6.10, not Euler's constant). Remark 6.12: the best constant satisfies $13<c<17$, using $\lambda_{\max}(K_I)=1.05158$ with error $\epsilon_1\simeq0.00122$. *Conditional on:* numerical computation of the spectrum of the compact operator K_I (Sect. 6, Toeplitz discretization q->1+, finite rank approximation T; Lemma 6.8-6.10) with an explicit error bound of size 0.00122.
- **THM-PAPER-0099-3** (Corollary 2 (eq. 6), corollary, scope: local; Introduction, Corollary 2 (eq. 6)). For $g\in C_c^\infty([2^{-1/2},2^{1/2}])$ with $\hat g(\frac i2)=0$ and $Z=\frac12+i S$ the multiset of nontrivial zeros: $c|\hat g(0)|^2+\sum_{s\in S}\hat g(s)\overline{\hat g(\bar s)}\ge \mathrm{Tr}(\vartheta(g)S\vartheta(g)^*)$ (Sonin's trace needs an extra contribution on the critical line between the first zeros $\frac12\pm14.1347i$, 'as if multiplying zeta by $(z-\tfrac12)^{17}$').
- **THM-PAPER-0099-4** (Theorem 3 / Theorem 4.7 (eq. 13, 83-84), theorem, scope: global; Sect. 4, Theorem 4.7). The functional $f\mapsto\mathrm{Tr}(\vartheta(f)S)$ is positive on $C_c^\infty(\mathbb R_+^*)$ and equals $W_\infty(f)+\int f(\rho^{-1})\,\epsilon(\rho)\,d^*\rho$, where $\epsilon(\rho^{-1})=\epsilon(\rho)$ and for $\rho\ge1$, $\epsilon(\rho)=\sum_n a\frac{\lambda(n)}{1-\lambda(n)^2}\langle\xi_n|\vartheta(\rho^{-1})\zeta_n\rangle$ in terms of prolate spheroidal data $\lambda(n),\xi_n,\zeta_n$ (normalizing constant 'a' as in the source).
- **THM-PAPER-0099-5** (Proposition 2.2, Corollary 2.3 (eq. 10, 42, 51), proposition/corollary, scope: global; Sect. 2, Prop 2.2, Cor 2.3). Trace-remainder $\delta(\rho)=\mathrm{Tr}\big((\vartheta_m(\rho^{-1})-P\vartheta_m(\rho^{-1})P)\tfrac12u_\infty^*d^-u_\infty\big)$ is a function with $\delta(\rho^{-1})=\delta(\rho)$ and for $\rho\ge1$: $\delta(\rho)=4\rho^{1/2}\iint_\Delta\cos(2\pi\rho xy)\cos(2\pi xy)\,dy\,dx=2\rho^{1/2}\big(\frac{\mathrm{Si}(2\pi(1+\rho))}{2\pi(1+\rho)}+\frac{\mathrm{Si}(2\pi(\rho-1))}{2\pi(\rho-1)}\big)$ (intro form); the functional $L(f)=\int f(\rho^{-1})(\delta(\rho)-\tau(\rho))d^*\rho=\mathrm{Tr}(\vartheta_m(f)P\hat P P)$ is positive without support restriction, and $2\theta'(t)+\hat\delta(t)\ge0$ ($\theta$ Riemann-Siegel angle), checked numerically in Figs 3-6.
- **THM-PAPER-0099-6** (Theorem 3.6 (eq. 58) with Prop 3.2, Lemma 3.3, theorem, scope: local; Sect. 3, Theorem 3.6, Cor. 3.8). For a symmetric bounded interval $I\subset\mathbb R_+^*$ there is a compact (Hilbert-Schmidt) operator $K_I$ on $L^2(I,d^*\rho)$ with $D\circ Q(\xi*\xi^*)=\langle\xi|(-2\,\mathrm{Id}+K_I)\xi\rangle$, where $Q=-(\rho\partial_\rho)^2+\frac14$ imposes vanishing of $\hat f(\pm\frac i2)$ and $D(f)=\int f(\rho^{-1})\delta(\rho)d^*\rho$. The jump of $\delta'$ at $\rho=1$ (from $-1$ to $+1$) produces $-2\delta_1$. Corollary 3.8: $D\circ Q\le0$ on $C_c^\infty(I)$ for $I=[u^{-1},u]$, $u=1.10246$.
- **THM-PAPER-0099-7** (Section 5, Prop 5.5, Lemma 5.4, computation/structure, scope: computational; Sect. 5-6, Lemma 5.4, Prop 5.5, Lemma 6.8, 6.10, Remark 6.12). The analogous functional $E\circ Q(h)=\int h(\rho^{-1})Q\epsilon(\rho)d^*\rho$ has operator $-\frac12\epsilon'(1^+)(\mathrm{Id}-K)$ on $L^2(I,d^*\rho)$ with $\epsilon'(1^+)\approx$ a constant related to $22.9965$ ($\frac12\epsilon'(1^+)\approx22.9965$ in the intro), so $E\circ Q$ is essentially negative on functions supported in a fixed compact interval; Section 6 shows for $I=[\frac12,2]$ that $K_I$ has exactly one eigenvalue $>1$ ($\lambda_{\max}=1.05158$). *Conditional on:* numerical Toeplitz-matrix/finite-rank approximation of K_I (not interval arithmetic).

### Key definitions

- Weil functional $W_\infty=-W_{\mathbb R}$ on $C_c^\infty(\mathbb R_+^*)$
- Sonin space $S(\alpha,\beta)\subset L^2(\mathbb R)_{ev}$ of even functions vanishing, with Fourier transform, on a symmetric interval (Def 4.4; $S(1,1)$)
- trace-remainder $\delta(\rho)$ (Def 2.1)
- quantized differential $d^-u=[H,u]$ with $H$ the Hilbert-transform-like operator of square 1
- 'essentially negative' functional (Def 3.4)

### Principal lemmas

- **THM-PAPER-0099-L1** (Lemma 4.1; Sect. 4, Lemma 4.1). For $\rho\ge1$, $\delta(\rho)=\mathrm{Tr}(\vartheta_m(\rho^{-1})\hat P_1P_1)$, expressed via prolate spheroidal functions (projections $P_\Lambda,\hat P_\Lambda$ at $\Lambda=1$). — *Role:* Moves the small square Delta into the big square Sigma using pairs of projections; link to the 'quantum cell' left out by the Berry-Keating cutoff.
- **THM-PAPER-0099-L2** (Lemma 4.2, Definition 4.3, Prop 4.5; Sect. 4). Pairs of orthogonal projections correspond to representations of the infinite dihedral group $\mathbb Z\rtimes\mathbb Z/2$; the angle operator; on range of $P_1\vee\hat P_1$ the irreducible components are 2-dimensional, labelled by eigenvalues of the prolate operator, and the orthogonal complement is Sonin's space on which the representation is trivial. — *Role:* Structure theory used to define S and prove Thm 4.7.
- **THM-PAPER-0099-L3** (Lemma 3.3 and Prop 3.5; Sect. 3, Lemma 3.3, Prop 3.5). The vanishing conditions $\hat f(\pm i/2)=0$ define an ideal $J$ in the convolution algebra; functionals $\varphi$ with such conditions are equivalent to $\varphi\circ Q$ on a symmetric interval. — *Role:* Shows the vanishing conditions can be absorbed without changing support.
- **THM-PAPER-0099-L4** (Lemma 6.8; Sect. 6, Lemma 6.8). Spectrum of the finite-rank operator $T$ (eq. 119) is $\{\lambda_{\max}(1-\beta_j)\}$ for explicit $\beta_j$. — *Role:* Numerical control of K_I.
- **THM-PAPER-0099-L5** (Lemma 6.9, Lemma 6.10; Sect. 6, Lemma 6.9-6.10). Lemma 6.9: elementary estimate for a pair of unit vectors and the rank-one projection $P_\varphi$ in a Hilbert space; Lemma 6.10: for $N_I=-\frac12\epsilon'(1^+)(\mathrm{Id}-K_I)$ on $L^2(I)$, $I=[-\frac12\log2,\frac12\log2]$, one has $\langle\xi|N_I\xi\rangle\le\gamma|\langle\xi_0|\xi\rangle|^2$ with $\xi_0$ the normalized constant vector. — *Role:* Reduces the single bad direction to the evaluation $\hat g(0)$, giving the $c|\hat g(0)|^2$ term.
- **THM-PAPER-0099-L6** (Lemma 1.4, Prop 1.5; Sect. 1). Schwartz kernel of $u_g$ and of $\vartheta_m(\rho^{-1})\frac12u_\infty^*d^-u_\infty$ in $L^2(\mathbb R_+^*)$; geometric identification of the trace as intersection with diagonal, splitting into the squares $\Delta$ and $\Sigma$. — *Role:* Bridges the operator picture and the geometric (Scaling Site square) picture; direct proof of $W_\infty(f)=-\frac12\mathrm{Tr}(\hat f\,u^*d^-u)$.

### Proof architecture

(1) Express W_infty(f) = -1/2 Tr(f^ u^* d^- u) via Schwartz kernels (Sect. 1) and split into the squares Delta (small) and Sigma (big). (2) Show the trace-remainder delta(rho) of the small square is explicit and that L = D + W_infty is positive for all test functions (Prop 2.2, Cor 2.3; positivity as Tr of product of two positive operators, also numerically checked via 2 theta' + delta^ >= 0). (3) For supports in a compact interval, impose hat f(+-i/2)=0 via Q: the jump of delta' at 1 yields -2 Id + compact (Thm 3.6) so D o Q is negative modulo finite rank. (4) Move Delta into Sigma using pairs of projections and prolate spheroidal functions: Tr(theta(f) S) = W_infty(f) + integral f(rho^-1) eps(rho) (Thm 4.7), where S is the projection onto Sonin's space and positivity is by construction. (5) Analyze E o Q similarly (Sect. 5): -1/2 eps'(1+)(Id - K) with K compact. (6) Section 6: discretize R_+^* by q^Z, identify K_q as Toeplitz matrix, numerically determine K on I=[1/2,2], build finite-rank T, find spectrum: exactly one eigenvalue >1 (lambda_max=1.05158) whose eigendirection is controlled by hat g(0), giving Theorem 6.11. Imported: Weil's explicit formula and Weil's equivalence of RH with negativity; Yoshida's reduction [34] to compact support (Prop. C.1 in appendix); Slepian-Pollak prolate theory; Toeplitz matrix theory; Sonin space (Sonine 19th c.).

Dependency edges: CAND-01965 → CAND-02189 (builds_on); CAND-02188 → CAND-01965 (builds_on); CAND-01965 → Connes 1999 semi-local trace formula (builds_on); CAND-01965 → Yoshida (ref [34]) archimedean Weil positivity (refines)

**Imported results.** Weil's explicit formula and Weil's criterion; Yoshida (ref [34]) reduction to compact support and the archimedean positivity statement; Theory of prolate spheroidal wave functions (Slepian-Pollak, Landau-Pollak) as used in Connes 1999 [11]; Hermitian Toeplitz matrix theory; Appendix C Prop C.1: RH iff sum W_v(g*g^#)<=0 for g with vanishing Mellin transform on a finite set F disjoint from zeros

**Techniques.** Weil explicit formula positivity; semi-local trace formula (Connes 1999); quantized calculus (Hilbert transform commutator); pairs of projections / infinite dihedral group representations; prolate spheroidal wave functions; Hermitian Toeplitz matrices, discretization q->1+; Sonin space compression of scaling action

## Context and interpretation

**Importance and obstacle overcome.** Provides an operator-theoretic, positivity-by-construction mechanism (trace of scaling action on Sonin's space) for the archimedean Weil inequality, quantitatively relating W_infty to Tr(theta(f)S) up to a rank-one error; overcomes the singularity of the distribution W_R at rho=1 by quantized-calculus/Schwartz-kernel technique, and the failure of Li's attempt by using the complement of range of P_1 v hat P_1.

**Relation to prior work.** Extends [17] (Scaling Hamiltonian = CAND-02189) and [11] (Connes 1999); refines Yoshida's explicit proof [34] of Weil positivity for the archimedean place; feeds into the follow-up quasi-inner functions paper (CAND-02188) which studies the Sonin space as kernel of the diagonal block of a quasi-inner function.

**Limitations and open questions.** Only the single archimedean place with support in (1/2,2) (so no finite primes) is treated; this range already follows from Yoshida [34]/direct computation, so the contribution is a conceptual explanation, not a new RH-relevant case. The constant c (13<c<17) is obtained from a numerical eigenvalue computation (lambda_max=1.05158 with error 0.00122), not a rigorous symbolic proof; the extra term c|hat g(0)|^2 is eliminated by imposing hat g(0)=0, legitimate by RH-equivalence (2) only through the finite exceptional set F. Extension to semi-local sets {inf,2,3,...,p} with support in (p^{-1},p) is only asserted as expected (Conjecture 4.1 of CAND-02189).

**Ideas in remarks/appendices/abandoned paths.** Corollary 2's observation that Sonin's trace needs an extra critical-line contribution 'as if zeta were multiplied by (z-1/2)^17' (Intro); the Toeplitz-discretization with q->1+ is conceptually tied to the Hasse-Weil limit of zeta over F_q as q->1 (Sect. 5-6 intro); function-field analogy that the vanishing at +-i/2 corresponds to isolating the H^1 contribution in the Lefschetz formula.

## Research potential

- **Hypotheses that might be weakened.** Support in (1/2,2) can be enlarged only by including the finite place p=2 (semi-local set {inf,2}), where the same trace-remainder argument (Lemma 4.1 analogue with the p-adic Sonin space of Prop 5.1 in CAND-02188) is expected; the vanishing conditions at +-i/2 could be replaced by control of the compact operator K_I on a larger interval where lambda_1(K_I) crosses new thresholds.
- **Generalizations.** Semi-local case S={inf,2,...,p}, support in (p^-1,p): the equality (12)-type identity delta=Tr(theta P^_1 P_1), Sonin spaces S(u(F)) of CAND-02188 and the inductive system there; also to Dirichlet L-functions/function fields where Lefschetz H^1 plays the role of the removed +-i/2.
- **Candidate connections.** Prolate spectrum / Landau-Pollak-Slepian theory; Toeplitz determinants and Szego-type asymptotics; Li's criterion; Yoshida's explicit positivity; Berry-Keating cutoff (the one 'quantum cell' observed in Figs 5-6 of CAND-02189).
- **Reusable lemmas.** Thm 3.6 (-2 Id + Hilbert-Schmidt decomposition of D o Q), Prop 2.2 closed form of delta(rho) with Si functions, Thm 4.7 formula Tr(theta(f)S)=W_inf(f)+integral f eps.
- **Possible experiments.** Rigorous interval-arithmetic verification of lambda_max(K_I)=1.05158 and the bound 13<c<17 (Remark 6.12 relies on numerical accuracy 0.00122); numerical test of the same decomposition for I=[1/3,3] with {inf,2,3} semi-local places; verify 2 theta'(t)+delta^(t)>=0 on a certified grid and prove it analytically.
- **Risks / barriers.** The step from this single-place identity to all primes requires controlling the compact operators uniformly as the prime set grows (growing-prime control is a different statement from each finite set); the support restriction (p^-1,p) grows with p but Weil positivity needed for RH requires all supports, so a global argument is still missing; the numerical Toeplitz step has no certified error budget.

## Audit notes (Level 1 reader)

Notation drift in the extracted text: Theorem 1 and the intro say hat g vanishes at '2i' / 'i/2 and 0' whereas Theorem 6.11 states vanishing at -i/2 (and (4) in the intro adds vanishing at 0); the vanishing at 0 is needed only to kill the c|hat g(0)|^2 term, so Theorem 1 as stated in the intro (without the c term) needs both conditions, consistent with eq. (5). Constant $\gamma$ in c=4\gamma/\log 2 is not Euler's gamma (defined in Lemma 6.10); the explicit value is only bounded via numerical computation (13<c<17). Statement of Theorem 1 might be misread as holding without hat g(0)=0. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01965`; harvest queries: kw_RH_any, kw_trace_formula_zeta, kw_weil_positivity, arxiv_weil_explicit, arxiv_zeta_zeros.
- Triage decision: include — Connes-Consani on Weil positivity via semilocal trace formula.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

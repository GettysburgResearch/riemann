# PAPER-0125 — Quasi-inner functions and local factors

| Field | Value |
|---|---|
| Authors | Connes, Alain; Consani, Caterina |
| Year / stratum | 2021 / S6 |
| Venue | J. Number Theory 226, 139-167 (2021). |
| Identifiers | zbMATH [1476.46071](https://zbmath.org/?q=an:1476.46071) · DOI [10.1016/j.jnt.2021.01.024](https://doi.org/10.1016/j.jnt.2021.01.024) · arXiv [2008.10974](https://arxiv.org/abs/2008.10974) |
| MSC | 46L85, 11M55, 11M26 |
| Families | D, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/2008.10974 |
| Selection | score 3.9195, in-pool citations 2, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** For finite sets F of places of Q containing the archimedean place, is the product $u=\prod_{v\in F}\rho_v$ of ratios of local L-factors $\rho_v(z)=\gamma_v(z)/\gamma_v(1-z)$ quasi-inner (i.e. $(1-P)uP$ compact for the Hardy projection $P$)? This is a first test of the strategy of CAND-01965 to prove Weil positivity from the semi-local trace formula.

**Historical motivation.** Connes-Consani Weil positivity strategy via Sonin space trace (CAND-01965) and the criticism of X.-J. Li's attempt via non-innerness of local ratios (CAND-02189).

### Main results

- **THM-PAPER-0125-1** (Definition (Introduction), definition, scope: global; Introduction, Definition). Let $\Omega\subset\mathbb C$ be an open disk or half-space. $u\in L^\infty(\partial\Omega)$ with $u\bar u=1$ is quasi-inner if $(1-P)uP$ is compact, $P$ the orthogonal projection of $L^2(\partial\Omega)$ onto the Hardy space $H^2(\Omega)$. Inner functions are quasi-inner; products of quasi-inner functions are quasi-inner; on the unit disk, $(1-P)uP\sim JH_u$ modulo finite rank where $H_u$ is the Hankel operator with symbol $u$.
- **THM-PAPER-0125-2** (Theorem 2.1 and Theorem 2.3, theorem, scope: global; Sect. 2, Thm 2.1, 2.3, Prop 2.4). $\rho_\infty(z)=\pi^{-z/2}\Gamma(z/2)/(\pi^{-(1-z)/2}\Gamma((1-z)/2))$ is quasi-inner relative to $C_-=\{\mathrm{Re}\,z\le\tfrac12\}$, and $(1-P)\rho_\infty P$ is an infinitesimal of infinite order. Theorem 2.3 gives explicit rank-one expansion $(1-P)\kappa P=\sum_n(-1)^{n+1}\frac{2\pi^{2n+1/2}}{(4n+1)\Gamma(n+1)\Gamma(n+1/2)}|\xi_n\rangle\langle\eta_n|$ for $\kappa=\rho_\infty\circ\psi$, $\psi(v)=\frac12+\frac{v-1}{v+1}$ (Cayley-type map). Proposition 2.4 independently: $\kappa\in C^\infty(S^1)+H^\infty(\mathbb U)$.
- **THM-PAPER-0125-3** (Fact 3.6, Lemma 3.5, Prop 3.7, proposition, scope: global; Sect. 3, Lemma 3.5, Fact 3.6, Prop 3.7). For a rational prime $p$, $\rho_p(z)=\frac{1-p^{z-1}}{1-p^{-z}}$ (as ratio of $\gamma_p$) is periodic of period $\log p$ with poles on $\frac{2\pi i}{\log p}\mathbb Z$ and is not quasi-inner (Fact 3.6). With $B_p$ the Blaschke product attached to its poles, $\kappa_pB_p=-p\frac{v+1}{v-1}$-type inner function (Prop 3.7(i)), $\ker(1-P)\kappa_pP$ is the shift-invariant subspace $B_pH^2(\mathbb U)$, and the cokernel is its image under the involution $Jf(z)=z^{-1}f(z^{-1})$.
- **THM-PAPER-0125-4** (Theorem 4.4 / Theorem 4.1 / Theorem 4.8 (main theorem), theorem, scope: global; Sect. 4, Theorem 4.1, Thm 4.4, Prop 4.5, Theorem 4.8). For any finite set $F$ of places of $\mathbb Q$ containing $\infty$, $u=\rho_\infty\prod_{p\in F\setminus\{\infty\}}\rho_p$ is quasi-inner relative to $C_-$. For a single prime, $\rho_\infty\rho_p$ is quasi-inner and $(1-P)\kappa\kappa_pP=E_\infty+E_p+E_0$ (explicit sum over poles); for general $F$ (Thm 4.8, with $\rho_\infty=\prod_{k=0}^{m-1}\varphi_{m,k}$ via Gauss multiplication) $\rho_\infty^{(m,k)}\rho_p$ is quasi-inner and $(1-P)\rho_\infty\prod\rho_pP$ is an infinitesimal of order $\frac1{2m}$ (m=number of finite places-based factorization; stated as 'order 1/2m'). Each individual $\rho_p$ is not quasi-inner.
- **THM-PAPER-0125-5** (Theorem 5.3(i) and Proposition 5.5, theorem, scope: global; Sect. 5, Theorem 5.3(i), Prop 5.5). (i) For $F$ finite containing the archimedean place and $u(F)=\prod_F\rho_v$, the Sonin space $S(u(F))=\ker (u(F))_{22}$ is infinite dimensional. Prop 5.5: the image under $F_\mu\circ w$ of Sonin's space $S(1,1)$ equals $\ker(1-P)\rho_\infty(1-P)=\ker(\rho_\infty)_{22}$.
- **THM-PAPER-0125-6** (Theorem 5.3(ii) with Lemma 5.6, theorem, scope: global; Sect. 5.3-5.4, Theorem 5.3(ii), Lemma 5.6). For finite sets $F\subset F'$ as above, multiplication by $D(F,F')=\prod_{p\in F'\setminus F}(1-p^{-z})$ defines an injective linear map $S(u(F))\to S(u(F'))$; hence the semi-local Sonin spaces form an inductive system of infinite dimensional spaces. Proof: $N_F=\prod(1-p^{z-1})\in H^\infty(C_-)$, $D_F=\prod(1-p^{-z})\in H^\infty(C_+)$ (Lemma 5.6), so $\xi\in S(u(F))$ implies $D\xi\in H^2(C_+)$ and $u(F')D\xi=N_{F''}u(F)\xi\in H^2(C_-)$.

### Key definitions

- quasi-inner function: unimodular u with (1-P)uP compact
- local factors $\gamma_\infty(z)=\pi^{-z/2}\Gamma(z/2)$, $\gamma_p(z)=(1-p^{-z})^{-1}$, $\rho_*(z)=\gamma_*(z)/\gamma_*(1-z)$
- semi-local Sonin space $S(u)=\ker u_{22}$, $u_{22}=(1-P)u(1-P)$
- local Sonin space $S(K,\alpha)=\{f\in L^2(K):f(x)=0=\mathcal F_\alpha f(x)\ \forall |x|<1\}$ (Def 5.1)
- Blaschke product $B_p$ associated to the poles of $\rho_p$

### Principal lemmas

- **THM-PAPER-0125-L1** (Lemma 3.1-3.4; Sect. 3). $\rho_p$ is $\log p$-periodic; Lemma 3.2-3.4 give an explicit basis $\zeta_n\in\ell^2(\mathbb N)$ and an isomorphism $V:\ell^2(\mathbb Z)\to\ell^2(\mathbb N)$, $V(\delta_n)=\zeta_n$; Lemma 3.5 gives $(1-P)\kappa_pP$ in terms of $V$ and the involution $I(\delta_n)=\delta_{-n}$. — *Role:* Computation of the off-diagonal block for a single prime.
- **THM-PAPER-0125-L2** (Lemma 4.3 and Lemma 4.6; Sect. 4.1, 4.3, Lemma 4.3, 4.6). Estimates on the decay of $\rho_\infty$ (and of its Gauss-factor pieces $\rho_\infty^{(m,k)}$) on the imaginary line; the terms $|\rho_\infty^{(m,k)}(\frac{2\pi in}{\log p})|=O(n^{-1/(2m)})$. — *Role:* Key analytic input for compactness of $(1-P)\rho_\infty\rho_pP$ and for the order of infinitesimal.
- **THM-PAPER-0125-L3** (Proposition 4.5; Sect. 4.2). $\kappa(v)\kappa_p(v)\in C(S^1)+H^\infty(\mathbb U)$ (in fact smooth away from $v=1$). — *Role:* Alternative route to quasi-innerness (Hankel compactness via Hartman).
- **THM-PAPER-0125-L4** (Proposition 5.4; Sect. 5.1). For a triangular block matrix of operators $U$ (modulo compacts, quasi-inner), the structure of the unitary is governed by the kernel of the matrix element $U_{22}$. — *Role:* Motivates defining the semi-local Sonin space as $\ker U_{22}$.
- **THM-PAPER-0125-L5** (Gauss multiplication step (Sect. 4.3); Sect. 4.3-4.4, Theorem 4.8). Using the Gauss multiplication formula for $\Gamma$, $\rho_\infty=\prod_{k=0}^{m-1}\varphi_{m,k}$ with each factor quasi-inner and having the decay properties of $\rho_\infty$ so that the products $\varphi_{m,k}\rho_p$ remain quasi-inner for $m$ large relative to the number of primes. — *Role:* The 'fundamental step' to pass from one prime to m primes.

### Proof architecture

Reduce quasi-innerness to compactness of Hankel operators on the disk through the Cayley transform psi. (1) Archimedean: show Fourier-type coefficients a_{-k} of kappa=rho_inf o psi decay rapidly (Thm 2.1, explicit series Thm 2.3, and independent proof by kappa in C^inf+H^inf, Prop 2.4). (2) Single prime: compute (1-P)kappa_p P via basis zeta_n (Lemma 3.2-3.5) showing it has a non-compact piece (Fact 3.6: poles accumulate on the line giving infinitely many Blaschke zeros), identify B_p kappa_p inner (Prop 3.7). (3) rho_inf rho_p: the poles of the product cancel the non-compact part; compute (1-P)kappa kappa_p P = E_inf + E_p + E_0 (Thm 4.4) using decay estimates of rho_inf on the imaginary axis (Lemma 4.3). (4) m+1 places: factor rho_inf into m quasi-inner factors via Gauss multiplication (Sect. 4.3), distribute over primes, and use that products of quasi-inner functions are quasi-inner (Thm 4.8, Thm 4.1). (5) Sonin space S(u)=ker u_22; Prop 5.5 identifies the classical Sonin space; Thm 5.3(ii) uses N_F in H^inf(C_-) and D_F in H^inf(C_+). Imported: Hankel operator compactness (Hartman, Martinez-Avendano-Rosenthal), Gauss multiplication formula, Rudin Thm 17.11 for H^inf membership.

Dependency edges: CAND-02188 → CAND-01965 (builds_on); CAND-02188 → CAND-02189 (builds_on); CAND-02188 → Hartman theorem on Hankel operators (imports)

**Imported results.** Hartman's theorem on compact Hankel operators (via Martinez-Avendano-Rosenthal GTM 237); Gauss multiplication theorem for Gamma; Rudin, Real and Complex Analysis Thm 17.11; Connes 1999 semi-local trace formula (for the context)

**Techniques.** Hardy space / Hankel operator compactness (Hartman theorem); Blaschke products and shift-invariant subspaces; Gauss multiplication formula for Gamma; asymptotic decay of archimedean ratio on the imaginary axis; quantized calculus and conformal invariance

## Context and interpretation

**Importance and obstacle overcome.** Shows the failure of ratio of local factors to be inner (obstruction in Li's attempt, [4]) is repaired by quasi-innerness for the archimedean place and for finite products with it, while individual non-archimedean ratios fail; this is the first test of the semi-local strategy of [5]. Obstacle: individual p-adic ratios are not quasi-inner (infinitely many Blaschke zeros), overcome by combining with a Gauss-factor of rho_inf with sufficiently slow-but-adequate decay O(n^{-1/(2m)}).

**Relation to prior work.** Direct sequel of CAND-02189 and CAND-01965; the archimedean case recovers Theorem 4.7/Sect. 4 structure of [5] by independent proof (Theorem 2.1 'independent direct proof'). Uses Hankel operator theory from the Hardy space textbook of Martinez-Avendano-Rosenthal.

**Limitations and open questions.** Only quasi-innerness (compactness of the off-diagonal block) is proved; this does not yet give Weil positivity. The identification of the abstractly defined space S(u(F))=ker u_22 with the geometric semi-local Sonin space is explicitly postponed to a future 'geometric paper'. Only the half plane Re z<=1/2 version is treated; also only the trivial character (zeta) is considered, not general L-functions.

**Ideas in remarks/appendices/abandoned paths.** Sect. 5.1: the Calkin-algebra triangular structure of quasi-inner unitaries, with kernel of U_22 governing the structure, suggests a classification of 'Sonin-type' spaces for any quasi-inner u (Prop 5.4).

## Research potential

- **Hypotheses that might be weakened.** Finite F: the order-1/(2m) infinitesimal bound degrades with number of places; a uniform-in-F bound would be needed for growing-prime control. Restriction to the trivial character could be dropped by replacing rho_v with ratios for Dirichlet characters.
- **Generalizations.** Quasi-innerness for ratios of gamma factors of L(s,chi) and of automorphic L-functions (GL_n gamma factors, Gauss multiplication for Gamma products); other half planes/domains; Schatten class of (1-P)uP as a quantitative invariant (here order 1/(2m)).
- **Candidate connections.** Hankel operators and Nehari problems; Blaschke zero structure of rho_p vs prime spectrum 2 pi i n/log p; Sonin-space inductive system and the Weil positivity program (CAND-01965): identify the trace Tr(theta(f)S_F) on S(u(F)) with the semi-local Weil functional.
- **Reusable lemmas.** Lemma 5.6 (N_F in H^inf(C_-), D_F in H^inf(C_+)) and the injection of Thm 5.3(ii); Prop 3.7 Blaschke-product description of the kernel for a single prime; Lemma 4.6 decay estimates for Gauss factors of rho_inf.
- **Possible experiments.** Numerically compute singular values of the Hankel matrix of kappa*kappa_p for F={inf,2}, {inf,2,3} to test the predicted decay n^{-1/(2m)} vs the actual rate; compute dim of truncations of S(u(F)) to see how it grows with |F|; test whether the injection of Thm 5.3(ii) is onto modulo finite dimension.
- **Risks / barriers.** Quasi-innerness is necessary-looking but not sufficient for positivity; the identification of S(u(F)) with geometric Sonin spaces and the trace compression remain unproven; non-uniformity in F obstructs passage to all primes.

## Audit notes (Level 1 reader)

Abstract and intro describe the order of infinitesimal as 'order 1/(2m)' while Theorem 4.8's proof says each factor is O(n^{-1/(2m)}); the relation between m (number of Gauss factors) and the number of primes in F is only loosely stated in extraction; the extracted text for Prop 3.7(i) shows the inner function as '-p (v+1)/(v-1)' which has modulus not 1 on the circle for p>1, likely garbled extraction of $-\frac{(v+1)/(v-1)\ \text{stuff}}{...}$; check original. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02188`; harvest queries: kw_RH_any, msc_11M26, arxiv_critical_line.
- Triage decision: include — Connes-Consani on quasi-inner functions and local factors, spectral program.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

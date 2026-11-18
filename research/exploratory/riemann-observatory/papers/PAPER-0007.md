# PAPER-0007 — An essay on the Riemann hypothesis

| Field | Value |
|---|---|
| Authors | Connes, Alain |
| Year / stratum | 2016 / S6 |
| Venue | Nash, John Forbes jun. (ed.) et al., Open problems in mathematics. Cham: Springer (ISBN 978-3-319-32160-8/hbk; 978-3-319-32162-2/ebook). 225-257 (2016). |
| Identifiers | zbMATH [1353.11095](https://zbmath.org/?q=an:1353.11095) · DOI [10.1007/978-3-319-32162-2_5](https://doi.org/10.1007/978-3-319-32162-2_5) · arXiv [1509.05576](https://arxiv.org/abs/1509.05576) |
| MSC | 11M26, 46L85, 11M06, 11M55 |
| Families | D, E |
| Work type | survey |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/1509.05576 |
| Selection | score 4.7062, in-pool citations 7, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Essay: survey how RH shaped algebraic geometry and present three strategies working at the level of explicit formulas: (i) analytic via Selberg trace formula and absorption spectra, (ii) algebraic-geometric Riemann-Roch/Weil-proof framework through the arithmetic and scaling sites, (iii) Weil cohomology via Segal Gamma-rings and topological cyclic homology.

**Historical motivation.** Riemann 1859 explicit formula, Weil 1948 proof for curves, Deligne 1973, Selberg trace formula, Connes 1999; invitation by Nash/Rassias for the Springer volume.

### Main results

- **THM-PAPER-0007-1** (Lemma 2.1, lemma, scope: global; Sec 2.3, eq (13)). Let $s(x,y)$ be a symmetric bilinear form on a vector space E over Q or R, and $\xi_0,\xi_1\in E$ with (1) $s(\xi_j,\xi_j)=0$, $s(\xi_0,\xi_1)=1$; (2) for every x with $s(x,x)>0$, $s(x,\xi_0)\ne0$ or $s(x,\xi_1)\ne0$. Then $s(x,x)\le2s(x,\xi_0)s(x,\xi_1)$ for all x in E.
- **THM-PAPER-0007-2** (Eq (17)-(18), reformulation (Weil/Li criterion), scope: global; Sec 3.1, (17)-(18)). $\mathrm{RH}\iff s(f,f)\le0$ for all real compactly supported f on $\mathbb R_+^*$ with $\int f(u)d^*u=\int f(u)du=0$, where $s(f,g)=N(f\star\tilde g)$, $\tilde g(u)=u^{-1}g(u^{-1})$, $N(h)=\sum_{n\ge1}\Lambda(n)h(n)+\int_1^\infty\frac{u^2h(u)-h(1)}{u^2-1}d^*u+c\,h(1)$, $c=\tfrac12(\log\pi+\gamma)$.
- **THM-PAPER-0007-3** (Eq (22), trace formula (recalled), scope: global; Sec 3.3). In the nuclear-space setting, $\mathrm{Tr}_{distr}\int h(w)\vartheta^*(w)d^*w=\sum_v\int_{K_v^\times}\frac{h(w^{-1})}{|1-w|}d^*w$ with spectral side involving all nontrivial zeros; minus sign leads to 'absorption spectrum' interpretation.
- **THM-PAPER-0007-4** (Thm 4.2 ([37,38]), theorem (recalled), scope: global; Sec 4.3.1). The set of points of the arithmetic site $\mathcal A=(\widehat{\mathbb N^\times},\mathbb Z_{max})$ over $\mathbb R^{max}_+$ is canonically isomorphic to $X_{\mathbb Q}=\mathbb Q^\times\backslash\mathbb A_{\mathbb Q}/\hat{\mathbb Z}^\times$, with Frobenius automorphisms $Fr_\lambda$ corresponding to the idele class group action.
- **THM-PAPER-0007-5** (Eq (31)-(32) ([37,38]), theorem (recalled), scope: global; Sec 4.3.1). Frobenius correspondences $\Psi(\lambda)$ on the square of the arithmetic site satisfy $\Psi(\lambda)\circ\Psi(\lambda')=\Psi(\lambda\lambda')$ if $\lambda\lambda'\notin\mathbb Q$ or both rational; if $\lambda,\lambda'$ irrational with $\lambda\lambda'\in\mathbb Q$, then $\Psi(\lambda)\circ\Psi(\lambda')=\mathrm{Id}_\epsilon\circ\Psi(\lambda\lambda')$.
- **THM-PAPER-0007-6** (Thm 4.3 ([40]), theorem (recalled), scope: global; Sec 4.3.2). On the quasi-tropical curve $C_p=\mathbb R_+^*/p^{\mathbb Z}$: (i) for a divisor D with deg(D) >= 0, the limit $\mathrm{Dim}_{\mathbb R}(H^0(D))=\lim_n p^{-n}\dim_{top}(H^0(D)_p^n)$ exists and equals deg(D); (ii) $\mathrm{Dim}_{\mathbb R}(H^0(D))-\mathrm{Dim}_{\mathbb R}(H^0(-D))=\deg(D)$ for all D in Div(C_p). The Jacobian J(C_p) is cyclic of order p-1.
- **THM-PAPER-0007-7** (Open Riemann-Roch inequality, conjectural target (not proved), scope: conditional; Sec 4.3.2 (end)). On the square of the arithmetic site one expects $\mathrm{Dim}_{\mathbb R}(H^0(D))+\mathrm{Dim}_{\mathbb R}(H^0(-D))\ge\tfrac12D\cdot D$ for divisors D(f)=\int\Psi(\lambda)f(\lambda)d^*\lambda, with $\tfrac12D(f)\cdot D(f)=s(f,f)$, which together with the strategy of Sec 2.3 would yield (17). *Conditional on:* a yet-to-be-developed intersection theory/Riemann-Roch inequality on the square of the arithmetic site.

### Key definitions

- s(f,g)=N(f * g~) with N of (18)
- arithmetic site (N^x, Z_max)
- Frobenius correspondence Psi(lambda)
- scaling site and quasi-tropical curve C_p=R_+^*/p^Z
- continuous dimension Dim_R

### Principal lemmas

- **THM-PAPER-0007-L1** (Lemma 2.1; Sec 2.3). Abstract Hodge-index type inequality s(x,x) <= 2 s(x,xi_0)s(x,xi_1) from isotropic pair xi_0, xi_1 with s(xi_0,xi_1)=1 and positivity-forces-nonorthogonality. — *Role:* Abstract skeleton of Weil's positivity step transposed to explicit formulas
- **THM-PAPER-0007-L2** (Def 4.1; Sec 4.3.1). Arithmetic site A = (N^ x, Z_max): the topos of N^x-sets with structure sheaf Z_max (tropical integers) with N^x acting by Frobenius k -> kn. — *Role:* Geometric space of the Riemann-Roch strategy
- **THM-PAPER-0007-L3** (Thm 4.2; Sec 4.3.1). Points of A over R^max_+ equal X_Q = Q^x \ A_Q / Z^x with Fr_lambda <-> idele action. — *Role:* Bridge between NCG and topos
- **THM-PAPER-0007-L4** (Thm 4.3; Sec 4.3.2). Riemann-Roch on C_p: Dim(H^0(D)) - Dim(H^0(-D)) = deg(D). — *Role:* Test of the quasi-tropical structure on periodic orbits

### Proof architecture

Essay with no new proofs. Sec 2 recalls Weil's proof (Riemann-Roch on C x C) and distills it into Lemma 2.1; Sec 3 formulates RH as negativity of s(f,f) (17) and discusses the 'minus sign' in explicit formulas versus the Selberg trace formula (absorption versus emission spectra); Sec 4 summarizes the arithmetic and scaling sites, Frobenius correspondences Psi(lambda), Riemann-Roch on periodic orbits; Sec 5 outlines Gamma-rings and topological cyclic homology as a route to a Weil cohomology. All technical results imported from Connes-Consani papers and Selberg/Weil/Li.

Dependency edges: CAND-01785 → CAND-01928 (summarizes (Thm 4.2, Psi(lambda))); CAND-01785 → CAND-01561 (summarizes NCG trace formula route)

**Imported results.** Weil positivity / Li criterion reductions [13,17,83]; Connes-Consani arithmetic site Thm 4.2 [37,38]; Scaling site Riemann-Roch Thm 4.3 [40]; Selberg trace formula [97,98]

**Techniques.** Weil explicit formula and positivity criterion; abstract Hodge-index inequality; Selberg trace formula comparison; nuclear-space trace formula on adele class space; topos of N^x-sets and tropical semirings; Newton polygon congruences; Segal Gamma-rings, topological cyclic homology (Hesselholt-Madsen)

## Context and interpretation

**Importance and obstacle overcome.** Clear conceptual map of the Weil-proof dictionary at the level of explicit formulas, isolating exactly the missing ingredient (Riemann-Roch inequality (12) on the square of A implying (17)) and relating the sign problem to absorption spectrum.

**Relation to prior work.** Summary of Connes-Consani (arithmetic site CAND-01928, scaling site [40]), Connes (1999), Connes-Consani-Marcolli (CAND-01561).

**Limitations and open questions.** Explicitly states the remaining gap: intersection theory and a Riemann-Roch inequality on the square of the arithmetic site (and a good H^j for j != 0, Serre duality). The author says it is unclear whether the framework is right for the final step. No new result about zeros.

## Research potential

- **Hypotheses that might be weakened.** The target Riemann-Roch inequality Dim H^0(D)+Dim H^0(-D) >= 1/2 D.D on the square of A: one could first test it for divisors D supported on finitely many periodic orbits C_p (where Thm 4.3 gives equality-type Riemann-Roch) as a restricted statement.
- **Generalizations.** Lemma 2.1 is purely linear-algebraic and applies to any symmetric form with an isotropic hyperbolic pair, so it can be used for any positivity problem on a space with a distinguished 'diagonal and Frobenius' pair (e.g. L-functions of other global fields).
- **Candidate connections.** Linking (17) with Li/Keiper coefficients and with the hyperring picture (CAND-01310); the continuous dimension Dim_R relative to type II dimension in matroid C*-algebras.
- **Reusable lemmas.** Lemma 2.1 (abstract Hodge index); formula (18) for N(h).
- **Possible experiments.** Numerically evaluate s(f,f) from (18) for explicit compactly supported test functions with zero mean and zero d^*u-mean, comparing with (17); check the sign pattern on finite-dimensional families (finite evidence only).
- **Risks / barriers.** No intersection theory on the square of the arithmetic site exists; failing to produce the positive-definite substitute for Serre duality; 'no Serre duality or good H^j for j != 0' (stated by author).

## Audit notes (Level 1 reader)

none noticed in inspected portion. Note the essay presents several results as heuristic or expected (the Riemann-Roch inequality (12) analog), not proved.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01785`; harvest queries: kw_RH_any, msc_11M06, msc_11M26, arxiv_explicit_formula, arxiv_rh_abs, arxiv_rh_ti.
- Triage decision: include — Connes essay on strategies to RH.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

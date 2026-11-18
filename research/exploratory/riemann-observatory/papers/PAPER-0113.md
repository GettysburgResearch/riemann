# PAPER-0113 — Noncommutative geometry and motives: the thermodynamics of endomotives

| Field | Value |
|---|---|
| Authors | Connes, Alain; Consani, Caterina; Marcolli, Matilde |
| Year / stratum | 2007 / S5 |
| Venue | Adv. Math. 214, No. 2, 761-831 (2007). |
| Identifiers | zbMATH [1125.14001](https://zbmath.org/?q=an:1125.14001) · DOI [10.1016/j.aim.2007.03.006](https://doi.org/10.1016/j.aim.2007.03.006) · arXiv [math/0512138](https://arxiv.org/abs/math/0512138) |
| MSC | 14A22, 14G10, 14C35, 14C25, 14G25, 14F43, 11G40, 81T15 |
| Families | D, E |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/math/0512138 |
| Selection | score 4.1388, in-pool citations 6, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Develop a category of (noncommutative) endomotives, extending Artin motives, and a cooling/distillation/dual-action procedure producing a representation of G x R_+^* (Galois x 'Frobenius in characteristic zero') on cyclic homology of a distilled Lambda-module, realizing the zeros of Riemann zeta and Dirichlet L-functions spectrally for the Bost-Connes system; also revisit the adele class space spectral realization (Weil positivity) and prove a Lefschetz formula for archimedean local factors.

**Historical motivation.** Realize Deninger's program (cohomological interpretation of zeros with Frobenius flow) and Connes' spectral realization within a motivic framework in which R_+^* x G plays the role of the Weil group; thermodynamics (type III, KMS) supplies the missing 'Frobenius in characteristic zero'.

### Main results

- **THM-PAPER-0113-1** (Theorem 3.13, theorem, scope: global; Sect. 3.3, Thm 3.13). The categories of algebraic endomotives $\mathcal E V^0_{K,E}$, Artin motives $\mathcal C V^0_{K,E}$, and analytic endomotives $C^*V^0_E$ are related: (1) $G\mapsto G(\bar K)$ gives a tensor functor $F:\mathcal E V^0_{K,E}\to C^*V^0_E$; (2) $\mathrm{Gal}(\bar K/K)$ acts by natural transformations of $F$; (3) Artin motives embed as a full subcategory of algebraic endomotives; (4) the composite $k\circ F:\mathcal E V^0_{K,E}\to KK\otimes E$ is well defined (statement partially read).
- **THM-PAPER-0113-2** (Lemma 4.3, lemma, scope: global; Sect. 4.1). If $\varphi$ is a regular extremal $KMS_\beta$ state on $\bar A$ whose GNS factor is of type $I_\infty$, there is an irreducible representation $\pi_\varphi$ on $H(\varphi)$ and an unbounded self-adjoint $H$ with $e^{-\beta H}$ trace class, $\varphi(x)=\mathrm{Trace}(\pi_\varphi(x)e^{-\beta H})/\mathrm{Trace}(e^{-\beta H})$ and $e^{itH}\pi_\varphi(x)e^{-itH}=\pi_\varphi(\sigma_t(x))$.
- **THM-PAPER-0113-3** (Theorem 4.16, theorem, scope: global; Sect. 4.3, Thm 4.16). For the Bost-Connes endomotive and a character $\chi$ of $\hat{\mathbb Z}^*$, the representation of $\mathbb R_+^*$ on $M=HC_0(p_\chi D(A,\varphi))$ realizes the zeros of $L_\chi$: for $z\in I_\beta$ viewed as character of $\mathrm{Hol}(I_\beta)$ with one-dimensional module $\mathbb C_z$, $M\otimes_{\mathrm{Hol}(I_\beta)}\mathbb C_z\ne\{0\}\iff L_\chi(-iz)=0$.
- **THM-PAPER-0113-4** (Theorem 5.5, theorem, scope: global; Sect. 5.1). The representation of $C_K$ on $H^1_{K,\mathbb C,\chi}=HC_0(H^1_{K,\mathbb C,\chi})$ gives the spectral realization of the zeros of the L-function with Grossencharakter $\chi$ (variant of Thm 1 of Connes 1999).
- **THM-PAPER-0113-5** (Theorem 5.6, theorem, scope: global; Sect. 5.2). For $f\in\mathcal S(C_K)$, the operator $\vartheta_m(f)=\int\vartheta_m(\gamma)f(\gamma)d^*\gamma$ on $H^1_{K,\mathbb C,\chi}$ is trace class with $\mathrm{Trace}(\vartheta_m(f)|_{H^1})=\sum_{L(\tilde\chi,\rho)=0,\ \rho\in\mathbb C/N^\perp}\hat f(\tilde\chi,\rho)$.
- **THM-PAPER-0113-6** (Theorem 5.7, theorem, scope: global; Sect. 5.2-5.3). For $h\in\mathcal S(C_K)$: $\mathrm{Trace}(\vartheta_m(h)|_{H^1})=\hat h(0)+\hat h(1)-\Delta\bullet\Delta h(1)-\sum_v\int'_{(K_v^*,e_{K_v})}\frac{h(u^{-1})}{|1-u|}d^*u$ (Lefschetz-type trace formula with explicit formula; statement as extracted, terms partly garbled).
- **THM-PAPER-0113-7** (Theorem 5.11, theorem, scope: global; Sect. 5.4 Weil positivity). The following are equivalent: (i) all L-functions with Grossencharakter on $K$ satisfy RH; (ii) $\mathrm{Trace}\,\vartheta_m(f\star f^\sharp)|_{H^1}\ge0$ for all $f\in\mathcal S(C_K)$, where $(f_1\star f_2)(g)=\int f_1(k)f_2(k^{-1}g)d^*g$ and $f^\sharp(g)=|g|^{-1}\bar f(g^{-1})$.
- **THM-PAPER-0113-8** (Theorems 7.4, 7.6, theorem, scope: global; Sect. 7.2-7.3). Lefschetz formula for archimedean local factors: for $K_v=\mathbb C$ (resp. $\mathbb R$, Weil group $W$), $m\in\mathbb N$, $z=\frac{1+m}{2}+is$: $\int'_{\mathbb C^*}\mathrm{Trace}(\pi(H^m,u))|u|_{\mathbb C}^{z}\frac{d^*u}{|1-u|_{\mathbb C}}=-2\,\Im\frac{d}{ds}\log L_{\mathbb C}(H^m,z)$ (resp. analogous over $W$).

### Key definitions

- analytic endomotive
- cooling morphism pi: A x_sigma R -> S(E_beta x R_+^*) (x) L^1
- distilled Lambda-module D(A,phi)
- dual action of R_+^* on HC_0
- H^1_{K,C,chi}

### Principal lemmas

- **THM-PAPER-0113-L1** (Proposition 4.12; Sect. 4.3). Assuming (4.26), the map Trace composed with pi defines a cyclic morphism (cooling to distilled module D(A,phi) = coker of Trace o pi). — *Role:* Distillation step producing the Lambda-module.
- **THM-PAPER-0113-L2** (Lemma 4.8, 4.9, 4.10, Cor 4.11; Sect. 4.2). Decay/analytic estimates (e.g. |Trace(g(H+c))|=O(e^{-beta c}c^{-N})) and for BC case with beta>1 on Hol(I_beta) acting on A_beta; elements of A_beta cap Ker tau. — *Role:* Analytic control making the cooling morphism well defined.
- **THM-PAPER-0113-L3** (Proposition 4.18; Sect. 4.5). For M type III_1 and lambda in ]0,1[, T=-ln2pi/lambda... M_T=M x_{sigma_T} Z is type III_lambda with Mod = lambda^Z and dual action of R_+^*/lambda^Z with fixed points M. — *Role:* Type III factors and unramified extensions: passage from III_1 to III_lambda mirrors unramified extension of finite fields.
- **THM-PAPER-0113-L4** (Proposition 4.15/Lemma 4.17; Sect. 4.4). Identification Omega-tilde_beta ~ hat Z^* x R_+^* ~ C_Q for beta>1; character-twisted trace expression. — *Role:* Matches the space of extremal KMS states with the idele class group of Q, connecting BC system to adele class space.
- **THM-PAPER-0113-L5** (Theorem 3.13 (4) / Props 3.1, 3.5, 3.7; Sect. 3). G acts canonically on X(K-bar); semigroup S acts by partial isomorphisms on projective limit X. — *Role:* Foundation of endomotive category.
- **THM-PAPER-0113-L6** (Proposition 5.10; Sect. 5.3). For K the function field of a curve C over F_q the (adelic) trace formula holds (statement not fully read). — *Role:* Consistency check in positive characteristic.

### Proof architecture

Sections 2-3 build the categories (KK-theory and Lambda-modules; Artin motives, algebraic then analytic endomotives; Bost-Connes system as example) and prove compatibility of correspondences with KK. Section 4: for KMS_beta states with beta above critical, type I implies representations pi_{eps,H}; cooling gives morphism A x_sigma R -> S(E_beta x R_+^*) (x) L^1; distillation takes the cokernel of Trace o pi to get D(A,phi); dual action of R_+^* on HC_0(D) gives spectrum; Thm 4.16 identifies it with zeros of L_chi for BC. Section 5 identifies the same structure with Connes' adele class space representation (Thm 5.5), proves the trace formula (Thms 5.6, 5.7) and Weil positivity equivalence with GRH (Thm 5.11). Sections 6-7: higher-dimensional correspondences, K-theory, and Lefschetz formula for archimedean local factors via Weil-form logarithmic derivatives.

**Imported results.** Bost-Connes KMS phase transition (Bost-Connes 1995); Connes 1999 trace formula for adele class space (CAND-00726); Weil explicit formula and Weil positivity criterion; Serre archimedean local factors; Takesaki/Connes classification of type III factors, Tomita-Takesaki modular theory

**Techniques.** Bost-Connes system and KMS states; type III factors and modular theory; cyclic (co)homology and Lambda-modules; KK-theory correspondences; Artin motives and Galois actions; Weil explicit formula as Lefschetz trace formula; Gamma-factor logarithmic derivatives (Serre local factors)

## Context and interpretation

**Importance and obstacle overcome.** Gives a functorial recipe (endomotive -> representation of G x R_+^*) reproducing zeros of zeta and abelian Artin L-functions, linking Connes' adele class space to the BC system and motives; also puts Weil positivity in a trace-formula form (Thm 5.11). Obstacle: making cooling/distillation rigorous for type III KMS data; the RH remains equivalent to positivity (open).

**Relation to prior work.** Builds on Bost-Connes 1995, Connes 1999 (CAND-00726), Connes-Marcolli 'Q-lattices', Meyer (CAND-01282), Deninger's program.

**Limitations and open questions.** RH not addressed beyond equivalence (Thm 5.11). Assumption (4.26) required for the distilled module; full Lefschetz formula for several places (archimedean plus non-archimedean) needs a theory combining NC spaces and motives (Sect. 7.4 'The question of the spectral realization'); cohomological detail deferred to forthcoming work [15].

## Research potential

- **Hypotheses that might be weakened.** Assumption (4.26) and type I of extremal KMS states: test whether weaker (e.g. type II or non-regular) hypotheses still give nonzero M; Thm 4.16 for beta>1 only.
- **Generalizations.** Replace BC by imaginary quadratic BC systems or GL_2 systems for L-functions of modular forms; extend Thm 7.4/7.6 to products over all places (Lefschetz formula for global L-function).
- **Candidate connections.** Connes trace formula (CAND-00726), Meyer representation (CAND-01282), Deninger flow program, Weil positivity/Li criterion; Thm 5.11 positivity of Trace theta_m(f * f^sharp) is testable numerically.
- **Reusable lemmas.** Lemma 4.3 (KMS_beta states give Trace(pi(x)e^{-beta H})), Lemma 4.8 decay estimates, Thm 7.4/7.6 archimedean Weil-form log-derivative formula.
- **Possible experiments.** Numerically evaluate Weil quadratic form Trace(theta(f*f^sharp)) via explicit formula for Gaussian-type f at K=Q; verify Thm 7.4 for m=1 using Gamma log-derivative.
- **Risks / barriers.** Positivity (Thm 5.11) equivalent to GRH; type III machinery hard to quantify; cyclic homology of distilled module not computed beyond spectrum identification.

## Audit notes (Level 1 reader)

Extraction garbles formulas in Thm 5.7 (term 'Delta bullet Delta h(1)' and index of sums) and Prop 4.18 (T=-ln2pi/lambda appears garbled; likely T=-2pi/ln lambda). Not verified against the published version. none else noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01520`; harvest queries: kw_RH_any, kw_trace_formula_zeta, kw_zeta_zeros, arxiv_zeta_zeros.
- Triage decision: include — Noncommutative geometry cohomological interpretation of spectral realization of L-function zeros.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

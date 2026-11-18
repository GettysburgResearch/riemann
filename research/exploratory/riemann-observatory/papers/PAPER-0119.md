# PAPER-0119 — The Weil proof and the geometry of the adelès class space

| Field | Value |
|---|---|
| Authors | Connes, Alain; Consani, Caterina; Marcolli, Matilde |
| Year / stratum | 2009 / S5 |
| Venue | Tschinkel, Yuri (ed.) et al., Algebra, arithmetic, and geometry. In honor of Yu. I. Manin on the occasion of his 70th birthday. Vol. I. Boston, MA: Birkhäuser (ISBN 978-0-8176-4744-5/hbk; 978-0-8176-4745-2/ebook). Progress in Mathematics 269, 339-405 (2009). |
| Identifiers | zbMATH [1208.11108](https://zbmath.org/?q=an:1208.11108) · DOI [10.1007/978-0-8176-4745-2_8](https://doi.org/10.1007/978-0-8176-4745-2_8) · arXiv [math/0703392](https://arxiv.org/abs/math/0703392) |
| MSC | 11M55, 58B34, 11M26, 46L55 |
| Families | D, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/math/0703392 |
| Selection | score 4.0755, in-pool citations 5, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Build a tentative dictionary between Weil's proof of RH for function fields (curves, divisors, correspondences, explicit formula, Riemann-Roch positivity, Frobenius) and the noncommutative geometry of the adele class space X_K = A_K/K^*; identify analogues of Frobenius (scaling action), degree, self-intersection of the diagonal, trivial correspondences, and algebraic points of the curve (via valuation systems / periodic orbits), leaving the analogue of principal divisors and Riemann-Roch open.

**Historical motivation.** Weil's 1940s proof for curves (Riemann-Roch on C x C, positivity of intersection), Connes 1999 trace formula (absorption spectrum), Connes-Marcolli endomotives and Bost-Connes system, 2007 dedication to Manin.

### Main results

- **THM-PAPER-0119-1** (Thm 4.16, theorem, scope: global; Sec 4.5, eq (4.40)). For K a global field and any $f\in\mathcal S(C_K)$, the operator $\vartheta_m(f)$ acting on $H^1(\mathbb A_K/K^*,C_K)$ is of trace class and $\mathrm{Tr}(\vartheta_m(f)|H^1)=\sum_{\rho\in\mathbb C/N^\perp,\ L(\tilde\chi,\rho)=0}\hat f(\tilde\chi,\rho)$ (all zeros, including off-critical, with multiplicity as in the setting of Meyer's nuclear spaces).
- **THM-PAPER-0119-2** (Thm 6.1, theorem (recalled from [11]), scope: global; Sec 6.1, eq (6.3)). $\mathrm{Tr}(\vartheta_m(f)|H^1)=\hat f(0)+\hat f(1)-(\log|a|)f(1)-\sum_{v\in\Sigma_K}\int'_{(K_v^*,e_{K_v})}\frac{f(u^{-1})}{|1-u|}d^*u$, with $|a|$ the module of the differential idele (log|a| = -log of discriminant for number fields; $=(2-2g)\log q$ analogue in function fields) and principal values taken w.r.t. $e_{K_v}$.
- **THM-PAPER-0119-3** (Prop 6.2 / Cor 6.3, proposition (reformulation of Weil's criterion), scope: global; Sec 6.2, (6.10)-(6.12)). All L-functions with Grossencharakter on K satisfy RH iff $\langle\Delta^{-1/2}f,\Delta^{-1/2}f^*\rangle\ge0$ for all $f\in\mathcal S(C_K)$, where $f^*(g)=f(g^{-1})$, $\Delta_z f(g)=|g|^zf(g)$; equivalently $\langle f,f^\sharp\rangle\ge 0$ with $f^\sharp(g)=|g|^{-1}f(g^{-1})$, pairing $\langle f_1,f_2\rangle=\mathrm{Tr}(\vartheta_m(f_1\star f_2)|H^1)$ (eq 4.47).
- **THM-PAPER-0119-4** (Lemma 4.17 + Prop 6.4, lemma/proposition, scope: global; Sec 4.5, 6.2). If f lies in V = range of Tr∘rho (restriction from adeles), then $\vartheta_m(f)|_{H^1}=0$ (because V is a convolution ideal and C_K is commutative); hence $\langle f,f^\sharp\rangle=0$ on V and by adding elements of V one can make $f\star f^\sharp(1)=\int_{C_K}|f(g)|^2|g|d^*g<\epsilon$ for any $\epsilon>0$ (surjectivity of E, App. 1 of [10]).
- **THM-PAPER-0119-5** (Prop 7.2, proposition, scope: global; Sec 7.2, eq (7.6)). RH for all Grossencharakter L-functions on K is equivalent to the Weil-type estimate $Z(f)\bullet_{trans}Z(f)\le 2d(Z(f))d'(Z(f))-\Delta\bullet\Delta\,(f\star f^\sharp)(1)$ for all f in S(C_K), where Z(f)=correspondence attached to f, with $\log|a|$ interpreted as $-\Delta\bullet\Delta\log q$ analogue (self-intersection of diagonal). *Conditional on:* Weil positivity criterion.
- **THM-PAPER-0119-6** (Thm 8.11, theorem, scope: global; Sec 8.2, Thm 8.11). For y in X_{K,v}, the representation $\pi_y$ of the groupoid C*-algebra of the v-valuation system is a positive-energy representation iff $y\in\Xi_{K,v}$ (the locus of adeles with y_w!=0 and |y_w|=1 for almost all w).
- **THM-PAPER-0119-7** (Thm 8.15, theorem, scope: global; Sec 8.4, eq (8.32)-(8.33)). For the C*-dynamical system $(C^*(G(p)),\sigma^p_t)$ over K=Q: (1) pi_y positive energy for y in A*_{Q,p}; (2) for $y_\infty=\lambda^{-1}$, $\lambda\in(1,p]$ the partition function is $Z_p(\lambda,\beta)=2\frac{1-p^{-\beta}}{1-p^{1-\beta}}f_p(\lambda,\beta)$; (3) the functionals $\psi_{\beta,y}(a)=\mathrm{Tr}(e^{-\beta H_y}\pi_y(a))$ are KMS_beta states depending weakly continuously on y.

### Key definitions

- Adele class space $X_K=\mathbb A_K/K^*$ (Def 4.1)
- $H^1(\mathbb A_K/K^*,C_K)$ = cokernel of restriction map of cyclic modules (Def 4.10)
- V = range of Tr∘rho in S(C_K) (Def 4.14)
- involution $f^\sharp(g)=|g|^{-1}f(g^{-1})$ (6.9)
- valuation systems $\Xi_{K,v}$ and groupoid G(v) (Sec 8)

### Principal lemmas

- **THM-PAPER-0119-L1** (Prop 4.13; Sec 4.5). The representation of C_K on $H^1_\chi(\mathbb A_K/K^*,C_K)$ gives the spectral realization of the zeros of L(chi,.) (all zeros, via Meyer's nuclear function spaces; variant of Cor 2 of [10]). — *Role:* Spectral side of the trace formula
- **THM-PAPER-0119-L2** (Lemma 4.17; Sec 4.5). For f in V, theta_m(f) vanishes on H^1. — *Role:* Source of the large radical of the trace pairing (analogue of trivial correspondences)
- **THM-PAPER-0119-L3** (Prop 8.21; Sec 8.5). The projection from the lifted locus $\tilde\Xi_{\mathbb Q}$ to $\Xi_{\mathbb Q}$ is surjective; two elements of the same v-component have the same image in $C_{\mathbb Q}$ iff they lie on one orbit of T (Tx=px at p, Tx=-x at infinity). — *Role:* Identification of periodic orbits / classical points
- **THM-PAPER-0119-L4** (Prop 8.22; Sec 8.6). Algebra B generated by the functions phi_a, psi_a; defines N(f)=... counting-function type expression on the cover. — *Role:* Arithmetic subalgebra, Frobenius and monodromy
- **THM-PAPER-0119-L5** (Lemma 10.1; Sec 10.1). Exact sequence $0\to C(T_j)\otimes\mathcal K\to A_j\to C^*(U)\to0$ for two real places model, with A the fibered product of A_j over C*(U). — *Role:* Vanishing-cycles analogy (Sec 10)

### Proof architecture

Expository/programmatic. Sec 2 recalls Weil's proof (correspondences, explicit formula, Riemann-Roch positivity via d(Z)d'(Z)-type bound, 2.4 dictionary). Secs 4-6 reformulate the Connes trace formula in Meyer's nuclear setting, giving the cohomological Lefschetz formula (6.3), and recast Weil positivity as <f,f^sharp> >= 0 (Prop 6.2/Cor 6.3) with the key observation that the form has a large radical V (Lemma 4.17, Prop 6.4) mimicking trivial correspondences. Sec 7 matches degree/codegree/self-intersection of diagonal with terms in (6.3), giving the intersection-theoretic restatement (Prop 7.2). Sec 8 builds valuation-system C*-dynamical systems (Thm 8.11, 8.15) producing 'classical points' as KMS states. Sec 9 treats functoriality/Weil group transfer, Sec 10 an analogy with vanishing cycles. Imported: Weil's positivity criterion [41], Meyer's nuclear analysis [32], trace formula [10,11], Bost-Connes [5].

Dependency edges: CAND-01561 → Connes 1999 trace formula (reformulates in cohomological form); CAND-01561 → Weil positivity criterion (imports and rephrases (Prop 6.2)); CAND-01561 → CAND-01928 (precursor of arithmetic site framework); CAND-01561 → CAND-01310 (precursor of hyperring/absolute arithmetic framework)

**Imported results.** Weil positivity criterion for Grossencharakter L-functions (Weil, Sur les formules explicites); Connes trace formula and Meyer's nuclear-space version; Weil's proof of RH for function fields (Weil, Mattuck-Tate, Grothendieck); Bost-Connes system KMS structure

**Techniques.** cyclic homology of cyclic modules and cokernel of restriction map; Meyer nuclear (Schwartz) function spaces and distributional traces; Weil explicit formula and Weil positivity criterion; Bost-Connes endomotive and KMS states / quantum statistical mechanics; groupoid C*-algebras and positive-energy representations; type II/III duality and scaling action as Frobenius analogue; intersection theory dictionary (degree, codegree, diagonal)

## Context and interpretation

**Importance and obstacle overcome.** Provides the clearest bridge between the Weil-proof architecture and the trace formula, showing that positive-definiteness on the quotient by the radical V is the exact obstruction, and that the nuclear-space version makes all zeros (not only critical) spectral. Overcomes the 'critical-zeros-only' limitation of the Hilbert-space spectral realization at the cost of losing positivity for free.

**Relation to prior work.** Builds on Connes [10] (Selecta 1999 spectral realization), Connes-Consani-Marcolli [11] (Noncommutative geometry and motives / endomotives), Meyer [32], Weil [41]; later superseded in programme by Connes-Consani arithmetic site / scaling site and hyperring papers.

**Limitations and open questions.** Does not prove RH or any new positivity. The analogue of principal divisors and a Riemann-Roch / Hodge-index replacement is explicitly missing (intro: 'leaves open the more difficult question'). The positivity <f,f^sharp> >= 0 is only restated. The dictionary is self-described as tentative. Functoriality/vanishing-cycle sections are sketches/analogies.

## Research potential

- **Hypotheses that might be weakened.** Prop 6.4(2) shows the diagonal term f*f^sharp(1) can be driven below any epsilon within a coset of V; the Weil positivity then is a statement about the quotient form. Testing whether a finite-dimensional or restricted-support subspace (e.g. f supported in |g| in [1,Lambda]) already forces the inequality gives a weaker, checkable hypothesis.
- **Generalizations.** Prop 6.2/7.2 are stated for arbitrary global fields K; the function-field case should reproduce Weil's proof, giving a testbed to identify the missing 'principal divisor' analogue via Prop 8.13 (Frobenius orbits).
- **Candidate connections.** Link to Meyer's nuclear-space trace and to Weil positivity numerics for Q (finite test functions); relation with Li/Keiper positivity and with the arithmetic-site scaling correspondences Psi(lambda) of CAND-01928.
- **Reusable lemmas.** Lemma 4.17 (convolution-ideal vanishing) and Prop 6.4(2) (radical absorbs diagonal term) are reusable for any positivity-on-quotient formulation; Thm 6.1 gives explicit local principal-value terms.
- **Possible experiments.** Numerically evaluate the quadratic form f -> Tr(theta_m(f*f^sharp)) from (6.3) on compactly supported test functions of C_Q modulo V; check sign for small families and compare with Weil's explicit formula with known zeros (verification only, finite scope).
- **Risks / barriers.** Positivity of a form on a quotient with a huge radical has no known Hilbert-space structure; Hodge-index analogue missing; all numerical checks are finite and cannot be global evidence.

## Audit notes (Level 1 reader)

Eq (6.8) as printed reads Delta_z(f*h)=Delta_z(f)*Delta_z(f); the second factor should be h (typo, Sec 6.2). Prop 6.2 proof is a one-line reduction to Weil [41]. Sections 8-10 were only skimmed at the level of statements, not verified.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01561`; harvest queries: kw_RH_any, kw_trace_formula_zeta, kw_weil_positivity, kw_zeta_zeros, msc_11M26, arxiv_connes_rh, arxiv_explicit_formula, arxiv_function_field_rh, arxiv_rh_abs, arxiv_weil_explicit, arxiv_zeta_zeros.
- Triage decision: include — Weil proof analogies for adeles class space.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

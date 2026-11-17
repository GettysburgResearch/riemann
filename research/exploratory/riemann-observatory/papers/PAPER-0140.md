# PAPER-0140 — Langlands' conjecture for GL(2) over functional fields

| Field | Value |
|---|---|
| Authors | Drinfeld, V. G. |
| Year / stratum | 1980 / S3 |
| Venue | Proc. int. Congr. Math., Helsinki 1978, Vol. 2, 565-574 (1980). |
| Identifiers | zbMATH [0444.12004](https://zbmath.org/?q=an:0444.12004) |
| MSC | 11R39, 14F05, 11F12 |
| Families | E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1978.2/ICM1978.2.ocr.pdf |
| Selection | score 2.7799, in-pool citations 6, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Prove Langlands' conjecture for GL(2) over a global function field k of characteristic p>0: a bijection between compatible systems of 2-dimensional irreducible lambda-adic Galois (Weil group) representations and cuspidal automorphic representations of GL_2(A), using moduli of F-sheaves (shtukas) and the Selberg trace formula. (A sketch, not a full proof.)

**Historical motivation.** Langlands' 1970s conjectural correspondence; for GL(2) over function fields, Eichler-Shimura for modular curves has no direct analogue, so Drinfeld introduces elliptic modules (1974-77) and then shtukas, covering the full cuspidal spectrum rather than just those with a discrete series component.

### Main results

- **THM-PAPER-0140-1** (Theorem A (Langlands' conjecture), theorem (announced, proof sketched), scope: global; Introduction 0.1-0.2, p.565-566). Let $k$ be a global field of characteristic $p>0$. Let $\Sigma_1$ be the set of isomorphism classes of compatible systems of absolutely irreducible 2-dimensional $\lambda$-adic representations of the Weil group $W$ of $k$ ($\lambda\nmid\infty p$, over number fields $E\subset\bar{\mathbb Q}$, $\Sigma_1=\varinjlim\Sigma_1(E)$) and $\Sigma_2$ the set of isomorphism classes of irreducible representations of $GL(2,\mathbb A)$ occurring in the space of cusp forms. Then $\Gamma=\{(\varrho,\pi)\in\Sigma_1\times\Sigma_2:\pi$ compatible with $\varrho\}$ is the graph of a bijection $\Sigma_1\to\Sigma_2$. Compatibility: for almost all places $v$, $L(s-\tfrac12,\pi_v)=[\det(1-F_vq_v^{-s},\varrho_\lambda)]^{-1}$ (Jacquet-Langlands L).
- **THM-PAPER-0140-2** (Theorem B (Petersson's conjecture), theorem, scope: global; 0.2, p.566). For an irreducible unitary representation $\pi$ of $GL(2,\mathbb A)$ occurring in the space of cusp forms, for every place $v$ of $k$ the local component $\pi_v$ does not belong to the complementary series.
- **THM-PAPER-0140-3** (Theorem C (Riemann hypothesis for $L(s,\pi)$, partly conditional), theorem, scope: conditional; 0.2, p.566; proof sketch 4.3, p.573). Let $\pi$ be as in Theorem B. Suppose either that one of the local components of $\pi$ belongs to the discrete series, or that every field finitely generated and of transcendence degree 3 over $\mathbb F_p$ has a smooth projective model (resolution of singularities in dimension 3). Then all zeros of $L(s,\pi)$ lie on the line $\mathrm{Re}\,s=\tfrac12$. *Conditional on:* resolution of singularities for 3-folds over F_p (second alternative).
- **THM-PAPER-0140-4** (Theorem A', theorem, scope: global; 0.3, p.566). For each $\pi\in\Sigma_2$ there exist a number field $E$ containing the field of definition of $\pi$ and 2-dimensional $\lambda$-adic representations $\varrho_\lambda$ of $W$ (for all places $\lambda$ of $E$ not dividing $\infty p$) such that for almost all $v$ and all $\lambda$: $L(s-\tfrac12,\pi_v)=\det(1-F_vq_v^{-s},\varrho_\lambda)^{-1}$. Theorem A follows from A' (0.3).
- **THM-PAPER-0140-5** (Theorem 4.1, theorem (cohomological), scope: global; Sec.4.1, p.572). With $V_i^{cusp}$ the cuspidal part of $\varinjlim_D\,[\prod_n \varinjlim H^i_c(\mathcal N^{2,n}_D\otimes K,\mathbb Q_l)]$, one has $V_1^{cusp}\otimes\bar{\mathbb Q}_l=\bigoplus_{\pi\in\Sigma_2^J}\varrho_\pi\otimes\pi^\vee\otimes\pi$-type decomposition as a representation of $W\times W\times GL(2,\mathbb A)$, where $\Sigma_2^J=\{\pi:\pi|_J$ trivial$\}$ and $\varrho_\pi$ is a 2-dimensional representation of $W$ over $\bar{\mathbb Q}_l$ compatible with $\pi$ (precise form is garbled in OCR).
- **THM-PAPER-0140-6** (Theorem 1.1, theorem, scope: global; Sec.1.2, p.568). For every finite subscheme $D\subset X$ and $d\ge1$ the coarse moduli scheme of left (right) F-sheaves of rank d with level D structure exists.
- **THM-PAPER-0140-7** (Theorem 2.1, theorem, scope: global; Sec.2.3, p.570). The category of constructible locally constant PF-sheaves of sets on $(X-D)^2$ is equivalent to the category of finite $\pi_1(X-D)\times\pi_1(X-D)$-sets.

### Key definitions

- F-sheaf (left/right) over S of rank d: locally free sheaf with map between (id x Fr_S)^*F and F whose cokernel is supported on the graphs of zero alpha and pole beta
- level D structure
- degenerate (alpha,beta)-F-sheaf and degenerator
- R-category (schemes localized at radical morphisms)
- compatible system of lambda-adic reps

### Principal lemmas

- **THM-PAPER-0140-L1** (Theorem 1.2; Sec.1.2, p.568). There exist open subschemes $U_i\subset M^d_D$ with $U_i\subset U_{i+1}$, $\bigcup U_i=M$, each a quotient of a smooth quasiprojective scheme over $(X-D)^2$ of relative dimension $2d-2$ by a finite group. — *Role:* exhausts the non-quasicompact moduli space of F-sheaves
- **THM-PAPER-0140-L2** (Theorem 2.2 (d=1, Lang); Sec.2.4, p.570). For $d=1$, $V_i\otimes\bar{\mathbb Q}_l=\bigoplus_{\chi\in\mathrm{Hom}(\mathrm{Pic}_DX/J,\bar{\mathbb Q}_l^*)}\varrho_\chi\boxtimes\varrho_\chi^{-1}\otimes\chi$ type decomposition, with $\varrho_\chi\in\mathrm{Hom}(\pi_1(X-D),\bar{\mathbb Q}_l^*)$ compatible with $\chi$ (class field theory realized geometrically). — *Role:* model case of the whole method
- **THM-PAPER-0140-L3** (Theorem 3.1; Sec.3.1, p.571). $\mathcal N^{m,n}_D$ is a quasiprojective surface; if $2m-n\ge2$ the complement of $\mathcal N^{m,n}\otimes K$ in the neighbouring piece is a countable disjoint sum of affine lines. — *Role:* describes non-quasicompactness and boundary strata
- **THM-PAPER-0140-L4** (Compactification (3.2)(1)-(7); Sec.3.2-3.4, p.571-572). For $2m-n\ge2$, $\mathcal N^{m,n}_D$ has a canonical compactification $\overline{\mathcal N}^{m,n}_D$ proper normal algebraic space over K; the fibres of a resolution of singularities have $H^0=\bar{\mathbb Q}_l$, $H^1=0$ (trees of rational curves); boundary $\Gamma^{m,n}_D$ described via degenerate F-sheaves (Sec.3.4); for D=0 it is isomorphic as an object of the R-category to $Y^{...}\otimes K$. — *Role:* controls boundary contribution in the trace formula comparison
- **THM-PAPER-0140-L5** (Lemma/construction 4.2; Sec.4.2, p.573). Proof of Theorem 4.1 combines Lefschetz fixed-point formula, Selberg trace formula and an explicit description of $\mathcal N_D(\mathbb F_q)$ analogous to Deuring's results on elliptic curves over F_p. — *Role:* core comparison of two trace formulas

### Proof architecture

Reduce A to A' (0.3): A' gives rho_lambda; compatibility of the system follows from [Deligne] using Weil conjectures; surjectivity of Gamma->Sigma_1 is Deligne's (via Jacquet-Langlands/Weil converse [5]); injectivity by strong multiplicity one and Chebotarev. For A': build moduli schemes M of rank-2 F-sheaves (shtukas) with level D structure and two legs (zero, pole) over (X-D)^2, define Frobenius-like correspondences F_1,F_2 and a GL(2,A) action; for rank 1 this recovers Lang's class field theory as Pic-torsor (Sec.2). For rank 2, quasi-compactness fails; one passes to open pieces N^{m,n}, compactifies them (Sec.3), and computes cohomology H^*_c of the generic fibre over K=Frac(k x k) as a W x W x GL(2,A)-module. The key Theorem 4.1 identifies the cuspidal part with a sum over pi of a 2-dim W-rep tensor pi, proved by the Lefschetz trace formula against the Selberg trace formula (the structure of Selberg trace formula matches the geometry of the moduli, e.g. the integral of f(s) d ln L(s) is why one needs the surface over X x X). Theorems B and C follow from analyzing the zeta function of an open subscheme of the moduli space: poles of zeta of a surface lie on Re s=0,1/2,1,2 (Weil conjectures proved by Deligne + Abhyankar resolution of singularities for surfaces) giving B; for 3-folds, if resolution holds, zeros/poles lie on Re s=n/2 giving second alternative of C; the first alternative follows from earlier papers [2],[3] (Drinfeld, Elliptic modules I,II) where rho_pi appears in H^1 of a surface of elliptic-module type.

Dependency edges: CAND-00651 → Deligne 1973 Les constantes des equations fonctionnelles (imports surjectivity); CAND-00651 → Drinfeld Elliptic modules I, II (extends); CAND-00651 → Jacquet-Langlands 1970 (uses L-functions)

**Imported results.** Deligne 1973 Les constantes des equations fonctionnelles (surjectivity onto Sigma_1); Jacquet-Langlands 1970 Automorphic forms on GL(2); Weil conjectures (Deligne 1974/1980) and Abhyankar resolution of surface singularities; Chebotarev density theorem, strong multiplicity one for GL(2); Drinfeld, Elliptic modules I, II (Mat. Sb. 94, 102); Ihara, Langlands, Kottwitz-style trace formula comparison cited as [6,8]

**Techniques.** moduli of F-sheaves (shtukas) of rank 2 with level structure; Lefschetz fixed point formula vs Selberg trace formula; compactification and boundary of non-quasicompact moduli; Weil conjectures (Deligne), Abhyankar resolution for surfaces; Lang's geometric class field theory as the d=1 case; Eichler-Shimura analogy via elliptic modules

## Context and interpretation

**Importance and obstacle overcome.** First proof of global Langlands for GL(2) in positive characteristic; Theorem C yields the Riemann hypothesis for all L(s,pi) of GL(2)-cusp forms when a discrete series component exists (conditional on resolution in dim 3 in general). The obstacle is non-quasicompactness of moduli of shtukas and the matching of geometric and Selberg trace formulas.

**Relation to prior work.** Extends Drinfeld's Elliptic modules I, II (discrete series case) and Lang; relies on Deligne's constants; analogy with Eichler-Shimura, Ihara; parallel with Burchnall-Chaundy-Baker-Krichever for commutative subrings (Drinfeld, Funct. Anal. Appl. 11).

**Limitations and open questions.** It is only a sketch (report, ICM 1978). Theorem C in general needs resolution of singularities in dimension 3 in characteristic p (open then); the analogous number-field Riemann hypothesis remains out of reach.

## Research potential

- **Hypotheses that might be weakened.** The resolution-of-singularities hypothesis in Theorem C: investigate whether the specific 3-fold (open subscheme of N_D x (X x v)) can be handled by a direct argument (e.g. Weil-type purity for this particular family) to remove the condition for non-discrete-series pi.
- **Generalizations.** Rank d via F-sheaves of rank d (Sec.1 is set up for general d; later extended by Drinfeld and Lafforgue); other function field L-functions where RH is proved geometrically.
- **Candidate connections.** Function-field RH for automorphic L-functions as a model for the RH for GL(2) over Q; Selberg trace formula vs Lefschetz as a template for a trace-formula explanation of zeros.
- **Reusable lemmas.** Theorem 2.1 (PW-sheaves / sheaves on products with partial Frobenius vs pi_1 x pi_1).
- **Possible experiments.** Count points of N_D(F_q) for small q, small genus X and compare with Hecke eigenvalues (explicit Deuring-style verification) to check Theorem 4.1 numerically in the genus 0 case.
- **Risks / barriers.** No number-field analogue of shtukas; finite characteristic geometry (Frobenius structure) is essential for RH.

## Audit notes (Level 1 reader)

Report-level sketch: Theorem 4.1 statement and several formulas are garbled in OCR and I could not verify their exact form. The Theorem C second alternative depends on a hypothesis (resolution in dim 3) that was open in 1978. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00651`; harvest queries: kw_function_field_rh.
- Triage decision: include — Drinfeld's Langlands for GL(2) over function fields, major function-field result.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

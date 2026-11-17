# PAPER-0117 — Spectral triples and \(\zeta\)-cycles

| Field | Value |
|---|---|
| Authors | Connes, Alain; Consani, Caterina |
| Year / stratum | 2023 / S6 |
| Venue | Enseign. Math. (2) 69, No. 1-2, 93-148 (2023). |
| Identifiers | zbMATH [1537.11121](https://zbmath.org/?q=an:1537.11121) · DOI [10.4171/LEM/1049](https://doi.org/10.4171/LEM/1049) · arXiv [2106.01715](https://arxiv.org/abs/2106.01715) |
| MSC | 11M55, 11M06, 46L87, 58B34 |
| Families | C, D |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/2106.01715 |
| Selection | score 4.1139, in-pool citations 3, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Why does the semi-local Weil quadratic form on [lambda^{-1},lambda] have extremely small eigenvalues, and can a prolate-vector-perturbed Dirac operator on the circle reproduce zeta zeros? The conceptual answer is the zeta-cycle: a circle whose scaling spectrum on the orthogonal complement of Sigma_mu E(S_0^ev) consists of critical-zero ordinates.

**Historical motivation.** Weil positivity on supports in [lambda^{-1},lambda] for all lambda is equivalent to RH; numerics showed surprisingly tiny eigenvalues (1e-48 at lambda^2=11), explained here by prolate functions and distilled into zeta-cycles.

### Main results

- **THM-PAPER-0117-1** (Definition 1.1 / 6.1, definition, scope: global; Sections 1, 6.2). A zeta-cycle is a circle $C_\mu=\mathbb R_+^*/\mu^{\mathbb Z}$, $L=\log\mu$, such that $\Sigma_\mu E(\mathcal S_0^{ev})$ is not dense in $L^2(C_\mu,d^*u)$, where $E(f)(x)=x^{1/2}\sum_{n>0}f(nx)$, $\Sigma_\mu g(u)=\sum_{k\in\mathbb Z}g(\mu^ku)$, $\mathcal S_0^{ev}$ = real even Schwartz functions with $f(0)=0=\int f$.
- **THM-PAPER-0117-2** (Theorem 1.1 = Theorem 6.4, theorem, scope: global; Section 6.2). (i) For a zeta-cycle $C$, the spectrum of the scaling action of $\mathbb R_+^*$ on the orthogonal complement of $\Sigma_\mu E(\mathcal S_0^{ev})$ in $L^2(C)$ consists of imaginary parts $s$ of zeros $\tfrac12+is$ of $\zeta$ on the critical line. (ii) Conversely if $s>0$ and $\zeta(\tfrac12+is)=0$, any circle of length an integer multiple of $2\pi/s$ is a zeta-cycle and its spectrum contains $is$.
- **THM-PAPER-0117-3** (Corollary 6.5, corollary, scope: global; Section 6.2). With $Z$ the set of ordinates of critical zeros: $H(L)=(\Sigma_\mu E(\mathcal S_0^{ev}))^\perp\ne\{0\}\iff\exists s\in Z,n\in\mathbb Z$ with $sL=2\pi n$.
- **THM-PAPER-0117-4** (Proposition 6.3, proposition, scope: global; Section 6.2). The $n$-fold cover of a zeta-cycle of length $L$ is a zeta-cycle of length $nL$.
- **THM-PAPER-0117-5** (Lemma 6.1, lemma, scope: global; Section 6.1). If $f$ has bounded variation on $(0,\infty)$, is rapidly decaying at $\infty$, $O(u^2)$ at $0$, and $\int_0^\infty f=0$, then $E(f)(u)$ is pointwise defined, $O(u^{1/2})$ as $u\to0$, rapidly decaying at $\infty$, and $\Sigma_\mu E(f)$ converges geometrically to a bounded measurable function.
- **THM-PAPER-0117-6** (Sections 1-5 (numerical), numerical finding, scope: computational; Section 1; Sections 2.5, 4, 5; Figs 1-3, 54). For $\lambda^2=11$ the smallest positive eigenvalue of the Weil form $Q^W_\lambda$ on $L^2([\lambda^{-1},\lambda],d^*u)$ is $2.389\times10^{-48}$; eigenvectors are approximated by prolate vectors from $E(\hat\psi_{m,\lambda})$, $m\le\nu(\lambda^2)\sim2\lambda^2$. For $D(\lambda,k)=(1-\Pi)D_0(1-\Pi)$, $D_0=-iu\partial_u$, eigenvalues become $k$-independent at special $\lambda$ and then equal zeta ordinates; first 31 zeros reproduced for $5\le\lambda^2\le16.5$ (authors estimate random-agreement probability ~$10^{-50}$).

### Key definitions

- $Q^W(f,g)=\sum_{1/2+is\in Z}\hat f(\bar s)\overline{\hat g(s)}$
- $E(f)(x)=x^{1/2}\sum_{n>0}f(nx)$
- $\Sigma_\mu$
- zeta-cycle
- $D(\lambda,k)=(1-\Pi)D_0(1-\Pi)$

### Principal lemmas

- **THM-PAPER-0117-L1** (Lemma 6.2; Section 6.1). $\mathcal S_0^{ev}$ is scaling invariant; $E\circ\lambda^{-1/2}\vartheta(\lambda)=\vartheta(\lambda)\circ E$, $\vartheta(\lambda)\Sigma_\mu=\Sigma_\mu\vartheta(\lambda)$; scaling induces an action of $\mathbb R_+^*/\mu^{\mathbb Z}$ on $\Sigma_\mu E(\mathcal S_0^{ev})$. — *Role:* Makes the complement a unitary representation of a compact abelian group (sum of characters $u^{is}$, $\mu^{is}=1$).
- **THM-PAPER-0117-L2** (Mellin identity in proof of Thm 6.4; Section 6.2). For $f\in\mathcal S_0^{ev}$: $\int u^{is}E(f)(u)d^*u=\zeta(\tfrac12+is)\int u^{is}f(u)d^*u$ (Fubini for $\Im$ large, then analytic continuation; pole of $\zeta(\tfrac12-iz)$ at $z=i/2$ cancelled since $\hat f(0)=0$). — *Role:* Core analytic step linking orthogonality to zeta zeros.
- **THM-PAPER-0117-L3** (Test function in Thm 6.4(i); Section 6.2). For $f(x)=e^{-\pi x^2}\pi x^2(-2\pi x^2+3)\in\mathcal S_0^{ev}$: $\int u^{is}E(f)(u)d^*u=(\tfrac14+s^2)\zeta_{\mathbb Q}(\tfrac12+is)$ ($\zeta_{\mathbb Q}$ completed zeta). — *Role:* A single test function forces $\tfrac12+is$ to be a zero.
- **THM-PAPER-0117-L4** (Prop 2.1, 2.3, Cor 2.4; Section 2). For $\lambda>1$, an explicit formula defines a lower-bounded lower semicontinuous quadratic form $Q^W_\lambda$ on $L^2([\lambda^{-1},\lambda],d^*u)$; its lower bound is the limit of smallest eigenvalues of finite-dimensional compressions (exact statements not read in detail). — *Role:* Rigorous framework for numerics.
- **THM-PAPER-0117-L5** (Prop 4.1, 4.2; Section 4). $D(\lambda,k)$ with periodic function multiplication gives a spectral triple; counting of nonzero eigenvalues for $E=2\pi\mu$ (not read in detail). — *Role:* Defines the spectral triple compared with zeros.

### Proof architecture

Section 6 (read in full): define E and Sigma_mu on S_0^ev; Lemma 6.1 (size/decay) and 6.2 (scaling equivariance); orthogonal complement is a unitary representation of a compact group, hence a sum of characters u^{is} with mu^{is}=1; orthogonality gives vanishing of the Mellin transform of E(f) for all f; the Mellin identity plus a test function shows 1/2+is is a zero (Thm 6.4(i)); conversely zero implies the character is orthogonal and well defined iff mu^{is}=1 (ii). Sections 2-5: numerical detection of tiny Weil-form eigenvalues, prolate-vector approximation, spectral triple, numerical coincidences.

Dependency edges: CAND-02085 → CAND-02040 (shares prolate/Sonin/Weil archimedean framework)

**Imported results.** Slepian-Pollak-Landau prolate theory (refs [11-13]); Weil explicit formula and Weil criterion; Numerical positivity of Q^W at lambda=sqrt2 (ref [14]); Functional equation of completed zeta

**Techniques.** Weil explicit formula quadratic form; prolate spheroidal wave functions and angle operator; scale-invariant Riemann sums E(f); Mellin transform and Poisson formula E(\hat f)(x)=E(f)(x^{-1}); harmonic analysis on compact abelian group; finite-rank perturbation of Dirac operator / spectral triples; high-precision numerical linear algebra

## Context and interpretation

**Importance and obstacle overcome.** Replaces the ad hoc Sobolev spaces of Connes' 1999 spectral realization by L^2 of a circle, giving a geometric realization of critical zeros and explaining tiny Weil-form eigenvalues via prolate functions. Periodization makes the E-operator scale compatible.

**Relation to prior work.** Refines Connes (1999) spectral realization; builds on Connes-Consani-Moscovici and Connes-Consani 'Weil positivity and trace formula, the archimedean place' (2006.13771); developed in 'Hochschild homology, trace map and zeta-cycles' (2207.10419), CAND-02040, 'Zeta zeros and prolate wave operators' (2310.18423).

**Limitations and open questions.** Theorem 1.1 shows nonzero H(L) forces critical zeros and each critical zero gives zeta-cycles; it says nothing about off-line zeros (unitary characters only see the critical line) and does not imply RH. Numerical coincidence of the first 31 zeros is evidence, only at special lambda. Positivity of Q^W_lambda for all lambda (RH-equivalent) is not addressed.

**Ideas in remarks/appendices/abandoned paths.** Corollary 6.5 gives a 'length spectrum' of zeta (lengths 2 pi n/s) analogous to closed geodesics; finite-cover stability and action of N^x lifts the scaling-site structure. Sections 2.2-2.4: archimedean contribution alone loses positivity for log lambda^2 in [0.493,0.893], prime 2 restores it, and positivity pins the prime p within ~1e-3 of 2.

## Research potential

- **Hypotheses that might be weakened.** Replace S_0^ev by smaller spaces (compactly supported test functions) and test whether non-unitary characters u^s could detect off-line zeros.
- **Generalizations.** Zeta-cycles for Dirichlet L-functions / number fields; function-field analogue (cf. CAND-00310) where Weil RH is known, as a test-bed.
- **Candidate connections.** Weil positivity (family C) via near-radical eigenvectors; prolate wave operator CAND-02040; Hochschild/trace-map follow-ups.
- **Reusable lemmas.** Lemma 6.1 and the Mellin identity for E(f).
- **Possible experiments.** Reproduce the k-independence criterion for D(lambda,k) with mpmath for lambda^2 in [5,16.5] and beyond 31 zeros; study scaling of the tiny Weil eigenvalue versus lambda^2, and its persistence when the prime-2 term is altered.
- **Risks / barriers.** Numerical coincidence at special lambda is not a proof; the 1e-50 probability is a heuristic. The construction sees only critical zeros by design; showing H(L) catches all zeros would be RH-equivalent.

## Audit notes (Level 1 reader)

The general Mellin identity (6.4) proof portion is partly garbled in the extracted text, so its full derivation was not independently verified. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02085`; harvest queries: kw_RH_any, kw_weil_positivity, kw_zeta_zeros, msc_11M06, arxiv_explicit_formula, arxiv_weil_explicit, arxiv_zeta_zeros.
- Triage decision: include — Weil quadratic form small eigenvalues and zeta-cycles.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

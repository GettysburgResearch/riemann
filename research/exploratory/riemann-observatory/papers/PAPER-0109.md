# PAPER-0109 — The UV prolate spectrum matches the zeros of zeta

| Field | Value |
|---|---|
| Authors | Connes, Alain; Moscovici, Henri |
| Year / stratum | 2022 / S6 |
| Venue | Proc. Natl. Acad. Sci. USA 119, No. 22, Article ID e2123174119, 7 p. (2022). |
| Identifiers | zbMATH [1556.34029](https://zbmath.org/?q=an:1556.34029) · DOI [10.1073/pnas.2123174119](https://doi.org/10.1073/pnas.2123174119) |
| MSC | 34B05, 47B25, 11M06 |
| Families | D |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/2112.05500 |
| Selection | score 4.2288, in-pool citations 4, seed lists 3, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Does the natural self-adjoint extension W_sa of the prolate wave operator W_lambda (commuting with Fourier transform and with the cutoff projection P_lambda and its Fourier conjugate) have negative eigenvalues whose ultraviolet behaviour reproduces that of the squares of the zeta zeros, and can a Dirac square root be built whose spectrum has Riemann-von Mangoldt counting asymptotics? (basis: arXiv v1 preprint of the PNAS paper; PNAS text not read)

**Historical motivation.** Prolate functions are eigenfunctions of the angle operator between P_lambda and its Fourier conjugate; earlier work used them to prove Weil positivity at the archimedean place. Here the commuting differential operator itself shows zeta-like negative spectrum.

### Main results

- **THM-PAPER-0109-1** (Lemma 2.1, lemma, scope: global; Section 2). The minimal operator $W_{\min}$ (closure of $W_\lambda\xi=-\partial_x((\lambda^2-x^2)\partial_x\xi)+(2\pi\lambda)^2x^2\xi$ on $\mathcal S(\mathbb R)\subset L^2(\mathbb R)$) has deficiency indices $(4,4)$.
- **THM-PAPER-0109-2** (Theorem 2.6, theorem, scope: global; Section 2, Theorem 2.6). There is a self-adjoint extension $W_{sa}$ of $W_{\min}$ (domain $L_\beta$ spanned by $\mathrm{Dom}\,W_{\min}$ and $\beta_\pm,\hat\beta_\pm$) such that: (i) $W_{sa}$ commutes with the Fourier transform; (ii) it commutes with $P_\lambda$ and $\hat P_\lambda=\tilde F P_\lambda\tilde F^{-1}$; (iii) it is the only self-adjoint extension of $W_{\min}$ commuting with $P_\lambda,\hat P_\lambda$; (iv) its spectrum is discrete and unbounded in both directions.
- **THM-PAPER-0109-3** (Corollary 3.2 (with Lemma 3.1), corollary, scope: global; Section 3). For $\lambda=1$ (even functions): if $\mu$ is a negative eigenvalue of $W_{sa}$, the eigenfunction $\phi_\mu$ belongs to Sonin's space (orthogonal complement of the eigenspaces attached to the classical prolate functions and their Fourier transforms). The authors do not claim all eigenvalues of $W_{sa}$ on Sonin space are negative (numerics: at most finitely many exceptions).
- **THM-PAPER-0109-4** (Proposition 4.2, proposition (semiclassical, heuristic), scope: asymptotic; Section 4). The semiclassical approximation to the number of negative eigenvalues $\xi$ of $W_{sa}$ with $-\xi\le E^2$ on even functions (equally on odd functions) is $2\sigma(E,\lambda)$, $\sigma(E,\lambda)\sim\frac{E}{2\pi}\left(\log\frac{E}{2\pi}-1+\log4-2\log\lambda+\lambda^2\right)+o(1)$.
- **THM-PAPER-0109-5** (Theorem 6.1, theorem (relying on Prop 4.2 and Prop 5.3), scope: asymptotic; Section 6). For $\lambda=\sqrt2$ the operator $\sqrt2\,\slashed D$ (Dirac square root of $W_\lambda$ via Darboux/Riccati, with a deformation parameter) has discrete simple spectrum in $\mathbb R\cup i\mathbb R$, imaginary eigenvalues symmetric under conjugation, and the counting function $N(E)$ of eigenvalues with $0<\Im\xi<E$ satisfies $N(E)\sim\frac{E}{2\pi}\left(\log\frac{E}{2\pi}-1\right)+O(1)$.

### Key definitions

- $W_\lambda=-\partial_x(\lambda^2-x^2)\partial_x+(2\pi\lambda)^2x^2$
- $P_\lambda=1_{[-\lambda,\lambda]}$, $\hat P_\lambda=\tilde FP_\lambda\tilde F^{-1}$
- Sonin space
- $W_{sa}$

### Principal lemmas

- **THM-PAPER-0109-L1** (Lemma 2.3; Section 2). If $\xi\in\mathrm{Dom}\,W_{\min}$ then $P_\lambda\xi\in\mathrm{Dom}\,W_{\max}$ and $WP_\lambda\xi=P_\lambda W\xi$; same for $\hat P_\lambda$. — *Role:* Allows an extension commuting with the cutoff projections.
- **THM-PAPER-0109-L2** (Lemma 2.4; Section 2). (i) The Fourier transform of $f(x)=\frac12\log((\lambda^2-x^2)^{-2})$ coincides off $0$ with $\cos(2\pi\lambda y)/|y|$; (ii) $\tilde F 1_{[-\lambda,\lambda]}(y)=\sin(2\pi\lambda y)/(\pi y)$. — *Role:* Fourier images of boundary data for the symplectic Omega pairing.
- **THM-PAPER-0109-L3** (Lemma 2.5; Section 2). $\{\alpha_\pm,\beta_\pm,\hat\alpha_\pm,\hat\beta_\pm\}$ forms a basis of $E_\pm=\mathrm{Dom}(W_{\max})/\mathrm{Dom}(W_{\min})$. — *Role:* Parametrizes self-adjoint extensions by boundary data.
- **THM-PAPER-0109-L4** (Lemma 3.1; Section 3). For real $\mu$ the unique solution $\xi_\mu$ with asymptotics $-\sin(2\pi x)/(\pi x)$ at infinity has Borel-summable expansion and equals the Fourier transform of the unique even solution $\phi_\mu$ vanishing on $[-1,1]$ and equal to $f_\mu$ for $x>1$. — *Role:* Links boundary behavior to support of the transform, hence Sonin-space membership.
- **THM-PAPER-0109-L5** (Lemma 5.1/5.2, Prop 5.3; Section 5 (skimmed)). Darboux construction with $p=x^2-\lambda^2$, $V=4\pi^2\lambda^2x^2$, $L=\partial p\partial+V$: Dirac operator whose square is two copies of $W_{sa}$ (exact statement not verified). — *Role:* Produces the isospectral family of Dirac operators.

### Proof architecture

Sec 2: Sturm-Liouville analysis on three intervals; four singular endpoints all limit-circle (LCNO at +-lambda, LCO at +-infinity), deficiency indices (4,4); the extension is singled out by commuting with Fourier transform and the cutoff projections via boundary functionals from the Lagrange/Green identity; discreteness from standard limit-circle theory. Sec 3: negative-eigenvalue eigenfunctions lie in Sonin space. Sec 4: semiclassical phase-space area count. Sec 5-6: Darboux/Riccati Dirac square root, transfer of the count. Numerical comparison with zeta zeros is evidence only.

Dependency edges: CAND-02040 → CAND-02085 (same prolate/Sonin/Weil archimedean program)

**Imported results.** Slepian-Pollak-Landau prolate theory (refs [14,15,16]); Sturm-Liouville limit-circle theory (refs [11],[17],[18]); Self-adjoint extension of Connes-Consani ref [1], Lemma 6; Weil positivity at the archimedean place via Sonin space (ref [4])

**Techniques.** Sturm-Liouville theory with limit-circle endpoints; deficiency indices and boundary-form parametrization of self-adjoint extensions; prolate spheroidal wave functions; semiclassical phase-space counting; Darboux transformation/Riccati equation; Borel summability of asymptotics

## Context and interpretation

**Importance and obstacle overcome.** Provides a canonical self-adjoint extension (unique commuting with both cutoff projections) of the prolate operator despite deficiency indices (4,4) and interior singularities, and a candidate spectral realization of the archimedean contribution (Sonin space, link to Weil positivity at the archimedean place) with the correct Riemann-von Mangoldt density. Not a Hilbert-Polya operator.

**Relation to prior work.** Builds on Connes-Consani prolate operator work, Slepian-Pollak-Landau theory, and Connes-Consani-Moscovici Weil positivity at the archimedean place; continued in Connes-Consani 'Spectral triples and zeta-cycles', 'Zeta zeros and prolate wave operators' (arXiv 2310.18423) and 'Heat expansion and zeta' (2402.13082).

**Limitations and open questions.** Only UV counting agreement, via a heuristic semiclassical approximation with O(1) error; no eigenvalue-by-eigenvalue identification, no connection to RH. Claim that all Sonin-space eigenvalues are negative is unproved. Infrared spectrum not claimed to match zeros. Rigorous Weyl law for this operator is not established in the part read.

**Ideas in remarks/appendices/abandoned paths.** Section 7 (not read in detail) is announced as speculative incl. a 2-dim black-hole geometry for the Dirac operator. Cor 3.2 remark: all but finitely many Sonin eigenvalues negative (numerical conjecture). The deformation parameter of the Dirac family may be tunable to match low zeros.

## Research potential

- **Hypotheses that might be weakened.** Prop 4.2 is heuristic; a rigorous Weyl-type asymptotic with error term for negative spectrum of W_sa on Sonin space would convert the UV match into a theorem and make Theorem 6.1 unconditional.
- **Generalizations.** General lambda (Prop 4.2 is stated for all lambda); odd functions; L-functions with other gamma factors.
- **Candidate connections.** CAND-02085 (zeta-cycles): same Sonin/prolate archimedean ingredient; test relation of negative W_sa spectrum to zeta-cycle eigenvalues at lambda^2=2.
- **Reusable lemmas.** Theorem 2.6(iii) uniqueness of the extension commuting with P_lambda and its conjugate; Lemma 2.4 boundary Fourier computations.
- **Possible experiments.** Diagonalize W_sa on Sonin space (lambda=1, sqrt2) at high precision, compare negative eigenvalues with -(gamma_n)^2; fit the O(1) remainder in N(E) against the Riemann-von Mangoldt remainder S(T).
- **Risks / barriers.** Counting-function agreement is much weaker than eigenvalue agreement; nothing implies RH; exact identification needs arithmetic (trace formula) input absent here.

## Audit notes (Level 1 reader)

Access caveat: v1 read, titled differently from PNAS; theorem numbering may differ. Boundary-functional sign conventions in eq (18) region not independently checked. In Thm 6.1, constants in Prop 4.2 (log4 - 2 log sqrt2 = log2) are hidden in O(1). Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02040`; harvest queries: kw_zeta_zeros, msc_11M06.
- Triage decision: include — Spectral realization: prolate operator spectrum matches zeta zeros.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

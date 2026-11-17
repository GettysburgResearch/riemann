# PAPER-0095 — Hamiltonian for the Hilbert-Pólya conjecture

| Field | Value |
|---|---|
| Authors | Yakaboylu, Enderalp |
| Year / stratum | 2024 / S7 |
| Venue | J. Phys. A, Math. Theor. 57, No. 23, Article ID 235204, 12 p. (2024). |
| Identifiers | zbMATH [1543.30020](https://zbmath.org/?q=an:1543.30020) · DOI [10.1088/1751-8121/ad4c2d](https://doi.org/10.1088/1751-8121/ad4c2d) · arXiv [2309.00405](https://arxiv.org/abs/2309.00405) |
| MSC | 30C15, 81Q10 |
| Families | D |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/2309.00405 |
| Selection | score 4.3142, in-pool citations 1, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Construct $\hat H=\hat S\hat H_{BK}\hat S^{-1}$ (similarity transform of Berry-Keating $\frac12(xp+px)$ on $L^2[0,\infty)$) whose Dirichlet condition at the origin selects $E_s=i(1/2-s)$ with $\zeta(s)=0$, and argue via a further similarity transformation that it is self-adjoint on a suitable domain, which would imply RH.

**Historical motivation.** Hilbert-Polya requires an operator with zeta in the eigenvalue condition and a self-adjoint domain; here a similarity transform of xp gives the zeta condition as a Dirichlet boundary condition.

### Main results

- **THM-PAPER-0095-1** (Eqs (1)-(3), Sec. I, formal construction, scope: global; Section I). With $\hat N=\frac12(\hat x\hat p^2+\hat p^2\hat x+\hat x/2)$ (shifted Laguerre number operator), $\alpha=(1+t)/(2-2t)$, $\Re t<1$, $\hat S=t^{\hat N}e^{\alpha\hat x}/(1+e^{\hat x})$, $\hat H=\hat S\hat H_{BK}\hat S^{-1}$: eigenfunctions $\Psi_s=\hat S|\phi_s\rangle$, $\phi_s=x^{s-1}/\sqrt{2\pi}$, $E_s=i(1/2-s)$; $\Psi_s(0)=\frac1{\sqrt{2\pi}}\frac{\sqrt t}{1-t}(1-2^{1-s})\Gamma(s)\zeta(s)$, so $\Psi_s(0)=0$ iff $\zeta(s)=0$.
- **THM-PAPER-0095-2** (Eqs (4)-(11), Sec. II, formal derivation, scope: global; Section II). For $\tilde H=e^{i\lambda\hat D}\hat He^{-i\lambda\hat D}$ and $\sinh\lambda=2t/(t^2-1)$ ($t$ real), $\tilde H=i\hat N_+-i\hat N_--i\sum_mc_m\beta\hat N_-^m$ with $\beta=(t^2-1)/t=1$, $c_m=B_m(2^m-1)/m!$. In Mellin space: $(-iz\,d/dz+i/2-iz-iz/(1+e^{-z}))g_s=E_sg_s$, $g_s=g_0(s)z^se^{-z}/(1+e^z)$, boundary condition $g_0(s)(1-2^{1-s})\Gamma(s)\zeta(s)=0$.
- **THM-PAPER-0095-3** (Eqs (12)-(18), unproved assumption, scope: global; Section II, Eqs (12)-(18)). Assuming a weight $\omega$ replacing $I_0(2\sqrt{yz})/\sqrt{yz}$ in the Mellin-space inner product, with $\omega'=\omega s(z)s(y)$ Hermitian and $z\partial_z\omega'(z,y)=-\partial_y(y\omega'^*(y,z))$, one gets $\langle V|H'U\rangle=BT+\langle U|H'V\rangle^*$; under the limit condition (17) the domains of $H'$ and $H'^*$ coincide so $H'$ is self-adjoint. The choice (18) $\omega'(z,y)=\frac{1/z}{1+e^{y/z}}+\frac{1/y}{1+e^{z/y}}$ is said to satisfy (14),(15),(17). Existence of the similarity transformation is assumed.
- **THM-PAPER-0095-4** (Discussion, remark, scope: conditional; Discussion). Replacing $(1+e^{\hat x})^{-1}$ by arbitrary $W(\hat x)$ gives the condition $\{\mathcal MW\}(s)=0$; if a self-adjoint realization existed, all zeros of the Mellin transform would lie on $\Re s=1/2$; cites 'local Riemann hypothesis' examples (orthogonal polynomials).
- **THM-PAPER-0095-5** (Discussion, status statement, scope: conditional; Discussion). Authors: 'If the formal argument ... can be rigorously established, our approach holds the potential to imply the validity of the RH. ... the second stage requires further rigorous treatment.' RH is not claimed proved.

### Key definitions

- $\hat D=\hat H_{BK}=\tfrac12(\hat x\hat p+\hat p\hat x)$
- $\hat N$, $\hat K=\hat N-\hat x/2$
- $\hat S=t^{\hat N}e^{\alpha\hat x}/(1+e^{\hat x})$
- $\hat H=\hat S\hat D\hat S^{-1}$ with Dirichlet condition $\Psi(0)=0$

### Principal lemmas

- **THM-PAPER-0095-L1** (Laguerre generating function (Sec. I, App. A); Sec. I, Eq. (3)). $e^{-z/2}\sum_nt^nL_n(z)=\frac{e^{-\alpha z}}{1-t}$ for $|t|<1$, continued to $\Re t<1$ by Borel summation; with $\chi_n(0)=1$ gives $\Psi_s(0)\propto\int_0^\infty z^{s-1}/(1+e^z)dz=\Gamma(s)\eta(s)$. — *Role:* Turns the Dirichlet condition into vanishing of eta/zeta.
- **THM-PAPER-0095-L2** (su(1,1) algebra (6); Sec. II). $[\hat D,\hat N]=i\hat K$, $[\hat N,\hat K]=i\hat D$, $[\hat K,\hat D]=-i\hat N$, Casimir $=1/4$; $\hat N_\pm=\hat K\pm i\hat D$ act by $(m+1)|m+1\rangle$, $m|m-1\rangle$. — *Role:* Reduces $\tilde H$ to the simple form (8) and recursion (9).
- **THM-PAPER-0095-L3** (Eqs (12), (14)-(17); Sec. II). Mellin form of the inner product $\langle V|\tilde HU\rangle=\iint\frac{I_0(2\sqrt{yz})}{\sqrt{yz}}s(z)s(y)v'^*(y)(-iz\partial_z-\tfrac i2)u'(z)$, $s(z)=ze^{-z}/(1+e^z)$; replacement by weight $\omega$ obeying Hermiticity, first-order PDE (15), and boundary condition (17). — *Role:* Heart of the self-adjointness argument.

### Proof architecture

Stage I: conjugate H_BK by S so the Dirichlet condition is Gamma(s)(1-2^{1-s})zeta(s) (formal, Laguerre generating function plus Borel resummation). Stage II: unitarily equivalent H tilde, su(1,1) reduction, Mellin-space solution, then assume a modified inner product (weight omega) making H symmetric and impose vanishing of boundary terms (17) to claim Dom H'=Dom H'*. No theorem is rigorously proved; the key step is an assumed existence of a similarity transformation.

Dependency edges: CAND-02425 → CAND-02040 (same goal (operator realization), different method; CAND-02040 rigorous on self-adjointness, weaker on spectrum identification)

**Imported results.** Self-adjointness of Berry-Keating D on abs. continuous L^2[0,infty) (refs [15-17]); Laguerre ODE/generating function, Sturm-Liouville for N [19,20]; Borel summation basics; Mellin transforms of orthogonal polynomials with critical-line zeros [23,24]; zeta(s)=(1-2^{1-s})^{-1}eta(s), Re s>0

**Techniques.** similarity transformation of Berry-Keating Hamiltonian; Laguerre polynomials and number operator; su(1,1) algebra and ladder operators; Borel summation; Mellin-space reformulation; boundary-term analysis for self-adjointness

## Context and interpretation

**Importance and obstacle overcome.** Attempt at Hilbert-Polya stage I (zeta zeros from a Dirichlet condition via an explicit boundary function) with only formal stage II. No RH claim.

**Relation to prior work.** Berry-Keating xp (refs [8,9]), Connes (ref [7]), Okubo (ref [6]), Sierra et al (ref [12]), Mellin transforms of orthogonal polynomials with critical-line zeros (refs [23-25]). Contrast with CAND-02040, rigorous self-adjointness but only UV spectral match.

**Limitations and open questions.** The paper says stage II needs rigorous treatment. Gaps: (a) boundedness/invertibility/closedness of S (t^N with Re t<1, series divergent for |t|>=1) not proved, so 'similarity' does not preserve spectrum; (b) phi_s=x^{s-1} is not in L^2, so Psi_s are generalized eigenfunctions and the Dirichlet condition is not an L^2 domain condition; (c) weight omega' in (18) is introduced to satisfy formal conditions; its positivity and the existence of the implementing transformation are assumed; (d) the domain (17) is shaped by the eigenfunctions themselves (circularity); (e) zeros of 1-2^{1-s} (incl. s=1) excluded without discussion.

**Ideas in remarks/appendices/abandoned paths.** Discussion: general W gives {MW}(s)=0 linking the method to the 'local Riemann hypothesis' for Mellin transforms of other functions with known critical-line zeros -- a ready calibration test-bed. The explicit weight (18) is a concrete inner-product kernel testable numerically.

## Research potential

- **Hypotheses that might be weakened.** Central unproved hypothesis: existence of a similarity transformation making H self-adjoint on the domain (17). Checkable weaker version: is the kernel omega'(z,y) of Eq (18) positive semi-definite on a dense domain? Indefiniteness would kill the construction.
- **Generalizations.** Replace 1/(1+e^x) by W with known critical-line Mellin zeros to calibrate the argument where the answer is known.
- **Candidate connections.** Mellin-space realizations of the explicit formula (Connes-style); kernel positivity (Weil positivity, de Branges spaces).
- **Reusable lemmas.** Psi_s(0)=const*Gamma(s)(1-2^{1-s})zeta(s) via the Laguerre generating function; su(1,1) reduction (7)-(8).
- **Possible experiments.** (1) test positive semi-definiteness of omega' of (18); (2) symbolically verify (15)-(16); (3) check whether Psi_s is in L^2 for Re s=1/2; (4) truncate in the Laguerre basis, impose Dirichlet, diagonalize and compare with zeros.
- **Risks / barriers.** Without bounded invertible S, similarity does not preserve spectrum; generalized eigenfunctions do not define a closed operator domain; the argument appears to prove too much (any Mellin transform W would have all zeros on the critical line, false in general) with no mechanism identified to use properties specific to 1/(1+e^x).

## Audit notes (Level 1 reader)

Discussion (pp.10-11): the claim that replacing (1+e^x)^{-1} by arbitrary W would force critical-line zeros is false for general W, so the self-adjointness step (Eqs 12-18) cannot be sound unless it uses properties specific to 1/(1+e^x); the paper only states it conditionally. Sec I: phi_s not in L^2, so eigenfunctions are generalized. Sec II after Eq (5): Bernoulli series converges only for |x|<pi; operator-valued Borel summation not justified. Eq (18) is garbled in the text extraction, exact form to be checked against the PDF.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02425`; harvest queries: kw_RH_any, kw_hilbert_polya, kw_zeta_zeros, arxiv_rh_abs, arxiv_zeta_zeros.
- Triage decision: include — Explicit Hamiltonian for Hilbert-Polya whose eigenfunctions vanish at origin at zeros.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

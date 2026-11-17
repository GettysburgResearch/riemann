# PAPER-0090 — Remarks on Weil's quadratic functional in the theory of prime numbers. I

| Field | Value |
|---|---|
| Authors | Bombieri, Enrico |
| Year / stratum | 2000 / S4 |
| Venue | Atti Accad. Naz. Lincei, Cl. Sci. Fis. Mat. Nat., IX. Ser., Rend. Lincei, Mat. Appl. 11, No. 3, 183-233 (2000). |
| Identifiers | zbMATH [1008.11034](https://zbmath.org/?q=an:1008.11034) |
| MSC | 11M26, 11M36, 42A38, 11R42 |
| Families | C, D |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — http://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0&fmt=pdf |
| Selection | score 4.327, in-pool citations 14, seed lists 4, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Study Weil's quadratic functional T[f*f^*] (equivalent to RH via the Guinand-Weil explicit formula) variationally on spaces of functions supported in a fixed interval, and via its Fourier-side infinite matrix and finite truncations H(Gamma;t); determine the number of negative eigenvalues in terms of zeros off the critical line, and what a failure of RH with finitely many bad zeros would force.

**Historical motivation.** Weil's 1952 reformulation of RH as positivity of a quadratic functional, mirroring the function-field proof; Yoshida (1992) first study.

### Main results

- **THM-PAPER-0090-1** (Theorem 1 (Sec. 3), theorem, scope: global; Sec. 3, Thm 1, (3.1)). RH holds iff \sum_\rho \hat g(\rho)\overline{\hat g(1-\bar\rho)}... >0 as stated: \sum_{\rho}\hat g(\rho)\hat{g^*}(\rho)... (3.1) \;>0 for every complex g\in C_0^\infty((0,\infty)), g\not\equiv0 (strengthening of Weil's criterion to strict positivity). [Exact displayed form (3.1) in the text is \sum_\rho \hat g(\rho)\overline{\hat g(1-\bar\rho)}>0; PDF extraction garbled the conjugations.]
- **THM-PAPER-0090-2** (Theorem 2, theorem, scope: global; Sec. 3, Thm 2). For T[f]=\int_0^\infty f+\int_0^\infty f^*-\sum_n\Lambda(n)\{f(n)+f^*(n)\}-(\log4\pi+\gamma)f(1)-\int_1^\infty\{f(x)+f^*(x)-\tfrac{2}{x}f(1)\}\tfrac{x\,dx}{x^2-1} on C_0^\infty((0,\infty)), with f^*(x)=\tfrac1x f(1/x): T[f]=T[f^*]=\sum_\rho\hat f(\rho). RH is equivalent to T[f*f^*]\ge0 on C_0^\infty((0,\infty)) with equality only for f\equiv0 (where * is multiplicative convolution).
- **THM-PAPER-0090-3** (Theorem 3, theorem (unconditional), scope: local; Sec. 4, Thm 3). For E a finite union of closed finite intervals in (0,\infty), the infimum of T[f*f^*] over the unit sphere of L^2(E) is attained.
- **THM-PAPER-0090-4** (Theorem 4, theorem, scope: local; Sec. 4, Thm 4). Let \lambda be the infimum of T[f*f^*] on the unit sphere of W_0=W_0^{1,2}([M^{-1},M]) (norm \|Df\|). If \lambda<0 the infimum is attained.
- **THM-PAPER-0090-5** (Theorem 5, theorem, scope: local; Sec. 4, Thm 5). \mu_+(M),\mu_-(M) (infima of T[f*f^*] over even/odd L^2([M^{-1},M]) unit-norm functions) are continuous decreasing functions of M.
- **THM-PAPER-0090-6** (Theorem 8, theorem, scope: finite; Sec. 8, Thm 8, Lemma 10). For a finite multiset Z of complex numbers closed under \rho\mapsto1-\rho (equivalently Gamma\subset\mathbb C symmetric under conjugation with multiplicities), \rho=1/2+i\gamma, the matrix H(\Gamma;t) has only real eigenvalues, and the number of negative eigenvalues equals the number of distinct complex-conjugate pairs (\gamma,\bar\gamma) in \Gamma; 0 is an eigenvalue iff some \gamma has multiplicity >1 (Lemma 10). Independent of arithmetic.
- **THM-PAPER-0090-7** (Theorem 10 / Theorem 11 and Corollary, theorem (conditional), scope: conditional; Sec. 10 Thm 10; Sec. 11 Thm 11 and Corollary; Intro alternatives (i)-(iii)). Suppose \zeta has only finitely many zeros 1/2+i\gamma with \gamma\notin\mathbb R, at least one. Then for each t>0 there exist w_\gamma, \lambda\le0 with \sum|w_\gamma|^2=1, \sum_{\gamma\notin\mathbb R}|w_\gamma|^2\ge-\sum_{\gamma\notin\mathbb R}w_\gamma\overline{(w_{\bar\gamma})}\ge1/2, and \lambda w_\gamma=\sum_{\gamma'}H(\gamma,\gamma';t)w_{\gamma'}, such that for f(x)=\phi(x)x^{-1/2}F(\log x) either T[f*f^*]=\lambda\|Df\|^2<0 or f\equiv0; and for 0<t<t_0 (explicit) f\equiv0. Corollary (Thm 11): if T[f*f^*]\ge0 for all smooth f supported in a bounded finite union of intervals E, then RH is true, or infinitely many zeros are off the line, or the x^{-\rho} are linearly dependent over E with an \ell^2 coefficient sequence putting at least half its \ell^2-mass on zeros off the line.
- **THM-PAPER-0090-8** (Theorem 12 (Sec. 12; reproves Yoshida), theorem, scope: local; Sec. 12, Thm 12). If F has compact support in an interval I of length |I|<\log2 then T[F(x)*\overline{F(-x)}]=\sum_\gamma|\hat F(\gamma)|^2\ge(\log\frac1{|I|}-\log\log\frac1{|I|}-O(1))\|F\|^2 (garbled in extraction; form as read), giving positivity for small support.

### Key definitions

- f^*(x)=x^{-1}f(1/x); f even/odd if f=\pm f^*
- T[f] Weil functional (Thm 2)
- V=span of \Phi(x)e^{\pm x/2}, \Phi(x)e^{-i\gamma x}; V^\circ codim 2 with F(\pm t)=0
- H(\Gamma;t) Hermitian matrix of the Fourier-side form
- Problem 1 (norm \|Df\| on W_0^{1,2}) and Problem 2 (L^2(E) norm)

### Principal lemmas

- **THM-PAPER-0090-L1** (Lemma 1; Sec. 4). Variational equation for Problem 1: \lambda Df(a)-L[f](a)=0 on (M^{-1},M), D=-D-D^2, L the Euler-Lagrange operator of T[f*f^*]. — *Role:* Euler-Lagrange equation for extremals
- **THM-PAPER-0090-L2** (Lemma 2, 3; Sec. 4-5). f in W_0 is Hoelder-1/2 continuous with bounds; Fourier decay f^(rho)=O(|rho|^{-2}) for L^2 f supported in [M^{-1},M]. — *Role:* compactness/decay for existence (Thm 3, 4) and passage to the limit
- **THM-PAPER-0090-L3** (Lemma 5-7; Sec. 5-6). Structure of D^2 f (bounded function plus two Dirac masses) and reduction of the eigenvalue problem to finite sums of exponentials e^{-i\gamma u} on the interval. — *Role:* identifies extremals as linear combinations of x^{-rho}
- **THM-PAPER-0090-L4** (Lemma 10; Sec. 8). H(\Gamma;t) has eigenvalue 0 iff some \gamma has multiplicity >1, with multiplicity \sum[m(\gamma)-1]; if all \gamma real, H is positive semidefinite. — *Role:* key rigidity: no zero eigenvalue for distinct nodes, so negative-eigenvalue count is deformation-invariant
- **THM-PAPER-0090-L5** (Lemma 13, 14; Sec. 10-11). If \lambda_N<0 control on the eigenvector coefficients (Lemma 13); F\equiv0 on E iff \lambda=\liminf\lambda_N=0 (Lemma 14). — *Role:* dichotomy in passage N->infinity: negative eigenvalue stays away from 0, or yields a linear relation among x^{-rho}

### Proof architecture

Sec. 2-3: Guinand-Weil explicit formula gives T[f]=sum f^(rho) and the positivity criterion. Sec. 4-6: two variational problems (norm \|Df\| on W_0, or L^2(E)); existence of minimizers via compactness using the log-derivative term of Gamma at infinity (Lemma 3, asymptotic Gamma'/Gamma(w/2)=log|w|+O(1)); Fourier transform turns the extremal equation into an infinite matrix. Sec. 8-9: for finite truncations Gamma, deformation argument (continuous motion of Gamma keeping conjugation symmetry and distinctness) plus Lemma 10 (0 never eigenvalue) gives Thm 8/9: #negative eigenvalues = #conjugate pairs. Sec. 10-11: pass N->infinity under finitely-many-off-line-zeros hypothesis; dichotomy (negative eigenvalue bounded away from 0 vs. linear relation). Sec. 12: Yoshida small-support positivity.

Dependency edges: CAND-00816 → Weil 1952 explicit formula (uses); CAND-00816 → Yoshida 1992 (reproves/extends)

**Imported results.** Guinand-Weil explicit formula (Guinand 1942, Weil 1952), proved in Sec. 2 by residues; Yoshida (1992) positivity for small support (reproved as Thm 12); Stirling-type asymptotics for Gamma'/Gamma

**Techniques.** Guinand-Weil explicit formula; direct method of calculus of variations on a space tied to the archimedean term; Fourier-side Gram/Hermitian matrices H(Gamma;t); homotopy/continuity invariance of inertia (number of negative eigenvalues); Mathematica experiments (Thm 8 found experimentally)

## Context and interpretation

**Importance and obstacle overcome.** First systematic variational/spectral treatment of Weil positivity beyond Yoshida; gives an exact inertia theorem (Thm 8) and a trichotomy for hypothetical RH failures. Obstacle: the quadratic form is not translation-invariant, minimizers must be pinned by fixing support; compactness comes from the prime-at-infinity term.

**Relation to prior work.** Extends Yoshida's Hermitian forms analysis; relates to Bombieri-Lagarias Li-criterion complements; sequel parts of the 'Remarks' series are not covered here.

**Limitations and open questions.** Results need finitely many zeros off the critical line (author suggests a density hypothesis could replace it). Linear independence of x^{-rho} (alternative (iii)) is left as an open, probably hard, question. Sec. 7 resolvent not used elsewhere. Extensions to Dedekind zeta noted without proof. Part I only; numerical eigenvalue behaviour near t_c^\pm (weak vs strong L^2 convergence of negative eigenvectors) left open (Sec. 12 end remarks).

## Research potential

- **Hypotheses that might be weakened.** Replace 'finitely many zeros off the line' in Thm 10/11 by a zero-density bound or by 'bounded number of negative eigenvalues of truncations' (stated by author, Sec. 1 end); remove the 'at least one' condition by working with truncation inertia.
- **Generalizations.** Thm 8/9 apply to arbitrary conjugation-symmetric finite multisets, so the inertia count extends to any L-function/Selberg class zero set; Dedekind zeta extension noted by author.
- **Candidate connections.** Connes' trace-formula and Weil positivity programme; de Branges-type Hilbert spaces; Li's criterion (Bombieri-Lagarias ref [1]); Yoshida's finite-calculation reduction for support [-t,t]; Montgomery pair-correlation via the same Fourier matrix.
- **Reusable lemmas.** Lemma 10 + Thm 8 (inertia = number of conjugate pairs) as a finite, auditable linear-algebra predicate; Thm 3 (existence of minimizers in L^2(E)).
- **Possible experiments.** Compute the truncated matrices H(Gamma_N;t) with the first N known zeros (all real) and certify positivity with directed rounding; test the transition t_c^\pm of the author's numerics; synthetic test: insert a fake conjugate pair into Gamma and verify the negative-eigenvalue count equals 1 (checks Thm 8).
- **Risks / barriers.** Finite positive truncations with real zeros are automatically PSD by Lemma 10 (Gamma all real), so numerical positivity is not evidence about RH; passage N->infinity is the whole difficulty. Support size t must exceed Yoshida's range for any nontrivial information.

## Audit notes (Level 1 reader)

PDF text extraction garbled several formulas (conjugations and over-bars in Thm 1, Thm 12), so displayed statements of Thm 1 and 12 are reconstructed and marked; verify against the PDF before citing. Sec. 7-9 and 12 proofs only skimmed; no errors noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00816`; harvest queries: kw_RH_any, kw_weil_positivity, msc_11M26, msc_11M36.
- Triage decision: include — Bombieri's analysis of Weil's positivity functional.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

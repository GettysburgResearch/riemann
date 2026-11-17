# PAPER-0006 — Finite Euler products and the Riemann hypothesis

| Field | Value |
|---|---|
| Authors | Gonek, S. M. |
| Year / stratum | 2012 / S5 |
| Venue | Trans. Am. Math. Soc. 364, No. 4, 2157-2191 (2012). |
| Identifiers | zbMATH [1300.11087](https://zbmath.org/?q=an:1300.11087) · DOI [10.1090/S0002-9947-2011-05546-7](https://doi.org/10.1090/S0002-9947-2011-05546-7) · arXiv [0704.3448](https://arxiv.org/abs/0704.3448) |
| MSC | 11M06, 11M26 |
| Families | A, C |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/0704.3448 (v1, 26 Apr 2007) |
| Selection | score 4.7333, in-pool citations 14, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Under RH, is zeta(s) well approximated by a short truncated Euler product in the right half of the critical strip, does the converse hold (good approximation implies at most finitely many zeros in the region), and can one build a family of non-analytic functions zeta_X(s) modelling zeta that satisfy a Riemann hypothesis, have simple repelling zeros, and converge to zeta(s) zeros as X grows?

**Historical motivation.** The author asks why both Euler product and functional equation are needed for RH, why zeros are simple and why they repel. He builds a model function whose structure makes these properties provable.

### Main results

- **THM-PAPER-0006-1** (Theorem 3.1, theorem (unconditional), scope: global; Sect. 3, Theorem 3.1, Eq. (10)). Let \sigma\ge0, X\ge2, P_X(s)=\exp\big(\sum_{n\le X^2}\frac{\Lambda_X(n)}{n^s\log n}\big) with \Lambda_X(n)=\Lambda(n) for n\le X, \Lambda(n)\big(2-\frac{\log n}{\log X}\big) for X<n\le X^2, 0 otherwise, and Z_X(s)=\exp\big(\sum_\rho[F_2((s-\rho)\log X)-F_2((s-1)\log X)]\big), F_2(z)=2E_2(2z)-E_2(z). Then \zeta(s)=P_X(s)Z_X(s)\big(1+O(X^{-\sigma-2}/(\tau^{-2}\log^2X))\big)-type uniform error as in (10), for \tau=|t|+2.
- **THM-PAPER-0006-2** (Theorem 3.3, theorem (conditional on RH), scope: asymptotic; Sect. 3, Theorem 3.3, Eqs. (19)-(21)). Assume RH. For \sigma\ge\tfrac12+\tfrac1{\log X}, |s-1|\ge\tfrac1{10}, any X\ge2: \zeta(s)=P_X(s)e^{R_X(s)} with R_X(s)\ll X^{1/2-\sigma}\big(\Phi(\tau)+\frac{\log\tau}{\log X}\big)+\frac{X}{\tau^2\log^2X}; moreover \arg\zeta(\sigma+it)=-\sum\frac{\Lambda_X(n)\sin(t\log n)}{n^\sigma\log n}+O(R_X(s)) for \sigma\ge1/2. Here \Phi is an admissible function (e.g. \Phi(t)=\tfrac12\log\tau/\log\log2\tau by Goldston-Gonek-type results). *Conditional on:* RH.
- **THM-PAPER-0006-3** (Theorem 3.5, theorem (conditional) with converse, scope: asymptotic; Sect. 3, Theorem 3.5, Eq. (28) and converse). Assume RH. For 2\le X\le t^2, |s-1|\ge1/10, \tfrac12+C\frac{\log\log2\tau}{\log X}\le\sigma\le1 with C>1: \zeta(s)=P_X(s)\big(1+O(\log^{(1-C)/2}t)\big). Conversely, if this holds for 2\le X\le t^2 in that region, then \zeta has at most finitely many zeros to the right of \sigma=\tfrac12+C\frac{\log\log 2\tau}{\log X}. *Conditional on:* RH for the forward direction.
- **THM-PAPER-0006-4** (Theorem 5.1 (and definition of zeta_X), theorem (conditional) with converse, scope: asymptotic; Sect. 5, Theorem 5.1, Eq. (36)). With \zeta_X(s)=P_X(s)+\chi(s)\overline{P_X}(1-s)-type reflection (in the text \zeta_X(s)=P_X(s)+\chi(s)\overline{P_X(s)}), \chi the functional equation factor: under RH, for 2\le X\le t^2, |s-1|\ge1/10 and \tfrac12+C\frac{\log\log 2\tau}{\log X}\le\sigma\le1, C>1, \zeta(s)=\zeta_X(s)(1+O(\log^{(1-C)/2}\tau)); conversely this implies finitely many zeros of zeta to the right of that curve. *Conditional on:* RH.
- **THM-PAPER-0006-5** (Theorem 6.2, theorem (unconditional), scope: global; Sect. 6, Theorem 6.2, Lemma 6.1). (RH for \zeta_X) Any zero \rho_X=\beta_X+i\gamma_X of \zeta_X(s) with 0\le\beta_X\le1 and \gamma_X\ge C_0 satisfies \beta_X=\tfrac12. Proof: P_X never vanishes, so zeros need |\chi(s)|=1, which Lemma 6.1 localizes to the critical line.
- **THM-PAPER-0006-6** (Theorems 7.1-7.2, 7.5-7.6, theorems (zero counting), scope: asymptotic; Sect. 7, Thms 7.1-7.6). N_X(t)\ge\frac t{2\pi}\log\frac t{2\pi}-\frac t{2\pi}-\frac1\pi\sum_{n\le X^2}\frac{\Lambda_X(n)\sin(t\log n)}{n^{1/2}\log n}+O_X(1) (unconditional, Thm 7.1). Under RH and 2\le X\le t^2 the sum f_X(t)\ll\Phi(t)+\log\tau/\log X (Thm 7.2). Under RH there is a constant C_3 with N_X(t) asymptotic to N(t) up to the same trigonometric sum for X<\exp(\cdot) and an unconditional count N\ll t\log t for X\le t^{C_4} (Thm 7.6). *Conditional on:* RH for Thm 7.2 and 7.5.
- **THM-PAPER-0006-7** (Theorems 8.1-8.2, theorems (simplicity), scope: asymptotic; Sect. 8, Thms 8.1-8.2). Assume RH. There is C_3>0 such that if X<\exp(C_3\log t/\Phi(t)) then all zeros of \zeta_X(\tfrac12+it) with t\ge C_0 are simple and N_X^{(1)}(t)=N_X(t) is given by Thm 7.1. Unconditionally, for X\le\exp(o(\log^{1-\epsilon}t)), the number of simple zeros up to height t is (1+o(1))\frac t{2\pi}\log\frac t{2\pi}. *Conditional on:* RH for Thm 8.1.
- **THM-PAPER-0006-8** (Theorem 9.1, theorem (conditional), scope: asymptotic; Sect. 9, Theorem 9.1). Assume RH. Let \gamma<\gamma' be consecutive zeta zero ordinates and I a closed subinterval of (\gamma,\gamma'). Then for all sufficiently large X, \zeta_X^*(\tfrac12+it) has no zeros in I and |\zeta_X^*(\tfrac12+it)|\to2|\zeta(\tfrac12+it)| as X\to\infty, uniformly in t in I. So zeros of zeta_X converge to the zeros of zeta. *Conditional on:* RH.

### Key definitions

- \tau=|t|+2
- \Lambda_X(n) smoothed von Mangoldt weight supported on n\le X^2
- P_X(s)=\exp\big(\sum_{n\le X^2}\Lambda_X(n)/(n^s\log n)\big)
- Z_X(s) product over zeros using F_2(z)=2E_2(2z)-E_2(z)
- admissible function \Phi(t)
- \zeta_X(s)=P_X(s)+\chi(s)\overline{P_X}(s)-type function (see audit note)
- N_X(t) count of zeros of \zeta_X

### Principal lemmas

- **THM-PAPER-0006-L1** (Lemma 3.2; Sect. 3, Lemma 3.2, Eqs. (16)-(17)). Assume RH, \Phi admissible, \sigma>1/2 bounded. Then \sum_\gamma\frac{\sigma-1/2}{(\sigma-1/2)^2+(t-\gamma)^2}\ll\log\tau+\frac{\Phi(t)}{\sigma-1/2}. — *Role:* Controls the sum over zeros defining Z_X(s) and R_X(s); converts RH into a bound in the right half of the strip.
- **THM-PAPER-0006-L2** (Theorem 2.1; Sect. 2, Theorem 2.1 and the mean square argument (4)). Let \sigma be bounded, \sigma\ge1/2, |s-1|>1/10, 1\le X\le t^2. The Lindelof Hypothesis holds iff \zeta(s)=\sum_{n\le X}n^{-s}+O(X^{1/2-\sigma}\tau^\epsilon). — *Role:* Contrast: short Dirichlet sums approximate zeta on the right half-strip under Lindelof, while the unconditional argument in Sect. 2 shows short sums cannot work on \sigma\le1/2.
- **THM-PAPER-0006-L3** (Theorem 4.1; Sect. 4, Theorem 4.1). Assume RH, \sigma\ge1/2 bounded, |s-1|>1/10, 2\le X\le t^2. Then \zeta(s)=\sum_{n\le X}n^{-s}+O(X^{1/2-\sigma}e^{C_1\Phi(t)}). — *Role:* Dirichlet-sum approximation under RH with an explicit error term, compared with the Euler product approximation.
- **THM-PAPER-0006-L4** (Lemma 6.1; Sect. 6, Lemma 6.1). There is an absolute C_0>0 such that if |\chi(\sigma+it)|=1 with 0\le\sigma\le1 and t\ge C_0, then \sigma=1/2. — *Role:* Gives RH for \zeta_X (Theorem 6.2).

### Proof architecture

Start from the explicit formula for zeta'/zeta with the smoothed weights Lambda_X (Titchmarsh Thm 14.20) to get the exact factorization zeta = P_X Z_X (Thm 3.1). Under RH, Lemma 3.2 bounds the zero sum in Z_X, making Z_X close to 1 away from the critical line, whence Theorem 3.3-3.5. The converse of Thm 3.5 uses that a zero of zeta at beta+i gamma with beta large contradicts the uniform bound on zeta/P_X - 1. Section 5 defines zeta_X(s)=P_X+chi*conj(P_X) so the functional equation is exact; RH for zeta_X is a one-line consequence of |chi|=1 only on the line. Sect. 7-8 count and show simplicity of zeros of zeta_X via argument of P_X on the line (the trigonometric prime sum) and its derivative. Sect. 9 compares zeta_X with zeta on the line under RH.

Dependency edges: CAND-01192 → Gonek-Hughes-Keating hybrid product (uses and refines); CAND-01192 → Titchmarsh Thm 14.20 (uses explicit formula)

**Imported results.** Gonek-Hughes-Keating hybrid Euler-Hadamard product [10]; Titchmarsh Theorem 14.20 (explicit formula for zeta'/zeta) and Theorem 13.3 (Lindelof criterion); Goldston-Gonek bound for admissible Phi(t)=(1/2)log tau/loglog 2tau [ref in Sect. 3] and Phi(t)=(1/6)log tau; Standard bounds for sums over zeros under RH; Mean value theorems for Dirichlet polynomials

**Techniques.** Explicit formula with smoothed Lambda_X weights; Second exponential integral E_2 and function F_2; Control of sums over zeros via admissible Phi(t) (Goldston-Gonek type bounds); Gonek-Hughes-Keating hybrid Euler-Hadamard product; Functional equation modeling zeta_X=P_X+chi*conj(P_X); Zero counting by argument principle and prime trigonometric sums; Mean square estimates for Dirichlet polynomials

## Context and interpretation

**Importance and obstacle overcome.** Provides an RH-equivalent-type criterion in terms of finite Euler products (forward direction and converse for finitely many zeros) and a tractable model family for which RH, simplicity and repulsion can be proved. The obstacle is crossing sigma=1/2 where the Euler product stops converging; it is overcome by using the functional equation to define zeta_X in sigma>=1/2 only.

**Relation to prior work.** Builds on Gonek-Hughes-Keating hybrid product (explicit version needed here), Titchmarsh's Lindelof-sum approximation, and Goldston-Gonek bounds on sums over zeros. Compared with the Dirichlet sum approximation in Sect. 2 and 4.

**Limitations and open questions.** The author notes the X-range in the simplicity and zero counting theorems is probably too restrictive and hopes to extend it; the best modelling is expected for X a power of t but results are most satisfactory for smaller X. Convergence of zeta_X zeros to those of zeta (Thm 9.1) is for fixed X-large uniformly only on closed subintervals between zeros; the paper offers no unconditional result about zeta's own zero multiplicity or repulsion. Analogues for L-functions are discussed in Sect. 11 but not read in detail.

## Research potential

- **Hypotheses that might be weakened.** Theorem 3.5 and Thm 5.1 converse: the exponent C>1 and the region sigma>=1/2+C log log(2 tau)/log X; one could try to push C towards 1 or reduce the region using stronger results on Phi(t) (e.g. Carneiro-Chandee-Milinovich on arg and log zeta under RH). Theorem 8.1 needs X<exp(C_3 log t/Phi(t)); extending towards X=t^c is flagged by the author.
- **Generalizations.** Sect. 11 constructs L_X(s,chi) for Dirichlet L-functions and studies linear combinations; one could attempt Selberg class members, and apply the P_X converse as a one-sided RH test in a region (no finite number of zeros beyond the curve).
- **Candidate connections.** Gonek-Hughes-Keating hybrid product; Li coefficients (CAND-01183, CAND-01219) through Euler product versus archimedean splitting; Euler-product-based RH criteria and Lindelof; random matrix models of zeta zeros.
- **Reusable lemmas.** Lemma 3.2 (zero-density sum) and Theorem 3.1 (explicit factorization with remainder) are reusable and unconditional for the latter. Lemma 6.1 and Theorem 6.2 give a simple template: a function P+chi*conj(P) with P nonvanishing satisfies RH iff |chi|=1 localizes to the line.
- **Possible experiments.** Compute zeta_X zeros for X in {10,20,50,100} on 0<t<10^4 and compare with true zeros; check |zeta_X|/|zeta| approaching 2 between zeros, and test the finite-zero converse by examining P_X(s)/zeta(s)-1 on lines sigma=1/2+C loglog(tau)/log X with a synthetic off-line zero.
- **Risks / barriers.** The criterion is a converse about finitely many zeros in a shrinking region, not RH itself; an unconditional version would require a bound on zeta/P_X - 1 uniformly down to the line, which is equivalent in strength to control of the zero sum Z_X. Numerics for zeta_X constrain only finite ranges.

## Audit notes (Level 1 reader)

Statement of Theorem 3.1 in the text extraction has the error term garbled (the O-term shows 'X^{-sigma-2}/(tau^2 log^2 X)'), so the exact error in (10) was reconstructed and needs checking against the source. The Theorem 3.3 error R_X uses the term X/(tau^2 log^2 X) read from the extraction. The definition of zeta_X(s) in text reads P_X(s)+chi(s)P_X-bar(s) with overlines lost, so the precise reflection is reconstructed and should be verified. Section 12 (appendix) and Sect. 10-11 were not read. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01192`; harvest queries: kw_RH_any, msc_11M06, msc_11M26, arxiv_critical_line, arxiv_rh_abs, arxiv_rh_ti.
- Triage decision: include — Equivalence of RH with approximation of zeta by finite Euler products.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

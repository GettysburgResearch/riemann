# PAPER-0124 — The mean-value of the Riemann zeta function

| Field | Value |
|---|---|
| Authors | Atkinson, F. V. |
| Year / stratum | 1949 / S2 |
| Venue | Acta Math. 81, 353-376 (1949). |
| Identifiers | zbMATH [0036.18603](https://zbmath.org/?q=an:0036.18603) · DOI [10.1007/BF02395027](https://doi.org/10.1007/BF02395027) |
| MSC | 11M06 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5697-11511_2006_Article_BF02395027.pdf (MathSciDoc archive copy of Acta Math. 81 (1949), 353-376) |
| Selection | score 4.0143, in-pool citations 67, seed lists 2, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Give an explicit formula with controlled error for I(T)=\int_0^T|\zeta(1/2+it)|^2dt, i.e. for the error term E(T)=I(T)-T\log(T/2\pi)-(2\gamma-1)T in the Hardy-Littlewood second-moment asymptotics, as a divisor-problem-type (Voronoi) expansion.

**Historical motivation.** Hardy-Littlewood: I(T)~T log T; Littlewood: error O(T^{1/2+eps}); Ingham and Titchmarsh reduced the exponent. Atkinson exploits the analogy with the Dirichlet divisor problem sum d(n) to obtain an exact expansion rather than just a bound, anticipating Omega and mean-square results for E(T).

### Main results

- **THM-PAPER-0124-1** (Theorem (p. 354), theorem (Atkinson's formula), scope: asymptotic; p. 354 (Theorem), assembled at the end (substituting (7.1),(7.2),(8.2),(10.2) into (4.4))). Let I(T)=\int_0^T|\zeta(\tfrac12+it)|^2dt. For T>\tau_0 and A T<N<A'T (any fixed 0<A<A'), I(T)=T\log T-T(1+\log 2\pi-2\gamma)+\Sigma_1+\Sigma_2+O(\log^2T) where, schematically, \Sigma_1 is a sum over n\le N of terms of size (T/2\pi)^{1/4}\sqrt2\,(-1)^n d(n)n^{-3/4}\,e(T,n)^{-1}\sin\big(2T\sinh^{-1}\sqrt{\pi n/2T}+\sqrt{2\pi nT+\pi^2n^2}-\pi/4\big)-type with e(T,n) =(1+\pi n/2T)^{1/4}-type amplitude, and \Sigma_2=-2\sum_{n\le N'}d(n)n^{-1/2}\big(\log\tfrac{T}{2\pi n}\big)^{-1}\sin\big(T\log\tfrac{T}{2\pi n}-T+\tfrac\pi4\big)-type, N'=\tfrac{T}{2\pi}+O(\sqrt T)-type cutoff. Exact amplitude/phase forms are taken from a garbled OCR of p.354 and from memory of the standard statement (E(T)=\Sigma_1+\Sigma_2+O(\log^2 T)); must be rechecked against the PDF image before citation. d(n) is the divisor function.
- **THM-PAPER-0124-2** (Eq. (3.4) (identity), lemma/identity, scope: global; Section 3, eqs (3.2)-(3.4)). For 0<\Re u<1: \zeta(u)\zeta(1-u)=\tfrac12\zeta(1-u)\Big[\tfrac{\Gamma'}{\Gamma}(1-u)+\tfrac{\Gamma'}{\Gamma}(u)\Big]\!\!\Big|_{\text{(schematic)}}+2\gamma-\log 2\pi+g(u,1-u)+g(1-u,u), with g(u,v)=2\sum_{n\ge1}d_{?}\ldots (see (3.2)); exact form garbled in OCR.

### Key definitions

- I(T)=\int_0^T|\zeta(1/2+it)|^2dt
- f(u,v)=\sum_{r,s\ge1}r^{-u}(r+s)^{-v}
- g(u,v) defined by (1.4)
- h(u,x)=2\int_0^\infty y^{-u}(1+y)^{u-1}\cos2\pi xy\,dy (4.3)

### Principal lemmas

- **THM-PAPER-0124-L1** (Eq. (2.1) and Section 2; Section 2). For \Re u,\Re v>1: \zeta(u)\zeta(v)=\zeta(u+v)+f(u,v)+f(v,u), where f(u,v)=\sum_{r\ge1}\sum_{s\ge1}r^{-u}(r+s)^{-v}; f is meromorphic for \Re(u+v)>0. — *Role:* Reduces |zeta|^2 to a double series classified by m-n, enabling Poisson summation.
- **THM-PAPER-0124-L2** (Section 3 (Poisson step); Section 3, (3.1)-(3.2)). For \Re u<0,\Re v>1,\Re(u+v)>0, g(u,v)=2\sum_{n\ge1}\sigma_{u+v-1}(n)\int_0^\infty y^{-u}(1+y)^{-v}\cos 2\pi ny\,dy-type, giving a divisor-sum expansion (g defined via f and Gamma factors as in (1.4)). — *Role:* Produces a single series with divisor-type coefficients; analytic continuation to the critical line.
- **THM-PAPER-0124-L3** (Section 4, (4.1)-(4.6); Section 4). Using Voronoi's formula d(n)=D(x)+\Delta(x) with \Delta(x) expressed by Bessel-type series (error O(x^{1/2}\log x)), g(u,1-u) is continued to \Re u=1/2 and I(T) is written as T\log T-T(1+\log2\pi-2\gamma)+I_1-I_2+I_3-I_4+O(1) (eq. (4.4)) with explicit oscillatory integrals (4.5),(4.6). — *Role:* Core structural step: approximate-functional-equation-type expression integrated along the critical line.
- **THM-PAPER-0124-L4** (Lemma 1 (p. 361); Section 5). Saddle-point lemma for \int_a^b\phi(x)\exp\{2\pi i(f(x)+kx)\}dx with f real, f''>0 on [a,b], f,\phi analytic in strips |z-x|\le\mu(x) with bounds \phi=O(\Phi), f=O(F\mu^{-1}), (f')^{-1}=O(\mu^2\Phi^{-1}) (exact conditions garbled), giving main term at the stationary point x_0 of f'+k plus explicit endpoint and error terms. — *Role:* General first-derivative saddle-point/stationary-phase tool used for every oscillatory integral.
- **THM-PAPER-0124-L5** (Lemma 2 (Section 6); Section 6). Asymptotic evaluation (stationary point plus O(a^{...}T^{-...})+O(b...)+R(T,k)) of integrals \int_a^b y^{-\alpha}(1+y)^{-\beta}(\log\tfrac{1+y}{y})^{-\gamma}\exp i\{T\log\tfrac{1+y}{y}+2\pi ky\}dy under a,b,\alpha,\beta,\gamma bounded etc. (statement garbled in OCR). — *Role:* Application of Lemma 1 to the integral types in I_1,I_2,I_3,I_4.
- **THM-PAPER-0124-L6** (Lemma 3 (Section 9/10); before (10.1)). Evaluation of the I_4-type integral: for n with T/(\pi(n^2-n)^{...})-type condition (10.1) the integral equals a main term involving d(n)n^{-1/2}(\log(T/2\pi n))^{-1}\sin(T\log\tfrac{T}{2\pi n}-T+\tfrac\pi4) plus O(T^{-1/2}...) (garbled). — *Role:* Produces the second group of oscillating terms, truncated at Z=T/2\pi+O(\sqrt T); tails controlled by partial summation with the divisor asymptotic.

### Proof architecture

(1) Write 2i*I(T)=\int \zeta(u)\zeta(1-u)du along u=1/2+it. (2) Identity zeta(u)zeta(v)=zeta(u+v)+f(u,v)+f(v,u), analytic continuation of f (Sec. 2). (3) Poisson summation in r gives g(u,v)=series with divisor coefficients, valid for Re u<0; continuation to 0<Re u<1 yields (3.4). (4) On u+v=1, continue g(u,1-u) to Re u=1/2 via Voronoi's summation formula for d(n) (Sec. 4); integrate to get I(T)=main terms+I_1-I_2+I_3-I_4. (5) Evaluate oscillatory integrals by a saddle-point lemma (Lemma 1, 2); outputs two sets of terms (Voronoi-like with arsinh phase, and a log(T/2 pi n) phase). (6) Estimate error pieces by second mean value theorem and partial summation (Secs 7-10). Imported: Voronoi summation, Poisson formula, Stirling, Hardy-Littlewood/Ingham/Titchmarsh asymptotics (historical).

Dependency edges: CAND-00078 → Voronoi summation formula (imports); CAND-00078 → Hardy-Littlewood 1918 / Ingham 1926 / Titchmarsh 1934 (improves); CAND-00409 → CAND-00078 (same family of mean-value methods (off-diagonal analysis))

**Imported results.** Voronoi's summation formula for the divisor function (Oppenheim, Proc. LMS 26 (1927)); Poisson summation formula; Stirling's formula; Hardy-Littlewood (1918), Littlewood (1922), Ingham (1926), Titchmarsh (1934): previous asymptotics and error exponents O(T^{1/2+eps}) -> O(T^{1/2}) and 5/12 (as stated in introduction, partly garbled)

**Techniques.** Voronoi summation formula; Poisson summation; Analytic continuation of double Dirichlet-type series; Stationary phase / saddle-point lemma; Divisor-problem analogy; Partial summation

## Context and interpretation

**Importance and obstacle overcome.** First exact explicit formula for the error term in the second moment of zeta on the critical line. Obstacle: unlike the divisor problem there is no direct Voronoi formula for |zeta|^2; Atkinson builds it from the zeta(u)zeta(v) double series with u+v=1 on the boundary of convergence, using analytic continuation in both variables and a careful saddle-point treatment.

**Relation to prior work.** Improves Ingham/Titchmarsh error terms O(T^{1/2}log T)-type to an expansion with O(log^2 T) remainder; gives the zeta analogue of the Voronoi expansion for Delta(x). Introduction says a follow-up on the connection to the divisor problem was planned.

**Limitations and open questions.** Does not itself give sharp bounds for E(T); those (E(T)=O(T^{1/3+eps})-type, mean-square of E(T), Omega-results) require further work. Unconditional, no RH implication. Constants A,A' and cutoffs N, N' are tied to T.

## Research potential

- **Hypotheses that might be weakened.** The restriction AT<N<A'T on the cutoff and the O(log^2T) remainder; sharper smoothing could lower the log power.
- **Generalizations.** Twisted second moment of zeta/Dirichlet L-functions (Atkinson-type formulas for \int |L(1/2+it,chi)|^2 and for \zeta with Dirichlet-polynomial twists); fourth moment analogues (Motohashi).
- **Candidate connections.** Mollified mean-square computations (Levinson/Conrey) use the same off-diagonal structure; Atkinson's f(u,v) decomposition is the root of the off-diagonal term analysis.
- **Reusable lemmas.** Lemma 1 (saddle-point with analytic strip hypotheses) is a self-contained reusable tool for oscillatory integrals with explicit endpoint errors.
- **Possible experiments.** Numerically evaluate E(T) at T in [10^3,10^6] via Odlyzko-Schonhage values and compare with Sigma_1+Sigma_2 truncated at N=T to validate the exact phase conventions, which are ambiguous in the OCR.
- **Risks / barriers.** Second-moment data is silent about zero locations; any use for RH needs mollified or twisted versions. OCR ambiguity of the main formula means exact statements must be re-extracted from the page images.

## Audit notes (Level 1 reader)

The theorem displayed on p. 354 is garbled in the pdftotext output (sin vs cos phase conventions, amplitude factors); I reconstructed the structure but flag it as unverified. Section titles and Lemma 3 statement boundaries also unclear. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00078`; harvest queries: kw_moments_zeta, msc_11M06.
- Triage decision: include — Atkinson's exact formula for the mean square error term.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

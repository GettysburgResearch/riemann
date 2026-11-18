# PAPER-0096 — Half-isolated zeros and zero-density estimates

| Field | Value |
|---|---|
| Authors | Maynard, James; Pratt, Kyle |
| Year / stratum | 2024 / S7 |
| Venue | Int. Math. Res. Not. 2024, No. 19, 12978-13014 (2024). |
| Identifiers | zbMATH [1566.11085](https://zbmath.org/?q=an:1566.11085) · DOI [10.1093/imrn/rnae191](https://doi.org/10.1093/imrn/rnae191) · arXiv [2206.11729](https://arxiv.org/abs/2206.11729) |
| MSC | 11M26, 11M06 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/2206.11729 |
| Selection | score 4.3142, in-pool citations 1, seed lists 0, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Can zero detection be made sensitive to the vertical distribution of zeros so as to improve the Ingham-Huxley zero-density bound N(sigma,T)<<T^{12/5(1-sigma)+o(1)}? Result: unconditional detection of 'half-isolated' zeros by short Dirichlet polynomials, and under Hypothesis F (zeros on finitely many vertical lines) the Density Hypothesis up to exp((loglog T)^{O(1)}).

**Historical motivation.** The exponent 12/5 (Ingham-Huxley, ~80 years old) gives primes in [x,x+x^{7/12+o(1)}]; no progress for sigma<=3/4. Heath-Brown (unpublished), Balasubramanian-Ramachandra and Conrey-Iwaniec detected isolated zeros with Turan power sums but fail with ~log T neighbouring zeros. Obstructed by vertical arithmetic progressions of zeros.

### Main results

- **THM-PAPER-0096-1** (Theorem 1, theorem (conditional), scope: conditional; Sec. 1; proof Sec. 5 via Props 20, 21). Assume Hypothesis F (the non-trivial zeros of \zeta lie on a finite number of fixed vertical lines). Then N(\sigma,T)\ll T^{2(1-\sigma)}\exp((\log\log T)^{O(1)}), where N(\sigma,T)=\#\{\rho=\beta+i\gamma:\zeta(\rho)=0,\beta\ge\sigma,0\le\gamma\le T\}. *Conditional on:* Hypothesis F.
- **THM-PAPER-0096-2** (Corollary 2, corollary (conditional), scope: conditional; Sec. 1; proof end Sec. 5). Under Hypothesis F, for \epsilon>0, \#\{p\in[x,x+x^{1/2+\epsilon}]\}=(1+o_\epsilon(1))\,x^{1/2+\epsilon}/\log x. *Conditional on:* Hypothesis F.
- **THM-PAPER-0096-3** (Corollary 3, corollary (conditional), scope: conditional; Sec. 1). Under Hypothesis F, with C large and y=\exp((\log\log X)^C), \#\{p\in[x,x+y]\}=(1+o(1))y/\log x for all but O(X\exp(-(\log\log X)^2)) integers x\in[X,2X]. *Conditional on:* Hypothesis F.
- **THM-PAPER-0096-4** (Theorem 4 (quantified as Proposition 16), theorem (unconditional), scope: asymptotic; Sec. 1; Sec. 4 Prop 16). There are an absolute C\ge1 and a fixed smooth non-negative w_0 supported in [1/2,2] such that if \rho_0=\beta_0+i\gamma_0 is half-isolated (Def. 9) with \gamma_0\in[T,2T], there is real Y\in[T^{(\log\log T)^3/\log T},T^{5/\log\log T}] with \Big|\sum_{n}\frac{\Lambda(n)}{n^{\rho_0}}w_0(n/Y)\Big|\ge(\log T)^{-C}.
- **THM-PAPER-0096-5** (Corollary 5, corollary (unconditional), scope: asymptotic; Sec. 1). The number of half-isolated zeros \rho_0=\beta+i\gamma with \beta\ge\sigma, \gamma\in[T,2T] is at most T^{2(1-\sigma)+o(1)} (Density Hypothesis strength).
- **THM-PAPER-0096-6** (Theorem 6 / Proposition 37, theorem (conditional, speculative), scope: conditional; Sec. 1; Appendix A). Assume Hypothesis F and that on each line with real part >1/2 zeros occur only in clusters of size \le T^{\epsilon_0}. Then \int_0^T|\zeta(1/2+it)|^5dt\ll_{\epsilon} T^{1+O(\epsilon_0)+\epsilon}. *Conditional on:* Hypothesis F, cluster-size bound T^{eps_0}.
- **THM-PAPER-0096-7** (Proposition 21, proposition (conditional), scope: conditional; Sec. 5; proved Sec. 6-7). Assume Hypothesis F, \sigma\in[1/2,1]. Then R_{N,H}(\sigma)\ll T^{2(1-\sigma)}\exp((\log\log T)^{O(1)}). *Conditional on:* Hypothesis F.

### Key definitions

- Hypothesis F: zeros lie on finitely many fixed vertical lines
- Y-half-isolated and half-isolated zero (Defs 8-9)
- cluster and maximal cluster (Def 18)
- R_{N,H}(sigma) (Def 19)
- detection by Dirichlet polynomial of length N (Def 17)
- 'bow' of zeros (Sec. 8): vertical arithmetic progression with real parts varying 1/2 -> sigma -> 1/2

### Principal lemmas

- **THM-PAPER-0096-L1** (Lemma 11 (Refined power sum estimate); Sec. 4). Let A,B>0, B large, z_1..z_R,c_1..c_R\in\mathbb C with z_1=0,c_1=1; \Im z_r\ge0; |\Re z_r|\le 1/(10A); |\arg c_r|\le1/10 if |\Im z_r|\le(\log B)^2/A; B\ge R\sum|c_r|... (precisely B\ge\sum_r|c_r|). Then \exists t\in[A,2A]: |\sum_r c_r e^{t z_r}|\ge B^{-99}. — *Role:* Polynomially (not exponentially) small Turan-type lower bound with t confined to a short real interval; engine of Thm 4. Proof via Lemma 10 (Jensen/subharmonic bound on the half-plane). Remark 13 shows each hypothesis is necessary; Remark 14: independently found by Bourgain and Sawin.
- **THM-PAPER-0096-L2** (Lemma 10; Sec. 4). If f analytic on closed upper half-plane with |f(z)|\le\exp(O(|z|^{1/2})), then \log|f(x+iy)|\le\frac y\pi\int_{\mathbb R}\frac{\log|f(t)|}{(t-x)^2+y^2}dt. — *Role:* Subharmonicity / Poisson-Jensen inequality used in proof of Lemma 11.
- **THM-PAPER-0096-L3** (Lemma 15; Sec. 4). With \rho_0 a zero, \gamma_0\in[T,2T], S_\approx(\rho_0) the zeros with \gamma_0\le\gamma\le\gamma_0+(\log T)^2,|\beta-\beta_0|\le1/(10\log Y), and W analytic with W(0)=1, there is Z in a discrete set V with \big|\sum_{\rho\in S_\approx}W(\rho-\rho_0)Z^{\rho-\rho_0}\big|\ge(\log T)^{-100}. — *Role:* Applies Lemma 11 to the local zero sum; requires half-isolation (no zeros to the right or below).
- **THM-PAPER-0096-L4** (Definitions 8-9; Sec. 4). \rho_0 is Y-half-isolated if every zero \rho' with |\rho'-\rho_0|\le(\log|\gamma_0|)^2 satisfies either |\beta'-\beta_0|\le1/(10\log Y) and \gamma'\ge\gamma_0, or \beta'\le\beta_0-(\log\log|\gamma_0|)^2/\log Y; \rho_0 is half-isolated if Y-half-isolated for some Y with (\log\log|\gamma_0|)^3\le\log Y\le\log|\gamma_0|/\log\log|\gamma_0|. — *Role:* Defines the class of zeros detectable by short polynomials.
- **THM-PAPER-0096-L5** (Proposition 20; Sec. 5-6). Assume Hypothesis F, sigma with zeros on Re s=sigma. Exists c_F>0: N(\sigma,2T)-N(\sigma,T)\ll T^{2(1-\sigma)}(\log T)^{O(1)}+N(\sigma+c_F,3T)(\log T)^{O(1)}+(\log T)^{O(1)}\sup_{T^{1/100}\le N\le T^{1/2}(\log T)^2,\,1\le H\ll T}R_{N,H}(\sigma). — *Role:* Combinatorial reduction using clusters (Def 18) and Type I/II/A-D classification; iterated O(1) times thanks to finitely many lines.
- **THM-PAPER-0096-L6** (Lemma 35; Sec. 7). Under Hypothesis F, there is a set D of at most \exp((\log\log T)^3) Dirichlet polynomials such that for any half-isolated \rho_0=\sigma+i\gamma and any A with \log A\in[(\log\log T)^4,\log T] there is B\in D with |B(\rho_0)|\ge\exp(-(\log\log T)^3), B(s)=\sum b(m)m^{-s}, |b(m)|\le\exp((\log\log T)^3), supported on m\in[Ae^{-2(\log\log T)^4},Ae^{(\log\log T)^2}]. — *Role:* Detector of flexible length, obtained by iterating Prop 16; allows arbitrary length choice to dodge the 'inconvenient' lengths (T^{2/5}) of Huxley-Ingham.
- **THM-PAPER-0096-L7** (Definition 18 / Lemmas 26,30-34; Sec. 6-7). A cluster is a set of zeros on one vertical line with consecutive ordinates increasing by <(\log T)^3. Maximal clusters are classified by size and by which detecting polynomial length works; Type D clusters contain a half-isolated zero near their bottom. — *Role:* Local-global structure: Hypothesis F implies each cluster has a half-isolated zero at its bottom.

### Proof architecture

Sec. 2 outline: classical zero detector SY(s)=sum Lambda(n)n^{-s}w(n/Y) ~ sum_rho Y^{rho-s}W(rho-s); at s=rho0 this is W(0)+sum over nearby zeros. If no nearby zeros (Heath-Brown isolated zeros) it is large. Vertical arithmetic progressions of zeros with difference 2*pi*c*i/log T make S_Y small for Y<T^{1/c-eps}, hence the restriction to half-isolated zeros (no zeros below). Sec. 4: Lemma 10 -> Lemma 11 (power sum) -> Lemma 15 -> Prop 16 (Thm 4). Under Hypothesis F, zeros on a line sigma form clusters with a half-isolated zero at the bottom; Sec. 5-7: Prop 20 reduces N(sigma,T) to counts R_{N,H} of clusters detected by Dirichlet polynomials of length N, combining Prop 16/Lemma 35 (flexible length detectors) with classical Ingham-Huxley detectors D_N (Def 17) and large-values estimates (mean value/Heath-Brown arrangement, Lemmas 27-28), giving Prop 21. Theorem 1 follows by iterating sigma -> sigma+c_F (O(1) times because finitely many lines). Corollaries 2-3 via explicit formula ([17, Thm 10.5], [8, Sec 7.1, 9.1]). Appendix A: fifth moment via Watt's mean value theorem.

Dependency edges: CAND-02444 → Ingham 1940 / Huxley 1972 zero-density (refines under Hypothesis F); CAND-02444 → Heath-Brown isolated zeros; Balasubramanian-Ramachandra; Conrey-Iwaniec (extends zero detection); CAND-02444 → Watt mean value theorem (imports (Appendix A))

**Imported results.** Ingham N(sigma,T)<<T^{3(1-sigma)/(2-sigma)+o(1)}; Huxley N(sigma,T)<<T^{3(1-sigma)/(3sigma-1)+o(1)} (Montgomery, Halasz); Combined 12/5 exponent; Large values estimates for Dirichlet polynomials (Heath-Brown arrangement; Huxley-Montgomery); Watt's mean value theorem; Ivic/Montgomery: N(sigma,T)<<T^{3/2(1-sigma)... } near sigma=1 (167(1-sigma)^{3/2}) from [18, Cor 12.5]; N(T+1)-N(T)<<log T

**Techniques.** Mellin-transform zero detectors with smooth weights; Jensen/Poisson subharmonic inequality for exponential sums with positive coefficients (Turan-type); half-isolation / cluster decomposition of zeros; large values of Dirichlet polynomials (Ingham, Huxley, Heath-Brown arrangement); Watt's mean value theorem for fifth moment

## Context and interpretation

**Importance and obstacle overcome.** First method for detecting zeros that tolerates many nearby zeros (as long as none lies below/right), giving an unconditional density result for a natural class and a conditional full Density Hypothesis under a rigidity hypothesis that is a strict weakening of RH (RH => Hypothesis F). Obstacle: power-sum bounds exponentially small in R; overcome by Lemma 11 (polynomial lower bound exploiting positivity and real t).

**Relation to prior work.** 

**Limitations and open questions.** Hypothesis F is not known; no unconditional improvement of Ingham-Huxley. Sec. 8: 'bows' of zeros (T^{3/5} of them at height T) are consistent with all current methods and defeat both local power-sum and global cluster arguments; authors say rigidity in real parts seems necessary. Authors suggest Hypothesis F can be relaxed (e.g. (log T)/(loglog T)^2 well-spaced lines in [T,2T]). Question whether only vertical-AP-like configurations make power sums small.

## Research potential

- **Hypotheses that might be weakened.** Hypothesis F -> O(log T/(loglog T)^2) lines per dyadic range (stated by authors); or cluster-size/bow-exclusion hypotheses; Prop 20 constant c_F and its O(1) iteration count is where the 'finitely many lines' enters.
- **Generalizations.** Lemma 11 is a general positive-coefficient Turan lemma usable for any L-function or zero-sum (Dirichlet, Hecke); half-isolation to Selberg class zero-density; apply to Landau-Siegel zero repulsion.
- **Candidate connections.** Zero-repulsion / pair-correlation (bows would need small vertical gaps); least quadratic non-residue obstruction (Remark 36, Heath-Brown); moments of zeta (5th moment, Thm 6).
- **Reusable lemmas.** Lemma 11 and Remark 13 counterexamples (Bourgain example R=12^k); Lemma 10; Prop 16 flexible-length detector Lemma 35.
- **Possible experiments.** Numerically search Odlyzko zero data for near-bow configurations (arithmetic progressions in imaginary parts with drift in real parts, impossible under RH so test only synthetic models); test Lemma 11 sharpness with Bourgain-type examples exponent 0.55; compute how many zeros of zeta at height ~1e22 are half-isolated per Def 9.
- **Risks / barriers.** Bows (Sec. 8, eq. (22)) are explicit potential obstruction; Hypothesis F is conditional and uses finite-line rigidity so gives nothing unconditional. Any claim must keep 'conditional on Hypothesis F' attached.

## Audit notes (Level 1 reader)

none noticed in inspected portion. Minor: Lemma 11 hypothesis (5) is printed 'B >= R sum|c_r|' in the extracted text, which looks like an extraction/typo artefact (the application in Lemma 15 uses B >= sum|c_r|); the Remark 12 case has B=R>A. Sec. 6-7 cluster-type lemmas were not verified line by line.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02444`; harvest queries: kw_zero_density, kw_zeta_zeros, msc_11M06, msc_11M26, arxiv_zero_density, arxiv_zeta_zeros.
- Triage decision: include — Maynard-Pratt new zero detection improves Ingham-Huxley density under RH-adjacent assumptions.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

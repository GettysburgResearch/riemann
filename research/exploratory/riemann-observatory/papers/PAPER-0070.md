# PAPER-0070 — On simple zeros of the Riemann zeta-function

| Field | Value |
|---|---|
| Authors | Bui, H. M.; Heath-Brown, D. R. |
| Year / stratum | 2013 / S5 |
| Venue | Bull. Lond. Math. Soc. 45, No. 5, 953-961 (2013). |
| Identifiers | zbMATH [1291.11118](https://zbmath.org/?q=an:1291.11118) · DOI [10.1112/blms/bdt026](https://doi.org/10.1112/blms/bdt026) · arXiv [1302.5018](https://arxiv.org/abs/1302.5018) |
| MSC | 11M26, 11M06 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1302.5018 |
| Selection | score 4.4957, in-pool citations 17, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Prove, assuming only RH (no GLH), that at least 19/27 of the zeros of zeta are simple, that is $\liminf N^*(T)/N(T)\ge 19/27$, by replacing the Conrey-Ghosh-Gonek (1998) GLH input with Heath-Brown's generalised Vaughan identity.

**Historical motivation.** Under RH, Montgomery's pair correlation gave 2/3 of zeros simple; Cheer-Goldston gave 0.6727; Conrey-Ghosh-Gonek reached 19/27 with the mollifier method but needed GLH (a sixth-moment-type bound for Dirichlet L-functions averages) to control error terms.

### Main results

- **THM-PAPER-0070-1** (Theorem, theorem, scope: asymptotic; Sec 1, p.1). Assuming RH, $\kappa^*:=\liminf_{T\to\infty}N^*(T)/N(T)\ge 19/27$, where $N^*(T)$ counts simple zeros with $0<\gamma<T$ and N(T) counts zeros with multiplicity. *Conditional on:* Riemann Hypothesis.
- **THM-PAPER-0070-2** (Corollary, corollary, scope: asymptotic; Sec 1, p.1-2). Assuming RH, $\kappa_d:=\liminf N_d(T)/N(T)\ge 0.84665$, obtained from the Theorem, Montgomery's inequality $2N^*(T)\le\sum_{0<\gamma\le T}\frac{(m(\rho)-2)(m(\rho)-3)}{m(\rho)}\le\sum m(\rho)-5N(T)+6N_d(T)$, and Cheer-Goldston's $\sum_{0<\gamma\le T} m(\rho)\le(1.3275+o(1))N(T)$ so that $\kappa_d\ge(5+2\kappa^*-1.3275)/6$. *Conditional on:* Riemann Hypothesis, Cheer-Goldston bound (imported; as stated its hypothesis is RH).
- **THM-PAPER-0070-3** (Lemma 2, lemma (key new estimate), scope: asymptotic; Sec 2 end; proved in Sec 3). With $M_\nu$ as in (3) and $M_{\nu,3}$ the part with $\eta<q\le y$, $\eta=L^A$, $L=\log T/2\pi$: $M_{\nu,3}\ll_\epsilon y^{1/3}T^{5/6+\epsilon}+\eta^{-1/2}TL^C$ for $\nu=1,2$, some absolute C>0, unconditionally. With mollifier length $y=T^\vartheta$, $\vartheta<1/2$, this is $o(TL^2)$, resp. $o(TL^3)$, so these terms are negligible.

### Key definitions

- m(rho) multiplicity; N(T), N^*(T), N_d(T)
- kappa^*=liminf N^*/N, kappa_d=liminf N_d/N
- L=log T/(2pi)
- mollifier b(k)=mu(k)P(log(y/k)/log y), y=T^theta, theta<1/2

### Principal lemmas

- **THM-PAPER-0070-L1** (Lemma 1; Sec 2). For fixed $\epsilon>0$ and mollifier $B(s)=\sum_{k\le y}b(k)k^{-s}$ with $b(k)=\mu(k)P(\log(y/k)/\log y)$, P real polynomial, $P(0)=0,P(1)=1$: $S_1=\sum_{0<\gamma\le T}B\zeta'(\rho)=\frac{TL^2}{2\pi}-M_1+O(TL)+O_\epsilon(yT^{1/2+\epsilon})$ and $S_2=\sum B\zeta'(\rho)B\zeta'(1-\rho)=\frac{TL^3}{2\pi}(\frac12+3\vartheta)\int_0^1P^2... -2\Re M_2+\dots$ (see source for exact main term). — *Role:* Imported essentially from Conrey-Ghosh-Gonek (3.13),(3.21),(3.26),(3.27),(5.1),(5.4),(5.5); reduces the problem to bounding M_1,M_2.
- **THM-PAPER-0070-L2** (Lemma 3; Sec 3.2). For any integer $r\ge1$: $\zeta'/\zeta(s)=\sum_{j=1}^r(-1)^{j-1}\binom rj\zeta(s)^{j-1}\zeta'(s)M(s)^j+(1-\zeta(s)M(s))^r\zeta'/\zeta(s)$ with $M(s)=\sum_{n\le X}\mu(n)n^{-s}$ (Heath-Brown's generalised Vaughan identity). — *Role:* Writes a_2 = -Lambda * log * log * b as a convolution of 9 factors (taking r=3, X=T^{1/2}) so that the character sums can be split into products of short Dirichlet polynomials and the maximal large sieve applied. The last term vanishes since Md<T^{3/2}.
- **THM-PAPER-0070-L3** (Eq. (1); Sec 2). Cauchy-Schwarz: $N^*(T)\ge\left|\sum_{0<\gamma\le T}B\zeta'(\rho)\right|^2/\sum_{0<\gamma\le T}|B\zeta'(\rho)|^2$ for any regular B; RH is used to identify $S_2=\sum|B\zeta'(\rho)|^2$. — *Role:* Entry point of the mollifier method; this is the only place RH is used in the deduction.

### Proof architecture

Following CGG: zeros with zeta'(rho)!=0 are simple, so Cauchy gives a lower bound for N^* from first and second mollified moments of zeta' at zeros. Lemma 1 (from CGG, unconditional) expresses these as main terms minus error sums M_1, M_2 (additive-character sums). Express additive characters through Dirichlet characters, split q=1 (main terms), 1<q<=eta=L^A (handled by Siegel's theorem as in CGG), and eta<q<=y (the part that needed GLH in CGG). For the last range: restrict to coprime (k,q), dyadic decomposition, reduce to maximal character sums S(Q,X,d), expand a_2 via Lemma 3 with r=3, X=T^{1/2} into O(L^9) 9-fold convolutions, redistribute d via CGG Lemma 3, treat large-factor terms by Polya-Vinogradov, then Perron's formula and the maximal large sieve. Result Lemma 2. Then choose P(x)=-vartheta x^2+(1+vartheta)x, let vartheta->1/2, giving S_1~(19/24)TL^2/2pi, S_2~(57/64)TL^3/2pi, ratio gives 19/27.

Dependency edges: CAND-01275 → Conrey-Ghosh-Gonek 1998 (kappa*>=19/27 under RH+GLH) (removes GLH from); CAND-01275 → Montgomery 1973 pair correlation (kappa*>=2/3) (improves); CAND-01275 → Cheer-Goldston (kappa*>=0.6727) (improves)

**Imported results.** Conrey-Ghosh-Gonek, Proc. LMS 76 (1998) 497-522: Lemma 1 and its main terms; CGG Lemma 3 on convolution divisor splitting; Heath-Brown, generalised Vaughan identity (Lemma 3); Siegel's theorem on exceptional zeros; Montgomery's inequality and Cheer-Goldston's sum bound for the Corollary; Large sieve (Montgomery-Vaughan type maximal version)

**Techniques.** Mollified moments of zeta' at zeros; Heath-Brown generalised Vaughan identity; Maximal large sieve for Dirichlet characters; Polya-Vinogradov; Perron's formula; Siegel's theorem for small moduli; Cauchy-Schwarz

## Context and interpretation

**Importance and obstacle overcome.** Shows GLH is unnecessary for the 19/27 simple-zero proportion. Obstacle: the sum over characters q in (L^A, y] with a_2 supported on a long range, where X is too large compared with Q for Cauchy plus the large sieve; overcome by more flexible factorization from the generalised Vaughan identity and using short Dirichlet polynomials instead of L(s,chi).

**Relation to prior work.** Same mollifier and same constant as CGG; the new content is unconditional treatment of the error M_{nu,3}. The authors also note a place where CGG appears to run into difficulties when deducing [6;(7.2)] from [6;(5.15)] and repair it via coprimality (Sec 3.1).

**Limitations and open questions.** Still conditional on RH, and the constant 19/27 is the limit of the CGG mollifier of this shape with theta<1/2. Improvement would need a longer mollifier (theta>1/2) or different structure. Does not give any simple-zero result without RH (best unconditional kappa^* is 0.4058, quoted).

**Ideas in remarks/appendices/abandoned paths.** Sec 3.1 remark on a technical gap in CGG's passage from (5.15) to (7.2); comment that finite Dirichlet polynomials sum_{h~H} h^{-s} psi(m) are more efficient than L(s,psi) when H is small.

## Research potential

- **Hypotheses that might be weakened.** RH enters only at S_2=sum |B zeta'(rho)|^2 identification; a version with a quantitative zero-density hypothesis could be tried, giving the same bound if the off-line contribution is controlled.
- **Generalizations.** Extend the same technique to other mollified moment results of Conrey-Ghosh-Gonek type that assumed GLH (e.g. multiplicities, gaps, or L-function families), and to Dirichlet L-functions simple zeros.
- **Candidate connections.** Pair-correlation and extremal-function bounds on the multiplicity sum (relevant to Cheer-Goldston constant 1.3275 in the corollary); lengthening the mollifier beyond y=T^{1/2}.
- **Reusable lemmas.** Lemma 2 (unconditional bound for the Dirichlet-character error sum) and the Vaughan-identity splitting scheme with Perron plus maximal large sieve are reusable wherever GLH-conditional character sum estimates appear.
- **Possible experiments.** Numerically check the main terms S_1~(19/24) T L^2/2pi and S_2~(57/64) T L^3/2pi against tabulated zeros of zeta' using Odlyzko data for moderate T.
- **Risks / barriers.** Convergence in L of the o(1) terms is slow (L^A factors); not usable numerically at accessible heights.

## Audit notes (Level 1 reader)

Extracted text drops exponents (the polynomial reads 'P(x)=-theta x+(1+theta)x' where it should be -theta x^2+(1+theta)x; I reconstruct this from the integral evaluations 19/24 and 57/64 but did not recompute). The statement of S_2 in Lemma 1 as extracted looks garbled; I report the main-term shape only. The remainder of Sec 3 after the Perron formula was not read, so the final large-sieve optimization yielding Lemma 2's exponents 1/3 and 5/6 was not checked. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01275`; harvest queries: kw_RH_any, kw_zeta_zeros, msc_11M06, msc_11M26, arxiv_rh_abs, arxiv_zeta_zeros.
- Triage decision: include — 19/27 simple zeros under RH alone.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

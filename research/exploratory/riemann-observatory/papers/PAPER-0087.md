# PAPER-0087 — Jensen polynomials for the Riemann xi-function

| Field | Value |
|---|---|
| Authors | Griffin, Michael J.; Ono, Ken; Rolen, Larry; Thorner, Jesse; Tripp, Zachary; Wagner, Ian |
| Year / stratum | 2022 / S6 |
| Venue | Adv. Math. 397, Article ID 108186, 17 p. (2022). |
| Identifiers | zbMATH [1490.11086](https://zbmath.org/?q=an:1490.11086) · DOI [10.1016/j.aim.2022.108186](https://doi.org/10.1016/j.aim.2022.108186) · arXiv [1910.01227](https://arxiv.org/abs/1910.01227) |
| MSC | 11M26, 11M06 |
| Families | B, C |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/1910.01227 |
| Selection | score 4.3687, in-pool citations 6, seed lists 1, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Make the GORZ asymptotic hyperbolicity result effective: give an explicit threshold N(d) such that the Jensen polynomials of xi are hyperbolic for n>=N(d); and relate low-lying zeros of xi^{(m)} to hyperbolicity for n>=m.

**Historical motivation.** GORZ (PNAS 2019) proved for each d hyperbolicity for n>=N(d) but ineffectively. An effective bound was needed to compare with Chasse's results (all n, d<=2e17) and Bombieri's commentary that large n and large d regimes complement each other.

### Main results

- **THM-PAPER-0087-1** (Theorem 1.1, theorem, scope: global; Sec 1, proof Sec 2.2). There is an absolute constant $c>0$ such that $J^{d,n}(X)=\sum_{j\le d}\binom dj\gamma(n+j)X^j$ is hyperbolic for all $d\ge1$ and $n\ge c\,e^{d/2}$, where $\psi(z)=\xi(1/2+z)=\sum\gamma(j)z^{2j}/j!$.
- **THM-PAPER-0087-2** (Theorem 1.2, theorem, scope: finite; Sec 1, proof Sec 5). If $RH_m(T)$ holds (all zeros $\rho^{(m)}$ of $\xi^{(m)}$ with $|\mathrm{Im}\rho^{(m)}|\le T$ lie on $\mathrm{Re}=1/2$) and $d\le\lfloor T\rfloor^2$, then $J^{d,n}$ is hyperbolic for all $n\ge m$. (A mild generalization of Chasse's Thm 1.8, recovers it for m=0.)
- **THM-PAPER-0087-3** (Corollary 1.3, corollary, scope: computational; Sec 1). Using Platt's verification $RH_0(3.06\times10^{10})$, $J^{d,n}$ is hyperbolic for all $n\ge0$ whenever $d\le9.36\times10^{20}$. *Conditional on:* Platt's rigorous computation of zeros up to 3.06e10.
- **THM-PAPER-0087-4** (Theorem 2.1, theorem, scope: asymptotic; Sec 2.1, proof Sec 3). With $\Delta(M)=\sqrt{\tfrac12(1-\gamma(M-2)\gamma(M)/\gamma(M-1)^2)}$ (real by log-concavity from hyperbolicity of $J^{2,n}$): (1) $\Delta(M)\sim1/\sqrt{2M}$, and for C>1, $M>M_C$ implies $1/\sqrt{2C(M-1)}\le\Delta(M)\le1/\sqrt M$; (2) there are holomorphic $G_m(z)$ on Re z>1 with $\log\frac{\gamma(M-j)}{\gamma(M)}=-\sum_{m\ge1}G_m(M)\Delta(M)^{2m-2}j^m$ for $1\le j<M$, $|G_m(M)|\ll_C(2C)^m$ uniformly, and $\lim G_m(M)=\frac{2m-1}{m(m-1)}$ as read from text; (3) $G_2(M)=1+(1-3G_3(M))\Delta(M)^2+O(\Delta^4)$.
- **THM-PAPER-0087-5** (Lemma 2.2, lemma, scope: finite; Sec 2.1). For the normalization $\tilde J^{d,n}(X)=\sum_kA_{d,k}(n)X^{d-k}$: $A_{d,0}=1$, $A_{d,1}=0$, $A_{d,2}=-d(d-1)$, so $\tilde J^{1,n}=H_1(X/2)$, $\tilde J^{2,n}=H_2(X/2)$, and $\deg(\tilde J^{d,n}-H_d(X/2))\le d-3$.
- **THM-PAPER-0087-6** (Theorem 2.3, theorem, scope: asymptotic; Sec 2.1, proof Sec 4). For $d\ge4$, $3\le k\le d$, $1<C<2$, and $n+d>\max\{10k^3,M_C\}$: $A_{d,k}(n)=\frac{(-1)^{\lfloor k/2\rfloor}(d-k)!\lfloor k/2\rfloor!}{d!}\times\{1+Z_{n+d}(\lfloor k/2\rfloor)\Delta^2+O_C(k^6(4C)^k\Delta^4)$ if k even; $\lfloor k/2\rfloor(G_3-2)\Delta+O_C(k^4(4C)^k\Delta^3)$ if k odd$\}$, where $Z_t$ is cubic in t with $Z(0)=Z(1)=0$.

### Principal lemmas

- **THM-PAPER-0087-L1** (Lemma 2.4; Sec 2.2). Let $c_{d,n,j}=\sum_{i\le\lfloor j/2\rfloor}\frac{(d-j+2i)!}{i!(d-j)!}A_{d,j-2i}(n)$. If $\sum_{j=3}^{d}2^{-j}\frac{(d-j)!}{(d-1)!}c_{d,n,j}^2<1$ then $J^{d,n}$ is hyperbolic. Proof: invert to $\tilde J=\sum c_{d,n,j}H_{d-j}(X/2)$ and apply Turan's theorem [Turan 1959, Thm III] with $c_{d,n,0}=1$. — *Role:* reduces hyperbolicity to an explicit quadratic inequality
- **THM-PAPER-0087-L2** (Section 2.2 estimates; Sec 2.2). Uses Theorem 2.3 to show the even-index sum is $\ll_C d^{13}(1+\sqrt{1+16C^2})^d\Delta(n+d)^8$ and the odd terms $\ll d^{9}(1+\sqrt{1+16C^2})^d\Delta^6$. With $\Delta\ge1/\sqrt{2C(n+d-1)}$, condition (2.9) holds when $n\ge\alpha_C d^{13/3}(1+\sqrt{1+16C^2})^{d/3}$; with $C=1+10^{-5}$ get $\le ce^{d/2}$ as the final constant. — *Role:* produces the exponential bound in Thm 1.1
- **THM-PAPER-0087-L3** (Cancellation via difference operators (Sec 2.2); Sec 2.2). Since $Z_{n+d}$ is cubic with $Z(0)=Z(1)=0$ and a k-th difference operator $\sigma_{k,x}$ annihilates polynomials of degree $<k$, the main terms of the alternating sums defining $c_{d,n,2\ell}$ cancel for $\ell\ge4$, leaving error $O(\Delta^4)$. — *Role:* key cancellation that gives the Delta^8 saving
- **THM-PAPER-0087-L4** (Theorem 1.2 proof (Sec 5); Sec 5). Via Polya's theory, RH_m iff J^{d,n} hyperbolic for d>=1, n>=m; the finite-height version uses Jensen polynomials uniformly approximating xi^{(n)}(1/2+it) on |t|<=T, following Chasse. — *Role:* finite height version

### Proof architecture

Rewrite the Jensen polynomial in the renormalization J~ with A_{d,0}=1, A_{d,1}=0, A_{d,2}=-d(d-1), so J~ is a perturbation of Hermite H_d(X/2). Expand J~ in Hermite polynomials with coefficients c_{d,n,j}, and use Turan's theorem on real zeros of Hermite sums, which reduces hyperbolicity to a quadratic bound (2.9). Estimate the coefficients using uniform-in-m bounds on the Taylor expansion of log gamma(M-j)/gamma(M) in the uniformizer Delta(M) (Theorem 2.1, proved from GORZ's integral representation and a saddle point analysis in Sec 3) and the coefficient asymptotics (Theorem 2.3, Sec 4), cancelling main terms via difference operators. Theorem 1.2 is a separate argument based on Chasse/Polya.

**Imported results.** Turan 1959, Thm III (real zeros of sums of Hermite polynomials); GORZ 2019 (asymptotic of xi derivatives and Hermite limit); Polya 1927 (RH iff all Jensen polynomials hyperbolic); Csordas-Norfolk-Varga 1986 and Dimitrov-Lucas 2011 (d<=3); Chasse 2013 (d<=2e17), Platt 2011/2017 (zeros to 3.06e10); Borcea-Branden, Obreschkoff

**Techniques.** Turan's theorem on real zeros of Hermite expansions; renormalization by a data-dependent uniformizer Delta(M); uniform-in-m coefficient bounds |G_m|<<(2C)^m; finite-difference cancellation; saddle point analysis in Lambert-type equation M=L(pi e^L+3/4)

## Context and interpretation

**Importance and obstacle overcome.** First effective version of GORZ. Obstacle: obtaining coefficient bounds uniform in both the order m and the argument M, rather than fixed-order asymptotics.

**Relation to prior work.** Direct sequel to GORZ 2019. Compare Chasse (2013, finite height approach), Csordas-Norfolk-Varga, Dimitrov-Lucas. Complemented by O'Sullivan (CAND-01869) and extended in spirit by Wagner (CAND-01962). Farmer is cited for a Berry 'cosine is a universal attractor' interpretation.

**Limitations and open questions.** The threshold is exponential in d (n >= c e^{d/2}). By Cor 1.3 it is complementary to the zero-height approach (d up to ~1e21 for all n). Authors note a converse of Thm 1.2 is very unlikely without hyperbolicity for all n>=m and all d, and that Jensen polynomials are inefficient detectors of violating zeros. Whether the e^{d/2} can be improved to polynomial (conjecturally the truth might be n >> d) is open. The constant c is unspecified (absolute but not computed, hence not a checkable explicit N(d)).

## Research potential

- **Hypotheses that might be weakened.** The choice C=1+10^{-5} and the restriction 1<C<2 in Thm 2.3 should be optimizable to reduce the exponent 1/2. The bound n+d>10k^3 is likely suboptimal.
- **Generalizations.** Replace xi by the completed L-functions of Wagner (CAND-01962) to give effective thresholds there. Apply Lemma 2.4 with the Hermite-combination polynomials P^{d,n} of CAND-01869 to get a better Turan-type bound.
- **Candidate connections.** Lemma 2.4 is a Hermite-basis stability criterion that could be tied to heat flow/de Bruijn-Newman arguments (a polynomial perturbation of Hermite stays real-rooted), and to the xi-geometry/derivative descent programme via Thm 1.2 (RH_m(T) for derivatives).
- **Reusable lemmas.** Theorem 2.1 (uniform Taylor expansion of log gamma(M-j)/gamma(M) in Delta(M)^2) and Lemma 2.4 (Turan-type sufficient criterion).
- **Possible experiments.** Compute the quantity sum_{j>=3}2^{-j}(d-j)!/(d-1)! c_{d,n,j}^2 numerically with high-precision gamma(n) and find the smallest n(d) for which it is <1 for d up to ~100, compare to the true hyperbolicity threshold from Sturm counts to see how much Turan's sufficient condition loses.
- **Risks / barriers.** Even the optimal N(d) leaves the region n<N(d), where RH is genuinely at stake; local zero census (Thm 1.2) uses d<=T^2 and says nothing globally.

## Audit notes (Level 1 reader)

Proof of Thm 2.1 and 2.3 (Sec 3-4) were read only from lossy text, so details of the uniformity argument were not verified. Statement of the limit of G_m(M) as extracted '(2m-1)/(m(m-1))' is probably garbled (m=1 singular); needs check in the PDF. Abstract says 'effective' while constant c is not explicit. Remark in intro: threshold exponent differs from O'Sullivan's cited e^{8d/9} (O'Sullivan cites a version with e^{8d/9} for arXiv v1 of this paper; v3 states e^{d/2}), suggesting version differences.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01931`; harvest queries: kw_RH_any, kw_laguerre_polya_xi, msc_11M06, msc_11M26, arxiv_jensen_poly, arxiv_rh_abs.
- Triage decision: include — Jensen polynomials hyperbolicity for Xi: major recent Polya-criterion result.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

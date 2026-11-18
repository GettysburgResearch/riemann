# PAPER-0121 — Mean-value theorems in the theory of the Riemann Zeta-function.

| Field | Value |
|---|---|
| Authors | Ingham, A. E. |
| Year / stratum | 1927 / S2 |
| Venue | Proc. Lond. Math. Soc. (2) 27, 273-300 (1927). |
| Identifiers | zbMATH [53.0313.01](https://zbmath.org/?q=an:53.0313.01) · DOI [10.1112/plms/s2-27.1.273](https://doi.org/10.1112/plms/s2-27.1.273) |
| MSC | 11M06 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://archive.org/details/london-mathematical-society-proceedings_1927-1928_27 (Proc. London Math. Soc. (2) 27, pp. 273-300; OCR text; text pages only, no page images viewed) |
| Selection | score 4.0333, in-pool citations 135, seed lists 2, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** (A) Sharpen the error term and generalise (to derivatives and complex parameters) the asymptotics of $\int_1^T\zeta^{(\mu)}(a+it)\zeta^{(\nu)}(b-it)dt$ (uniform in a bounded range of Re a, Re b), including Littlewood's refinement for the mean square; (B) prove the asymptotic for the fourth moment on the critical line.

**Historical motivation.** Mean-value theorems for zeta gives information about its growth and zero distribution (Lindelof's hypothesis follows from int|zeta|^{2k} = O(T^{1+eps}) for all k). Hardy and Littlewood (1917, 1921) had int|zeta|^2~2T log T and int|zeta|^4 = O(T log^4 T); Littlewood's note gave refinements without proofs; Ingham supplies proofs, derivatives, and the fourth-moment asymptotic at sigma=1/2.

### Main results

- **THM-PAPER-0121-1** (Theorem B, theorem, scope: asymptotic; Introduction p. 277; proof in sec. 7, pp. 298-300). As $T\to\infty$: $\int_0^T|\zeta(\tfrac12+it)|^4dt=\frac1{2\pi^2}T\log^4T+O(T\log^3T)$. *Conditional on:* Hardy-Littlewood approximate functional equation for $\zeta(s)^2$, eq. (18) (assumed, proof unpublished at time).
- **THM-PAPER-0121-2** (Theorem A, theorem, scope: asymptotic; Introduction, eqs (8)-(13), pp. 275-276; proof secs 1-4). Let $h,h',k$ be fixed constants, $a=\alpha+i\alpha'$, $b=\beta+i\beta'$ complex with $-h\le\alpha\le h$, $|\alpha'|\le h'$, $-h\le\beta\le h$, $|\beta'|\le h'$, $k$ as in (8) and let $\mu,\nu\ge0$ be integers. Define $A(\sigma)=\max(0,\tfrac12-\sigma)$-type quantity ($A(\sigma)=\tfrac12-\sigma$ for $\sigma<\tfrac12$... as printed (10)) and $F(T,c)=\int_1^T f(\tau,c)d\tau$-type main term with $f(\tau,c)=\zeta(c)+\tau^{1-c}\zeta(2-c)$-type expression (10)-(12). Then (i) $\int_k^T\zeta^{(\mu)}(a+it)\zeta^{(\nu)}(b-it)dt$ equals the main term $\partial^{\mu+\nu}$ of $F(T,a+b-1)$ (derivatives in a and b) $+\,O\big(T^{1/2+\dots}(\log T)^{\mu+\nu+2}\big)$ uniformly in the stated ranges ((11)-(13)), with the precise error $O(T^{A(\alpha)+A(\beta)}\dots(\log T)^{\mu+\nu+2})$ as printed; (ii) if $a$ lies outside the intervals $(-\delta,\delta)$ and $(1-\delta,1+\delta)$ then $(\log T)^{\mu+\nu+2}$ may be replaced by $(\log T)^{\mu+\nu+1}$. [The precise exponents of T in the error are not recoverable from the OCR.]
- **THM-PAPER-0121-3** (Theorem A' (sec. 5), corollary, scope: asymptotic; Section 5, p. 295). $\int_0^T|\zeta(\tfrac12+it)|^2dt=T\log T-(1+\log2\pi-2C)T+O(T^{1/2}\log T)$, with $C$ Euler's constant (the error term $O(T^{1/2}\log T)$ as printed 'O(T log T)^{1/2}'; replaces Littlewood's $O(T^{1/2+\epsilon})$); (this also corrects a slip in Littlewood's coefficient $1+\log2\pi$).
- **THM-PAPER-0121-4** (Theorem A'' (sec. 5), corollary, scope: asymptotic; Section 5, pp. 295-296). For $\nu\ge0$, $\int_0^T|\zeta^{(\nu)}(\tfrac12+it)|^2dt=\frac{T}{2\nu+1}\log^{2\nu+1}\!T\,+\,\sum$ lower-order terms $T\log^{2\nu+1-n}T$ with explicit coefficients given through $c_n$ defined by $\zeta$'s Laurent expansion $\frac{y}{e^y-1}$-type generating function ($c_0=1$, $c_1=C-1$) $+O[T^{1/2}(\log T)^{2\nu+2}]$.
- **THM-PAPER-0121-5** (Introduction eq. (2), classical result (imported), scope: asymptotic; Introduction p. 273). For fixed $\alpha>-1/2$, $\beta>-1/2$, $\alpha+\beta>1$: $\int_1^T\zeta^{(\mu)}(\alpha+ti)\zeta^{(\nu)}(\beta-ti)dt\sim\ldots T$ (Hadamard, Landau, Schnee), the case $\mu=\nu=0$, $\alpha=\beta=\sigma>1/2$ giving $\int|\zeta(\sigma+it)|^2\sim\zeta(2\sigma)T$.

### Key definitions

- $\zeta^{(\mu)}$: $\mu$-th derivative of zeta
- $d(n)$: divisor function
- $\chi(s)$ with $\zeta(s)=\chi(s)\zeta(1-s)$
- Hankel-type contour $C(\theta)$ enclosing the negative real axis
- Hardy-Littlewood approximate functional equation for zeta^2 (eq. 18)

### Principal lemmas

- **THM-PAPER-0121-L1** (Approximate functional equation (18) for $\zeta(s)^2$; Introduction, eq. (18), p. 277). As $t\to\infty$: $\zeta^2(\tfrac12+it)=\sum_{n\le t/2\pi}d(n)n^{-1/2-it}+\big(\tfrac{t}{2\pi}\big)^{-2it}\!\!\cdots\sum d(n)n^{-1/2+it}+O(\log t)$, i.e. $\zeta^2=S+\bar{\bar{S}}$-type main sum $\sum_{n\le t/2\pi}d(n)n^{-1/2-it}$ plus a twisted conjugate sum $+O(\log t)$ (communicated to Ingham by Hardy and Littlewood; proof not published at the time). — *Role:* Replaces the usual AFE in Theorem B; the main term from diagonal $m=n$ gives $(1/4)T\log^4T\cdot$... resulting in $\frac{1}{2\pi^2}T\log^4T$.
- **THM-PAPER-0121-L2** (Lemma B11 (Ramanujan/Landau); Section 6, p. 296; Landau Hilfssatz 10, Hardy-Littlewood Lemma 3.51 cited). As $x\to\infty$: $\sum_{n\le x}\frac{d(n)^2}{n}=\frac1{4\pi^2}\log^4x+O(\log^3x)$ (via Ramanujan's formula $\sum_{n\le x}d(n)^2=\frac1{\pi^2}x\log^3x+O(x\log^2x)$). — *Role:* Gives the diagonal term of the mean fourth power: $\frac1{2\pi^2}T\log^4T$.
- **THM-PAPER-0121-L3** (Lemmas B3, B4 (cited in sec. 7); Section 7, eqs (42)-(44), pp. 298-299). Landau/Hardy-Littlewood-type bounds for the off-diagonal sums $\sum_{m\ne n}\frac{d(m)d(n)}{\sqrt{mn}\,|\log(m/n)|}=O(T\log^3T)$ [with the cutoff $m,n\le T'/2\pi$] and its oscillatory counterpart $O(\sqrt T\log^3T)$. — *Role:* Control of the non-diagonal terms in $\int|S|^2dt$.
- **THM-PAPER-0121-L4** (Section 1, representation (19)-(20); Section 1, pp. 277-279). For complex $s$: $\zeta(s)=\frac{\Gamma(1-s)}{2\pi i}\cdot(\text{Hankel contour integral }\int_{C(0)}\frac{z^{-s}}{e^{-z}-1}dz)$-type variant of Riemann's contour formula; splitting with parameters $x,y$ gives $\zeta(s)=\sum_{n\le x}n^{-s}+\chi(s)\sum_{n\le y}n^{s-1}+\Omega(x,y,s)$ and $\chi(s)\chi(1-s)=1$, $\Omega(x,y,s)=\chi(s)\Omega(y,x,1-s)$ (eq. (20)-(22)). — *Role:* Starting point of the proof of Theorem A: a variant of the approximate functional equation with an explicit remainder Omega treated directly (not merely by inequality), which is what eliminates Littlewood's extra error term.

### Proof architecture

Part A (secs 1-5): write zeta(a+ti)zeta(b-ti) via (20) with x=y=sqrt(t/2pi) as U1+U2+U3 and V1+V2+V3 (Dirichlet polynomials of length sqrt(t/2 pi) and error Omega terms), integrate the 9 products; Lemmas A1-A9 control oscillatory integrals with the phase t log t (second mean-value theorem, Lemma A2) and the Omega terms are evaluated directly rather than bounded via an inequality (this is what removes Littlewood's O(HT^{-1/2+eps}) term); the case mu,nu>0 follows from differentiating in complex a,b (reason for complex parameters). Part B (secs 6-7): write zeta^2(1/2+it)=S+bar-type S + rho with |rho|=O(log t) from the Hardy-Littlewood AFE for zeta^2; then |zeta|^4 <= 2|S|^2+2|bar S|^2 ... (41); main term: diagonal m=n, sum d(n)^2/n gives (1/4pi^2)log^4; off-diagonal sums bounded using Lemma B3,B4; the cross term |S|^2 vs twisted term via Schwarz.

Dependency edges: CAND-00077 → CAND-00219 (extends mean-value method; uses AFE ideas); CAND-00077 → CAND-00076 (refines Theorem 2.41); CAND-00077 Theorem B → Hardy-Littlewood AFE for zeta^2 (depends on (unpublished at the time))

**Imported results.** Hardy-Littlewood: AFE for zeta^2 (eq. (18); communicated privately, unpublished); Ramanujan's formula $\sum_{n\le x}d(n)^2=\pi^{-2}x\log^3x+O(x\log^2x)$ (Messenger of Math. 1916); Hardy-Littlewood Lemma 3.51 / Landau Hilfssatz 10 (off-diagonal estimates); Littlewood's mean-square refinement (eq. (6), proof unpublished manuscript communicated to Ingham); Hardy-Littlewood: int|zeta|^2~2T log T and int|zeta|^4=O(T log^4 T)

**Techniques.** Hankel/Riemann contour formula with complex parameters; approximate functional equation for zeta and (assumed) for zeta^2; second mean-value theorem for oscillatory integrals (Lemma A2); diagonal/off-diagonal decomposition of Dirichlet polynomial mean squares; Ramanujan's asymptotics for sum d(n)^2; partial summation; differentiation in complex parameters to obtain derivatives

## Context and interpretation

**Importance and obstacle overcome.** First asymptotic for the fourth power mean of zeta on the critical line (T log^4 T/(2 pi^2)), filling in the missing value sigma=1/2 (the earlier Hardy-Littlewood result was only an upper bound O(T log^4 T)); also gives the sharp second moment with error O(T^{1/2} log T) (previously O(T^{1/2+eps}) by Littlewood) with a uniform treatment of derivatives. The obstacle was that the ordinary AFE is insufficient for zeta^2's mean square, so a degree-2 AFE for zeta^2 is needed and the Omega remainder must be integrated exactly rather than majorised.

**Relation to prior work.** Extends Hadamard-Landau-Schnee (fixed sigma), Hardy-Littlewood 1917 (CAND-00076, Thm 2.41) and 1921-22 (CAND-00219, Theorems D, E) and Littlewood's C. R./Proc. note (Littlewood 1, no proofs, error O(T^{1/2+eps})); Carlson later gave a Dirichlet-series proof of the fixed-sigma fourth moment; Titchmarsh found Fourier-transform proofs of similar formulas.

**Limitations and open questions.** Theorem B's error O(T log^3 T) is only a factor log T smaller than the main term; the proof relies on an approximate functional equation for zeta^2 that Ingham explicitly says was 'communicated' and 'no proof has yet been published'. The paper treats Theorem B only for the line sigma=1/2 (fixed sigma already known). No lower-order terms for the fourth moment are given; Ingham notes the true second-order terms are not obtained. Theorem A's uniformity is limited to bounded real parts and bounded imaginary parts of a,b.

**Ideas in remarks/appendices/abandoned paths.** Footnote p. 278: starting from the contour formula (20) one can give a proof of the approximate functional equation formally simpler than Hardy-Littlewood's, 'identical in principle'. Section 5 corrects a slip in Littlewood's coefficient of T (his -(1+log 2 pi) should be -(1+log 2pi-2C)). Remark that Carlson (Dirichlet-series proof of the fixed-sigma fourth moment) and Titchmarsh (Fourier transform method) have alternative proofs, suggesting Theorem B might admit an approach not using AFE for zeta^2.

## Research potential

- **Hypotheses that might be weakened.** Theorem B depends on the (then unpublished) AFE for zeta^2 with O(log t) error; to weaken, find which lower accuracy (e.g. O(t^{epsilon}) error) is sufficient: with error O(t^{eps}) the argument via Schwarz in (45) would give only T^{1+eps}. Quantifying the necessary accuracy of the AFE for zeta^2 (error O(log t) vs O(t^{delta})) is a concrete question.
- **Generalizations.** Mean fourth power for Dirichlet L-functions (Heath-Brown 1981 gets polynomial in log with all lower-order terms) and for the moments of derivatives zeta^{(mu)}zeta^{(nu)} at sigma=1/2 (Theorem A with higher moments); extension to twisted fourth moments with mollifiers.
- **Candidate connections.** Sixth and higher moments via random matrix conjecture (Keating-Snaith: int|zeta|^{2k} ~ c_k T log^{k^2} T with a_k=1/(2 pi^2) for k=2); the diagonal/off-diagonal split here is the prototype for the recipe/ratios conjectures of Conrey-Farmer-Keating-Rubinstein-Snaith; Atkinson's and Motohashi's spectral treatment of the error E_2(T).
- **Reusable lemmas.** Lemma A2 (oscillatory integral bound), Theorem A as a uniform asymptotic with derivatives (usable for mean values of zeta'/zeta type quantities in mollifier computations), Lemma B11.
- **Possible experiments.** Numerically evaluate int_0^T|zeta(1/2+it)|^4dt for T up to 1e5-1e6 with mpmath/arb and fit to T P_4(log T) with P_4 leading 1/(2pi^2); check the size of the error term against Ingham's O(T log^3 T) (true error is O(T^{2/3+eps}) after later work); test Theorem A'' coefficients for nu=1.
- **Risks / barriers.** Reliance on an unpublished AFE; the diagonal method cannot see secondary main terms beyond the log^3 T order without the off-diagonal (shifted divisor) contributions, as shown later by Heath-Brown 1979 and the full lower-order terms.

## Audit notes (Level 1 reader)

Theorem A statement: the OCR of eqs (10)-(13) is garbled (function A(sigma), the exact form of f(tau,c) and the exact power of T in the error term) so my restatement is a faithful paraphrase only for the structure; verify exponents against the page image before use. Theorem A' error term appears printed O(T log T)^{1/2} (i.e. O(T^{1/2} log T)). Point to flag: Theorem B is proved modulo eq. (18), an AFE for zeta^2 attributed to Hardy-Littlewood with no published proof at the time (Ingham states this explicitly, p. 277 and footnote); this is a disclosed dependency, not an error.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00077`; harvest queries: kw_moments_zeta, msc_11M06.
- Triage decision: include — Ingham's fourth moment of zeta.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

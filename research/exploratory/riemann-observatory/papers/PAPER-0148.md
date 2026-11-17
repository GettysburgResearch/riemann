# PAPER-0148 — The approximate functional equation in the theory of the zeta-function, with applications to the divisor-problems of Dirichlet and Piltz.

| Field | Value |
|---|---|
| Authors | Hardy, G. H.; Littlewood, J. E. |
| Year / stratum | 1922 / S2 |
| Venue | Lond. M. S. Proc. (2) 21, 39-74 (1922). |
| Identifiers | zbMATH [48.1163.01](https://zbmath.org/?q=an:48.1163.01) · DOI [10.1112/plms/s2-21.1.39](https://doi.org/10.1112/plms/s2-21.1.39) |
| MSC |  |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://archive.org/details/london-mathematical-society-proceedings_1922-1923_21 (Proc. London Math. Soc. (2) 21, pp. 39-74; PDF page images viewed for statements of Theorems A, C, D, E, F) |
| Selection | score 2.2238, in-pool citations 25, seed lists 1, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Prove the approximate functional equation for zeta(s) uniformly in the critical strip with the optimal error term (no spurious log|t|), and apply it to (a) the mean fourth power of zeta in the strip and (b) the order of the error term in the Piltz divisor problem.

**Historical motivation.** The 1921 Math. Zeitschrift memoir (Hardy-Littlewood, 'The zeros of Riemann's Zeta-function on the critical line', Math. Z. 10) proved a weaker approximate functional equation (with log|t| factor, fixed sigma); the authors wanted the perfect form for the Lindelof programme (mean values) and for divisor problems of Dirichlet and Piltz.

### Main results

- **THM-PAPER-0148-1** (Theorem A (1.11)-(1.17), theorem, scope: asymptotic; Section 1.1, pp. 39-40 (proof in section 2)). Let $H,K>0$ be constants, $s=\sigma+it$ with $-H\le\sigma\le H$, and $x>K$, $y>K$, $2\pi xy=|t|$. (i) $\zeta(s)=\sum_{n<x}n^{-s}+\chi(s)\sum_{n<y}n^{s-1}+R$ with $\chi(s)=2(2\pi)^{s-1}\sin(\tfrac12 s\pi)\Gamma(1-s)$ and $R=O(x^{-\sigma})+O(y^{\sigma-1}|t|^{1/2-\sigma})$. (ii) If in addition $x\ge y$, $R=O\big(x^{1-\sigma}/(|t|^{1/2}+x\,\mathfrak S(y))\big)$ where $\mathfrak S(y)$ is the distance from $y$ to the nearest integer. (iii) If $x\le y$, $R=O\big(|t|^{1/2-\sigma}y^{\sigma}/(|t|^{1/2}+y\,\mathfrak S(x))\big)$. The O-constants depend only on $H,K$.
- **THM-PAPER-0148-2** (Theorem C (2.941)-(2.943), corollary, scope: asymptotic; Section 2.94, p. 58). Uniformly for $0\le\sigma\le H$: $\zeta(s)=\sum_{n<x}n^{-s}+\chi'\sum_{n<y}n^{s-1}+O(x^{-\sigma})+O(|t|^{1/2-\sigma}y^{\sigma-1})$ with $\chi'=(|t|/2\pi e)^{-it}(|t|/2\pi)^{1/2-\sigma}e^{\frac14\pi i\,\mathrm{sgn}\,t}$. In particular for $\sigma=1/2$, $x=y=\sqrt{|t|/2\pi}$: $\zeta(\tfrac12+it)=\sum_{n<x}n^{-1/2-it}+(|t|/2\pi e)^{-it}e^{\frac14\pi i\,\mathrm{sgn}\,t}\sum_{n<x}n^{-1/2+it}+O(|t|^{-1/4})$; hence $\zeta(\tfrac12+it)=O(t^{1/4})$.
- **THM-PAPER-0148-3** (Theorem D (3.11)-(3.13), theorem, scope: asymptotic; Section 3.1, p. 59; proof 3.31-3.5). (i) For $1/2<\sigma<1$, as $T\to\infty$: $\frac1{2T}\int_{-T}^{T}|\zeta(\sigma+it)|^4dt\sim\sum_{n\ge1}\frac{[d(n)]^2}{n^{2\sigma}}=\frac{[\zeta(2\sigma)]^4}{\zeta(4\sigma)}$. (ii) $\int_{-T}^{T}|\zeta(\tfrac12+it)|^4dt=O[T(\log T)^4]$. (iii) $\int_{2}^{T}|\zeta(\sigma+it)|^4dt=O[T(\log T)^4]$ uniformly for $1/2\le\sigma\le2$, $T>2$.
- **THM-PAPER-0148-4** (Theorem E (3.14), theorem, scope: asymptotic; Section 3.1, p. 59-61 (proof of the case $\int|Z|^2\sim T\log T$)). $\int_{-T}^{T}|\zeta(\tfrac12+it)|^2dt\sim2T\log T$ as $T\to\infty$ (already due to Hardy-Littlewood 1917, Acta Math. 41, pp. 151-156; new short proof from Theorem C with $x=t/(2\pi\sqrt{\log t})$, $y=\sqrt{\log t}$).
- **THM-PAPER-0148-5** ((1.21), Theorem D corollary, corollary, scope: asymptotic; Section 1.2, p. 41, eq. (1.21)-(1.22)). $\int_{-T}^{T}|\zeta(\tfrac12+it)|^4dt=O(T\log^4T)$, described as 'a further stage in the direction of Lindelof's hypothesis' $\zeta(\tfrac12+it)=O(|t|^\epsilon)$ (which would follow from $\int|\zeta|^{2p}=O(T^{1+\epsilon})$ for every p).
- **THM-PAPER-0148-6** (Theorem F (4.41)-(4.42), theorem, scope: asymptotic; Section 4.4, p. 70). Let $d_k(n)$ be the number of representations of $n$ as an ordered product of $k$ factors and $\Delta_k(x)=\sum_{n\le x}d_k(n)-x P_{k-1}(\log x)$ the Piltz error term. For every integer $k\ge4$ and $\epsilon>0$: $\Delta_k(x)=O(x^{\frac{k-2}{k}+\epsilon})$, i.e. $\alpha_k\le\frac{k-2}{k}$, where $\alpha_k$ is the infimum of exponents $\theta$ with $\Delta_k(x)=O(x^{\theta+\epsilon})$.
- **THM-PAPER-0148-7** ((4.22)-(4.24), table p. 69, conditional / remark, scope: asymptotic; Section 4.1-4.2, pp. 68-69). The fourth-power bound (4.21) $\int_{-T}^T|\zeta(\tfrac12+it)|^4dt=O(T^{1+\epsilon})$ yields $\alpha_k\le (k-2)/k$ for $k>3$ [(4.22)]. A further improvement $\alpha_k\le (k-1)/(k+2)$ for $k>3$ [(4.23)] would follow from the (then unpublished, 'lies very deep') estimate (4.24) $\zeta(\tfrac12+it)=O(t^{1/6+\epsilon})$. Lower bounds: Hardy: $\alpha_k\ge(k-1)/(2k)$ (4.19), and previously $\alpha_k\le (k-1)/(k+1)$ (Landau, 4.16); on Lindelof's hypothesis $\alpha_k\le 1/2$ (4.17). *Conditional on:* zeta(1/2+it)=O(t^{1/6+eps}).

### Key definitions

- $\chi(s)=2(2\pi)^{s-1}\sin(\tfrac12 s\pi)\Gamma(1-s)$ with $\zeta(s)=\chi(s)\zeta(1-s)$
- $\mathfrak S(y)$: distance from $y$ to nearest integer
- $\Delta_k(x)=\sum_{n\le x}d_k(n)-x P_{k-1}(\log x)$ (Piltz error)
- $\alpha_k=\inf\{\theta:\Delta_k(x)=O(x^{\theta+\epsilon})\ \forall\epsilon>0\}$
- $d_k(n)$: number of ordered factorizations of n into k factors

### Principal lemmas

- **THM-PAPER-0148-L1** (Section 2.3-2.7 (proof of Theorem A, contour representation); Sections 2.3-2.42, pp. 44-47). For $x\equiv 1/2 \pmod 1$, $\sigma>1$: $\zeta(s)-\sum_{n<x}n^{-s}=\frac{x^{1-s}}{s-1}-\frac12 x^{-s}-\dots$ is written as contour integrals $\frac1{2i}\int z^{-s}\cot\pi z\,dz$ along rays $L_1,L_2$ at angles $\pm\pi/4$ from $x$ to infinity; splitting $\cot\pi z\mp i$ into $2\sum e^{\pm 2\pi i\nu z}$ yields $J_1,J_2$ with $\zeta(s)-\sum_{n<x}n^{-s}=I_1+I_2+O(x^{-\sigma})$. — *Role:* Starting point: Riemann-Siegel-style contour decomposition, valid for all s via analytic continuation.
- **THM-PAPER-0148-L2** (Section 2.5-2.6 (saddle-point for $\int z^{-s}e^{2\pi i\nu z}dz$); Sections 2.5-2.7, pp. 47-52). Integrals $k_{\nu,1},k_{\nu,2}$ along $[0,\infty)$ deformed to the imaginary axis segment $L_3$ and the line from $-i\pi x$... $L_4$ (here denoted by authors) produce the main terms $\chi(s)\sum_{\nu\le y_2}\nu^{s-1}$ via $\int_{C}e^{\mp\dots}z^{-s}dz=(2\nu\pi)^{s-1}e^{\dots}\Gamma(1-s)$ and error terms $O(x^{-\sigma})$, $O(y^{\sigma-1}|t|^{1/2-\sigma})$. — *Role:* Gives part (i); the sharper parts (ii),(iii) analyse the nearly resonant term $\nu=y$ (integers near y) giving $\mathfrak S(y)$.
- **THM-PAPER-0148-L3** (Lemma alpha...eta (section 3.2), esp. Lemma gamma-delta; Sections 3.2-3.3, pp. 61-64). With $D(n,\sigma)=\sum_{\nu\le n}d(\nu)\nu^{-\sigma}$: $D=O(1)$ ($\sigma>1$), $O(\log^2n)$ ($\sigma=1$), $O(n^{1-\sigma}\log n)$ ($1/2<\sigma<1$), and uniformly $O(n^{\mu}\log n)$ with $\mu=\max(1-\sigma,0)$; Lemma $\epsilon$: $\sum_{\nu}d(\nu)d(\nu+r)=O(n\log^3n)$ uniformly for $0\le r<Kn$; Lemma $\zeta$ (Ramanujan): $\sum d(n)^2n^{-s}=\zeta(s)^4/\zeta(2s)$ for $\sigma>1$; Lemma $\eta$: $\sum_{\nu\le n}d(\nu)^2=O(n\log^3 n)$ (Ramanujan: $\sim\frac{1}{\pi^2}n\log^3n$). — *Role:* Divisor-sum estimates feeding the diagonal and off-diagonal bounds in the proof of Theorem D.
- **THM-PAPER-0148-L4** (Lemmas theta, iota (sec. 4.3); Section 4.3, p. 70). Lemma theta: for fixed $\delta,\epsilon\in(0,1)$ there is $A(\epsilon)$ such that for each $\omega'>1$ there is $\omega\in[\omega',2\omega']$ with $\int_{1/2}^{1+\delta}|\zeta(\sigma+i\omega)|^4d\sigma<A\omega^{\epsilon}$ (from (3.13)). Lemma iota: Landau/Perron-type truncated formula $A(x)=\sum_{n<x}a_n=\frac1{2\pi i}\int_{1+\delta-i\omega}^{1+\delta+i\omega}f(s)\frac{x^s}{s}ds+O(x^{1+\delta}/\omega)$ for $a_n=O(n^\epsilon)$, $x=\sqrt{m(m+1)}$. — *Role:* Used to prove Theorem F by shifting the line of integration to Re s=1/2 and applying $\int|\zeta|^4$ bound to $f=\zeta^k$.

### Proof architecture

Section 2: reduce to x = 1/2 mod 1, y non-integer; write zeta(s)-sum_{n<x} n^{-s} via the cot z contour integral; deform contours; extract the main term chi(s) sum n^{s-1} (via Gamma/Hankel) and bound the remainder; treat the near-resonant term to get the S(y) factor (parts (ii),(iii)), and use the functional equation to swap x and y (the restriction x>=y is irrelevant in (i)). Section 3: insert Theorem C with x~t/(2 pi sqrt(log t)) (Theorem E) or x=sqrt(t/2pi) (Theorem D) so that zeta is a Dirichlet polynomial of length ~sqrt(t); mean value of |sum a_n n^{-s}|^2-type products reduces to divisor correlation sums D(n,sigma), sum d(v)d(v+r) (Lemma epsilon), with diagonal giving Ramanujan's sum zeta(2sigma)^4/zeta(4sigma). Section 4: apply Theorem D in the form int |zeta(1/2+it)|^4 = O(T^{1+eps}) with Perron's formula for zeta^k to get Delta_k(x)=O(x^{(k-2)/k+eps}).

Dependency edges: CAND-00219 → CAND-00076 (re-proves Theorem 2.41 via approximate functional equation); CAND-00077 → CAND-00219 (fourth moment sharpened to asymptotic by Ingham (uses zeta^2 AFE)); Theorem F → Theorem D(iii) (uses int_{1/2}^{1+delta}|zeta|^4 bound (Lemma theta))

**Imported results.** Ramanujan, Messenger of Math. 45 (1916): sum d(n)^2 n^{-s}=zeta(s)^4/zeta(2s) (proofs by B. M. Wilson); Hardy-Littlewood, Acta Math. 41 (1917) for int|zeta|^2~2T log T; Landau Handbuch (Perron formula, formula (1) p.826, Hilfssatz 8 p.841); Piltz (1881), Landau for alpha_k<=(k-1)/(k+1); Hardy 1915 and Landau 1915 for alpha_k>=(k-1)/(2k)

**Techniques.** contour integral representation via cot(pi z) and Hankel contours; saddle-point/steepest descent estimates along rays; generalised (Hadamard/Cauchy) integrals; mean values of Dirichlet polynomials via divisor sums; Ramanujan's formula sum d(n)^2 n^{-s}=zeta(s)^4/zeta(2s); Perron-type truncated formula and shifting of line for Piltz divisor problem

## Context and interpretation

**Importance and obstacle overcome.** Gives the approximate functional equation in its sharpest uniform form (removing the superfluous log|t| of the 1921 Math. Z. version and holding uniformly in sigma) by a new contour argument, and uses it to prove the fourth-moment bound and the Piltz-problem exponent alpha_k<=(k-2)/k, the first nontrivial gain from mean-value theory of zeta over Landau's (k-1)/(k+1); the method (zeta as a short Dirichlet polynomial + divisor correlation) is the template for later moment computations (Ingham, Titchmarsh) toward Lindelof.

**Relation to prior work.** Improves Hardy-Littlewood, Math. Z. 10 (1921) and gives simpler proof of the mean-square (Acta Math. 41, 1917). Upgrades Landau's alpha_k<=(k-1)/(k+1). Followed by Ingham (1927) who adds asymptotic fourth moment (CAND-00077), by Titchmarsh's Fourier-transform approach, and by Weyl/Hardy-Littlewood's zeta(1/2+it)=O(t^{1/6+eps}).

**Limitations and open questions.** Error terms uniform only for |sigma|<=H with fixed H. The fourth-moment result at sigma=1/2 is only O(T log^4 T), not an asymptotic (Ingham 1927 later gives T log^4 T/(2 pi^2), CAND-00077); asymptotic (i) is limited to 1/2<sigma<1. The improvement (4.23) is conditional on a then-unproved t^{1/6} bound; Lindelof is only approached. The authors note the strict extension outside the critical strip is of 'secondary importance'.

**Ideas in remarks/appendices/abandoned paths.** Remark 2.8: for x of size |t| (y bounded) one recovers Lemma 2 of Hardy-Littlewood 1917, showing that the old 'short sum' approximation is a degenerate case of the approximate functional equation; the table on p. 69 comparing the four candidate bounds (k-1)/(2k), (k-1)/(k+2), (k-2)/k, (k-1)/(k+1) is a compact map of what mean-value input buys. Section 2.91 gives an explicit form of the S(y) contribution (integrals along L1,L2 of z^{-s}e^{2 pi i nu z}) that 'may possibly find applications'.

## Research potential

- **Hypotheses that might be weakened.** In Theorem A the constants depend on H and K; the dependence on the proximity of y to an integer S(y) in (ii)/(iii) could be quantified in a modern Riemann-Siegel/Hardy-Littlewood framework to give uniform bounds for short-interval mean values. Theorem D(i) needs sigma>1/2 fixed; investigating uniformity as sigma->1/2+ (the main term blows up like (2sigma-1)^{-4}) would show how the transition to T log^4 T/(2 pi^2) occurs.
- **Generalizations.** Approximate functional equation for degree-2 L-functions / Dirichlet L-functions (Hardy-Littlewood treated zeta; the contour method generalises to Hurwitz zeta and to L(s,chi)); extension to zeta^2 (Hardy-Littlewood's unpublished approximate functional equation for zeta(s)^2 used in Ingham 1927, CAND-00077).
- **Candidate connections.** Divisor correlation Lemma epsilon (sum d(v)d(v+r)) is the origin of the shifted-divisor-problem approach to fourth moments (Estermann, Heath-Brown, Motohashi); S(y) factor connects to resonance phenomena near integers in Riemann-Siegel expansions; alpha_k bounds link to Lindelof-on-average.
- **Reusable lemmas.** Theorem A(ii),(iii) with the S(y) denominator (a clean, uniform short-sum approximation); Lemma epsilon on the divisor correlation sum.
- **Possible experiments.** Check numerically (mpmath) the sharpness of the error term in Theorem A(ii) as y approaches an integer, e.g. t chosen so that y=sqrt(t/2pi) is near an integer, comparing |R| with x^{1-sigma}/(|t|^{1/2}+x S(y)). Compute (1/2T)int_{-T}^T|zeta(sigma+it)|^4 for sigma=0.6,0.75 versus zeta(2sigma)^4/zeta(4sigma).
- **Risks / barriers.** Getting beyond (k-2)/k for Delta_k needs sub-convexity for zeta(1/2+it) (Weyl/Hardy-Littlewood t^{1/6}) or higher moments; the divisor-correlation method for fourth moments saturates at T log^4 T without extra input (Atkinson, Motohashi).

## Audit notes (Level 1 reader)

none noticed in inspected portion for the mathematical statements viewed as page images (Theorem A pp. 39-40, Theorem C p. 58, Theorem D p. 59, Theorem F p. 70). The reading of the unpublished claim (4.24) zeta(1/2+it)=O(t^{1/6+eps}) as 'which lies very deep, of which no proof has yet been published' is a historical note (Weyl 1921 independently). OCR quality is moderate; page-level misreadings in the middle of Section 2 (contour signs, factors) were not independently verified. Date discrepancy: paper 'Read March 10th, 1921', volume dated 1922-23 (Proc. LMS (2) 21 (1923) per the zbMATH record year 1922).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00219`; harvest queries: citation_expansion.
- Triage decision: include — Approximate functional equation: core tool for moments, zeros on line, Riemann-Siegel.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

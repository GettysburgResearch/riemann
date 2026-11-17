# PAPER-0146 — Sur les zéros de la fonction \(zeta (s)\) de \textit{Riemann}.

| Field | Value |
|---|---|
| Authors | Hardy, G. H. |
| Year / stratum | 1914 / S2 |
| Venue | C. R. 158, 1012-1014 (1914). |
| Identifiers | zbMATH [45.0716.04](https://zbmath.org/?q=an:45.0716.04) |
| MSC |  |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://archive.org/details/ComptesRendusAcademieDesSciences0158 (page images of C. R. 158, pp. 1012-1014, read directly; OCR cross-checked) |
| Selection | score 2.3857, in-pool citations 34, seed lists 2, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Does the Riemann zeta function have zeros on the critical line Re s = 1/2 at all, and in fact infinitely many? (Bohr-Landau had just shown, Comptes Rendus 12 Jan 1914, that almost all zeros lie in 1/2-delta<sigma<1/2+delta; Hardy proves infinitely many lie exactly on the line.)

**Historical motivation.** Riemann (1859) asserted that most zeros are real zeros of Xi without proof; Bohr and Landau (Jan 1914) proved concentration near the line; Hardy answered (communicated to the London Math. Society 12 March 1914, C. R. note 6 April 1914) the basic existence question. Landau and Hardy-Littlewood quickly simplified and quantified the argument.

### Main results

- **THM-PAPER-0146-1** (Theorem (unnumbered, p. 1012 and conclusion p. 1014), theorem, scope: asymptotic; p. 1012 (statement), pp. 1013-1014 (proof)). The function $\zeta(s)$ has infinitely many zeros on the line $\sigma=1/2$; equivalently Riemann's $\Xi(t)=\xi(1/2+it)$ (real for real $t$) has infinitely many real zeros. Proof by contradiction: if $\Xi(2t)$ kept a constant sign for $t>T>1$ one gets an impossible inequality.
- **THM-PAPER-0146-2** (formula (1), formula, scope: global; p. 1012, eq. (1)). From the Cahen-Mellin integral $e^{-y}=\frac1{2\pi i}\int_{k-i\infty}^{k+i\infty}\Gamma(u)y^{-u}du$ ($\Re y>0,k>0$) one gets $1+\frac1{\pi i}\int_{k-i\infty}^{k+i\infty}\Gamma(u)y^{-u}\zeta(2u)du=1+2\sum_{n\ge1}e^{-n^2y}$ ($k>1/2$); moving to $\Re u=1/4$ and using $\Xi$: $1+\sqrt{\pi/y}-\frac2\pi\int_{-\infty}^{\infty}(\pi/y)^{1/4+ti}\frac{\Xi(2t)}{1/4+4t^2}dt=1+2\sum_{n\ge1}e^{-n^2y}$.
- **THM-PAPER-0146-3** (formulas (2),(3), formula, scope: global; pp. 1012-1013, (2),(3)). With $y=\pi e^{i\alpha}$, $|\alpha|<\pi/2$, $q=e^{i\pi\tau}=e^{-y}$ and $F(q)=1+2\sum q^{n^2}=\vartheta_3(0,\tau)$: $\int_0^\infty\frac{(e^{\alpha t}+e^{-\alpha t})\Xi(2t)}{1/4+4t^2}dt=\pi\cos\tfrac14\alpha-\tfrac12\pi e^{\frac14 i\alpha}F(q)$, and differentiating $2p$ times in $\alpha$: $\int_0^\infty\frac{(e^{\alpha t}+e^{-\alpha t})t^{2p}\Xi(2t)}{1/4+4t^2}dt=\frac{(-1)^p\pi}{4^{2p}}\cos\tfrac14\alpha-\big(\tfrac{d}{d\alpha}\big)^{2p}[\tfrac12\pi e^{\frac14 i\alpha}F(q)]$.
- **THM-PAPER-0146-4** (Lemma in section 2 (unnumbered), lemma, scope: asymptotic; p. 1013, section 2). As $\alpha\to\pi/2$ (so $q\to-1$ along a path tangent to the ray $\arg q=\pi$), every $(d/dy)^{2p}F(q)=2\sum n^{4p}q^{n^2}\to0$, for each $p$; justified by Bohr-M. Riesz summability of the Dirichlet series $1^{-s}+0+0-4^{-s}+\dots$ representing $(1-2^{1-2s})\zeta(2s)$, which is entire of finite order in half-planes and has value $(1-2^{1-2s})\zeta(2s)=0$ at negative integers $s$ (hence Cesaro-summable to 0).
- **THM-PAPER-0146-5** (formula (4), consequence, scope: asymptotic; pp. 1013-1014, (4)). Hence as $\alpha\to\pi/2$: $\int_0^\infty\frac{(e^{\pi t/2}+e^{-\pi t/2})t^{2p}\Xi(2t)}{1/4+4t^2}dt=\frac{(-1)^p\pi}{4^{2p}}\cos\frac{\pi}{8}$ (if $\Xi(2t)$ has constant sign for $t>T$, the tail $\int_T^\infty$ has that sign).
- **THM-PAPER-0146-6** (inequalities (5),(6), contradiction step, scope: asymptotic; p. 1014, (5),(6)). For odd $p$: $\int_T^\infty<-\int_0^T<KT^{2p}$ with $K$ independent of $p$, while if $\Xi(2t)>\delta>0$ on $(2T,2T+1)$ then $\int_T^\infty>\delta K_1(2T)^{2p}$; so $\delta K_1 2^{2p}<K$ for all odd $p$, absurd for large $p$.

### Key definitions

- $\Xi(t)=\xi(1/2+it)$ with $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ (real for real $t$)
- $F(q)=1+2\sum_{n\ge1}q^{n^2}=\vartheta_3(0,\tau)$, $q=e^{i\pi\tau}$
- $y=\pi e^{i\alpha}$, $q=e^{-y}$

### Principal lemmas

- **THM-PAPER-0146-L1** (Cahen-Mellin integral (cited from Cahen, Ann. ENS 1894, p.99; Mellin, Acta Soc. Fenn. 20 (1895)); p. 1012). $e^{-y}=\frac1{2\pi i}\int_{k-i\infty}^{k+i\infty}\Gamma(u)y^{-u}du$ for $\Re y>0$, $k>0$. — *Role:* Converts the theta series into an integral of Xi against a kernel, linking zeros of Xi to theta-function behaviour.
- **THM-PAPER-0146-L2** (Bohr-Riesz summability lemma (cited); p. 1013). A Dirichlet series with an entire continuation of finite order in half-planes is summable by Cesaro means of sufficiently high order everywhere, with the value given by the continuation. — *Role:* Gives that all derivatives $(d/dy)^{2p}F(q)\to0$ as $q\to-1$, so the right side of (3) tends to the explicit constant in (4).

### Proof architecture

Start from the Cahen-Mellin formula applied to zeta(2u)Gamma(u) on Re u=1/4 and rewrite via Riemann's Xi to obtain a Fourier-type integral identity for the theta function theta_3(0,tau). Analytic continuation in a rotation parameter alpha towards pi/2 (q->-1 tangentially) plus differentiation 2p times yields moment identities for Xi(2t) weighted by cosh-type kernels. Bohr-Riesz summability shows the theta-derivative term vanishes at the boundary, so the weighted moments equal (-1)^p pi cos(pi/8)/4^{2p}: they alternate in sign with p. If Xi had eventually constant sign, one compares odd moments: tail integral versus bounded head integral leads to growth 2^{2p} vs constant K, contradiction for large p. Imported: Cahen-Mellin integral, Riemann's functional equation / Xi, Bohr-Riesz summability.

Dependency edges: CAND-00179 → Cahen-Mellin integral (uses); CAND-00179 → Bohr-Riesz summability (imports); CAND-00076 → CAND-00179 (full account / strengthening in section 4)

**Imported results.** Cahen-Mellin integral (Cahen 1894; Mellin 1895); Bohr-Riesz summability theorem for Dirichlet series; Riemann's functional equation/ Xi representation; Bohr-Landau concentration theorem (C. R. 12 Jan 1914), cited motivationally

**Techniques.** Cahen-Mellin integral; Riemann Xi function and theta transformation; analytic continuation in the angle alpha; moment method: differentiate 2p times and let p grow (alternating-sign moments); Bohr-Riesz / Cesaro summability of Dirichlet series; argument by contradiction on constant sign of Xi

## Context and interpretation

**Importance and obstacle overcome.** First proof that infinitely many zeros are on the critical line, answering a question open since Riemann (1859); before this only Gram's numerical zeros (and the Bohr-Landau concentration result) were known. The obstacle was that no analytic handle existed that detects real zeros of Xi; Hardy's idea transfers the problem to the theta function at q->-1, where odd moments of Xi are computable exactly.

**Relation to prior work.** Builds on Cahen (1894), Mellin (1895), Riemann's Xi, Bohr-Riesz summability. Preceded by Bohr-Landau C. R. 12 Jan 1914. Landau (Math. Ann. 76, 1915) simplified: no property of theta_3 beyond theta_3(0,tau)=0 type behaviour at q=-1 is needed; Hardy-Littlewood 1917 (CAND-00076 sec. 4) replaced the method by a different one giving zeros in [T,T+T^{1/4+eps}].

**Limitations and open questions.** Qualitative only: no counting function, no proportion of zeros on the line. This note says nothing about all zeros; N_0(T) lower bounds are only qualitative here (the full memoir Hardy-Littlewood 1917 gives N_0(T)>cT^{1/2-eps}-type results in the later paper; see CAND-00076, sec. 4: zero between T and T+T^{1/4+delta}). The sketch omits details of the contradiction (the unit-interval lower bound in (6) is stated rather quickly); the full note is 3 pages and the proof is an outline.

**Ideas in remarks/appendices/abandoned paths.** The moment identity (3) in alpha with 2p derivatives is a family of exact linear relations on Xi that is much stronger than needed; their rate of convergence as alpha->pi/2 could encode zero-density information (p. 1013).

## Research potential

- **Hypotheses that might be weakened.** The contradiction needs only that a nonvanishing sign persists beyond T with a quantitative positive lower bound on a unit interval (inequality (6)); this is the only point where 'constant sign' is used, so the same moment identities could give sign-change density statements if the measure of sign-constancy is quantified.
- **Generalizations.** Landau extended to Dirichlet L-functions with characters (Math. Ann. 76 (1915)) and zeros in T..T+T^delta; the method works for any Dirichlet series whose Mellin transform of a theta-type series is Xi-like. Possible modern extension: moment identities from other modular theta/Eisenstein series to produce critical-line zeros for degree-2 L-functions.
- **Candidate connections.** Link to Bohr-Landau zero-density; to Selberg's positive-proportion theorem (a quantitative descendant of the same sign-change idea); to Hardy Z-function sign-change counts; to the Cahen-Mellin route in CAND-00076.
- **Reusable lemmas.** Identity (2)-(3): exact weighted moments of Xi against cosh(alpha t) in terms of theta_3, reusable as a test bed for numerical verification of the alternation of signs of moments.
- **Possible experiments.** Numerically compute $\int_0^\infty \frac{\cosh(\alpha t)t^{2p}\Xi(2t)}{1/4+4t^2}dt$ for alpha near pi/2 and moderate p with mpmath to see the (-1)^p pi cos(pi/8) 4^{-2p} limit; investigate whether quantitative control of the rate at which the theta derivative tends to 0 yields a lower bound for the number of sign changes of Xi(2t) up to T.
- **Risks / barriers.** The method only detects sign changes of Xi, hence only zeros of odd order on the line; it gives no information about zeros off the line and does not by itself yield a positive proportion.

## Audit notes (Level 1 reader)

none noticed in inspected portion. Minor: in (6) the strictly positive lower bound on a unit interval is asserted 'd'apres notre hypothese'; K and K_1 independence from p is asserted without proof (a 3-page Note). OCR of the C.R. scan is poor for formulas; formulas above were read from page images.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00179`; harvest queries: citation_expansion.
- Triage decision: include — Hardy's proof of infinitely many zeros on the critical line.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

# PAPER-0108 — Gaps between zeros of \({\zeta}(s)\) and the distribution of zeros of \(\zeta'(s)\)

| Field | Value |
|---|---|
| Authors | Radziwiłł, Maksym |
| Year / stratum | 2014 / S5 |
| Venue | Adv. Math. 257, 6-24 (2014). |
| Identifiers | zbMATH [1287.11104](https://zbmath.org/?q=an:1287.11104) · DOI [10.1016/j.aim.2014.02.010](https://doi.org/10.1016/j.aim.2014.02.010) · arXiv [1301.3232](https://arxiv.org/abs/1301.3232) |
| MSC | 11M06, 11M26 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1301.3232 |
| Selection | score 4.2403, in-pool citations 8, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** How are small gaps between consecutive zeros of zeta (vertical distribution) related to how close zeros of zeta' lie to the critical line (horizontal distribution)? Prove the Farmer-Ki conjecture (Conjecture 2) in a stronger quantitative form, under RH.

**Historical motivation.** Levinson's method puts 1/3 of zeros on the line using the horizontal distribution of zeta' zeros; Soundararajan's conjecture (A iff B), Zhang's A implies B, Ki's criterion, and Farmer-Ki's conjecture; the Conrey-Iwaniec / Montgomery link from small gaps to absence of Siegel zeros.

### Main results

- **THM-PAPER-0108-1** (Main Theorem, theorem, scope: conditional; Section 1, p.2). Assume RH. Let $A,\delta>0$. (i) If $m'(\varepsilon)\gg\varepsilon^{A}$ as $\varepsilon\to0$ then $m(\varepsilon^{1/2})\gg\varepsilon^{A+\delta}$ for all $\varepsilon\le1$. (ii) If $m(\varepsilon^{1/2})\gg\varepsilon^{A}$ as $\varepsilon\to0$ then $m'(\varepsilon)\gg\varepsilon^{A+\delta}$ for all $\varepsilon\le1$. Here $m'(\varepsilon)=\liminf_{T\to\infty}\frac{2\pi}{T\log T}\sum_{T\le\gamma'\le2T}w\big(\frac{(\beta'-1/2)\log T}{\varepsilon}\big)$ and $m(\varepsilon)=\liminf_{T\to\infty}\frac{2\pi}{T\log T}\sum_{T\le\gamma\le2T}w\big(\frac{(\gamma^+-\gamma)\log T}{\varepsilon}\big)$, $w=\mathbf 1_{[0,1]}$ (the stated reading of the indicator of the unit interval). Equivalent restatement: $\log m(\varepsilon)\sim\log m'(\varepsilon^{1/2})$ as $\varepsilon\to0$ when one of them is $\ge\varepsilon^A$. *Conditional on:* RH.
- **THM-PAPER-0108-2** (Theorem 1, theorem, scope: conditional; Section 2, p.3). Assume RH. Let $A,\delta>0$. There is $C=C(\delta,A)$ (approximately $(B\delta/A)^{32A/\delta}$, $B$ absolute) such that if $0<\varepsilon<C$ and $m'(\varepsilon)\ge c\,\varepsilon^{A}$ then $m(\varepsilon^{1/2-\delta})\ge (c/8)\,\varepsilon^{A}$. *Conditional on:* RH.
- **THM-PAPER-0108-3** (Theorem 2, theorem, scope: conditional; Section 2, p.3; proved in Section 8). Assume RH. Let $A,\delta>0$. There is $C=C(\delta,A)$ such that if $0<\varepsilon<C$ and $m(\varepsilon^{1/2})\ge c\,\varepsilon^{A}$ then $m'(\varepsilon)\ge (c/4)\,\varepsilon^{A+\delta}$. *Conditional on:* RH.
- **THM-PAPER-0108-4** (Proposition 1, proposition, scope: conditional; Section 2, p.3). Let $0<\delta,\varepsilon<1$ and $S_{\varepsilon,\delta}(T)$ the set of zeros $\rho'=\beta'+i\gamma'$ of $\zeta'$ with $T\le\gamma'\le2T$, $\beta'-1/2\le\varepsilon/\log T$ and $|\gamma_c-\gamma_c^{\pm}|>\varepsilon^{1/2-\delta}/\log T$ ($\rho_c=1/2+i\gamma_c$ the zero of $\zeta$ nearest $\rho'$; $\gamma_c^\pm$ the neighbouring ordinate closest to $\gamma_c$). There is $C(\delta,A)$ with $|S_{\varepsilon,\delta}(T)|\le\varepsilon^{A}\,T\log T$ for $0<\varepsilon<C$. *Conditional on:* RH.
- **THM-PAPER-0108-5** (Proposition 2, proposition, scope: conditional; Section 2, p.3; proof Section 4). Let $0<\delta<1$, $0<\varepsilon<c$ ($c$ absolute) and $Z=Z_{\varepsilon,\delta}(T)$ a set of $\delta/\log T$-well-spaced ordinates of zeros $\rho'\ne\rho$ with $\beta'-1/2\le\varepsilon/\log T$, $T\le\gamma'\le2T$. If $|Z|\gg\varepsilon^{A}T\log T$ then for any $\kappa>0$ all but $\kappa|Z|$ elements satisfy $\sqrt{\frac{\beta'-1/2}{\log T}}\ll|\rho'-\rho_c|\ll\sqrt{A\log(\varepsilon\kappa\delta)^{-1}}\cdot\sqrt{\frac{\beta'-1/2}{\log T}}$. Complements the classical lower bound $|\rho'-\rho_c|\ge\sqrt{\tfrac23(\beta'-\tfrac12)/\log T}$ (Soundararajan). *Conditional on:* RH.
- **THM-PAPER-0108-6** (Corollary 1, corollary, scope: conditional; Section 1, p.2; proof Section 9). Assume RH and the Pair Correlation Conjecture. For every $\delta>0$, $\varepsilon^{3/2+\delta}\ll m'(\varepsilon)\ll\varepsilon^{3/2-\delta}$ as $\varepsilon\to0$. *Conditional on:* RH, Pair Correlation Conjecture.
- **THM-PAPER-0108-7** (Corollary 2, corollary, scope: asymptotic; Section 1, p.2). Let $A>0$. If $m'(\varepsilon)\gg\varepsilon^{A}$ for all $\varepsilon>0$ (under RH), then for all primitive characters $\chi$ mod $q$ with $q$ sufficiently large, $L(1,\chi)>(\log q)^{-18}$; hence no Siegel zero and class number $h(-d)\ge c\sqrt d(\log d)^{-18}$ (noneffective). *Conditional on:* RH, Conrey-Iwaniec Thm 1.1.

### Key definitions

- $\rho=\beta+i\gamma$ zeros of $\zeta$; $\rho'=\beta'+i\gamma'$ zeros of $\zeta'$; under RH $\beta'\ge1/2$
- $m'(\varepsilon)$, $m(\varepsilon)$ as in Main Theorem (liminf densities)
- $\rho_c$: zero of zeta closest to rho' (ties: closer to origin)
- $A_N(s)$, $B_N(s)$ Selberg-type Dirichlet polynomials
- well-spaced sets of ordinates with spacing delta/log T

### Principal lemmas

- **THM-PAPER-0108-L1** (Lemma 1 (Selberg); Section 3, p.4). For $\sigma=1/2+2/\log N$, $N\le T$, $T\le t\le2T$: $\sum_\rho\frac{\sigma-1/2}{(\sigma-1/2)^2+(t-\gamma)^2}\ll|A_N(s)|+\log T$, with $A_N(s)=\sum_{n\le N}\Lambda(n)W_N(n)n^{-s}$, $W_N(n)=1$ for $n\le N^{1/2}$, $\log(N/n)/\log N$ otherwise. — *Role:* Controls zero density near a point via a short Dirichlet polynomial (imported, eq. (2.2) of Selberg).
- **THM-PAPER-0108-L2** (Lemma 2; Section 3, p.4). For $T\le t\le2T$, $N\le T$: the number of zeros in $[t-\pi/\log N,t+\pi/\log N]$ is $\ll\frac{\log T}{\log N}+\frac{|B_N(1/2+it)|}{\log N}$ with $B_N(s)=\sum_{n\le N}\Lambda(n)n^{-s}(1-\log n/\log N)$. — *Role:* Local zero-count bound via Fejer kernel and explicit formula; used to bound near-zero contributions in the Hadamard-type sum for zeta'.
- **THM-PAPER-0108-L3** (Lemma 3; Section 3, p.5). Let $A(s)$ be a Dirichlet polynomial of length $x$ with positive coefficients, points $s_r=\sigma_r+it_r$, $T\le t_r\le2T$, $0\le\sigma_r-1/2\le\varepsilon/\log T$, $|t_i-t_j|\ge\delta/\log T$, $100\varepsilon<\delta<1$. If $x^k\le T$ then $\sum_r|A(s_r)|^{2k}\le\frac{20\log T}{\delta}\int_{-2T}^{2T}|A(1/2+it)|^{2k}dt$. — *Role:* Large-sieve-type bound for off-line well-spaced points; proof by mean-value (subharmonicity) over disjoint discs plus a majorant principle.
- **THM-PAPER-0108-L4** (Lemma 4; Section 3, p.6). For well-spaced points as in Lemma 3 and $N^k\le T/\log T$, the number of $s_r$ with $|A_N(s_r)|>(k/e)\log N$ or $|B_N(s_r)|>(k/e)\log N$ is $\ll(e^{-k}/\delta)T\log T$. — *Role:* Moment/Chebyshev tail bound turning Lemma 3 plus Soundararajan's moment bound into a count of exceptional zeros of zeta'.
- **THM-PAPER-0108-L5** (Lemma 5; Section 3, p.6). Uniformly for $T\le t\le2T$, $N\le T$, $0<c<1$: $\frac{\zeta'}{\zeta}(s)=\sum_{|s-\rho|<c/\log T}\frac1{s-\rho}+O\big(\frac{\log T}{c}E_{T,N}(s)\big)$ with $E_{T,N}$ built from $|A_N|,|B_N|$; and $\sum_r|E_{T,N}(s_r)|^{2k}\ll(k^{2k}/\delta)T\log T$. — *Role:* Localisation of zeta'/zeta to nearby zeros; enters the proof of Proposition 1.
- **THM-PAPER-0108-L6** (Lemma 6 (Zhang); Section 4, p.7). If $\rho'\ne\rho$ then $\frac12\log\gamma'=\sum_\rho\frac{\beta'-1/2}{(\beta'-1/2)^2+(\gamma'-\gamma)^2}+O(1)$. — *Role:* Basic identity from zeta'(rho')=0 linking beta'-1/2 to the zero distribution of zeta; start of proof of Prop. 2.
- **THM-PAPER-0108-L7** (Lemma 7 (Soundararajan), Lemma 11 (Zhang), Lemma 12 (Soundararajan); Sections 5-8 (lines ~436, 670, 675 of text)). Statements on two-zero configurations controlling zeta'-zeros and on the converse direction (a small gap of zeta zeros yields a zeta' zero near the line); precise forms not read in detail. — *Role:* Imported inputs for Theorem 1 (Lemma 7) and Theorem 2 (Lemmas 11-12).
- **THM-PAPER-0108-L8** (Lemma 8 (Gonek), Lemma 9, Lemma 10; Sections 6-7). Gonek's mean-value estimate for Dirichlet polynomials with Lambda coefficients (x=a/b, a,b<=N); Lemma 9 is a moment bound for $B_N$ when $N^k\le T$; Lemma 10 bounds a related mean value on $[T,2T]$. Exact statements not read in detail. — *Role:* Moment estimates feeding the second-moment/shape part of Theorem 1 (Corollary 3, Section 7).

### Proof architecture

Throughout RH. Direction m' => m (Theorem 1): fix a zero rho' of zeta' with beta'-1/2 <= eps/log T. Prop. 2 shows that for all but a small fraction of such zeros, the nearest zeta zero rho_c dominates the Zhang identity (Lemma 6), so |rho'-rho_c| is of order sqrt((beta'-1/2)/log T). Proof of Prop. 2: split zeros rho by |gamma-gamma'|<pi/log N (controlled by Lemma 2 via B_N) and the rest (controlled by Selberg's Lemma 1 via A_N); Lemma 3/4 (large sieve + Chebyshev with 2k-th moments, k ~ A log(1/(kappa eps delta)), N^k ~ T/log T) show |A_N|,|B_N| are <= (k/e)log N at all but kappa|Z| points. Prop. 1 then says few such zeta' zeros can have zeta-gap larger than eps^{1/2-delta}/log T; Lemma 5 and Gonek-type moment estimates (Lemmas 8-10) feed the proof; Theorem 1 follows by pigeonholing each close zeta' zero to a close zeta-gap (losing factor 8). Converse (Theorem 2, Section 8): following Zhang, a gap of size <= eps^{1/2}/log T next to zero rho yields a zero rho' of zeta' with beta'-1/2 <= eps/log T (Lemma 11), with Soundararajan's Lemma 12 used for the counting. Corollary 1 combines Main Theorem with Lemma 13 (PCC gives eps^{3+delta} << m(eps) << eps^{3-delta}); Corollary 2 combines the Main Theorem with Conrey-Iwaniec Thm 1.1. Sections 5-9 were not read in full, so this skeleton for Sections 5-9 is partly inferred from the section headers and statements.

Dependency edges: CAND-01416 → Zhang (zeta' zeros and small gaps) (extends); CAND-01416 → Soundararajan 1998 conjecture (partial resolution (quantitative form)); CAND-01416 → Farmer-Ki conjecture (proves); CAND-01416 → CAND-01810 (related: small-gap / pair-correlation inputs (Montgomery formula)); CAND-01416 → Conrey-Iwaniec Siegel zero criterion (applies)

**Imported results.** Selberg: Lemma 1, eq. (2.2) of Selberg's paper, and the zeta'/zeta local approximation (Selberg, eq. (14)); Soundararajan: moment bound $\int|D_N(1/2+it)|^{2k}\ll k!T(\log N)^{2k}$ for $N^k\le T/\log T$ (Lemma 3 in Soundararajan [17]); Zhang: Lemma 3 (identity), Lemma 11; Soundararajan Lemma 7 and Lemma 12; Gonek mean value (Lemma 8); Conrey-Iwaniec Theorem 1.1 (m(1/4)>0 implies L(1,chi)>(log q)^{-18}); Montgomery/Goldston-type pair-correlation inputs for Lemma 13/Corollary 1; majorant principle (Montgomery, Topics, Ch.3 Thm 3)

**Techniques.** Selberg-type Dirichlet polynomial approximations to zeta'/zeta and to zero counts; Fejer-kernel explicit formula bound (Lemma 2); large sieve / subharmonic mean-value inequality for off-line well-spaced points; 2k-th moment (Soundararajan-type) bound and Chebyshev counting; Zhang's identity relating beta'-1/2 to sum over zeros of zeta; Gonek mean-value for Dirichlet polynomials with von Mangoldt coefficients; majorant principle for positive-coefficient Dirichlet polynomials

## Context and interpretation

**Importance and obstacle overcome.** Gives the first quantitative two-way equivalence between the small-gap statistics of zeta zeros and proximity of zeta' zeros to the half-line (under RH), settling Farmer-Ki. The obstacle is that a zeta' zero near the line may come from a regularly spaced cluster rather than a small gap; the author overcomes it by showing, via moment/large-sieve control of Selberg's Dirichlet polynomials, that for almost all such zeros a single nearest zero of zeta dominates, so a pairing zeta' zero to a gap is forced.

**Relation to prior work.** Extends Zhang (small gaps imply zeta' zeros near line) and Soundararajan (1998 conjecture and key lemma), Ki (criterion for negation of B), Farmer-Ki (Conjecture 2); uses Selberg's Dirichlet-polynomial technique, Gonek's mean value, Conrey-Iwaniec for the Siegel zero corollary; Corollary 2 is weaker than a result already due to Farmer-Ki (as the author notes).

**Limitations and open questions.** All results conditional on RH (the beta'>=1/2 equivalence is used as a normalization). Quantitative exponent loss: m'(eps) vs m(eps^{1/2}) only up to eps^{delta} in the exponent, so only 'log m ~ log m'(eps^{1/2})' not a sharp relation; constant C(delta,A) is very small ((B delta/A)^{32A/delta}) and ineffective in the Siegel-zero corollary. Corollary 1 requires the Pair Correlation Conjecture so cannot improve Levinson's proportion unconditionally. Open (authors): whether Farmer-Ki threshold exp(-eps^{-1/2+delta}) can be improved for the Siegel zero problem; the conjecture m'(eps) asymp m(eps^{1/2}) (not proved); Soundararajan Conjecture 1 (liminf of gaps zero iff liminf of (beta'-1/2)log gamma' zero) remains open.

## Research potential

- **Hypotheses that might be weakened.** RH is used for beta'>=1/2 and for Selberg/Soundararajan machinery (Lemmas 1,2,5); the dependence of C(delta,A) on delta/A is exponentially poor and could be improved by replacing the Chebyshev moment bound by a sharper large-deviation estimate in Lemma 4. The condition |t_i-t_j|>=delta/log T with 100*eps<delta<1 in Lemma 3 could be relaxed with a different mean-value inequality.
- **Generalizations.** Analogues for zeros of derivatives of L(s,chi) or other degree-d L-functions with Selberg-class Dirichlet polynomials (Lemmas 1-5 only need an explicit formula and mean-value bounds); higher derivatives zeta^{(k)}; passing from lower-density m to an almost-all version.
- **Candidate connections.** Carneiro-Chandee-Littmann-Milinovich (CAND-01810): Theorem 7 there (N(T,0.606894) >> N(T)) gives m(eps)>0 for eps>=0.606894-type thresholds under RH plus simple zeros, which would feed Radziwill's Theorem 2 direction; Levinson-Conrey loss analysis for Corollary 1 exponents (eps^{3/2}).
- **Reusable lemmas.** Lemma 3 (large sieve at off-line well-spaced points) and Lemma 4 (tail count via 2k-th moments) are reusable whenever one needs a pointwise bound for Dirichlet polynomials on a sparse set of points off the critical line; Lemma 5 gives a localized zeta'/zeta expansion.
- **Possible experiments.** Compute with Odlyzko-type zero tables the empirical m'(eps) and m(eps) for T around 1e6..1e12 and test whether log m'(eps) ~ log m(eps^{1/2}) holds numerically against the predictions (8/9pi)eps^{3/2} and (pi/6)eps^3; test the dominance of rho_c in Lemma 6 / Prop. 2 (ratio |rho'-rho_c| / sqrt((beta'-1/2)/log T)).
- **Risks / barriers.** The key lower bound |rho'-rho_c|>=sqrt(2/3 (beta'-1/2)/log T) and the exponent 1/2 (square root) is intrinsic: removing the delta loss requires much finer control on clusters; the Siegel-zero application is weaker than Farmer-Ki and ineffective.

## Audit notes (Level 1 reader)

Main Theorem (ii) is stated with m(eps^{1/2}) >> eps^A and conclusion m'(eps) >> eps^{A+delta}, while Theorem 2 gives m'(eps) >= (c/4)eps^{A+delta} only for eps<C(delta,A); the 'for all eps<=1' of the Main Theorem presumably absorbs small-eps constants (not checked). Text extraction renders w as the unit-interval indicator; Prop. 2's displayed upper bound sqrt(A log(eps kappa delta)...) as extracted is garbled (likely log of the inverse); I read it as sqrt(A log((eps kappa delta)^{-1})). Corollary 2 requires m'(eps)>>eps^A for ALL eps>0 but uses m(1/4)>0, a consequence of Main Theorem (i) with eps=1/16 and A,delta fixed; this seems consistent. Sections 5-9 not read line by line.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01416`; harvest queries: kw_RH_any, kw_pair_correlation, kw_zeta_zeros, msc_11M06, msc_11M26, arxiv_pair_corr, arxiv_rh_abs, arxiv_zeta_zeros.
- Triage decision: include — Settles Farmer-Ki conjecture linking small gaps with zeros of zeta' near the line.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

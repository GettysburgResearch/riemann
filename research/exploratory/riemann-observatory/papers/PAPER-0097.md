# PAPER-0097 — Vinogradov's integral and bounds for the Riemann zeta function.

| Field | Value |
|---|---|
| Authors | Ford, Kevin |
| Year / stratum | 2002 / S5 |
| Venue | Proc. Lond. Math. Soc., III. Ser. 85, No. 3, 565-633 (2002). |
| Identifiers | zbMATH [1034.11044](https://zbmath.org/?q=an:1034.11044) · DOI [10.1112/S0024611502013655](https://doi.org/10.1112/S0024611502013655) · arXiv [1910.08209](https://arxiv.org/abs/1910.08209) |
| MSC | 11M06, 11N05, 11L15, 11D72, 11M35 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — arXiv:1910.08209 (v1, dated 25 Oct 2001; 4500-line text) |
| Selection | score 4.3135, in-pool citations 48, seed lists 2, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Obtain explicit constants in Richert-type bound |zeta(sigma+it)|<=A t^{B(1-sigma)^{3/2}} log^{2/3} t, by explicit bounds for Vinogradov's integral and Weyl-type sums S(N,t)=max|sum_{N<n<=R}(n+u)^{-it}|.

**Historical motivation.** Richert 1967 B=100; successive reductions (Kulas 18.4974, Cheng 46); applications to zero-free regions, PNT error, zero densities, divisor problem.

### Main results

- **THM-PAPER-0097-1** (Theorem 1, theorem, scope: global; p.1). For $t\ge3$, $1/2\le\sigma\le1$: $|\zeta(\sigma+it)|\le At^{B(1-\sigma)^{3/2}}\log^{2/3}t$ and, for $0<u\le1$, $|\zeta(s,u)-u^{-s}|\le At^{B(1-\sigma)^{3/2}}\log^{2/3}t$, with $B=4.45$, $A=76.2$ (Hurwitz zeta).
- **THM-PAPER-0097-2** (Theorem 2, theorem, scope: global; p.4). For positive integer $N\le t$ and $\lambda=\log t/\log N$: $S(N,t)\le 9.463N^{1-1/(133.66\lambda^2)}$ (S(N,t)=max_{0<u<=1}max_{N<R<=2N}|sum_{N<n<=R}(n+u)^{-it}|). Proved here for large lambda via Vinogradov method; for 2.6<=lambda<=87 by older methods (Sec. 6, Lemma 6.8).
- **THM-PAPER-0097-3** (Corollary 2A, corollary, scope: global; p.4). For a Dirichlet character mod q, $q\le N\le qt$ ... $\max_R|\sum_{N<n\le R}\chi(n)n^{-it}|\le10.463\frac{\phi(q)N}{q}e^{-\log^3(N/q)/(133.66\log^2t)}$ (as printed; OCR partially garbled).
- **THM-PAPER-0097-4** (Theorem 3, theorem, scope: global; p.6). For integers $k\ge1000$, $2k^2\le s\le\frac{k^2}2(\tfrac12+\log\tfrac{3k}8)$ (as printed): $J_{s,k}(P)\le k^{2.055k^3-5.91k^2+3s}1.06^{sk+2s^2/k-9.7278k^3}P^{2s-k(k+1)/2+\Delta_s}$ for $P\ge1$, $\Delta_s=\frac38k^2e^{1/2-2s/k^2+1.7/k}$. Also for $k\ge129$ there is $s\le\rho k^2$ with $J_{s,k}(P)\le k^{\theta k^3}P^{2s-k(k+1)/2+0.001k}$ with $(\rho,\theta)=(3.21432,2.3291)$ for $k\ge200$, etc.
- **THM-PAPER-0097-5** (Theorem 4, theorem, scope: global; p.7). For $k\ge60$, $0.9k\le h\le k-2$, $2t\le s\le\lfloor h/2\rfloor t$, $P\ge e^{Dk^2}$ with $D\ge10$ and constraints (1.10): $J_{s,k,h}(\mathcal C(P,P^\eta))\le e^CP^{2s-\frac t2(h+k)+t(t-1)/2\cdot\ ...+\eta s^2/(2t)+ht\exp\{-s/(ht)\}}$ (exponent as printed, OCR-unclear), with explicit C; here $J_{s,k,h}(B)$ counts solutions of $\sum(x_i^j-y_i^j)=0$, $h\le j\le k$, $x_i,y_i\in B$ and $\mathcal C(P,R)$ = integers <=P with all prime factors in $(\sqrt R,R]$.
- **THM-PAPER-0097-6** (Lemma 7.3, lemma, scope: global; Sec. 7). If $S(N,t)\le CN^{1-1/(D\lambda^2)}$ for $1\le N\le t$, then with $B=9\sqrt3\,D^{?}$ (as printed 'B = 9 sqrt(3D)'), for $15/16\le\sigma\le1$, $t\ge10^{100}$: $|\zeta(s)|\le\big(\frac{C+1+10^{-80}}{\log^{2/3}t}+1.569CD^{1/3}\big)t^{B(1-\sigma)^{3/2}}\log^{2/3}t$ (and same for Hurwitz).
- **THM-PAPER-0097-7** (Lemma 7.1, lemma, scope: finite; Sec. 7). For $1/2\le\sigma\le1$, $0<u\le1$, $t\ge3$, if $\sigma\le15/16$ or $t\le10^{100}$: $|\zeta(s)|,|\zeta(s,u)-u^{-s}|\le58.1t^{4(1-\sigma)^{3/2}}\log^{2/3}t$.

### Key definitions

- S(N,t)
- J_{s,k}(P), J_{s,k}(P;h), J_{s,k,h}(B)
- C(P,R)
- Hurwitz zeta zeta(s,u)

### Principal lemmas

- **THM-PAPER-0097-L1** (Lemma 5.1; Sec. 5). Core Vinogradov-method lemma bounding the Weyl-type sum via mean values J_{s,k,h}(B) of incomplete systems (statement not read in detail) — *Role:* the 'core of the argument' per Ford; links S(N,t) to Theorem 3 and 4
- **THM-PAPER-0097-L2** (Proposition ZRD (Zero Representation Dominates); Sec. 2). Not read in detail; used in Sec. 2-3 to compare numbers of representations among systems of polynomial equations — *Role:* counting-solution comparison tool in bounds for J_{s,k}
- **THM-PAPER-0097-L3** (Lemma 3.2 / 3.3 / 3.4; Sec. 3). Explicit bounds for J_{s,k}(P) obtained by Wooley's efficient differencing combined with Arkhipov-Karatsuba idea (statements not read in detail) — *Role:* produce Theorem 3
- **THM-PAPER-0097-L4** (Lemma 4.1; Sec. 4). Efficient-differencing bound for J_{s,g,h} over smooth-like sets C(P,R) (not read in detail) — *Role:* produces Theorem 4
- **THM-PAPER-0097-L5** (Lemma 6.8; Sec. 6). Theorem 2 holds for 2.6<=lambda<=87, via Corollary 6.4 with tabulated (k,n) choices — *Role:* covers small lambda by older Vinogradov/Weyl-differencing methods
- **THM-PAPER-0097-L6** (Lemma 8.1; Sec. 8). Incomplete-system differencing lemma; Sec. 8 says its use in place of Lemma 4.1 could lower B by about 0.09 (about 2%) — *Role:* discussion of further improvement

### Proof architecture

(Sec. 2-4) Explicit bounds for Vinogradov's integral J_{s,k}(P) (Theorem 3, Wooley's method + Arkhipov-Karatsuba) and for incomplete-system counts J_{s,k,h} over the set C(P,R) of integers with all prime factors in (sqrt R, R] (Theorem 4), avoiding the large divisor count of ordinary smooth numbers. (Sec. 5) Vinogradov's method (Lemma 5.1) bounds S(N,t) in terms of both, giving Theorem 2 for large lambda; (Sec. 6) older methods for 2.6<=lambda<=87. (Sec. 7) Apply Euler-Maclaurin type formula (7.1) and Theorem 2 to bound zeta(s) and Hurwitz zeta, giving Theorem 1 via Lemma 7.3 and 7.1. (Sec. 8) Limits of the method.

Dependency edges: CAND-01233 → CAND-01368 (uses B=4.45, A=76.2)

**Imported results.** Wooley's results on J_{s,k}(P) and efficient differencing [29,30,34]; Arkhipov-Karatsuba, Tyrina bounds; Kulas S(N,t) bound; Cheng explicit methods; Richert 1967 form of the bound; Pintz Theorem 8 for PNT error term (used in applications); Montgomery Theorem 12.3 (zero density); Carlson theorem (Titchmarsh 7.9)

**Techniques.** Vinogradov mean value theorem (explicit); Wooley efficient differencing; Arkhipov-Karatsuba improvement; incomplete systems (Mardzhanishvili); C(P,R) sets of integers with prime factors in (sqrt R,R]; Weyl differencing for small lambda; explicit Euler-Maclaurin for Hurwitz zeta

## Context and interpretation

**Importance and obstacle overcome.** Reduced the explicit constant B in Richert bound from 18.4974 (Kulas), 46 (Cheng) to 4.45 with A=76.2, fully explicit, enabling zero-free region 1/57.54, PNT error with c=0.2098, zero density N(sigma,T)<<T^{58.05(1-sigma)^{3/2}}log^{15}T, and divisor problem exponents. Obstacle: explicit constants in Vinogradov method growing with k; overcome via C(P,R) sets and incomplete-system differencing.

**Relation to prior work.** Corrects an error in Montgomery Corollary 12.5 (B=100 gives T^{167...} stated, per paper); notes flaws in Fujii and Panteleeva divisor problem claims (stated in Sec. 1(v)). Supplies inputs to CAND-01233.

**Limitations and open questions.** B=4.45 is far from the limit expected; Sec. 8 discusses that even with ideal Vinogradov integral bounds the method has a barrier, and that Lemma 8.1 could reduce B by only ~0.09. Under RH any B>0 works.

## Research potential

- **Hypotheses that might be weakened.** Theorem 2's constant 133.66 in the exponent and Theorem 3's k>=1000 range; improvements via Wooley's later efficient congruencing / Bourgain-Demeter-Guth decoupling (post-2002) to J_{s,k}(P) could lower B (not assessed by the paper).
- **Generalizations.** Dirichlet L-function version via Corollary 2A; Hurwitz zeta already included.
- **Candidate connections.** Explicit zero-free regions, zero density, mean values sigma_k bounds sigma_k<=1-(1/3)(Bk)^{-2/3} from Carlson (stated in Sec. 1(iv)).
- **Reusable lemmas.** Theorem 2 (explicit S(N,t)); Lemma 7.3 translating exponential sum bound constants (C,D) into (A,B).
- **Possible experiments.** Recompute B using Lemma 7.3 with the optimal-in-range D after substituting post-2002 Vinogradov mean value bounds (BDG 2016) in Theorem 3 inputs; check numerically Theorem 2 for moderate N,t.
- **Risks / barriers.** Does not address RH; B is limited by method; heavy numerical parameter checking; proofs of Sec. 2-6 not independently verified by this reader.

## Audit notes (Level 1 reader)

Exponent in Theorem 4 and the 'B = 9 sqrt(3D)' formula in Lemma 7.3 are OCR-garbled in my reading (line 3777 ff.) and recorded as printed with caveat. Introduction says Lemma 7.1 constant 58.1 and Theorem 1 uses A=76.2; no inconsistency noticed. Long proofs not read.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01368`; harvest queries: kw_moments_zeta, kw_zero_density, kw_zero_free, msc_11M06, msc_11N05.
- Triage decision: include — Sharpest explicit bounds for zeta, zero-free region via Vinogradov integral.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

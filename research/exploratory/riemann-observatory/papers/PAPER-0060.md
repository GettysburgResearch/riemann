# PAPER-0060 — Partial sums of the Möbius function

| Field | Value |
|---|---|
| Authors | Soundararajan, K. |
| Year / stratum | 2009 / S5 |
| Venue | J. Reine Angew. Math. 631, 141-152 (2009). |
| Identifiers | zbMATH [1184.11040](https://zbmath.org/?q=an:1184.11040) · DOI [10.1515/CRELLE.2009.044](https://doi.org/10.1515/CRELLE.2009.044) · arXiv [0705.0723](https://arxiv.org/abs/0705.0723) |
| MSC | 11N37 |
| Families | A, C |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/0705.0723 |
| Selection | score 4.5291, in-pool citations 21, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Under RH, improve the Maier-Montgomery bound M(x) << sqrt(x) exp(C (log x)^{39/61}) for the Mertens function M(x)=sum_{n<=x} mu(n); key input is the frequency with which ordinates of zeta zeros cluster abnormally in short intervals, which yields lower bounds for |zeta(sigma+it)| off the line outside a thin exceptional set of t.

**Historical motivation.** Littlewood (RH implies M(x)<<x^{1/2+eps}); Landau, Titchmarsh refined; Maier-Montgomery (exp(C(log x)^{39/61}) factor) opened the use of local zero clustering; this paper pushes that approach to the exponent 1/2 with a log log power.

### Main results

- **THM-PAPER-0060-1** (Theorem 1, theorem (conditional on RH), scope: asymptotic; Sec 1 (p.1); proved in Sec 5). Assume RH. For large $x$, $M(x)\ll \sqrt{x}\,\exp\big((\log x)^{1/2}(\log\log x)^{14}\big)$. *Conditional on:* RH.
- **THM-PAPER-0060-2** (Theorem 2, theorem (conditional on RH), scope: asymptotic; Sec 1 p.2; proof Sec 3). Assume RH. Let $T$ be large, $0\le h\le\sqrt T$, $(\log\log T)^2\le V\le \log T/\log\log T$. The number $R$ of well-spaced points $T\le t_1<\dots<t_R\le 2T$ ($t_{j+1}-t_j\ge1$) with $N(t_j+h)-N(t_j-h)-\frac{h}{\pi}\log\frac{t_j}{2\pi}>V$ satisfies $R\ll T\exp\!\big(-V\log\frac{V}{\log\log T}+3V\log\log V\big)$. *Conditional on:* RH.
- **THM-PAPER-0060-3** (Definition 3 (V-typical point), definition, scope: finite; Sec 1 p.2). $t\in[T,2T]$ is $V$-typical if (i) with $x=T^{1/V}$, $\big|\sum_{n\le x}\frac{\Lambda(n)\log(x/n)}{n^{\sigma+it}\log n\log x}\big|\le 2V$ for all $\sigma\ge1/2$; (ii) every subinterval of $(t-1,t+1)$ of length $2\pi V/\log T$ contains at most $3V$ zero ordinates; (iii) every subinterval of $(t-1,t+1)$ of length $2\pi V/((\log V)\log T)$ contains at most $V$ zero ordinates.
- **THM-PAPER-0060-4** (Proposition 4, proposition (conditional on RH), scope: asymptotic; Sec 1 p.3; proof Sec 4). Assume RH. Every $t\in[T,2T]$ is $V$-typical when $V\ge(\tfrac12+o(1))\log T/\log\log T$. For $(\log\log T)^2\le V\le\log T/\log\log T$ the number of well-spaced $V$-atypical points in $[T,2T]$ is $R\ll T\exp(-V\log\frac{V}{\log\log T}+4V\log\log V)$. *Conditional on:* RH.
- **THM-PAPER-0060-5** (Proposition 5, proposition (conditional on RH), scope: asymptotic; Sec 1 p.3; proof Sec 4). Assume RH, $T\le t\le 2T$ $V$-typical for some $(\log\log T)^2\le V\le\log T/\log\log T$, $\sigma_0=\frac12+\frac V{\log T}$. For $2\ge\sigma\ge\sigma_0$: $\log|\zeta(\sigma+it)|\ge -V\log\log V$ (stated; proof gives $\ge -CV$). For $\frac12<\sigma\le\sigma_0$: $\log|\zeta(\sigma+it)|\ge -V\log\frac{\sigma_0-1/2}{\sigma-1/2}-8V\log\log V$. *Conditional on:* RH.

### Key definitions

- V-typical / V-atypical point (Definition 3)
- F(s)=sum_rho Re 1/(s-rho)
- well-spaced points: gaps >=1

### Principal lemmas

- **THM-PAPER-0060-L1** (Lemma 6; Sec 2 pp.3-4). Selberg/Beurling-Vaaler extremal minorant and majorant $F_\pm$ of $\chi_{[-h,h]}$: even entire, $F_-\le\chi\le F_+$, $\int|F_\pm-\chi|\le1/\Delta$, $\hat F_\pm(x)=0$ for $|x|\ge\Delta$, $\hat F_\pm(x)=\frac{\sin 2\pi hx}{\pi x}+O(1/\Delta)$, and $|F_\pm(z)|\ll e^{2\pi\Delta|y|}/(\Delta|z|^2)$ for $|z|\ge2h$. — *Role:* Band-limited approximation to the indicator of an interval, fed into the explicit formula (imported, Selberg/Vaaler)
- **THM-PAPER-0060-L2** (Lemma 7; Sec 2 p.4). Explicit formula for $\sum_\rho h(\gamma)$ with $h$ analytic in $|\mathrm{Im}\,s|\le\frac12+\epsilon$, $|h(s)|\ll(1+|s|)^{-1-\delta}$. — *Role:* Converts zero counting in a window into a prime sum (imported, standard)
- **THM-PAPER-0060-L3** (Lemma 8; Sec 2 p.5). Large-sieve-type moment inequality: for $A(s)=\sum_{p\le N}a(p)p^{-s}$, well-spaced $s_r=\sigma_r+it_r$, $\sigma_r\ge\alpha$, $N^k\le T$: $\sum_r|A(s_r)|^{2k}\ll T(\log T)^2k!\big(\sum_{p\le N}|a(p)|^2p^{-2\alpha}\big)^k$. — *Role:* High-moment bound on prime sums at well-spaced points; the source of the exp(-V log V) tail (imported from Maier-Montgomery Lemma 5)
- **THM-PAPER-0060-L4** (Lemma 9; Sec 4 p.7). For $T\le t\le2T$ $V$-typical and $\frac12<\sigma\le\sigma_0$: $\log|\zeta(\sigma+it)|\ge\log|\zeta(\sigma_0+it)|-V\log\frac{\sigma_0-1/2}{\sigma-1/2}-7V\log\log V$. — *Role:* Propagates the bound from sigma_0 toward the critical line using zero spacing conditions (ii),(iii)
- **THM-PAPER-0060-L5** (Lemma 10; Sec 4 p.8). Uniformly for $\frac12<\sigma\le2$, $2\le x\le T$: $\log|\zeta(\sigma+it)|\ge\mathrm{Re}\sum_{n\le x}\frac{\Lambda(n)\log(x/n)}{n^{\sigma+it}\log n\log x}-\Big(1+\frac{x^{1/2-\sigma}}{(\sigma-1/2)\log x}\Big)\frac{F(\sigma+it)}{\log x}+O(1)$, where $F(s)=\sum_\rho\mathrm{Re}\frac1{s-\rho}$. — *Role:* Smoothed prime-sum lower bound for log|zeta| in terms of zero-sum F
- **THM-PAPER-0060-L6** (Lemma 11; Sec 4 p.8-9). For $t\in[T,2T]$ $V$-typical and $2\ge\sigma\ge\sigma_0$ there is an absolute $C$ with $\log|\zeta(\sigma+it)|\ge -CV$. — *Role:* Gives (3) of Prop 5

### Proof architecture

Perron formula (9) with c=1+1/log x truncated at height [x], M(x)=(1/2 pi i) int x^s/(s zeta(s)) ds + O(log x). Contour is deformed to a staircase: for |t|<=x_0=exp(sqrt(log x)) one vertical line at Re s=1/2+1/log x using |zeta(1/2+1/log x+it)|^{-1} << (|t|+2)^{loglog x}; for each integer n in [x_0,x] a vertical unit segment at Re s=1/2+V_n/log x, where V_n is the least integer in [(loglog n)^2, log n/loglog n] making [n,n+1] V_n-typical (existence from Prop 4 first assertion), joined by horizontal segments. Prop 5 gives 1/|zeta| <= exp(V_n log(...) + 8 V_n loglog V_n) on the verticals; dyadic summation over [T,2T] uses #{n: V_n=V} from Prop 4 (minimality of V_n means some point in [n,n+1] is (V-1)-atypical) to show the exceptional weight exp(-V log(V/loglog T)) beats the cost exp(V log(log x/log T)), giving the exp((log x)^{1/2}(loglog x)^{14}) saving. Prop 4 and Thm 2 come from the Goldston-Gonek bound |S(T)|<=(1/2+o(1)) log T/loglog T, Selberg minorants with Delta=(1+eta)log T/(2 pi V), eta=1/log V, explicit formula, reduction to prime sums, and the 2k-th moment Lemma 8 with k=floor(V/(1+eta)). Prop 5 from Hadamard factorization (7), conditions (i)-(iii) and Lemmas 9-11.

Dependency edges: CAND-01251 → Goldston-Gonek 2007 (S(T) bound) (imports); CAND-01251 → Maier-Montgomery 2009 (M(x) with exponent 39/61) (improves); CAND-01180 → CAND-01251 (same extremal-function method family (Selberg vs Carneiro-Vaaler majorants))

**Imported results.** Goldston-Gonek: |S(T)|<=(1/2+o(1))log T/loglog T and N(t+h)-N(t)-(h/2pi)log(t/2pi) bound (Theorem 1 of Goldston-Gonek, cited as [3]); Selberg/Vaaler extremal functions (Lemma 6); Maier-Montgomery large sieve Lemma 5 (Lemma 8 here); Landau/Titchmarsh classical bound |zeta(1/2+1/log x+it)|^{-1} << (|t|+2)^{loglog x} (Titchmarsh 14.14.2); standard explicit formula and Stirling

**Techniques.** Perron formula with piecewise-linear contour dependent on local zero-statistics; Selberg-Beurling-Vaaler band-limited majorants/minorants; explicit formula for zero counts in windows; high-moment large sieve over well-spaced points (Maier-Montgomery); Goldston-Gonek bound on S(T) and N(t+h)-N(t); Hadamard factorization/Re zeta'/zeta partial fraction bound; dyadic decomposition and minimal-V selection

## Context and interpretation

**Importance and obstacle overcome.** Reduces the conditional upper bound for M(x) on RH from exp(C(log x)^{39/61}) to exp((log x)^{1/2}(loglog x)^{14}). The obstacle was controlling 1/|zeta| near the critical line along most of the contour; the author replaces a uniform bound by a contour adapted to each unit interval via local typicality and quantifies the rarity of atypical t through a Gaussian-like tail from moments of prime sums.

**Relation to prior work.** Improves Maier-Montgomery (exponent 39/61). Uses Goldston-Gonek's treatment of S(T) and Soundararajan's own large-values paper (Moments of the Riemann zeta function, Annals 2009) as analogue. Conjectural comparators: Gonek-Ng-type conjecture M(x)=O(sqrt x (logloglog x)^{5/4}) as limsup order, Farmer-Gonek-Hughes bound S(t)<<sqrt(log t loglog t).

**Limitations and open questions.** Entirely conditional on RH; says nothing toward proving RH. The tail bound in Thm 2 is far from the expected Gaussian R<<T exp(-C V^2/loglog T); the author states this would improve the result to M(x)<<sqrt x exp(C(loglog x)^3) and notes Thm 2 could be sharpened to the Gaussian shape for V<<(loglog T) logloglog T by adapting [12]; follow-up with Hughes and Ng announced. Even then far from the conjectured size of M(x).

## Research potential

- **Hypotheses that might be weakened.** Thm 2 and Prop 4 use only RH plus Goldston-Gonek input; any unconditional replacement would need zero-density ingredients (e.g. working in a zero-free region sigma>1/2+delta would give classical bounds but not this). Conditions on V range could be loosened by improving Lemma 8 for larger k (currently N^k<=T limits k).
- **Generalizations.** The V-typicality framework should transfer to 1/L(s,chi) for Dirichlet/automorphic L under GRH, giving Mertens-type bounds for sum mu(n)chi(n); also to bounds for sum of Liouville lambda and for sum mu(n)/n type tails. Replace the Selberg minorant by the Carneiro-Vaaler optimal minorants of log|zeta| (as in Chandee-Soundararajan, CAND-01180) to sharpen the exponent 14 on loglog.
- **Candidate connections.** Link with Robin-type arithmetic and signed Mobius cancellation programmes: the M(x)<<sqrt(x)exp(...) bound is the Mobius-cancellation quantitative form equivalent to RH only as x^{1/2+eps}; a gap between sqrt(x) exp((log x)^{1/2+o(1)}) and x^{1/2} is a quantitative reading of Odlyzko-te Riele-style disproof of Mertens (|M(x)|<sqrt x false). Tie with Gonek-Hejhal / Ng large-value conjectures for M(x).
- **Reusable lemmas.** Prop 5 (lower bound for |zeta| near critical line at V-typical points) and Thm 2 (frequency of abnormally dense zero windows on RH) are reusable black boxes; Lemma 10 is a clean smoothed lower bound for log|zeta| in terms of a short prime sum plus F(s).
- **Possible experiments.** Numerically compute for T up to 10^6-10^8 the empirical tail of N(t+h)-N(t)-(h/pi)log(t/2pi) using Odlyzko zero tables and compare to exp(-V log(V/loglog T)) vs Gaussian exp(-C V^2/loglog T); compute minimal V_n of Section 5 and test how large the exponent 14 on loglog x really needs to be.
- **Risks / barriers.** The result is conditional on RH, so it cannot be used as evidence for RH; improvement requires Gaussian-quality tail for large V (V >> loglog T), which needs moments of S(t) and joint zeros statistics far beyond current technology; typicality condition (i) forces x=T^{1/V} small so V cannot be taken below about (loglog T)^2 with this method.

## Audit notes (Level 1 reader)

Prop 5 as stated gives (3) lower bound -V loglog V whereas Lemma 11 proves the stronger -CV; consistent but statement of (3) is weaker than proof (noted by author after Lemma 11). In the proof of Thm 2 the displayed claim 'Ck log log T / (eta^2 V^2)' bound is combined with k=floor(V/(1+eta)); the bookkeeping of the factor (log T)^2 and eta^{-2}=log^2 V is absorbed into the 3V loglog V term but I did not re-derive constants. Section 5's tail (after (13) and the large-V ranges) was only skimmed. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01251`; harvest queries: kw_RH_any, citation_expansion, arxiv_rh_abs, arxiv_zeta_zeros.
- Triage decision: include — Best RH-conditional bound for M(x).
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

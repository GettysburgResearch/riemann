# PAPER-0012 — Moments of the Riemann zeta function

| Field | Value |
|---|---|
| Authors | Soundararajan, Kannan |
| Year / stratum | 2009 / S5 |
| Venue | Ann. Math. (2) 170, No. 2, 981-993 (2009). |
| Identifiers | zbMATH [1251.11058](https://zbmath.org/?q=an:1251.11058) · DOI [10.4007/annals.2009.170.981](https://doi.org/10.4007/annals.2009.170.981) · arXiv [math/0612106](https://arxiv.org/abs/math/0612106) |
| MSC | 11M06, 11M50 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/math/0612106 |
| Selection | score 4.6127, in-pool citations 142, seed lists 2, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Assuming RH, obtain an upper bound for the moments $M_k(T)=\int_0^T|\zeta(1/2+it)|^{2k}dt$ for every real $k>0$ that is nearly of the conjectured order $T(\log T)^{k^2}$, by bounding the measure of the set where $\log|\zeta(1/2+it)|$ is large.

**Historical motivation.** Conjecture M_k(T) ~ C_k T(log T)^{k^2} (Keating-Snaith; Diaconu-Goldfeld-Hoffstein; CFKRS lower terms). Only k=1,2 known; for 0<k<=2 RH upper bounds due to Ramachandra and Heath-Brown. For k>2 Lindelof-type bounds only give T exp(2kC log T/loglog T). Selberg's Gaussian law for log|zeta| in range V ~ sqrt(loglog T) suggested Gaussian tail extends; this paper realizes it conditionally (up to epsilon in exponent).

### Main results

- **THM-PAPER-0012-1** (Corollary A, corollary of Theorem, scope: asymptotic; Sec. 1). Assume RH. For every real $k>0$ and $\epsilon>0$: $T(\log T)^{k^2}\ll_kM_k(T)\ll_{k,\epsilon}T(\log T)^{k^2+\epsilon}$. (Lower bound is Ramachandra's, under RH, for all real k>0.) *Conditional on:* RH.
- **THM-PAPER-0012-2** (Corollary B, corollary, scope: asymptotic; Sec. 1). Assume RH, $k\ge0$ fixed, $T$ large: $\mathrm{meas}\{t\in[0,T]:|\zeta(\tfrac12+it)|\ge(\log T)^k\}=T(\log T)^{-k^2+o(1)}$. *Conditional on:* RH.
- **THM-PAPER-0012-3** (Theorem (main), theorem, scope: asymptotic; Sec. 1, p.3). Assume RH. Let $T$ be large, $V\ge3$, $S(T,V)=\{t\in[T,2T]:\log|\zeta(\tfrac12+it)|\ge V\}$. If $10\sqrt{\log\log T}\le V\le\log\log T$: $\mathrm{meas}\,S(T,V)\ll T\frac{V}{\sqrt{\log\log T}}\exp\Big(-\frac{V^2}{\log\log T}\big(1-\frac4{\log_3T}\big)\Big)$; if $\log\log T<V\le\tfrac12(\log\log T)\log_3T$: $\ll T\frac V{\sqrt{\log\log T}}\exp\Big(-\frac{V^2}{\log\log T}\big(1-\frac{7V}{4(\log\log T)\log_3T}\big)^2\Big)$; if $V>\tfrac12(\log\log T)\log_3T$: $\ll T\exp(-\tfrac1{33}V\log V)$. ($\log_3=\log\log\log$.) *Conditional on:* RH.
- **THM-PAPER-0012-4** (Proposition, proposition (key inequality), scope: asymptotic; Sec. 1 p.3; proved Sec. 2). Assume RH. Let $t\in[T,2T]$, $2\le x\le T^2$, $\lambda_0=0.4912\ldots$ the positive root of $e^{-\lambda}=\lambda+\lambda^2/2$. For all $\lambda\ge\lambda_0$: $\log|\zeta(\tfrac12+it)|\le\mathrm{Re}\sum_{n\le x}\frac{\Lambda(n)}{n^{\frac12+\frac\lambda{\log x}+it}\log n}\frac{\log(x/n)}{\log x}+\frac{(1+\lambda)}2\frac{\log T}{\log x}+O\big(\frac1{\log x}\big)$. *Conditional on:* RH.
- **THM-PAPER-0012-5** (Corollary C, corollary, scope: asymptotic; Sec. 1 p.4). Assume RH. For all large $t$, $|\zeta(\tfrac12+it)|\le\exp\Big(\big(\tfrac{1+\lambda_0}4+o(1)\big)\frac{\log t}{\log\log t}\Big)\le\exp\Big(\frac38\frac{\log t}{\log\log t}\Big)$. (Take $x=(\log T)^{2-\epsilon}$ in the Proposition and bound the sum trivially.) *Conditional on:* RH.
- **THM-PAPER-0012-6** (Sec. 4 families (sketch), theorem sketch (conditional on GRH), scope: asymptotic; Sec. 4). Assuming GRH: for primitive $\chi\bmod q$ ($q$ prime), $\sum^*|L(\tfrac12,\chi)|^{2k}\ll_{k,\epsilon}q(\log q)^{k^2+\epsilon}$ for all real $k>0$; for fundamental discriminants, $\sum^\flat_{|d|\le X}L(\tfrac12,\chi_d)^k\ll_{k,\epsilon}X(\log X)^{k(k+1)/2+\epsilon}$; analogous bounds for quadratic twists of an elliptic curve with exponent $k(k-1)/2+\epsilon$ (sketched). *Conditional on:* GRH.

### Key definitions

- S(T,V)={t in [T,2T]: log|zeta(1/2+it)|>=V}
- lambda_0=0.4912... root of e^{-lambda}=lambda+lambda^2/2
- M_k(T)=int_0^T |zeta(1/2+it)|^{2k} dt
- log_3 = log log log

### Principal lemmas

- **THM-PAPER-0012-L1** (Lemma 1; Sec. 2). Unconditionally, for $s$ not equal to 1 or a zero and $x\ge2$: $-\frac{\zeta'}\zeta(s)=\sum_{n\le x}\frac{\Lambda(n)\log(x/n)}{n^s\log x}+\frac1{\log x}\big(\frac{\zeta'}\zeta\big)'(s)+\frac1{\log x}\sum_\rho\frac{x^{\rho-s}}{(\rho-s)^2}-\frac{x^{1-s}}{(1-s)^2\log x}+\frac1{\log x}\sum_{k\ge1}\frac{x^{-2k-s}}{(2k+s)^2}$. — *Role:* Selberg-type smoothed explicit formula (Titchmarsh 14.20); integrated in sigma to get log|zeta(s_0)|.
- **THM-PAPER-0012-L2** (Lemma 2; Sec. 3). Assume RH, $T\le t\le2T$, $2\le x\le T^2$, $\sigma\ge\tfrac12$: $\sum_{n\le x,\,n\ne p}\frac{\Lambda(n)\log(x/n)}{n^{\sigma+it}\log n\log x}\ll\log\log\log T+O(1)$. — *Role:* Removes prime-square and higher prime powers; uses RH-explicit-formula bound $\sum_{p\le z}(\log p)p^{-2it}\ll z/T+\sqrt z(\log zT)^2$.
- **THM-PAPER-0012-L3** (Lemma 3; Sec. 3). For $T$ large, $2\le x\le T$, $k\in\mathbb N$ with $x^k\le T/\log T$, and complex $a(p)$: $\int_T^{2T}\Big|\sum_{p\le x}\frac{a(p)}{p^{1/2+it}}\Big|^{2k}dt\ll Tk!\Big(\sum_{p\le x}\frac{|a(p)|^2}p\Big)^k$. — *Role:* Mean value theorem for high moments of short Dirichlet polynomials over primes (Gaussian-like moment growth k!).
- **THM-PAPER-0012-L4** (Eq. (4)-(5), Sec. 2; Sec. 2 (4)-(5)). For $t\in[T,2T]$: $-\mathrm{Re}\frac{\zeta'}\zeta(s)=\frac12\log T+O(1)-F(s)$ with $F(s)=\sum_\rho\frac{\sigma-1/2}{(\sigma-1/2)^2+(t-\gamma)^2}\ge0$ (RH); consequently $\log|\zeta(\tfrac12+it)|-\log|\zeta(s_0)|\le(\sigma_0-\tfrac12)\frac{\log T}2+O(1)-\frac{F(s_0)}2$ (using $\log(1+x^2)\ge x^2/(1+x^2)$). — *Role:* Key positivity: zeros near the point only help the upper bound for log|zeta| (the 'benign' effect), enabling a one-sided inequality.

### Proof architecture

Proposition: use RH to get F(s)>=0 and (4); integrate (4) from sigma=1/2 to sigma_0=1/2+lambda/log x to relate log|zeta(1/2+it)| to log|zeta(s_0)| (5); express log|zeta(s_0)| via Lemma 1 integrated in sigma from sigma_0 to infinity (6); add (5) and (6): the coefficient of F(s_0) becomes x^{1/2-sigma0}/((sigma0-1/2)log^2 x) - 1/log x - (sigma0-1/2)/2 which for lambda>=lambda_0 (e^{-lambda}=lambda+lambda^2/2) is <=0, so the zero term can be dropped. Theorem: reduce to primes via Lemma 2; set A and x=T^{A/V}, z=x^{1/loglog T}; split sum into S1 (p<=z) and S2 (z<p<=x). If t in S(T,V) then S2>=V/(8A) or S1>=V(1-7/(8A))=V_1. Bound meas by 2k-th moment: Lemma 3 gives S2 moment << T k!(sum_{z<p<=x}1/p)^k with sum ~ logloglog T (so decays like exp(-(V/2A) log V)); S1 moment << T k!(loglog T)^k... pick k~V_1^2/loglog T for V<=(loglog T)^2 (Gaussian tail exp(-V_1^2/loglog T)) or k=[10V] otherwise. Combine to get Theorem; integrate via (2) (layer-cake formula) to get Corollaries A and B; Corollary C from Proposition with x=(log T)^{2-eps}.

**Imported results.** Selberg's central limit theorem for log zeta (comparison; not used in proof); Ramachandra (RH) lower bound M_k(T) >>_k T(log T)^{k^2} for real k>0; Hadamard factorization (Davenport Ch. 12) and Stirling; Prime number theorem under RH explicit formula (Davenport Ch. 17-18) for Lemma 2; Rudnick-Soundararajan lower bounds for family moments (Sec. 4); Jutila 1983 large deviations for log|zeta| (comparison, unconditional range V<=loglog T)

**Techniques.** Selberg smoothed explicit formula for zeta'/zeta; one-sided inequality via positivity of F(s) under RH (zeros near 1/2+it help); Dirichlet polynomial high-moment mean value (k! growth) with x^k <= T/log T; Chebyshev-type tail bounds via 2k-th moments; layer-cake (distribution function) integration; sharp lambda_0 from e^{-lambda}=lambda+lambda^2/2

## Context and interpretation

**Importance and obstacle overcome.** First upper bound for every real k>0 within T^{o(1)}-power-of-log (exponent k^2+eps) of the conjecture, under RH. Obstacle: Selberg's approach for Re log zeta is hampered by zeros near 1/2+it; the key novelty is the realization that for upper bounds, those zeros help (F>=0), via the Proposition with the exact optimizing constant lambda_0. Also yields explicit Littlewood constant (1+lambda_0)/4 < 3/8 and Corollary B on the measure where |zeta| ~ (log T)^k.

**Relation to prior work.** 

**Limitations and open questions.** RH-conditional; the eps loss in exponent k^2+eps (later removed by Harper 2013 'Sharp conditional bounds for moments of the Riemann zeta function' giving M_k(T)<<_k T(log T)^{k^2}). The Theorem range for V and the 1/33 constant not optimized; the conjectured Gaussian bound (3) is only obtained with the factor (1-4/log_3 T). Unconditional analogue is open (author asks how much can be recovered unconditionally using Selberg zero-density approach). Corollary C constant 3/8 later improved by Chandee-Soundararajan to (log 2)/2 x ... (log 2)/2 for exponent, i.e., exp((log 2/2+o(1)) log t/loglog t).

## Research potential

- **Hypotheses that might be weakened.** RH is used for F(s)>=0 and Lemma 2. A zero-density version (with Selberg zero-free-in-density-sense) might give unconditional bounds for k with exponent loss depending on zero-density constants; Lemma 3 range x^k<=T/log T can be changed by large-sieve-type improvements.
- **Generalizations.** Already sketched for Dirichlet characters, quadratic family (with prime square contribution (1/2)loglog x giving (log X)^{k(k+1)/2}) and quadratic twists of elliptic curves (exponent k(k-1)/2). Extends to other GRH L-functions in families; to moments in short intervals (Arguin-Ouimet-Radziwill), to Dedekind zeta and to joint moments of zeta and its derivative; to Re log in the Selberg class.
- **Candidate connections.** Harper's sharp bound (iteration of this Proposition with refined Euler-product approximation removes the epsilon); Farmer-Gonek-Hughes (CAND-01208) Conj. E predicts tail exp(-2 d^2 log T) at V=d sqrt(log T loglog T) vs this Theorem's third range exp(-V log V/33), showing the distance; Goldston-Gonek (CAND-01222) uses an analogous extremal-function/explicit-formula approach for Im log (S(t)) while this paper handles Re log; CFKRS (CAND-01239) supplies the full-asymptotics target whose leading coefficient (log T)^{k^2} matches Corollary A.
- **Reusable lemmas.** The Proposition (RH one-sided bound for log|zeta| with optimal lambda_0) is directly reusable for any L-function with Hadamard product and Re zero-sum positivity; Lemma 3 (k! mean value for short prime Dirichlet polynomials) is a standard black box.
- **Possible experiments.** Numerically test the Proposition's inequality for random t in [T,2T] at moderate T (compute the prime sum with x=T^{A/V} and compare with log|zeta|) to see slack; verify sharpness of lambda_0 by checking the coefficient of F in (7) numerically; compare empirical meas S(T,V)/T for V up to ~ 2 loglog T with the Theorem's bounds; for families, test the (log X)^{k(k+1)/2} exponent for quadratic Dirichlet L-functions.
- **Risks / barriers.** RH essential; epsilon in k^2+eps arises from the A=(1/2) log_3 T cutoff and the loss in 1/(1-4/log_3 T); removing it requires more careful handling of the transition between primes <= z and <= x (done by Harper). Constants (1/33, 10, 8) are artefacts. Unconditional analogues require handling zeros off the line, which breaks positivity F>=0.

## Audit notes (Level 1 reader)

In the extracted text the hypothesis range of the Theorem prints as '10 log log T <= V <= log log T' (sqrt lost in OCR); the proof section states 'sqrt(loglog T)' explicitly: '10 sqrt(loglog T) <= V <= (3/8)log T/loglog T'. Sec. 3 reduction: 'we may assume 10 sqrt(loglog T) <= V <= (3/8) log T/loglog T' uses Corollary C to exclude larger V. In Sec. 3, the definition of S1 uses exponent 1/2+lambda_0/log x with lambda_0 inside the sum (matching the Proposition). Section 4 sketches are explicitly sketches (no full proofs). Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01201`; harvest queries: kw_RH_any, kw_moments_zeta, msc_11M06, msc_11M50, arxiv_critical_line, arxiv_moments_zeta, arxiv_rh_abs.
- Triage decision: include — Landmark conditional moment upper bounds, basis of later GRH-conditional moment work.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

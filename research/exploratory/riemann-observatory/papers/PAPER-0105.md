# PAPER-0105 — Maxima of a randomized Riemann zeta function, and branching random walks

| Field | Value |
|---|---|
| Authors | Arguin, Louis-Pierre; Belius, David; Harper, Adam J. |
| Year / stratum | 2017 / S6 |
| Venue | Ann. Appl. Probab. 27, No. 1, 178-215 (2017). |
| Identifiers | zbMATH [1362.60050](https://zbmath.org/?q=an:1362.60050) · DOI [10.1214/16-AAP1201](https://doi.org/10.1214/16-AAP1201) · arXiv [1506.00629](https://arxiv.org/abs/1506.00629) |
| MSC | 60G70, 11M06, 60J80, 60G50 |
| Families | B, F |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1506.00629 |
| Selection | score 4.3054, in-pool citations 21, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Verify rigorously the first two terms of the Fyodorov-Hiary-Keating conjecture for the maximum of log|zeta| on a bounded interval of the critical line, for the randomized Euler-product model $\sum_{p\le T}\mathrm{Re}(U_pp^{-ih})p^{-1/2}$, by identifying an approximate branching-random-walk structure.

**Historical motivation.** Fyodorov-Hiary-Keating conjecture (random matrix / log-correlated field heuristics, freezing transition); Farmer-Gonek-Hughes conjecture on max|zeta| over long intervals; Bramson's work on branching Brownian motion; Kistler's multiscale second moment; Harper's earlier result with -2 log log log T <= second order <= -1/4 log log log T.

### Main results

- **THM-PAPER-0105-1** (Theorem 1.2, theorem, scope: asymptotic; Section 1.2, eq. (6); restated (8)-(9) Section 1.4). Let $(U_p,p\text{ primes})$ be i.i.d. uniform on the unit circle. Then $\max_{h\in[0,1]}\sum_{p\le T}\frac{\mathrm{Re}(U_pp^{-ih})}{p^{1/2}}=\log\log T-\tfrac34\log\log\log T+o_P(\log\log\log T)$, i.e. the error divided by $\log\log\log T$ tends to 0 in probability as $T\to\infty$. Equivalently (with $T=e^{2^n}$, $m_n(\varepsilon)=n\log2-\tfrac34\log n+\varepsilon\log n$): $\lim_n\mathbb P(m_n(-\varepsilon)\le\max_{h\in[0,1]}X_n(h)\le m_n(\varepsilon))=1$ for all $\varepsilon>0$.
- **THM-PAPER-0105-2** (Proposition 1.1 (Harper, imported), imported theorem, scope: conditional; Section 1.1, eq. (4); Prop. 1 of Harper [19]). Assume RH. For $T$ large there is $\mathcal H\subseteq[T,T+1]$ of measure $\ge0.99$ with $\log|\zeta(1/2+it)|=\mathrm{Re}\sum_{p\le T}\frac1{p^{1/2+it}}\frac{\log(T/p)}{\log T}+O(1)$ for all $t\in\mathcal H$. *Conditional on:* RH.
- **THM-PAPER-0105-3** (Lemma 2.1, lemma, scope: asymptotic; Section 2.1, eq. (26)-(27)). For $h,h'\in\mathbb R$ and $k\ge1$, with $\sigma^2=(\log2)/2$: $\sigma_k^2=\mathbb E[Y_k(h)^2]=\sigma^2+O(e^{-c2^{k/2}})$, and the covariance $\rho_k(h,h')$ of the scale-$k$ increments equals $\sigma^2$ up to $O(e^{-c 2^{k/2}})$ error when $k\le h\wedge h'$ ($h\wedge h'=\lfloor\log_2|h-h'|^{-1}\rfloor$) and decays like $e^{-2(h\wedge h'-k)}$-type bounds after (as printed; branching-point decorrelation); exact two-sided bounds as in the paper.
- **THM-PAPER-0105-4** (Propositions 2.2 and 2.4, proposition, scope: asymptotic; Section 2.1, (34)-(38)). Large-deviation (tilted measure) control: for $0<\lambda<C$ and $k$ large, the cumulant generating function of the scale-$k$ increment satisfies $\psi_k^{(1)}(\lambda)=\lambda^2\sigma_k^2/2+O(e^{-2^{k-1}})$ (Prop. 2.2) and the tilted law has mean $\lambda\sigma_k^2+O(e^{-2^{k-1}})$, variance $\sigma_k^2+O(e^{-2^{k-1}})$; Prop. 2.4 gives the analogous statement for the pair $(Y_k(h),Y_k(h'))$ with covariance matrix $\Sigma_k$.
- **THM-PAPER-0105-5** (Proposition 3.2 (upper bound), proposition, scope: asymptotic; Section 3, eqs. (72), (77)). For all $\varepsilon>0$ and the truncated process $X_{r,n}=X_n-X_r$: $\lim_{n\to\infty}\mathbb P\big(\max_{h\in[0,1]}X_{r,n}(h)\ge m_{n-r}(\varepsilon)\big)=0$. Proof via a first-moment bound on $Z^+$, the count of exceedances with barrier: $\mathbb P(Z^+>0)\le\mathbb E[Z^+]\le c\,2^r(\log n)^6(n-r)^{-2\varepsilon}$ (Prop. 3.5), using Lemma 3.4 (barrier $X_{r,k}(h)\le(k-r)\mu(\varepsilon)+(\log n)^2$ for all $k$, with high probability).
- **THM-PAPER-0105-6** (Proposition 3.6 (lower bound), proposition, scope: asymptotic; Section 3, eq. (84) and following). For all $\varepsilon>0$: $\lim_{n\to\infty}\mathbb P\big(\max_{h\in[0,1]}X_{r,n}(h)\ge m_{n-r}(-\varepsilon)\big)=1$, proved by the second moment (Paley-Zygmund) on the modified number of exceedances $Z^-=\sum_h\mathbf 1_{J^-(h)}$, where $J^-(h)=\{X_{r,n}(h)\in[m_{n-r}(-\varepsilon),m_{n-r}(-\varepsilon)+\delta],\ X_{r,k}(h)\le(k-r)\mu(-\varepsilon)+1\ \forall k\}$.

### Key definitions

- $X_n(h)=\sum_{p\le e^{2^n}}\mathrm{Re}(U_pp^{-ih})p^{-1/2}$, $h\in[0,1]$
- scale increment $Y_k(h)=\sum_{2^{k-1}<\log p\le2^k}W_p(h)$, $W_p(h)=\mathrm{Re}(U_pp^{-ih})p^{-1/2}$
- $\sigma^2=(\log2)/2$, branching point $h\wedge h'=\lfloor\log_2|h-h'|^{-1}\rfloor$
- $m_n(\varepsilon)=n\log2-\tfrac34\log n+\varepsilon\log n$
- truncated process $X_{r,k}=X_k-X_r$
- barrier-modified exceedance counts $\tilde Z$ / $Z^\pm$

### Principal lemmas

- **THM-PAPER-0105-L1** (Lemma 2.1; Section 2.1, eqs. (26)-(27)). Variance of increments is $\sigma^2=(\log2)/2$ up to $O(e^{-c2^{k/2}})$; covariance equals variance for $k\le h\wedge h'$ and decays after (approximate tree structure). — *Role:* Establishes the approximate branching structure with branching point $h\wedge h'=\lfloor\log_2|h-h'|^{-1}\rfloor$.
- **THM-PAPER-0105-L2** (Lemma 2.12; Section 2 (line ~1057 of text); used in Section 1.4 eq. (18)). Ballot-type estimate: a Gaussian random walk bridge with centred increments ending near the final level avoids a linear barrier with probability of order $1/n$ (probability that bridge from 0 to $m$ stays below the barrier is $\asymp n^{-1}$). — *Role:* Source of the $-\tfrac34\log n$ vs $-\tfrac14\log n$ correction: the barrier costs a factor $n^{-1}$ in the first moment (eq. (18)).
- **THM-PAPER-0105-L3** (Proposition 2.5 / Corollary 2.6 / Lemma 2.7; Section 2.1-2.3). Sharp one-point estimates for the probability that $X_{r,k}$ ends in a window while staying below the barrier (Berry-Esseen comparison with Gaussian random walk after the tilt of Prop. 2.2). — *Role:* First-moment (upper bound) estimates with barrier.
- **THM-PAPER-0105-L4** (Proposition 2.9 / Proposition 2.10 / Proposition 2.11; Section 2). Two-point estimates for $(X(h_1),X(h_2))$: Prop. 2.9 for $m\ge h_1\wedge h_2+\Delta$, Prop. 2.10 for $m\le h_1\wedge h_2-\Delta$ (tilted two-dimensional Gaussian-walk comparisons), and Prop. 2.11 on convex-set probabilities for the 2-D walk. — *Role:* Second-moment estimates (pair of exceedances) on both sides of the branching point; the paper stresses only two points $h_1,h_2$ at a time are needed.
- **THM-PAPER-0105-L5** (Lemma 3.1 / Lemma 3.3; Section 3, eqs. (68)-(73)). Reduction of the full max to $X_{r,n}$ (cutting first r scales): events where $\max X_n\ge m_n(2\varepsilon)$ but $\max X_{r,n}\le m_{n-r}(\varepsilon)$ have vanishing probability (and the reverse for the lower bound); Lemma 3.3 reduces continuum max to a discrete set $H_n\cap[0,1]$ via chaining continuity estimates (Section 2.2). — *Role:* Technical reductions in the proof of Theorem 1.2.
- **THM-PAPER-0105-L6** (Lemma 3.4; Section 3, eq. (75)). For all $\varepsilon>0$, $\lim_n\mathbb P\big(\exists h\in[0,1],k\in\{\lfloor\log n\rfloor^2,\dots,n\}: X_{r,k}(h)>(k-r)\mu(\varepsilon)+(\log n)^2\big)=0$. — *Role:* Establishes the barrier with high probability (union bound over scales and 2^k intervals).
- **THM-PAPER-0105-L7** (Lemma 3.9-3.13; Section 3 (lines ~1396-1700)). Two-point second-moment bounds for $Z^-$ in the regimes $h_1\wedge h_2\le r-\Delta$, $r-\Delta\le h_1\wedge h_2\le r+\Delta$, $r+\Delta<h_1\wedge h_2\le n-\Delta$ and the near-diagonal case. — *Role:* Show $\mathbb E[Z^{-2}]\le(1+o(1))\mathbb E[Z^-]^2$ giving Paley-Zygmund lower bound.

### Proof architecture

Model: with T=e^{2^n}, X_n(h)=sum_{p<=e^{2^n}} Re(U_p p^{-ih})/sqrt p decomposed into scale increments Y_k(h) (primes with 2^{k-1}<log p<=2^k), each with variance sigma^2=(log2)/2. Lemma 2.1: increments nearly identical for h,h' before branching point h^h'=floor(log_2|h-h'|^{-1}) and nearly independent after, giving an approximate binary-tree BRW with 2^n leaves. Naive first moment 2^n P(X_n>=m) fails for m=n log2 - (3/4) log n (it gives -(1/4) log n, equal to the independent heuristic); the fix is a barrier: with high probability X_k(h) < k log2 + B for all k (Lemma 3.4, union bound over 2^k points). First moment with barrier = 2^n P(X_n>m) * P(walk bridge stays below barrier | X_n>m) with the second factor ~1/n (ballot theorem, Lemma 2.12) giving E[Z~]=O(n^{-eps}), hence upper bound (Prop 3.5). Lower bound: second moment (Paley-Zygmund) of Z~ (barrier-modified count; first r scales cut: X_{r,k}=X_k-X_r) with two-point estimates (Props 2.9-2.11, Lemmas 3.9-3.13) separated into the regimes before/after the branching point; a Berry-Esseen comparison with an exact Gaussian BRW (Lemma 2.8, Berry-Esseen type, Cor. 17.2 in Bhattacharya-Rao) plus exponential tilting Q_lambda; chaining estimates (Section 2.2) pass from discrete grid to continuum. Only first and second moments (at most two walks simultaneously) are used. Proposition 1.1 (Harper) is NOT used in the proof of Thm 1.2; it only motivates the model.

Dependency edges: CAND-01996 → Harper 2013 (Prop. 1, model justification, RH-conditional) (motivated by (model); improves model result); CAND-01996 → Fyodorov-Hiary-Keating conjecture (proves analogue for the random model); CAND-01996 → Kistler multiscale second moment (applies); CAND-01996 → Bramson / BRW barrier methods (adapts)

**Imported results.** Harper (2013), Proposition 1 (RH): log|zeta| approximated by a short prime sum on a large set (motivation only, not used in the proof of Thm 1.2); Berry-Esseen type result: Lemma 2.8 (Cor. 17.2 in Bhattacharya-Rao; Theorem 1.3 in [17]); Ballot theorem / random walk barrier estimates (Lemma 2.12); Prime number theorem with error terms (Lemma 2.1 inputs); Selberg central limit theorem (heuristic only); Paley-Zygmund inequality

**Techniques.** approximate branching random walk / multiscale decomposition (Kistler multiscale second moment); barrier (ballot theorem) argument for first moment; Paley-Zygmund inequality with truncated count; exponential tilting (Cramer-type change of measure); Berry-Esseen Gaussian approximation; chaining continuity estimates; prime number theorem-type estimates for sums over primes; Gaussian comparison/large deviations

## Context and interpretation

**Importance and obstacle overcome.** First rigorous proof of the log log log T coefficient -3/4 for a model of zeta, confirming the BRW (log-correlated) heuristic and explaining the extra -1/2 log log log T relative to independent Gaussians (-1/4 log log log T); the obstacle is the strong correlations of nearby h (naive second moment fails to leading order), overcome by the barrier/ballot-theorem trick adapted from Bramson-type arguments to a process with only approximate tree structure.

**Relation to prior work.** Improves Harper [19], who proved the leading term log log T and showed the second-order term lies in [-2,-1/4] times log log log T for this model, using a Gaussian comparison needing log T points; the new proof only needs two points at a time. Uses Kistler's multiscale method (applied to cover times on 2D torus by Cortines-Louidor-Saglietti? [5]) and Bramson's BRW techniques.

**Limitations and open questions.** Result is for a random model (independent uniform $U_p$), not for zeta itself; error term is $o_P(\log\log\log T)$, so only the first two terms are determined (the FHK conjecture states $O_P(1)$, not proved even for the model here). The conjecture for zeta itself remains open; the authors note their approach needs only two-point control, which could feasibly be achieved for zeta. Harper's Prop. 1.1 needs RH. The conjecture for the characteristic polynomial of CUE is not rigorously known even to leading order at the time of writing. Open: tightness of maximum around its median (O_P(1)), distribution of the maximum.

## Research potential

- **Hypotheses that might be weakened.** Model is i.i.d. uniform U_p; replace by pseudo-random or equidistributed twists p^{-i tau} (tau uniform on [0,T]) using moment estimates (only two-point control needed per the authors); remove the o_P(log log log T) error to O_P(1) (later work of Arguin-Ouimet and others) by sharpening the ballot/second moment steps.
- **Generalizations.** Other log-correlated fields from Euler products: Dirichlet L-functions L(1/2+it,chi) in a family, characteristic polynomials of CUE (via Euler-product model), Selberg-class degree-d L-functions (variance scales with degree); maxima over longer intervals ([0,T^theta]) with different log-correlation.
- **Candidate connections.** Relevant to the Riemann Observatory 'moment/large values' branch: Lindelof-type upper bounds (RH implies max|zeta|<<exp(C log T/loglog T)) vs. the bounded-interval max exp(loglog T - 3/4 logloglog T); connects with Harper's RH-conditional Prop. 1 (so full transfer to zeta requires RH in Harper's input); also with Radziwill (CAND-01416) only via shared use of Selberg-type Dirichlet polynomials.
- **Reusable lemmas.** Lemma 2.1 (approximate tree structure of Euler products), Lemma 3.4 (barrier by union bound over scales), Lemma 2.12 (ballot estimate) and Props 2.9-2.11 (two-point tilted estimates) are reusable for any prime-indexed log-correlated field.
- **Possible experiments.** Numerically sample the model X_n(h) for n up to ~15 (primes up to e^{2^15}) and fit max - n log 2 + 0.75 log n to check the -3/4 coefficient; compare with actual zeta data on [T,T+1] for T about 1e6-1e9 (Fyodorov-Hiary-Keating numerics) to see finite-n correction sizes.
- **Risks / barriers.** Transfer to actual zeta requires controlling the joint law of p^{-i tau} at two heights for all primes up to T (moments) and Harper's RH-conditional Euler-product approximation (Prop 1.1); an unconditional version would need a substitute for Prop 1.1 near zeros; note that zeta near its zeros is not captured and the max statistics could be affected by 'abnormally close to zeros' set outside H.

## Audit notes (Level 1 reader)

Lemma 2.1: my transcription of the covariance bound after the branching point is from garbled text (extraction shows 'e^{-2(h^h'-k)}' pieces); treat my inline exponent as approximate and consult eq. (27) in the paper. Section 1.4: the text writes P(X_n(0)>=m) approximated as 'm e^{-m^2/(log2)n}' (extraction garbled; presumably n^{1/2}/m e^{-m^2/((log 2) n)}). Also reference attribution '[5] cover times on the 2D torus' mentions authors I did not verify in my record. Otherwise none noticed in inspected portion; proofs of Props 2.x and 3.x not verified.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01996`; harvest queries: msc_11M06, arxiv_critical_line.
- Triage decision: include — Randomized zeta maximum via branching random walk, supports FHK.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

# PAPER-0015 — Extreme values of the Riemann zeta function and its argument

| Field | Value |
|---|---|
| Authors | Bondarenko, Andriy; Seip, Kristian |
| Year / stratum | 2018 / S6 |
| Venue | Math. Ann. 372, No. 3-4, 999-1015 (2018). |
| Identifiers | zbMATH [1446.11153](https://zbmath.org/?q=an:1446.11153) · DOI [10.1007/s00208-018-1663-2](https://doi.org/10.1007/s00208-018-1663-2) · arXiv [1704.06158](https://arxiv.org/abs/1704.06158) |
| MSC | 11M06 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1704.06158 |
| Selection | score 4.6105, in-pool citations 31, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** How large can |zeta(1/2+it)| (unconditionally) and S(t), S_1(t) (under RH) be, via Bondarenko-Seip long-resonator method combined with convolution (smoothing) formulas for zeta and log zeta, so that the pole of zeta no longer obstructs the range T^beta<=t<=T for all 0<=beta<1? Note: the main lower bound carries an extra log_3 factor (sqrt(log T log_3 T / log_2 T)) that the triage summary omitted.

**Historical motivation.** Montgomery's RH Omega_pm for S(t) of size (log t/log log t)^{1/2} and his heuristic that it is optimal vs Farmer-Gonek-Hughes' sqrt(log t log log t) prediction; Soundararajan's resonance method and Bondarenko-Seip's long resonators gave exp(c sqrt(log T log_3T/log_2T)) with c<1/sqrt2.

### Main results

- **THM-PAPER-0015-1** (Theorem 1, theorem, scope: asymptotic; Intro, Thm 1 (p.1); proof Sec. 4 (pp.12-14)). Let $0\le\beta<1$ and $0<c<\sqrt{1-\beta}$. For all sufficiently large $T$ there is $t\in[T^\beta,T]$ with $|\zeta(\tfrac12+it)|\ge\exp\Big(c\sqrt{\tfrac{\log T\,\log\log\log T}{\log\log T}}\Big)$. In particular $\max_{1\le t\le T}|\zeta(1/2+it)|\ge\exp\big((1+o(1))\sqrt{\log T\log_3T/\log_2T}\big)$ (constant improved from $1/\sqrt2$ in Bondarenko-Seip [2] to $1$).
- **THM-PAPER-0015-2** (Theorem 2 (4), theorem, scope: conditional; Thm 2 (p.3); proof Sec. 5 (pp.14-15)). Assume RH, fix $0\le\beta<1$. There is $c>0$ with $\max_{T^\beta\le t\le T}|S(t)|\ge c\sqrt{\log T\,\log_3T/\log_2T}$ for all large $T$, where $S(t)=\frac1\pi\arg\zeta(1/2+it)$. *Conditional on:* RH.
- **THM-PAPER-0015-3** (Theorem 2 (5), theorem, scope: conditional; Thm 2 (p.3); proof Sec. 5 (via formula (10), even kernel)). Assume RH, fix $0\le\beta<1$. There is $c_1>0$ with $\max_{T^\beta\le t\le T}S_1(t)\ge c_1\sqrt{\log T\,\log_3T/(\log_2T)^3}$, where $S_1(t)=\int_0^tS(\tau)d\tau$. *Conditional on:* RH.
- **THM-PAPER-0015-4** (Lemma 1, lemma, scope: global; Sec. 2, eq (6)). For $1/2\le\sigma<1$ and $K$ analytic in the strip $\sigma-2\le y\le0$ with $\max|K(x+iy)|=O(|x|^{-2})$: $\int_{\mathbb R}\zeta(\sigma+i(t+u))K(u)\,du=\sum_{n\ge1}\hat K(\log n)n^{-\sigma-it}+2\pi K(-t-i(1-\sigma))$.

### Key definitions

- Resonator $R(t)=\sum_{m\in\mathcal M'}r(m)m^{-it}$, $r(m_j)=(\sum_{n\in\mathcal M,(1-T^{-1})^{j-1}\le n\le(1+T^{-1})^{j+2}}f(n)^2)^{1/2}$
- $f$ multiplicative supported on squarefree n with $f(p)=\sqrt{\frac{\log N\log_2N}{\log_3N}}\frac1{\sqrt p(\log p-\log_2N-\log_3N)}$ for $p\in P$
- $S(t)=\frac1\pi\arg\zeta(1/2+it)$, $S_1(t)=\int_0^tS$
- $\log_kx$ iterated logarithm

### Principal lemmas

- **THM-PAPER-0015-L1** (Lemma 2 (Selberg; Tsang Lemma 5); Sec. 2, (7)-(10)). For $1/2\le\sigma<1$, K analytic in strip with $V(x)=\max|K|=O(1/(|x|\log^2|x|))$, $t\ne0$: $\int\log\zeta(\sigma+i(t+u))K(u)du=\sum_{n\ge2}\frac{\Lambda(n)}{\log n}\hat K(\log n)n^{-\sigma-it}+2\pi\sum_{\beta>\sigma}\int_0^{\beta-\sigma}K(\gamma-t-i\alpha)d\alpha+O(V(t))$; under RH the zero sum vanishes, giving (8),(9),(10) for S and S_1. — *Role:* Imported convolution formula for log zeta; makes the RH-dependence of Theorem 2 explicit (only through absence of zeros right of sigma).
- **THM-PAPER-0015-L2** (Lemma 3; Sec. 3 p.7). The resonator support set $\mathcal M$ (squarefree numbers with few prime divisors in each prime block $P_k$) satisfies $|\mathcal M|\le N$ for N large. — *Role:* Size control of resonator (imported from [2, Lemma 2]).
- **THM-PAPER-0015-L3** (Lemma 4; Sec. 3 pp.8-9, (12)-(16)). $\frac1{\sum_i f(i)^2}\sum_{n\in\mathcal M}f(n)^2\sum_{p|n}\frac1{f(p)\sqrt p}\ge(\gamma+o(1))\sqrt{\log N\log_3N/\log_2N}$. — *Role:* Key combinatorial estimate: concentration of the multiplicative weight f^2 on integers with many prime factors in every block; yields the sqrt factor and the improved constant.
- **THM-PAPER-0015-L4** (Lemma 5; Sec. 3 p.10). $\int|R(t)|^2\Phi(t/T)dt\ll T\sum_{n\in\mathcal M}f(n)^2$ with $R(t)=\sum_{m\in\mathcal M'}r(m)m^{-it}$, $\Phi(t)=e^{-t^2/2}$. — *Role:* Upper bound for resonator mass (diagonal vs off-diagonal via discretisation at scale 1+1/T).
- **THM-PAPER-0015-L5** (Lemma 6; Sec. 3 p.11, (23)). If $F(t)=\sum a_nn^{-1/2-it}$ converges absolutely with $a_n\ge0$, then $\int F|R|^2\Phi(t/T)dt\ge T\min_{n\le T^\epsilon}a_n\exp\big((\gamma+o(1))\kappa\sqrt{\log T\log_3T/\log_2T}\big)\sum_{\mathcal M}f(n)^2$ (as printed; the sqrt scaling with kappa=log N/log T should apply to the kappa factor). — *Role:* Resonance lower bound for nonnegative Dirichlet series (used with F built from the kernel transform).
- **THM-PAPER-0015-L6** (Lemma 7; Sec. 3 p.11, (24)). For $G(t)=\sum_{n\ge2}\frac{\Lambda(n)a_n}{\log n}n^{-1/2-it}$, $a_n\ge0$: $\int G|R|^2\Phi(t/T)dt\ge cT\sqrt{\log T\log_3T/\log_2T}\min_{p\in P}a_p\sum_{\mathcal M}f(n)^2$. — *Role:* Prime-supported version used for S(t), S_1(t); the sqrt gain comes from Lemma 4.

### Proof architecture

Choose a kernel K with compactly supported Fourier transform (Thm 1: K(t)=sin^2((eps log T)t)/((eps log T)t^2), \hat K = (pi/2)max(1-|xi|/(2 eps log T),0)); replace the approximation zeta=sum n^{-1/2-it}-T^{1/2-it}/(1/2-it) by Lemma 1, so the pole contributes only the harmless term 2pi K(t-i/2). Average |zeta|*K against the resonator weight |R(t)|^2 Phi(t/T) with R built from the Bondarenko-Seip multiplicative f on squarefree integers with primes in (e log N log_2 N, log N exp((log_2N)^gamma) log_2 N]; N=T^kappa, kappa<1-beta. Trivial bound |R|<=R(0) kills the tails/pole term and Hardy-Littlewood second moment controls the off-range; Lemma 5 gives an upper bound for the resonator mass, Lemma 6 a lower bound for the main nonnegative Dirichlet series F(t)=sum \hat K(log n) n^{-1/2-it}, hence a point t with |zeta|>=exp(...) after shrinking T by 2 log T. For Theorem 2 use RH to kill zero terms in Selberg's formula (Lemma 2), choose K odd (S) or even (S_1, via Tsang's formula with bounded correction h(t)), and Lemma 7 for the prime sum; only positive real parts of nonnegative-coefficient series are detectable, which blocks Omega_- results.

**Imported results.** Hardy-Littlewood second moment of zeta; Selberg's second moment bound for S(t); Selberg/Tsang convolution formula for log zeta (Tsang [10, Lemma 5]); Bondarenko-Seip [2, Lemma 2] resonator size and mass estimates; Theorem 9.9 of Titchmarsh/Heath-Brown: h(t)=S_1(t)-(1/pi)int_{1/2}^2 log|zeta(sigma+it)|dsigma bounded (under RH)

**Techniques.** resonance method (Soundararajan) with long resonator on large primes; multiplicative resonator coefficients on block-structured squarefree integers; convolution formulas for zeta and log zeta (Selberg, Tsang); kernels with compactly supported Fourier transform; Hardy-Littlewood second moment, Cauchy-Schwarz; discretisation of resonator at scale 1+1/T

## Context and interpretation

**Importance and obstacle overcome.** Best-known unconditional Omega result for the maximum of |zeta(1/2+it)| (constant 1 in the exponent) and first strengthening of Montgomery's RH Omega for S(t). The obstacle was the pole term T^{1/2-it}/(1/2-it) in the approximate formula, which restricted resonator length to beta>=1/2; convolution against a smooth kernel makes the pole negligible for all beta in [0,1).

**Relation to prior work.** Strengthens the main theorem of Bondarenko-Seip [2] (Math. Ann.? Bull. LMS 2017, c<1/sqrt2) to c<sqrt(1-beta) and covers all beta in [0,1); uses Selberg [7] and Tsang [10,11] convolution formulas; supersedes Tsang's Omega for S under RH in the exponent form.

**Limitations and open questions.** No measure estimate for the set where large values occur (contrast Soundararajan). Method only catches large positive values of real part of nonnegative-coefficient Dirichlet series: no Omega_pm for S(t), no Omega_- for S_1(t). Intervals T^beta<=t<=T are long. Unconditional Omega for S_1 left open (authors suggest a stronger measure result). Gap between this Omega bound exp(c sqrt(log T log_3T/log_2T)) and Littlewood's RH upper bound exp(C log T/log_2T) remains; Farmer-Gonek-Hughes conjecture sqrt(log T log_2 T) for max log|zeta| is untouched.

**Ideas in remarks/appendices/abandoned paths.** Remark (p.4): conditional Omega_+ for S_1 of size (log T)^{1/2}(log_2 T)^{-3/2 -ish} follows directly from earlier work [3] via the explicit formula for log|zeta| and integration by parts with sigma=1/2+1/log_2 t. Remark (p.4): the authors can adapt Soundararajan's measure result and Tsang's argument to reprove Tsang's unconditional Omega_+ for S_1; a stronger measure theorem for larger values would give (5) unconditionally.

## Research potential

- **Hypotheses that might be weakened.** RH in Thm 2 enters only via vanishing of the sum over zeros with beta>sigma in Lemma 2 (7); a zero-density input could give an unconditional S_1 or S bound in a restricted range. Condition c<sqrt(1-beta) comes from N=T^kappa, kappa<1-beta, and the bound R(0)^2 in the tail: a non-trivial treatment of the tail could enlarge kappa.
- **Generalizations.** Lemma 1 holds for any L-function with convolution formula (Dirichlet L, Hecke); the resonator Lemmas 4-7 are formal in nonnegative coefficients, so Omega results for L(1/2+it,chi) in t-aspect and for degree-d L-functions follow if second moments are known. Also relevant to extreme values of zeta in other half-plane strips sigma>1/2.
- **Candidate connections.** Compare with Arguin-Belius-Bourgade-Radziwill-Soundararajan (CAND-01957): typical-short-interval max is log log T while resonator gives sqrt-scale global max; both inform the Farmer-Gonek-Hughes vs Littlewood dispute. Resonator weights |R|^2 as a positive kernel relate to the positivity/heat-flow viewpoint (Polymath15, CAND-01890).
- **Reusable lemmas.** Lemma 1 (convolution formula for zeta with pole term explicit) and Lemma 4 (resonator concentration estimate) are standalone tools.
- **Possible experiments.** Numerically compute the resonator ratio int F|R|^2/int |R|^2 for moderate N to test the sqrt(log N log_3 N/log_2 N) gain; test whether the optimal resonator on a block structure with gamma<1 can be improved by optimising the prime-range exponent gamma (Lemma 4 constant gamma+o(1)).
- **Risks / barriers.** Square-root-of-log scale looks intrinsic to long-resonator with log N<=log T; reaching exp(c log T/log_2T) (Littlewood's order) would need a different amplifier. Positivity restriction is structural.

## Audit notes (Level 1 reader)

Minor extraction/typographic points in inspected portion: Lemma 6 as printed shows exp((gamma+o(1)) kappa sqrt(...)) but the proof of Thm 1 and the final c<sqrt(1-beta) require sqrt(kappa) scaling (consistent with Lemma 4 for N=T^kappa); likely a lost radical in text extraction or a typo. Final step 'changing T to T/(2 log T) and making beta slightly smaller' is stated without detail. Triage summary omitted the log_3 factor. Otherwise none noticed.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01786`; harvest queries: kw_RH_any, msc_11M06, arxiv_rh_abs.
- Triage decision: include — Resonance method gives record Omega results for zeta and arg zeta.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

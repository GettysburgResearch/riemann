# PAPER-0051 — Zero-free regions for the Riemann zeta function.

| Field | Value |
|---|---|
| Authors | Ford, Kevin |
| Year / stratum | 2002 / S5 |
| Venue | Bennett, M. A. (ed.) et al., Number theory for the millennium II. Proceedings of the millennial conference on number theory, Urbana-Champaign, IL, USA, May 21--26, 2000. Natick, MA: A K Peters (ISBN 1-56881-146-2/hbk). 25-56 (2002). |
| Identifiers | zbMATH [1034.11045](https://zbmath.org/?q=an:1034.11045) · arXiv [1910.08205](https://arxiv.org/abs/1910.08205) |
| MSC | 11M06, 11M26 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arXiv:1910.08205 (v5, 18 Feb 2025, with corrections to the 2002 published version) |
| Selection | score 4.5594, in-pool citations 26, seed lists 3, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Give explicit constants in Vinogradov-Korobov zero-free regions for zeta, given an explicit bound |zeta(sigma+it)|<=A|t|^{B(1-sigma)^{3/2}}log^{2/3}|t|, and a fully explicit region for all |t|>=3.

**Historical motivation.** Popov c=6.9e-5, Heath-Brown c~0.0269B^{-2/3}, Cheng c=1/990; Ford improved the constant as function of B.

### Main results

- **THM-PAPER-0051-1** (Theorem 1, theorem (conditional on (1.2)), scope: asymptotic; p.1). If $|\zeta(\sigma+it)|\le A|t|^{B(1-\sigma)^{3/2}}\log^{2/3}|t|$ ($|t|\ge3$, $1/2\le\sigma\le1$) holds with constant B, then for $|t|$ large, $\zeta(\beta+it)\ne0$ when $1-\beta\le \dfrac{0.05507B^{-2/3}}{(\log|t|)^{2/3}(\log\log|t|)^{1/3}}$. *Conditional on:* (1.2); with B=4.45 (Ford's companion paper) gives c=1/49.13.
- **THM-PAPER-0051-2** (Theorem 2, theorem, scope: asymptotic; p.2). Suppose (1.2) holds with $0<B<10$, $A\ge1$, $T_0\ge e^{30000}$, $\log T_0/\log\log T_0\ge1740/B$ (as printed), and all zeros $\beta+it$ with $T_0-1\le t\le T_0$ satisfy $1-\beta\ge M_1B^{-2/3}(\log t)^{-2/3}(\log\log t)^{-1/3}$, where $M_1=\min\{0.05507,\,0.1652/(2.9997+\max_{t\ge T_0}X(t)/\log\log t)\}$ and $X(t)=1.1582\log A+0.8332+0.234\log(B/\log\log t)+(1.239B^{-4/3}-2.065B^{-1/3})(\log\log t/\log t)^{1/3}$. Then the same bound holds for all zeros with $t\ge T_0$.
- **THM-PAPER-0051-3** (Theorem 3, theorem (uses RH-verification to height 5.45e8 and Cheng-Graham-type bound (1.6)), scope: global; p.3). With $T_0=5.45\times10^8$, $J(t)=\min(\tfrac14\log t+1.8521,\tfrac16\log t+\log\log t+\log3)$, $\zeta(\beta+it)\ne0$ for $t\ge T_0$ and $1-\beta\le\frac{0.04962-c_6(t)}{J(t)+0.155\log\log t+0.675}$, with $c_6(t)$ given by (1.8)-(9.9).
- **THM-PAPER-0051-4** (Theorem 4, theorem, scope: global; p.3). $\zeta(\beta+it)\ne0$ for $|t|\ge3$ and $1-\beta\le\frac1{8.464\log|t|}$.
- **THM-PAPER-0051-5** (Theorem 5, theorem, scope: global; p.3). $\zeta(\beta+it)\ne0$ for $|t|\ge3$ and $1-\beta\le \dfrac1{57.54(\log|t|)^{2/3}(\log\log|t|)^{1/3}}$ (uses A=76.2, B=4.45 from companion paper and T_0=e^{54550}).

### Key definitions

- (1.2) Richert-type bound with constants A,B
- zero detector (Lemma 2.2)
- J(t), M_1, X(t), c_6(t)

### Principal lemmas

- **THM-PAPER-0051-L1** (Lemma 2.2; Sec. 2). For f a quotient of entire functions of finite order, no zero/pole at z_0, 0, and a.e. $\eta>0$: $-\Re\frac{f'(z_0)}{f(z_0)}\cdot\frac{\pi}{2\eta}=\sum_{|\Re(z_0-\rho)|\le\eta}m_\rho\Re\frac{\pi}{2\eta}\cot\frac{\pi(\rho-z_0)}{2\eta}+\frac1{4\eta}\int_{-\infty}^\infty[\log f(z_0-\eta+\tfrac{2\eta iu}{\pi})-\log f(z_0+\eta+\tfrac{2\eta iu}{\pi})]\cosh^{-2}u\,du$ (exact normalisation as printed in paper; text OCR garbled) — *Role:* main 'zero detector': integrates over two vertical lines instead of a circle, replacing Heath-Brown's Lemma 3.2
- **THM-PAPER-0051-L2** (Lemma 5.1; Sec. 5). For real $a_1,a_2$, $b_j$ per (5.2) and any $\eta>0,t_1,t_2$: $\int_{-\infty}^\infty\cosh^{-2}u\sum_{j=1}^4 b_j\log|\zeta(1+\eta+ijt_1+iut_2)|du\ge-2b_0\log\zeta(1+\eta)$ — *Role:* combines the log|zeta| terms via a trigonometric-polynomial positivity (5.1) instead of the trivial |zeta|>=1/zeta(sigma); main source of improvement over Heath-Brown
- **THM-PAPER-0051-L3** (Lemma 4.1; Sec. 4). Under (1.2), for $0<\eta<\pi/4$, $\sigma-\eta\ge1/2$, $1\le\sigma\le1+\eta$, $t\ge100$: $-\Re\zeta'/\zeta(s)\le-\sum_{\rho\in S}\Re\frac\pi{2\eta}\cot\frac{\pi(s-\rho)}{2\eta}+\frac1{2\eta}(\tfrac23\log\log t+B(1-\sigma+\eta)^{3/2}\log t+\log A)-\frac1{4\eta}\int\frac{\log|\zeta(s+\eta+2\eta iu/\pi)|}{\cosh^2u}du$ — *Role:* upper bound for -Re zeta'/zeta using zero detector
- **THM-PAPER-0051-L4** (Lemma 7.1; Sec. 7). For $t\ge10000$, $\zeta(\beta+it)=0$, (6.1), (1.2), $1-\beta\le\eta/2$, $\eta\le1/4$, $0<\lambda\le\min(1-\beta,\eta/250)$: $\frac1\lambda(0.16521-0.1876(\frac{1-\beta}\lambda-1))\le1.471\ldots$ (as printed; inequality garbled by OCR) — *Role:* key inequality linking real part of a zero to eta, optimized in Sec. 8
- **THM-PAPER-0051-L5** (Lemma 3.3; Sec. 3). $\sum_\rho|\rho|^{-2}\le0.0463$ over nontrivial zeros; proof uses $\sum\Re\rho/|\rho|^2=1+\gamma/2-\log(4\pi)/2$ (as printed) and zeros on the critical line for $|\Im\rho|\le5.45\times10^8$. — *Role:* bounds contribution of far zeros
- **THM-PAPER-0051-L6** (Lemma 3.4; Sec. 3). If $|\zeta(\sigma+iy)|\le Xt^Y(\log t)^Z$ for $1\le|y|\le t$ ($Y+Z\ge0.1$) then for $0<a\le1/2$, $t\ge100$, $1/2\le\sigma\le1-1/t$: $\int\frac{\log|\zeta(\sigma+it+iau)|}{\cosh^2u}du\le2(\log X+Y\log t+Z\log\log t)$. — *Role:* bounds the log-integral term
- **THM-PAPER-0051-L7** (Lemma 9.1-9.2; Sec. 9). Variants of the above for $t\ge5.45\times10^8$ using $J(t)$ from (1.6), giving (9.8) for $1-\beta\le1/160$. — *Role:* small-height (classical) zero-free region Theorem 3-4

### Proof architecture

Heath-Brown-type argument: assume zeta(beta+it)=0 near the Vinogradov-Korobov edge. Zero detector Lemma 2.2 (two vertical lines) converts -Re zeta'/zeta at a point 1+eta-ish into a sum over zeros in a strip plus log-integrals of zeta on the two lines. Upper side uses (1.2) via Lemma 3.4/4.1; lower side uses Lemma 5.1 (trigonometric polynomial positivity at 1+eta+ijt) rather than trivial 1/zeta(sigma). Combine at s=sigma+it with sigma slightly above 1 for several shifts, optimize parameters (Sec. 6-8) to get Lemma 7.1 and Theorem 2. Sec. 9 treats moderate t via Theorem 3 using RH-verification to 5.45e8 and bounds for |zeta(1/2+it)|; Theorem 5 patches regimes at T_0=e^{54550}.

Dependency edges: CAND-01233 → CAND-01368 (depends on (supplies B=4.45, A=76.2))

**Imported results.** Ford 2002 Theorem 1: (1.2) with B=4.45, A=76.2 (companion paper arXiv 1910.08209); Platt-Trudgian/[15]: RH verified to height 5.45e8; Hiary-Patel-Yang |zeta(1/2+it)|<=0.618|t|^{1/6}log|t|; Lehman |zeta(1/2+it)|<=4(t/2pi)^{1/4}; Stechkin classical zero-free region 1/9.646; zero density bound O(T^{1-delta}) (Titchmarsh Ch 9); Hadamard product theory

**Techniques.** Heath-Brown zero detector with vertical-line contour; cosh^{-2} weighted Jensen/Poisson-type integral; trigonometric polynomial positivity (3+4cos+cos2-type) with extra free parameters a_1,a_2; explicit Hadamard product estimates; numerical optimisation of parameters

## Context and interpretation

**Importance and obstacle overcome.** Gave the best explicit Vinogradov-Korobov zero-free region with c=1/57.54 valid for all |t|>=3, usable in explicit prime-number-theorem error terms. New trick: Lemma 5.1 avoiding wasteful lower bound on |zeta(1+eta+it)|.

**Relation to prior work.** Direct refinement of Heath-Brown's explicit zero-free region method; uses Ford's companion bound on zeta; supersedes Cheng 1/990 and Stechkin-type for large t.

**Limitations and open questions.** Region still Vinogradov-Korobov shape; improvement over Heath-Brown ~17% in constant; classical-type region for all |t|>=3 not improved over Heath-Brown. Further improvements depend on better B or verification of RH to larger height. Published version corrected in 2025 (footnote on Cheng-Graham Lemma 3 error).

## Research potential

- **Hypotheses that might be weakened.** Hypothesis (1.2) enters only through Lemma 3.4/4.1 integral bound; any improved B directly feeds Theorem 1 (c ~ 0.05507 B^{-2/3}). Higher RH verification height T_0 improves Theorem 4 constant 8.464.
- **Generalizations.** Explicit zero-free regions for Dirichlet L-functions with fixed conductor and large t (paper says method improves there); Dedekind zeta.
- **Candidate connections.** Explicit PNT error terms, explicit bounds on sums over zeros (Lemma 3.3 type), computational verification of RH to larger heights.
- **Reusable lemmas.** Lemma 2.2 (two-line zero detector) and Lemma 5.1 (positivity trick) as reusable tools.
- **Possible experiments.** Re-optimise the parameters (a_1,a_2,eta,lambda) with a rigorous interval-arithmetic implementation to certify Theorem 2 constants; recompute Theorem 4 using Lehman's bound and extended RH verification height.
- **Risks / barriers.** Vinogradov-Korobov exponent 2/3 barrier; no approach to RH (does not touch critical line).

## Audit notes (Level 1 reader)

Hypothesis in Theorem 2 'log T_0/ log log T_0 >= 1740/B' is garbled in OCR; check against PDF. The paper's own footnote records an error in the cited Cheng-Graham bound (1.6) and a v5 correction; Theorem 3/4 numerical statements depend on corrected inputs. No other issues noticed.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01233`; harvest queries: kw_zero_free, msc_11M06, msc_11M26, arxiv_zero_free.
- Triage decision: include — Standard explicit Vinogradov-Korobov zero-free region.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

# PAPER-0020 — Explicit bounds for the Riemann zeta function and a new zero-free region

| Field | Value |
|---|---|
| Authors | Bellotti, Chiara |
| Year / stratum | 2024 / S7 |
| Venue | J. Math. Anal. Appl. 536, No. 2, Article ID 128249, 33 p. (2024). |
| Identifiers | zbMATH [1552.11100](https://zbmath.org/?q=an:1552.11100) · DOI [10.1016/j.jmaa.2024.128249](https://doi.org/10.1016/j.jmaa.2024.128249) · arXiv [2306.10680](https://arxiv.org/abs/2306.10680) |
| MSC | 11M06, 11L15, 11M26, 11L07 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/2306.10680 |
| Selection | score 4.6065, in-pool citations 6, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Improve Ford's explicit Richert-type bound |zeta(sigma+it)|<=A|t|^{B(1-sigma)^{3/2}}log^{2/3}|t| (reducing A and B) by sharpening explicit Vinogradov mean value bounds and parameter choices, and feed this into MTY's machinery to enlarge the Korobov-Vinogradov zero-free region.

**Historical motivation.** Richert (B=100), Cheng (A=175,B=46), Ford (A=76.2,B=4.45) gave successive explicit versions; Ford predicted (Sec. 8, point 1) that optimising the Vinogradov integral argument could lower B by under 0.02, consistent with 4.45 -> 4.43795. Used in all explicit Korobov-Vinogradov zero-free regions and PNT error terms.

### Main results

- **THM-PAPER-0020-1** (Theorem 1.1, theorem, scope: global; Sec. 1 (1.3); proof Sec. 5 (5.1)). For all |t|\ge3 and 1/2\le\sigma\le1: |\zeta(\sigma+it)|\le A|t|^{B(1-\sigma)^{3/2}}\log^{2/3}|t|, and also |\zeta(\sigma+it,u)-u^{-s}|\le A|t|^{B(1-\sigma)^{3/2}}\log^{2/3}|t| for the Hurwitz zeta, 0<u\le1, with A=70.6995, B=4.43795.
- **THM-PAPER-0020-2** (Theorem 1.2, theorem, scope: global; Sec. 1; proof Sec. 6). \zeta(\sigma+it)\ne0 for |t|\ge3 and \sigma\ge1-\dfrac1{54.004(\log|t|)^{2/3}(\log\log|t|)^{1/3}}. *Conditional on:* Yang's Littlewood region for |t|<=exp(463388), MTY argument with P_40, T_0=exp(463388), M_1=0.050007, E=1.8008278, R=468.
- **THM-PAPER-0020-3** (Theorem 1.3, theorem, scope: asymptotic; Sec. 1 (1.5); proof Sec. 7). For sufficiently large |t|, \zeta(\sigma+it)\ne0 for \sigma\ge1-\dfrac1{48.0718(\log|t|)^{2/3}(\log\log|t|)^{1/3}}. *Conditional on:* MTY argument with P_46 and B=4.43795.
- **THM-PAPER-0020-4** (Theorem 1.5, theorem, scope: global; Sec. 1; Lemmas 4.1 (84<=lambda<=220), 4.2 (lambda>=220), N>=e^{288 lambda}). For integer N\ge2, N\le t, \lambda=\log t/\log N: S(N,t):=\max_{0<u\le1}\max_{N<R\le2N}\Big|\sum_{N\le n\le R}(n+u)^{-it}\Big|\le 8.7979\,N^{1-1/(132.94357\,\lambda^2)}.
- **THM-PAPER-0020-5** (Theorem 1.4, theorem, scope: global; Sec. 1; proof Sec. 3). Explicit Vinogradov mean value bound: for k\ge90000 and 0.138128k^2\le s\le k^2\big(0.6494+\tfrac12\log\tfrac{8k}{25D}-\tfrac{1-D/k}{2-D/k}\tfrac Dk+\tfrac{2.051}{k}\big), 1\le D\le0.4k: J_{s,k}(P)\le k^{2.055k^3-0.414k^2+3nk+1.06nk+2(n^2-n)k+0.099912k^2}P^{2s-k(k+1)/2+\Delta_s} (P\ge1) with \Delta_s as in (1.10) (precise exponent as printed in paper).
- **THM-PAPER-0020-6** (Corollary 1.6, corollary, scope: global; Sec. 1). For \chi mod q, q\le N\le qt... (2\le N\le qt): \max_{N<R\le2N}\big|\sum_{N<n\le R}\chi(n)n^{-it}\big|\le 9.7979\,\tfrac{\varphi(q)}{q}Ne^{-\log^3(N/q)/(132.94357\log^2t)}.
- **THM-PAPER-0020-7** (Prime number theorem consequence, corollary, scope: asymptotic; Sec. 1). With c=48.0718 in (1.4): \pi(x)-\mathrm{li}(x)\ll x\exp\{-d(\log x)^{3/5}(\log\log x)^{-1/5}\} with d=0.212579 (via Pintz/Ford).

### Key definitions

- S(N,t)=max_{0<u<=1}max_{N<R<=2N}|sum_{N<=n<=R}(n+u)^{-it}|, lambda=log t/log N
- Vinogradov integral J_{s,k}(P)=\int_{[0,1]^k}|\sum_{x<=P}e(\alpha_1x+...+\alpha_kx^k)|^{2s}d\alpha
- type (d,T) k-tuples of polynomials and K_{s,d}(P,Q;Psi;q)

### Principal lemmas

- **THM-PAPER-0020-L1** (Theorem 2.6 (Tyrina); Sec. 2-3). Vinogradov mean value J_{s,k}(P)<<P^{2s-y(s)} for s<<k^2 with y the inverse of x(y)=-y+2k-(k+1)\log(1-2(y-k)/(k^2-k)); explicit Lambert-W expression y(x) in Sec. 3. — *Role:* Imported; basis of Thm 1.4 (case 1 of Tyrina) for s<<k^2.
- **THM-PAPER-0020-L2** (Lemma 3.1; Sec. 3). For 1\le D\le0.4k, k\ge90000 and 0.138128k\le n\le k(0.6494+\tfrac12\log\tfrac{8k}{25D}-\tfrac{1-D/k}{2-D/k}\tfrac Dk+\tfrac{2.051}k)+1: J_{nk,k}(P)\le C_nP^{2nk-k(k+1)/2+\Delta_n}, with C_n explicit (starts from Delta_{n_0}<=0.4k^2, n_0=ceil(0.1247k)). — *Role:* Recursion for Delta_n starting at n_0 instead of 1 (modification of Ford Lemma 3.6); yields Thm 1.4.
- **THM-PAPER-0020-L3** (Lemma 2.9 (Ford Lemma 5.1); Sec. 2, 4, 8). For integers k,r,s>=2 and h,g with 1<=h<=g<=k, N>0 and M_1,M_2 in [1,N]: S(N,t)<=2M_1M_2+... (bound in terms of J-type mean values, Weyl-differencing), see Sec. 8 Lemma 8.2 for the m-version. — *Role:* Basic estimate of exponential sum S(N,t) via Vinogradov integral.
- **THM-PAPER-0020-L4** (Lemma 4.1; Sec. 4). For 84\le\lambda\le220, N\ge e^{288\lambda}: S(N,t)\le8.7979N^{1-1/(132.94357\lambda^2)}. — *Role:* Critical range lambda>=84 (Ford had critical lambda=87); proven by combining Lemma 2.9 with (4.2),(4.4),(4.6)-(4.8) and Theorem 2.8-type parameter choices.
- **THM-PAPER-0020-L5** (Lemma 4.2; Sec. 4). For \lambda\ge220, N\ge e^{288\lambda}: the same bound S(N,t)<=8.7979N^{1-1/(132.94357 lambda^2)} holds. — *Role:* Large-lambda range using Thm 1.4 (k>=90000) input.
- **THM-PAPER-0020-L6** (Section 5 (proof of Thm 1.1); Sec. 5). |\zeta(\sigma+it)|\le21.3t^{4(1-\sigma)^{3/2}}\le70.6995t^{4.43795(1-\sigma)^{3/2}}\log^{2/3}t (5.1), using (1-\sigma)\le4(1-\sigma)^{3/2} for \sigma\le15/16 (as in Ford Lemma 7.1); remark that with 4.4 one gets sigma<=459/484 but A unaffected. — *Role:* Conversion from S(N,t) bound to A,B constants.
- **THM-PAPER-0020-L7** (Theorem 8.1; Sec. 8). For 1.001\le m\le2, \lambda\ge84: \tilde S(N,t):=\max_u\max_{N<R\le mN}|\sum_{N\le n\le R}(n+u)^{-it}|\le(m-1)\,8.7979N^{1-1/(132.94357\lambda^2)}. — *Role:* Suggested route to reduce A to about 49 if an analogous bound could be proved for lambda<=84.

### Proof architecture

Follows Ford 2002. (i) Improve explicit Vinogradov mean value bounds J_{s,k}: for k>=90000 via Preobrazhenskii's argument with Tyrina's explicit bounds for s<<k^2 and modified recursion starting at n_0 (Thm 1.4/Lemma 3.1); for smaller k use Ford's variant (p.590 of Ford) shifting the critical lambda from 87 to 84. (ii) Combine with Weyl-shift/Lemma 2.9 (Ford Lemma 5.1) and Lemmas 2.1-2.5 (Ford 3.2',3.3',3.4,3.5) to bound S(N,t), Lemmas 4.1/4.2 -> Thm 1.5. (iii) Pass from S(N,t) to zeta via Ford Lemma 7.1-7.3 (Euler-Maclaurin type) giving A=70.6995,B=4.43795 (Sec. 5). (iv) Zero-free regions: plug A,B (and new T_0,M_1,E,R) into MTY22 machinery with P_40 (Thm 1.2, with Yang's Littlewood region for t<=exp(463388)) and P_46 (Thm 1.3).

Dependency edges: CAND-02341 → Ford 2002 (improves A,B of); CAND-02341 → CAND-02337 (plugs improved A,B into the MTY machinery); CAND-02341 → CAND-02339 (uses Yang's Littlewood region for t<=exp(463388)); CAND-02341 → Tyrina / Preobrazhenskii (imports explicit Vinogradov mean value bounds)

**Imported results.** Ford 2002 lemmas (2.1-2.5, 2.7-2.12) incl. Thm 3, Thm 4, Lemma 5.1, 7.1-7.3; Tyrina 1987 Theorem 1: Vinogradov mean value for s<<k^2; Preobrazhenskii 2011 argument for k>=90000; Steiner 2019; Mossinghoff-Trudgian-Yang 2022/24 Lemmas 4.x and trigonometric polynomials P_40,P_46; Yang 2023 explicit Littlewood region (C=21.432 as cited) for t<=exp(463388); Pintz PNT error term

**Techniques.** Vinogradov mean value theorem explicit bounds (Tyrina, Preobrazhenskii, Steiner); Ford's incomplete Diophantine system counting K_{s,d}(P,Q;Psi;q); Weyl-shift exponential sum estimates; careful numerical parameter optimisation; reuse of MTY non-negative trigonometric polynomial machinery

## Context and interpretation

**Importance and obstacle overcome.** Slight but propagating reductions in A,B improve the explicit Korobov-Vinogradov constant from 55.241 to 54.004 and asymptotic constant from 48.1588 to 48.0718. Obstacle: the critical regime lambda~84-87 of the exponential sum bound; overcome by shifting the critical case to lambda=84 with better Vinogradov integral bounds.

**Relation to prior work.** 

**Limitations and open questions.** Author states a substantial further reduction of B is unlikely via parameter choices alone. A could drop to about 49 if a bound of form (m-1)cN^{1-1/(u lambda^2)} were available for lambda<=84 (Sec. 8). Only constants improve; the shape of the region and the exponent 2/3 are unchanged.

## Research potential

- **Hypotheses that might be weakened.** The restriction lambda>=84 (and N>=e^{288 lambda}) in Lemmas 4.1/4.2 is the binding constraint; extending to lambda<84 is the stated route to A~49. Any further improvement of explicit Vinogradov mean value bounds (post Bourgain-Demeter-Guth main conjecture, whose explicit constants are unavailable) would feed B.
- **Generalizations.** Hurwitz zeta bound in Thm 1.1 yields explicit Dirichlet L-function bounds via L(s,chi)=q^{-s}sum chi(m)zeta(s,m/q) (Cor 1.6); Korobov-Vinogradov regions for L-functions (Khale).
- **Candidate connections.** Combine with Yang's explicit k-th derivative test (CAND-02339) and MTY degree-40/46 polynomials; Vinogradov mean value explicit bounds of Steiner.
- **Reusable lemmas.** Theorem 1.5 / Corollary 1.6 (explicit exponential-sum bound for sum chi(n)n^{-it}), Lemma 3.1 (recursion start at n_0), Theorem 8.1.
- **Possible experiments.** Recompute (A,B) from Thm 1.5 by rerunning Ford Lemma 7.1-7.3 conversion with the new (8.7979, 132.94357); explore lambda<84 case numerically via Ford's small-k variant; recompute crossover T_0=exp(463388) between Yang's region and the new one.
- **Risks / barriers.** Heavy dependence on Ford's lemma scaffold; numerical verification of the optimisation is laborious and was not reproduced here. Still a bound far from anything near the critical line.

## Audit notes (Level 1 reader)

Constants attributed to MTY22 and Yang23: Bellotti cites Yang's C_1=21.432 whereas Yang's v2 has 21.233 (version difference, not an error in this paper). Printed exponent of k in Theorem 1.4 (J_{s,k} bound) is garbled in the extraction ('k^{2.055k^3...}') so exact display should be checked in the PDF. Lemma 4.1 requires lambda in [84,220] and N>=e^{288 lambda}; the treatment of the complementary small-N ranges was not examined. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02341`; harvest queries: kw_zero_free, msc_11M06, msc_11M26, arxiv_zero_free.
- Triage decision: include — Explicit zeta bound with new zero-free region.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

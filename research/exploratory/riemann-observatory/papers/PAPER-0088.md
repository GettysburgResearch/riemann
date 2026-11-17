# PAPER-0088 — On the zeros of the Riemann zeta function in the critical strip

| Field | Value |
|---|---|
| Authors | Brent, Richard P. |
| Year / stratum | 1979 / S3 |
| Venue | Math. Comput. 33, 1361-1372 (1979). |
| Identifiers | zbMATH [0422.10031](https://zbmath.org/?q=an:0422.10031) · DOI [10.2307/2006473](https://doi.org/10.2307/2006473) |
| MSC | 11M06, 11-04, 65E05, 30-04 |
| Families | B |
| Work type | computation_report |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://maths-people.anu.edu.au/~brent/pd/rpb047.pdf |
| Selection | score 4.3602, in-pool citations 21, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Rigorous machine verification that the first 75,000,001 zeros of zeta (all zeros with 0<t<32,585,736.4) are simple and on the critical line, via Gram blocks, Rosser's rule, the Riemann-Siegel formula with rigorous rounding/truncation bounds, and Lehman's version of Turing's method. NOTE: the triage line says 81,000,001 zeros, which is wrong for this paper; the abstract and Section 1 give 75,000,000 zeros (H(75,000,001)). Later extensions: Brent-van de Lune-te Riele-Winter 1982 (200,000,001) and van de Lune-te Riele-Winter 1986 (1,500,000,001).

### Main results

- **THM-PAPER-0088-1** (Abstract / Section 1, computational theorem, scope: computational; Abstract, Sec. 1, Sec. 4 end (p. 1365)). The zeta function has exactly $75{,}000{,}000$ zeros $\sigma+it$ with $0<t<32{,}585{,}736.4$; all are simple and lie on $\sigma=1/2$. Equivalently $H(75{,}000{,}001)$ holds, where $H(n)$ = the first $n$ zeros are simple and on the line. Here $N(32{,}585{,}736.4)=75{,}000{,}000$. *Conditional on:* correctness of the Univac 1100/42 program and hardware, and of the error bounds (5.2).
- **THM-PAPER-0088-2** (Theorem 3.1 (Lehman's version of Turing), imported theorem, scope: global; Sec. 3, p. 1364). If $A=0.114$, $B=1.71$, $C=168\pi$ and $C<u<v$, then $\left|\int_u^v S(t)\,dt\right|<A\ln v+B$, where $S(t)=N(t)-1-\theta(t)/\pi$.
- **THM-PAPER-0088-3** (Theorem 3.2, theorem, scope: global; Sec. 3, pp. 1364-1365). If $K$ consecutive Gram blocks with union $[g_n,g_p)$ satisfy Rosser's rule, with $K\ge 0.0061[\ln g_p]^2+0.08\ln g_p$, then $N(g_n)\le n+1$ and $N(g_p)\ge p+1$.
- **THM-PAPER-0088-4** (Sec. 5.2 bounds (5.2), error bound, scope: computational; Sec. 5.2, p. 1367). Computed single-precision $\tilde Z(t)$ satisfies $|\tilde Z-Z|\le 2\cdot10^{-5}+5\cdot10^{-16}\tau\ln\tau+3\tau^{-2}\tau^{1/4}$ (Method A) and $\le(5\cdot10^{-16}\tau\ln\tau+3\tau^{-2})\tau^{1/4}+8\cdot10^{-9}|\tilde Z|$ (Method B), with $\tau=t/2\pi$, for $t>20000\pi$ and $n=2$ in Riemann-Siegel.
- **THM-PAPER-0088-5** (Sec. 4 / Table 3, computational observation, scope: computational; Sec. 3-4, pp. 1364-1365). Rosser's rule fails for infinitely often (Lehman [12]); first failure B_{13,999,525}. In the computation to 75,000,000 the program needed help (case (b)) only 15 times; each time B_j contained k-2 zeros and a neighbouring Gram block had k'+2.
- **THM-PAPER-0088-6** (Sec. 6, Tables 1-4, statistics / conjecture, scope: computational; Sec. 6, p. 1368). Average Gram block length up to n=70,000,000 is 1.1873; conjecture: it tends to a limit $\lambda\le2$. About 74 percent of Gram intervals contain exactly one zero; no block longer than 7 found; only one Gram interval (G_{61,331,768}) with more than three zeros.

### Principal lemmas

- **THM-PAPER-0088-L1** (Lemma 5.1; p. 1366). $\sum_{k\le m}k^{-1/2}\le2m^{1/2}\le2\tau^{1/4}$ and $\sum_{k\le m}k^{-1/2}\ln k\le2m^{1/2}\ln m\le\tau^{1/4}\ln\tau$. — *Role:* elementary sums for the rounding analysis
- **THM-PAPER-0088-L2** (Lemma 5.2; p. 1366). $\theta(t)<\pi\tau\ln\tau$. — *Role:* bound on phase size feeding error amplification
- **THM-PAPER-0088-L3** (Lemma 5.3; p. 1366). If $|L(k)-\ln k|\le\delta_1\ln k$, $|\tilde\theta-\theta|<\delta_2\theta$, $|\tilde c(x)-\cos x|\le\delta_3$ on $[0,2\pi)$, and $\tilde s(t)=\sum_{k\le m}2k^{-1/2}\tilde c[t\cdot L(k)-\tilde\theta(t)]$, then $|\tilde s(t)-s(t)|\le4\pi\tau^{5/4}\ln\tau(\delta_1+\delta_2)+4\tau^{1/4}\delta_3$. — *Role:* master rounding-error bound for the Riemann-Siegel main sum; proof omitted as 'tedious' (following Lehman, Rosser-Yohe-Schoenfeld)
- **THM-PAPER-0088-L4** ((2.8); p. 1363). $|R_2(\tau)|<3\tau^{-7/4}$ for $\tau>2000$ (weakened from the empirically sharper bound 0.006 tau^{-7/4}-type constants), used with n=2 terms of Riemann-Siegel. — *Role:* truncation error bound

### Proof architecture

(i) Riemann-Siegel formula (2.6) with 3 terms gives Z(t) with rigorous remainder (2.8). (ii) Evaluate Z at Gram points and inside Gram blocks until k sign changes are found in each block B_j (Gram-point goodness: (-1)^j Z(g_j)>0); this yields N(g_n)>=n+1 by exhibiting n+1 sign changes, hence n+1 zeros on the line. (iii) Rounding bounds (5.2) from Lemma 5.3 certify the sign of the computed Z (Method A fast, Method B accurate, multiple precision at Gram points when needed). (iv) Upper bound N(g_n)<=n+1 from Theorem 3.2 (Turing/Lehman) by showing a few Gram blocks past n satisfy Rosser's rule (4 blocks in [g_n,g_{n+5}]). Counting plus sign changes shows all zeros are simple and on the line.

**Techniques.** Riemann-Siegel formula with rigorous remainder; Gram points and Gram blocks; Rosser's rule heuristic made rigorous by Turing-Lehman counting; forward rounding error analysis for single/double precision; sign-change detection of Z(t)

## Context and interpretation

**Importance and obstacle overcome.** Pushed rigorous verification of the Riemann hypothesis from 3.5 million zeros (Rosser-Yohe-Schoenfeld 1969) to 75 million, with a program about 3.6 times faster than the CDC 3600 one, and gave the first large statistical tables of Gram block structure. Obstacle: certifying signs of Z(t) under floating-point rounding; solved by explicit forward error bounds and the cheap-then-expensive Method A/B strategy.

**Relation to prior work.** 

**Limitations and open questions.** Finite verification only (t<32,585,736.4); says nothing about RH globally. Rigor depends on unverified hardware/program correctness and on omitted 'tedious' rounding proofs (proof of Lemma 5.3 omitted). Author errata: replace H(10) by H(15) on p.1361; B_{2k} should be |B_{2k}| in (2.3); the bound on |r_n(t)| two lines after (2.3) is incorrect (corrected in arXiv:1609.03682), without effect on the zero computation. Remark: Rosser-rule failures grow, so the method requires ever more extra work at larger height.

## Research potential

- **Hypotheses that might be weakened.** None to weaken; but the t>20000 pi and n=2 restrictions in (5.2) and the 168 pi threshold in Theorem 3.1 are the load-bearing numerical conditions for any re-implementation.
- **Generalizations.** Same Gram/Turing architecture is used for Dirichlet L-functions and for the zeros of zeta near the line at larger heights; Odlyzko-Schonhage replaced the per-point Riemann-Siegel sum with fast multi-evaluation.
- **Candidate connections.** Proof-producing computation (AGENTS.md): a re-verification with interval arithmetic (Platt 2011, Platt-Trudgian) is the modern directed-rounding analogue; this paper's (5.2) is a hand-derived analytic bound, not an interval-arithmetic certificate.
- **Reusable lemmas.** Theorem 3.2 (explicit Turing criterion) and Lemma 5.3 as a template for rounding bounds.
- **Possible experiments.** Reproduce H(n) for n up to 1e6-1e7 with mpmath/interval arithmetic; count Gram blocks and compare to Table 1 (J(1,n) at n=1e6 should equal 756,... per Table 1 values) as a regression test; test conjecture of average Gram block length limit.
- **Risks / barriers.** Only a finite ladder; no inference to infinitely many zeros or to global RH is available from it (see AGENTS.md boundary).

## Audit notes (Level 1 reader)

Triage summary states 81,000,001 zeros, but the paper proves 75,000,001 (75,000,000 zeros with t<32,585,736.4); the 81,000,000 figure appears only in later papers' error-analysis ranges. Proof of Lemma 5.3 omitted in text. Errata at author's page: H(10)->H(15) p.1361; B_{2k}->|B_{2k}| (2.3); bound on |r_n(t)| incorrect (corrected arXiv:1609.03682), not affecting computation. Pages 1369-1372 not read.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00340`; harvest queries: kw_RH_any, kw_zeta_zeros, msc_11M06.
- Triage decision: include — Brent's verification of RH for first 81 million zeros.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

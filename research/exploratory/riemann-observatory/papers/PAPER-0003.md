# PAPER-0003 — Bounding \(S(t)\) and \(S_1(t)\) on the Riemann hypothesis

| Field | Value |
|---|---|
| Authors | Carneiro, Emanuel; Chandee, Vorrapan; Milinovich, Micah B. |
| Year / stratum | 2013 / S5 |
| Venue | Math. Ann. 356, No. 3, 939-968 (2013). |
| Identifiers | zbMATH [1325.11084](https://zbmath.org/?q=an:1325.11084) · DOI [10.1007/s00208-012-0876-z](https://doi.org/10.1007/s00208-012-0876-z) · arXiv [1309.1526](https://arxiv.org/abs/1309.1526) |
| MSC | 11M06, 11M26, 11M36, 41A30 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1309.1526 |
| Selection | score 4.8702, in-pool citations 36, seed lists 3, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Assuming RH, improve the explicit constant C in Littlewood's bound |S(t)| <= (C+o(1)) log t/log log t, where pi S(t)=arg zeta(1/2+it). Goldston-Gonek had C=1/2. The paper also bounds the antiderivative S_1(t)=int_0^t S(u)du.

**Historical motivation.** Littlewood (1924) proved S(t)=O(log t/loglog t) under RH. Only the constant has improved (Ramachandra-Sankaranarayanan 1.119, Fujii 0.67, Goldston-Gonek 1/2). Extremal functions of exponential type had worked for bounding |zeta(1/2+it)| (Chandee-Soundararajan), and this paper applies them to S(t) and S_1(t).

### Main results

- **THM-PAPER-0003-1** (Theorem 1, theorem, scope: asymptotic; Sec 1 p.2; proof in Sec 3). Assume RH. For t sufficiently large, $-\left(\frac{\pi}{24}+o(1)\right)\frac{\log t}{(\log\log t)^2}\le S_1(t)\le\left(\frac{\pi}{48}+o(1)\right)\frac{\log t}{(\log\log t)^2}$, with the $o(1)$ terms $O(\log\log\log t/\log\log t)$. *Conditional on:* Riemann Hypothesis.
- **THM-PAPER-0003-2** (Theorem 2, theorem, scope: asymptotic; Sec 1 p.2; proved in Sec 4 (from Thm 1 via Lemma 7) and again in Sec 5 (directly, via extremal functions for an odd function)). Assume RH. For t sufficiently large, $|S(t)|\le \frac14\frac{\log t}{\log\log t}+O\left(\frac{\log t\,\log\log\log t}{(\log\log t)^2}\right)$. *Conditional on:* Riemann Hypothesis.

### Key definitions

- S(t)=(1/pi) arg zeta(1/2+it) by continuous variation along 2, 2+it, 1/2+it, with the average convention at ordinates
- S_1(t)=int_0^t S(u)du
- f_1(x)=1-x arctan(1/x)
- F(x)=arctan(1/x)-x/(1+x^2)
- Extremal majorant: real entire function of exponential type 2 pi Delta, >= f, minimizing the L^1 distance

### Principal lemmas

- **THM-PAPER-0003-L1** (Lemma 3 (eq. 5); Sec 2). Assume RH, $f_1(x)=1-x\arctan(1/x)$. For $t\ge2$: $S_1(t)=\frac{1}{4\pi}\log t-\frac1\pi\sum_\gamma f_1(t-\gamma)+O(1)$, sum over ordinates of nontrivial zeros $\rho=1/2+i\gamma$. — *Role:* Turns S_1 into a sum over zeros of a fixed test function, so extremal majorants/minorants can be applied. Proof uses S_1(t)=(1/pi) int_{1/2}^{3/2} log zeta(sigma+it) d sigma + O(1) (Titchmarsh Thm 9.9) and Hadamard factorization of xi.
- **THM-PAPER-0003-L2** (Lemma 4 (eq. 8); Sec 2, before Lemma 5). Assume RH, $F(x)=\arctan(1/x)-x/(1+x^2)$. Then $S(t)=\frac1\pi\sum_\gamma F(t-\gamma)+O(1)$ for t not an ordinate; F=-f_1'. — *Role:* Same representation for S(t); used for the direct proof in Sec 5.
- **THM-PAPER-0003-L3** (Lemma 5; Sec 2). Guinand-Weil explicit formula under RH for h analytic in $|\Im s|\le 1/2+\epsilon$ with $|h(s)|\ll(1+|s|)^{-(1+\delta)}$, h real on the real line: $\sum_\rho h(\gamma)=h(1/(2i))+h(-1/(2i))-\frac1{2\pi}\hat h(0)\log\pi+\frac1{2\pi}\int h(u)\Re\frac{\Gamma'}{\Gamma}(\frac14+\frac{iu}2)du-\frac1{2\pi}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}(\hat h(\frac{\log n}{2\pi})+\hat h(-\frac{\log n}{2\pi}))$. — *Role:* Imported tool (Iwaniec-Kowalski Thm 5.12); converts zero sums into prime sums and a gamma integral.
- **THM-PAPER-0003-L4** (Lemma 6; Sec 3; proof Sec 6). For $f_1$ and $\Delta\ge1$ there are unique real entire $g^\pm_\Delta$ of exponential type $2\pi\Delta$ with $g^-_\Delta\le f_1\le g^+_\Delta$, $|g^\pm_\Delta(z)|\ll \Delta^2 e^{2\pi\Delta|y|}/(1+\Delta|z|)$, $\hat g^\pm_\Delta$ continuous, supported in $[-\Delta,\Delta]$, $\ll1$, and exact L^1 distances $\int(f_1-g^-_\Delta)=\int_{1/2}^{3/2}\frac1\Delta\{\log(1+e^{-2\pi\Delta(\sigma-1/2)})-\log(1+e^{-2\pi\Delta})\}d\sigma$, and similarly for g^+ with log(1-e^{...}). — *Role:* Extremal majorant/minorant; supplies the sharp constant pi/48 and pi/24 (via integral of f_1 = pi/2 and the L^1 gap). Proved in Sec 6 by Gaussian subordination (Carneiro-Littmann-Vaaler).
- **THM-PAPER-0003-L5** (Lemma 7; Sec 4). For $t\ge2$, $0<h\le\sqrt t$: $-\frac{h\log t}{4\pi}+\frac1h\int_{t-h}^{t}S(u)du+\vartheta^-_{h,t}\le S(t)\le\frac{h\log t}{4\pi}+\frac1h\int_t^{t+h}S(u)du+\vartheta^+_{h,t}$, with $\vartheta^\pm=O(h)+O(1/t)$. — *Role:* Unconditional comparison between S(t) and averages of S, from monotonicity of N(t); with Theorem 1 and h ~ 1/loglog t gives Theorem 2.
- **THM-PAPER-0003-L6** (Lemma 8; Sec 5; proof Sec 6). For $f(x)=\arctan(1/x)-x/(1+x^2)$ and $\Delta\ge1$ there are unique real entire extremal majorant and minorant $m^\pm_\Delta$ of exponential type $2\pi\Delta$ with Fourier transform supported in $[-\Delta,\Delta]$ and analogous size bounds. — *Role:* Odd-function extremal problem solved via Carneiro-Littmann truncated Gaussian subordination; gives direct proof of Theorem 2.

### Proof architecture

Under RH, write S_1(t) and S(t) as (1/4pi)log t minus (1/pi)sum over zeros of f_1(t-gamma) resp. of F(t-gamma) (Lemmas 3, 4). Replace f_1 or F by optimal extremal majorant/minorant of exponential type 2 pi Delta (Lemmas 6, 8), apply the Guinand-Weil formula (Lemma 5). The prime sum is bounded trivially by e^{pi Delta} using PNT and partial summation. The gamma integral gives (log t)/(Delta) times the L^1 gap. Choosing pi Delta ~ log log t - 2 log log log t gives the stated bounds. Route A: Theorem 1, then Lemma 7 with h ~ 1/loglog t gives Theorem 2. Route B: direct extremal bound for F gives Theorem 2.

Dependency edges: CAND-01181 → Goldston-Gonek 2007 (S(t) bound with constant 1/2) (improves); CAND-01181 → Chandee-Soundararajan (|zeta(1/2+it)| under RH) (same method as); CAND-01181 → CAND-01264 (is simplified and generalized by)

**Imported results.** Guinand-Weil explicit formula (Iwaniec-Kowalski Thm 5.12); Titchmarsh Thm 9.9 (S_1 as integral of log zeta); Carneiro-Littmann-Vaaler Gaussian subordination for even functions; Carneiro-Littmann extremal functions for truncated/odd Gaussians; PNT and Stirling

**Techniques.** Beurling-Selberg extremal majorants/minorants; Gaussian subordination framework (Carneiro-Littmann-Vaaler; Carneiro-Littmann for odd truncated functions); Guinand-Weil explicit formula; Hadamard factorization of xi; Stirling for Gamma'/Gamma; trivial bound of prime sums via PNT; local comparison S(t) vs S_1(t+/-h)-S_1(t) from monotonicity of N

## Context and interpretation

**Importance and obstacle overcome.** Shows the Goldston-Gonek constant was not the limit of the method. The idea is that the Goldston-Gonek increment bound loses a factor of 2, so one should bound S itself, or its integral, with a matched extremal problem. The obstacle was solving the extremal problem for the non-even, non-integrable-in-the-usual-sense function F, which needed new truncated-Gaussian subordination.

**Relation to prior work.** Improves Goldston-Gonek (1/2 to 1/4). For S_1, improves Karatsuba-Korolev (1/40) and Fujii (-0.51 <= . <= 0.32 times log t/(loglog t)^2) to -pi/24 <= . <= pi/48. Claims Theorem 2 only recovers, but does not improve, Goldston-Gonek's |S(t+h)-S(t)| bound (4), so corollaries on zero multiplicity and gaps are recovered but not improved.

**Limitations and open questions.** Conditional on RH. Asymptotic with no explicit t0 and no explicit constants in the error. Prime sums are estimated trivially, and the authors say a significant breakthrough in prime-sum estimates would be needed to approach the Farmer-Gonek-Hughes heuristic S(t)=O(sqrt(log t loglog t)). The order of magnitude log t/loglog t is untouched.

**Ideas in remarks/appendices/abandoned paths.** Footnote 1 on p.9 (Radziwill version of Lemma 7). Remark in Sec 1 that the S(t) bound matches the S_1(t+/-h)-S_1(t) route since S_1'=S a.e. Appendix A (not read in detail).

## Research potential

- **Hypotheses that might be weakened.** RH is used only through zeros being 1/2+i gamma in the explicit formula and in Lemmas 3 and 4. A zero-density or partial-RH substitute would give a bound with an additive term from off-line zeros, but this is not in the paper.
- **Generalizations.** Done for L-functions in CAND-01264. Other test functions (S_n(t), higher iterated integrals) fit the same Gaussian-subordination method. Making t-dependence explicit gives usable explicit bounds.
- **Candidate connections.** A better prime-sum estimate in the explicit formula (beyond trivial) is the stated barrier. Combination with zero-density or pair-correlation input on gaps is a possible link.
- **Reusable lemmas.** Lemma 6 and Lemma 8 (extremal majorants and minorants with exact L^1 gaps) and Lemma 7 (S(t) vs average of S) are reusable. Lemma 7 compares S(t) with averages of S.
- **Possible experiments.** Numerically evaluate sum_gamma f_1(t-gamma) and F(t-gamma) against the extremal functions g^+/-_Delta and m^+/-_Delta using tabulated zeros, to measure how large t must be before the bound is informative.
- **Risks / barriers.** The trivial treatment of the prime sum caps the method at 1/4; improvement would need genuine cancellation in prime sums, which is unavailable without strong input.

## Audit notes (Level 1 reader)

none noticed in inspected portion. The pdf text extraction drops some symbols (e.g. constants in Theorem 1 were read from the abstract and the visible statement). The Radziwill footnote says a version of Lemma 7 with constants +/-1/(2pi) was independently obtained, consistent with the 1/(4pi) used here only after optimal use of h.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01181`; harvest queries: kw_RH_any, msc_11M06, msc_11M26, msc_11M36, arxiv_rh_abs, arxiv_rh_ti.
- Triage decision: include — Improves conditional constants for S(t) and S_1(t).
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

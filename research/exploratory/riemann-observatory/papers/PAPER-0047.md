# PAPER-0047 — On the zeros of the Riemann zeta-function in the critical strip. IV

| Field | Value |
|---|---|
| Authors | van de Lune, J.; te Riele, H. J. J.; Winter, D. T. |
| Year / stratum | 1986 / S4 |
| Venue | Math. Comput. 46, 667-681 (1986). |
| Identifiers | zbMATH [0585.10023](https://zbmath.org/?q=an:0585.10023) · DOI [10.2307/2008005](https://doi.org/10.2307/2008005) |
| MSC | 11M06, 11-04, 11Y35 |
| Families | B |
| Work type | computation_report |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://ir.cwi.nl/pub/1808/1808D.pdf |
| Selection | score 4.5622, in-pool citations 39, seed lists 3, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Extend the rigorous Gram-block/Rosser-rule verification of RH to the first 1,500,000,001 zeros (0<t<545,439,823.215), re-check earlier ranges, and tabulate exact Gram block and Rosser-exception statistics.

### Main results

- **THM-PAPER-0047-1** (Abstract / Sec. 1, computational theorem, scope: computational; Abstract, Sec. 1, p. 667-668). The first $1{,}500{,}000{,}001$ zeros $\sigma+it$ with $0<t<545{,}439{,}823.215$ all have $\sigma=1/2$ and are simple (RH verified in this rectangle). *Conditional on:* correctness of FORTRAN/COMPASS programs on CDC Cyber 175/750 and Cyber 205, and of the extended error analysis.
- **THM-PAPER-0047-2** (Sec. 2 error bounds, error bound, scope: computational; Sec. 2, p. 668-669). For $t=2\pi\tau$ in $(3.5\times10^7,5.6\times10^8)$ (zero #81,000,000 to #1,500,000,000): $|\tilde Z(t)-Z(t)|<3\times10^{-7}\tau^{-1/4}$ (method A) and $<5.5\times10^{-3}\tau^{-5/4}$ (method B); safe constant bounds $3\times10^{-5}$, $2.1\times10^{-11}$; the program used $10^{-4}$ and $2.5\times10^{-7}$. (Exponents as extracted from OCR; sign/exponent forms unverified.) Not a single Gram point failed method B.
- **THM-PAPER-0047-3** (Sec. 1 completion, computational, scope: computational; p. 667). Using Theorem 3.2 of Brent [1], five Gram blocks of lengths 1,1,2,1,1 in $[g_{1,500,000,000},g_{1,500,000,006})$ all satisfy Rosser's rule, giving $N(g_{1.5\cdot10^9})$ upper bound and so $H(1{,}500{,}000{,}001)$.
- **THM-PAPER-0047-4** (Tables 1-2, statistics, scope: computational; Sec. 3, pp. 669-672). Exact counts on $[g_0,g_{1.5\cdot10^9})$: average Gram block length 1.2089; 1,036,704,539 blocks of length 1; 3055 exceptions to Rosser's rule (2973 of length 2, 82 of length 3), the missing two zeros always in an adjacent Gram block.
- **THM-PAPER-0047-5** (Table 5, statistics, scope: computational; p. 672). Gram intervals with exactly m zeros, m=0..4, over $[g_0,g_{1.5\cdot10^9})$: 206,769,423 / 1,089,161,153 / 201,369,458 / 2,699,933 / 33 (13.78 / 72.61 / 13.42 / 0.18 percent).
- **THM-PAPER-0047-6** (Sec. 3 end, observation, scope: computational; pp. 673-674). Closest pair of zeros observed lies in $B_{1,048,449,112}$ with $(t_{n+1}-t_n)\log t_n/2\pi=0.00034$; first Gram block of length 9 is $B_{542,964,969}$; maxima of |S| near exceptions are about 2.0-2.2.

### Proof architecture

Same architecture as Brent 1979: Riemann-Siegel evaluation of Z(t) with rigorous error bounds, separation of the zeros inside Gram blocks (programs CYBER 175/750; vectorised on CYBER 205), closure by Brent's Theorem 3.2 (Turing-Lehman). Imported: Brent [1] Thm 3.2, error analysis of van de Lune et al. [6] (extended here to t<5.6e8). Earlier ranges re-run: [g_156.8M,g_200M) re-verified exactly; [g_1000,g_5M) and [g_200M,g_210M) rechecked with exact agreement with [1],[7].

**Techniques.** Riemann-Siegel formula; Gram blocks, Rosser's rule, Turing-Lehman method; vectorised summation of the main sum (Q8-calls on CYBER 205); exact statistical tabulation of Rosser exceptions

## Context and interpretation

**Importance and obstacle overcome.** Roughly a 7.5-fold extension over 200 million zeros in 1982 and the standard reference in the 1980s for verified RH height; the vectorised Cyber 205 program overcame the cost growth (about 900 plus 1000 CPU hours).

**Relation to prior work.** 

**Limitations and open questions.** Finite verification; no theoretical consequence for infinite RH. Error analysis 'omitted as tedious' (refers to [6]). Authors flag a possible unrecoverable configuration (zero pattern '0 0 1 3') in which the afterwards adjacent-block search would fail and ask where it first occurs. Hardware-dependent truncated arithmetic enters the proof.

## Research potential

- **Hypotheses that might be weakened.** None; computational. Rigor audit target: the extended error analysis (Sec. 2) which is only sketched in this paper (details in [6]).
- **Generalizations.** Later: Odlyzko-Schonhage fast algorithm, ZetaGrid (1e13 zeros), Platt interval-arithmetic verification (arXiv 2011, to 3e10). Comparison basis for Gram-block statistics versus random-matrix predictions.
- **Candidate connections.** Table 5 and exception statistics provide data for testing GUE/ Keating-Snaith predictions about S(t) tails (max |S| near exceptions about 2.2).
- **Reusable lemmas.** Not applicable (no new lemmas).
- **Possible experiments.** Verify Table 5 proportions against GUE predictions for number-variance; check the growth of exceptions to Rosser's rule vs. conjectured S(t) distribution.
- **Risks / barriers.** Finite ladder; cannot be used as evidence of global RH (AGENTS.md boundary). Not an interval-arithmetic or machine-checked certificate.

## Audit notes (Level 1 reader)

pdftotext output of Tables 1-3 is garbled so table numbers should be rechecked against the print. The error exponents in Sec. 2 (tau^{-1/4}, tau^{-5/4}) are OCR-sensitive. Triage line is accurate (1,500,000,001 zeros). Pages 674-681 not read, including corrigenda for earlier papers.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00739`; harvest queries: kw_RH_any, kw_zeta_zeros, msc_11M06, msc_11Y35.
- Triage decision: include — Verification of RH for first 1.5e9 zeros.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

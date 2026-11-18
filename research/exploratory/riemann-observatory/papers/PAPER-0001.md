# PAPER-0001 — The Riemann hypothesis is true up to \(3 \cdot 10^{12}\)

| Field | Value |
|---|---|
| Authors | Platt, Dave; Trudgian, Tim |
| Year / stratum | 2021 / S6 |
| Venue | Bull. Lond. Math. Soc. 53, No. 3, 792-797 (2021). |
| Identifiers | zbMATH [1482.11111](https://zbmath.org/?q=an:1482.11111) · DOI [10.1112/blms.12460](https://doi.org/10.1112/blms.12460) · arXiv [2004.09765](https://arxiv.org/abs/2004.09765) |
| MSC | 11M06, 11M26 |
| Families | B |
| Work type | computation_report |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/2004.09765 |
| Selection | score 4.8995, in-pool citations 50, seed lists 5, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Rigorously verify, with interval/ball arithmetic and a Turing-method completeness check, that all non-trivial zeros of zeta with 0<gamma<=H lie on Re s=1/2, and push H to 3 000 175 332 800; then record immediate corollaries (explicit prime estimates, de Bruijn-Newman upper bound).

**Historical motivation.** Earlier large verifications (Gourdon 2004, H=2.44e12; Wedeniwski ZetaGrid; Franke et al. H=1e11) used unpublished, non-interval floating arithmetic and did not document rounding/truncation control (concern noted by Tao and Helfgott). Platt (2017) gave a rigorous H=3.06e10. This paper gives the first rigorous verification exceeding Gourdon's height.

### Main results

- **THM-PAPER-0001-1** (Theorem 1, theorem (finite computation, rigorous), scope: finite; Section 1, p.2; method Section 2). The Riemann hypothesis holds up to height $H=3\,000\,175\,332\,800$: the lowest $12\,363\,153\,437\,138$ non-trivial zeros $\rho$ have $\Re\rho=1/2$ (equivalently every non-trivial zero with $0<\gamma\le H$ lies on the critical line and, in the counted range, all expected zeros are accounted for).
- **THM-PAPER-0001-2** (Corollary 1, corollary (conditional on Buthe's theorem + Theorem 1), scope: finite; Section 3.1, p.4). With Schoenfeld's RH bound $|\psi(x)-x|\le\frac{\sqrt x}{8\pi}\log^2x$ valid for $x>59$ whenever RH holds up to $H\ge4.92\sqrt{x/\log x}$ (Buthe), one has unconditionally: $|\psi(x)-x|\le\frac{\sqrt x}{8\pi}\log^2x$ for $59<x\le2.169\cdot10^{25}$; $|\theta(x)-x|\le\frac{\sqrt x}{8\pi}\log^2x$ for $599<x\le2.169\cdot10^{25}$; $|\pi(x)-\operatorname{li}(x)|\le\frac{\sqrt x}{8\pi}\log^2x$ for $2657<x\le2.169\cdot10^{25}$.
- **THM-PAPER-0001-3** (Corollary 2, corollary (conditional on Polymath15 Table 1 + Theorem 1), scope: global; Section 3.4, p.5). The de Bruijn-Newman constant satisfies $\Lambda\le0.2$ (improving 0.22; Polymath15 Table 1 row 2 requires $H>2.51\cdot10^{12}$, with their X corresponding to 2H). Combined with Rodgers-Tao $\Lambda\ge0$ this gives $0\le\Lambda\le0.2$. RH is equivalent to $\Lambda\le0$.

### Key definitions

- H: largest known height with all zeros 0<gamma<=H on Re s=1/2
- N(sigma,T) zero-counting function (mentioned)
- de Bruijn-Newman constant Lambda, $H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)du$, $\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})\exp(-\pi n^2e^{4u})$

### Principal lemmas

- **THM-PAPER-0001-L1** (Algorithm of Section 2 (no numbered lemmas); Section 2, p.2). Evaluate the completed zeta function (Hardy Z-type real-valued function) on the critical half-line on a lattice with sampling rate ~0.01 (about 25 samples per zero on average); each sign change certifies a zero on Re s=1/2; Turing's method (Trudgian's improvements I, II) shows the count of sign-change zeros equals N(H), hence no zeros off the line. — *Role:* Core verification argument: rigorous counting + Turing completeness.
- **THM-PAPER-0001-L2** (Implementation change; Section 2, p.2-3). Code rewritten from MPFI to Arb (midpoint-radius ball arithmetic, ~50% space saving); no attempt to isolate zeros beyond what is needed (the default sampling isolates 999 997.5 of every 10^6 zeros). — *Role:* Performance; keeps rigor via ball arithmetic.
- **THM-PAPER-0001-L3** (Computational budget; Section 2, p.3). About 7.5 million core-hours on 3.6GHz Xeons; ~110 000 units of height per GHz-hour (vs 80 000 000 for Gourdon's non-rigorous double-precision FFT and 3 800 for Wedeniwski). — *Role:* Documents cost and comparison with unpublished/non-rigorous earlier verifications (Gourdon H=2.44e12, Wedeniwski ZetaGrid ~2.41e11 claim).

### Proof architecture

Not a mathematical proof but a computer-assisted verification: (a) Platt's 2017 algorithm (Math. Comp. 86) computes Z(t) (completed zeta on the half line) via FFT-based Riemann-Siegel/Shannon-Whittaker sampling with rigorously bounded truncation errors, in interval/ball arithmetic; (b) sign changes count zeros on the line; (c) a Turing-method argument (Trudgian) shows the number of zeros up to H equals the number found, excluding off-line zeros. The paper itself contains no new analysis, only code port (MPFI->Arb), parameter tuning and the large-scale run, plus corollaries via black-box theorems (Buthe, Polymath15).

**Imported results.** Platt, Isolating some non-trivial zeros of zeta, Math. Comp. 86 (2017) 2449-2467 (algorithm, rigorous bounds); Trudgian, Improvements to Turing's method I, II (completeness argument); Buthe 2016, Estimating pi(x) and related functions under partial RH assumptions (Corollary 1); Schoenfeld 1976 explicit RH bounds; Polymath15 (2019) heat-flow upper bound, Table 1 (Corollary 2); Rodgers-Tao Lambda>=0

**Techniques.** interval/ball arithmetic (Arb); FFT-based evaluation with Shannon-Whittaker-Nyquist interpolation; rigorous truncation bounds for Riemann-Siegel / Gamma factor; Turing's method (Trudgian variant); high-performance computing

## Context and interpretation

**Importance and obstacle overcome.** Gives a rigorous, peer-reviewed H that is larger than all prior claims (22% above Gourdon) and feeds many explicit results (zero-free regions, zero-density, prime-counting error terms, sign changes of pi(x)-li(x), de Bruijn-Newman bound). The obstacle was cost: ball arithmetic and a higher sampling rate (25 per zero vs 1.2) made the run ~725 times slower than Gourdon's.

**Relation to prior work.** Direct extension of Platt 2017 using the same algorithm, with Arb replacing MPFI; independently confirms Gourdon/Wedeniwski/Franke et al. to this height. Supersedes H=3.06e10 of Platt as the rigorous record at the time (later superseded by nothing cited here).

**Limitations and open questions.** Finite verification only; says nothing about RH globally (explicit zero-free/de Bruijn-Newman constants improve only mildly because explicit estimates are already near the RH-conditional ones). Zeros are not isolated or stored (no database produced). Not a published artifact set: the paper does not state hashes, code repository or output logs, so independent replay depends on code and data outside this note. Corollary 2 is only a 'mild' improvement; getting Lambda<0.19 would need H slightly above 10^13.

**Ideas in remarks/appendices/abandoned paths.** Footnote 2 in Section 3.4: Polymath15's X corresponds to 2H, so the next table entry (Lambda<0.19) needs H slightly above 1e13. Section 2 records the cost model (GHz-hours per unit height), a useful benchmark for planning any further rigorous verification.

## Research potential

- **Hypotheses that might be weakened.** The conditional corollaries rely on the single parameter H; any statement of the form 'RH up to H implies explicit bound B(H)' (Buthe-type, Polymath15 Table 1, Kadiri-Lumley zero-density) can be re-run with H=3.0001753328e12 as an extremely cheap improvement.
- **Generalizations.** Same algorithm for Dirichlet L-functions / Dedekind zeta in rigorous interval arithmetic; extend to 'zeros isolated and stored' databases; compute with ball arithmetic the Turing-method completeness for degree-2 L-functions.
- **Candidate connections.** Feeds the de Bruijn-Newman program (Polymath15; Rodgers-Tao Lambda>=0): improving H to >1e13 lowers the upper bound Lambda; connects to explicit prime-number-theorem error terms (Platt-Trudgian 2021 Math. Comp.), to Robin/Lagarias-type explicit RH-equivalent inequalities that need RH to height H to settle finite ranges, and to Kadiri/Simonic zero-density explicit estimates.
- **Reusable lemmas.** Büthe's criterion 'RH to height H gives Schoenfeld's bound for 4.92 sqrt(x/log x)<=H' is reusable verbatim; Polymath15's Table 1 maps (H,X) to Lambda upper bounds.
- **Possible experiments.** Re-verify a short window near height 3e12 with an independent Arb or python-flint implementation (zero count by Turing's method versus N(T) from Riemann-von Mangoldt with explicit Backlund-type bounds) to test the 'produce checker artifacts' standard of the archive; compute the new explicit Büthe range (x<=2.169e25) check against ψ(x) data.
- **Risks / barriers.** Runtime scales roughly linearly with H in the verification (cost ~H log H); another factor 10 in H costs ~10x more with ball arithmetic. The result is a finite computation: it cannot be turned into global evidence, and it cannot decide RH-equivalent global functionals without a locality theorem.

## Audit notes (Level 1 reader)

Minor presentational issues, none affecting mathematics: Theorem 1 gives the count 12 363 153 437 138 but the paper does not state the corresponding explicit Turing bound or error margins; footnote 1 discusses ambiguity in reported heights for Wedeniwski (5.72e10 vs 1.07e11 vs 1.53e11 vs 2.41e11). Text typo in Section 3.1: 'is confirmed by and can be improved improved slightly'. No code, hash or artifact is cited, so the claim is not independently checkable from the paper alone.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01775`; harvest queries: kw_RH_any, kw_debruijn_newman, msc_11M06, msc_11M26, arxiv_rh_abs, arxiv_rh_ti, arxiv_verification_zeros.
- Triage decision: include — Current record rigorous verification of RH to 3e12.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
